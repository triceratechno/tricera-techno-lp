#!/usr/bin/env python3
"""
CRM同期スクリプト

customers/*.md の YAML frontmatter を単一の真実として、
- DASHBOARD.md の顧客サマリー表
- SCHEDULE.md の今日／今週タスク
- index.html の customers JS 配列

をすべて自動更新する。

使い方:
    python crm/scripts/sync.py

依存: 標準ライブラリのみ（PyYAMLなし）

各出力ファイルには以下のマーカーで自動生成領域を囲んである:
    <!-- BEGIN: AUTO-CUSTOMER-TABLE -->
    ...
    <!-- END: AUTO-CUSTOMER-TABLE -->
"""
import os
import re
import sys
from datetime import date, datetime
from pathlib import Path

ROOT = Path(__file__).parent.parent  # crm/
CUSTOMERS_DIR = ROOT / "customers"
DASHBOARD_PATH = ROOT / "DASHBOARD.md"
SCHEDULE_PATH = ROOT / "SCHEDULE.md"
INDEX_PATH = ROOT / "index.html"


def parse_frontmatter(text: str) -> tuple[dict, str]:
    """シンプルなYAMLフロントマターパーサ（標準ライブラリのみ）"""
    if not text.startswith("---"):
        return {}, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, text
    fm_text = parts[1].strip()
    body = parts[2].lstrip("\n")
    data = {}
    current_key = None
    current_list = None
    for raw_line in fm_text.split("\n"):
        line = raw_line.rstrip()
        if not line.strip():
            continue
        # リスト要素
        if line.lstrip().startswith("- ") and current_list is not None:
            current_list.append(line.lstrip()[2:].strip())
            continue
        # キー: 値 または キー:
        m = re.match(r"^([\w\-]+)\s*:\s*(.*)$", line)
        if m:
            key, val = m.group(1), m.group(2).strip()
            if val == "":
                # 次の行からリストが続く可能性
                current_list = []
                data[key] = current_list
                current_key = key
            else:
                # 引用符を剥がす
                if (val.startswith('"') and val.endswith('"')) or (
                    val.startswith("'") and val.endswith("'")
                ):
                    val = val[1:-1]
                data[key] = val
                current_list = None
                current_key = key
    return data, body


def load_customers() -> list[dict]:
    customers = []
    for path in sorted(CUSTOMERS_DIR.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        fm, body = parse_frontmatter(text)
        fm["_file"] = path.name
        fm["_id"] = fm.get("id", path.stem)
        customers.append(fm)
    return customers


def status_emoji(status: str) -> str:
    if "制作" in status or "成約" in status:
        return "🟢"
    if "FB待ち" in status or "応答待ち" in status:
        return "🟡"
    if "無料" in status or "相談" in status:
        return "🔵"
    if "完了" in status:
        return "⚫"
    return "⚪"


def priority_emoji(priority: str) -> str:
    return {"P0": "🔴", "P2": "🟡", "P3": "⚪"}.get(priority, "⚪")


def render_dashboard_table(customers: list[dict]) -> str:
    lines = [
        "| 顧客 | プラン | ステータス | 次のアクション | 期限 | 優先度 |",
        "|---|---|---|---|---|---|",
    ]
    for c in customers:
        name = c.get("display_name", c["_id"])
        if c.get("real_name"):
            name = f"{name}（{c['real_name']}）"
        elif c.get("nickname"):
            name = f"{name}（{c['nickname']}）"
        plan = c.get("plan", "—")
        if c.get("plan_price"):
            plan = f"{plan} ¥{c['plan_price']}"
        status = f"{status_emoji(c.get('status', ''))} {c.get('status', '—')}"
        next_action = c.get("next_action", "—")
        next_due = c.get("next_action_due", "—")
        priority = f"{priority_emoji(c.get('priority', ''))} {c.get('priority', '—')}"
        link = f"[{name}](customers/{c['_file']})"
        lines.append(
            f"| {link} | {plan} | {status} | {next_action} | {next_due} | {priority} |"
        )
    return "\n".join(lines)


def render_schedule_p0(customers: list[dict]) -> str:
    p0 = [c for c in customers if c.get("priority") == "P0"]
    if not p0:
        return "_（現在P0タスクなし）_"
    lines = []
    for c in p0:
        name = c.get("display_name", c["_id"])
        action = c.get("next_action", "")
        due = c.get("next_action_due", "")
        lines.append(f"- [ ] **{name}** — {action}（期限：{due}）")
    return "\n".join(lines)


def render_schedule_p2(customers: list[dict]) -> str:
    p2 = [c for c in customers if c.get("priority") == "P2"]
    if not p2:
        return "_（現在P2タスクなし）_"
    lines = []
    for c in p2:
        name = c.get("display_name", c["_id"])
        action = c.get("next_action", "")
        due = c.get("next_action_due", "")
        lines.append(f"- [ ] **{name}** — {action}（{due}）")
    return "\n".join(lines)


def replace_marker(text: str, marker: str, content: str) -> str:
    """<!-- BEGIN: marker --> ... <!-- END: marker --> を content で置換"""
    pattern = re.compile(
        rf"(<!-- BEGIN: {marker} -->)(.*?)(<!-- END: {marker} -->)",
        re.DOTALL,
    )
    if not pattern.search(text):
        # マーカーがなければ末尾に追加
        text = (
            text.rstrip()
            + f"\n\n<!-- BEGIN: {marker} -->\n{content}\n<!-- END: {marker} -->\n"
        )
        return text
    return pattern.sub(rf"\1\n{content}\n\3", text)


def render_index_customer_array(customers: list[dict]) -> str:
    """index.html の `const customers = [...]` を再生成するためのJS文字列"""
    items = []
    for c in customers:
        # JSオブジェクトとして最低限のフィールドのみ自動同期
        # 詳細データ（detail/sections）は手動メンテナンスを残す
        # ここでは「概要パネル」用の薄いオブジェクトを生成
        cid = c.get("_id", "")
        name = c.get("display_name", cid).replace('"', '\\"')
        real = (c.get("real_name") or c.get("nickname") or "").replace('"', '\\"')
        priority = c.get("priority", "P3")
        status = c.get("status", "").replace('"', '\\"')
        plan = c.get("plan", "").replace('"', '\\"')
        plan_price = c.get("plan_price", "")
        plan_price_str = f"¥{plan_price}" if plan_price else "—"
        next_action = c.get("next_action", "").replace('"', '\\"')
        next_due = c.get("next_action_due", "").replace('"', '\\"')
        contact = (c.get("contact_method") or "—").replace('"', '\\"')
        daw = (c.get("daw") or "—").replace('"', '\\"')
        genre = (c.get("genre") or "—").replace('"', '\\"')
        # ステータスからキーを推定
        status_key = "active"
        if "成約" in status or "入金確認待ち" in status:
            status_key = "paid"
        elif "FB待ち" in status or "応答待ち" in status or "待ち" in status:
            status_key = "waiting"
        elif "無料" in status or "相談" in status:
            status_key = "free"
        items.append(
            f'  {{ id: "{cid}", name: "{name}", real: "{real}", priority: "{priority}", '
            f'statusKey: "{status_key}", status: "{status}", plan: "{plan}", '
            f'planPrice: "{plan_price_str}", nextAction: "{next_action}", '
            f'nextDue: "{next_due}", contact: "{contact}", daw: "{daw}", genre: "{genre}", '
            f'file: "customers/{c["_file"]}" }}'
        )
    return "const customersAuto = [\n" + ",\n".join(items) + "\n];"


def update_dashboard(customers: list[dict]):
    text = DASHBOARD_PATH.read_text(encoding="utf-8")
    table = render_dashboard_table(customers)
    text = replace_marker(text, "AUTO-CUSTOMER-TABLE", table)
    DASHBOARD_PATH.write_text(text, encoding="utf-8")
    print(f"[OK]{DASHBOARD_PATH.name} updated")


def update_schedule(customers: list[dict]):
    text = SCHEDULE_PATH.read_text(encoding="utf-8")
    p0 = render_schedule_p0(customers)
    p2 = render_schedule_p2(customers)
    text = replace_marker(text, "AUTO-P0-TASKS", p0)
    text = replace_marker(text, "AUTO-P2-TASKS", p2)
    SCHEDULE_PATH.write_text(text, encoding="utf-8")
    print(f"[OK]{SCHEDULE_PATH.name} updated")


def update_index_html(customers: list[dict]):
    """index.html のJSデータの自動生成は手動メンテナンスを尊重するため、
    別ファイル `data-auto.js` として書き出す。
    index.html は本体のcustomers定義を維持しつつ、必要に応じてこのファイルを参照可能。
    """
    data_path = ROOT / "data-auto.js"
    js = render_index_customer_array(customers)
    js = "// 自動生成ファイル — 編集禁止。crm/scripts/sync.py が生成する。\n" + js
    data_path.write_text(js, encoding="utf-8")
    print(f"[OK]{data_path.name} written (read-only auto data)")


def main():
    if not CUSTOMERS_DIR.is_dir():
        print(f"ERROR: {CUSTOMERS_DIR} not found", file=sys.stderr)
        sys.exit(1)

    customers = load_customers()
    print(f"Loaded {len(customers)} customers")

    # 優先度・期限でソート（P0 → P2 → P3、期限が近い順）
    priority_order = {"P0": 0, "P2": 1, "P3": 2}
    customers.sort(key=lambda c: (priority_order.get(c.get("priority", "P3"), 9),
                                    c.get("next_action_due", "9999")))

    update_dashboard(customers)
    update_schedule(customers)
    update_index_html(customers)
    print(f"\n[OK] Sync complete at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")


if __name__ == "__main__":
    main()

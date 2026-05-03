# 🦖 トリケラテクノ CRM

> Claude Codeで顧客対応・スケジュール・データベースを一元管理するための運用ディレクトリ。
> Notion持ち込みもしやすいMarkdown形式で、編集はそのまま `git` で版管理できる。

## ディレクトリ構成

```
crm/
├── README.md               ← このファイル（Claudeへの指示の出し方）
├── DASHBOARD.md            ← 全顧客一覧（毎日まずこれを開く）
├── SCHEDULE.md             ← 期限つきタスク／フォローアップキュー
├── PLAYBOOK.md             ← 運用ルール・SLA・ステータス定義（最重要）
├── plans.md                ← プラン一覧と料金表
├── customers/              ← 顧客ごとのファイル
│   ├── minoru.md
│   ├── daiki.md
│   ├── natsuki.md
│   ├── tatsuyan.md
│   └── hirokazoo.md
├── templates/              ← よく使うテンプレ
│   ├── new-customer.md
│   ├── feedback-report.md
│   ├── follow-up-message.md
│   └── upsell-pitch.md
└── log/                    ← 月次の応対ログ
    └── 2026-05.md
```

## 一日の流れ（推奨）

1. 朝：`DASHBOARD.md` と `SCHEDULE.md` を確認 → 今日やることを決める
2. 顧客とやり取りが発生 → Claude Codeに「〇〇さん（顧客名）からこのメッセージ来た。返信を作って」と依頼
3. 返信送付後 → 該当の `customers/<id>.md` の `last_updated` と `next_action` を更新
4. 夜：`log/<YYYY-MM>.md` に1行ログを残す

## Claude Codeへの指示例

| やりたいこと | 指示の例 |
|---|---|
| 返信案を作る | 「Minoruさんからこんなメッセージ来た（貼り付け）。返信を作って」 |
| データベースを更新 | 「ここまでのやり取りを送るので、Minoruさんのファイル更新して」 |
| 楽曲FBを作る | 「この楽曲を分析してFBレポートを作って。アンケート回答も踏まえて」 |
| Notion用に出力 | 「DASHBOARDをNotion貼り付け用に整形して出して」 |
| 新規顧客追加 | 「新しい顧客（名前・LINE履歴）を `customers/` に追加して」 |
| 戦略を考える | 「（顧客名）さんへの次の一手を考えて」 |
| ダッシュボード同期 | 「全customersファイルからDASHBOARDとSCHEDULEを最新に同期して」 |

## 運用上の絶対ルール（PLAYBOOK.md からの抜粋）

1. **約束した期日は守る**（特にFB送付の「週末まで」）
2. **名前を取り違えない**（DAn ≠ Dさん の混同事故防止）
3. **やり取りしたら即時更新**（顧客ファイル → ダッシュボード → スケジュール）
4. **`next_action` が空の顧客はゼロにする**

## このCRMをClaude Codeで使う時の前提

- 「Dさん」と言われたら **hirokazooさん**（PsyTrance/Bitwig）。**DAIKIさんではない**
- 顧客ファイルの frontmatter（`---` で囲まれた部分）は機械可読を意図しているので、構造を壊さずに値だけ更新する
- Markdownの見出し階層（`#`〜`###`）はNotion持ち込み時の構造になるので変えない
- 個人情報（メール・本名）は **このリポジトリの中だけ**で扱う

## 引き継ぎ元

- `C:\Users\神田 元夫\Downloads\TriceraTechno_CRM_Code引き継ぎ_v2.docx`
- 上記docxの内容を 2026-05-03 に取り込み、構造化したのがこのCRM

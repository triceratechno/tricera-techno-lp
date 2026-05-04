# 🛠️ CRMスクリプト

## sync.py — データ同期

`customers/*.md` のYAMLフロントマターを真実として、以下を自動更新する：

- `crm/DASHBOARD.md` の顧客サマリー表
- `crm/SCHEDULE.md` の P0／P2 タスクリスト
- `crm/data-auto.js`（自動生成データ・index.html から参照可能）

### 使い方

```bash
# プロジェクトルートで
python crm/scripts/sync.py

# 文字エンコーディング問題が出たら
PYTHONIOENCODING=utf-8 python crm/scripts/sync.py
```

### 動作の仕組み

各出力ファイルには自動生成領域を示すマーカーが置いてある：

```markdown
<!-- BEGIN: AUTO-CUSTOMER-TABLE -->
（自動生成される領域）
<!-- END: AUTO-CUSTOMER-TABLE -->
```

このマーカーの中身だけが書き換わる。マーカー外の手動編集は保持される。

### マーカー一覧

| ファイル | マーカー | 内容 |
|---|---|---|
| DASHBOARD.md | `AUTO-CUSTOMER-TABLE` | 顧客サマリー表（名前・プラン・ステータス・次のアクション・期限・優先度） |
| SCHEDULE.md | `AUTO-P0-TASKS` | P0優先度のタスクリスト |
| SCHEDULE.md | `AUTO-P2-TASKS` | P2優先度のタスクリスト |

### data-auto.js について

index.html の表示は手動メンテナンスを尊重する設計のため、`data-auto.js` は **「サブセットの自動生成データ」** として別ファイルに書き出される。
index.html 内の詳細データ（FB履歴、技術分析、LTVシナリオなど）は自動同期の対象外。

将来的に index.html を「`data-auto.js` を読み込んで描画する」形にリファクタすれば、完全自動化も可能。

### Claude Codeへの依頼の仕方

```
「customers の最新版で sync.py を回して、ダッシュボード同期して」
```

### トラブルシューティング

- **マーカーが見つからない警告**：マーカーがない場合、ファイル末尾に追記される。手動で適切な場所に移動できる。
- **YAMLパースエラー**：customers/*.md の `---` フロントマターのインデントを確認。タブと半角スペースが混在しているとエラーになる。
- **文字化け**：Windowsの cp932 環境では `PYTHONIOENCODING=utf-8` を頭に付ける。

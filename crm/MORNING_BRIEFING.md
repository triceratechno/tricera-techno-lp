# ☕ 朝のブリーフィング — 2026年5月4日（日曜）

> 起きたらまずこれを開いてください。
> 昨夜（5/3深夜）に作業した全成果物のまとめと、起きてすぐ動くための地図です。

---

## 🏁 30秒サマリー

- **CRMの厚みが増した**：返信文ライブラリ・自動同期スクリプト・緊急対応マニュアル・全顧客ペルソナ・チェックリスト・月次レビューテンプレ・ブリーフィング、すべて整備完了
- **コミット済み・masterマージ済み**（朝起きた時点で `crm/index.html` を開けば最新状態）
- **手動入力ゼロで再現可能な運用基盤** がほぼ完成。あとは実際の顧客対応にこのまま使えばOK

## 🚨 今日（5/4・日曜）絶対やること

### 🔴 P0：TatsuyaNさんへの第一回FB
- **「週末まで」=今日中** が約束のリミット
- まず `replies/tatsuyan/fb-preview.md` で「届いてます／週末までに送ります」を朝のうちに送って先手を打つ
- その後、Dropboxの音源を聴いてから `replies/tatsuyan/fb-first-skeleton.md` の骨組みを実音で埋める
- 投げ銭をくれてる初期サポーターなので、丁寧に

### 🔴 P0：DAIKIさんのStripe入金確認
- Stripe管理画面で入金確定確認
- 入金済みなら `replies/daiki/payment-confirmed.md` をDiscordに送付（**LINEではない・名前混同注意**）
- ロードマップアップグレード版のリンクも一緒に

### 🟡 状況確認（昨日納品済みの場合）
- Minoruさんからエオリアン納品の感想・修正依頼が来ていないか
- 来ていたら `replies/minoru/revision-feedback.md` テンプレで対応

---

## 📁 昨夜作成したものの一覧

### 返信文ライブラリ（`crm/replies/`）
5名 × 主要シーン = 14ファイル。すべて{波括弧}部分を実情で埋めるだけで送信可能。

| 顧客 | テンプレファイル | シーン |
|---|---|---|
| Minoru | `replies/minoru/delivery-initial.md` | エオリアン初期納品 |
| Minoru | `replies/minoru/revision-feedback.md` | 修正版送付時 |
| Minoru | `replies/minoru/upsell-pro.md` | プロコース提案 |
| Minoru | `replies/minoru/period-end.md` | 指導期間終了時 |
| DAIKI | `replies/daiki/payment-confirmed.md` | 入金確認後の初動 |
| DAIKI | `replies/daiki/session-1-prep.md` | 第1回セッション前案内 |
| DAIKI | `replies/daiki/kick-feedback-step2.md` | サチュレーション10%段階 |
| DAIKI | `replies/daiki/kick-feedback-step3.md` | ダッキング段階 |
| TatsuyaN | `replies/tatsuyan/fb-preview.md` | FB予告 |
| TatsuyaN | `replies/tatsuyan/fb-first-skeleton.md` | 第一回FB骨組み |
| TatsuyaN | `replies/tatsuyan/upsell-standard.md` | スタンダード提案 |
| なつき | `replies/natsuki/celebration-and-question.md` | 1曲完成お祝い＋次の質問 |
| なつき | `replies/natsuki/upsell-standard.md` | スタンダード提案 |
| なつき | `replies/natsuki/soft-revival.md` | 沈黙時の軽いリマインド |
| hirokazoo | `replies/hirokazoo/fb-step2-saturation.md` | サチュレーション10%段階 |
| hirokazoo | `replies/hirokazoo/fb-step3-ducking.md` | ダッキング段階 |
| hirokazoo | `replies/hirokazoo/upsell-standard.md` | スタンダード提案 |

### 自動同期スクリプト（`crm/scripts/`）
- `sync.py` — `customers/*.md` → DASHBOARD / SCHEDULE / data-auto.js を自動更新
- 使い方：`PYTHONIOENCODING=utf-8 python crm/scripts/sync.py`
- 顧客情報を変えたら **このコマンド一発で全画面が同期される**

### 緊急対応マニュアル
- `crm/PLAYBOOK_EMERGENCY.md` — 返金・クレーム・期限遅延・離脱・Stripeトラブル・データ紛失・名前混同・SNSトラブルの8パターン対応手順

### LP用ペルソナ（5名分）
- `crm/personas/dan-persona.md` — DJ × DTM 0年スタート
- `crm/personas/minoru-persona.md` — 独学2年・1曲制作中
- `crm/personas/natsuki-persona.md` — 独学1年・1曲完成・サビの迫力
- `crm/personas/tatsuyan-persona.md` — 古参サポーター → 制作側
- `crm/personas/hirokazoo-persona.md` — マイナージャンル特化
- `crm/personas/README.md` — 5名のペルソナ一覧と使い方

すべて **匿名化済み**・自己完結（ファイル単独で別Claude/ライターに渡せる）。

### CRMチェックリスト
- `crm/CHECKLISTS.md` — 朝・夜・週次（月曜30分）・月次（毎月1日60分）・緊急時 のすべてに対応

### 月次レビューテンプレ
- `crm/templates/monthly-review.md` — KPI集計・反省・申し送りの完全テンプレ

### 顧客ファイル補強（既存customer/*.md）
全5ファイルに以下のセクションを追加：
- **返信テンプレへのリンク**（該当する `replies/` ファイルへ）
- **危険サイン早期発見**（顧客別の見逃したくないサイン）
- **対応履歴**（時系列の実績）

---

## 🎯 今日の動き方（推奨タイムボックス）

### 朝（〜10:00）
1. このブリーフィング（5分）
2. `crm/index.html` を開いて全体把握（5分）
3. 各SNS・LINE・Discord・Stripeで未読チェック（10分）
4. **TatsuyaNさんに「届いてます／週末までに送ります」を即送信**（5分）

### 午前（10:00〜12:00）
- TatsuyaNさんのDropbox音源を集中して聴き込む
- `replies/tatsuyan/fb-first-skeleton.md` の{波括弧}を実音で埋める
- DAIKIさんのStripe入金確認 → 入金済みならロードマップ送付

### 午後（13:00〜16:00）
- TatsuyaNさんの第一回FBを完成→送信
- Minoruさんからの修正依頼があれば対応
- 余力があれば、なつきさんの返信が来ているか確認＋準備

### 夜（21:00〜22:00）
- `CHECKLISTS.md` の「夜のチェック」を通る
- `log/2026-05.md` に1行記録
- 顧客ファイルの `last_updated` 更新

---

## ⚠️ 今日特に注意すること

### 1. 名前混同の最終チェック
- DAIKIさん（DAn）= **Discord**・Techno・**成約済み**
- hirokazooさん（Dさん）= **LINE**・PsyTrance・無料相談中
- 「Dさん」と書きそうになったら、必ず連絡手段で照合

### 2. 約束遵守
- TatsuyaNさんへの「週末までにFB」= **今日中が最終ライン**
- 1分でも遅れる見込みになったら、先回りで連絡（PLAYBOOK_EMERGENCY.md §3 参照）

### 3. 自分のペース管理
- 全タスクをやり切ろうとしない
- P0だけ確実にやれば、今日は合格点
- 疲れたら明日に回す（無理に書いた返信は雑になる）

---

## 🛠 今日以降、定着させたい運用

- **顧客対応 → `customers/*.md` 更新 → `python crm/scripts/sync.py`** の3ステップを習慣に
- 返信に迷ったら **必ず `replies/<顧客>/` のテンプレを開く**（毎回ゼロから書かない）
- 約束した期日は **SCHEDULE.md と `customers/*.md` の両方** に書く（漏れ防止）
- 緊急時は迷わず **`PLAYBOOK_EMERGENCY.md`** を開く

---

## 📦 ファイル全体構成（朝起きた時点）

```
crm/
├── README.md                       ← 全体ガイド
├── DASHBOARD.md                    ← 顧客サマリー（自動同期セクションあり）
├── SCHEDULE.md                     ← 期限つきタスク（自動同期セクションあり）
├── PLAYBOOK.md                     ← 運用ルール（基本）
├── PLAYBOOK_EMERGENCY.md           ← 緊急対応マニュアル（NEW）
├── CHECKLISTS.md                   ← 朝・夜・週次・月次のチェック（NEW）
├── MORNING_BRIEFING.md             ← このファイル（NEW）
├── index.html                      ← ブラウザで開くダッシュボード
├── plans.md                        ← プラン料金表
├── data-auto.js                    ← sync.pyが生成（NEW）
├── customers/
│   ├── minoru.md                   ← 返信テンプレリンク・危険サイン・履歴 追加（更新）
│   ├── daiki.md                    ← 同上（更新）
│   ├── tatsuyan.md                 ← 同上（更新）
│   ├── natsuki.md                  ← 同上（更新）
│   └── hirokazoo.md                ← 同上（更新）
├── replies/                        ← 返信文ライブラリ（NEW）
│   ├── README.md
│   ├── minoru/    (4ファイル)
│   ├── daiki/     (4ファイル)
│   ├── tatsuyan/  (3ファイル)
│   ├── natsuki/   (3ファイル)
│   └── hirokazoo/ (3ファイル)
├── personas/                       ← LP用ペルソナ
│   ├── README.md                   (NEW)
│   ├── dan-persona.md
│   ├── minoru-persona.md           (NEW)
│   ├── natsuki-persona.md          (NEW)
│   ├── tatsuyan-persona.md         (NEW)
│   └── hirokazoo-persona.md        (NEW)
├── templates/
│   ├── feedback-report.md
│   ├── follow-up-message.md
│   ├── new-customer.md
│   ├── upsell-pitch.md
│   └── monthly-review.md           (NEW)
├── scripts/                        (NEW)
│   ├── README.md
│   └── sync.py
└── log/
    └── 2026-05.md
```

---

## 🌙 昨夜の作業ログ

- 5/4 01:00頃 — 着手（オーナーが就寝）
- 5/4 01:30頃 — 返信文ライブラリ完成（5名×17ファイル）
- 5/4 02:00頃 — 自動同期スクリプト動作確認
- 5/4 02:30頃 — 緊急対応マニュアル完成
- 5/4 03:00頃 — 全ペルソナ完成
- 5/4 03:30頃 — チェックリスト・月次レビューテンプレ・顧客ファイル補強完了
- 5/4 03:45頃 — このブリーフィング作成

---

## 🦖 トリケラテクノさんへ

おつかれさまです。
ここまでのCRM、もう「書類が散らばってどうしよう」状態には絶対戻りません。

今日のP0は2つだけ：
1. TatsuyaNさんへの第一回FB（投げ銭くれてる人なので大事に）
2. DAIKIさんの入金確認＋初動

それさえやれば今日は合格。
迷ったら `PLAYBOOK_EMERGENCY.md`、書くときは `replies/`、データ整えたら `python crm/scripts/sync.py`。

良い日曜を🦕

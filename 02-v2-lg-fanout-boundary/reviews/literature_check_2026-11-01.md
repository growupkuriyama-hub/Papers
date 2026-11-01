# 新しい結果の文献調査（C3）— 2026-11-01

対象：`02-v2-lg-fanout-boundary/main.tex`（2026-11-01、37ページ）。投稿前チェックリストの「本文に残る新しい結果の文献調査」。
調査者：Claude。方法は二つ。(1) 研究文献庫（Research-Library）の原典 PDF の全文検索。(2) Web 検索（一般検索と詳しい検索を合わせて数回）。**網羅的な調査ではない**ので、「見つからなかった」は「存在しない」を意味しない。

## 1. 調べた主張と結論

| 主張（label） | 先行研究で見つかったもの | 判断 |
|---|---|---|
| 線形因子 Ω(‖G‖θ̄) が全てのファンアウト・全ての型付けで必要（`prop:linear-factor-all-fanout`、4f+1 文字以上） | 上界だけ。Yoshinaka 2008（Thm 1）、Yoshinaka 2011（Lemma 7, Thm 1：‖K_G‖ ≤ \|P\|θ_G）、Eyraud–Heinz–Yoshinaka 2016 §2.5.2（IPTtD。「特徴標本は大きさと厚さの多項式」）、Coste–Nicolas 2019（厚さによる上界）。いずれも**下界は述べていない** | 新しいと判断してよい。原稿の「Yoshinaka の上界が定数倍まで達成される」という書き方は正確 |
| 自明な型付けで Θ(‖G‖θ̄)（`cor:trivial-exact`） | 上界は Yoshinaka 2011 の直接の帰結（原稿も明記）。下界側は上と同じ | 新しいのは下界の部分。原稿の書き方（上界は既知の型付き版、達成は標識族）で問題ない |
| 局所群（LG）型付けの多項式データ（`thm:local-group-polydata`）と、擬多様体の境界（`thm:fanout-one-data`） | LG の代数（LG = Grp ∗ D、U₁ の除外）は古典（Straubing 1985、Tilson 1987、Almeida et al. 2009。原稿で引用済み）。**文法推論・分布学習で LG を扱った文献は見つからなかった** | 新しいと判断してよい。代数が古典であることは原稿に明記済み |
| 非可換群での持ち主ごとの同時置換（`prop:block-replacement-interface`） | ゼロ和（Davenport 定数）は古典（Geroldinger–Halter-Koch、引用済み）。**学習・文法の短縮に使った例は見つからなかった** | 新しいと判断してよい（技術） |
| 括弧付き倍増族がファンアウト2で持ち上がらない（`thm:doubling-no-lift`） | ファンアウトについてクラスが単調でないことは Yoshinaka 2011 の例（引用済み）。指数族そのものは 01（引用済み） | 新しいと判断してよい |
| L_R の例（`prop:feature-cross-typed`、今回付録 H に復帰） | 多次元代入可能性は Yoshinaka 2009/2011（引用済み）。この例自体は見つからなかった | 新しい例。主張は「多次元代入可能でない」ことだけで、控えめ |

## 2. 注意すべき点

1. **著者自身の旧版 arXiv:2605.11644。** 公開されている題は *The Value of Finite Observation in Positive-Data Learning of Multiple Context-Free Languages* で、archive-v1 の README に書かれた題（*Positive-Data Learning of Multiple Context-Free Languages under Fixed Finite-Monoid Typing*）と異なる。中身は 02 の前身（観測で守られた組の代入可能性、正準の学習器、観測の量とデータ）。
   - 現行 02-v2 はこの旧版を引用していない。Elsevier はプレプリントの公開を認めているので違反ではないが、**カバーレターに「arXiv:2605.11644 の大幅な改訂版」と書くこと**を勧める。査読者が旧版を見つけたときの混乱を防げる。
   - 03（`03_scl-compression`）と 07 はこの arXiv 番号を引用している。博士論文の構成表（`doctoral-thesis-minimal/STATUS.yaml`）も同じ番号を持つ。題の食い違いは、次に v1 側の記録を触るときに直すとよい。
2. **Coste–Nicolas 2019 と Coste–Garet–Nicolas 2012**（局所代入可能性）は、比較の根拠を制限する別の偏りで、原稿の序論で区別済み。データの下界は述べていない（原典を検索して確認）。
3. **見つからなかったが、念のため査読者推薦で考慮するとよい分野**：形式言語の短縮補題（pumping）でのゼロ和の利用、Simon の分解林を学習に使う研究。今回の検索では該当なし。

## 3. 調べた原典（Research-Library）

REF-01-05 de la Higuera 1997、REF-02-02 Yoshinaka 2008、REF-02-04 Yoshinaka 2015、REF-02-06 Eyraud–Heinz–Yoshinaka 2016、REF-02-07 Coste–Nicolas 2019、REF-02-08 Numaya et al. 2023（本文の文字を取り出せず未確認）、REF-02-09 Kanazawa–Yoshinaka 2023、REF-03-04 Yoshinaka 2011、REF-03-20 Case–Yoshinaka–Zeugmann 2013。
検索語：lower bound、tight、optimal、necessary、thickness、characteristic sample の長さ・大きさ、exponential。

## 4. 結論

本文に残る新しい結果について、先行研究と重なるものは見つからなかった。原稿の帰属（代数は古典、定性的な学習は Yoshinaka、上界は Yoshinaka の型付き版）は、調べた範囲で正確である。投稿前に残る作業は、カバーレターでの旧版 arXiv の扱いだけである。

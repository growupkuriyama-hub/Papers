# 02-v3 新生 #2 CFG — 構成案と出典対応表（2026-11-20 着手）

**仮題：** *Which Fixed Typings Give Polynomial Characteristic Data? A Classification for Substitutable Context-Free Languages*

**コンセプト（著者決定 2026-11-20）：** fan-out 1（CFG）に絞る。これまでの #2（02-v2）の成果のうち fan-out 1 で閉じている部分を中心に据える。

1. LG 境界（擬多様体レベル）
2. U₁ 型付けの個別分類（孤立文字定理）
3. 線形因子の必要性と、二文字 U₁ での θ̄²
4. 任意で rank 1 との対比

目標は英文 28〜32 ページ。

## 0. 設計上の決定（要著者確認）

| 論点 | 暫定方針 | 理由 |
|---|---|---|
| 枠組み | **02-v2 の枠組みを f=1 に特殊化**する。reduced good 表示、規則厚さ θ̄_G、作用素 `B_{1,s}`, `B^{≤r}_{1,s}` | 退避資料の証明はすべてこの枠組みで書かれ、監査も受けている。クラスと特性標本の定義は #1 と一致する（02-v2 の `lem:fanout-one-classes`）ので、#1 との比較は一つの補題で済む |
| 表記 | `\Cmcf{1}{s}` を `\Ccf{s}` に置き換える（#1 と同じ記号） | #1 との連続性 |
| 指数下界の族 | **自己完結の三文字族**（43pp 版の `prop:three-letter-family`、付録 `app:three-letter-family`）を使う。#1 の五文字括弧族は比較として引用するだけ | 個別型付けの障害 `cor:typing-level-obstruction` が三文字族の文字ごとの像を使うため、自己完結の族が必要 |
| LG 十分性の証明 | 当面は 02-v2 の一般 f の証明を f=1 に限定して流用する（正しさが保たれる）。そのうえで **f=1 専用の短縮（付録 A の大幅削減）を後続タスク**にする | 着手時点で証明の連鎖を切らないため |
| MCFG への言及 | 結論で「十分性は全 fan-out に持ち上がる（02-v2／博士論文）」と一言だけ触れる。主張はしない | 細切れ投稿（サラミ）を避ける |
| #1 との差分 | 序論で明示する。#1 は LI∨Grp で十分、U₁ が障害、必要性は主張しない。本稿は (a) LG で十分、(b) 擬多様体レベルの同値、(c) 個別型付けの分類、(d) 指数の形、を示す | 査読対策 |

## 1. 主定理（序論に置く）

| 番号 | 内容 | 出典 |
|---|---|---|
| Theorem A | f=1, r_max≥2：擬多様体 V が一様な多項式特性データ長を持つ ⇔ V ⊆ LG。LG なら O(‖G‖²θ̄)、LG 外なら指数（3·2ⁿ−1 以上） | 現行 `main.tex` の `thm:fanout-one-data` と `thm:local-group-polydata`（f=1）。43pp 版の `thm:fanout-one-data` と三文字族 |
| Theorem B | U₁ への型付け s（r_max≥2）：多項式 ⇔ 型 1 の文字がちょうど1つ。一般の型付けでは、孤立文字は多項式、文字が互いに素な e,e,z 語は指数 | plan1 断片 Part 1：`cor:u1-classification`, `thm:two-letter-fanout-one`, `cor:two-letter-fanout-one`, `cor:typing-level-obstruction`, `def:isolated-letter` |
| Theorem C | 上界の形：(i) どの型付けでも（2文字以上）Ω(‖G‖θ̄) が必要。自明な型付けでは Θ(‖G‖θ̄)。(ii) 二文字 U₁ 型付けは多項式だが θ̄² の依存が必要。定重みならちょうど θ̄²/4 程度 | 43pp 版の `prop:linear-factor-all-fanout`(iv)（f=1・2文字版）と `cor:trivial-exact`。plan1 断片の `prop:binary-u1-quadratic`。parked_u1 の `prop:binary-u1-weight-slice` |
| （任意）Prop R | rank 1 なら、どの型付けでも O(‖G‖²θ̄)。rank 2 で初めて LG が効く | parked_u1 の `thm:rankone-polydata`（f=1 に特殊化） |

**見どころの一文：** 擬多様体レベルの境界は LG だが、個々の型付けでは LG の外（二文字 U₁）でも多項式になりうる。ただしその代償は θ̄²。

## 2. 節構成と出典

`O` = `02-v2-lg-fanout-boundary/parked/planA_2026-11-16/original_en_43pp.tex`（43pp 版）
`P1` = `02-v2-lg-fanout-boundary/parked/plan1_small_alphabet_2026-11-11.tex`（64pp 版の断片）
`PU` = `02-v2-lg-fanout-boundary/parked/parked_u1_typing_level.tex`
`M` = `02-v2-lg-fanout-boundary/main.tex`（Plan A＋light B、2026-11-17）

| 節 | 内容 | 主な出典（ラベル） | 見込み |
|---|---|---|---|
| 1 序論 | 背景、#1 との差分、Theorems A–C、証明の方法 | 新規執筆。M の序論の一部 | 3.5 p |
| 2 準備 | 型付け、CFG（good・reduced・size・thickness）、型付き代入可能性、特性標本 | O §2（`def:characteristic-sample`, `def:semigroup-typing`, `def:prefix-suffix-typing`, `def:standard-mcfg`→CFG 化, `def:grammar-properties`, `def:class-cmcf`）、M `lem:fanout-one-classes` | 3 p |
| 3 再構成と特性データ | 作用素、健全性、型付き証人、型付き厚さ→データ長、区別部分標的、希少型 | O §3–4（`def:reconstruction`, `prop:reconstruction-soundness`, `prop:completeness`, `prop:good-normalization`, `thm:data-from-typed-thickness`, `lem:distinguishing`, `prop:rare-type`, `prop:typed-thickness-exponential`） | 4 p |
| 4 LG の十分性 | スライド因子座標、短い代表元、O(‖G‖²θ̄) | O §5.1, 5.3, `app:local-group`（`thm:lg-characterization`, `cor:lg-type-level-shortest`）、`app:group-blocks`（f=1 で縮約） | 3 p（＋付録） |
| 5 擬多様体の境界 | 三文字族、Theorem A | O §7（`prop:three-letter-family`, `def:uniform-polydata`, `thm:fanout-one-data`）、M §6 の注記（`rem:fanout-one-data`） | 2.5 p |
| 6 個々の型付け | 文字が互いに素な障害、孤立文字、U₁ の分類、二文字 U₁ の二次 | P1 Part 1 全体、PU `prop:binary-u1-weight-slice` | 3 p |
| 7 上界の形 | 線形因子、自明な型付けでの Θ、（任意）rank 1 | O §6（`prop:linear-factor-all-fanout`(iv), `cor:trivial-exact`）、PU `thm:rankone-polydata` | 1.5 p |
| 8 結論 | 開いている点：U₁ 以外の個別分類、‖G‖ の1因子、MCFG への持ち上げ | 新規 | 0.7 p |
| 付録 A | 群のブロック置換（f=1 版） | O `app:group-blocks`, `app:window-group` | 2–3 p |
| 付録 B | LG 座標とブロック短縮 | O `app:local-group` | 3 p |
| 付録 C | 三文字族の代入可能性 | O `app:three-letter-family` | 2.5 p |
| 付録 D | 孤立文字定理の証明 | P1 `app:two-letter-fanout-one`（ChatGPT 11/09 査読の修正点を反映：`lem:app-h-tree`(d) は k≥1 に限定など） | 6–7 p |
| 付録 E | U₁ 型付け（文字ごとの像、二次） | P1 `app:u1-typings` | 1.5 p |
| 付録 F | 線形因子族 | O `app:linear-factor-fanout`（f=1 に特殊化） | 1 p |
| 付録 G | 型付き証人・特性データの補助証明、good 正規化 | O `app:typed-witness-aux-proofs`, `app:normalization-details`, `app:qualitative-construction-details` | 3 p |

**合計見込み：本文 21 p＋付録 20 p ≈ 41 p（現状のまま組んだ場合）。** 目標の 28〜32 p にするには次の圧縮が必要。

- 付録 A を f=1 用に短縮する（−2 p）。
- 付録 G のうち Yoshinaka 由来の定性的部分は引用で済ませる（−2 p）。
- 付録 D の記述を整理する（−1〜2 p）。
- tuple 表記を CFG 表記に置き換える（全体で −2〜3 p）。

## 3. 作業順序

1. [x] ディレクトリ・README・PAPER.yaml・この対応表（2026-11-20）
2. [x] `main.tex` の骨組み：題名、アブストラクト草稿、序論草稿、主定理の文、節見出しと出典コメント
3. [ ] §2–3 を O から移植し、f=1 の CFG 表記に置き換える
4. [ ] §5 と付録 C を移植する（三文字族）
5. [ ] §6 と付録 D・E を P1 から移植し、査読指摘（11/09）を反映する
6. [ ] §7 と付録 F
7. [ ] §4 と付録 A・B：まず流用し、次に f=1 用に短縮する
8. [ ] 全体の独立監査（移植後の本文に対して）
9. [ ] 日本語版（著者の希望があれば）

## 4. 禁止事項・注意

- 02-v2 のファイルは編集しない（凍結）。出典はコピーして移植し、ここに出典ラベルを記録する。
- fan-out 2 の研究結果（`reviews/` の P_tree, AB, U₂ など）は持ち込まない。
- #1（TCS-D-26-00494）は審査中。引用は arXiv:1409.6247v5 の番号で行い、採択を前提にした記述はしない。

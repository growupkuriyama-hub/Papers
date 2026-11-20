# 02-v3 新生 #2 CFG — 構成案と出典対応表

**仮題：** *Which Fixed Typings Give Polynomial Characteristic Data? A Classification for Substitutable Context-Free Languages*

**コンセプト（著者決定 2026-11-20）：** fan-out 1（CFG）に絞る。これまでの #2（02-v2）の成果のうち fan-out 1 で閉じている部分を中心に据える。

1. LG 境界（擬多様体レベル）
2. U₁ 型付けの個別分類（孤立文字定理）
3. 線形因子の必要性と、二文字 U₁ での厚さ二乗
4. （rank 1 の対比は #1 の線形定理と重なるので、引用だけにする）

**枠組み（著者決定 2026-11-20 17:41）：** #1 の枠組みをそのまま使い、そこに結果を足していく形で再構築する。具体的には次のとおり。

- 任意の reduced CFG による表示、BUNF、作用素 `Rec_s`、通常の厚さ `τ_G`、型付き厚さ `τ^typ_s(G)`
- 結論の形も #1 の Cor. 7.5 と同じにする：「各 reduced CFG `G_*` に対し、`Rec_s` の特性データは `|G_*|` と `τ_{G_*}+1` の多項式」

## 0. 全体の設計：「#1 は型付き厚さに帰着した。本稿はそれを計算する」

#1 はすべての上界を一つに帰着している。

- **#1 Cor. 6.3：** `Rec_s` の特性データは `|G|` と `τ^typ_s(G)` の多項式（G は reduced BUNF）。
- **#1 Prop. 7.3：** 任意の reduced CFG を、大きさと通常の厚さを多項式に保ったまま BUNF にできる。

したがって本稿の上界は、すべて次の形の主張に帰着する。

> 「この型付け s では、reduced BUNF G について τ^typ_s(G) ≤ poly(|G|, τ_G+1)」

02-v2 の上界（LG の短縮、孤立文字定理）は、**reduced good（ε-free）表示と規則厚さ θ̄** で書かれている。そこで二つを繋ぐ**橋渡し補題**を新しく証明する（§3。新しい数学だが短い）。

| 補題 | 内容 | 状態 |
|---|---|---|
| Lemma 3.1（ε 除去と厚さ） | reduced BUNF の G から reduced good で rank ≤2 の G⁺ を作れる。L_{G⁺}(A)=L_G(A)∖{λ}、‖G⁺‖ ≤ c\|G\|、θ̄_{G⁺} ≤ 3\|V\|(τ_G+1) | **草稿を main.tex に執筆（要監査）** |
| Lemma 3.2（型付き厚さの移送） | τ^typ_s(G) ≤ max{1, t_typ(G⁺,s)} | **草稿を執筆（要監査）** |
| Lemma 3.3（尺度の比較） | reduced good な H では τ_H ≤ θ̄_H、かつ \|H\| と ‖H‖ は定数倍の差 | **草稿を執筆（要監査）** |
| Cor. 3.4（主系） | reduced good で rank ≤2 の H について t_typ(H,s) ≤ q(‖H‖, θ̄_H) なら、任意の reduced CFG に対し Rec_s の特性データは多項式 | **草稿を執筆（要監査）** |

**下界**は希少型の論法で示す。対象は「クラス全体で特性標本を持つ任意の set-driven 作用素」で、#1 Thm 5.3 により Rec_s もこれに含まれる。表示の尺度は Lemma 3.3 で移す。

## 1. 主定理（#1 の尺度で述べる）

| 番号 | 内容 | 根拠 |
|---|---|---|
| Theorem A | r_max ≥2 を前提に、擬多様体 V が一様な多項式特性データ長を持つ ⇔ V ⊆ LG。(i) LG なら reduced BUNF で τ^typ_s(G) ≤ c_{\|S\|}\|V\|²(τ_G+1)。よって任意の reduced CFG で Rec_s のデータは poly(\|G_*\|)·(τ_{G_*}+1)（#1 Cor. 7.5 の LI∨Grp を LG へ一般化）。(ii) LG 外：#1 Prop. 6.4 と Cor. 6.6 | 02-v2 `cor:lg-type-level-shortest`（f=1）＋主系。代数は 02-v2 `thm:lg-characterization` |
| Theorem B | U₁ への型付け s：多項式 ⇔ 型 1 の文字がちょうど1つ。一般の型付けでは、孤立文字は多項式、文字が互いに素な e,e,z 語は指数 | 02-v2 の `thm:two-letter-fanout-one`、`lem:app-h-other`（t_typ の上界）＋主系。障害は三文字族（`cor:typing-level-obstruction`）＋Lemma 3.3 |
| Theorem C | (i) どの型付けでも（3文字以上）データ ≥ c·\|G\|·τ_G となる標的がある。(ii) LG 型付けは厚さについて線形 poly(\|G\|)(τ_G+1) だが、二文字 U₁ 型付け s_{U,2} は多項式であってもどんな p についても p(\|G\|)·(τ_G+1) では抑えられない | 02-v2 `prop:linear-factor-all-fanout`(iv)、`prop:binary-u1-quadratic`、Lemma 3.3 |

**見どころ：** 擬多様体レベルの境界は LG である。一方、個々の型付けでは LG 外でも多項式になりうる（s_{U,2}）。ただしそのときは厚さについて線形な上界が崩れる。

## 2. 節構成と出典

`C1` = `01_fixed-h-cfg/main.tex`（#1 R1。番号は R1 のビルドによる。投稿時には arXiv 版の番号と照合する）
`O` = `02-v2-lg-fanout-boundary/parked/planA_2026-11-16/original_en_43pp.tex`
`P1` = `02-v2-lg-fanout-boundary/parked/plan1_small_alphabet_2026-11-11.tex`
`PU` = `02-v2-lg-fanout-boundary/parked/parked_u1_typing_level.tex`

| 節 | 内容 | 出典 | 見込み |
|---|---|---|---|
| 1 序論 | 問い、#1 との差分、Theorems A–C | 新規 | 3 p |
| 2 #1 の枠組みの再掲 | Ccf_s、Rec_s、BUNF、τ_G、τ^typ_s、C1 の Thm 5.3、Lem 6.2、Cor 6.3、Prop 6.4、Cor 6.6、Prop 7.3、Cor 7.5。証明は引用で済ませる | C1 §2–§7 | 2.5 p |
| 3 橋渡し | Lemma 3.1–3.3、Cor 3.4、下界の一般原理（区別部分標的） | **新規**、O `lem:distinguishing`, `prop:rare-type` | 2.5 p |
| 4 LG の十分性 | スライド因子座標、短い代表元（f=1）、Theorem A(i) | O `app:local-group`, `cor:lg-type-level-shortest`, `app:group-blocks`（f=1 に縮約） | 2 p＋付録 |
| 5 擬多様体の境界 | Theorem A(ii)：C1 Prop 6.4＋代数 | O `thm:fanout-one-data` の論法 | 1 p |
| 6 個々の型付け | 障害、孤立文字、U₁ の分類 | P1 Part 1、O `prop:three-letter-family` | 3 p |
| 7 上界の形 | 線形因子、厚さについて線形な上界の破れ | O `prop:linear-factor-all-fanout`(iv)、P1 `prop:binary-u1-quadratic` | 1.5 p |
| 8 結論 | 開いている点（U₁ 以外の個別分類、\|G\| の次数）、MCFG への持ち上げ（主張しない） | 新規 | 0.5 p |
| 付録 A | LG 座標とブロック短縮（f=1） | O `app:local-group`, `app:group-blocks`, `app:window-group` | 4–5 p |
| 付録 B | 三文字族 | O `app:three-letter-family` | 2.5 p |
| 付録 C | 孤立文字定理 | P1 `app:two-letter-fanout-one`（11/09 査読の修正を反映） | 6–7 p |
| 付録 D | U₁ 型付けの補題、二次の族 | P1 `app:u1-typings` | 1.5 p |
| 付録 E | 線形因子族 | O `app:linear-factor-fanout`（f=1） | 1 p |

**見込み：本文 16 p＋付録 16 p ≈ 32 p。** 改訂前の構成より軽くなる理由は二つ。#1 の定性的な部分（再構成・健全性・完全性・good 正規化・Gold）をすべて引用で済ませられることと、02-v2 の特性データの補助証明（`app:typed-witness-aux-proofs` 等）が #1 の Lem 6.2・Cor 6.3 に置き換わることである。

## 3. 作業順序

1. [x] ディレクトリ・README・PAPER.yaml・対応表（2026-11-20）
2. [x] main.tex の骨組み
3. [x] #1 の枠組みへの切り替え、橋渡し補題の草稿（2026-11-20）
4. [ ] §2 を C1 の定義から書き、番号を arXiv 版と照合する
5. [x] 付録 A と §4（LG）：fan-out 1 専用の自己完結した証明（前置積の鳩の巣）に置き換えた（2026-11-20）
6. [x] 付録 B・C・D と §6（2026-11-20 移植。代表元版の証人補題 `lem:rep-witness` を新設）
7. [x] §7 と付録 E（2026-11-20 移植。線形因子は三文字の CFG 版）
8. [ ] 橋渡し補題を含む全体の独立監査
9. [ ] 日本語版（著者の希望があれば）

## 4. 未決事項・注意

- **代表元と最短生成語の違い（2026-11-20 発見）：** 孤立文字定理が抑えるのは、同じ型で同じ分布を持つ最短の語（代表元）である。非終端記号の最短の生成語ではない。#1 の `Rec_s` の証人集合は ω(X)（実際の生成語）を使うので、Lemma `lem:rep-witness`（ω を代表元に置き換えても #1 の完全性の証明がそのまま通る）を新しく入れた。#1 の Thm 5.2 の証明が ω について「型・共有文脈・L_{G̃}(X) への所属」以外を使っていないことを確認する必要がある（TODO）。

- 自明な型付けで Θ(\|G\|τ_G) が達成されるか：#1 の Lem 6.2 では O(\|G\|²τ) 程度しか出ない。Yoshinaka の O(\|P\|θ) は規則厚さによる。そこで (i) は下界だけを主張し、自明な型付けとの比較は注記に回す。
- 線形因子族の「表示は最小に近い」という主張を、任意の reduced CFG（BUNF）について示し直すか：要検討。
- 02-v2 のファイルは編集しない。fan-out 2 の研究結果は持ち込まない。
- #1 は審査中。引用番号は arXiv:1409.6247v5（著者提供 PDF、2026-11-20 照合済み）に合わせた。採択を前提にした記述はしない。

## 5. 独立監査（2026-11-20）

別エージェントによる監査報告は [reviews/audit_v3_2026-11-20.md](reviews/audit_v3_2026-11-20.md)。致命的な誤りはなし。Major は2件で、どちらも修正済み。

- **M1：** 主系の仮定を「λ-free BUNF」（X→YZ, X→Y, X→a）に限定した。孤立文字定理の適用範囲に合わせるため。
- **M2：** Theorem C(i) を「3文字以上」に直した。二文字版は計算機による小さな検証（q≤6, k≤3）だけで、証明はまだない。

ほかに修正したもの：
- rep-witness の文脈 χ′ を、型付き精密化での最短の道として定義し直した。
- homogeneity は G の中で直接論じる形にした。
- LG の特徴付け (iv) を任意の k で述べた。
- isolated-data (i) の論拠を直した。
- 二文字 U₁ についての τ 形の一文を追加した。
- 編集上の重複・断片を整理した。

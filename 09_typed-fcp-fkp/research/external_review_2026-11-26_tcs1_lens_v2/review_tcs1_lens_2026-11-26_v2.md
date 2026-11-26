# 09 論文を TCS #1 の Reviewer 1・2 の目で査読する（第 2 版、独立査読、2026-11-26）

- 対象：「Frames versus Exemplars: An Exponential Gap for Syntactic Categories under Finite Observation」（栗山貴之、単著、JoLLI 投稿予定）
- 版：`growupkuriyama-hub/Papers` コミット `0fbc9e4`。**行番号はすべて `09_typed-fcp-fkp/main.tex @0fbc9e4`**。手元でコンパイルし、21 頁、番号は `.aux` で確認した（Lemma 3.7＝核の縮約補題、Lemma 4.3＝捕獲、Theorem 4.4＝下界、Theorem 4.5＝定理 A の本体、Prop 4.7＝`prop:Ln-sU`、Prop 5.5＝dual の反駁、Prop 6.5＝weak FCP の非単調性）。
- 手順：main.tex を全文読み、主要な証明を一行ずつ追った → `tools/*.py` を実行 → 自前の検証コードを書いて実行（付録 B）→ ここで判断を固めた → `response_round1.tex`（E.1、R1.1–R1.37、R2.1–R2.11）と #1 の R1 原稿（main.tex）を読んだ → 最後に `research/` の過去の査読記録を読んだ。
- 原稿は編集していない。commit も push もしていない。

> **先行査読との関係。** Project には同じ日付・同じ観点の先行査読（`claude/review_tcs1_lens_2026-11-26.md`）と、それへの著者の対応記録がある。判断を固めるまではそれを読まず、数学の検証・計算・指摘の洗い出しはすべて独立に行った。§8 で両者を比べ、**本報告で初めて出た指摘**を明示した。依頼どおり対象は `0fbc9e4` だが、新しい指摘のうち `origin/main`（`496c972`）にも残っているものは §8 に印を付けた。

---

## 0. 結論（先に）

1. **主定理を崩す反例や穴はない。** Lemma 3.7、Lemma 4.1、Prop 4.2、Lemma 4.3、Theorem 4.4、Theorem 4.5、Prop 4.6、Prop 4.7、Lemma 5.1、Cor 5.2、Cor 5.4、Prop 5.5、Prop 6.1、Prop 6.3、Prop 6.4 を一行ずつ追い、確認した。Prop 6.5 は KY2017 Lemma 13 の証明の内部に依存する一歩を除いて確認した。`tools/` の 4 本は全件通過、自前の独立実装（付録 B）も全件通過。
2. **証明の小さな穴が 1 つ、過去の修正の退行が 1 つ。**
   - Prop 3.5 の証明（636–637 行）は d が段階 j > i に現れると仮定している。正例の提示は語を繰り返すとは限らない。
   - Remark 3.6 の "as above"（667–668 行）は、コミット `6de90d6` で消えた正規化の段落を指している（過去の指摘 I-05・I-08 の退行）。
3. **計算で新しく分かったこと（論文の問いに答える）。**
   - **Remark 5.3 の最後の問い「M_n のどの特性標本も因子 w\*_{n−1} を含むか」は、n = 3 で否定的に答えが出る。** 因子 w\*_2 = ⌊⌊aa⌋⌊aa⌋⌋ を含まない、Rec_{s_U} の M_3 の特性標本（11 語、‖K‖ = 152）を見つけ、独立な二つの実装で確認した（§1.5）。この問いは `origin/main` にも残っている。
   - 一方、特性標本の**最長の語**の長さの最小値は n = 2 で 9、n = 3 で 16 であり、どちらも |w\*_{n−1}| を超える。問いは「ある語の長さが 2^{Ω(n)} か」に置き換えるべきである。
   - H_n は核 {w\*_i}（型 1）、{u_i}（型 ζ）について typed strong 1-FKP を持つ（n = 2, 3, 4 で全数確認）。Theorem 4.4 の下界は O(n) 倍の範囲で最適であり、隔たりは**同じ文法の証人の長さ**の隔たりである（先行査読と同じ結論、独立に確認）。
4. **主張の範囲が定理を超える箇所。** Abstract・§5 冒頭・結論は、dual の下界まで「隔たりから」出るように書いている（Prop 5.5 は定理 A を使わない）。Abstract の "learners with membership queries" は KY2017 の Algorithms 1・2 という特定の実装についての結果を一般化しすぎている。283–284 行の "learnable" は系 5.2 の仮定 M_n ∈ C^cf_s より広い。
5. **観測器の役割。** 定理 A の下界には観測器が効いていない（Lemma 3.7 により自明に「どの観測器でも」になる）。上界で観測器が必要かは未解決（OP 8.3）。動機づけの例 1.1 でも、単数の名詞句は型なしの一つの枠 (λ, *barks*) で名指せており、観測器は要らない（142–150 行）。
6. **推薦**
   - Reviewer 1：**Major revision**。数学は正しい。自明な系・既知事実の再証明・重複・記号の衝突が多く、12〜13 頁で書ける。
   - Reviewer 2：**Major revision（現状のままなら reject 寄り）**。観測器を主題に掲げながら、定理 A で観測器が効いているのは一つの有限族の上界だけで、そこで観測器が必要かどうかも未解決。観測器そのものの結果は Theorem B の側にある。
   - 編集者の統合判定：**Major revision**。

---

## 1. 数学の検証

### 1.1 総括表

| 主張 | 行 | 判定 | 根拠・メモ |
|---|---|---|---|
| Lemma 2.1（Clark の包含） | 392–402 | 確認済み | 既知。出典の明記がない（R1-m3） |
| Lemma 2.2（到達文脈） | 414–424 | 確認済み | 民間伝承的。一行で足りる |
| Lemma 2.5（型付き細分化） | 506–527 | 確認済み | ĥ(w_i) が入っている（過去の I-03 の修正は保たれている） |
| Lemma 3.1, 3.2 | 546–580 | 確認済み | Lemma 3.2 は KY2017 式 (1) の直接の帰結（著者稿で式 (1) を確認） |
| Prop 3.5 | 618–654 | **軽微な穴** | 636–637 行（§1.2.7） |
| Remark 3.6 | 662–677 | **参照切れ** | 668 行 "as above"（§7） |
| **Lemma 3.7** | 684–705 | **確認済み** | §1.2.1 |
| Lemma 4.1 | 734–749 | 確認済み | 自前で n ≤ 3 の全出現・全置換を確認 |
| Prop 4.2(a)(b) | 751–779 | 確認済み | 自前で n ≤ 4 |
| **Lemma 4.3** | 781–798 | **確認済み** | §1.2.2。自前で n = 2, 3, 4 の全出現（空の出現を含む 22／119／1,227 組） |
| **Theorem 4.4** | 800–828 | **確認済み** | §1.2.3 |
| **Theorem 4.5** | 838–861 | **確認済み** | 非終端記号 2n、規則 6n−4（8／14／20）、ρ = 4 を自前で数えた |
| Prop 4.6 | 863–880 | 確認済み | |w\*_j| − |v| = |w\*_{j−1}| を確認。どの証明にも使われていない |
| **Prop 4.7** | 889–912 | **確認済み（一行の観察）** | §1.2.4。910 行で Section 6 の Prop 6.1(c) を前方参照 |
| Lemma 5.1 | 938–960 | 確認済み | #1 Thm 4.2 の健全性不変式から直ちに従う |
| Cor 5.2 | 962–981 | 確認済み | 2·(‖K‖²/2)·‖K‖ = ‖K‖³。ただし小さな n では非常に弱い（n = 3 で ‖K‖ ≥ 2.2。私が見つけた特性標本は ‖K‖ = 143〜152） |
| Cor 5.4 | 998–1016 | 確認済み | |Sub(D)| ≤ ‖D‖²、核の数 ≤ |Sub|^k、ρ ≤ (2r+1)‖D‖ |
| **Prop 5.5** | 1018–1051 | **確認済み** | §1.2.5 |
| Remark 5.7 | 1084–1101 | 確認済み | 非代入性の証人 (a^ℓ, db^ℓ), (λ, cb^{2i}) を手で確認。**もっと短い導出がある**（§1.6） |
| Prop 6.1(a)(b)(c) | 1110–1151 | 確認済み | |
| Cor 6.2 | 1153–1163 | 確認済み | 「on L_*」の量化が曖昧（R1-m7） |
| Prop 6.3 | 1175–1204 | 確認済み | b ≤ a ≤ 2b を m ≥ 2n で手計算 |
| Prop 6.4 | 1206–1250 | 確認済み（証明の書き方は不十分） | §1.2.6 |
| **Prop 6.5** | 1271–1407 | **確認済み（KY 依存の一歩を除く）** | §1.2.8。表は長さ 6 以下の全語で独立に確認 |

### 1.2 一行ずつの検証

#### 1.2.1 Lemma 3.7（核の縮約補題）— 確認済み
- P_0 ⊆ P_1 ⊆ P_2。K_i ⊆ cl(K_i) ⊆ K_i^{▷◁} なので Lemma 3.2 が使え、P_0^▷ = P_1^▷ = P_2^▷。
- P_1 ⊆ F_{τ(A)} は、cl(K_i) ⊆ F_{τ(A_i)} と規則の型整合性から出る。これで Lemma 3.1 の最後の主張（Y ⊆ F_μ を仮定）が使える。
- 健全性：どちらの族も前不動点なら最小前不動点 (L(G,A))_A を含むので、初期成分の和は L を含む。⊆ L はどちらも K_S ⊆ L と同値。K_S = ∅ でも K_S^▷ が全文脈になり (λ,λ) を含むので正しい。

#### 1.2.2 Lemma 4.3（捕獲）— 確認済み
- z = ⌊w\*_{n−1}u_{n−1}⌋ ∈ M_n（n ≥ 2 で u_{n−1} は標識付き）。m = 1 + |w\*_{n−1}| = 3·2^{n−1} − 1。
- x が R = z[1..m] の中にあるので、q は u_{n−1}⌋ で終わる。q' を作ると pxq' = w\*_n。
- e ∈ K_B について、Lemma 2.2 より peq ∈ M_n ⊆ L_n。末尾の u_{n−1} の出現は Lemma 4.1 により E_{n−1} 節点なので、置換して peq' ∈ L_n。左右の消去で peq' = w\*_n ⇔ e = x。
- x ∈ L(G,B) ⊆ K_B^{▷◁} から K_B^▷ ⊆ D(x) ∌ (p,q')。よって (p,q') を拒否する e ∈ K_B があり、それは x。K_B = ∅ のときは K_B^▷ が全文脈で矛盾になり、B は z の導出に現れない。

#### 1.2.3 Theorem 4.4 — 確認済み
- 節点数最小の導出木では、同じ非終端記号が一本の道に二度現れない（αβ ≠ λ ならポンプで無限、αβ = λ なら木が小さくなる）。ε 規則・単位規則があっても成り立つ。
- 位置 m と m+1 をともに含む節点（chain node）は根からの一本の道をなし、高々 |N| 個。
- j ≤ m について、j を含む最深の chain node の子で j を含むものは chain node でない。その子が m+1 を含めば区間なので m も含み、chain node になってしまう。よって子は R の中にある。
- R は高々 ρ|N| 個の断片で覆われ、各断片は終端記号（長さ 1）か Lemma 4.3 により核の語（長さ ≤ κ）。m ≤ ρ|N|max(κ,1)。型付きは Lemma 3.7 で同じ文法・同じ核に移る。
- 注意：自明な「語を並べるだけ」の文法 S → w（w ∈ M_n）と K_S = {u_n} でも ρ|N|κ ≈ 3·2^n(2n+1) であり、下界はこの自明な提示とも O(n) 倍しか違わない。下界の意味は「積が指数的」以上ではない（R2-M4 参照）。

#### 1.2.4 Prop 4.7 — 確認済み（ただし一行の観察）
- 使うのは L_n ∩ F_1 = {w\*_n}（自前で n ≤ 4）と ∅^{▷◁} = ∅（有限言語）だけ。
- 一般に、型付き核は型で均質なので、どの型付き核提示でも **κ ≥ max_{μ∈ŝ(L)} min{|w| : w ∈ L ∩ F_μ}**。これは #1 の式 (♠)（#1 main.tex 1167–1171 行）の右辺とまったく同じ量で、#1 Cor 6.6 はこの量で typed thickness を下から押さえている。885–887 行も "the isolated-fibre argument ... transferred here from yields to kernels" と認めている。

#### 1.2.5 Prop 5.5 — 確認済み
- 収束後に reset は起きない（D_j ⊆ M_n = L(G)）。極限文法に無効な候補規則は残らない（Prop 3.5 と同じく C^◁ ⊆ Sub(L\*)）。
- データ ⌈y⌉ からは c = (⌈,⌉)、⌊yy'⌋ からは標識付きの側を固定した c。{c}^◁（M_n 相対）= L(E_{n−1}) は、y' が一つの括弧対で包まれた語であることから分割が一意に決まることで従う。
- (⌊, λ, ⌋) ∈ H_t は r ≥ 2 と Sub^{≤m} の定義（459–460 行、空の w_i を許す）から。
- 型なし：候補 {(λ,λ)} → ⌊{c}{c}⌋ を落とすのは x_1 = x_2 = w\*_{n−1} だけ。型付き：({c},ζ) → ⌊({c},1)({c},ζ)⌋ は型整合的で、落とすには型 1 の子 w\*_{n−1} が要る。

#### 1.2.6 Prop 6.4 — 結論は確認済み、証明は散文
- 上界：S_+ は a^{1+p+q}b^q と a^{p+q}zb^q を生成する。{z}^{▷◁} = L_+ を、x = a^m b^n（m > n ⇔ 全 p ≥ q で m+p ≠ n+q）、x = a^m z b^n（n ≤ m ⇔ 全 p ≥ q で n+q ≤ m+p）、y を含む語（p を大きく取れば落ちる）、λ（p = q = 0 で落ちる）に分けて手で確認した。
- 1229–1236 行の "all nonnegative differences p−q preserve exactly ..." は、R1 が #1 で R1.29 として求めた「数学的な文」になっていない（R1-M6）。
- 下界：|i − j| > p の文脈が全核語を受理し、差 j−i の語を拒否する。a^{p+1} が覆われない。正しい。

#### 1.2.7 Prop 3.5 の穴
- 636–637 行「d ∈ L\* \ L(G) かつ d = t_j（j > i）ならば段階 j は reset」。d が提示の中で j ≤ i にしか現れない場合が抜けている。
- 修正：「d ∈ D_j となる j > i をとる（D_i ⊆ D_j）。D_j ⊄ L(G) = L(G_{j−1}) なので段階 j は reset」。

#### 1.2.8 Prop 6.5 — KY 依存の一歩を除いて確認済み
- (a) 表（1296–1315 行）の 12 行を、**自前の独立な所属判定**（tools/ を使わず、分解の全列挙で書いた）で、長さ 6 以下の全語（1,111,111 語 × 12 行）について確認した。不一致 0。著者のスクリプトは長さ 5 まで。
- Claim（1317–1334 行）：x_t = #cde^t a ∈ L_2、#cd²e²a ∈ L_3 で L_5 を排除する議論を確認した。
- S_1 の段落（1355–1371 行）は短いが、M^◁ ⊆ {(a#,a),(b#,b)}^◁ = L_1 ∪ L_1^@ ∪ J_0 ⊆ M^◁ と挟めば等号が出る。
- (b)：G_0 の構成、cl_1(L(G,B)) が L' 相対の閉包と一致することは確認した。ただし「KY Lemma 13 の証明は任意の CFG に適用でき、L(G_0,B)^{▷◁} は i > k_1 で Vc^id^ie^iV_0 の語を含まず、有限の W ⊆ L(G_0,B)^▷ は大きな c^id^ie^i を受理する」という一歩は KY の証明の中身に依存する。**著者稿（Kanazawa の頁の PDF）で、Lemma 13 の番号・対象（D ⇒⁺ a^{m6}$a^{l6}）・Lemma 7 経由で Ogden の補題を使うことは確認した**が、証明の内部の二つの主張そのものは本報告では**未検証**（過去の Astra 査読が検算している）。
- 「C ⊆ L(G,B)^▷ なので C は @ を含まない」という一歩が書かれていない（R1-m6）。

### 1.3 `tools/` の実行結果（そのまま実行）

| スクリプト | 結果 |
|---|---|
| `check_deletion_family.py 4` | n = 2, 3, 4 で全通過（捕獲 17／108／1,204 組、(U) 20／1,967 組、Rec(M_n) = M_n） |
| `check_reduction_identity.py 4000` | 恒等式 4,000 件、規則同値 2,230 件、反例 0（README の記載と一致） |
| `check_toy_example.py` | 例 1.1 の等式すべて一致 |
| `check_weak_fcp_s0.py` | 受理文脈 140、閉包検査 111,111、表の検査 1,333,332、反例 0 |

### 1.4 自前の検証（付録 B、`python3 -I verify_09_review.py`、約 18 秒、最後の行 `ALL OK`）

| 検査 | 結果 |
|---|---|
| Lemma 4.1（n ≤ 3 の全出現・全置換）、Prop 4.2(a)、Theorem 4.5(i)（H_n の言語、2n、6n−4、ρ = 4、型付き強 1-FCP） | n = 2, 3, 4 で成立 |
| Lemma 4.3 の全数検査（空の出現を含む） | 22／119／1,227 組、違反 0 |
| H_n が核 {w\*_i}, {u_i} で typed strong 1-FKP（§1.5） | n = 2, 3, 4 で成立。ρ|N|κ = 80／240／704、下界 5／11／23 |
| Rec_{s_U} の M_2 の特性標本 | **ただ一つ、M_2 全体**（‖K‖ = 42） |
| Rec_{s_U} の M_3 の特性標本で因子 w\*_2 を含まないもの | **存在する**（§1.5） |
| 特性標本の最長の語の最小値 | n = 2 で 9、n = 3 で 16（|w\*_{n−1}| = 4, 10） |
| Prop 6.5 の表 | 長さ 5 以下（付録の既定）で不一致 0。別に長さ 6 以下でも不一致 0 |

### 1.5 新しい計算結果：Remark 5.3 の問いへの答え（n = 3）と、見本側の上界

**(a) 特性標本は因子 w\*_{n−1} を含まなくてよい。** 992–993 行は "we do not know whether every characteristic sample of M_n must contain a factor w\*_{n−1}" と書いている。n = 3 では答えは否である。次の K ⊆ M_3（11 語、‖K‖ = 152）について L(Rec_{s_U}(K)) = M_3 であり、どの語も w\*_2 = `[[aa][aa]]` を因子に持たない（`[ ]` = ⌊ ⌋、`{ }` = ⌈ ⌉）。

```
{{{a}}}  {{[aa]}}  {[{a}{a}]}  {[{a}[aa]]}  {[[aa]{a}]}
[{{a}}[{a}{a}]]  [[{a}{a}]{{a}}]  [{{a}}[{a}[aa]]]  [[[aa]{a}]{{a}}]  [[{a}[aa]]{{a}}]  [{{a}}[[aa]{a}]]
```

確認は二つの独立な実装で行った（CYK による所属判定と、不動点による生成。#1 §4.1 の (B)(U)(L)(S) をそのまま実装）。一方、長さ L 以下の語だけからなる特性標本があるかを調べると、最小の L は n = 2 で 9、n = 3 で 16 で、|w\*_{n−1}| = 4, 10 を超える。**修正案：** 992–993 行の問いを削り、"we do not know whether every characteristic sample must contain a datum of length 2^{Ω(n)}; for n = 3 there are characteristic samples without the factor w\*_{2}" とする。この問いは `origin/main` の 1038 行にも残っている。

**(b) 見本側の上界。** H_n（Prop 4.2(b)）は、M_n 相対で、核 K_{(E_i,1)} = {w\*_i}、K_{(E_i,ζ)} = {u_i} について typed strong 1-FKP を持つ（n = 2, 3, 4 で全数確認）。手での理由：w\*_i の文脈はすべて標識を含むので {w\*_i}^{▷◁} ∩ F_1 = {w\*_i}。{u_i}^{▷◁} は w\*_n から E_i 節点を一つ抜いた無標識の文脈で w\*_i を落とし、標識付きの E_i の語はすべて残す。したがって ρ|N|max(κ,1) ≤ 4·2n·max(3·2^{n−1}−2, 2n+1)、Theorem 4.4 と O(n) 倍の範囲で一致する。830–836 行の「w\*_{n−1} ほどの長さの核が必要か分からない」の「十分」側はこれで示される。定理 A は「同じ文法 H_n の 2n 個のカテゴリーが、長さ 2n 以下の枠でも、長さ 3·2^{n−1}−2 以下の見本でも名指せ、どの文法でも見本の積はこれより大きく小さくできない」と述べるのが最も明快である。（この観察は同日の先行査読にもあり、著者は対応済みと記録している。）

### 1.6 Remark 5.7 のもっと短い導出

Remark 5.7（1084–1101 行）は、#1 Prop 9.7 の証明を二分文法から始め直し、合同的文法が 1-FKP を持つこと（Yoshinaka 2015 §6.3、Clark–Yoshinaka 2016 §6.5.3）と KY Thm 6 を組み合わせている。しかし本稿の **Lemma 5.1 だけで足りる**：L ∈ C^cf_s（λ ∉ L）なら #1 の Rec_s が特性標本 K を持ち（#1 Thm 5.3／Cor 5.4）、Lemma 5.1 の G_K は階数 2 で very weak 1-FKP を持つ。KY Thm 6 から Primal_{2,1} が L を同定する。外部の二つの文献と #1 の命題の証明の「始め直し」が不要になり、本稿の中で閉じる。（λ ∈ L の場合だけ一言添える。）

---

## 2. 査読報告：Reviewer 1（#1 の R1 の観点）

### 総評
二つの有限な提示（文脈による提示と核による提示）を比べる問題設定は自然であり、捕獲補題（Lemma 4.3）と被覆の数え上げ（Theorem 4.4）は短く正しい。#1 の §6 が L_n^−（本稿の M_n）を区別する組の相手としてしか使わなかったのに対し、M_n そのものの核の下界を、任意の文法・任意の観測器について示した点は新しい。

しかし原稿の大部分は、既知事実の証明つき再録、自明な系、同じ内容の繰り返し、#1 からの移植である。新しい中身は 6〜7 頁に収まる。主張の要約が定理を超えている箇所がいくつかあり、学習器の証明に小さな穴が、改訂の途中で切れた参照が一つある。#1 で私が指摘した型の問題（未定義の語、記号の衝突、定理文への注釈の混入、民間伝承的な事実の証明、学習器と構成手続きの混同）がほぼすべて再現している。

### 推薦：Major revision
結論が崩れる誤りはないので reject ではない。ただし (i) 定理 A を見本側の上界を含めた正しい形で述べ直すこと、(ii) 学習器についての主張の範囲を定理に合わせること、(iii) 自明な部分を削って短くすることが受理の前提である。

### Major

**R1-M1　学習器についての主張が定理を超えている**（R1.7「学習器と構成手続きの混同」、R1.10「学習可能なのは RS_h であって RS ではない」と同じ型）
- 箇所：Abstract 83–85 行、279 行（"It yields lower bounds for algorithms"）、917–919 行（"turns it into lower bounds for three learning algorithms"）、1452–1456 行、結論 1527–1529 行。
- 問題：
  1. Prop 5.5（dual）は Lemma 4.3 も Theorem 4.4 も使っていない。枠は短いのだから、隔たりから dual の下界が出るはずがない。正しく書いているのは Remark 5.6 の 1075–1079 行だけである。
  2. Abstract の "for learners with membership queries" は、KY2017 の Algorithms 1・2 を「追加の刈り込みなしで」（1075–1076 行）走らせたときの結果であり、学習問題の下界ではない。Cor 5.4 も r, k 固定の Primal_{r,k} についてだけである。
  3. 84・281 行の "set-driven" は本稿で定義されていない（#1 §2.1 の語）。
- 修正案：Abstract を "it yields exponential lower bounds on the characteristic data of the author's reconstruction Rec_s and on the data used by the primal learner of Kanazawa and Yoshinaka; a separate refutation argument gives a lower bound for their dual learner" とする。§5 冒頭と結論も同じ形に。

**R1-M2　"learnable" の範囲**（R1.10 型）
- 箇所：283–284 行・988 行 "for every typing under which M_n is learnable"。
- 問題：系 5.2 の仮定は M_n ∈ C^cf_s である。「Rec_s が M_n を再構成できる ⇔ M_n ∈ C^cf_s」という定理はない。
- 修正案："for every typing s with M_n ∈ C^cf_s"。

**R1-M3　Prop 3.5 の証明の穴と Remark 3.6 の参照切れ**（R1.24・R1.25「これは証明として受け入れられない」と同じ型）
- 箇所：636–637 行、667–668 行。
- 修正案：§1.2.7 の一文。668 行は、消えた段落の要点を一文で戻す："a nonterminal with empty context set denotes F_μ, which equals {c}^◁ ∩ F_μ for a reaching context c of the trimmed grammar (Lemma 2.2)"。

**R1-M4　定理 A の述べ方：見本側の上界がない**（R1.3「論文の位置づけ」、R1.5 型）
- 箇所：231–249 行、800–861 行、830–836 行。
- 問題：下界に対応する上界が書かれていないので、隔たりが「文法の大きさ」の隔たりなのか「証人の長さ」の隔たりなのかが読者に分からない。実際には H_n 自身が見本でも提示でき（§1.5(b)）、下界は O(n) 倍の範囲で最適である。
- 修正案：§1.5(b) の命題を Prop 4.2(c) として加え、定理 A を「同じ H_n で枠 ≤ 2n、見本 ≤ 3·2^{n−1}−2、どの文法でも ρ|N|max(κ,1) ≥ 3·2^{n−1}−1」の形に。

**R1-M5　Prop 4.7 は自明な系で、#1 の (♠)／Cor 6.6 と同じ量**（R1.22「far too trivial a corollary」、R1.32「folklore」）
- 箇所：889–912 行。関連して 245–248、263–265、1062、1443–1445 行。
- 問題：§1.2.4 のとおり、証明は「初期記号の核は L ∩ F_μ に入る」だけである。"the mark observer lengthens the exemplars"（889 行の題）は、核は型で均質という**定義**から出る効果であり、観測の効果と読ませるのは誤解を招く。
- 修正案：命題を削り、§4 の末尾に一文："Since typed kernels are type-homogeneous, κ ≥ max_μ min{|w| : w ∈ L ∩ F_μ}, the quantity (♠) of [tcs1]; for L_n under s_U this is 3·2^n − 2 [tcs1, Cor. 6.6]"。4 か所の強調も弱める。

**R1-M6　Prop 6.4 の閉包の証明が散文**（R1.29「Make the statement mathematical」）
- 箇所：1229–1236 行。
- 修正案：§1.2.6 の場合分け（3 行）に置き換える。

**R1-M7　先行研究と #1 への帰属**（R1.1・R1.3・R1.37 型）
- Lemma 5.1（938–960 行）は #1 Thm 4.2 の健全性不変式 [[x]] ⇒\* w ⟹ x ≡_L w（#1 main.tex 819–829 行）の閉包の形の言い換えである。明記する。
- Remark 5.7（1084–1101 行）は §1.6 のとおり Lemma 5.1 と #1 の特性標本の存在から一行で出る。外部文献の組み合わせより本稿内の導出を主にする。
- 統語概念束の出典（100–103 行）：Clark の ICGI 2010 と JLC 2015 だけでなく、最初に定義した Clark, "A learnable representation for syntax using residuated lattices", FG 2009, LNCS 5591, pp. 183–198 (2011) を挙げる。Lemma 2.1 の名前 "Clark's inclusion"（392 行）にも具体的な出典（命題番号）を添える。
- 989 行の "M_n ∉ C^cf_{s_0} [tcs1, Prop 6.4]"：#1 では命題文ではなく証明の末尾にある（#1 main.tex 1350–1353 行）。"[tcs1, proof of Prop. 6.4]" とする。

**R1-M8　長さ：半分で書ける**（R1.2「less than half the current length」、R1.30–R1.32、R1.34–R1.35）
21 頁 → 12〜13 頁を目安に、次を削る・縮める・移す：
- Lemma 2.1、2.2、3.1、3.2 の証明（出典と一行で足りる）。
- 定義 3.3 と定義 3.4 は同じ概念の二つの語彙である（609–610 行の "iff" が示している）。一つにする。
- Remark 3.6（662–677 行）：序論 321 行からしか参照されていない。序論の一文に。
- 679–682 行と 707–710 行は同じ文（"a typed kernel presentation is nothing but ..."）。一方を削る。
- Theorem 4.4 と Theorem 4.5(ii) は同じ主張。Theorem 4.5 は既出の命題を並べただけである。
- Prop 4.6（863–880 行）：OP 8.3 からしか参照されていない。OP の中へ。
- Prop 4.7（R1-M5）。
- 小節 5.3 は Remark 5.7 一つのためにある（R1.34「There is no need to devote an entire subsection」）。§1.6 の一行に。
- Prop 6.5 の証明（1281–1407 行、約 2.5 頁）は付録へ。
- 考察の "Observation as morphology"（1434–1448 行）は Theorem B の繰り返し。

**R1-M9　用語の氾濫と二重の語彙**（R1.8「A flood of excessive terminology」、R1.9）
- frame/context、exemplar/kernel、observer/typing、presentation/very weak property、category/nonterminal が並行して使われる。
- 本稿で定義されていない語：set-driven（84、281 行）、isolated-fibre argument（885 行）、typed thickness（886 行）、ceiling（863、866 行）、constituent（863 行）、licensing condition（79、206 行）、capture phenomenon（251 行、定義の前）。
- 修正案：数学の本文は context/kernel/typing に統一し、frame/exemplar/observer は序論の動機づけだけで使う。未定義の語は削るか定義する。

**R1-M10　記号の衝突と番号の衝突**（R1.2「inconsistent use of metavariables」、R1.33）

| 記号 | 衝突箇所（行） |
|---|---|
| m | 語 m ∈ L_n（735）／位置 m = 1+|w\*_{n−1}|（783）／指数 a^m（1177、1207） |
| B | Lemma 4.3 の非終端記号（784）／**同じ Prop 6.5 の証明の中で**、集合 B = {w : |w|_a = |w|_b}（1293）と非終端記号 B（1393） |
| M | 主役の M_n／鏡映文脈の集合 M（1355） |
| E, H, J, C, F | E_i・𝓔_i／KY 表の E（1304）。H_n・H_i・半群 𝖧・表の H。J_i・J_0・表の J。文脈集合 C・𝒞(G,A)・表の C。ファイバー F_μ・表の F・1196 行の F |
| P | 規則集合（404）／P_0, P_1, P_2（691）／P = {a^m b^n : m ≠ n}（1207） |
| k | 核の数の上限／c^k（1265）／k_1, k_2（1394） |
| L_1 | L_n の n = 1／KY の L_1（1261） |
| t | 型 t（183、319）／段階 t（1027）／x_t（1322） |

- **番号の衝突**：小節 5.3（1082 行）と Remark 5.3、小節 6.1（1167 行）と Prop 6.1 が同じ番号になる。"Section 5.3" と "Remark 5.3" の取り違えが起きやすい。定理の通し番号を節と独立にするか、小節を減らす。

**R1-M11　定理文の注釈**（R1.13「Technically unnecessary words should be removed, especially in the statements of theorems」）
- 定理 A の 241–248 行（"Without the deletion ... Cor. 6.6"）は定理の外へ。(ii) の括弧（237–238 行）も。
- Theorem 4.4 の "(of any cardinality)"（802 行）、Cor 5.2 の括弧の中の証明（965–967 行）、Cor 5.4 の "if k grows with n ..."（1006–1007 行）、Prop 4.7 の "whatever bound k ..."（893–894 行）。

### Minor
- R1-m1：338–344 行 "Here the target M_n contains words of length 2n+1; the lower bound comes from the way categories are named, not from the length of the words"。M_n は長さ 3·2^n − 3 までの語も含み、下界の証明は長さ 3·2^{n−1}+2n−1 の語 z を使う。根拠は L_n との比較（同じ長い語を含むのに線形の見本提示がある）であり、そう書く。
- R1-m2：Python の引用（207–209 行）。Language Reference §6.2.9 は「関数本体に yield 式を使うとジェネレータ関数になる」とだけ述べ、「到達しない分岐でも」は書いていない（docs.python.org で確認）。1462–1468 行の例で支える。
- R1-m3：Lemma 2.1（392 行）に出典がない（R1-M7）。
- R1-m4：Remark 5.6 の表の最終行 "data at convergence ≥ 3·2^{n−1}−2"（1065 行）。Prop 5.5 が言うのは「ある一つのデータの長さ」。行名を "length of some datum" に。
- R1-m5：M_n は有限なので KY の学習器は必ず収束する。Cor 5.4・Prop 5.5 の「収束するなら」が空でないことを一文で言う。
- R1-m6：Prop 6.5(b)（1397–1403 行）で「C ⊆ L(G,B)^▷ なので C は @ を含まない」を明記する。
- R1-m7：Cor 6.2（1154–1155 行）"converges to a correct grammar on L_*"：どの提示についての主張かを書く（「ある提示で収束すれば、型なしの学習器はすべての提示で収束する」）。
- R1-m8：Fact 2.3(c)（447–448 行）はどこからも参照されていない（Prop 6.3、6.4 は KY Prop 2 を直接引く）。削る。
- R1-m9：#1 では M_n を L_n^− と書く（#1 Prop 6.4(iv)）。姉妹論文の間で記号を揃えるか、対応を一度だけ書く。
- R1-m10：#1 との関係の説明が 333–337、347–356、983–994 行の三か所にある。一か所に。
- R1-m11：Cor 5.2 の下界は小さな n では非常に弱い（n = 3 で ‖K‖ ≥ 2.2。私が見つけた特性標本は ‖K‖ = 143〜152）。漸近的な主張であることを一言。

### Typo
- 297–298 行：「Propositions~\ref{thm:duality}, Propositions~\ref{...}」の "Propositions" の重複。ラベル `thm:duality` は Proposition を指すので `prop:` に。
- 609 行："a ($s$-typed)" → "an ($s$-typed)"。
- 319 行の F_t、183 行の s^{−1}(t)：本文の記号 F_μ に合わせる。
- 1059 行："poly data" → "polynomial data"。
- 1084 行：Remark の題の "; known" は本文で出典を書けば不要。
- 863 行：命題の題 "constituents around a ceiling"（ceiling 未定義）。

---

## 3. 査読報告：Reviewer 2（#1 の R2 の観点）

### 総評
観測器を細かくすると文脈の側は得をし、核の側は損をする、という Theorem B の見方は筋がよく、#1 で私が求めた「型付けが満たすべき条件」の問いに一歩近づいている。Prop 6.3・6.4 の U_1 での厳密性と、Prop 6.5 の weak FCP の非単調性は、観測器そのものについての結果である。

しかし題と Abstract が前面に出している定理 A について、観測器が実際に効いている部分がない。
- M_n の見本の下界は観測器なしで成り立ち、「どの観測器でも」は Lemma 3.7 から自明に出る。
- M_n の枠の上界で観測器が**必要**かどうかは未解決（OP 8.3）。
- L_n で観測器が見本を長くするのは、型付き核が型で均質という定義からの一行の帰結（Prop 4.7）。
- 動機づけの例 1.1 でも、単数の名詞句は型なしの一つの枠 (λ, *barks*) で名指せる（142–150 行）。1436–1438 行の "the plural observer replaces the agreement frame" は、例が示していることより強い。
- 結果はすべて一つの有限で人工的な族についてのもので（1478 行で著者も認めている）、#1 の R2.3 で述べた「範囲の分からない技術的強化」の懸念がそのまま当てはまる。

### 推薦：Major revision（現状のままなら reject 寄り）
次のいずれかを強く求める。(i) OP 8.3 を解く（型なしの枠も指数的、または多項式であることを示す）。(ii) 捕獲補題を族によらない形に一般化する。どちらもできなければ、題と Abstract を実際に示したこと（型なしの見本提示の指数下界と、観測器のもとでの枠の上界）に合わせる。

### Major

**R2-M1　観測器の意義と、型付けが満たすべき条件**（R2.1「the interest of the setting ... remains unclear」「the conditions a typing must satisfy could be studied」）
- 箇所：257–274 行、1420–1448 行、Theorem A(i)。
- 問題：枠の上界（Prop 4.2(b)）は、M_n = L_n ∩ ŝ_U^{−1}(ζ) であることと、i < n の文脈 (⌈^{n−i}, ⌉^{n−i}) が既に標識を含むことだけを使う。つまり観測器は、対象の認可条件そのものを符号化するように選ばれている。Theorem A(i) は Prop 4.2(a) と Prop 6.1(c) の数行の系であり、型付き文脈集合が KY2023 の拡張正則閉包に入る（Remark 3.6）ことを考えると、枠の側は「正則フィルタを使える文脈」の当然の結果に見える。
- 修正案：一般の原理として述べる。例：「Acc を 𝖲^♯ のイデアルとする。L の型付き文脈提示で、根でない各非終端記号の文脈集合のどの文脈 (u,v) も ŝ(u)·𝖲^♯·ŝ(v) ⊆ Acc を満たすなら、その提示は L ∩ ŝ^{−1}(Acc) の型付き文脈提示に移る」。これで「どの観測器なら枠が得をするか」に具体的な答えが一つ出る。

**R2-M2　適用範囲：一つの有限族**（R2.3「a technical strengthening on a class of unknown extent」）
- 箇所：781–828 行、1477–1483 行。
- 問題：Lemma 4.3 は「ただ一つの語を消す」構造と、Lemma 4.1 の置換性に依存している。消す語が複数の場合、無限の場合（すべての深さの和など）、他の族で同じ捕獲が起きるかが分からない。考察は "for the language of all depths we prove nothing"（1473–1474 行）とする。
- 修正案：Lemma 4.3 を族によらない形で述べる。例：「L の語 w と、w のある構成素を置き換えた w' ∉ L について、置き換えの外にある長い因子 R の中の構成素は核に入る」。Theorem 4.4 をその系にし、無限の場合に何が言えるかを一段落で述べる。

**R2-M3　どの証明にも使われない成分**（R2.2「the components are then read by no proof」、R2.6「is never used」）
- Prop 4.6（863–880 行）：OP 8.3 からのみ。
- Remark 3.6（662–677 行）：序論 321 行からのみ。
- Fact 2.3(c)（447–448 行）：参照なし。
- 定義 3.4（596–610 行）：定義 3.3 と同じ内容。
- 型付き dual 学習器：Prop 5.5 の型付きの場合でしか使われず、議論は型なしの場合の変形。
- 修正案：削除、または OP・脚注へ。

**R2-M4　大きさの尺度を揃える**（R2.3 型）
- 箇所：596–608 行、800–807 行、Remark 5.6 の表。
- 問題：枠の側は |N|、ρ、文脈の長さを別々に、見本の側は積 ρ|N|max(κ,1) で評価している。さらに §1.2.3 のとおり、自明な「語の列挙」の提示も積は 3·2^n(2n+1) 程度で、下界はそれと O(n) 倍しか違わない。読者は「見本はどうやっても列挙と大差ない」のか「列挙よりはよいがなお指数」なのかを知りたい。
- 修正案：枠の側も ρ|N|ℓ（H_n で 16n²）で書き、表を同じ尺度に揃える。§1.5(b) の上界と合わせて「16n² 対 Θ̃(2^n)」と一行で言う。

**R2-M5　使う前の参照と繰り返し**（R2.4「objects are regularly used before they are introduced」「several results restate what their proofs have just established」）
- 序論の定理 A（227、247–248 行）が Lemma 3.7、Prop 4.7、#1 Cor 6.6 を前方参照する。"What the observer buys"（257–274 行）は Cor 6.2、Remark 5.7、Prop 5.5 を使う。
- Prop 3.5 の証明（653 行）が後ろの Lemma 3.7 を使う。Prop 4.7 の証明（908–911 行）が Section 6 の Prop 6.1(c) を使う。
- 679–682 行と 707–710 行の重複、882–887 行の序論の繰り返し、1434–1448 行の Theorem B の繰り返し。
- 修正案：序論の定理 A は (i)(ii) だけを述べ、説明は定理の外に一度だけ。Lemma 3.7 を Prop 3.5 の前へ。Prop 4.7 は R1-M5 のとおり一文にすれば前方参照も消える。

**R2-M6　長い証明と再録は付録へ**（R2.11「could be condensed or given in appendix」）
- Prop 6.5 の証明（1281–1407 行、約 2.5 頁）。論文の主題から外れている。
- §2 の学習器の再録（451–477 行）。§5 でしか使わない。

**R2-M7　例の一貫性：Python と例 1.1**（R2.7「Example 4.3 is not in SSBNF」と同じ「例が主張に合っていない」型）
- 箇所：206–229 行、1458–1475 行、1434–1438 行。
- 問題：
  - 序論は Python のジェネレータを「大域的な認可条件のなじみ深い例」（206 行）とし、"admission"（220–221 行）と書く。考察は「分類は関数についてのもので、構文的な妥当性ではない」（1469–1470 行）とする。M_n は文法性の条件として導入されているので、例と矛盾する。
  - 「すべての道がちょうど n 個の構成子を通る本体」は Python として極めて人工的で、M_n の決定的な性質（除かれる構造がただ一つ）は Python には一般にない（ジェネレータでない関数は無数にある）。
  - JoLLI の読者には例 1.1（数の一致）と M_n の橋渡しのほうが重要だが、それがない。しかも例 1.1 は観測器の必要性を示していない（総評）。
- 修正案：Python は考察に戻すか削除する。序論では例 1.1 の数の素性を一般化した「どこかに一つ標識があれば認可される」構文で M_n を導入し、観測器が**必要になる**例（型なしの短い枠では名指せないカテゴリー）を一つ示す。

### Minor
- R2-m1：題。"under Finite Observation" は観測器が隔たりを生むように読める。下界が観測器によらないことが分かる題か副題に。
- R2-m2：1516–1520 行の番号のない "Further questions" は OP にまとめるか削る。
- R2-m3：JoLLI（Springer）の書式。"Statements and Declarations" の下に Funding／Competing interests／Data availability／生成 AI をまとめる。**Funding の記載がない**。データの URL（1542 行）は `tree/main` でコミットを固定していない。投稿時は commit permalink か DOI に。
- R2-m4：査読用に英語版にも行番号（`lineno`）を付ける（日本語版には付いている）。
- R2-m5：KY2017 の番号は LATA 版（Springer）を引いているが、照合されたのは著者稿である。刊行版で番号が一致するかを一度確認する。

### Typo
- 1065 行の表の行名（R1-m4）。863 行の "ceiling"。

---

## 4. #1 との関係：サラミ・スライスの評価

### 4.1 依存の大きさ

| 09 の項目 | #1（arXiv:1409.6247v5 = R1 原稿の番号） | 判定 |
|---|---|---|
| 族 L_n、G_n、w\*_i、u_i、s_U | §6（#1 main.tex 1244–1271 行）、Prop 6.4(ii) の u_i | 同一（09 も 333–335 行で認めている） |
| M_n | L_n^−（Prop 6.4(iv)）。s_U で代入可能、s_0 で不可能（証明の末尾 1350–1353 行） | 同一の対象、記号だけ違う |
| Rec_s、C^cf_s | §4.1、Def 2.1 | 再録。定義が一致することを確認した |
| **Prop 4.7** | **Cor 6.6 と (♠)** | **論法は同一**（§4.2） |
| 表 5.6 の L_n の列 | Prop 6.4(ii)(iii)、Cor 6.6 | 結論が同じ（多項式 対 指数） |
| Lemma 5.1 | Thm 4.2 の健全性不変式 | 閉包の形への言い換え |
| Remark 5.7 | Prop 9.7 ＋ Yoshinaka 2015 §6.3 ＋ KY Thm 6 | 既知（09 も "known" と明記）。§1.6 のとおり Lemma 5.1 から一行 |
| **Lemma 4.3、Theorem 4.4** | なし（#1 に FCP/FKP・KY2017 への言及はない。grep で確認） | **新規** |
| Cor 5.2（M_n の正例データの下界） | なし（#1 Prop 6.4(iii)(iv) の対象は L_n） | 新規。ただし弱い（‖K‖ ≥ 立方根） |
| Cor 5.4、Prop 5.5、Theorem B、Prop 6.3–6.5 | なし（KY2017 の系統） | 新規 |

### 4.2 #1 Cor 6.6 と Prop 4.7
- #1 Cor 6.6：L_n の縮約 BUNF 文法はすべて τ^typ_{s_U}(G) ≥ 3·2^n − 2。根拠は式 (♠) τ^typ ≥ max_μ min{|w| : w ∈ L ∩ F_μ} と、型 1 のファイバー L_n ∩ F_1 = {w\*_n}。
- 09 Prop 4.7：s_U-型付きの核提示はすべて K_S = {w\*_n} の初期記号を持つ。根拠は同じファイバー {w\*_n} と、型付き核は均質（K_S ⊆ L ∩ F_{τ(S)}）であること。
- 両者は「孤立したファイバーのただ一つの語が長い」という同じ事実の言い換えで、09 で増えたのは K_S ≠ ∅（∅^{▷◁} = ∅）の一行だけ。885–887 行は正直に書いているが、番号付きの命題にし、序論（245–248、263–265 行）・表（1062 行）・考察（1443–1445 行）で「観測器が見本を長くする」と強調するのは、#1 の結果を新しい結果に見せる効果を持つ。

### 4.3 評価
- **焼き直しは Prop 4.7（と表の L_n の列）に限られ、量は小さい。** 中心（Lemma 4.3、Theorem 4.4、Prop 5.5、Theorem B の厳密性、Prop 6.5）は #1 にない。**サラミ・スライスとまでは言えない。**
- **ただし Cor 5.2 は #1 に入りうる。** Cor 5.2 は Rec_s についての結果で、Lemma 5.1 のとおり Rec_s(K) の非終端記号 [[y]] の核は {y} なので、捕獲補題は「R の中の節点のラベルは自分の収量そのもの」と読める。この形なら FCP/FKP の語彙なしに半頁で証明でき、#1 の Prop 6.4 の (v) として置ける。#1 の R1・R2 が両方を読めば、「#1 の Section 6 の続きを別論文に分けた」と受け取る可能性がある。
- **対策**
  1. Prop 4.7 を一文の注意に格下げし、#1 の (♠)／Cor 6.6 を出典にする。
  2. Lemma 5.1 に #1 Thm 4.2 を明記する。
  3. 09 を「KY2017 の系統（文脈 対 核）の論文で、例として #1 の族を使う」と位置づける。序論の "Relation to the fixed-typing theory"（347–356 行）は一段落に縮める。
  4. Cor 5.2 は本稿に残してよいが、#1 の審査で同じ問い（M_n の特性データ）が出たら、#1 には本稿を引用して答える、という分担を決めておく。
- **#1 の審査との連動。** 09 は #1 を arXiv:1409.6247v5（2026-10-23 付、arXiv で確認）の番号で引いており、R1 原稿の番号（Def 2.1、Lemma 2.2、Prop 3.1、§4.1、Prop 6.4、Cor 6.6、Prop 9.7）と一致することを確認した。#1 の次の改訂で番号が変われば、版を明示し直す必要がある。

---

## 5. 主張の範囲

| 箇所 | 主張 | 定理が実際に示す範囲 | 判定 |
|---|---|---|---|
| 題 60–61 | "An Exponential Gap ... under Finite Observation" | 見本の下界は観測器なしで成り立つ。枠の上界は s_U のもと。型なしの枠は未解決 | **やや超える**（R2-m1） |
| Abstract 81–83 | 標識の観測器のもとで枠は 2n 以下、見本は「どの観測器でも」指数 | 正しい | 確認済み |
| Abstract 83–85 | 隔たりが Rec_s と「所属質問を用いる学習器」の指数下界を与える | dual は隔たりから出ない。学習器は KY2017 の Algorithms 1・2（刈り込みなし、r, k 固定）に限る | **超える**（R1-M1） |
| 序論 206、220–221 | Python のジェネレータは大域的な認可条件、"admission" | 考察 1469–1470 行は「妥当性でなく分類」 | **自己矛盾**（R2-M7） |
| 序論 212–216 | 下界は制限した断片についてで、Python 全体には主張しない | 正しく限定 | 確認済み |
| 序論 283–284 | "for every typing under which M_n is learnable" | 系 5.2 は M_n ∈ C^cf_s を仮定 | **超える**（R1-M2） |
| 序論 286–292 | primal は r, k 固定で 2^{Ω(n)}、dual は r ≥ 2, k ≥ 1 | Cor 5.4、Prop 5.5 と一致 | 確認済み |
| 序論 341–344 | 下界は名指し方から来て、語の長さからではない | 根拠は L_n との比較であって、M_n の語が短いことではない | **やや不正確**（R1-m1） |
| 考察 1436–1438 | 例 1.1 で複数の観測器が一致の枠に取って代わる | 例 1.1 では型なしの枠 (λ, *barks*) で足りる | **超える**（R2 総評） |
| 結論 1524–1529 | 隔たりが Rec_s と「分布学習器」のデータを押さえる | dual は別の議論 | **超える**（R1-M1） |

三つの一般化について：
- **Python**：Abstract からは消えている。序論・考察でも深さを固定した断片に限定されている（コミット 8944043）。残る問題は「認可条件」と「分類」の矛盾、§6.2.9 に書かれていない「到達しない分岐」の典拠、M_n の「除かれる構造がただ一つ」が Python にないことの三点。
- **有限観測**：本文の "What the observer buys"（257–274 行）は正確で誠実である。題、Abstract の最初の二文、考察の "Observation as morphology" が、それより強い。
- **学習可能性**：序論の箇条書き（281–291 行）は正確。Abstract、§5 冒頭（917–919 行）、結論（1527–1529 行）で範囲が広がる。

---

## 6. 正確さ：英日の食い違いと書誌

### 6.1 英語版と日本語版
- ラベル 46 個の種類と順序が一致した。証明環境の数も一致（23 個）。
- 数式（インライン・ディスプレイ・align・gather）をすべて取り出し、空白を除いて多重集合で比べた。違いは句読点・表の見出しの言語・日本語の語順による式の切れ目だけで、**数学的内容の食い違いは見つからなかった**。定理 A、定理 B、Prop 6.3、Prop 6.5 は目視でも照合した。
- 書式の違い：日本語版には行番号がある。英語版の定理 B の見出し（297–298 行）の "Propositions" の重複は、日本語版では起きていない。

### 6.2 引用文献の書誌（自分で外部ページを開いたものだけ「確認済み」）

| 文献 | 判定 | 確認先 |
|---|---|---|
| Clark 2010（ICGI 2010, LNAI 6339, pp. 38–51） | 確認済み | Leiß 2014 の参考文献（Crossref） |
| Clark 2015（JLC, online 2013） | 雑誌名・年は確認済み。**巻号・頁 25(5):1203–1229 は未検証** | KCL の頁、Clark の頁（Advance Access 2013-08-09）、MaRDI |
| Clark–Eyraud 2007（JMLR 8:1725–1745） | 確認済み。Example 2 は §2.1 にあり、内容も記述どおり | JMLR の PDF |
| Clark–Yoshinaka 2016（Topics in GI, pp. 143–172） | 未検証 | 著者の他論文の書誌と一致するだけ |
| Coste–Nicolas 2019（PMLR 93, pp. 155–168） | 確認済み。巻名は "Proceedings of The 14th ICGI 2018"（会議は 2018 年） | PMLR |
| Harris 1954、Kanazawa 1998、Ogden 1968 | 未検証（周知の書誌） | — |
| KY2017（LATA, LNCS 10168, pp. 77–88） | 題・著者・頁 77–88 は確認済み（東北大の業績頁）。巻番号 10168 は未検証。**番号（Prop 2(i)(ii)、Prop 10、Thms 3–6、Lemmas 8, 12, 13、Thm 14、Algorithms 1・2、式 (1)）は著者稿で確認**。刊行版との一致は未検証。Springer の頁はレート制限で開けなかった | Kanazawa の頁の PDF、東北大 |
| KY2023（PMLR 217, pp. 8–22） | 確認済み | PMLR |
| Kuriyama #1（arXiv:1409.6247v5） | 確認済み（v5 は 2026-10-23 付）。題も一致 | arXiv |
| Leiß 2014（FG 2014, LNCS 8612, pp. 121–137） | 確認済み | Crossref |
| Python 3.12 Reference §6.2.9 | 節番号と記述は確認済み。「到達しない分岐」は書かれていない（R1-m2） | docs.python.org |
| Yoshinaka 2011（DLT, LNCS 6795, pp. 429–440） | 確認済み | 東北大の業績頁、dblp |
| Yoshinaka 2015（MoL 14, ACL, pp. 87–98） | 確認済み。題は単数 "General Perspective ..."（本稿どおり）。DOI 10.3115/v1/W15-2308 を足すとよい | ACL Anthology |
| （追加を推奨）Clark, FG 2009, LNCS 5591, pp. 183–198 (2011) | 書誌は Leiß 2014 の参考文献（Crossref）で確認 | R1-M7 |

---

## 7. 過去の査読記録との照合（退行の確認）

| 過去の指摘 | 当時の対応 | 現版（0fbc9e4） |
|---|---|---|
| I-03 Lemma 2.5 の型の積 | ĥ(w_i) を追加 | **保たれている**（513 行） |
| I-04 L_K の strong 1-FKP | S_+, S_− に分割 | 保たれている（1214–1236 行）。閉包の証明は散文（R1-M6） |
| I-05 学習器の正規化（空の C, K） | Prop 3.5 の証明に段落を追加 | **コミット `6de90d6`（2026-11-25）で段落ごと削除**。逆方向を使わなくなったので削除自体は妥当 |
| I-08 EXREG の対応 | Remark 3.6 を具体化 | 残っているが、**668 行の "as above" が I-05 の消えた段落を指して参照切れ（退行）**。`git log -S` で確認 |
| I-06 H_n の添字 | 存在する子だけ | 保たれている（761–763 行） |
| I-07 尺度の区別 | 表の注記 | 保たれている（1069–1074 行） |
| I-09 Prop 4.6 | 本文に追加 | 残っているが、どの証明にも使われない（R2-M3） |
| I-10 計算の再現性 | ソート済みの列から選択 | 保たれている（2,230 件が再現） |
| I-11 Yoshinaka 2015 の題 | 単数に | 保たれている |
| Astra 3.1 L_n の s_U の行 | Prop 4.7 を追加し表を分割 | 保たれている。ただし Prop 4.7 は自明な系として扱うべき（R1-M5） |
| Astra 3.2 s_0 版の weak 2-FCP | 6.5(a) に追加 | 保たれている（1373–1384 行） |
| Astra：Prop 3.5 の reset の場合分け | 見送り | 証明の形は変わったが、「d = t_j, j > i」という形で穴が残っている（R1-M3） |
| Astra：Funding | 「著者に確認」 | **未対応**（R2-m3） |
| Astra：データの URL をコミット固定 | 「投稿時に差し替え」 | **未対応**（1542 行） |

過去の二回の外部査読（ChatGPT 11-24、Astra 11-25）の数学的な判定（主定理は正しい）と、私の検証は一致した。

---

## 8. 同日の先行査読（Project の `claude/review_tcs1_lens_2026-11-26.md`）との比較

判断を固めたあとで読んだ。数学の判定、Prop 3.5 の穴、Remark 3.6 の退行、見本側の上界、Prop 4.7 と (♠)、dual の帰属、"learnable" の範囲、Python の矛盾、長さ・用語・記号の問題では、**独立に同じ結論になった**。

**本報告で初めて出た指摘・確認**（★ は `origin/main` = `496c972` にも残っているもの）

| 指摘 | 本報告の箇所 |
|---|---|
| ★ Remark 5.3 の問い「特性標本は因子 w\*_{n−1} を含むか」は n = 3 で否定的に解決。問いを「長さ 2^{Ω(n)} の語が要るか」に置き換えるべき | §1.5(a) |
| n = 2 の特性標本は M_2 全体ただ一つ。特性標本の最長の語の最小値は n = 2, 3 で 9, 16 | §1.4 |
| ★ Remark 5.7 は Lemma 5.1 と #1 の特性標本の存在から一行で出る（外部文献の組み合わせが不要） | §1.6、R1-M7 |
| ★ Fact 2.3(c) はどこからも参照されていない | R1-m8 |
| ★ Prop 6.5 の証明の中で B が二つの意味（1293／1393 行）、M が M_n と衝突（1355 行） | R1-M10 |
| 小節 5.3 と Remark 5.3、小節 6.1 と Prop 6.1 の番号の衝突 | R1-M10 |
| 統語概念束の最初の出典 Clark FG 2009（LNCS 5591）、Lemma 2.1 の出典 | R1-M7 |
| 例 1.1 でも観測器は不要（型なしの枠 (λ, *barks*)）、1436–1438 行の主張は強すぎる | R2 総評、§5 |
| Abstract の "learners with membership queries" は特定の実装（刈り込みなし）の結果の一般化 | R1-M1 |
| Theorem A(i) は Prop 4.2(a) と Prop 6.1(c) の数行の系で、Remark 3.6 から枠の側は EXREG の当然の結果に見える | R2-M1 |
| 自明な列挙の提示でも積は 3·2^n(2n+1) 程度で、下界はそれと O(n) 倍しか違わない | §1.2.3、R2-M4 |
| Cor 5.2 は FCP/FKP の語彙なしに #1 の Prop 6.4(v) として書ける（サラミの危険の具体的な形） | §4.3 |
| Prop 6.5 の表を独立な実装で長さ 6 以下まで確認（著者のスクリプトは 5 まで） | §1.2.8 |
| KY2017 の番号を著者稿で確認（先行査読では未検証） | §6.2 |
| Python の M_n の決定的な性質（除かれる構造がただ一つ）が Python にない | R2-M7 |
| Cor 6.2 の量化の曖昧さ | R1-m7 |

**先行査読と判断が分かれた点**
- Clark 2015 の巻号・頁：先行査読は「確認済み」とするが、私は雑誌名と年までしか確認できなかったので「未検証」とした。
- R2 の推薦の強さは同じ（Major、現状なら reject 寄り）。ただし私は、Theorem B（U_1 での厳密性、weak FCP の非単調性）は観測器そのものの結果であると評価し、総評でそう書いた（先行査読の「観測器が実際に効いている結果が一つもない」より限定的）。

---

## 9. 編集者向けの統合判定

**判定：Major revision。**

二人の査読者は、数学が正しいことで一致している。主要な証明は一行ずつ確認され、著者の検査と独立な検査がすべて通過した。R1 は、学習器についての主張の範囲、自明な系と既知事実の再証明、重複、記号、長さを問題にしている。R2 は、観測器を主題に掲げながら定理 A で観測器が効いている部分がないこと、結果が一つの有限族に限られることを問題にしている。

R2 の懸念の大部分は、見本側の上界を加えて定理 A を「同じ文法での証人の長さの隔たり」として述べ直し、題と Abstract を実際の内容に合わせ、観測器が効く結果（Theorem B）を前に出せば和らぐ。OP 8.3 を解くか捕獲補題を一般化できれば、評価は大きく上がる。

### 投稿前に直すべき項目の優先順位表

| 順位 | 項目 | 行 | 指摘 | 手間 |
|---|---|---|---|---|
| **P0-1** | Prop 3.5 の証明の穴（d ∈ D_j となる j > i をとる） | 636–637 | R1-M3 | 一文 |
| **P0-2** | Remark 3.6 の "as above" の参照切れ（退行） | 667–668 | R1-M3、§7 | 一文 |
| **P0-3** | dual の下界を「隔たりから」と書かない。"learners with membership queries" を KY2017 の primal/dual に限る。"set-driven" を定義するか削る | 83–85, 279, 917–919, 1527–1529 | R1-M1 | 数文 |
| **P0-4** | "learnable" を M_n ∈ C^cf_s に | 283–284, 988 | R1-M2 | 一語 |
| **P0-5** | Remark 5.3 の問いを n = 3 の反例に合わせて差し替える | 992–993 | §1.5(a) | 一文 |
| **P0-6** | 見本側の上界（H_n の typed strong 1-FKP）を加え、定理 A を述べ直す | 231–249, 830–861 | R1-M4, R2-M4 | 命題一つ |
| **P0-7** | Prop 4.7 を一文の注意に格下げし、#1 の (♠)／Cor 6.6 を出典に | 889–912 ほか 4 か所 | R1-M5, §4 | 削除が中心 |
| **P0-8** | Python：「認可条件」と「分類」の矛盾を解消、§6.2.9 に書かれていない典拠を直す | 206–229, 1458–1475 | R2-M7, R1-m2 | 段落の移動 |
| P1-1 | Prop 6.4 の閉包を場合分けの証明に | 1229–1236 | R1-M6 | 小 |
| P1-2 | 定理文の注釈を外へ | 237–248, 802, 893–894, 965–967, 1006–1007 | R1-M11 | 小 |
| P1-3 | 帰属：Lemma 5.1 に #1 Thm 4.2、Remark 5.7 を Lemma 5.1 から導く、Clark FG 2009、Lemma 2.1 の出典、"proof of Prop. 6.4" | 100–103, 392, 938–960, 989, 1084–1101 | R1-M7 | 小 |
| P1-4 | 例 1.1 と考察 1436–1438 行：観測器が要る例を示すか、主張を弱める | 129–194, 1434–1438 | R2 総評, R2-M7 | 小〜中 |
| P1-5 | 題と Abstract を実際の内容に合わせる | 60–61, 70–90 | R2-m1, §5 | 小 |
| P1-6 | 使われない成分を削る・移す（Prop 4.6、Remark 3.6、Fact 2.3(c)、定義 3.4、型付き dual 学習器） | 447–448, 596–677, 863–880 | R2-M3, R1-m8 | 中 |
| P1-7 | 記号・番号の衝突を解消し、用語を一本化 | 全体（特に 1293/1393, 1355, 1082, 1167） | R1-M9, R1-M10 | 中 |
| P1-8 | 前方参照の解消（Lemma 3.7 を Prop 3.5 の前へ等）、重複の削除 | 653, 679–682/707–710, 908–911 | R2-M5 | 小 |
| P1-9 | Prop 6.5 の証明と学習器の再録を付録・§5 へ | 451–477, 1281–1407 | R2-M6 | 中 |
| P1-10 | 全体を 12〜13 頁に | 全体 | R1-M8 | 大 |
| P2-1 | 枠の上界の一般原理（イデアルとの交わり） | 751–779 | R2-M1 | 中（任意だが評価が上がる） |
| P2-2 | 捕獲補題の一般化、または OP 8.3 | 781–828, 1509–1514 | R2-M2 | 大（研究） |
| P2-3 | JoLLI の書式（Statements and Declarations、Funding、commit permalink、英語版の行番号）、KY2017 刊行版の番号確認 | 1535–1556 | R2-m3〜m5 | 小 |
| P2-4 | Minor・Typo の残り | — | R1-m*, Typo | 小 |

---

## 付録 A：英語版の査読報告

### Report of Reviewer 1

**Summary.** The paper compares context-based (frame) and kernel-based (exemplar) finite presentations of context-free grammars in the presence of a fixed finite-semigroup typing. For the one-word deletion M_n = L_n \ {w\*_n} of the bracketed doubling family, an s_U-typed grammar with 2n nonterminals has the typed strong 1-FCP with contexts of length ≤ 2n, whereas every CFG for M_n with an SPP (K_A^{▷◁}) satisfies ρ|N|max(κ,1) ≥ 3·2^{n−1}−1, under every typing. I checked Lemma 3.7, Lemma 4.3, Theorem 4.4, Theorem 4.5, Prop 4.7 and Prop 5.5 line by line; they are correct. The author's finite checks and my own independent implementation (n ≤ 4) all pass. The capture lemma with the covering count is a neat argument. Most of the remaining text, however, consists of known facts reproved, trivial corollaries, repetitions and material transplanted from the author's earlier paper, and several summary sentences claim more than the theorems give.

**Recommendation: major revision.**

**Major comments.**
1. *Learning claims.* Prop 5.5 (dual learner) uses neither Lemma 4.3 nor Theorem 4.4, so the abstract (ll. 83–85), §5 (ll. 917–919) and the conclusion (ll. 1527–1529) should not present it as a consequence of the gap. "Learners with membership queries" should read "the primal and dual learners of Kanazawa and Yoshinaka (2017)": the results concern Algorithms 1–2 without pruning, not the learning problem. "Set-driven" is not defined in this paper.
2. *"Learnable".* L. 284 should say "every typing s with M_n ∈ C^cf_s", which is what Cor 5.2 assumes.
3. *A proof gap and a dangling reference.* The proof of Prop 3.5 (ll. 636–637) assumes d occurs at a stage j > i; take any j > i with d ∈ D_j instead. "As above" in Remark 3.6 (l. 668) refers to a paragraph deleted in a later revision.
4. *Missing upper bound.* H_n itself has the typed strong 1-FKP with kernels {w\*_i} (type 1) and {u_i} (type ζ), so Theorem 4.4 is tight up to a factor O(n), and the gap is one of witness length on the same grammar. State Theorem A in that form.
5. *Prop 4.7* is the observation κ ≥ max_μ min{|w| : w ∈ L ∩ F_μ}, i.e. the quantity (♠) of [tcs1], whose Cor 6.6 is the same statement for typed thickness. Reduce it to a sentence and stop presenting it as an effect of observation.
6. *Prop 6.4.* The closure computation (ll. 1229–1236) is prose; give the three-line case analysis.
7. *Attribution.* Lemma 5.1 is the closure form of the soundness invariant of [tcs1, Thm 4.2]; Remark 5.7 follows in one line from Lemma 5.1 and the existence of characteristic samples in [tcs1]; cite Clark's FG 2009 paper for the syntactic concept lattice and give a source for Lemma 2.1; the fact M_n ∉ C^cf_{s_0} is in the proof of [tcs1, Prop 6.4].
8. *Length.* The paper can be written in 12–13 pages (standard lemmas cited, Definitions 3.3/3.4 merged, Remark 3.6 and Prop 4.6 moved, Theorem 4.4/4.5(ii) merged, the subsection for Remark 5.7 removed, the proof of Prop 6.5 moved to an appendix, the repetitions in §7 cut).
9. *Terminology.* Two parallel vocabularies are used; "set-driven", "isolated-fibre argument", "typed thickness", "ceiling", "constituent", "licensing condition" are undefined.
10. *Symbols and numbering.* m, B (twice inside the proof of Prop 6.5), M, E, H, J, C, F, P, k, L_1, t have several meanings; Section 5.3 vs Remark 5.3 and Section 6.1 vs Proposition 6.1 collide.
11. *Theorem statements.* Remove commentary from Theorem A (ll. 237–248), Theorem 4.4 ("of any cardinality"), Cor 5.2, Cor 5.4 and Prop 4.7.

**Minor comments.** The question at the end of Remark 5.3 has a negative answer for n = 3: there is a characteristic sample of M_3 for Rec_{s_U} (11 words) without the factor w\*_2; ask instead whether some datum must have length 2^{Ω(n)}. The sentence on word length (ll. 341–344) should rest on the comparison with L_n. §6.2.9 of the Python reference does not mention unreachable branches. Rename the last row of the table in Remark 5.6. Say that convergence of the KY learners on the finite M_n is automatic. In Prop 6.5(b), state that C ⊆ L(G,B)^▷ and hence contains no @. Fact 2.3(c) is never used. Clarify the quantification in Cor 6.2. Typos at ll. 297–298, 319, 609, 1059, 1084, 863.

### Report of Reviewer 2

**Summary.** Theorem B — refinement helps contexts and hurts kernels, strict at U_1, with the weak FCP non-monotone — is a genuine result about observation and partly answers the question I raised on [tcs1] about the conditions a typing should satisfy. Theorem A, however, which the title and abstract put forward, contains no part where the observer actually matters: the kernel lower bound for M_n holds with no observer (and "under every observer" follows trivially from Lemma 3.7); whether the context upper bound needs the observer is open (OP 8.3); the effect on L_n is definitional (Prop 4.7); and even the motivating Example 1.1 names the singular noun phrases by the untyped frame (λ, *barks*). Everything concerns one finite, artificial family.

**Recommendation: major revision (leaning towards reject in the present form).** Settle OP 8.3, or generalize the capture lemma beyond this family, or align the title and abstract with what is proved.

**Major comments.**
1. *Role of the observer.* The context upper bound only uses M_n = L_n ∩ ŝ_U^{−1}(ζ) and that every non-root context already contains a mark; Theorem A(i) is a few-line corollary of Prop 4.2(a) and Prop 6.1(c). State the general principle (intersection with an ideal of 𝖲^♯) and thereby say which observers help contexts.
2. *Scope.* Formulate the capture lemma for general languages and say what survives for infinite unions.
3. *Unused components.* Prop 4.6, Remark 3.6, Fact 2.3(c), Definition 3.4, the typed dual learner.
4. *Measure.* Compare both sides by the same measure (ρ|N|ℓ = 16n² against ρ|N|max(κ,1) = Θ̃(2^n)); note that even the trivial listing presentation is within O(n) of the lower bound.
5. *Forward references and repetition.* Theorem A in the introduction cites Lemma 3.7, Prop 4.7 and [tcs1, Cor 6.6]; Prop 3.5 uses the later Lemma 3.7; Prop 4.7 uses Prop 6.1(c); ll. 679–682 and 707–710 repeat each other.
6. *Appendix.* Move the 2.5-page proof of Prop 6.5 and the recap of the KY learners out of the main line.
7. *Examples.* The Python generator is called a licensing condition (l. 206, "admission", ll. 220–221) but a classification of functions in the discussion (ll. 1469–1470); its exact-depth fragment is artificial, and the defining feature of M_n (a single excluded structure) has no Python counterpart. For JoLLI, connect M_n to Example 1.1 and give an example where the observer is actually needed.

**Minor comments.** Title; numbered open problems instead of "Further questions"; Springer "Statements and Declarations" with a funding statement and a commit permalink for the scripts; line numbers in the English manuscript; confirm KY2017 numbering against the published version.

---

## 付録 B：自前の検証コード（`verify_09_review.py`）

実行：`python3 -I verify_09_review.py [N]`（N は Prop 6.5 の表の検査の最大語長、既定 5。N = 6 は約 3 分）。Python 3、標準ライブラリのみ。`tools/` は import していない。出力：

```
(1) n=2: Lemma4.1/Prop4.2/Thm4.5(i)/capture(22 pairs) ok=True
(2) n=2: H_n typed strong 1-FKP with kernels w*_i,u_i: True; rho|N|kappa=80 vs lower bound 5
(1) n=3: Lemma4.1/Prop4.2/Thm4.5(i)/capture(119 pairs) ok=True
(2) n=3: H_n typed strong 1-FKP with kernels w*_i,u_i: True; rho|N|kappa=240 vs lower bound 11
(1) n=4: Lemma4.1/Prop4.2/Thm4.5(i)/capture(1227 pairs) ok=True
(2) n=4: H_n typed strong 1-FKP with kernels w*_i,u_i: True; rho|N|kappa=704 vs lower bound 23
(3) n=2: characteristic samples for Rec_sU: 1; = M_2 itself: True
(3) n=3: characteristic K, |K|=11, ||K||=152, contains factor w*_2: False
    K = ['{{{a}}}', '{{[aa]}}', '{[{a}{a}]}', '{[{a}[aa]]}', '{[[aa]{a}]}', '[{{a}}[{a}{a}]]', '[[{a}{a}]{{a}}]', '[{{a}}[{a}[aa]]]', '[[[aa]{a}]{{a}}]', '[[{a}[aa]]{{a}}]', '[{{a}}[[aa]{a}]]']
(3) n=2: minimal max-datum length over characteristic samples = 9 (|w*_(n-1)|=4)
(3) n=3: minimal max-datum length over characteristic samples = 16 (|w*_(n-1)|=10)
(4) Prop 6.5 table: 111111 words x 12 rows, mismatches=0
ALL OK
```

（長さ 6 以下の Prop 6.5 の表の検査は、同じ判定関数を使う別のスクリプトで 1,111,111 語 × 12 行、不一致 0。M_3 の反例は、CYK による判定と不動点による生成の二つの実装で確認した。英日の数式比較は、数式を空白なしで取り出して多重集合で比べる短いスクリプトで行った。）

```python
#!/usr/bin/env python3
"""Independent checks for the TCS#1-lens review of paper 09 (main.tex @0fbc9e4).
Written from scratch; does not import tools/*.py.  Run: python3 -I verify_09_review.py
Alphabet: a; floor [ ]; ceiling { }.  s_U(w)='Z' iff w contains a ceiling bracket.
 (1) Lemma 4.1 replacement property (n<=3), Prop 4.2(a), Thm 4.5(i) (H_n: 2n NTs, 6n-4 rules,
     rho<=4, typed strong 1-FCP), Lemma 4.3 capture (exhaustive over occurrences in R), n<=4
 (2) Exemplar UPPER bound not stated in the paper: H_n has the typed strong 1-FKP with
     kernels {w*_i} (type 1) and {u_i} (type Z)
 (3) Rec_{s_U}: n=2 all characteristic samples; n=3 a characteristic sample WITHOUT the factor
     w*_2 (answers the question at the end of Remark 5.3 negatively for n=3); minimal
     max-datum length of characteristic samples for n=2,3
 (4) Prop 6.5: table of context sets relative to L^+, all words of length <= N (default 5)
"""
import itertools, re, sys

# ---------- bracketed doubling family ----------
def levels(n):
    E=[{'a'}]
    for _ in range(n):
        p=E[-1]; E.append({'['+x+y+']' for x in p for y in p}|{'{'+x+'}' for x in p})
    return E
def wstar(i):
    w='a'
    for _ in range(i): w='['+w+w+']'
    return w
def u(i): return '{'*i+'a'+'}'*i
def sU(w): return 'Z' if ('{' in w or '}' in w) else '1'
def subs(L): return {m[i:j] for m in L for i in range(len(m)) for j in range(i+1,len(m)+1)}
def D(x,L):
    out=set()
    for m in L:
        k=m.find(x)
        while k>=0: out.add((m[:k],m[k+len(x):])); k=m.find(x,k+1)
    return out
def fillers(L,c):
    p,q=c; return {m[len(p):len(m)-len(q)] for m in L if len(m)>=len(p)+len(q) and m.startswith(p) and m.endswith(q)}
def ctxcl(L,C):
    r=None
    for c in C:
        S=fillers(L,c); r=S if r is None else r&S
    return r
def kercl(L,K): return ctxcl(L,set.intersection(*[D(k,L) for k in K]))

def H(n):
    NT=[(i,'1') for i in range(n)]+[(i,'Z') for i in range(1,n+1)]
    P=[((0,'1'),['a'])]+[((i,'1'),['[',(i-1,'1'),(i-1,'1'),']']) for i in range(1,n)]
    for i in range(1,n+1):
        for al,be in [('1','Z'),('Z','1'),('Z','Z')]:
            if (i-1,al) in NT and (i-1,be) in NT: P.append(((i,'Z'),['[',(i-1,al),(i-1,be),']']))
        for al in '1Z':
            if (i-1,al) in NT: P.append(((i,'Z'),['{',(i-1,al),'}']))
    lang={}
    for i in range(n+1):
        for t in '1Z':
            X=(i,t)
            if X not in NT: continue
            S=set()
            for lhs,rhs in P:
                if lhs==X:
                    for comb in itertools.product(*[[s] if isinstance(s,str) else sorted(lang[s]) for s in rhs]): S.add(''.join(comb))
            lang[X]=S
    return NT,P,lang

def part1(nmax=4):
    ok=True
    for n in range(2,nmax+1):
        E=levels(n); Ln=E[n]; Mn=Ln-{wstar(n)}
        if n<=3:
            for m in Ln:
                for j in range(n+1):
                    for y in E[j]:
                        k=m.find(y)
                        while k>=0:
                            ok&=all(m[:k]+y2+m[k+len(y):] in Ln for y2 in E[j]); k=m.find(y,k+1)
        for i in range(n+1):
            ok&= ctxcl(Ln,{('{'*(n-i),'}'*(n-i))})==E[i] and kercl(Ln,{u(i)})==E[i]
        NT,P,lang=H(n)
        ok&= lang[(n,'Z')]==Mn and len(NT)==2*n and len(P)==6*n-4 and max(len(r) for _,r in P)==4
        for i in range(n):
            cl=ctxcl(Mn,{('{'*(n-i),'}'*(n-i))})
            ok&= lang[(i,'1')]=={x for x in cl if sU(x)=='1'}
            if i: ok&= lang[(i,'Z')]=={x for x in cl if sU(x)=='Z'}
        z='['+wstar(n-1)+u(n-1)+']'; m=1+len(wstar(n-1)); cnt=0
        for i in range(m):
            for j in range(i,m+1):
                p,x,q=z[:i],z[i:j],z[j:]; qp=q[:-len(u(n-1))-1]+wstar(n-1)+']'
                for t in Mn:
                    if len(t)>=len(p)+len(q) and t.startswith(p) and t.endswith(q):
                        e=t[len(p):len(t)-len(q)]; cnt+=1
                        ok&= ((p+e+qp) in Mn)==(e!=x)
        # (2) exemplar upper bound
        up=all({x for x in kercl(Mn,{wstar(i)}) if sU(x)=='1'}=={wstar(i)} for i in range(n)) and \
           all({x for x in kercl(Mn,{u(i)}) if sU(x)=='Z'}==E[i]-{wstar(i)} for i in range(1,n+1))
        kap=max(len(wstar(n-1)),len(u(n)))
        print(f'(1) n={n}: Lemma4.1/Prop4.2/Thm4.5(i)/capture({cnt} pairs) ok={ok}')
        print(f'(2) n={n}: H_n typed strong 1-FKP with kernels w*_i,u_i: {up}; rho|N|kappa={4*2*n*kap} vs lower bound {3*2**(n-1)-1}')
        ok&=up
    return ok

# ---------- Rec_s of #1, Sec. 4.1 ----------
def rec_language(K,target,s=sU):
    F=subs(K); Dk={x:D(x,K) for x in F}; par={x:x for x in F}
    def find(x):
        while par[x]!=x: par[x]=par[par[x]]; x=par[x]
        return x
    by={}
    for x in F:
        for c in Dk[x]: by.setdefault((c,s(x)),[]).append(x)
    for l in by.values():
        for y in l[1:]: par[find(y)]=find(l[0])
    comp={}
    for x in F: comp.setdefault(find(x),set()).add(x)
    close=lambda S:set().union(*[comp[find(x)] for x in S]) if S else set()
    res=set()
    for t in target:
        n=len(t); T={(i,i+1):(close({t[i]}) if t[i] in F else set()) for i in range(n)}
        for l in range(2,n+1):
            for i in range(n-l+1):
                j=i+l; S=set()
                for k in range(i+1,j):
                    for x in T[(i,k)]:
                        for y in T[(k,j)]:
                            if x+y in F: S.add(x+y)
                T[(i,j)]=close(S)
        if T[(0,n)]&set(K): res.add(t)
    return res
norm=lambda K:sum(len(w)+1 for w in K)

def part3():
    E=levels(2); M2=E[2]-{wstar(2)}
    chars=[K for r in range(1,6) for K in itertools.combinations(sorted(M2),r) if rec_language(set(K),M2)==M2]
    print(f'(3) n=2: characteristic samples for Rec_sU: {len(chars)}; = M_2 itself: {chars==[tuple(sorted(M2))]}')
    E=levels(3); M3=E[3]-{wstar(3)}; K=set(M3)
    for w in sorted(M3,key=lambda w:(-len(w),w)):
        if rec_language(K-{w},M3)==M3: K=K-{w}
    nofac=not any(wstar(2) in w for w in K)
    print(f'(3) n=3: characteristic K, |K|={len(K)}, ||K||={norm(K)}, contains factor w*_2: {not nofac}')
    print('    K =',sorted(K,key=len))
    for n,Mn in [(2,M2),(3,M3)]:
        for Lm in sorted({len(w) for w in Mn}):
            if rec_language({w for w in Mn if len(w)<=Lm},Mn)==Mn:
                print(f'(3) n={n}: minimal max-datum length over characteristic samples = {Lm} (|w*_(n-1)|={len(wstar(n-1))})'); break
    return nofac

# ---------- Prop 6.5 table ----------
def inV(x): return all(ch in 'ab#' for ch in x)
def inV0(x): return all(ch in 'ab' for ch in x)
def L1(x,sep='$'):
    if x.count(sep)!=1: return False
    v,z=x.split(sep); return inV(v) and z==v.replace('#','')[::-1]
def dec(x):
    for p in range(len(x)+1):
        v=x[:p]
        if not inV(v): break
        r=x[p:]; i=len(r)-len(r.lstrip('c')); r=r[i:]; j=len(r)-len(r.lstrip('d')); r=r[j:]; k=len(r)-len(r.lstrip('e')); z=r[k:]
        if inV0(z): yield v,i,j,k,z
def L23(x,which):
    for v,i,j,k,z in dec(x):
        if (which==2 and i!=j) or (which==3 and j!=k): continue
        cands=[v.split('#')[0]] if '#' in v else ([v] if (i or j or k) else [v[:t] for t in range(len(v)+1)])
        if any((c.count('a')>=c.count('b')) if which==2 else (c.count('a')<=c.count('b')) for c in cands): return True
    return False
def L4(x): return re.fullmatch(r'[ab#]*\$[ab]*c*%f*',x) is not None
def L5(x):
    if x.count('%')!=1: return False
    pre,post=x.split('%')
    if set(post)-{'f'}: return False
    kk=len(pre)-len(pre.rstrip('c'))
    return any(i==j and e!=k for k in range(kk+1) for v,i,j,e,z in dec(pre[:len(pre)-k]))
def Lp(x): return L1(x) or L1(x,'@') or L23(x,2) or L23(x,3) or L4(x) or L5(x)
def J0(x): return any(i==j==k for v,i,j,k,z in dec(x))
bal=lambda x: inV0(x) and x.count('a')==x.count('b')
ROWS={'Q':([('','#cd'),('a','b#de')],bal),
 'F':([('','cd'),('','ade')],lambda x:'#' in x and bal(x.split('#',1)[0]) and inV(x.split('#',1)[1])),
 'H':([('a#c','d')],lambda x:re.fullmatch(r'c*d*',x) is not None and x.count('c')==x.count('d')),
 'E':([('a#cd','e')],lambda x:set(x)<={'e'}),'C':([('b#c','de')],lambda x:set(x)<={'c'}),
 'J':([('b#d','e')],lambda x:re.fullmatch(r'd*e*',x) is not None and x.count('d')==x.count('e')),
 'T':([('$','a%')],inV0),
 'U':([('e','c%')],lambda x:(lambda m: m is not None and len(m.group(1))!=len(m.group(3)))(re.fullmatch(r'(e*)([ab]*)(c*)',x))),
 'S45':([('','f')],lambda x:L4(x) or L5(x)),
 'S2':([('',''),('a#','b')],lambda x:L23(x,2) or J0(x)),'S3':([('',''),('b#','a')],lambda x:L23(x,3) or J0(x)),
 'S1':([('a#','a'),('b#','b')],lambda x:L1(x) or L1(x,'@') or J0(x))}
def part4(N):
    bad=0; cnt=0
    for l in range(N+1):
        for t in itertools.product('abcdef#$%@',repeat=l):
            x=''.join(t); cnt+=1
            for C,f in ROWS.values():
                bad+= all(Lp(p+x+q) for p,q in C)!=bool(f(x))
    print(f'(4) Prop 6.5 table: {cnt} words x 12 rows, mismatches={bad}')
    return bad==0

if __name__=='__main__':
    r=[part1(4), part3(), part4(int(sys.argv[1]) if len(sys.argv)>1 else 5)]
    print('ALL OK' if all(r) else 'SOME CHECK FAILED')
```

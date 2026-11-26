# 09 論文を TCS #1 の Reviewer 1・2 の目で査読する（2026-11-26）

- 対象：「Frames versus Exemplars: An Exponential Gap for Syntactic Categories under Finite Observation」（栗山貴之、単著、JoLLI 投稿予定）
- 版：GitHub `growupkuriyama-hub/Papers` コミット `0fbc9e4`（HEAD と一致を確認）。行番号はすべて `09_typed-fcp-fkp/main.tex @0fbc9e4`。
- コンパイル結果：英語版 21 頁、日本語版 24 頁。番号は `.aux` から確認した（Lemma 3.7 = 核の縮約補題、Lemma 4.3 = 捕獲、Theorem 4.4 = 下界、Theorem 4.5 = 定理 A、Prop 4.7 = `prop:Ln-sU`、Prop 5.5 = 反駁、Prop 6.5 = weak FCP の非単調性）。
- 手順：main.tex を全文読み、主要な証明を手で追った。そのあと `tools/*.py` を実行し、自前の検証コードを書いた（付録 B）。ここまでで判断を固めてから、`response_round1.tex` と EM 版 PDF（48 項目と引用が同一であることを確認）、#1 の R1 原稿、`research/` の過去の査読記録を読んだ。
- 原稿の編集、commit、push はしていない。

---

## 0. 結論（先に）

1. **主定理を崩す反例や穴は見つからなかった。** Lemma 3.7、Lemma 4.3、Theorem 4.4、Theorem 4.5（定理 A）、Prop 4.7、Prop 5.5 は一行ずつ追って確認した。Prop 6.1、6.3、6.4、6.5 も、KY2017 の証明に依存する部分を除いて確認した。`tools/` の 4 本は全件通過した。自前の検査（n = 2, 3, 4）も全件通過した。
2. **証明の小さな穴が 1 つ、退行が 1 つある。**
   - Prop 3.5 の証明（636–637 行）は「d が j > i の段階で現れる」と仮定している。正例の提示は語を繰り返すとは限らないので、この仮定は成り立たないことがある。
   - Remark 3.6 の "as above"（668 行）は参照先を失っている。コミット `6de90d6` が、Prop 3.5 の証明にあった正規化の段落を消したためである。この段落は過去の査読（I-05、I-08）への対応として入れたもので、過去に直した点の退行にあたる。
3. **論文に書かれていない上界が成り立つ。H_n は、kernel {w\*_i}（型 1）と {u_i}（型 ζ）について typed strong 1-FKP を満たし、κ = |w\*_{n−1}| である**（n = 2, 3, 4 で全数確認）。したがって Theorem 4.4 の下界は O(n) 倍の範囲で最適である（ρ|N|κ ≤ 8n·(3·2^{n−1}−2)）。同じ文法 H_n が frame でも exemplar でも提示でき、両者の差は**証人の長さだけ**である。定理 A はこの形で述べるのがいちばん明快である。
4. **Prop 4.7 は #1 の (♠)／Cor 6.6 を kernel に言い換えたものである。** 一般には「typed kernel の κ は max_μ min{|w| : w ∈ L ∩ F_μ} 以上」という一行の観察で済む。L_n の列は #1 Prop 6.4／Cor 6.6 の焼き直しと読まれる危険がある（サラミ評価、§4）。
5. **主張の範囲が定理を超えている箇所がある。**
   - Abstract・§5 冒頭・結論は、dual learner の下界も「隔たりから従う」と読める書き方をしている。実際には Prop 5.5 は定理 A を使っていない。
   - 284 行の "for every typing under which M_n is learnable" は、系 5.2 の仮定 M_n ∈ C^cf_s より広い。
   - Python の例は、序論では「認可条件」（206 行）と呼ばれ、考察では「妥当性ではなく関数の分類」（1469 行）と呼ばれていて、自己矛盾している。
6. **推薦**
   - R1：**Major revision**（数学は正しいが、自明な部分・重複・長さに難がある。半分の長さで書ける）。
   - R2：**Major revision（現状では reject 寄り）**。観測器に依存する部分は、L_n では自明（Prop 4.7）、M_n では未解決（OP 8.3）である。観測器に依存しない部分は、一つの有限で人工的な族についての結果である。
   - 編集者の統合判定：**Major revision**。

---

## 1. 数学の検証

### 1.1 総括表

| 主張 | 行 | 判定 | 根拠・メモ |
|---|---|---|---|
| Lemma 2.1（Clark の包含） | 392–402 | 確認済み | 既知（Clark 2015、KY2017 式(1)）。証明は不要 |
| Lemma 2.2（到達文脈） | 414–424 | 確認済み | 既知 |
| Lemma 2.5（型付き細分化） | 506–527 | 確認済み | 中間の終端記号列の型 ĥ(w_i) が入っている（I-03 の修正は保たれている） |
| Lemma 3.1, 3.2 | 546–580 | 確認済み | 既知の帰結 |
| Prop 3.5（型付き学習器の健全性） | 618–654 | **軽微な穴** | 636–637 行の「d = t_j with j > i」（§1.2.8） |
| Remark 3.6 | 662–677 | **参照切れ** | 668 行 "as above" の参照先が消えている（§7） |
| **Lemma 3.7**（核の縮約） | 684–705 | **確認済み** | §1.2.1 |
| Lemma 4.1（節点構造） | 734–749 | 確認済み | 二種類の括弧でも、一致は深さだけで決まる |
| Prop 4.2(a)(b) | 751–779 | 確認済み | 自前計算でも確認（n ≤ 4） |
| **Lemma 4.3**（捕獲） | 781–798 | **確認済み** | §1.2.2。`check_deletion_family.py` (C) で n = 4 の 1,204 組 |
| **Theorem 4.4** | 800–828 | **確認済み** | §1.2.3 |
| **Theorem 4.5（定理 A）** | 838–861 | **確認済み** | 規則数 6n−4 を自前で数えた（n = 2, 3, 4 で 8, 14, 20） |
| Prop 4.6 | 863–880 | 確認済み | どの証明にも使われていない（OP 8.3 からの参照のみ） |
| **Prop 4.7** | 889–912 | **確認済み（ただし自明）** | §1.2.4 |
| Lemma 5.1 | 938–960 | 確認済み | #1 Thm 4.2 の健全性不変量の言い換え（§4） |
| Cor 5.2 | 962–981 | 確認済み | 2·(‖K‖²/2)·‖K‖ = ‖K‖³ |
| Cor 5.4 | 998–1016 | 確認済み | Σ_{j≤k} C(e,j) ≤ e^k、\|Sub(D)\| ≤ ‖D‖² |
| **Prop 5.5**（dual の反駁） | 1018–1051 | **確認済み** | §1.2.5。全データからの文脈 c を自前で全数確認 |
| Prop 6.1（双対性） | 1110–1151 | 確認済み | (a)(b)(c) とも |
| Cor 6.2 | 1153–1163 | 確認済み | |
| Prop 6.3 | 1175–1204 | 確認済み | 不等式 b ≤ a ≤ 2b を m ≥ 2n で手計算した |
| Prop 6.4 | 1206–1250 | 確認済み（証明は不十分） | L_+ = {z}^{▷◁} の証明（1229–1236 行）が散文で、証明になっていない。自前の有界検査で確認 |
| **Prop 6.5**（weak FCP） | 1271–1407 | **確認済み（KY 依存部を除く）** | §1.2.6 |
| Remark 5.7 の非代入性の例 | 1096–1100 | 確認済み | |

### 1.2 一行ずつの検証（要点）

#### 1.2.1 Lemma 3.7（核の縮約補題）— 確認済み
- P_0 ⊆ P_1 ⊆ P_2 で、Lemma 3.2 の仮定 X_i ⊆ Y_i ⊆ X_i^{▷◁} は K_i ⊆ cl(K_i) ⊆ K_i^{▷◁} から成り立つ。よって P_0^▷ = P_1^▷ = P_2^▷。
- P_1 ⊆ F_{τ(A)} は、cl(K_i) ⊆ F_{τ(A_i)} と型整合性から従う。Lemma 3.1 の最後の主張は K_A ⊆ F_{τ(A)} を仮定しており、ここで満たされている。
- 健全性は、どちらの族も K_S ⊆ L と同値になる。K_S = ∅ でも成り立つ（K_S^▷ が全文脈になり (ε,ε) を含む）。

#### 1.2.2 Lemma 4.3（捕獲補題）— 確認済み
- z = ⌊w\*_{n−1}u_{n−1}⌋ ∈ M_n。n ≥ 2 なので u_{n−1} は標識付きであり、z ≠ w\*_n。m = 1 + |w\*_{n−1}| = 3·2^{n−1} − 1。
- x が R の中にあるので、q は z[m+1..] = u_{n−1}⌋ を接尾辞に持つ。q' を作ると pxq' = w\*_n。
- e ∈ K_B について、Lemma 2.2 より peq ∈ M_n ⊆ L_n。接尾辞の u_{n−1} の出現は Lemma 4.1 により E_{n−1} 節点なので、置き換えると peq' ∈ L_n。左右の消去により、peq' = w\*_n ⇔ e = x。
- x ∈ K_B^{▷◁} より K_B^▷ ⊆ D(x) であり、(p,q') ∉ D(x)。よって (p,q') を拒否する e ∈ K_B が存在し、それは e = x に限られる。K_B = ∅ の場合も矛盾として処理されている。

#### 1.2.3 Theorem 4.4 — 確認済み
- 最小の導出木で同じ非終端記号が道の上に繰り返されないこと：αβ ≠ ε ならポンプで無限になり、αβ = ε なら木を小さくできる。ε 規則があっても成り立つ。
- 位置 m と m+1 を両方含む節点（chain node）は根からの一本の道をなし、高々 |N| 個。
- j ≤ m について、j を含む最深の chain node の子のうち j を含むものは chain node ではない。この子が m+1 を含むと、区間なので m も含んで chain node になってしまう。よってこの子は R の中にある。
- 断片の数は ρ|N| 以下で、各断片は終端記号か kernel の語（Lemma 4.3）。よって m ≤ ρ|N| max(κ,1)。型付きの場合は Lemma 3.7 で同じ文法・同じ kernel に移る。

#### 1.2.4 Prop 4.7 — 確認済み（ただし一行の観察）
- 証明は L_n ∩ F_1 = {w\*_n}（自前で n ≤ 4 を確認）と、∅^{▷◁} = ∅（有限言語）だけを使う。
- 一般には、どの型付き kernel 提示でも、各 μ ∈ ŝ(L) について型 μ の初期記号の kernel は L ∩ F_μ の空でない部分集合になる。よって **κ ≥ max_{μ∈ŝ(L)} min{|w| : w ∈ L, ŝ(w) = μ}**。これは #1 の式 (♠)（#1 main.tex 1167–1171 行）とまったく同じ量である。Prop 4.7 はこの量が L_n では 3·2^n − 2 になることを言っているだけである（§4 で扱う）。

#### 1.2.5 Prop 5.5（dual 学習器の反駁）— 確認済み
- 極限の文法に無効な候補規則が残らないこと：Prop 3.5 と同じく、C^◁ ⊆ Sub(L\*) = ⋃_j E_j から従う。
- {c}^◁ = L(G_n, E_{n−1})（M_n 相対）。c = (⌊, y'⌋) の場合、y' が素な平衡語（外側の括弧が対応する語）なので分割は一意である。**自前で、M_n の全データ（n = 2, 3, 4 で 5／41／1,805 語）から読み取った c がすべてこれを満たし、{c}^◁ ∩ F_1 = {w\*_{n−1}} であることを確認した。**
- (⌊, ε, ⌋) ∈ H_t：Sub^{≤m} の定義（459–460 行）は空の w_i を許すので成り立つ。
- 型付きの候補 ({c},ζ) → ⌊({c},1)({c},ζ)⌋ は型整合的で無効である。検査で落ちるのは w\*_{n−1} ∈ E_i のときに限る。

#### 1.2.6 Prop 6.5（weak FCP の非単調性）— KY 依存部を除いて確認済み
- Claim（1317–1334 行）：x_t = #cde^t a ∈ L_2、#cd²e²a ∈ L_3。L_5 との比較で k = t とすると j ≠ k に反する、という議論を一行ずつ確認した。
- S_2：a#xb は末尾が b で、先頭のブロックが a なので L_1 ∪ L_1^@ にも L_4 ∪ L_5 にも入らない。正しい。
- S_1：M^◁ ⊆ {(a#,a),(b#,b)}^◁ = L_1 ∪ J_0 ⊆ (M ∪ X)^◁ ⊆ M^◁ と挟めば等号が出る。原稿の書き方は短すぎるが結論は正しい。
- (b)：「C ⊆ L(G,B)^▷ だから C は @ を含まない」という一歩が書かれていない（Minor R1-m6）。
- 表と閉包は `check_weak_fcp_s0.py` で長さ 5 以下を全数確認した。KY2017 の Lemma 8・12・13 の**証明**への依存は、私は原典を開けなかったので**未検証**である。過去の査読（Astra、LEDGER 2026-11-25 追記）は著者稿に対して照合済みとしている。

#### 1.2.7 Prop 6.4 — 結論は確認済み、証明は不十分
- {z}^{▷◁}（L_K 相対）= {a^m b^n : m > n} ∪ {a^m z b^n : n ≤ m} = L_+。手計算で確認した。また、長さ 7 以下の全語（文脈 a^p, b^q、p, q < 12）で自前の検査を行い、{y} 側も含めて一致した。
- ただし 1229–1236 行は "all nonnegative differences p−q preserve exactly ..." という散文であり、R1 が受け入れる証明ではない。3 行で書ける：x = a^m b^n なら、すべての p ≥ q について m+p ≠ n+q ⇔ m > n。x = a^m z b^n なら n+q ≤ m+p ⇔ n ≤ m。y を含む語は p を大きく取れば落ちる。

#### 1.2.8 Prop 3.5 の小さな穴
- 636–637 行：「d ∈ L\* \ L(G) かつ d = t_j（j > i）ならば stage j は reset」。提示の中で d が j ≤ i にしか現れない場合が抜けている。
- 修正案："choose j > i with d ∈ D_j (possible since D_i ⊆ D_j); then D_j ⊄ L(G_{j−1}) = L(G), so stage j is a reset."

### 1.3 計算による検証（実行結果）

| スクリプト | 結果 |
|---|---|
| `tools/check_toy_example.py` | 期待どおり（例 1.1 の閉包が一致） |
| `tools/check_reduction_identity.py` | 恒等式 3,000 件、規則同値 1,672 件で反例なし |
| `tools/check_weak_fcp_s0.py` | 受理文脈 140 個、閉包の検査 111,111 件、表の検査 1,333,332 件で反例なし |
| `tools/check_deletion_family.py 4` | n = 2, 3, 4 ですべて通過（捕獲 17／108／1,204 組、(U) 20／1,967 組） |
| 自前 `my_checks.py`（付録 B） | すべて通過（下表） |

自前の検査の内容と結果：

| 検査 | 結果 |
|---|---|
| (1) H_n が kernel {w\*_i}／{u_i} で **typed strong 1-FKP**、未型付けの族 (K^{▷◁}) も SPP | n = 2, 3, 4 で成立。ρ\|N\|κ = 64／240／704、下界 5／11／23、比は 12.8／21.8／30.6（≤ 8n） |
| (2) \|N\| = 2n、規則数 6n−4、ρ ≤ 4 | 成立 |
| (3) Prop 5.5：全データから得た c で {c}^◁ = L(E_{n−1})、型 1 の部分は {w\*_{n−1}} | n = 2, 3, 4 の全データで成立 |
| (4) M_n は s_0 で代入可能でなく、s_U で代入可能 | n = 2, 3 で成立（s_0 の反例は ⌊⌊aa⌋ と ⌊⌈a⌉） |
| (5) Prop 6.4 の {z}^{▷◁} = L_+、{y}^{▷◁} = L_− | 長さ 7 以下で成立 |
| (6) L_n の型 1 のファイバーは {w\*_n} | n = 1..4 で成立 |
| Python（3.13.18 で実行） | 到達しない分岐の yield → generator。pass → ordinary。`((yield 0), ((yield 0), 0))` → generator。lambda の中の yield → 外側は ordinary。内包表記の中の yield → SyntaxError。論文の記述と一致 |

### 1.4 新しい観察（論文に入れるべきもの）

**命題（提案）** H_n（Prop 4.2(b)）は、M_n 相対で、kernel K_{(E_i,1)} = {w\*_i}、K_{(E_i,ζ)} = {u_i} について typed strong 1-FKP を持つ。よって
 ρ|N| max(κ,1) ≤ 4·2n·(3·2^{n−1} − 2)。
Theorem 4.4 と合わせると、この積は Θ̃(2^n) になる（O(n) の係数を除いて一致）。

証明の骨子：
- {u_i}^{▷◁}（M_n 相対）= L(E_i) \ {w\*_i}。w\*_i は、w\*_n から E_i 節点を一つ抜いた無標識の文脈で落ちる。標識付きの語はどの文脈でも残る。
- {w\*_i}^{▷◁} = L(E_i)。w\*_i の文脈は標識を含むものだけだからである。型 1 との交わりは {w\*_i} になる。

意味：
- 定理 A は「**同じ文法 H_n** の 2n 個のカテゴリーが、長さ 2n 以下の frame でも、長さ 3·2^{n−1} − 2 以下の exemplar でも名指せる。ただし、どの文法でも exemplar をこれより大きく短くはできない」と言い直せる。
- 隔たりが**文法のサイズではなく証人の長さ**にあることが一目でわかる。
- 830–836 行の問い（kernel に w\*_{n−1} ほどの長さが必要か）について、「十分である」側が示される。

---

## 2. 査読報告：Reviewer 1（#1 の R1 の観点）

### 総評
二つの有限な提示を比べる問題設定は自然である。Lemma 4.3 と Theorem 4.4 の組み合わせは短く、正しい。#1 の Section 6 が L_n と M_n を「区別する組」としてしか使わなかったのに対し、M_n そのものの exemplar 下界を任意の文法・任意の観測器について示した点は新しい。

一方で、原稿の大半は、既知の事実の再証明、自明な系、同じ内容の繰り返し、#1 からの移植で占められている。中心となる新しい内容は 6〜7 頁に収まる。主張の範囲が定理を超えた箇所が数か所ある。学習アルゴリズムについての一つの証明に小さな穴があり、改訂の途中で参照が切れた箇所もある。#1 で私が指摘した型の問題（未定義語、記号の衝突、定理文への注釈の混入、民間伝承的な事実の証明）がほぼすべて再現している。

### 推薦：Major revision
数学的な誤りで結論が崩れる箇所はない。したがって reject ではない。ただし、(i) 定理 A を正しい形（§1.4 の上界を含む）で述べ直すこと、(ii) 自明な部分を削ること、(iii) 主張の範囲を定理に合わせることが受理の前提になる。

### Major

**R1-M1　定理 A の述べ方：exemplar 側の上界が抜けていて、隔たりの性質が見えない**（R1.3、R1.5 型）
- 箇所：231–249、800–861 行。
- 問題：Theorem 4.4 の下界に対応する上界が書かれていない。実際には H_n 自身が、kernel {w\*_i}, {u_i} について typed strong 1-FKP を持つ（κ = |w\*_{n−1}|）。積の比は 8n 以下である（§1.4、自前で n ≤ 4 を確認）。
- 修正案：定理 A を「同じ H_n で、frame の長さは 2n 以下、exemplar の長さは 3·2^{n−1} − 2 以下。どの文法でも ρ|N|max(κ,1) ≥ 3·2^{n−1} − 1」と書き直す。830–836 行の「わからない」の一部は解消する。

**R1-M2　Prop 4.7 は自明な系で、#1 の (♠)／Cor 6.6 そのもの**（R1.22「far too trivial a corollary」、R1.32「folklore」型）
- 箇所：882–912、241–248、263–265、1443–1445 行。
- 問題：証明は「初期記号の kernel は L ∩ F_μ に入る」だけである。#1 の (♠)（#1 main.tex 1167–1171 行）が同じ量を typed thickness について述べている。"the mark observer lengthens the exemplars" は、型の均質な kernel という定義から出る人工的な結果であり、観測の効果ではない。
- 修正案：命題としては削除する。§4.2 の終わりに一文を置く："Since typed kernels are type-homogeneous, κ ≥ max_μ min{|w| : w ∈ L ∩ F_μ}, the quantity (♠) of [tcs1]; for L_n under s_U this is 3·2^n − 2." Abstract・序論・考察の関連する文も短くする。

**R1-M3　学習器の下界の帰属：dual の下界は定理 A から出ていない**（R1.7「学習器と構成手続きの混同」、R1.13 型）
- 箇所：Abstract 83–85 行、917–919 行（"turns it into lower bounds for three learning algorithms"）、結論 1527–1529 行。考察 1450–1456 行は dual を正しく別扱いにしているので、そちらに合わせればよい。
- 問題：Prop 5.5 は Theorem 4.4 も Lemma 4.3 も使っていない。frame は短いのだから、隔たりから dual の下界が出るはずがない。Remark 5.6（1075–1079 行）だけが正しく「反駁のコスト」と書いている。
- 修正案："Theorem A yields lower bounds for the reconstruction Rec_s and for the primal learner; a separate refutation argument gives a lower bound for the dual learner."

**R1-M4　学習可能性の主張の範囲**（R1.10「RS vs RS_h」、R1.7 型）
- 箇所：283–284 行 "for every typing under which M_n is learnable"、989 行。
- 問題：系 5.2 の仮定は M_n ∈ C^cf_s である。Rec_s が M_n を正しく再構成できるのは C^cf_s のときだけ、という定理はない。
- 修正案："for every typing s with M_n ∈ C^cf_s".

**R1-M5　Prop 3.5 の証明の穴、Remark 3.6 の参照切れ**（R1.24・R1.25 型の「証明として受け入れられない」）
- 箇所：636–637 行、668 行。
- 修正案：§1.2.8 の一文を入れる。668 行の "as above" は、消えた正規化の段落の要点（"a nonterminal with empty context set denotes F_μ, which equals {c}^◁ ∩ F_μ for a reaching context c of the trimmed grammar by Lemma 2.2"）を一文で書き戻す。

**R1-M6　Prop 6.4 の L_± = {z}^{▷◁}, {y}^{▷◁} の証明**（R1.29「Make the statement mathematical」型）
- 箇所：1229–1236 行。
- 修正案：§1.2.7 の 3 行の証明に置き換える。

**R1-M7　長さ：半分で書ける**（R1.2、R1.30–R1.32、R1.34–R1.35 型）
削れる・短くできる箇所（概算で 21 頁 → 12〜13 頁）：
- Lemma 2.1 の証明（392–402 行）。Clark 2015 Props 3.26, 3.28 と KY2017 式(1) を引用すれば足りる。Lemma 2.2、Lemma 3.1、Lemma 3.2 も同様に、一行の証明と出典で足りる。
- 定義 3.3 と定義 3.4 は同じ概念を二つの語彙で定義している。609–610 行の "iff" がそれを示している。どちらかに統一する。
- Prop 3.5 と型付き学習器（618–660 行）。Cor 5.4 の型付きの場合は Lemma 3.7 で型なしに落とせる。Cor 6.2 は「Lemma 3.7 ＋ KY Thm 6」の一文で言える。型付き学習器を定義しなくても論文は成り立つ。
- Remark 3.6（662–677 行）。証明に使われていない。序論の一文に縮める。
- Theorem 4.4 と Theorem 4.5(ii) は重複している。一つにまとめる。
- Prop 4.6（863–880 行）。証明に使われていない。OP 8.3 の中に移す。
- Prop 4.7（R1-M2）。
- Remark 5.7 と、そのためだけの小節 5.3（1082–1101 行）。"known" と書いた結果に小節は要らない（R1.34「There is no need to devote an entire subsection」）。
- Prop 6.5 の証明（1281–1407 行、約 2.5 頁）は付録へ移す。
- 考察の "Observation as morphology"（1434–1448 行）は Theorem B の繰り返しである。

**R1-M8　用語の氾濫と二重の語彙**（R1.8「A flood of excessive terminology」、R1.9 型）
- frame/context、exemplar/kernel、observer/typing、presentation/very weak property、category/nonterminal の言語、が並行して使われている。
- 次の語は 09 で定義されていない：isolated-fibre argument（885 行）、typed thickness（886 行）、set-driven（84・281 行。#1 §2.1 でのみ定義）、ceiling（863・866 行）、constituent（863 行）、licensing condition（79・206 行）。
- 修正案：数学の本文では context/kernel/typing に一本化する。frame/exemplar/observer は序論の動機づけの段落でだけ使う。未定義の語は削るか定義する。

**R1-M9　記号の衝突**（R1.2「inconsistent use of metavariables」、R1.33 型）
| 記号 | 衝突箇所 |
|---|---|
| m | 語 m ∈ L_n（735 行）／長さ m = 1+\|w\*_{n−1}\|（783 行）／指数 a^m（1177、1207 行） |
| E | 非終端記号 E_i（721 行）／KY 表の E（1304 行）／集合族 𝓔_i（ひとつは避けたが、表で再び衝突） |
| H | 文法 H_n（756 行）／H_i（463 行）／半群 𝖧（490 行）／KY 表の H（1303 行） |
| J | J_i（463 行）／J_0（1268 行）／KY 表の J（1306 行） |
| C | 文脈集合 C／KY 表の非終端記号 C（1305 行）／𝒞(G,A)（407 行） |
| F | ファイバー F_μ／KY 表の F（1302 行） |
| B, P | B（Lemma 4.3 の非終端記号、784 行）／B = {w : \|w\|_a = \|w\|_b}（1293 行）。P（規則集合、404 行）／P_0, P_1, P_2（691 行）／P = {a^m b^n : m ≠ n}（1207 行） |
| L_1 | L_n の n = 1（722 行）／KY の L_1（1261 行） |
| M | M_n／鏡映文脈の集合 M（1355 行） |
| k | kernel の数 k／c^k（1265 行）／k_1, k_2（1394 行） |
| c | 文脈 c（866、1034 行）／文字 c（1177 行） |
| v | 語 v = ⌈w\*_{j−1}⌉（865 行）／文脈 (u,v) |
| p | 接頭辞 p（790 行）／上界 p（1242 行） |
| R | 接頭辞 R（783 行）／正規表現 R_μ（663 行） |
| t | 型 t（183 行、319 行の F_t）／段階 t（1027 行）／添字 x_t（1322 行） |
| 1 | U_1 の単位元 1／新しい単位元 𝟏_♯ |

修正案：Section 4・5・6 で記号を分ける。KY の表は KY の記号のままでよいが、本文の記号と衝突しないものに付け替える。

**R1-M10　定理文に混ざった注釈**（R1.13「Technically unnecessary words should be removed, especially in the statements of theorems」）
- 定理 A の 241–248 行（"Without the deletion ... Cor. 6.6"）は定理の外に出す。
- 定理 A (ii) の括弧（237–238 行）、Theorem 4.4 の "(of any cardinality)"（802 行。「有限」と重複）。
- Cor 5.2 の括弧の中の証明（966–967 行）、Cor 5.4 の "if k grows with n ..."（1006–1007 行）、Prop 4.7 の "whatever bound k ..."（893–894 行）。

### Minor
- R1-m1（R1.1・R1.3 型、帰属）：Lemma 5.1（938–960 行）は #1 Thm 4.2 の健全性不変量 [[x]] ⇒\* w ⟹ x ≡_L w（#1 main.tex 819–829 行）から直ちに従う。そう明記する。
- R1-m2（帰属）：Python の引用（207–209 行）。Language Reference §6.2.9 が述べているのは "Using a yield expression in a function's body causes that function to be a generator function" までである。「到達しない分岐でも」は参照文献には書かれていない。例か "as is easily checked" で支える。
- R1-m3：343–344 行 "the lower bound comes from the way categories are named, not from the length of the words"。下界の証明は長さ 3·2^n − 2 の語 z が M_n に属することを使っている。"not only from the length of the shortest words" などに弱める。
- R1-m4：Rem 5.6 の表の最終行 "data at convergence ≥ 3·2^{n−1}−2"（1065 行）。Prop 5.5 が言うのは「ある一つのデータの長さ」である。行名を "maximal datum length" に直す。
- R1-m5：KY の学習器を収束させるのは、M_n が有限なので自明である（全データが出た後は J, H, E が固定される）。Cor 5.4 と Prop 5.5 の「収束するなら」が空でないことを一文で言う。
- R1-m6：Prop 6.5(b)（1397–1403 行）。「C ⊆ L(G,B)^▷ なので C は @ を含まない」という一歩を明記する。
- R1-m7：#1 での記号は L_n^−（#1 Prop 6.4(iv)）、09 では M_n である。姉妹論文の間で揃える。
- R1-m8：Remark 5.3 の "M_n ∉ C^cf_{s_0} [tcs1, Prop 6.4]"（989 行）。この事実は #1 では命題文ではなく証明の末尾にある（#1 main.tex 1350–1353 行）。"[tcs1, proof of Prop. 6.4]" とする。
- R1-m9：#1 との関係が 3 か所で繰り返されている（333–337、347–356、983–994 行）。一か所にまとめる。

### Typo
- 297–298 行："Propositions~\ref{thm:duality}, Propositions~\ref{...}" → "Propositions 6.1 and 6.3–6.5"。ラベル名 `thm:duality` も `prop:` にする。
- 609 行："a ($s$-typed)" → "an ($s$-typed)"。
- 319 行："F_t" → "F_μ"（本文の記号に合わせる。183 行の s^{−1}(t) も同様）。
- 1059 行："poly data" → "polynomial data"。
- 1084 行：Remark の題に "; known" とある。本文で出典を述べれば題からは外せる。

---

## 3. 査読報告：Reviewer 2（#1 の R2 の観点）

### 総評
観測器を加えると frame と exemplar が逆向きに振る舞う、という Theorem B の見方は筋がよい。#1 で私が求めた「型付けが満たすべき条件」に一歩近づいてもいる。しかし、観測器を主題とする論文としては、観測器が実際に効いている結果が一つもない：
- (a) L_n での隔たりは、型の均質な kernel という定義から自明に出る（Prop 4.7）。
- (b) M_n での exemplar の下界は観測器なしで成り立つ（Theorem 4.4）。
- (c) M_n で frame に観測器が**必要**かどうかは未解決である（OP 8.3）。

題の "under Finite Observation" と Abstract は、この状況より強く読める。結果はすべて、一つの有限で人工的な族についてのものであり、#1 の R2.3 で述べた「範囲の分からない技術的強化」という懸念がそのまま当てはまる。

### 推薦：Major revision（現状では reject 寄り）
次のいずれかを強く求める。(i) OP 8.3 を解く（型なしの frame も指数的であることを示す）。(ii) 主定理を族に依存しない形に一般化する（下の R2-M2）。どちらもできない場合は、題と Abstract を下界の実際の内容（型なしの exemplar 提示の指数下界）に合わせる。

### Major

**R2-M1　観測器の役割と、観測器が満たすべき条件**（R2.1「the conditions a typing must satisfy could be studied」）
- 箇所：257–274、1420–1448 行。
- 問題：frame の上界（Prop 4.2(b)）は、M_n = L_n ∩ s_U^{−1}(ζ) であることと、i < n の文脈 (⌈^{n−i}, ⌉^{n−i}) が既に標識を含むことだけを使っている。観測器は対象の認可条件そのものを符号化するように選ばれている。
- 修正案：一般の原理として述べる。例：「Acc が 𝖲^♯ のイデアルで、L ∩ ŝ^{−1}(Acc) の各非終端記号に、完成した語の型が Acc に入る文脈集合があれば、L の型付き frame 提示は L ∩ ŝ^{−1}(Acc) に移る」。そうすれば、どの観測器なら frame が得をするかという問いに、具体的な答えが一つ出る。

**R2-M2　適用範囲：一つの有限族**（R2.3「a technical strengthening on a class of unknown extent」）
- 箇所：1477–1483 行（"finite and artificial" と認めている）。
- 問題：Lemma 4.3 は「ただ一つの語を消す」構造に依存している。消す語が複数の場合、無限言語の場合、他の族で同じ捕獲が起きるかが分からない。
- 修正案：Lemma 4.3 を族に依存しない形で述べる。例：「L の語 w が、w と一点で違う語 w' ∈ L との差分の外に長い因子 R を持つなら、R の中の構成素はすべて kernel に入る」。Theorem 4.4 をその系にする。少なくとも、無限の場合（すべての深さの和など）について何が言えて何が言えないかを述べる。

**R2-M3　どの証明にも使われない成分**（R2.2「the components are then read by no proof」、R2.6「is never used」）
- Prop 4.6（863–880 行）：参照は OP 8.3 だけ。
- Remark 3.6（662–677 行）：参照は序論 321 行だけ。
- Fact 2.3(c)（447–448 行）：背景としてのみ。
- 定義 3.4 と定義 3.3 の重複（R1-M7）。
- 型付き dual 学習器：使われているのは Prop 5.5 の型付きの場合だけ。この場合は型なしの場合と同じ議論の変形である。
- 修正案：どれも削除するか、未解決問題・脚注へ移す。

**R2-M4　使う前の参照と繰り返し**（R2.4「objects are regularly used before they are introduced」「several results restate what their proofs have just established」）
- 序論の定理 A（227、247–248 行）が、Lemma 3.7、Prop 4.7、#1 Cor 6.6 に前方参照している。
- "What the observer buys"（257–274 行）は、Cor 6.2、Rem 5.7、Prop 5.5 を定義の前に使っている。
- 679–682 行と 707–710 行は同じ文の繰り返しである（"a typed kernel presentation is nothing but ..."）。
- 882–887 行は序論の繰り返し。Theorem 4.5 は既出の命題を並べただけ。考察 1434–1448 行は Theorem B の繰り返し。
- 修正案：序論の定理 A は (i)(ii) だけを述べる。説明は定理の外に一度だけ置く。

**R2-M5　付録へ回すべきもの**（R2.11「could be condensed or given in appendix」）
- Prop 6.5 の証明（約 2.5 頁、1281–1407 行）。KY の表と Claim を含め、論文の主題（frame と exemplar の隔たり）から外れている。
- §2 の学習器の再録（451–477 行）。Prop 5.5 でしか使わないので、Section 5 の直前か付録に移す。

**R2-M6　例の一貫性：Python**（R2.7「Example 4.3 is not in SSBNF」と同じ型の「例が主張と合っていない」）
- 箇所：206–216、1458–1475 行。
- 問題：
  - 序論では「大域的な認可条件のなじみ深い例」（206 行）と呼び、考察では「分類は関数についてのもので、構文的な妥当性ではない」（1469–1470 行）と書いている。M_n は文法性の条件ではなく分類である。
  - 「すべての道がちょうど n 個の構成子を通る」本体は、Python の例として極めて人工的である。
  - JoLLI の読者には、序論の例 1.1（数の一致）と M_n のつながりのほうが重要だが、その橋渡しがない。
- 修正案：Python は考察に戻すか削除する。序論では、例 1.1 の数の素性を一般化した「どこかに一つ標識があれば認可される」構文の例で M_n を導入する。言語学の例で、実証的な主張はしないこと。

**R2-M7　大きさの尺度**（R2.3 型）
- 箇所：596–608、800–807 行。
- 問題：frame 側は |N|、ρ、文脈長を別々に評価し、exemplar 側は積 ρ|N|max(κ,1) で評価している。下界が積でしか出ないことは理解できるが、比較は同じ尺度でしてほしい。
- 修正案：frame 側も ρ|N|ℓ（= 16n²）で書き、表 5.6 を同じ尺度で揃える。§1.4 の上界と合わせれば、隔たりは 16n² 対 Θ̃(2^n) と一行で言える。

### Minor
- R2-m1：題。"under Finite Observation" は観測器が下界に効いているように読める。案："Frames versus Exemplars: Exponential Exemplar Lower Bounds from a One-Word Deletion"。または副題で観測器の役割（上界にだけ使う）を示す。
- R2-m2：1516–1520 行の "Further questions" は OP の外にあり、番号も付いていない。OP にまとめるか削る。
- R2-m3：JoLLI（Springer）の書式。Elsevier 型の "Declaration of competing interest"（1535 行）、"Data availability"（1538 行）ではなく "Statements and Declarations" を使う。Funding の記載がない。データの URL（1542 行）は `tree/main` でコミットを固定していない。投稿時には commit permalink か Zenodo の DOI にする。
- R2-m4：査読用に英語版にも行番号（`lineno`）を付ける（日本語版には付いている）。

### Typo
- 1065 行の表の行名（R1-m4 と同じ）。
- 863 行の命題の題 "constituents around a ceiling"：「ceiling」は未定義である。

---

## 4. #1 との関係：サラミ・スライスの評価

### 4.1 依存の大きさ

| 09 の項目 | #1 の対応箇所（R1 = arXiv v5 の番号） | 判定 |
|---|---|---|
| 族 L_n、G_n、w\*_i、u_i、s_U | #1 §6（main.tex 1244–1271 行）、Prop 6.4(ii) の u_i | 同一（09 も 333–335 行で認めている） |
| M_n | #1 の L_n^−（Prop 6.4(iv)）。s_U で代入可能、s_0 で代入不可能（証明末尾） | 同一の対象。記号だけが違う |
| Rec_s、C^cf_s | #1 §4.1、Def 2.1 | 再録（09 の 928–936 行）。#1 の定義と一致することを確認した |
| **Prop 4.7** | **#1 Cor 6.6 と (♠)** | **論法は同一**：L_n ∩ F_1 = {w\*_n} が typed thickness（#1）または kernel の長さ（09）を下から押さえる。09 での追加は、K_S ≠ ∅（∅^{▷◁} = ∅）の一行だけ |
| 表 5.6 の L_n の列 | #1 Prop 6.4(ii)(iii)、Cor 6.6 | 位置と結論が同じ（多項式 vs 指数） |
| Lemma 5.1 | #1 Thm 4.2 の健全性不変量（main.tex 819–829 行） | 言い換え |
| Remark 5.7 | #1 Prop 9.7 ＋ Yoshinaka 2015 §6.3 ＋ KY Thm 6 | 既知（09 も "known" と明記） |
| **Lemma 4.3、Theorem 4.4** | なし | **新規**（#1 は M_n を区別する組の相手としてしか使わない） |
| Cor 5.2（M_n の正例データの下界） | なし（#1 Prop 6.4(iii)(iv) の対象は L_n） | 新規 |
| Cor 5.4、Prop 5.5、Theorem B の厳密性、Prop 6.5 | なし（KY2017 の系統） | 新規 |

### 4.2 #1 Cor 6.6 と Prop 4.7 の関係（詳しく）
- #1 Cor 6.6 は、L_n のどの縮約 BUNF 文法も τ^typ_{s_U}(G) ≥ 3·2^n − 2 を満たすことを、式 (♠) τ^typ ≥ max_μ min{|w| : w ∈ L ∩ F_μ} から導いている。
- 09 Prop 4.7 は、型付き kernel 提示で κ ≥ |w\*_n| を示している。型付き kernel は ⊆ L ∩ F_μ を満たさなければならないので、κ ≥ max_μ min{|w| : w ∈ L ∩ F_μ} が一般に成り立つ。これは (♠) の右辺と同じ量である。
- 両者は「孤立したファイバー {w\*_n} の唯一の語が長い」という同じ事実の、二つの言い換えである。
- 09 の 885–887 行は "the isolated-fibre argument ... transferred here from yields to kernels" と正直に書いている。しかし命題として番号を付け、Abstract 以外の 4 か所（序論 245–248・263–265 行、表 1062 行、考察 1443–1445 行）で「観測器が exemplar を長くする」と強調するのは、#1 の結果を新しい結果に見せる効果を持つ。

### 4.3 評価
- **#1 の結果の焼き直しは Prop 4.7（と表の L_n の列）に限られ、量としては小さい。** 09 の中心（Lemma 4.3、Theorem 4.4、Prop 5.5、Theorem B の厳密性、Prop 6.5）は #1 にない。サラミ・スライスとまでは言えない。
- **ただし危険はある。** 編集者や査読者が #1 と 09 を並べて読むと、09 の Section 4〜5 は「#1 §6 の族について #1 が残した問いを解く続編」に見える。Prop 4.7 と Lemma 5.1 がそれを強める。
- **対策**
  1. Prop 4.7 を一文の注意に格下げし、#1 Cor 6.6／(♠) を出典にする（R1-M2）。
  2. Lemma 5.1 に #1 Thm 4.2 を明記する（R1-m1）。
  3. 09 を「KY2017 の系統の論文（frame vs exemplar）で、例として #1 の族を使う」と位置づける。序論の "Relation to the fixed-typing theory" は一段落に縮める。
  4. 記号を #1 に揃える（M_n ↔ L_n^−）。
- **#1 の審査との連動の危険。** #1 は審査中である。#1 の R2 で Section 6 の番号や記号が変われば、09 の引用（Cor 6.6、Prop 6.4、Prop 9.7、Prop 3.1、Lemma 2.2、Def 2.1）がずれる。09 は "arXiv:1409.6247v5" に固定して引用しているので（173–174 行の脚注）、現状は問題ない。#1 の改訂版が出たら、版を明示し直す。

---

## 5. 主張の範囲の確認

| 箇所 | 主張 | 定理が実際に示す範囲 | 判定・修正案 |
|---|---|---|---|
| 題 | "An Exponential Gap ... under Finite Observation" | exemplar の下界は観測器なしで成り立つ。frame の上界は s_U だけ。型なしの frame は未解決 | **やや超える**。R2-m1 |
| Abstract 81–83 行 | 標識の観測器のもとで frame は 2n 以下、exemplar は「どの観測器でも」指数的 | 正しい | 確認済み |
| Abstract 83–85 行 | 隔たりが Rec_s と「所属質問を用いる学習器」の指数下界を与える | dual の下界は隔たりから出ていない。「学習器」は KY2017 の Algorithms 1・2（r, k 固定）に限る | **超える**。R1-M3 |
| 序論 206 行 | Python のジェネレータは「大域的な認可条件のなじみ深い例」 | 考察 1469 行は「妥当性ではなく分類」 | **自己矛盾**。R2-M6 |
| 序論 212–216 行 | 制限した断片についての下界で、Python 全体については何も主張しない | 正しく限定されている | 確認済み |
| 序論 283–284 行 | "for every typing under which M_n is learnable" | 系 5.2 は M_n ∈ C^cf_s を仮定 | **超える**。R1-M4 |
| 序論 286–292 行 | primal は r, k 固定で 2^{Ω(n)}、dual は r ≥ 2, k ≥ 1 | 系 5.4、Prop 5.5 と一致 | 確認済み |
| 序論 343–344 行 | 下界は名指し方から来て、語の長さからではない | 長い語 z の存在を使っている | **やや超える**。R1-m3 |
| 考察 1452–1454 行 | 隔たりが primal と Rec_s の指数データを説明する | 正しい | 確認済み |
| 結論 1524–1529 行 | 隔たりが Rec_s と「分布学習器」のデータを押さえる | dual は別の議論 | **超える**。R1-M3 |
| 結論 1532–1533 行 | Python の例は独立に定義された断片での研究を示唆する | 示唆にとどまる | 問題なし |

三つの一般化について：
- **Python**：Abstract からは消えており、序論・考察でも「深さを固定した断片」に限定されている（2026-11-26 のコミット 8944043）。残っている問題は、"licensing condition" という呼び方と、考察の「分類」との矛盾だけである。Python 3.12 Reference §6.2.9 の番号と記述は確認した。到達しない分岐の yield については、Python 3.13.18 で再現した。
- **有限観測**：本文の "What the observer buys"（257–274 行）は正確で誠実である。題だけが強い。
- **学習可能性**：序論の箇条書きは正確である（r, k 固定、Algorithms 1・2、Rec_s）。Abstract・§5 冒頭・結論の要約で範囲が広がっている。

---

## 6. 正確さ：日英の食い違いと書誌

### 6.1 英語版と日本語版
- 定理類の環境 37 個の種類・順序・ラベルが一致する。環境の中の数式は、句読点を除いてすべて一致した（自前の比較スクリプト）。
- 本文・証明・表を含む全体の数式の比較でも、違いは表の見出しの言語と、日本語の語順による式の分割だけだった。
- **数学的内容に関わる食い違いは見つからなかった。** Abstract、Python の段落（日本語 207–216、1177–1189 行）の範囲の限定も一致している。
- 違いは書式だけである（日本語版には行番号があり、英語版にはない → R2-m4）。

### 6.2 引用文献の書誌

| 文献 | 判定 | 確認先 |
|---|---|---|
| Clark 2010（ICGI 2010, LNAI 6339, pp. 38–51） | 確認済み | Leiß 2014 の参考文献（Crossref） |
| Clark 2015（JLC 25(5):1203–1229, online 2013） | 確認済み | 他論文の書誌（doi:10.1093/logcom/ext037）と著者の頁（Advance Access 2013-08-09） |
| Clark–Eyraud 2007（JMLR 8:1725–1745） | 確認済み | JMLR |
| Clark–Yoshinaka 2016（pp. 143–172, DOI） | 未検証（自分では開いていない） | 過去の査読（Astra）は §6.5.3 を確認済み |
| Coste–Nicolas 2019（PMLR 93:155–168） | 確認済み | PMLR。巻の名は "Proceedings of The 14th ICGI 2018" |
| Harris 1954（Word 10(2–3):146–162） | 未検証（周知の書誌） | |
| Kanazawa 1998（CSLI） | 未検証（周知） | |
| KY2017（LATA, LNCS 10168, pp. 77–88, DOI） | 未検証（自分では開いていない） | Astra が書誌を確認。定理・補題の番号は著者稿でのみ照合済み。刊行版本文との一致は誰も確認していない |
| KY2023（PMLR 217, pp. 8–22） | 未検証（自分では開いていない） | Astra が確認 |
| Kuriyama（#1, arXiv:1409.6247v5） | 確認済み | arXiv：v5 は 2026-10-23 付。番号は R1 原稿と一致 |
| Leiß 2014（FG 2014, LNCS 8612, pp. 121–137, DOI） | 確認済み | Crossref |
| Ogden 1968（MST 2(3):191–194） | 未検証 | |
| Python 3.12 Reference §6.2.9 | 確認済み（節番号と記述）。「到達しない分岐」は参照文献に書かれていない（R1-m2） | docs.python.org |
| Yoshinaka 2011（DLT, LNCS 6795, pp. 429–440） | 確認済み | 東北大学の業績頁、researchr |
| Yoshinaka 2015（MoL 14, pp. 87–98, ACL） | 確認済み。DOI 10.3115/v1/W15-2308 を足すとよい | ACL Anthology |

補足：JoLLI に投稿するなら、同誌に載った統語概念束の論文（例：Wurm 2017, JoLLI 26(2)）に一言触れると、読者との接点が増える（任意）。

---

## 7. 過去の査読記録との照合（退行の確認）

| 過去の指摘 | 当時の対応 | 現版（0fbc9e4） |
|---|---|---|
| I-03 Lemma 2.5 の型の積 | ĥ(w_i) を追加 | **保たれている**（513 行） |
| I-04 L_K の strong 1-FKP | S_+, S_− に分割 | 保たれている（1214–1236 行）。ただし閉包の証明は散文（R1-M6） |
| I-05 学習器の正規化（空の C, K） | Prop 3.5 の証明に段落を追加 | **コミット 6de90d6 で段落ごと削除**。逆方向を使わなくなったので削除自体は妥当 |
| I-08 EXREG の対応 | Remark 3.6 を具体化 | 本文は残っているが、**668 行の "as above" が I-05 の消えた段落を指していて参照切れ**（退行） |
| I-06 H_n の添字 | 存在する子だけに制限 | 保たれている（761–763 行） |
| I-07 尺度の区別 | 表の注記 | 保たれている（1069–1074 行） |
| I-09 Prop 4.6 | 本文に追加 | 残っているが、どの証明にも使われていない（R2-M3） |
| I-11 Yoshinaka 2015 の題（単数） | 修正 | 保たれている |
| Astra 3.1 L_n の s_U 行 | Prop 4.7 を追加し表を分割 | 保たれている。ただし Prop 4.7 は自明な系として扱うべき（R1-M2） |
| Astra 3.2 s_0 版の weak 2-FCP | 6.5(a) に追加 | 保たれている（1373–1384 行） |
| Astra：Funding の記載 | 「著者に確認」 | **未対応**（R2-m3） |
| Astra：データの URL をコミットに固定 | 「投稿時に差し替え」 | **未対応**（1542 行） |
| Astra：Prop 3.5 の reset の場合分け | 見送り | 新しい証明でも「d = t_j, j > i」という形で穴が残っている（R1-M5） |
| Astra：`check_deletion_family.py` (E) の長さの打ち切り | 見送り | そのまま。Lemma 5.1 は証明で独立に示されているので影響はない |

過去の査読（ChatGPT 11-24、Astra 11-25）の数学的な判定（主定理は CORRECT）と、私の検証は一致した。**過去の査読が挙げていない新しい指摘**は次のとおり。
- exemplar 側の上界（§1.4、R1-M1）
- Prop 4.7 が (♠) と同じ量であること（R1-M2）
- dual の下界が隔たりから出ていないこと（R1-M3）
- 「learnable」の範囲（R1-M4）
- Prop 3.5 の新しい形の穴、Remark 3.6 の参照切れ（退行）（R1-M5）
- Python の序論と考察の矛盾（R2-M6）
- frame 上界の一般原理（R2-M1）

---

## 8. 編集者向けの統合判定

**判定：Major revision。**

二人の査読者は、数学が正しいことで一致している。主要な証明は一行ずつ確認され、計算による検査もすべて通過した。

R1 は提示の問題（自明な系、重複、記号、長さ）と主張の範囲を問題にしている。R2 は、観測器という主題に対して観測器が実際に効いている結果がないこと、適用範囲が一つの有限族であることを問題にしている。R2 の懸念は、§1.4 の上界を加えて定理 A を「同じ文法での証人の長さの隔たり」として述べ直し、題と Abstract を下界の実際の内容に合わせれば、大部分が和らぐ。OP 8.3 を解くか Lemma 4.3 を一般化できれば、評価は大きく上がる。

### 投稿前に直すべき項目の優先順位表

| 順位 | 項目 | 行 | 対応する指摘 | 手間 |
|---|---|---|---|---|
| **P0-1** | Prop 3.5 の証明の穴（d = t_j, j > i） | 636–637 | R1-M5 | 一文 |
| **P0-2** | Remark 3.6 の "as above" の参照切れ（退行） | 668 | R1-M5 | 一文 |
| **P0-3** | dual の下界を「隔たりから」と書かない（Abstract・§5 冒頭・結論） | 83–85, 917–919, 1527–1529 | R1-M3 | 数文 |
| **P0-4** | "learnable" を M_n ∈ C^cf_s に直す | 283–284, 989 | R1-M4 | 一語 |
| **P0-5** | exemplar 側の上界（H_n の typed strong 1-FKP）を加え、定理 A を述べ直す | 231–249, 830–861 | R1-M1, R2-M7 | 命題一つ（証明は数行） |
| **P0-6** | Prop 4.7 を一文の注意に格下げし、#1 の (♠)／Cor 6.6 を出典にする | 882–912 ほか 4 か所 | R1-M2, §4 | 削除が中心 |
| **P0-7** | Python：序論の「認可条件」と考察の「分類」の矛盾を解消する（考察に戻すことを推奨） | 206–216, 1458–1475 | R2-M6 | 段落の移動 |
| P1-1 | Prop 6.4 の L_± の閉包に 3 行の証明を書く | 1229–1236 | R1-M6 | 小 |
| P1-2 | 定理文の注釈を外に出す | 237–248, 802, 893–894, 966–967, 1006–1007 | R1-M10 | 小 |
| P1-3 | Lemma 5.1 に #1 Thm 4.2 を明記し、記号を #1 に揃える（M_n ↔ L_n^−） | 938–960 | R1-m1, R1-m7 | 小 |
| P1-4 | 題と Abstract を下界の内容に合わせる | 60–61, 70–90 | R2-m1, §5 | 小 |
| P1-5 | 使われない成分を削るか移す（Prop 4.6、Remark 3.6、定義 3.4、型付き学習器） | 596–677, 863–880 | R2-M3, R1-M7 | 中 |
| P1-6 | 記号の衝突を解消し、用語を一本化する | 全体 | R1-M8, R1-M9 | 中 |
| P1-7 | Prop 6.5 の証明を付録へ移し、§2 の学習器の再録を §5 へ移す | 451–477, 1281–1407 | R2-M5 | 中 |
| P1-8 | 長さを 12〜13 頁に縮める（Lemma 2.1 等の証明、重複、Remark 5.7 の小節、考察の繰り返し） | 全体 | R1-M7, R2-M4 | 大 |
| P2-1 | frame 上界の一般原理（イデアルとの交わり）を述べる | 751–779 | R2-M1 | 中（任意だが評価を上げる） |
| P2-2 | Lemma 4.3 を族に依存しない形にする、または OP 8.3 に挑む | 781–828, 1509–1514 | R2-M2 | 大（研究） |
| P2-3 | JoLLI の書式（Statements and Declarations、Funding、commit permalink、行番号） | 1535–1556 | R2-m3, R2-m4 | 小 |
| P2-4 | Typo（297–298, 609, 319, 1059, 1065, 1084 行） | — | Typo | 小 |
| P2-5 | Python の引用で「到達しない分岐」を参照文献に帰さない。343–344 行を弱める。表の行名 | 207–209, 343–344, 1065 | R1-m2〜m4 | 小 |

---

## 付録 A：英語版の査読報告（要約版）

### Report of Reviewer 1

**Summary.** The paper compares frame-based (context) and exemplar-based (kernel) finite presentations of context-free grammars when a fixed finite-semigroup typing is available. The main result (Theorem A = Thm 4.5) shows that for the one-word deletion M_n = L_n \ {w\*_n} of the bracketed doubling family, an s_U-typed grammar with 2n nonterminals has the typed strong 1-FCP with contexts of length ≤ 2n. In contrast, every CFG for M_n with an SPP of the form (K_A^{▷◁}) satisfies ρ|N|max(κ,1) ≥ 3·2^{n−1}−1, under any typing. Theorem B describes how the typed FCP/FKP classes behave under refinement of the typing. I checked Lemma 3.7, Lemma 4.3, Theorem 4.4, Theorem 4.5, Prop 4.7 and Prop 5.5 line by line and found them correct. The finite checks supplied by the author and my own independent checks (n ≤ 4) all pass. The capture lemma with the covering count is a neat argument. However, most of the remaining text consists of known facts with proofs, trivial corollaries, repetitions and material transplanted from the author's earlier paper. Several summary sentences claim more than the theorems give.

**Recommendation: major revision.**

**Major comments.**
1. *Missing upper bound; restate Theorem A.* H_n itself has the typed strong 1-FKP with kernels {w\*_i} (type 1) and {u_i} (type ζ), so κ = |w\*_{n−1}| and ρ|N|κ ≤ 8n(3·2^{n−1}−2) (I verified this for n ≤ 4). Theorem 4.4 is therefore tight up to O(n). The gap is a gap in witness length on the *same* grammar. Please state Theorem A in this form (ll. 231–249, 830–861).
2. *Prop 4.7 is a trivial corollary.* Typed kernels are type-homogeneous, so κ ≥ max_μ min{|w| : w ∈ L ∩ F_μ}. This is exactly the quantity (♠) of [tcs1], whose Cor. 6.6 is the same statement for typed thickness. Reduce Prop 4.7 to one sentence, cite (♠)/Cor. 6.6, and tone down the four places that present it as an effect of observation (ll. 245–248, 263–265, 1062, 1443–1445).
3. *Attribution of learning lower bounds.* Prop 5.5 (dual learner) uses neither Lemma 4.3 nor Theorem 4.4. The abstract (ll. 83–85), the opening of §5 (ll. 917–919) and the conclusion (ll. 1527–1529) should not present it as a consequence of the gap; the discussion (ll. 1450–1456) already separates the two correctly.
4. *Scope of "learnable".* Line 284 says "every typing under which M_n is learnable", but Cor 5.2 assumes M_n ∈ C^cf_s. Use the latter wording.
5. *Proof gap and a dangling reference.* The proof of Prop 3.5 (ll. 636–637) assumes that d occurs at some stage j > i. Take instead any j > i with d ∈ D_j. The "as above" in Remark 3.6 (l. 668) refers to a normalization paragraph that was deleted in a later revision.
6. *Prop 6.4.* The proof of L_+ = {z}^{▷◁} (ll. 1229–1236) is prose, not a proof. It can be written in three lines.
7. *Length.* The paper could be written in about 12–13 pages. Candidates for cutting or shortening: proofs of standard lemmas (2.1, 2.2, 3.1, 3.2); the duplicate Definitions 3.3/3.4; the typed learners, which are needed only marginally; Remark 3.6 and Prop 4.6, which no proof uses; the duplication of Theorem 4.4 in Theorem 4.5(ii); the subsection devoted to the known Remark 5.7; the long proof of Prop 6.5 (move it to an appendix); and the repetitions in §7.
8. *Terminology.* The paper uses two parallel vocabularies (frame/context, exemplar/kernel, observer/typing, presentation/very weak property). Several terms are undefined: "isolated-fibre argument", "typed thickness", "set-driven", "ceiling", "licensing condition".
9. *Metavariables.* m, E, H, J, C, F, B, P, L_1, M, k, c, v, p, R and t are each used with two or three meanings (see the table in §2 of the Japanese report).
10. *Theorem statements.* Remove commentary from the statements: Theorem A (ll. 237–248), Theorem 4.4 ("of any cardinality"), Cor 5.2 (parenthetical proof), Cor 5.4 (last sentence), Prop 4.7 ("whatever bound k ...").

**Minor comments.**
- Lemma 5.1 is the soundness invariant of [tcs1, Thm 4.2]; say so.
- §6.2.9 of the Python reference does not mention unreachable branches.
- Weaken ll. 343–344: the lower bound does use a word of length 3·2^n − 2.
- The row "data at convergence" in the table of Remark 5.6 is a bound on the maximal datum length.
- Since M_n is finite, convergence of the KY learners is automatic; say so.
- In Prop 6.5(b), make explicit that C ⊆ L(G,B)^▷ and that C therefore contains no @.
- Use the notation of [tcs1] (L_n^−) for M_n.
- The fact M_n ∉ C^cf_{s_0} is in the proof, not the statement, of [tcs1, Prop 6.4].

**Typos.** l. 297–298 (repeated "Propositions"); l. 609 ("a (s-typed)"); l. 319 (F_t); l. 1059 ("poly data"); l. 1084.

### Report of Reviewer 2

**Summary.** The duality picture of Theorem B is attractive, and it partly addresses the question raised in my report on [tcs1] about the conditions a typing should satisfy. As it stands, however, no result of the paper actually depends on observation. The gap for L_n is definitional (Prop 4.7). The exemplar lower bound for M_n holds with no observer. Whether frames for M_n *need* the observer is open (OP 8.3). All results concern a single finite, artificial family.

**Recommendation: major revision (leaning reject in the present form).** Either settle OP 8.3, or generalize the capture lemma beyond this family, or align the title and abstract with what is proved.

**Major comments.**
1. *Role of the observer.* The frame upper bound uses only that M_n = L_n ∩ s_U^{−1}(ζ) and that every non-root context in H_n already contains a mark. State the general principle (intersection with an ideal of 𝖲^♯ preserves typed frame presentations under a stated condition). This gives a concrete answer to the question of which observers help frames.
2. *Scope.* Lemma 4.3 depends on deleting exactly one word. Formulate it for general languages (a long factor outside the difference between two words that differ at one node), and derive Theorem 4.4 as a corollary. Discuss infinite unions.
3. *Unused components.* Prop 4.6 (cited only in OP 8.3), Remark 3.6 (cited only in the introduction), Fact 2.3(c), the duplicate Definitions 3.3/3.4 and the typed dual learner.
4. *Forward references and repetition.* Theorem A in the introduction refers to Lemma 3.7, Prop 4.7 and [tcs1, Cor 6.6]. "What the observer buys" uses Cor 6.2, Rem 5.7 and Prop 5.5. Ll. 679–682 and 707–710 repeat the same sentence. Ll. 882–887 and 1434–1448 repeat earlier material.
5. *Appendix.* Move the 2.5-page proof of Prop 6.5 and the recap of the KY learners out of the main line.
6. *The Python example.* It is called a "licensing condition" in the introduction (l. 206) but "a classification of functions, not of syntactic validity" in the discussion (ll. 1469–1470). The exact-depth fragment is artificial. For a JoLLI readership, connect M_n to the agreement example 1.1 instead, and keep Python in the discussion or drop it.
7. *Measure.* Compare frames and exemplars with the same measure: ρ|N|ℓ = 16n² against ρ|N|max(κ,1) = Θ̃(2^n).

**Minor comments.**
- Consider a title that reflects that the lower bound is observer-free.
- Move the "Further questions" into the numbered open problems.
- Follow Springer's "Statements and Declarations" format and add a funding statement.
- Use a commit permalink or DOI for the scripts.
- Add line numbers to the English manuscript.

---

## 付録 B：自前の検証コード（`my_checks.py`）

実行：`python3 -I my_checks.py`（Python 3.13.18、約 4 秒）。出力は §1.3 の表のとおりで、最後の行は `ALL OK`。

```python
#!/usr/bin/env python3
"""Independent checks written for the TCS#1-lens review of paper 09 (commit 0fbc9e4).

Encoding: a -> 'a', floor ⌊ ⌋ -> '[' ']', ceil ⌈ ⌉ -> '{' '}'.
  (1) Matching exemplar UPPER bound for M_n (not stated in the paper):
      the s_U-typed grammar H_n has the typed STRONG 1-FKP with kernels
      {w*_i} for (E_i,1) and {u_i} for (E_i,zeta), and its untyped kernel family
      ({w*_i}^RL, {u_i}^RL) is an untyped SPP; kappa = |w*_{n-1}|.
  (2) Theorem 4.5(i): |N| = 2n, #productions = 6n-4, rho <= 4.
  (3) Prop 5.5: for EVERY datum of M_n, the context c read off it satisfies
      {c}^<| = L(E_{n-1}) relative to M_n, and {c}^<| ∩ F_1 = {w*_{n-1}}.
  (4) M_n not s_0-substitutable, M_n s_U-substitutable (n = 2,3).
  (5) Prop 6.4: bounded check of {z}^RL = L_+ and {y}^RL = L_-.
  (6) Prop 4.7: the type-1 fibre of L_n is {w*_n}.
"""
import itertools


def levels(n):
    E = [{'a'}]
    for _ in range(n):
        p = E[-1]
        E.append({'[' + x + y + ']' for x in p for y in p} | {'{' + x + '}' for x in p})
    return E


def wstar(i):
    w = 'a'
    for _ in range(i):
        w = '[' + w + w + ']'
    return w


def u(i):
    return '{' * i + 'a' + '}' * i


def typ(w):
    return 'e' if w == '' else ('Z' if '{' in w else '1')


def D(L, x):
    out = set()
    for m in L:
        s = m.find(x)
        while s != -1:
            out.add((m[:s], m[s + len(x):]))
            s = m.find(x, s + 1)
    return out


def closure_ctx(L, C):
    """C^<| over a finite L, for nonempty C (result is a set of factors)."""
    res = None
    for (p, q) in C:
        S = {m[len(p):len(m) - len(q)] for m in L
             if len(m) >= len(p) + len(q) and m.startswith(p) and m.endswith(q)}
        res = S if res is None else res & S
    return res


def closure_ker(L, K):
    C = set.intersection(*(D(L, k) for k in K))
    assert C, 'kernel without common context'
    return closure_ctx(L, C)


def check_upper(n):
    E = levels(n)
    Ln = E[n]
    Mn = Ln - {wstar(n)}
    NT = [(i, '1') for i in range(n)] + [(i, 'Z') for i in range(1, n + 1)]
    ker = {(i, '1'): {wstar(i)} for i in range(n)}
    ker.update({(i, 'Z'): {u(i)} for i in range(1, n + 1)})
    lang = {(i, '1'): {wstar(i)} for i in range(n)}
    lang.update({(i, 'Z'): E[i] - {wstar(i)} for i in range(1, n + 1)})
    P = [((0, '1'), ('a',))]
    for i in range(1, n):
        P.append(((i, '1'), ('[', (i - 1, '1'), (i - 1, '1'), ']')))
    for i in range(1, n + 1):
        for a_ in '1Z':
            for b_ in '1Z':
                if (a_, b_) == ('1', '1'):
                    continue
                if (i - 1, a_) in lang and (i - 1, b_) in lang:
                    P.append(((i, 'Z'), ('[', (i - 1, a_), (i - 1, b_), ']')))
            if (i - 1, a_) in lang:
                P.append(((i, 'Z'), ('{', (i - 1, a_), '}')))
    rho = max(len(r) for _, r in P)
    ok = (len(NT) == 2 * n and len(P) == 6 * n - 4 and rho <= 4)
    untyped = {}
    for A in NT:
        cl = closure_ker(Mn, ker[A])
        untyped[A] = cl
        typed = {x for x in cl if typ(x) == A[1]}
        if typed != lang[A]:
            ok = False
            print('  typed strong FKP FAIL', n, A)
    for A, rhs in P:
        prods = {''}
        for sym in rhs:
            if isinstance(sym, tuple):
                prods = {p + x for p in prods for x in untyped[sym]}
            else:
                prods = {p + sym for p in prods}
        if not prods <= untyped[A]:
            ok = False
            print('  untyped pre-fixed FAIL', n, A, rhs)
    if not untyped[(n, 'Z')] <= Mn:
        ok = False
        print('  untyped soundness FAIL', n)
    kappa = len(wstar(n - 1))
    prod = rho * len(NT) * kappa
    print(f'(1,2) n={n}: |N|={len(NT)} prods={len(P)} rho={rho} kappa={kappa} '
          f'rho|N|kappa={prod}  lower bound 3*2^(n-1)-1={3 * 2 ** (n - 1) - 1}  '
          f'ratio={prod / (3 * 2 ** (n - 1) - 1):.1f}  ok={ok}')
    return ok


def check_refutation(n):
    E = levels(n)
    Mn = E[n] - {wstar(n)}
    target = E[n - 1]
    ok = True
    for m in Mn:
        if m[0] == '{':
            c = ('{', '}')
        else:
            inner = m[1:-1]
            splits = [(inner[:k], inner[k:]) for k in range(1, len(inner))
                      if inner[:k] in target and inner[k:] in target]
            assert len(splits) == 1
            y, y2 = splits[0]
            c = ('[', y2 + ']') if typ(y2) == 'Z' else ('[' + y, ']')
        cl = closure_ctx(Mn, [c])
        if cl != target or {x for x in cl if typ(x) == '1'} != {wstar(n - 1)}:
            ok = False
            print('  refutation FAIL', n, m, c)
    print(f'(3) n={n}: all {len(Mn)} data give c with {{c}}^<|=L(E_{n-1}), fibre-1 part={{w*_{n-1}}}: {ok}')
    return ok


def substitutable(L, typer):
    facs = {}
    for m in L:
        for i in range(len(m)):
            for j in range(i + 1, len(m) + 1):
                facs.setdefault(m[i:j], set()).add((m[:i], m[j:]))
    byctx = {}
    for x, cs in facs.items():
        for c in cs:
            byctx.setdefault((typer(x), c), []).append(x)
    for xs in byctx.values():
        for y in xs[1:]:
            if facs[y] != facs[xs[0]]:
                return False, (xs[0], y)
    return True, None


def check_subst(n):
    Mn = levels(n)[n] - {wstar(n)}
    s0 = substitutable(Mn, lambda w: 0)
    sU = substitutable(Mn, typ)
    print(f'(4) n={n}: M_n s0-substitutable={s0[0]} (witness {s0[1]}), sU-substitutable={sU[0]}')
    return (not s0[0]) and sU[0]


def check_LK(maxlen=7, B=12):
    """Prop 6.4 on bounded fragments."""
    def inLK(w):
        if set(w) <= set('ab'):
            k = len(w) - len(w.lstrip('a'))
            return w == 'a' * k + 'b' * (len(w) - k) and k != len(w) - k
        for mark, rel in (('z', lambda m, n: n <= m), ('y', lambda m, n: m <= n)):
            if w.count(mark) == 1 and set(w) <= set('ab' + mark):
                l, r = w.split(mark)
                if set(l) <= {'a'} and set(r) <= {'b'} and rel(len(l), len(r)):
                    return True
        return False
    ok = True
    ctx = [(('a' * p), ('b' * q)) for p in range(B) for q in range(B)]
    Dz = [(p, q) for p, q in ctx if inLK(p + 'z' + q)]
    Dy = [(p, q) for p, q in ctx if inLK(p + 'y' + q)]
    assert all(len(p) >= len(q) for p, q in Dz) and all(len(p) <= len(q) for p, q in Dy)
    for L in range(maxlen + 1):
        for t in itertools.product('abyz', repeat=L):
            x = ''.join(t)
            inz = all(inLK(p + x + q) for p, q in Dz)
            iny = all(inLK(p + x + q) for p, q in Dy)
            def Lplus(w):
                if set(w) <= set('ab') and inLK(w):
                    k = len(w) - len(w.lstrip('a'))
                    return k > len(w) - k
                return 'z' in w and inLK(w)
            def Lminus(w):
                if set(w) <= set('ab') and inLK(w):
                    k = len(w) - len(w.lstrip('a'))
                    return k < len(w) - k
                return 'y' in w and inLK(w)
            if inz != Lplus(x) or iny != Lminus(x):
                ok = False
                print('  LK FAIL', x, inz, Lplus(x), iny, Lminus(x))
                return False
    print(f'(5) Prop 6.4: {{z}}^RL = L_+ and {{y}}^RL = L_- on all words of length <= {maxlen} '
          f'(contexts a^p,b^q with p,q < {B}): {ok}')
    return ok


def check_isolated_fibre(n):
    Ln = levels(n)[n]
    f1 = {x for x in Ln if typ(x) == '1'}
    print(f'(6) n={n}: type-1 fibre of L_n = {{w*_n}}: {f1 == {wstar(n)}}')
    return f1 == {wstar(n)}


if __name__ == '__main__':
    res = []
    for n in (2, 3, 4):
        res.append(check_upper(n))
    for n in (2, 3, 4):
        res.append(check_refutation(n))
    for n in (2, 3):
        res.append(check_subst(n))
    res.append(check_LK())
    for n in (1, 2, 3, 4):
        res.append(check_isolated_fibre(n))
    print('ALL OK' if all(res) else 'SOME CHECK FAILED')
```

（Python の挙動の確認には、別に 6 つの関数定義を `inspect.isgeneratorfunction` で判定する短いスクリプトを使った。結果は §1.3 の表のとおり。日英の比較スクリプトは、定理類の環境と本文の数式を正規化して多重集合で比べるもので、結果は §6.1 のとおり。）
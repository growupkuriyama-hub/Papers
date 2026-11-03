# b と c の両方を含む逃げ道：全内容スペクトルによる多項式上界と、影の抽出不能例

**研究日：** 2026-11-03  
**対象：** 栗山貴之、論文 #2 `op:fanout-two`、三文字内容型付け  
**現行ソース：** [`02-v2-lg-fanout-boundary/main.tex`](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/main.tex)、取得した Git blob SHA `b72cd2ed648f802886f0ab7c60a72f9f40c0864b`。  
**位置づけ：** 第七報。中心の未解決問題の肯定・否定のいずれも解決していない。ただし、前回の補題 M を強化する**新しい条件付き多項式上界**を得た。文献上の新規性は未確認。

## 0. 主張別判定表

| 主張 | 判定 | 根拠 |
|---|---|---|
| 短い両文字代表を持つ一つの重い非終端の、最短純粋語導出中での出現数は `m+1` 以下 | **証明済み** | §2、補題 2.1 |
| **全内容スペクトル上界** `k ≤ 19(r+1)^3 v^3 θ^3(θ+m+20)^3` | **証明済み** | §3、定理 3.1 |
| したがって超多項式の `k` を持つ反例族は、全内容語の相異なる `a` 個数を超多項式種類必要とする | **証明済みの必要条件** | §4.1 |
| その各個数は相異なる `a` 骨格で実現されねばならない | **証明済みの必要条件** | §4.2 |
| 全ての重い非終端が短い両文字代表を持つ場合、`k ≤ (r+1)vθ(m+1)` | **証明済み（強い追加仮定）** | §4.3 |
| `a^k,b^4,c^4∈L` でも、`a,b` だけ／`a,c` だけの受理語が存在しない例 | **反例を構成、全 arity の代入可能性を証明** | §5 |
| `A_i→A_{i-1}A_{i-1} \mid (bc)^+` 型の自然な候補 | **反証（`n=2`、arity 1）** | §6・§7 |
| 新しい一般の影の抽出、`m` 自体の多項式上界、または `op:fanout-two` の最終解決 | **未解決** | §8 |
| 新結果と同一の先行定理の不存在 | **未確認** | §9 |

**要旨。** `m` は、言語中で内容がちょうど `{a,b,c}` であり、`a` の個数が `1,…,k−1` である語に現れる **異なる `a` 個数の数**である。この `m` を追加パラメータとすれば、短い二文字の逃げ道が存在しない重い非終端も「例外」として数えられる。これを前回の補題 M の二色・損失比の帰納に組み込むと、上記の多項式が得られる。**`m` が文法パラメータの多項式であることは示せていない**ため、中心問題はなお残る。

---

## 1. 設定と、使用する既報の再点検

`Σ={a,b,c}`、`c(w)` は非空語の文字集合、`L∈𝒞_{2,c}`。`G=(V,Σ,P,S,fan)` は `L∩Σ⁺` の reduced good な MCFG 表示、`fan≤2`、`rank≤r`（`r≥2`）、`v=|V|≥1`、`θ=θ̄_G≥1`。`k=μ_a(L)=min{j≥1:a^j∈L}≥5` とする。`T` は `a^k` の節点数最小の成功導出木である。節点 `u` の生成組の総長を `ℓ_u` と呼び、`ℓ_u>θ` の節点を **重い**という。

ここで

\[
\mathcal A_{abc}(L;k)=\{j\in\{1,\dots,k-1\}:\exists w\in L,\ c(w)=\{a,b,c\},\ |w|_a=j\},
\qquad m=|\mathcal A_{abc}(L;k)|.
\tag{1.1}
\]

必ず `0≤m≤k−1` であり、`m` は**語数**ではなく、**`a` 個数の異なる値の個数**である。以後 `m` に文法サイズ由来の上界を暗黙に仮定しない。

### 1.1 原稿から直接確認した基本事項

`main.tex` の `def:grammar-properties`、`def:tuple-substitutable`、`lem:thickness-equivalence` を再確認した。good は λ-free / nondeleting / nonpermuting / nonmerging を意味し、全成分は非空。reduced good 性から、各非終端 `B` には長さ `≤θ` の生成組 `ρ_B` があり、各規則が直接書く終端数は `≤θ`。またファンアウト2の許容二穴文脈は、**二穴の間に非空の固定語**を持つ。

`T` の同一根葉経路に同名非終端 `B` が二度現れることはない。祖先の `B` を子孫の `B` に置き換えると、非削除性により語長は増えない。短くなれば `k` の最小性に、同長なら `T` の節点数最小性に反する。よって

\[
\operatorname{height}(T)\le v,\qquad
\text{同名非終端の出現は互いに比較不能。}\tag{1.2}
\]

重い節点の数を `N` とすると、根が重い場合、その直接書込みと重くない子の語に分解して

\[
k\le N(\theta+r\theta)=N(r+1)\theta.
\tag{1.3}
\]

根が重くない場合は `k≤θ`。重い節点集合は祖先に関して上閉なので、この数え上げに抜けはない。

一方、重い `B` の長さ `≤θ` の生成組が純粋 `a` だけなら、その出現を差し替えて `a^j∈L`、`1≤j<k` が得られる。従って**重い非終端の短い生成組には必ず `b` または `c` が入る**。

### 1.2 前回の補題 M の使用範囲

[第六報 `chatgpt_mixed_escapes_2026-11-03.md`](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/reviews/chatgpt_mixed_escapes_2026-11-03.md) の補題 M は、「**全ての重い非終端**に短い二文字逃げ道がある」場合に適用できる。逆に、巨大な `k` をもつ族に必要なのは、短い二文字逃げ道を欠く非終端が**少なくとも一つ**あることだけである。「全ての重い非終端が (★)」という強い仮定へ置き換えてはならない。

以下では補題 M をブラックボックスとして適用せず、その二文字ラン障害、行の剛性、頻出ラベルの比、二段刈込みの論理を再検証し、**両文字型節点を例外に加えた証明**を §3 に記す。

---

## 2. 新しい補題：両文字代表の出現回数は全内容スペクトルで抑えられる

**補題 2.1（両文字代表の出現数）。** `B` は `T` に重い出現を持つ非終端であり、`ρ_B∈L_B(G)` が

\[
\|\rho_B\|_1\le\theta,
\qquad |\rho_B|_b\ge1,\quad |\rho_B|_c\ge1
\tag{2.1}
\]

を満たすとする。ここで `|ρ_B|_x` は成分全体における文字数の和である。このとき、`T` における `B` の**重い出現数**は高々 `m+1`。

**証明。** `T` の一番左の `a` の位置を一つ保護する。式 (1.2) により、`B` の全ての出現は反鎖をなし、同じ位置を所有する出現は高々一つである。保護位置を含まない重い `B` の出現を `u_1,…,u_q` と並べる。

各 `u_i` に対して

\[
d_i:=\ell_{u_i}-|\rho_B|_a\ge\ell_{u_i}-\|\rho_B\|_1>0.
\]

初めの `j` 個の出現の生成組を同時に `ρ_B` に差し替える（`1≤j≤q`）。互いに比較不能なので合法な成功導出のままであり、根の語 `W_j` は `L` に属する。`ρ_B` が `b,c` を含み、保護した `a` は全置換の外にあるから `c(W_j)={a,b,c}`。さらに

\[
1\le |W_j|_a=k-\sum_{i=1}^{j}d_i<k.
\]

`d_i>0` ゆえに `|W_1|_a,…,|W_q|_a` は**互いに異なる**。したがって `q≤m`。保護位置を含む可能性のある一出現を戻すと、全重い出現数は `≤m+1`。□

**注意。** これは `B` 一つについての命題である。`B` の子孫の他の非終端に二文字逃げ道があっても使える。従って、依頼の局所条件 (★) に**そのまま適用できる**。逆に、`m` が大きいと出現数上界は弱い。

### 2.2 非終端の色分け

重い出現をもつ各非終端の長さ `≤θ` の生成組を調べ、次のいずれかに分類する。

- **一色型**：`{a,b}` のみで `b` を含む短い生成組、または `{a,c}` のみで `c` を含む短い生成組がある。どちらか一つをラベル単位で固定し、色 `x(B)∈{b,c}` と代表 `ω_B` を選ぶ。
- **両文字型**：そのような一色の短い生成組がない。このとき §1.1 により純粋 `a` の短い生成組もないので、**長さ `≤θ` の全生成組が `b,c` 双方を含む**。一つ `ρ_B` を選ぶ。

両文字型非終端の重い出現総数は、補題 2.1 によって

\[
N_{bc}\le v(m+1).
\tag{2.2}
\]

これが第六報にはなかった計数である。二文字逃げ道が**任意の長さ**で存在しないとまでは要求しない。長さ `≤θ` に制限した分割で足りる。

---

## 3. 主結果：全内容スペクトルをパラメータとする多項式上界

**定理 3.1（全内容スペクトル上界）。** §1 の全条件の下で

\[
\boxed{\displaystyle
k\le19(r+1)^3v^3\theta^3\bigl(\theta+m+20\bigr)^3.}
\tag{3.1}
\]

特に `r` 固定で `v,θ,m` が `n` の多項式なら、`μ_a(L)` も `n` の多項式である。`m=0` の場合には `k=O_r(v^3θ^6)`。

### 3.1 二文字影と非飽和色の例外数（再確認）

`x∈{b,c}` に対し `L_x=L∩{a,x}⁺` とする。`L_x` は `(2,c_{\{a,x\}})`-代入可能である。実際、二文字上の許容文脈における共通受理を三文字上の代入可能性へ入れてから、その文脈に戻せばよい。なお、**切り出した文法の厚さを `θ` で抑えたとは主張しない**。

`a^k` の因子として `a⁴` が現れる。原稿 `lem:app-two-runs` と `lem:app-two-alternate` の次の二文字帰結を確認する。

> `L_x` が Parikh 飽和でなければ、`aa` を因子に持ち、互いに異なる内部 `x`-ランを二つ以上持つ語は `L_x` にない。

確認の要点は次のとおり。`(a,aa)` と `(aa,a)` は、共通する二穴文脈 `□₁a□₂`（実際の `a⁴` の左右文脈付き）を受理し、成分の内容が一致する。従って `a`-ラン間の一文字再配分が可能である。内部の `x`-ランが1文字なら、再配分で `aaxa` または `axaa` 型を作り、`ax` と `xa` に共通の一穴文脈が生じるので、Parikh 飽和を強制する。したがって非飽和なら二つの内部 `x`-ランは長さ `≥2`。`x⁴` が現れない場合、その二つの `x`-ランを合流させる代入により `x⁴` を作る矛盾が得られる。`x⁴` も現れる場合、原稿 `lem:app-two-alternate` により四ラン以上の受理語の**全**ランが長さ1となり、`aa` に反する。いずれも二文字影の**内部だけ**の議論である。

非飽和色 `x` の一色型・重い節点からなる反鎖が10個あれば、根の最初と最後の各2個の `a` を保護し、少なくとも6節点を保護外に選べる。各節点は最大2区間を所有し、区間の隣接グラフの最大次数は `≤4`。よって非隣接の2節点を選び、双方を `ω_B` に差し替える。得られる語は**第三の文字を含まない** `L_x` の語で、`aa` と二つの分離した内部 `x`-ランを持つ。上の帰結に矛盾する。したがって非飽和色について、各深さの重い節点は高々9個、深さは `≤v`。二色合計の例外数は

\[
N_{\mathrm{nonsat}}\le18v.
\tag{3.2}
\]

### 3.2 飽和色の行の剛性と頻出比（再確認）

`L_x` が Parikh 飽和であるとする。`(p,q)` と `(p+δ,q)` がともにその Parikh 像に入り、`p≥1`、`1≤δ<k` なら、飽和性から `x^q a^p` と `x^q a^{p+δ}` が受理される。両語はある一穴文脈で `a` と `a^{1+δ}` を受理するから、代入可能性により `D_L^{(1)}(a)=D_L^{(1)}(a^{1+δ})`（正確には `L_x` での分布等式）を得る。`a^k` 中の `a^{1+δ}` を `a` に縮めれば `a^{k-δ}∈L_x` となる矛盾。よって

\[
(p,q),(p+\delta,q)\in\Psi(L_x),\ p\ge1,\ 0<\delta<k
\quad\text{は不可能。}\tag{3.3}
\]

飽和色 `x` に割り当てられた重い出現が **`θ` 回を超える**非終端 `B` を頻出と呼ぶ。選んだ短い代表の `a,x` 個数を `p_B,q_B` とする：`p_B+q_B≤θ`、`q_B≥1`。同じ `B` の重い出現は反鎖である。一出現だけ差し替える語は `x` 個数 `q_B`、`a` 個数 `k−(ℓ_u−p_B)` を持ち、未置換の他の `B` が残るので `a` は1個以上。式 (3.3) より、同じ `B` の各重い出現の損失 `g_B=ℓ_u−p_B` は一定。

同色の二つの頻出ラベル `B,C` に対し、それぞれ `q_C` 個の `B` 出現を差し替えた語と、`q_B` 個の `C` 出現を差し替えた語を比べる。`q_B,q_C≤θ` なのでいずれも元の同名出現を一つ以上残し、`a` は正、`x` 個数はともに `q_Bq_C`。式 (3.3) より `q_Cg_B=q_Bg_C`。従って、色 `x` の全頻出ラベルに共通な正の比 `α_x` があり、

\[
\alpha_x=g_B/q_B>0,\qquad
\alpha_x\le\ell_u=p_B+\alpha_xq_B\le\theta(1+\alpha_x)
\tag{3.4}
\]

が各頻出出現に成り立つ。**`α_b=α_c` とは言っていない**。色 `x` に頻出ラベルがなければ `α_x` は定義しない。

### 3.3 全例外数と二段刈込み

次を例外節点と呼ぶ：非飽和色の一色型重い節点、飽和色だが非頻出の一色型重い節点、両文字型重い節点。式 (3.2)、非頻出の定義、式 (2.2) から、例外節点の総数は

\[
E:=v(\theta+m+19)
\tag{3.5}
\]

以下で抑えられる。残る重い節点は、飽和色の頻出節点であり、比は最大二種類だけである。置く：

\[
\begin{aligned}
H&:=v\theta+E=v(2\theta+m+19),\\
A_1&:=(r+1)\theta H, &P_1&:=\theta(1+A_1),\\
A_2&:=H(\theta+rP_1), &P_2&:=\theta(1+A_2).
\end{aligned}\tag{3.6}
\]

**第一段階。** 頻出比が存在すれば最小のものを `α₁` とする。その頻出節点 `u` の長さは `ℓ_u≤θ(1+α₁)`。`α₁≤θ` なら既に `α₁≤A₁`。そうでなければ、`u` 以下の**どの色**の頻出節点も長さが `≥α₁>θ` である。一深さにある頻出節点の生成長は合計 `≤ℓ_u` なので、その個数は `≤⌊θ(1+α₁)/α₁⌋≤θ`。深さ `≤v` から頻出節点は `≤vθ` 個、例外は `≤E` 個。合計 `≤H` 個の重い節点があり、式 (1.3) の部分木版を適用して

\[
\alpha_1\le\ell_u\le H(r+1)\theta=A_1.
\]

その色の**全頻出節点**の長さは `≤P₁`。

**第二段階。** 頻出比が二色に存在すれば、大きい方を `α₂` とする。`α₂≤P₁` なら自明に `α₂≤A₂`（式 (3.6)）。`α₂>P₁≥θ` の場合、この色の頻出節点 `u` から下の導出木を、第一段階の色の頻出節点に到達したら**長さ `≤P₁` の部分木として停止**し、軽い子でも停止する。停止前の core 節点は大きい比の頻出節点か例外節点だけである。前者は一深さ `≤θ` 個（各長さ `≥α₂`、根長 `≤θ(1+α₂)`）、総数 `≤vθ`。後者を足して core は `≤H` 節点。各 core が直接書く終端は `≤θ`、停止した子は一つ `≤P₁` なので

\[
\alpha_2\le\ell_u\le H(\theta+rP_1)=A_2.
\]

よって、二色のどの頻出節点も `ℓ_u≤P₂`。頻出比がゼロまたは一種類のときも同じ上界が成立する（頻出比なしなら空虚）。

従って長さ `>P₂` の節点は**全て例外**、個数 `≤E`。大きい節点の直書きと大きくない子の出力に分ければ

\[
\boxed{k\le E\theta+(1+rE)P_2.}\tag{3.7}
\]

根に大きい節点がない場合は `k≤P₂` であり、同式がその場合も含む。

### 3.4 明示定数の検算

`Q:=θ+m+20` と置く。`r≥2, v,θ≥1, m≥0` から

\[
E\le vQ,\quad H\le2vQ,\quad
A_1\le2(r+1)v\theta Q,\quad
P_1\le3(r+1)v\theta^2Q,
\]

\[
A_2\le8r(r+1)v^2\theta^2Q^2,\qquad
P_2\le9r(r+1)v^2\theta^3Q^2,
\qquad1+rE\le2rvQ.
\]

したがって

\[
\begin{aligned}
k&\le vQ\theta+18r^2(r+1)v^3\theta^3Q^3\\
 &\le19(r+1)^3v^3\theta^3Q^3.
\end{aligned}
\]

これは定理 (3.1) である。係数比較は `1≤r+1`、`v,θ,Q≥1` による。さらに、式 (3.5)–(3.7) と最終 19 係数の大小を `r=2,3,4`、`v=1,…,4`、`θ=1,…,6`、`m=0,…,8` の整数範囲で算術検査し、違反はなかった。この検査は**数学的証明の代用ではなく**上記不等式の実装上の確認である。□

---

## 4. 肯定側への帰結と、残る障害の定量化

### 4.1 超多項式反例に必要な全内容スペクトルの豊かさ

`r` 固定で `v_n,θ_n=n^{O(1)}`、`k_n=μ_a(L_n)=n^{\omega(1)}` とすると、(3.1) より

\[
m_n\ge
\left(\frac{k_n}{19(r+1)^3v_n^3\theta_n^3}\right)^{1/3}
-\theta_n-20.
\tag{4.1}
\]

従って **`m_n=n^{\omega(1)}` が必要**。特に `k_n≥2^{cn}` で `v_n,θ_n=poly(n)` なら `m_n≥2^{\Omega(n)}`。単に短い mixed-content 語が多数存在するだけでは足りず、`1,…,k−1` の範囲に**異なる `a` 個数が指数的に多数**必要になる。

### 4.2 その個数は互いに異なる `a` 骨格を必要とする

前回の[スペクトル報告](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/reviews/chatgpt_a_spectrum_2026-11-03.md)の定理 S の、ここで必要な部分を独立に確認する。`a⁴` が現れるので `(a,aa)` と `(aa,a)` の二穴分布が一致し、`a` ラン間で一文字ずつ再配分できる。同じ `a` 骨格の受理語に `a` 個数差 `0<δ<k` があれば、余剰を一つの `a` ランへ集め、一穴の共通文脈で `a` と `a^{1+δ}` を受理させる。よって両者の一穴分布が一致し、`a^k` を `a^{k-δ}` に縮められる。矛盾する。

ゆえに、(1.1) で数えた `m` 種類の `a` 個数を実現する全内容語は、**少なくとも `m` 種類の異なる `a` 骨格**を持つ。これは単なる Parikh 像の豊かさでなく、`b,c` だけからなる隙間の**配置・文字列の多様性**を要求する。もっとも、これだけで隙間の複雑さが文法サイズの下界になるとは示せていない。

### 4.3 全ての重いラベルが両文字型の場合にはより鋭い上界

ここだけは**依頼の (★) より強く**、`T` の全ての重い節点のラベルが、長さ `≤θ` で `b,c` を共に含む生成組を持つと仮定する。補題 2.1 を全ラベルに適用すれば重い節点は `≤v(m+1)` 個。式 (1.3) より

\[
\boxed{k\le(r+1)v\theta(m+1).}\tag{4.2}
\]

従ってこの特別な場合には `m≥k/((r+1)vθ)−1` が必要で、指数 `k` はほぼ同じ指数規模の全内容スペクトルを要求する。**全ての重い節点**という追加条件を、補題 M から勝手に導いてはいない。

---

## 5. `b⁴,c⁴` が受理されても、`a` と一文字だけの混合語は強制されない

「`b⁴` と `c⁴` の両方が `L` にある」あるいは「全内容の短い語がある」という事実だけで、全内容語の `c` を消して **`a,b` の双方を含む語**へ、または `b` を消して **`a,c` の双方を含む語**へ移す推論は**できない**。次は全 arity で内容代入可能な具体例である。純粋な `b⁴,c⁴` 自身はもちろん二文字部分言語に属するが、それは特定の重い非終端の生成組を与えることを意味しない。

**命題 5.1（影の抽出に対する内容障壁）。** 任意の整数 `k≥5` に対し

\[
\begin{aligned}
F&=\{w\in\{a,b,c\}^+:c(w)=\{a,b,c\},\ |w|_a=|w|_b,\ |w|_c=4\},\\
L^{\dagger}_k&=\{a^k,b^4,c^4\}\ \cup\ F.
\end{aligned}\tag{5.1}
\]

とする。このとき：

1. `L†_k` は文脈自由であり、**すべての `d≥1`** について `(d,c)`-tuple-substitutable。従って `L†_k∈𝒞_{2,c}`。
2. `μ_a(L†_k)=k`、`a^k,b⁴,c⁴∈L†_k`。全内容の**短い語** `abcccc` も受理する。
3. `L†_k∩{a,b}⁺={a^k,b^4}`、`L†_k∩{a,c}⁺={a^k,c^4}`。特に、`a` と `b` を共に含む二文字語も、`a` と `c` を共に含む二文字語も**一つも存在しない**。
4. `m(L†_k,k)=k−1`。実際、全ての `j≥1` に対して `a^j b^j c^4∈F`。

**証明。** `F` は `{w:|w|_a=|w|_b}` と正則条件 `c(w)=Σ, |w|_c=4` の共通部分だから文脈自由（`#a=#b` の言語は CFL で、正則言語との共通部分も CFL）。有限集合との和も CFL。

任意の arity `d` で、成分ごとの内容が等しい二組 `X,Y` が、ある許容文脈 `E` を共通に受理するとする。各文字について成分全体の個数差を `Δ_a,Δ_b,Δ_c` と置く。成分の内容が等しいので、どの文脈で埋めても完成語の**内容**は `X` と `Y` で一致する。

共通受理語の内容が `{a}`、`{b}`、`{c}` なら、受理語はそれぞれ唯一の `a^k`、`b^4`、`c^4` であるから、当該文字数の差は0、他の文字差も0、すなわち `Δ=(0,0,0)`。従って全ての文脈で受理結果は同じである。

共通受理語の内容が `Σ` なら、式 (5.1) の条件から `Δ_a−Δ_b=0` および `Δ_c=0`。他の任意の文脈でも、完成語の内容が `Σ` なら、`|w|_a−|w|_b` と `|w|_c` の条件は両者で一致する。完成語が二文字の内容ならどちらも不受理。完成語が純粋一文字なら、組 `X,Y` の各成分もその文字だけからなるので、`Δ_a−Δ_b=0, Δ_c=0` から、その一文字の個数差も0である（`a` の場合 `Δ_b=0`、`b` の場合 `Δ_a=0`、`c` の場合 `Δ_c=0`）。従って単語 `a^k,b⁴,c⁴` への所属も一致する。以上より全ての許容文脈で同時に受理／不受理であり、全 arity の代入可能性が従う。残りの項目は定義から直接従う。□

**射程の注意。** この命題は**言語レベルの代入可能性から全内容語の一文字を消した混合語は強制できない**ことの反例であり、`L†_k` に `θ=poly(log k)` の reduced good ランク2表示があるとは主張していない。また、特定の非終端が (★) を満たすとは示していない。従って `op:fanout-two` の反例ではない。`m=k−1` なので、定理 3.1 の `m` を取り除く論証にもならない。

この例は同時に、`b⁴,c⁴` の存在、全内容語の存在、全 arity の代入可能性、無数の全内容 `a` 個数が**互いに両立**することを示す。`b,c` のどちらかを消すには、これらの一般条件だけでなく、**短い文法導出から得られる共通文脈の具体的構造**が必要である。

---

## 6. 自然な反例候補の正確な反証

依頼にある無限の逃げ道 `D=(bc)^+` を用いた文法を

```text
A_0 -> a | D
A_i -> A_(i-1) A_(i-1) | D     (i >= 1)
D   -> bc | bc D
start A_n
```

とする。`n=2` では、ユーザー提示の arity 1 違反に加えて、**もっと短い証明書**がある。

\[
X=(bcbc),\qquad Y=(bc),\qquad c(X)=c(Y)=\{b,c\}.
\]

**共通受理文脈**は `E=□`：`bcbc,bc∈L(G_2)`（いずれも `A_2→D`）。しかし**食い違う文脈** `F=□a` において

\[
F[X]=bcbca\in L(G_2),\qquad F[Y]=bca\notin L(G_2).
\tag{6.1}
\]

前者の導出は `A₂→A₁A₁`、左の `A₁→D→bc`、右の `A₁→A₀A₀→bc\,a` である。後者は `D` の語でなく、`A₂→A₁A₁` の両側の長さが各 `≥2` なので長さ3では導けない。よって **`G₂` は arity 1 で内容代入可能でない**。これは無限言語全体に対する真の反証であり、長さ上限による推定ではない。

依頼に記載された別の証明書についても、正確な所属判定器で

```text
aabcbc   : True
aaabcbc  : True
aaabc    : True
aaaabc   : False
```

を再確認した。相異なる文脈で `a` と `aa` の分布が一致しない。

---

## 7. Python 3 標準ライブラリによる検査

以下は**全文**。Windows で `py -3 bc_escapes_check.py` として実行できる。`compressed_D_model(n)` は対象となる無限 CFG の**全ての入力語**に対して、任意の分割点を再帰的に調べる**正確な所属判定器**である。`modular_model(k)`（実際には命題 5.1 の CFL の所属述語）も正確である。`test_observed` は受理語を指定した長さまで列挙し、arity 1 と2の全ての**観察された**組・許容文脈を集める。**違反があれば本物の証明書、見つからなければ有限長の観察にすぎない**。

```python
# Python 3 standard library only; runnable: py -3 bc_escapes_check.py
from collections import defaultdict
from functools import lru_cache
from itertools import product


def content(w):
    return frozenset(w)


def occurrences(w, d):
    n = len(w)
    if d == 1:
        for i in range(n):
            for j in range(i + 1, n + 1):
                yield (w[i:j],), (w[:i], w[j:])
    else:
        for i in range(n):
            for j in range(i + 1, n):
                for p in range(j + 1, n):
                    for q in range(p + 1, n + 1):
                        yield (w[i:j], w[p:q]), (w[:i], w[j:p], w[q:])


def fill(ctx, tup):
    if len(tup) == 1:
        return ctx[0] + tup[0] + ctx[1]
    return ctx[0] + tup[0] + ctx[1] + tup[1] + ctx[2]


def test_observed(member, length_max, alphabet='abc'):
    positive = []
    for n in range(1, length_max + 1):
        for letters in product(alphabet, repeat=n):
            w = ''.join(letters)
            if member(w):
                positive.append(w)
    for d in (1, 2):
        contexts = defaultdict(set)
        shared = defaultdict(set)
        for w in positive:
            for tup, ctx in occurrences(w, d):
                contexts[tup].add(ctx)
                shared[(tuple(map(content, tup)), ctx)].add(tup)
        for (typ, ctx), tuples in shared.items():
            if len(tuples) < 2:
                continue
            first = min(tuples)
            for second in sorted(tuples):
                if first == second:
                    continue
                for p, q in ((first, second), (second, first)):
                    for e in sorted(contexts[p]):
                        u, v = fill(e, p), fill(e, q)
                        if not member(v):
                            return len(positive), {
                                'arity': d,
                                'types': [sorted(t) for t in typ],
                                'x': p, 'y': q,
                                'common': ctx, 'different': e,
                                'accepted': u, 'rejected': v,
                            }
    return len(positive), None


def modular_model(k):
    # Exact membership: a singleton a^k, b^4, c^4, plus balanced abc with four c.
    def member(w):
        if w in ('a' * k, 'bbbb', 'cccc'):
            return True
        return set(w) == set('abc') and w.count('a') == w.count('b') and w.count('c') == 4
    return member


def compressed_D_model(n):
    # A_0 -> a | D ; A_i -> A_(i-1) A_(i-1) | D ; D -> bc | bc D.
    # Exact for all input lengths; no bounded derivation approximation.
    @lru_cache(None)
    def is_A(i, w):
        if len(w) >= 2 and len(w) % 2 == 0 and w == 'bc' * (len(w) // 2):
            return True
        if i == 0:
            return w == 'a'
        for cut in range(1, len(w)):
            if is_A(i - 1, w[:cut]) and is_A(i - 1, w[cut:]):
                return True
        return False
    return lambda w: is_A(n, w)


def emit(name, member, cap):
    count, witness = test_observed(member, cap)
    print(name, 'bound', cap, 'positive-count', count)
    if witness is None:
        print('  NO WITNESS IN THIS BOUNDED SEARCH (observation only)')
    else:
        print('  EXACT FAILURE CERTIFICATE:', witness)
        print('  common:', fill(witness['common'], witness['x']),
              fill(witness['common'], witness['y']))
        print('  separating:', witness['accepted'], witness['rejected'])

if __name__ == '__main__':
    emit('CFL all-arity model k=5', modular_model(5), 8)
    emit('naive doubling with (bc)^+ n=2', compressed_D_model(2), 7)
    bad = compressed_D_model(2)
    print('  user-supplied witness exact:',
          bad('aabcbc'), bad('aaabcbc'), bad('aaabc'), bad('aaaabc'))
```

**実行結果（Python 3）：**

```text
CFL all-arity model k=5 bound 8 positive-count 453
  NO WITNESS IN THIS BOUNDED SEARCH (observation only)
naive doubling with (bc)^+ n=2 bound 7 positive-count 27
  EXACT FAILURE CERTIFICATE: {'arity': 1, 'types': [['b', 'c']],
    'x': ('bcbc',), 'y': ('bc',), 'common': ('', ''),
    'different': ('', 'a'), 'accepted': 'bcbca', 'rejected': 'bca'}
  common: bcbc bc
  separating: bcbca bca
  user-supplied witness exact: True True True False
```

最初の対象（`L†_5`）の無違反は**観察**。その全 arity の正しさは §5 の**一般証明**による。二番目の違反は、判定器が任意長の語に対して正確なので**反証**。計算は主定理 (3.1) の証明を代替していない。

---

## 8. 厳密な到達点、未解決部分、次の一点

### 8.1 今回できたこと

補題 M の「全重い非終端が短い二文字逃げ道を持つ」という前提を外し、**短い両文字代表しか持たない非終端の出現数を全内容スペクトル `m` で計数する**ことに成功した。全重い節点を漏れなく分類して二段刈込みを行ったため、`m` を追加変数とする一様な多項式上界 (3.1) が得られた。条件 (★) の非終端**一つ**についても補題 2.1 が適用できる。

その結果、真の超多項式反例を作るには、短い `bc` 代替を使った導出を、`a` 個数が超多項式に多様な**全内容の語**へ展開できなければならない。さらに定理 S によって、それぞれが異なる `a` 骨格を必要とする。この条件は、過去の「少数の符号・少数の骨格」候補を評価する際の有用な足切りになる。

### 8.2 今回できなかったこと

- 一般の `(★)` から短い `{a,b}` または `{a,c}` の生成組を抽出すること。
- `m` を `‖G‖,θ` の多項式で抑えること。命題 5.1 は `m` 自体が大きくても内容代入可能性に矛盾しないことを示している。
- `G_n` が reduced good、fan-out `≤2`、rank `≤2`、`‖G_n‖,θ̄_{G_n}=poly(n)`、`μ_a(L_n)=n^{ω(1)}` を**同時に満たす**族を構成すること。
- `op:fanout-two`、及び三文字以上の全内容型に対する一様な多項式上界を解決すること。

### 8.3 次に絞るべき一点

**`m` の大きさそのものではなく、それを生む骨格の短い導出可能性を問う。** 具体的には、`a^k` の節点数最小導出 `T` の重い反鎖から得られる `b,c` 混合語で、`m` 個の異なる `a` 骨格が強制される場合、そのうち二つから `D_L(a)=D_L(a^{1+δ})`（`0<δ<k`）を生む**共通の二穴・一穴文脈**を構成できるかを問う。これができれば `m` を圧縮し、定理 (3.1) から中心問題の肯定へ進める。できないなら、その共通文脈を回避する符号化方式と、ファンアウト2・ランク2・小厚さを同時に与える具体的文法が必要である。

### 8.4 特徴標本下界への正確な射程

**今回は新たな超多項式下界を証明していない。** 原稿 `prop:rare-type` により、仮に適格な反例族が得られれば、純粋型 `{a}` の最短語が `a^{k_n}` であることから、`𝓑^{≤r}_{2,c}`（固定 `r≥2`）、`𝓑_{2,c}`、および **`𝒞_{2,c}` 全体に特徴標本を持つ集合駆動作用素**の全特徴標本に、長さ `k_n` の `{a}` 型語が必要となる。アルファベットは **`Σ={a,b,c}`**、ファンアウトは `≤2`、ランクは構成できた場合に限り `≤2` と明示しなければならない。しかし、本報告の命題 5.1 には必要な小厚さの表示が示されていないので、その推論を適用して**新規の下界であるとは主張しない**。

---

## 9. 参照と先行研究の扱い

1. 栗山貴之、[現行 `main.tex`](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/main.tex)：`def:grammar-properties`、`def:tuple-substitutable`、`lem:thickness-equivalence`、`lem:no-insertion`、`prop:rare-type`、`lem:power-transfer`、付録 `app:two-letter-content`、`op:fanout-two`。本報告の数理上の定義と既知の主張の正本。
2. 第六報 [`chatgpt_mixed_escapes_2026-11-03.md`](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/reviews/chatgpt_mixed_escapes_2026-11-03.md)：二色損失比と二段刈込みの発想。本報告 §3 で再度論証した。
3. [`chatgpt_a_spectrum_2026-11-03.md`](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/reviews/chatgpt_a_spectrum_2026-11-03.md)：同一 `a` 骨格の差の剛性。本報告 §4.2 では必要部分を再証明した。
4. [`claude_ternary_content_2026-11-01.md`](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/reviews/claude_ternary_content_2026-11-01.md)：再配分・交換・隙間の合流。今回の上界では三文字の合流を仮定していない。
5. Ryo Yoshinaka, [*Efficient learning of multiple context-free languages with multidimensional substitutability from positive data*](https://doi.org/10.1016/j.tcs.2010.12.058), *Theoretical Computer Science* **412** (2011), 1821–1831。多次元代入可能性と学習の基礎。
6. Alexander Clark and Rémi Eyraud, *Polynomial Identification in the Limit of Substitutable Context-free Languages*, *JMLR* **8** (2007), 1725–1745。代入可能性の原型。

**新規性について：** 本報告の補題 2.1、定理 3.1 と同じ「全内容の `a` 個数スペクトルで例外ラベルを数える」形の結果が刊行文献にあるかどうか、**未確認**。原稿への採用前に原著・最近のプレプリントとの定理単位の照合が必要である。

# 定理 A の線形因子ギャップに関する検討報告

**日付**：2026-11-02  
**対象**：Takayuki Kuriyama, *Distributional Learning of Multiple Context-Free Languages under Fixed Finite-Semigroup Typing: Local Groups and the Length of Characteristic Data*  
**原稿正本**：[GitHub `02-v2-lg-fanout-boundary/main.tex`](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/main.tex)、取得時 Git blob `07fa399bf6edab0e1d6298754612484f82db32e6`。  
**結論**：**一般のギャップは未解決**。二次下界も全局所群に対する線形上界も証明できなかった。一方、(a) 証人の使用回数を加味した上界、(b) 任意の型付けでの有限・語長幅有界標的の線形上界、(c) 一文字アルファベットの有限局所群型付け標的の線形上界、(d) 有限代入可能言語の部分語反鎖性、を厳密に得た。これらは下界構成を絞るための部分結果であり、一般問題の解決と主張しない。

## 0. 主張別の判定（最初に読む表）

| 番号 | 主張 | 判定 | 根拠・適用範囲 |
|---|---|---|---|
| R0 | 二次上界の二つの `\|G\|` は別の箇所から来る | **証明済み（既存）** | `lem:heavy-node-count` → `lem:marked-heavy-window-group`／`lem:local-group-shortest` と、`lem:witness-length-template`／`cor:distribution-representatives`；§§4–5、付録 C |
| R1 | 全局所群型付けで最短特徴標本が `O(\|G\|θ̄)` | **未解決** | 原稿にあるのは `O(\|G\|²θ̄)`；本報告の追加結果は限定クラスのみ |
| R2 | 固定群型付けにおける `ω(\|G\|θ̄)`、特に `Ω(\|G\|²θ̄)` 下界 | **未解決** | Z₂、S₃、窓型付けについて必要な標的族・最小性・全 arity の証明を構成できていない |
| R3 | 型付き非終端・規則の**出現重み付き**代表長による上界 | **証明済み（本報告の命題 1）** | `cor:distribution-representatives` の証人を個別に数え直す。両正準作用素 |
| R4 | 有限標的で全語の長さ `M` が `M=O(θ̄)` なら線形上界 | **証明済み（本報告の定理 2）** | **任意の**固定型付け・ファンアウト・固定ランク。両正準作用素 |
| R5 | 有限 `f,s`-代入可能言語の同型受理語は真の部分語関係を持たない | **証明済み（本報告の補題 3）** | `d=1` だけを使用。さらに各 arity の同時埋込み版も証明 |
| R6 | 一文字アルファベット・有限標的・局所群型付けでは線形上界 | **証明済み（本報告の定理 4）** | `|L∩Σ⁺|≤|S|` と `lem:local-group-shortest`。両正準作用素、クラス全体に特徴標本を持つ集合駆動作用素 |
| R7 | 固定した Z₂ 上で、受理語の型が異なる二つの代入可能言語の和も代入可能 | **反証** | §4.3 の 4 文字の明示的反例。下界構成における危険な操作 |
| R8 | 自明型付けの `Θ(\|G\|θ̄)` | **証明済み（既存）** | `cor:trivial-exact`；下界は `|Σ|≥4f+1`, `r_max≥2`。L1/L2 |
| R9 | 本報告の数学的部分結果の文献的な初出性 | **未確認** | 2026-11-02 時点の限定的照合のみ。新規性・査読済み性を主張しない |

**記号**：以下 `n=\|G\|`, `T=\bar\theta_G≥1`, `r=r_{\max}` と書く。`f,r,s,Σ` を固定し、`G` は明記しない限り reduced good、`L(G)=L∩Σ⁺` とする。サンプル長は `\|K\|_+=\sum_{w∈K}(|w|+1)`。`N_typ` は trimmed full yield-type refinement の非開始型付き非終端数と型付き規則数の合計であり、`N_typ≤|S^♯|^{fr}n`。上界の定数は `f,r,s,Σ` に依存する。`L1` は原稿の `\mathcal B^{≤r}_{f,s}` と `\mathcal B_{f,s}`、`L2` はクラス全体に特徴標本を持つ任意の集合駆動作用素に対する主張とする。

## 1. Q0：二重計数の正確な場所

`lem:thickness-equivalence` (iv) は、各非終端 `A` に固定部分が長さ `≤T` の導出的文脈 `E_A` を与える。`lem:witness-length-template` (ii),(iv) は、代表長上限 `b` に対し、両正準作用素の共通の特徴標本 `W` を作り、

```text
|W| ≤ C_s(G) = O(n),
||W||_+ ≤ C_s(G) (1 + 2T + r b).
```

代表として意味的な類 `Cl_{L,s}(X)` の最短タプルを許すのが `cor:distribution-representatives` である。同系の式で `C_s(G)` を `N_typ` に鋭くできる：

\[
\|K\|_+\le N_{\rm typ}(1+2T+r\tau(G,s))+\mathbf1_{\{\varepsilon\in L\}}.\tag{1}
\]

一方、`lem:heavy-node-count` (§5、1346–1369行) では、`λ`-minimal 導出の祖先・子孫に同じ `(A,λ-vector)` ラベルが現れればその間を縮約できるため、各経路は高々 `|V||N|^f` 個の節点を持つ。重い節点の反鎖の幅が定数以下なら根の長さは `O(T |V||N|^f)`。`lem:marked-heavy-window-group` は同時ブロック置換によってその定数幅を示し、`lem:local-group-shortest`（付録 C、2703–2756行）では局所群の sliding-factor 座標にも適用する。ゆえに

\[
\tau(G,s)\le t_{\rm typ}(G,s)\le C_{f,r,s,\Sigma}|V|T=O(nT).\tag{2}
\]

(1) の **型付き規則数** `O(n)` と、(2) の **経路ラベル数** `O(|V|)` が掛け合わされ、二次になる。反鎖定数を改善するだけでは経路上の `|V|` は消えない。`prop:block-replacement-interface` の非可換群の順序保持、`lem:local-group-shortest` の buffer は、この経路上界の係数を制御するのであって、二つ目の `n` を消す仕組みではない。

`prop:typed-thickness-exponential` は `t_typ ≫ τ` が起こることを既に示す。さらに `τ ≫ T` の **非終端が定数個**というだけでは不十分である。多数の型付き規則がその非終端を右辺に使えば、同じ長い代表を規則ごとの証人で何度も数えるからである。次節で必要十分ではないが正確な**十分条件**を得る。

## 2. 命題 1：出現重み付きの精密な上界（Q2 の部分結果）

**命題 1（証人の incidence-sensitive bound）**。原稿 `cor:distribution-representatives` と同じ仮定を置く。型付き非開始非終端の集合を `\mathscr X`、型付き規則の集合を `\mathscr R` とする。各 `X∈\mathscr X` にその意味的類の最短代表を選び、長さを `τ_X` とする。`d_X` を `\mathscr R` の右辺に現れる `X` の**子出現数（重複込み）**と定める。すると両正準作用素に共通する特徴標本 `K` が存在して

\[
\boxed{\ \|K\|_+\le
N_{\rm typ}(1+2T)+\sum_{X\in\mathscr X}(1+d_X)\tau_X
+\mathbf1_{\{\varepsilon\in L\}}.\ }\tag{3}
\]

従って `\sum_X(1+d_X)(\tau_X-T)_+=O(nT)` なら **`\|K\|_+=O_{f,r,s,Σ}(nT)`** である。

**証明**。原稿の `cor:distribution-representatives` の証明（3021–3042行）は、各 `X` に `ι(X)∈Cl_{L,s}(X)` を取り、`χ(X)=E_A` として、次の二種類の語を `K` に収める。

1. 各型付き非終端 `X` につき `E_A[ι(X)]`。
2. 各型付き規則 `R:X→ρ(Y_1,…,Y_q)` につき `E_A[ρ(ι(Y_1),…,ι(Y_q))]`。

これらが標的の語であることは `lem:typed-homogeneity` と `lem:witnessed-composition` による。`prop:completeness` と `prop:reconstruction-soundness` により、全ての `K⊆K'⊆L` において両正準作用素の出力が `L` になる。したがって characteristic 性は原稿と同じである。

型付き非終端の証人は `|E_A|_fix+τ_X≤T+τ_X` 文字、型付き規則の証人は `|E_A|_fix + e(R)+∑_{j=1}^{q}τ_{Y_j}≤2T+∑_j τ_{Y_j}` 文字である。ここで `e(R)` はテンプレートが直接書き込む終端文字数であり、`lem:thickness-equivalence` (i) より `e(R)≤T`。異なる証人語が一致すれば集合として一回しか数えないので、**すべて別の語とみなして**上から数えれば

\[
\begin{aligned}
\|K\|_+
&\le |\mathscr X|(1+T)+\sum_X\tau_X
+|\mathscr R|(1+2T)+\sum_{R\in\mathscr R}\sum_{Y\text{ child of }R}\tau_Y
+\mathbf1_{\{\varepsilon\in L\}}\\
&\le N_{\rm typ}(1+2T)+\sum_X(1+d_X)\tau_X+\mathbf1_{\{\varepsilon\in L\}}.
\end{aligned}
\]

これが (3)。さらに `\sum_Xd_X≤r|\mathscr R|` より

\[
\sum_X(1+d_X)\tau_X\le
T\bigl(|\mathscr X|+r|\mathscr R|\bigr)
+\sum_X(1+d_X)(\tau_X-T)_+.
\]

`N_typ≤C_s(G)=O(n)` を代入すると結論を得る。□

**限界**：この命題は二次から線形への**一般的な証明ではない**。例えば一つの `X` に `τ_X=Θ(nT)`, `d_X=Θ(n)` が同時に生じるなら右辺は依然 `Θ(n²T)` になり得る。これが実際の最短特徴標本の下界であるとは限らず、証人の共有・重複除去はさらに研究が必要である。

## 3. 定理 2：有限標的の語長幅が有界なら、型付けを問わず線形（Q2 の部分解決）

**定理 2（finite bounded-length-spread bound）**。`s` は **任意の固定有限半群型付け**、`f≥1`, `r_max≥1` は固定とする。`L∈C_{f,s}` が非空有限言語で、`L∩Σ⁺≠∅` とする。その正の語の最短長、最長長をそれぞれ `m,M` とする。任意の reduced good rank-`≤r_max` 表示 `G` に対し、両正準作用素に共通の特徴標本 `K` が存在し

\[
\boxed{\ \|K\|_+\le N_{\rm typ}\bigl(1+2T+r_{\max}M\bigr)
+\mathbf1_{\{\varepsilon\in L\}}.\ }\tag{4}
\]

特に `M≤C m`、または `M≤CT`（`C` は族に依存しない定数）なら

\[
\|K\|_+=O_{f,r_{\max},s,\Sigma,C}(nT).\tag{5}
\]

**証明**。trimmed refinement の各型付き非終端 `X` は、ある成功導出木に現れる。その成功導出の終端語 `w` は `L∩Σ⁺` に属し、`|w|≤M`。good 文法では右辺の各変数がちょうど一度現れ、各成分は非空であり、`X` 部分木の全ての成分は成功語中の互いに交わらない区間に現れる。従ってその部分木が生成するタプル `u_X` は `\|u_X\|_1≤|w|≤M`。各 `X` について選べるため、**`t_typ(G,s)≤M`**。`thm:data-from-typed-thickness` に代入して (4) を得る。

また reduced 性より任意の規則は何らかの成功導出に現れる。その導出語の長さは `[m,M]` に属するので、規則厚さの定義から `m≤θ_G≤M`、すなわち `m≤T≤M`。`M≤Cm` なら `M≤CT`。`N_typ≤|S^♯|^{fr_max}n` を (4) に適用して (5) を得る。□

**系 2.1（等長の有限標的）**。`L∩Σ⁺⊆Σ^M` なら `θ_G=M`、`t_typ≤M` であり、**局所群か否かに関係なく** `O(nT)`。原稿 `prop:linear-factor-all-fanout` の族はまさにこの場合に属するため、その族をそのまま変形せずに二次下界を出すことはできない。

**系 2.2（有限標的の二次下界に対する必要条件）**。固定 `f,r,s,Σ` で `n=\|G\|` とすると、有限標的について (4) は `cs_{f,s}^{≤r}(L)≤C_0n(T+M+1)` を与える（`C_0` は固定パラメータのみに依存）。したがって `cs(L)=ω(nT)` なら必ず `M/T→∞`。さらに `cs(L)=Ω(n²T)` なら必ず **`M=Ω(nT)`** である。

**証明**。`T≥1`, `n≥1` とし、(4) から上記評価を得る。これをそれぞれの下界で割って整理する。二次の場合、定数 `c>0` に対し `cn²T≤C_0n(T+M+1)`、従って `M≥(c/C_0)nT-T-1=Ω(nT)`。□

この必要条件はユーザーの「長さ `≈nT` の語が `≈n` 個」という設計上の要請と整合するが、そのような語を代入可能性を壊さず作れることまでは保証しない。

## 4. 補題 3：有限代入可能言語の部分語反鎖性（Q1 の構成に対する障害）

**補題 3（全 arity 同時埋込みポンプ）**。`f≥1`、`s` を任意の型付けとし、`L` を `(f,s)`-tuple-substitutable とする。ある `1≤d≤f`、適法 `d`-文脈 `E`、非空成分タプル `x=(x_1,…,x_d)` と `y=(y_1,…,y_d)` が存在して、

- `s^{(d)}(x)=s^{(d)}(y)`、`E[x],E[y]∈L`、
- 全成分について `y_h=p_h x_h q_h`（`p_h,q_h∈Σ*`）、
- 少なくとも一成分で `|p_h|+|q_h|>0`、

を満たすなら、**`L` は無限言語**である。

**証明**。最初の条件と代入可能性から `D_L^{(d)}(x)=D_L^{(d)}(y)`。各非負整数 `j` に対し、`E` の第 `h` 穴を `p_h^j □_h q_h^j` に置換した文脈を `E_j` とする。元の `E` の穴と穴の間には少なくとも一文字の固定部があるため、`E_j` はすべて適法な `d`-文脈である。`E_0[x]=E[x]∈L`。`E_j[x]∈L` なら `E_j∈D_L^{(d)}(x)=D_L^{(d)}(y)` より `E_j[y]∈L`。しかし

\[
E_j[y]=E_j[(p_hx_hq_h)_h]=E_{j+1}[x].
\]

帰納法により `E_j[x]∈L` が全ての `j≥0` で成立する。長さは `|E[x]|+j\sum_h(|p_h|+|q_h|)` で厳密に増加する。従って相異なる無限個の語が `L` に属する。□

**系 3.1（有限標的の同型受理語の因子反鎖）**。`L` が有限なら、**同じ `s` 型を持つ二つの相異なる正の受理語 `u,v∈L` で、`u` が `v` の連続真部分語となるものは存在しない**。

**証明**。`d=1`、`E=□`、`x=u`, `y=v` と置き、`v=p u q` に補題 3 を適用する。□

**系 3.2（導出非終端内の障害）**。有限標的の reduced good 表示で、同じ型付き非終端 `X` の二つの実現タプルが成分ごとに連続部分語として埋まり、少なくとも一成分で真に短い、ということはない。

**証明**。原稿 `lem:typed-homogeneity` と `lem:identity-canonical-contexts` により、二つのタプルの型は等しく、同じ適法導出的文脈 `E_A` に受理される。補題 3 を適用する。□

**Z₂ 構成への明示的な警告**。`s(a)=1∈Z₂`, `s(c)=0∈Z₂` とすると、`c^{in}a` と `c^{jn}a`（`0<i<j`）は同じ奇型で、前者が後者の真の接尾語である。したがって、これら二語を含む有限言語は **fan-out 1 ですでに** `(1,s)`-substitutable になれない。`S→A_i`、`A_i→c^n A_{i-1}\mid b` のような「深い鎖＋早期停止」の素朴な候補は、早期停止語や異なる深さの語の間でこの障害を検査しない限り、下界の証明に使用できない。

### 4.3 反例：全語型を分離した合併も安全ではない

`Σ={p,q,x,y}`、`s:Σ⁺→Z₂` を `s(q)=1`, `s(p)=s(x)=s(y)=0` とする。`L_0={px,py}`、`L_1={qx}` とする。`L_0` は自明な型付けでも 1-substitutable である。実際、受理語に現れる非空因子の分布は

```text
D(p)  = {□x, □y}
D(x)  = D(y) = {p□}
D(px) = D(py) = {□}
```

であり、異なる分布同士は交わらない。`L_1` は一語言語なので同様に 1-substitutable である。しかも `s(L_0)={0}`, `s(L_1)={1}` で全語の型が分離している。ところが和 `L=L_0∪L_1` では `x,y` がともに型 0 で `p□` に同時に受理されるのに、`q□` は `x` だけを受理する。ゆえに `L` は **(1,s)-substitutable でない**。□

つまり「短い証人語は偶型、長い必須語は奇型にするから、両者は干渉しない」という設計は**一般に不正**である。判定に関わるのは**受理文全体の型だけではなく、全 arity の穴の型と共有文脈**である。

## 5. 定理 4：一文字・有限・局所群では線形上界（Q2 の部分解決）

**定理 4**。`Σ={a}`、固定 `f≥1`, `r_max≥1` とし、正の像 `S` が局所群である固定型付け `s` をとる。`L∈C_{f,s}` を有限言語、`G` をその任意の reduced good rank-`≤r_max` 表示とする。このとき

\[
\boxed{\ \|L\|_+=O_{f,r_{\max},s,\Sigma}(nT).\ }\tag{6}
\]

特に **`K=L` 自体が**両正準作用素に共通の特徴標本である。さらに、この `K=L` は、クラス全体に特徴標本を持つ**任意の集合駆動作用素**にとっても特徴標本である（L2 型の上界）。

**証明**。`u=a^i`, `v=a^j` を異なる正の受理語で `i<j` とする。`u` は `v` の真の部分語であるから、系 3.1 により `s(u)≠s(v)`。従って有限集合 `L∩Σ⁺` の各受理語は異なる型を持ち、**`|L∩Σ⁺|≤|S|`**。

`S∈LG` なので原稿 `thm:local-group-polydata`、具体的には `lem:local-group-shortest` と `lem:witness-length-template` (i) から、型付き根 `S_{(m)}` の最短語について

\[
\mu_m(L)\le t_{\rm typ}(G,s)\le C_{f,r_{\max},s,\Sigma}|V|T\le C_{f,r_{\max},s,\Sigma}nT.
\]

任意の受理語 `a^i` はその型 `m=s(a^i)` を持つ**唯一の**受理語なので、`i=μ_m(L)`。したがって、

\[
\|L\|_+\le |S|\bigl(C_{f,r_{\max},s,\Sigma}nT+1\bigr)
+\mathbf1_{\{\varepsilon\in L\}}=O(nT).
\]

両正準作用素は対象 `L` の部分集合上で sound かつ sample-consistent である（`prop:reconstruction-soundness` と原稿の再構成定義）。`K=L` は有限で、`K⊆K'⊆L` の唯一の選択肢が `K'=L` だから、`L(B(L))=L` となり `L` 自身が特徴標本である。一般のクラス全体に特徴標本を持つ集合駆動作用素 `A` についても、`L` の何らかの特徴標本 `F⊆L` が存在する。`F⊆L⊆L` なので特徴標本の定義から `L(A(L))=L`、同じく `K=L` が特徴標本である。□

`L∩Σ⁺=∅` の場合は `L⊆{ε}` で定数長とする。有限局所群の正の像が一元の自明型付けなら、正の受理語は高々1個というさらに強い事実が従う。ただし **この定理は一文字の有限標的のみ**を扱い、多文字・無限標的のギャップは閉じない。

## 6. Q1：二次下界の成否と構成上の要件

### 6.1 既存の下界（検証）

`prop:linear-factor-all-fanout` (§6、付録 G) は `|Σ|≥4f+1`, `r_max≥2`、**全ての型付け**に対して、

\[
L^{(f)}_{q,k}=\{w_0,\ldots,w_q\},\quad
|w_i|=W=2fq+2^k+2f,\quad
\|G^{(f)}_{q,k}\|=(7f+11)q+6k+3f+10
\]

を与える。各部分集合が全 arity `1≤d≤f` で代入可能であり、どの特徴標本も全 `q+1` 語を含む。従って最短長は**正確に** `(q+1)(W+1)`。定量的に `\|G\|≥q+1` は原稿付録 G の witness-cardinality 論法で得られ、表示は最小 reduced good 表示の定数倍以内。L1 と L2 の両方で成立する。`q=k=n` なら `W=2^n+Θ(n)`、`q=n,k` 固定なら `W=Θ(n)` であり、いずれも `Ω(nT)`。ただし全語が等長なので、定理 2 により**同族の最短特徴標本に `Ω(n²T)` は不可能**である。

### 6.2 新しい二次下界は未構成

希望される次の全条件を同時に満たす族は、本報告では得られなかった。

1. `n=Θ(最小 reduced good 表示サイズ)`、`T=θ̄_G`、`≈n` 個の必須語がそれぞれ `Ω(nT)` の長さを持つこと。
2. それらを除いた標的も `C_{f,s}` に属し、**全 arity** の同型タプルの文脈共有 ⇒ 分布一致を証明できること。
3. すべての規則が長さ `O(T)` の成功導出に使われ、単に長い語専用の規則を追加して `θ̄_G` を `Ω(nT)` にしてしまわないこと。
4. **L1 と L2 を分離**し、L2 には対象と削除対象の双方がクラスに属すること、L1 には少なくとも正準作用素の soundness を使うこと。
5. 表示のサイズについて `Ω(n)` の独立の下界、または原稿付録 G と同程度の規則証人数の下界を立てること。

定理 2 と系 2.2 から、有限標的の二次下界では**短い成功文**と**長さ `Ω(nT)` の受理文**が共存しなければならない。同時に補題 3 は、同型の受理文の因子包含を禁止する。これらの制約は、Z₂ の早期停止鎖と、既存の等長マーカー構成の単純合成を阻む。

**S₃・非可換性について**：`prop:block-replacement-interface` は元のブロック順序を保つための**上界の補題**であり、下界を与えない。非可換群で order-interleaving があることと、最短特徴標本の長さが超線形であることは別命題。本報告では S₃ の反例標的を証明できなかった。

**窓型付けについて**：局所自明性から定数個の窓情報だけで型を決定できるが、それだけでは各非終端の意味的最短代表 `τ_X=O(T)` を導けない。従って一般の窓型付けの線形上界は**未証明**。

### 6.3 `reviews/chatgpt_problemG_2026-11-01.md` との接続

GitHub 同リポジトリの同ファイルを確認した。同レビューの定理 1、可換群の語問題 `L=φ^{-1}(1)` に対する `|H|≤(r+2)T²` は、**対象言語が群の単位元語全体であり、群のサイズを変化させている**という条件の下での命題である。本問では `s`、したがって群像 `H` 自体が固定され、また `L` は群語問題に限られない。その定理から `τ_X=O(T)`、`∑_X(1+d_X)τ_X=O(nT)` を直接導くことはできない。特に `H_ab` への議論も、任意の代入可能標的における意味的類の最短代表を与えない。転用は**未確認**。

## 7. Q3：型付け別の現時点の境界

ここで表の「上界」は、固定 `f,r_max,s,Σ`、任意の標的 `L∈C_{f,s}` と任意の reduced good 表示 `G` に対する、**両正準作用素に共通の最短特徴標本**の上界である。「下界」は固定型付けに属する標的族についての L1/L2 の双方。特に断らなければ `Ω(nT)` の既存の下界は `|Σ|≥4f+1`, `r_max≥2` に依存する。

| 型付け | 全標的の `O(nT)` | 超線形下界 `ω(nT)` | 既存の全標的上界 | 判定・条件 |
|---|---|---|---|---|
| **自明** | **証明済み**（`cor:trivial-exact`） | 二次等の超線形は**反証** | `O(nT)` | **Θ(nT)**、下界は `|Σ|≥4f+1`、L1/L2 |
| **窓** `s_{k,ℓ}`、局所自明 | **未解決**（ただし定理 2・4 の限定域は線形） | **未解決** | `O(n²T)` (`thm:window-group-polydata`) | 自明群でも `|V|` を除けない現行証明；下界 `Ω(nT)` は大文字表で成立 |
| **可換群**（Z₂ を含む） | **未解決**（一文字・有限なら証明済み） | **未解決** | `O(n²T)`、Davenport 定数が係数を改善 | 下界 `Ω(nT)` は大文字表。レビューの可換群語問題だけでは全標的を扱えない |
| **非可換群**（S₃ を含む） | **未解決** | **未解決** | `O(n²T)`、順序保存の置換補題を使用 | 下界 `Ω(nT)` は大文字表。ブロック交錯は二次下界を意味しない |
| **一般の局所群 LG** | **未解決** | **未解決** | `O(n²T)` (`thm:local-group-polydata`) | 下界 `Ω(nT)` は大文字表。sliding-factor 型付けも含む |

**例外的に解決した断面**：任意の型付けで**有限かつ語長比 `M/m=O(1)`**なら定理 2 により `O(nT)`。一文字アルファベットの**有限 LG 標的**なら定理 4 により `O(nT)`。いずれも普遍的な結論と取り違えない。

**非 LG 型付け**は定理 A の前提外。原稿 `thm:fanout-one-data` は fan-out 1 の**擬多様体レベル**で LG が多項式保証の境界であることを扱う。個別の非 LG 型付けごとに指数下界があるという意味ではない。また fan-out 2 での内容型付けには別の現象がある（`thm:fanout-two` と `cor:two-letter-semilattice`）。

## 8. 推奨される次の数学的命題

最も直接的な標的は、命題 1 の余剰項

\[
\mathcal E(G,s)=\sum_X(1+d_X)(\tau_X-T)_+
\]

を、**特徴標本の語の共有を考慮して** `O(nT)` に圧縮できるか、という問いである。これは `τ` の最大値のみを見るより細かい。検証すべき二つの独立方向を分ける。

- **上界方向**：各右辺型付き子出現の witness requirement を、同じ受理語内の複数の occurrence で同時に満たす「証人被覆」の構成を与える。各規則を別語で証明する必要があるかを吟味する。`O(nT)` の被覆定理が得られれば Q2 を解くが、**本報告では未証明**。
- **下界方向**：有限長さ集合の比 `M/T` を `Ω(n)` にしながら、同型因子反鎖を守り、削除後も全 arity の代入可能性が保たれる語族を作る。根や規則に長語専用規則が残り `θ̄_G` が膨らんでいないか、各規則に長さ `O(T)` の成功語を**列挙**して検査する。**本報告では未構成**。

下界として用いる標的の最短特徴標本を直接評価し、`t_typ` や `τ` の大きさだけでは結論しない。今回の証明は構造的なものであり、Python による有限数値実験は実施していない（従って観察を定理へ昇格していない）。

## 9. 参照先と先行研究照合の限界

1. Kuriyama, GitHub 現行 `main.tex`（上記 blob）。定義：§2 `def:standard-mcfg`, `def:grammar-properties`, `def:tuple-substitutable`。学習器：§3 `def:characteristic-sample`, `prop:completeness`, `prop:reconstruction-soundness`。長さ：§4 `lem:thickness-equivalence`, `lem:witness-length-template`, `thm:data-from-typed-thickness`, `prop:rare-type`, `cor:typed-sandwich`, `cor:distribution-representatives`。局所群：§5 `prop:block-replacement-interface`, `lem:marked-heavy-window-group`, `thm:local-group-polydata`、付録 C `lem:local-group-shortest`。下界：§6 `prop:linear-factor-all-fanout`, `cor:trivial-exact` と付録 G。
2. `reviews/chatgpt_problemG_2026-11-01.md`（GitHub 同ディレクトリ）。「可換群語問題の `|H|≤(r+2)T²`」「一般群・アフィン群の文法サイズ下界」は本問へ直接転用していない。
3. Ryo Yoshinaka (2011), “Efficient learning of multiple context-free languages with multidimensional substitutability from positive data,” *Theoretical Computer Science* 412(19), 1821–1831. DOI: [10.1016/j.tcs.2010.12.058](https://doi.org/10.1016/j.tcs.2010.12.058)。
4. Ryo Yoshinaka (2015), “General Perspective on Distributionally Learnable Classes,” *MoL 2015*, 87–98, [ACL Anthology](https://aclanthology.org/W15-2308/)。一般の分布学習枠組みと先行性の確認。
5. Alexander Clark and Rémi Eyraud (2007), “Polynomial Identification in the Limit of Substitutable Context-free Languages,” *JMLR* 8, 1725–1745, [JMLR](https://jmlr.csail.mit.edu/papers/v8/clark07a.html)。
6. Yuval Filmus (2011), “Lower bounds for context-free grammars,” *Information Processing Letters* 111, 895–898, DOI: [10.1016/j.ipl.2011.06.006](https://doi.org/10.1016/j.ipl.2011.06.006)。導出木部分構造・計数下界の先例。ただし**本報告の特定の補題・上界が既知かどうかは未確認**。

**採用判定**：命題 1、定理 2、補題 3、定理 4 は原稿に追加できる候補の独立した補題・系として証明を記述した。ただしそれらの文献的新規性、より一般の定理との重複、主論文への最良の配置は**未確認**。最重要の `Θ(nT)` 対 `Θ(n²T)` の一般判定は**未解決**のままである。

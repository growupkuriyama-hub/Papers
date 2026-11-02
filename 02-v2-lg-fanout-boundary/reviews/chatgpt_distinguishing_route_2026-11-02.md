# 区別の補題の一般的利用：可換群篩いには規則厚さ以下の区別語が存在する

**研究日：2026-11-02**  
**対象：**栗山貴之、論文 #2 `02-v2-lg-fanout-boundary/main.tex`  
**位置付け：**数学的研究報告（未査読）。新しい反例族の構成には至らなかったが、D1 の可換群篩いによる超多項式下界を**否定する一般定理**を証明した。  
**原稿取得：**2026-11-02、[GitHub 作業正本](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/main.tex)（取得時の最終更新表示 2026-11-02 04:41:18 UTC）。過去の三報告も GitHub から同日に取得した。以後の更新は本報告へ自動反映されない。

## 0. 主張の判定表

| ID | 主張 | 判定 | 根拠 |
|---|---|---|---|
| D1-A | 任意の reduced good MCFG `G`、可換群値の任意の剰余類 `C` について、`L(G)\\C` が非空なら長さ `≤ θ̄_G` の語を含む | **証明済み** | §2、定理2.2 |
| D1-B | `Parikh(L)-Parikh(L)` が生成する整数格子は、長さ `≤ θ̄_G` の受理語同士の差で既に生成される | **証明済み** | §2、定理2.1 |
| D1-C | 同じ `G` から選べる `≤2|P|+1` 語の集合が、すべての可換群剰余類の**真の削除**を同時に検出する | **証明済み** | §2、系2.3。特徴標本ではない |
| D1-D | 可換群篩いだけによる、`θ̄_G=poly(n)` かつ最短差語 `n^{ω(1)}` の族 | **反証** | 定理2.2が全ファンアウト・全ランクで排除 |
| D1-E | `H_{2,2}` と偶数 `c` 篩いは、ともに `(2,s_U)` 代入可能で最短差語長4 | **証明済み** | §3。全 arity の証明と厳密な列挙表示 |
| EXP-1 | 既存倍増族は `n=2` ですでに2穴違反を持つ | **証明済み** | §4、明示的反例。プログラムで再検査 |
| EXP-2 | ショートカット倍増・ブロック族を篩いに替えれば目的の反例になる | **反証（当該候補）** | §4。元の標的の代入可能性が成立しない |
| D2-G | 任意の真部分標的 `L'∈C_{2,s_U}` への差について `poly(‖G‖,θ̄_G)` の区別語上界 | **未解決** | §5。可換群の線形性を一般の `L'` に移せない |
| D3 | 篩いの道では `op:S1` と `op:fanout-two` を否定的に解決できない | **証明済みの方法論的帰結** | §2、§6。問題自体は未解決 |
| NOV | 定理2.1–2.3の文献上の初出性 | **未確認** | §7。既存の厚さ補題から導く本報告の証明であり、新規性は主張しない |

「証明済み」は以下に自足的な証明があるという意味で、論文としての独立査読や新規性の判定を含まない。

## 1. 正本の定義・量化・先行探索の位置

原稿の `def:standard-mcfg`、`def:grammar-properties`、`def:tuple-substitutable`、`prop:abelian-coset-filter`、`lem:thickness-equivalence`、`lem:type-deletion`、`lem:distinguishing`、`prop:rare-type`、`prop:linear-factor-all-fanout`、§8の `lem:power-transfer`、`thm:doubling-no-lift`、`lem:unique-word-rigid`、`prop:unique-two-letter-shapes`、`prop:sl-reduction`、`thm:two-letter-content`、§9の `op:S1`、`op:fanout-two`、`prop:unique-word-route`、`lem:unique-word-gap` を照合した。

- `G=(V,Σ,P,S,fan)` は MCFG。`fan(S)=1`、ファンアウト上限 `f`、規則ランク上限 `r`。規則 `R:A→ρ(B₁,…,B_k)` は線形で、**good** なら各変数はちょうど一度現れ、各成分は空でなく、nonpermuting・nonmerging でもある。**reduced** は全非終端の到達可能性・生成可能性。
- `‖G‖=|V|+Σ_{R∈P}(1+rank(R)+Σ_i|α_i|)`。`θ_G(R)` は **R を使用する成功導出の文の最小長**であり、`θ̄_G=max(1,max_R θ_G(R))`。これは最小導出木節点数とは異なる。
- `(f,s)` 代入可能性は、すべての `1≤d≤f` に対して、同じ**成分別型**を持つ正の `d`-タプル `x,y` が一つの受理許容文脈を共有すると、全ての許容 `d`-文脈に関する分布が一致する条件。`d=2` では穴の間の固定セパレータは**非空**。
- `s_U:{a,b,c}⁺→U₁` は `a,b↦1`、`c↦ζ`（`ζ²=ζ`）。`C_{f,s}` は `(f,s)` 代入可能な `f`-MCFL のクラス。
- `L'⊊L` がともに `C_{f,s}` なら、原稿 `lem:distinguishing` により `L` の特徴標本は `L\L'` に交わる。対象は `B^{≤r}_{f,s}`（`r≥1`）、`B_{f,s}`、および両標的に特徴標本を持つ集合駆動作用素。従って `min{|w|:w∈L\L'}` は、その**区別方法によって強制される語長**の下界である。下界が小さいことは、特徴標本全体が小さいことを意味しない。

既存ノートとの照合：

1. `reviews/chatgpt_problemG_2026-11-01.md` は、可換**群の語問題全体**を CFG で表す際の `|H|≤(r+2)T²` を論じている。本報告は対象言語 `L` の **任意の可換群への像の剰余類削除**を扱うため別命題である。この既存評価の正否を本報告から再証明したとはしない。
2. `reviews/chatgpt_power_rare_words_2026-11-02.md` はショートカット倍増の1穴違反とブロック族の2穴違反、長い汚染語の必要性を示す。
3. `reviews/chatgpt_short_unique_words_2026-11-02.md` は唯一の純語 `W` が長ければ多数の `c` を含む伴走語が必要という密度補題を与える。これらは**型の削除**に関する障害であって、本報告の可換群篩いの上界とは独立である。

## 2. 主結果：可換群の篩いは `θ̄_G` 以下の語で必ず破れる

本節では `f`、`r`、型付け `s`、代入可能性の仮定を**一切使用しない**。仮定は `G` が reduced good であることだけである。厳密には、証明に必要なのは **成功導出内の非終端置換が可能であることと線形・非削除性**、各規則の有限厚さである。

`π:Σ*→ℤ^Σ` を Parikh 写像とし、`L=L(G)`、`θ=θ̄_G` とおく。非終端 `A` ごとに、その生成するタプルの全成分長が最小のもの `u_A` を一つ選ぶ。`q_A=Σ_i π(u_{A,i})` とする。`G` は reduced なのでこの選択が可能。規則

`R:A→ρ(B₁,…,B_k)`

に現れる**直接終端**の Parikh ベクトルを `t_R` とし、整数ベクトル

`δ_R := t_R + Σ_{j=1}^k q_{B_j} − q_A ∈ ℤ^Σ`

を定義する。`k=0` でもよい。

### 補題2.0（局所差の短い二語による実現）

各規則 `R` について、`p_R,q_R∈L` が存在して

`|p_R|,|q_R|≤θ_G(R)≤θ`、かつ `π(p_R)−π(q_R)=δ_R`

を満たす。

**証明。** `R` を使う長さ `θ_G(R)` の成功導出木 `T_R` を取る。`R` の一つの使用箇所 `v` における `A`-タプルを `z_A`、その子の実際のタプルを `z_{B_j}` とする。この箇所の外側の導出木は固定し、`A` の箇所だけを入れ替える。

第一の入れ替えでは `A` の部分木を `u_A` の導出に置換する。`u_A` は全成分長が最小なので `‖u_A‖₁≤‖z_A‖₁`。ゆえに新しい成功文 `q_R` は元の文より長くなく、`|q_R|≤θ_G(R)`。

第二の入れ替えでは `R` の適用そのものは残し、子 `B_j` をそれぞれ最短タプル `u_{B_j}` の導出に置換する。`‖u_{B_j}‖₁≤‖z_{B_j}‖₁` であり、`ρ` は線形・非削除なので、置換後の `A`-タプルの全長も増えない。新しい成功文 `p_R` も `|p_R|≤θ_G(R)`。

外部文脈は両方で同じである。したがって Parikh 差はそこで相殺され、

`π(p_R)−π(q_R)=t_R+Σ_j q_{B_j}−q_A=δ_R`。

各入れ替えは同一非終端 `A` の通常の MCFG 導出の交換であり、**成分数が1でも2でもそれ以上でも合法**である。非削除性によって全成分の終端文字が成功文へ一度ずつ残る。□

### 定理2.1（短い成功語による全 Parikh 差格子の生成）

`L_{≤θ}:={w∈L:|w|≤θ}` とおくと、次の **ℤ^Σ の部分群（格子）**は等しい：

\[
\boxed{\ 
\left\langle\pi(u)-\pi(v):u,v\in L\right\rangle
=
\left\langle\pi(u)-\pi(v):u,v\in L_{\le\theta}\right\rangle.
\ }
\tag{2.1}
\]

より具体的に両辺は `⟨δ_R:R∈P⟩` に等しい。さらに、`u_S∈L_{≤θ}` であり、`K_ab(G):={u_S}∪{p_R,q_R:R∈P}` は上述の生成関係を実現する。

**証明。** 任意の成功導出木 `T` の各節点に使われた規則を `R(v)` と記す。直接終端の Parikh ベクトルの和が成功文 `w` の Parikh ベクトルであり、子の `q_B` と親の `−q_A` は木の内部で打ち消し合う。したがって

\[
\pi(w)-q_S=\sum_{v\in T}\delta_{R(v)}. \tag{2.2}
\]

これは定義からの**有限和の完全な恒等式**であり、代入可能性を使わない。また `u_S` の導出から得る文は `L` に属し、`|u_S|≤θ` である（どの規則の成功導出も `S`-語を与え、その長さは `θ` 以下のものが少なくとも一つ存在する）。よって式(2.2)から、すべての `π(w)−π(u_S)` が `δ_R` の整数生成群に入り、任意の二語の差もそうなる。

反対に補題2.0より、各 `δ_R=π(p_R)−π(q_R)` は**長さ `≤θ` の二つの成功語の差**である。従って `⟨δ_R⟩` は右辺に含まれる。右辺は明らかに左辺に含まれるため、三群は一致する。□

### 定理2.2（可換群剰余類の短い反例語）

任意の可換群 `A`（有限でなくてもよい）、準同型 `φ:Σ*→A`、部分群 `H≤A`、元 `γ∈A` に対して、

\[
\boxed{\quad
L\setminus\varphi^{-1}(\gamma+H)\ne\emptyset
\ \Longrightarrow\ 
\min_{w\in L\setminus\varphi^{-1}(\gamma+H)}|w|\le\bar\theta_G.
\quad}\tag{2.3}
\]

**証明。** `φ` は Parikh 写像を介して `ℤ^Σ` からの群準同型に一意に延長される。仮に `L_{≤θ}` の全語が `γ+H` に入るとする。このとき `u_S∈L_{≤θ}` なので `φ(u_S)∈γ+H`。さらに定理2.1の短い語同士の差はすべて `H` に写り、従って `φ(δ_R)∈H`。式(2.2)から、任意の `w∈L` について `φ(w)−φ(u_S)∈H`、すなわち `φ(w)∈γ+H` となる。対偶で式(2.3)を得る。□

**重要な適用範囲。** 無限可換群への篩いは一般には `f`-MCFL を保たないが、式(2.3)は集合論的な言語の命題としてなお成立する。**有限**可換群なら篩い言語が正則であり、`L` が `f`-MCFL なら `L∩φ⁻¹(γ+H)` も `f`-MCFL である。加えて `L∈C_{f,s}` なら原稿 `prop:abelian-coset-filter` により代入可能性も全 arity `1≤d≤f` で保存される。従って **D1 の `L'` は確かにクラス内にあり、差語長には式(2.3)が適用される**。

### 系2.3（あらゆる可換群篩いに共通の、多項式長の hitting set）

補題2.0の選択によって

\[
K_{\mathrm{ab}}(G)=\{u_S\}\cup\bigcup_{R\in P}\{p_R,q_R\}
\]

を作ると、`K_ab(G)⊂L`、すべての語の長さは `≤θ` で、

\[
|K_{\mathrm{ab}}(G)|\le2|P|+1,
\qquad
\|K_{\mathrm{ab}}(G)\|_+\le(2|P|+1)(\bar\theta_G+1).
\]

さらに**任意の**可換群・準同型・剰余類 `C=φ⁻¹(γ+H)` に対して、

`L\C≠∅ ⇒ K_ab(G)\C≠∅`

である。**証明。** `K_ab(G)⊂C` なら `u_S,p_R,q_R` の値がすべて同じ剰余類にあり、`φ(δ_R)=φ(p_R)−φ(q_R)∈H`。式(2.2)で `L⊂C`。対偶を取る。語数と長さは構成から従う。□

**注意：** `K_ab(G)` は群篩いで切り落とされる部分を**検出**するための集合であり、`B^{≤r}_{f,s}` や `B_{f,s}` の**特徴標本だとは主張しない**。全ての部分標的を識別する保証はない。

**D1への決着。** `f=2`、固定 `r≥2`、`Σ={a,b,c}`、`s=s_U` に特殊化しても式(2.3)は成り立つ。従って、`‖G_n‖,θ̄_{G_n}=n^{O(1)}` なのに可換群篩いで `min|L_n\L_n'|=n^{ω(1)}` という族は**存在しない**。同様に `f=1`、任意の `f≥2`、半束の内容型付けでも存在しない。これは `op:fanout-two` の**肯定的解決**ではなく、ひとつの下界技法の限界の確定である。

## 3. 全 arity で安全な、具体的な篩いの小例

`k,m≥1` に対し

\[
H_{k,m}:=\{w\in\{a,b,c\}^+:\ |w|_b-|w|_c=0,\quad |w|_a+k|w|_c=km\}.
\]

これは先行報告 `chatgpt_power_rare_words_2026-11-02.md` §8 の族であり、**今回の新しい反例構成ではない**。`k=m=2` と固定すると `H=H_{2,2}` は19語、全部長さ4である。`φ(w)=|w|_c mod 2` として

`H'=H∩φ⁻¹(0) = {a⁴} ∪ {bbcc の異なる全順列}`

は7語である。よって `H'⊊H`、`min{|w|:w∈H\H'}=4`。

**すべての arity にわたる代入可能性の独立証明。** `d≥1`、正の `d`-タプル `x,y` と任意の一つの許容文脈 `E` が `E[x],E[y]∈H` を満たすとする。加法的写像

`F(w)=(|w|_b−|w|_c, |w|_a+2|w|_c)∈ℤ²`

について両辺が `(0,4)` なので、固定文脈の Parikh 寄与を消去すると `Σ_i F(x_i)=Σ_i F(y_i)`。従って**任意**の許容 `d`-文脈 `Q` で `F(Q[x])=F(Q[y])` となり、`Q[x]∈H ⇔ Q[y]∈H`。これは `d=1` と `d=2` を省略しない同一の計算であり、実際には全 `d≥1` に成立する。`s_U` の成分別型が等しいという条件を仮定しなくても成り立つ。

`H'` では上記二つの整数線形条件に `|w|_c≡0 (mod 2)` を追加する。同じ共通文脈から `Σ_i |x_i|_c≡Σ_i |y_i|_c (mod 2)` が従い、**任意の**許容 `Q` で三つの条件が同時に保存される。よって `H,H'` はどちらも `(d,s_U)` 代入可能、特に `(1,s_U)` と `(2,s_U)` 代入可能である。

**有限文法と数値の監査。** `H` の各語 `w` を一つの規則 `S→w` にした列挙 CFG を `G_H`、`H'` の7語を同様に並べた文法を `G_{H'}` とする。それぞれ reduced good、ファンアウト**1以下（従って2以下）**、規則ランク**0（従って2以下）**である。`|V|=1`、全規則が一つの4文字定数だから、原稿のサイズ定義で

`‖G_H‖=1+19(1+4)=96, θ̄_{G_H}=4`、

`‖G_{H'}‖=1+7(1+4)=36, θ̄_{G_{H'}}=4`。

従って `H,H'∈C_{2,s_U}`。原稿 `lem:distinguishing` から、`H` の特徴標本には `H\H'` の語が必要であるが、この方法が要求する最短語長は4にすぎない。**上界(2.3)と整合する**。

### 上界 `θ̄_G` はこれ以上一律には下げられない（鋭さ）

奇数 `m≥1` に対し `J_m={a^m,b^m}⊂{a,b,c}⁺` とする。`J'_m={a^m}=J_m∩{w:|w|_b≡0 (mod 2)}`。これは固定の可換群 `ℤ/2ℤ` による篩いであり、`min|J_m\J'_m|=m`。

`J_m` が**全 arity** で代入可能であることを直接確かめる。`d=1` で共通受理文脈 `E` に固定文字があるなら、その固定文字は `a` または `b` であり、`E[x]` と `E[y]` はともに同じ単一文字の長さ `m` の冪である。従って `x=y`（二つとも同じ文字で長さが等しい）。固定文字が全くなければ `E=□₁` で `x,y∈{a^m,b^m}`、両者の受理文脈は `E` のみで一致する。`d≥2` では許容文脈の中間セパレータが非空だから前者の場合しか起こらず、共有文脈から各成分 `x_i,y_i` は同じ文字の冪であることと、タプルの総長が等しいことが従う。任意の試験文脈 `F` に対して、`F[x]` と `F[y]` が同じ文字だけからなり長さ `m` となる条件は等価である。よって分布は一致する。これは型の一致を使わないので `J_m∈C_{f,s_U}`（任意 `f`）、単語言語 `J'_m` も同様である。

列挙文法 `S→a^m|b^m` は reduced good、ファンアウト1、ランク0、`‖G_m‖=2m+3`、`θ̄_{G_m}=m`。従って

`min{|w|:w∈J_m\J'_m}=m=θ̄_{G_m}`。

**定理2.2の係数1は鋭い**。この鋭さは定数規則の語そのものが長い例であり、`‖G_m‖` を小さく保つ超多項式例ではない。


## 4. D1 候補の再検査と有限全数検査

### (a) 群の語問題を2穴へ移す案

問題Gの既存報告は、CFG が**群の単位元ファイバーそのもの**を表すときの群サイズと厚さの関係を調べる。ところが本問の `L'` は、既に生成された `L` の**可換群剰余類による切出し**である。`L` の短い成功導出だけで全 Parikh 差格子が生成される（定理2.1）ため、内部に二成分を持たせても可換群フィルターの「最初の失敗」を長くできない。非可換群の語問題に関する既存の指数下界は、**可換群の篩い**についての反例ではない。

### (b) Parikh 格子の剰余案

任意の部分格子 `Λ≤ℤ^Σ` と coset `v+Λ` を選んでも、定理2.2を `A=ℤ^Σ/Λ` に適用できる。従って「すべての短い受理語は格子 coset に入り、長い受理語だけが外れる」は、最短外れ語が `θ̄_G` を超えるなら**不可能**である。`Λ` が無限指数でもこの純代数的な結論は成立する。ただし `L∩π⁻¹(v+Λ)` の MCFG 所属性は別途検証が必要であり、一般にはこの切出しのクラス内所属を自動主張できない。

### (c) 既存のショートカット／ブロック案

- `A₀→a|c`、`A_i→A_{i−1}A_{i−1}|c` は `‖G_n‖=8n+5`、`θ̄=n+1` で唯一の `c`-free 語 `a^{2^n}` を持つ。しかし原稿と先行レビューにある1穴の反例により、**標的 `L_n` 自体が `C_{1,s_U}` に入らない**。`L'` を篩いへ変更しても `L_n` の不適格性は修復されない。
- `L_{k,m}={a^k,bc}^m`（`k≥2,m≥3`）は先行報告の2穴反例により `C_{2,s_U}` に入らない。`k=2^p,m=2^q` の小さい CFG では `‖G‖=6(p+q)+10`、`θ̄=2^p+2^{q+1}−2` なので、対角 `p=q=n` では**厚さも指数的**。篩いへの変更だけでは二つの欠陥を解消しない。
- 原稿 `lem:power-transfer` は特定の語内のブロック間で冪を移すが、変換前後の Parikh ベクトルは一致する。したがって**Parikh 準同型の篩いはその二語を区別しない**。そのことと定理2.2は整合する。

### 全数検査の結果

付録Aの Python 3 標準ライブラリだけのコードで、対象有限言語の**すべての正の出現タプル**と**すべての許容共通文脈**を列挙した。受理語に現れない正のタプルは分布が空なので、違反の発見には不要であり、これは各有限言語についての**真の全数検査**である。

| 言語 | 語数 | 最大長 | `d=1` | `d=2` |
|---|---:|---:|---|---|
| 原稿の倍増族 `n=1` | 2 | 4 | PASS | PASS |
| 原稿の倍増族 `n=2` | 6 | 10 | PASS | **FAIL** |
| ショートカット倍増 `n=1` | 5 | 2 | **FAIL** | PASS（単独の2穴条件のみ） |
| ブロック `{aa,bc}³` | 8 | 6 | PASS | **FAIL** |
| `H_{2,2}` | 19 | 4 | PASS | PASS |
| `H_{2,2}∩{#c 偶数}` | 7 | 4 | PASS | PASS |

**明示的な2穴反例（原稿の倍増族、早くも n=2）。** `W₂=bbaabbaabb` は唯一の `c`-free 語である。タプル

`x=(bb,abb)`、`y=(bba,bb)`、

許容文脈 `E=□₁ a □₂ aabb`、`F=□₁ aabba □₂` と置くと、成分型は双方 `(1,1)` で、中間固定部はどちらも非空である。しかも

`E[x]=E[y]=F[x]=bbaabbaabb=W₂∈L₂`、

`F[y]=bbaaabbabb∉L₂`。

最後の不所属は、`F[y]` が `c`-free であるのに `W₂` と異なることから直ちに従う。従って **`L₂∉C_{2,s_U}`**。これは原稿 `thm:doubling-no-lift` の十分条件 `n≥2|S|+2` を、この具体例について小さな `n` にまで改善する個別観察であり、原定理を否定しない。

## 5. D2：一般の区別の道では何が残るか

### 5.1 証明済みの一般化

本報告の上界は、可換群値に関する**任意の剰余類（格子 coset）**のフィルターに対して成立する。群が有限か、群の元が巨大か、モジュラスが指数的かは問わない。`θ̄_G` という長さ上界は `‖G‖`、`f`、`r` にも依存しない。

`L'` が `L∩φ⁻¹(γ+H)` であり、有限可換群を用いるなら `L,L'∈C_{f,s}` の条件も原稿の closure proposition で満たされ、これを区別の補題へ正当に接続できる。`s_U` でも内容型付けでも同じである。

### 5.2 一般の `L'⊊L` に移せない理由

証明の決定的な行は `π(p_R)−π(q_R)=δ_R` と全木での **線形な総和(2.2)** である。任意の部分標的 `L'` は、二つの短い語が `L'` に入るならその Parikh 差を保存した全ての文も `L'` に入る、という閉性を持たない。従って局所差を格子へ蓄積する議論は使えない。

とくに、型削除 `L'=L\s_U⁻¹(1)` は `s_U` の値が **冪等半束**であり、群値の差として表現できない。ファンアウト1の三文字倍増族は `θ̄=4n` に対して `3·2^n−2` の型1語を強制するから、これを群フィルターと取り違えると定理2.2に矛盾する。半束型の受理集合との交わりにも、定理2.2を適用してはならない。

### 5.3 先行の唯一語補題の可否

| 先行補題・技法 | 多数の語にまたがる一般の差への適用 |
|---|---|
| 規則厚さ・最短の非終端タプル・成功導出での置換 | **適用可能**。本報告 §2 はここだけを利用 |
| 節点最小導出での同一非終端の再出現排除 | **そのままでは不可**。交換後の語が特定の唯一語に等しいという前提が消える |
| heavy 節点の層・反鎖を汚染 `c` へ変える密度補題 | **一般化未証明**。差集合が複数型にまたがる場合、交換した語がどちら側に入るか不明 |
| `lem:unique-word-gap` の「長い他型語」 | **そのままでは不可**。唯一語と別型語の二分が失われる |
| `lem:power-transfer` の2穴分布 | **語の移動としては適用可能**。ただし Parikh ベクトル不変なので可換群篩いの違反検出には直接効かない |
| 本報告の「局所 Parikh 差格子の生成」 | **群 coset 篩いには完全に適用可能**。一般の部分言語の代入可能性を代替するものではない |

**一般問題の判定：未解決。** 固定 `f=2,r≥2,s=s_U` について、任意の `L'⊊L`、`L,L'∈C_{2,s_U}` が常に `min|L\L'|≤poly(‖G‖,θ̄_G)` を満たすかは、本報告からは導けない。反例も構成していない。

## 6. D3：区別する部分標的の作り方と未解決問題への影響

以下は **固定三文字型付け `s_U`**、ランク上限 `r≥2`（下界の既存族は rank 2）についての分類。各欄は、**その作り方による真部分標的の差集合の最短語長が、`‖G‖,θ̄_G` に対して**どうなるかを表す。`μ^dist(L)` 全体は各行の最大を含むので、「一つの行の多項式」は `μ^dist` 全体の多項式上界ではない。

| `L'⊊L` の選び方 | `f=1, s_U` | `f=2, s_U` | 根拠 |
|---|---|---|---|
| 型の削除 `L\s_U⁻¹(m)` | **指数（族あり）** | **未解決** | 原稿 `prop:three-letter-family`、`thm:doubling-no-lift`、`op:fanout-two` |
| 一語削除 `L\{w}` がクラスに属する場合 | **指数（族あり）** | **未解決** | 三文字倍増族では唯一型1語を削除可能 |
| **有限可換群 coset** の篩い | **多項式（証明）** | **多項式（証明）** | 本報告定理2.2：実際に `≤θ̄_G` |
| **Parikh 格子 coset** の篩い（切出しがMCFLの場合） | **多項式（証明）** | **多項式（証明）** | 定理2.2：`ℤ^Σ/Λ`、有限・無限指数を問わない |
| `s_U⁻¹(Acc)` との交わり（真部分標的） | **指数（族あり）** | **未解決** | 型1の除去を `Acc={ζ}` と書ける |
| 任意の `L'⊊L`（総合 `μ^dist`） | **指数（族あり）** | **未解決** | 型削除の例を含む。ファンアウト2の一般上界も下界も未確定 |

**比較上の注意。** `Σ={a,c}` の二文字型付け `s_{U,2}` なら、原稿 `cor:two-letter-semilattice` は **`f≥2` の特徴データ全体の多項式上界**を証明している。これは上表の三文字 `s_U` に移植できない。また LG に属する型付けでは `thm:A(i)` から全特徴標本について上界がある。本定理は、逆に **非LGの半束型でも可換群篩いだけなら障害がない**と定式化した。

`op:S1`（ファンアウト1、二文字の一つの中立文字）について：本結果はどの可換群篩いの道も超多項式下界を与えないことを示すが、型の削除などを排除せず、**問題は未解決**。

`op:fanout-two`（半束のファンアウト2境界）について：同じく可換群篩いの道は閉じるが、一般の `L'` と希少型は残る。**ファンアウトで境界が動くか否かを決着させない**。

`prop:unique-word-route` について：本結果は唯一型語の長さ上界ではない。多くの語にまたがる群篩いによって唯一語の剛性を回避する構想があっても、**群篩いの区別距離は厚さ以下**になる。そのため、この経路では唯一語を使わない超多項式下界は得られない。

### 作用素・アルファベット・ファンアウト・ランクの最終確認

- **新しい上界(2.3)：**任意の有限アルファベット、任意ファンアウト、任意規則ランク（上限なしでも各有限文法で成立）、任意型付け、代入可能性不要。`L` と `G` の関係だけの主張で、学習作用素への仮定はない。
- **区別の補題からの下界：**`f=1` または `2`、固定 `Σ,s`、`L,L'∈C_{f,s}` のときのみ、`B^{≤r}_{f,s}`（すべての `r≥1`）および `B_{f,s}`、さらに両標的に特徴標本を持つ集合駆動作用素に適用。ファンアウト2の**新しい超多項式下界は存在しない**。
- **既存の指数例：**`f=1`、`Σ={a,b,c}`、`s_U`、rank 2、reduced good `‖G_n‖=13n+7, θ̄=4n`、唯一型1語の長さ `3·2^n−2`。この例を `f=2` の下界として主張しない。
- **小例 `H,H'`：**`f≤2` の表現（実際のファンアウト1）、rank 0（rank上限2の内側）、`Σ={a,b,c}`、`s_U`。差語長4は `B^{≤2}_{2,s_U}`、`B_{2,s_U}`、および両言語に特徴標本がある集合駆動作用素への区別補題と適合する。

## 7. 文献・限界・次の研究方向

**証明上の位置付け。** 原稿の `lem:thickness-equivalence` の「全非終端が短い生成組を持つ」「各規則に短い成功導出がある」という着想から、規則の両側で最短タプルを使い、**加法的な Parikh 差を短い二語で表す**のが本報告の核心である。Seki et al. (1991) の MCFG の非削除・線形テンプレートと整合する。Parikh 像に関する古典的な半線形性とは異なり、式(2.1)は**規則厚さによる生成語長の上界**を与える。本命題と同値の既存の定理があるかは**未確認**。査読原稿に移す場合、既存の重み付き文法・可換化・格子生成の補題との照合が必要である。

**本報告では証明していないこと：**一般の `μ^dist(L)` の多項式上界、`op:S1` の解決、`op:fanout-two` の解決、三文字 Parikh-saturated 言語全体のデータ上界、可換群以外の正則フィルターに対する同様の上界。有限全数検査の PASS から無限の族に関する代入可能性を推定していない。

**次の方向として合理的なのは**、(i) 可換群 coset では表現できない**非加法的な**部分標的を構成する、(ii) 二穴分布を保存しながら `c` の位置・順序を区別する部分言語を設計する、(iii) `L'` への所属が規則の局所差に関して閉じない場合の短縮不可能性を調べる、というもの。この提案自体は未証明である。

**参照したもの：**

1. Kuriyama, *Positive-Data Learning of Multiple Context-Free Languages under Fixed Finite-Semigroup Typing*, [作業原稿](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/main.tex)、2026-11-02取得。
2. [chatgpt_problemG_2026-11-01.md](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/reviews/chatgpt_problemG_2026-11-01.md)、[chatgpt_power_rare_words_2026-11-02.md](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/reviews/chatgpt_power_rare_words_2026-11-02.md)、[chatgpt_short_unique_words_2026-11-02.md](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/reviews/chatgpt_short_unique_words_2026-11-02.md)。主張を使う際は本報告の証明と区別した。
3. H. Seki, T. Matsumura, M. Fujii, T. Kasami, “On Multiple Context-Free Grammars,” *Theoretical Computer Science* **88** (1991), 191–229。プロジェクト資料03に収録。
4. R. Yoshinaka, “Efficient Learning of Multiple Context-Free Languages with Multidimensional Substitutability from Positive Data,” *Theoretical Computer Science* **412** (2011), 1821–1831。プロジェクト資料03に収録。
5. J. Esparza, P. Ganty, S. Kiefer, M. Luttenberger, “Parikh's Theorem: A Simple and Direct Automaton Construction,” *Information Processing Letters* **111** (2011), 614–619。Parikh 像の一般的背景。本報告の厚さ上界の先例であるとは主張しない。

---

## 付録A：Windows `py -3` で動く全数検査コード（全文）

**実行：**以下を `check_distinguishing.py` として保存し、PowerShell で `py -3 check_distinguishing.py`。Python 3 標準ライブラリ以外は不要。`d=1` と `d=2` を**別々に**調べる。`d=2` が PASS でも `d=1` が FAIL なら `(2,s_U)` ではない。比較が共有文脈に限られること、正の穴・非空中間セパレータを検査することに注意。

```python
"""Finite (1,s_U)/(2,s_U) substitutability checker; Python 3 stdlib only.

Save as check_distinguishing.py, run: py -3 check_distinguishing.py
Exact for the supplied finite languages. The source language L is not
truncated by word length. For any finite L, every positive tuple with
nonempty distribution arises as an occurrence in an accepted sentence.
"""
from collections import defaultdict
from itertools import product, permutations


def kind(word):
    return 'z' if 'c' in word else '1'


def instances(word, d):
    n = len(word)
    if d == 1:
        for i in range(n):
            for j in range(i + 1, n + 1):
                yield (word[i:j],), (word[:i], word[j:])
    elif d == 2:
        for i in range(n):
            for j in range(i + 1, n + 1):
                for k in range(j + 1, n):  # positive separator
                    for ell in range(k + 1, n + 1):
                        yield (word[i:j], word[k:ell]), (word[:i], word[j:k], word[ell:])
    else:
        raise ValueError('only d=1,2')


def fill(context, items):
    if len(items) == 1:
        return context[0] + items[0] + context[1]
    return context[0] + items[0] + context[1] + items[1] + context[2]


def exhaustive(language, d):
    """Returns (number of observed tuples, shared typed-context pairs, witness or None).

    witness = (common context, x, y, distinguishing context, accepted, rejected).
    """
    L = set(language)
    distributions = defaultdict(set)
    for w in L:
        for tup, ctx in instances(w, d):
            distributions[tup].add(ctx)
    groups = defaultdict(set)
    for tup, distribution in distributions.items():
        tp = tuple(map(kind, tup))
        for ctx in distribution:
            groups[(ctx, tp)].add(tup)
    compared = 0
    for (common, tp), tuples in sorted(groups.items(), key=lambda x: repr(x[0])):
        ordered = sorted(tuples)
        for idx, x in enumerate(ordered):
            for y in ordered[idx + 1:]:
                compared += 1
                dx, dy = distributions[x], distributions[y]
                if dx != dy:
                    if dx - dy:
                        z, q = x, y
                        witness = sorted(dx - dy)[0]
                    else:
                        z, q = y, x
                        witness = sorted(dy - dx)[0]
                    assert fill(common, z) in L and fill(common, q) in L
                    assert fill(witness, z) in L and fill(witness, q) not in L
                    return len(distributions), compared, (common, z, q, witness, fill(witness, z), fill(witness, q))
    return len(distributions), compared, None


def doubling(n):
    out = {'a'}
    for _ in range(n):
        out = {'b' + x + y + 'b' for x in out for y in out} | {'c' + x + 'c' for x in out}
    return out


def shortcut(n):
    out = {'a', 'c'}
    for _ in range(n):
        out = {x + y for x in out for y in out} | {'c'}
    return out


def blocks(k, m):
    return {''.join(t) for t in product(('a' * k, 'bc'), repeat=m)}


def weighted(k, m):
    # #b = #c = j; #a + k #c = k*m.
    out = set()
    for j in range(m + 1):
        a = k * (m - j)
        multiset = 'a' * a + 'b' * j + 'c' * j
        out.update(''.join(t) for t in set(permutations(multiset)))
    return out


def run(name, L):
    print(name, '|L|=', len(L), 'maxlen=', max(map(len, L)))
    for d in (1, 2):
        nt, np, bad = exhaustive(L, d)
        print('  d=', d, 'tuples=', nt, 'pairs=', np, 'status=', 'FAIL' if bad else 'PASS')
        if bad:
            E, x, y, F, good, no = bad
            print('    E=', E, 'x=', x, 'y=', y, 'F=', F)
            print('    F[x]=', good, 'F[y]=', no)


def main():
    for n in (1, 2):
        run('doubling_%d' % n, doubling(n))
    run('shortcut_1', shortcut(1))
    run('blocks_2_3', blocks(2, 3))
    H = weighted(2, 2)
    run('weighted_2_2', H)
    run('weighted_2_2_parity_c_even', {w for w in H if w.count('c') % 2 == 0})


if __name__ == '__main__':
    main()
```

**結論：**可換群の篩いについては、超多項式の区別語を構成できないというだけでなく、**区別語長 `≤θ̄_G`** と、全可換群篩いに共通の `O(|P|θ̄_G)` サイズの検出集合を証明した。一般の部分標的 `L'` に対する距離、したがってファンアウト2の未解決問題は残る。

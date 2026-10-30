# 二文字 U₁・ファンアウト1：厚さ指数の検証報告

| 主張 | 判定 | 根拠の節 |
|---|---|---|
| 全ての有限 `(1,s)`-代入可能言語で特徴データ長が `θ̄² poly(‖G‖)` 以下 | **未解決** | §8 |
| 無限言語も含む一般の (Q+)／指数が2を超える (Q−) | **未解決** | §8 |
| **正の加法重みが一定の言語**では、任意の reduced good CFG 表示について `μ* ≤ floor((θ̄+1)²/4)` | **証明済み** | §3 |
| 同じ条件で全ての純型非終端の収率長が `floor((θ̄+1)²/4)` 以下、`t_typ, τ ≤ max{floor((θ̄+1)²/4), |V|(θ̄−1)+1}` | **証明済み** | §2–§3 |
| 上の重み条件と代入可能性の下で、原稿の二つの再構成作用素に `O_r(‖G‖² θ̄²)` の共通特徴標本が存在 | **証明済み**（原稿の代表元再構成系を前提とする系） | §3.4 |
| この部分クラスの `μ*` 上界は、原稿の圧縮ブロック族で **等号達成**。`θ̄` の指数2は `poly(‖G‖)` を許しても下げられない | **証明済み** | §4 |
| 純 `b` 短絡を加える多段ブロック族が有限代入可能なら、短絡の長さは各段の既存の全 `b` 収率長に一致し、短絡は言語として冗長 | **証明済み** | §5.1 |
| 「正の重みが一定」なら代入可能、または有限代入可能なら必ず正の重みが一定 | **反証済み**（両方向とも偽） | §5.2、§6.3 |
| 過去の有限言語特徴付けの結論 | **証明済み**（既報の証明の一箇所を修復） | §6.2 |
| 今回の二段短絡96件・一般短絡120件の合否や比率 | **観測** | §7、§11 |

**結論。** 一般の問いは決着していない。一方、依頼に挙げられた「正の加法重み ψ を固定し、ブロック数や内部符号化を変える」方針全体に対し、**条件付き (Q0) を完全証明した**。その条件下では、元の文法をどのように圧縮しても二乗を超えず、しかも稀な型の最短長には鋭い定数を含む上界がある。重み係数は言語ごとに変えてよく、係数の大きさに依存する隠れた定数はない。

**文献上の新規性：未調査。** 本報告は取得した原稿・指定された三報告との比較であり、公刊文献に対する新規性を主張しない。既存の二乗下界は今回の新発見として数えていない。

## 1. 取得版、定義、適用範囲

### 1.1 最新 main の取得記録

2026-10-30 に GitHub の `main` から取得し、同時に取得した Git checkout の内容とも照合した。

- Repository: `growupkuriyama-hub/papers`（GitHub の表示名は `Papers`）。
- 原稿: <https://github.com/growupkuriyama-hub/papers/blob/main/02_fixed-h-mcfg/main.tex>
- **取得した `main.tex` の Git blob SHA: `17858cdfac03203c2814bc0d01806a340bd4b814`**。
- 照合した checkout の HEAD commit: `b9ed3a4b2fc4cb8170eec576479069a718e57081`。
- commit 時刻: `2026-10-30T12:48:27Z`。blob SHA と commit SHA は別物である。
- 固定版: <https://github.com/growupkuriyama-hub/papers/blob/b9ed3a4b2fc4cb8170eec576479069a718e57081/02_fixed-h-mcfg/main.tex>

指定された過去の報告も同じ checkout の blob と一致した。

| `02_fixed-h-mcfg/revision/` 内のファイル | Git blob SHA |
|---|---|
| `astra_binary_u1_fanout1_2026-10-30.md` | `87578f506fd5f0f32cde7525224f8de1022e5d15` |
| `deepseek_binary_u1_f1_search_2026-10-30.md` | `e548e67c68d415a5ca1c2cd500db665aa5c01a6f` |
| `chatgpt_binary_u1_fanout1_2026-10-30.md` | `d66f45edf797c6d7453fb9c37456a2c99220e4ed` |

添付の `project-master-v15-2026-10-28.md` の正本ルーティングも確認した。原稿・リポジトリのファイルは変更していない。本報告の版固定後の更新は対象外。

### 1.2 原稿との対応

| 読んだ箇所 | 本報告での位置づけ |
|---|---|
| `prop:binary-u1-quadratic`、`app:binary-u1-quadratic` | 出発点の圧縮ブロック族。§4で再証明し、新しい上界との等号を示す。 |
| `rem:fanout-one-data` | 二文字・一穴の一般多項式問題は未解決。 |
| `thm:binary-u1-polydata`、`app:binary-u1` | ファンアウト2の結果。一般上界として一穴へ流用しない。 |
| `lem:app-u1-shallow`、`lem:app-u1-runs` | 一穴にも適用できる条件付き上界。今回の重み上界は別の証明。 |
| `lem:app-lf-descent` | 最短成功規則使用の分解式と長さ下降。§2で必要な分解式を再証明。 |
| `cor:distribution-representatives` | `τ` 上界から特定の再構成作用素の特徴標本へ移す。 |
| `prop:rare-type` | 任意のクラス全域の集合駆動型作用素に対する下界。§4.3で識別論法も記す。 |
| `def:standard-mcfg`、`def:grammar-properties` | 記号サイズ、rank、reduced/good の定義。 |
| `def:tuple-substitutable`、`lem:thickness-equivalence` | 非空因子のみを比較する一穴分布、元の文法の厚さ。 |

### 1.3 記号

以下、`Σ={a,b}`、`s(a)=1`、`s(b)=ζ`。純語は `a⁺` の語、混合語は **bを少なくとも一つ含む語**（`b^j` も混合）。`G` は非空の `L⁺=L∩Σ⁺` の reduced good CFG、rank≤r、`r≥2` 固定とする。`L⁺=∅` は正語のデータを必要とせず別扱いにできる。

\[
 v=|V|,\quad g=\|G\|,\quad \theta=\bar\theta_G,\quad
 B(\theta)=\left\lfloor\frac{(\theta+1)^2}{4}\right\rfloor.
\]

`g=|V|+Σ_R(1+rank(R)+テンプレート中の端末・変数出現数)`。`θ_G(R)` は **Rを少なくとも一度使う成功導出の文全体の最短長**、`θ=max_R θ_G(R)≥1`。全規則を同じ文で使う量ではない。

一穴分布は `D_L(x)={(u,v):uxv∈L}`。`x,y` は非空で、同型・共有文脈があれば分布が等しいことを `(1,s)`-代入可能性と呼ぶ。

`μ*` は実現した二つの語型の最短受理長の最大。`t_typ` は実現した型付き非終端の最短生成収率長の最大。`τ` はそれらの **同型・同分布類** の最短代表長の最大。したがって `μ*≤τ≤t_typ`。`t_typ` の下界をデータ長の下界に読み替えない。

`ε∈L` のときは正語について証明し、最後に datum `ε` の符号長1を加える。空因子は比較しない。

## 2. 任意の CFG に使える二つの補題

### 2.1 最短成功使用の正確な分解

**補題1。** `d_A=min{|w|:w∈L_A(G)}`、`o_A` を成功導出の A 部分木を除いた文脈の最小固定長とする。規則 `R:A→ρ(A₁,…,A_q)` が明示的に `c_R` 文字を書くとき

\[
 \theta_G(R)=o_A+c_R+\sum_{j=1}^q d_{A_j}.\tag{2.1}
\]

特に `d_A≤θ`、`c_R+Σd_{A_j}≤θ`。

**証明。** R を使う成功導出でその出現を一つ選ぶ。外部文脈は長さ≥`o_A`、各子は長さ≥`d_{A_j}`。非削除・線形性からこれらと明示文字が重複なく文を構成し、下界を得る。逆に、最短外部文脈に R を置き、各子をそれぞれ最短収率で完成すれば等号を達成する。reduced 性でこれらは全て存在し、長さは非負整数なので最小値を達成する。A の最短収率を導く根規則を選べば `o_A+d_A≤θ`。この議論に文法の非循環性は不要。□

### 2.2 混合型の上界は一般に線形

**補題2。** 代入可能性を仮定せず、混合語を生成する任意の非終端 A について

\[
 \min\{|w|:w\in L_A(G),\ |w|_b>0\}
 \le v(\theta-1)+1.\tag{2.2}
\]

さらに、L が混合語を持てば `μ_ζ(L)≤θ`。

**証明。** A から到達でき、明示的に b を書く規則 R がある。その左辺 B への最短依存経路を選ぶ。この経路は非終端を繰り返さず、A と B を含めて q≤v 節点を持つ。経路の各規則では次の節点に至る子だけを残し、その他の子を最短収率で完成する。

末端規則 R の全ての子も最短にすれば、その局所収率長は≤θで、明示 b を含む。それより上の一段で付け加える長さは、指定された経路子 C の最短長を局所最短長から引いた値で、補題1より≤`θ−d_C≤θ−1`。従って全長は≤`θ+(q−1)(θ−1)≤v(θ−1)+1`。明示 b は非削除性で残る。

最後の主張は、明示 b を書く任意の規則の最短成功使用を取ればよい。その文は b を含み、長さ≤θ。□

したがって一般問題の難所は純型である。ただし混合型非終端への bound と、開始記号への bound は異なる。

## 3. 主結果 (Q0)：正の加法重みが一定なら二乗で止まる

### 3.1 仮定と非終端への重みの移送

ある実数 `λ>0`、`W>0` が存在し、全ての `w∈L(G)` が

\[
 \psi(w):=|w|_a+\lambda|w|_b=W\tag{H}
\]

を満たすと仮定する。一般の正の重み `α|w|_a+β|w|_b=C` は α で割ればこの形になる。`λ,W` は固定されたクラス定数ではなく、**対象言語ごとに任意に変わってよい**。以下の上界には `λ,W` は現れない。

(H) は正の重みなので L は有限になるが、有限性だけから (H) は従わない（§6.3）。また (H) 自体は代入可能性を意味しない（§5.2）。

**補題3。** 各非終端 A の全収率は共通の重み `w_A>0` を持つ。純収率が存在すれば、それは唯一の語 `a^{w_A}` であり、`w_A` は正整数となる。

**証明。** reduced 性で A の固定成功文脈 `(u,v)` がある。全ての `z∈L_A` について `uzv∈L` だから、加法性により `ψ(z)=W−ψ(u)−ψ(v)` は z に依存しない。正語の重みは正。純語 `a^ℓ` の重みは ℓ なので純収率は一意。□

### 3.2 純型の鋭い上界

**定理4（重み一定言語の純収率上界）。** (H) を満たす G の任意の純語生成非終端 A について、その唯一の純収率 `a^{ℓ_A}` は

\[
 \boxed{\ell_A\le B(\theta)
       =\left\lfloor\frac{(\theta+1)^2}{4}\right\rfloor.}\tag{3.1}
\]

この主張には代入可能性も rank の固定も必要ない。

**証明。** `θ≥1` であるから `θ≤B(θ)`。

1. **`0<λ≤1` の場合。** A の最短無型収率 z は長さ≤θ。補題3から `ℓ_A=ψ(z)≤|z|≤θ`。

2. **`λ>1` かつ `ℓ_A<λ` の場合。** b を含む語の重みは少なくとも λ なので、A は混合収率を持てない。純収率は一意であるから `ℓ_A=d_A≤θ`。

3. **`λ>1` かつ `ℓ_A≥λ` の場合。** `a^{ℓ_A}` の任意の有限導出木を取り、純収率長が≥λである節点のうち、子にその条件を満たす節点がないものを一つ選ぶ。その非終端を B、純収率長を h、適用規則を R とする。`h≥λ` であり、各子 C の純収率長は `<λ`。

   補題3によりその子 C は混合収率を持てず、唯一の純語だけを生成する。規則 R 自身も純導出に現れるため明示 b を書かない。従って **R の局所収率は、どの子導出を選んでも長さ h の純語** である。これが肝心な点で、短い混合子で R の最短使用をさらに縮めることはできない。

   R の最短成功使用を実現する文の当該出現を選ぶ。その内側は長さ h、重み h である。(H) より外側の重みは `W−h`。一文字の重みは最大 λ なので外側の文字数は少なくとも `(W−h)/λ`。従って

   \[
   \begin{aligned}
   \theta&\ge\theta_G(R)
      \ge h+\frac{W-h}{\lambda}\\
      &=\frac W\lambda+\left(1-\frac1\lambda\right)h
      \ge\frac W\lambda+\lambda-1.
   \end{aligned}\tag{3.2}
   \]

   よって

   \[
    \ell_A\le W\le\lambda(\theta+1-\lambda)
      =\frac{(\theta+1)^2}{4}
        -\left(\lambda-\frac{\theta+1}{2}\right)^2
      \le\frac{(\theta+1)^2}{4}.
   \]

   最初の `ℓ_A≤W` は、A の成功文脈の重みが非負であることから従う。`ℓ_A` が整数なので床を取れる。

全場合を尽くした。□

**解釈。** 「長い a ブロックの内部まで短絡する」には、純収率が初めて b 一文字分の重み λ に達する規則を通る。その規則の子はまだ b を生成できないため、その局所使用長≥λを短絡できない。さらに外部を完成する最低限の文字数が `(W−h)/λ` 必要になる。両方を同じ規則の成功使用で数えると、単なる `θ≥λ` と `θ≥W/λ` より強い **和の制約** (3.2) が得られる。

### 3.3 μ*・t_typ・τ の結論

**系5。** (H) の下で

\[
 \boxed{\mu^\star(L,s)\le B(\theta),\qquad
 t_{\rm typ}(G,s)\le
 T:=\max\{B(\theta),\ v(\theta-1)+1\}.}\tag{3.3}
\]

L が代入可能なら同じ T が τ の上界になる。

**証明。** 純型開始記号があれば定理4を適用する。混合型があれば補題2の開始記号についての別の結論 `μ_ζ≤θ≤B(θ)` を用いる。実現型が一つでも同じ結論。各非終端について純型は定理4、混合型は補題2で評価できるため `t_typ≤T`。生成収率自身がその分布類の代表なので `τ≤t_typ`。□

ここで `μ*` と特徴標本の**総符号長**は別物であり、総符号長の上界まで定数 `1/4` が鋭いとは述べていない。

### 3.4 特徴データの条件付き二乗上界

**系6。** さらに `L∈C^{mcf}_{1,s}` とする。原稿の二つの作用素 `B^{≤r}_{1,s}` と `B_{1,s}` は共通の特徴標本 K を持ち、

\[
\begin{split}
 \|K\|_+
 &\le 3^r g\,[1+2\theta+rT]+\mathbf1_{\{\varepsilon\in L\}}\\
 &\le 3^r(r+3)g^2\theta^2+\mathbf1_{\{\varepsilon\in L\}}.
\end{split}\tag{3.4}
\]

**証明。** `cor:distribution-representatives` の仮定は、good/reduced、rank≤r、代入可能性で満たされる。型付き非終端・規則の合計は `N_typ≤3^r g`。実際、正の非終端型は高々2個、rank q の規則の子型選択は高々 `2^q` 通りであり、この表示はそれを上から評価している。系5の `τ≤T` を同系の

`‖K‖_+≤N_typ(1+2θ+rτ)+1_{ε∈L}`

へ代入すれば第一不等式。具体的には、各型付き非終端 X の最短分布代表を、その元非終端の短い成功文脈へ挿入した文と、各型付き規則の子をこれらの代表で埋めて同じ文脈へ挿入した文を集める。原稿の witnessed composition と再構成系により、両作用素で全ての有限正例拡張に対して復元が L となる。

`B(θ)≤θ²`、`v(θ−1)+1≤vθ≤vθ²` より `T≤vθ²≤gθ²`。また `1+2θ≤3θ²`、`g≥1` なので第二不等式を得る。□

**量化。** これは特定の二作用素についての標本の存在定理である。「任意の集合駆動型作用素がこの長さを達成する」とは言っていない。

## 4. 等号を達成する既存の圧縮ブロック族

本節は原稿の下界を再確認する部分であり、今回新たな下界族ではない。

### 4.1 全因子・全文脈に対する代入可能性

整数 `k,M≥1` に対し `L_{k,M}={a^k,b}^M` と置く。語が L に属する必要十分条件は、全ての極大 a-run の長さが k の倍数であり、`ψ(w)=|w|_a/k+|w|_b=M` となること。最大 a-run を `a^k` ごとに区切り、各 b を一つのブロックにすれば十分性も従う。

同型非空 x,y が `(u,v)` を共有すると仮定する。重みの加法性から `ψ(x)=ψ(y)`。

純型なら `x=a^p,y=a^q` に対して `p/k=q/k`、従って x=y。

混合型なら `x=a^α x' a^β`、`y=a^{α'}y'a^{β'}` と書く。x',y' は b で始まり b で終わる。内部の a-run は既に k の倍数である。u の末尾 a-run 長を t、v の先頭 a-run 長を z とすると、共有文脈によって `t+α,t+α',β+z,β'+z` は k の倍数。従って `α≡α' (mod k)`、`β≡β' (mod k)`。

任意の文脈 `(p,q)` に対し、`pxq` と `pyq` の a-run 条件は一致する。内部条件は上記の通り、p,q の内部条件は共通、二つの境界条件は α,β の剰余だけで決まるからである。また総重みも等しい。従って `pxq∈L⇔pyq∈L`。これで任意のパラメータ・全ての因子・全ての文脈に対する代入可能性を示した。有限言語なので CFG 言語でもある。□

### 4.2 元の圧縮文法の正確な厚さ

`k=2^m,M=2^n`、`m,n≥1` として

\[
 C_0\to a,\quad C_j\to C_{j-1}C_{j-1}\ (1\le j\le m),
\]
\[
 A_0\to C_m\mid b,\quad
 A_i\to A_{i-1}A_{i-1}\ (1\le i\le n),\quad S=A_n.
\]

帰納的に `L(C_j)={a^{2^j}}`、`L(A_i)={a^k,b}^{2^i}`。全規則・非終端が成功導出に現れ、全て good、rank≤2。

非終端数は `m+n+2`、規則サイズは順に `2`、`5m`、`3`、`2`、`5n`。従って `g=6m+6n+9`。

| 非終端 | 最短収率 d | 最短外部長 o |
|---|---:|---:|
| A_i | `2^i` | `M−2^i` |
| C_j | `2^j` | `M−1+k−2^j` |

A_i の外部では残る `M−2^i` ブロックを全て b にする。C_j は C_m 内の残り `k−2^j` 個の a が必須で、外側の `M−1` ブロックを b にする。これらは下界を達成しているため正確値である。補題1より

| 規則 | 正確な最短成功使用長 |
|---|---:|
| `A_i→A_{i−1}A_{i−1}`、`A_0→b` | M |
| `A_0→C_m`、全ての C_j の規則 | `M+k−1` |

従って **`θ=M+k−1`**。純型最短受理長は `kM`、混合型最短受理長は M なので `μ*=kM`。全ての型付き非終端には長さ≤kMの収率があり、純型開始記号の分布代表は唯一の純受理語であるから `τ=t_typ=μ*=kM`。

`m=n` では `k=M`、`θ=2k−1` なので

\[
 \boxed{\mu^\star=\tau=t_{\rm typ}=k^2
       =\frac{(\theta+1)^2}{4}.}\tag{4.1}
\]

(H) の正規化では `λ=k,W=kM`。定理4の上界の等号である。

### 4.3 任意の集合駆動型作用素への下界

特徴標本 F は「任意の有限 `F⊆D⊆L` に対して作用素の出力言語が L」とする原稿の意味で用いる。全クラスに特徴標本を持つ集合駆動型作用素を任意に取る。

`L'=L\a⁺` もクラスに属する。実際、同型 x,y を同じ文脈に入れた全体の型は等しいため、L の分布等値を全体型 ζ に制限しても保たれる。文脈自由性は正規言語との共通部分で保たれる。ここでは有限なのでその点も直接明らか。

F が純語を含まなければ `F⊆L'`。L' の特徴標本 F' との和 `F∪F'` は L と L' の両方に含まれ、両方の特徴標本を拡張する。その一つの入力への出力が L と L' の両方でなければならなくなり矛盾。従って F は唯一の純語 `a^{kM}` を含み、`‖F‖_+≥kM+1`。原稿の二作用素についても rare-type 命題、またはそれらの class-wide characteristic property で同様。

`m=n` なら `g=12n+9`、`θ=2^{n+1}−1`、下界は `4^n+1`。任意の固定 `c<2` と多項式 p について

\[
 \frac{4^n}{p(12n+9)(2^{n+1}-1)^c}\longrightarrow\infty.
\]

よってこの部分クラスでさえ `θ^c poly(g)` の総特徴データ上界は不可能。**指数2は重み一定部分クラスでは確定した**。指数2での g の最適次数は本報告では決めていない。

## 5. 多段化を試す：全 b 短絡の剛性と失敗証明書

### 5.1 多段の純 b 短絡は重みを変えられない

**命題7。** 整数 `k≥1`、`M_j≥2`、`u_j≥1` に対し

\[
 K_0=\{a^k,b\},\qquad
 K_j=K_{j-1}^{M_j}\cup\{b^{u_j}\}\quad(1\le j\le d).
\]

`K_d` が `(1,s)`-代入可能なら、全ての j で

\[
 u_j=\prod_{i=1}^j M_i,
 \qquad K_d=\{a^k,b\}^{\prod_{i=1}^d M_i}.
\]

従ってどのような圧縮 CFG 表示を使っても、系5–6の二乗上界が適用される。

**証明。** 有限代入可能言語には異なる二つの正の b 冪は共存できない。もし `b^p,b^q∈L`、p<q なら同型で空文脈を共有するため分布が一致し、`(ε,b^{q-p})` に対して交換を繰り返すと `b^{p+t(q-p)}∈L` が全ての t≥0で成立してしまう。

各段の全 b 収率は上位の段で他の全スロットを b 冪で埋めて根へ持ち上げられる。したがって同じ段に異なる b 冪が二つあれば最終段にも異なる b 冪が二つ生じる。帰納的に `K_0` の b 冪長は1、`K_{j-1}^{M_j}` の b 冪長は `∏_{i≤j}M_i` に固定され、短絡の長さ u_j はそれに一致する必要がある。一致すると追加した b 冪は既に `K_{j-1}^{M_j}` にあるので冗長であり、帰納的に表示の等式が従う。§4.1によりこの場合の代入可能性も成り立つ。□

明示的な `b^{u_j}` を倍増文法で圧縮しても、この言語論的必要条件は変わらない。また一般の (H) の上界は表示に依存しないので、圧縮で別の抜け道が生じることもない。

### 5.2 b の側も長いトークンにする場合

二段の試験族を

\[
 J_{k,t,M,u,P}
 =\left(\{a^k,b^t\}^{M}\cup\{b^u\}\right)^P
 \quad(M,P\ge2)
\]

とする。全 b 語 `b^{tMP}` と `b^{uP}` があるため、代入可能なら必ず `u=tM`。このとき言語は `{a^k,b^t}^{H}`、`H=MP≥4` に等しい。

`t=1` なら §4.1 で代入可能。**t≥2 の場合は代入可能でない。** 全パラメータに通用する証明書は

\[
 x=b^{2t},\quad y=a^k b^t,\quad
 E=(\varepsilon,b^{(H-2)t}),\quad
 F=(b,b^{(H-2)t-1}).
\]

x,y はどちらも混合型。`E[x]=b^{Ht}` と `E[y]=a^k b^{(H-1)t}` はそれぞれ H ブロックからなり受理される。`F[x]=b^{Ht}` も受理されるが、`F[y]=b a^k b^{(H-1)t-1}` は先頭の極大 b-run が長さ1であるため `{a^k,b^t}^H` に属さない。

従って試験範囲に限らず、`J` の代入可能性は **`t=1` かつ `u=M`** と同値。この失敗は「重み一定 ⇒ 代入可能」という誤った推論を排除する。上界定理4は代入可能性を仮定しないので、この失敗によって影響されない。

### 5.3 a-padding を持つ短絡

`J=( {a^k,b}^M ∪ {z} )²` で z を一般の短い二文字語にした。§10の完全判定器が得た例：

| k,M,z | g,θ,μ* | 同型因子 x,y | 共有文脈 E | 区別文脈 F | `F[x]∈J,F[y]∈J` |
|---|---|---|---|---|---|
| 2,2,aba | 30,5,8 | aaaaab, aabaaa | (ε,a) | (a,ε) | true,false |
| 2,2,bab | 30,5,8 | aaaaba, aabaaa | (ε,a) | (ε,b) | true,false |
| 2,4,ab | 35,7,16 | a, aaaaaa | (ε,aaaaaaaab) | (ε,aaaaaaaaaa) | false,true |

各行は完全に指定された有限言語に対する反証書であり、全パラメータについての不可能性定理ではない。特に、一般の z を含む多段構成を全て否定したとは述べない。

## 6. 有限言語の構造：再検証と既報の証明修復

### 6.1 純因子の剛性と混合受理語の分布

**補題8。** 有限で `(1,s)`-代入可能な L では、各固定文脈 E が受理する純因子は高々一つ。

**証明。** `E[a^p],E[a^q]∈L`、p<q とする。純因子は同型で E を共有するので分布一致。`d=q−p` として、`E=(u,v)`、`E_k=(u a^{kd},v)` を使うと、`E_k[a^p]` の受理から分布一致によって `E_k[a^q]=E_{k+1}[a^p]` の受理を得る。k=0から帰納すると無限個の相異なる語が L に入る。矛盾。□

従って純受理語は高々一つ。また各純型非終端の純収率も一つで、その分布類の純代表はその語自身のみとなる。すなわち有限の場合、純型について **`τ_{A,1}=ℓ_A`**。これは一般の無限言語には使えない。

**補題9。** 有限で `(1,s)`-代入可能な L の各混合受理語 w は `D_L(w)={(ε,ε)}` を満たす。

**証明。** 全ての混合受理語は同型で空文脈を共有するので同じ分布を持つ。この分布が正の固定長を持つ文脈 `(u,v)` を含むなら、任意の混合受理語 z から `uzv` を作れ、これも混合受理語である。反復すると長さが無限に増加して有限性に反する。□

### 6.2 有限特徴付けの修復

**命題10。** 有限 L の代入可能性は、次の二条件と同値である。

(i) 純受理語は高々一つ。

(ii) 共通文脈を持つ任意の二つの混合因子の分布が等しい。

**証明。** 必要性は補題8と定義から従う。十分性は混合同士について (ii) そのものなので、同じ文脈 `(u,v)` に受理される `a^i,a^j`、i<j の存在を排除すればよい。

u,v がともに a のみからなる場合は、異なる二つの純受理語ができて (i) に反する。u が b を含む場合、混合因子 `x=u a^i`、`y=u a^j` は文脈 `(ε,v)` を共有するので (ii) から分布一致。`d=j−i` として文脈 `(ε,a^{kd}v)` を使うと、`u a^{i+kd}v∈L` から `u a^{i+(k+1)d}v∈L` を得る。これを反復すると無限個の語となり矛盾。

u が b を含まず v が b を含む場合は、混合因子 `x=a^i v`、`y=a^j v` と文脈 `(u a^{kd},ε)` で同じ反復をする。従って i<j は不可能で、純同士の分布条件も満たす。□

**既報の証明の問題点。** DeepSeek 報告 §3.3 は「`ua^iv` は `ua^jv` の真の因子」としていたが、一般には偽。例えば u=b,v=ba,i=1,j=2 では `baba` は `baaba` の因子ではない。上記はその箇所を **混合接頭辞／接尾辞の分布一致からの反復** で置き換えた証明である。特徴付けの結論自体は保持できるが、誤った因子包含を今後の証明で使ってはいけない。

### 6.3 重み一定は有限クラス全体を覆わない

`L₀={aa,ab,bbb}` は代入可能だが、正の一定加法重みを持たない。

代入可能性を解析的に確認する。非空因子は a,aa,ab,b,bb,bbb のみで、分布は次の通り。

| 因子 | 型 | 全分布 |
|---|---|---|
| a | 1 | `{(ε,a),(a,ε),(ε,b)}` |
| aa | 1 | `{(ε,ε)}` |
| b | ζ | `{(a,ε),(ε,bb),(b,b),(bb,ε)}` |
| bb | ζ | `{(ε,b),(b,ε)}` |
| ab | ζ | `{(ε,ε)}` |
| bbb | ζ | `{(ε,ε)}` |

同型因子について、異なる分布は互いに交わらず、共有する ab と bbb の分布は一致する。その他の語の分布は空であり、共有文脈条件を満たさない。よって全因子について代入可能。

一定重み (H) があれば aa と ab から `2=1+λ`、すなわち λ=1。そのとき bbb の重みは3で aa の2と異なる。従って (H) は存在しない。□

この例により、§3だけでは有限の場合の一般 (Q+) は証明できない。

## 7. 計算検証の範囲、正確性、観測結果

### 7.1 判定・測定方法

§10は標準ライブラリのみの再現コードである。有限言語を完全生成し、全語 w、全切断 `0≤i<j≤|w|` について因子 `w[i:j]` と文脈 `(w[:i],w[j:])` を登録する。これは全分布と厳密に一致する。分布が空の非出現因子は共有文脈を持てないため無視してよい。

同型・同文脈のグループ内で全分布を比較し、不一致なら因子対、共有文脈、区別文脈、区別文脈での受理真偽を返す。グループ内で最初の一因子との比較だけで足りるのは、集合の等しさが同値関係だからである。

厚さは無型最短収率 d と最短外部長 o を min-plus 緩和で計算して、**元の文法の各規則**に (2.1) を適用した値の最大。試験文法は全て非循環で、規則の最短長を独立に実現できる。型付き収率は完全生成された各非終端言語から直接求める。代入可能性を通過した場合のみ、分布集合が等しい同型因子の最短長を使って τ も正確に求める。

### 7.2 結果（全て観測）

- 圧縮ブロック族6件を完全生成・完全判定。最大256語。`μ*=τ=t_typ`、各規則の正確な θ、§4の式と一致。
- `m=n=1,2,3,4,6,8,12` は整数 DP で厚さを算出し、解析的な `μ*=4^n` と等号を照合。大きい n では全語生成をしていない。この区別をログにも記した。
- 二段 b 短絡：`k∈{2,3,4},t∈{1,2},M∈{2,4},u=1,…,8,P=2` の **96件**を全検査。合格6、不合格90、未検査0。§5.2の解析的分類と一致。合格例の最大 `μ*/θ²` は 1/3。
- 一般短絡：`k∈{2,3},M∈{2,4}`、全ての長さ1～4の二文字語 z、計 **120件**を全検査。合格9、不合格111、未検査0。合格した全例で z は既存の `{a^k,b}^M` に既に含まれた。**この最後の観測を、任意の z への不可能性証明には使わない。**
- 厚さや比率が良くてもクラス所属に失敗する例：`k=2,t=1,M=2,u=1,P=2` は `μ*/θ²=1/2` だが代入可能でない。

開発途中には「u=tMならt>1も合格する」という仮のテスト期待値を置いたが、完全判定で失敗した。§5.2の証明書を調べ、最終コードでは正しい期待値 `t=1,u=M` に直した。失敗した試行の唯一の標準エラーは以下だった（最終コードの完全ログは§11）。

```text
Traceback (most recent call last):
  File "/workspace/scratch/1c3c685b0758/repro.py", line 183, in <module>
    if __name__=='__main__': main()
                             ^^^^^^
  File "/workspace/scratch/1c3c685b0758/repro.py", line 158, in main
    assert (c is None)==(u==t*M)
           ^^^^^^^^^^^^^^^^^^^^^
AssertionError
```

計算はいずれも普遍命題の証明の代用ではない。§3、§4、§5.1–§5.2、§6の一般命題には別途完全な解析的証明を載せた。

## 8. 残る一般問題と十分な未証明命題

### 8.1 今回証明していないこと

一般の有限 L が重み一定であることは偽。各文脈・非終端に異なる局所重みを与え、それらを両立させる議論は未完了。有限性から得られる純因子長の一意性だけでは、全非終端に共通する正の λ は出ない。

無限言語は正の一定重み (H) の対象外である。純因子の分布類が複数の長さを含む場合に、生成収率でなく最短分布代表を短縮する一般的な方法は本報告では得ていない。

既報の指数欠陥立方体・`log M`・b個数／長さスペクトル上界は障害を説明するが、「多くの混合語がある」ことだけは有限性にも因子反鎖性にも矛盾しない。今回、それらから一般の二乗上界へ進む未証明の推論はしていない。

### 8.2 (Q+) に十分な未証明命題 U₂

> **U₂（未証明）。** 固定 r に対して多項式 `q_r` が存在する。任意の `L∈C^{mcf}_{1,s}` とその reduced good、rank≤r 表示 G、純型を実現する各非終端 A について、長さ≤θの導出的成功文脈 E_A を選び、
> \[
> \kappa_A:=\min\{j\ge1:E_A[a^j]\in L\}
> \le q_r(g)\theta^2.
> \]

**十分性の証明。** E_A に受理される同型因子は、元の純収率と文脈を共有するため代入可能性で同じ分布を持つ。逆に同じ分布の因子は E_A に受理される。従って `τ_{A,1}=κ_A`。混合型は補題2から `τ_{A,ζ}≤v(θ−1)+1`。原稿の代表元再構成系で `‖K‖_+≤3^r g[1+2θ+r max{q_r(g)θ²,v(θ−1)+1}]+1`、すなわち二乗×g多項式が従う。□

有限言語に限定した U₂ なら、補題8によって `κ_A=ℓ_A` である。従って有限版の核心は **純語生成非終端の唯一の純収率長を、元の無型厚さの二乗で抑えること** に帰着する。§3は共通の正の加法重みが存在する場合に、この命題を `q_r=1` より鋭く証明したもの。

### 8.3 (Q−) に十分な未証明命題 N₂₊

> **N₂₊（未証明）。** ある固定 δ>0、整数 d≥1、定数 C と、有限代入可能言語 L_n の reduced good、rank≤2 表示 G_n が存在し、
> \[
> g_n\le C n^d,\quad \theta_n\ge2^n,\quad
> L_n\cap a^+=\{a^{N_n}\},\quad
> N_n\ge\theta_n^{2+\delta}/(C n^d).
> \]

**十分性の証明。** §4.3の型削除による識別論法から全てのクラス全域の集合駆動型作用素の特徴標本は長さ≥N_n+1。任意の多項式 p に対し `N_n/[θ_n²p(g_n)]≥2^{δn}/poly(n)→∞`。従って二乗×g多項式上界は不可能となる。□

この n の正規化は一つの十分条件であり、(Q−) の必要条件とは主張しない。注意として、単に `μ*≥θ^c/poly(g)`、c>2 と書くだけでは g と θ の関係次第で `θ²poly(g)` と両立し得る。指数を区別するには、上のように多項式 g 因子を超える増大条件も必要である。

§3により N₂₊ の候補は、少なくとも十分大きい n では正の一定加法重み (H) を持てない。§5.1型の全 b 短絡の多段化でも構成できない。それ以外の構成、または無限言語による反例の存在は未解決。

## 9. 論文挿入用 English LaTeX 案

以下は一般問題を解決したと述べず、重み一定の条件付き定理を挿入する案である。既存の thickness lemma と representative corollary の記法を使用する。最終の sharpness は既存 `prop:binary-u1-quadratic` と本報告§4に対応する。文献上の新規性は未調査。

```latex
\begin{lemma}[Short mixed yields at fan-out one]
\label{lem:binary-u1-short-mixed-path}
Let $G$ be a reduced good CFG over $\{\mathtt a,\mathtt b\}$,
with $v$ nonterminals and $\theta=\bar\theta_G$.
If a nonterminal $A$ has a yield containing $\mathtt b$, it has one
of length at most $v(\theta-1)+1$.
If $L(G)$ contains a word containing $\mathtt b$, then
$\mu_\zeta(L(G))\le\theta$.
\end{lemma}
\begin{proof}
Write $d_C$ for the shortest yield length of $C$ and $o_C$ for
its shortest successful outside length. For a rule
$R:C\to\rho(C_1,\ldots,C_q)$ writing $c_R$ terminals,
linearity and nondeletion give
\[
 \theta_G(R)=o_C+c_R+\sum_jd_{C_j}.
\]
The lower bound follows by considering any occurrence of $R$;
the upper bound is attained by independently choosing a shortest
outside context and shortest child yields. In particular,
$c_R+\sum_jd_{C_j}\le\theta$ and $d_C\ge1$.
Choose a simple dependency path from $A$ to the left-hand side
of a rule writing $\mathtt b$. Complete all off-path children
by shortest yields. At the last node the local yield has length
at most $\theta$. Each preceding node contributes at most
$\theta-1$, since its designated path child has shortest length
at least one. The path has at most $v$ nodes, and the written
$\mathtt b$ survives. This proves the first bound.
For the second, a shortest successful use of any rule writing
$\mathtt b$ is a mixed sentence of length at most $\theta$.
\end{proof}

\begin{theorem}[A sharp quadratic rare-type bound on a positive weight slice]
\label{thm:binary-u1-weight-slice-quadratic}
Let $G$ be a reduced good CFG over $\{\mathtt a,\mathtt b\}$,
with $v$ nonterminals and $\theta=\bar\theta_G$.
Suppose there are real numbers $\lambda,W>0$ such that
\[
 |w|_{\mathtt a}+\lambda|w|_{\mathtt b}=W
 \qquad(w\in L(G)).
\]
Put $B(\theta)=\lfloor(\theta+1)^2/4\rfloor$.
Every nonterminal generating a pure word has a unique pure yield,
and its length is at most $B(\theta)$. Consequently,
\[
 \mu^\star(L(G),s_{U,2})\le B(\theta),\qquad
 t_{\mathrm{typ}}(G,s_{U,2})
 \le\max\{B(\theta),v(\theta-1)+1\}.
\]
Neither assertion requires substitutability, and the constants
are independent of $\lambda$ and $W$.
\end{theorem}
\begin{proof}
Let $\psi(w)=|w|_{\mathtt a}+\lambda|w|_{\mathtt b}$.
A fixed successful context for a nonterminal $A$ shows that
all its yields have one weight $w_A>0$. Thus a pure yield,
if present, is the unique word $\mathtt a^{\ell_A}$ with
$\ell_A=w_A$.
A shortest untyped $A$-yield has length at most $\theta$.
If $\lambda\le1$, its weight gives $\ell_A\le\theta$.
If $\lambda>1$ but $\ell_A<\lambda$, no $A$-yield can contain
$\mathtt b$, so again $\ell_A\le\theta$.

It remains to consider $\lambda>1$ and $\ell_A\ge\lambda$.
In a derivation of $\mathtt a^{\ell_A}$, choose a node whose
yield length $h$ is at least $\lambda$ and all of whose children
have yield lengths less than $\lambda$.
Let $R$ be its rule. Each child has fixed weight less than
$\lambda$, hence cannot generate a word containing $\mathtt b$;
its pure yield is unique. The rule writes no $\mathtt b$.
Therefore every local yield obtained by applying $R$ is the
same pure word of length $h$.
In a shortest successful use of $R$, the outside has weight
$W-h$, and hence length at least $(W-h)/\lambda$ because no
letter has weight greater than $\lambda$. It follows that
\[
 \theta\ge h+\frac{W-h}{\lambda}
 \ge \frac W\lambda+\lambda-1.
\]
Since the weight of a successful outside context for $A$ is
nonnegative, $\ell_A\le W$. Thus
\[
 \ell_A\le W\le\lambda(\theta+1-\lambda)
 \le\frac{(\theta+1)^2}{4}.
\]
Taking integer parts proves the pure-yield bound; the earlier
cases also satisfy it since $\theta\le B(\theta)$.
The mixed-yield bound follows from
Lemma~\ref{lem:binary-u1-short-mixed-path}.
At the start symbol, the sharper bound $\mu_\zeta\le\theta$
from that lemma, together with the pure bound, proves the
assertion about $\mu^\star$.
\end{proof}

\begin{corollary}[Quadratic data on a positive weight slice]
\label{cor:binary-u1-weight-slice-data}
Fix $r\ge2$. Let $L\in\Cmcf{1}{s_{U,2}}$, and let $G$ be a
reduced good rank-$\le r$ presentation of $L\cap\Sigma^+$
satisfying the hypothesis of
Theorem~\ref{thm:binary-u1-weight-slice-quadratic}.
Write $g=\|G\|$ and
$T=\max\{B(\theta),v(\theta-1)+1\}$.
The operators $\mathcal B^{\le r}_{1,s_{U,2}}$ and
$\mathcal B_{1,s_{U,2}}$ have a common characteristic sample $K$
with
\[
 \|K\|_+\le3^r g(1+2\theta+rT)+\mathbf1_{\{\eps\in L\}}
 \le3^r(r+3)g^2\theta^2+\mathbf1_{\{\eps\in L\}}.
\]
\end{corollary}
\begin{proof}
We have $\tau\le t_{\mathrm{typ}}\le T$ and
$N_{\mathrm{typ}}\le3^r g$. Substitute these bounds into
Corollary~\ref{cor:distribution-representatives}.
Since $B(\theta)\le\theta^2$, $v\le g$, and $\theta\ge1$,
one has $T\le g\theta^2$ and $1+2\theta\le3\theta^2$,
which gives the second inequality.
\end{proof}

\begin{remark}[Sharpness and scope]
For the presentations $G_{n,n}$ in
Proposition~\ref{prop:binary-u1-quadratic}, take
$\lambda=2^n$ and $W=4^n$. Then
\[
 \mu^\star=4^n=(\bar\theta_{G_{n,n}}+1)^2/4,
 \qquad \|G_{n,n}\|=12n+9.
\]
Thus the rare-type bound is attained, and no bound
$p(\|G\|)\bar\theta_G^{\,c}$ with a polynomial $p$ and fixed
$c<2$ can bound characteristic-data length even in this
subclass. The theorem does not settle the binary fan-out-one
problem for general finite or infinite targets.
\end{remark}
```

## 10. 再現用 Python ソース全文

以下を `repro.py` として保存し、`python3 repro.py` を実行する。入力ファイル・ネットワーク・外部パッケージは不要。全ての比率は有理数で計算する。

```python
#!/usr/bin/env python3
"""Exact finite checks only. Python standard library; no sampling or cutoffs."""
from collections import defaultdict
from itertools import product
from fractions import Fraction


def T(w): return ('T', w)
def N(a): return ('N', a)
def typ(w): return int('b' in w)


def distributions(words):
    D = defaultdict(set)
    for w in sorted(words):
        for i in range(len(w)):
            for j in range(i + 1, len(w) + 1):
                D[w[i:j]].add((w[:i], w[j:]))
    return D


def check(words):
    D = distributions(words)
    groups = defaultdict(list)
    for x in sorted(D):
        for e in sorted(D[x]):
            groups[(typ(x), e)].append(x)
    for (t, e), xs in sorted(groups.items()):
        x = xs[0]
        for y in xs[1:]:
            if D[x] != D[y]:
                f = sorted(D[x] ^ D[y])[0]
                return (x, y, e, f,
                        f[0]+x+f[1] in words, f[0]+y+f[1] in words)
    return None


def parameters(P, start):
    """Exact shortest yields and outside costs by monotone relaxation."""
    V = sorted({a for a, rhs in P})
    inf = float('inf')
    d = dict.fromkeys(V, inf)
    while True:
        old = d.copy()
        for a, rhs in P:
            d[a] = min(d[a], sum(len(x) if k=='T' else d[x] for k,x in rhs))
        if d == old: break
    assert all(d[a] < inf for a in V)
    o = dict.fromkeys(V, inf); o[start] = 0
    while True:
        old = o.copy()
        for a, rhs in P:
            for j,(k,b) in enumerate(rhs):
                if k == 'N':
                    side = sum(len(x) if h=='T' else d[x]
                               for i,(h,x) in enumerate(rhs) if i != j)
                    o[b] = min(o[b], o[a] + side)
        if o == old: break
    assert all(o[a] < inf for a in V)
    costs = [o[a]+sum(len(x) if k=='T' else d[x] for k,x in rhs)
             for a,rhs in P]
    g = len(V) + sum(1+sum(k=='N' for k,x in rhs)
                    +sum(len(x) if k=='T' else 1 for k,x in rhs) for a,rhs in P)
    return g, max(costs), costs, d, o


def languages(P):
    """All examples are DAGs; recursion lists the complete finite languages."""
    by = defaultdict(list)
    for a,rhs in P: by[a].append(rhs)
    cache = {}
    active = set()
    def visit(a):
        if a in cache: return cache[a]
        assert a not in active, 'this enumerator requires a DAG'
        active.add(a); out = set()
        for rhs in by[a]:
            opts = [{x} if k=='T' else visit(x) for k,x in rhs]
            out.update(''.join(z) for z in product(*opts))
        active.remove(a); cache[a] = out
        return out
    for a in by: visit(a)
    return cache


def measured(P, start):
    langs = languages(P); L = langs[start]
    g,theta,costs,d,o = parameters(P,start)
    cert = check(L)
    mu = max(min(len(w) for w in L if typ(w)==t)
             for t in (0,1) if any(typ(w)==t for w in L))
    tt = max(min(len(w) for w in Q if typ(w)==t)
             for Q in langs.values() for t in (0,1) if any(typ(w)==t for w in Q))
    tau = None
    if cert is None:
        D = distributions(L)
        tau = 0
        for Q in langs.values():
            for t in (0,1):
                xs = sorted(w for w in Q if typ(w)==t)
                if not xs: continue
                x = xs[0]
                assert all(D[z] == D[x] for z in xs)
                tau = max(tau, min(len(y) for y in D if typ(y)==t and D[y]==D[x]))
    return L,g,theta,costs,mu,tt,tau,cert


def block(m,n):
    P = [('C0',(T('a'),))]
    for j in range(1,m+1): P.append((f'C{j}',(N(f'C{j-1}'),N(f'C{j-1}'))))
    P += [('A0',(N(f'C{m}'),)),('A0',(T('b'),))]
    for i in range(1,n+1): P.append((f'A{i}',(N(f'A{i-1}'),N(f'A{i-1}'))))
    return P,f'A{n}'


def nested(k,t,M,u,Pow=2):
    # M is 2 or 4; Pow=2. b-shortcut is written explicitly here.
    rules = [('C',(T('a'*k),)), ('B0',(N('C'),)), ('B0',(T('b'*t),))]
    levels = M.bit_length()-1
    assert M == 2**levels
    for i in range(1,levels+1):
        rules.append((f'B{i}',(N(f'B{i-1}'),N(f'B{i-1}'))))
    rules += [('D',(N(f'B{levels}'),)),('D',(T('b'*u),)),('S',(N('D'),N('D')))]
    assert Pow==2
    return rules,'S'


def describe(z):
    return 'PASS' if z is None else 'FAIL certificate='+repr(z)


def main():
    print('Binary U1 exponent: exact finite checks, standard library only')
    print('Every positive factor and its full two-sided distribution is enumerated.')
    print('No randomized sampling, no language-size cutoff, no skipped cases.')
    print('BLOCK FAMILY: complete enumeration and original-grammar rule costs')
    for m,n in [(1,1),(1,2),(2,1),(2,2),(3,1),(2,3)]:
        P,S=block(m,n)
        L,g,th,costs,mu,tt,tau,c=measured(P,S)
        assert c is None
        assert (g,th,mu,tt,tau)==(6*m+6*n+9,2**m+2**n-1,2**(m+n),2**(m+n),2**(m+n))
        assert mu <= (th+1)**2//4
        print('m=%d n=%d words=%d g=%d theta=%d mu=%d ttyp=%d tau=%d mu/theta^2=%s %s'%
              (m,n,len(L),g,th,mu,tt,tau,Fraction(mu,th*th),describe(c)))
        print('  all-rule-costs='+repr(costs))
    print('COMPRESSED BALANCED FAMILY: integer DP only, NOT word enumeration')
    for j in (1,2,3,4,6,8,12):
        P,S=block(j,j); g,th,costs,d,o=parameters(P,S); mu=4**j
        assert g==12*j+9 and th==2**(j+1)-1 and mu==(th+1)**2//4
        print('j=%d g=%d theta=%d mu=%d mu/(g theta)=%s mu/theta^2=%s equality=True'%
              (j,g,th,mu,Fraction(mu,g*th),Fraction(mu,th*th)))
    print('TWO-LEVEL b-SHORTCUT GRID: k=2,3,4; t=1,2; M=2,4; u=1..8; P=2')
    total=good=0; best=Fraction(0); best_case=None
    for k,t,M,u in product((2,3,4),(1,2),(2,4),range(1,9)):
        P,S=nested(k,t,M,u)
        L,g,th,costs,mu,tt,tau,c=measured(P,S)
        total+=1
        assert (c is None)==(t==1 and u==M)
        if c is None:
            good+=1
            ratio=Fraction(mu,th*th)
            if ratio>best: best,best_case=ratio,(k,t,M,u,g,th,mu,tau)
            assert mu <= (th+1)**2//4
            assert tt <= max((th+1)**2//4,len({a for a,rhs in P})*(th-1)+1)
    print('total=%d PASS=%d FAIL=%d SKIPPED=0'%(total,good,total-good))
    print('max PASS mu/theta^2=%s case(k,t,M,u,g,theta,mu,tau)=%r'%(best,best_case))
    for args in [(2,1,2,1),(2,1,2,3),(2,1,4,2),(2,1,2,2)]:
        P,S=nested(*args); L,g,th,costs,mu,tt,tau,c=measured(P,S)
        print('nested=%r words=%d g=%d theta=%d mu=%d ratio=%s %s'%
              (args,len(L),g,th,mu,Fraction(mu,th*th),describe(c)))
        print('  all-rule-costs='+repr(costs))
    print('PADDED/MULTISTAGE GRID: k=2,3; M=2,4; every binary shortcut z of length 1..4')
    total2=good2=new2=0; failure_examples=[]
    for k,M in product((2,3),(2,4)):
        for length in range(1,5):
            for chars in product('ab',repeat=length):
                z=''.join(chars); P,S=nested(k,1,M,1)
                P[-2]=('D',(T(z),))
                L,g,th,costs,mu,tt,tau,c=measured(P,S)
                total2+=1
                base={''.join(q) for q in product(('a'*k,'b'),repeat=M)}
                if c is None:
                    good2+=1; new2+=int(z not in base)
                if (k,M,z) in [(2,2,'aba'),(2,2,'bab'),(2,4,'ab')]:
                    failure_examples.append((k,M,z,g,th,mu,costs,c))
    print('total=%d PASS=%d FAIL=%d nonredundant-PASS=%d SKIPPED=0'%
          (total2,good2,total2-good2,new2))
    for item in failure_examples: print('padded (k,M,z,g,theta,mu,all-rule-costs,certificate)=',item)
    print('FINITE STRUCTURAL CLAIMS: selected exact checks')
    for L in [{'aa','ab','bbb'}, {'aaa','aab','aba','baa','bab','bb'},
              {'baba','baaba'}, {'aaaa','aab','baa','bb','b'}]:
        c=check(L)
        print('L=%r %s'%(sorted(L),describe(c)))
    assert check({'aa','ab','bbb'}) is None
    # At lambda=1, aa and ab agree, but bbb has weight 3 rather than 2.
    assert 'baba' not in {'baaba'[i:j] for i in range(5) for j in range(i+1,6)}
    print('The asserted factor implication u a^i v | u a^j v is false: baba is not a factor of baaba.')
    print('ALL ASSERTIONS PASSED. Numerical outcomes are observations, not universal proofs.')

if __name__=='__main__': main()

```

## 11. 最終再現コードの実行ログ全文

次は§10のコードを実行して得た標準出力の全文。終了コード0、標準エラーなし。行の省略・手編集はしていない。

```text
Binary U1 exponent: exact finite checks, standard library only
Every positive factor and its full two-sided distribution is enumerated.
No randomized sampling, no language-size cutoff, no skipped cases.
BLOCK FAMILY: complete enumeration and original-grammar rule costs
m=1 n=1 words=4 g=21 theta=3 mu=4 ttyp=4 tau=4 mu/theta^2=4/9 PASS
  all-rule-costs=[3, 3, 3, 2, 2]
m=1 n=2 words=16 g=27 theta=5 mu=8 ttyp=8 tau=8 mu/theta^2=8/25 PASS
  all-rule-costs=[5, 5, 5, 4, 4, 4]
m=2 n=1 words=4 g=27 theta=5 mu=8 ttyp=8 tau=8 mu/theta^2=8/25 PASS
  all-rule-costs=[5, 5, 5, 5, 2, 2]
m=2 n=2 words=16 g=33 theta=7 mu=16 ttyp=16 tau=16 mu/theta^2=16/49 PASS
  all-rule-costs=[7, 7, 7, 7, 4, 4, 4]
m=3 n=1 words=4 g=33 theta=9 mu=16 ttyp=16 tau=16 mu/theta^2=16/81 PASS
  all-rule-costs=[9, 9, 9, 9, 9, 2, 2]
m=2 n=3 words=256 g=39 theta=11 mu=32 ttyp=32 tau=32 mu/theta^2=32/121 PASS
  all-rule-costs=[11, 11, 11, 11, 8, 8, 8, 8]
COMPRESSED BALANCED FAMILY: integer DP only, NOT word enumeration
j=1 g=21 theta=3 mu=4 mu/(g theta)=4/63 mu/theta^2=4/9 equality=True
j=2 g=33 theta=7 mu=16 mu/(g theta)=16/231 mu/theta^2=16/49 equality=True
j=3 g=45 theta=15 mu=64 mu/(g theta)=64/675 mu/theta^2=64/225 equality=True
j=4 g=57 theta=31 mu=256 mu/(g theta)=256/1767 mu/theta^2=256/961 equality=True
j=6 g=81 theta=127 mu=4096 mu/(g theta)=4096/10287 mu/theta^2=4096/16129 equality=True
j=8 g=105 theta=511 mu=65536 mu/(g theta)=65536/53655 mu/theta^2=65536/261121 equality=True
j=12 g=153 theta=8191 mu=16777216 mu/(g theta)=16777216/1253223 mu/theta^2=16777216/67092481 equality=True
TWO-LEVEL b-SHORTCUT GRID: k=2,3,4; t=1,2; M=2,4; u=1..8; P=2
total=96 PASS=6 FAIL=90 SKIPPED=0
max PASS mu/theta^2=1/3 case(k,t,M,u,g,theta,mu,tau)=(3, 1, 2, 2, 30, 6, 12, 12)
nested=(2, 1, 2, 1) words=23 g=28 theta=4 mu=8 ratio=1/2 FAIL certificate=('a', 'aaa', ('', 'aaab'), ('', 'aaaaa'), False, True)
  all-rule-costs=[4, 4, 3, 3, 3, 2, 2]
nested=(2, 1, 2, 3) words=24 g=30 theta=5 mu=8 ratio=8/25 FAIL certificate=('a', 'aaa', ('', 'abbb'), ('', 'aaaaa'), False, True)
  all-rule-costs=[5, 5, 4, 4, 4, 5, 4]
nested=(2, 1, 4, 2) words=285 g=35 theta=7 mu=16 ratio=16/49 FAIL certificate=('a', 'aaaaa', ('', 'aaaaaaabb'), ('', 'aaaaaaaaaaa'), False, True)
  all-rule-costs=[7, 7, 6, 6, 6, 6, 4, 4]
nested=(2, 1, 2, 2) words=16 g=29 theta=5 mu=8 ratio=8/25 PASS
  all-rule-costs=[5, 5, 4, 4, 4, 4, 4]
PADDED/MULTISTAGE GRID: k=2,3; M=2,4; every binary shortcut z of length 1..4
total=120 PASS=9 FAIL=111 nonredundant-PASS=0 SKIPPED=0
padded (k,M,z,g,theta,mu,all-rule-costs,certificate)= (2, 2, 'aba', 30, 5, 8, [5, 5, 4, 4, 4, 5, 4], ('aaaaab', 'aabaaa', ('', 'a'), ('a', ''), True, False))
padded (k,M,z,g,theta,mu,all-rule-costs,certificate)= (2, 2, 'bab', 30, 5, 8, [5, 5, 4, 4, 4, 5, 4], ('aaaaba', 'aabaaa', ('', 'a'), ('', 'b'), True, False))
padded (k,M,z,g,theta,mu,all-rule-costs,certificate)= (2, 4, 'ab', 35, 7, 16, [7, 7, 6, 6, 6, 6, 4, 4], ('a', 'aaaaaa', ('', 'aaaaaaaab'), ('', 'aaaaaaaaaa'), False, True))
FINITE STRUCTURAL CLAIMS: selected exact checks
L=['aa', 'ab', 'bbb'] PASS
L=['aaa', 'aab', 'aba', 'baa', 'bab', 'bb'] FAIL certificate=('ab', 'ba', ('', 'a'), ('', 'b'), False, True)
L=['baaba', 'baba'] FAIL certificate=('a', 'aa', ('b', 'ba'), ('b', 'aba'), True, False)
L=['aaaa', 'aab', 'b', 'baa', 'bb'] FAIL certificate=('aab', 'b', ('', ''), ('', 'aa'), False, True)
The asserted factor implication u a^i v | u a^j v is false: baba is not a factor of baaba.
ALL ASSERTIONS PASSED. Numerical outcomes are observations, not universal proofs.
```

## 12. 自己点検（最終）

| 点検項目 | 結果 | 根拠・限界 |
|---|---|---|
| 一穴だけを使い、二穴の移送を持ち込まなかったか | 確認済み | 全証明は CFG の連続部分木、一穴分布、正の加法重みのみ。fan-out 2 の transfer/deep は使用していない。 |
| θ̄ を元の文法で正確に計算したか | 確認済み | §2.1に全規則の正確な等式。§4.2に圧縮文法の全規則種別。試験候補も元の規則から計算し、代表例の全規則コストをログに収録。一般上界は型精錬後の厚さに置き換えていない。 |
| 下界を任意の集合駆動型作用素、上界を特定の作用素について述べたか | 確認済み | §4.3の下界はクラス全域で特徴標本を持つ任意の集合駆動型作用素。§3.4の上界は原稿の二つの再構成作用素。 |
| 代入可能性を全パラメータ・全因子・全文脈で証明したか | 該当する主張について確認済み | ブロック族は§4.1、多段の成立例は§5.1から同族へ帰着。重み一定だけで代入可能とは主張していない。失敗族の一般反証は§5.2。 |
| 有限検査を普遍命題の根拠にしていないか | 確認済み | 定理4・系5–6は解析的証明。96件・120件の集計は観測と明記。未検査パラメータへの外挿なし。 |
| 圧縮・多段化・自然な反例候補を試したか | 確認済み | 圧縮ブロックは上界の等号例。全 b 短絡の多段化は解析的に排除。bトークン長変更・a-paddingは完全検査し反証書を保存。 |
| 重み条件を全有限言語へ誤って一般化していないか | 確認済み | §6.3に代入可能だが重み一定でない明示例と全分布表。一般 (Q+) は未解決。 |
| μ*・τ・t_typ・総特徴データ長を混同していないか | 確認済み | 鋭い定数1/4は μ* と純収率について。総符号長には別途再構成系を適用。一般作用素への下界は識別論法による。 |
| 一般問題を決着したと称していないか | 確認済み | 成果は正の重み一定という条件下の (Q0)。一般 (Q+)・(Q−)、無限言語の場合は未解決。 |
| 十分な未証明命題を両方向に明記したか | 確認済み | §8.2 U₂、§8.3 N₂₊。双方で十分性だけを証明し、命題自体は未証明と表示。 |
| 再現コード・ログ・英語 LaTeX を一つのファイルに収めたか | 確認済み | §9–§11。実験用の別ファイルを受け取る必要はない。 |
| 文献上の新規性を確認したか | 未調査 | 本報告は新規性を保証しない。 |

# 結論の要約表

| 主張 | 判定 | 根拠の節 |
|---|---|---|
| 一般の問題 M：三文字・fan-out 2 の全対象で $\mu_1\le Q(g,\theta)$ | 未解決 | §8 |
| **短い規則使用と最短純導出の相互差替えに、重み誤差 $D$ の証明書があれば、$\mu_1\le\lfloor(\theta+(r+1)D+1)^2/4\rfloor$** | 証明済み | 定理2.2 |
| 全受理語の正の重み $|w|_a+|w|_b+\lambda|w|_c$ が幅 $D$ の区間に入る場合、上の二乗上界がすべての表示で成立 | 証明済み | 系3.1 |
| 特に重み一定なら、三文字・fan-out 2 でも $\mu_1\le\lfloor(\theta+1)^2/4\rfloor$ | 証明済み | 系3.2 |
| 上の $\theta$ だけの二乗評価は、arity 1・2 の両方で代入可能な明示族で等号達成 | 証明済み | 定理4.1 |
| **一文字一辺の経路制約＋型によらない共通の加法量制約**の三文字言語では、$\mu_1\le16(r+1)^4\theta^4(\theta+3)+2$ | 証明済み | 定理6.1 |
| この経路・加法量の結果は、負の係数を持つ制約、非正則言語、先行報告の内部削除閉性を持たない言語も扱う | 証明済み | §6.4 |
| 相互差替え証明書の最適誤差は、一変数の区間交差、さらに**二つの混合証人語の整数式**で正確に計算できる | 証明済み | 定理5.1 |
| その整数式を代入可能性から一様に多項式で抑える命題 C | 未解決 | §8.1 |
| $g_n\theta_n=n^{O(1)}$、$\mu_1(L_n)=n^{\omega(1)}$ を満たす適格な反例族 | 未解決 | §8.2 |
| 小さい重み切片5例の全 arity 1・2 検査、およびクラス外の実 fan-out 2 文法5例での誤差公式の照合 | 計算による観測（証明ではない） | 付録B |

**結論。** 一般の M は解けていない。ただし今回は、前回の削除閉性とは異なる二つの部分上界を得た。第一は、規則の短い成功使用を実際に利用する、誤差を許した重み保存の二乗上界である。第二は、候補に挙げられた「位相＋加法量」のうち、全体の加法量の目標値が型によらず共通である場合を、負の係数も含めて排除する五次上界である。最後に、一般 M を、前回の命題 R の代入閉包ではなく、二つの具体的な差替え証人語の個数比較に帰着した。

## 1. 資料と設定

### 1.1 参照版と先行結果の扱い

2026年10月31日に以下を公開リポジトリから取得した。以下の SHA は Git blob SHA である。

| 資料 | SHA |
|---|---|
| `02-v2-lg-fanout-boundary/main.tex` | `d9d589e69936e6d461ed1ac1cb6f51981ebe2090` |
| `astra_ternary_u1_fanout2_2026-10-30.md` | `933df5d0de85d6edcddf1f0604b95d90338bbc8b` |
| `chatgpt_ternary_u1_fanout2_2026-10-30.md` | `0c05c1348059cf6f6b8d431cb2223bcf56528f7a` |
| `astra_s2_shortcontext_2026-10-31.md` | `7f6763d32b802304ec31d6037c19db25b155d7ff` |
| `astra_binary_u1_fanout1_2026-10-30.md` | `87578f506fd5f0f32cde7525224f8de1022e5d15` |
| `astra_binary_u1_fanout1_exponent_2026-10-30.md` | `3abc0d071ce056e9b83a74ab71658161299e9525` |
| `chatgpt_binary_u1_fanout1_2026-10-30.md` | `d66f45edf797c6d7453fb9c37456a2c99220e4ed` |
| `deepseek_binary_u1_f1_search_2026-10-30.md` | `e548e67c68d415a5ca1c2cd500db665aa5c01a6f` |

原稿へのリンクは [main.tex](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/main.tex)、報告群は [revision ディレクトリ](https://github.com/growupkuriyama-hub/Papers/tree/main/02_fixed-h-mcfg/revision) にある。プロジェクトの `project-master-v15-2026-10-28.md` の資料運用も参照した。原稿は変更していない。

今回使う先行結果は、原稿 `lem:thickness-equivalence`、`prop:rare-type`、`cor:typed-sandwich`、および、クラス外の実験族の排除に使う Astra 三文字報告の定理7.2である。重み一定の場合の出発点は Astra fan-out 1 exponent 報告 §3、原稿 `prop:binary-u1-weight-slice`。今回の差分は、純語の一意性を使わず組の総長で扱うこと、近似的保存まで許すこと、全言語でなく有限の差替え証人だけを使うことにある。

Astra fan-out 1 報告 §2–3の欠陥立方体は読んだが、その単射性の証明を二成分の交錯へそのまま移してはいない。ChatGPT fan-out 1報告 §3–4の欠陥計数、DeepSeek 報告 §4のブロック族、および Astra exponent 報告 §4の圧縮版も、arity 2 のクラス所属を保証するものとして使わない。原稿 §8が示すとおり、その点は独立の条件である。

### 1.2 設定

基本設定は依頼どおりとする。

\[
\Sigma=\{a,b,c\},\quad s(a)=s(b)=1,\quad s(c)=\zeta,
\quad g=\|G\|,\ v=|V|,\ \theta=\bar\theta_G\ge1.
\]

$L^+=L\cap\Sigma^+$ は純語を含み、$G$ はその reduced good 表示、fan-out $\le2$、rank $\le r$、$r\ge2$ とする。$N=\mu_1(L)$ と書く。純語 $w\in L^+$、$|w|=N$ と、その節点数最小の導出木 $T$ を固定する。

語または組の成分全体に対し

\[
A(x):=|x|_a+|x|_b,\qquad C(x):=|x|_c,
\qquad \psi_\lambda(x):=A(x)+\lambda C(x)\quad(\lambda>0)
\tag{1.1}
\]

とする。組の量は全成分について加える。$T$ の節点 $u$ の組を $\mathbf w_u$、その総長を $\ell_u$ とする。非削除性により、すべての $\mathbf w_u$ は全成分が純であり、$1\le\ell_u\le N$ である。

原稿 `lem:thickness-equivalence` から、各非終端の短い生成組の総長、および各規則の直接の端末数は $\theta$ 以下である。本報告で用いる $\theta$ は、型付き文法の厚さではなく、常に元の $G$ の規則厚さである。

## 2. 短い規則使用を使う有限の重み証明書

### 2.1 差替え証人の正確な定義

$T$ で使われる各規則

\[
R:B\longrightarrow\rho(B_1,\ldots,B_q),\qquad q\le r
\]

について、$R$ を使う長さ $\theta_G(R)\le\theta$ の成功導出を一つ選び、その語を $Z_R$ とする。その中で $R$ の出現を一つ指定する。指定出現における子組を $\boldsymbol\eta_{R,1},\ldots,\boldsymbol\eta_{R,q}$、その親の組を $\boldsymbol\eta_R$、外側の導出文脈を $D_R$ と書く。

\[
Z_R=D_R[\boldsymbol\eta_R],\qquad
\boldsymbol\eta_R=\rho(\boldsymbol\eta_{R,1},\ldots,\boldsymbol\eta_{R,q}).
\tag{2.1}
\]

同じ規則の $T$ 内の複数出現には、同じ選択した証人を使ってよい。

$T$ の節点 $u$ が規則 $R$ を使い、その第 $j$ 子が $u_j$ であるとき、次の受理語を作る。

- **子を短い証人へ差し替える語** $V_{u,j}$：$T$ の $u_j$ 部分木を、$\boldsymbol\eta_{R,j}$ の導出に置き換える。
- **短い成功使用へ元の部分木を戻す語** $U_u$：$Z_R$ の指定した親部分木を、$T$ の $u$ 部分木に置き換える。

どちらも同じ非終端の導出を置き換えるので $G$ の成功導出である。これは文法的な差替えであり、異なる型の組に代入可能性を適用しているのではない。

有限集合

\[
\mathcal W(T,Z):=\{w\}\cup\{Z_R:R\text{ は }T\text{ で使用}\}
\cup\{U_u:u\in T\}\cup\{V_{u,j}:u_j\text{ は }u\text{ の子}\}
\tag{2.2}
\]

を定める。$T$ 自体のサイズは多項式とは限らないので、この集合の構成が多項式時間でできるとは主張しない。

### 補題2.1（差替え語の数値範囲）

$z\in\mathcal W(T,Z)$ について

\[
z\in L^+,\qquad 1\le |z|\le N+\theta,
\qquad 0\le C(z)\le\theta.
\tag{2.3}
\]

さらに

\[
\begin{aligned}
\psi_\lambda(V_{u,j})&=N-\ell_{u_j}+\psi_\lambda(\boldsymbol\eta_{R,j}),\\
\psi_\lambda(U_u)&=\psi_\lambda(D_R)+\ell_u.
\end{aligned}
\tag{2.4}
\]

**証明。** $V_{u,j}$ では、元の純語から長さ $\ell_{u_j}$ の組の寄与を除き、長さ $\|\boldsymbol\eta_{R,j}\|_1\le|Z_R|\le\theta$ の組を入れる。各端末は線形・非削除性によりちょうど一度残るため、長さと重みは寄与の差で計算できる。元の語に $c$ はなく、新しい $c$ はこの短い組にしか現れない。

$U_u$ では、短い語 $Z_R$ の内部組を除き、総長 $\ell_u\le N$ の純な組を入れる。外側の長さ・$c$ の数はともに $\theta$ 以下である。これで長さの上界、$c$ 個数の上界と (2.4) を得る。$Z_R$ 自体と $w$ についても (2.3) は成立する。すべて正当な成功導出であり、$G$ は $\lambda$-free なので出力は正長である。$\square$

### 定理2.2（有限差替え証明書からの二乗上界）

ある $\lambda>0,D\ge0$ について

\[
\left|\psi_\lambda(z)-N\right|\le D
\qquad(z\in\mathcal W(T,Z))
\tag{2.5}
\]

が成り立つなら

\[
\boxed{N\le
\left\lfloor\frac{(\theta+(r+1)D+1)^2}{4}\right\rfloor.}
\tag{2.6}
\]

この主張は代入可能性を使わない。ファンアウト2に固有の仮定も使わず、組の総長と線形・非削除性で成立する。

**証明。** $B=(\theta+(r+1)D+1)^2/4$ と置く。まず小さい $\lambda$ を処理する。

$0<\lambda\le1$ なら、任意の選択した $Z_R$ に対し $\psi_\lambda(Z_R)\le|Z_R|\le\theta$ なので、(2.5)より $N\le\theta+D$。$r+1\ge2$ と $\theta\ge1$ により

\[
B-(\theta+D)\ge
\frac{(\theta+2D+1)^2}{4}-(\theta+D)
=\frac{(\theta-1)^2}{4}+\theta D+D^2\ge0.
\]

$1<\lambda\le D$ なら、$\psi_\lambda(Z_R)\le\lambda\theta\le D\theta$ だから $N\le D(\theta+1)$。このとき

\[
B-D(\theta+1)\ge
\frac{(\theta+1+2D)^2}{4}-D(\theta+1)
=\frac{(\theta+1)^2}{4}+D^2\ge0.
\]

以下 $\lambda>\max\{1,D\}$ とし、$t=\lambda-D>0$ と置く。

もし $N<t$ なら、$T$ の根が使う規則 $R$ の各子 $u_j$ について $\ell_{u_j}<t$ である。(2.4)と(2.5)から

\[
\psi_\lambda(\boldsymbol\eta_{R,j})\le\ell_{u_j}+D<\lambda.
\tag{2.7}
\]

$c$ を一つでも含む組の重みは $\lambda$ 以上なので、これらの子組はすべて純である。$R$ のテンプレートも純導出に現れるため $c$ を直接書かない。よって $\boldsymbol\eta_R$ は純であり、開始記号の生成語として長さ $\le|Z_R|\le\theta$ である。したがって $N\le\theta\le B$。

残りは $N\ge t$。$T$ の中で $\ell_u\ge t$ を満たし、どの子もこの条件を満たさない節点を一つ選ぶ。$h=\ell_u$、その規則を $R$、子の数を $q$ とする。各子は $\ell_{u_j}<t$ なので (2.7) が成立し、証人の子組はすべて純である。また (2.4)と(2.5)の下側から

\[
\|\boldsymbol\eta_{R,j}\|_1
=\psi_\lambda(\boldsymbol\eta_{R,j})
\ge\ell_{u_j}-D.
\]

テンプレートが直接書く純文字数を $e_R$ とすると

\[
h=e_R+\sum_{j=1}^q\ell_{u_j},\qquad
\|\boldsymbol\eta_R\|_1
=e_R+\sum_{j=1}^q\|\boldsymbol\eta_{R,j}\|_1
\ge h-qD\ge h-rD.
\tag{2.8}
\]

逆向き差替え $U_u$ に (2.5) を用いると

\[
\psi_\lambda(D_R)+h\ge N-D.
\tag{2.9}
\]

一文字の重みは高々 $\lambda$ なので、外側の長さは $\psi_\lambda(D_R)/\lambda$ 以上である。$N-D-h$ が負でも次の下界は有効である。

\[
\begin{aligned}
\theta\ge |Z_R|
&=\|\boldsymbol\eta_R\|_1+|D_R|_{\rm fix}\\
&\ge h-rD+\frac{N-D-h}{\lambda}.
\end{aligned}
\tag{2.10}
\]

$h\ge\lambda-D$ と $\lambda>1$ より、整理して

\[
\begin{aligned}
N&\le\lambda(\theta+rD)+D-(\lambda-1)h\\
&\le\lambda(\theta+rD)+D-(\lambda-1)(\lambda-D)\\
&=-\lambda^2+\lambda(\theta+(r+1)D+1)\\
&\le\frac{(\theta+(r+1)D+1)^2}{4}=B.
\end{aligned}
\]

すべての場合で $N\le B$ であり、$N$ は整数なので床を取れる。$\square$

**今回の核心。** 短い受理語があるというだけではなく、ある規則の**子組が純でなければならない閾値**を作り、その規則の短い成功使用における「内側」と「外側」の費用を同時に数えた。二成分が交錯しても各端末の寄与は一度ずつであるため、長さと加法重みの式は崩れない。

## 3. 重み一定から、幅のある重み区間へ

### 系3.1（正の重みが有界幅に入る部分クラス）

ある $\lambda>0$ と実数 $W_-,W_+$ が存在し、$D=W_+-W_-\ge0$、

\[
W_-\le A(z)+\lambda C(z)\le W_+
\qquad(z\in L^+)
\tag{3.1}
\]

とする。このときすべての指定の表示 $G$ について (2.6) が成立する。

**証明。** $w$ の重みは $N$ であり、$w$ と差替え語のすべてが $L^+$ に属する。その二語の重みの差の絶対値は、共通の区間の幅 $D$ 以下である。従って (2.5) が成立し、定理2.2を適用できる。$\square$

$D$ を固定した言語部分クラスでは、これはすべての表示に一様な二乗上界である。$D$ 自身が $g,\theta$ の固定多項式以下と分かる場合も M の多項式上界を与える。しかし任意の有限言語について、そのような小さい幅を確保したわけではない。

### 系3.2（三文字・fan-out 2 の重み一定）

全 $z\in L^+$ について

\[
|z|_a+|z|_b+\lambda|z|_c=W\qquad(\lambda>0)
\tag{3.2}
\]

なら

\[
\boxed{\mu_1(L)\le\left\lfloor\frac{(\theta+1)^2}{4}\right\rfloor.}
\tag{3.3}
\]

**証明。** 系3.1で $D=0$ とする。純語の重みはその長さなので $N=W$ である。純語が何種類あるか、また各成分の文字順序が何かは証明に使わない。$\square$

これは原稿 `prop:binary-u1-weight-slice` の純型上界を今回の設定へ拡張する。二文字の証明で使えた「純語は一つ」という結論を三文字に持ち込んだわけではない。また (3.3) は $\mu_1$ の上界であり、この節だけで全型付き非終端の $\tau$ を抑えたとは主張しない。

## 4. arity 2 のクラス内でも二乗評価は数値的に鋭い

### 定理4.1（全重み切片と全規則の厚さ）

整数 $k,m\ge1$、$W=km$ に対し

\[
L_{k,m}:=\{z\in\{a,b,c\}^+: |z|_a+|z|_b+k|z|_c=W\}.
\tag{4.1}
\]

この言語は全 arity で組代入可能であり、特に $\mathcal C^{\mathrm{mcf}}_{2,s}$ に属する。次の明示的な rank $\le1$ の good CFG $G_{k,m}$ について

\[
\mu_1(L_{k,m})=km,\quad
\theta_{G_{k,m}}=k+m-1,\quad
\|G_{k,m}\|=13km-4k-2.
\tag{4.2}
\]

したがって $k=m$ なら (3.3) の等号を達成する。

**文法。** 非終端は $A_1,\ldots,A_W$、開始記号は $A_W$。$A_0$ は導入しない。

\[
\begin{array}{ll}
A_1\to a\mid b,&\\
A_j\to aA_{j-1}\mid bA_{j-1}&(2\le j\le W),\\
A_k\to c,&\\
A_j\to cA_{j-k}&(k<j\le W).
\end{array}
\tag{4.3}
\]

$k=1$ では $A_1\to c$ も定数規則として加わる。

**言語と代入可能性の証明。** $A_j$ が生成する語は正の重み $j$ の語全体である。規則の最初の文字の重みを引いた残りへ進む帰納法で、包含の両方向が従う。各規則は重みを保存し、逆に重み $j$ の正長語の先頭が $a,b$ なら残りの重みは $j-1$、$c$ なら $j-k$ である。残りが空の場合だけ対応する定数規則を使う。

同型の非空二組 $\mathbf x,\mathbf y$ が許容文脈 $E$ を共有すると、重みの加法性と全体重み $W$ から

\[
\sum_i\psi_k(x_i)=W-\psi_k(E)=\sum_i\psi_k(y_i).
\]

任意の別の許容文脈 $F$ でも全体重みは一致し、成分が非空なので全体語は正長である。従って $F[\mathbf x]\in L_{k,m}\iff F[\mathbf y]\in L_{k,m}$。この議論は任意の arity に対して成立し、特に arity 1・2を含む。内側区切りを空にする操作はしていない。

**reduced・good 性とサイズ。** すべての規則は線形、非削除、非置換、非併合、$\lambda$-free である。任意の $A_j$ へ、重み $W-j$ の純な接頭辞を出力して到達でき、その後にどの規則を使っても純な接尾辞で完了できる。従ってすべての規則は成功使用を持つ。非終端数は $W$。$a,b$ の定数規則のサイズ合計は4、その他の $a,b$ 規則は各サイズ4で $2(W-1)$ 個、$c$ 定数規則はサイズ2、残る $c$ 規則は各サイズ4で $W-k$ 個。合計は

\[
W+4+8(W-1)+2+4(W-k)=13W-4k-2.
\]

**全規則の厚さの証明。** 重み $t\ge0$ を表す語の最短長を

\[
d(t):=\lfloor t/k\rfloor+(t\bmod k),\qquad d(0)=0
\tag{4.4}
\]

とする。$c$ を最大限使うとこの長さを達成する。$c$ を一つ減らすごとに重み1の文字が $k$ 個必要になるので、これより短くできない。

$A_j$ に至る外側は、この右線形文法では重み $W-j$ の接頭辞であり、最短長は $d(W-j)$。先頭文字の重みが $q\in\{1,k\}$ の規則の最短成功使用は正確に

\[
\theta_G(R)=d(W-j)+1+d(j-q).
\tag{4.5}
\]

外側と残りの接尾辞を独立に最短に選べるので上界を達成し、各々の最短性から下界も得る。$j=q$ なら最後の項は0であり、定数規則も含む。

$a,b$ 規則では $q=1$。$j$ の $k$ による剰余を調べると、$W-j$ と $j-1$ の剰余の和は常に $k-1$ なので、(4.5) はすべて $m+k-1$。$c$ 規則では $q=k$ で、$k\mid j$ の場合は $m$、$k\nmid j$ の場合は $m+k-1$ になる。これで全規則を評価し、最大は $m+k-1$ と分かる。

最後に純語の長さは必ず $W=km$ で、そのような語は存在するので $\mu_1=km$。$k=m$ なら $km=(\theta+1)^2/4$ である。$\square$

**鋭さの範囲。** これは $\theta$ だけによる上界の等号例である。本表示のサイズは $\Theta(km)$ なので、$\theta^c\operatorname{poly}(g)$、$c<2$ をすべて排除したことにはならない。原稿の fan-out 1 の対数サイズ・ブロック族による強い指数最適性を、そのまま arity 2 へ移したとは主張しない。

## 5. 最適な重み誤差は二つの証人語で測れる

### 定理5.1（一変数近似の厳密公式）

$\mathcal W=\mathcal W(T,Z)$ を固定し、$a_i=A(z_i)$、$c_i=C(z_i)$ とする。

\[
\Delta(T,Z):=\inf_{\lambda>0}\max_{z_i\in\mathcal W}|a_i+\lambda c_i-N|.
\tag{5.1}
\]

混合証人語の組に対して

\[
J(T,Z):=
\max_{c_i,c_j>0}
\frac{|c_j(N-a_i)-c_i(N-a_j)|}{c_i+c_j}
\tag{5.2}
\]

と置く。最大を取る集合が空なら0とする。このとき

\[
\Delta(T,Z)=\max\left\{
0,\ \max_{c_i=0}|a_i-N|,\ \max_{c_i>0}(a_i-N),\ J(T,Z)
\right\}.
\tag{5.3}
\]

特に

\[
J(T,Z)\le\Delta(T,Z)\le\max\{\theta,J(T,Z)\},
\tag{5.4}
\]

および

\[
\boxed{
N\le\left\lfloor
\frac{(\theta+(r+1)\max\{\theta,J(T,Z)\}+1)^2}{4}
\right\rfloor.
}
\tag{5.5}
\]

**証明。** まず $\lambda\ge0$ を許して、誤差 $D$ 以下の解がある条件を調べる。$c_i=0$ については $|a_i-N|\le D$ が必要十分である。$c_i>0$ については

\[
\frac{N-a_i-D}{c_i}\le\lambda\le\frac{N-a_i+D}{c_i}.
\tag{5.6}
\]

これらの閉区間と $[0,\infty)$ に共通部分があるための必要十分条件は、各上端が0以上で、すべての下端がすべての上端以下となることである。前者は $D\ge a_i-N$。後者を二つの添字 $i,j$ について両方向に書くと

\[
|c_j(N-a_i)-c_i(N-a_j)|\le(c_i+c_j)D.
\]

これで $\lambda\ge0$ に対する最小誤差は (5.3) になる。混合証人がない場合、条件は $\lambda$ に依存せず、同じ式が成立する。

最適な共通部分が $\{0\}$ だけの場合も、$\lambda\downarrow0$ とすると有限個の連続関数の最大値がその最小値へ収束する。従って $\lambda>0$ に対する下限も同じである。正の最適値が必ず達成されると仮定してはいない。

純な証人語は受理されるので、その長さ $a_i$ は $N$ 以上である。補題2.1から $a_i\le N+\theta$ なので、$|a_i-N|\le\theta$。混合証人についても $a_i-N\le|z_i|-N\le\theta$。(5.3)から (5.4) が従う。

任意の $\epsilon>0$ に対し、(2.5)を $D=\Delta(T,Z)+\epsilon$ で満たす正の $\lambda$ がある。定理2.2の実数上界を適用して $\epsilon\downarrow0$ とすれば

\[
N\le(\theta+(r+1)\Delta(T,Z)+1)^2/4.
\]

さらに (5.4) を使い、最後に整数性で床を取ると (5.5) になる。$\square$

### 系5.2（大きい純語には、不整合な二つの短絡証人が必要）

\[
N>\frac{((r+2)\theta+1)^2}{4}
\tag{5.7}
\]

なら、任意の上記の $T,Z$ の選択に対し、二つの混合証人語 $z_i,z_j\in\mathcal W(T,Z)$ があって

\[
\frac{|c_j(N-a_i)-c_i(N-a_j)|}{c_i+c_j}
\ge\frac{2\sqrt N-\theta-1}{r+1}>\theta.
\tag{5.8}
\]

しかも各語は長さ $N+\theta$ 以下、各 $c$ 個数は $1$ 以上 $\theta$ 以下である。

**証明。** 定理2.2を下限に適用した式から

\[
\Delta(T,Z)\ge\frac{2\sqrt N-\theta-1}{r+1}.
\]

(5.7)なら右辺は $\theta$ より大きい。(5.3)のうち、$J$ 以外の項は $\theta$ 以下なので、$J=\Delta$ でなければならない。有限集合上の最大値を実現する二語を選ぶ。残りは補題2.1による。$\square$

この二語は単に任意の受理語ではなく、**最短純導出と、各規則の長さ $\theta$ 以下の成功使用を、一箇所で差し替えて得られる語**である。両者の $c$ 個数が等しければ、左辺は $|a_i-a_j|/2$ になる。異なる場合には、失った純文字数を $c$ の個数で割った値の不整合を測っている。

## 6. 位相＋共通加法量の候補は反例にならない

### 6.1 対象となる言語の定義

有限有向グラフで、各文字 $a,b,c$ はそれぞれ**一つの指定された辺**を表すとする。異なる文字が同じ始点・終点を持ってよく、ループもよい。開始・終了頂点を $p,q$ とし、$R_{p,q}$ を $p$ から $q$ への経路ラベル集合とする。

任意の整数行列による加法写像

\[
\phi:\mathbb Z^3\to\mathbb Z^d
\]

と $h\in\mathbb Z^d$ を選び、

\[
L^+=\{w\in R_{p,q}\cap\Sigma^+:\phi(\Psi(w))=h\}
\tag{6.1}
\]

とする。係数は負でも零でもよく、言語ごとに変わってよい。重要なのは、右辺の $h$ が**純語・混合語で共通**なことである。すべてのこの種の言語が fan-out 2 の MCFL であるとは仮定しない。以下は、実際に指定の表示 $G$ を持ち、純語を含むものについての定理である。

### 定理6.1（共通加法量を持つ経路言語の上界）

(6.1) が指定の表示 $G$ を持ち、純語を含むなら

\[
\boxed{\mu_1(L)\le16(r+1)^4\theta^4(\theta+3)+2.}
\tag{6.2}
\]

さらに (6.1) は全 arity で組代入可能である。従って fan-out $\le2$ の表示があれば、arity 1・2の条件は自動的に満たされる。

証明には、次の二つの初等補題を使う。

### 補題6.2（短い組から作る小さい Parikh 差分）

各非終端 $B$ に $\|\boldsymbol\omega_B\|_1\le\theta$ の生成組を固定する。$b:=\Psi(\boldsymbol\omega_S)$ とし、各規則 $R:A\to\rho(B_1,\ldots,B_t)$ に

\[
\delta_R:=\Psi\bigl(\rho(\boldsymbol\omega_{B_1},\ldots,
\boldsymbol\omega_{B_t})\bigr)-\Psi(\boldsymbol\omega_A)
\tag{6.3}
\]

を対応させる。$M=(r+1)\theta$ と置くと

\[
\|b\|_1\le\theta,\quad b\ge0,\quad
\|\delta_R\|_\infty\le M.
\tag{6.4}
\]

任意の成功導出木 $T'$ の語 $w'$ は

\[
\Psi(w')=b+\sum_{u\in T'}\delta_{R(u)}.
\tag{6.5}
\]

(6.1)の下では $\phi(b)=h$、$\phi(\delta_R)=0$ である。

**証明。** 規則の直接の端末数は $\theta$ 以下、子は高々 $r$ 個で各短組の総長は $\theta$ 以下なので、(6.3)の第一項の総長は $M$ 以下。第二項の総長は $\theta$ 以下で、どちらも非負ベクトルなので、各座標の差の絶対値は $M$ 以下である。

節点の実際の組の Parikh ベクトルから、その非終端の固定した短組のベクトルを引くと、当該規則の $\delta_R$ と、各子の同じ差の和になる。これは各変数が一度ずつ使われることによる。葉から帰納して、根に至ると (6.5) を得る。

$\boldsymbol\omega_S$ は受理語なので $\phi(b)=h$。ある $A$ の導出文脈を一つ固定する。そこへ $\boldsymbol\omega_A$ と、(6.3)の規則で作った組を入れると、ともに受理語であり $\phi$ 値は $h$。固定外側の $\phi$ 値を引くと、この二組の値が等しいので $\phi(\delta_R)=0$ となる。$\square$

### 補題6.3（二変数の小さい非負整数解）

整数係数の有限連立一次方程式

\[
A\binom{x}{y}=d,
\quad |A_{ij}|\le B,\quad |d_i|\le H,
\quad B,H\ge1
\tag{6.6}
\]

が非負整数解を持つなら、$x+y\le4BH$ の非負整数解を持つ。

**証明。** 係数行列の階数で分ける。階数0では、整合性から全右辺も0なので $(0,0)$ を選ぶ。

階数2では独立な二行を取る。その行列式は零でない整数なので絶対値は1以上。Cramer の公式の各分子の絶対値は $2BH$ 以下なので、唯一の解は $x,y\le2BH$ である。仮定によりその解は非負整数であり、残りの方程式も満たす。

階数1では、非零の一行 $ux+vy=t$ を取る。全体系は整合的であるから、この一行を満たす解は他の行も満たす。片方の係数が0なら、他方の変数は非負整数として固定されて $\le|t|\le H$ であり、自由な変数を0にする。

両係数が同符号なら、必要に応じて式に $-1$ を掛けて両者を正とできる。そのとき任意の非負整数解は $x+y\le t\le H$。

両係数が異符号なら、変数交換と符号変更で $ux-vy=t$、$u,v>0$ とする。$d_0=\gcd(u,v)$。非負整数解のうち $x+y$ が最小のものを選ぶ。もし $x\ge v/d_0$ かつ $y\ge u/d_0$ なら、$(v/d_0,u/d_0)$ を引いても非負の解であり、和が減って矛盾する。したがって片方がその閾値未満である。

$x<v/d_0\le v$ の場合、$vy=ux-t\le uv+|t|$ から $y\le u+|t|$、従って $x+y\le u+v+|t|\le2B+H$。$y<u/d_0\le u$ の場合は $ux=vy+t\le uv+|t|$ から $x\le v+|t|$ となり、やはり和は $2B+H$ 以下。この二場合が残りを尽くす。$2B+H\le4BH$、$H\le4BH$ より結論を得る。$\square$

### 6.2 定理6.1の長さ上界の証明

$U=\operatorname{span}_{\mathbb R}\{\delta_R\}$ とする。補題6.2より、すべての受理語の Parikh ベクトルはアフィン空間 $b+U$ に入り、そこに属する任意の整数ベクトル $x$ は $\phi(x)=h$ を満たす。

$b+U$ を、小さい整数係数の一次方程式で記述する。以下 $B=2M^2$ と置く。

- $\dim U=0$ なら $x_i=b_i$、$i=1,2,3$ とする。
- $\dim U=1$ なら、零でない一つの生成ベクトル $\delta$ と $\delta_k\ne0$ を選び、$j\ne k$ に対して
  \[
  \delta_k(x_j-b_j)-\delta_j(x_k-b_k)=0
  \]
  とする。この二式は $x-b$ が $\delta$ の実数倍であることと同値である。
- $\dim U=2$ なら、独立な二つの生成ベクトル $\delta,\delta'$ を取り、$n=\delta\times\delta'$ として $n\cdot x=n\cdot b$ とする。$n\ne0$ で、この平面はちょうど $b+U$ である。
- $\dim U=3$ なら方程式は不要である。

どの場合も係数の絶対値は $B$ 以下、右辺の絶対値は $B\theta$ 以下。階数2の場合、外積の各成分は絶対値 $M^2$ 以下の二項の差なので $2M^2=B$ 以下であり、右辺は $\|b\|_1\le\theta$ により評価できる。他の場合はこれより小さい。

純受理語を一つ取り、その使う辺の集合を $J\subseteq\{a,b\}$ とする。$J\ne\varnothing$。この純語の Parikh ベクトルは上のアフィン方程式を満たす。

$c$ の座標を0とし、$a,b$ の二座標に加えて次を課す。

1. 各頂点における「出辺数−入辺数」は、開始頂点 $p$ で $+1$、終了頂点 $q$ で $-1$、他で0。$p=q$ ならすべて0。
2. $J$ に属さない辺の個数は0、$J$ の各辺の個数は1以上。

辺の流量方程式の係数は $-1,0,1$、右辺も $-1,0,1$ である。$e_i=1_{\{i\in J\}}$ として $x_i=e_i+z_i$、$z_i\ge0$ と置き、$i\notin J$ には $z_i=0$ を加える。得られた二変数 $z_a,z_b$ の整数連立方程式は、係数の絶対値 $B$ 以下、右辺の絶対値

\[
H:=B(\theta+3)
\]

以下である。元の純語の個数から $e$ を引けば非負整数解がある。

補題6.3により、$z_a+z_b\le4BH$ の解を選べる。元に戻した辺の個数は同じ非空支持 $J$ を持ち、

\[
x_a+x_b\le4B^2(\theta+3)+2
=16(r+1)^4\theta^4(\theta+3)+2.
\tag{6.7}
\]

この辺多重集合を $p$ から $q$ への経路として並べられることを確認する。元の純語が $J$ を経路として使うので、$J$ の無向の支持は連結で、必要な開始・終了頂点を含む。新しい個数は同じ支持を持ち、上の流量条件を満たす。$p\ne q$ なら一時的に $q$ から $p$ への辺を一本加えると、全頂点で入次数と出次数が一致する。$p=q$ なら追加は不要である。

この平衡した連結な有向多重グラフでは、未使用の出辺を辿り続けると、開始頂点以外では入出次数の均衡のため途中で止まらず、閉路を作れる。辺が残った場合、支持の連結性から、これまでの閉路に接する未使用辺を持つ頂点がある。未使用部分も平衡しているので、そこでさらに閉路を作り、元の閉路へ挿入する。有限回で全辺を使う閉路を得る。追加辺があった場合はその位置で切って除くと $p$ から $q$ への経路になる。

そのラベルを $u$ とする。純な正長語であり、$\Psi(u)\in b+U$ なので $\phi(\Psi(u))=h$。従って (6.1)により $u\in L^+$。長さは (6.7) 以下なので、$\mu_1(L)$ もその上界を満たす。これで長さ評価を証明した。$\square$

### 6.3 定理6.1の全 arity の代入可能性の証明

同型の非空組 $\mathbf x,\mathbf y$ が許容文脈 $E$ を共有するとする。各非空内部区切りの最初と最後の文字は、それぞれ一つの指定辺なので、穴の両端の頂点を決める。外側区切りが空なら、その側の頂点は $p$ または $q$ が決める。従って各 $x_i,y_i$ は、同じ二頂点を結ぶ経路である。

二つの受理語に対して共通の加法量 $h$ から固定部分を引けば

\[
\sum_i\phi(\Psi(x_i))=\sum_i\phi(\Psi(y_i)).
\]

任意の別の許容文脈 $F$ で、一方が経路として接続できれば、各穴の両端が等しいので他方も接続できる。逆方向は $\mathbf x,\mathbf y$ を交換した同じ両端一致から従う。さらに全体の加法量も一致するので、どちらが (6.1)に属するかも一致する。成分が非空なので全体語は正長である。以上は arity 1・2を含むすべての arity についての、全組・全文脈の証明である。$\square$

### 6.4 この部分クラスが覆うもの、覆わないもの

非正則かつ前回の内部削除閉性を満たさない例は

\[
L_{\pm}:=\{w\in\Sigma^+: |w|_a+|w|_c=|w|_b\}.
\tag{6.8}
\]

一頂点に三つのループを置き、$\phi=(1,-1,1)$、$h=0$ とすれば (6.1)である。good CFG は

\[
S\to xb\mid bx\mid xSb\mid bSx\mid SS
\qquad(x\in\{a,c\})
\tag{6.9}
\]

で与えられる。全規則が個数差0を保つ。逆に差0の正長語について、接頭辞の差が最初に0へ戻る位置を取ると、最初と最後の文字は異符号で、内部と残りの接尾辞の差は0である。内部が空なら $xb,bx$、非空なら帰納法と $xSb,bSx$ を使い、非空の残りは $SS$ で連接する。これで全語を生成する。すべての規則は成功使用を持ち、rank は高々2である。

$a^*b^*$ との共通部分は $\{a^n b^n:n\ge1\}$ なので非正則である。後者が正則なら、pumping length $t$ に対する $a^tb^t$ の最初の $t$ 文字内の非空部分を削除すると $a$ の個数だけが減り、矛盾する。$acbb$ は (6.8) に属すが、純文字 $a,b$ に挟まれた $c$ を消した $abb$ は属さない。従って前回の IE は成立しない。$(cb)^m$ は無界な $c$-run 数を与え、$(ab)^Dcb(ab)^D$ は任意に長い純な両側を持つ混合因子を与える。

一方、Astra 三文字報告 §5の一般的な位相族は、型ごとに別の目標 $h_1,h_\zeta$ を許していた。定理6.1は、その一般形を全部排除するものではない。$P_{N,m}$ も通常は型ごとに異なる Parikh 値を用いるので、この共通目標の仮定に入らない。また単に (6.1) の**部分集合**であるだけでは不十分である。最後に作った小さい整数解から語を受理するため、(6.1)との等号が必要になる。

## 7. 試した否定方向と、計算の役割

### 7.1 実 fan-out 2 の小厚さ・長純語は、それだけでは不足

次の文法を検査用に用いた。

\[
A_0\to(a,b),\qquad
A_i\to(x_1y_1,x_2y_2)(A_{i-1},A_{i-1})\mid(c,c),
\quad1\le i\le n,
\]
\[
S\to x_1ax_2(A_n).
\tag{7.1}
\]

これは reduced good、fan-out 2、rank 2であり、

\[
g=11n+10,\quad\theta=2n+3,\quad
N=2^{n+1}+1.
\tag{7.2}
\]

**数値式の証明。** 純組は $A_i$ で $(a^{2^i},b^{2^i})$ のみなので、純受理語は $a^{2^n+1}b^{2^n}$ のみ。各 $A_i$ の無型最短総長は2であり、$A_i$ の外側の最短長は $1+2(n-i)$。$A_0$ の定数規則の最短成功使用は $2n+3$、$A_i$ の二子規則は $2(n-i)+5$、短絡規則は $2(n-i)+3$、開始規則は5である。すべて独立に短い兄弟を選んで達成でき、その部分の非空最短長2から下界も得られる。最大は $2n+3$。

非終端は $n+2$ 個、$A_0$ の規則サイズ3、各段の二子規則サイズ7と短絡サイズ3、開始規則サイズ5なので、$g=n+2+3+10n+5=11n+10$。規則の各変数は一度ずつ順序を保って現れ、同じ子の二成分を区切りなく接続する規則はない。開始規則の二成分の間には文字 $a$ がある。従って good であり、全規則は成功使用を持つ。$\square$

しかし $n\ge2$ では、唯一の純語は長さ7以上で、内部が一定でも完全交互でもない。Astra 三文字報告の定理7.2と純部分への遺伝（同補題7.1）により、arity 2 の代入可能性を満たさない。**(7.1)は M の反例ではない。** 今回の計算では、代入可能性を必要としない定理2.2・5.1が、こうした小厚さ・長純語にも整合するかだけを確かめた。

### 7.2 欠陥立方体からの推論を保留した理由

fan-out 1 の指数欠陥立方体では、最初に選択の異なる連続区間の中で最初の混合文字を比較し、出力の相異性を示せた（Astra binary fan-out 1報告 §2.1）。fan-out 2では、一つの所有者が二つの離れた区間に寄与し、一方の区間の長さ変更が、他の所有者の混合文字の位置へ影響する。元の単射性証明のその箇所は、そのままでは使えない。

本報告は「二成分版の指数単射性は偽」とまでは主張しない。未証明の一般化を使わず、有限の規則使用・差替えと、加法量の一次方程式へ方針を移した。F8 の前向き移送と汲み上げだけで最短純語を縮めたとも主張しない。

## 8. 一般 M に残る正確な中間命題と否定の設計仕様

### 8.1 中間命題 C：二つの差替え証人の個数整合性

> **命題 C（未証明）。** 固定 $r$ と今回の型付けに対し、ある定数 $C>0$、整数 $k\ge0$ があり、すべての対象 $L,G$ について、最短純語の導出 $T$ と各規則の最短成功使用 $Z_R$ を選んで、すべての混合証人対 $z,z'\in\mathcal W(T,Z)$ に対し
> \[
> \left|C(z')\bigl(N-A(z)\bigr)-C(z)\bigl(N-A(z')\bigr)\right|
> \le\bigl(C(z)+C(z')\bigr)C(g+\theta)^k
> \tag{8.1}
> \]
> が成立する。

**十分性の証明。** (8.1)は $J(T,Z)\le C(g+\theta)^k$ そのものである。(5.5)に代入すると

\[
N\le\frac{\left(\theta+(r+1)\left(\theta+C(g+\theta)^k\right)+1\right)^2}{4}
\]

となり、固定 $r,C,k$ に対し $g,\theta$ の多項式である。$\square$

実は、多項式上界の有無という水準では C と M は同値である。M が真なら、補題2.1と $\lambda=1$ から

\[
\Delta(T,Z)\le\max_{z\in\mathcal W}\bigl||z|-N\bigr|
\le\max\{N,\theta\},
\]

従って $J\le\Delta$ も多項式であり、これはどの証人選択でも成立する。したがって C は一般問題を解いた補題ではなく、**その未解決部分を一変数の近似保存量と二つの整数式へ具体化したもの**である。

前回の命題 R と異なり、全置換の $2^k$ 個の組合せも、その無限代入閉包も要求しない。必要なのは、一つの最短純導出、各規則の短い成功使用、および一箇所の相互差替えだけである。ただし $T$ のサイズ自体は小さいと分からず、(8.1)の中には未知の $N$ が現れる。そのため、これを直ちに多項式時間の算法と解釈してはならない。

### 8.2 否定方向の設計仕様

反例族を完成するには、次をすべて満たす必要がある。

1. **固定性と表示。** 固定アルファベット・固定型付け・固定 $r$ のもとで、明示的な reduced good fan-out $\le2$ 文法 $G_n$ を与え、$g_n\theta_n=n^{O(1)}$ を全規則の最短成功使用から証明する。
2. **希少な純型。** 純語を生成し、そのすべての長さが $N_n=n^{\omega(1)}$ 以上であることを証明する。長い一つの生成組の存在だけでは不十分である。
3. **全分布。** arity 1・2、全非空組、全許容文脈で代入可能性を証明する。有限例の検査や純部分の分類だけでは代用しない。
4. **新しい必要条件。** 今回の三文字型付けでは、どの最短純導出と短い規則使用を選んでも、系5.2の不整合な二語が存在し、その正規化された差は少なくとも
   \[
   \frac{2\sqrt{N_n}-\theta_n-1}{r+1}
   \]
   に達する。各語の $c$ 個数は $\theta_n$ 以下である。それほど異なる「純文字数の欠損／混合文字数」の比を許してなお、二穴代入可能性を保つ必要がある。
5. **今回排除した形式を避ける。** 正の共通重みの幅が多項式以下の族は使えない。また三文字で (6.1) の全経路・共通加法量切片そのものを使う族も使えない。

位相方式を続けるなら、具体的には、型ごとの異なる目標 $h_1,h_\zeta$ を使う、共通加法量切片の真部分集合に追加の構造制約を入れる、または中立文字を増やす、などの方向が残る。ただしこれらが成功するとは予測していない。型ごとの目標を使う場合、Astra 三文字報告 §5.1の位相・加法量補題により全 arity の代入可能性を確保できる一方、MCFL 性・小厚さ・長い純最短語の両立は別途証明しなければならない。追加の構造制約を入れる場合は、その制約についても全分布一致を改めて示す必要がある。

従来の必要条件も残る。F3の長さスペクトル、F4の文字支持、F5の NFA 規模、F6の深い挿入と多数の run、純 singleton の場合の F7を同時に満たす必要がある。今回、その三点の完成証明 (i)–(iii) を持つ新しい反例族は得ていない。

#### 位相方式で次に構成すべき族の、さらに具体的な仕様

固定された一文字一辺のグラフ、固定された $U_1$ 型付けを選び、中立文字を少なくとも二つ持たせる。各 $n$ について整数加法写像 $\phi_n$ と二つの目標 $h_{n,1},h_{n,\zeta}$ を指定し、

\[
\mathcal L_n=\{w\in R_{p,q}\cap\Sigma^+:
\phi_n(\Psi(w))=h_{n,s(w)}\}
\tag{8.2}
\]

を考える。この枠で必要な残りの二項は、次のように完全に分離できる。

- **整数解側。** 中立辺だけの非負整数個数ベクトル $x$ で、$\phi_n(x)=h_{n,1}$、$p$ から $q$ の流量条件、非空の支持の経路連結条件（非零次数の頂点と $p,q$ を含む無向支持が連結）を満たすものが存在し、そのすべてが $\|x\|_1\ge N_n=n^{\omega(1)}$ を満たす。
- **文法側。** (8.2) の全体を生成する reduced good fan-out $\le2$、固定 rank の $G_n$ を明示し、規則の明示端末・変数出現を実際に数えて $g_n=n^{O(1)}$、各規則に長さ $n^{O(1)}$ の成功使用を与える。大きい行列係数や長い端末列を、展開しない略記によって無料で文法へ埋め込んではならない。

**この二項が反例に十分であることの証明。** 全 arity の代入可能性は、次の理由で自動的に成立する。同じ型ベクトルの二組が共有文脈 $E$ に受理されれば、全体型は一致するため、その二語の目標値は同じ $h_{n,s(E[\mathbf x])}$ である。固定部分を引いて組の加法量の和が一致する。さらに非空内部区切りと固定開始・終了頂点から各成分の両端が一致する。別の許容文脈 $F$ でも接続可能性は一致し、全体型も二組で一致し、加法量も一致するので、(8.2)への所属が一致する。この論証は arity 1 と2をともに含む。

整数解側の流量・連結条件は、§6.2の Euler 路の構成により、純な経路語の個数ベクトルであることと同値である。従って純語が存在し、その最短長は $N_n$ 以上。文法側は MCFL 性と規模・厚さの条件を保証する。これで問題 M の適格な反例条件がすべて成立する。$\square$

この仕様を満たす具体的な $\phi_n,h_{n,1},h_{n,\zeta},G_n$ は今回得ていない。三文字の場合、二つの目標を同じにする方式は定理6.1で排除された。型別に異なる目標を使うことが、この方式で残された具体的な自由度である。

### 8.3 M と全特徴データ問題の区別

肯定方向で得たのは、明記した部分クラスの $\mu_1$ 上界と、一般 M の具体的な帰着である。これだけで全型付き非終端の $\tau$ を抑えたことにはならず、一般 SC_A や三文字型付けの特徴データ多項式性も未解決である。

否定方向で仕様1–3を満たす族が得られれば、原稿 `prop:rare-type` と `cor:typed-sandwich` により、どの特徴標本も純型を含み、その符号長は少なくとも $N_n+1$ となる。この含意は表示に依らないが、今回の不適格な実験族 (7.1) には適用しない。

## 付録A. 論文挿入用の英語 LaTeX 案

以下は証明済みの主要結果だけを記す。未証明命題 C は含めない。label は `astra-pure-20261031-` を含むものとし、取得原稿との衝突を確認した。コンパイルは実施していない。

```latex
\begin{theorem}[A finite approximate-weight certificate]
\label{thm:astra-pure-20261031-certificate}
Let $G$ be a reduced good MCFG of rank at most $r\ge1$ over
$\{a,b,c\}$, and put $\theta=\bar\theta_G$.
Give $a,b$ type $1$ and $c$ type $\zeta$ in $U_1$.
Let $w$ be a shortest pure word, of length $N$, and fix a
successful derivation $T$ of $w$.
For each rule $R$ used in $T$, choose a shortest successful use
$Z_R=D_R[\boldsymbol\eta_R]$ of that rule, with designated child
yields $\boldsymbol\eta_{R,j}$.
For a node $u$ of $T$ using $R$, let $U_u$ be obtained by
replacing the designated $R$-subtree of $Z_R$ by the subtree
at $u$.  For its $j$th child $u_j$, let $V_{u,j}$ be obtained
by replacing that child subtree of $T$ by a derivation of
$\boldsymbol\eta_{R,j}$.
Let $\mathcal W$ consist of $w$, all $Z_R$, all $U_u$,
and all $V_{u,j}$.

Suppose there are $\lambda>0$ and $D\ge0$ such that
\[
 \bigl||z|_a+|z|_b+\lambda|z|_c-N\bigr|\le D
 \qquad(z\in\mathcal W).
\]
Then
\[
 N\le\left\lfloor
 \frac{(\theta+(r+1)D+1)^2}{4}\right\rfloor.
\]
No substitutability assumption is needed.
\end{theorem}

\begin{proof}
Write $\psi(z)=|z|_a+|z|_b+\lambda|z|_c$, extended additively
to tuples and fixed parts of contexts.  Let $\ell_u$ be the
total length of the yield at $u$.  Every yield in $T$ is pure
by nondeletion.  Linearity and nondeletion give
\[
 \psi(V_{u,j})=N-\ell_{u_j}+\psi(\boldsymbol\eta_{R,j}),
 \qquad \psi(U_u)=\psi(D_R)+\ell_u.
\]
Put $B=(\theta+(r+1)D+1)^2/4$.
If $\lambda\le1$, a selected short word $Z_R$ gives
$N\le\theta+D\le B$.  The last inequality follows from
\[
 \frac{(\theta+2D+1)^2}{4}-(\theta+D)
 =\frac{(\theta-1)^2}{4}+\theta D+D^2\ge0.
\]
If $1<\lambda\le D$, then $N\le D\theta+D\le B$, since
\[
 \frac{(\theta+1+2D)^2}{4}-D(\theta+1)
 =\frac{(\theta+1)^2}{4}+D^2\ge0.
\]
It remains to assume $\lambda>\max\{1,D\}$.
Set $t=\lambda-D$.

For any child with $\ell_{u_j}<t$, the certificate implies
$\psi(\boldsymbol\eta_{R,j})\le\ell_{u_j}+D<\lambda$.
Such a child yield contains no $c$.  Its total length is
therefore its weight and is at least $\ell_{u_j}-D$.
If $N<t$, apply this observation at the root.  Its rule writes
no $c$, so the designated local yield of the short witness
is a pure start yield of length at most $\theta$.
Thus $N\le\theta\le B$.

Otherwise choose a lowest node with total yield length
$h\ge t$.  Every child lies below the threshold.  If its rule
is $R$ and has $q\le r$ children, all the designated witness
children are pure and the rule itself writes only neutral
letters.  Consequently
\[
 \|\boldsymbol\eta_R\|_1\ge h-qD\ge h-rD.
\]
The reverse graft $U_u$ gives $\psi(D_R)\ge N-D-h$.
Every letter has weight at most $\lambda$, hence
\[
 \theta\ge |Z_R|
 \ge h-rD+\frac{N-D-h}{\lambda}.
\]
Using $h\ge\lambda-D$ and $\lambda>1$, we obtain
\[
 \begin{split}
 N&\le\lambda(\theta+rD)+D-(\lambda-1)h\\
  &\le-\lambda^2+\lambda(\theta+(r+1)D+1)
  \le B.
 \end{split}
\]
Taking the integer part proves the assertion.
\end{proof}

\begin{corollary}[Bounded positive-weight oscillation]
\label{cor:astra-pure-20261031-weight-band}
Under the same grammar assumptions, suppose the values
$|z|_a+|z|_b+\lambda|z|_c$, for $z\in L(G)$ and some
$\lambda>0$, lie in an interval of width $D$.
If $L(G)$ contains a pure word, then
\[
 \mu_1(L(G))\le
 \left\lfloor\frac{(\bar\theta_G+(r+1)D+1)^2}{4}\right\rfloor.
\]
In particular, constant weight gives
$\mu_1(L(G))\le\lfloor(\bar\theta_G+1)^2/4\rfloor$,
also for fan-out two and two neutral letters.
\end{corollary}

\begin{proof}
Every grafted word in the preceding theorem is accepted by
$G$.  Its weight differs from that of the shortest pure word
by at most the width $D$.  Apply the theorem, and then set
$D=0$ for the final assertion.
\end{proof}

\begin{lemma}[Two-variable nonnegative integer solutions]
\label{lem:astra-pure-20261031-two-variables}
Let an integer linear system $Ax=d$ in two variables have a
nonnegative integer solution.  If all coefficients of $A$
have absolute value at most $B\ge1$, and all entries of $d$
have absolute value at most $H\ge1$, then there is such a
solution with $x_1+x_2\le4BH$.
\end{lemma}

\begin{proof}
At rank zero use zero.  At rank two choose two independent
rows.  Their determinant is a nonzero integer.  Each Cramer
numerator has absolute value at most $2BH$, so the unique
solution has sum at most $4BH$.
At rank one, consistency makes a single nonzero row
$ux_1+vx_2=t$ sufficient.  If one coefficient is zero, set
the free variable to zero; the other is at most $H$.
If both coefficients have the same sign, change the sign of
the equation if necessary; any nonnegative solution then has
sum at most $H$.
In the remaining case write $ux_1-vx_2=t$ with $u,v>0$,
and let $d_0=\gcd(u,v)$.  Choose a nonnegative integer
solution of least coordinate sum.  It cannot have both
$x_1\ge v/d_0$ and $x_2\ge u/d_0$, since subtracting
$(v/d_0,u/d_0)$ preserves the equation and reduces the sum.
If $x_1<v$, the equation gives $x_2\le u+|t|$.
If $x_2<u$, it gives $x_1\le v+|t|$.
Thus the sum is at most $2B+H\le4BH$ in either case.
\end{proof}

\begin{theorem}[Common additive constraints on edge-labelled paths]
\label{thm:astra-pure-20261031-path-fibre}
Each letter of $\Sigma=\{a,b,c\}$ labels one designated edge
of a finite directed graph.  Fix vertices $p,q$, an integer
linear map $\phi:\mathbb Z^3\to\mathbb Z^d$, and $h\in\mathbb Z^d$.
Let
\[
 L^+=\{w\in\Sigma^+: w\text{ labels a path from }p\text{ to }q,
                         \ \phi(\Psi(w))=h\}.
\]
Give $a,b$ type $1$ and $c$ type $\zeta$.
If $L^+$ contains a pure word and has a reduced good MCFG
presentation $G$ of rank at most $r$, then, writing
$\theta=\bar\theta_G$,
\[
 \mu_1(L^+)\le16(r+1)^4\theta^4(\theta+3)+2.
\]
The language is tuple-substitutable at every arity with
nonempty components and nonempty internal separators.
The coefficients of $\phi$ need not be positive or bounded.
\end{theorem}

\begin{proof}
For every nonterminal $A$, choose a yield $\boldsymbol\omega_A$
of total length at most $\theta$, and put
$b=\Psi(\boldsymbol\omega_S)$.
For a rule $R:A\to\rho(B_1,\ldots,B_t)$ put
\[
 \delta_R=\Psi(\rho(\boldsymbol\omega_{B_1},\ldots,
                    \boldsymbol\omega_{B_t}))
             -\Psi(\boldsymbol\omega_A).
\]
Set $M=(r+1)\theta$ and $B=2M^2$.
The thickness lemma gives $b\ge0$, $\|b\|_1\le\theta$, and
$\|\delta_R\|_\infty\le M$.
Induction on a derivation tree, subtracting the chosen short
yield at each node, gives
\[
 \Psi(w)=b+\sum_{u}\delta_{R(u)}.
\]
Moreover $\phi(b)=h$ and $\phi(\delta_R)=0$:
insert the two yields at the head of $R$ into one fixed
successful context and cancel its additive value.
Thus, for $U=\operatorname{span}_{\mathbb R}\{\delta_R\}$,
every integer point of $b+U$ satisfies the required additive
constraint, and every accepted Parikh vector belongs to $b+U$.

This affine space has integer defining equations with
coefficients bounded by $B$ and right sides bounded by $B\theta$.
At dimension zero use $x_i=b_i$.
At dimension one choose a nonzero generator $\delta$ and
$\delta_k\ne0$, and use
$\delta_k(x_j-b_j)-\delta_j(x_k-b_k)=0$ for $j\ne k$.
At dimension two use a normal vector obtained as the cross
product of two independent generators; its coordinates have
absolute value at most $2M^2$.
At dimension three no equations are needed.
These constructions prove the stated coefficient bounds.

Choose the nonempty edge support $J\subseteq\{a,b\}$ of
one pure accepted word.  Impose $x_c=0$, the flow equations
for a path from $p$ to $q$, zero counts outside $J$, and
positive counts on $J$.
Write $x_i=1_{i\in J}+z_i$ for $i=a,b$, with $z_i\ge0$;
for unused edges impose $z_i=0$.
The resulting integer system in two variables has coefficients
bounded by $B$ and right sides bounded by $H=B(\theta+3)$.
The chosen pure word supplies a nonnegative integer solution.
By Lemma~\ref{lem:astra-pure-20261031-two-variables}, another
solution has
\[
 x_a+x_b\le4BH+2=16(r+1)^4\theta^4(\theta+3)+2.
\]

The resulting edge multiplicities have the same support $J$
and the required flow imbalance.  Their underlying support is
connected because the original pure word traverses it.
If $p\ne q$, add one edge from $q$ to $p$ to balance all
vertices.  A finite balanced directed multigraph with connected
support has an Euler circuit: follow unused edges to form a
closed trail, and, while edges remain, form another closed
trail at a visited vertex incident with unused edges and splice
it into the first.  Balance prevents stopping at a different
vertex, and connectivity supplies such a visited vertex.
If an edge was added, cut the circuit at that edge and remove
it.  This produces the required path from $p$ to $q$.
Its label is pure, nonempty, has a Parikh vector in $b+U$,
and hence belongs to $L^+$.  This proves the length bound.

Finally suppose two nonempty tuples share an admissible
accepting context.  Every nonempty fixed internal separator
specifies its endpoint vertices because each letter denotes
one edge.  Empty outer separators are anchored by $p$ or $q$.
Consequently corresponding tuple components connect the same
two vertices.  Cancelling the fixed additive value of the
shared context also equates the sums of their component
$\phi$-values.  In every other admissible context the tuples
therefore have the same path compatibility and the same total
additive value.  Both completed words are nonempty, so their
membership agrees.  This proves the assertion for every arity,
including arities one and two.
\end{proof}
```

## 付録B. 計算の範囲、ソース全文、実行ログ全文

今回の数理計算は、以下の Python プログラムの一回の実行である。標準ライブラリのみを使用した。

1. $L_{k,m}$ の $(k,m)=(1,2),(2,1),(2,2),(2,3),(3,2)$ の5例。最大重みは6。各有限言語を完全生成し、全受理語の全一穴・二穴分解から全分布を作って検査した。成分は非空、二穴の中央区切りも非空である。未知の長語を打ち切って分布を近似したものではない。
2. (7.1)の $n=2,3,4,5,6$ の5例。言語全体は列挙せず、非循環文法の短い組と短い外側を動的計画で求め、全規則の最短成功使用長、および差替え証明書の個数ベクトルを計算した。この族は arity 2 のクラス外であり、通過例として数えない。
3. (5.3)の有理数公式と、一変数の絶対値関数の折点を列挙した直接最小化を照合した。非負の折点は、残差が0になる点と、二つの符号付き残差が一致する点、境界0を含む。有限個の一次関数の最大値の最小化なのでこの候補列挙は対象の数値問題について完全である。

個数の実装では中立文字を合計して数える。各非終端で選んだ純導出を固定しており、同じ非終端の複数出現が生む同じ個数ベクトルは重複除去した。これは $\Delta,J$ の最大値を変えない。二成分文法の具体的テンプレートは (7.1) に明記し、計算ではその加法的な端末・子寄与を用いている。

数理実験をこれ以上広い一般探索と見なしてはならない。一般の代入可能性から命題 C を検証した計算も、任意の整数係数の経路言語を網羅した計算もしていない。定理2.2、5.1、6.1は計算結果に依存しない。

### B.1 ソース全文

```python
from collections import defaultdict
from fractions import Fraction as F
from functools import lru_cache

def add(*vectors):
    return tuple(sum(v[i] for v in vectors) for i in range(2))

def sub(x, y):
    return tuple(a-b for a, b in zip(x, y))

def delta_formula(points, n):
    pure = max([abs(a-n) for a,c in points if c == 0] + [0])
    boundary = max([a-n for a,c in points if c > 0] + [0])
    mixed = [(a,c) for a,c in points if c > 0]
    pair = max([F(abs(d*(n-a)-c*(n-b)), c+d)
                for a,c in mixed for b,d in mixed] + [F(0)])
    return max(F(pure), F(boundary), pair), pair

def delta_breakpoints(points, n):
    candidates = {F(0)}
    for a,c in points:
        if c:
            candidates.add(F(n-a,c))
        for b,d in points:
            if c+d:
                candidates.add(F(2*n-a-b,c+d))
            if c != d:
                candidates.add(F(b-a,c-d))
    candidates = [x for x in candidates if x >= 0]
    return min(max(abs(F(a)+x*c-n) for a,c in points)
               for x in candidates)

# A rule is (head, terminal count vector, children).
# The two counts are all neutral letters and all marked letters.
def certificate(rules, start):
    heads = sorted({a for a,t,ch in rules})
    byhead = {a:[(t,ch) for b,t,ch in rules if b == a] for a in heads}
    @lru_cache(None)
    def shortest(a):
        choices = [add(t, *(shortest(b) for b in ch)) for t,ch in byhead[a]]
        return min(choices, key=lambda x:(sum(x), x))
    @lru_cache(None)
    def pure(a):
        choices = []
        for t,ch in byhead[a]:
            if t[1] == 0:
                children = [pure(b) for b in ch]
                if all(x is not None for x in children):
                    choices.append((add(t, *(x[0] for x in children)), (t,ch)))
        return min(choices, key=lambda x:(sum(x[0]), x[1])) if choices else None
    outside = {start:(0,0)}
    for a in reversed(heads):
        assert a in outside
        for t,ch in byhead[a]:
            for j,b in enumerate(ch):
                candidate = add(outside[a], t,
                                *(shortest(d) for k,d in enumerate(ch) if k != j))
                if b not in outside or (sum(candidate),candidate) < (sum(outside[b]),outside[b]):
                    outside[b] = candidate
    minima = [sum(add(outside[a],t,*(shortest(b) for b in ch))) for a,t,ch in rules]
    theta = max(minima)
    root = pure(start)[0]
    n = sum(root)
    points = {root}
    seen = set()
    def visit(a):
        if a in seen:
            return
        seen.add(a)
        local, (t,ch) = pure(a)
        points.add(add(outside[a], t, *(shortest(b) for b in ch)))
        points.add(add(outside[a], local))
        for b in ch:
            points.add(add(sub(root,pure(b)[0]),shortest(b)))
            visit(b)
    visit(start)
    assert all(a >= 0 and 0 <= c <= theta and 1 <= a+c <= n+theta for a,c in points)
    delta, pair = delta_formula(points,n)
    assert delta == delta_breakpoints(points,n)
    rank = max(len(ch) for a,t,ch in rules)
    bound = (F(theta)+(rank+1)*delta+1)**2/4
    assert n <= bound
    return n,theta,delta,pair,bound,minima

def weight_rules(k,m):
    total = k*m
    rules = []
    for j in range(1,total+1):
        for _letter in 'ab':
            rules.append((j,(1,0),() if j == 1 else (j-1,)))
        if j >= k:
            rules.append((j,(0,1),() if j == k else (j-k,)))
    return rules,total

@lru_cache(None)
def weight_words(k,total):
    if total == 0:
        return frozenset({''})
    result = {letter+w for letter in 'ab' for w in weight_words(k,total-1)}
    if total >= k:
        result |= {'c'+w for w in weight_words(k,total-k)}
    return frozenset(result)

def check_all_contexts(language):
    dist = defaultdict(set)
    groups = defaultdict(set)
    for w in sorted(language):
        for i in range(len(w)):
            for j in range(i+1,len(w)+1):
                x,e = (w[i:j],),(w[:i],w[j:])
                dist[x].add(e)
                groups[(e,tuple('c' in z for z in x))].add(x)
                for k in range(j+1,len(w)):
                    for ell in range(k+1,len(w)+1):
                        x,e = (w[i:j],w[k:ell]),(w[:i],w[j:k],w[ell:])
                        assert all(x) and e[1]
                        dist[x].add(e)
                        groups[(e,tuple('c' in z for z in x))].add(x)
    return all(len({frozenset(dist[x]) for x in xs}) == 1 for xs in groups.values())

for k,m in [(1,2),(2,1),(2,2),(2,3),(3,2)]:
    rules,start = weight_rules(k,m)
    n,theta,delta,pair,bound,minima = certificate(rules,start)
    language = weight_words(k,k*m)
    ok = check_all_contexts(language)
    assert ok and n == k*m and theta == k+m-1 and delta == 0
    assert all(x in (m,k+m-1) for x in minima)
    print(f'WEIGHT k={k} m={m} words={len(language)} N={n} theta={theta} '
          f'Delta={delta} J={pair} bound={bound} arity_1_2={ok}')

for n in range(2,7):
    # Actual fan-out two: A0 -> (a,b);
    # Ai -> (x1 y1,x2 y2)(A_{i-1},A_{i-1}) | (c,c);
    # S -> x1 a x2 (A_n).  Counts suffice for the certificate.
    rules = [(0,(2,0),())]
    for i in range(1,n+1):
        rules += [(i,(0,0),(i-1,i-1)), (i,(0,2),())]
    rules += [(n+1,(1,0),(n,))]
    N,theta,delta,pair,bound,minima = certificate(rules,n+1)
    assert N == 2**(n+1)+1 and theta == 2*n+3
    print(f'NONCLASS_F2 n={n} N={N} theta={theta} Delta={delta} J={pair} bound={bound}')
print('ALL_ASSERTIONS_PASSED; finite context tests stop at weight 6; certificate tests stop at n=6')
```

### B.2 実行ログ全文

実行コマンドは `python3 verify_pureword.py`。終了コード0、標準エラー出力なし。標準出力は次の全文である。`bound` は実際の最大規則ランクを用いた定理2.2の実数上界であり、整数部分を取る前の値を表示している。

```text
WEIGHT k=1 m=2 words=9 N=2 theta=2 Delta=0 J=0 bound=9/4 arity_1_2=True
WEIGHT k=2 m=1 words=5 N=2 theta=2 Delta=0 J=0 bound=9/4 arity_1_2=True
WEIGHT k=2 m=2 words=29 N=4 theta=3 Delta=0 J=0 bound=4 arity_1_2=True
WEIGHT k=2 m=3 words=169 N=6 theta=4 Delta=0 J=0 bound=25/4 arity_1_2=True
WEIGHT k=3 m=2 words=97 N=6 theta=4 Delta=0 J=0 bound=25/4 arity_1_2=True
NONCLASS_F2 n=2 N=9 theta=7 Delta=8/3 J=8/3 bound=64
NONCLASS_F2 n=3 N=17 theta=9 Delta=8 J=8 bound=289
NONCLASS_F2 n=4 N=33 theta=11 Delta=96/5 J=96/5 bound=30276/25
NONCLASS_F2 n=5 N=65 theta=13 Delta=128/3 J=128/3 bound=5041
NONCLASS_F2 n=6 N=129 theta=15 Delta=640/7 J=640/7 bound=1032256/49
ALL_ASSERTIONS_PASSED; finite context tests stop at weight 6; certificate tests stop at n=6
```

## 自己点検表

| 点検項目 | 結果 |
|---|---|
| 量化子：一般 M と部分クラスを区別したか | はい。一般 M は未解決。重み区間と共通加法量経路言語では、条件を満たすすべての言語・すべての指定の表示に上界を証明 |
| 多項式の係数に言語の大きな重みを隠していないか | はい。系3.2は $\lambda,W$ に依存しない。定理6.1は整数写像の係数や目標値に依存しない |
| 規則の短い成功使用を本当に使ったか | はい。定理2.2は選択した $Z_R$ の内側と外側を同時に評価。定理6.1は元の厚さ補題による全非終端の短い組と各規則の端末数を使用 |
| 内側の区切りの非空性を守ったか | はい。位相言語の代入可能性では非空の内部区切りが端点を決定する。有限検査も $j<k$ を課す。文法的差替えを、空区切りを使う代入可能性と取り違えていない |
| arity 1 と2を両方扱ったか | はい。等号例と経路・加法量族は全 arity の全組・全文脈を証明。二成分の失敗族は arity 2 の不成立を明記 |
| 組の成分は非空か | はい。主証明で生成組は元の $\lambda$-free 文法から取る。新たに作る語は非空の辺支持を保つ |
| 二成分の交錯を無視していないか | はい。数値評価は全成分の総長と Parikh 寄与で行い、線形・非削除性により加法性を保証。欠陥立方体の順序による単射性は未証明のまま使用しない |
| 最短純語の「一意性」を誤用していないか | はい。語の一意性は仮定しない。純語の長さ $N$ と、純な組の総長を使う |
| 正の重みの特殊ケースを全有限言語へ広げていないか | はい。重み区間条件は追加仮定。一般の有限純部分だけでは解決していない |
| 加法量経路定理で型ごとの別目標を許したか | いいえ。共通の一つの $h$ が必須であり、型別の $h_1,h_\zeta$ は未処理と明記 |
| 加法量経路定理で切片の真部分集合を誤って扱っていないか | はい。定義 (6.1) との等号が必要。小さい整数解に対応する経路が受理される根拠を明示 |
| 有理点から無根拠に整数点へ移っていないか | はい。非負整数解の存在は元の純語から得る。小さい整数解は二変数補題で別に証明 |
| 個数ベクトルが実際の経路語になるか確認したか | はい。元の純経路と同じ非空支持、流量条件、連結性を保ち、Euler 路の構成を証明 |
| $\lambda=0$ の境界を正の重みと混同していないか | はい。定理5.1では下限として扱い、正の $\lambda$ による近似と極限で定理2.2につなぐ |
| 等号例の全規則の厚さを評価したか | はい。(4.5)により全定数規則と全非定数規則を扱い、最大値を明示 |
| 数値的な二乗の鋭さと $\theta^c\operatorname{poly}(g)$ の不可能性を区別したか | はい。今回の等号例の表示は大きく、後者の強い最適性は主張しない |
| 不適格な文法を M の反例に数えていないか | はい。(7.1)は arity 2 の不成立により明確に除外 |
| $\mu_1$ と $\tau,t_{\rm typ}$、特徴データを区別したか | はい。肯定は $\mu_1$ の部分結果。否定への rare-type の含意は、適格な反例族が完成した場合だけ |
| 命題 C を証明済みと扱っていないか | はい。多項式上界の有無として M と同値な、具体的な未解決命題とした |
| 証明に計算への依存があるか | いいえ。今回の証明済み結果はすべて本文の解析的証明による。既知の singleton 分類は先行報告の定理として引用 |
| 計算のソース・ログ・打切り範囲を省略したか | いいえ。今回の実行の全文を付録Bに収録。既報の大量探索を今回再実行したとは述べていない |
| 英語案は証明済み結果だけか | はい。有限重み証明書、重み区間の系、二変数補題、共通加法量経路定理のみ |
| 文献上の新規性まで認証したか | 未認証。指定原稿・指定報告との差分を示した。網羅的文献調査と独立査読は未実施 |

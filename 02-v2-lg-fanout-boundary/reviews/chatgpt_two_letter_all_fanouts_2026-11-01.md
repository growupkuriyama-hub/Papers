# 二文字の内容型付け：ファンアウト $f\ge2$ への拡張

**証明監査・一般化報告書（2026-11-01）**  
対象：Takayuki Kuriyama, 論文 #2、`thm:two-letter-content` および付録 H。  
**結論：固定した任意の $f\ge2$ に一般化できる。** 非飽和側の挿入閾値と、飽和側の純粋節点の閾値を同時に変更すれば、指定された形の特徴標本長の多項式上界が得られる。$f$ に関する一様な多項式上界を主張するものではない。

## 0. 補題別の判定（先に結論）

以下で $v=|V|$、$\theta=\bar\theta_G\ge1$、$r\ge2$、$f\ge2$ は固定し、

\[
D_f:=(6f+1)3^f,\quad
A_f:=(2f+1)(2f+2),\quad
C_{f,r}:=(r+1)\bigl(6r(3f+1)+D_f\bigr)
\]

とする。

| 原稿の箇所 | 判定 | $f\ge2$ における変更・結論 |
|---|---|---|
| `lem:app-two-basic` (i) | **そのまま成り立つ** | 任意の次数 $d\le f$ の型付き非終端に関する分布同値類の表示。定数なし。 |
| `lem:app-two-basic` (ii) | **そのまま成り立つ** | 同じ非終端を持つ祖先・子孫で全Parikhベクトルが等しければ、間の規則は恒等。`good` の４条件を使い、$f$ に依存しない。 |
| `lem:app-two-runs` (i)–(iv) | **そのまま成り立つ** | 用いる代入可能性は $d=1,2$ のみ。$L\in\mathcal C_{f,c}$、$f\ge2$ で利用可。 |
| `lem:app-two-alternate` | **そのまま成り立つ** | 前項から直接従う。 |
| `lem:app-two-insertion` | **修正して成り立つ** | $d\le f$、印は $\le4f$、隣接グラフ最大次数 $\le2f$。$|Q|\ge\boxed{6f+2}$ とすれば、結論 (a)(b) は不変。 |
| `prop:app-two-nonsaturated` | **修正して成り立つ** | 重い節点の反鎖 $\le6f+1$、型付きラベル $\le3^f v$。$t_{\rm typ}\le\boxed{D_f(r+1)v\theta}$。 |
| `lem:app-two-saturated`：成分内容の和が $\Sigma$ | **修正して成り立つ** | $1\le t_a,t_b\le f$、深さの種類 $\le\theta+2f+1$、同じ深さの重い節点 $\le\theta+2f$。$\tau_X\le A_f(r+1)v\theta^3$。 |
| 同上：全成分が同一文字、(P1) | **そのまま成り立つ** | $h=d\le f$ に置換すればよい。 |
| 同上：(P2) | **修正して成り立つ** | 大きい $K$ の場合を $K>\theta+2(f-1)$ とする。各非終端・同じ $b$-個数は１本のパス上に高々２回。パス長 $\le2v(q+1)$。 |
| 同上：(P3) | **修正して成り立つ** | **重要**：「重い純粋節点」を $\ell_u>\theta+f-1$ と定義する（$f=2$ の $\theta+1$ の一般化）。これで同名節点の非比較性が回復。 |
| 同上：(P4) | **修正して成り立つ** | 上記の閾値により、反復する重い純粋節点で $g_u\le K-f\le K-h$。頻出閾値 $m_B>\theta$ は変更不要。 |
| 同上：(P5) | **修正して成り立つ** | $\alpha_*=(r+1)(\theta+f-1)(2\theta+1)v\le3f(r+1)v\theta^2$。 |
| 同上：(P6) | **修正して成り立つ** | $T_*=(\alpha_*+1)\theta\le(3f+1)(r+1)v\theta^3$、$p+K\le[6r(3f+1)(r+1)+5]v^2\theta^5$。 |
| `thm:two-letter-content` | **修正して成り立つ** | $\tau(G,c)\le C_{f,r}v^2\theta^5$、両学習作用素に共通の特徴標本の長さ $\le4^{fr}(3+rC_{f,r})\|G\|^3\theta^5+\mathbf 1_{\{\varepsilon\in L\}}$。 |
| `cor:two-letter-semilattice` | **修正して成り立つ** | 二文字上の任意の有限半束型付けについて同じ上界が成り立つ。 |

**確認点：** $f=2$ では $D_2=13\cdot9=117$、$C_{2,r}=(r+1)(42r+117)$ となり、原稿の定数を**ちょうど再現**する。

## 1. 原稿・仮定・量化の照合

確認した編集正本：[`Papers/02-v2-lg-fanout-boundary/main.tex`](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/main.tex)、GitHub contents API から 2026-11-01 に取得、**blob SHA `e4b21e9db05a0d6089f56b09ee0ef11ec1ef23ae`**。以下の行番号はこの版のソース行を指す：定義は 408–646、厚さ・特徴標本は 947–1240、定理と系は 1930–1968、付録Hは 3102–3444。プロジェクトマスター v16（10月23日の #2 作業状態）はこの版の代用としなかった。

原稿の設定を保つ：$\Sigma=\{\mathtt a,\mathtt b\}$、$c(w)$ は非空語 $w$ の文字内容、$c$ の正像は $\{\{a\},\{b\},\{a,b\}\}$ であり、空語用 fresh completion は $|\mathsf S^\sharp|=4$。$L\in\mathcal C_{f,c}$ は **すべての $1\le d\le f$ における** $(d,c)$-組代入可能性を満たす。$G=(V,\Sigma,P,S,\mathrm{fan})$ は $L(G)=L\cap\Sigma^+$ を生成する reduced good MCFG、fan-out $\le f$、規則rank $\le r$。`good` は $\lambda$-free、非削除、非置換、非融合（nonmerging）を意味する。

$\theta=\max\{1,\theta_G\}$、$v=|V|\ge1$ とする。原稿 `lem:thickness-equivalence` の (i),(ii),(iv) により、各規則が書く端末は $\le\theta$、各 $B\in V$ に $\omega_B\in L_B(G)$ で $\|\omega_B\|_1\le\theta$ があり、各 $A$ に許容文脈 $E_A$ で $|E_A|_{\rm fix}\le\theta$ がある。各 $A$ の成分数 $d\le f$ に対して、$E_A$ は正しい順序の $d$ 個の穴を持ち、隣り合う穴の間には少なくとも一文字がある。

型付き精密化 $\widetilde G_0$ は実現された各成分の $\widehat c$-型で $A$ を細分化したものとし、$t_{\rm typ}(G,c)$ はその型付き非終端の最短導出タプルの最大長、$\tau(G,c)$ は同じ型・同じ分布を持つ**任意のタプル**の最短代表長の最大値。重要な区別は $\tau\le t_{\rm typ}$ だが逆は一般に成立しないこと。$N_{\rm typ}$ は、原稿と同じく非開始型付き非終端数＋非開始型付き規則数を表す。

$\mathcal B^{\le r}_{f,c}$ は rank cap あり、$\mathcal B_{f,c}$ は cap を要求しない原稿の集合駆動作用素である。以下の**特徴標本の存在**はこの二作用素への共通保証であり、任意の Gold 学習器のデータ長・収束段階・実行時間への保証ではない。また $f,r$ は定数として固定され、$C_{f,r}$ および $4^{fr}$ の $f,r$ 依存は隠さない。

## 2. $f$ に依存しない補題：詳細証明

### 2.1 `lem:app-two-basic` (i)

$X=A_{\mathbf t}$ を arity $d\le f$ の実現された型付き非終端とし、$\mathbf u\in L_X$ を固定する。原稿 `lem:typed-homogeneity` より、$L_X$ のすべてのタプルは $c^{(d)}$-型 $\mathbf t$ と分布 $\mathcal D_L^{(d)}(\mathbf u)$ を共有する。$E_A$ は $\mathbf u$ を受け入れるので、同じ型 $\mathbf t$ の $\mathbf z$ が $E_A[\mathbf z]\in L$ を満たせば、$(d,c)$-組代入可能性により $\mathcal D_L^{(d)}(\mathbf z)=\mathcal D_L^{(d)}(\mathbf u)$ となる。逆向きは、分布が等しければ $E_A$ で受け入れられることから直ちに従う。従って

\[
\operatorname{Cl}_{L,c}(X)
=\{\mathbf z\in(\Sigma^+)^d:\ c^{(d)}(\mathbf z)=\mathbf t,\ E_A[\mathbf z]\in L\}.
\]

原稿の証明のままで、$d\le2$ を使わない。

### 2.2 `lem:app-two-basic` (ii)：恒等経路

同一非終端 $B$ の祖先 $u$ と真の子孫 $u'$ の総Parikhベクトルが等しいとする。非削除と線形性から、$u'$ のすべての文字は $u$ のyield内に残り、経路上で規則が書いた端末・他の子部分木が書いた端末が加わるだけである。後者は $\lambda$-free と生産性から非空なので、Parikh等号のもとでは存在できない。従って経路上は rank 1 かつ書き込み端末ゼロ。唯一の子の成分変数は、非削除により各々一度、非置換により本来の順序で現れ、各親成分は $\lambda$-free により空ではない。端末なしで親成分が二つ以上の変数を含めば、非置換の下で少なくとも一組の連続する子成分変数が隣接し、非融合に反する。したがって各親成分に変数が一つだけ入り、親子の fan-out は同じで写像は成分ごとの恒等写像。これは **任意の $f$** で成立する。

### 2.3 `lem:app-two-runs` と `lem:app-two-alternate`

ここでは原稿の四つの含意を、それぞれ使う代入可能性も含めて確認する。

1. $px^4q\in L$ なら、二つの二成分タプル $(x,xx)$ と $(xx,x)$ は同じ内容型 $(\{x\},\{x\})$ で、許容文脈 $p\square_1x\square_2q$ を共有する。**$d=2$ の代入可能性**により分布が等しい。従って、二つの異なる $x$-run の長さを一つずつ移す操作は membership を保存する。$x$-skeleton と $x$ の総数が同じ任意の二語は、このような単位移動で結ばれるため (i) を得る。
2. $xxyx$ または $xyxx$ があると (i) で両方を同じ前後の文脈で実現できる。そこで $xy$ と $yx$ は同じ内容 $\Sigma$ で一つの文脈を共有し、**$d=1$ の代入可能性**によりすべての文脈で交換可能。隣接転置は Parikh 同値類内の全文字列を結ぶので (ii) の Parikh 飽和が従う。
3. 非飽和なのに $xx$ と単独の内部 $y$-run が共存すると、前者の余分な $x$ を (i) でその内部run直前の $x$-run に運べ、$xxyx$ を生む。(ii) に矛盾する。よって (iii)。
4. 非飽和で $y^4$ が出現しないとする。$xx$ を持つ語に二つの内部 $y$-run $y^e,y^{e'}$ があれば、(iii) から $e,e'\ge2$。両run間の $x$-run を (i) により長さ 1 と 2 の両方で実現し、内容 $\Sigma$ の単一タプル $xy^ex$ と $xxy^e$ を交換する。すると二つのrunを合体した $y^{e+e'}$ を含む語が $L$ に現れる。$e+e'\ge4$ に反する。よって (iv)。

最後に、両方の $a^4,b^4$ が出現し、$L$ が非飽和と仮定する。4 run 以上ある語ではそれぞれの文字に内部runがある。一方の内部runを (i) で長さ1に縮め、他方に長さ2以上のrunが残れば (iii) に反する。両文字について反復し、4 run 以上の語はすべて長さ1のrunからなる（`lem:app-two-alternate`）。どの議論も代入可能性の次数は1か2であり、$f\ge2$ にそのまま含まれる。

## 3. 挿入補題：正確な閾値 $6f+2$

**一般化した補題。** $X=A_{\mathbf t}$ の arity $d\le f$、その $\widetilde G_0$-導出木 $T$ は最短総yield長、その中で最小節点数とする。重い節点（$\ell_u>\theta$）の反鎖 $Q$ が $|Q|\ge6f+2$ なら、原稿の (a)(b) はそのまま成立する。

**証明。** 各純粋成分（内容 $\{x\}$）の先頭・末尾それぞれ最大2文字に印を置き、各混合成分（内容 $\Sigma$）では $a,b$ を一つずつ選んで印を置く。各成分の印は $\le4$ 個、総数 $\le4f$。反鎖の節点の部分木は互いに交わらず、一つの印は高々一つの反鎖節点の部分木に書かれる。したがって、印を書かない節点の集合 $Q_0$ は

\[
|Q_0|\ge |Q|-4f\ge2f+2.
\]

$u\in Q_0$ の部分木を、同じ非終端 $B_u$ の短い導出 $\omega_{B_u}$ に無型で置き換える。$\ell_u>\theta\ge\|\omega_{B_u}\|_1$ だから総yield長は減少し、元の $G$ において有効な導出を得る。印を保持した混合成分は両文字を保持する。もし純粋成分すべても元の内容型を保持するなら、根の内容型ベクトルは変化せず、原稿 `lem:witness-length-template(i)` により新導出は同じ型付き $X$ の導出となり、$T$ の最短性に矛盾する。ゆえにある純粋成分に異なる文字が挿入される。変化したブロックの前後の先頭・末尾2文字はすべて保持されるため、その元の純粋成分の長さは少なくとも5である。原稿の (a)、すなわちある $x^5$ の出現、が成立する。

根の各成分の中で、節点 $u\in Q_0$ の各子yield成分が占める連続区間を $u$ の *block* と呼ぶ。非削除により各所有者の block は高々 $f$ 個。異なる所有者の block 同士が端末文字を挟まず隣接するとき所有者を結ぶ無向グラフを作る。block 一つの左右に隣接する block は高々2個なので最大次数 $\Delta\le2f$。したがって貪欲法で独立集合 $I$ を取り

\[
|I|\ge \left\lceil\frac{|Q_0|}{2f+1}\right\rceil
\ge\left\lceil\frac{2f+2}{2f+1}\right\rceil=2.
\]

$I$ 内の節点を**同時に** $\omega_{B_u}$ へ置き換える。異なる節点は反鎖なので操作は干渉せず、無型 $G$ の導出であり、$W=E_A[\mathbf u']\in L$。各所有者について前段と同じ最短性の議論から、もとの $\mathbf u$ のある純粋成分内に他方の文字を挿入する block がある。その block は成分両端から2文字以上離れ、$x,y,x$ の内部runを作る。独立性により、異なる所有者から選んだ変更blockの間には少なくとも一つの**変更されない元の文字**が残る。従って同一文字 $x$ の純粋成分に作られる二つの $y$-run は別々の内部runである。

$I$ の異なる二節点を選ぶ。両方が同じ文字 $x$ の純粋成分に変更を作るなら、$W$ に $xx$（純粋成分の保持された冒頭2文字）と**二つの内部 $y$-run**があり、run数は少なくとも5。異なる文字の純粋成分に変更を作るなら、$a^5,b^5$ の両方が $L$ の語の因子として存在し、$W$ の中には $a,b,a$ と $b,a,b$ の内部変化が別々にあり、run数は少なくとも6、かつ $aa$（または $bb$）がある。これは (b) そのものである。□

**原稿の置換箇所**（ソース行 3228–3280）：仮定 `arity $d\le2$` → `arity $d\le f$`、`$|Q|\ge14$` → `$|Q|\ge6f+2$`、`at most $8$ marks` → `at most $4f$ marks`、`$|Q_0|\ge6$` → `$|Q_0|\ge2f+2$`、`at most two blocks` → `at most $f$ blocks`、`maximum degree at most $4$` → `at most $2f$`、`$|I|\ge|Q_0|/5$` → `at least $\lceil|Q_0|/(2f+1)\rceil$`。**$6f+2$ はこの貪欲独立集合評価から2点を得るのに十分な閾値**であり、一般に最小の閾値だとは主張しない。

## 4. 非Parikh飽和の場合：$D_f=(6f+1)3^f$

上の補題の結論と §2 のrun補題により、最短かつ節点数最小の $T$ で重い節点の反鎖は高々 $6f+1$ 個。詳しくは、$a^4,b^4$ がともに出ないなら挿入補題(a)に矛盾；両方出るなら挿入補題(b) の $W$ は長さ2以上のrunを含む4-run以上の語で、`lem:app-two-alternate` に矛盾；片方のみ（例えば $a^4$）出るなら、挿入補題(a) は $a^5$ を与え、(b) は $aa$ と二つの内部 $b$-runを持つ語を与えるが、$b^4$ が出ないため `lem:app-two-runs(iv)` に矛盾する。

各成分の内容型は $\{a\},\{b\},\{a,b\}$ の3種類なので、arity $d\le f$ の型付きラベル数は $\le3^f v$。同一型付きラベルが $T$ の一本のパスで二度現れれば、上の部分木を下の部分木で置換すると同じ根内容型で総長は増えず、節点数が厳密に減少する（総長が減れば最短性にも反する）。よって一パスは $\le3^f v$ 節点。重い節点は祖先について閉じ、同一深さの重い節点は反鎖なので、重い節点の総数は

\[
H\le(6f+1)3^f v=D_fv.
\]

根が重くなければ総yield長 $\le\theta$。根が重ければ全ての端末文字は、重い節点自身が書くか、その重い節点の非重い子（高々 $r$ 個）のyieldに属する。各重い節点の書き込みは $\le\theta$、各非重い子の総yieldは $\le\theta$。ゆえに

\[
\boxed{t_{\rm typ}(G,c)\le D_f(r+1)v\theta.}
\]

これは **型付き導出自体の長さ** の上界なので、もちろん $\tau(G,c)\le t_{\rm typ}$ でもある。$f=2$ で原稿行 3281–3305 の $117$ が得られる。

## 5. Parikh飽和の場合：すべての (P1)–(P6)

任意の型付き $X=A_{\mathbf t}$（arity $d\le f$）を固定。$E_A$ の固定文字の Parikh ベクトルを $(p,q)$ とすれば $p+q\le\theta$。$\mathcal P=\Psi(L\cap\Sigma^+)$ とし、`lem:app-two-basic(i)` と飽和性から、$\tau_X$ は、成分内容型 $\mathbf t$ を持ち、固定文字を加えたベクトルが $\mathcal P$ に入るタプルの最短総長である。全成分内容の和は $\Sigma$ か、全成分が同じ一文字型か、のどちらかである。

### 5.1 内容の和が $\Sigma$ の場合

$a$ を含む成分数を $t_a$、$b$ を含む成分数を $t_b$ とすると $1\le t_a,t_b\le f$。内容型 $\mathbf t$ のタプルで総Parikhベクトル $(n_a,n_b)$ を持つものが存在する必要十分条件は $n_a\ge t_a,n_b\ge t_b$（各成分に一文字ずつ配分して、残りを含有可能な成分へ足す）。この条件と $(p+n_a,q+n_b)\in\mathcal P$ を満たす $n_a+n_b$ 最小の組を選ぶ。$c_a=n_a-t_a+1$、$c_b=n_b-t_b+1$ はともに1以上。飽和性から $W=a^{p+n_a}b^{q+n_b}\in L$、その節点数最小の成功導出を $T$ とする。

重い節点 $u$ で $a_u<c_a$ かつ $b_u<c_b$ なら、$u$ を短い $\omega_{B_u}$ に置換すると総長は減少する一方、元の $a,b$ 数から引かれる数はそれぞれ $\le n_a-t_a$、$\le n_b-t_b$ なので、新しい語のParikhベクトルから固定文字 $(p,q)$ を引いたものは必要下限 $t_a,t_b$ を保つ。新しい語は $L$ に属し最適性に反する。従って各重い節点は $a_u\ge c_a$ または $b_u\ge c_b$。

同一非終端の祖先 $u$、真の子孫 $u'$ について、$a_u-a_{u'},b_u-b_{u'}\ge0$。両差がそれぞれ $c_a,c_b$ 未満で総差が正なら、上と同じ置換により最小 $(n_a,n_b)$ に矛盾。両差が0なら §2.2 の恒等経路を削除して節点数最小性に矛盾する。したがって

\[
 a_u-a_{u'}\ge c_a\quad\text{または}\quad b_u-b_{u'}\ge c_b.
\]

各パス上で $\bigl(\lfloor a_u/c_a\rfloor,\lfloor b_u/c_b\rfloor\bigr)$ は成分ごとに非増加であり、同一非終端は同じ組値では繰り返せない。$n\ge t\ge1$、$p\ge0$ に対し

\[
\left\lfloor\frac{p+n}{n-t+1}\right\rfloor\le p+t,
\quad\text{なぜなら}\quad (p+t)(n-t+1)-(p+n)=(n-t)(p+t-1)\ge0.
\]

ゆえに組値の変化回数を含む値の総数は $\le1+p+t_a+q+t_b\le\theta+2f+1$。一本のパスの節点数は $\le v(\theta+2f+1)$。同じ深さの重い節点のyieldは互いに交わらず、各節点で $a_u\ge c_a$ または $b_u\ge c_b$ だからその数は

\[
\le\frac{p+n_a}{c_a}+\frac{q+n_b}{c_b}\le p+t_a+q+t_b\le\theta+2f.
\]

重い節点の総数は $\le v(\theta+2f)(\theta+2f+1)$。各重い節点の端末書き込みと非重い子部分木を数え、$W$ の全ての端末を覆えば

\[
\tau_X\le|W|\le\max\{\theta,(r+1)\theta v(\theta+2f)(\theta+2f+1)\}
\le\boxed{A_f(r+1)v\theta^3}.
\]

最後の不等式は $\theta+2f\le(2f+1)\theta$、$\theta+2f+1\le(2f+2)\theta$、$v,r+1,\theta\ge1$ による。これが原稿行 3325–3365 の正しい置換である。

### 5.2 全成分が $\{a\}$ の場合（$\{b\}$ は対称）

$h=d\le f$ とし、

\[
K:=\min\{k\ge h:(p+k,q)\in\mathcal P\}.
\]

$X$ は実現されているので $K$ は有限で、$\tau_X=K$。**$K\le\theta+2(f-1)$ なら $K\le(2f-1)\theta$** で既に要求する上界に収まる。以下、

\[
\boxed{K>\theta+2(f-1)\ge p+2(h-1)} \tag{H_f}
\]

を仮定する。$W=b^qa^{p+K}\in L$ の節点数最小の成功導出 $T$ を固定する。各節点 $u$ のParikhベクトルは $(a_u,b_u)$、$B_u$ は非終端である。

**(P1) Row rigidity（式は変更不要）。** もし $(c_0,y),(c_0+\delta,y)\in\mathcal P$、$c_0\ge1$、$1\le\delta\le K-h$ なら、飽和性によって文脈 $(b^ya^{c_0-1},\varepsilon)$ が $a$ と $a^{1+\delta}$ を両方受け入れる。両語の内容は $\{a\}$ なので $(1,c)$-代入可能性から全分布が一致する。$W$ に対する文脈 $(b^qa^{p+K-\delta-1},\varepsilon)$ で $a^{1+\delta}$ を $a$ に交換して、$(p+K-\delta,q)\in\mathcal P$ を得る。$K-\delta\ge h$ なのに $K-\delta<K$、矛盾。従ってこのような二点は存在しない。

**(P2) Height（$h\le f$ の真の修正点）。** 同一非終端を持つ祖先 $u$、真の子孫 $u'$ について $b_u=b_{u'}$ なら、$\delta=a_u-a_{u'}$ は、0 なら恒等経路削除による節点数最小性への矛盾、$1\le\delta\le K-h$ なら $u$ を $u'$ で置換して (P1) または $K$ の最小性への矛盾となる。従って $\delta\ge K-h+1$。同一パスに同じ $B$ かつ同じ $b$-個数の三節点があれば、$a$-個数の最大値は少なくとも $2(K-h+1)$ となるが、

\[
2(K-h+1)>p+K\qquad\Longleftrightarrow\qquad K>p+2h-2
\]

で、これは $(H_f)$ によって成立する。従って同じ $(B,b)$ はパス上に高々二度。$b$-個数はパスに沿って非増加で $0,1,\dots,q$ の $q+1$ 種だから、パス長は $\le2v(q+1)$。$b$ を含む節点（*mixed*）は、$b$ を書き込むいずれかの節点へのパス上にあり、その書き込み節点は高々 $q$ 個なので

\[
M:=\#\{u:b_u>0\}\le2vq(q+1)\le4v\theta^2.
\]

**(P3) Heavy pure nodes（変更必須）。** $b_u=0$ の節点で

\[
\boxed{\ell_u>\theta+f-1}\tag{HP_f}
\]

を満たすものを *heavy pure* とする。$g_u:=\ell_u-x_{B_u}$ とすれば、$\|\omega_{B_u}\|_1\le\theta$ から $g_u\ge f\ge2$。同一非終端の比較可能な heavy pure 節点 $u\succ u'$ があれば (P2) と $(HP_f)$ から

\[
a_u\ge a_{u'}+(K-h+1)
\ge(\theta+f)+(K-h+1)
=K+\theta+(f-h)+1>p+K,
\]

矛盾する。ゆえに **同一非終端の heavy pure 節点は互いに非比較**。heavy pure 節点の反鎖 $J$ に属する部分木を各々 $\omega_{B_u}$ で置換した語は、Parikhベクトル

\[
(p+K-\sigma(J),\ q+Y(J)),\qquad
\sigma(J)=\sum_{u\in J}g_u,\quad Y(J)=\sum_{u\in J}y_{B_u}
\]

を持つ。二つの反鎖 $J,J'$ について $\sigma(J),\sigma(J')\le K-h$、$Y(J)=Y(J')$ なら、両 resulting points の $a$ 座標は $\ge p+h\ge1$、$a$ 座標の差は $\le K-h$。従って (P1) により $\sigma(J)=\sigma(J')$。

**(P4) Repeated nonterminals。** 同じ $B$ が heavy pure 節点に $m_B\ge2$ 回現れるなら、それらは (P3) によって互いに非比較で、二つの長さは少なくとも $\theta+f$。従って各節点 $u$ について

\[
\ell_u\le p+K-(\theta+f)\le K-f,
\qquad f\le g_u\le\ell_u\le K-f\le K-h.
\]

(P3) を二つの単集合反鎖に適用して $g_u=g_B$ は一定となり、$\ell_u=\ell_B=x_B+g_B$ も一定。$y_B=0$ なら一つを置換した語は同じ $b$-個数のまま $a$-個数を $g_B\in[1,K-h]$ 減らし、$K$ の最小性に反する。ゆえに $y_B\ge1$。$B$ を *frequent* と呼ぶ条件は原稿通り $m_B>\theta$ とする。

頻出 $B,C$ について、$y_C\le\theta<m_B$ 個の $B$ 節点と、$y_B\le\theta<m_C$ 個の $C$ 節点をそれぞれ選べる。これらは同数の $b$ を置換により追加し（$Y=y_By_C$）、かつ

\[
y_Cg_B\le(m_B-1)\ell_B\le p+K-\ell_B\le K-f\le K-h
\]

であり、$C$ 側も同様。(P3) の反鎖比較から $y_Cg_B=y_Bg_C$。したがって全頻出非終端で

\[
\alpha:=g_B/y_B\quad\text{は共通},\qquad
\ell_B=x_B+\alpha y_B\le(1+\alpha)\theta.
\]

**(P5) Ratio bound。** 頻出非終端がある場合

\[
\boxed{\alpha\le\alpha_*:=(r+1)(\theta+f-1)(2\theta+1)v
\le3f(r+1)v\theta^2.}\tag{R_f}
\]

$\alpha\le\theta$ なら明らか。$\alpha>\theta$ なら頻出 $B$ の heavy pure 節点 $u$ を一つ固定し、その部分木にある heavy pure 節点数を $H_u$ とする。純粋節点の部分木はすべて純粋であり、heavy pure はこの中で祖先について閉じる。heavy pure 節点が書く端末数は $\le\theta$、その非-heavy-pure な子のyieldは $\le\theta+f-1$、子数は $\le r$ なので

\[
\ell_B\le(r+1)(\theta+f-1)H_u.
\]

heavy pure の祖先数で階層化すると、(P3) の非比較性により階層数は高々 $v$、各階層は反鎖。頻出ラベルの節点の各yieldは $\ell_C\ge\alpha$（$y_C\ge1$）、それらを含む $u$ の長さは $\ell_B\le(1+\alpha)\theta$ なので、各階層に頻出節点は $\le(1+\alpha)\theta/\alpha<\theta+1$ 個。非頻出節点は全木で、各ラベルにつき $\le\theta$ 個、合計 $\le v\theta$。よって $H_u\le v(\theta+1)+v\theta=v(2\theta+1)$。$\alpha\le g_B\le\ell_B$ と合わせて $(R_f)$ を得る。最後の不等式は $\theta+f-1\le f\theta$ と $2\theta+1\le3\theta$ による。

**(P6) Counting。** $b_u=0$ で

\[
\ell_u>T_*:=(\alpha_*+1)\theta
\le(3f+1)(r+1)v\theta^3
\]

を満たす節点を *large* と呼ぶ。$T_*>\theta+f-1$ なので large は heavy pure である。(P4)–(P5) により頻出非終端が large をラベル付けすることはない。非頻出ラベルはそれぞれ高々 $\theta$ 回なので、large 節点は全木で $\le v\theta$ 個。純粋祖先の長さは子孫の長さ以上なので、large は純粋な祖先について閉じる。

$W$ の全 $a$ は、mixed 節点が書いた文字、large 節点が書いた文字、または mixed でも large でもない極大部分木のyieldのいずれかにある。前二者の書き込みは各節点 $\le\theta$、後者の部分木根数は $\le rM+rv\theta+1$、各yieldの長さは $\le T_*$。よって

\[
\begin{aligned}
p+K&\le\theta M+(rM+rv\theta+1)T_*+\theta\cdot v\theta\\
&\le5v\theta^3+(6rv\theta^2)\,(3f+1)(r+1)v\theta^3\\
&\le\boxed{\bigl[6r(3f+1)(r+1)+5\bigr]v^2\theta^5}.
\end{aligned}
\]

ここで $M\le4v\theta^2$ と、$4rv\theta^2+rv\theta+1\le6rv\theta^2$（$r\ge2$, $v,\theta\ge1$）を使用。$\tau_X=K\le p+K$ だから純粋場合の上界が完成する。$(H_f)$ を満たさない小さい $K$ の場合は既に $K\le(2f-1)\theta$ と評価した。$b$ のみの成分の場合は文字を交換すれば同じ証明。

### 5.3 上記の全場合をまとめた定数

$D_f\ge A_f$ は $f\ge2$ で成立する。実際 $3^f\ge f+2$ を $f=2$ を起点に帰納的に示せば

\[
D_f=(6f+1)3^f\ge(6f+1)(f+2)\ge(2f+1)(2f+2)=A_f.
\]

また $D_f(r+1)\ge5$。したがって §5.1 の $A_f(r+1)v\theta^3$、§5.2 の $[6r(3f+1)(r+1)+5]v^2\theta^5$、$K$ が小さい場合の $(2f-1)\theta$ のすべてを、一つの

\[
\boxed{\tau(G,c)\le C_{f,r}v^2\theta^5,\qquad
C_{f,r}=(r+1)\bigl[6r(3f+1)+(6f+1)3^f\bigr]}
\]

で覆える。なお飽和側は $\tau$ を直接評価するのであり、**$t_{\rm typ}$ に同じ上界を主張していない**。

## 6. 特徴標本：すべての $f\ge2$ での完成証明

非飽和の場合は §4 で $t_{\rm typ}\le D_f(r+1)v\theta$、ゆえに $\tau\le t_{\rm typ}$。飽和の場合は §5 で $\tau\le C_{f,r}v^2\theta^5$。前者の上界も後者の右辺以下（$D_f(r+1)\le C_{f,r}$、$v,\theta\ge1$）なので、すべての場合に $\tau\le C_{f,r}v^2\theta^5$。

原稿の型付き規則数評価 `C_s(G)` は fan-out $f$、rank $r$ の一般の場合として既に証明されており、$|\mathsf S^\sharp|=4$ を入れるだけで

\[
N_{\rm typ}(G,c)\le C_c(G)
=|V|4^f+|P|4^{fr}
\le\boxed{4^{fr}\|G\|}.
\]

原稿 `cor:distribution-representatives` は、$L\in\mathcal C_{f,c}$ に対して**両方の作用素** $\mathcal B^{\le r}_{f,c}$、$\mathcal B_{f,c}$ に共通の特徴標本 $K$ を与え、

\[
\|K\|_+\le N_{\rm typ}(1+2\theta+r\tau(G,c))
 +\mathbf1_{\{\varepsilon\in L\}}.
\]

$|V|=v\le\|G\|$、$1+2\theta\le3\|G\|^2\theta^5$ を代入すれば

\[
\boxed{\|K\|_+\le4^{fr}(3+rC_{f,r})\|G\|^3\theta^5
 +\mathbf1_{\{\varepsilon\in L\}}.}
\]

非飽和の場合はさらに $1+2\theta\le3\|G\|\theta$ を使うと

\[
\boxed{\|K\|_+\le4^{fr}[3+rD_f(r+1)]\|G\|^2\theta
 +\mathbf1_{\{\varepsilon\in L\}}.}
\]

これらは特徴標本の**総符号長** $\|K\|_+$ の存在上界。特徴標本の総数と、学習器の計算時間、Gold 収束時点は別の量である。

## 7. `main.tex` に置換できる LaTeX

以下は現行 `thm:two-letter-content`、`cor:two-letter-semilattice` に相当する**置換候補**。原稿の添字・作用素表記に合わせ、$r_{\max}$ を使用する。定理を採用する場合、付録H冒頭の $\mathcal C_{2,c}$ と `fan-out $\le2$`、各補題の仮定・証明を本報告 §2–§6 に沿って同時に変更する必要がある。**定理の文だけを差し替えてはならない**。

```latex
\begin{theorem}[Content typings on two letters at every fan-out at least two]
\label{thm:two-letter-content}
Let $\Sigma=\{\mathtt a,\mathtt b\}$, $c:=c_\Sigma$, $f\ge2$,
$r_{\max}\ge2$, and put
\[
 D_f:=(6f+1)3^f,\qquad
 C_{f,r_{\max}}:=(r_{\max}+1)
 \bigl(6r_{\max}(3f+1)+D_f\bigr).
\]
For every $L\in\Cmcf{f}{c}$ and every reduced good
fan-out-$\le f$, rank-$\le r_{\max}$ presentation $G$ of
$L\cap\Sigma^+$,
\[
 \tau(G,c)\le C_{f,r_{\max}}|V|^2\bar\theta_G^{\,5}.
\]
The operators $\mathcal B^{\le r_{\max}}_{f,c}$ and
$\mathcal B_{f,c}$ have a common characteristic sample $K$ with
\[
 \|K\|_+\le
 4^{fr_{\max}}(3+r_{\max}C_{f,r_{\max}})
 \|G\|^3\bar\theta_G^{\,5}
 +\mathbf 1_{\{\eps\in L\}}.
\]
If $L$ is not Parikh-saturated, then
\[
 t_{\mathrm{typ}}(G,c)\le
 D_f(r_{\max}+1)|V|\bar\theta_G,
\]
and one may take
\[
 \|K\|_+\le
 4^{fr_{\max}}\bigl(3+r_{\max}D_f(r_{\max}+1)\bigr)
 \|G\|^2\bar\theta_G
 +\mathbf 1_{\{\eps\in L\}}.
\]
All constants depend only on the fixed parameters $f,r_{\max}$.
\end{theorem}

\begin{corollary}[Semilattice typings on two letters at all higher fan-outs]
\label{cor:two-letter-semilattice}
Let $f\ge2$, $r_{\max}\ge2$, and let
$s:\{\mathtt a,\mathtt b\}^+\twoheadrightarrow\mathsf S$
be a typing with $\mathsf S\in\mathbf{SL}$, including $s_{U,2}$.
Then $s$ satisfies the condition of
Definition~\ref{def:uniform-polydata} at fan-out $f$
and rank $r_{\max}$.  For every $L\in\Cmcf{f}{s}$
and every reduced good fan-out-$\le f$,
rank-$\le r_{\max}$ presentation $G$ of $L\cap\Sigma^+$,
the characteristic-sample bounds of
Theorem~\ref{thm:two-letter-content} hold for the operators
$\mathcal B^{\le r_{\max}}_{f,s}$ and $\mathcal B_{f,s}$,
with $C_{f,r_{\max}}$ and $D_f$ as in that theorem.
\end{corollary}

\begin{proof}
Since $\mathsf S$ is a semilattice, $s(w)$ depends only on
$c_\Sigma(w)$, so $s\preceq c_\Sigma$.
Thus $\Cmcf{f}{s}\subseteq\Cmcf{f}{c_\Sigma}$.
Apply Theorem~\ref{thm:two-letter-content} to the content typing
and transfer the common characteristic sample to both
$s$-typed operators by Lemma~\ref{lem:typing-monotone}.
\end{proof}
```

**定理証明として付録に挿入する要約（既存の証明末尾の置換）**：非飽和では一般化した `prop:app-two-nonsaturated` により $\tau\le t_{\rm typ}\le D_f(r+1)v\theta$、飽和では一般化した `lem:app-two-saturated` により $\tau\le C_{f,r}v^2\theta^5$。$N_{\rm typ}\le4^{fr}\|G\|$ と代表長版特徴標本評価を結合すると上記2式を得る。**ただしこの要約は §2–§5 の新しい補題証明を代用しない**。

### 原稿の文言修正が必要な場所

- 付録H `Content Typings on Two Letters at Fan-Out Two` → `... at Every Fan-Out At Least Two`。冒頭の $\mathcal C_{2,c}$、fan-out $\le2$ を $\mathcal C_{f,c}$、fan-out $\le f$ に置き換える。
- 本文「Two letters」の定理名と、続く段落の `at fan-out two` を上記に合わせて修正。ただし fan-out one は引き続き未解決。
- §9 `op:fanout-two` は **三文字以上（または一般アルファベット）の fan-out 2 問題として残る**。二文字の部分が全 $f\ge2$ で肯定的に解決された旨を明記する。
- 原稿の §8「Reduction to semilattices」そのものの一般命題は変更不要。二文字の系だけ高次 $f$ に広げる。

### 付録Hに対する文単位の差替え対応表

| 現行ソースの行・箇所 | 現行の中心句 | 置換すべき主張 |
|---|---|---|
| 3105–3115 冒頭 | `L\in\Cmcf{2}{c}`、`fan-out $\le2$` | `L\in\Cmcf{f}{c}`、`fan-out $\le f$`、`fixed $f\ge2$`。 |
| 3229–3234 挿入補題仮定 | `arity $d\le2$`、`$|Q|\ge14$` | `arity $d\le f$`、`$|Q|\ge6f+2$`。 |
| 3238–3244 印 | `at most $8$ marks`、`$|Q_0|\ge6$` | `at most $4f$ marks`、`$|Q_0|\ge2f+2$`。 |
| 3259–3267 ブロックグラフ | `at most two blocks`、`maximum degree at most $4$`、`$|I|\ge|Q_0|/5$` | `at most $f$ blocks`、`maximum degree at most $2f$`、`$|I|\ge\lceil|Q_0|/(2f+1)\rceil\ge2$`。 |
| 3287–3305 非飽和命題 | `13`、`9v`、`117v`、`117(r+1)v\theta` | `6f+1`、`3^fv`、`(6f+1)3^fv`、`D_f(r+1)v\theta`。 |
| 3310–3312 飽和補題結論 | `(42r(r+1)+30(r+1))v^2\theta^5` | $C_{f,r}v^2\theta^5$（§5.3 の一括評価を使う）。 |
| 3330–3366 内容の和が $\Sigma$ | `both lie in $\{1,2\}$`、`$\theta+5$`、`$\theta+4$`、`30(r+1)` | `both lie in $\{1,\dots,f\}$`、`$\theta+2f+1$`、`$\theta+2f$`、`$A_f(r+1)$`。 |
| 3368–3370 純粋成分の入口 | `$h\in\{1,2\}$`、`$K>\theta+2$` | `$1\le h\le f$`、`$K>\theta+2(f-1)$`。小さい $K$ は別途直ちに評価。 |
| 3381–3386 (P2) | `false as $K>p+2$` | `false since $2(K-h+1)>p+K$ by $K>\theta+2(f-1)\ge p+2(h-1)$`。 |
| 3387–3390 (P3) | `greater than $\theta+1$`、`$g_u\ge2$` | `greater than $\theta+f-1$`、`$g_u\ge f$`。同名の比較可能節点は $K+\theta+(f-h)+1>p+K$ に矛盾。 |
| 3394–3401 (P4) | `$\ell_u\le K-2$`、`$g_u\le K-2\le K-h$` | `$\ell_u\le K-f$`、`$g_u\le K-f\le K-h$`。 |
| 3407–3421 (P5) | `$(r+1)(\theta+1)(2\theta+1)v\le6(r+1)v\theta^2$` | `$(r+1)(\theta+f-1)(2\theta+1)v\le3f(r+1)v\theta^2$`、非重い子の閾値も $\theta+f-1$。 |
| 3423–3431 (P6) | `$T_*\le7(r+1)v\theta^3$`、`$42r(r+1)+5$` | `$T_*\le(3f+1)(r+1)v\theta^3$`、`$6r(3f+1)(r+1)+5$`。 |
| 3432–3444 定理証明 | `117`、`$4^{2r}$`、`$C_r$` | `$D_f$`、`$4^{fr}$`、`$C_{f,r}$`。 |

上表の行番号は該当ブロックを探すための目安であり、**原稿の旧文を単純置換するだけで周囲のすべての数式が自動整合するという意味ではない**。変更箇所の完全な論証は §§2–6 に示した。

## 8. 障害・反例候補・先行研究に関する慎重な扱い

今回追跡した付録Hの証明には **$f\ge3$ 固有の未解決箇所は残らなかった**。ただし元の $f=2$ の (P3) をそのまま保持すると、同名の比較可能な純粋節点について

\[
(K-h+1)+(\theta+2)>p+K
\]

が $h\ge3$ では保証されない。これは旧証明の**実質的な障害**であって反例ではない。本報告は重さの閾値を $\ell>\theta+f-1$ に変更して克服した。また (P2) の旧仮定 $K>p+2$ は $h\ge3$ で三反復の排除に不足するため、$K>\theta+2(f-1)$ に強化した。

反例候補を報告する段階には至らない。なぜなら上記修正後は (P2)–(P6) を含め、提示した証明が閉じるからである。もし本主張を査読前に攻撃的に検証するなら、**同時置換で複数の不連続blockが作る内部runの独立性**（§3）と、**(P5) での heavy pure 階層の非比較性**（§5.2）を重点的に独立監査する価値がある。

既知性：[Clark–Eyraud (2007), JMLR 8, 1725–1745](https://jmlr.csail.mit.edu/beta/papers/v8/clark07a.html) はCFGの代入可能性に基づく正例学習、[Yoshinaka (2011), *Theoretical Computer Science* 412(19), 1821–1831](https://www.sciencedirect.com/science/article/pii/S0304397510007668) はMCFGの多次元代入可能性の基本枠組みを扱う。今回の**二文字内容型付けに限った全ファンアウトの明示的 $O_{f,r}(\|G\|^3\bar\theta_G^5)$ 上界**が既に同一の形で公刊されているかは、今回参照したソースおよび限定的な公開文献検索では**未確認**。従って「世界初」「先行研究に存在しない」等の主張はしない。またこの報告書は論文査読済みの証明ではないので、論文反映前には別個の検証を推奨する。

**計算実験：実施していない。** この報告の根拠は上記の組合せ論的・文法理論的証明であり、有限のテスト結果を定理の根拠としていない。

---

## 付記：到達した結果と限界

- **証明できた範囲**：任意の固定 $f\ge2$、固定 $r\ge2$、二文字内容型付け $c_\Sigma$、$L\in\mathcal C_{f,c_\Sigma}$、任意の reduced good $\le f$-MCFG・rank $\le r$ 表示 $G$ に対して、上記の代表長・特徴標本長上界。二文字のすべての有限半束型付けにも移行可。
- **証明していない範囲**：$f=1$、三文字以上の内容型付け、一般の有限半群型付け、$f$ を変数とした多項式時間・多項式データの一様性、全てのGold学習器の収束時間。
- **採用時の要注意点**：$t_{\rm typ}$ の線形上界は**非飽和時だけ**。飽和時は代わりに $\tau$ を直接評価する。特徴標本の存在は原稿 `cor:distribution-representatives` と `lem:typing-monotone` への依存を明示する。

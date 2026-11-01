# 付録 H「Content Typings on Two Letters at Fan-Out Two」独立査読報告

**査読日**: 2026-11-01
**対象**: `main_latest.tex`（`02-v2-lg-fanout-boundary/main.tex` と同一の行番号。以下、行番号はこのファイルによる）
**範囲**: §2–§4 の定義（型付け、$C_{f,s}$、許容文脈、型付き非終端 $X=A_{\mathbf t}$、$\widetilde G_0$、$L_X$、$\mathrm{Cl}_{L,s}(X)$）、`lem:typed-homogeneity`、`lem:thickness-equivalence`、`lem:witness-length-template`(i)、`thm:data-from-typed-thickness`、`cor:distribution-representatives`、$C_s(G)$、§8 の "Two letters"、付録 H 全体（`lem:app-two-basic`–定理の証明）、および要旨・序論・`op:S1`・`op:fanout-two` の記述。
**方法**: 各行の論理を手で追い、必要に応じて代数を展開し、Python 3（標準ライブラリのみ）で有限言語・不等式・小さな文法を全数検査した。有限の検査は「観察」であり、証明の代わりではない。特定の反例が見つかればそれ自体が証明になるが、今回は見つからなかった。

---

## 1. 判定の表

| # | 補題・項目 | 判定 | 問題の箇所と理由 | 直し方の提案 |
|---|---|---|---|---|
| 1 | `lem:app-two-basic`(i)（3139–3143 行） | 正しい | なし。$E_A$ が $u$ と $z$ の共通文脈になり、$(2,c)$-代入可能性で分布が一致する。逆方向も $E_A\in\mathcal D_L(z)$ から従う。 | なし。 |
| 2 | `lem:app-two-basic`(ii)（3145–3153 行） | 正しい | なし。Parikh 差が非負の和（経路上の終端＋兄弟の生成組）で、零なら消える。nondeletion/nonpermutation/nonmerging/$\lambda$-free で各成分は一変数、fan-out 一致、恒等。 | なし。 |
| 3 | `lem:app-two-runs`(i)（3171–3183 行） | 正しい | なし。$Z\ne\varepsilon$、文脈 $U\square_1Z\square_2V$ は許容的。1 単位移動で組成のグラフが連結。左右どちらの向きも対称に動く。 | なし。 |
| 4 | `lem:app-two-runs`(ii)（3185–3189 行） | 正しい | なし。$UxxyxV$ から (i) で $UxyxxV$、1 穴文脈 $Ux\square xV$ が $xy$ と $yx$ を受理し、両方内容 $\Sigma$。隣接交換で Parikh 飽和。 | なし。 |
| 5 | `lem:app-two-runs`(iii)（3191–3194 行） | 正しい | なし。$xx$ があるので spare $x$ があり、内部 $y$ 塊の直前の $x$ 塊へ移すと $xxyx$。 | なし。 |
| 6 | `lem:app-two-runs`(iv)（3196–3208 行） | 正しい | なし。$e,e'\ge2$、spare $x$ から $R$ を 2 と 1 にした $W_2,W_1$ が存在。文脈 $(U,xV')$ と $(U_1,y^{e'}V_1)$ で $y^{e+e'}$ が出る。 | なし。 |
| 7 | `lem:app-two-alternate`（3217–3225 行） | 正しい | なし。4 個以上の run なら第 2・第 3 run が内部で異文字。各 $y$ で内部 $y$ 塊を長さ 1 に再配分でき、$x$ 塊は不変。 | なし。 |
| 8 | `lem:app-two-insertion`(a)（3240–3258 行） | 正しい | なし。印は $\le8$、$|Q_0|\ge6$。単独差し替えで総長が減り、純成分が純のままなら `lem:witness-length-template`(i)（$\lambda=\widehat c$）で $L_X$ に入り矛盾。よって他の文字が純成分の内部 block に入り、長さ $\ge5$。 | なし。 |
| 9 | `lem:app-two-insertion`(b)（3260–3277 行） | 正しい（説明の補足を推奨） | 数学的には正しい。ただし「gap is nonempty or contains a block of an owner outside $I$」は、gap に別の $I$-block が入る場合を明示していない。また「both $a^5$ and $b^5$ occur by (a)」は (a) を $h_1,h_2$ にそれぞれ適用する意味。 | 連続する $I$-block の間には必ず $x$ がある、と一文補う。different-letter の場合は「(a) を $h_1$ と $h_2$ に適用して」と書く。 |
| 10 | `prop:app-two-nonsaturated`（3285–3303 行） | 正しい | なし。3 場合（両方なし／両方あり／片方だけ）で矛盾。型付きラベル $\le9v$、パスで反復なし、重い節点 $\le117v$、長さ $\le117(r+1)v\theta$。 | なし。 |
| 11 | `lem:app-two-saturated`（合併が $\Sigma$ の場合、3311–3352 行） | 修正が必要（軽微） | 3345 行の $\lfloor(p+n)/(n-t+1)\rfloor\le p+t$ の根拠として「$(n-t)(t-1)\ge0$」とあるが、差の式は $(p+t)(n-t+1)-(p+n)=(n-t)(p+t-1)$ であり、$(n-t)(t-1)$ ではない。不等式自体は正しい。 | 根拠を「$p+t-1\ge0$ より $(p+n)/(n-t+1)=1+(p+t-1)/(n-t+1)\le p+t$」に直す。 |
| 12 | `lem:app-two-saturated`（全成分 $\{a\}$ の場合、3354–3428 行） | 正しい | なし。(P1) の代入可能性は $a$ と $a^{1+\delta}$（ともに内容 $\{a\}$）の 1 穴比較だけ。(P2)–(P6) の数え上げ・不等式も整合。 | なし。 |
| 13 | 定理の証明（3431–3442 行） | 修正が必要（軽微） | 3440 行の「$1+2\theta\le3\lVert G\rVert^2\theta\le3\lVert G\rVert^2\theta^5$」は第 1 上界には使えるが、第 2 上界（$\lVert G\rVert^2\theta$）には余分な $\lVert G\rVert$ が残る。第 2 上界には鋭い $1+2\theta\le3\theta$ を使う必要がある。定理の主張自体は正しい。 | 「第 1 上界には $1+2\theta\le3\lVert G\rVert^2\theta^5$、第 2 上界には $1+2\theta\le3\theta\le3\lVert G\rVert\theta$ を使う」と場合を分けて書く。 |
| 14 | `cor:two-letter-semilattice`（1959–1963 行） | 正しい | なし。$s\preceq c$、$\mathcal C_{2,s}\subseteq\mathcal C_{2,c}$、`lem:typing-monotone` の向き（$c$ の特徴標本は $s$ の特徴標本）も正しい。 | なし。 |
| 15 | 要旨・序論・§8 の説明・`op:S1`・`op:fanout-two` | 正しい（範囲内） | なし。「二文字では多項式、三文字以上は未解決」「境界がファンアウトで動くとは言わない」の範囲に収まっている。 | なし。 |

**総括**: 定理・補題の主張に反例はなく、数学的内容は正しいと判断する。証明の記述として修正が必要なのは、上の #11 の不等式の根拠の式と、#13 の第 2 上界の算術の書き方の 2 箇所（いずれも軽微）。#9 は説明の補足を推奨する。

---

## 2. 各補題の行単位の検討

### 2.1 `lem:app-two-basic`（3126–3154 行）

#### (i)（3139–3143 行）

主張は
\[
\mathrm{Cl}_{L,c}(X)=\{\mathbf z\in(\Sigma^+)^d:\ c^{(d)}(\mathbf z)=\mathbf t,\ E_A[\mathbf z]\in L\}.
\]

- $u\in L_X$ を固定する。`lem:typed-homogeneity` により、$\mathrm{Cl}_{L,c}(X)$ は「$u$ と同じ型と同じ分布を持つ $\mathbf z$」全体である。$E_A[L_A(G)]\subseteq L$ かつ $L_X\subseteq L_A(G)$ なので $E_A\in\mathcal D_L(u)$。
- $\mathbf z$ が型 $\mathbf t$ で $E_A[\mathbf z]\in L$ なら、$E_A\in\mathcal D_L(\mathbf z)\cap\mathcal D_L(u)$。$d\le2$ なので $(2,c)$-代入可能性が使え、$\mathcal D_L(\mathbf z)=\mathcal D_L(u)$、すなわち $\mathbf z\in\mathrm{Cl}$。
- 逆に $\mathbf z\in\mathrm{Cl}$ なら $E_A\in\mathcal D_L(\mathbf z)$、つまり $E_A[\mathbf z]\in L$。
- よって等式が従う。$\tau_X$ が「そのような $\mathbf z$ の最小総長」であることも定義どおり。

**判定: 正しい。** 特に、$E_A$ が $u$ と $\mathbf z$ の共通の許容文脈になる点、および $d\le2$ で $(2,c)$ が使える点が正しく押さえられている。

#### (ii)（3145–3153 行）

- $u$ を $u'$ の真の祖先とし、$\Psi(u)=\Psi(u')$ とする。nondeletion と linearity により、$u'$ の生成組の各文字は $u$ の生成組に一度ずつ現れる。差は「経路上の規則が書く終端」と「経路から外れた兄弟の生成組」の非負和。Parikh ベクトルが等しいので差は零、したがって経路上に終端はなく、兄弟も存在しない。
- よって経路上の各規則は rank 1、子は 1 つ。nondeletion で各変数は一度、nonpermutation で順序どおり、$\lambda$-free で各成分は非空。
- 1 成分に 2 変数が入ると、その 2 変数は（終端がないので）隣接し、nonpermutation により $\xi^\kappa,\xi^{\kappa+1}$ の形になる。nonmerging がこれを禁ずる。よって各成分は 1 変数で、fan-out が一致し、規則は成分ごとの恒等。
- 差し替えで同じ tuple が得られ、節点は少なくとも 1 個減る。

**判定: 正しい。** 兄弟の生成組が非空であることは $\lambda$-free と reduced から従う。$u'$ の生成組が $u$ の生成組の「部分 tuple」であること（各成分が順序を保つ部分語）も nonpermutation/nondeletion から従う。

---

### 2.2 `lem:app-two-runs`（3156–3209 行）

#### (i)（3171–3183 行）

- $px^4q\in L$ を取る。$(x,xx)$ と $(xx,x)$ はともに型 $(\{x\},\{x\})$。文脈 $p\square_1x\square_2q$ は許容的（中間の $x$ が非空）で、両方を受理する。$(2,c)$-代入可能性より $\mathcal D_L(x,xx)=\mathcal D_L(xx,x)$。
- $R,R'$ を $x$-run とし、$|R|\ge2$、$R'$ が $R$ の左にあるとする。$w=U\,x\,Z\,xx\,V$ と書く。ここで最初の $x$ は $R'$ の最後の文字、$xx$ は $R$ の最初の 2 文字、$Z$ は 2 つの run の間の因子。$R'\ne R$ なので $Z\ne\varepsilon$。
- 文脈 $E=U\square_1Z\square_2V$ は許容的。$E[(x,xx)]=w$。分布が等しいので $E[(xx,x)]=U\,xx\,Z\,x\,V\in L$ も成り立つ。これは $R$ から $R'$ へ $x$ を 1 個移した語で、$x$-skeleton と $x$ の個数を保つ。
- $R'$ が $R$ の右にある場合は、$xx$ を $R$（左）の最初の 2 文字、$x$ を $R'$（右）の最後の文字にして、文脈 $U\square_1Z\square_2V$ が $(xx,x)$ と $(x,xx)$ を受理する。同じ分布の等式で逆向きの移動ができる。
- $x$-skeleton が同じ語は $x$-run の個数 $\rho$ が同じで、run の長さは $|w|_x$ の $\rho$ 個の正の整数への分割。任意の 2 つの分割は「大きさ $\ge2$ の部分から他の部分へ 1 単位移す」操作で連結する（すべての余剰を第 1 成分に集めればよい）。

**判定: 正しい。** 特に $Z\ne\varepsilon$ が文脈の許容性に必要で、$R'$ と $R$ が隣接しない場合も $Z$ は他の run を含むので非空。左右の向きの対称性も上のとおり。

#### (ii)（3185–3189 行）

- $UxxyxV\in L$ とする（$UxyxxV$ も対称）。$UxxyxV$ と $UxyxxV$ は同じ $x$-skeleton（$Ux y xV$）と同じ $x$ の個数（3）を持つので、(i) より $UxyxxV\in L$。
- 1 穴文脈 $Ux\square xV$ は $xy$ と $yx$ を受理する：$Ux\,xy\,xV=UxxyxV$、$Ux\,yx\,xV=UxyxxV$。両方の内容は $\Sigma$。$(1,c)$-代入可能性より $\mathcal D_L(xy)=\mathcal D_L(yx)$（1 次元分布）。
- したがって任意の文脈で隣接する $xy$ を $yx$ に（および逆に）置き換えてよい。隣接交換で同じ Parikh ベクトルを持つ語はすべて互いに移れるので、$L$ は Parikh 飽和。

**判定: 正しい。** ここで使うのは 1 穴文脈（$Ux\square xV$）であって 2 穴文脈ではない。$xy,yx$ の内容がともに $\Sigma$ である点も正しい。

#### (iii)（3191–3194 行）

- $w\in L$ が $xx$ を含み、内部 $y$-run で長さ 1 のものを持つとする。$xx$ があるので $w$ には spare $x$ がある（$|w|_x>$ $x$-run の個数）。
- その $y$-run の直前の $x$-run を $A$ とする。$A$ がすでに長さ $\ge2$ なら $w$ 自身が $xxyx$ を含む。$A$ が長さ 1 なら、spare $x$ を他の $x$-run から $A$ へ (i) で移す。$y$-run は内部なので、その次は $x$。よって得られた語は $xxyx$ を含む。
- (ii) より $L$ は Parikh 飽和。$\square$

**判定: 正しい。** $A$ が長さ 1 で、長さ $\ge2$ の $x$-run が $A$ 自身しかない場合は、$A$ が長さ $\ge2$ の場合に吸収される。spare $x$ の移動は (i) の範囲内。

#### (iv)（3196–3208 行）

- $w\in L$ が $xx$ を含み、内部 $y$-run を 2 つ持つとする。そのうち連続する 2 つを $y^e,y^{e'}$ とし、間の $x$-run を $R$、$y^e$ の直前の $x$-run を $A_0$ とする。
- (iii) より $e,e'\ge2$。
- $w$ は $xx$ を含むので spare $x$ がある。$x$-run の個数を $\rho$、$x$ の個数を $n$ とすると $n\ge\rho+1$。
  - $R$ を長さ 2 にする：他の $\rho-1$ 個の run を 1 以上にして $R=2$ にするには $n-2\ge\rho-1$、つまり $n\ge\rho+1$。可能。
  - $R$ を長さ 1 にする：$n-1\ge\rho-1$、つまり $n\ge\rho$。可能。
  - よって (i) により、$W_2=U\,x\,y^e\,xx\,V'$ と $W_1=U_1\,x\,y^e\,x\,y^{e'}V_1$ がともに $L$ に入る。$x$-skeleton と $x$ の個数は $w$ と同じ。
- 文脈 $E=U\square\,xV'$ は $xy^ex$ と $xxy^e$ を受理する：
  - $E[xy^ex]=U\,xy^ex\,xV'=U\,x\,y^e\,x\,x\,V'=W_2$。
  - $E[xxy^e]=U\,xxy^e\,xV'=U\,xx\,y^e\,x\,V'$。
  両方の内容は $\Sigma$ なので、$(1,c)$-代入可能性より $\mathcal D_L(xy^ex)=\mathcal D_L(xxy^e)$。
- 文脈 $E'=U_1\square\,y^{e'}V_1$ は $xy^ex$ を受理する：$E'[xy^ex]=U_1\,x\,y^e\,x\,y^{e'}V_1=W_1$。分布が等しいので $E'[xxy^e]=U_1\,xx\,y^e\,y^{e'}V_1=U_1\,xx\,y^{e+e'}V_1\in L$。
- $e+e'\ge4$ なので $y^4$ が現れ、矛盾。

**判定: 正しい。** 特に、$W_2$ と $W_1$ の存在は「spare $x$ があること」から正しく従う。$R$ を 1 または 2 に固定しても他の run を正にできる。$y^{e+e'}$ が因子として現れることも、文脈 $E'$ の定義から正しい。$E[xxy^e]$ が $L$ に入る理由は、分布の等式でも (i) でもよい（本文は両方を書いている）。

---

### 2.3 `lem:app-two-alternate`（3211–3226 行）

- $w\in L$ が 4 個以上の run を持つ。第 2・第 3 run は内部で、異なる文字。よって各文字 $y$ について、$w$ は内部 $y$-run $\beta$ を持ち、$y$-run を少なくとも 2 つ持つ。
- 各 $y$ について、$y^4$ が現れる（仮定）ので (i) が使える。$\beta$ から別の $y$-run へ $y$ を移して $\beta$ の長さを 1 にできる。この操作は $x$-run を変えない（$x$-run は同じ因子として残る）。
- もし $w$ の $x$-run に長さ $\ge2$ のものがあれば、得られた語は $xx$ を含み、内部 $y$-run の長さ 1 を持つ。これは (iii) に反する。
- よってすべての $x$-run は長さ 1。$x$ は両方の文字でよいので、すべての run が長さ 1。

**判定: 正しい。** $\beta$ がすでに長さ 1 なら操作は不要。長さ $\ge2$ なら spare $y$ があり、別の $y$-run が存在する。$x$-run が「同じ因子として残る」ことも正しい。

---

### 2.4 `lem:app-two-insertion`（3228–3278 行）

#### (a)（3240–3258 行）

- 純成分（内容 $\{x\}$）の最初と最後の $\min\{2,|u_i|\}$ 文字、内容 $\Sigma$ の成分の $a$ と $b$ を 1 つずつ印にする。$d\le2$ で、両方の成分が純なら $4+4=8$、片方が純で片方が混合なら $4+2=6$、両方が混合なら $2+2=4$。よって印は高々 8 個。
- 各印は 1 つの節点が書く。$Q$ の節点の部分木は互いに素なので、印を書く $Q$-節点は高々 8 個。よって $|Q_0|\ge|Q|-8\ge6$。
- $h\in Q_0$ を取り、型添字を消して $h$ の部分木を $\omega_{C_h}$ の導出に差し替える。nondeletion により $h$ の生成組の各文字は $u$ に現れ、$\|\omega_{C_h}\|_1\le\theta<\ell_h$ なので新しい根 tuple は $L_A(G)$ に入り、総長が減る。
- 内容 $\Sigma$ の成分では、印の $a$ と $b$ が $h$ の部分木の外にあるので、差し替え後も内容 $\Sigma$ のまま。
- すべての純成分が純のまま（同じ内容 $\{x\}$）なら、新しい tuple は型 $\mathbf t$ を持ち、$\widehat c$-vector が $u$ と一致する。`lem:witness-length-template`(i) を $\lambda=\widehat c$ で使うと新しい tuple は $L_X$ に入る。しかし総長が減るので、$T$ の最小性に反する。
- よってある純成分で内容が $\{x\}$ から $\Sigma$ に変わる。$h$ の block（根成分のうち $h$ の生成組の 1 成分が占める区間）がその純成分の中にあり、他の文字を含む。
- $h\in Q_0$ なので block は印を含まない。純成分の印は最初の 2 文字と最後の 2 文字なので、block はその間（位置 $3$ から $n-2$）にあり、成分の長さは $\ge5$。
- よって $u$ のある成分は内容 $\{x\}$ で長さ $\ge5$、つまり $x^5$ が $E_A[u]\in L$ に現れる。これが (a)。

**判定: 正しい。** 特に「純成分が純のまま」というとき、内容が $\{y\}$ に変わることはない（印の $x$ が両端に残るので、成分は $x$ を含む）。この点は本文で明示されていないが、印の議論から従う。

#### (b)（3260–3277 行）

- 各 $h\in Q_0$ は高々 2 つの block を持つ（arity $\le2$）。同じ根成分で block が文字を挟まず隣接するとき、持ち主同士を辺で結ぶ。各 block は高々 2 つの隣接 block を持つので、持ち主のグラフの最大次数は $\le4$。独立集合 $I$ で $|I|\ge|Q_0|/5\ge6/5$、整数なので $|I|\ge2$。
- $I$ の部分木を同時に差し替える。$I$ は反鎖なので差し替えは独立で、$u'\in L_A(G)$、$W=E_A[u']\in L$。
- 純成分内で、$I$ の異なる持ち主の block の間には必ず $x$ がある：隣接していればグラフの辺になり $I$ の独立性に反する。隣接していなければ、間の文字は $x$（純成分）か、$I$ 外の持ち主の block（差し替えないので $x$ のみ）である。間に別の $I$-block がある場合は、連続する $I$-block に分けて同じ議論を繰り返す。よって異なる持ち主の作る $y$-run は distinct。
- 各 $h\in I$ は、自分の block の中に他の文字 $y$ の run を少なくとも 1 つ作り、それは前後を $x_h$ で挟まれる。純成分の最初の 2 文字と最後の 2 文字は印なので、$I$ の block に含まれず、残る。
- $h_1\ne h_2\in I$ を取る。
  - $x_{h_1}=x_{h_2}=:x$ なら、$W$ は $xx$（長さ $\ge5$ の純成分の最初の 2 文字）を含み、内部 $y$-run を 2 つ持つ。よって run は 5 個以上。
  - $x_{h_1}\ne x_{h_2}$ なら、$a^5$ と $b^5$ がともに現れる（(a) を $h_1,h_2$ に適用）。$x:=x_{h_1}$、$y:=x_{h_2}$ とすると、2 つの純成分に $x,y,x$ と $y,x,y$ の run が現れる。2 成分は異なる文字なので、境界で同じ文字の run が融合することはなく、6 個の distinct な run。$W$ は $xx$ も含む。

**判定: 正しい（説明の補足を推奨）。** 数学的な穴はない。ただし、次の 2 点は文章を補うとよい。

1. 3266–3267 行の「their gap is nonempty or contains a block of an owner outside $I$」は、gap に別の $I$-block が入る場合を明示していない。連続する $I$-block の間には必ず $x$ がある、と一文補えば十分。
2. 3274–3275 行の「both $\mathtt a^5$ and $\mathtt b^5$ occur by (a)」は、(a) を $h_1$ と $h_2$ にそれぞれ適用する意味。$h_1$ の純成分は $x_{h_1}$、$h_2$ の純成分は $x_{h_2}$ で、$x_{h_1}\ne x_{h_2}$ なので両方の 5 乗が出る。

---

### 2.5 `prop:app-two-nonsaturated`（3280–3304 行）

- $X$ と $T$ を挿入補題のとおりに取る。重い節点の反鎖が 14 個以上あれば挿入補題が使える。
- 場合分け：
  - $a^4$ も $b^4$ も現れない：(a) の $x^5$ は $x^4$ を含むので不可能。
  - 両方現れる：(b) の $W$ は 4 個以上の run と $xx$（長さ $\ge2$ の run）を持つ。`lem:app-two-alternate` は「4 個以上の run を持つすべての語のすべての run が長さ 1」を言うので矛盾。
  - 片方だけ、例えば $x_0^4$ だけ現れる：(a) より $x=x_0$。$y^5$ は現れない（現れれば $y^4$ が現れる）。(b) の「両方の 5 乗が現れない限り 2 つの内部 $y$-run」により $W$ は $xx$ と 2 つの内部 $y$-run を持つ。`lem:app-two-runs`(iv)（$y^4$ が現れない）に矛盾。
- よって重い節点の反鎖は高々 13 個。
- 型付きラベルは (非終端, 各成分の内容)。成分の内容は $\{a\},\{b\},\{a,b\}$ の 3 通り、arity $\le2$ なので高々 $3^2=9$ 通り/非終端、全体で $\le9v$。
- パス上で型付きラベルが反復しない：同じラベルの祖先 $u$ と子孫 $u'$ があれば、$u$ の部分木を $u'$ の部分木で置き換える。型付きラベルが同じなので型付き導出として valid で、根の型は $\mathbf t$ のまま。生成組は長くならず（$u'$ の生成組は $u$ の生成組の部分 tuple）、節点は減る。これは $T$ の最小性（総長最小、次に節点数最小）に反する。よってパスは $\le9v$ 節点。
- 重い節点は祖先について閉じ、同じ深さでは反鎖。深さは $\le9v$、各深さの重い節点は $\le13$。よって重い節点は $\le13\cdot9v=117v$。
- 根が重くなければ $\|u\|_1\le\theta$。根が重ければ、各文字は重い節点が直接書くか、その軽い子（$\le r$ 個、各総長 $\le\theta$）の生成組に属する。重い節点は $\le117v$ 個なので
  \[
  \|u\|_1\le117v\cdot\theta+117v\cdot r\theta=117(r+1)v\theta.
  \]
- よって $t_{\mathrm{typ}}(G,c)=\max_X\min_{u\in L_X}\|u\|_1\le117(r+1)v\theta$。

**判定: 正しい。** 型付きラベルの置き換えが「型付き導出として valid」である点は、ラベルが同じなので直接言える（`lem:app-two-basic`(ii) の Parikh の場合と違って、unique lifting を持ち出す必要はない）。重い節点の数え上げも正しい。

---

### 2.6 `lem:app-two-saturated`（3306–3429 行）

#### 準備（3311–3322 行）

- $X=A_{\mathbf t}$、$(p,q)=\Psi(E_A)$、$\mathcal P=\Psi(L\cap\Sigma^+)$。
- `lem:app-two-basic`(i) と Parikh 飽和性より
  \[
  \tau_X=\min\{\|\mathbf z\|_1:\ c^{(d)}(\mathbf z)=\mathbf t,\ (p,q)+\textstyle\sum_i\Psi(z_i)\in\mathcal P\}.
  \]
  これは正しい。$E_A[\mathbf z]$ の Parikh ベクトルが $(p,q)+\sum_i\Psi(z_i)$ で、飽和性より所属は Parikh ベクトルだけで決まる。
- ノード $u$ の生成組の Parikh ベクトル $(a_u,b_u)$、$\omega_B$ の $(x_B,y_B)$。部分木の差し替えで Parikh ベクトルが
  \[
  \Psi(w)-(a_u,b_u)+(x_B,y_B),\qquad
  \Psi(w)-(a_u-a_{u'},b_u-b_{u'})
  \]
  になる、という計算も正しい。

#### 合併が $\Sigma$ の場合（3324–3352 行）

- $t_a,t_b$ を $a,b$ を含む成分の個数とすると、$1\le t_a,t_b\le2$。型 $\mathbf t$ で $n_a$ 個の $a$、$n_b$ 個の $b$ を持つ tuple が存在する条件は $n_a\ge t_a$ かつ $n_b\ge t_b$。合併が $\Sigma$ なので各文字を要求する成分が少なくとも 1 つあり、余りはその文字を許す成分に自由に入れられる。正しい。
- $\tau_X$ は $n_a+n_b$ の最小値（条件付き）。最小対 $(n_a,n_b)$ を固定し、$c_a=n_a-t_a+1$、$c_b=n_b-t_b+1$。
- 重い節点 $u$ で $a_u<c_a$ かつ $b_u<c_b$ なら、$\omega_{B_u}$ に差し替えると新しい個数は
  \[
  n'_a=n_a-a_u+x_B\ge n_a-a_u\ge t_a,\qquad
  n'_b=n_b-b_u+y_B\ge t_b,
  \]
  かつ $n'_a+n'_b<n_a+n_b$（$a_u+b_u>\theta\ge x_B+y_B$）。これは $(n_a,n_b)$ の最小性に反する。よって重い節点は $a_u\ge c_a$ または $b_u\ge c_b$。
- 同じ非終端の祖先 $u$ と子孫 $u'$ で、$\Delta a=a_u-a_{u'}$、$\Delta b=b_u-b_{u'}$ とする。$\Delta a<c_a$ かつ $\Delta b<c_b$ なら、差し替えで新しい個数 $n_a-\Delta a\ge t_a$、$n_b-\Delta b\ge t_b$、総長は減る（$\Delta a+\Delta b>0$ の場合）か、$\Delta a=\Delta b=0$ で `lem:app-two-basic`(ii) により同じ語を少ない節点で導出できる。どちらも矛盾。よって $\Delta a\ge c_a$ または $\Delta b\ge c_b$。
- パス上で $(\lfloor a_u/c_a\rfloor,\lfloor b_u/c_b\rfloor)$ は成分ごとに非増加。値が一定の間は同じ非終端が反復しない（上の $\Delta$ の議論）。よって各値についてパスは $\le v$ 節点。
- 値の個数：$a_u\le p+n_a$、$b_u\le q+n_b$ なので
  \[
  \lfloor a_u/c_a\rfloor\le\left\lfloor\frac{p+n_a}{n_a-t_a+1}\right\rfloor\le p+t_a,
  \quad
  \lfloor b_u/c_b\rfloor\le q+t_b.
  \]
  ここで
  \[
  \frac{p+n}{n-t+1}=1+\frac{p+t-1}{n-t+1}\le p+t
  \]
  を使う（$p+t-1\ge0$、$n-t+1\ge1$）。よって値は高々 $1+(p+t_a)+(q+t_b)\le\theta+5$ 個。パスは $\le v(\theta+5)$ 節点。
- 同じ深さの重い節点の生成組は互いに素。$a_u\ge c_a$ の節点の $a$ の総数は $\le p+n_a$、$b_u\ge c_b$ の節点の $b$ の総数は $\le q+n_b$。よって同じ深さの重い節点は
  \[
  \le\frac{p+n_a}{c_a}+\frac{q+n_b}{c_b}\le p+t_a+q+t_b\le\theta+4.
  \]
- 重い節点は祖先について閉じ、深さは $\le v(\theta+5)$。よって重い節点は $\le(\theta+4)v(\theta+5)$。
- 根が軽ければ $|W|\le\theta$。重ければ、各文字は重い節点が直接書くか、その軽い子（$\le r$ 個、各 $\le\theta$）に属する。よって
  \[
  \tau_X\le|W|\le(r+1)\theta\cdot(\theta+4)v(\theta+5)
  \le30(r+1)v\theta^3.
  \]
  ここで $(\theta+4)(\theta+5)\le30\theta^2$（$\theta\ge1$）を使う。正しい。

**問題点**: 3345 行の「(as $(n-t)(t-1)\ge0$)」は、差の式が違う。実際、
\[
(p+t)(n-t+1)-(p+n)=(n-t)(p+t-1)
\]
であり、$(n-t)(t-1)$ ではない。例えば $p=5,n=3,t=1$ では実際の差は $10$、$(n-t)(t-1)=0$。不等式自体は $p+t-1\ge0$ から正しい。**修正: 根拠を $(n-t)(p+t-1)\ge0$ に直す。**

#### 全成分が $\{a\}$ の場合（3354–3428 行）

- 成分数を $h:=d\in\{1,2\}$。$K:=\min\{k\ge h:(p+k,q)\in\mathcal P\}$ とすると $\tau_X=K$。$K\le\theta+2$ なら $\tau_X=K\le\theta+2\le(42r(r+1)+30(r+1))v^2\theta^5$ なので、$K>\theta+2\ge p+2$ としてよい。
- $W=b^q a^{p+K}\in L$ の節点数最小の導出 $T$ を取る。
- **(P1) 行剛性**: $(c_0,y),(c_0+\delta,y)\in\mathcal P$、$c_0\ge1$、$1\le\delta\le K-h$ とすると、文脈 $b^y a^{c_0-1}\square$ が $a$ と $a^{1+\delta}$ を受理する。両方の内容は $\{a\}$ なので $(1,c)$-代入可能性より $\mathcal D_L(a)=\mathcal D_L(a^{1+\delta})$。文脈 $b^q a^{p+K-\delta-1}\square$ は $a^{1+\delta}$ を受理して $W$ を与えるので、$a$ も受理し、$(p+K-\delta,q)\in\mathcal P$ で $h\le K-\delta<K$。これは $K$ の最小性に反する。正しい。
- **(P2) 高さ**: 同じ非終端の祖先 $u$ と子孫 $u'$ で $b_u=b_{u'}$ なら、$\Delta a=a_u-a_{u'}$。$\Delta a=0$ は `lem:app-two-basic`(ii) で節点最小性に反する。$1\le\Delta a\le K-h$ なら、差し替えで $(p+K-\Delta a,q)\in\mathcal P$、$K-\Delta a\ge h$、$K-\Delta a<K$ で $K$ の最小性に反する。よって $\Delta a\ge K-h+1$。
  - パス上で $b_u$ は $q+1$ 通りの値。同じ非終端・同じ $b_u$ の値の節点が 3 個あると、$a_u\ge2(K-h+1)$、一方 $a_u\le p+K$。$K>p+2$ より $p+K<2(K-h+1)$（$h\le2$）なので矛盾。よって同じ（非終端, $b$ 値）はパス上で高々 2 個。パスは $\le2v(q+1)$ 節点。
  - $b$ を含む節点（mixed）は、$q$ 個の $b$ を書く節点へのパス上にある。よって $M\le2vq(q+1)\le4v\theta^2$。
- **(P3) 重い純節点**: $b$ を含まず $\ell_u=a_u>\theta+1$ の節点を重い純節点、$g_u=\ell_u-x_{B_u}\ge2$ とする。同じ非終端の重い純節点が比較可能なら、上側は (P2) より $\ell_u\ge K-h+1+\theta+2>p+K$、矛盾。よって同じ非終端の重い純節点は反鎖で、生成組は互いに素。
  - 反鎖 $J$ を一括差し替えすると、$a$ は $\sigma(J)=\sum g_u$ 減り、$b$ は $Y(J)=\sum y_{B_u}$ 増える。$(p+K-\sigma(J),q+Y(J))\in\mathcal P$。
  - $\sigma(J),\sigma(J')\le K-h$、$Y(J)=Y(J')$ なら、$a$ の個数は $p+K-\sigma$ と $p+K-\sigma'$ で、どちらも $\ge p+h\ge1$。$\sigma<\sigma'$ とすると (P1) に反する。よって $\sigma=\sigma'$。
- **(P4) 反復ラベルと比**: 同じ $B$ の重い純節点が $m_B\ge2$ 個あれば、生成組は互いに素で、各 $\ell_u\le p+K-(\theta+2)\le K-2$、$g_u\le K-2\le K-h$。2 つの singleton を (P3) で比較すると $g_B$ が共通、$\ell_B=x_B+g_B$ も共通。
  - $y_B=0$ なら 1 回の差し替えで $(p+K-g_B,q)\in\mathcal P$、$h\le K-g_B<K$、矛盾。よって $y_B\ge1$。
  - $m_B>\theta$ の $B$ を frequent と呼ぶ。frequent $B,C$ について、$y_C$ 個の $B$ 節点と $y_B$ 個の $C$ 節点を取る（$m_B>\theta\ge y_C$、$m_C>\theta\ge y_B$）。両方とも反鎖で $Y=y_By_C$、$\sigma$ は $\le K-h$。よって (P3) より $y_Cg_B=y_Bg_C$。したがってすべての frequent $B$ で $g_B/y_B=\alpha$ が共通。$\ell_B=x_B+\alpha y_B\le(1+\alpha)\theta$。
- **(P5) 比の上界**: $\alpha_*=(r+1)(\theta+1)(2\theta+1)v\le6(r+1)v\theta^2$。$\alpha\le\theta$ なら $\alpha\le\alpha_*$。$\alpha>\theta$ なら frequent $B$ の重い純節点 $u$ を取る。
  - $u$ の部分木の重い純節点は祖先について閉じる。各重い純節点は $\le\theta$ 文字を直接書き、重くない子を $\le r$ 個持ち、その子の総長は $\le\theta+1$。よって $\ell_B\le(r+1)(\theta+1)H_u$。
  - 重い純節点を「その部分木内の重い純節点の proper ancestor の数」でグループ分けする。(P3) より comparable な重い純節点は非終端が異なるので、グループは高々 $v$ 個、各グループは反鎖。
  - 1 つのグループの frequent 節点は長さ $\ge\alpha$、生成組は $u$ の生成組内で互いに素。よって個数は $\le(1+\alpha)\theta/\alpha<\theta+1$。
  - 非 frequent ラベルの重い純節点は木全体で $\le v\theta$。よって $H_u\le v(\theta+1)+v\theta=v(2\theta+1)$。
  - 以上より $\alpha\le g_B\le\ell_B\le(r+1)(\theta+1)v(2\theta+1)=\alpha_*$。
- **(P6) 総数**: $T_*=(\alpha_*+1)\theta\le7(r+1)v\theta^3$。$b$ を含まず $\ell_u>T_*$ の節点を large とする。
  - frequent ラベルは large に現れない（$\ell_B\le(1+\alpha)\theta\le T_*$）。よって large は非 frequent ラベルで、各非終端 $\le\theta$ 個、全体で $\le v\theta$ 個。large は「mixed でない」範囲で祖先について閉じる。
  - $W$ の各 $a$ は、mixed 節点が直接書くか、large 節点が直接書くか、mixed/large を含まない極大純部分木（根は木の根か mixed/large の子）の生成組に属する。
  - 極大純部分木の本数は $\le1+r(M+v\theta)$、各総長 $\le T_*$。よって
    \[
    p+K\le\theta M+(rM+rv\theta+1)T_*+\theta\cdot v\theta
    \le5v\theta^3+6rv\theta^2\cdot7(r+1)v\theta^3
    \le(42r(r+1)+5)v^2\theta^5.
    \]
    ここで $M\le4v\theta^2$、$4rv\theta^2+rv\theta+1\le6rv\theta^2$ を使う。
- 以上で $\tau_X=K\le p+K\le(42r(r+1)+5)v^2\theta^5$。合併が $\Sigma$ の場合の $30(r+1)v\theta^3$ と合わせて、$\tau_X\le(42r(r+1)+30(r+1))v^2\theta^5$。

**判定: 正しい（#11 の根拠の式だけ修正）。** (P1) で使う代入可能性が「$a$ と $a^{1+\delta}$（ともに内容 $\{a\}$）の 1 穴比較」だけであること、(P2)–(P6) の比較がすべて純 $a$ の組（内容 $\{a\}$）であることを確認した。定数 $42r(r+1)+5$ の算術も再計算し、正しい。

---

### 2.7 定理の証明（3431–3442 行）

- $L$ が Parikh 飽和なら `lem:app-two-saturated`、そうでなければ `prop:app-two-nonsaturated` と $\tau\le t_{\mathrm{typ}}$ より
  \[
  \tau(G,c)\le C_rv^2\theta^5.
  \]
  正しい。
- $c$ の像は 3 要素、$|\mathsf S^\sharp|=4$、$N_{\mathrm{typ}}\le C_c(G)\le4^{2r}\|G\|$。正しい。
- `cor:distribution-representatives` より
  \[
  \|K\|_+\le N_{\mathrm{typ}}(1+2\theta+r\tau(G,c))+\mathbf 1_{\{\eps\in L\}}.
  \]
  正しい。
- 第 1 上界：$1+2\theta\le3\|G\|^2\theta^5$、$r\tau\le rC_r\|G\|^2\theta^5$ より
  \[
  \|K\|_+\le4^{2r}(3+rC_r)\|G\|^3\theta^5+1.
  \]
  正しい。
- 第 2 上界：$1+2\theta\le3\theta$、$r\tau\le117r(r+1)v\theta\le117r(r+1)\|G\|\theta$ より
  \[
  \|K\|_+\le4^{2r}(3+117r(r+1))\|G\|^2\theta+1.
  \]
  正しい。

**問題点**: 3440 行の「$1+2\theta\le3\|G\|^2\theta\le3\|G\|^2\theta^5$」を第 2 上界にそのまま使うと、
\[
4^{2r}\|G\|(3\|G\|^2\theta+117r(r+1)\|G\|\theta)
=4^{2r}\|G\|^2\theta(3\|G\|+117r(r+1))
\]
となり、$3\|G\|$ の分だけ主張より大きい。第 2 上界には $1+2\theta\le3\theta$ を使う必要がある。**修正: 第 1 上界と第 2 上界で $1+2\theta$ の評価を分けて書く。** 定理の主張自体は正しい。

---

### 2.8 `cor:two-letter-semilattice`（1959–1963 行）

- $s:\{\mathtt a,\mathtt b\}^+\twoheadrightarrow\mathsf S$、$\mathsf S\in\mathbf{SL}$。$\mathsf S$ は可換・冪等なので $s(w)$ は $w$ に現れる文字の $s$-像の積。よって $c(w)=c(w')$ なら $s(w)=s(w')$、すなわち $s\preceq c$。
- したがって $\mathcal C_{2,s}\subseteq\mathcal C_{2,c}$。$L\in\mathcal C_{2,s}$ なら $L\in\mathcal C_{2,c}$ で、定理が $\mathcal B_{2,c}$ と $\mathcal B^{\le r}_{2,c}$ の共通特徴標本 $K$ を与える。
- `lem:typing-monotone` の向きは「$s\preceq t$ のとき、$t$ の特徴標本は $s$ の特徴標本」。ここでは $s\preceq c$ なので、$c$ の特徴標本 $K$ は $s$ の特徴標本でもある。
- よって $s$ はファンアウト 2・ランク $r$ で定理の上界を持つ。

**判定: 正しい。** 特に `lem:typing-monotone` の向き（$c$ の標本が $s$ の標本になる）は正しい。逆向きではない。

---

### 2.9 要旨・序論・§8 の説明・`op:S1`・`op:fanout-two`

- 要旨（89–95 行）：「ファンアウト 2 で LG が境界かは未解決；SL の内容型付けに帰着し、二文字では多項式」— 定理と `prop:sl-reduction` の範囲内。三文字以上を「未解決」としているのも正しい。
- 序論（201–212 行）：「二文字では多項式、大きいアルファベットは未解決」— 正しい。
- §8 の説明（1965–1977 行）：$x^4$ が出たときの $x$-skeleton と個数、$xx$ の隣の $y$-run が飽和か長い run の融合かを強制する、という要約は (i)–(iv) の証明と整合。「ファンアウトを分離しない」「二文字のファンアウト 1 は未解決」「三文字以上は未解決」も範囲内。
- `op:S1`（2009–2018 行）：$a^p,a^q$ が $(\eps,\eps)$ を共有し、$a^{p+k(q-p)}\in L$ を強制する、という議論は $(1,s_{U,2})$-代入可能性から正しい。有限 target が型 1 の語を高々 1 つしか持てない、も正しい。Corollary と合わせて「ファンアウト 1 で超多項式、ファンアウト 2 で多項式」を示せる、という条件文も正しい。
- `op:fanout-two`（2020–2039 行）：「二文字では肯定（定理）」は正しい。三文字以上を未解決としているのも正しい。

**判定: 正しい（範囲内）。** 証明した範囲を超える主張は見つからなかった。

---

## 3. 計算による検証

### 3.1 有限言語での補題の検査

**方法**：$\Sigma=\{\mathtt a,\mathtt b\}$ 上の長さ $\le7$ の語 255 個から、内容型ごとに高々 1 語（純 $a$ 1 語、純 $b$ 1 語、混合 1 語）を選ぶ 15,423 個の有限言語を系統的に作り、$(2,c)$-代入可能性を全数検査した。有限言語では分布は観測された文脈の集合に一致するので、この検査は正確である。通過した 7,999 個の言語について、`lem:app-two-runs`(i)–(iv) と `lem:app-two-alternate` の結論を全数検査した。

**結果**：
- 15,423 個中 7,999 個が $(2,c)$-代入可能。
- そのうち $x^4$ が現れるもの 5,136 個、4 run 以上の語を持つもの 3,200 個。
- **補題の違反は 0 個**。
- 非自明な検査の内訳：`runs(iii)` が非空なもの 640 個、`runs(iv)` が非空なもの 32 個、`alternate` が非空なもの 128 個。いずれも違反なし。
- 長さ $\le8$ の singleton で $x^4$ が現れ、$(2,c)$-代入可能なもの 68 個。そのうち 4 run 以上を持つものは 0 個。
- 追加のランダム検査：$x^4$ を含む語からサイズ 1–4 の部分集合を 2,000 個作り、546 個が通過、違反 0 個（サイズ 4 の通過例 10 個を含む）。

**観察と限界**：
- 通過した有限言語の多くは「内容型ごとに高々 1 語」の形で、しかも $x^4$ を持つ語は $a$-run が 1 つだけのものが多い。実際、この範囲では「$a^4$ を持ち、$a$-run が 2 個以上ある語」を含む通過言語は 0 個だった（$a,b$ の対称性から $b$ も同様）。したがって `runs(i)` の再配分の議論は、有限検査ではほとんど演習されていない。この部分は 2.2(i) の記号的証明で確かめた。
- 有限言語は非空なら Parikh 飽和でないので、`runs(ii)` の検査は「$x^4$ と $xxyx$/$xyxx$ を持つ通過言語があれば違反」という形で行い、0 個だった。これは (ii) の結論と整合する。
- 有限検査は証明ではない。通過言語に関する限り反例がない、という観察である。

**通過例**（一部）：
- $\{\mathtt a^4\mathtt b^4\}$（singleton、$a^4,b^4$ を持つが 2 run なので `alternate` は空）
- $\{\mathtt a^4,\mathtt a^4\mathtt b^4,\mathtt b^4\}$
- $\{\mathtt a^4,\mathtt a\mathtt b\mathtt a\mathtt b\mathtt a\mathtt b\}$（$a^4$ と 6 run の語を別々に持つ）
- $\{\mathtt a^4,\mathtt a\mathtt b\mathtt a\mathtt b,\mathtt b^4\}$（`alternate` が非空で、4 run の語はすべて長さ 1 の run）

### 3.2 不等式の検査

- $\lfloor(p+n)/(n-t+1)\rfloor\le p+t$（$0\le p\le100$、$1\le n\le100$、$1\le t\le n$）：違反 0。
- 差の式：$(p+t)(n-t+1)-(p+n)=(n-t)(p+t-1)$ を $p,n,t\le30$ で確認。本文の「$(n-t)(t-1)$」はこれと一致しない。例えば $p=5,n=3,t=1$ では実際の差は $10$、$(n-t)(t-1)=0$。不等式自体は $p+t-1\ge0$ から正しい。
- $(\theta+4)(\theta+5)\le30\theta^2$、$(\theta+1)(2\theta+1)\le6\theta^2$（$\theta\le200$）：違反 0。
- $4rv\theta^2+rv\theta+1\le6rv\theta^2$、$5v\theta^3\le5v^2\theta^5$、$117(r+1)v\theta\le C_rv^2\theta^5$、$42r(r+1)+30(r+1)\le C_r$（$r,v\le20$、$\theta\le50$）：違反 0。
- 定理の第 1・第 2 上界の算術（$2\le r\le7$、$v\le19$、$\theta\le19$、$g\ge v$）：違反 0。ただし、これは「主張された上界が正しい」ことの数値確認であり、3440 行の導出の書き方の問題とは別である。

### 3.3 小さな文法での $\tau$ の計算

文法：
\[
S\to A\mid B\mid AB,\qquad A\to\mathtt a^4,\qquad B\to\mathtt b^4
\]
（$S,A,B$ は fan-out 1、ランク 2、reduced good。$L=\{\mathtt a^4,\mathtt b^4,\mathtt a^4\mathtt b^4\}$。）

型付き非終端と $E_A$ を定義どおりに取り、$L$ が有限なので $E_A[\mathbf z]\in L$ を満たす tuple を長さ 8 まで全数探索すると：
- $S_{(\{a\})}$：$\tau=4$（$\mathtt a^4$）
- $S_{(\{b\})}$：$\tau=4$（$\mathtt b^4$）
- $S_{(\{a,b\})}$：$\tau=8$（$\mathtt a^4\mathtt b^4$）
- $A_{(\{a\})}$：$\tau=4$
- $B_{(\{b\})}$：$\tau=4$

よって $\tau(G,c)=8$。$v=3$、$\theta=8$、$r=2$、$C_2=42\cdot2\cdot3+117\cdot3=603$ で、定理の上界は
\[
C_2v^2\theta^5=603\cdot9\cdot32768=177{,}831{,}936.
\]
$\tau=8\le177{,}831{,}936$。上界は非常に緩いが、定理の主張と矛盾しない。これは健全性の確認であり、証明ではない。

### 3.4 スクリプト全文と出力

以下は `tools/appH_verify.py` の全文と、`py -3 appH_verify.py 7` の出力である。

```python
"""Appendix H verification script (Python 3 standard library only).

Run:  py -3 appH_verify.py [N]

Part 1: finite-language checks of the lemmas of Appendix H.
Part 2: numerical checks of the inequalities used in the proof.
Part 3: a tiny grammar whose tau is computed by exhaustive enumeration.

The finite checks are observations, not a substitute for the proof.
"""
import sys
from itertools import product
from math import floor

A, B = 'a', 'b'
SIGMA = (A, B)


# ----------------------------------------------------------------------
# Finite words, runs, skeletons, contexts
# ----------------------------------------------------------------------
def words_upto(n, alphabet=SIGMA):
    out = ['']
    for k in range(1, n + 1):
        out.extend(''.join(t) for t in product(alphabet, repeat=k))
    return out


def content(w):
    return frozenset(w)


def factors(w):
    return {w[i:j] for i in range(len(w)) for j in range(i + 1, len(w) + 1)}


def occurrences1(x, w):
    out = []
    for i in range(len(w) - len(x) + 1):
        if w[i:i + len(x)] == x:
            out.append((w[:i], w[i + len(x):]))
    return out


def occurrences2(x, y, w):
    out = []
    lx, ly = len(x), len(y)
    for i in range(len(w) - lx + 1):
        if w[i:i + lx] != x:
            continue
        j0 = i + lx
        for k in range(j0 + 1, len(w) - ly + 1):
            if w[k:k + ly] == y:
                out.append((w[:i], w[j0:k], w[k + ly:]))
    return out


def distributions(L):
    D1, D2 = {}, {}
    for w in L:
        fs = sorted(factors(w), key=lambda s: (len(s), s))
        for x in fs:
            D1.setdefault(x, set()).update(occurrences1(x, w))
        for x in fs:
            for y in fs:
                occ = occurrences2(x, y, w)
                if occ:
                    D2.setdefault((x, y), set()).update(occ)
    return D1, D2


def check_substitutable(L):
    """Exact (2,c)-substitutability for a finite L.

    D1[x] = set of (v0,v1) with v0 x v1 in L; D2[(x,y)] similarly.
    For finite L these sets are exactly the observed contexts.
    """
    D1, D2 = distributions(L)
    items1 = sorted(D1)
    for i, x in enumerate(items1):
        for y in items1[i + 1:]:
            if content(x) != content(y):
                continue
            if D1[x] & D1[y] and D1[x] != D1[y]:
                return False
    items2 = sorted(D2)
    for i, p in enumerate(items2):
        for q in items2[i + 1:]:
            if tuple(map(content, p)) != tuple(map(content, q)):
                continue
            if D2[p] & D2[q] and D2[p] != D2[q]:
                return False
    return True


def runs(w, x):
    out = []
    i = 0
    while i < len(w):
        if w[i] == x:
            j = i
            while j < len(w) and w[j] == x:
                j += 1
            out.append((i, j - i))
            i = j
        else:
            i += 1
    return out


def skeleton(w, x):
    out = []
    i = 0
    while i < len(w):
        if w[i] == x:
            out.append(x)
            while i < len(w) and w[i] == x:
                i += 1
        else:
            out.append(w[i])
            i += 1
    return ''.join(out)


def internal_runs(w, y):
    rs = runs(w, y)
    return [r for k, (_, r) in enumerate(rs) if 0 < k < len(rs) - 1]


def check_lemmas(L, N):
    """Return a list of violations of runs(i)-(iv) and alternate on L."""
    bad = []
    for x in (A, B):
        if not any(x * 4 in w for w in L):
            continue
        y = B if x == A else A
        # runs(i)
        by_inv = {}
        for w in words_upto(N):
            by_inv.setdefault((skeleton(w, x), w.count(x)), []).append(w)
        for key, ws in by_inv.items():
            vals = {w in L for w in ws}
            if len(vals) > 1:
                bad.append(('runs(i)', x, key))
        # runs(ii): a nonempty finite L is never Parikh-saturated
        for f in (x + x + y + x, x + y + x + x):
            if any(f in w for w in L):
                bad.append(('runs(ii)', x, f))
        # runs(iii)
        for w in L:
            if x + x in w:
                for _, ln in internal_runs(w, y):
                    if ln < 2:
                        bad.append(('runs(iii)', x, w, ln))
        # runs(iv)
        if not any(y * 4 in w for w in L):
            for w in L:
                if x + x in w and len(internal_runs(w, y)) > 1:
                    bad.append(('runs(iv)', x, w))
    # alternate
    if any(A * 4 in w for w in L) and any(B * 4 in w for w in L):
        for w in L:
            if len(runs(w, A)) + len(runs(w, B)) >= 4:
                for _, ln in runs(w, A) + runs(w, B):
                    if ln != 1:
                        bad.append(('alternate', w, ln))
    return bad


def finite_checks(N=7):
    print('== Part 1: finite-language checks ==')
    ws = words_upto(N)
    pure_a = [w for w in ws if set(w) == {A}]
    pure_b = [w for w in ws if set(w) == {B}]
    mixed = [w for w in ws if set(w) == {A, B}]
    print('N =', N, ': |words| =', len(ws),
          ', pure a =', len(pure_a), ', pure b =', len(pure_b),
          ', mixed =', len(mixed))
    passed = []
    tested = 0
    for wa in [None] + pure_a:
        for wb in [None] + pure_b:
            for wm in [None] + mixed:
                L = frozenset(w for w in (wa, wb, wm) if w is not None)
                if not L:
                    continue
                tested += 1
                if check_substitutable(set(L)):
                    passed.append(L)
    passed = sorted(set(passed), key=lambda s: (len(s), sorted(s)))
    print('languages tested:', tested, ' (at most one word per content type)')
    print('languages passing (2,c)-substitutability:', len(passed))
    with4 = [L for L in passed if any(A * 4 in w or B * 4 in w for w in L)]
    with4runs = [L for L in passed
                 if any(len(runs(w, A)) + len(runs(w, B)) >= 4 for w in L)]
    violations = [(L, check_lemmas(set(L), N)) for L in passed]
    violations = [(L, b) for L, b in violations if b]
    print('passing with x^4:', len(with4),
          ', passing with a word of >=4 runs:', len(with4runs))
    print('lemma violations among passing languages:', len(violations))
    for L, b in violations[:5]:
        print('  VIOLATION', sorted(L), b[:2])
    # a few representative passing languages
    print('examples of passing languages:')
    for L in passed[:5]:
        print('  ', sorted(L))
    # non-vacuous counts
    nv3 = 0
    nv4 = 0
    nva = 0
    for L in passed:
        for x in (A, B):
            y = B if x == A else A
            if any(x * 4 in w for w in L):
                if any(x + x in w for w in L) and any(internal_runs(w, y) for w in L):
                    nv3 += 1
                    break
        for x in (A, B):
            y = B if x == A else A
            if (any(x * 4 in w for w in L) and not any(y * 4 in w for w in L)
                    and any(x + x in w for w in L)
                    and any(len(internal_runs(w, y)) > 1 for w in L)):
                nv4 += 1
                break
        if (any(A * 4 in w for w in L) and any(B * 4 in w for w in L)
                and any(len(runs(w, A)) + len(runs(w, B)) >= 4 for w in L)):
            nva += 1
    print('non-vacuous runs(iii) instances:', nv3,
          ', runs(iv):', nv4, ', alternate:', nva)
    # singleton search up to N+1 for a word with x^4 and >=4 runs
    singles = 0
    singles4 = 0
    for w in words_upto(N + 1):
        if (A * 4 in w or B * 4 in w) and check_substitutable({w}):
            singles += 1
            if len(runs(w, A)) + len(runs(w, B)) >= 4:
                singles4 += 1
    print('singletons of length <=', N + 1, 'with x^4 passing:', singles,
          '; of these with >=4 runs:', singles4)
    print()


# ----------------------------------------------------------------------
# Part 2: inequalities
# ----------------------------------------------------------------------
def inequalities():
    print('== Part 2: inequality checks ==')
    bad = 0
    for p in range(0, 101):
        for n in range(1, 101):
            for t in range(1, n + 1):
                lhs = (p + n) // (n - t + 1)
                if lhs > p + t:
                    bad += 1
                    print('  FAIL floor:', p, n, t, lhs, p + t)
    print('floor((p+n)/(n-t+1)) <= p+t on p<=100, n<=100, t<=n: failures =', bad)
    # the actual difference of the two sides before flooring
    diff_ok = True
    for p in range(0, 30):
        for n in range(1, 30):
            for t in range(1, n + 1):
                lhs = (p + t) * (n - t + 1) - (p + n)
                rhs = (n - t) * (p + t - 1)
                if lhs != rhs:
                    diff_ok = False
                    print('  DIFF MISMATCH', p, n, t, lhs, rhs)
                    break
            if not diff_ok:
                break
        if not diff_ok:
            break
    print('(p+t)(n-t+1)-(p+n) = (n-t)(p+t-1) checked:', diff_ok)
    bad = 0
    for th in range(1, 201):
        if (th + 4) * (th + 5) > 30 * th * th:
            bad += 1
        if (th + 1) * (2 * th + 1) > 6 * th * th:
            bad += 1
    print('(theta+4)(theta+5)<=30 theta^2 and (theta+1)(2theta+1)<=6theta^2, theta<=200: failures =', bad)
    bad = 0
    for r in range(1, 20):
        for v in range(1, 20):
            for th in range(1, 50):
                if 4 * r * v * th * th + r * v * th + 1 > 6 * r * v * th * th:
                    bad += 1
                if 5 * v * th ** 3 > 5 * v * v * th ** 5:
                    bad += 1
                Cr = 42 * r * (r + 1) + 117 * (r + 1)
                if 117 * (r + 1) * v * th > Cr * v * v * th ** 5:
                    bad += 1
                if 42 * r * (r + 1) + 30 * (r + 1) > Cr:
                    bad += 1
    print('(P6) auxiliary inequalities on r,v,theta<=20,20,50: failures =', bad)
    # theorem arithmetic: first and second bound, over a grid
    bad = 0
    for r in range(2, 8):
        for v in range(1, 20):
            for th in range(1, 20):
                g = v + 10  # any g >= v
                Cr = 42 * r * (r + 1) + 117 * (r + 1)
                N = 4 ** (2 * r) * g
                # first bound: N*(3 g^2 th^5 + r Cr g^2 th^5)
                lhs1 = N * (3 * g * g * th ** 5 + r * Cr * g * g * th ** 5)
                rhs1 = 4 ** (2 * r) * (3 + r * Cr) * g ** 3 * th ** 5
                if lhs1 > rhs1:
                    bad += 1
                # second bound: N*(3 th + 117 r(r+1) v th)
                lhs2 = N * (3 * th + 117 * r * (r + 1) * v * th)
                rhs2 = 4 ** (2 * r) * (3 + 117 * r * (r + 1)) * g * g * th
                if lhs2 > rhs2:
                    bad += 1
    print('theorem first/second bound arithmetic on grid: failures =', bad)
    print()


# ----------------------------------------------------------------------
# Part 3: a tiny grammar and its tau
# ----------------------------------------------------------------------
def tiny_grammar():
    print('== Part 3: a tiny grammar (sanity check, not a proof) ==')
    # S -> A | B | AB, A -> aaaa, B -> bbbb.  L = {a^4, b^4, a^4 b^4}.
    L = {A * 4, B * 4, A * 4 + B * 4}
    print('L =', sorted(L), '; (2,c)-substitutable:', check_substitutable(L))
    # typed nonterminals and contexts (from the definitions, by hand)
    # (name, type, E_A, max length to search)
    typed = [
        ('S_({a})', ({A},), ('', ''), 8),
        ('S_({b})', ({B},), ('', ''), 8),
        ('S_({a,b})', (frozenset({A, B}),), ('', ''), 8),
        ('A_({a})', ({A},), ('', B * 4), 8),
        ('B_({b})', ({B},), (A * 4, ''), 8),
    ]
    tau = {}
    for name, ty, E, maxlen in typed:
        best = None
        for w in words_upto(maxlen):
            if not w or content(w) not in ty:
                continue
            word = E[0] + w + E[1]
            if word in L and (best is None or len(w) < best):
                best = len(w)
        tau[name] = best
    print('tau by exhaustive enumeration over these typed nonterminals:', tau)
    tauG = max(tau.values())
    v, theta, r = 3, 8, 2
    Cr = 42 * r * (r + 1) + 117 * (r + 1)
    bound = Cr * v * v * theta ** 5
    print('v =', v, ', theta =', theta, ', r =', r)
    print('tau(G,c) =', tauG, '; theorem bound C_r v^2 theta^5 =', bound)
    print('tau <= bound:', tauG <= bound)
    print()


if __name__ == '__main__':
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 7
    finite_checks(N)
    inequalities()
    tiny_grammar()

```

出力：

```text
== Part 1: finite-language checks ==
N = 7 : |words| = 255 , pure a = 7 , pure b = 7 , mixed = 240
languages tested: 15423  (at most one word per content type)
languages passing (2,c)-substitutability: 7999
passing with x^4: 5136 , passing with a word of >=4 runs: 3200
lemma violations among passing languages: 0
examples of passing languages:
   ['a']
   ['aa']
   ['aaa']
   ['aaaa']
   ['aaaaa']
non-vacuous runs(iii) instances: 640 , runs(iv): 32 , alternate: 128
singletons of length <= 8 with x^4 passing: 68 ; of these with >=4 runs: 0

== Part 2: inequality checks ==
floor((p+n)/(n-t+1)) <= p+t on p<=100, n<=100, t<=n: failures = 0
(p+t)(n-t+1)-(p+n) = (n-t)(p+t-1) checked: True
(theta+4)(theta+5)<=30 theta^2 and (theta+1)(2theta+1)<=6theta^2, theta<=200: failures = 0
(P6) auxiliary inequalities on r,v,theta<=20,20,50: failures = 0
theorem first/second bound arithmetic on grid: failures = 0

== Part 3: a tiny grammar (sanity check, not a proof) ==
L = ['aaaa', 'aaaabbbb', 'bbbb'] ; (2,c)-substitutable: True
tau by exhaustive enumeration over these typed nonterminals: {'S_({a})': 4, 'S_({b})': 4, 'S_({a,b})': 8, 'A_({a})': 4, 'B_({b})': 4}
v = 3 , theta = 8 , r = 2
tau(G,c) = 8 ; theorem bound C_r v^2 theta^5 = 177831936
tau <= bound: True


```

---

## 4. LaTeX の修正案

### 4.1 3345 行（`lem:app-two-saturated`、合併が $\Sigma$ の場合）

現行：
```latex
Since
$\lfloor(p+n)/(n-t+1)\rfloor\le p+t$ for $n\ge t\ge1$ (as $(n-t)(t-1)\ge0$), it
takes at most $1+(p+t_{\mathtt a})+(q+t_{\mathtt b})\le\theta+5$ values, so paths
have at most $v(\theta+5)$ nodes.
```

修正案：
```latex
Since
\[
\frac{p+n}{n-t+1}=1+\frac{p+t-1}{n-t+1}\le p+t
\qquad(n\ge t\ge1,\ p\ge0),
\]
it takes at most $1+(p+t_{\mathtt a})+(q+t_{\mathtt b})\le\theta+5$ values, so
paths have at most $v(\theta+5)$ nodes.
```
（あるいは「as $(n-t)(p+t-1)\ge0$」とだけ直してもよい。）

### 4.2 3440–3441 行（定理の証明の第 2 上界）

現行：
```latex
With
$v\le\|G\|$, $1+2\theta\le3\|G\|^2\theta\le3\|G\|^2\theta^5$ and the two bounds on
$\tau$, this gives both stated bounds.
```

修正案：
```latex
For the first bound use $1+2\theta\le3\|G\|^2\theta\le3\|G\|^2\theta^5$ and
$r\tau\le rC_r\|G\|^2\theta^5$; for the second use the sharper
$1+2\theta\le3\theta$ and $r\tau\le117r(r+1)\|G\|\theta$.  Both stated bounds
follow.
```
（第 2 上界では $3\|G\|^2\theta$ ではなく $3\theta$ を使う、と明示する。）

### 4.3 3266–3267 行（`lem:app-two-insertion`(b) の説明）

現行：
```latex
Inside a pure component of letter $x$, two blocks of distinct owners in $I$ are
separated by an unchanged letter $x$: their gap is nonempty or contains a block
of an owner outside $I$, which is kept.
```

修正案：
```latex
Inside a pure component of letter $x$, consider two consecutive blocks of owners
in $I$.  If they were adjacent, their owners would be joined in the graph, so
they are not; hence between them there is either a terminal $x$ or a block of an
owner outside $I$ (which is kept and consists of $x$'s).  Thus distinct owners in
$I$ create distinct $y$-runs.
```

### 4.4 3274–3275 行（different-letter の場合）

現行：
```latex
Otherwise both $\mathtt a^5$ and $\mathtt b^5$ occur by (a), and with
$x:=x_{h_1}$ and $y:=x_{h_2}$ the two pure
components contain the runs $x,y,x$ and $y,x,y$ respectively;
```

修正案：
```latex
Otherwise $x_{h_1}\ne x_{h_2}$; applying (a) to $h_1$ and to $h_2$ shows that
both $\mathtt a^5$ and $\mathtt b^5$ occur.  With
$x:=x_{h_1}$ and $y:=x_{h_2}$ the two pure
components contain the runs $x,y,x$ and $y,x,y$ respectively;
```

---

## 5. 総合判定

**定理・補題の主張は正しいと判断する。ただし、3345 行の不等式の根拠の式と、3440–3441 行の第 2 上界の算術の書き方の 2 箇所は証明の記述として誤りなので修正し、3266–3267 行と 3274–3275 行の説明を補えば、この付録は投稿可能である。**

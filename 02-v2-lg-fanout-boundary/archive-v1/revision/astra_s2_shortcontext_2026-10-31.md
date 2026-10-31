# 結論の要約表

| 主張 | 判定 | 根拠の節 |
|---|---|---|
| 三文字の一般の SC_A、および一般の $\tau(G,s)\le Q(g,\theta)$ | 未解決 | §7 |
| 任意の実現型の生成組から、純成分の両端と混合成分の $c$ を保存した、総長 $4(2p+z)(r+1)v\theta$ 以下の生成組を作れる。ただし純成分への $c$ 混入を許す | 証明済み | 定理2.1 |
| **純文字に挟まれた $c$-run の削除に閉じた部分クラス**では、すべての表示について $\tau\le16(r+1)v\theta$、特徴データ長は $O_r(g^2\theta)$ | 証明済み | 定理3.1・系3.2 |
| 任意位置の $c$ の削除に閉じた部分クラスでは、さらに $\tau\le8(r+1)v\theta$ | 証明済み | 系3.3 |
| 上の部分クラスは、非正則言語、無界な $c$-run 数、任意に深い挿入を許す | 証明済み | 命題4.1 |
| $(2,s)$-代入可能性だけで、純文字に挟まれた $c$-run を削除できる | 反証済み（反例あり） | 命題5.1、既知族 $P_{3,2}$ |
| 短い混合語の長さだけから、最短純語の長さを一様に抑えられる | 反証済み（反例あり） | 命題5.1、既知族 $P_{N,2}$ |
| F3 の移送と F4 の汲み上げを、その記載どおりの前向き規則として反復すれば、初期集合より短い純語を作れる | 反証済み（反例あり） | 命題6.1。実際には不変量による一般的な不可能性 |
| 有限な「部分木置換の全組合せ」を種とする代入閉包から、多項式長の同型代表が出るという中間命題 R | 未解決 | §7.2 |
| $P_{N,2}$、$1\le N\le5$ の arity 1・2 の全分布検査と内部削除の照合 | 計算による観測（証明ではない） | 付録B |

**到達点。** 一般の主問題は解けていない。今回の追加結果は、導出文脈を用いた「型を一部壊す短縮」を明示的に分離し、その後の修復が可能な、言語だけで定義される部分クラスについて SC_A を証明したことである。前回の bounded-run 定理や NFA 定理の再証明で終わらせてはいない。一方、追加した削除閉性を一般の代入可能性から導いたとは主張しない。

## 1. 資料、設定、先行報告との差分

### 1.1 照合した版

2026年10月31日に以下を取得した。SHA はファイルの Git blob SHA であり、commit SHA ではない。

| 資料 | blob SHA |
|---|---|
| [本論文 v2 main.tex](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/main.tex) | `d9d589e69936e6d461ed1ac1cb6f51981ebe2090` |
| [Astra 先行報告](https://github.com/growupkuriyama-hub/Papers/blob/main/02_fixed-h-mcfg/revision/astra_ternary_u1_fanout2_2026-10-30.md) | `933df5d0de85d6edcddf1f0604b95d90338bbc8b` |
| [ChatGPT 先行報告](https://github.com/growupkuriyama-hub/Papers/blob/main/02_fixed-h-mcfg/revision/chatgpt_ternary_u1_fanout2_2026-10-30.md) | `0c05c1348059cf6f6b8d431cb2223bcf56528f7a` |
| [先行検証器](https://github.com/growupkuriyama-hub/Papers/blob/main/02_fixed-h-mcfg/revision/check_ternary_u1_fanout2.py) | `01035cca51d68b7cc0ba48484a23e246efb63510` |

プロジェクトの `project-master-v15-2026-10-28.md` も参照したが、数学的定義・定理の基準は上記の現行原稿とした。先行検証器は読んだが再実行していない。今回の計算は付録Bの独立した短いプログラムだけである。

先行報告との関係は次のとおり。

- Astra §3 と原稿 `lem:app-u1-runs` は、同時置換で生じる $c$-run の**個数**を言語全体の上界と比較する。今回は個数の上界を仮定せず、置換後に特定の run を消せるという**閉性**を使う。
- Astra §4 と原稿 `lem:app-u1-shallow` は、純成分への $c$ 混入を禁止する。今回は混入を認めたまま短い組を作り、文法の外で受理を保って修復する。
- ChatGPT 定理5.1は有限オートマトンの状態数を使う。今回の定理3.1は正則性を要求しない。
- ChatGPT 定理4.1（F3）と定理2.1（F4）は正しい既知結果として扱う。§6では、それらを前向きの推論規則として使った場合の限界を新たに明示する。
- $P_{N,m}$ は Astra §5–6 の既知族である。§5の反例族そのものを新規構成とはしない。

### 1.2 記法と量化

$\Sigma=\{a,b,c\}$、$s(a)=s(b)=1$、$s(c)=\zeta$、$\zeta^2=\zeta$ とする。$L\in\mathcal C^{\mathrm{mcf}}_{2,s}$、$G$ は依頼の reduced good 表示、$g=\|G\|$、$v=|V|$、$\theta=\bar\theta_G\ge1$、ランク上限 $r\ge2$ は固定する。

非空の型付き非終端を一つ固定し、$X=A_{\mathbf t}$、$d=\operatorname{fan}(A)\in\{1,2\}$ とする。$\mathbf t$ 中の $1$ の数を $p$、$\zeta$ の数を $z$ と書く。したがって $p+z=d$。以下の主張は、**すべての**実現型 $\mathbf t$、**すべての**この条件の表示 $G$ に対するものである。

原稿 `lem:thickness-equivalence` により、各非終端 $B$ に

\[
\omega_B\in L_B(G),\qquad \|\omega_B\|_1\le\theta
\tag{1.1}
\]

を固定でき、各規則の端末寄与も $\theta$ 以下である。また同補題(iv)の許容導出文脈 $E_A$ は

\[
|E_A|_{\rm fix}\le\theta,
\qquad E_A[L_A(G)]\subseteq L\cap\Sigma^+
\tag{1.2}
\]

を満たす。$d=2$ のとき、その内側区切りは非空である。

原稿 `lem:typed-homogeneity` と `lem:app-u1-fillers` を使用する。特に

\[
\tau_X=\min\{\|\vec x\|_1:
\vec x\in(\Sigma^+)^d,\ s^{(d)}(\vec x)=\mathbf t,
\ E_A[\vec x]\in L\}.
\tag{1.3}
\]

この等式については証明も再確認した。任意の生成組 $\vec u\in L_X$ と、右辺の条件を満たす $\vec x$ は、同じ型で許容文脈 $E_A$ を共有するため、その arity の代入可能性により全分布が一致する。逆に同じ分布なら $E_A$ を受理する。ここで $\vec x$ 自身の文法による生成は要求しない。

$L\cap\Sigma^+=\varnothing$ なら実現型付き非終端はなく、対象の主張は空虚である。以下は非空の場合を扱う。$\varepsilon\in L$ の場合も $G$ は正長部分の表示であり、最後の標本評価にだけ $1$ を加える。

## 2. 無条件にできること：印を保存した短い生成組

### 定理2.1（純成分の両端を保存する短縮）

上の設定で、次を満たす $\vec u,\vec y\in L_A(G)$ が存在する。

1. $s^{(d)}(\vec u)=\mathbf t$。
2. $t_i=1$ なら、$y_i$ の先頭・末尾は、それぞれ $u_i$ の先頭・末尾と同じ純文字である。
3. $t_i=\zeta$ なら、$y_i$ は $c$ を少なくとも一つ含む。
4. 総長は
   \[
   \|\vec y\|_1\le B_X:=4(2p+z)(r+1)v\theta.
   \tag{2.1}
   \]

第2項は $y_i$ 全体が純であることを意味しない。ここが一般の SC_A との差である。生成組の存在と (2.1) は、代入可能性を使わない文法側の主張である。

**証明。** $A$ から型 $\mathbf t$ の組を生成する導出木のうち、節点数が最小のものを $T$ とし、その根の組を $\vec u$ とする。各節点に、非終端とその節点が実際に生成する組の型ベクトルを記す。

一つの根から葉への経路に同じラベルが二度あれば、上の部分木を下の部分木で置き換えられる。両者の非終端は等しく、成分ごとの型も等しいため、準同型性によりその上の各規則の出力型、したがって根型も変わらない。この置換は真に節点を減らすので、$T$ の選択に反する。各非終端の型ベクトルは高々 $2^2=4$ 種類であるから、すべての経路の節点数は $4v$ 以下である。

各純根成分では最初と最後の文字を印し、各混合根成分では一つの $c$ を印す。長さ1の純成分では二つの印は同じ位置でよい。相異なる印の数 $m$ は

\[
1\le m\le2p+z
\tag{2.2}
\]

である。線形・非削除性により、根の各端末位置は、それを直接書く一意の節点に由来する。印を書いた節点までの根からの経路の和集合を $H$ とする。すると

\[
|H|\le4mv\le4(2p+z)v.
\tag{2.3}
\]

$H$ の外へ出る子部分木をすべて、その根非終端 $B$ の $\omega_B$ の導出で置き換える。これらの部分木は互いに祖先・子孫でなく、どれも印を書かない。したがって同時置換は正当な $A$-導出を与える。その根組を $\vec y$ とする。

印そのものは削除されない。また純根成分の最初の印より前、または最後の印より後に、新たな端末が出現することもない。実際、置換される各成分は、元の根組の中で非空の連続区間として現れる。最初の印より前にそのような区間があれば、元からその印が先頭文字でなかったことになる。最後の印より後についても、元の末尾性に反する。テンプレートと変数の位置は置換で変えない。よって純成分の両端文字は保存される。混合成分に印した $c$ も保存される。

長さ1の純成分には印以外の位置がないので、その成分に寄与する置換区間はない。この場合も純成分の非空性と両端についての主張は成立する。

$\vec y$ の全端末は、$H$ の節点が直接書く端末か、$H$ から外へ出る子部分木の置換組に由来する。各 $H$ 節点の直接の端末数は $\theta$ 以下で、外へ出る子は高々 $r$ 個、各置換組長は $\theta$ 以下である。したがって

\[
\|\vec y\|_1\le(r+1)\theta|H|
\le4(2p+z)(r+1)v\theta.
\]

置換後も $G$ の生成組であるため全成分は非空であり、(1.2)より $E_A[\vec y]\in L$ である。以上ですべての項を示した。$\square$

### 2.2 arity・型別の上界

| arity | 対象型 | $2p+z$ | (2.1) の係数：$(r+1)v\theta$ の倍数 |
|---|---|---:|---:|
| 1 | $(1)$ | 2 | 8 |
| 1 | $(\zeta)$ | 1 | 4 |
| 2 | $(1,1)$ | 4 | 16 |
| 2 | $(1,\zeta)$、$(\zeta,1)$ | 3 | 12 |
| 2 | $(\zeta,\zeta)$ | 2 | 8 |

純成分がなければ、$\vec y$ はすでに所望の型である。これは原稿 `lem:app-u1-parikh` の “Type $\zeta$ only” を三文字でそのまま利用できる理由でもある。混合型二種類では、純成分が左か右かによって印の数も長さ評価も変わらず、混合成分の印した $c$ はどちらの位置でも保存される。

## 3. 新しい部分クラスでの SC_A

### 3.1 言語だけによる追加条件

次の性質を **内部 $c$-run 削除閉性** と呼ぶ。

\[
\begin{split}
\mathrm{IE}:\quad &\forall P,Q\in\Sigma^*,\ \forall\alpha,\beta\in\{a,b\},\ \forall k\ge1,\\
&P\alpha c^k\beta Q\in L
\ \Longrightarrow\ P\alpha\beta Q\in L.
\end{split}
\tag{3.1}
\]

これは言語の性質であり、特定の文法に対する条件ではない。先頭や末尾の $c$-run の削除は要求しない。内部 run の長さや個数には上限を置かない。

さらに強い **$c$ 削除閉性** を

\[
\mathrm{DE}:\quad
PcQ\in L,\ PQ\ne\varepsilon
\ \Longrightarrow\ PQ\in L
\quad(P,Q\in\Sigma^*)
\tag{3.2}
\]

とする。DE から IE が従う。実際、$\alpha,\beta$ が残るため各中間語は非空であり、DE を $k$ 回適用できる。

固定 $r$ に対し

\[
\mathfrak E_{2,s}:=
\{L\in\mathcal C^{\mathrm{mcf}}_{2,s}:L\text{ は IE を満たす}\}
\tag{3.3}
\]

を部分クラスとする。以下は、その各言語のすべての指定の表示に一様に成り立つ。

### 定理3.1（内部削除閉性の下での代表長）

$L\in\mathfrak E_{2,s}$ なら、任意の実現 $X=A_{\mathbf t}$ に対し

\[
\boxed{\tau_X\le4(2p+z)(r+1)v\theta.}
\tag{3.4}
\]

特に

\[
\boxed{\tau(G,s)\le16(r+1)v\theta\le16(r+1)g\theta.}
\tag{3.5}
\]

**証明。** 定理2.1の $\vec y$ を取る。$t_i=1$ の各成分 $y_i$ の先頭と末尾は純文字である。したがって $y_i$ 中の任意の極大 $c$-run は、その直前・直後に $a$ または $b$ を持ち、両隣の文字も $y_i$ の内部にある。

受理語 $E_A[\vec y]$ の中で、その run を一つ選ぶ。全体の語は $P\alpha c^k\beta Q$ の形となり、IE により $P\alpha\beta Q$ も受理される。変更したのは一つの成分の内部だけであり、$E_A$ の固定部分は一文字も変えていない。削除によって純文字は失われないので、その成分の両端は依然として純文字である。残った $c$-run に対しても同じ理由で IE を適用できる。

$c$ の個数は有限で、各操作で少なくとも一つ減るから、$t_i=1$ の全成分から $c$ を消し尽くせる。最終組を $\vec x$ とする。純成分の両端の印は残るため、各 $x_i$ は非空である。$t_i=\zeta$ の成分には一切操作をせず、定理2.1で保存した $c$ が残る。したがって $s^{(d)}(\vec x)=\mathbf t$ であり、各段階での IE の適用から $E_A[\vec x]\in L$ である。また削除しかしていないので

\[
\|\vec x\|_1\le\|\vec y\|_1\le4(2p+z)(r+1)v\theta.
\]

(1.3)から (3.4) を得る。$p+z\le2$ より $2p+z\le4$ なので (3.5) が従う。

$d=1$ では一つの成分だけに上の操作を行う。$d=2$ では必要な成分だけに操作を行い、もとの非空の内側区切りには触れない。よって両 arity で用いた文脈は最後まで許容である。$\square$

**重要な区別。** $\vec y$ は $A$ の生成組である。修復後の $\vec x$ は一般に $A$ の生成組である必要がない。したがって証明したのは $\tau$ の上界であり、$t_{\rm typ}$ の同じ上界ではない。原稿 `prop:typed-thickness-exponential` と矛盾しない。

### 系3.2（特徴データ）

同じ仮定の下で、両復元作用素に共通する特徴標本 $K$ があり、

\[
\boxed{
\|K\|_+\le3^{2r}g\bigl(1+2\theta+16r(r+1)v\theta\bigr)
+\mathbf1_{\{\varepsilon\in L\}}.
}
\tag{3.6}
\]

したがって固定 $r$ では $O_r(g^2\theta)$ である。

**証明。** 原稿 `cor:distribution-representatives` は

\[
\|K\|_+\le N_{\rm typ}(1+2\theta+r\tau)+\mathbf1_{\{\varepsilon\in L\}}
\]

を与える。原稿の型分割数の評価 $N_{\rm typ}\le3^{2r}g$ と (3.5) を代入すると (3.6) になる。$v\le g$、$g,\theta\ge1$ より、括弧内の各項に $g$ を掛けた量は固定 $r$ に対し $g^2\theta$ の定数倍以下である。$\square$

### 系3.3（任意位置の削除を許す場合）

DE が成り立つなら

\[
\tau_X\le4d(r+1)v\theta,
\qquad
\tau(G,s)\le8(r+1)v\theta.
\tag{3.7}
\]

**証明。** 定理2.1の証明に使う印を変更する。純根成分には一つの純文字だけを印し、混合根成分には一つの $c$ を印す。印の数は $d$、経路長は $4v$ 以下なので、これらを結ぶ $H$ は高々 $4dv$ 節点である。$H$ の外へ出る子を $\omega_B$ で置き換えれば、長さは $4d(r+1)v\theta$ 以下になる。

この場合、純成分の両端が純であるとは限らない。しかしその成分には印した純文字が残る。各対象成分の $c$ を、位置に関係なく DE で一つずつ消す。印した純文字が常に残るため、どの中間語も非空であり、各対象成分も空にならない。混合成分と $E_A$ の固定部分は変更しない。よって最終組は型 $\mathbf t$、受理文脈は $E_A$ のままであり、長さは増えない。(1.3)を使い、最後に $d\le2$ を代入する。$\square$

## 4. 部分クラスの大きさと限界

### 命題4.1（正則性も run 数制限も要求していない）

\[
L_{\rm bal}:=\{w\in\{a,b,c\}^+:|w|_a=|w|_b\}
\tag{4.1}
\]

は $\mathfrak E_{2,s}$ に属し、DE も満たす。非正則であり、任意に深い挿入と無界な $c$-run 数を持つ。

**証明。** まず文脈自由性を示す。次の文法を取る。

\[
S\to c\mid ab\mid ba\mid aSb\mid bSa\mid SS.
\tag{4.2}
\]

すべての規則は $a,b$ の個数差を0に保ち、正長の語だけを生成するので、生成言語は (4.1) に含まれる。

逆向きは語長の帰納法で示す。正長の $w$ が個数差0を持つとする。先頭が $c$ なら、$w=c$ の場合は定数規則、残りが非空の場合はその残りの差も0なので、帰納法と $SS$ を使う。先頭が $a$ なら、先頭からの差が初めて0に戻る最短接頭辞は $aub$ で、$u$ の差は0である。$u=\varepsilon$ なら $ab$、$u\ne\varepsilon$ なら帰納法と $aSb$ でその接頭辞を生成する。残りの接尾辞が非空なら、それも差0で元の語より短いので、帰納法と $SS$ で連接する。先頭が $b$ の場合は、最初に差0へ戻る接頭辞が $bua$ となり、定数規則 $ba$ または $bSa$ と、必要なら $SS$ を用いる。これで全語を生成する。

(4.2) は fan-out 1、rank $\le2$、線形・非削除・非置換・非併合・$\lambda$-free で、すべての規則は成功使用を持つ。従って reduced good 表示の存在も満たす。

全 arity の組代入可能性を確認する。$\delta(w):=|w|_a-|w|_b\in\mathbb Z$ とする。同型の二組 $\vec x,\vec y$ が許容文脈 $E$ を共有すれば

\[
\delta(E)+\sum_i\delta(x_i)=0
=\delta(E)+\sum_i\delta(y_i),
\]

よって $\sum_i\delta(x_i)=\sum_i\delta(y_i)$。任意の許容文脈 $F$ に対しても $\delta(F[\vec x])=\delta(F[\vec y])$ なので、片方が (4.1) に属することと他方が属することは同値である。成分が非空なので置換後の全体語も非空である。この証明はすべての arity に通用し、特に arity 1 と2を含む。非空内部区切りを緩和する必要はない。

$c$ を消しても $\delta$ は変わらないため、非空性を保つ限り DE が成立する。

非正則性について、正則言語 $a^*b^*$ との共通部分は $\{a^n b^n:n\ge1\}$ である。これが正則なら pumping length $h$ に対し $a^h b^h$ の最初の $h$ 文字内で非空区間を汲み下げられるが、$a$ の数だけが減って等数性に反する。正則言語は共通部分に閉じるので、$L_{\rm bal}$ は正則ではない。

最後に、任意の $D\ge1$ について

\[
a^Db^D\,c\,a^Db^D\in L_{\rm bal}
\]

は長さ $2D$ の純な両側を持つ。また $(abc)^m\in L_{\rm bal}$ は $m$ 個の $c$-run を持つ。これで残りの主張も示した。$\square$

この例により、定理3.1を有限 NFA の定理から直接導くことはできず、F1の「深い挿入がない」条件も、F2の run 数有界条件も満たさない場合を実際に含む。

一方、定理3.1が三文字の一般クラスを扱うわけではない。IE は追加仮定であり、有限純部分や一原始語の冪という候補条件から IE が従うことも証明していない。またこの部分クラス内の非 Parikh 飽和の既知例として、ChatGPT 命題5.3の $(ab\mid c)^+$ がある。トークン境界の内部 $c$-run を消してもこの言語に残るが、$abc$ と同じ Parikh ベクトルの $acb$ は属さない。したがって定理3.1は Parikh 飽和を暗に仮定していない。

## 5. 削除による修復は一般には不可能

### 命題5.1（追加条件を省けない）

既知族の特殊形

\[
P_{N,2}:=\{(ab)^N,\ cabab,\ abcab,\ ababc\},\qquad N\ge1
\tag{5.1}
\]

は $\mathcal C^{\mathrm{mcf}}_{2,s}$ に属する。$N\ne2$ なら IE を満たさない。また、すべてが長さ5の受理語 $abcab$ を持つ一方、$\mu_1(P_{N,2})=2N$ である。

**証明。** Astra §5.1–5.2の位相・加法量の証明を、この特殊形について具体的に展開する。状態を0,1、文字が表す辺を $a:0\to1$、$b:1\to0$、$c:0\to0$ とし、始点・終点を0とする。正長の経路語は $(ab\mid c)^+$。その中で、型1の Parikh 値を $(N,N,0)$、型 $\zeta$ の値を $(2,2,1)$ に固定すると、ちょうど (5.1) になる。

同型の非空組 $\vec x,\vec y$ が許容文脈 $E$ を共有するとする。各非空の内部区切りは、最初・最後の文字が表す辺からその両端状態を決める。外側区切りが非空なら同じ方法で境界状態が決まり、空なら指定始点・終点0が境界状態を決める。従って $x_i,y_i$ は各 $i$ で同じ両端状態を持つ経路である。

同じ型の組と同じ文脈を使った全体語の型は等しいため、二つの受理語の指定 Parikh 値は一致する。固定部分の Parikh 値を引けば

\[
\sum_i\Psi(x_i)=\sum_i\Psi(y_i).
\]

任意の別の許容文脈 $F$ でも、各成分の両端状態が等しいので経路として接続可能かどうかは一致する。全体型と全体 Parikh 値も等しいため、(5.1)の条件を満たすかどうかも一致する。これで全文脈・全非空組について全 arity の代入可能性を示した。有限言語なので各語を開始記号の定数規則にすれば good CFG 表示を持つ。

$abcab=a\,b c a\,b$ は受理されるが、内部の $c$ を消すと $abab=(ab)^2$ になる。$N\ne2$ ではこれが (5.1) にないので IE は偽である。純受理語は一つだけで長さ $2N$、混合語 $abcab$ の長さは常に5であり、残りの主張も従う。$\square$

**この反例の意味。** 短い混合語を見つけるだけでは、型1への安価な修復は導けない。ただし一般の SC_A への反例ではない。Astra 系6.3により、この族のすべての表示で

\[
\theta=\max\{2N,5\}.
\tag{5.2}
\]

したがって、最短純語が長いと規則厚さも長い。$g\theta$ が小さい超多項式下界はここから得られない。

## 6. F3・F4をそのまま反復する方針の厳密な限界

### 命題6.1（前向き規則の最短純語不変量）

任意の初期受理語集合 $W_0\subseteq L\cap\Sigma^+$ を取る。既知の F3 と F4を次の形でのみ使用し、得られた語を追加する操作を任意の有限回行う。

- F3：純なホスト中の同じ文字で切った二組に対し、既知の $Up_iZq_iV$ から $Up_jZq_jV$ を追加する。
- F4：既知の同型の $u,puq$ から $p^kuq^k$、$k\ge0$ を追加する。

この操作で得られる任意の集合 $W$ について、$W_0$ に純語がなければ $W$ にも純語はない。純語があれば

\[
\min\{|w|:w\in W\cap\{a,b\}^+\}
=
\min\{|w|:w\in W_0\cap\{a,b\}^+\}.
\tag{6.1}
\]

**証明。** F3 では $p_i\alpha q_i=p_j\alpha q_j$ なので

\[
|p_i|+|q_i|=|p_j|+|q_j|.
\]

両組の成分は純であり、$U,Z,V$ は変更しない。よって追加語は、その移送元と長さも $c$ の個数も等しい。追加語が純なら移送元も純で、同じ長さの語がすでに存在する。

F4 では追加語の長さは $|u|+k(|p|+|q|)\ge|u|$ である。$u$ が混合ならすべての追加語も $u$ を含むので混合である。$u$ が純なら、仮定の同型性から $puq$ も純であり、$p,q$ も純である。従ってこの場合に追加される純語も、すでにある純語 $u$ より短くない。

各操作は既存語を削除しない。以上を操作回数について帰納的に適用すると、純語の不存在または最小長が保存される。すべての有限回の結果の和集合を取っても、各追加語には有限の生成履歴があるので同じ主張が成り立つ。$\square$

これは F3・F4 が無用だという主張ではない。また**代入可能性の全推論**について短縮不能だという主張でもない。F3・F4から分布同値を得たうえで、別の文脈に対する一般の一穴・二穴代入を使う方法は、この命題の対象外である。

例えば、Astra §8.3の $c,uc,u^2$（$u$ は純）から $u$ を強制する議論は、混合語の一穴同値を別の文脈へ運び、さらに純語の共有文脈を使う。これは上記二つの前向き規則だけではない。今回必要な短縮も、その種の追加の共有文脈を確保する段階を明示しなければならない。

## 7. 一般の SC_A に残る障害と具体的な中間命題

### 7.1 できたことと、できていないこと

定理2.1により、すべての実現型について、多項式長の受理語 $E_A[\vec y]$ までは得られる。純成分に印した端の文字と、混合成分の $c$ は残せる。しかし所望の純成分の内部に $c$ が入ることを防げていない。

定理3.1は IE によりこれを解消する。一般の場合には、命題5.1が示すとおり、その $c$ を消すだけでは失敗する。F3・F4の前向き反復も、命題6.1により最短純語を下げる道具としては不十分である。

未達の項目は明確である。

- 一般の arity 1、型 $(1)$ に対する多項式上界は未証明である。
- 型 $(1,1),(1,\zeta),(\zeta,1)$ の一般上界も未証明である。
- 「純部分が有限」または「純部分が一原始語の冪に含まれる」だけを仮定した全表示の上界は未証明である。
- $\mu_1(L_n)=n^{\omega(1)}$ と $g_n\theta_n=n^{O(1)}$ を両立する反例族も得ていない。

### 7.2 導出の有限な置換族に限定した命題 R

以下は未証明であるが、任意の短い文脈を量化した前回の SC より、調べる構造と使用可能な推論を具体化したものである。

定理2.1の導出木 $T$ と印付き骨格 $H$ を取る。$H$ から外へ出る子部分木の根を $B_1,\ldots,B_k$、それぞれの元の生成組を $\eta_1,\ldots,\eta_k$ とする。同じ非終端が複数回現れてよい。各出現は独立したスロットとして区別する。

\[
k\le r|H|\le4r(2p+z)v\le16rv.
\tag{7.1}
\]

骨格の規則と、その規則が直接書く端末を固定すると、根組を得る線形な組代入写像 $F_H$ が定まる。各スロットで $\eta_j$ と $\omega_{B_j}$ のいずれかを選び、

\[
\mathcal W_H:=
\left\{E_A\!left[F_H(\xi_1,\ldots,\xi_k)\right]:
\xi_j\in\{\eta_j,\omega_{B_j}\}\right\}
\tag{7.2}
\]

とする。これは高々 $2^k$ 語の有限集合であり、すべて $L(G)$ に属する。すべて元の選択なら $E_A[\vec u]$、すべて短い選択なら $E_A[\vec y]$ になる。

**(7.2)の全組合せが受理される理由。** 各スロットは、互いに素な部分木の根である。各選択肢は同じ非終端の生成組なので、任意の選択を同時に行っても元の規則をそのまま適用できる。順序・交錯の形は $F_H$ に固定され、スロットを入れ替えない。最後に $E_A$ がすべての $A$-生成組を受理する。

$\operatorname{Sub}_s^{\le2}(W)$ を、$W$ を含み、次の推論で閉じた最小の正長語集合と定義する。

\[
\frac{E[\vec x],\ E[\vec y],\ F[\vec x]}
{F[\vec y]},
\quad
s^{(d)}(\vec x)=s^{(d)}(\vec y),\quad d\in\{1,2\}.
\tag{7.3}
\]

ここで全成分は非空、$E,F$ は許容文脈であり、$d=2$ では**両方の**内側区切りが非空である。(7.3)は F3・F4だけに限定した規則ではなく、代入可能性の全推論である。最小集合は有限段階の追加の和集合として定義できる。

> **未証明命題 R（印付き導出骨格からの短い代表）。** 固定 $r$ ごとに多項式 $P_r$ が存在し、任意の設定 $L,G,A,\mathbf t$ に対して、定理2.1の構成を選んで、
> \[
> E_A[\vec x]\in\operatorname{Sub}_s^{\le2}(\mathcal W_H),\quad
> s^{(d)}(\vec x)=\mathbf t,\quad
> \vec x\in(\Sigma^+)^d,\quad
> \|\vec x\|_1\le P_r(g,\theta)
> \tag{7.4}
> \]
> を満たす $\vec x$ が得られる。

**R が SC_A に十分であることの証明。** (7.2)より $\mathcal W_H\subseteq L$。$L$ の arity 1・2 の代入可能性により、(7.3)の前提三語が $L$ にあれば結論も $L$ にある。推論段階についての帰納法から

\[
\operatorname{Sub}_s^{\le2}(\mathcal W_H)\subseteq L.
\]

したがって (7.4)の組は $E_A$ に受理される。型と非空性も (7.4)に明記されているので、そのまま SC_A の組となる。(1.3)により $\tau\le P_r(g,\theta)$ が従う。$\square$

**この定式化についての留保。** R が SC_A より論理的に弱いとは主張しない。閉包の中に短い語を要求するため、追加の強さを持ち得る。B4の「より具体的」の側を満たす提案である。任意の短い文脈の代わりに、$4v$ 以下の経路、$16v$ 以下の骨格節点、$16rv$ 以下の互いに独立した置換スロット、その全組合せという、実際の導出から来る構造だけを扱う。

また、$2^k$ 個の種を多項式個と呼んではならないし、元の $\eta_j$ の長さも多項式とは限らない。閉包が MCFL であること、閉包計算が停止すること、多項式時間で (7.4) の証明書が見つかることは、いずれも主張していない。IE の場合には $L$ 自体の削除閉性を使ったため、今回の定理3.1は R の証明でもない。

次の研究で実際に不足しているのは、この有限な置換族から、**純型を再実現する共有文脈を (7.3) で強制する論証**である。run の個数を増やすだけでは足りず、純文字の端を保持したままの可換化も仮定できない。

### 7.3 主結果への位置づけ

今回の部分結果をもって、一般の三文字型付けの fan-out 1／2 の指数対多項式分離が得られたとは言えない。原稿 `cor:typing-level-obstruction`、`op:fanout-two`、`rem:binary-u1-scope` の未解決部分は残る。

また、ある $U_1$ 型付けについて fan-out 2 で否定例が得られた場合でも、それだけで fan-out $f\ge3$ の代入可能性まで確保されるわけではない。全 fan-out の境界に関する結論には、対象の各 arity におけるクラス所属を別途確認する必要がある。今回そのような否定例は構成していない。

## 付録A. 証明済み結果の英語 LaTeX 挿入案

以下は定理2.1、定理3.1、系3.2–3.3の挿入案であり、未証明命題 R は含めない。新設 label はすべて `astra-s2-20261031-` を含み、取得した `main.tex` の既存 label と衝突しない。既存のパッケージや独自マクロに依存しにくい通常の記法を用いた。コンパイルは行っていない。

```latex
\begin{lemma}[Endpoint-preserving compression]
\label{lem:astra-s2-20261031-compression}
Let $G$ be a reduced good MCFG of fan-out at most two and
rank at most $r$, and put $v=|V|$ and $\theta=\bar\theta_G$.
Let $s(a)=s(b)=1$ and $s(c)=\zeta$ in $U_1$.
For every realized typed nonterminal $A_{\mathbf t}$, let
$p$ and $z$ be the numbers of coordinates of $\mathbf t$ equal
to $1$ and $\zeta$, respectively.  There are tuples
$\mathbf u,\mathbf y\in L_A(G)$ such that
$s^{(d)}(\mathbf u)=\mathbf t$,
\[
 \|\mathbf y\|_1\le 4(2p+z)(r+1)v\theta,
\]
every coordinate $y_i$ with $t_i=1$ has the same first and last
letters as $u_i$, and every coordinate $y_i$ with $t_i=\zeta$
contains $c$.  No purity assertion is made about the interiors
of the former coordinates.
\end{lemma}

\begin{proof}
Choose a derivation from $A$ of type $\mathbf t$ with the fewest
nodes, and label each node by its nonterminal and the type vector
of its yield.  A repeated label on a path could be cut out:
the replacement is a derivation from the same nonterminal,
and equality of component types preserves every type above it.
This would reduce the number of nodes.  Hence each path has at
most $4v$ nodes.

Mark the first and last letters of each pure root coordinate
and one occurrence of $c$ in each other root coordinate.
There are at most $2p+z$ distinct marked positions; the two marks
in a coordinate of length one coincide.  Let $H$ be the union
of the paths to nodes that write marked positions.  Then
$|H|\le4(2p+z)v$.

For each nonterminal $B$, choose a tuple $\omega_B\in L_B(G)$
of total length at most $\theta$, using
Lemma~\ref{lem:thickness-equivalence}(ii).
Replace every subtree hanging off $H$ by a derivation of the
appropriate $\omega_B$.  The replacements are at incomparable
nodes and avoid all marked positions.  Their yields occupy the
same variable positions in the unchanged templates.  Every
original component contributed by a replaced subtree is nonempty,
so none can have occurred before a marked first letter or after
a marked last letter.  Thus the asserted endpoint letters and
marked occurrences of $c$ survive.  In particular, a pure root
coordinate of length one cannot receive an unmarked replacement
block.  The resulting tuple $\mathbf y$ belongs to $L_A(G)$.

Each node of $H$ writes at most $\theta$ terminals by
Lemma~\ref{lem:thickness-equivalence}(i), and has at most $r$
children outside $H$, each replaced by a tuple of total length
at most $\theta$.  Every terminal of $\mathbf y$ is accounted
for in one of these ways.  Therefore
$\|\mathbf y\|_1\le(r+1)\theta|H|$, proving the bound.
\end{proof}

\begin{theorem}[Short representatives under interior marker erasure]
\label{thm:astra-s2-20261031-interior-erasure}
Let $\Sigma=\{a,b,c\}$, let $s(a)=s(b)=1$ and $s(c)=\zeta$
in $U_1$, and let $L$ be a $(2,s)$-tuple-substitutable MCFL
of fan-out at most two.  Assume that, for all
$P,Q\in\Sigma^*$, $\alpha,\beta\in\{a,b\}$ and $k\ge1$,
\[
 P\alpha c^k\beta Q\in L
 \quad\Longrightarrow\quad P\alpha\beta Q\in L.
\]
For every reduced good presentation $G$ of $L\cap\Sigma^+$
of fan-out at most two and rank at most $r$,
\[
 \tau(G,s)\le16(r+1)|V|\bar\theta_G.
\]
More precisely, a realized typed nonterminal with $p$ pure
coordinates and $z$ impure coordinates has representative length
at most $4(2p+z)(r+1)|V|\bar\theta_G$.
\end{theorem}

\begin{proof}
Fix $X=A_{\mathbf t}$ and use the context $E_A$ from
Lemma~\ref{lem:thickness-equivalence}(iv).
Lemma~\ref{lem:astra-s2-20261031-compression} supplies a tuple
$\mathbf y\in L_A(G)$ within the claimed length bound.
Thus $E_A[\mathbf y]\in L$.

If $t_i=1$, both endpoints of $y_i$ are neutral letters.
Every maximal $c$-run in $y_i$ is therefore immediately
flanked by neutral letters belonging to that same coordinate.
Apply the assumed erasure implication to one such run in the
whole accepted word.  This changes only the interior of $y_i$;
it changes neither $E_A$ nor any other coordinate, and leaves
the neutral endpoints in place.  Each step strictly decreases
the number of occurrences of $c$.  Repeating the procedure
removes all $c$'s from every coordinate with $t_i=1$.
Leave coordinates with $t_i=\zeta$ unchanged.

The resulting tuple $\mathbf x$ has no empty coordinate,
has type $\mathbf t$, satisfies $E_A[\mathbf x]\in L$,
and is no longer than $\mathbf y$.  When the arity is two,
the nonempty internal separator of $E_A$ has never been changed.
Lemma~\ref{lem:app-u1-fillers} now bounds $\tau_X$.
Finally $2p+z\le4$, which gives the uniform bound.
\end{proof}

\begin{corollary}[Characteristic data]
\label{cor:astra-s2-20261031-erasure-data}
Under the assumptions of
Theorem~\ref{thm:astra-s2-20261031-interior-erasure},
put $g=\|G\|$, $v=|V|$, and $\theta=\bar\theta_G$.
There is a characteristic sample for both reconstruction
operators in Corollary~\ref{cor:distribution-representatives}
whose encoded length is at most
\[
 3^{2r}g\bigl(1+2\theta+16r(r+1)v\theta\bigr)
 +\mathbf1_{\{\varepsilon\in L\}}.
\]
In particular, this is $O_r(g^2\theta)$.
\end{corollary}

\begin{proof}
Insert the representative bound into
Corollary~\ref{cor:distribution-representatives}, and use
$N_{\rm typ}\le3^{2r}g$.  Since $v\le g$ and $g,\theta\ge1$,
the stated asymptotic bound follows term by term.
\end{proof}

\begin{corollary}[Unrestricted marker erasure]
\label{cor:astra-s2-20261031-unrestricted-erasure}
In the same setting, assume the stronger condition
\[
 PcQ\in L,\quad PQ\ne\varepsilon
 \quad\Longrightarrow\quad PQ\in L.
\]
Then $\tau_X\le4d(r+1)v\theta$ for each realized typed
nonterminal of arity $d$, and $\tau(G,s)\le8(r+1)v\theta$.
\end{corollary}

\begin{proof}
In the compression construction, mark just one neutral letter
in each pure root coordinate and one occurrence of $c$ in each
impure root coordinate.  There are $d$ marks, so their paths
contain at most $4dv$ nodes.  Replacing the subtrees outside
these paths gives a tuple of length at most $4d(r+1)v\theta$.
Each intended pure coordinate still contains its marked neutral
letter.  Delete all its occurrences of $c$, one at a time,
using the stronger assumption.  The marked letter ensures
nonemptiness at every step.  All other coordinates and all
fixed parts of $E_A$ are unchanged.  Thus the resulting tuple
has the required type, is accepted by $E_A$, and satisfies the
same length bound.  Apply Lemma~\ref{lem:app-u1-fillers} and
then $d\le2$.
\end{proof}
```

## 付録B. 計算の範囲、ソース全文、実行ログ全文

今回実施した数学的計算は、下記プログラムの一回の実行だけである。対象は $P_{N,2}$ の **$N=1,2,3,4,5$ の5例**。各例は4語からなり、対象の各有限言語については全受理語の全一穴・二穴分解を列挙する。二穴では添字 $i<j<k<\ell$ を課すため、二成分と中央区切りのすべてが非空である。

各組の全分布は全受理語の分解から作られる。一つでも受理文脈を持つ組は必ず列挙に現れ、現れない組は分布が空なので共有文脈を持たない。同じ文脈と型でグループ化した組の分布がすべて一致するかを調べる。従って各入力有限言語に関する検査は全数検査である。ただし $N\ge6$ への外挿、一般の文法列挙、命題Rの閉包計算はしていない。

命題5.1の任意の $N$ の証明は上の解析的証明に依存し、この検査には依存しない。定理2.1、3.1、命題4.1、6.1も計算を前提にしていない。資料取得・本文編集・label照合は数理実験ではなく、以下の実行ログに混ぜていない。

### B.1 ソース全文（Python 3、標準ライブラリのみ）

```python
from collections import defaultdict


def observations(language):
    distributions = defaultdict(set)
    groups = defaultdict(set)
    for w in sorted(language):
        n = len(w)
        for i in range(n):
            for j in range(i + 1, n + 1):
                x, e = (w[i:j],), (w[:i], w[j:])
                distributions[x].add(e)
                groups[(e, tuple('c' in u for u in x))].add(x)
                for k in range(j + 1, n):
                    for ell in range(k + 1, n + 1):
                        x = (w[i:j], w[k:ell])
                        e = (w[:i], w[j:k], w[ell:])
                        assert all(x) and e[1]
                        distributions[x].add(e)
                        groups[(e, tuple('c' in u for u in x))].add(x)
    return distributions, groups


def check(language):
    distributions, groups = observations(language)
    for xs in groups.values():
        if len({frozenset(distributions[x]) for x in xs}) != 1:
            return False
    return True


for n in range(1, 6):
    language = {'ab' * n} | {'ab' * i + 'c' + 'ab' * (2-i)
                             for i in range(3)}
    ok = check(language)
    erased = 'abab'
    mu = min(len(w) for w in language if 'c' not in w)
    print(f'N={n} words={len(language)} arity_1_2={ok} '
          f'abcab_in_L={"abcab" in language} '
          f'erased_abab_in_L={erased in language} mu_1={mu}')
    assert ok and mu == 2*n and ((erased in language) == (n == 2))
print('ALL_ASSERTIONS_PASSED')
```

### B.2 実行ログ全文

実行コマンドは `python3 verify_s2.py`。終了コード0、標準エラー出力なし。標準出力の全文は以下のとおり。

```text
N=1 words=4 arity_1_2=True abcab_in_L=True erased_abab_in_L=False mu_1=2
N=2 words=4 arity_1_2=True abcab_in_L=True erased_abab_in_L=True mu_1=4
N=3 words=4 arity_1_2=True abcab_in_L=True erased_abab_in_L=False mu_1=6
N=4 words=4 arity_1_2=True abcab_in_L=True erased_abab_in_L=False mu_1=8
N=5 words=4 arity_1_2=True abcab_in_L=True erased_abab_in_L=False mu_1=10
ALL_ASSERTIONS_PASSED
```

## 自己点検表

| 点検項目 | 結果 |
|---|---|
| すべての $L,G,A,\mathbf t$ の量化を区別したか | はい。一般の定理2.1と、IE／DEを追加した定理3.1・系3.3を区別。部分クラス内ではすべての指定の表示に一様 |
| 多項式の係数が対象の言語や表示に依存していないか | はい。定理3.1の一様な多項式は $Q_r(g,\theta)=16(r+1)g\theta$。DEでは係数を8にできる |
| 内側の区切りが非空か | はい。主証明は $E_A$ の固定部分を変更しない。反例族の証明は内部区切りの非空性を状態決定に用いる。命題Rの推論では $E,F$ の両方に非空条件を課す |
| 穴の成分が最後まで非空か | はい。純成分は印した純文字、混合成分は印した $c$ が残る。IEの証明では純成分の両端を保存 |
| arity 1 と2を両方扱ったか | はい。§2.2で全6型を列記。最終的な分布同値への移行には該当arityの代入可能性を使用 |
| 混合型の左右を区別したか | はい。純成分の位置に関係なくその成分内だけを削除し、他方の混合成分は変更しない |
| 生成組と分布代表を混同していないか | はい。短縮した $\vec y$ は生成組、修復した $\vec x$ は生成組とは限らない。結論は $\tau$ の評価 |
| 純成分に $c$ が混入する可能性を隠していないか | はい。定理2.1では混入を明示的に許し、IE／DEまたは未証明の修復段階が必要だと明記 |
| 二成分の交錯を排除していないか | はい。各置換部分木の成分が占める区間に対して議論し、異なる部分木間の順序を変更しない |
| 規則厚さを型付き文法の厚さと取り違えていないか | はい。使用する $\omega_B$ と各規則の端末数は元の $G$ の $\theta$ で評価。型付き厚さの多項式性は主張しない |
| IEが代入可能性から従うと誤認していないか | はい。$P_{3,2}$ で明示的に反証 |
| 一般のB2、または有限純部分というB1を解いたか | いいえ。それらは未解決。今回のB1はIEで定義した別の部分クラス |
| F3・F4の限界を過大主張していないか | はい。命題6.1は指定した前向き規則だけの不変量。全代入推論による短縮は排除しない |
| 命題Rの位置づけは正確か | はい。十分性だけを証明し、R自体は未解決。SC_Aより弱いとは主張せず、有限な導出置換族に具体化した提案とした |
| 下界と $\tau$ の大きさを混同していないか | はい。新しい超多項式下界はなし。$P_{N,2}$ の $\mu_1$ の大きさは同時に大きい $\theta$ に吸収される |
| 数理的な証明が計算に依存するか | いいえ。本報告の証明済み結果はすべて解析的。有限計算は5例の独立照合のみ |
| 計算のコード・ログ・打切り範囲を省略したか | いいえ。付録Bに今回の数理計算のソース全文・標準出力全文・終了状態・範囲を収録 |
| 英語案に未証明結果を混ぜたか | いいえ。定理2.1・3.1と系3.2–3.3だけを掲載。labelは取得原稿と照合、コンパイルは未実施 |
| 世界の先行文献に対する新規性を確認したか | 未確認。指定原稿・二つの指定報告との差分を示したもので、網羅的文献調査・独立査読を済ませたとの主張はしない |
| 一般問題を解決したという結論になっていないか | はい。一般SC_A、一般多項式上界、超多項式下界はいずれも未解決と冒頭・§7に明記 |

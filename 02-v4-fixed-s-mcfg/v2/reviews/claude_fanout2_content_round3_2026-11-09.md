# 探索報告（第3回）：内容型付けでの容量の議論と、稀な型でない下界の道（`op:fanout-two`）

Claude, 2026-11-09。依頼文「探索依頼（第3回）」への報告。記号は依頼文 §1・§2 に従う。原稿の番号は main.pdf（2026-11-09 版）のものを使う：`prop:zeta-capacity` = 命題 9.2、`lem:distinguishing` = 補題 4.5、`prop:rare-type` = 命題 4.6、`lem:type-deletion` = 補題 4.4、`thm:two-letter-content` = 定理 8.6、`prop:binary-u1-quadratic` = 命題 7.8。

## 1. 要約（3行）

1. **主張 M は正しい [証明済み]。** 定数を確定して $\mu_M(L)\le(2|M|-1+\kappa_{\overline M})\,|V|\,(\rho_{\max}+r\bar\theta_G)$ が成り立ち、$\max\{\bar\theta,\cdot\}$ も要らない（定理 M）。証明は印を付けた葉の方針どおりで、分岐点は「下にある印の集合」による類分けで自然に扱える。同じ論法で、印を Parikh 錐に一般化した定理 P と、散在部分語に一般化した定理 W が出る。定理 W はファンアウト $f$ で因子 $\binom{k+f-1}{f-1}$ を払う。
2. **課題2 [証明済み＋条件付き].** $L\setminus L'$ が「短い部分語 $u$ を含み、内容が $M$ に入る $L$ の語の全体」という切片を含むなら、$\min|L\setminus L'|$ は多項式である（系 W）。よって既知の $\{\mathtt{aab},\mathtt{baa}\}\supsetneq\{\mathtt{aab}\}$ のような位置で分ける部分標的は、$\kappa$ を超多項式にしない限り伸ばせない。完全性については、標準作用素の仮説がつねに $\mathcal C_{f,s}$ に入るなら、最短の特徴標本の長さは差集合族 $\{L\setminus L'\}$ の最小打撃集合の長さ $h(L)$ にちょうど等しい（命題 H）。
3. **否定例の必要条件（更新）.** 稀な内容による下界でも、部分語で証拠づけられる道具2の下界でも、ある語が $M$ の外の文字を $\|G\|,\bar\theta$ について超多項式個含まなければならない（N7・N8）。ただしファンアウト1の否定例 $L_n$（命題 7.1）は $\kappa_{\mathtt c}=2^n$ でこの条件をみたす。したがってこの条件は**ファンアウトを分けない**。

---

## 2. 課題1：主張 M の判定

### 2.0 設定と記号

- $G=(V,\Sigma,P,S)$ は既約、$\varepsilon$-free、nondeleting で、ファンアウトは任意、rank $\le r$ とする。$L=L(G)$。nonpermuting と nonmerging は定理 M・P では使わず、定理 W でだけ使う。
- $\mathrm{In}(A):=L_A(G)$（$A$ の産出する組の集合）。組 $\mathbf y$ の長さ $|\mathbf y|$ は成分の長さの和、内容 $c(\mathbf y)$ は成分に現れる文字の集合とする。
- $M\subseteq\Sigma$ を空でないとし、$\overline M:=\Sigma\setminus M$ とおく。$\#_{\overline M}(\mathbf y)$ は $\mathbf y$ の中の $\overline M$ の文字の出現数である。
- $\lambda_M(A):=\min\{|\mathbf y|:\mathbf y\in\mathrm{In}(A),\ c(\mathbf y)\subseteq M\}$（なければ $\infty$）。
- $\mathrm{cap}(A):=\sup\{\#_{\overline M}(\mathbf y):\mathbf y\in\mathrm{In}(A)\}$。$\kappa_{\overline M}:=\kappa_{\overline M}(L)=\mathrm{cap}(S)$。
- 導出木の各節点 $\eta$（ラベル $A_\eta$）について、その規則のテンプレートに書かれた終端記号を「$\eta$ が書く出現」と呼ぶ。語の各文字の出現は、ちょうど一つの節点が書く（nondeleting なので、どの出現も最終的な語に残る）。$\mathbf x_\eta$ は $\eta$ の内側（$\eta$ の部分木が産出する組）を表す。

使う基本事実は二つで、どちらも nondeleting と線形性から直ちに出る。

- **(F1) 部分木の置き換え.** $\eta$ の部分木を、同じラベル $A_\eta$ の別の導出木で置き換えても、$G$ の導出木になる。結果の語は、元の語から $\mathbf x_\eta$ の文字の出現を除き、新しい組の文字をすべて加えたものである（文脈 $o_\eta$ は固定され、その文字は相対的な順序ごと保たれる）。
- **(F2) 圧縮.** $\eta'$ が $\eta$ の真の子孫で $A_{\eta'}=A_\eta$ なら、$\eta$ の部分木を $\eta'$ の部分木で置き換えたものは $G$ の導出木である。結果の語は、元の語から「$\eta$ の部分木にあって $\eta'$ の部分木にない節点」が書く出現を除いたものである（ただし文字の並びの順は一般に保たれない。§3.1(c) を参照）。節点の数は真に減る。

### 2.1 定理 M

**定理 M [証明済み].** 上の設定で、内容がちょうど $M$ の語が $L$ にあり、$\kappa_{\overline M}<\infty$ とする。このとき
$$\mu_M(L)\;\le\;\bigl(2|M|-1+\kappa_{\overline M}\bigr)\,|V|\,\bigl(\rho_{\max}+r\,\bar\theta_G\bigr).$$

*証明.* $k:=|M|$、$\mu:=\mu_M(L)$ とおく。長さ $\mu$ で内容 $M$ の語の導出木のうち、節点数が最小のもの $T$ をとり、その語を $W$ とする。$M$ の各文字について $W$ の出現を一つずつ選び、これを**印**とする（印は $k$ 個）。

**原理（最小性）.** $T$ から (F1)・(F2) で得た木 $T'$ が次の三つをみたすとする：(a) 節点数が $T$ より少ないか、語が $W$ より短い。(b) 印がすべて残る。(c) 加わった文字がすべて $M$ に入る。すると $T'$ の語の内容は $M$ を含み（b）、$M$ に含まれる（c、元の文字は $M$ に入る）ので、ちょうど $M$ である。長さは $\ge\mu$ でなければならないので、(a) の「短い」は起こらない。長さが $\mu$ に等しければ、節点数の最小性に反する。よって**このような $T'$ は存在しない**。

**段階1（シュタイナー木と類）.** 節点 $\eta$ について、$\eta$ の部分木の節点が書く印の集合を $\mathrm{Mk}(\eta)$ とし、$\mathrm{Mk}(\eta)\ne\emptyset$ の節点の全体を $\mathrm{St}$（シュタイナー木）とおく。$\mathrm{St}$ は根を含み、親について閉じている（$\mathrm{Mk}$ は親に向かって増える）。
- **(1a) 類は鎖である.** $\mathrm{Mk}(\eta)=\mathrm{Mk}(\eta')=:Q\ne\emptyset$ なら、$\eta$ と $\eta'$ の部分木は $Q$ の印を書く節点を共有するので、二つは比較可能である。さらに、その間の節点 $\eta''$ では、$\mathrm{Mk}$ の単調性から $\mathrm{Mk}(\eta'')=Q$ となる。よって $\mathrm{Mk}$ の値ごとの類は、根から下への道の一区間である。
- **(1b) 類は高々 $2k-1$ 個.** 集合族 $\{\mathrm{Mk}(\eta):\eta\in\mathrm{St}\}$ は $k$ 元集合の空でない部分集合の族で、ラミナー（二つの元は包含関係にあるか交わらない）である。部分木どうしが入れ子か交わらないからである。$k$ 元集合上のラミナー族の空でない元は高々 $2k-1$ 個である（包含関係による木を作ると、葉は $\le k$ 個で、子を1個しかもたない内部節点 $Q$ は、子に入らない $Q$ の元を少なくとも1個もつ。これを数えればよい）。
- **(1c) 類の中のラベルは相異なる.** 同じ類の $\eta$ とその子孫 $\eta'$ が同じラベルをもてば、(F2) で圧縮する。除かれる出現は、$\eta$ の部分木にあって $\eta'$ の部分木にない節点が書くものである。$\mathrm{Mk}(\eta)=\mathrm{Mk}(\eta')$ なので、そこに印はない。よって (b) が成り立つ。文字は加わらないので (c) も成り立ち、節点は減る。これは原理に反する。
- **分岐点の扱い.** 分岐点（$\mathrm{St}$ の子を二つ以上もつ節点）や、自分の規則で印を書く節点は、自分の $\mathrm{Mk}$ の類に属する。その下の $\mathrm{St}$ の子の $\mathrm{Mk}$ は真に小さいので、別の類に入る。よって (1c) の圧縮は、類の中だけで行われる限り印を壊さない。依頼文の「区間」はこの類のことで、類の数は (1b) により $2k-1$ 以下である。
- 以上から $|\mathrm{St}|\le(2k-1)|V|$。

**段階2（外の節点）.** $\eta\notin\mathrm{St}$ とする。
- **(2a)** $\mathbf x_\eta$ は $M$ の上にある（$W$ の内容が $M$ だから）。よって $\lambda_M(A_\eta)\le|\mathbf x_\eta|$。逆に、$\eta$ の部分木を、長さ $\lambda_M(A_\eta)$ で $M$ の上にある組の導出で置き換える (F1)。$\eta$ の部分木に印はないので (b) が成り立ち、加わる文字は $M$ に入るので (c) も成り立つ。原理から語は短くならないので、$|\mathbf x_\eta|=\lambda_M(A_\eta)$。
- **(2b)** $\mathrm{St}$ の外の道でもラベルは相異なる。(1c) と同じく圧縮すればよい（印は関係しない）。

**段階3（重い節点）.** $\eta\notin\mathrm{St}$ で $\lambda_M(A_\eta)>\bar\theta$ のとき、$\eta$ を**重い**と呼ぶ。そうでない外の節点を**軽い**と呼ぶ。
- **(3a) 重い節点の容量は $\ge1$.** $A:=A_\eta$ を左辺とする規則 $R$ をとる（$\eta$ の規則でよい）。厚さの定義より、$R$ を使う成功導出で長さ $\theta_G(R)\le\bar\theta$ の文がある。その $R$ の節点の内側 $\mathbf y\in\mathrm{In}(A)$ は $|\mathbf y|\le\bar\theta<\lambda_M(A)$ をみたす。よって $\mathbf y$ は $M$ の上になく、$\overline M$ の文字を含む。
- **(3b) 重さは上に閉じる.** 外の節点 $\eta'$ が重く、その親 $\eta$ も外にあれば、$\lambda_M(A_\eta)=|\mathbf x_\eta|\ge|\mathbf x_{\eta'}|=\lambda_M(A_{\eta'})>\bar\theta$。よって $\eta$ も重い。したがって軽い節点の部分木はすべて軽く、重い節点の全体 $H$ は、$\mathrm{St}$ の節点の子を根とする部分木の森をなす。
- **(3c) $H$ の葉は $\le\kappa_{\overline M}$ 個.** $H$ の葉（重い子をもたない重い節点）を $\eta_1,\dots,\eta_q$ とすると、これらは互いに比較不能である。各 $\eta_i$ の部分木を、(3a) の $\overline M$ の文字を含む組の導出で置き換える。部分木どうしは交わらないので、置き換えは同時にできる (F1)。結果は $L$ の語で、$\overline M$ の文字を $\ge q$ 個含む（nondeleting なので、置き換えた組の文字はすべて残る）。よって $q\le\kappa_{\overline M}$。
- **(3d)** $H$ の各節点は、その森の根からある葉への道の上にある。そのような道は $\mathrm{St}$ の外にあるので、(2b) により節点数は $\le|V|$。よって $|H|\le\kappa_{\overline M}|V|$。

**段階4（数える）.** $W$ の出現は、それを書く節点で分類できる。
- $\mathrm{St}\cup H$ の節点が書くもの：$\le|\mathrm{St}\cup H|\,\rho_{\max}$ 個。
- 軽い節点が書くもの：各軽い節点は、親が $\mathrm{St}\cup H$ に属する軽い節点（「最上の軽い節点」）のどれか一つの部分木に属する（3b）。最上の軽い節点は $\le r|\mathrm{St}\cup H|$ 個あり、それぞれの部分木の出現数は $|\mathbf x|=\lambda_M\le\bar\theta$ である（2a）。

よって $\mu\le|\mathrm{St}\cup H|(\rho_{\max}+r\bar\theta)\le(2k-1+\kappa_{\overline M})|V|(\rho_{\max}+r\bar\theta)$。根は $\mathrm{St}$ に属するので（$k\ge1$）、根が軽いという場合は生じず、$\max\{\bar\theta,\cdot\}$ は不要である。∎

**系 M1 [証明済み].** $|V|,r,\rho_{\max}\le\|G\|$ なので $\mu_M(L)\le2(2|M|-1+\kappa_{\overline M})\|G\|^2\bar\theta_G$。$\Sigma$ を固定すれば、$\kappa_{\overline M}$ が多項式である限り $\mu_M$ も多項式である。

### 2.2 一般化：Parikh 錐（定理 P）

Parikh 写像を $\varphi:\Sigma^*\to\mathbb N^\Sigma$ とし、$p\in\mathbb N^\Sigma$、$|p|:=\sum_\sigma p(\sigma)$、$\mathrm{supp}(p)\subseteq M$ とする。
$$\mu_{p,M}(L):=\min\{|w|:w\in L,\ \varphi(w)\ge p,\ c(w)\subseteq M\}.$$

**定理 P [証明済み].** $\kappa_{\overline M}<\infty$ で、$\mu_{p,M}(L)<\infty$ とする。
- $|p|\ge1$ なら $\mu_{p,M}(L)\le(2|p|-1+\kappa_{\overline M})|V|(\rho_{\max}+r\bar\theta)$。
- $p=0$ なら $\mu_{0,M}(L)\le\max\{\bar\theta,\ \kappa_{\overline M}|V|(\rho_{\max}+r\bar\theta)\}$。

*証明.* 定理 M の証明で、内容 $M$ の条件を「$\varphi\ge p$ かつ $c\subseteq M$」に置き換え、$p(\sigma)$ 個の $\sigma$ の出現に印を付ける（印は計 $|p|$ 個）。
- 原理の (b)・(c) から、$\varphi(\text{新しい語})\ge p$ と $c\subseteq M$ が出る。Parikh ベクトルは可換なので、文字の順序は関係しない。
- 段階1〜4 は字句どおり通る。
- $p=0$ では $\mathrm{St}=\emptyset$ で、根は外の節点になる。根が軽ければ $\mu\le\bar\theta$。重ければ $H$ は根を含む部分木で、根を $\mathrm{St}$ の代わりにして同じく数えればよい。∎

**注.**
- $p=\mathbf 1_M$（$M$ の各文字を1つずつ）が定理 M である。
- $U_1$ 型付けで $M=\Sigma_1$、$p=0$ とすると、型 $1$ の語は内容が $\Sigma_1$ に入る語なので、原稿の命題 9.2（`prop:zeta-capacity`）の内部評価そのものになる。定理 P は両者を一つにまとめたものである。

### 2.3 確認すべき点

- **区間の定義と分岐点.** §2.1 段階1の (1a)〜(1c) と「分岐点の扱い」のとおり。区間を「$\mathrm{Mk}$ が一定の極大な鎖」と定義すれば、分岐点は自分の鎖の最下端に属する。圧縮は鎖の内部でしか行わないので、印が保たれる。依頼文の案 3. はこれで正しい。
- **$M=\Sigma$ の場合.** $\kappa=0$ となり、$\mu_\Sigma\le(2|\Sigma|-1)|V|(\rho_{\max}+r\bar\theta)$。既知の事実と矛盾しない。
  - 同じ論法は、印を「規則の集合 $Q$ の各規則を使う節点」に置き換えても通る。このときは段階3が不要になる（外の節点には内容の制約がなく、$\lambda(A)\le\bar\theta$）。よって $Q$ のすべての規則を使う最短の語は $\le(2|Q|-1)|V|(\rho_{\max}+r\bar\theta)$。$|Q|=1$ で $\theta_G(R)\le\bar\theta$ と整合し、$Q=P$ でも多項式である。Yoshinaka の標本が $\sum_R\theta(R)$ で抑えられることとも合う。
  - 因子 $\bar\theta$ は除けない：$X_i\to X_{i-1}X_{i-1}$、$X_0\to\mathtt a\mid\mathtt b$ では $\mu_\Sigma=\bar\theta=2^n$。
- **`thm:two-letter-content`（定理 8.6）との関係.** 矛盾しない。定理 M は $\kappa_{\overline M}=\infty$ のとき空虚で、二文字では $\kappa=\infty$ の目標（例えば $\Sigma^+$）が普通にある。定理 8.6 はその場合も含めて多項式を与えるので、定理 M より強い。
- **`prop:binary-u1-quadratic`（命題 7.8）との関係.** 依頼文の見込みには訂正が要る。命題 7.8 の下界は、実は稀な型の語による。原稿の本文にあるとおり、純な語 $\mathtt a^{2^{m+n}}$ が型 $1$（内容 $\{\mathtt a\}$）の唯一の語である。それでも矛盾しないことを一行で言うと、次のとおり。
  > $\kappa_{\mathtt b}(L_{m,n})=2^n\le\bar\theta=2^m+2^n-1$ なので、定理 M は $\mu_{\{\mathtt a\}}\le(1+2^n)|V|(1+2\bar\theta)=O(\|G\|\bar\theta^2)$ を許し、$\mu=2^{m+n}\approx\bar\theta^2/4$ はその範囲に収まる。
  
  定理 M はむしろ、二次の下界が「線形の $\kappa$」と「線形の $\lambda$」の積であることを示している。スクリプト [2b] で $\mu_{\mathtt a}=2^{m+n}$、$\kappa_{\mathtt b}=2^n$、$\bar\theta=2^m+2^n-1$ を確かめた [観察]。
- **ファンアウト1の否定例との関係.** 命題 7.1 の $L_n\in\mathcal C_{1,c_\Sigma}$ では、$\mu_{\{\mathtt a,\mathtt b\}}=3\cdot2^n-2$、$\kappa_{\mathtt c}=2^n$ である [観察（スクリプト [2]）。$\kappa_{\mathtt c}$ は $\mathrm{cap}(E_i)=\max(2\,\mathrm{cap}(E_{i-1}),\mathrm{cap}(E_{i-1})+2)$ からも直ちに出る]。定理 M の要求「$\kappa$ が超多項式」は、ファンアウト1の実際の否定例でみたされている。したがって定理 M は**ファンアウト1と2を分けない**。分けるのは、原稿の定理 8.2（冪の移送）の側である。

### 2.4 帰結（依頼文どおり）

**系 M2 [証明済み].** 道具1（稀な型）で `op:fanout-two` を肯定的に解くには、ある内容 $M$ について $\kappa_{\overline M}(L_n)\ge\mu_M(L_n)/(|V|(\rho_{\max}+r\bar\theta))-(2|M|-1)$ が $\|G_n\|,\bar\theta_{G_n}$ について超多項式でなければならない。第2回の報告で残っていた内容型付けの「隙間」（$\mathtt b$ を欠くだけの短い導出）は、印によって閉じる。

---

## 3. 課題2：道具2（区別する部分標的）

### 3.1 (a) 容量の議論は道具2にどこまで一般化できるか

定理 M の論法が使うのは、目標の集合 $X$（ここでは $L\setminus L'$）について次の二つである。
- **(U)** 有界個の印が残る限り、圧縮しても $X$ から出ない。
- **(D)** 印の外の部分木を「局所的に良い」組に置き換えても $X$ から出ない。ここで「局所的」とは、良さが置き換える組だけで決まること（内容 $\subseteq M$ がその例）である。

これに合う $L'$ の形を三つ挙げ、合わない形も述べる。

**(a-i) 型の集合（`lem:type-deletion` 型）.** $L'=L\setminus c_\Sigma^{-1}(\mathcal Q)$ なら $L\setminus L'=\bigcup_{M\in\mathcal Q}L\cap c^{-1}(M)$ で、$\min|L\setminus L'|=\min_{M\in\mathcal Q}\mu_M$。これは定理 M に帰着する [証明済み]。

**(a-ii) 散在部分語による証拠（定理 W）.** $u\in M^+$、$k:=|u|$ について $\mathrm{Up}(u):=\{w: u\sqsubseteq w\}$（$\sqsubseteq$ は散在部分語）とし、
$$\mu_{u,M}(L):=\min\{|w|:w\in L\cap\mathrm{Up}(u)\cap M^+\}$$
とおく。

**定理 W [証明済み].** $G$ が既約で良く（nonpermuting を使う）、ファンアウト $\le f$、rank $\le r$ とする。$\kappa_{\overline M}<\infty$ で $\mu_{u,M}<\infty$ なら
$$\mu_{u,M}(L)\le\Bigl((2k-1)\tbinom{k+f-1}{f-1}+\kappa_{\overline M}\Bigr)|V|(\rho_{\max}+r\bar\theta).$$
$f=1$ では因子は $1$ で、定理 M と同じ定数になる。

*証明.* 長さ $\mu_{u,M}$ で $\mathrm{Up}(u)\cap M^+$ に入る語の導出木のうち、節点数が最小の $T$ をとる。$u$ の一つの埋め込みの $k$ 個の出現を印とする。印は語の中の位置の順に並べておく。

原理は定理 M と同じだが、(b) を「印がすべて残り、**相対順序も保たれる**」に強める。そうすれば新しい語も $u$ を散在部分語として含む。

- **外の節点の置き換え (F1).** 文脈が固定されるので、文脈にある印の順序は保たれる。よって段階2・3は字句どおり通る。
- **$\mathrm{St}$ の圧縮だけが問題になる.** ファンアウト $\ge2$ では、圧縮で順序が崩れうる（例は下の (c)）。そこで節点 $\eta$（$\mathrm{fan}(A_\eta)=d$）の**署名**を
$$\sigma(\eta):=\bigl(A_\eta,\ \mathrm{Mk}(\eta),\ \pi_\eta\bigr)$$
と定める。$\pi_\eta:\mathrm{Mk}(\eta)\to\{1,\dots,d\}$ は、各印が $\mathbf x_\eta$ の何番目の成分にあるかを表す写像である。
  - nonpermuting な規則だけからなる導出では、各節点の組の成分は最終的な語の中で $1,\dots,d$ の順に現れる（規則ごとの帰納法）。よって $\pi_\eta$ は印の順序について単調非減少で、$\mathrm{Mk}$ を固定すると $\pi_\eta$ の候補は $\le\binom{k+f-1}{f-1}$ 個である。
- **主張：同じ類の $\eta$ とその子孫 $\eta'$ が同じ署名をもてば、(F2) の圧縮は印の相対順序を保つ.**
  - $\mathbf x_\eta=(y_1,\dots,y_d)$、$\mathbf x_{\eta'}=(z_1,\dots,z_d)$ とし、$z_i$ が入っている $y$ の成分の番号を $j(i)$ とする。
  - 印 $m$ が $z_i$ にあれば、$\pi_{\eta'}(m)=i$ かつ $\pi_\eta(m)=j(i)$ である。署名が等しいので $j(i)=i$。
  - 外の文脈 $o_\eta=o_0\square_1o_1\cdots\square_do_d$ にある印と $z_i$ の中の印の前後関係は、「$o_t$ の $t<i$ か $t\ge i$ か」だけで決まり、これは圧縮の前後で変わらない（前は $y_i$ の中、後は穴 $i$ の中にある）。
  - $z_i$ と $z_{i'}$（$i<i'$）の中の印は、前後どちらでも $z_i$ が先にある。$\eta$ の部分木にあって $\eta'$ の部分木にない部分に印はない（$\mathrm{Mk}$ が等しい）。
  - よって相対順序は保たれる。
- **数える.** 一つの類（鎖）の中で、同じ署名は二度現れない。現れれば圧縮できて、原理に反する。よって鎖の長さは $\le|V|\binom{k+f-1}{f-1}$。類は $\le2k-1$ 個なので $|\mathrm{St}|\le(2k-1)\binom{k+f-1}{f-1}|V|$。以下は段階3・4のとおり。∎

**系 W（道具2への適用）[証明済み].** $L,L'\in\mathcal C_{f,c_\Sigma}$、$L'\subsetneq L$ とし、$G$ を $L$ の既約で良い表示とする。ある $u\in M^+$ について
$$\emptyset\ne L\cap\mathrm{Up}(u)\cap M^+\subseteq L\setminus L'$$
なら、$\min|L\setminus L'|\le\bigl((2k-1)\binom{k+f-1}{f-1}+\kappa_{\overline M}\bigr)|V|(\rho_{\max}+r\bar\theta)$。より一般に、$U$ が散在部分語の順序で上に閉じた集合で、$\emptyset\ne L\cap U\cap M^+\subseteq L\setminus L'$ なら、$k$ を $U$ の極小元の最大長として同じ評価が成り立つ。Higman の補題により極小元は有限個で、$L\cap U\cap M^+$ の任意の語は、ある極小元 $u$ について $L\cap\mathrm{Up}(u)\cap M^+$ に入る。

**(a-iii) 文法の部分（規則の部分集合 $P'\subseteq P$）.** $Q:=P\setminus P'$、$L':=L(G')$ とする。
- $L\setminus L'$ は「どの導出も $Q$ を使う語」の集合で、$U_Q:=\{w\in L:\ Q\text{ を使う導出がある}\}$ に含まれる。
- 等号 $L\setminus L'=U_Q$ が成り立つ場合（例えば $G$ が曖昧でない場合）は、$\min|L\setminus L'|\le\min_{R\in Q}\theta_G(R)\le\bar\theta$ となって自明である [証明済み]。
- 一般には、厚さを与える $R\in Q$ の短い文が、別の $Q$ を使わない導出で $L'$ に入りうる。つまり (U) に当たる「$Q$ を使うことが保たれれば $X$ にとどまる」が**曖昧さのために崩れる**。容量の論法は、$L$ の語の性質ではなく導出の性質しか保たないからである。

**(a-iv) 正則言語との共通部分 $L'=L\cap R$.**
- $\Sigma^*\setminus R$ が「散在部分語で上に閉じた集合 $\cap$ 内容 $\subseteq M$」の和なら、(a-ii) に入る。
- 一般には効かない。理由は二つある。
  - (1) 圧縮と置き換えは文字を除く操作なので、除くことで変わる性質は保たれない。例えば $L\setminus L'=L\cap\{\#_{\mathtt a}\not\equiv0\bmod q\}$（原稿の命題 2.9(iii) によりクラスに入る形）は (U) をみたさない。ただしこの種の可換群の剰余類は、2026-11-01〜07 の閉じた道（$\mu_{\mathtt{ab}}\le\max\{9(r+1)v\theta,226v^3\theta^3\}$）で扱い済みである。
  - (2) 印の**連続性や隣接**に依存する性質は、外の置き換えでは保たれる。しかし圧縮では、署名を固定しても、隣接が「間に $o_t$ が入る」形で壊れうるかどうかを確かめていない。これは [予想]（因子の証拠でも定理 W と同型の評価が成り立つ）として残す。

**(c) なぜファンアウト $f$ で因子 $\binom{k+f-1}{f-1}$ が出るか [証明済み＋観察].** 規則 $A(x_1\mathtt c x_2,\ \mathtt d)\leftarrow A(x_1,x_2)$ は良い（$\varepsilon$-free、nondeleting、nonpermuting、nonmerging）。
- $S(x_1\mathtt e x_2)\leftarrow A(x_1,x_2)$、$A(\mathtt a,\mathtt b)$ とあわせると、$\mathtt{acbed}\in L$ になる（$A$ の節点が2つ）。
- 上の $A$ の部分木を下のもので置き換えると $\mathtt{aeb}$ になり、$\mathtt b$ と $\mathtt e$ の前後が入れ替わる。
- 下の $A$ の第2成分 $\mathtt b$ が、上の $A$ では第1成分 $\mathtt{acb}$ の中にあるからで、署名の $\pi$ が異なる場合に当たる。
- ファンアウト1では $j(i)=i$ が自動的に成り立つので、この因子は出ない。

これは上界の論法がファンアウトで変わる箇所である。しかし評価は依然として多項式なので、境界がファンアウトで動くことを示すものではない。

### 3.2 (b) 道具2が稀な型より本当に強い例

**命題 B [証明済み].** $n\ge2$ について $L_n:=\{\mathtt{ab},\ \mathtt b\mathtt a^n\}$、$L'_n:=\{\mathtt{ab}\}$ とする。
- (i) $L_n,L'_n\in\mathcal C_{2,c_\Sigma}$（$\Sigma=\{\mathtt a,\mathtt b\}$。実際はすべての $f$ で）。
- (ii) 道具1が与えるのは $\mu_{\{\mathtt a,\mathtt b\}}(L_n)=2$ だけである（$L_n$ に現れる内容は $\{\mathtt a,\mathtt b\}$ のみ）。一方、道具2は $\mathtt b\mathtt a^n$（長さ $n+1$）を特徴標本に強制する。
- (iii) $n=2^t$ のとき、$S\to\mathtt{ab}\mid\mathtt bX_t$、$X_j\to X_{j-1}X_{j-1}$、$X_0\to\mathtt a$ は $L_n$ の既約で良い表示で、$\|G\|=O(t)$、$\bar\theta=n+1$。

*証明 (i).* $L'_n$ は一語なので、各組の分布は高々1点である。共通の文脈をもつ同じ型の組は等しいので、条件は自明に成り立つ。以下 $L:=L_n$ とする。
- **$d=1$.**
  - 内容 $\{\mathtt b\}$ の因子は $\mathtt b$ だけである。
  - 内容 $\{\mathtt a\}$ の因子は $\mathtt a^j$（$1\le j\le n$）で、$\mathcal D(\mathtt a^j)=\{(\mathtt b\mathtt a^h,\mathtt a^q):h+j+q=n\}\cup(\{(\varepsilon,\mathtt b)\}\text{ if }j=1)$。二つの $\mathtt a^j,\mathtt a^{j'}$ が文脈を共有すれば、それは $(\mathtt b\mathtt a^h,\mathtt a^q)$ の形なので $j=j'$、または $(\varepsilon,\mathtt b)$ なので $j=j'=1$。
  - 内容 $\{\mathtt a,\mathtt b\}$ の因子は $\mathtt{ab}$ と $\mathtt b\mathtt a^j$（$1\le j\le n$）で、$\mathcal D(\mathtt{ab})=\{(\varepsilon,\varepsilon)\}$、$\mathcal D(\mathtt b\mathtt a^j)=\{(\varepsilon,\mathtt a^{n-j})\}$。共有が起こるのは $\mathtt{ab}$ と $\mathtt b\mathtt a^n$ の $(\varepsilon,\varepsilon)$ だけで、どちらの分布も $\{(\varepsilon,\varepsilon)\}$ に等しい。
- **$d=2$.** 許容文脈では $v_1\ne\varepsilon$ なので、長さ $\ge3$ の語にしか現れない。つまり $E[\mathbf x]=\mathtt b\mathtt a^n$ である。
  - $x_1$ が $\mathtt b$ を含めば、$v_0=\varepsilon$、$x_1=\mathtt b\mathtt a^i$、$x_2=\mathtt a^j$ となり、$\mathcal D(\mathbf x)=\{(\varepsilon,\mathtt a^p,\mathtt a^q):p\ge1,\ i+p+j+q=n\}$。これは $i+j$ だけで決まる。
  - $x_1$ が $\mathtt a$ だけからなれば、$\mathtt b$ は $v_0$ の先頭にあり、$\mathcal D(\mathbf x)=\{(\mathtt b\mathtt a^h,\mathtt a^p,\mathtt a^q):p\ge1,\ h+i+p+j+q=n\}$。これも $i+j$ だけで決まる。
  - $x_2$ が $\mathtt b$ を含むことはない（$\mathtt b$ は先頭にしかない）。
  - 同じ成分の型で文脈を共有すれば、$i+j$ が等しく、同じ場合分けに入るので、分布は等しい。

  よって $(2,c_\Sigma)$-代入可能である。どちらも有限言語なので 2-MCFL である。∎

*(ii)* 内容 $\{\mathtt a,\mathtt b\}$ の最短語は $\mathtt{ab}$ なので、道具1は $\mathtt{ab}$ しか強制しない。$L'_n\subsetneq L_n$ でどちらもクラスに入るので、補題 4.5 より、特徴標本は $L\setminus L'=\{\mathtt b\mathtt a^n\}$ を含む。∎

*(iii)* 厚さは $\bar\theta=n+1$（$X$ の規則を使う文は $\mathtt b\mathtt a^n$ だけ）で、大きさは数えれば出る。∎

**評価.**
- 命題 B は、道具2が道具1より絶対値で強い（$2$ 対 $n+1$）ことを示す最小の例である。
- しかし $\bar\theta$ に対しては強くない。$\min|L\setminus L'|=\bar\theta$ であり、これは系 W（$u=\mathtt{ba}$、$M=\{\mathtt a,\mathtt b\}$、$\kappa=0$）の評価にも収まる。
- 既知の $\{\mathtt{aab},\mathtt{baa}\}\supsetneq\{\mathtt{aab}\}$ も同じで、$L\setminus L'=\{\mathtt{baa}\}=L\cap\mathrm{Up}(\mathtt{ba})\cap\{\mathtt a,\mathtt b\}^+$ である。所属は有限言語の網羅検査で確かめた [観察（網羅）]。

**超多項式への延長について [証明済みの否定的結果＋未解決].** 系 W により、位置で分ける部分標的を伸ばした族が超多項式になるためには、次のどちらかが必要である。
- (α) $L\setminus L'$ の語 $w$ について、$\kappa_{\overline{c(w)}}$ が超多項式であること。
- (β) $w$ が $L\setminus L'$ に入ることが、どの短い部分語 $u\sqsubseteq w$ でも証拠づけられないこと。つまり、$u\sqsubseteq w'$、$c(w')\subseteq c(w)$ をみたす $w'\in L'$ がつねにあること。

「$\mathtt{aab}$ と $\mathtt{baa}$」型の延長、すなわち $L\setminus L'$ を $\mathtt b$ の位置で切り出すもの（例：$\{\mathtt a^{N}\mathtt b,\mathtt b\mathtt a^{N}\}$ 型や、多ブロックでの $\mathtt b$ の配置）は、短い部分語 $\mathtt{ba}$ や $\mathtt b\mathtt a^j$ で証拠づけられるので、(β) に入らない。超多項式の族は見つかっていない。

(β) の候補は、ブロック長の大小比較のような「長距離の比較」で決まる差である（例：$\mathtt a^i\mathtt b\mathtt a^j$ で $i>j$）。ただし、この種の言語は補題5（$\mathtt a$ と $\mathtt{aa}$ の分布の共有）にかかりやすく、所属は確かめていない。

### 3.3 (c) $\tau$ と道具2の関係（下界の完全性）

**命題 H.** $L\in\mathcal C_{f,s}$ とし、$\mathcal F_L:=\{L\setminus L':L'\in\mathcal C_{f,s},\ L'\subsetneq L\}$ とおく。$h(L):=\min\{\|F\|_+:F\subseteq L\text{ が有限で、}\mathcal F_L\text{ のすべての元と交わる}\}$ と定める。
- **(i) [証明済み]** 標準作用素 $B^{\le r}_{f,s}$、$B_{f,s}$ と、クラス全体で特徴標本をもつ集合駆動作用素について、任意の特徴標本 $F$ は $\|F\|_+\ge h(L)$ をみたす。また $h(L)\ge\max_{X\in\mathcal F_L}\min_{w\in X}|w|$ であり、互いに交わらない $X_1,\dots,X_q\in\mathcal F_L$ について $h(L)\ge\sum_i\min_{w\in X_i}|w|$。
- **(ii) [条件付き]** 作用素 $B$ が $L$ 上で健全（$K\subseteq L$ なら $L(B(K))\subseteq L$。原稿の命題 3.10）かつ標本無矛盾（$K\subseteq L(B(K))$）で、さらに

  > **(Hyp)** すべての有限 $K\subseteq L$ について $L(B(K))\in\mathcal C_{f,s}$

  をみたすとする。このとき、有限の $F\subseteq L$ が $B$ の特徴標本であることと、$F$ が $\mathcal F_L$ のすべての元と交わることは同値である。したがって最短の特徴標本の長さは $h(L)$ に等しい（$\varepsilon$ の扱いは原稿どおり）。

*証明.*
- (i) 前半は、補題 4.5 をすべての $L'$ に適用したものである。後半の二つの不等式は、打撃集合の定義から直ちに出る。
- (ii) 「特徴標本 ⇒ 交わる」は (i) である。逆を示す。$F$ がすべてと交わり、$F\subseteq K\subseteq L$ を有限とする。$L'':=L(B(K))$ は健全性から $\subseteq L$、無矛盾性から $\supseteq K\supseteq F$、(Hyp) から $\in\mathcal C_{f,s}$ である。$L''\ne L$ なら $L''\in\mathcal C_{f,s}$、$L''\subsetneq L$ となり、$F\cap(L\setminus L'')=\emptyset$ で仮定に反する。よって $L(B(K))=L$。∎

**帰結（問いの整理）.** 依頼文の「$\tau$ が超多項式なら道具2の下界が出るか」は、次の二つの問いに分かれる。
- **Q1（Hyp）.** 標準作用素の仮説はクラスに入るか。入れば、データの下界は差集合族 $\mathcal F_L$ だけで決まる。
- **Q2（打撃と最大最小の差）.** $h(L)$ は $\max_X\min|X|$（道具2を一つの $L'$ で使うもの）と多項式で結びつくか。

$\tau$ は上界（系 4.8）にしか現れない。したがって (Hyp) のもとでは、「$\tau$ が超多項式 ⇒ 下界」は「$\tau\le\mathrm{poly}(h(L))$」、つまり上界の解析が多項式の範囲で最適であることと同値である。どちらの問いも未解決である。

Q2 について一つ証明した。これは、自然に思いつく「指数個の互いに交わらない差」の例が働かないことを示す。

**補題 S [証明済み].** $|\Sigma|\ge2$、$n\ge3$、$f\ge1$ とする。
- (i) $\Sigma^n\in\mathcal C_{f,c_\Sigma}$。
- (ii) $\Sigma^n\setminus\{w\}\in\mathcal C_{f,c_\Sigma}$ と、$w$ がある文字のべき $\sigma^n$ であることは同値である。
- (iii) 任意の内容 $M$ について $\Sigma^n\setminus c^{-1}(M)\in\mathcal C_{f,c_\Sigma}$（補題 4.4）。

*証明.*
- (i) $\Sigma^n$ では、$E\in\mathcal D(\mathbf x)$ は $|E|_{\mathrm{fix}}=n-|\mathbf x|$ だけで決まる。共有があれば全長が等しく、分布も等しい。
- (ii)「⇐」：$L'=\Sigma^n\setminus\{\sigma^n\}$ とする。
  - 成分のどこかに $\sigma$ 以外の文字を含む組では、$E[\mathbf x]\ne\sigma^n$ がつねに成り立つので、分布は「全長が合うすべての許容文脈」になる。同じ型の $\mathbf y$ も同じ文字を含むので、共有すれば分布は等しい。
  - すべての成分が $\sigma$ だけからなる組 $(\sigma^{i_1},\dots,\sigma^{i_d})$ の分布は、「全長が合い、$\sigma$ だけではない許容文脈」で、$\sum i_t$ だけで決まる。
- (ii)「⇒」：$w$ が二種類の文字を含めば、ある位置で $w=p\sigma\tau q$、$\sigma\ne\tau$ と書ける。$x=\sigma\tau$、$y=\tau\sigma$ は同じ内容である。両方を受理する文脈がある：$|p'|=i$ を固定すると、$p'\sigma\tau q'=w$ と $p'\tau\sigma q'=w$ は両立せず（$w[i{+}1..i{+}2]$ が $\sigma\tau$ か $\tau\sigma$ かで決まる）、それぞれ $(p',q')$ を一意に決める。よって「どちらかを拒む」文脈は高々 $n-1$ 個で、長さ $n-2$ の文脈 $(n-1)|\Sigma|^{n-2}\ge2(n-1)$ 個より少ない（$n\ge3$）。一方、文脈 $(p,q)$ は $y$ を受理し（$p\tau\sigma q\ne w$）、$x$ を受理しない。よって分布は等しくない。
- (iii) は補題 4.4。∎

したがって $\Sigma^n$ の部分標的は、内容ごとの削除と単一文字のべきの削除で尽きる。$\mathcal F_{\Sigma^n}$ の互いに交わらない元は $O(2^{|\Sigma|})$ 個しかなく、$h(\Sigma^n)$ は $\sum_M\mu_M$ と同じ大きさである。スクリプト [6] で、$\{\mathtt a,\mathtt b\}^{3,4}$、$\{\mathtt a,\mathtt b,\mathtt c\}^3$ の単一の削除を網羅的に調べ、(ii) と一致した [観察（網羅）]。

---

## 4. 試した候補の表（課題3は最小限）

課題3（新しい否定の族の設計）は、本格的には行っていない。代わりに、内容型付け版の系6を確定させた。

**系 6c [証明済み].** $L\in\mathcal C_{f,c_\Sigma}$（$f\ge1$）とする。
- (a) $w\in L$、$uwv\in L$、$c(u)\cup c(v)\subseteq c(w)$ なら、すべての $n\ge0$ について $u^nwv^n\in L$。
- (b) さらに $\kappa_{\overline M}(L)<\infty$ なら、(a) の状況で $uv\in M^*$。

*証明.*
- (a) $c(uwv)=c(w)$ なので、補題5より $\mathcal D^{(1)}_L(uwv)=\mathcal D^{(1)}_L(w)\ni(u,v)$、すなわち $u^2wv^2\in L$。内容は不変なので、帰納法で一般の $n$ に及ぶ。
- (b) $uv$ が $\overline M$ の文字を含めば、$u^nwv^n$ の $\overline M$ の文字の数は $n$ とともに増え、$\kappa_{\overline M}<\infty$ に反する。よって $uv\in M^*$。∎

| 対象 | ファンアウト | $\|G\|$ | $\bar\theta$ | 量 | $\kappa$ | 状態 |
|---|---|---|---|---|---|---|
| $L_n$（命題 7.1） | 1 | $13n+7$ | $4n$ | $\mu_{\mathtt{ab}}=3\cdot2^n-2$ | $\kappa_{\mathtt c}=2^n$ | $\mathcal C_{1,c}$ に入る。定理 M と整合。$\mathcal C_{2,s}$ には入らない（定理 8.2） |
| $L_{m,n}$（命題 7.8） | 1 | $6m+6n+9$ | $2^m+2^n-1$ | $\mu_{\mathtt a}=2^{m+n}$ | $\kappa_{\mathtt b}=2^n$ | 二次は $\kappa\cdot\lambda$ の積として現れる（§2.3） |
| $\{\mathtt{ab},\mathtt b\mathtt a^n\}\supsetneq\{\mathtt{ab}\}$ | 任意 | $O(\log n)$ | $n+1$ | $\min|L\setminus L'|=n+1$ | $0$ | 命題 B。道具2 > 道具1（絶対値）。系 W の範囲内 |
| $\{\mathtt{aab},\mathtt{baa}\}\supsetneq\{\mathtt{aab}\}$ | 任意 | — | — | $3$ | $0$ | 系 W の範囲内（$u=\mathtt{ba}$） |
| $\Sigma^n\setminus\{w\}$ | 任意 | — | $n$ | — | — | 補題 S：クラスに入るのは $w=\sigma^n$ のときだけ |

---

## 5. 否定例の必要条件（更新版）

$L_n\in\mathcal C_{2,c_\Sigma}$ で、特徴標本の長さが $\|G_n\|,\bar\theta_{G_n}$ について超多項式になる族を否定例と呼ぶ。

- **N1–N4, N6**：第1・2回のまま。
- **N5'（定理 M・P、証明済み）**：稀な内容 $M$ による否定例なら、$\kappa_{\overline M}\ge\mu_M/(|V|(\rho_{\max}+r\bar\theta))-(2|M|-1)$ が超多項式。
- **N6'（系 6c、証明済み）**：$w,uwv\in L$、$c(uv)\subseteq c(w)$ なら反復で閉じる。$\kappa_{\overline M}<\infty$ のもとでは $uv\in M^*$。
- **N7（新、証明済み）**：N5' はファンアウトを分けない。命題 7.1 の $L_n$ はファンアウト1で N5' をみたす。ファンアウト2で新たに効く制約は、現状では冪の移送（定理 8.2）と2-組の代入可能性だけである。
- **N8（新、系 W、証明済み）**：道具2で一つの $L'$ による否定例なら、$L\setminus L'$ のどの短い $\kappa$ の語 $w$ についても、$w$ のどの短い部分語 $u$ にも、$u\sqsubseteq w'$、$c(w')\subseteq c(w)$ をみたす $w'\in L'$ がなければならない。
- **N9（新、命題 H、条件付き）**：(Hyp) のもとでは、否定例は $h(L)$ が超多項式であることと同値である。すなわち、一つの長い差か、多項式長の差が超多項式個互いに交わらずにあること。$\Sigma^n$ のような「自由」な目標では後者は起こらない（補題 S）。

---

## 6. 次の一手（3つ以内）

1. **(Hyp) の検証（Q1）.** 標準作用素 $B_{f,s}$ の仮説 $L(B(K))$ が $(f,s)$-代入可能かを調べる。正しければ、`op:fanout-two` は差集合族の打撃問題に完全に帰着する（命題 H）。まず小さい $K$ で計算し、反例が出れば (Hyp) を弱めた形（例えば $L(B(K))\supseteq$ ある $L''\in\mathcal C$）を探す。
2. **(β) 型の差の所属検査.** 短い部分語で証拠づけられない差、例えば $\mathtt a^i\mathtt b\mathtt a^j$ 型の長さの比較を、内容型付け $\Sigma=\{\mathtt a,\mathtt b,\mathtt c,\mathtt d\}$ のもとで、2-組の文脈で作れるかを試す。系 6c と補題5（$\mathtt a$ と $\mathtt{aa}$ の分布の共有）が最初の障害になるはずなので、最初に有界長検査で崩れ方を見る。
3. **ファンアウト2固有の制約の定量化.** N7 によれば、容量はファンアウトを分けない。定理 8.2 の冪の移送を「$\kappa$ を担う $\overline M$ の文字の配置」に当てはめ、ファンアウト1の $L_n$ のように $\kappa$ が二分木の葉に分散する形が2-組の条件でどこまで許されるかを調べる。これは否定・肯定のどちらの向きにも効く。

---

## 7. スクリプト

`check_claude_fanout2_content_round3_2026-11-09.py`（標準ライブラリのみ、約30秒、乱数の種 20261109）。第2回のスクリプトは手元になかったので、同じ機能を書き直した。

**機能.**
- MCFG をデータとして持ち、良い条件を assert で検査する。
- $\|G\|$、厳密な $\theta_G$（最小内側長と最小外側長の不動点）を計算する。
- $(A,\text{内容})$ ごとの最小長を厳密に動的計画法で求め、それから $\mu_M$ を得る。
- $\mathrm{cap}$ と $\kappa_{\overline M}$ を計算する（$|V|+1$ 回を超えて増え続けるものを $\infty$ と判定する）。
- 長さ $\le N$ の語を列挙する。
- 有限言語について、内容型付けでの $d\le2$ の代入可能性を**網羅的に**検査する。

**出力の要点 [観察（計算のみ）].**
- **[2]** $L_n$（$n\le8$）：$\|G\|=13n+7$、$\bar\theta=4n$、$\mu_{\mathtt{ab}}=3\cdot2^n-2$、$\kappa_{\mathtt c}=2^n$。定理 M の評価は成立。
- **[2b]** $L_{m,n}$：$\mu_{\mathtt a}=2^{m+n}$、$\kappa_{\mathtt b}=2^n$、$\bar\theta=2^m+2^n-1$。$\mu/\bar\theta^2$ は $0.10$〜$0.44$。
- **[3]** 乱択の既約で良い文法 1138 個（ファンアウト $\le2$、rank $\le2$、$\Sigma=\{\mathtt a,\mathtt b,\mathtt c\}$）で、$\mu_M$ が有限の組 2233 個（うち $\kappa$ 有限 1750 個）について、定理 M の違反は 0 個（比の最大は 1.000 で、$S\to\mathtt a$ のような自明な文法で等号）。厳密な動的計画法と列挙（長さ $\le9$）の照合 729 件で、不一致は 0 件。
- **[4]** 定理 W：長さ $\le9$ で見つかった 5570 件で違反は 0 件。
- **[5]** §3.1(c) の並べ替えの例 $\mathtt{acbed}\to\mathtt{aeb}$ を確認した。
- **[6]**
  - $\{\mathtt{ab},\mathtt b\mathtt a^n\}$（$n=2..6$）、$\{\mathtt{ab}\}$、$\{\mathtt{aab},\mathtt{baa}\}$、$\{\mathtt{aab}\}$ はすべてクラスに入る（網羅）。
  - $\Sigma^n\setminus\{w\}$ がクラスに入るのは $w=\sigma^n$ だけ（補題 S と一致）。
  - 内容ごとの削除もクラスに入る。

乱択検査は弱い確認にすぎず、証明は §2・§3 である。

# 二補題の独立検証報告（2026-10-31）

## 結論の表

| 対象 | 判定 | 根拠の節 |
|---|---|---|
| `lem:order-homogenize`（付録 A） | **正しいが記述に不足（不足している一文を §1.6 に提示）** | §1.1–§1.6 |
| `lem:app-u1-parikh`（付録 H） | **正しいが記述に不足（不足している一文を §2.11 に提示）** | §2.1–§2.11 |

**判定の意味。** 現行原稿の明示された仮定（reduced good grammar、非空成分、非空の二穴中間区切り、主定理での $r=r_{\max}\ge2$）の下では、両補題に反例・数式上の矛盾は見いだされず、全段を論理的に補完して証明できる。上の「不足」は**結論を変更する必要のない説明不足**であり、「修正可能な穴」や「誤り」を意味しない。ただし、依存補題の正しさは本書に記した範囲で検証したものであり、原稿全体の形式化・機械証明ではない。

**資料の取得状況（2026-10-31 時点）。** 指定された３ファイルはすべて GitHub 接続経由で取得できた。取得不能ファイルはない。一般の raw URL の直接取得は成功しなかったため、同じリポジトリのファイル内容を接続経由で読んだ。

- 現行原稿：[`02-v2-lg-fanout-boundary/main.tex`](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/main.tex)、**4,528 行**、Git blob SHA `0a4007b4f708441a630a46d18cf2263b9ba72dd3`。この版に行番号を付す。
- 旧監査：[`02_fixed-h-mcfg/revision/chatgpt_u1_parikh_theta4_audit_2026-10-30.md`](https://github.com/growupkuriyama-hub/Papers/blob/main/02_fixed-h-mcfg/revision/chatgpt_u1_parikh_theta4_audit_2026-10-30.md)、331 行、blob SHA `43ae813c67f2a20a5e1a621d34e9921a929311d3`。
- 別査読：[`reviews/deepseek_referee_2026-10-31.md`](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/reviews/deepseek_referee_2026-10-31.md)、397 行、blob SHA `349ca24c2f4ecc7c79177ac5197deeb39dda4a46`。

**独立性。** 以下の数学的検証は現行 `main.tex` の主張・仮定から行い、旧監査と別査読の結論は §3 で事後照合した。推測・計算結果と証明を混同しない。

---

## 1. `lem:order-homogenize` の検証

### 1.1 ステップ O1：同型対 $(t,t)$ と Erdős–Szekeres

**原文の引用（L2398–2402）。**

> “For $(t,t)$, Erd\H{o}s--Szekeres gives a monotone subsequence of length $m$.”

**主張。** $m'\ge(m-1)^2+1$ 個の相異なる実直線上の点 $p_t(i)$ を、元の添字順に見たとき、長さ $m$ の狭義単調部分列がある。

**検証。** Erdős–Szekeres の長さの定理は、相異なる $m'$ 個の数列に長さ $m$ の狭義増加部分列または長さ $m$ の狭義減少部分列が存在する十分条件が
\[
  m'\ge (m-1)(m-1)+1=(m-1)^2+1
\]
である、と述べる。増加ならすべての $i<j$ に $p_t(i)<p_t(j)$、減少ならすべての $i<j$ でこの不等式が偽である。したがって対象の真偽は一定。$m=m_j\ge N\ge3$ は当然満たす。

**判定：正しい。** $m'=m_j$ が $m_{j-1}$ の二乗型閾値であることと完全に一致する。

### 1.2 ステップ O2：補助補題 `lem:two-sequence` 自体

**原文の引用（L2358–2384）。**

> “Let $m\ge3$, $m'\ge(m-1)^2+1$ and $\mathrm{lt}\ldots$ be monotone in each argument with fixed directions.”

> “If columns are nonincreasing in $i$, let $J(i):=\min\{j>i:\mathrm{lt}(i,j)=1\}$”

> “If columns are nondecreasing, let $\kappa$ be the least index with $\mathrm{lt}(\kappa,\kappa+1)=1$”

**主張。** 三角領域 $i<j$ の二値関数が各行・各列について共通の向きで単調なら、$m'\ge(m-1)^2+1$ から、すべての前向き添字対で同色になる $m$ 添字を選べる。

**検証。** $\mathrm{lt}$ を $1-\mathrm{lt}$ に交換すると行の非増加は非減少になり、列の単調性も保たれる。よって行を非減少としてよい。

**列が非増加の場合：** 行 $i$ の最初の $1$ の列を $J(i)$ とし、存在しなければ $\infty$ とする。$i<i'$ なら $J(i)\le i'$ の場合は $J(i')>i'\ge J(i)$。$J(i)>i'$ の場合、$i'<j<J(i)$ で $\mathrm{lt}(i,j)=0$、列の非増加性から $\mathrm{lt}(i',j)=0$、したがって $J(i')\ge J(i)$。$J(i)=\infty$ の場合も、列の非増加性で $J(i')=\infty$ となる。ゆえに $J$ は非減少である。鎖
\[
  i_1=1,\qquad i_{a+1}=J(i_a)
\]
が $m$ 個の有限項を持てば、$a<b$ について $i_b\ge J(i_a)$、行の非減少性により $\mathrm{lt}(i_a,i_b)=1$。鎖が $L\le m-1$ 項で終わるなら、区間
\[
 [i_1,i_2),\ldots,[i_{L-1},i_L),[i_L,m']
\]
は $[m']$ を分割し、少なくとも一つは $\lceil m'/L\rceil\ge\lceil m'/(m-1)\rceil\ge m$ 個の添字を含む。その区間内では $i\ge i_a$ かつ $j<J(i_a)\le J(i)$ なので $\mathrm{lt}(i,j)=0$。末尾区間でも $J(i_L)=\infty$ である。十分な数の $0$ が得られる。

**列が非減少の場合：** 最初の隣接 $1$ の始点を $\kappa$、存在しなければ $\kappa=m'$ とする。$i\ge\kappa$ のとき、$\mathrm{lt}(\kappa,\kappa+1)=1$ を行方向に延長して $\mathrm{lt}(\kappa,i+1)=1$、さらに列の非減少性で $\mathrm{lt}(i,i+1)=1$。ゆえに全 $\kappa\le i<j$ は行の非減少性によって $1$。一方、$i<j\le\kappa$ なら $j-1<\kappa$ なので $\mathrm{lt}(j-1,j)=0$、列の非減少性で $\mathrm{lt}(i,j)\le0$。両区間 $[1,\kappa]$ と $[\kappa,m']$ の大きい方は $\lceil(m'+1)/2\rceil$ 個以上を含む。$m\ge3$ なら
\[
 (m-1)^2+1\ge2m-1,
\]
したがってこの個数は $m$ 以上になる。$1$ の隣接対が一つもない場合も前半の区間は全体で全 $0$ となる。

**判定：正しい。** 原文の「$J$ is nondecreasing」と「Then $\mathrm{lt}(i,j)=1$」は上記の単調性の連鎖が省略されているが、結論は成立する。

### 1.3 ステップ O3：異型対 $(t,u)$ に補助補題を適用

**原文の引用（L2400–2404）。**

> “For $t\ne u$ (both now monotone), relabel the current indices $1,\ldots,m'$”

> “for fixed $j$, monotone in $i$ in the direction opposite to $p_t$.”

**主張。** $(t,t)$ をすべて先に処理すると、異型対の比較行列は `lem:two-sequence` の行・列でそれぞれ方向一定の単調関数になる。

**検証。** すでにすべての型列 $p_t(i)$ は共通の選択添字列上で狭義増加か狭義減少である。固定 $i$ に対して $j$ を増やせば $p_u(j)$ は一定方向に変わる。よって $[p_t(i)<p_u(j)]$ も $p_u$ の向きに単調。固定 $j$ に対して $i$ を増やせば $p_t(i)$ が一定方向に変わるので、しきい値判定 $[p_t(i)<\text{constant}]$ は $p_t$ と**逆向き**に単調である。例えば $p_t$ 増加なら比較値は非増加、$p_t$ 減少なら比較値は非減少。方向は固定 $i$ や固定 $j$ に依存しない。元のインデックスの間隔は不要で、順序を保って $1,\ldots,m'$ と再添字付けしてよい。

**判定：正しい。** 特に問題指定の「$i$ については $p_t$ と逆向き」は正しく扱われている。

### 1.4 ステップ O4：抽出回数・前段の保存・指数評価

**原文の引用（L2387–2401）。**

> “$m_{\ell+1}:=(m_\ell-1)^2+1$, so $m_k\le N^{2^k}$.”

> “Treat the pairs one at a time, the pairs $(t,t)$ first”

> “earlier homogeneity persists in subsets.”

**主張。** $k=|\mathcal O|$ 回の縮約を施せば長さ $m_k$ から長さ $m_0=N$ が残り、既処理の比較の真偽は崩れない。閾値は $N^{2^k}$ 以下。

**検証。** 第 $j$ 段では $m_{k-j+1}$ 個の添字から $m_{k-j}$ 個を得る。$m_{h+1}=(m_h-1)^2+1$ はちょうど補助補題／Erdős–Szekeres に必要な長さ。全型の自己対を先に処理するので、以後の異型段の単調性は縮約で失われない。真偽一定という条件は「**選択した集合内の全 $i<j$ について**」という全称命題であり、集合を小さくしてもそのまま成立する。

数値評価は $m_h\ge3$ を使って
\[
  m_{h+1}=m_h^2-2m_h+2\le m_h^2
\]
なので、$m_0=N$ からの帰納法で $m_h\le N^{2^h}$。$n>m_k$ の場合は任意の $m_k$ 添字に先に制限すればよい。

**判定：正しい。**

### 1.5 ステップ O5：$i>j$ と $i=j$ を使う側は必要とするか

**原文の引用（L2266–2275、L2308–2318、L2430–2438）。**

> “the order of $(t,i)$ and $(u,i)$ does not depend on $i$” (`lem:group-block-order` の仮定 (i))

> “for every two block positions $t,u$ on a common line … for all $i<j$” (`lem:group-interval` の仮定)

> “The pattern of an index records … their order on shared lines” (`lem:block-replacement(b)` の証明)

**主張。** `lem:order-homogenize` は $i<j$ しか均質化しないが、後段の順序分類は任意のブロック対の位置関係を必要とする。

**検証。** $i<j$ については補題が**全順序対** $(t,u)$ と $(u,t)$ を含めて真偽を均質化する。$i>j$ で $p_t(i)<p_u(j)$ を調べたければ、$j<i$ に対する $p_u(j)<p_t(i)$ を見てその真偽を反転すればよい。同一直線の点はすべて異なるため、等号の例外はない（自己型でも別添字の点は異なる）。したがって **$i>j$ は独立の均質化を必要としない**。一方 $i=j$ はこの反転法では出ないが、`lem:block-replacement(b)` は均質化**以前**に同じ block pattern（本数、行への割当、同一行内の同一所有者の順序）を持つ所有者だけを選ぶ。ゆえに $p_t(i)<p_u(i)$ は残ったすべての $i$ で同じで、`lem:group-block-order` の仮定 (i) が成立する。

各利用箇所の帰結は以下のとおり。

| 利用箇所 | 要請される情報 | どこで供給されるか | 判定 |
|---|---|---|---|
| `lem:group-block-order`（L2266 以降） | 同添字の順序と異添字の前後両向き | 同じ pattern と、逆順の型対の否定 | 成立 |
| `lem:group-interval`（L2308 以降） | 同一添字で同じ並び、$i<j$ の真偽 | 記述された仮定と `group-block-order` | 成立 |
| `lem:block-replacement(b)`（L2430 以降） | 最大 $f^2$ 個の前向き比較と同一所有者の pattern | pattern 抽出後の `order-homogenize` | 成立 |
| `prop:block-replacement-interface`（L1324 以降） | 上記の合成から任意の非可換群で同時保存 | `block-replacement(b)` の抽出と `group-interval` | 成立 |

`lem:group-interval` の非可換積の検算も行った。$P_p$ を元の先頭 $p$ チャンクの積、$Q_p$ を置換後の同じ積とすると、チャンク $(p,p']$ のみを置換した積は
\[
 P_p(Q_p^{-1}Q_{p'})(P_{p'}^{-1}P_n).
\]
これが $P_n$ に等しい条件は、左右から順序を保って因子を消去することにより
\[
 P_pQ_p^{-1}=P_{p'}Q_{p'}^{-1}
\]
と**同値**。可換性は使用していない。減少向きの class では所有者区間 $(a,b]$ がチャンク区間 $(n-b,n-a]$ に写る。各 class の境界状態を $\kappa_j$ または $\kappa_{n-j}$ とするため、$n+1>|\mathbb G|^c$（$c\le f$）からの鳩の巣原理で同じ所有者区間が全 class に有効となる。

**判定：利用側も正しい。** ただし「$i=j$ を pattern が、$i>j$ を逆順型対が処理する」という接続を明記すれば、量化の心配がなくなる。

### 1.6 補題1の不足している一文

`lem:order-homogenize` の証明直後または `lem:block-replacement(b)` の適用直前に、次の **一文** を挿入することを勧める。

> **The reverse ordered pair $(u,t)$ determines comparisons with $i>j$ by negation, while the common block pattern fixes all comparisons with $i=j$; hence Lemma~\ref{lem:group-block-order} has both of its hypotheses after the extraction.**

これは証明の**補足**であり、補題の主張や閾値に変更は必要ない。

---

## 2. `lem:app-u1-parikh` の検証

以下、$\Sigma=\{\mathtt a,\mathtt b\}$、$s(\mathtt a)=1$、$s(\mathtt b)=\zeta$、$v=|V|\ge1$、$\theta=\bar\theta_G\ge1$、$r=r_{\max}\ge2$ とする。後二つの不等式は定理 `thm:binary-u1-polydata` の適用域と付録 H 冒頭の設定に由来する。$E_A$ の固定部分の Parikh ベクトルを $(p,q)$ とし、$p+q\le\theta$、$\omega_B$ のそれを $(x_B,y_B)$ とするので $x_B+y_B\le\theta$。成功導出の全ての非終端成分は非空である（good grammar）。

### 2.1 ステップ P0a：`lem:app-u1-fillers` と Parikh 条件への置換

**原文の引用（L3362–3375、L3535–3541）。**

> “$\operatorname{Cl}_{L,s}(X)=\{\tuple z\in(\Sigma^+)^d:s^{(d)}(\tuple z)=\mathbf t,\ E_A[\tuple z]\in L\}$”

> “By Lemma~\ref{lem:app-u1-fillers} and Parikh saturation, $\tau_X$ is the least $\|\tuple z\|_1$ …”

**主張。** 任意の非空 $d$-tuple の型が $X=A_{\mathbf t}$ と一致するとき、分布同値であることは $E_A$ に受理されることと同値。さらに Parikh 飽和なら受理は $\mathcal P=\Psi(L\cap\Sigma^+)$ におけるベクトル包含に等しい。

**検証。** $L_X$ の元 $\tuple u$ は、導出的な許容文脈 $E_A$ に必ず受理される。`lem:typed-homogeneity` により $L_X$ は共通の分布同値類に属す。同型 $\tuple z$ が $E_A$ に受理されれば、$E_A$ は $\tuple z$ と $\tuple u$ の**共通許容文脈**となるため、$(f,s)$-tuple substitutability を arity $d$ で使って分布が一致する。逆に分布が一致すれば $E_A$ にも受理される。$E_A$ は実際の成功導出から切り出され、その内側の $d-1$ 個の区切りは非空（good / nonmerging）、各穴に入れる成分も非空なので、ここで禁止された空成分の代入は一切ない。Parikh 飽和は
\[
 E_A[\tuple z]\in L
 \iff (p,q)+\sum_{i=1}^{d}\Psi(z_i)\in\mathcal P
\]
を与える。ゆえに
\[
\tau_X=\min\left\{\sum_i|z_i|:\ z_i\in\Sigma^+,\ s(z_i)=t_i,
\ (p,q)+\sum_i\Psi(z_i)\in\mathcal P\right\}.
\]

**判定：正しい。** この等式は $L_X$ に含まれないが**同一分布をもつ語**も代表として使う点で重要。単なる typed shortest yield の最小化と取り違えてはいけない。

### 2.2 ステップ P0b：部分木置換の Parikh 差分と零差分

**原文の引用（L3538–3544、L3377–3399）。**

> “$\Psi(w)-(a_u,b_u)+(x_{B_u},y_{B_u})$”

> “for a proper descendant $u'$ with $B_{u'}=B_u$ … $\Psi(w)-(a_u-a_{u'},b_u-b_{u'})$”

**主張。** ある節点 $u$ の導出を同じ非終端の短い導出へ置き換えると、総 Parikh ベクトルはその節点に由来する寄与だけ変化する。同じ非終端の子孫導出への置換でも同様。

**検証。** MCFG 規則の非削除性・線形性により、節点 $u$ の全ての文字の出現は成功語のどこかに**ちょうど一度**現れる。したがって元の寄与 $\Psi(\operatorname{yield}(u))=(a_u,b_u)$ を引き、差し替えた tuple の寄与 $(x_B,y_B)$ を足す。祖先と子孫が同じ非終端なら、子孫の全成分は同じスロットに合法に代入でき、全体の変化は $-(a_u-a_{u'},b_u-b_{u'})$ となる。**同じ非終端であることだけで型が保存されるとは主張していない**が、ここで欲しいのは $G$ の成功語と Parikh 像への所属なので型を保存する必要はない。

零差分については `lem:app-u1-identity` を確認した。$\Psi(u)=\Psi(u')$ なら、祖先から子孫までで規則が新たに書いた終端と傍枝の非空 yield がともにゼロ。ゆえに経路上には終端も傍枝もなく、rank one、nondeleting / nonpermuting / nonmerging / $\lambda$-free から各成分は対応成分変数１個だけ。従って恒等写像の連鎖であり、節点を省けて元の成功語の最少節点性に矛盾する。

**判定：正しい。** とくに arity two の成分順序は nonpermuting により保持される。

### 2.3 ステップ P0c：全成分が型 $\zeta$ の場合

**原文の引用（L3546–3548）。**

> “Mark one letter $\mathtt b$ in each component and argue as in Lemma~\ref{lem:app-u1-shallow}.”

**主張。** $d=1,2$ の全成分 $\zeta$ 型の場合、短い代表が存在し、$\tau_X\le8(r+1)v\theta$。

**検証。** 型付き非終端 $X$ からの節点数最少導出 $T$ を選ぶ。根から葉への経路で同じ型付きラベルが二度出れば上側を下側で切り詰めても $X$ の型と導出可能性は保たれ、最少節点性に矛盾。型付き非終端の個数は $2^f v\le4v$。各根成分に存在する $\mathtt b$ を１個ずつ印付けすれば印は $d\le2$ 個、印を記す節点から根へ至る経路の和 $H$ は $|H|\le2\cdot4v=8v$。$H$ にぶら下がる各部分木を $\omega_B$ に差し替えても印付き $\mathtt b$ は不変なので、どの根成分も $\zeta$ 型のまま。新 tuple は元と同じ型で $L_A(G)$ に属し、`lem:app-u1-fillers`（または typed exchange）から分布同値の代表である。$H$ 上の各節点の終端書き込みは $\theta$ 文字以下、境界にある子は高々 $r$ 個、差し替え後の各 yield は $\theta$ 以下だから
\[
\tau_X\le(r+1)\theta|H|\le8(r+1)v\theta.
\]
本来の `lem:app-u1-shallow` が用いる「pure 成分に新しく $\mathtt b$ が現れないための deep insertion 不在」という仮定は、ここでは**pure 成分が最初から存在しない**ので不要である。

**判定：正しいが説明省略あり。** 数学的欠落ではなく「argue as」の展開が必要。

### 2.4 ステップ P0d：混合型 $(1,\zeta)$ と $(\zeta,1)$

**原文の引用（L3549–3569）。**

> “The fillers may be taken as $(\mathtt a^c,\mathtt b^y)$”

> “every heavy node has $a_u\ge c$ or $b_u\ge y$.”

> “paths have at most $v(\theta+3)$ nodes.”

**主張。** 混合型で $\tau_X$ を最小にする $c,y\ge1$ があり、$\tau_X=c+y\le12(r+1)v\theta^3$。

**検証。** 型 $(1,\zeta)$ の最短候補を探すとき、１番目は $\mathtt a$ のみ、２番目には $\mathtt b$ が少なくとも１つ。固定 $(p,q)$ の下で Parikh ベクトルだけが受理を決めるので、２番目に余分な $\mathtt a$ がある候補はそれを全て取り去って $\mathtt b^y$ としても、$\mathcal P$ への所属が保たれるとは**限らない**。正確には、総 $\mathtt a$ 数が $p+c$、総 $\mathtt b$ 数が $q+y$ である最短候補の第２成分に $\mathtt a$ があれば、その分を**第１成分に移す**ことで総 Parikh ベクトルを保ち、型 $(1,\zeta)$ と総長も保ったまま $(\mathtt a^c,\mathtt b^y)$ へ移せる。よって $c,y\ge1$ としてよい。

成功語 $W=\mathtt b^{q+y}\mathtt a^{p+c}\in L$ を選び、これを導く節点数最少の $T$ を取る。heavy を $a_u+b_u>\theta$ とする。もし $a_u<c$ かつ $b_u<y$ なら $\omega_B$ への置換後のベクトルは
\[
  (p+c-a_u+x_B,q+y-b_u+y_B)
\]
で両座標の余剰は依然正、総長は heavy 部分木を $\le\theta$ に差し替えるので厳密に小さい。前段の代表式に矛盾する。祖先 $u$ と同ラベルの子孫 $u'$ の差が両座標とも $(c,y)$ 未満で正なら、子孫導出への置換後は少なくとも１個の $\mathtt a$ と $\mathtt b$ を保つ、かつ総長が減る。差分が零なら identity 補題が矛盾を与える。ゆえに
\[
 a_u-a_{u'}\ge c\quad\text{または}\quad b_u-b_{u'}\ge y.
\]
経路上で $\bigl(\lfloor a_u/c\rfloor,\lfloor b_u/y\rfloor\bigr)$ は各成分非増加で、最上位で高々 $(\lfloor(p+c)/c\rfloor,\lfloor(q+y)/y\rfloor)\le(p+1,q+1)$。したがって**値が変わる回数**は高々 $p+q+2$、値の総数は高々 $p+q+3\le\theta+3$。同値の連続区間には同一非終端が２度現れ得ない（現れれば差分が両座標とも閾値未満）。経路長は高々 $v(\theta+3)$。

同一深さの heavy 節点は互いに独立な yield を持ち、各節点は $a_u\ge c$ または $b_u\ge y$ だから、１深さにつき
\[
 \#\{\text{heavy nodes}\}\le\left\lfloor\frac{p+c}{c}\right\rfloor+
 \left\lfloor\frac{q+y}{y}\right\rfloor\le p+q+2\le\theta+2.
\]
heavy 祖先閉性と、根が軽い場合の自明な上界から
\[
\begin{aligned}
 c+y&\le |W|\le\max\{\theta,(r+1)\theta\,v(\theta+2)(\theta+3)\}\\
 &\le12(r+1)v\theta^3,
\end{aligned}
\]
最後は $(\theta+2)(\theta+3)\le12\theta^2$（$\theta\ge1$）による。$(\zeta,1)$ は２成分の役割を入れ替えるだけで、Parikh 飽和のため生成語の具体的な字順は関係しない。

**判定：正しい。** なお「混合型では $(a^c,b^y)$ にしてよい」の理由は **文字を捨てることではなく、成分間で再配分すること**である。

### 2.5 ステップ P1：行剛性

**原文の引用（L3575–3581）。**

> “there are no $(c_0,y),(c_0+\delta,y)\in\mathcal P$ with $c_0\ge1$ and $1\le\delta\le K-h$.”

**主張。** 型 $(1,\ldots,1)$（成分数 $h=1,2$）で最短の総純長 $K$ が与えられると、同じ $\mathtt b$ 数を持ち $\mathtt a$ 数の差が $1,\ldots,K-h$ である Parikh 像の２点は存在しない。

**検証。** $c_0\ge1$ なので $\mathtt b^y\mathtt a^{c_0-1}\square$ は arity one の許容文脈。これは型1の $\mathtt a$ と $\mathtt a^{1+\delta}$ の両方を受理するため分布は一致する。一方 $K-\delta\ge h\ge1$ により $\mathtt b^q\mathtt a^{p+K-\delta-1}\square$ も許容文脈で、長いほうの filler を入れた語は $W=\mathtt b^q\mathtt a^{p+K}\in L$。従って短いほうへの交換で
\[
 (p+K-\delta,q)\in\mathcal P,
 \qquad h\le K-\delta<K,
\]
となり $K$ の最短性に反する。$y=0$ や $q=0$ も外側文脈が空でよいことから支障なし。

**判定：正しい。** 非空性は $\mathtt a$ と $\mathtt a^{1+\delta}$ について満たされている。

### 2.6 ステップ P2：高さと mixed 節点数

**原文の引用（L3582–3591）。**

> “$a_u-a_{u'}\ge K-h+1$”

> “paths have at most $2v(q+1)$ nodes.”

**主張。** 同じ非終端と同じ $b$ 数が同一経路で３回現れず、混合節点数 $M\le4v\theta^2$。

**検証。** $u\supsetneq u'$ で同非終端、$b_u=b_{u'}$ なら $\delta=a_u-a_{u'}\ge0$。$\delta=0$ は identity 補題と節点数最少性に反する。$1\le\delta\le K-h$ では祖先を子孫へ置換すると $\mathtt b$ 数は $q$ のままで $K-\delta\ge h$、従って $\tau_X=K$ に反する。よって $\delta\ge K-h+1$。もし同一経路に同ラベル・同 $b$ 数の３節点があれば、２回の差分から
\[
 p+K\ge2(K-h+1)
 \quad\Longrightarrow\quad K\le p+2h-2\le p+2,
\]
だが仮定 $K>\theta+2\ge p+2$ に矛盾。$b$ 数は $0,\ldots,q$、非終端は $v$ 個、各組は経路上高々２回なので高さ $\le2v(q+1)$。各 mixed 節点は少なくとも１つの $\mathtt b$ を含み、その $\mathtt b$ の書き込み節点への祖先経路にある。$\mathtt b$ の出現は全体でちょうど $q$ 個だから
\[
 M\le2vq(q+1)\le4v\theta^2
\]
（$q\le\theta$、$q+1\le2\theta$）。$q=0$ なら mixed 節点なし。

**判定：正しい。**

### 2.7 ステップ P3：重い純節点と反鎖の比較

**原文の引用（L3592–3606）。**

> “Call a pure node $u$ heavy if $\ell_u:=a_u>\theta+1$”

> “two antichains with $\sigma(J),\sigma(J')\le K-h$ and $Y(J)=Y(J')$ have $\sigma(J)=\sigma(J')$”

**主張。** 同一非終端で heavy pure な節点は比較不能、かつ等しい追加 $b$ 数を生む二つの反鎖の削除 $a$ 数は、$\sigma\le K-h$ の範囲で等しい。

**検証。** heavy pure な $u$ は $\ell_u\ge\theta+2$。$\omega_{B_u}$ の $a$ 数 $x_{B_u}\le\theta$ より $g_u:=\ell_u-x_{B_u}\ge2$。同じ非終端の比較可能な heavy pure 節点 $u\supsetneq u'$ はともに $b=0$ だから (P2) で $\ell_u-\ell_{u'}\ge K-h+1$。すると
\[
 \ell_u\ge K-h+1+\theta+2=K+\theta-h+3>p+K
\]
（$p\le\theta$、$h\le2$）となり、成功語の $a$ 数を超えて矛盾。

反鎖 $J$ は互いに重ならず、各節点の置換で $g_u$ 個の $a$ を減らし $y_{B_u}$ 個の $b$ を増やすので、結果の Parikh ベクトルは
\[
 (p+K-\sigma(J),q+Y(J)),\quad
 \sigma(J)=\sum_{u\in J}g_u,\quad Y(J)=\sum_{u\in J}y_{B_u}.
\]
$J,J'$ に $Y(J)=Y(J')$、$\sigma(J),\sigma(J')\le K-h$ を仮定すると、同じ $b$ 行の二点の $a$ 数の差は
\[
 |\sigma(J)-\sigma(J')|\le K-h,
\]
その小さいほうの $a$ 数は $p+K-\max\{\sigma(J),\sigma(J')\}\ge p+h\ge1$。従って (P1) により差は零。

**判定：正しい。** **反鎖でない集合を同時置換したとは一度も言っていない。**

### 2.8 ステップ P4：頻出非終端と比の共通性

**原文の引用（L3607–3621）。**

> “each has $\ell_u\le p+K-(\theta+2)\le K-2$”

> “$y_Cg_B\le(m_B-1)\ell_B\le p+K-\ell_B\le K-2\le K-h$”

> “all frequent $B$ share a ratio $\alpha:=g_B/y_B$”

**主張。** heavy pure 節点が２個以上ある同非終端 $B$ は共通長さを持ち、$y_B\ge1$。$m_B>\theta$ の頻出非終端間で $g_B/y_B$ は共通。

**検証。** (P3) で同非終端の heavy pure 節点は反鎖であり、$m_B\ge2$ のとき各 $u$ のほかに長さ $\ge\theta+2$ の節点がある。よって
\[
 \ell_u\le p+K-(\theta+2)\le K-2,
 \qquad 2\le g_u\le\ell_u\le K-2\le K-h.
\]
同一ラベル２節点の singleton 反鎖は $Y=y_B$ が等しいので (P3) で $g_u=g_{u'}=:g_B$、従って長さも $\ell_B=x_B+g_B$ に一致する。$y_B=0$ なら singleton 置換で $q$ が不変かつ $h\le K-g_B<K$ となり矛盾。よって $1\le y_B\le\theta$。

頻出 $B,C$ に対して $m_B>\theta\ge y_C$ だから $y_C\le m_B-1$、$m_C>\theta\ge y_B$ だから $y_B\le m_C-1$。互いに反鎖である $B$ 節点から $y_C$ 個、$C$ 節点から $y_B$ 個を**別々に**取る。前者の $\sigma=y_C g_B$ は、$m_B$ 個の disjoint yields が全体の $a$ 個数 $p+K$ に入ることから
\[
 y_Cg_B\le(m_B-1)\ell_B\le p+K-\ell_B
 \le K-2\le K-h.
\]
後者も $y_Bg_C\le K-h$。二反鎖の $Y$ はともに $y_B y_C$、よって (P3) から $y_Cg_B=y_Bg_C$。分母が正だから
\[
\frac{g_B}{y_B}=\frac{g_C}{y_C}=:\alpha>0,\qquad
\ell_B=x_B+\alpha y_B\le(1+\alpha)\theta.
\]

**判定：正しい。** **旧監査で穴とされた $y_Cg_B\le K-h$ は現行原稿に明記され、必要な正当化も上の通り成立する。**

### 2.9 ステップ P5：比 $\alpha$ の上界

**原文の引用（L3622–3633）。**

> “$\alpha_*:=(r+1)(\theta+1)(2\theta+1)v$”

> “Group them by their number of heavy proper ancestors in the subtree”

> “$H_u\le v(2\theta+1)$”

**主張。** 頻出ラベルが存在すれば、その共同比は $\alpha\le\alpha_*\le6(r+1)v\theta^2$。

**検証。** $\alpha\le\theta$ の場合は $\alpha_*\ge\theta$ なので自明。$\alpha>\theta$ では頻出 $B$ の heavy pure 節点 $u$ を固定する。$u$ の純部分木内では heavy pure 祖先閉性がある。heavy pure 節点は自分で高々 $\theta$ 終端を書き、heavy でない子を高々 $r$ 個持ち、その子の各 yield は高々 $\theta+1$。すべての文字はこれらのいずれかに属するので
\[
 \ell_B\le(r+1)(\theta+1)H_u,
\]
$H_u$ は $u$ 以下の heavy pure 節点数。(P3) の comparable heavy pure 節点のラベル相異性から、同一路径の heavy proper ancestor 数は $0,\ldots,v-1$ の高々 $v$ 値。同じ値をもつ節点同士は**比較不能（反鎖）**である。各反鎖に含まれる頻出ラベルの節点は長さ $\ell_C=x_C+\alpha y_C\ge\alpha$、相異なる節点の yield は互いに交わらず、いずれも $u$ の yield に含まれる。従って反鎖一つあたり
\[
 \#\{\text{頻出節点}\}\le\frac{\ell_B}{\alpha}
 \le\frac{(1+\alpha)\theta}{\alpha}<\theta+1.
\]
左辺は整数なので $\le\theta$。高々 $v$ 反鎖で頻出節点は $\le v\theta$。非頻出ラベルは各非終端につき**全 $T$ 中**高々 $\theta$ 個だから、$u$ 下の非頻出節点も $\le v\theta$。従って $H_u\le2v\theta\le v(2\theta+1)$。

$y_B\ge1$ と $g_B=\alpha y_B$ から $\alpha\le g_B\le\ell_B$、上の文字数評価に代入して
\[
 \alpha\le\ell_B\le(r+1)(\theta+1)v(2\theta+1)=\alpha_*.
\]
さらに $(\theta+1)(2\theta+1)\le6\theta^2$（$\theta\ge1$）。

**判定：正しい。** 「各 group は反鎖」という原文の性質と、非頻出節点の**全木での**個数を区別して使っている。

### 2.10 ステップ P6：大型節点・総数・定数の組立て

**原文の引用（L3634–3655）。**

> “$T_*:=(\alpha_*+1)\theta\le7(r+1)v\theta^3$”

> “there are at most $v\theta$ large nodes”

> “$p+K\le\theta M+(rM+rv\theta+1)T_*+\theta\cdot v\theta$”

**主張。** $p+K\le(42r(r+1)+5)v^2\theta^5$、したがって純型の場合も目的上界。

**検証。** large pure を $\ell_u>T_*=(\alpha_*+1)\theta$ とする。$T_*\ge\theta+1$ なので全 large は heavy。頻出節点の長さは (P4)–(P5) より
\[
 \ell_B\le(1+\alpha)\theta\le T_*,
\]
よって large を持つラベルは非頻出であり、**全大節点数**は $H_{\rm large}\le v\theta$。pure subtree の中で large は祖先閉。全 $\mathtt a$ 文字は (a) mixed 節点自身が書く、(b) large 節点自身が書く、(c) 極大 non-large pure subtree の yield に属する、のどれか。重複して数えることは上界のため無害。極大 non-large pure subtree の根は、木の根、mixed の子、large の子のいずれかなので本数は $\le1+rM+rH_{\rm large}$。各節点の直接の終端は $\le\theta$、各 non-large subtree の yield は $\le T_*$ なので
\[
 p+K\le\theta M+\theta H_{\rm large}+(rM+rH_{\rm large}+1)T_*
 \le\theta M+v\theta^2+(rM+rv\theta+1)T_*.
\]
各評価の定数は次のように出る。
\[
\begin{aligned}
 \alpha_*&\le6(r+1)v\theta^2,\\
 T_*=(\alpha_*+1)\theta&\le7(r+1)v\theta^3,\\
 \theta M+v\theta^2&\le4v\theta^3+v\theta^2\le5v\theta^3,\\
 rM+rv\theta+1&\le4rv\theta^2+rv\theta+1\le6rv\theta^2,
\end{aligned}
\]
最後の不等式は $r,v,\theta\ge1$（今回の適用は $r\ge2$）から $rv\theta+1\le2rv\theta^2$ を使う。従って
\[
\begin{aligned}
 p+K&\le5v\theta^3+42r(r+1)v^2\theta^5\\
 &\le(42r(r+1)+5)v^2\theta^5.
\end{aligned}
\]
純型の $\tau_X=K\le p+K$。$K\le\theta+2$ の小さい場合も $K\le3\theta$ で目標上界の範囲。混合型は $12(r+1)v\theta^3$、全 $\zeta$ 型は $8(r+1)v\theta$ である。$v,\theta\ge1$ と $r\ge2$ から
\[
 \max\{(42r(r+1)+5)v^2\theta^5,\ 12(r+1)v\theta^3,\ 8(r+1)v\theta\}
 \le(42r(r+1)+12(r+1))v^2\theta^5.
\]
この最終係数は**正しく組み立てられている**。$42$ は $6\times7$、$12$ は混合型の $(\theta+2)(\theta+3)$ の評価、残る $+5$ はその $12(r+1)$ の余裕に吸収される。

**判定：正しい。** ただし $rM+rv\theta+1\le6rv\theta^2$ は $r\ge1$ の仮定が必要であり、付録 H と主定理の $r=r_{\max}\ge2$ に依存する。rank $0$ だけを独立に論ずる場合には、別の自明な場合分けが必要。

### 2.11 型の場合分け・主定理への合成・不足している一文

**原文の引用（L3546、L3549、L3570、L3655–3668）。**

> “Type $\zeta$ only.”

> “Mixed type, say $\mathbf t=(1,\zeta)$ (the other order is symmetric).”

> “Type $1$ only, with $h:=d\in\{1,2\}$.”

**主張。** 全可能型を被覆し、Parikh 補題と shallow 補題を併用した定理 `thm:binary-u1-polydata` の定数 $C_r$ と標本上界が導かれる。

**検証（型）。** 非空成分を持つ arity one は $(1)$ または $(\zeta)$ の２通り。arity two は $(1,1)$、$(1,\zeta)$、$(\zeta,1)$、$(\zeta,\zeta)$ の４通り。これらは順に「Type $1$ only」（$h=1,2$）、「Mixed type」（両向き）、「Type $\zeta$ only」（$d=1,2$）で**漏れなく**網羅される。$(\zeta,1)$ の対称性は $E_A$ の穴を物理的に入れ替えるという意味ではなく、**Parikh ベクトルと最小総長の議論で成分の役割を入れ替える**という意味であり、二穴内側区切りを空にしない。

**検証（主定理の定数）。** `lem:app-u1-shallow` に $f=2$, $c=6$ を代入すると
\[
2^{f+1}cf(r+1)v\theta=2^3\cdot6\cdot2(r+1)v\theta
=96(r+1)v\theta.
\]
`lem:app-u1-deep` により、この shallow 条件が破れたときは Parikh 飽和。したがってどちらの場合も
\[
\tau(G,s)\le C_r v^2\theta^5,
\quad C_r:=42r(r+1)+96(r+1),
\]
とすることができる。これは２ケースの定数の**和**で抑える緩いが正当な評価である。実際 Parikh 側の定数は $42r(r+1)+12(r+1)$ なので $C_r$ 以下、shallow 側は $v,\theta\ge1$ により $C_rv^2\theta^5$ 以下。

$|\mathsf S^\sharp|=3$、$r\ge2$ なので
\[
N_{\rm typ}\le |V|3^2+|P|3^{2r}\le3^{2r}\|G\|,
 \qquad v\le\|G\|.
\]
また $1+2\theta\le3\|G\|^2\theta^5$。代表長に基づく特徴標本の一般式
\[
\|K\|_+\le N_{\rm typ}(1+2\theta+r\tau)+\mathbf1_{\{\varepsilon\in L\}}
\]
に代入すれば
\[
\boxed{\|K\|_+\le3^{2r}(3+rC_r)\|G\|^3\theta^5+\mathbf1_{\{\varepsilon\in L\}}},
\]
完全に原文の定理に一致する。

**判定：正しい。** ただし `lem:app-u1-parikh` の本文の “argue as …” は今回の検証を踏まえて明文化した方が査読しやすい。

**補題2の不足している一文（L3546 の直後に挿入可能な英文）。**

> **Indeed, a node-minimal derivation from $X$ has paths of length at most $2^fv$, and marking one $\mathtt b$ in each of its at most two root components leaves at most $2\cdot2^fv$ marked ancestor nodes; replacing all off-path subtrees by $\omega_B$ preserves the $\zeta$-type of every component and gives total length at most $8(r+1)v\theta$.**

併せて、rank の適用範囲を明確にする場合は (P6) の直前に「Here $r=r_{\max}\ge2$ as fixed in the theorem.」を追記すれば、定数評価が非零ランクに依存する点も明示される。**補題の結論・定数を修正する必要はない。**

---

## 3. 旧監査および別査読との照合（独立検証後）

**旧監査の (P4) 指摘。** 旧監査 §1.4 は、頻出 $B,C$ の反鎖の $\sigma$ が $K-h$ 以下であることを**書いて示す必要**があると述べる。現在版 L3607–3621 は
\[
 y_Cg_B\le(m_B-1)\ell_B\le p+K-\ell_B\le K-2\le K-h
\]
を明示している。§2.8 の通り、この不等式に必要な「同ラベルの重い純節点の互いの比較不能性」「$m_B\ell_B\le p+K$」「$m_B-1\ge y_C$」も証明から復元可能。**旧監査の指摘は現行版で解消済み**である。旧監査のその後の $\theta^4$ 改善が未解決であることは、ここで審査対象とする $\theta^5$ の正否に影響しない。

**別査読との照合。** DeepSeek 報告は (P1)–(P6) の破綻を見つけず、`lem:order-homogenize` も確認しつつ再読を推奨している。本書の判定はその結論を前提にせず §§1–2 の場合分け・差分式・数値定数を再導出した結果であり、**同じ結論に達した**。本書は指定された二補題に限定し、同報告の他の軽微な指摘（別命題・要旨等）は評価対象としない。

---

## 4. 計算確認の範囲と意味

結果は**有限範囲の観測**である。証明は §§1–2 に置き、この節と付録のプログラムは反例探索・転記ミス検出の補助に限定する。

| 実験 | 探索範囲 | 結果 | 解釈 |
|---|---|---|---|
| Erdős–Szekeres の閾値 | $N=3,k=1,m_1=5$。５点の全 $5!=120$ 順列 | 反例０ | 証明の代用ではない |
| 閾値より短い１型列 | $n=4,N=3$、順列 $(1,3,0,2)$ | 長さ３の単調部分列なし | $m_1=5$ がこの場合に鋭い |
| `lem:two-sequence` | $m=3,m'=5$。三角領域の全 $2^{10}=1024$ 二値彩色を走査し、そのうち行列の方向一定単調性を満たす176件 | 反例０ | この小規模の補助補題を全列挙 |
| 順序均質化・別線 | $N=3$、別線に１型ずつ、$k=2,m_k=17$。独立ランダム400件 | 反例０ | 同一直線の交差問題は含まない |
| 順序均質化・同線 | $N=3$、１本に２型、$k=4$、$n=8<m_k=65,537$、ランダム300件 | 均質３集合なし65件 | **仮定に達しないので補題の反例ではない** |
| arity one の代表長 | `G_all`, `G_b`、長さ $1$–$6$ の全２文字語 | $\tau=1$（該当する実現型について）、上界3456 | 小さい CFG 特別例のみ。arity two の網羅的実験ではない |

$k=4$ で定理の閾値 $m_4=65,537$ まで上げて全３部分集合を調べるには $\binom{65537}{3}$ 通りを扱う必要があり、今回は実施していない。反例探索を有限範囲で打ち切った事実から一般命題の正しさは導けない。

## 付録 A. 実行した Python コード全文

実行環境：Python 3、標準ライブラリのみ。乱数 seed は `20261031`。探索は上表の範囲で打ち切り、外部ソルバは用いていない。

```python
from itertools import permutations, combinations, product
from random import Random

rng = Random(20261031)

def valid_index_set(I, line_values):
    # line_values: list of lines, line: list of (type, list of coordinates)
    for line in line_values:
        for (t, xs) in line:
            for (u, ys) in line:
                vals = {xs[i] < ys[j] for i, j in combinations(I, 2)}
                if len(vals) != 1:
                    return False
    return True

def find_set(n, N, lines):
    for I in combinations(range(n), N):
        if valid_index_set(I, lines):
            return I
    return None

# The exact one-type threshold: m_1=(3-1)^2+1=5.
perms5 = list(permutations(range(5)))
fail_5 = sum(find_set(5, 3, [[('t', p)]]) is None for p in perms5)
# A classical extremal permutation of length four.
critical4=(1,3,0,2)
print('ES: N=3, k=1, m_k=5, permutations tested:', len(perms5), 'failures:',fail_5)
print('ES: n=4, permutation',critical4,'has I size 3:',find_set(4,3,[[('t',critical4)]]))

# Exhaustive two-sequence lemma on all 2^10 possible 0/1 colorings on triangular domain.
def monotone(seq):
    return all(seq[i] <= seq[i+1] for i in range(len(seq)-1)) or all(seq[i] >= seq[i+1] for i in range(len(seq)-1))

def is_fixed_direction(b, n):
    for orientation in (+1, -1):
        for col_orientation in (+1,-1):
            rowok = all(all((b[i,j] <= b[i,j+1] if orientation == 1 else b[i,j] >= b[i,j+1])
                            for j in range(i+1,n-1)) for i in range(n-1))
            colok = all(all((b[i,j] <= b[i+1,j] if col_orientation == 1 else b[i,j] >= b[i+1,j])
                            for i in range(j-2)) for j in range(2,n))
            if rowok and colok:
                return True
    return False

n=5
pairs=list(combinations(range(n),2))
monotone_colorings=0
bad_colorings=0
for vals in product((0,1),repeat=len(pairs)):
    b=dict(zip(pairs, vals))
    if not is_fixed_direction(b,n):
        continue
    monotone_colorings +=1
    if not any(len({b[i,j] for i,j in combinations(I,2)}) == 1
               for I in combinations(range(n),3)):
        bad_colorings+=1
print('two-sequence: n=5, all binary colorings:',2**len(pairs),
      'monotone/fixed-direction:',monotone_colorings,'violations:',bad_colorings)

# Two lines, one type on each: k=2, m_2=17 for N=3.
trials=400
miss=0
for _ in range(trials):
    a=list(range(17)); b=list(range(17))
    rng.shuffle(a); rng.shuffle(b)
    if find_set(17,3,[[('t',a)],[('u',b)]]) is None:
        miss+=1
print('order-homogenize: N=3, k=2, m_k=17, 2 separate lines,',trials,
      'random configurations, failures:',miss)

# Two types on the same line, n below the theorem's threshold (m_4=65537): exploratory.
trials=300
miss=0
example=None
for _ in range(trials):
    values=list(range(16));rng.shuffle(values)
    a,b=values[::2],values[1::2]
    if find_set(8,3,[[('t',a),('u',b)]]) is None:
        miss+=1
        if example is None: example=(a,b)
print('order-homogenize: N=3, k=4, n=8 < m_k=65537,',trials,
      'random configurations, missing homogeneous 3-set:',miss)
print('first short-length missing example:',example)

# One-nonterminal fan-out-1 MCFGs (CFG), length <= 6; each has theta=2.
# Grammar G_all: S -> a | b | a S | b S.  L(G_all) = {a,b}^+.
# Grammar G_b: S -> b | a S | b S | S a | S b.
# A semantic representative for E_S = □ is a shortest word in L of type t.
from itertools import product as cart
for name, predicate in (
    ('G_all',lambda w:bool(w)),
    ('G_b',lambda w:'b' in w),
):
    words=[''.join(p) for n in range(1,7) for p in cart('ab',repeat=n)]
    w=[z for z in words if predicate(z)]
    realized=sorted(set('zeta' if 'b' in z else 'one' for z in w))
    taus={t:min(len(z) for z in w if ('zeta' if 'b' in z else 'one')==t)
          for t in realized}
    r,v,theta=1,1,2
    bound=(42*r*(r+1)+12*(r+1))*v**2*theta**5
    print(name,'words len<=6:',len(w),'realized types:',realized,
          'observed tau:',taus,'lemma bound:',bound)
```

## 付録 B. 実際の標準出力（そのまま）

```text
ES: N=3, k=1, m_k=5, permutations tested: 120 failures: 0
ES: n=4, permutation (1, 3, 0, 2) has I size 3: None
two-sequence: n=5, all binary colorings: 1024 monotone/fixed-direction: 176 violations: 0
order-homogenize: N=3, k=2, m_k=17, 2 separate lines, 400 random configurations, failures: 0
order-homogenize: N=3, k=4, n=8 < m_k=65537, 300 random configurations, missing homogeneous 3-set: 65
first short-length missing example: ([5, 6, 15, 3, 0, 12, 14, 7], [13, 2, 11, 1, 10, 9, 8, 4])
G_all words len<=6: 126 realized types: ['one', 'zeta'] observed tau: {'one': 1, 'zeta': 1} lemma bound: 3456
G_b words len<=6: 120 realized types: ['zeta'] observed tau: {'zeta': 1} lemma bound: 3456
```

### 付録実験の文法の具体形と限界

`G_all`：$S\to\mathtt a\mid\mathtt b\mid\mathtt a S\mid\mathtt b S$、ゆえに $L(G_{\rm all})=\{\mathtt a,\mathtt b\}^+$。

`G_b`：$S\to\mathtt b\mid\mathtt a S\mid\mathtt b S\mid S\mathtt a\mid S\mathtt b$、ゆえに $L(G_b)=\Sigma^*\mathtt b\Sigma^*$。

いずれも arity $1$、rank $1$、$v=1$、$\theta=2$ の reduced good 文法。両言語は Parikh 飽和で、$(1,s)$-substitutable でもある（同じ型の非空語は、対応する文脈集合が完全に一致する）。$S$ に対する文脈 $E_S=\square$ での最短代表は、存在する型について $\mathtt a$ または $\mathtt b$ の長さ1。観測中に比較した理論値は
\[
(42\cdot1\cdot2+12\cdot2)\cdot1^2\cdot2^5=3456.
\]
ここでは $r=1$ の小文法も例示しているが、**§2 の (P6) の大域評価は主定理の $r\ge2$ の下で検証した**。これらの短い実験が arity two や一般 MCFG の厳密検証を与えるとは主張しない。

---

## 最終節：この二つの補題が誤りだった場合に影響を受ける主張

ここは**反実仮想の依存関係**である。上記の結論は両補題とも現在の仮定で成立するというものであり、以下は「誤りだった」と断定するものではない。

| 仮に破綻する補題 | 直接影響 | 間接影響を受ける主要主張 | 影響の限定 |
|---|---|---|---|
| `lem:order-homogenize` | `lem:block-replacement(b)` の非可換群の場合、`lem:group-interval` を使うための均質化抽出 | `prop:block-replacement-interface` の一般有限群部分、`lem:marked-heavy-window-group`、`thm:window-group-polydata`、`lem:local-group-shortest`、`thm:local-group-polydata`、**定理 A(i)**。さらにこれを正の方向で使う **定理 B(i)** の当該方向 | 可換群の零和証明 `lem:block-replacement(a)` は独立。定理 A(ii)、定理 C(i)、C(ii) への直接の依存はない |
| `lem:app-u1-parikh` | 6-deep insertion がある Parikh 飽和言語に対する $\tau$ 上界 | `thm:binary-u1-polydata`、**定理 C(i)**、それに直接言及する結論・開問題の既証明側の記述 | `lem:app-u1-shallow` の浅い場合、`lem:app-u1-deep` の Parikh 飽和への還元、**定理 A(i)** の群論的上界は、この補題には依存しない |

**総合結論。** 指定の現行ソースについて、(1) 順序均質化の Erdős–Szekeres 閾値・二単調列・逆向き比較・部分集合保存・$m_k$ の評価・利用側の同添字処理、および (2) Parikh 代表等式・部分木の差分式・全型・(P1)–(P6)・定数計算・主定理への合成を追跡した結果、**証明を破壊する誤りは発見されなかった**。提案した追記は説明の明確化である。計算結果は独立した証明とは扱わない。

# 群の語問題の文脈自由文法はどこまで小さく薄くできるか — 問題G の計算的探索

（2026-11-01。依頼文 `prompts/prompt_deepseek_group_word_problem_2026-11-01.md` に対する報告。
別スレッドの Claude の報告 `reviews/claude_two_letter_fanout1_2026-11-01.md` の §2 の続き。
スクリプトは Python 3 標準ライブラリのみ。`py -3 check_group_word_problem_2026_11_01.py` で動く。
**この報告書のファイルはローカルに保存しただけで、commit も push もしていない。**）

---

## 0. 主張ごとの判定

| # | 主張 | 判定 | 根拠 |
|---|---|---|---|
| G0 | $H_n=\mathbb Z/N\rtimes\mathbb Z/n$（$N=2^n-1$、$a\mapsto(x\mapsto x+1)$、$b\mapsto(x\mapsto 2x)$）で $b^n=1$、$\operatorname{ord}(a)=N$、$\lvert H_n\rvert=n(2^n-1)$、$\varphi$ は全射 | **証明済み＋数値検証** | §1.1、出力 A |
| G1 | 群の等式 $a^{2^j}=b^{\,n-j}\,a\,b^{\,j}$（$0\le j<n$、長さ $n+1$） | **証明済み＋数値検証**（$n\le 6$、全ての $j$） | §1.1、出力 A |
| G2 | 逆向きの向き $b^{\,j}a\,b^{\,n-j}=a^{2^j}$ は**一般には成り立たない**（$n\ge3$） | **証明済み（反例を計算）** | §1.1 |
| G3 | 値付き文法 $G_V$ の完全性（$V$ の全ての値で完全）の**厳密判定手続き**（長さの上限なし、任意の $r\ge2$） | **証明済み** | §2.2（$r=2$）、§2.3（一般 $r$） |
| G4 | その判定手続きの正しさ（区間 DP との全数一致） | **観察（有限の全数検査、720 例で不一致 0）** | §2.4 |
| G5 | $n=2,3$ の最小 $\lvert V\rvert$（$r=2,3,4$、条件 (a)「$V$ 上で完全」） | **証明済み（全探索）** | §3.1–3.2 |
| G5′ | 実際の要件 (b)（$L(G_V)=L$ のみ）での最小 $\lvert V\rvert$ | **観察（長さを切った全数検査）**：$n=2$ で $5,3,3$、$n=3,r=2$ で $\le12$。(a) との差は小さい | §3.5 |
| G6 | $n=4,5,6$ の $\lvert V\rvert$ の上界（貪欲＋局所探索） | **観察（上界。最小性は未証明）** | §3.2 |
| G7 | $\lvert V\rvert\approx0.56$–$0.83\,\lvert H\rvert$（$r=2$）。$r$ を上げると減るが $n$ とともに増える | **観察** | §3.3 |
| G8 | 一般の reduced good な文脈自由文法でも各非終端の生成物の値は一つに定まる | **証明済み** | §4.1 補題 4.1 |
| G9 | **模擬補題**：任意の reduced good なランク $\le r$ の文法 $G$（$L(G)=L$）に対し $\min\lvert V\rvert\le\lVert G\rVert+2$。従って $\lVert G\rVert\ge\min\lvert V\rvert-2$ | **証明済み** | §4.2 定理 4.2 |
| G10 | 系：値付き族の最小 $\lVert G_V\rVert$ と一般の文法の最小 $\lVert G\rVert$ は多項式因子を除いて等価 | **証明済み** | §4.3 系 4.3 |
| G11 | 問題G（$H_n$ 上） | **未解決**。今回の計算は「正（多項式上界が成り立つ）に傾く強い証拠」を与えるが、$\min\lvert V\rvert$ の下界の証明が無い | §7 |
| G12 | 可換群 $\mathbb Z/N$ では $\lvert V\rvert$ ははるかに小さく、代わりに $\bar\theta$ が $N$ 程度に大きい（$N\lesssim\bar\theta$） | **観察** | §5 |
| G13 | 乗数 $q=3,4$ のアフィン族でも同じ比 $\lvert V\rvert/\lvert H\rvert\approx0.55$–$0.62$ | **観察** | §6 |

「証明済み」はこの報告書内で証明を書いたもの、「観察」は有限の計算結果で、証明ではない。

---

## 1. 設定

### 1.1 群と語問題

$\Sigma=\{a,b\}$、$n\ge2$、$N:=2^n-1$、
$$H_n:=\mathbb Z/N\rtimes\mathbb Z/n=\{(j,c):j\in\mathbb Z/n,\ c\in\mathbb Z/N\},\qquad
(j_1,c_1)(j_2,c_2)=(j_1+j_2,\ 2^{j_2}c_1+c_2)$$
を「$x\mapsto 2^jx+c \pmod N$ を、語の左から順に作用させる」群とする。すなわち語 $w=w_1\cdots w_m$ の値は
$\varphi(w)=\varphi(w_1)\circ\cdots\circ\varphi(w_m)$（$\circ$ は写像の合成）で、
$a=(0,1)$（$x\mapsto x+1$）、$b=(1,0)$（$x\mapsto 2x$）、そして
$$L:=\varphi^{-1}(1)\cap\Sigma^+ .$$

**出力 A の検証結果**（スクリプト `check_affine`、$n=2,\dots,6$）：

| $n$ | $\lvert H_n\rvert$ | $N=\operatorname{ord}(a)$ | $\operatorname{ord}(b)$ | 直径 | 最短の値 $1$ の語の長さ（girth） | $\lvert H_n\rvert=n(2^n-1)$ | $a^{2^j}=b^{n-j}ab^j$ |
|---|---|---|---|---|---|---|---|
| 2 | 6 | 3 | 2 | 2 | 2 | ✓ | ✓（全ての $j$） |
| 3 | 21 | 7 | 3 | 5 | 3 | ✓ | ✓ |
| 4 | 60 | 15 | 4 | 8 | 4 | ✓ | ✓ |
| 5 | 155 | 31 | 5 | 10 | 5 | ✓ | ✓ |
| 6 | 378 | 63 | 6 | 13 | 6 | ✓ | ✓ |

群の公理（結合則・逆元）と、$\{a,b\}$ が $H_n$ 全体を生成すること（全射性）も全数検査した。逆向きの等式
$b^{\,j}a\,b^{\,n-j}=a^{2^j}$ は**一般には偽**である：実際 $b^{\,j}ab^{\,n-j}=a^{2^{n-j}}$ なので、$j=1$ で $a^{2^{n-1}}\ne a^{2}$（$n\ge3$、$2^{n-1}\not\equiv2 \bmod 2^n-1$）。
$n$ が偶数のとき $j=n/2$ だけは両辺が一致するが、全ての $j$ では一致しない（出力 A の "reversed form" 列）。これは
Claude の報告 §2.3 の向きの指定が正しいことの確認でもある（向きを間違えると族の設計が壊れる）。

### 1.2 値付き文法 $G_V$

$V\subseteq H_n$、$1\in V$ とし、非終端を $\{X_g:g\in V\}$、開始記号 $X_1$ とする。規則は
$$X_g\to x\quad(\varphi(x)=g),\qquad
X_g\to X_{h_1}\cdots X_{h_k}\quad(2\le k\le r,\ h_i\in V,\ h_1\cdots h_k=g).$$
$G_V$ の生成する語は必ず値 $1$ なので $L(G_V)\subseteq L$。問題は $L(G_V)=L$ となる最小の $V$。

ここで**2つの条件を区別する**：

- **(a) 強い条件**：$V$ の**全ての**値 $g$ について、値 $g$ の全ての語が $X_g$ から解析できる（「$V$ 上で完全」）。
- **(b) 実際の要件**：$L(G_V)=L$、すなわち**値 $1$ の**全ての語が $X_1$ から解析できる。

(a)$\Rightarrow$(b) だが逆は一般に成り立たない（値 $1$ 以外の非終端が不完全でも $L(G_V)=L$ にはなりうる）。
§2 の判定手続きは (a) を**厳密に**判定する。(b) は長さの上限を切った全数検査（区間 DP）で確かめる（観察）。
両者の差は小さく、$n=2$ では $r=2$ で一致（5）、$r\ge3$ で (b) の方が小さい（3 対 4）。$n=3,r=2$ では (b) で 12、 (a) で 13（§3.5）。
本報告の表は断らない限り **(a) の厳密な最小値**を載せ、(b) の値を併記する。**(a) の値は (b) の上界**である。

大きさは原稿 `def:standard-mcfg` の記号単位の定義
$\lVert G\rVert=\lvert V\rvert+\sum_{(A\to\rho(B_1,\dots,B_r))}(1+r+\sum_i\lvert\alpha_i\rvert)$
に従う。終端規則は $1+0+1=2$、積規則 $X_g\to X_{h_1}\cdots X_{h_k}$ は $1+k+k=1+2k$。
$k$ 子の規則の個数は
$$c_k:=\#\{(q_1,\dots,q_k)\in V^k:\ q_1\cdots q_k\in V\}$$
（群上のたたみ込みで $O(k\lvert V\rvert\lvert H\rvert)$ で計算）なので
$$\lVert G_V\rVert=\lvert V\rvert+4+\sum_{k=2}^{r}c_k(1+2k).$$
$r$ を固定すれば $\lVert G_V\rVert=O_r(\lvert V\rvert^{r})$。

厚さは原稿 §4 の定義どおり $\theta_G(R)=\min\{\lvert w\rvert:w\in L(G)\ \text{が}\ R\ \text{を使う成功導出を持つ}\}$、$\bar\theta_G=\max\{1,\max_R\theta_G(R)\}$。完全性（$V$ の全ての値で）が成り立てば、$X_g$ の最短生成物は Cayley 距離 $d(1,g)$、$X_1$ の空でない最短生成物は girth なので、
$$\theta(R)=C(p)-d^*(p)+\sum_i d^*(h_i),\qquad d^*(g)=\begin{cases}\text{girth}&g=1\\ d(1,g)&g\ne1\end{cases}$$
（$C(p)$ は $X_p$ を含む最短の文の長さ）。$C$ は文脈を「$q$ が $p$ 規則の子になりうる」と緩めて上から評価した（§8 の `theta_bar`）。従って報告する $\bar\theta$ は**上界**で、下界 $\bar\theta\ge\max\{d^*(q_1)+d^*(q_2):q_1q_2=1\}$（親が根の2子規則）を併記する。

---

## 2. 完全性の厳密判定

以下、$V$ は有限で $1,a,b\in V$ とする（$a,b$ は $L$ に現れるので必須、$1$ は開始記号）。

### 2.1 最小反例補題

**補題 2.1.** $g\in V$ について、値 $g$ の語で $X_g$ から解析できないものが存在するなら、値 $g$ の語 $w$ で
「$2\le k\le r$ の任意の分割 $w=w_1\cdots w_k$ に対し、ある $i$ で $\varphi(w_i)\notin V$」を満たすものが存在する。

*証明.* 解析できない語のうち最短の $w$ を取る。ある分割で全ての $\varphi(w_i)\in V$ なら、各 $w_i$ は短く値が $V$ に属するので最短性から $X_{\varphi(w_i)}$ から解析でき、規則で $w$ が解析できて矛盾。□

**系.** $G_V$ が $V$ の全ての値で完全 $\iff$ どの $g\in V$ にも「分割不能な値 $g$ の語」が存在しない。

### 2.2 $r=2$ の判定（グラフ到達可能性）

$r=2$ では分割は1か所なので、値 $g$ の語 $w$ が分割可能 $\iff$ ある真の接頭辞の値 $h$ について $h\in V$ かつ $h^{-1}g\in V$。そこで
$$H_g:=V\cap gV^{-1}=\{h\in V:h^{-1}g\in V\}$$
とおくと、$w$ が分割不能 $\iff$ どの真の接頭辞の値も $H_g$ に入らない。

**定理 2.2.** $r=2$ のとき、$G_V$ が $V$ の全ての値で完全であるためには、各 $g\in V$ について、$H\setminus H_g$ が誘導するグラフ（辺 $x\to x\varphi(a)$、$x\to x\varphi(b)$）において
$\{a,b\}\setminus H_g$ から $\{g\,a^{-1},\,g\,b^{-1}\}\setminus H_g$ への路が存在しないことが必要十分である。

*証明.* 分割不能な語 $w=z_1\cdots z_m$（$m\ge2$）を取る。真の接頭辞の値 $x_1,\dots,x_{m-1}$ は $H_g$ の外にあり、
$x_{i+1}=x_i\varphi(z_{i+1})$。特に $x_1\in\{a,b\}$、$x_{m-1}=g\,\varphi(z_m)^{-1}\in\{g a^{-1},g b^{-1}\}$。逆にそのような路があれば、
その路の値の列を接頭辞の値に持つ語（最後の1文字で $g$ に到達）が分割不能になる。□

（$m=2$ のときは $x_1$ が両方の役を兼ねる。定理の主張は路の長さ0を含む。）

### 2.3 一般の $r$ の判定（有限オートマトン）

分割の情報を状態に持てば、$r$ が任意でも**長さの上限なし**で判定できる。状態を $(g,D)$ とする：
$g$ は現在の接頭辞の値、$D$ は「最後の分割点の値 $s$ と、閉じた部分の個数 $k$」の集合
（閉じた部分の値はすべて $V$ に入っているものだけを数える）。語を1文字進める前に、現在位置で分割を置ける：
$(s,k)\in D$、$k+1\le r-1$、$s^{-1}g\in V$ なら $(g,k+1)$ を $D$ に加える。

**定理 2.3.** 語 $w$（長さ $\ge2$、値 $g\in V$）が分割不能であることと、上のオートマトンで $w$ を読み終えた状態 $(g,D)$ が
「$k\ge1$、$k+1\le r$、$s^{-1}g\in V$ なる $(s,k)\in D$ を持たない」ことは同値である。
従って「値 $g$ の分割不能語が存在するか」は有限状態の到達可能性で厳密に判定できる。

*証明.* $D$ は「接頭辞を $k$ 個の $V$ 値部分と1個の開いた部分に分ける全分解」をちょうど表す（帰納法）。読み終えたとき開いた部分を閉じられる分解が
ちょうど $2\le k+1\le r$ 個の $V$ 値部分への分割である。□

状態数は $\lvert H\rvert\cdot2^{\lvert H\rvert r}$ の最悪値を持つが、実用上は小さい。**部分集合による支配除去**（同じ $g$ で $D_1\subseteq D_2$ なら $D_2$ を捨てる。小さい $D$ の方が分割不能語を見つけやすい）で大幅に減る。
なお完全性は $r$ について単調（$r=2$ の規則は $r\ge3$ の規則でもある）なので、$r=2$ で完全なら全 $r$ で完全であり、実装ではこれを高速路に使う。

### 2.4 判定手続きの検証（観察）

定理 2.2・2.3 を、独立に実装した区間 DP（`parses`：$can[i][j]$ = 部分語 $w[i:j]$ が $X_{\varphi(w[i:j])}$ から解析できる、
$part[k][i][j]$ = $k$ 個の解析可能部分への分割、長さの小さい順）と突き合わせた。

- $n=2$（$\lvert H\rvert=6$）：**全ての** $2^6$ 個の $V$ について $r=2$ で一致（不一致 0）。
- $n=2,3$、$r=2,3,4$：各 $(n,r)$ についてランダムな 120 個の $V$ で一致（**計 720 例、不一致 0**）。
- 判定手続きが「不完全」と言った場合、その証人は実際に $\ell\le12$ の範囲で見つかった（有限の観察）。

この検証の過程で、区間 DP の側に2つの実装上の落とし穴があった（$k$ 部分分割の表を「1部分＝1文字」で初期化していた点、および最後の1文字の逆元の向き）。
両方とも修正した上で上の一致を得ている。**判定手続き（定理 2.2・2.3）はこの報告の全ての数値の土台なので、この一致は重要である。**

---

## 3. C1：値付き文法の族

### 3.1 方法

- $n=2,3$：**全探索**。$V\supseteq\{1,a,b\}$ を大きさの小さい順に全て試し、定理 2.2・2.3 で完全性を判定。最初に完全になったものが最小（定理 2.2・2.3 が厳密なので、これは証明である）。
  試した部分集合の個数は $n=3$ で $\sum_{k=3}^{13}\binom{18}{k-3}=156\,000$ 程度。
- $n=4,5,6$：**貪欲法＋局所探索**。$V=H$ から出発し、1個ずつ落としても完全な限り落とす（ランダム順、複数回）。その後、大きさを保つ1-swap 局所探索。
  $r\ge3$ ではオートマトンの状態数が増えるので、状態数の上限（4000）を置き、上限に達したら「完全性は未確認」として**その要素を落とさない**（＝受理した $V$ は必ず完全。従って報告値は最小値の**上界**）。
- 各 $V$ について、$\lvert V\rvert$、$\lVert G_V\rVert$、$\bar\theta$、$N$、直径、還元性（全非終端が到達可能かつ生産的）を計算し、
  さらに**独立な全数検査**として、値 $1$ の全ての語（長さ $\le13$ または $14$）が区間 DP で解析できることを確かめた。

### 3.2 結果

**表 3.1（$H_n$、値付き文法 $G_V$）**

| $n$ | $\lvert H\rvert$ | $N=\operatorname{ord}(\varphi(a))$ | 直径 | $r$ | 最小 $\lvert V\rvert$ | 方法 | $\lVert G_V\rVert$ | $\bar\theta$（下界） | 厳密な完全性 | 全数検査の長さ |
|---|---|---|---|---|---|---|---|---|---|---|
| 2 | 6 | 3 | 2 | 2 | **5** | 全探索 | 114 | 7（≥4） | ✓ | 14 |
| 2 | 6 | 3 | 2 | 3 | **4** | 全探索 | 390 | 9（≥4） | ✓ | 14 |
| 2 | 6 | 3 | 2 | 4 | **3** | 全探索 | 520 | 12（≥4） | ✓ | 14 |
| 3 | 21 | 7 | 5 | 2 | **13** | 全探索 | 557 | 17（≥7） | ✓ | 13 |
| 3 | 21 | 7 | 5 | 3 | **8** | 全探索 | 1 370 | 16（≥6） | ✓ | 13 |
| 3 | 21 | 7 | 5 | 4 | **6** | 全探索 | 3 710 | 19（≥6） | ✓ | 13 |
| 4 | 60 | 15 | 8 | 2 | **37** | 貪欲 | 4 366 | 29（≥12） | ✓ | 13 |
| 4 | 60 | 15 | 8 | 3 | ≤35 | 貪欲（上限付き） | 178 851 | 38（≥12） | ✓ | 12 |
| 4 | 60 | 15 | 8 | 4 | ≤35 | 貪欲（上限付き） | 8 064 291 | 47（≥12） | ✓ | 12 |
| 5 | 155 | 31 | 10 | 2 | **87** | 貪欲 | 21 506 | 38（≥15） | ✓ | 13 |
| 5 | 155 | 31 | 10 | 3 | ≤87 | （下記注） | — | — | — | — |
| 6 | 378 | 63 | 13 | 2 | **212** | 貪欲 | 126 641 | 50（≥19） | ✓ | 13 |
| 6 | 378 | 63 | 13 | 3 | ≤212 | （下記注） | — | — | — | — |

注（$n=5,6$ の $r\ge3$）：上限付き貪欲は $n=5$ で 89、$n=6$ で 213 を返したが、どちらも $r=2$ の値（87、212）より悪い。
完全性は $r$ について単調（$r=2$ の規則は $r\ge3$ の規則でもある）なので $\min_{r\ge3}\lvert V\rvert\le87$（$n=5$）、$\le212$（$n=6$）が確定しており、
89・213 は探索が局所解に落ちたことを示すだけである。従って $n\ge5$ の $r\ge3$ については新しい情報が無く、表には $r=2$ の上界を流用する。
$r\ge3$ で $r=2$ を明確に上回ったのは $n=2,3$（全探索）と $n=4$（37 → 35）だけである。

**表 3.1b（実際の要件 (b) での最小 $\lvert V\rvert$。値 $1$ の全数検査による上界）**

| $n$ | $r$ | (a) 厳密 | (b) 上界 | (b) の検査長 | (b) の $V$ の大きさ／$\lvert H\rvert$ |
|---|---|---|---|---|---|
| 2 | 2 | 5 | **5** | 14 | 0.83 |
| 2 | 3 | 4 | **3** | 14 | 0.50 |
| 2 | 4 | 3 | **3** | 14 | 0.50 |
| 3 | 2 | 13 | **≤12** | 13 | ≤0.57 |
| 3 | 3 | 8 | **≤8** | 13 | ≤0.38 |
| 3 | 4 | 6 | **≤6** | 13 | ≤0.29 |

（$n=2$ の $r\ge3$ で (b) が 3 になるのは $V=\{1,a,b\}$。$n=3,r=3$ の「≤8」は (a) の 8 をそのまま流用したもので、
(b) の貪欲は 9 で止まった（局所解）。$n=3,r=2$ の 12 は貪欲の上界で、厳密な (b) 最小は 12 以下。）

**表 3.2（比と増え方、$r=2$）**

| $n$ | $\lvert H\rvert=n(2^n-1)$ | $N=2^n-1$ | 最小 $\lvert V\rvert$（上界） | $\lvert V\rvert/\lvert H\rvert$ | $\lVert G_V\rVert$ | $\bar\theta$ | $\lVert G_V\rVert/N$ |
|---|---|---|---|---|---|---|---|
| 2 | 6 | 3 | 5（厳密） | 0.833 | 114 | 7 | 38 |
| 3 | 21 | 7 | 13（厳密） | 0.619 | 557 | 17 | 80 |
| 4 | 60 | 15 | 37 | 0.617 | 4 366 | 29 | 291 |
| 5 | 155 | 31 | 87 | 0.561 | 21 506 | 38 | 694 |
| 6 | 378 | 63 | 212 | 0.561 | 126 641 | 50 | 2 010 |

### 3.3 読み方

1. **$\lvert V\rvert$ は $\lvert H\rvert$ の定数割合**（$r=2$ で 0.56–0.83、$n\ge3$ ではほぼ 0.56–0.62）。$\lvert H\rvert=n(2^n-1)$ なので $\lvert V\rvert$ は $n$ について指数である。
   $n=2,3$ は全探索なので**証明済み**、$n\ge4$ は貪欲の上界なので「そのような $V$ が存在する」ことの観察である（最小性は未証明）。
2. **$\lVert G_V\rVert$ は $\lvert V\rvert$ の多項式**（$r=2$ で $\lvert V\rvert+4+5c_2$、$c_2\approx0.56\lvert V\rvert^2$）。従って $\lVert G_V\rVert$ も $n$ について指数。
   表 3.2 の最後の列のように $\lVert G_V\rVert/N$ は $n$ とともに増える。
3. **$\bar\theta$ は小さい**。$\bar\theta=7,17,29,38,50$（$n=2,\dots,6$）で、大体 $3$–$4$ 倍の直径、$8n$ 程度。$N=2^n-1$ と比べると $n=6$ で $\bar\theta=50<N=63$。
   つまり $H_n$ では**厚さは多項式（実際ほぼ線形）なのに、大きさが指数**である。これは $a^{2^j}=b^{n-j}ab^j$（長さ $n+1$）のせいで、
   $a^{2^j}$ の最短表示が $O(n)$ になるからである。Claude の報告 §2.3 の「重い節点の値は短い語で書ける」という観察が、まさにこの形で実現している。
4. 従って、素朴な不等式 $N\le(\lVert G_V\rVert\bar\theta)^c$ は $c=1$ でも余裕で成り立つ（$\lVert G_V\rVert\gg N$）。**この族は問題G の反例ではない。**

### 3.4 ランクを上げるとどうなるか

$n=2,3$（全探索）では $r$ を上げると最小 $\lvert V\rvert$ は単調に減る：$n=3$ で $13\to8\to6$（$r=2,3,4$）。
$n=4$ では $37\to\le35\to\le35$ で、$r\ge3$ の利得は小さい（探索が同じ局所解に落ちている可能性もある）。
理由は明快で、ランク $r$ が大きいと「$r$ 文字以下の語で値が $V$ に入るものは無条件に解析できる」ので、$V$ を小さくできる。
しかし $n$ を固定して $r$ を上げても、必要なおおよその要素数は $\lvert H\rvert$ の定数割合より下がりきらないように見える（$n=4$ で 0.58）。
**固定した $r$ に対して $\lvert V\rvert$ が $n$ について多項式になる証拠は無い。**

### 3.5 条件 (a) と (b) の差（どこまで小さい $V$ で $L(G_V)=L$ になるか）

(a) の最小値は (b) の上界なので、実際にどこまで下がるかを別に測った。方法は「値 $1$ の全ての語（長さ $\le L$）を区間 DP で解析する」全数検査で、
$H$ から出発して1個ずつ落とす貪欲（`check_true_min.py`）と、$n=2$ の全部分集合の検査（`check_value1_only.py`）を使った。

- $n=2$（$\lvert H\rvert=6$）：$r=2$ では (b) の最小は 5 で (a) と一致。$r=3,4$ では (b) の最小は **3**（$V=\{1,a,b\}$）で、(a) の 4 より小さい。
  $V=\{1,a,b\}$ は値 $1$ の語だけを見れば完全（長さ $\le14$ で確認）だが、値 $a$ などの語が解析できず (a) を満たさない。
- $n=3$（$\lvert H\rvert=21$）：$r=2$ で (b) の上界は **12**（(a) は 13）、$r=3$ で 8（(a) と同じ、貪欲は 9 で停止）。
- いずれも $\lvert V\rvert/\lvert H\rvert$ は 0.29–0.83 で、**指数性の結論は変わらない**。

つまり (a) は (b) より少し強いが、$\lvert V\rvert$ の増え方（$\lvert H\rvert$ の定数割合）は同じである。
(b) を厳密に判定する手続き（長さの上限なし）は本報告では与えていない。これは残作業である。

---

## 4. C2：一般の文脈自由文法との関係

### 4.1 非終端の値は一つに定まる

**補題 4.1.** $G$ を reduced な文脈自由文法（ファンアウト1、ランク $\le r$）で $L(G)=L$ とする。各非終端 $X$ について、$L_X$ の全ての語は同じ値を持つ。

*証明.* reduced なので $X$ は生産的で、原稿 `lem:thickness-equivalence`(iv) の文脈 $E_X$（成功導出から $X$ 部分木を1個消して得られる文脈）が存在し、任意の $u\in L_X$ について $E_X[u]\in L(G)=L$。
$E_X=v_0\blank v_1$ と書けば $\varphi(v_0)\varphi(u)\varphi(v_1)=1$、群なので $\varphi(u)=\varphi(v_0)^{-1}\varphi(v_1)^{-1}$ は $u$ に依らない。□

（この補題は Claude の報告 §2.3 の最初の項目の証明である。原稿の定理A(i) と同じ議論。）

### 4.2 模擬補題：一般の文法 → 値付き文法

**定理 4.2（模擬補題）.** $G$ を reduced good なファンアウト1・ランク $\le r$（$r\ge2$）の文脈自由文法で $L(G)=L$ とする。このとき
$$V^*\subseteq H,\quad \lvert V^*\rvert\le\lVert G\rVert+2,\quad L(G_{V^*})=L$$
が存在する。従って
$$\boxed{\ \min\{\lvert V\rvert:L(G_V)=L\}\ \le\ \lVert G\rVert+2\ }\qquad\text{つまり}\qquad \lVert G\rVert\ \ge\ \min\lvert V\rvert-2 .$$

*証明.*
(1) $V_0:=\{v(X):X\in V(G)\}$ とおく（補題 4.1）。$1=v(S)\in V_0$。
(2) 規則 $R:\ X\to\alpha_0Y_1\alpha_1\cdots Y_k\alpha_k$（$\alpha_i\in\Sigma^*$、$k\le r$）を「平らな列」
$\alpha_0$ の各文字、$Y_1$、$\alpha_1$ の各文字、…、$Y_k$、$\alpha_k$ の各文字
に分ける。文字数 $\sum_i\lvert\alpha_i\rvert$ と $k$ 個の子、合わせて $p_R:=\sum_i\lvert\alpha_i\rvert+k$ 個の部分（ピース）になる。
この列の接頭辞の値（＝$\varphi$ による積）を全部 $V^*$ に入れる。ピースの値は
「1文字なら $a$ か $b$」「子なら $v(Y_j)\in V_0$」なので、接頭辞の値の個数は高々 $p_R$ 個。
(3) よって $\lvert V^*\rvert\le\lvert V_0\rvert+\sum_R p_R+2\le\lvert V\rvert+\sum_R(1+k+\sum_i\lvert\alpha_i\rvert)+2=\lVert G\rVert+2$
（$p_R\le1+k+\sum_i\lvert\alpha_i\rvert=$ 規則 $R$ の大きさ、原稿の定義）。$+2$ は $a,b$ を確実に入れるため。
(4) $L(G_{V^*})\supseteq L(G)$ を導出木の帰納法で示す。$X\Rightarrow^* y$ なら $y$ が $X_{v(X)}$ から $G_{V^*}$ で導出できる。
規則 $R$ の適用で $y=\alpha_0y_1\alpha_1\cdots y_k\alpha_k$ となるとき、平らな列の接頭辞の値の列
$1=g_0,g_1,\dots,g_{p_R}=v(X)$ は全て $V^*$ に入り、各ピースの値 $g_{i-1}^{-1}g_i$ も $V^*$ に入る（1文字なら $a,b$、子なら $v(Y_j)$）。
左結合の2分木で $X_{g_{p}}\to X_{g_{p-1}}X_{g_{p-1}^{-1}g_p}$、… と分解すれば、葉は1文字（$X_a\to a$、$X_b\to b$）と
子の生成物（帰納法の仮定）になる。ランクは2なので $r\ge2$ で許される。
(5) 逆向き $L(G_{V^*})\subseteq L$ は値の定義から明らか。□

### 4.3 系：問題G への橋

**系 4.3.** 固定した $r\ge2$ とアルファベット $\{a,b\}$ について、次の2つの最小値は多項式因子を除いて等しい：
$$\min\{\lVert G\rVert:\ G\ \text{は reduced good、ファンアウト1、ランク}\le r,\ L(G)=L\},
\qquad
\min\{\lVert G_V\rVert:\ L(G_V)=L\}.$$

*証明.* $G_V$ は一般の文法なので左 $\le$ 右。逆向きは定理 4.2 と $\lVert G_{V^*}\rVert=O_r(\lvert V^*\rvert^r)$ から。□

**問題G への帰結.** 群の族 $(H_n,\varphi_n)$ について、もし
$\min\lvert V\rvert\ \ge\ c\,\lvert H_n\rvert$（$c>0$ は $n$ に依らない）が**証明**できれば、定理 4.2 によりランク $\le r$ の任意の文法で
$$\lVert G\rVert\ \ge\ c\,n\,(2^n-1)-2\ \ge\ 2^n-1=N\qquad(n\ \text{大}),$$
すなわち $N\le\lVert G\rVert$。これは問題G の多項式（実際1次）上界であり、**問題G は $H_n$ 上で正**となる。

### 4.4 多重非終端は $\lvert V\rvert$ を減らせるか

一般の文法は同じ値の非終端を複数持てる。定理 4.2 は「値を共有する非終端を1つにまとめても言語は減らない」ことを示している
（まとめた文法 $G_{V^*}$ は元の文法の生成物を全て生成する）。従って**多重非終端は値付き族に対する本質的な利点を与えない**。
これは依頼文 C2 の問い（最小 $\lvert V\rvert$ が一般の文法の非終端数の下界になるか）への答えで、
「下界になる」が正しく、しかも定数倍（$\lVert G\rVert\ge\min\lvert V\rvert-2$）で成り立つ。

ただし注意：定理 4.2 の $V^*$ は「平らな列の接頭辞の値」を全部入れるので、$\lvert V^*\rvert$ は $\lVert G\rVert$ 程度まで大きくなりうる。
$\min\lvert V\rvert$ を**非終端数の**下界として読むには $\lVert G\rVert\ge\lvert V(G)\rvert$ を使えばよい（定義より明らか）。

---

## 5. C3：可換群との比較

$H=\mathbb Z/N$、$\varphi(a)=1$、$\varphi(b)=\lambda$（$\lambda\in\mathbb Z/N$）。$L=\{w:\lvert w\rvert_a+\lambda\lvert w\rvert_b\equiv0\}$。
同じ判定手続き（定理 2.2・2.3 は群の一般論なのでそのまま使える）で最小 $\lvert V\rvert$ を求めた。

**表 5.1（可換群、$r=2$。$N=7$ は全探索、$N\ge15$ は貪欲の上界）**

| $N$ | $\lambda$ | 直径 | $\lvert V\rvert$ | $\lvert V\rvert/N$ | $\bar\theta$ | $\bar\theta/N$ | 方法 |
|---|---|---|---|---|---|---|---|
| 7 | 1 | 6 | 5 | 0.71 | 28 | 4.0 | 全探索 |
| 7 | 2 | 3 | 6 | 0.86 | 16 | 2.3 | 全探索 |
| 7 | 3 | 3 | 6 | 0.86 | 12 | 1.7 | 全探索 |
| 15 | 1 | 14 | 7 | 0.47 | 60 | 4.0 | 貪欲 |
| 15 | 2 | 7 | 10 | 0.67 | 32 | 2.1 | 貪欲 |
| 15 | 3 | 6 | 10 | 0.67 | 25 | 1.7 | 貪欲 |
| 31 | 1 | 30 | 8 | 0.26 | 186 | 6.0 | 貪欲 |
| 31 | 2 | 15 | 15 | 0.48 | 80 | 2.6 | 貪欲 |
| 31 | 3 | 11 | 18 | 0.58 | 46 | 1.5 | 貪欲 |
| 63 | 1 | 62 | 13 | 0.21 | 315 | 5.0 | 貪欲 |
| 63 | 2 | 31 | 18 | 0.29 | 192 | 3.0 | 貪欲 |
| 63 | 3 | 22 | 30 | 0.48 | 86 | 1.4 | 貪欲 |

（$N=7$ の $r=3$：$\lambda=1$ で $\lvert V\rvert=3$、$\lambda=2,3$ で $4$。$\bar\theta$ はそれぞれ 35、20、15。[^1]）

[^1]: 貪欲は種（乱数）で結果が変わる。$\bar\theta$ は $V$ に依存するので、同じ $\lvert V\rvert$ でも $\bar\theta$ は数割動く（例：$N=15,\lambda=1$ で 60 と 75）。比 $\bar\theta/N$ の桁は変わらない。

**読み方.** 可換群では $\lvert V\rvert$ は $N$ よりずっとゆっくり増える（$\lambda=1$ で $5,7,8,13$。$\log N$ 程度か）。
その代わり $\bar\theta$ が $N$ 程度（$\lambda=1$ では girth が $N$ そのもの）に大きくなる。つまり
$$N\ \lesssim\ \bar\theta\qquad(\text{全ての検査で } \bar\theta\ge N/3),$$
であり、Claude の報告 §2.3 の予想「可換なら位数は $\bar\theta$ のおよそ二乗で抑えられる」は、今回の範囲では**もっと強い形**（$N\lesssim\bar\theta$）で成り立っている。
非可換 $H_n$ との違いは**コストの場所**である：非可換では $\bar\theta$ が $O(n)$ に留まる代わりに $\lvert V\rvert$（従って $\lVert G_V\rVert$）が指数的、
可換では $\lvert V\rvert$ が小さい代わりに $\bar\theta$ が指数的である。問題G が難しいのは前者の状況だけである。

---

## 6. C4：乗数を変えた族

$H=\mathbb Z/(q^n-1)\rtimes\mathbb Z/n$、$b:x\mapsto qx$（$q=3,4$）。$q$ は $\bmod q^n-1$ で位数 $n$、$a^{q^j}=b^{n-j}ab^j$ が同様に成り立つ。
$r=2$ の貪欲の結果：

| $q$ | $n$ | $N=q^n-1$ | $\lvert H\rvert$ | 直径 | $\lvert V\rvert$ | $\lvert V\rvert/\lvert H\rvert$ | $\lVert G_V\rVert$ | $\bar\theta$ |
|---|---|---|---|---|---|---|---|---|
| 3 | 2 | 8 | 16 | 5 | 10 | 0.62 | 354 | 18 |
| 3 | 3 | 26 | 78 | 9 | 45 | 0.58 | 5 949 | 29 |
| 4 | 2 | 15 | 30 | 7 | 17 | 0.57 | 886 | 24 |
| 4 | 3 | 63 | 189 | 12 | 104 | 0.55 | 29 908 | 42 |

比は $q=2$ の 0.56–0.62 と同じである。従って「$\lvert V\rvert$ が $\lvert H\rvert$ の定数割合」は乗数 $2$ に固有の現象ではなく、
この型のアフィン族一般の性質らしい。**問題G の反例を作るには、この比を $0$ に近づける別の仕組みが要る。**

---

## 7. 問題G の見通し

今回の計算は、問題G の候補族 $H_n$ について、**否定（反例）の方向には何も出なかった**。むしろ逆向きの強い証拠が出た。

1. 値付き文法の完全性には厳密な判定手続きがあり（定理 2.2・2.3）、$n=2,3$ の全探索で最小 $\lvert V\rvert$ は $5,13$（$r=2$、条件 (a)）、
   $n=4,5,6$ の貪欲で $37,87,212$。いずれも $\lvert H\rvert=n(2^n-1)$ の 0.56–0.83 倍で、$n$ について指数。
   実際の要件 (b) で緩めても $\lvert V\rvert/\lvert H\rvert$ は 0.29–0.83 で、指数性は変わらない（§3.5）。
2. $\bar\theta$ は小さく（$n=6$ で 50、$N=63$）、$\lVert G_V\rVert$ は $10^5$ 台。$N$ は $\lVert G_V\rVert$ に比べて小さい。
3. 模擬補題（定理 4.2）により、一般の文脈自由文法（同じランク）でも $\lVert G\rVert\ge\min\lvert V\rvert-2$。
   従って $\min\lvert V\rvert$ が $\lvert H\rvert$ の定数割合である**証明**が出れば、問題G は $H_n$ 上で正で決着する（$N\le\lVert G\rVert$）。
4. 足りないのは $\min\lvert V\rvert$ の**下界の証明**だけである。$n\ge4$ は貪欲の上界しか無い。
   下界の手がかりとして、値 $g$ の分割不能語の存在は「$H\setminus H_g$ の路の存在」（$r=2$）という有限の条件なので、
   $V$ が小さいときに路を作れることを示せばよい。たとえば $a$ 軸（$\langle a\rangle$ の $n$ 個の剰余類）ごとに
   「$H_g$ に入らない接頭辞値」を並べる議論が考えられるが、今回は時間が足りず証明に至らなかった。

**問題G 自体の現状**：未解決。ただし今回の結果は「$H_n$ は反例ではない」ことを強く示唆し、
反例を作るには (i) $\lvert V\rvert/\lvert H\rvert\to0$ となる別の群の族、(ii) 値付き族の完全性を逃れる別の文法の形、
のどちらかが必要である。定理 4.2 は (ii) の道をほぼ塞いでいる（多重非終端では逃れられない）ので、
残る可能性は (i) の「別の族」に絞られる。可換群が (i) になりえないことも §5 が示している（$\bar\theta$ が指数的になる）。

---

## 8. スクリプト全文

### 8.1 本体（判定・探索・大きさ・厚さ）

`reviews/check_group_word_problem_2026_11_01.py`（Python 3 標準ライブラリのみ。`py -3 check_group_word_problem_2026_11_01.py c1` で $n=2,3$ の全探索（表 3.1 の上6行）を再生成し、$n=4,5$ の $r=2$ の貪欲まで進む。$r\ge3$ の貪欲は遅いので、表の残りは `run_greedy.py` / `run_greedy_capped.py` で個別に実行した）。

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Group word problem vs. context-free grammar size (problem G of paper #2).

Value-labelled grammars G_V: nonterminals X_g (g in V subset of H), rules
    X_g -> x                   (x in Sigma = {a,b}, phi(x) = g)
    X_g -> X_{h1} ... X_{hk}   (2 <= k <= r, h_i in V, h1...hk = g)
The generated language is always a subset of L = phi^{-1}(1) cap Sigma^+.
C1: minimal V with L(G_V) = L, and the growth of |V|, ||G_V||, theta.

Exactness: the completeness test below is exact (no length cut-off); brute
force (length <= lmax) is used only as an independent check.

Windows:  py -3 check_group_word_problem_2026-11-01.py c1
"""
import sys, time, random
from collections import deque
from itertools import combinations


# ================================================================= groups
class FiniteGroup:
    def __init__(self, tab, one, la, lb, names=None):
        self.tab = tab
        self.M = len(tab)
        self.itab = [0] * self.M
        for x in range(self.M):
            for y in range(self.M):
                if tab[x][y] == one:
                    self.itab[x] = y
                    break
        self.one = one
        self.LA, self.LB = la, lb
        self.letters = (la, lb)
        self.names = names or [str(i) for i in range(self.M)]
        self._dist = None
        self.nbr = [[self.tab[x][y] for y in self.letters] for x in range(self.M)]

    def dist(self):
        if self._dist is None:
            d = [None] * self.M
            d[self.one] = 0
            q = deque([self.one])
            while q:
                x = q.popleft()
                for y in self.letters:
                    z = self.tab[x][y]
                    if d[z] is None:
                        d[z] = d[x] + 1
                        q.append(z)
            self._dist = d
        return self._dist

    def girth(self):
        d = self.dist()
        return min(1 + d[self.itab[x]] for x in self.letters)

    def diameter(self):
        return max(self.dist())

    def word_value(self, w):
        t = self.one
        for x in w:
            t = self.tab[t][x]
        return t


def make_affine(n, mult=2):
    """H = Z/N : Z/n, N = mult^n - 1 (mult has order n mod N);
       (j,c): x -> mult^j x + c (mod N); a = (0,1) (x->x+1),
       b = (1,0) (x -> mult x);  |H| = n(N).  mult=2 gives H_n."""
    N = mult ** n - 1
    els = [(j, c) for j in range(n) for c in range(N)]
    idx = {e: i for i, e in enumerate(els)}
    M = len(els)
    tab = [[0] * M for _ in range(M)]
    for x, (j1, c1) in enumerate(els):
        for y, (j2, c2) in enumerate(els):
            tab[x][y] = idx[((j1 + j2) % n, (pow(mult, j2, N) * c1 + c2) % N)]
    names = ['b^%d a^%d' % (j, c) for (j, c) in els]
    g = FiniteGroup(tab, idx[(0, 0)], idx[(0, 1)], idx[(1, 0)], names)
    g.n, g.N = n, N
    return g


def make_cyclic(N, lam=1):
    """Z/N with a -> 1, b -> lam."""
    tab = [[(i + j) % N for j in range(N)] for i in range(N)]
    g = FiniteGroup(tab, 0, 1 % N, lam % N, ['a^%d' % i for i in range(N)])
    g.n, g.N = None, N
    return g


# ================================================================= exact tests
def complete_r2(G, V):
    """EXACT rank-2 criterion.  G_V is complete at every value of V iff for
    every g in V, in the graph induced on H \\ H_g (H_g = V cap gV^{-1}), no
    vertex of {a,b}\\H_g reaches a vertex of {g.a^{-1}, g.b^{-1}}\\H_g
    (the possible values of the last proper prefix)."""
    Vf = frozenset(V)
    tab, inv = G.tab, G.itab
    for g in Vf:
        Hg = set()
        for h in Vf:
            if tab[inv[h]][g] in Vf:
                Hg.add(h)
        starts = [x for x in G.letters if x not in Hg]
        if not starts:
            continue
        targets = set()
        for x in G.letters:
            y = tab[g][inv[x]]          # last letter x: y . phi(x) = g
            if y not in Hg:
                targets.add(y)
        if not targets:
            continue
        seen = set(starts)
        dq = deque(starts)
        while dq:
            u = dq.popleft()
            if u in targets:
                return False, g
            for w in G.nbr[u]:
                if w not in Hg and w not in seen:
                    seen.add(w)
                    dq.append(w)
    return True, None


def bad_word_r(G, V, r, target, cap=200000):
    """EXACT for any r >= 2: word w with value target, |w|>=2, every split of w
    into 2..r parts has a part with value outside V.  BFS on (value, D),
    D = set of (s,k) = (prefix value at last split point, closed parts).
    All states have length >= 2 (seeded by the four words of length 2), so the
    terminal test is uniform and the subset pruning is sound."""
    Vf = frozenset(V)
    one, tab, inv = G.one, G.tab, G.itab

    def closure(D, g):
        add = set()
        for (s, k) in D:
            if k + 1 <= r - 1 and tab[inv[s]][g] in Vf:
                add.add((g, k + 1))
        return D | frozenset(add) if add else D

    def term_ok(g, D):
        return any(k >= 1 and k + 1 <= r and tab[inv[s]][g] in Vf for (s, k) in D)

    base = frozenset({(one, 0)})
    seen = set()
    byval = {}
    q = deque()
    for x in G.letters:
        for y in G.letters:
            g1 = tab[one][x]
            D1 = closure(base, g1)          # one split, at position 1
            st = (tab[g1][y], D1)
            if st in seen:
                continue
            seen.add(st)
            byval.setdefault(st[0], []).append(D1)
            q.append((st, (x, y)))
    while q:
        (g, D), w = q.popleft()
        if g == target and not term_ok(g, D):
            return w, None
        D2 = closure(D, g)
        for x in G.letters:
            g2 = tab[g][x]
            st = (g2, D2)
            if st in seen:
                continue
            if any(Dold <= D2 for Dold in byval.get(g2, ())):
                continue
            seen.add(st)
            byval.setdefault(g2, []).append(D2)
            q.append((st, w + (x,)))
            if len(seen) > cap:
                return None, 'cap'
    return None, None


def complete_exact(G, V, r):
    """EXACT: is every word whose value lies in V parseable from its X_g?
    (Sufficient for L(G_V) = L; the decision procedure for this condition.)
    Monotone in r, so an r=2-complete V is complete for every r."""
    ok2, _ = complete_r2(G, V)
    if ok2:
        return True, None
    if r == 2:
        return False, _
    Vf = frozenset(V)
    for g in sorted(Vf):
        w, why = bad_word_r(G, Vf, r, g)
        if why == 'cap':
            return None, g
        if w is not None:
            return False, g
    return True, None


# ================================================================= brute force
def parses(G, V, r, w):
    """can[i][j]: w[i:j] parses from X_{val(i,j)}; part[k][i][j]: w[i:j] splits
    into exactly k parseable parts (no condition on val(i,j) itself)."""
    m = len(w)
    if m == 0:
        return False
    p = [G.one]
    for x in w:
        p.append(G.tab[p[-1]][x])
    ip = [G.itab[x] for x in p]
    val = [[0] * (m + 1) for _ in range(m + 1)]
    for i in range(m):
        for j in range(i + 1, m + 1):
            val[i][j] = G.tab[ip[i]][p[j]]
    can = [[False] * (m + 1) for _ in range(m + 1)]
    part = [[[False] * (m + 1) for _ in range(m + 1)] for _ in range(r + 1)]
    for L in range(1, m + 1):
        for i in range(0, m - L + 1):
            j = i + L
            if L == 1:
                can[i][j] = val[i][j] in V
            else:
                for k in range(2, min(r, L) + 1):
                    pk, pkm1 = part[k], part[k - 1]
                    for mid in range(i + 1, j):
                        if pkm1[i][mid] and can[mid][j]:
                            pk[i][j] = True
                            break
                if val[i][j] in V:
                    for k in range(2, min(r, L) + 1):
                        if part[k][i][j]:
                            can[i][j] = True
                            break
            part[1][i][j] = can[i][j]
    return can[0][m]


def first_unparsed(G, V, r, maxlen, values=None):
    values = {G.one} if values is None else set(values)
    bad = []

    def rec(pref, t):
        if bad:
            return
        if len(pref) >= 2 and t in values and not parses(G, V, r, pref):
            bad.append(tuple(pref))
            return
        if len(pref) == maxlen:
            return
        for x in G.letters:
            pref.append(x)
            rec(pref, G.tab[t][x])
            pref.pop()
    rec([], G.one)
    return bad[0] if bad else None


# ================================================================= search
def greedy_min(G, r, seed=0, try_local=True):
    V = set(range(G.M))
    rng = random.Random(seed)
    improved = True
    while improved:
        improved = False
        cand = [x for x in V if x not in (G.one, G.LA, G.LB)]
        rng.shuffle(cand)
        for x in cand:
            W = V - {x}
            ok, _ = complete_exact(G, W, r)
            if ok:
                V = W
                improved = True
    return V


def one_swap(G, r, V, tries=200, seed=0):
    """local search at constant size: replace x in V by y outside V."""
    rng = random.Random(seed)
    V = set(V)
    for _ in range(tries):
        out = [x for x in range(G.M) if x not in V]
        ins = [x for x in V if x not in (G.one, G.LA, G.LB)]
        if not out or not ins:
            break
        x, y = rng.choice(ins), rng.choice(out)
        W = (V - {x}) | {y}
        ok, _ = complete_exact(G, W, r)
        if ok:
            V = W
    return V


# ================================================================= size, theta
def rule_counts(G, V, r):
    """number of rules X_p -> X_{q1}...X_{qk} with all q_i in V and product in V
    (= p), for each k; computed by convolution over the group."""
    V = list(V)
    Vf = frozenset(V)
    tab = G.tab
    cnt = {}
    cur = {x: 1 for x in V}                 # number of 1-tuples with product x
    for k in range(2, r + 1):
        nxt = {}
        for q in V:
            for x, c in cur.items():
                y = tab[q][x]
                nxt[y] = nxt.get(y, 0) + c
        c = sum(nxt.get(p, 0) for p in Vf)
        cnt[k] = c
        cur = nxt
    return cnt


def grammar_size(G, V, r, nletters=2):
    v = len(V)
    cnt = rule_counts(G, V, r)
    s = v + nletters * 2
    for k, c in cnt.items():
        s += c * (1 + 2 * k)               # 1 + rank + |template|
    return s, cnt


def theta_bar(G, V, r):
    """theta_G(R) = length of the shortest sentence of L(G) using R.
    With completeness at all values of V the shortest yield of X_g is d*(g)
    (Cayley distance; girth for g = 1, lambda-free).  Returns (theta, lower).
    The value is an upper bound for theta_G: the context costs C(q) use the
    relaxation "q can be a child of a p-rule", which can only enlarge C."""
    V = list(V)
    Vf = frozenset(V)
    dist = G.dist()
    gir = G.girth()
    dstar = {x: dist[x] for x in V}
    dstar[G.one] = gir
    tab, inv, one = G.tab, G.itab, G.one
    fmax = [None] * (r + 1)
    fmax[1] = {x: dstar[x] for x in V}
    for k in range(2, r + 1):
        fk = {}
        for p in range(G.M):
            best = -1
            for q in V:
                prev = fmax[k - 1].get(tab[inv[q]][p])
                if prev is None:
                    continue
                cand = prev + dstar[q]
                if cand > best:
                    best = cand
            if best >= 0:
                fk[p] = best
        fmax[k] = fk
    prod = [None] * (r + 1)
    prod[1] = set(Vf)
    for k in range(2, r + 1):
        prod[k] = {tab[a][b] for a in prod[k - 1] for b in Vf}
    C = {one: gir}
    for _ in range(3 * len(V) + 10):
        changed = False
        for p in V:
            if p not in C:
                continue
            base = C[p] - dstar[p]
            for k in range(2, r + 1):
                if p not in fmax[k]:
                    continue
                tot = base + fmax[k][p]
                for q in V:
                    if tab[inv[q]][p] not in prod[k - 1]:
                        continue
                    if q not in C or tot < C[q]:
                        C[q] = tot
                        changed = True
        if not changed:
            break
    worst = 1
    for p in V:
        if p not in C:
            continue
        base = C[p] - dstar[p]
        for k in range(2, r + 1):
            if p in fmax[k]:
                worst = max(worst, base + fmax[k][p])
    lower = fmax[2].get(one, 1) if r >= 2 else 1
    return worst, lower


def reachable(G, V, r):
    Vf = frozenset(V)
    tab, inv = G.tab, G.itab
    prod = [None] * (r + 1)
    prod[1] = set(Vf)
    for k in range(2, r + 1):
        prod[k] = {tab[a][b] for a in prod[k - 1] for b in Vf}
    reached = {G.one}
    changed = True
    while changed:
        changed = False
        for p in list(reached):
            for k in range(2, r + 1):
                for q in Vf:
                    if q in reached:
                        continue
                    if tab[inv[q]][p] in prod[k - 1]:
                        reached.add(q)
                        changed = True
    return reached


# ================================================================= C1
def fmt_v(G, V, maxn=12):
    ns = sorted(G.names[x] for x in V)
    if len(ns) <= maxn:
        return '{%s}' % ', '.join(ns)
    return '{%s, ...} (%d elements)' % (', '.join(ns[:maxn]), len(ns))


def wstr(G, w):
    return ''.join('a' if x == G.LA else 'b' for x in w)


def section_c1(ns=(2, 3, 4, 5), ranks=(2, 3, 4), exact_n=(2, 3), lmax=14):
    print('=' * 80)
    print('C1  value-labelled grammars for H_n = Z/(2^n-1) : Z/n')
    print('=' * 80)
    rows = []
    for n in ns:
        G = make_affine(n)
        print('\nn=%d : |H|=%d  N=ord(a)=%d  diameter=%d  girth=%d'
              % (n, G.M, G.N, G.diameter(), G.girth()))
        for r in ranks:
            t0 = time.time()
            if n in exact_n:
                method = 'exact'
                base = {G.one, G.LA, G.LB}
                rest = [x for x in range(G.M) if x not in base]
                V = None
                for k in range(len(base), G.M + 1):
                    for extra in combinations(rest, k - len(base)):
                        W = base | set(extra)
                        ok, _ = complete_exact(G, W, r)
                        if ok:
                            V = W
                            break
                    if V:
                        break
            else:
                method = 'greedy+swap'
                V = greedy_min(G, r, seed=100 * n + r)
                V = one_swap(G, r, V, tries=150, seed=7)
            ok, wit = complete_exact(G, V, r)
            bad = first_unparsed(G, V, r, lmax)
            size, cnt = grammar_size(G, V, r)
            th, low = theta_bar(G, V, r)
            rech = reachable(G, V, r)
            print('  r=%d  |V|=%-4d  ||G_V||=%-8d  theta=%-3d[>=%d]  '
                  'compl=%s  brute(%d)=%s  reduced=%s  %.1fs'
                  % (r, len(V), size, th, low, ok, lmax,
                     'ok' if bad is None else 'FAIL ' + wstr(G, bad),
                     len(rech) == len(V), time.time() - t0))
            print('        V = %s' % fmt_v(G, V))
            rows.append(dict(n=n, r=r, v=len(V), size=size, theta=th, theta_lo=low,
                             H=G.M, N=G.N, diam=G.diameter(), method=method,
                             exact=ok, brute=bad, reduced=len(rech) == len(V),
                             V=sorted(V), rules=cnt))
    return rows


if __name__ == '__main__':
    what = sys.argv[1] if len(sys.argv) > 1 else 'c1'
    if what == 'c1':
        section_c1()

```

補助スクリプト 1：報告の数値をまとめて再計算する（`py -3 run_all_outputs.py` → `out_all.txt`）。

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Reproduces every number in the report that is cheap to recompute.
Output goes to out_all.txt (and stdout).
Windows: py -3 run_all_outputs.py
"""
import sys, time
from itertools import combinations
from check_group_word_problem_2026_11_01 import (make_affine, make_cyclic,
                                                 complete_exact, complete_r2,
                                                 bad_word_r, first_unparsed,
                                                 grammar_size, theta_bar,
                                                 reachable, greedy_min, one_swap)

F = open('out_all.txt', 'w', encoding='utf-8')


def p(*a):
    s = ' '.join(str(x) for x in a)
    print(s)
    sys.stdout.flush()
    F.write(s + '\n')
    F.flush()


def row(G, V, r, lmax=13):
    ok, _ = complete_exact(G, V, r)
    size, cnt = grammar_size(G, V, r)
    th, low = theta_bar(G, V, r)
    rech = reachable(G, V, r)
    bad = first_unparsed(G, V, r, lmax)
    return dict(v=len(V), size=size, th=th, low=low, ok=ok, rech=len(rech),
                rules=cnt, brute=(bad is None))


def exact_min(G, r, kmax):
    base = {G.one, G.LA, G.LB}
    rest = [x for x in range(G.M) if x not in base]
    for k in range(len(base), min(kmax, G.M) + 1):
        t0 = time.time()
        cnt = 0
        for extra in combinations(rest, k - len(base)):
            cnt += 1
            V = base | set(extra)
            ok, _ = complete_exact(G, V, r)
            if ok:
                return k, V, cnt, time.time() - t0
        p('        |V|=%d : %6d subsets checked, none' % (k, cnt))
    return None, None, 0, 0.0


p('#' * 72)
p('# A. group H_n = Z/(2^n-1) : Z/n,  a = (x->x+1), b = (x->2x)')
p('#' * 72)
for n in range(2, 7):
    G = make_affine(n)
    # order of a, of b
    x, oa = G.one, None
    for k in range(1, G.N + 2):
        x = G.tab[x][G.LA]
        if x == G.one:
            oa = k
            break
    x, ob = G.one, None
    for k in range(1, n + 2):
        x = G.tab[x][G.LB]
        if x == G.one:
            ob = k
            break
    # surjectivity: BFS from identity
    seen = {G.one}
    frontier = [G.one]
    while frontier:
        nf = []
        for u in frontier:
            for y in G.letters:
                z = G.tab[u][y]
                if z not in seen:
                    seen.add(z)
                    nf.append(z)
        frontier = nf
    ident = all(G.word_value([G.LB] * (n - j) + [G.LA] + [G.LB] * j) ==
                G.word_value([G.LA] * (1 << j)) for j in range(n))
    rev = all(G.word_value([G.LB] * j + [G.LA] + [G.LB] * (n - j)) ==
              G.word_value([G.LA] * (1 << j)) for j in range(n))
    p('n=%d  N=%d  |H|=%d  ord(a)=%d  ord(b)=%d  diam=%d  girth=%d  '
      'generated=%d  a^{2^j}=b^{n-j}ab^j:%s  reversed form:%s'
      % (n, G.N, G.M, oa, ob, G.diameter(), G.girth(), len(seen),
         'yes' if ident else 'NO', 'yes' if rev else 'no'))

p('')
p('#' * 72)
p('# C1. value-labelled grammars G_V   (exact minimisation for n=2,3;')
p('#     greedy + 1-swap for n=4,5,6, r=2)')
p('#' * 72)
for n in (2, 3):
    G = make_affine(n)
    p('n=%d  |H|=%d  N=%d  diam=%d  girth=%d' % (n, G.M, G.N, G.diameter(), G.girth()))
    for r in (2, 3, 4):
        t0 = time.time()
        k, V, cnt, dt = exact_min(G, r, kmax=G.M if n == 2 else 15)
        if V is None:
            p('  r=%d : no complete V up to size 15' % r)
            continue
        d = row(G, V, r, 14)
        p('  r=%d  MIN |V|=%d (exhaustive, %d subsets, %.1fs)  ||G_V||=%d  '
          'theta=%d (>=%d)  complete=%s  brute(l<=14)=%s  reduced=%s'
          % (r, k, cnt, dt, d['size'], d['th'], d['low'], d['ok'], d['brute'],
             d['rech'] == d['v']))
        p('        V = {%s}' % ', '.join(G.names[x] for x in sorted(V)))
for n in (4, 5, 6):
    G = make_affine(n)
    p('n=%d  |H|=%d  N=%d  diam=%d  girth=%d' % (n, G.M, G.N, G.diameter(), G.girth()))
    for r in (2,):
        t0 = time.time()
        V = greedy_min(G, r, seed=100 * n + r)
        V = one_swap(G, r, V, tries=40, seed=3)
        d = row(G, V, r, 13)
        p('  r=%d  GREEDY |V|=%d/%d (%.3f |H|)  ||G_V||=%d  theta=%d (>=%d)  '
          'complete=%s  brute(l<=13)=%s  reduced=%s  (%.0fs)'
          % (r, d['v'], G.M, d['v'] / G.M, d['size'], d['th'], d['low'], d['ok'],
             d['brute'], d['rech'] == d['v'], time.time() - t0))
        p('        rules per k = %s' % (d['rules'],))

p('')
p('#' * 72)
p('# C3. abelian H = Z/N, a -> 1, b -> lambda')
p('#' * 72)
for N in (7, 15, 31, 63):
    for lam in (1, 2, 3):
        G = make_cyclic(N, lam)
        p('N=%d lam=%d  |H|=%d  diam=%d  girth=%d' % (N, lam, G.M, G.diameter(), G.girth()))
        if N == 7:
            for r in (2, 3):
                k, V, cnt, dt = exact_min(G, r, kmax=N)
                if V is None:
                    p('  r=%d : none' % r)
                    continue
                d = row(G, V, r, 12)
                p('  r=%d  MIN |V|=%d (exhaustive)  ||G_V||=%d  theta=%d  '
                  'complete=%s  V={%s}' % (r, k, d['size'], d['th'], d['ok'],
                                           ', '.join(G.names[x] for x in sorted(V))))
        else:
            V = greedy_min(G, 2, seed=7 + lam)
            V = one_swap(G, 2, V, tries=30, seed=5)
            d = row(G, V, 2, 11)
            p('  r=2  GREEDY |V|=%d/%d (%.2f N)  theta=%d  complete=%s'
              % (d['v'], G.M, d['v'] / G.M, d['th'], d['ok']))

p('')
p('#' * 72)
p('# C4. multiplier q: H = Z/(q^n-1) : Z/n')
p('#' * 72)
for q in (3, 4):
    for n in (2, 3):
        G = make_affine(n, q)
        V = greedy_min(G, 2, seed=10 * q + n)
        V = one_swap(G, 2, V, tries=20, seed=1)
        d = row(G, V, 2, 11)
        p('q=%d n=%d  N=%d  |H|=%d  diam=%d  |V|=%d (%.2f|H|)  ||G_V||=%d  '
          'theta=%d  complete=%s'
          % (q, n, G.N, G.M, G.diameter(), d['v'], d['v'] / G.M, d['size'],
             d['th'], d['ok']))
F.close()

```

---

### 8.2 判定手続きの検証スクリプト（720 例の一致検査）

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""exploration 7: validate both exact criteria against the corrected DP."""
import random, itertools, time, sys
from check_group_word_problem_2026_11_01 import (make_affine, make_cyclic,
                                                 complete_r2, bad_word_r, parses)


def brute_first_bad(G, V, r, maxlen, values):
    bad = []

    def rec(pref, t):
        if bad:
            return
        if len(pref) >= 2 and t in values and not parses(G, V, r, pref):
            bad.append(tuple(pref))
            return
        if len(pref) == maxlen:
            return
        for x in G.letters:
            pref.append(x)
            rec(pref, G.tab[t][x])
            pref.pop()
    rec([], G.one)
    return bad[0] if bad else None


def check(G, r, tests, maxlen):
    nfalse = 0
    for V in tests:
        # (a) criterion for rank r
        Vf = frozenset(V)
        exact = True
        for g in Vf:
            w, why = bad_word_r(G, Vf, r, g)
            if w is not None:
                exact = False
                break
        bf = brute_first_bad(G, V, r, maxlen, Vf)
        if exact and bf is not None:
            print('  MISMATCH: exact says complete, brute finds', bf, 'V=', sorted(V))
            nfalse += 1
        if (not exact) and bf is None:
            # exact witness may be longer than maxlen; check the witness parses
            pass
    return nfalse


def main():
    for n in (2, 3):
        G = make_affine(n)
        print('n=%d |H|=%d' % (n, G.M))
        rng = random.Random(11)
        base = {G.one, G.LA, G.LB}
        rest = [x for x in range(G.M) if x not in base]
        for r in (2, 3, 4):
            tests = []
            for _ in range(120):
                k = rng.randint(0, min(len(rest), 12))
                tests.append(base | set(rng.sample(rest, k)))
            t0 = time.time()
            nf = check(G, r, tests, 12)
            print('  r=%d: %d sets, mismatches=%d, %.1fs' % (r, len(tests), nf, time.time() - t0))


if __name__ == '__main__':
    main()
```

---

## 9. 出力

### 9.1 群の検証（`check_affine`、$n=2,\dots,6$）

```text
########################################################################
# A. group H_n = Z/(2^n-1) : Z/n,  a = (x->x+1), b = (x->2x)
########################################################################
n=2  N=3  |H|=6  ord(a)=3  ord(b)=2  diam=2  girth=2  generated=6  a^{2^j}=b^{n-j}ab^j:yes  reversed form:yes
n=3  N=7  |H|=21  ord(a)=7  ord(b)=3  diam=5  girth=3  generated=21  a^{2^j}=b^{n-j}ab^j:yes  reversed form:no
n=4  N=15  |H|=60  ord(a)=15  ord(b)=4  diam=8  girth=4  generated=60  a^{2^j}=b^{n-j}ab^j:yes  reversed form:no
n=5  N=31  |H|=155  ord(a)=31  ord(b)=5  diam=10  girth=5  generated=155  a^{2^j}=b^{n-j}ab^j:yes  reversed form:no
n=6  N=63  |H|=378  ord(a)=63  ord(b)=6  diam=13  girth=6  generated=378  a^{2^j}=b^{n-j}ab^j:yes  reversed form:no

```

### 9.2 C1（$n=2,3$ 全探索、$n=4,5,6$ 貪欲）

```text
# C1. value-labelled grammars G_V   (exact minimisation for n=2,3;
#     greedy + 1-swap for n=4,5,6, r=2)
########################################################################
n=2  |H|=6  N=3  diam=2  girth=2
        |V|=3 :      1 subsets checked, none
        |V|=4 :      3 subsets checked, none
  r=2  MIN |V|=5 (exhaustive, 1 subsets, 0.0s)  ||G_V||=114  theta=7 (>=4)  complete=True  brute(l<=14)=True  reduced=True
        V = {b^0 a^0, b^0 a^1, b^0 a^2, b^1 a^0, b^1 a^1}
        |V|=3 :      1 subsets checked, none
  r=3  MIN |V|=4 (exhaustive, 1 subsets, 0.0s)  ||G_V||=390  theta=9 (>=4)  complete=True  brute(l<=14)=True  reduced=True
        V = {b^0 a^0, b^0 a^1, b^0 a^2, b^1 a^0}
  r=4  MIN |V|=3 (exhaustive, 1 subsets, 0.0s)  ||G_V||=520  theta=12 (>=4)  complete=True  brute(l<=14)=True  reduced=True
        V = {b^0 a^0, b^0 a^1, b^1 a^0}
n=3  |H|=21  N=7  diam=5  girth=3
        |V|=3 :      1 subsets checked, none
        |V|=4 :     18 subsets checked, none
        |V|=5 :    153 subsets checked, none
        |V|=6 :    816 subsets checked, none
        |V|=7 :   3060 subsets checked, none
        |V|=8 :   8568 subsets checked, none
        |V|=9 :  18564 subsets checked, none
        |V|=10 :  31824 subsets checked, none
        |V|=11 :  43758 subsets checked, none
        |V|=12 :  48620 subsets checked, none
  r=2  MIN |V|=13 (exhaustive, 1670 subsets, 0.0s)  ||G_V||=557  theta=17 (>=7)  complete=True  brute(l<=14)=True  reduced=True
        V = {b^0 a^0, b^0 a^1, b^0 a^2, b^0 a^3, b^0 a^4, b^0 a^5, b^1 a^0, b^1 a^1, b^1 a^3, b^1 a^4, b^2 a^0, b^2 a^1, b^2 a^5}
        |V|=3 :      1 subsets checked, none
        |V|=4 :     18 subsets checked, none
        |V|=5 :    153 subsets checked, none
        |V|=6 :    816 subsets checked, none
        |V|=7 :   3060 subsets checked, none
  r=3  MIN |V|=8 (exhaustive, 281 subsets, 1.3s)  ||G_V||=1370  theta=16 (>=6)  complete=True  brute(l<=14)=True  reduced=True
        V = {b^0 a^0, b^0 a^1, b^0 a^2, b^0 a^3, b^1 a^0, b^1 a^1, b^1 a^2, b^2 a^2}
        |V|=3 :      1 subsets checked, none
        |V|=4 :     18 subsets checked, none
        |V|=5 :    153 subsets checked, none
  r=4  MIN |V|=6 (exhaustive, 66 subsets, 0.4s)  ||G_V||=3710  theta=19 (>=6)  complete=True  brute(l<=14)=True  reduced=True
        V = {b^0 a^0, b^0 a^1, b^0 a^2, b^1 a^0, b^1 a^1, b^2 a^2}
n=4  |H|=60  N=15  diam=8  girth=4
  r=2  GREEDY |V|=37/60 (0.617 |H|)  ||G_V||=4366  theta=29 (>=12)  complete=True  brute(l<=13)=True  reduced=True  (0s)
        rules per k = {2: 865}
n=5  |H|=155  N=31  diam=10  girth=5
  r=2  GREEDY |V|=87/155 (0.561 |H|)  ||G_V||=21506  theta=38 (>=15)  complete=True  brute(l<=13)=True  reduced=True  (1s)
        rules per k = {2: 4283}
n=6  |H|=378  N=63  diam=13  girth=6
  r=2  GREEDY |V|=212/378 (0.561 |H|)  ||G_V||=126641  theta=50 (>=19)  complete=True  brute(l<=13)=True  reduced=True  (7s)
        rules per k = {2: 25285}

```

### 9.3 C3（可換群）

```text
# C3. abelian H = Z/N, a -> 1, b -> lambda
########################################################################
N=7 lam=1  |H|=7  diam=6  girth=7
        |V|=2 :      1 subsets checked, none
        |V|=3 :      5 subsets checked, none
        |V|=4 :     10 subsets checked, none
  r=2  MIN |V|=5 (exhaustive)  ||G_V||=99  theta=28  complete=True  V={a^0, a^1, a^2, a^3, a^4}
        |V|=2 :      1 subsets checked, none
  r=3  MIN |V|=3 (exhaustive)  ||G_V||=109  theta=35  complete=True  V={a^0, a^1, a^3}
N=7 lam=2  |H|=7  diam=3  girth=4
        |V|=3 :      1 subsets checked, none
        |V|=4 :      4 subsets checked, none
        |V|=5 :      6 subsets checked, none
  r=2  MIN |V|=6 (exhaustive)  ||G_V||=165  theta=16  complete=True  V={a^0, a^1, a^2, a^3, a^4, a^5}
        |V|=3 :      1 subsets checked, none
  r=3  MIN |V|=4 (exhaustive)  ||G_V||=296  theta=20  complete=True  V={a^0, a^1, a^2, a^4}
N=7 lam=3  |H|=7  diam=3  girth=3
        |V|=3 :      1 subsets checked, none
        |V|=4 :      4 subsets checked, none
        |V|=5 :      6 subsets checked, none
  r=2  MIN |V|=6 (exhaustive)  ||G_V||=165  theta=12  complete=True  V={a^0, a^1, a^2, a^3, a^4, a^6}
        |V|=3 :      1 subsets checked, none
  r=3  MIN |V|=4 (exhaustive)  ||G_V||=268  theta=15  complete=True  V={a^0, a^1, a^2, a^3}
N=15 lam=1  |H|=15  diam=14  girth=15
  r=2  GREEDY |V|=7/15 (0.47 N)  theta=60  complete=True
N=15 lam=2  |H|=15  diam=7  girth=8
  r=2  GREEDY |V|=10/15 (0.67 N)  theta=32  complete=True
N=15 lam=3  |H|=15  diam=6  girth=5
  r=2  GREEDY |V|=10/15 (0.67 N)  theta=25  complete=True
N=31 lam=1  |H|=31  diam=30  girth=31
  r=2  GREEDY |V|=8/31 (0.26 N)  theta=186  complete=True
N=31 lam=2  |H|=31  diam=15  girth=16
  r=2  GREEDY |V|=15/31 (0.48 N)  theta=80  complete=True
N=31 lam=3  |H|=31  diam=11  girth=11
  r=2  GREEDY |V|=18/31 (0.58 N)  theta=46  complete=True
N=63 lam=1  |H|=63  diam=62  girth=63
  r=2  GREEDY |V|=13/63 (0.21 N)  theta=315  complete=True
N=63 lam=2  |H|=63  diam=31  girth=32
  r=2  GREEDY |V|=18/63 (0.29 N)  theta=192  complete=True
N=63 lam=3  |H|=63  diam=22  girth=21
  r=2  GREEDY |V|=30/63 (0.48 N)  theta=86  complete=True

```

### 9.4 C4（乗数 $q=3,4$）

```text
# C4. multiplier q: H = Z/(q^n-1) : Z/n
########################################################################
q=3 n=2  N=8  |H|=16  diam=5  |V|=10 (0.62|H|)  ||G_V||=354  theta=18  complete=True
q=3 n=3  N=26  |H|=78  diam=9  |V|=45 (0.58|H|)  ||G_V||=5949  theta=29  complete=True
q=4 n=2  N=15  |H|=30  diam=7  |V|=17 (0.57|H|)  ||G_V||=886  theta=24  complete=True
q=4 n=3  N=63  |H|=189  diam=12  |V|=104 (0.55|H|)  ||G_V||=29908  theta=42  complete=True

```

### 9.5 判定手続きと区間 DP の一致検査（720 例）

```text
n=2 |H|=6
  r=2: 120 sets, mismatches=0, 62.1s
  r=3: 120 sets, mismatches=0, 154.7s
  r=4: 120 sets, mismatches=0, 194.0s
n=3 |H|=21
  r=2: 120 sets, mismatches=0, 3.0s
  r=3: 120 sets, mismatches=0, 40.2s
  r=4: 120 sets, mismatches=0, 63.4s
```

### 9.6 条件 (b)（値 1 だけの完全性）の検査

```text
n=2 r=2 |H|=6  brute length 14
  smallest (of the tested V) passing value-1 completeness: |V|=5, also complete at every value? True
  V = b^0 a^0, b^0 a^1, b^0 a^2, b^1 a^0, b^1 a^1
n=2 r=3 |H|=6  brute length 14
  smallest (of the tested V) passing value-1 completeness: |V|=3, also complete at every value? False
  V = b^0 a^0, b^0 a^1, b^1 a^0
n=2 r=4 |H|=6  brute length 14
  smallest (of the tested V) passing value-1 completeness: |V|=3, also complete at every value? False
  V = b^0 a^0, b^0 a^1, b^1 a^0

n=3 r=2 |H|=21  value-1-only min |V| <= 12  (2s, brute length 13)
   ||G_V||=451  theta<=18  strict-complete(r=2)=False  reduced=True
   V = b^0 a^0, b^0 a^1, b^0 a^2, b^0 a^3, b^0 a^6, b^1 a^0, b^1 a^2, b^1 a^3, b^1 a^4, b^2 a^0, b^2 a^1, b^2 a^3
n=3 r=3 |H|=21  value-1-only min |V| <= 9  (3s, brute length 13)
   ||G_V||=2596  theta<=24  strict-complete(r=2)=False  reduced=True
   V = b^0 a^0, b^0 a^1, b^0 a^3, b^0 a^4, b^0 a^6, b^1 a^0, b^1 a^3, b^1 a^4, b^2 a^2
```

---

## 10. 他の報告の主張の確認

依頼文の指示どおり、使う前に確かめた。

| 主張（Claude の報告） | 確認結果 |
|---|---|
| $a^{2^j}=b^{n-j}ab^j$（長さ $n+1$） | **確認**。$n\le6$、全ての $j$ で数値一致（出力 A）。逆向きは偽（§1.1） |
| $b^n=1$、$\operatorname{ord}(a)=N=2^n-1$、$\lvert H_n\rvert=n(2^n-1)$ | **確認** |
| 各非終端の生成物は同じ値を持つ | **確認＋証明**（補題 4.1） |
| 可換の場合、位数は $\bar\theta$ のおよそ二乗で抑えられる | **今回の範囲ではもっと強い**（$\bar\theta\gtrsim N/3$、表 5.1） |
| 問題G が否定なら `op:S1` が否定で解ける | 使っていない（今回は問題G を直接計算した）。含意自体は原稿の定理A(iii) から従う |
| $L_{\varphi,1}$ が小さい文法を持つかは不明 | **今回の計算で「値付き族では指数的」と分かった**。一般の文法でも定理 4.2 により同程度の下界 |

なお、Claude の報告 §7 のスクリプトが「$n=2..8$ で数値確認」と書いている等式は、今回独立に実装して $n\le6$ で確認した（$n=7,8$ は計算していない）。

---

## 11. 限界と次の課題

1. **$n\ge4$ の最小性は未証明**。貪欲は 1要素除去について極小だが、大域最小ではない。厳密な最小を $n=4$ で求めるには
   $\binom{57}{k}$ の全探索は無理なので、分枝限定か ILP が要る。今回の $n=4$ の値（37）は上界である。
2. **$\bar\theta$ は上界**。文脈コスト $C$ の緩和（§1.2）のため、報告値より真の値が小さい可能性がある。ただし桁は変わらない（$O(r\cdot\text{直径})$）。
3. **$\min\lvert V\rvert$ の下界の証明**が最重要の残作業。$r=2$ なら定理 2.2 のグラフ条件なので、組合せ的に攻められる可能性がある。
4. 定理 2.3 のオートマトンは状態数が最悪で二重指数なので、$n\ge6$、$r\ge4$ の厳密計算には記号化（$D$ の同値類）が要る。
5. 問題G の反例候補としては、今回のアフィン族以外（ランプライター型、$Z/p\rtimes Z/(p-1)$ の別の生成元）を試す余地が残っている。
   ただし定理 4.2 があるので、$\lvert V\rvert/\lvert H\rvert\to0$ を示せる族でなければならない。

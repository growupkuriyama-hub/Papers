# 窓の型付けにおける最短特徴標本の長さ — 族 F_n の厳密計算

- 実行日: 2026-10-31（Asia/Tokyo）
- 対象原稿: `02-v2-lg-fanout-boundary/main.tex`（変更していない）
- 成果物: `02-v2-lg-fanout-boundary/reviews/check_window_gap_search.py`、本報告書
- 実行環境: Windows, Python 3.12（`py -3`）、標準ライブラリのみ
- 計算の位置づけ: ファンアウト1、ランク上限2の作用素 $B_{1,s}^{\le 2}$ を定義どおり実装し、$F_n$ の $n\le 4$ を厳密に（または上界・下界を）計算した。$n\le 3$ の一部は全数検査、$n=3$ の最短値は未解決、$n=4$ は上界と下界。

---

## 0. 主張の判定表

| # | 主張 | 判定 | 根拠 |
|---|---|---|---|
| 1 | $B_{1,s}^{\le2}$ の実装が定義（Start/Const/Comp/Link、$q\le2$、空ギャップ可）と一致する | 計算による検証 | §2 の T1。原稿の標識族と括弧付き倍増族で既知の結論を再現 |
| 2 | $\|G_n\|=12n+7$、$\theta_{G_n}=4n-1$ | 証明 | §6.1 補題 1（規則の数え上げと最短文の帰納法） |
| 3 | 各型の $\mu_m$ の表（$n\le5$） | 証明 | §3.1、§6.1 補題 2（型長漸化式） |
| 4 | $n=1$ の $\mathrm{cs}=8$（全型付け） | 証明（全数検査） | §3.2、$2^2$ 部分集合の全数検査 |
| 5 | $n=2$ の $\mathrm{cs}$：$s_{00}=20$, $s_{01}=44$, $s_{10}=36$, $s_{11}=44$ | 証明（全数検査） | §3.2、$2^6$ 部分集合の全数検査 |
| 6 | $n=3$ の上界：$s_{00}\le38$, $s_{01}\le94$, $s_{10}\le86$, $s_{11}\le144$ | 計算 | §3.2、局所探索。$s_{01},s_{10},s_{11}$ は full $B$ で再検証済み |
| 7 | $n=3$ の下界：$s_{00}\ge8$, $s_{01}\ge22$, $s_{10}\ge20$, $s_{11}\ge34$ | 証明 | 希少型の下界（原稿 prop:rare-type）の代入 |
| 8 | $n=3$ の $s_{01}$ の下界 60（$A$-部分問題） | 計算による観察（未証明） | §3.2。$A$ 型12語を覆う最小コストの探索。任意の補助語を許す厳密証明ではない |
| 9 | $n=4$ の上界：$s_{00}\le62$, $s_{01}\le210$, $s_{10}\le158$, $s_{11}\le336$ | 計算 | §3.2。$s_{01},s_{10},s_{11}$ は maxgap=0 の部分作用素で検証（full $B$ の上界として有効） |
| 10 | 証拠集合 $\mathrm{Wit}$ の長さの閉形式（$s_{00},s_{01},s_{10},s_{11}$） | 計算（$n\le30$）＋漸近の証明 | §3.3、§6.2。$\Theta(n^2)$ か $\Theta(n^3)$ かは証明、定数付き閉形式は計算 |
| 11 | $F_n$ は $n\le4$ で Clark–Eyraud 代入可能 | 計算（全数検査） | §6.3。原稿の既知事実の再現 |
| 12 | $F_n$ は全ての $n$ で Clark–Eyraud 代入可能 | **未解決** | §6.3。決定的パーサの単射性に障害（反例あり）。$n\le4$ のみ検証 |
| 13 | 証拠集合（標準標本）の長さは $s_{00},s_{10}$ で $\Theta(n^2)=\Theta(\|G\|\bar\theta)$ | 証明 | §6.2 の上界と §3.3 の閉形式 |
| 14 | 証拠集合（標準標本）の長さは $s_{01},s_{11}$ で $\Theta(n^3)=\Theta(\|G\|^2\bar\theta)$ | 証明 | §6.2 の上界と閉形式 |
| 15 | 最短 $\mathrm{cs}$ の次数：$s_{10}$ は $n^2$ 型、$s_{01}$ は $n^3$ 型に近い | **観察**（$n\le4$） | §4。上界の比 $1.84$（$s_{10}$）対 $2.23$（$s_{01}$） |
| 16 | 償却（長い語1本で全段を賄う）は $F_n$ では自動的には起きない | 計算 | §3.4。$\{S_n,R_n\}$ は 2 語しか導出しない |
| 17 | 互いに共有できない長い代表を必要とする族では $\mathrm{cs}$ は加法的 | 証明＋計算 | §5。非交差アルファベットの2本の背骨で $\mathrm{cs}=2\,\mathrm{cs}(F_n)$ |
| 18 | 主問い（窓の型付けで $\Theta(\|G\|\bar\theta)$ か $\Theta(\|G\|^2\bar\theta)$ か） | **型付け依存**（部分的解決） | §4、§7。一様な答えはない |

記号: $s_{00}=s_{\mathrm{triv}}$, $s_{01}=s_{0,1}$（末尾1文字）, $s_{10}=s_{1,0}$（先頭1文字）, $s_{11}=s_{1,1}$（先頭と末尾）。

---

## 1. 設定と実装

### 1.1 作用素 $B_{1,s}^{\le2}$

有限集合 $K\subseteq\Sigma^+$ に対し、$\mathrm{Obs}(K)$ を $K$ の語の空でない因子全体とする。$B_{1,s}^{\le2}(K)$ の非終端は $[x]$（$x\in\mathrm{Obs}(K)$）で、規則は

- Start: $\widehat S\to[w]$（$w\in K$）、
- Const: $[x]\to x$（$x\in\mathrm{Obs}(K)$）、
- Comp: $x=\alpha_0u_1\alpha_1\cdots u_q\alpha_q$（$1\le q\le2$、$u_i\in\mathrm{Obs}(K)$ 非空、$\alpha_i\in\Sigma^*$）に対し $[x]\to\alpha_0[u_1]\alpha_1\cdots[u_q]\alpha_q$、
- Link: $s(x)=s(y)$ かつ $uxv,uyv\in K$ なる共通文脈 $(u,v)$ があるとき $[x]\to[y]$。

ファンアウト1では $q=2$ の中間ギャップ $\alpha_1$ は空でよい（原稿の非併合条件は同一子の連続成分にのみ課される）。本実装はこの定義をそのまま実装している。

### 1.2 実装の要点

- Link は同値関係を生成する（対称で、共通文脈を介して推移閉包を取る）。実装では union-find で Link 成分に縮約した。
- 到達可能性は区間 DP（forward CYK）で判定する。目標語 $w$ の各区間 $[i,j)$ に対し、その区間を導出する Link 成分の集合 $R[i][j]$ を長さの短い順に計算する。Comp は子区間 $[p,e]$、$[e+b,q]$ と親文字列 $x=\mathrm{prefix}+u_1+\mathrm{mid}+u_2+\mathrm{suffix}$ を構成し、$x\in\mathrm{Obs}(K)$ かを見る。これにより規則を列挙せず、到達した非終端だけを展開する。
- 健全性（原稿 prop:reconstruction-soundness）により、$F\subseteq L$ が特徴標本であることは $L\subseteq L(B(F))$ と同値である（規則集合は $K$ について単調）。実際、$F$ が特徴標本なら $K=F$ で $L(B(F))=L$。逆に $L\subseteq L(B(F))$ なら、任意の $F\subseteq K\subseteq L$ に対し $B(F)\subseteq B(K)$ なので $L\subseteq L(B(F))\subseteq L(B(K))\subseteq L$。
- 制限作用素 `maxgap=g`: Comp の全ギャップの長さを $g$ 以下に制限した部分作用素。$B^{\mathrm{gap}\le g}\subseteq B$ なので、これで被覆が言えれば full $B$ でも被覆が言える（$n=4$ の上界検証に使用）。
- 検算:
  - 原稿の標識族（$f=1$、$q,k$ 小）で「特徴標本は $L$ 全体だけ」を再現（各語が essential）。
  - 括弧付き倍増族で「型1の語 $W_n$ が必ず要る」を再現（$W_n$ は型1の唯一語で、$L\setminus\{W_n\}$ から導出できない）。

### 1.3 族 $F_n$ と型付け

$$E_0\to a,\qquad E_i\to lE_{i-1}E_{i-1}\mid cE_{i-1}r\quad(1\le i\le n),\qquad S\to E_n.$$

$L_n=L(E_n)$、語数 $2,6,42,1806,\ldots$。型付けは
$$s_{k,\ell}(w)=w\ (|w|<\max\{1,k+\ell\}),\qquad s_{k,\ell}(w)=(\mathrm{pref}_k(w),\mathrm{suf}_\ell(w))\ (\text{otherwise}).$$
本報告では $s_{00},s_{01},s_{10},s_{11}$ を扱う。

---

## 2. T1: 基盤検証

### 2.1 標識族（linear-factor family）

$f=1$ の標識族
$$L^{(1)}_{q,k}=\{a^iAb^iBc^iCd^iDz^{4(q-i)+2^k}:0\le i\le q\}$$
について、$q\le3$、$k\le2$ で「$L$ の任意の真部分集合は特徴標本でない」ことを全数検査した。各語 $w$ について $L\setminus\{w\}$ が $w$ を導出できるかを調べ、すべての $w$ で導出不能（=essential）だった。これは原稿 prop:linear-factor-all-fanout(ii) の「唯一の特徴標本は $L$ 自身」という結論と一致する。

### 2.2 括弧付き倍増族

$E_0\to a$、$E_i\to pE_{i-1}E_{i-1}q\mid uE_{i-1}v$（$p,q,u,v$ は括弧の代用文字）で、$s_U$ は $u,v$ を型0、他を型1に送る。$n\le3$ で
- 型1の語は $W_n=pW_{n-1}W_{n-1}q$ ただ1つ、
- $L\setminus\{W_n\}$ は $W_n$ を導出しない
ことを確認した。これは原稿 prop:bracketed-family(iii)(iv) と一致する。

（出力は §付録 A.1。）

---

## 3. T2: $F_n$ の計算

### 3.1 (a) 文法量と $\mu_m$

**補題 1（証明）.** $G_n$ は縮約済み良形で
$$\|G_n\|=12n+7,\qquad \theta_{G_n}=4n-1\quad(n\ge1).$$

*証明.* 非終端は $S,E_0,\ldots,E_n$ の $n+2$ 個。規則は $S\to E_n$（サイズ $1+1+1=3$）、$E_0\to a$（$1+0+1=2$）、$E_i\to lE_{i-1}E_{i-1}$（$1+2+3=6$）が $n$ 本、$E_i\to cE_{i-1}r$（$1+1+3=5$）が $n$ 本。よって $(n+2)+3+2+11n=12n+7$。$\theta$ は各規則を使う最短文の長さの最大。$S\to E_n$ は最短語（長さ $2n+1$）、$E_0\to a$ は $1$、$E_i\to lE_{i-1}E_{i-1}$ は $1+2(2i-1)=4i-1$、$E_i\to cE_{i-1}r$ は $(2i-1)+2=2i+1$。最大は $4n-1$。$\square$

**補題 2（証明）.** 各段の型ごとの最短語長は次のとおり（$i\ge1$）：
- $s_{00}$: $m_i=2i+1$（$m_0=1$）。
- $s_{01}$: $p_i=i^2+i+1$（型 $a$）、$q_i=2i+1$（型 $r$）。
- $s_{10}$: $\ell_i=4i-1$（型 $l$）、$c_i=2i+1$（型 $c$）。
- $s_{11}$: $(l,a)_i=i^2+i+1$、$(c,r)_i=2i+1$、$(l,r)_i=4i-1$（$i\ge2$）。$i=1$ では $(l,a),(c,r)$ のみで長さ3。

*証明.* 型の合成（$l$ 規則は先頭を $l$、末尾を第2子の末尾にし、$c$ 規則は先頭 $c$・末尾 $r$ にする）に関する帰納法。$s_{01}$ の $a$ 型は右端の全 $l$ 背骨で、各段の第1子に最短語（長さ $2(i-1)+1$）を置くので $p_i=1+p_{i-1}+(2(i-1)+1)=p_{i-1}+2i$、$p_0=1$ より $p_i=i^2+i+1$。$r$ 型は $c$ 連鎖で $q_i=q_{i-1}+2$、$q_0=1$ より $q_i=2i+1$。他も同様。$\square$

数値（スクリプトの出力）:

| $n$ | $\|G_n\|$ | $\theta_{G_n}$ | $\|L_n\|$ | $\|L_n\|_+$ | $\mu_a$（$s_{01}$） | $\mu_r$（$s_{01}$） |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | 19 | 3 | 2 | 8 | 3 | 3 |
| 2 | 31 | 7 | 6 | 44 | 7 | 5 |
| 3 | 43 | 11 | 42 | 584 | 13 | 7 |
| 4 | 55 | 15 | 1806 | 49724 | 21 | 9 |
| 5 | 67 | 19 | 3263442 | 179656424 | 31 | 11 |

$s_{10}$ では $\mu_l=4n-1$、$\mu_c=2n+1$。$s_{11}$ では $\mu_{(l,a)}=n^2+n+1$、$\mu_{(l,r)}=4n-1$（$n\ge2$）、$\mu_{(c,r)}=2n+1$。

### 3.2 (b) 最短特徴標本 $\mathrm{cs}$

#### $n=1$（全数検査、証明）

$L_1=\{laa,car\}$。どの型付けでも2語とも必要で、$\mathrm{cs}=8$。

#### $n=2$（全数検査、証明）

$L_2$ の6語（$ccarr,claar,lcarcar,lcarlaa,llaacar,llaalaa$）の $2^6=64$ 部分集合を全数検査した。

| 型付け | $\mathrm{cs}$ | 最短標本の例 |
|---|---:|---|
| $s_{00}$ | 20 | $\{ccarr,claar,lcarcar\}$ |
| $s_{01}$ | 44 | $L_2$ 全体 |
| $s_{10}$ | 36 | $L_2\setminus\{llaalaa\}$ |
| $s_{11}$ | 44 | $L_2$ 全体 |

$s_{01},s_{11}$ では $n=2$ で全語が必要である。$s_{10}$ では $llaalaa$（全 $l$ 語）だけが不要。

#### $n=3$（上界は計算、下界は希少型）

$|L_3|=42$、$\|L_3\|_+=584$。全数検査は $2^{42}$ で不可能なので、次の上界・下界を求めた。

| 型付け | 下界（希少型、証明） | 上界（計算） | 上界の標本 |
|---|---:|---:|---|
| $s_{00}$ | 8 | 38 | 証拠集合（4語） |
| $s_{01}$ | 22 | 94 | 局所探索（8語、full $B$ で検証） |
| $s_{10}$ | 20 | 86 | 局所探索（8語、full $B$ で検証） |
| $s_{11}$ | 34 | 144 | 局所探索（12語、full $B$ で検証） |

上界の標本（$s_{01}$、長さ94）:
```
cccarrr, cclaarr, clcarcarr, cllaacarr, lccarrccarr,
llcarlaalcarlaa, llcarcarlcarlaa, llcarlaaclaar
```
上界の標本（$s_{10}$、長さ86）:
```
cccarrr, cclaarr, clcarcarr, cllaacarr, cllaalaar,
lccarrccarr, llcarcarccarr, lccarrlcarcar
```
上界の標本（$s_{11}$、長さ144、12語）:
```
cclaarr, clcarlaar, lccarrlcarcar, lccarrlcarlaa, llcarlaaccarr,
llcarlaalcarlaa, lccarrclaar, lccarrllaacar, llcarcarclaar,
cllaalaar, clcarcarr, cccarrr
```

$s_{01}$ の下界については、$A=\{w\in L_3:w\text{ は }a\text{ で終わる}\}$（12語）を覆う問題を別に解いた。$A$ の語だけを使う場合は最小コスト60（4語）で、$2^{12}$ の全数検査で確認。$r$ 語を補助に許す場合も、4096通りの $A$ 部分集合と貪欲補助語の探索で60を下回らなかった（出力は付録 A.6）。これは**計算による観察**であり、任意の補助語に対する厳密な下界ではない（したがって表の下界は希少型の22のまま）。

#### $n=4$（上界は計算、下界は希少型）

$|L_4|=1806$、$\|L_4\|_+=49724$。full $B$ の被覆判定は遅いので、$n=4$ の上界は maxgap=0 の部分作用素で検証した（full $B$ の上界として有効）。

| 型付け | 下界（希少型） | 上界（計算） | 備考 |
|---|---:|---:|---|
| $s_{00}$ | 10 | 62 | 証拠集合（5語）。maxgap=0 で検証（full の上界として有効） |
| $s_{01}$ | 32 | 210 | 証拠集合220から貪欲に除去。maxgap=0 |
| $s_{10}$ | 26 | 158 | 証拠集合212から貪欲に除去。maxgap=0 |
| $s_{11}$ | 48 | 336 | 証拠集合422から貪欲に除去。maxgap=0（除去は時間予算で途中停止） |

$s_{01}$ の上界210の標本:
```
ccccarrrr, cclcarcarrr, cclcarlaarr, ccllaacarrr, ccllaalaarr,
clccarrccarrr, clccarrlcarlaar, cllcarlaaccarrr, lcccarrrcccarrr,
cllcarlaalcarlaar, lcccarrrlccarrlcarlaa, llccarrlcarlaacccarrr,
llccarrlcarlaalccarrlcarlaa
```
$s_{10}$ の上界158の標本:
```
ccccarrrr, ccclaarrr, cclcarcarrr, ccllaacarrr, ccllaalaarr,
clccarrccarrr, clccarrlcarcarr, cllcarcarccarrr, lcccarrrcccarrr,
lcccarrrlccarrccarr, llccarrccarrcccarrr
```
$s_{11}$ の上界336の標本（maxgap=0、20語）:
```
ccccarrrr, ccclaarrr, cclcarcarrr, cclcarlaarr, ccllaacarrr,
ccllaalaarr, clccarrccarrr, clccarrlcarcarr, clccarrlcarlaar,
cllcarcarccarrr, cllcarlaaccarrr, lcccarrrcccarrr,
cllcarlaalcarcarr, cllcarlaalcarlaar, lcccarrrlccarrccarr,
llccarrccarrcccarrr, lcccarrrlccarrlcarlaa,
llccarrlcarlaacccarrr, llccarrlcarlaalccarrccarr,
llccarrlcarlaalccarrlcarlaa
```

### 3.3 (c) 証拠集合 $\mathrm{Wit}$ の長さ

原稿の証拠集合（各型付き非終端に最短代表と文脈 $c^{n-i}\cdot r^{n-i}$、各型付き規則にその合成）を厳密に構成し、重複を除いた長さを計算した。

| $n$ | $s_{00}$ | $s_{01}$ | $s_{10}$ | $s_{11}$ |
|---:|---:|---:|---:|---:|
| 1 | 8 (2語) | 8 (2) | 8 (2) | 8 (2) |
| 2 | 20 (3) | 44 (6) | 44 (6) | 44 (6) |
| 3 | 38 (4) | 112 (10) | 112 (10) | 188 (15) |
| 4 | 62 (5) | 220 (14) | 212 (14) | 422 (24) |
| 5 | 92 (6) | 376 (18) | 344 (18) | 758 (33) |

閉形式（$n\ge1$、$n=1$ の $s_{11}$ のみ別）:
$$
\begin{aligned}
W_{00}(n)&=3n^2+3n+2,\\
W_{01}(n)&=\tfrac43n^3+8n^2+\tfrac83n-4,\\
W_{10}(n)&=16n^2-12n+4,\\
W_{11}(n)&=2n^3+27n^2-29n-22\quad(n\ge2),\qquad W_{11}(1)=8.
\end{aligned}
$$
これらは型長漸化式から得られる和の閉形式で、スクリプトで $n\le30$ を確認した（$W_{01},W_{10},W_{11}$ の閉形式は計算による同定。漸近次数 $\Theta(n^3),\Theta(n^2),\Theta(n^3)$ は §6.2 で証明する）。

### 3.4 (d) 償却の構成

「短い証拠＋稀な型ごとに長い語1本」が特徴標本になるかを試した。

- $\{S_n,R_n\}$（$S_n$ は最短の $a$ 終わり語、$R_n=c^na r^n$）だけでは、$n=3$ で $2/42$ 語しか導出しない（$n=2$ で $2/6$、$n=4$ で $2/1806$）。長い語1本は、それ自身と一部の因子しか Link の共通文脈を持たないため、償却が自動的には起きない。
- 「$r$ 型の短い証拠（長さ $\le 2n+3$ の証拠集合の語）＋ $S_n,R_n$」は $n=3$ で長さ70、被覆 $14/42$。$a$ 型の段ごとの文脈が不足する。
- 完全な証拠集合は $n=3$ で長さ112、被覆 $42/42$。短い証拠だけでは $a$ 型の長い代表（$S_i$、長さ $i^2$）を段ごとに用意するコストが残る。
- 一方、$s_{10}$ では証拠集合が $16n^2-12n+4$ で済み、$s_{01}$ の $\tfrac43n^3$ より次数が1つ低い。これは「どの型が長い代表を強制するか」の違いである。

---

## 4. T3: 増え方の判定

$\|G_n\|=\Theta(n)$、$\bar\theta_{G_n}=\Theta(n)$ なので、$n^2=\Theta(\|G\|\bar\theta)$、$n^3=\Theta(\|G\|^2\bar\theta)$ に対応する。

### 4.1 証拠集合の増え方（証明可能な上界）

$n=1,\ldots,30$ の $W(n)$ と比:

| $n$ | $\|G\|$ | $\theta$ | $\|G\|\theta$ | $\|G\|^2\theta$ | $W_{00}$ | $W_{01}$ | $W_{10}$ | $W_{11}$ |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2 | 31 | 7 | 217 | 6727 | 20 | 44 | 44 | 44 |
| 3 | 43 | 11 | 473 | 20339 | 38 | 112 | 112 | 188 |
| 4 | 55 | 15 | 825 | 45375 | 62 | 220 | 212 | 422 |
| 5 | 67 | 19 | 1273 | 85291 | 92 | 376 | 344 | 758 |
| 10 | 127 | 39 | 4953 | 629031 | 332 | 2156 | 1484 | 4388 |
| 20 | 247 | 79 | 19513 | 4819711 | 1262 | 13916 | 6164 | 26198 |
| 30 | 367 | 119 | 43673 | 16027991 | 2792 | 43276 | 14044 | 77408 |

比 $W/n^2$ と $W/n^3$:

| $n$ | $s_{00}$: $W/n^2$ | $s_{01}$: $W/n^2$ | $s_{01}$: $W/n^3$ | $s_{10}$: $W/n^2$ | $s_{10}$: $W/n^3$ | $s_{11}$: $W/n^3$ |
|---:|---:|---:|---:|---:|---:|---:|
| 3 | 4.22 | 12.44 | 4.15 | 12.44 | 4.15 | 6.96 |
| 4 | 3.88 | 13.75 | 3.44 | 13.25 | 3.31 | 6.59 |
| 5 | 3.68 | 15.04 | 3.01 | 13.76 | 2.75 | 6.06 |
| 10 | 3.32 | 21.56 | 2.16 | 14.84 | 1.48 | 4.39 |
| 20 | 3.15 | 34.79 | 1.74 | 15.41 | 0.77 | 3.27 |
| 30 | 3.10 | 48.08 | 1.60 | 15.60 | 0.52 | 2.87 |

- $s_{00}$: $W/n^2\to3$（$3n^2$）。
- $s_{10}$: $W/n^2\to16$（$16n^2$）。
- $s_{01}$: $W/n^3\to4/3$（$\tfrac43n^3$）。
- $s_{11}$: $W/n^3$ は $n=30$ で2.87、まだ減少中。$\Theta(n^3)$ の範囲（$2n^3$ が主項）。

### 4.2 最短標本の上界の比（計算）

$n=3$ と $n=4$ の最良上界の比:

| 型付け | $n=3$ | $n=4$ | 比 | $n^2$ の比 $(4/3)^2$ | $n^3$ の比 $(4/3)^3$ |
|---|---:|---:|---:|---:|---:|
| $s_{00}$ | 38 | 62 | 1.63 | 1.78 | 2.37 |
| $s_{01}$ | 94 | 210 | 2.23 | 1.78 | 2.37 |
| $s_{10}$ | 86 | 158 | 1.84 | 1.78 | 2.37 |
| $s_{11}$ | 144 | 336* | 2.33* | 1.78 | 2.37 |

（* $s_{11}$ の $n=4$ は maxgap=0 での貪欲除去の途中値336。除去は時間予算で停止しており、同じ最適化水準ではないので参考値。）

**観察（証明ではない）.** $s_{10}$ の比1.84は $n^2$ の1.78に近く、$s_{01}$ の比2.23は $n^3$ の2.37に近い。$n$ が小さいので、これは「観察」であって証明ではない。しかし、証拠集合の閉形式が $s_{10}$ で $n^2$、$s_{01}$ で $n^3$ であることは証明できるので、「標準的な構成」の次数が型付けで変わることは確実である。

---

## 5. T4: 償却が効かない族の設計

### 5.1 非交差アルファベットの2本の背骨

$F_n$ の2つのコピーを、文字を互いに素な集合に写して作る：
- コピー A: $a\mapsto A,\ l\mapsto L,\ c\mapsto C,\ r\mapsto R$。
- コピー B: $a\mapsto x,\ l\mapsto y,\ c\mapsto z,\ r\mapsto w$。

開始記号 $S\to S_A\mid S_B$、型付けは末尾1文字。2つのコピーの型は完全に異なり、因子も共通でない。したがって $B(F)$ の導出はコピーを跨げず、
$$\mathrm{cs}(L_A\uplus L_B)=\mathrm{cs}(L_A)+\mathrm{cs}(L_B)=2\,\mathrm{cs}(F_n).$$
クラス所属: 各コピーは $F_n$ なので Clark–Eyraud 代入可能。非交差和も代入可能である（同じ文脈は同一コピー内にしか存在しない）。文法量: 新しい開始記号1個と各コピーの文法、開始規則2本（各サイズ3）で
$$\|G\|=1+2(12n+7)+6=24n+21,\qquad \theta=4n-1.$$
計算では $n=1$ で16、$n=2$ で88、$n=3$ で188（上界）を確認した。$n=3$ は maxgap=0 で84語全部を被覆。これは「共有できない長い代表」を2本必要とする族で、コストが加法的になることを示す。

### 5.2 色付き $F_n$（段ごとに別アルファベット）

段 $i$ が自分のアルファベットを持ち、開始記号が各段の $E_{i,i}$ を生成する族。段同士は非交差なので
$$\mathrm{cs}=\sum_{i=1}^n\mathrm{cs}(F_i).$$
クラス所属は各段の代入可能性と非交差性から従う。文法量は、各段の開始記号 $S_i$ とその規則（サイズ4）を除き、共有開始 $S$（1個）と $n$ 本の開始規則（各サイズ3）を加えて
$$\|G\|=\sum_{i=1}^n(12i+7)-4n+1+3n=6n^2+12n+1,\qquad \theta=4n-1.$$
$n=1,2,3$ で $\mathrm{cs}$ は $8,52,146$（$F_3$ は上界94を使用）。$\|G\|=\Theta(n^2)$、$\theta=\Theta(n)$ なので、もし $\mathrm{cs}(F_i)=\Theta(i^3)$ なら $\mathrm{cs}=\Theta(n^3)=\Theta(\|G\|\theta)$ であり、$\Theta(\|G\|^2\theta)$ にはならない。つまり、段ごとにアルファベットを複製すると、文法サイズが $n^2$ になり、二次の因子は「文法の共有」に由来することがわかる（この段落の「なら」は観察・予想であり、$\mathrm{cs}(F_i)$ の厳密な次数は §7 の未解決問題である）。

### 5.3 長い語1本では償却しない

$\{S_n,R_n\}$ だけでは $n=2,3,4$ でそれぞれ $2/6,2/42,2/1806$ 語しか導出しない。長い語は、それ自身を Start として使えるが、他の段の非終端を Link で置き換えるには、同じ文脈に置かれた語（証拠）が必要である。$F_n$ では段ごとに文脈 $c^{n-i}\cdot r^{n-i}$ が異なるため、1本の語で全段の文脈を同時に供給するのは難しい。これが $s_{01}$ の $n^3$ 型の証拠集合が生じる構造的理由である。

### 5.4 設計の結論

- 非交差化（2本の背骨、色付き段）で「共有できない長い代表」を強制できる。コストは加法的になり、$\mathrm{cs}=2\,\mathrm{cs}(F_n)$ や $\sum_i\mathrm{cs}(F_i)$ になる。
- しかし、非交差化すると文法サイズも段の数だけ増える。$\|G\|\sim n$ を保ったまま $\mathrm{cs}\sim n^3$ を得るには、$F_n$ のように段が文法を共有し、かつ文脈が段ごとに異なる構造が必要である。$F_n$ の $s_{01}$ はその候補になっている。
- 逆に、$s_{10}$ のように長い代表を強制しない型付けでは、同じ $F_n$ でも標準標本が $n^2$ で済む。したがって「窓の型付け」を一括りにした単一の答えはない。

---

## 6. T5: 証明できること

### 6.1 文法量（補題 1、補題 2）

§3.1 に証明した。

### 6.2 $\mathrm{cs}$ の上界と下界

**上界（証明）.** 原稿 Theorem data-from-typed-thickness の証拠集合を、$G_n$ の最短代表と文脈 $\chi(E_i)=c^{n-i}\cdot r^{n-i}$ で構成する。型付き非終端・規則の数は $O(n)$、各証拠語の長さは $O(\bar\theta+t_{\mathrm{typ}})$。$t_{\mathrm{typ}}$ は型ごとの最短代表の最大で、補題 2 から
- $s_{00}$: $t_{\mathrm{typ}}=2n+1$、$W=O(n^2)$。
- $s_{01}$: $t_{\mathrm{typ}}=n^2+n+1$、$W=O(n^3)$。
- $s_{10}$: $t_{\mathrm{typ}}=4n-1$、$W=O(n^2)$。
- $s_{11}$: $t_{\mathrm{typ}}=n^2+n+1$、$W=O(n^3)$。

閉形式は §3.3 のとおり（計算で $n\le30$ を確認）。漸近次数は、$s_{01}$ では $a$ 型非終端の証拠 $c^{n-i}S_ir^{n-i}$ が $i=1,\ldots,n$ で長さ $\ge i^2$ なので $\Omega(n^3)$、$s_{10}$ ではすべての代表が $O(n)$ なので $O(n^2)$。

**下界（証明）.** 原稿 prop:rare-type をそのまま適用する。型 $m$ の最短語長 $\mu_m$ に対し
$$\mathrm{cs}\ge\sum_{m\in M_L}(\mu_m+1).$$
補題 2 の値を代入すると
- $s_{00}$: $2n+2$。
- $s_{01}$: $(n^2+n+1+1)+(2n+1+1)=n^2+3n+4$。
- $s_{10}$: $(4n-1+1)+(2n+1+1)=6n+2$。
- $s_{11}$: $(n^2+n+1+1)+(4n-1+1)+(2n+1+1)=n^2+7n+4$（$n\ge2$）。

これは $B_{1,s}^{\le2}$ だけでなく、クラス全体で特徴標本を持つ任意の集合駆動作用素に成り立つ（原稿の命題の主張）。

**系.** $s_{01}$ では $n^2+3n+4\le\mathrm{cs}\le\tfrac43n^3+O(n^2)$。$s_{10}$ では $6n+2\le\mathrm{cs}\le16n^2+O(n)$。$s_{00}$ では $2n+2\le\mathrm{cs}\le3n^2+3n+2$。

### 6.3 $F_n$ の Clark–Eyraud 代入可能性

**$n\le4$ の全数検査（計算）.** 原稿の `check_open_doubling_family.py` と同じ判定を実行し、$n\le4$ で違反なしを確認した（出力は付録 A.5）。$n=4$ は1806語、最長31。

**一般 $n$ の証明の試み（未完成）.** 原稿の括弧付き倍増族の付録 C の決定的パーサを $F_n$ に適合させる。スタック記号を $E_0,\ldots,E_n$ と $c$ 枝の閉じ記号 $R_1,\ldots,R_n$ とし、遷移を
$$E_0Z\xrightarrow{a}Z,\quad E_iZ\xrightarrow{l}E_{i-1}E_{i-1}Z,\quad E_iZ\xrightarrow{c}E_{i-1}R_iZ,\quad R_iZ\xrightarrow{r}Z$$
とする。認識補題（$E_iZ\xrightarrow{w}Z\iff w\in L(E_i)$）と交換補題（同じ $L(E_i)$ の語は同値）は括弧付き族と同様に示せる。しかし、括弧付き族の (P1)（各文字がスタック上の部分単射）は $F_n$ では**失敗する**。具体的には、$n=3$ で
- 語 $lllaacarllaalaa$ のプレフィックス $lllaaca$ はスタック $R_1E_2$ に至り、
- 語 $lclaarlcarlaa$ のプレフィックス $lclaa$ はスタック $R_2E_2$ に至る。

どちらも次の文字 $r$ で同じスタック $E_2$ に移る（$r$ は $R_1$ も $R_2$ も同じようにポップする）。したがって「同じ文脈 $v$ で受理される2つのスタックは一致する」という最後のステップが使えない。この非単射性は、$c$ 枝の閉じ記号がレベルの違う $R_i$ を区別しないことに由来する。

したがって、現時点では
- $n\le4$: 計算で代入可能（証明済み、有限全数検査）、
- 全ての $n$: **未解決**（パーサの単射性の回復が必要）
である。非単射性を回復するには、スタックに「保留中の $c$ 枝のレベルの集合」を持たせる、あるいは右から読む双対パーサを使う、といった修正が考えられるが、本作業では完成しなかった。これは原稿の「$n\le4$ で全数検査済み」という記述を、一般 $n$ の証明へ拡張する際の具体的な障害である。

---

## 7. 結論

1. **型付け依存である。** $F_n$ の標準的な証拠集合の長さは、$s_{00}$ で $3n^2+3n+2$、$s_{10}$ で $16n^2-12n+4$、$s_{01}$ で $\tfrac43n^3+8n^2+\tfrac83n-4$、$s_{11}$ で $2n^3+27n^2-29n-22$ である（$n\le30$ で確認、漸近次数は証明）。$s_{00},s_{10}$ は $\Theta(\|G\|\bar\theta)$、$s_{01},s_{11}$ は $\Theta(\|G\|^2\bar\theta)$ の次数を持つ。
2. **最短標本の次数は未解決。** $n=1,2$ は全数検査で厳密、$n=3$ は $22\le\mathrm{cs}(s_{01})\le94$ などの上下界、$n=4$ は上界のみ。$n=3\to4$ の上界の比は $s_{10}$ で1.84（$n^2$ の1.78に近い）、$s_{01}$ で2.23（$n^3$ の2.37に近い）。これは**観察**であり、証明ではない。
3. **償却は自動ではない。** $\{S_n,R_n\}$ は2語しか導出しない。段ごとの文脈が異なるため、長い語1本で全段を賄うには、段ごとの文脈証拠が必要である。非交差アルファベットで共有を断つとコストは加法的になるが、文法サイズも増える。
4. **一般 $n$ の Clark–Eyraud 代入可能性は未証明。** $n\le4$ は全数検査。パーサの単射性が障害で、$R_1E_2$ と $R_2E_2$ が同じ $r$ 遷移を持つ反例がある。

**主問いへの回答（現時点）.** 「窓の型付け」に対して単一の答えはない。先頭文字 $s_{10}$ と自明型 $s_{00}$ は $\Theta(\|G\|\bar\theta)$ 側、末尾文字 $s_{01}$ と $s_{11}$ は $\Theta(\|G\|^2\bar\theta)$ 側の標準標本を持つ。最短標本が同じ次数かは、$n\le4$ の計算では $s_{10}$ が $n^2$ 寄り、$s_{01}$ が $n^3$ 寄りに見えるが、厳密な証明には $n$ に一様な下界が必要である。

---

## 付録 A. 実行コマンドと出力全文

### A.0 環境

```
> py -3 --version
Python 3.12.10
```
（実行環境: Windows、`py -3` は Python 3.12.10。標準ライブラリのみ。）

### A.1 `py -3 check_window_gap_search.py fast`

実行時間: 約81秒（出力末尾に `fast sections done in 81.1s`）。同じスクリプトの再実行では52秒だった（個々の内訳の秒数は環境依存）。

```text
=== T1: validation on known examples ===
[T1-a] linear-factor family (trivial typing);
       expected: every word is essential, hence only F=L works
  q=1 k=1 |L|=2  full_missing=0  essential=2  PASS
  q=2 k=1 |L|=3  full_missing=0  essential=3  PASS
  q=2 k=2 |L|=3  full_missing=0  essential=3  PASS
  q=3 k=1 |L|=4  full_missing=0  essential=4  PASS
  q=3 k=2 |L|=4  full_missing=0  essential=4  PASS
[T1-b] bracketed doubling family;
       expected: W_n is the unique type-1 word and is necessary
  n=1 |L|=2  type1=['paaq']  W_n=paaq  unique=True  derives_without=False  PASS
  n=2 |L|=6  type1=['ppaaqpaaqq']  W_n=ppaaqpaaqq  unique=True  derives_without=False  PASS
  n=3 |L|=42  type1=['pppaaqpaaqqppaaqpaaqqq']  W_n=pppaaqpaaqqppaaqpaaqqq  unique=True  derives_without=False  PASS

=== T2(a): ||G_n||, theta_G, mu_m ===
n  ||G_n||  theta_G  |L_n|  total||L_n||_+  mu(triv)
1      19        3       2              8  [3]
     s01: [('(|a)', 3), ('(|r)', 3)]
     s10: [('(c|)', 3), ('(l|)', 3)]
     s11: [('(c|r)', 3), ('(l|a)', 3)]
2      31        7       6             44  [5]
     s01: [('(|r)', 5), ('(|a)', 7)]
     s10: [('(c|)', 5), ('(l|)', 7)]
     s11: [('(c|r)', 5), ('(l|a)', 7), ('(l|r)', 7)]
3      43       11      42            584  [7]
     s01: [('(|r)', 7), ('(|a)', 13)]
     s10: [('(c|)', 7), ('(l|)', 11)]
     s11: [('(c|r)', 7), ('(l|r)', 11), ('(l|a)', 13)]
4      55       15    1806          49724  [9]
     s01: [('(|r)', 9), ('(|a)', 21)]
     s10: [('(c|)', 9), ('(l|)', 15)]
     s11: [('(c|r)', 9), ('(l|r)', 15), ('(l|a)', 21)]
5      67       19  3263442      179656424  [11]
     s01: [('(|r)', 11), ('(|a)', 31)]
     s10: [('(c|)', 11), ('(l|)', 19)]
     s11: [('(c|r)', 11), ('(l|r)', 19), ('(l|a)', 31)]

=== T2(b): exact cs for n=1,2 (all subsets) ===
n=1 |L|=2 total||L||_+=8
  s00: cs=8  F=['car', 'laa']  (0.00s)
  s01: cs=8  F=['car', 'laa']  (0.00s)
  s10: cs=8  F=['car', 'laa']  (0.00s)
  s11: cs=8  F=['car', 'laa']  (0.00s)
n=2 |L|=6 total||L||_+=44
  s00: cs=20  F=['ccarr', 'claar', 'lcarcar']  (0.18s)
  s01: cs=44  F=['ccarr', 'claar', 'lcarcar', 'lcarlaa', 'llaacar', 'llaalaa']  (0.58s)
  s10: cs=36  F=['ccarr', 'claar', 'lcarcar', 'lcarlaa', 'llaacar']  (0.54s)
  s11: cs=44  F=['ccarr', 'claar', 'lcarcar', 'lcarlaa', 'llaacar', 'llaalaa']  (0.62s)

=== T2(c): length of the manuscript witness set Wit ===
n  typing  |Wit|  ||Wit||_+  maxlen
1  s00      2          8       3
1  s01      2          8       3
1  s10      2          8       3
1  s11      2          8       3
2  s00      3         20       7
2  s01      6         44       7
2  s10      6         44       7
2  s11      6         44       7
3  s00      4         38      11
3  s01     10        112      15
3  s10     10        112      15
3  s11     15        188      15
4  s00      5         62      15
4  s01     14        220      27
4  s10     14        212      23
4  s11     24        422      27
5  s00      6         92      19
5  s01     18        376      43
5  s10     18        344      31
5  s11     33        758      43

=== T2(d): amortised samples ===
  n=1 {S_n,R_n}: |F|=2 len=8 coverage=2/2
  n=1 short-r-evidence+{S_n,R_n}: |F|=2 len=8 coverage=2/2
  n=1 full witness: |W|=2 len=8 coverage=2/2
  n=2 {S_n,R_n}: |F|=2 len=14 coverage=2/6
  n=2 short-r-evidence+{S_n,R_n}: |F|=6 len=44 coverage=6/6
  n=2 full witness: |W|=6 len=44 coverage=6/6
  n=3 {S_n,R_n}: |F|=2 len=22 coverage=2/42
  n=3 short-r-evidence+{S_n,R_n}: |F|=7 len=70 coverage=14/42
  n=3 full witness: |W|=10 len=112 coverage=42/42

=== T3: growth of the witness construction and of the bounds ===
n  ||G||  theta  ||G||*theta  ||G||^2*theta  W(triv) W(s01) W(s10) W(s11)  R(s01) R(s10) R(s11)
 1    19     3         57         1083       8      8      8      8  8 8 8
 2    31     7        217         6727      20     44     44     44  14 14 22
 3    43    11        473        20339      38    112    112    188  22 20 34
 4    55    15        825        45375      62    220    212    422  32 26 48
 5    67    19       1273        85291      92    376    344    758  44 32 64
 6    79    23       1817       143543     128    588    508   1208  58 38 82
 7    91    27       2457       223587     170    864    704   1784  74 44 102
 8   103    31       3193       328879     218   1212    932   2498  92 50 124
 9   115    35       4025       462875     272   1640   1192   3362  112 56 148
10   127    39       4953       629031     332   2156   1484   4388  134 62 174
15   187    59      11033      2063171     722   6336   3424  12368  274 92 334
20   247    79      19513      4819711    1262  13916   6164  26198  464 122 544
30   367   119      43673     16027991    2792  43276  14044  77408  994 182 1114

Ratios W/n^2 and W/n^3 for n=1..30:
n   s00: W/n2  s01: W/n2 W/n3  s10: W/n2 W/n3  s11: W/n2 W/n3
 1    8.00      8.00   8.00      8.00   8.00      8.00   8.00
 2    5.00     11.00   5.50     11.00   5.50     11.00   5.50
 3    4.22     12.44   4.15     12.44   4.15     20.89   6.96
 4    3.88     13.75   3.44     13.25   3.31     26.38   6.59
 5    3.68     15.04   3.01     13.76   2.75     30.32   6.06
10    3.32     21.56   2.16     14.84   1.48     43.88   4.39
20    3.15     34.79   1.74     15.41   0.77     65.50   3.27
30    3.10     48.08   1.60     15.60   0.52     86.01   2.87

=== T4: families designed against amortisation ===
[T4-A] two-spine family: disjoint-alphabet copies of F_n, s_{0,1}
       predicted cs = 2 * cs(F_n); verified by a covering sample
  n=1 |L|=4 upper sample |F|=4 len=16 coverage(full)=4/4
       (disjointness: no factor of one copy is a factor of the other)
  n=2 |L|=12 upper sample |F|=12 len=88 coverage(full)=12/12
       (disjointness: no factor of one copy is a factor of the other)
  n=3 |L|=84 upper sample |F|=16 len=188 coverage(maxgap=0)=84/84
       (disjointness: no factor of one copy is a factor of the other)
[T4-B] coloured F_n: level i has its own alphabet; cs is additive
  n=1 |L|=2  level sizes=[2]  additive cs=sum_i cs(F_i)=8
       (cs(F_1)=8 and cs(F_2)=44 are exact; cs(F_3)<=94 is the
        upper bound from the search3 mode; additivity is by
        disjoint alphabets, so the union needs all of them)
  n=2 |L|=8  level sizes=[2, 6]  additive cs=sum_i cs(F_i)=52
       (cs(F_1)=8 and cs(F_2)=44 are exact; cs(F_3)<=94 is the
        upper bound from the search3 mode; additivity is by
        disjoint alphabets, so the union needs all of them)
  n=3 |L|=50  level sizes=[2, 6, 42]  additive cs=sum_i cs(F_i)=146
       (cs(F_1)=8 and cs(F_2)=44 are exact; cs(F_3)<=94 is the
        upper bound from the search3 mode; additivity is by
        disjoint alphabets, so the union needs all of them)
[T4-C] one long a-word + one long r-word alone:
  n=2 |{S_n,R_n}|=2 len=14 coverage(full)=2/6
  n=3 |{S_n,R_n}|=2 len=22 coverage(full)=2/42
  n=4 |{S_n,R_n}|=2 len=32 coverage(maxgap=0)=2/1806

fast sections done in 81.1s
```

### A.2 `py -3 check_window_gap_search.py search3 240`

実行時間: 約10分（$s_{00}$ 20秒、$s_{01}$ 153秒、$s_{10}$ 97秒、$s_{11}$ 304秒、証拠集合の full 検証を含む）。

```text
=== T2(b): n=3, exact is open; upper and lower bounds ===
n=3 |L|=42 total||L||_+=584
  s00:
    rare-type lower bound = 8
    witness upper bound: |Wit|=4 len=38
    witness words: ['cccarrr', 'cclaarr', 'clcarcarr', 'lccarrccarr']
    witness coverage under full B: missing=0 (1.8s)
    local-search upper bound (maxgap=0 search): len=38 F=['cccarrr', 'cclaarr', 'clcarcarr', 'lccarrccarr'] (20.4s)
    full verification: missing=0
  s01:
    rare-type lower bound = 22
    witness upper bound: |Wit|=10 len=112
    witness words: ['cccarrr', 'cclaarr', 'clcarcarr', 'clcarlaar', 'cllaacarr', 'cllaalaar', 'lccarrccarr', 'lccarrlcarlaa', 'llcarlaaccarr', 'llcarlaalcarlaa']
    witness coverage under full B: missing=0 (2.3s)
    [s01] improve 104  rm2add1 lccarrlcarlaa clcarlaar -> llcarcarlcarlaa  (25.2s)
    [s01] improve 94  rm2add1 llcarlaaccarr cllaalaar -> llcarlaaclaar  (62.6s)
    local-search upper bound (maxgap=0 search): len=94 F=['cccarrr', 'cclaarr', 'clcarcarr', 'cllaacarr', 'lccarrccarr', 'llcarlaalcarlaa', 'llcarcarlcarlaa', 'llcarlaaclaar'] (153.4s)
    full verification: missing=0
  s10:
    rare-type lower bound = 20
    witness upper bound: |Wit|=10 len=112
    witness words: ['cccarrr', 'cclaarr', 'clcarcarr', 'clcarlaar', 'cllaacarr', 'cllaalaar', 'lccarrccarr', 'lccarrlcarcar', 'llcarcarccarr', 'llcarcarlcarcar']
    witness coverage under full B: missing=0 (2.4s)
    [s10] improve 108  replace llcarcarlcarcar -> lccarrclaar  (0.1s)
    [s10] improve 96  rm2add1 lccarrlcarcar lccarrclaar -> lccarrlcarlaa  (4.6s)
    [s10] improve 86  rm2add1 lccarrlcarlaa clcarlaar -> lccarrlcarcar  (11.5s)
    local-search upper bound (maxgap=0 search): len=86 F=['cccarrr', 'cclaarr', 'clcarcarr', 'cllaacarr', 'cllaalaar', 'lccarrccarr', 'llcarcarccarr', 'lccarrlcarcar'] (97.0s)
    full verification: missing=0
  s11:
    rare-type lower bound = 34
    witness upper bound: |Wit|=15 len=188
    witness words: ['cccarrr', 'cclaarr', 'clcarcarr', 'clcarlaar', 'cllaacarr', 'cllaalaar', 'lccarrccarr', 'lccarrlcarcar', 'lccarrlcarlaa', 'llcarcarccarr', 'llcarlaaccarr', 'llcarcarlcarcar', 'llcarcarlcarlaa', 'llcarlaalcarcar', 'llcarlaalcarlaa']
    witness coverage under full B: missing=0 (3.2s)
    [s11] improve 184  replace llcarcarlcarcar -> lccarrclaar  (0.1s)
    [s11] improve 180  replace llcarcarlcarlaa -> lclaarccarr  (0.2s)
    [s11] improve 178  replace llcarlaalcarcar -> lccarrllaacar  (0.4s)
    [s11] improve 166  rm2add1 llcarcarccarr lccarrccarr -> llcarcarclaar  (44.0s)
    [s11] kick 160 (126.8s)
    [s11] improve 156  replace lccarrllaalaa -> cllaalaar  (128.8s)
    [s11] improve 154  replace lclaarccarr -> clcarcarr  (131.0s)
    [s11] kick 150 (223.5s)
    [s11] improve 144  replace llcarcarccarr -> cccarrr  (225.6s)
    local-search upper bound (maxgap=0 search): len=144 F=['cclaarr', 'clcarlaar', 'lccarrlcarcar', 'lccarrlcarlaa', 'llcarlaaccarr', 'llcarlaalcarlaa', 'lccarrclaar', 'lccarrllaacar', 'llcarcarclaar', 'cllaalaar', 'clcarcarr', 'cccarrr'] (303.6s)
    full verification: missing=0
```

### A.3 `py -3 check_window_gap_search.py n4 420`

実行時間: 約20分（$s_{11}$ の1パスが420秒を超えたため、336 で手動停止）。

```text
=== T2(b): n=4, upper bounds (restricted operator maxgap=0) ===
n=4 |L|=1806 total||L||_+=49724
  s00: rare lower=10  witness |W|=5 len=62
    witness coverage (maxgap=0): 1806/1806 (6.2s)
    pruned upper bound: |F|=5 len=62 F=['ccccarrrr', 'ccclaarrr', 'cclcarcarrr', 'clccarrccarrr', 'lcccarrrcccarrr']
  s01: rare lower=32  witness |W|=14 len=220
    witness coverage (maxgap=0): 1806/1806 (11.2s)
    removed ccclaarrr              new len=210 (138.1s)
    pruned upper bound: |F|=13 len=210 F=['ccccarrrr', 'cclcarcarrr', 'cclcarlaarr', 'ccllaacarrr', 'ccllaalaarr', 'clccarrccarrr', 'clccarrlcarlaar', 'cllcarlaaccarrr', 'lcccarrrcccarrr', 'cllcarlaalcarlaar', 'lcccarrrlccarrlcarlaa', 'llccarrlcarlaacccarrr', 'llccarrlcarlaalccarrlcarlaa']
  s10: rare lower=26  witness |W|=14 len=212
    witness coverage (maxgap=0): 1806/1806 (10.4s)
    removed llccarrccarrlccarrccarr new len=188 (9.6s)
    removed cllcarcarlcarcarr      new len=170 (43.2s)
    removed cclcarlaarr            new len=158 (114.2s)
    pruned upper bound: |F|=11 len=158 F=['ccccarrrr', 'ccclaarrr', 'cclcarcarrr', 'ccllaacarrr', 'ccllaalaarr', 'clccarrccarrr', 'clccarrlcarcarr', 'cllcarcarccarrr', 'lcccarrrcccarrr', 'lcccarrrlccarrccarr', 'llccarrccarrcccarrr']
  s11: rare lower=48  witness |W|=24 len=422
    witness coverage (maxgap=0): 1806/1806 (11.2s)
    removed llccarrccarrlccarrlcarlaa new len=396 (23.0s)
    removed llccarrccarrlccarrccarr new len=372 (58.5s)
    removed cllcarcarlcarcarr      new len=354 (136.0s)
    removed cllcarcarlcarlaar      new len=336 (210.0s)
```

（$s_{11}$ の貪欲除去は1パスが時間予算420秒を超えたため、336 の時点で停止した。336 の標本のリストは A.3.1 の追試で得た。）

### A.3.1 `py -3 check_window_gap_search.py n4s11`

$s_{11}$ の $n=4$ 標本を短時間で再現するための部分除去。maxgap=0。

```text
=== T2(b): n=4, s11 partial pruning (maxgap=0) ===
start: |W|=24 len=422
  keep llccarrlcarlaalccarrlcarlaa (coverage 1758/1806, 10.3s)
  removed llccarrccarrlccarrlcarlaa new len=396 (10.0s)
  keep llccarrlcarlaalccarrccarr  (coverage 1662/1806, 9.7s)
  removed llccarrccarrlccarrccarr new len=372 (9.4s)
  keep lcccarrrlccarrlcarlaa      (coverage 1686/1806, 9.5s)
  keep llccarrlcarlaacccarrr      (coverage 1734/1806, 9.5s)
  keep lcccarrrlccarrccarr        (coverage 1446/1806, 9.9s)
  keep llccarrccarrcccarrr        (coverage 938/1806, 9.2s)
  removed cllcarcarlcarcarr        new len=354 (9.3s)
  removed cllcarcarlcarlaar        new len=336 (8.8s)
partial-pruned: |F|=20 len=336
F=['ccccarrrr', 'ccclaarrr', 'cclcarcarrr', 'cclcarlaarr', 'ccllaacarrr', 'ccllaalaarr', 'clccarrccarrr', 'clccarrlcarcarr', 'clccarrlcarlaar', 'cllcarcarccarrr', 'cllcarlaaccarrr', 'lcccarrrcccarrr', 'cllcarlaalcarcarr', 'cllcarlaalcarlaar', 'lcccarrrlccarrccarr', 'llccarrccarrcccarrr', 'lcccarrrlccarrlcarlaa', 'llccarrlcarlaacccarrr', 'llccarrlcarlaalccarrccarr', 'llccarrlcarlaalccarrlcarlaa']
```

（除去の順序は長い語から。`keep` は「その語を除くと被覆が落ちる」ことを示す。この標本は maxgap=0 で 1806/1806 を被覆するので、full $B$ でも特徴標本である。）

### A.4 補助計算（$n=3$ の局所探索）

`search3` モードを240秒/型付けで実行した出力が A.2 である。$s_{01}=94$、$s_{10}=86$、$s_{11}=144$ を得た（full $B$ で検証済み）。時間予算を変えると上界は変わりうる。

### A.5 `py -3 check_open_doubling_family.py`（$F_n$ の代入可能性、$n\le4$）

```text
1 2 maxlen 3 CE-substitutable True None mu_a 3 n(n+1)+1= 3
2 6 maxlen 7 CE-substitutable True None mu_a 7 n(n+1)+1= 7
3 42 maxlen 15 CE-substitutable True None mu_a 13 n(n+1)+1= 13
4 1806 maxlen 31 CE-substitutable True None mu_a 21 n(n+1)+1= 21
```

（`True` は Clark–Eyraud 代入可能、`mu_a` は末尾 $a$ の最短語長。$n(n+1)+1$ と一致。）

### A.6 `py -3 check_window_gap_search.py subA`（$s_{01}$ の $A$-部分問題）

```text
=== T2(b) side computation: n=3, s01, A-subproblem ===
|A|=12 |R|=30
  new best 74 ['lccarrlcarlaa', 'lccarrllaalaa', 'lclaarlcarlaa', 'llcarcarlcarlaa', 'lllaacarlcarlaa'] (73.4s)
  new best 60 ['lccarrlcarlaa', 'lclaarlcarlaa', 'llcarlaalcarlaa', 'lllaalaalcarlaa'] (143.9s)
best A-cover found: 60 ['lccarrlcarlaa', 'lclaarlcarlaa', 'llcarlaalcarlaa', 'lllaalaalcarlaa'] (172.6s)
(heuristic; not a proof that no smaller cover exists)
```

---

## 付録 B. 実装の検算（内部）

- `BGrammar` の forward DP と、素朴な backward DP（規則を列挙してトップダウンに試す実装）を、$n\le3$ のランダムな $F$ で比較し、導出集合が一致することを確認した（開発時の比較スクリプト、12通り/型付け）。
- Link の推移閉包は union-find で計算。共通文脈 $(u,v)$ は $F$ の語の全因子出現から列挙。
- Comp の $q=1$ で $u_1=x$（自己ループ）は除いた。$q=2$ は子が2つとも非空。
- 型付けの短い語のタグ（$|w|<m_0$ なら $w$ 自身）を実装。

---

## 付録 C. 再現性の注意

- 局所探索は決定的なシード（`seed=7`）と時間予算に依存する。時間予算を変えると上界が変わりうる。
- $n=4$ の上界は maxgap=0 の部分作用素で検証している。full $B$ の上界としては有効だが、maxgap=0 でない導出を許す full $B$ では、より小さい標本が存在する可能性は否定しない（上界は「この標本が特徴標本である」ことの証明であって、最小性の証明ではない）。
- 証拠集合の閉形式は、型長 DP の辞書式タイブレーク（最短・辞書式最小）に依存する。タイブレークを変えると定数項が変わりうるが、漸近次数は変わらない。
- 数値はすべてスクリプトの出力からの転記である。転記ミスを避けるため、付録 A の全文と照合すること。

# 型別目標をもつ経路・加法量族の系統的探索

**日付：** 2026年10月31日
**対象：** $\Sigma$ 上の型付け $s:\Sigma^+\to U_1=\{1,\zeta\}$（$\zeta^2=\zeta$）、ファンアウト $\le2$、規則ランク $\le r$。言語は Astra 2026-10-31 §8.2 の設計仕様

\[
L=\{w\in R_{p,q}\cap\Sigma^+:\varphi(\Psi(w))=h_{s(w)}\},
\qquad
R_{p,q}=\text{一文字一辺の有向グラフの }p\to q\text{ 経路ラベル},
\]

に属するものとする。$\mu_1(L)=\min\{|w|:w\in L,\ w\text{ は純}\}$、$g=\|G\|$、$\theta=\bar\theta_G$。

**結論。** この型の族で $h_1\ne h_\zeta$ のものには反例が存在しない。より強く、**任意の** reduced good 表示 $G$ に対して
\[
\mu_1(L)\le(2r+1)|V|\,\bar\theta_G\le(2r+1)\|G\|\,\bar\theta_G
\]
が成り立つ（定理4.1、本報告で証明）。したがって $g_n\theta_n=n^{O(1)}$ なら $\mu_1(L_n)=n^{O(1)}$ であり、$\mu_1=n^{\omega(1)}$ は起こらない。この上界はグラフ・$\varphi$ の係数・$d$・文字数に依存しない。$h_1=h_\zeta$ の共通目標の場合は、三文字なら既知の Astra 2026-10-31 定理6.1（五次上界）が適用される。四文字以上で $h_1=h_\zeta$ の場合は本報告の範囲外である（§7）。一般の問題 M（すべての $(2,s)$-代入可能 MCFL）は未解決のままである。

計算部分は、基盤の既知例による検算、6族の増え方の表、近道規則の失敗の確認、および定理の構造補題のランダム文法による検査である。これらは観測であり、定理4.1の証明は計算に依存しない。

---

## 1. 結論の要約表

| 主張 | 判定 | 根拠の節 |
|---|---|---|
| 一般の問題 M（すべての $(2,s)$-代入可能なファンアウト $\le2$ の MCFL に対する $\mu_1$ の多項式上界） | 未解決 | §1, §7 |
| **Astra §8.2 の型（一文字一辺の経路＋型別目標、任意の $d$・任意の整数係数・任意の文字数）で $h_1\ne h_\zeta$ なら $\mu_1\le(2r+1)|V|\bar\theta_G$** | 証明済み | §4（定理4.1） |
| 同じ型で $g_n\theta_n=n^{O(1)}$ なら $\mu_1(L_n)=n^{O(1)}$ | 証明済み | §4.4（系4.6） |
| 同じ型で $h_1\ne h_\zeta$ なら反例の族は存在しない | 証明済み | §4（定理4.1より） |
| $h_1=h_\zeta$ の共通目標では $\mu_1\le16(r+1)^4\theta^4(\theta+3)+2$（三文字の場合） | 証明済み | 付録A（Astra 2026-10-31 定理6.1） |
| $h_1=h_\zeta$ では線形上界は成立しない（$G_{n,n}$ で $\mu_1/(g\theta)\sim2^n/n$） | 計算による観測（証明ではない） | §2.2 |
| $G_{m,n}$ の $\|G\|=6m+6n+9$、$\bar\theta=2^m+2^n-1$、$\mu_1=2^{m+n}$ の検算 | 計算による観測（証明ではない） | §2.2 |
| $L_{k,m}$ の $\|G\|=13km-4k-2$、$\bar\theta=k+m-1$、$\mu_1=km$ の検算 | 計算による観測（証明ではない） | §2.2 |
| 族A, A', B1, B2, C, D の増え方の表：すべての正しい表示で $\bar\theta=\Theta(\mu_1)$、比 $\mu_1/(g\theta)\to0$ | 計算による観測（証明ではない） | §3 |
| 近道規則を加えた文法は $n\ge2$ で $L(G)\ne L$、かつ一穴代入可能性が破れる | 計算による観測（証明ではない） | §3.4（Astra 2026-10-30 §8.3 の証明と一致） |
| $d=2$ の族Dの言語は文脈自由（したがってファンアウト2の MCFL） | 証明済み | §3.3 |
| 一般の $d\ge2$ の経路・加法量族の MCFL 性 | 未解決 | §7（$d=2$ の族D以外は未確認） |
| 有限言語の代入可能性判定器が $P_{N,2}$ を通し $K_2$ を arity 2 で落とすこと | 計算による観測（証明ではない） | §2.3 |
| 定理4.1の3つの構造補題（$|\Phi_B|\le2$、分裂な子は高々1個、定数な子は純のみ）のランダム文法275例での検査 | 計算による観測（証明ではない） | §2.4 |

---

## 2. 計算の基盤と検査

### 2.1 基盤

`check_s2_typewise_search.py`（Python 3.12、標準ライブラリのみ）は次の4部品を実装する。

**(a) 有限言語の $(2,s)$-代入可能性の判定器（arity 1, 2）。**
有限言語 $L$ の全受理語について、$0\le i<j\le|w|$ の一穴出現と $0\le i<j<k<\ell\le n$ の二穴出現をすべて列挙する。成分は非空、二穴の中央区切り $w[j:k]$ も $k>j$ により非空である。各出現の組 $\mathbf x$ と文脈 $E$、型ベクトル $s^{(d)}(\mathbf x)$ をキーにして、同じキーをもつ組の**全分布**（$L$ の全語における全出現から再計算）が一致するかを検査する。同じキーの最初の組との一致を見れば、推移性により群内の全対の一致と同値である。返された違反証人は `validate_certificate` で、文脈の非空性・型の一致・$E[\mathbf x],E[\mathbf y]\in L$・$F[\mathbf x]\in L$ と $F[\mathbf y]\notin L$ の食い違い（またはその逆）を文字列連結で直接再検査する。有限言語に対しては打切りなしの全数検査である。

**(b) 経路・繊維言語の最短純語。**
各文字がちょうど一本の辺をラベルする有向グラフ、$\varphi:\mathbb Z^\Sigma\to\mathbb Z^d$、$h_1,h_\zeta$ に対し、状態 $(v,x)$（頂点、$\varphi$ 値）上の幅優先探索で、純な文字だけを使い $(p,0)$ から $(q,h_1)$ への最短非空経路を求める。探索は深さごとに進み、初めて受理状態に到達した深さが $\mu_1$ である。状態の再訪はより浅い深さを優先するので最短性は保たれる。

**(c) ファンアウト1の reduced good CFG の解析。**
規則を（頭、テンプレート）で表し、テンプレートは端末ブロックと子の列である。次を計算する。
- 大きさ $\|G\|=|V|+\sum_R(1+\operatorname{rank}(R)+\sum_i|\alpha_i|)$（原稿 `def:standard-mcfg`）。
- 各非終端の最小生成長 $d_A$ と最小外側長 $o_A$ の不動点。規則の厚さ $\theta_G(R)=o_A+\text{直接端末数}+\sum_j d_{B_j}$、$\bar\theta_G=\max_R\theta_G(R)$。これは原稿 `lem:thickness-equivalence` の (i)–(iv) と整合する。
- 長さ $\ell$ 以下の生成語（長さごとの不動点。同じ長さのコピー規則も閉じる）。
- reduced（全非終端が到達可能かつ生成可能）と good（$\lambda$-free、非削除、非置換、非併合。ファンアウト1では各子の変数が一度ずつ順序を保って現れることがテンプレート表現から自動）。
- 純な生成物だけを使う最短生成長（型ごとの繊維の最短語の検算用）。

**(d) 言語の照合。**
長さ $\ell$ 以下の窓で $L(G)$ と $L$ を集合として比較し、不一致語を返す。これは有限窓の検査であり、全長の証明ではない。

### 2.2 既知例による検算

**論文の $G_{m,n}$（`prop:binary-u1-quadratic`）。** $C_0\to\mathtt a$、$C_j\to C_{j-1}C_{j-1}$、$A_0\to C_m\mid\mathtt b$、$A_i\to A_{i-1}A_{i-1}$、開始 $A_n$。$\mathtt a$ を中立、$\mathtt b$ を $\zeta$ とする。解析器の出力は次のとおりで、論文の数値と一致した。

| $(m,n)$ | $\|G\|$（期待 $6m+6n+9$） | $\bar\theta$（期待 $2^m+2^n-1$） | $\mu_1$（期待 $2^{m+n}$） | reduced / good |
|---|---:|---:|---:|---|
| (1,1) | 21 | 3 | 4 | 真 / 真 |
| (1,2) | 27 | 5 | 8 | 真 / 真 |
| (2,1) | 27 | 5 | 8 | 真 / 真 |
| (2,2) | 33 | 7 | 16 | 真 / 真 |
| (2,3) | 39 | 11 | 32 | 真 / 真 |
| (3,2) | 39 | 11 | 32 | 真 / 真 |

**Astra 2026-10-31 定理4.1 の重み切片 $L_{k,m}$。** $L_{k,m}=\{z\in\{a,b,c\}^+:|z|_a+|z|_b+k|z|_c=km\}$ を、一頂点・三ループのグラフ、$\varphi=(1,1,k)$、$h_1=h_\zeta=km$ の繊維として実現した。文法 $A_1\to a\mid b$、$A_j\to aA_{j-1}\mid bA_{j-1}$、$A_k\to c$、$A_j\to cA_{j-k}$（$j>k$）を使った。

| $(k,m)$ | $\|G\|$（期待 $13km-4k-2$） | $\bar\theta$（期待 $k+m-1$） | $\mu_1$（期待 $km$） | 長さ $km+1$ 以下で $L(G)=L$ |
|---|---:|---:|---:|---|
| (1,2) | 20 | 2 | 2 | 真 |
| (2,1) | 16 | 2 | 2 | 真 |
| (2,2) | 42 | 3 | 4 | 真 |
| (2,3) | 68 | 4 | 6 | 真 |
| (3,2) | 64 | 4 | 6 | 真 |

いずれも期待値と一致し、文法の言語は（$L$ が有限なので）全長で一致した。$\mu_1$ は繊維の幅優先探索と文法の純生成長の両方で同じ値になった。

**共通目標の対照実験（$\Delta=0$）。** 上の $G_{n,n}$ は $h_1=h_\zeta=2^n\cdot2^n$ の**共通目標**であり、本報告の定理4.1の仮定（$h_1\ne h_\zeta$）を満たさない。また $G_{n,n}$ の言語は経路・繊維型そのものではなく（$\mathtt a$ の連の長さが $2^m$ で割り切れるという位置的な条件をもつ）、本報告の族の型の反例でもない。ここでは「共通目標なら $\mu_1/(g\theta)$ が増え得る」ことの対照としてのみ使う。比 $\mu_1/(\|G\|\bar\theta)$ は $n$ とともに増える。

| $n$ | $\|G_{n,n}\|$ | $\bar\theta$ | $\mu_1$ | $\mu_1/(\|G\|\bar\theta)$ |
|---:|---:|---:|---:|---:|
| 1 | 21 | 3 | 4 | 6.349e-02 |
| 2 | 33 | 7 | 16 | 6.926e-02 |
| 3 | 45 | 15 | 64 | 9.481e-02 |
| 4 | 57 | 31 | 256 | 1.449e-01 |
| 5 | 69 | 63 | 1024 | 2.356e-01 |
| 6 | 81 | 127 | 4096 | 3.982e-01 |

この対照は、定理4.1で $\Delta\ne0$ が本質的であることを示す。$\Delta=0$ ではすべての非終端で $|\Phi_B|=1$ となり、分裂・定数の区別が消えるため、純語の導出が二分規則で自由に枝分かれできる。実際 $G_{n,n}$ の $\mu_1=4^n$ は $\bar\theta=2^{n+1}-1$ の二乗程度であり、線形上界は成り立たない。

### 2.3 代入可能性判定器の検算

- Astra 2026-10-31 命題5.1 の $P_{N,2}=\{(ab)^N\}\cup\{(ab)^ic(ab)^{2-i}:0\le i\le2\}$、$N=1,\dots,5$：すべて arity 1・2 を通過（$\mu_1=2N$）。Astra の証明と一致。
- Astra 2026-10-30 §8.1 の $K_2$：arity 1 は通過、arity 2 は失敗。検出した証人は
  \[
  \mathbf x=(\mathtt{cba},\mathtt b),\quad
  \mathbf y=(\mathtt{cb},\mathtt{ab}),\quad
  E=(\varepsilon,\mathtt a,\mathtt c),\quad
  F=(\mathtt{bca},\mathtt{ab},\varepsilon)
  \]
  で、$E[\mathbf x]=E[\mathbf y]=\mathtt{cbaabc}\in K_2$、$F[\mathbf x]=\mathtt{bcacbaabb}\in K_2$、$F[\mathbf y]=\mathtt{bcacbabab}\notin K_2$ である。`validate_certificate` で再検査した。Astra 報告 §8.1 の証人とは別の証人だが、同じ違反である。
- 有限言語 $\{\mathtt a,\mathtt b\}$：arity 1・2 を通過。

### 2.4 定理4.1の構造補題のランダム検査

シード 20261031 の乱数で、非終端3〜5個・アルファベット $\{a,b,c\}$・非終端番号の小さい方だけを子に持つ非循環文法を4000個生成し、言語が有限（最大長 $\le10$、語数2〜40）で、かつ「純語がすべて $\varphi=h_1$、混合語がすべて $\varphi=h_\zeta$、$h_1\ne h_\zeta$」を満たす $d=1$ の $\varphi$ が見つかるものを抽出した。275例が条件を満たした。各例で次を検査した。

- $|\Phi_B|\le2$（$\Phi_B$ は非終端 $B$ の全生成物の $\varphi$ 値の集合）：違反0。
- 一つの規則の分裂な（$|\Phi|=2$）子が2個以上：違反0。
- 分裂な頭の $c$ を含まない規則で、全子が純生成物を持ち、かつ定数な子が混合生成物を持つ：違反0。
- $\mu_1\le(2r+1)|V|\bar\theta$：違反0。

これは定理の証明の各段階を有限例で確認したものであり、証明ではない。証明は §4 にある。

---

## 3. 族の一覧と増え方

### 3.1 族の定義

すべて $d=1$、$\Sigma_1=\{a,b\}$（族Cは $\{a,b,d\}$）、$\zeta$ 文字は $c$ である。$N=2^n$、$\mu_1$ は繊維の幅優先探索で正確に求めた。

- **族A（二分＋分離した混合部）**：一頂点、$a:0\to1$、$b:1\to0$、$c:0\to0$。$\varphi(a)=1$、$\varphi(b)=0$、$\varphi(c)=0$、$h_1=N$、$h_\zeta=0$。
  \[
  L_A=\{(ab)^N\}\cup\{c^m:m\ge1\},\qquad \mu_1=2N.
  \]
  文法：$E_0\to ab$、$E_i\to E_{i-1}E_{i-1}$、$C\to c\mid cC$、$S\to E_n\mid C$。
- **族A'（豊かな混合部）**：一頂点、三ループ。$\varphi(a)=1$、$\varphi(b)=-1$、$\varphi(c)=0$、$h_1=N$、$h_\zeta=0$。
  \[
  L_{A'}=\{w:\ |w|_a-|w|_b=N\}\cup\{w:\ |w|_a=|w|_b,\ |w|_c\ge1\},\qquad \mu_1=N.
  \]
  文法：$D$ は均衡純語、$M$ は $c$ を含む均衡語、$Q_0\to Da\mid a$、$Q_i\to Q_{i-1}Q_{i-1}$、$S\to Q_n\mid Q_nD\mid M$。純部分は $(Da)^N D$（$D$ は空でもよい）の分解による。
- **族B1（二頂点、$c$ を頂点1のループに）**：$a:0\to1$、$b:1\to0$、$c:1\to1$。$\varphi(a)=1$、$\varphi(b)=0$、$\varphi(c)=0$、$h_1=N$、$h_\zeta=1$。
  \[
  L_{B1}=\{(ab)^N\}\cup\{ac^mb:m\ge1\},\qquad \mu_1=2N.
  \]
- **族B2（二頂点、$c$ を戻り辺に）**：$a:0\to0$、$b:0\to1$、$c:1\to0$。$\varphi(a)=1$、$\varphi(b)=0$、$\varphi(c)=0$、$h_1=N$、$h_\zeta=0$。
  \[
  L_{B2}=\{a^N\}\cup\{(bc)^m:m\ge1\},\qquad \mu_1=N.
  \]
- **族C（中立文字3個）**：$a:0\to1$、$b:1\to0$、$d:0\to0$、$c:0\to0$。$\varphi(a)=1$、$\varphi(b)=0$、$\varphi(d)=1$、$\varphi(c)=0$、$h_1=N$、$h_\zeta=0$。
  \[
  L_C=\{w\in\{d,ab\}^*:\ |w|_{ab}+|w|_d=N\}\cup\{c^m:m\ge1\},\qquad \mu_1=N.
  \]
- **族D（$d=2$）**：一頂点、三ループ。$\varphi(a)=(1,0)$、$\varphi(b)=(0,1)$、$\varphi(c)=(-1,0)$、$h_1=(N,0)$、$h_\zeta=(0,0)$。
  \[
  L_D=\{a^N\}\cup\{w\in\{a,c\}^+:\ |w|_a=|w|_c\ge1\},\qquad \mu_1=N.
  \]
  $L_D$ は文脈自由（$D\to ac\mid ca\mid aDc\mid cDa\mid DD$、$S\to A_n\mid D$）である。

すべての族で $h_1\ne h_\zeta$ であり、定理4.1の仮定を満たす。また $L$ は経路・繊維型であり、Astra §8.2 の証明により全 arity で代入可能性を持つ。

### 3.2 増え方の表

窓は $\ell=8$ である。`win_eq` は長さ8以下で $L(G)=L$ であったかを示す。`bound` は定理4.1の上界 $(2r+1)|V|\bar\theta$。$\mu_1$ は幅優先探索の厳密値。

**族A**（$\|G\|=6n+18$、$\bar\theta=2^{n+1}$、$\mu_1=2^{n+1}$）

| $n$ | $N$ | $\|G\|$ | $\bar\theta$ | $\mu_1$ | $\mu_1/(\|G\|\bar\theta)$ | win_eq | bound |
|---:|---:|---:|---:|---:|---:|---|---:|
| 1 | 2 | 24 | 4 | 4 | 4.167e-02 | 真 | 80 |
| 2 | 4 | 30 | 8 | 8 | 3.333e-02 | 真 | 200 |
| 3 | 8 | 36 | 16 | 16 | 2.778e-02 | 真 | 480 |
| 4 | 16 | 42 | 32 | 32 | 2.381e-02 | 真 | 1120 |
| 5 | 32 | 48 | 64 | 64 | 2.083e-02 | 真 | 2560 |
| 6 | 64 | 54 | 128 | 128 | 1.852e-02 | 真 | 5760 |
| 7 | 128 | 60 | 256 | 256 | 1.667e-02 | 真 | 12800 |
| 8 | 256 | 66 | 512 | 512 | 1.515e-02 | 真 | 28160 |

**族A'**（$\|G\|=6n+69$、$\bar\theta=2^n+2$、$\mu_1=2^n$）

| $n$ | $N$ | $\|G\|$ | $\bar\theta$ | $\mu_1$ | $\mu_1/(\|G\|\bar\theta)$ | win_eq | bound |
|---:|---:|---:|---:|---:|---:|---|---:|
| 1 | 2 | 75 | 5 | 2 | 5.333e-03 | 真 | 125 |
| 2 | 4 | 81 | 6 | 4 | 8.230e-03 | 真 | 180 |
| 3 | 8 | 87 | 10 | 8 | 9.195e-03 | 真 | 350 |
| 4 | 16 | 93 | 18 | 16 | 9.558e-03 | 真 | 720 |
| 5 | 32 | 99 | 34 | 32 | 9.507e-03 | 真 | 1530 |
| 6 | 64 | 105 | 66 | 64 | 9.235e-03 | 真 | 3300 |
| 7 | 128 | 111 | 130 | 128 | 8.870e-03 | 真 | 7150 |
| 8 | 256 | 117 | 258 | 256 | 8.481e-03 | 真 | 15480 |

**族B1**（$\|G\|=6n+20$、$\bar\theta=2^{n+1}$、$\mu_1=2^{n+1}$）

| $n$ | $N$ | $\|G\|$ | $\bar\theta$ | $\mu_1$ | $\mu_1/(\|G\|\bar\theta)$ | win_eq | bound |
|---:|---:|---:|---:|---:|---:|---|---:|
| 1 | 2 | 26 | 4 | 4 | 3.846e-02 | 真 | 80 |
| 2 | 4 | 32 | 8 | 8 | 3.125e-02 | 真 | 200 |
| 3 | 8 | 38 | 16 | 16 | 2.632e-02 | 真 | 480 |
| 4 | 16 | 44 | 32 | 32 | 2.273e-02 | 真 | 1120 |
| 5 | 32 | 50 | 64 | 64 | 2.000e-02 | 真 | 2560 |
| 6 | 64 | 56 | 128 | 128 | 1.786e-02 | 真 | 5760 |
| 7 | 128 | 62 | 256 | 256 | 1.613e-02 | 真 | 12800 |
| 8 | 256 | 68 | 512 | 512 | 1.471e-02 | 真 | 28160 |

**族B2**（$\|G\|=6n+19$、$\bar\theta=\max(4,2^n)$、$\mu_1=2^n$）

| $n$ | $N$ | $\|G\|$ | $\bar\theta$ | $\mu_1$ | $\mu_1/(\|G\|\bar\theta)$ | win_eq | bound |
|---:|---:|---:|---:|---:|---:|---|---:|
| 1 | 2 | 25 | 4 | 2 | 2.000e-02 | 真 | 80 |
| 2 | 4 | 31 | 4 | 4 | 3.226e-02 | 真 | 100 |
| 3 | 8 | 37 | 8 | 8 | 2.703e-02 | 真 | 240 |
| 4 | 16 | 43 | 16 | 16 | 2.326e-02 | 真 | 560 |
| 5 | 32 | 49 | 32 | 32 | 2.041e-02 | 真 | 1280 |
| 6 | 64 | 55 | 64 | 64 | 1.818e-02 | 真 | 2880 |
| 7 | 128 | 61 | 128 | 128 | 1.639e-02 | 真 | 6400 |
| 8 | 256 | 67 | 256 | 256 | 1.493e-02 | 真 | 14080 |

**族C**（$\|G\|=6n+20$、$\bar\theta=2^n+1$、$\mu_1=2^n$）

| $n$ | $N$ | $\|G\|$ | $\bar\theta$ | $\mu_1$ | $\mu_1/(\|G\|\bar\theta)$ | win_eq | bound |
|---:|---:|---:|---:|---:|---:|---|---:|
| 1 | 2 | 26 | 3 | 2 | 2.564e-02 | 真 | 60 |
| 2 | 4 | 32 | 5 | 4 | 2.500e-02 | 真 | 125 |
| 3 | 8 | 38 | 9 | 8 | 2.339e-02 | 真 | 270 |
| 4 | 16 | 44 | 17 | 16 | 2.139e-02 | 真 | 595 |
| 5 | 32 | 50 | 33 | 32 | 1.939e-02 | 真 | 1320 |
| 6 | 64 | 56 | 65 | 64 | 1.758e-02 | 真 | 2925 |
| 7 | 128 | 62 | 129 | 128 | 1.600e-02 | 真 | 6450 |
| 8 | 256 | 68 | 257 | 256 | 1.465e-02 | 真 | 14135 |

**族D**（$d=2$、$\|G\|=6n+32$、$\bar\theta=\max(4,2^n)$、$\mu_1=2^n$）

| $n$ | $N$ | $\|G\|$ | $\bar\theta$ | $\mu_1$ | $\mu_1/(\|G\|\bar\theta)$ | win_eq | bound |
|---:|---:|---:|---:|---:|---:|---|---:|
| 1 | 2 | 38 | 4 | 2 | 1.316e-02 | 真 | 80 |
| 2 | 4 | 44 | 4 | 4 | 2.273e-02 | 真 | 100 |
| 3 | 8 | 50 | 8 | 8 | 2.000e-02 | 真 | 240 |
| 4 | 16 | 56 | 16 | 16 | 1.786e-02 | 真 | 560 |
| 5 | 32 | 62 | 32 | 32 | 1.613e-02 | 真 | 1280 |
| 6 | 64 | 68 | 64 | 64 | 1.471e-02 | 真 | 2880 |
| 7 | 128 | 74 | 128 | 128 | 1.351e-02 | 真 | 6400 |
| 8 | 256 | 80 | 256 | 256 | 1.250e-02 | 真 | 14080 |

**観察。** どの族でも $\mu_1=\Theta(2^n)$、$\bar\theta=\Theta(2^n)$、$\|G\|=\Theta(n)$ であり、$\mu_1/(\|G\|\bar\theta)=\Theta(1/n)\to0$ である。すなわち $\bar\theta$ は $\mu_1$ と同程度に増え、反例の条件 $\mu_1=n^{\omega(1)}$ かつ $g\theta=n^{O(1)}$ は満たされない。これは定理4.1の上界（$\mu_1\le(2r+1)|V|\theta$、ここで $|V|=\Theta(n)$）と整合する。

### 3.3 族Dの MCFL 性

族Dの言語 $L_D=\{a^N\}\cup\{w\in\{a,c\}^+:|w|_a=|w|_c\ge1\}$ は、有限言語 $\{a^N\}$ と均衡言語（文脈自由）の和であり、文脈自由言語の和は文脈自由である。したがって $L_D$ はファンアウト1（したがって $\le2$）の MCFL である。$d=2$ の一般の経路・加法量族は2カウンタ言語になり得るので、$L$ が MCFL であることは一般には別途確認が必要である（§7）。

### 3.4 近道規則の試み

族Aで、$E_i\to E_{i-1}E_{i-1}$ に加えて $E_i\to c$ を各段に置き、開始を $S\to E_n$ とした文法を試した（Astra 2026-10-30 §8.3 の $H_n$ と同じ型）。$\|G\|=8n+8$、$\bar\theta=n+3$ で $\theta$ は小さくなるが、言語が一致しない。

| $n$ | $\mu_1$ | $\|G\|$ | $\bar\theta$ | 窓一致 | 不一致の例 |
|---:|---:|---:|---:|---|---|
| 1 | 4 | 16 | 4 | 偽 | 文法が $c^m$ ($m\ge2$) を生成しない |
| 2 | 8 | 24 | 5 | 偽 | 余分：`ababc`, `cabab`；不足：`ccc` など |
| 3 | 16 | 32 | 6 | 偽 | 余分：`ababcc`, `cababc`, `ccabab` など；不足：`ccccc` など |
| 4 | 32 | 40 | 7 | 偽 | 余分：`ababccc`, `cababcc` など |
| 5 | 64 | 48 | 8 | 偽 | 余分：`ababcccc`, `cababccc` など |
| 6 | 128 | 56 | 9 | 真（窓8が短すぎる） | — |

$n\le4$ では言語が有限なので、その全体を列挙して代入可能性を全数検査した。

| $n$ | 語数 | 最長長 | arity 1・2 | 証人 |
|---:|---:|---:|---|---|
| 1 | 2 | 4 | 通過 | なし |
| 2 | 5 | 8 | **失敗** | $d=1$、$(\mathtt{cc})$ と $(\mathtt c)$ |
| 3 | 24 | 16 | **失敗** | $d=1$、$(\mathtt{cc})$ と $(\mathtt c)$ |
| 4 | 455 | 32 | **失敗** | $d=1$、$(\mathtt{cc})$ と $(\mathtt c)$ |

$n\ge2$ の失敗は Astra 2026-10-30 §8.3 の強制補題（$c,uc,u^2\in L$、$u$ 純なら $u\in L$）による証明と一致する。近道規則で $\theta$ を下げると、$E_i$ が短い混合生成物を持ち、$E_i\to E_{i-1}E_{i-1}$ が純×混合の組み合わせで $\varphi\ne h_\zeta$ の語を生成する。これが言語一致を壊す。

---

## 4. 証明：二繊維型の線形上界

課題3（候補が見つかった場合の (i)–(iii) の証明）は該当しない。反例候補は見つからず、代わりに**族全体を排除する定理**を証明する。以下の証明は計算に依存しない。

### 4.1 定理

**定理4.1（二繊維型の線形上界）。**
$\Sigma$ を有限アルファベット、$\Sigma_1\subseteq\Sigma$、$\varphi:\Sigma^*\to\mathbb Z^d$ をモノイド準同型、$h_1,h_\zeta\in\mathbb Z^d$、$h_1\ne h_\zeta$ とする。$L\subseteq\Sigma^+$ が
\[
L\cap\Sigma_1^+\subseteq\varphi^{-1}(h_1),
\qquad
L\cap(\Sigma^+\setminus\Sigma_1^+)\subseteq\varphi^{-1}(h_\zeta)
\tag{4.1}
\]
を満たすとする。$G$ を $L$ の reduced good なファンアウト1の CFG 表示で、規則ランク $\le r$、$\theta=\bar\theta_G$、$V$ を非終端集合とする。$L\cap\Sigma_1^+\ne\emptyset$ なら
\[
\boxed{\mu_1(L)\le(2r+1)|V|\theta.}
\tag{4.2}
\]

**注意4.2.** 仮定 (4.1) は「純語はすべて同じ $\varphi$ 値 $h_1$ をもち、混合語はすべて同じ $\varphi$ 値 $h_\zeta$ をもつ」ことだけを言う。経路・グラフ・係数の符号は使わない。したがって定理は Astra §8.2 の族をすべて含み、さらに「二繊維型」の任意の言語を含む。$h_1=h_\zeta$ の場合は仮定を満たすが、定理の結論は偽である（§2.2の対照）。$h_1\ne h_\zeta$ は補題4.4で「差が $0$ か $\Delta$ のいずれか」という形で使われ、補題4.5の Minkowski 和で「3値が相異なる」ことを保証する。

**注意4.3.** ファンアウト $\le2$ の MCFG でも、生成物をタプルとして総長と全 $\varphi$ 値で議論すれば同じ証明が通用する（§4.5）。本報告の計算はファンアウト1の表示だけを扱った。

### 4.2 補題

以下 $L_B(G)$ は非終端 $B$ の生成物（ファンアウト1では語）の集合、$\varphi$ は語について加法的とする。

**補題4.4（各非終端の $\varphi$ 値は高々2個）。**
各 $B\in V$ に対して
\[
\Phi_B:=\{\varphi(u):u\in L_B(G)\}
\]
は高々2元である。さらに、純な生成物の値を $p_B$、混合の生成物の値を $m_B$ と書けば（存在する場合）、
\[
p_B-m_B\in\{0,\ \Delta\},\qquad \Delta:=h_1-h_\zeta.
\tag{4.3}
\]

**証明。** 原稿 `lem:thickness-equivalence`(iv) により、$B$ に成功文脈 $E_B$（$|E_B|_{\rm fix}\le\theta$）で、すべての $u\in L_B(G)$ に対して $E_B[u]\in L(G)=L$ となるものが取れる。$E_B$ の固定部の $\varphi$ 値を $\varphi(E_B)$ と書く。$E_B$ が混合なら、すべての $u$ について $E_B[u]$ は混合なので $\varphi(u)=h_\zeta-\varphi(E_B)$、すなわち $p_B=m_B$。$E_B$ が純なら、純な $u$ については $E_B[u]$ は純なので $\varphi(u)=h_1-\varphi(E_B)$、混合の $u$ については $\varphi(u)=h_\zeta-\varphi(E_B)$。よって $p_B-m_B=h_1-h_\zeta=\Delta$。$\square$

**補題4.5（Minkowski 和と分裂な子の一意性）。**
規則 $R:A\to\rho(B_1,\dots,B_q)$ に対して
\[
\varphi(\rho)+\Phi_{B_1}+\cdots+\Phi_{B_q}\subseteq\Phi_A.
\tag{4.4}
\]
したがって $|\Phi_{B_j}|=2$ となる子 $B_j$ は高々1個である。

**証明。** 任意の $u_j\in L_{B_j}$ に対して $\rho(u_1,\dots,u_q)\in L_A(G)$ であり、$\varphi$ の加法性から $\varphi(\rho(u_1,\dots,u_q))=\varphi(\rho)+\sum_j\varphi(u_j)$。よって (4.4)。$\Phi_A$ は高々2元（補題4.4）。二つの子 $B_i,B_j$ が $|\Phi|=2$ なら、$\Phi_{B_i}=\{v_i,v_i-\delta_i\}$、$\Phi_{B_j}=\{v_j,v_j-\delta_j\}$、$\delta_i,\delta_j\ne0$ と書けて、和は
\[
V,\quad V-\delta_i,\quad V-\delta_j,\quad V-\delta_i-\delta_j
\]
を含む。$\delta_i\ne\delta_j$ なら最初の3つは相異なる。$\delta_i=\delta_j=\delta$ なら $V,V-\delta,V-2\delta$ であり、$\mathbb Z^d$ は捩れなしなので $2\delta\ne0$、よって3つは相異なる。いずれも $|\Phi_A|\le2$ に反する。$\square$

**補題4.6（定数な子は純のみ）。**
規則 $R:A\to\rho(B_1,\dots,B_q)$ が純な導出に現れる（したがって $\rho$ は $c$ を含まず、各 $B_j$ は純な生成物を持つ）とし、$|\Phi_A|=2$ とする。このとき $|\Phi_{B_j}|=1$ なる子 $B_j$ は混合の生成物を持たない。

**証明。** $B_j$ が混合の生成物 $u$ を持つと仮定する。他の子の純な生成物 $u_l$ と、$B_j$ の純な生成物 $u'$ を取る。$|\Phi_{B_j}|=1$ なので $\varphi(u)=\varphi(u')$。よって $\rho(u_1,\dots,u,\dots,u_q)$ は混合な $A$ の生成物で、その $\varphi$ 値は純な組 $\rho(u_1,\dots,u',\dots,u_q)$ の値と等しい。純な組の値は $p_A$、混合な組の値は $m_A$ で、$|\Phi_A|=2$ より $p_A\ne m_A$。矛盾。$\square$

**補題4.7（最短純語の導出の性質）。**
$w$ を最短の純語（$|w|=\mu_1$）とし、$T$ を $w$ の導出のうち長さ最小・同長なら節点数最小のものとする。このとき：
(i) $T$ の各節点の生成物は、その非終端の最短の純生成物である。
(ii) 根から葉への経路に同じ非終端は現れない。特に $T$ の高さは $|V|$ 以下。
(iii) $B$ が純生成物のみを持つなら、$B$ の最短純生成物の長さ $d_B$ は $2\theta$ 以下。

**証明。** (i) 節点 $u$ の非終端を $B$、生成物を $y$ とする。$y'$ を $B$ のより短い純生成物とすると、$y'$ の $\varphi$ 値は補題4.4より $p_B=\varphi(y)$。$T$ の $u$ を $y'$ の導出で置き換えると、$w$ と同じ文脈 $E$ により $E[y']\in L(G)=L$ が得られ、純で $\varphi$ 値は $\varphi(E)+p_B=h_1$。よって $w$ より短い純語が $L$ に存在し、$\mu_1$ の最小性に反する。
(ii) 同じ非終端 $B$ が $u$（上）と $v$（下）に現れるとする。$u$ の部分木を $v$ の部分木で置き換えると、$B$ の純生成物が純生成物に置き換わり、$\varphi$ 値は $p_B$ のまま。よって純語で $\varphi=h_1$ の $L$ の語が得られ、長さは短くなるか（$v$ の生成物が短い場合）、同じで節点が減る（同じ長さの場合）。いずれも $T$ の選択に反する。
(iii) $B$ の最短純生成物 $y$ の導出で規則 $R:B\to\rho(D_1,\dots,D_q)$ を使う。$B$ が純生成物のみを持つので $\rho$ は $c$ を含まず、各 $D_j$ も純生成物のみを持つ（混合生成物があれば、$c$ を含まない $\rho$ により $B$ に混合生成物ができる）。$y$ の最小性から各子の生成物は $D_j$ の最短純生成物で、$d_B=|\rho|+\sum_jd_{D_j}$。$R$ の最短成功使用 $z$ は長さ $\le\theta$ で、$z=E[\rho(\eta_1,\dots,\eta_q)]$、$\eta_j\in L_{D_j}(G)$。$D_j$ は純生成物のみなので $\eta_j$ は純で $|\eta_j|\ge d_{D_j}$。よって $\sum_jd_{D_j}\le|z|\le\theta$。原稿 `lem:thickness-equivalence`(i) より $|\rho|\le\theta$。したがって $d_B\le2\theta$。$\square$

### 4.3 定理4.1の証明

$w$ を最短純語、$T$ を補題4.7の導出とする。$T$ の節点の非終端を $|\Phi_B|$ で分類する。$|\Phi_B|=2$ のものを**分裂**、$|\Phi_B|=1$ のものを**定数**と呼ぶ。$L\cap\Sigma_1^+\ne\emptyset$ かつ $L\cap(\Sigma^+\setminus\Sigma_1^+)\ne\emptyset$ のとき、根 $S$ は $|\Phi_S|=|\{h_1,h_\zeta\}|=2$ なので分裂である。$L$ が純語のみからなるときは、すべての規則が純語の導出にのみ使われるので $\theta\ge\mu_1$ であり (4.2) は自明である。以下、混合語も存在するとする。

補題4.5より、各規則の分裂な子は高々1個である。したがって $T$ の分裂な節点は根から一本の鎖をなす。補題4.7(ii) よりその長さは $|V|$ 以下である。鎖の各節点の規則は純な導出に現れるので $c$ を含まず、その直接端末数は $\theta$ 以下（原稿 `lem:thickness-equivalence`(i)）。鎖節点の子のうち分裂でないもの（定数な子）は補題4.6より純生成物のみを持ち、補題4.7(iii) よりその部分木の生成物の長さは $2\theta$ 以下である。鎖節点の子は高々 $r$ 個である。

$T$ のすべての端末は、鎖節点が直接書く端末か、鎖節点の定数な子の部分木に属する端末のいずれかである。よって
\[
|w|\le|V|\cdot\theta+|V|\cdot r\cdot2\theta=(2r+1)|V|\theta.
\]
$|w|=\mu_1$ なので (4.2) を得る。$\square$

### 4.4 系

**系4.6.** 定理4.1の仮定の下で、$L$ の任意の reduced good ファンアウト $\le2$、ランク $\le r$ の表示 $G$ に対して
\[
\mu_1(L)\le(2r+1)\|G\|\,\bar\theta_G.
\]
特に、族 $(L_n,G_n)$ が $g_n\theta_n=n^{O(1)}$ を満たすなら $\mu_1(L_n)=n^{O(1)}$ であり、$\mu_1(L_n)=n^{\omega(1)}$ は起こらない。

**証明。** $|V|\le\|G\|$ を (4.2) に代入する。$\square$

**系4.7（族の排除）。** Astra 2026-10-31 §8.2 の設計仕様（一文字一辺の経路、任意の $d$、任意の整数係数、型別目標 $h_1,h_\zeta$）で $h_1\ne h_\zeta$ なら、反例の族は存在しない。$h_1=h_\zeta$ で三文字なら Astra 2026-10-31 定理6.1により $\mu_1\le16(r+1)^4\theta^4(\theta+3)+2$ である。$h_1=h_\zeta$ で四文字以上の場合は本報告の範囲外である（§7）。

### 4.5 ファンアウト2への拡張（証明の同一性）

ファンアウト $\le2$ の MCFG では、非終端 $B$ の生成物はタプル $\mathbf u=(u_1,\dots,u_d)$、$d\le2$、その長さは $\|\mathbf u\|_1$、$\varphi$ 値は $\sum_i\varphi(u_i)$ とする。成功文脈 $E_B$ は $d$ 穴文脈で、$E_B[\mathbf u]\in L$ がすべての $\mathbf u\in L_B(G)$ について成り立つ。補題4.4の $\Phi_B$ をタプルの全 $\varphi$ 値の集合とすれば、同じ証明で $|\Phi_B|\le2$ と (4.3) が従う。補題4.5の Minkowski 和はタプルの全 $\varphi$ 値について成立する。補題4.6の「定数な子」は混合成分を含むタプルを持たない子で、同じ論法で排除できる。補題4.7(iii) は $d_B$ を純タプルの最小総長とし、$d_B=|\rho|+\sum_jd_{D_j}$（線形・非削除性）と最短成功使用の子タプルの総長 $\ge d_{D_j}$ から $d_B\le2\theta$ を得る。鎖の長さは $|V|$、子は高々 $r$ 個。よって (4.2) はファンアウト $\le2$ でも成り立つ。本報告の計算はファンアウト1の表示のみを扱ったが、定理の適用範囲はファンアウト $\le2$ である。

---

## 5. 族が失敗した理由

### 5.1 障害 (O5) の定量的な形

族A, A', B1, B2, C, D のいずれでも、長い純語を作る規則（$E_i\to E_{i-1}E_{i-1}$ や $Q_i\to Q_{i-1}Q_{i-1}$）は、その非終端が純語しか生成しないため、純語の文でしか使われない。したがって
\[
\theta_G(R)\ge\text{（その規則を使う最短の純文の長さ）}\ge\mu_1/(\text{段数})
\]
となり、$\bar\theta$ は $\mu_1$ と同程度になる。表のとおり、族Aでは $\bar\theta=\mu_1$、族A'では（$n\ge2$ で）$\bar\theta=\mu_1+2$、族B1では $\bar\theta=\mu_1$ である。これが (O5) の具体的な現れである。

### 5.2 近道規則が失敗する理由

近道規則 $E_i\to c$ を加えると、$E_i$ は短い混合生成物 $c$ を持つ。すると $E_i\to E_{i-1}E_{i-1}$ は「純×純」「混合×混合」「純×混合」の3種の組を生成する。$\varphi$ の加法性から、純×混合の組の $\varphi$ 値は $p_{E_{i-1}}+m_{E_{i-1}}$ であり、これは親が混合なら $h_\zeta$ でなければならないが、実際は $h_1$ 側の値とずれる。計算で得られた余分語（`ababc`, `cabab` など）がこれである。また $n\ge2$ では一穴代入可能性も破れる（Astra 2026-10-30 §8.3 の強制補題）。近道で $\theta$ を下げると言語かクラス所属が壊れる。

「近道の $\varphi$ 値を各段で合わせられるか」という問いへの答えは、この族では**否**である。補題4.4により、各非終端の純生成物の値 $p_i$ と混合生成物の値 $m_i$ の差は $0$ か $\Delta$ でなければならない。倍増規則 $E_i\to E_{i-1}E_{i-1}$ の子の組を純・混合で場合分けすると、親の値は $2p_{i-1}$、$p_{i-1}+m_{i-1}$、$2m_{i-1}$ の3種になり、親の高々2値に収めるには $p_{i-1}=m_{i-1}$（すなわち $\Delta=0$）が必要である。$h_1\ne h_\zeta$ ではこれが成り立たないので、近道を各段に置いても $\varphi$ を合わせられない。これが定理4.1の補題4.5・4.6の具体的な現れである。

### 5.3 定理4.1による統一的な説明

定理4.1の証明の要点は、$h_1\ne h_\zeta$ のとき、各非終端の $\varphi$ 値が高々2個で、その差が $\Delta$ か $0$ のいずれかであること（補題4.4）、二つの「分裂な」子を同時に持てないこと（補題4.5）、分裂な親の定数な子は純生成物しか持てないこと（補題4.6）である。この3点から、純語の導出の「分裂な鎖」は高々 $|V|$ 節点で、残りの純生成物のみの部分木は高々 $2\theta$ の長さしか持てない。よって純語の長さは $(2r+1)|V|\theta$ 以下になる。族A–Dの $\bar\theta=\Theta(\mu_1)$ はこの上界の帰結であり、近道規則は補題4.6の条件（定数な子が混合生成物を持つ）に違反するために言語を壊す。

### 5.4 残る自由度（一般の問題 M に向けて）

定理4.1は「純語が単一の $\varphi$ 繊維に含まれ、混合語が別の単一の繊維に含まれる」という二繊維性だけを使う。したがって、一般の問題 M の反例候補は次のいずれかでなければならない。

1. 純語が複数の加法量を持つ（単一の準同型の繊維でない）。たとえば、純語の Parikh ベクトルが複数の一次方程式を満たす、あるいは加法量が非可換モノイドに値を取る。
2. 混合語の側も複数の繊維に分かれる。
3. 加法量の代わりに、型付き文法の構造（型付き非終端の分布）を本質的に使う言語。

Astra §8.2 の設計仕様は 1・2 を満たさないので、この型では反例が出ない。Astra 2026-10-31 §8.2 が「型別に異なる目標を使うことが残された自由度」と述べた部分は、本報告の定理で閉じる。

---

## 6. 実行したコマンドと出力

### 6.1 コマンド

```text
cd C:\Users\Owner\Documents\GitHub\Papers\02_fixed-h-mcfg\revision
py -3 check_s2_typewise_search.py
```

Python 3.12.10、標準ライブラリのみ。乱数シードは 20261031（§2.4）。実行時間は約4.3秒、終了コード0、標準エラー出力なし。

### 6.2 出力全文

```text
=== ENV ===
python 3.12.10 | standard library only

=== 1. FINITE (2,s)-SUBSTITUTABILITY (arity 1,2) ===
P_{1,2} words=4 arity1_2=PASS mu1=2
P_{2,2} words=4 arity1_2=PASS mu1=4
P_{3,2} words=4 arity1_2=PASS mu1=6
P_{4,2} words=4 arity1_2=PASS mu1=8
P_{5,2} words=4 arity1_2=PASS mu1=10
K_2 words=6 arity1=PASS arity2=FAIL (expected) witness d=2 x=('cba', 'b') y=('cb', 'ab')
finite language {a,b}: arity1_2=PASS

=== 2. GRAMMAR ANALYSER ON KNOWN EXAMPLES ===
G_{1,1} size=21 theta=3 mu1=4 reduced=True good=True
G_{1,2} size=27 theta=5 mu1=8 reduced=True good=True
G_{2,1} size=27 theta=5 mu1=8 reduced=True good=True
G_{2,2} size=33 theta=7 mu1=16 reduced=True good=True
G_{2,3} size=39 theta=11 mu1=32 reduced=True good=True
G_{3,2} size=39 theta=11 mu1=32 reduced=True good=True
L_{1,2} size=20 theta=2 mu1=2 equal_up_to_3=True
L_{2,1} size=16 theta=2 mu1=2 equal_up_to_3=True
L_{2,2} size=42 theta=3 mu1=4 equal_up_to_5=True
L_{2,3} size=68 theta=4 mu1=6 equal_up_to_7=True
L_{3,2} size=64 theta=4 mu1=6 equal_up_to_7=True

=== 2b. COMMON-TARGET CONTROL (paper G_{n,n}; Delta = 0) ===
This family is NOT of the task's two-target type; it shows that with
h1 = h_zeta the ratio mu1/(||G|| theta) can grow.
G_{1,1} size=21 theta=3 mu1=4 ratio=6.349e-02
G_{2,2} size=33 theta=7 mu1=16 ratio=6.926e-02
G_{3,3} size=45 theta=15 mu1=64 ratio=9.481e-02
G_{4,4} size=57 theta=31 mu1=256 ratio=1.449e-01
G_{5,5} size=69 theta=63 mu1=1024 ratio=2.356e-01
G_{6,6} size=81 theta=127 mu1=4096 ratio=3.982e-01

=== 3. FAMILY TABLES ===
columns: n N mu1 ||G|| theta rank ratio=mu1/(||G||theta) window_eq |V| bound=(2r+1)|V|theta

-- family A  (ab)^N | c^+
n=1 N=2 mu1=4 size=24 theta=4 rank=2 ratio=4.167e-02 win_eq=True reduced=True good=True |V|=4 bound=80
n=2 N=4 mu1=8 size=30 theta=8 rank=2 ratio=3.333e-02 win_eq=True reduced=True good=True |V|=5 bound=200
n=3 N=8 mu1=16 size=36 theta=16 rank=2 ratio=2.778e-02 win_eq=True reduced=True good=True |V|=6 bound=480
n=4 N=16 mu1=32 size=42 theta=32 rank=2 ratio=2.381e-02 win_eq=True reduced=True good=True |V|=7 bound=1120
n=5 N=32 mu1=64 size=48 theta=64 rank=2 ratio=2.083e-02 win_eq=True reduced=True good=True |V|=8 bound=2560
n=6 N=64 mu1=128 size=54 theta=128 rank=2 ratio=1.852e-02 win_eq=True reduced=True good=True |V|=9 bound=5760
n=7 N=128 mu1=256 size=60 theta=256 rank=2 ratio=1.667e-02 win_eq=True reduced=True good=True |V|=10 bound=12800
n=8 N=256 mu1=512 size=66 theta=512 rank=2 ratio=1.515e-02 win_eq=True reduced=True good=True |V|=11 bound=28160

-- family A' rich mixed
n=1 N=2 mu1=2 size=75 theta=5 rank=2 ratio=5.333e-03 win_eq=True reduced=True good=True |V|=5 bound=125
n=2 N=4 mu1=4 size=81 theta=6 rank=2 ratio=8.230e-03 win_eq=True reduced=True good=True |V|=6 bound=180
n=3 N=8 mu1=8 size=87 theta=10 rank=2 ratio=9.195e-03 win_eq=True reduced=True good=True |V|=7 bound=350
n=4 N=16 mu1=16 size=93 theta=18 rank=2 ratio=9.558e-03 win_eq=True reduced=True good=True |V|=8 bound=720
n=5 N=32 mu1=32 size=99 theta=34 rank=2 ratio=9.507e-03 win_eq=True reduced=True good=True |V|=9 bound=1530
n=6 N=64 mu1=64 size=105 theta=66 rank=2 ratio=9.235e-03 win_eq=True reduced=True good=True |V|=10 bound=3300
n=7 N=128 mu1=128 size=111 theta=130 rank=2 ratio=8.870e-03 win_eq=True reduced=True good=True |V|=11 bound=7150
n=8 N=256 mu1=256 size=117 theta=258 rank=2 ratio=8.481e-03 win_eq=True reduced=True good=True |V|=12 bound=15480

-- family B1 a c^+ b
n=1 N=2 mu1=4 size=26 theta=4 rank=2 ratio=3.846e-02 win_eq=True reduced=True good=True |V|=4 bound=80
n=2 N=4 mu1=8 size=32 theta=8 rank=2 ratio=3.125e-02 win_eq=True reduced=True good=True |V|=5 bound=200
n=3 N=8 mu1=16 size=38 theta=16 rank=2 ratio=2.632e-02 win_eq=True reduced=True good=True |V|=6 bound=480
n=4 N=16 mu1=32 size=44 theta=32 rank=2 ratio=2.273e-02 win_eq=True reduced=True good=True |V|=7 bound=1120
n=5 N=32 mu1=64 size=50 theta=64 rank=2 ratio=2.000e-02 win_eq=True reduced=True good=True |V|=8 bound=2560
n=6 N=64 mu1=128 size=56 theta=128 rank=2 ratio=1.786e-02 win_eq=True reduced=True good=True |V|=9 bound=5760
n=7 N=128 mu1=256 size=62 theta=256 rank=2 ratio=1.613e-02 win_eq=True reduced=True good=True |V|=10 bound=12800
n=8 N=256 mu1=512 size=68 theta=512 rank=2 ratio=1.471e-02 win_eq=True reduced=True good=True |V|=11 bound=28160

-- family B2 a^N | (bc)^+
n=1 N=2 mu1=2 size=25 theta=4 rank=2 ratio=2.000e-02 win_eq=True reduced=True good=True |V|=4 bound=80
n=2 N=4 mu1=4 size=31 theta=4 rank=2 ratio=3.226e-02 win_eq=True reduced=True good=True |V|=5 bound=100
n=3 N=8 mu1=8 size=37 theta=8 rank=2 ratio=2.703e-02 win_eq=True reduced=True good=True |V|=6 bound=240
n=4 N=16 mu1=16 size=43 theta=16 rank=2 ratio=2.326e-02 win_eq=True reduced=True good=True |V|=7 bound=560
n=5 N=32 mu1=32 size=49 theta=32 rank=2 ratio=2.041e-02 win_eq=True reduced=True good=True |V|=8 bound=1280
n=6 N=64 mu1=64 size=55 theta=64 rank=2 ratio=1.818e-02 win_eq=True reduced=True good=True |V|=9 bound=2880
n=7 N=128 mu1=128 size=61 theta=128 rank=2 ratio=1.639e-02 win_eq=True reduced=True good=True |V|=10 bound=6400
n=8 N=256 mu1=256 size=67 theta=256 rank=2 ratio=1.493e-02 win_eq=True reduced=True good=True |V|=11 bound=14080

-- family C  3 neutral
n=1 N=2 mu1=2 size=26 theta=3 rank=2 ratio=2.564e-02 win_eq=True reduced=True good=True |V|=4 bound=60
n=2 N=4 mu1=4 size=32 theta=5 rank=2 ratio=2.500e-02 win_eq=True reduced=True good=True |V|=5 bound=125
n=3 N=8 mu1=8 size=38 theta=9 rank=2 ratio=2.339e-02 win_eq=True reduced=True good=True |V|=6 bound=270
n=4 N=16 mu1=16 size=44 theta=17 rank=2 ratio=2.139e-02 win_eq=True reduced=True good=True |V|=7 bound=595
n=5 N=32 mu1=32 size=50 theta=33 rank=2 ratio=1.939e-02 win_eq=True reduced=True good=True |V|=8 bound=1320
n=6 N=64 mu1=64 size=56 theta=65 rank=2 ratio=1.758e-02 win_eq=True reduced=True good=True |V|=9 bound=2925
n=7 N=128 mu1=128 size=62 theta=129 rank=2 ratio=1.600e-02 win_eq=True reduced=True good=True |V|=10 bound=6450
n=8 N=256 mu1=256 size=68 theta=257 rank=2 ratio=1.465e-02 win_eq=True reduced=True good=True |V|=11 bound=14135

-- family D  d=2
n=1 N=2 mu1=2 size=38 theta=4 rank=2 ratio=1.316e-02 win_eq=True reduced=True good=True |V|=4 bound=80
n=2 N=4 mu1=4 size=44 theta=4 rank=2 ratio=2.273e-02 win_eq=True reduced=True good=True |V|=5 bound=100
n=3 N=8 mu1=8 size=50 theta=8 rank=2 ratio=2.000e-02 win_eq=True reduced=True good=True |V|=6 bound=240
n=4 N=16 mu1=16 size=56 theta=16 rank=2 ratio=1.786e-02 win_eq=True reduced=True good=True |V|=7 bound=560
n=5 N=32 mu1=32 size=62 theta=32 rank=2 ratio=1.613e-02 win_eq=True reduced=True good=True |V|=8 bound=1280
n=6 N=64 mu1=64 size=68 theta=64 rank=2 ratio=1.471e-02 win_eq=True reduced=True good=True |V|=9 bound=2880
n=7 N=128 mu1=128 size=74 theta=128 rank=2 ratio=1.351e-02 win_eq=True reduced=True good=True |V|=10 bound=6400
n=8 N=256 mu1=256 size=80 theta=256 rank=2 ratio=1.250e-02 win_eq=True reduced=True good=True |V|=11 bound=14080

=== 4. SHORTCUT ATTEMPTS (do they still generate L?) ===
A-shortcut n=1 N=2 mu1=4 size=16 theta=4 window_eq=False only_G=[] only_L=['cc', 'ccc', 'cccc', 'ccccc', 'cccccc', 'ccccccc']
A-shortcut n=2 N=4 mu1=8 size=24 theta=5 window_eq=False only_G=['ababc', 'cabab'] only_L=['ccc', 'cccc', 'ccccc', 'cccccc', 'ccccccc', 'cccccccc']
A-shortcut n=3 N=8 mu1=16 size=32 theta=6 window_eq=False only_G=['ababcc', 'ababccc', 'cababc', 'cababcc', 'ccabab', 'ccababc'] only_L=['ccccc', 'cccccc', 'ccccccc', 'cccccccc']
A-shortcut n=4 N=16 mu1=32 size=40 theta=7 window_eq=False only_G=['ababccc', 'ababcccc', 'cababcc', 'cababccc', 'ccababc', 'ccababcc'] only_L=[]
A-shortcut n=5 N=32 mu1=64 size=48 theta=8 window_eq=False only_G=['ababcccc', 'cababccc', 'ccababcc', 'cccababc', 'ccccabab'] only_L=[]
A-shortcut n=6 N=64 mu1=128 size=56 theta=9 window_eq=True only_G=[] only_L=[]

=== 5. FINITE CHECK OF THE SHORTCUT LANGUAGE (small n) ===
A-shortcut n=1 |L|=2 maxlen=4 arity1_2=PASS witness=None
A-shortcut n=2 |L|=5 maxlen=8 arity1_2=FAIL witness=(1, ('cc',), ('c',))
A-shortcut n=3 |L|=24 maxlen=16 arity1_2=FAIL witness=(1, ('cc',), ('c',))
A-shortcut n=4 |L|=455 maxlen=32 arity1_2=FAIL witness=(1, ('cc',), ('c',))

=== 6. STRUCTURAL CHECKS ON RANDOM ACYCLIC GRAMMARS ===
acyclic two-fibre grammars checked=275 (trials=4000, errors=0)
violations: |Phi_B|<=2: 0; at most one split child: 0; constant child pure-only: 0
violations of mu1 <= (2r+1)|V|theta: 0

=== 7. SUMMARY ===
Known-example validation: PASS
Family tables: every correct grammar satisfies mu1 <= (2r+1)|V|theta;
  along every family mu1 grows like 2^n and theta also grows like 2^n,
  hence mu1/(||G||theta) tends to 0, not to infinity.
Shortcut grammars: window equality fails for n>=2; the full finite
  language fails arity-1 substitutability for n>=2.
Common-target control: mu1/(||G||theta) grows like 2^n/n (Delta=0),
  which is exactly the case excluded by the report's theorem.
Structural lemmas: no violation in the random acyclic sample
ALL_ASSERTIONS_PASSED
```

---

## 7. 限界と未解決点

1. **一般の問題 M は未解決である。** 定理4.1は二繊維型の言語だけを扱う。$(2,s)$-代入可能な MCFL 全体では、純語が単一の $\varphi$ 繊維に収まらない言語があり得る。§5.4 に残る自由度を整理した。
2. **$d\ge3$ の MCFL 性は未確認である。** $d=1$ は文脈自由（正則言語と一次方程式の共通部分）、$d=2$ は族Dのように文脈自由になる場合があるが、一般の $d=2$ は2カウンタ言語になり得る。定理4.1は MCFL 表示が存在すればその表示に対して上界を与えるが、存在自体は別問題である。
3. **計算の窓は有限である。** 族の表の `win_eq` は長さ8以下の一致にすぎない。族Aの $n\ge3$ では純語 $(ab)^N$ が窓の外にあり、純部分の一致は構成的な議論（$E_i$ が $(ab)^{2^i}$ を生成すること）に依存する。表の数値（$\|G\|,\bar\theta,\mu_1$）は定義から厳密に計算した値であり、窓の一致は補助的な検査である。
4. **近道文法の $n\ge5$ の全数検査はしていない。** $n\ge5$ では言語が大きすぎて全列挙できない。$n\le4$ の全数検査と Astra 2026-10-30 §8.3 の解析的証明（$c,uc,u^2$ からの強制）で失敗は証明されている。
5. **文献上の新規性は未確認である。** 定理4.1の証明は初等的で、既知の議論の組合せかもしれない。本報告は指定原稿・指定報告との差分を示すもので、網羅的な文献調査や独立査読を経たものではない。
6. **共通目標・四文字以上は本報告では扱っていない。** 定理4.1は $h_1\ne h_\zeta$ を要求する。$h_1=h_\zeta$ の三文字の場合は Astra 2026-10-31 定理6.1で覆われるが、中立文字が3個以上の共通目標の場合は、定理6.1の三文字の証明の一般化を本報告では確認していない。ただし本報告の族C・Dは $h_1\ne h_\zeta$ なので定理4.1で覆われる。
7. **定理4.1の計算による検証は有限例に限る。** §2.4 の275例は証明の各段階の sanity check であり、証明そのものではない。証明は §4 の解析的議論である。

---

## 付録A. 定理4.1の適用範囲のまとめ

| 言語の型 | $h_1=h_\zeta$ | $h_1\ne h_\zeta$ |
|---|---|---|
| 経路（一文字一辺）＋加法量、三文字、任意の $d$ | Astra 2026-10-31 定理6.1：$\mu_1\le16(r+1)^4\theta^4(\theta+3)+2$ | 本報告 定理4.1：$\mu_1\le(2r+1)|V|\theta$ |
| 同上、四文字以上、任意の $d$ | Astra 定理6.1の三文字の証明をそのまま一般化した結果は本報告では確認していない | 本報告 定理4.1（文字数に依存しない） |
| 一般の二繊維型（経路でない） | 定理4.1の証明は $\Delta=0$ で崩れる（対照実験） | 定理4.1 |
| 一般の $(2,s)$-代入可能 MCFL | 未解決 | 未解決 |

本報告の計算が扱った族はすべて $h_1\ne h_\zeta$ であり、定理4.1で覆われる。Astra §8.2 の設計仕様で $h_1\ne h_\zeta$ の部分は、グラフ・$\varphi$・$d$・文字数によらず反例を出さない。

---

## 付録B. 使用した既知結果と引用箇所

- 原稿 `02-v2-lg-fanout-boundary/main.tex`：
  - `def:standard-mcfg`（大きさ $\|G\|$ の定義）— §2.1(c)。
  - `lem:thickness-equivalence`（(i) 直接端末数 $\le\theta$、(iv) 短い成功文脈 $E_A$）— §4.2 補題4.4、補題4.7(iii)。
  - `prop:binary-u1-quadratic`（$G_{m,n}$ の数値）— §2.2 の検算。
  - `prop:u1-weight-all-fanout`（共通目標・一定重みの二乗上界）— §1 の背景。
  - `op:fanout-two`（一般の問題 M）— §1、§7。
- Astra 2026-10-31 `astra_s2_pureword_2026-10-31.md`：
  - §2 定理2.2（有限差替え証明書からの二乗上界）— 本報告では直接使わないが、共通目標側の背景。
  - §6 定理6.1（共通加法量の経路言語の五次上界）— §1、付録A。
  - §8.2（設計仕様）— §1、§3.1、§5.4。
- Astra 2026-10-31 `astra_s2_shortcontext_2026-10-31.md`：
  - 命題5.1（$P_{N,2}$ の代入可能性と $\mu_1=2N$）— §2.3 の検算。
- Astra 2026-10-30 `astra_ternary_u1_fanout2_2026-10-30.md`：
  - 補題5.1（一文字一辺の経路言語の全 arity 代入可能性）— §3.1 の族のクラス所属。
  - §8.3（周期倍増＋$c$ 短絡の失敗、強制補題）— §3.4、§5.2。
- ChatGPT 2026-10-30 `chatgpt_ternary_u1_fanout2_2026-10-30.md`：
  - 定理5.1（NFA の状態数による代表長）— §1 の障害 (O3) の背景。

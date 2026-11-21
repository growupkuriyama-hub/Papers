# 第四段・早期チェックポイント1（2026-11-14）

**状態**：主補題 P0^ℓ・P1^ℓ の証明完了（手計算）。定理Lの全体証明と数値検査は作業中。この断片だけで再開できるように書く。GitHub・原稿は変更していない。

## 対象クラス（新しい定義）

ℓ≥1 を固定する。$s_\ell:=s_{\ell-1,\ell-1}$（`def:prefix-suffix-typing` の窓型付け）、$N_\ell(w)\in\mathbb N^{\Sigma^\ell}$ を $w$ の長さ ℓ の因子の出現数ベクトルとする。

**定義（ℓ-局所計数言語）**：ある $\mathcal Q\subseteq M_{\ell-1,\ell-1}\times\mathbb N^{\Sigma^\ell}$ について
$$L\cap\Sigma^+=\{w\in\Sigma^+:(s_\ell(w),N_\ell(w))\in\mathcal Q\}.$$

含まれるもの：
- SL_ℓ・LT_ℓ・LTT_ℓ（ℓ-因子の有無・閾値・接頭接尾）と任意の $Q\subseteq\mathbb N^\Sigma$ の交わり。$|w|\ge\ell-1$ なら $\Psi(w)=\Psi(\mathrm{pref}_{\ell-1}w)+\pi(N_\ell(w))$（π は因子の末尾文字）だから。
- 定理Pの $\mathrm{Path}_D(s,t)\cap\Psi^{-1}(Q)$（各文字が一意な辺なら、歩道性は 2-因子の条件、端点は接頭・接尾 1 文字）。つまり **ℓ=2 の場合**。
- ℓ=1：$\Psi^{-1}(Q)$（可換言語）。
- ℓ-因子の個数条件（例：$|w|_{ab}=|w|_{ba}$）。

## 補題 P0^ℓ [独立に証明]

$y,y'\in(\Sigma^+)^d$ が各成分で $s_\ell(y_i)=s_\ell(y'_i)$、$\mathrm{alph}(y_i)=\mathrm{alph}(y'_i)$、かつ $\sum_iN_\ell(y_i)=\sum_iN_\ell(y'_i)$ を満たすなら、任意の $E\in\mathcal E_d$ で $E[y]\in L\iff E[y']\in L$。とくに $y\equiv_{L,s}y'$（$s\preceq c_\Sigma\times s_\ell$ の任意の型付け）。

*証明*：$\widehat s_\ell$ は単射でないモノイド準同型なので $s_\ell(E[y])=s_\ell(E[y'])$。$E[y]$ の ℓ-因子の出現は、(a) ある片（文脈片 $v_m$ または成分）の内部、(b) 二つ以上の片にまたがるもの、に分かれる。(b) の出現は、ある片の長さ $\le\ell-1$ の接尾、完全に含まれる中間片（長さ $\le\ell-2<2(\ell-1)$ なので $s_\ell$ は語そのものを記録）、ある片の長さ $\le\ell-1$ の接頭からなる。したがって (b) の多重集合は片の $s_\ell$ 型の列だけで決まる。(a) の和は $\sum N(v_m)+\sum_iN_\ell(y_i)$。よって $N_\ell(E[y])=N_\ell(E[y'])$。代入可能性は使わない。∎

**注意（依頼文の警告への回答）**：穴の間の固定区切りが ℓ−1 文字未満でも問題ない。またがり因子は片の型の**列**で決まり、短い片は型が語全体を記録するから。

## 補題 P1^ℓ（不純窓の色） [独立に証明]

設定は第三段報告と同じ（極大自由節点 η、成分 $\varphi_\kappa$、DFS 接頭反鎖 $I_j$、置換後の成分 $\psi^{(j)}_\kappa$、$U_j$ は $I_j$ の占める原位置）。

- $\psi^{(j)}_\kappa$ の内部 ℓ-窓のうち、置換文字（短い生成組 $u_{B_\nu}$ の文字）を一つでも含むものを**不純窓**、その多重集合を $\mathrm{Imp}_\kappa(j)\in\mathbb N^{\Sigma^\ell}$ とする。
- **色**：$\mathrm{col}(j):=\bigl(s_\ell(\psi^{(j)}_\kappa),\ \mathrm{Imp}_\kappa(j)\bigr)_{\kappa\le g}$。
- 種類数 $\le T_\ell^{\,f}(1+B)^{k^\ell f}$。ここで $T_\ell=|s_\ell(\Sigma^+)|$、$B=rH(\theta+f(\ell-1))$。

**主張**：$\mathrm{col}(j)=\mathrm{col}(j')$（$j<j'$）なら各 κ について
$$Z_\kappa:=\#\{\varphi_\kappa\text{ の内部窓で }U_j\text{ と交わらず }U_{j'}\text{ と交わるもの}\}=N_\ell(\psi^{(j)}_\kappa)-N_\ell(\psi^{(j')}_\kappa)\ \ge0$$
は de Bruijn グラフ $D_\ell$（頂点 $\Sigma^{\ell-1}$、辺 $\Sigma^\ell$）上の circulation である。さらに $N_\ell(W_j)-N_\ell(W_{j'})=\sum_\kappa Z_\kappa$、$s_\ell(W_j)=s_\ell(W_{j'})$ が成り立つ。

*証明*：
1. 置換は空でない語（good 文法は ε-free）で $U_j$ の連を置き換える。したがって $\psi^{(j)}_\kappa$ の窓で原文字だけからなるものは、$\varphi_\kappa$ の窓で $U_j$ と交わらないもの（**純窓**）とちょうど一対一に対応する。
2. よって $N_\ell(\psi^{(j)}_\kappa)=\mathrm{Pure}_\kappa(j)+\mathrm{Imp}_\kappa(j)$。$U_j\subseteq U_{j'}$ より $\mathrm{Pure}(j')\subseteq\mathrm{Pure}(j)$ で、色が等しいので差は $Z_\kappa\ge0$。
3. 長さ $\ge\ell-1$ の語の内部窓は、$\mathrm{pref}_{\ell-1}$ から $\mathrm{suf}_{\ell-1}$ への $D_\ell$ の歩道である。$s_\ell$ 型が等しければ両端が等しいか、語そのものが等しい。どちらでも差は circulation。
4. $W_j$ と $W_{j'}$ は η の成分以外で一致する（$W_j=E_A[x_{I_j}]$）。P0^ℓ の証明と同じく、またがり窓は片の型の列で決まり一致する。∎

**否定的観察（予定）**：色を第三段の「置換文字の Parikh」だけにすると、境界をまたぐ窓の補正で $N_\ell(W_j)-N_\ell(W_{j'})\ne\sum Z_\kappa$ となりうる。数値検査で頻度を測る予定。

## 定理L（主張・証明は作業中）

$L$ は ℓ-局所計数言語、$s\preceq c_\Sigma\times s_\ell$（$c_\Sigma$ 自身を含む）、$L\in\mathcal C^{\rm mcf}_{f,s}$ とする。このとき任意の reduced good 表示 $G$（元の $v,\theta$）について
$$\tau(G,s)=O_{k,\ell,f,r}\bigl(v^{Kf+2}\theta^{Kf+1}\bigr),\qquad K=k^\ell .$$

証明の骨格：
- W2 を $D_\ell$ の辺（ℓ-因子）で行う。
- 印は各成分・各辺の最初の $c_*$ 個の窓の全位置。
- 補題 ER（凍結ブロック付き Euler 再配線）を $D_\ell$ で使う。
- 穴は $J$ の固定頂点 $u_J$ に置き、$t,h$ は先頭を共通の $h_J^{(\ell)}$ にして窓型を一致させる。

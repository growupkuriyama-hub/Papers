# 第六段 チェックポイント1：共有文字の同期接合（予想U）

**日付**：2026-11-14　／　**作成**：Claude（Opus 5.5、新規セッション）　／　**状態**：研究アーカイブ・未査読
**原稿への変更**：なし（GitHub `main`、英日 LaTeX、PDF、定理A/B/C、`op:fanout-two` には触れていない）

## 0. 資料の確認状況（初手の宣言）

公開リポジトリ `growupkuriyama-hub/Papers` を取得した（commit `3ebfdc5`、2026-11-14 17:17 JST。依頼書を追加したコミット）。

| 資料 | 扱い |
|---|---|
| `reviews/PROMPT_CLAUDE_FANOUT2_ROUND6_OVERLAPPING_PROJECTIONS_2026-11-14.md` | 全文を読んだ |
| `HANDOFF_CURRENT.md` | 全文を読んだ |
| `main.tex` | `def:grammar-properties`、admissible 文脈 $\mathcal E_d$、`def:tuple-substitutable`／`def:class-cmcf`、`prop:abelian-coset-filter`、`lem:filling-identity`、`lem:thickness-equivalence`、τ の定義、`cor:distribution-representatives`、`op:fanout-two` を読んだ。`def:uniform-polydata` は位置の確認のみ |
| `reviews/audit_Ltensor_prime_independent_2026-11-14.md` | 全文を読んだ |
| `reviews/STATUS_fable_fanout2_round5_2026-11-14.md` | 全文を読んだ |
| `reviews/fable_fanout2_round5_report.md` | プロジェクト内の同内容の写し（`claude/fable_fanout2_round5_report_2026-11-14.md`）を全文読んだ |
| `reviews/audit_theorem_P_independent_2026-11-14.md` | §1〜§7 を読んだ |
| `reviews/audit_theorem_L_independent_2026-11-14.md`、`audit_theorem_S_independent_2026-11-13.md`、`check_fable_fanout2_round5.py`、`audit_fable_round5_debruijn_ell2_ell3_2026-11-14.py`、`parked/plan1_boundary_extensions_2026-11-11.tex` | **未読**（存在は確認した）。L 監査の E1（$K+1$ 区間）・E2（ℓ=1 の非空穴）は L^⊗′ 監査と第五段報告に書かれた形でだけ知っている |

ラベル：**[独立証明]**（このセッションで証明）、**[引用補題]**、**[条件付き]**、**[明示反例]**、**[有界検査]**、**[予想]**、**[未解決]**。反例には量化ラベル (A)〜(D)（依頼書 §4）を付ける。

## 1. 冒頭の要約

1. **[独立証明] U1a（語の同時実現）。** 一般に $\Sigma=A\cup B$、$C=A\cap B$ のとき、$P\in A^*$、$Q\in B^*$ が一つの語の射影になるための必要十分条件は $\pi_C(P)=\pi_C(Q)$（語として）。共有一文字なら $|P|_c=|Q|_c$。共有二文字では Parikh 一致は不十分（`cd` と `dc`）。
2. **[独立証明] U1b（穴つき分割の同時実現）。** 穴と区切りの**一片ごと**に共有射影が一致し、穴は全文字上で非空、内側区切りも全文字上で非空であることが必要十分。全語での一致は穴ごとの一致を含意しない（具体例 §2.3）。
3. **[独立証明] 保存則。** 同色 DFS 切り口から得る差分について、**各 η 成分 κ ごとに** $Z_{\kappa,A}(\to\gamma)=Z_{\kappa,B}(\to\gamma)$（$\gamma\in C$、「γ で終わる窓の数」）。任意の ℓ で成り立つ。ただし $(i,b,J)$ ごとにまとめた和では、A 側と B 側で κ のまとめ方が違うので一致しない。
4. **[明示反例 (A)] 第五段の同順位束ねは重なりへ移植できない。** 例R（good、fan-out 2、rank 2、$A=\{a,c,e\}$、$B=\{b,c\}$、共有は $c$ のみ）では、A 側は穴1個（$\Delta_c=1$）、B 側は穴2個（錨順に bb：$\Delta_c=0$、cc：$\Delta_c=1$）。順位1の束ねは $c$ の個数が合わず、順位2は B だけの穴が $c$ を含むので不可能。**結論への反例ではない**（言語は Parikh 条件で、結論は成り立つ）。
5. **[独立証明] 修復の方針：穴を κ ごとに立て、Σ 上の語として直接作る。** すると同期（U1b の一片ごとの一致）は自動で満たされ、穴の数は $\le\operatorname{fan}(\eta)\le f$。例Rでは $h=(\mathtt{ab},\mathtt{ca})$、$t=(\mathtt{aabb},\mathtt{caca})$ で Y 側・F 側とも構成でき、$e'=2=f$。
6. **[独立証明] ℓ=2・共有一文字の簡約。** $\operatorname{dat}_{\rm ov}$ は、$c$ の個数、$a,b$ の個数、内側の $c$ 区間のうち $a$ を含むものの数 $\nu_A$、$b$ を含むものの数 $\nu_B$、両端の区間の空・非空だけで決まる（逆も成り立つ）。とくに内側区間の $a$ の列と $b$ の列を**独立に**並べ替えても $\operatorname{dat}_{\rm ov}$ は変わらない。
7. **[独立証明] 万能穴補題 H\*。** ℓ=2 で、任意の circulation の組 $(Z_A,Z_B)$（$c$ に入る数が等しい）と、必要な文字（$a$、$b$、$c$ のうち要るもの）を含む任意の語 $h$ に対し、$h$ を局所的に膨らませた $t$ があり、**どの文脈でも** $\operatorname{dat}(utv)-\operatorname{dat}(uhv)=(Z_A,Z_B)$。注意：ŝ が一致するのは、射影が長さ $\ge2$ のときに限る（§4.3）。
8. **最も危険な未証明箇所：「同じ $h$ を Y 側と F 側の両方に置けるか」（hostability）。** とくに $Z_A=p\cdot aa$、$Z_B=p'\cdot bb$（$c$ を含まない削除）で、$h$ が $a$ と $b$ を両方含む必要がある場合。F 側の文 $W_{j'}$ が「$a$ と $b$ を同じ $c$ 区間に持てない」データを持つと、$c$ を含まない $h$ は置けない。この場合は §5 で部分的に処理したが、一般の証明はまだない。
9. 有界検査：`claude_fanout2_round6_sync_test_2026-11-14.py` は全 assert を通過した（約30秒、ログ `out_sync_test_v1.txt`）。有限検査は証明の代わりではない。
10. **`op:fanout-two` は OPEN のまま。**

---

## 2. U1：同時実現の必要十分条件

設定：$\Sigma=A\cup B$、$C=A\cap B$、$\pi_X$ は $X$ への削除射影。$\pi_C\circ\pi_A=\pi_C=\pi_C\circ\pi_B$ である（$C\subseteq A,B$）。

### 2.1 U1a **[独立証明]**

**補題 U1a.** $P\in A^*$、$Q\in B^*$ について、$\pi_A(W)=P$、$\pi_B(W)=Q$ を満たす $W\in\Sigma^*$ が存在する $\iff$ $\pi_C(P)=\pi_C(Q)$。このような $W$ の全体は、$P=P_0\gamma_1P_1\cdots\gamma_nP_n$、$Q=Q_0\gamma_1Q_1\cdots\gamma_nQ_n$（$\gamma_k\in C$、$P_k\in(A\setminus C)^*$、$Q_k\in(B\setminus C)^*$）として
$$W\in (P_0\sqcup\!\sqcup\,Q_0)\,\gamma_1\,(P_1\sqcup\!\sqcup\,Q_1)\cdots\gamma_n\,(P_n\sqcup\!\sqcup\,Q_n)$$
（$\sqcup\!\sqcup$ はシャッフル）に一致する。

*証明.* (⇒) $\pi_C(P)=\pi_C(\pi_AW)=\pi_C(W)=\pi_C(Q)$。(⇐) 上の形の $W$ をとれば、$A$ の文字だけを拾うと $P_0\gamma_1P_1\cdots$、$B$ の文字だけを拾うと $Q_0\gamma_1Q_1\cdots$ になる。逆に任意の $W$ は $\pi_C(W)=\gamma_1\cdots\gamma_n$ の文字で区切られ、区切りの間は $(A\setminus C)\cup(B\setminus C)$ の語で、その $A$ 部分が $P_k$、$B$ 部分が $Q_k$ である。∎

- 共有一文字 $C=\{c\}$ では $\pi_C(P)=c^{|P|_c}$ なので、条件は $|P|_c=|Q|_c$。
- 共有二文字 $C=\{c,d\}$ では、$P=\mathtt{cd}$、$Q=\mathtt{dc}$ は Parikh が等しいが実現できない。有界検査 [1]：長さ $\le4$ で同様の対が 554 組。

### 2.2 U1b **[独立証明]**

**補題 U1b.** $P_0,\dots,P_e,p_1,\dots,p_e\in A^*$、$Q_0,\dots,Q_e,q_1,\dots,q_e\in B^*$ とする。$v_0,\dots,v_e\in\Sigma^*$、$z_1,\dots,z_e\in\Sigma^+$ で
$$\pi_A(v_k)=P_k,\ \pi_B(v_k)=Q_k,\quad \pi_A(z_m)=p_m,\ \pi_B(z_m)=q_m,\quad v_1,\dots,v_{e-1}\ne\varepsilon$$
（すなわち $F=v_0\square v_1\cdots\square v_e\in\mathcal E_e$、$F[\mathbf z]$ の射影が指定どおり）を満たすものが存在する $\iff$

1. 各片で $\pi_C(P_k)=\pi_C(Q_k)$、各穴で $\pi_C(p_m)=\pi_C(q_m)$；
2. 各穴で $p_mq_m\ne\varepsilon$；
3. 各内側区切りで $P_kQ_k\ne\varepsilon$（$1\le k\le e-1$）。

*証明.* (⇒) 1 は U1a の必要性を各片に使う。2・3 は $\Sigma=A\cup B$ より「$u=\varepsilon\iff\pi_A(u)=\pi_B(u)=\varepsilon$」から。(⇐) 各片と各穴に U1a を独立に使い、並べる。∎

- **射影で消える片**（例：$P_k=\varepsilon$ だが $Q_k=\mathtt b$）は許される。admissible 性は全文字上の非空性で判定する。両端 $v_0,v_e$ は空でもよい。
- **束ねた穴 $(t_m,h_m)$** には、同じ文脈 $F$ に対して $t$ 側と $h$ 側の両方で条件 1・2 が要る。すなわち $\pi_C(t_{m,A})=\pi_C(t_{m,B})$ かつ $\pi_C(h_{m,A})=\pi_C(h_{m,B})$。両射影が穴に参加するかどうか（参加パターン）は、条件 1 から $C$ の文字を含む限り強制される：一方の射影に $c$ があれば他方にも同じ数の $c$ が要る。型（内容型）は $\operatorname{alph}(t_m)=\operatorname{alph}(h_m)$。

### 2.3 全語の一致と穴ごとの一致の区別 **[有界検査で全数照合]**

- 有界検査 [2]：$|W|\le7$ の全ての $W$ と全ての 2 穴分割から得る射影の組は 129278 通りで、補題 U1b の条件を満たす組（同じ長さ制限）と完全に一致した。
- 例：$\pi_A$ 側 $(\varepsilon\,|\,\mathtt c\,|\,\mathtt a\,|\,\varepsilon\,|\,\mathtt c)$、$\pi_B$ 側 $(\varepsilon\,|\,\varepsilon\,|\,\mathtt b\,|\,\mathtt c\,|\,\mathtt c)$。全語 $\mathtt{cac}$ と $\mathtt{bcc}$ は $c$ が 2 個ずつで同時実現できるが、穴1の $c$ の個数が 1 と 0 で違うので、この穴分割は実現できない。

---

## 3. 保存則と、同順位束ねの失敗

### 3.1 補題K（共有文字の保存則） **[独立証明]**

$\ell\ge1$、$u,u'\in A^*$ が $\widehat s_\ell(u)=\widehat s_\ell(u')$ を満たし、$Z:=N_\ell(u)-N_\ell(u')$ とする。各文字 $\gamma$ について
$$|u|_\gamma-|u'|_\gamma=Z(\to\gamma):=\sum_{w:\ \text{最後の文字が}\ \gamma}Z(w).$$

*証明.* $|u|\ge\ell-1$ なら、$u$ の各位置 $>\ell-1$ はちょうど一つの ℓ-窓の最後の文字なので $|u|_\gamma=\#\{\gamma\text{ で終わる窓}\}+|u[{:}\ell-1]|_\gamma$。$\widehat s_\ell$ が等しいので、両語が長ければ接頭 $\ell-1$ 文字が等しく、短ければ $u=u'$ で $Z=0$。ℓ=1 では窓は文字そのもの。∎

**系K.** 同色の $j<j'$ について、P1^⊗（第五段 5.2、L^⊗′ 監査 B4。span は全文字上で定義）の $Z_{\kappa,b}=N_\ell(\pi_b\psi^{(j)}_\kappa)-N_\ell(\pi_b\psi^{(j')}_\kappa)$ を $b=A,B$ に適用すると、$\gamma\in C$ について
$$Z_{\kappa,A}(\to\gamma)=|\psi^{(j)}_\kappa|_\gamma-|\psi^{(j')}_\kappa|_\gamma=Z_{\kappa,B}(\to\gamma).$$
（$|\pi_Aw|_\gamma=|w|_\gamma=|\pi_Bw|_\gamma$。色は $\widehat s_\ell(\pi_b\psi_\kappa)$ を含むので補題Kが使える。）[引用補題：P1^⊗ の主張1]

**注意.** 一致は**κ ごと**である。P1^⊗ と補題C は $Z$ を頻出強連結成分 $J$ ごとにまとめるが、$\kappa\mapsto J_{\kappa,A}$ と $\kappa\mapsto J_{\kappa,B}$ は別の分割を与えるので、$J$ ごとの和では一致しない。

### 3.2 例R：同順位束ねの移植が壊れる **[明示反例 (A)]**

**言語.** $\Sigma=\{a,b,c,e\}$、$A=\{a,c,e\}$、$B=\{b,c\}$（$C=\{c\}$）、$L_R=\{w\in\Sigma^+:|w|_a=|w|_b+|w|_c\}$。所属は Parikh だけで決まり、Parikh は ℓ=2 の射影データから決まるので、$L_R$ は依頼書の形 $\{w:\operatorname{dat}_{\rm ov}(w)\in\mathcal Q\}$ をもつ。`prop:abelian-coset-filter`(ii) により $(f,c_\Sigma)$-代入可能、CFL なので $L_R\in\mathcal C^{\rm mcf}_{2,c_\Sigma}$。

**文法**（全規則 good：検査 [6] で 17 規則を機械的に確認）。
- $S\to xy\mid yx\mid xSy\mid ySx$（$x=a$、$y\in\{b,c\}$）、$S\to e\mid eS\mid Se\mid SS$、$S\to C$。
- $C\to\xi_1^1\,\xi_2^1\,\xi_1^2\ (B_M,S)$（rank 2）。
- $B_m\to(\xi_1^1\xi_2^1,\ \xi_1^2\xi_2^2)\ (B_{m-1},B_{m-1})$、$B_m\to(e,e)$、$B_0\to(\mathtt{ab},\mathtt{ac})$。

$L(G)=L_R$：$B$ の各成分は重み 0 の葉の連結なので健全、完全性は一行目の CFG による（標準的な議論。機械検査はしていない）。

**型付き非終端** $X=C_{\{a,b,c\}}$（arity 1）。脱出 $(e,e)$ は文字 $e$ を持ち込むので、型 $\{a,b,c\}$ の導出は $B_M$ の完全二分木を強制される。$S$ の子は大きさ 1（$S\to\mathtt{ab}$）。よって
$$x=(\mathtt{ab})^N\cdot\mathtt{ab}\cdot(\mathtt{ac})^N,\qquad N=2^M,\qquad \pi_A(x)=a^{N+1}(ac)^N,\quad \pi_B(x)=b^{N+1}c^N.$$

**一段**（有界検査は縮小定数 $c_*=50$、$M=8$、$\eta=B_5$ が葉 $[64,96)$ を覆う）。切り口 $I_1=\{\eta$の最初の葉$\}$、$I_2=\{$最初の二葉の親$\}$ をともに $(e,e)$ に置換。色（各 κ・各射影の $\widehat s_2$ と span 版の不純窓）は一致する [6]。差分：
$$Z_{1,A}=\{aa{:}1\},\ Z_{1,B}=\{bb{:}1\};\qquad Z_{2,A}=\{ac{:}1,ca{:}1\},\ Z_{2,B}=\{cc{:}1\}.$$
κ ごとの保存則：$\Delta_c(1)=0$、$\Delta_c(2)=1$（A・B で一致）。

**頻出成分.** $\pi_A(x)$ では $\{aa,ac,ca\}$ が一つの強連結成分 $J_A$。$\pi_B(x)$ では $\{bb\}$ と $\{cc\}$ が別の成分で、錨順は bb が先（間の $bc$ は稀）。

**同順位束ね（第五段 補題B を射影ごとの穴に移植）.** A 側の穴は $J_A$ の 1 個（$Z=Z_{1,A}+Z_{2,A}$、$\Delta_c=1$）、B 側は 2 個（$\Delta_c=0$ と $1$）。
- 順位1：A の穴（$\Delta_c=1$）と B の bb 穴（$\Delta_c=0$）。$|t_A|_c-|h_A|_c=1\ne0=|t_B|_c-|h_B|_c$ なので、$h$ 側と $t$ 側の両方で $c$ の個数を合わせることは**どんな $h$ を選んでも**できない（U1b 条件1）。
- 順位2：B だけの cc 穴は $c$ を含むが、$c\in A$ なので $\pi_A$ 側が空にならない。A 側に $t=h$ の自明な部分を足しても $\Delta_c$ は $0\ne1$。

錨順が逆（cc が先）なら順位1が合うので、これは**特定の手順の失敗 (A)** であり、補題の普遍量化への反例 (B) でも、総長の下界 (D) でもない。

### 3.3 κ ごとの穴による修復（例Rで実行） **[独立証明（この例）／有界検査]**

- κ=1：$h_1=\mathtt{ab}$、$t_1=\mathtt{aabb}$。κ=2：$h_2=\mathtt{ca}$、$t_2=\mathtt{caca}$（§4.2 の H\* による）。
- Y 側：$y^\pi=(\mathtt{ab})^{N-1}\,\mathtt{aabb}\,(\mathtt{ac})^N$ は $x$ と同じデータ・内容をもち、$t_1,t_2$ を順に（間に非空の $\mathtt a$）含む。$y'=y^\pi[t\to h]$ のデータは $\operatorname{dat}(x)-\sum_\kappa Z_\kappa$ [6]。
- F 側：$F[h]:=W_{j'}$（$\mathtt{ab}$ と、その後の $\mathtt{ca}$ を穴にする）。$F[t]$ のデータは $W_j$ のデータに一致し、両方 $L_R$ に入る [6]。
- 穴は 2 個で $e'=2=f$。代入可能性と移送は第五段 補題B の手順4・5と同じ（射影を使わない部分）。

---

## 4. ℓ=2・共有一文字の構造

以下 $\Sigma=\{a,b,c\}$、$A=\{a,c\}$、$B=\{b,c\}$、ℓ=2。

### 4.1 補題G（区間表示） **[独立証明]**

$w=w_0\,c\,w_1\,c\cdots c\,w_n$（$n=|w|_c$、$w_k\in\{a,b\}^*$）、$\alpha_k=|w_k|_a$、$\beta_k=|w_k|_b$ とする。$n\ge1$ のとき
$$N_2(\pi_Aw):\ aa=\sum_k(\alpha_k-1)^+,\ \ ac=\#\{k<n:\alpha_k>0\},\ \ ca=\#\{k>0:\alpha_k>0\},\ \ cc=\#\{0<k<n:\alpha_k=0\},$$
$\widehat s_2(\pi_Aw)$ は最初と最後の文字（$\pi_Aw$ が 1 文字ならその語）。B 側も同様。したがって
$$\operatorname{dat}_{\rm ov}(w)\ \longleftrightarrow\ \Gamma(w):=\bigl(n,\ |w|_a,\ |w|_b,\ \nu_A,\ \nu_B,\ [\alpha_0>0],[\alpha_n>0],[\beta_0>0],[\beta_n>0]\bigr),$$
$\nu_A=\#\{0<k<n:\alpha_k>0\}$、$\nu_B$ も同様（$n=0$ のときは $(\alpha_0,\beta_0)$）。両者は互いに決め合う。

*証明.* 公式は $\pi_Aw=a^{\alpha_0}c\,a^{\alpha_1}c\cdots$ の長さ 2 の因子を数えるだけである。逆向き：$\Gamma$ から公式で $N_2$ と端の文字が決まる。$N_2$ と端の文字から $n=ac+cc+[\text{先頭が }c]$、$|w|_a=aa+ca+[\text{先頭が }a]$、$\nu_A=ca-[\alpha_n>0]$。∎

**系G.** 内側区間の $\alpha$ の列と $\beta$ の列を**独立に**並べ替えても、また $a$ を非空区間の間で移しても（各非空区間に 1 個以上残す）、$\operatorname{dat}_{\rm ov}$ は変わらない。区間の中での $a$ と $b$ の並びも自由である。

有界検査 [3]：長さ $\le9$ の全 29524 語で $\operatorname{dat}_{\rm ov}\leftrightarrow\Gamma$、乱数 3000 例で系G。

**含意.** ℓ=2・共有一文字では、目標言語は「Parikh ベクトル＋各射影の $a$-連・$b$-連の数＋端の情報」で所属が決まる言語である。ℓ≥3 では長さ ℓ の窓が複数の短い区間にまたがるので、この並べ替え不変性は失われる。

### 4.2 補題 H\*（万能穴） **[独立証明]**

$Z_A=p\,aa+q\,cc+r(ac+ca)$、$Z_B=p'\,bb+q'\,cc+r'(bc+cb)$（D₂ の 2 頂点グラフ上の circulation の一般形）で、$m:=q+r=q'+r'$ とする（保存則）。$h\in\Sigma^+$ が、$p+r>0$ なら $a$ を、$p'+r'>0$ なら $b$ を、$m>0$ なら $c$ を含むとする。$t$ を次で定める：$h$ の最初の $a$ を $a^{1+p}$ に、最初の $b$ を $b^{1+p'}$ に、最初の $c$ を
$$c\,(Y_1c)(Y_2c)\cdots(Y_mc),\qquad Y_j=a^{[j\le r]}\,b^{[j\le r']}$$
に置き換える。このとき $t\ne\varepsilon$、$\operatorname{alph}(t)=\operatorname{alph}(h)$、各射影の最初と最後の文字は $h$ と同じで、任意の $u,v\in\Sigma^*$ について
$$N_2(\pi_A(utv))-N_2(\pi_A(uhv))=Z_A,\qquad N_2(\pi_B(utv))-N_2(\pi_B(uhv))=Z_B.$$

*証明.* 三つの置換は互いに離れた位置で起きるので、窓の変化は足し合わせられる。(a) $a\to a^{1+p}$：$\pi_A$ で $a$ の直後に $a^p$ を挿入するので、窓 $(a,y)$ が $(a,a)^p(a,y)$ になり、差は $p\,aa$。$\pi_B$ は不変。(b) $b$ も同様。(c) $c\to c(Y_1c)\cdots(Y_mc)$：$\pi_A$ では $c$ の直後に $\pi_A(Y_1c\cdots Y_mc)$ が入り、それは $c$ で終わるので、元の窓 $(c,y)$ は最後に残る。追加される内部窓は、$Y_j$ が $a$ を持てば $ca,ac$、持たなければ $cc$。合計 $r(ac+ca)+(m-r)cc=Z_A$ の $c$ 部分。B も同様で $(m-r')=q'$。内容：$r>0$ なら $p+r>0$ で $h$ は $a$ を含む。∎

**ŝ についての注意（§4.3 の検査で発見）.** 射影が 1 文字の語は $\widehat s_2$ で語そのものとして区別されるので、たとえば $h=\mathtt{ab}$（$\pi_A=\mathtt a$）と $t=\mathtt{aabb}$（$\pi_A=\mathtt{aa}$）は $\widehat s_2(\pi_A\cdot)$ が違う。したがって
- 内容型 $s=c_\Sigma$ では問題ない（穴の型は内容だけ）。
- 文脈に入れた全体の $\widehat s_2$ は、全体の射影が長さ $\ge2$ なら一致する。応用では宿主の射影は頻出窓を含み長いので成り立つ。
- 型付け $s\preceq c_\Sigma\times(\widehat s_2\circ\pi_A)\times(\widehat s_2\circ\pi_B)$ を使うなら、$|\pi_bh|\ge2$ か $\pi_bh=\pi_bt$ を追加で要求する。

有界検査 [5]：乱数 7308 例で差分の式と内容・端の文字を確認（短い射影の例外 325 件は上の注意どおり）。

### 4.3 帰結：同期の問題は「同じ $h$ を両側に置けるか」に帰着する **[独立証明]**

第五段 補題B の手順4（代入可能性）・手順5（移送）は射影を使わない。必要なのは Σ 上の穴語の組 $(t_\beta,h_\beta)_{\beta\le e'}$ で

- (J1) 非空、同じ型；
- (J2) **Y 側**：現在の状態を実現する $y^\pi$ が $t_\beta$ を順に因子として含み（同じ根成分の穴の間は非空）、$y'=y^\pi[t\to h]$ が「状態 $-\sum Z$」を実現する；
- (J3) **F 側**：$F\in\mathcal E_{e'}$ で $F[h]\in L$、$F[t]\in L$

であること。H\* により、$h$ が決まれば $t$ は決まり、(J2) は「次の状態 $S-Z$ を実現する語で $h$ を因子に含むものがある」、(J3) は「$W_{j'}$ と同じデータの文で $h$ を因子に含むものがある」に帰着する（位置によらない差分）。U1b の一片ごとの同期は、穴を Σ 上の語として作る限り**自動的に**成り立つ。

したがって残る問題は次の **hostability** だけである。

> **(HC)** 各 κ（または同じ根成分内でまとめた κ の組）について、必要な文字を含む同じ語 $h$ が、Y 側の状態と F 側のデータの両方に因子として実現できる。穴の総数は $\le f$。

---

## 5. hostability の現状

必要な文字集合を $R_\kappa\subseteq\{a,b,c\}$ とする。W2 により $\operatorname{supp}Z_{\kappa,b}$ は一つの頻出強連結成分 $J_{\kappa,b}$ に入り、D₂ の 2 頂点グラフでは $J\in\{\{aa\},\{cc\},J_3\supseteq\{ac,ca\}\}$。$c$ と $a$ が両方 $R_\kappa$ に入るのは $J_{\kappa,A}=J_3$ のときだけである（$aa$ と $cc$ を同じ強連結成分に入れるには $ac,ca$ が要る）。

| $R_\kappa$ | 使う $h$ | Y 側 | F 側 | 状態 |
|---|---|---|---|---|
| $\{a\}$、$\{b\}$、$\{c\}$ | $\mathtt a$、$\mathtt b$、$\mathtt c$ | 該当文字があれば可 | 同左 | **[独立証明]** |
| $\{a,c\}$ | $\mathtt{ca}$ | $ca$ 頻出なので、$c$ の直後に $a$ を置ける | $W_{j'}$ に残る印付きの $ca$ 窓（$\ge c_*-f$）から同様 | **[独立証明の素描]**（最終報告で詳述予定） |
| $\{b,c\}$ | $\mathtt{cb}$ | 同上 | 同上 | 同上 |
| $\{a,b,c\}$ | $\mathtt{cab}$ | $\nu_A,\nu_B$ がともに大（$J_3$ が両側）なので内側区間を揃えられる | 同上（印付き窓から $\nu^F_A,\nu^F_B\ge1$） | 同上 |
| $\{a,b\}$（$c$ を含まない削除） | $\mathtt{ab}$／$\mathtt{ba}$、または $a\,c^k\,b$／$b\,c^k\,a$ | **[独立証明]** Y 側は常に $a,b$ を共に含む区間を実現できる（$\varphi_\kappa$ が $c$ を含まなければその区間、含めば $J_3$ が両側） | **[未解決]** $W_{j'}$ のデータが「$a,b$ を共に含む区間」を許さない場合がある | **最も危険** |

$\{a,b\}$ の場合について示せたこと：

- **[独立証明]** $x_i$ が $c$ を含まず、κ が $x_i$ の中で最初の η 成分なら、$\varphi_\kappa$ より前の部分 $U$（η の外、$c$ なし）は印付きの $aa$ と $bb$ を含むので $\mathtt{ab}$ か $\mathtt{ba}$ を因子にもち、$U$ はそのまま $W_{j'}$ に現れる。Y 側は区間内の並びが自由なので向きを合わせられる。
- **[独立証明]** $x_i$ が $c$ を含まず、κ が二番目の η 成分なら、根成分 $i$ に穴を 2 個使える（$\operatorname{fan}(\eta)\le2$ が全部 $x_i$ にある）。全削除を「$a$ の穴」と「$b$ の穴」の 2 個にまとめればよい（$c$ のない区間では位置が無関係）。
- **[未解決]** $x_i$ が $c$ を含み、$W_{j'}$ が $a$ と $b$ を同じ区間に持てない（$\nu^F_A=0$ または $\nu^F_B=0$ で、両端の区間も片方しか持たない）場合。$h=a\,c^k\,b$ の $k$ を Y 側と F 側で一致させる必要がある。いくつかの具体例では一致が見つかったが、一般の議論はまだない。

## 6. 最も危険な未証明箇所（優先順）

1. **(HC) の $\{a,b\}$ 型**：上記。反例を探す有界探索を次に行う（抽象モデル：$x$、η 位置、置換 $\psi$、文脈を小さく列挙し、Y 側・F 側の実現可能な $h$ の形の集合が交わるかを総当たり）。
2. **複数の穴の順序と非空区切り**：F 側は自由に並べられるが、Y 側で二つの穴を同じ根成分に置くとき、別の区間を使う必要がある（$c$…$c$ 型の穴は区間を占有する）。資源（区間数）は頻出性から足りるはずだが未記述。
3. **ℓ≥3**：系G の並べ替え不変性が失われ、$c$ の位置が窓をまたいで効く。κ ごとの穴は依然として保存則を満たすが、H\* の類似（位置によらない膨張）は未検討。
4. **共有二文字 $\{c,d\}$**：U1a により共有射影は語として一致が要る。κ ごとの保存則は文字ごとの個数しか与えないので、$\pi_C(t)$ を両側で一致させるには追加の議論が要る。
5. 引用のみで再証明していないもの：型付き高さ（補題A）、DFS 接頭反鎖の評価、W2（$K+1$ 区間）、P1^⊗（span 版）。

## 7. 再現

- `python3 -I claude_fanout2_round6_sync_test_2026-11-14.py`（標準ライブラリのみ、シード 20261114、約30秒）。末尾に `ALL CHECKS PASSED`。
- 節 [6] の「η の極大性」の assert は空検査（常に真）で、極大性は検査していない。例Rの文法の $L(G)=L_R$ の完全性も機械検査していない。

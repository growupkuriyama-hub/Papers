# 研究報告（第二段）：局所鳩の巣法の監査と、非交互言語への一般化

**2026-11-13 / Claude Opus 5.5**（Fable 5.2 セッションの引き継ぎ）
**対象**：`op:fanout-two`（02-v2-lg-fanout-boundary）。GitHub の原稿・`main`・PDF・PR は変更していない。研究資料として納品する。

**記号**：YES = 「LG は fan-out 2 でも境界」、NO = 「SL が一様多項式データ長を持つ」（引き継ぎ書の規約）。$k=|\Sigma|$、$v=|V|$、$r$ はランク上限、$\theta=\bar\theta_G$（元の reduced good 表示 $G$ の規則厚さ）、$c=c_\Sigma$ は内容型付け。

**信頼度ラベル**：
- [手証明] この報告の中で完全な証明を与えたもの。
- [原稿] `main.tex` の補題をそのまま使ったもの。
- [計算のみ] 有限の計算でしか確かめていないもの。
- [未解決] 証明も反例もないもの。

以前のAI報告の結論には依存していない。使ったのは定義と反例だけである。

---

## 0. 結論の要約（10行）

1. **ChatGPT 修復案の判定は VALID。** 6項目すべてを独立に再証明した。反例はない。補足が要る点は5つあるが（§2.3）、どれも証明の穴ではなく、書き方が足りないだけである。
2. したがって、段付きParikhクラス $\mathcal N_{\rm st}$ で $\tau(G,c)\le 2kfH\theta(1+rH(1+rH\theta)^k)$（$H=v(2^k-1)^f$）が成り立つ。§2 にこの報告独自の完全な証明を書いた。[手証明]
3. **新しい定理S** [手証明]：$L\in\mathcal C^{\rm mcf}_{f,c}$ が次の条件を満たすとする。「$ab\not\equiv_L ba$ となる二文字 $a\ne b$ が、$L$ のどの語にも散在部分語 $aba$・$bab$ として現れない」。このとき、すべての reduced good 表示 $G$ について
   $$\tau(G,c)\le 4kf^2H\theta\bigl(1+rH\cdot 3^{\binom k2}(1+rH\theta)^k\bigr)=O_{k,f,r}(v^{k+2}\theta^{k+1}).$$
4. 定理Sは $\mathcal N_{\rm st}$ を真に含み、語順に依存する。例として、N字型の段順序の言語 $L_\natural=\{w\in{\rm ND}_P:|w|_a=|w|_d\}$ は $\mathcal C^{\rm mcf}_{f,c}$（全ての $f$）に入るが、どの段の分け方と $Q$ をとっても $\mathcal N_{\rm st}$ には入らない（§3.5）。
5. 定理Sの仮定は、段も $Q$ も使わない語順だけの内在的な条件である。言い換えると「$L$ の中で可換でない文字は交互に現れない」（非交互言語）。
6. **系** [手証明]：YES の証拠となる族（$\|G_n\|,\theta_{G_n}$ が多項式で $\tau$ が超多項式）は、可換でない二文字が交互に現れる語を必ず含む。fan-out 1 の既知の指数族はこの条件を満たしており（$\mathtt{b\,a\cdots a\,b}$）、矛盾しない。
7. 経路言語（Route 1）について：自由な因子が「頻出文字の強連結成分」に収まることを示した（補題W1・W2）[手証明]。しかし、穴を順序どおりに差し込む補題（順序付き接合）が証明できず、上界は [未解決]。
8. 三つの隙間（Route 2）について：局所鳩の巣法の削除領域は、一つの成分の中で深さ $n$ に対して $\lfloor n/2\rfloor+1$ 個の断片に分かれうる [計算のみ、$n\le12$]。障壁は「隙間が3つ」ではなく「隙間の数が有界でない」ことであり、定理Sはこの断片を可換性で一か所に集めている。
9. 新しい指数下界は得ていない。`op:fanout-two` は [未解決] のまま。
10. Python 3 の検査3本（§9）で、修復と定理Sの証明の手順を、成分を移動する規則と交差テンプレートを含む導出木の上で実行した。すべての assert を通過した。これは有限の検査であり、証明の代わりではない。

---

## 1. 復元した研究状況

- **GitHub**：`main` の最新は `a45267f`（2026-11-13 21:15）。引き継ぎ書と一致し、それ以降のコミットはない。
- **読んだ資料**：
  - `STATUS_fanout2_pigeonhole_2026-11-13.md`
  - `PROMPT_FABLE_FANOUT2_ROUND2_2026-11-13.md`（添付と同一内容）
  - `claude_fanout2_local_pigeonhole_2026-11-13.md`（全文）
  - `independent_review_local_pigeonhole_2026-11-13.md`
  - `local_pigeonhole_repair_2026-11-13.md`
  - `check_free_node_counterexample_2026-11-13.py`（再実行して成功）
  - `main.tex` の §2・§3（`def:output-refinement`、`prop:output-invariants`、`lem:typed-homogeneity`）、§5（`lem:thickness-equivalence`、`lem:witness-length-template`、`cor:distribution-representatives`）、`def:uniform-polydata`、`thm:fanout-one-data`、`lem:power-transfer`、`thm:doubling-no-lift`、`op:fanout-two`
  - `astra_fanout2_map_2026-11-10.md` の §1–3.3
- **前の Fable の進捗**：このチャットで見えるのは、資料を読み始めて課題リストを作ったところまでである。証明・計算・結論は一つも出力されていない。それ以上の未保存の作業は分からないので、推測で補っていない。

---

## 2. 課題A：修復証明の監査

### 2.1 判定表

| # | 論点 | 判定 | 根拠 |
|---|---|---|---|
| 1 | 型付き状態 $(B,\mathrm{alph}(u_1),\dots,\mathrm{alph}(u_d))$ で短絡すると高さ $\le H$ | **正しい** | 補題A。成分が移動する規則でも成り立つ。内容は準同型なので、同じ型付きラベルの部分木を入れ替えても祖先すべての成分内容は変わらない |
| 2 | 骨格節点 $\le 2kfH$ | **正しい** | 補題B(1)。印は $\le 2kf$ 個で、各印を含む節点は一本の鎖（長さ $\le H$）。印は一度も消さない |
| 3 | $\lvert I_j\rvert\le rH$、$\lvert U_{j+1}\setminus U_j\rvert\le H\theta$ | **正しい** | 補題B(3)。より精密には $\lvert I_j\rvert\le(r-1)(H-1)+1$ |
| 4 | 局所移動補題（同じ段の複数の穴、異なる成分にある同じ文字） | **正しい（補足が要る）** | 補題C。$\mathbb 1$ は重複を数える。同じ文字は異なる成分にしか現れず、各成分が印を2個ずつ与える |
| 5 | 削除を順に行っても予備文字と分布同値が保たれる | **正しい** | 補題D。$P',P'+z$ は元の木で決まる定数。印と未削除の領域は残る |
| 6 | $\tau$ の上界から、元の $\|G\|,\theta$ の多項式で特徴標本が出る | **正しい** | `cor:distribution-representatives` と $N_{\rm typ}\le 2^{kfr}\|G\|$。型付き文法の厚さは一度も使わない |

**総合判定：VALID。** 以下 §2.2 は修復ノートを承認するためではなく、独立に組み立て直した完全な証明である。

### 2.2 独立の完全証明（$\mathcal N_{\rm st}$）

**設定。** $\mathrm{st}:\Sigma\to\{1..t\}$、ND は段が非減少の語の全体とする。
$L\cap\Sigma^+={\rm ND}\cap\Psi^{-1}(Q)$（$Q$ は任意）、$L\in\mathcal C^{\rm mcf}_{f,c}$ とする。
$G$ は $L\cap\Sigma^+$ の reduced good 表示で、fan-out $\le f$、rank $\le r$ とする。
型付き非終端 $X=A_{\mathbf T}$（arity $d\le f$）を固定する。

**補題A（型付き短絡）。** $x\in L_X$ と、その $A$ からの導出木 $\mathcal T$ の対のうち、節点数が最小のものをとる。各節点 $\nu$ のラベルを $(B_\nu,\mathrm{alph}(y_{\nu,1}),\dots,\mathrm{alph}(y_{\nu,d_\nu}))$ とする。このとき、根から葉への道の上でラベルはすべて異なる。したがって道の節点数は $H:=\sum_B(2^k-1)^{\mathrm{fan}(B)}\le v(2^k-1)^f$ 以下である。

*証明。* $G$ は ε-free なので成分は空でない。よってラベルの個数は $H$ 以下。
祖先 $\nu$ と真の子孫 $\nu'$ が同じラベルを持つとする。$\nu$ の部分木を $\nu'$ の部分木に置き換えた木 $\mathcal T'$ を考える。
各規則の出力内容は、テンプレートの終端の集合と子の成分内容の和集合で決まる（`def:output-refinement` の $\mathrm{out}_\rho$ で、内容半群は可換で冪等）。$\nu$ の位置で成分内容の組が変わらないので、帰納的に祖先すべての成分内容が変わらない。
よって $\mathcal T'$ の生成組は根で型 $\mathbf T$ を持つ。`prop:output-invariants`(ii)(iv) により $L_X$ に入る。節点数が真に減るので最小性に矛盾する。∎

成分が親の別の成分へ移る規則でも、議論は位置ではなく内容の準同型だけを使うので通る。独立査読の反例 $A\to(p,\xi^1b\xi^2)(A)$ では、$A(1)$ のラベルは $(\{p\},\{x,b,y\})$、$A(0)$ のラベルは $(\{x\},\{y\})$ で異なり、矛盾しない（`check_typed_height` で確認）。

**補題B（骨格・塊・接頭反鎖）。**
**印**：各成分 $x_i$ と各 $a\in\mathrm{alph}(x_i)$ について、$a$ の最初と最後の出現。
$\mathrm{pos}(\nu)$ は $\nu$ の生成組の位置の集合。$\mathrm{pos}(\nu)$ が印を含まない節点を**自由**と呼ぶ。good な規則は nondeleting で線形なので、各節点の各成分は根のある成分の連続因子である。

1. 骨格節点（自由でない節点）は $N_{\rm sk}\le 2kfH$ 個以下。
   位置 $p$ を含む節点は、$p$ を明示的に書く規則節点の祖先の鎖そのものである（長さ $\le H$）。印は $\le 2kf$ 個。
2. 自由な節点の各成分は、ある $x_i$ の一つの段の塊（単一の段の極大な因子）に入る。
   成分が段 $s<s'$ の文字 $a,b$ を含むとする。$x_i$ は ND（$E_A[x]\in{\rm ND}$）なので、$x_i$ の中の最後の $a$ は、因子の中の $a$ と $b$ の間にあり、因子の内部にある。これは印なので矛盾。
   さらに、自由な因子に現れる各文字 $a$ の最初と最後の出現は、同じ塊の中で $\mathrm{pos}(\nu)$ の外にある。
3. 極大な自由節点 $\eta$ について、その部分木の葉を DFS 順に $\lambda_1..\lambda_q$ とする。$I_j$ を「葉がすべて $\{\lambda_1..\lambda_j\}$ に入る極大な節点」の集合、$U_j:=\bigcup_{\nu\in I_j}\mathrm{pos}(\nu)$ とする。このとき
   - $\lvert I_j\rvert\le rH$、
   - $\varnothing=U_0\subsetneq U_1\subsetneq\cdots\subsetneq U_q=\mathrm{pos}(\eta)$、
   - $\lvert U_{j+1}\setminus U_j\rvert\le H\theta$。

   *証明。* $I_j$ の節点（$\eta$ 以外）の親は、葉の区間が $j$ と $j+1$ をまたぐので $\lambda_{j+1}$ の祖先であり、一本の鎖（$\le H$）をなす。各親が $I_j$ に与える子は $r-1$ 個以下。
   $U_{j+1}\setminus U_j$ は、$\lambda_{j+1}$ の祖先のうち $I_j$ に覆われないもの（鎖、$\le H$ 個）が明示的に書く終端であり、規則ごとに $\le\theta$ 個（`lem:thickness-equivalence`(i)）。
   $\lambda_{j+1}$ は ε-free の定数規則なので、包含は真。∎

**色。** 各 $B$ に $\|u_B\|_1\le\theta$ の $u_B\in L_B(G)$ を固定する（同補題(ii)）。$\mathrm{col}(j):=\sum_{\nu\in I_j}\Psi(u_{B_\nu})$ とおく。座標は $\le rH\theta$ なので、色は $C=(1+rH\theta)^k$ 種類以下。
$x_{I_j}$ を $I_j$ の各節点を $u_{B_\nu}$ の導出に替えた組とする。これは $G$ の $A$ からの導出である。$W_j:=E_A[x_{I_j}]\in L(G)$ であり、$\Psi(W_j)=e_A+\Psi(x)-\Psi(U_j)+\mathrm{col}(j)\in Q$。

**補題C（局所移動）。** $y$ は空でない語の $d$ 組で、$y_1\cdots y_d$ が ND とする。$b_1,\dots,b_e$（$e\le f$）は $y$ の相異なる塊で、組の中での位置順に並ぶとする（段は非減少）。$b_\kappa$ の段を $s_\kappa$ とし、$0\ne z_\kappa\in\mathbb N^{\Sigma_{s_\kappa}}$、$T_\kappa=\mathrm{supp}\,z_\kappa$、$z=\sum z_\kappa$、$\mathbb 1:=\sum_\kappa\mathbb 1_{T_\kappa}$（**重複を数える**）とする。
次を仮定する。
- (i) $P',P'+z\in Q$ かつ $P'\ge2\mathbb 1$、
- (ii) $\Psi(b_\kappa)\ge z_\kappa+2\cdot\mathbb 1_{T_\kappa}$。

このとき、$y$ と「各 $b_\kappa$ から Parikh が $z_\kappa$ の文字を消した組」$y^-$ について $y\equiv_{L,c}y^-$。

*証明。*
- $c:=P'-\mathbb 1\ge\mathbb 1$ なので、各 $\kappa$ に互いに異なる予備の一文字 $g_\kappa\in T_\kappa$ を $c$ から取れる。
- $c$ の残りの文字を段の順に並べ、段 $s$ の部分の末尾に「$\square_\kappa g_\kappa$（$s_\kappa=s$ の $\kappa$ を順に）」を置いた文脈を $F$ とする。穴の間には $g_\kappa$ があるので $F\in\mathcal E_e$。
- $t'_\kappa:=\hat1_\kappa$（$T_\kappa$ の各文字を一つずつ）、$t_\kappa:=\hat z_\kappa\hat1_\kappa$ とする。$F[t']$ と $F[t]$ はどちらも ND で、Parikh は $P'$ と $P'+z$ なので、どちらも $L$ に入る。型は等しいので、arity $e\le f$ の代入可能性から $D(t)=D(t')$。
- $y$ の各 $b_\kappa$ を「残り・$\hat z_\kappa\hat1_\kappa$・$g_\kappa$」の順に並べ替える（(ii) から可能）。単一の段の塊の中の並べ替えは、どの文脈でも ND 性と Parikh を変えないので $\equiv$ を保つ。
- 任意の $E$ について、因子 $\hat z_\kappa\hat1_\kappa$ を穴に替えた $F_E$ は $\mathcal E_e$ に入る（$g_\kappa$ が残るため）。よって $E[y^\pi]\in L\iff E[y']\in L$（$y'$ は $\hat z$ を消した組）。
- 内容は $\hat1_\kappa$ が残るので保たれる。$y'$ と $y^-$ は塊の中の並べ替えで移り合う。∎

ここで (i) の $P'\ge2\mathbb 1$ について補足する。同じ文字 $a$ を含む $T_\kappa$ が複数あれば、塊は相異なり段は同じなので、別々の成分に属する。各成分は $a$ の印（最初と最後）を2個ずつ持つ。

**補題D（順次適用）。** 貪欲法で得る領域 $R=U_{j'}\setminus U_j$（$\mathrm{col}(j)=\mathrm{col}(j')$）は互いに素で、印を含まない。どの順で削っても、各段階で補題Cの仮定が成り立つ。

*証明。*
- $P':=\Psi(W_{j'})$ と $P'+z=\Psi(W_j)$ は元の木で決まり、削除の順序によらない。
- $R\subseteq\mathrm{pos}(\eta)$ が触れる塊は、補題B(2) より $\le\mathrm{fan}(\eta)\le f$ 個である。
- (ii) は、その塊の中の $R$ の文字（まだ消していない）と印（決して消さない）から従う。
- $P'\ge2\mathbb 1$ は、$P'$ が印を全部含むことから従う（印は $U_{j'}\subseteq\mathrm{pos}(\eta)$ の外にある）。
- ND 性は削除で保たれる。∎

**定理（$\mathcal N_{\rm st}$）。** 各極大自由節点で、切り口を左から処理する。現在の $j$ の色が最後に現れる $j'$ まで飛び、$U_{j'}\setminus U_j$ を削る。そのあと一段を残す。
残る段は色ごとに高々一つなので $\le C$ 個。一段あたり $\le H\theta$ 位置。極大自由節点は $\le rN_{\rm sk}$ 個。補題C・Dより、最終的な組 $x''$ は $x''\equiv x$ を満たし、
$$\tau_X\le\|x''\|_1\le N_{\rm sk}\theta+rN_{\rm sk}CH\theta\le 2kfH\theta\bigl(1+rH(1+rH\theta)^k\bigr).$$
さらに `cor:distribution-representatives` と $N_{\rm typ}\le 2^{kfr}\|G\|$ から、$\|K\|_+\le 2^{kfr}\|G\|(1+2\theta+r\tau)+1$。∎ [手証明]

### 2.3 補足（修復ノートに書き足すべき点）

1. 補題Cの $\mathbb 1$ は重複を数える。$P'\ge2\mathbb 1$ の根拠は「同じ文字を含む塊は別の成分にある」ことである（ノートでは暗黙）。
2. 塊を段の非減少順に並べられるのは、$y_1\cdots y_d$ が ND だからである（$E_A[x]\in$ ND から従い、削除で保たれる）。
3. 順次適用で使うのは、元の木で決まる $P',P'+z$ と、印（不変）だけである。途中の組の $E_A$ による受理は不要。
4. $H$ は「実際に現れる型付き非終端の数」に置き換えられる。$\lvert I_j\rvert\le(r-1)(H-1)+1$ と精密化できる。
5. 結論は $\tau$（同値類の代表）の上界であり、$t_{\rm typ}$（実際に生成できる短い組）の上界ではない（ノートの注意は正しい）。

---

## 3. 新定理S：非交互言語の局所鳩の巣法

### 3.1 定義

- **独立関係**：$I_L:=\{(a,b):a\ne b,\ \forall u,v\ (uabv\in L\iff ubav\in L)\}$。統語的に可換な文字の対である。その補集合（$a=b$ を含む）を依存関係 $D_L$ とする。$L\cap\Sigma^+$ は定義から $I_L$ 閉（隣り合う独立な文字の交換で閉じる）。
- **分離**：語 $w$ が $I$ 分離であるとは、どの依存対 $a\ne b$ についても、$w$ の中で $a$ の出現が全部 $b$ の出現より前にあるか、全部後にあることをいう。これは「散在部分語 $aba$・$bab$ を含まない」ことと同値である。
- **向き** $o(w)$：$w$ に両方現れる各依存対について、どちらが先か。値は $3^{\binom k2}$ 通り以下。
- **非交互言語**：$L\cap\Sigma^+$ のすべての語が $I_L$ 分離であるとき、$L$ を非交互という。

### 3.2 主張

**定理S** [手証明]。$f,r\ge1$ とし、$L\in\mathcal C^{\rm mcf}_{f,c}$ は非交互とする。$G$ を $L\cap\Sigma^+$ の reduced good 表示（fan-out $\le f$、rank $\le r$）とする。このとき
$$\tau(G,c)\le 4kf^2H\theta\Bigl(1+rH\cdot3^{\binom k2}(1+rH\theta)^k\Bigr),\qquad H=v(2^k-1)^f .$$
したがって $L$ は $\mathcal B^{\le r}_{f,c}$ と $\mathcal B_{f,c}$ について、$\|K\|_+\le2^{kfr}\|G\|(1+2\theta+r\tau)+1$ の特徴標本を持つ。

### 3.3 証明

以下 $I=I_L$ とし、「独立」は $I$ に関するものとする。

**S0（並べ替え不変性）。** すべての $i$ で $y_i\sim_I y'_i$（隣り合う独立な文字の交換で移り合う）なら、$y\equiv_{L,c}y'$。
*証明。* 内容は等しい。任意の $E$ について $E[y]\sim_I E[y']$ であり、$L\cap\Sigma^+$ は $I$ 閉である。∎

**S1（投影補題と系）。** $u\sim_I v$ であることと、すべての依存対 $(a,b)$（$a=b$ を含む）で $\pi_{\{a,b\}}(u)=\pi_{\{a,b\}}(v)$ であることは同値である。
*証明（$\Leftarrow$、長さの帰納法）。* $u=au'$ とする。$v$ の中で最初の $a$ より前にある文字 $b$ は、$a$ と独立である（依存なら $\pi_{\{a,b\}}$ の先頭が食い違う）。その $a$ を交換で先頭へ移し、両辺から消して帰納法を使う。∎
**系 S1'**：$I$ 分離な $u,v$ について、$u\sim_I v\iff\Psi(u)=\Psi(v)$ かつ $o(u)=o(v)$（各投影は $a^mb^n$ か $b^na^m$）。したがって、$I$ 分離な語 $w$ が $L$ に入るのは、$\Psi,o$ が $w$ と等しい語が $L$ にあるとき、かつそのときに限る。

**S2（自由な因子はクリーク）。** 印として、各成分・各文字について、最初の $2f$ 個と最後の $2f$ 個の出現をとる（$\le4kf^2$ 個）。このとき、自由な節点の成分（$x_i$ の因子 $\varphi$）に現れる相異なる二文字は独立である。
*証明。* 依存する $a,b$ が $\varphi$ の中でこの順に現れたとする。$E_A[x]\in L$ は分離なので、$a$ は全部 $b$ より前にある。すると $x_i$ の最後の $a$ は、$\varphi$ の中の $a$ と $b$ の間、つまり $\varphi$ の中にある。これは印なので矛盾。∎

**S3（間の可換性）。** $w\in L$ で、文字 $b\ne a$ が二つの $a$ の出現の間にあれば、$(a,b)\in I$。（依存なら $aba$ が現れ、分離に反する。）

**色。** $\mathrm{col}(j):=\bigl(\sum_{\nu\in I_j}\Psi(u_{B_\nu}),\ o(W_j)\bigr)$。種類は $\le3^{\binom k2}(1+rH\theta)^k=:C_S$。補題A・B(1)(3) は §2.2 と同じものを使う（骨格は $\le4kf^2H$）。

**S4（一段の削除）。** $\eta$ を極大自由節点、$j<j'$ で $\mathrm{col}(j)=\mathrm{col}(j')$、$R=U_{j'}\setminus U_j$ とする。$y$ は $x$ から位置の集合 $\mathrm{Del}$ を削った組で、$\mathrm{Del}\cap(\text{印}\cup R)=\varnothing$ かつ $y\equiv x$ とする。このとき $y\equiv y\setminus R$。

*証明。*
- **準備。** $\eta$ の成分のうち $R$ と交わるものを、位置の順に $\varphi_1..\varphi_e$（$e\le f$）とする。$\tilde\varphi_\kappa=\varphi_\kappa\setminus\mathrm{Del}$（$y_{i_\kappa}$ の連続因子）、$T_\kappa=\mathrm{alph}(R\cap\varphi_\kappa)$、$z_\kappa=\Psi(R\cap\varphi_\kappa)$ とおく。
- **(a) 写しの選択。** 各 $\kappa$ と $a\in T_\kappa$、それに予備 $g_\kappa\in T_\kappa$ に、成分 $i_\kappa$ の「最初の $2f$ 個」の印から $a$ の出現を一つずつ、互いに重ならないように割り当てる。
  - これは可能である。$a$ は $\varphi_\kappa$ の中で印でない位置に出るので、最初の $2f$ 個はすべて $\varphi_\kappa$ より前にある。最後の $2f$ 個はすべて後にある。
  - 同じ成分・同じ文字が必要な枠は $\le2f$ 個である。
- **(b) $y$ の側。** 成分 $i_\kappa$ で、選んだ写しを $\tilde\varphi_\kappa$ の直前に動かし、$\tilde\varphi_\kappa$ を $h_\kappa\,\hat z_\kappa\,g_\kappa\,\rho_\kappa$ の順に並べた組を $y^\pi$ とする。ここで $h_\kappa$ は $T_\kappa$ の各文字一つずつ、$\hat z_\kappa=R\cap\varphi_\kappa$、$\rho_\kappa$ は $\tilde\varphi_\kappa$ の残りである。
  - 反転する対は二種類しかない。
    - 写し（文字 $a$）と、それが越えた文字。越えた文字は、写しと $R\cap\varphi_\kappa$ の中の $a$ の間にある。$E_A[y]\in L$ なので、S3 により独立である。
    - $\tilde\varphi_\kappa$ と写しの内部の対。その文字は $\mathrm{alph}(\varphi_\kappa)$ に入るので、S2 により独立である。
  - よって $y\sim_I y^\pi$、S0 から $y\equiv y^\pi$。
- **(c) 組。** $t_\kappa=h_\kappa\hat z_\kappa$、$t'_\kappa=h_\kappa$ とおく。どちらも内容は $T_\kappa$ である。
- **(d) $F$ の側。** $W:=W_{j'}\in L$ は、$E_A[x]$ の各 $\varphi_\kappa$ を空でない $\psi_\kappa$ に替えた語で、印は元の位置関係のまま残る。
  - 同様に、印の写しを $\psi_\kappa$ の直前に $h'_\kappa g'_\kappa$ の順で動かす。越える文字は、写しと $\psi_\kappa$ の後にある最後側の印 $a$ の間にあるので、S3 により独立である。
  - 得られる $W'$ は $W'\sim_IW$、したがって $W'\in L$。
  - $h'_\kappa$ を穴に替えた文脈を $F$ とする。穴の間には $g'_\kappa$ があるので $F\in\mathcal E_e$ であり、$F[t']=W'\in L$。
- **(e) $F[t]\in L$。** $F[t]$ は、$W'$ の $h'_\kappa$ の直後に $T_\kappa$ の文字を挿入した語である。挿入した $a$ と $h'_\kappa$ の中の $a$ の間には $T_\kappa$ の文字しかない。これは $a$ と独立なので、$a$ に依存する文字ではない。よって分離と向きは保たれる。
  - $\Psi(F[t])=\Psi(W_{j'})+z=\Psi(W_j)$（色の Parikh 部分が等しいため）。
  - $o(F[t])=o(W_{j'})=o(W_j)$（色の向き部分が等しいため）。
  - $W_j\in L$ なので、S1' から $F[t]\in L$。
- **(f) 分布の一致。** 共通の受理文脈 $F$ を持つので、arity $e\le f$ の代入可能性から $D(t)=D(t')$。
- **(g) 置き換え。** 任意の $E\in\mathcal E_d$ について、$E[y^\pi]=F_E[t]$ かつ $E[y']=F_E[t']$ である（$y'$ は $y^\pi$ から $\hat z$ を消した組。$g_\kappa$ があるので $F_E\in\mathcal E_e$）。型も等しいので $y^\pi\equiv y'$。
- **(h) 仕上げ。** $y'$ は $y\setminus R$ から同じ置換（の制限）で得られ、反転は独立な対だけなので $y'\sim_I y\setminus R$。
  以上をつなげて $y\equiv y^\pi\equiv y'\equiv y\setminus R$。∎

**本証明。** §2.2 と同じ貪欲法で領域を選ぶ。領域は互いに素で、印と交わらない。S4 を順に適用し、各段で $y\equiv x$ を保つ。長さは §2.2 と同じ数え方で
$$\|x''\|_1\le4kf^2H\theta+r\cdot4kf^2H\cdot C_SH\theta .$$
∎

### 3.4 $\mathcal N_{\rm st}$ との関係

$\mathcal N_{\rm st}$ の言語では、同じ段の文字は $I_L$ に入る。異なる段の文字は ND の語で分離している。よって $\mathcal N_{\rm st}\subseteq$ 非交互言語であり、定理Sは §2 の定理を（定数は異なるが）含む。
パリク飽和言語は $I_L$ が全体のときにあたる。

### 3.5 真に非可換な例

段の半順序を N字型の $1<3,\ 2<3,\ 2<4$ とし、$a\mapsto1$、$b\mapsto2$、$c\mapsto3$、$d\mapsto4$ とする。${\rm ND}_P$ を「比較可能な段 $s<s'$ について、$s'$ の文字が $s$ の文字より前に来ない語」の全体とし、$L_\natural:=\{w\in{\rm ND}_P\cap\Sigma^+:|w|_a=|w|_d\}$ とおく。

- **$L_\natural$ は全ての $f$ で $\mathcal C^{\rm mcf}_{f,c}$ に入る** [手証明]。
  - CFL（カウンタと正則の交わり）なので MCFL である。
  - 内容が成分ごとに等しく、共通の受理文脈を持つ $x,y$ をとる。ND$_P$ への所属は、各成分の内部の順序（共通文脈から両方とも ND$_P$）と内容だけで決まる。
  - $|\cdot|_a-|\cdot|_d$ の総和は、共通文脈により等しくなる。
- **非交互である。** 依存対はちょうど比較可能な段の対で、ND$_P$ の語では分離している。
- **どの $\mathcal N_{\rm st}$ にも入らない。**
  - $ad,da\in L_\natural$ なので、仮に $\mathcal N_{\rm st}$ に入るなら $\mathrm{st}'(a)=\mathrm{st}'(d)$。
  - $acd,adc\in L_\natural$ なので $\mathrm{st}'(c)=\mathrm{st}'(d)$。
  - すると $cda$ も ND$'$ で Parikh が同じなので $L_\natural$ に入るはずだが、$a$ が $c$ の後にあり $cda\notin L_\natural$。矛盾。

### 3.6 系（YES 方向への必要条件）

`op:fanout-two` を YES にする族 $(L_n,G_n)$（$\|G_n\|,\theta_{G_n}$ が多項式、$\tau$ または $\mu^\star$ が超多項式）では、十分大きいすべての $n$ で $L_n$ は非交互でない。つまり、$ab\not\equiv_{L_n}ba$ となる $a,b$ が $aba$ の形で現れる語を含む。[手証明]

---

## 4. Route 1：経路言語（部分結果と障壁）

文字は $D$ の辺で、一つの文字は一本の辺とする。$L\cap\Sigma^+=\mathrm{Path}_D(u,v)\cap\Psi^{-1}(Q)$ とおく。$D$ が自己ループ以外の閉路を持つと、例えば $b:1\to2$、$d:2\to1$ について $bdb$ が現れ、$bd\not\equiv db$ なので非交互ではない。つまり定理Sの外である。

**補題W1** [手証明]。歩道 $w$ の台グラフ $S(w)$ の異なる強連結成分を結ぶ辺の文字は、$w$ にちょうど1回現れる（戻れないため）。したがって印のない因子は一つの強連結成分のブロックに入る。

**補題W2（頻度の隙間）** [手証明]。$c_1\ge1$、$c_{i+1}=kc_i+1$ とおく。$k$ 文字の出現回数は $k+1$ 個の区間 $[c_i,c_{i+1})$ の少なくとも一つを避ける。その区間を使って「頻出」を $\ge c_{i+1}$、「稀」を $<c_i$ と定めると、頻出文字の部分グラフの弱連結成分はすべて強連結である。

*証明。* 頻出の辺 $b:p\to q$ について、$q$ から頻出辺で到達できる頂点の集合を $Z$ とし、$p\notin Z$ と仮定する。
- 歩道は $b$ を通るたびに $Z$ に入るので、$Z$ に入る回数は $\ge c_{i+1}$、出る回数は $\ge c_{i+1}-1$。
- $Z$ から出る辺はすべて稀なので、出る回数は $\le k(c_i-1)<c_{i+1}-1$。矛盾。∎

これにより、印を「最初・最後の $c_{k+2}$ 個」とれば、自由な因子は頻出文字の強連結成分 $K_\kappa$ の中の歩道になる。各 $\eta$ 成分の Parikh 差 $z_\kappa$ は、色を成分ごとに分ける（種類 $(1+rH\beta)^{kf}$、$\beta$ は端点型の短い代表の長さ）と循環になることも示せる（端点型 = 最初と最後の文字は矩形帯で LG に入り、通常の骨格の議論で $\beta=O(rfvk^{2f}\theta)$）。

**障壁（[未解決]）：順序付き接合。** 定理Sの (d) にあたる段階では、$W_{j'}$ から閉歩道の多重集合 $m_\kappa$ を取り出し、それを $\psi_\kappa$ の直前に、$\kappa$ の順を保ったまま差し込む必要がある。

- 経路言語では文字の交換ができないので、動かせるのは閉部分歩道だけである。
- $K_\kappa$ の文字の写しは、チェックポイントの間のいくつもの区間に散らばりうる。ある区間から取り出す部分は、それ自体が循環でなければならない。
- 例えば $a^{50}bc^{50}d\cdots$（$b,d$ が稀、$a,c$ がループ）では、二つの頻出成分が稀な辺でしかつながらない。成分ごとに穴を分ける必要があり、ブロック単位で一つの穴にする方法は失敗する。

---

## 5. Route 2：三つの隙間 → 隙間の数は有界でない

交互の交差テンプレート $A\to(\xi_1^1\xi_2^1,\ \xi_2^2\xi_1^2)$（奇数段）／$(\xi_1^1\xi_2^1,\ \xi_1^2\xi_2^2)$（偶数段）からなる完全二分木を考える。このとき、DFS 接頭領域 $U_j$ は第2成分の中で最大 $\lfloor n/2\rfloor+1$ 個の断片に分かれる [計算のみ、$n\le12$、`check_walk_lemmas` G]。

- 局所鳩の巣法の削除領域 $R$ は、一つの成分の中で $\Theta(H)$ 個の隙間を持ちうる。arity $f$ の代入可能性は、それを直接は一度に比べられない。
- $\mathcal N_{\rm st}$ と定理Sでは、自由な因子の文字が互いに可換なので、断片を一つの穴に集められる（S4(b)）。
- 下界を作るなら、「自由な因子の中で可換でない文字が交互に現れ、断片が $>f$ 個に分かれたまま集められない」構成が必要である。

三つの隙間に関する新しい剛性補題も、指数下界の構成も得ていない [未解決]。

---

## 6. 試した構成と、成功・失敗の理由

| 構成 | 結果 | 理由 |
|---|---|---|
| 修復案の 6 項目の再証明 | 成功 | §2 |
| 段を半順序に一般化（ND$_P$） | 成功 → 定理S | 自由な因子は反鎖。印の写しは「二つの $a$ の間は独立」で動かせる |
| 段の概念なしの一般化（非交互） | 成功 | 投影補題で「$(\Psi,o)$ が同じ分離語は $\sim_I$」 |
| 向きを自由にした $\mathrm{Sep}_I$ そのもの | 定理の仮定外 | 内容型付きで代入可能でない（$x_1=ab$、$y_1=ba$、文脈 $a\square$）。仮定 $L\in\mathcal C$ は自動的には成り立たない |
| 有界交互（各依存対が $\le m$ 回交互） | 失敗 | 色に、交互の連（ラン）ごとの Parikh と連の骨格が要る。$W_j$ と $W_{j'}$ で連の構造がずれうるので、$F[t]\in L$ が示せない |
| 経路言語（ブロックごとに一つの閉歩道の穴） | 失敗 | 頻出成分が稀な辺でしかつながらない例がある（§4） |
| 経路言語（$\eta$ 成分ごとの穴、頻度の隙間つき） | 途中まで | W1・W2 と $z_\kappa$ が循環になることまでは成立。順序付き接合で止まる |
| 経路言語で $f=1$ | 途中まで | 領域は連続な閉歩道になるが、短い閉歩道 $h$ を隣に作る段階が同じ接合問題になる |

---

## 7. `op:fanout-two` について解決したこと・残ること

- **解決**（全ての $f\ge1$、全ての $\Sigma$）：非交互言語 $\cap\ \mathcal C^{\rm mcf}_{f,c}$ では $\tau$ が多項式である。これは $\mathcal N_{\rm st}$、パリク飽和言語、任意の段の半順序の ND$_P$ 型を含む。
- **残る**：可換でない文字が交互に現れる言語。自己ループ以外の閉路を持つ経路言語、Dyck 型、$(ab)^n$ 型の周期を含むものなど。
- **方向**：NO（SL の成功）には全ての $L\in\mathcal C^{\rm mcf}_{f,c}$ が必要なので、まだ示していない。YES（下界）は、§3.6 の必要条件を満たし、かつ §5 の隙間を集められない構成でなければならない。証拠としては NO 寄りの状況が広がったが、証明ではない。

---

## 8. 次に攻める補題（3つ）

1. **順序付き接合補題（経路言語）。**
   歩道 $\omega$ と、チェックポイント $\pi_1<\dots<\pi_e$（$\pi_\kappa$ の頂点は頻出の強連結成分 $K_\kappa$ にある）を考える。各 $K_\kappa$ の文字は $\ge c$ 回現れるとする。
   問い：Parikh・端点・チェックポイントの順を保ったまま、各 $\pi_\kappa$ に $K_\kappa$ を覆う長さ $\le B(k)$ の閉歩道を因子として露出させる並べ替えはあるか。真なら、定理Sの証明が経路言語でそのまま通る。偽なら、反例のグラフが新しい下界の種になる。
2. **有界交互への拡張。**
   各依存対が $L$ の語の中で $\le m$ 回しか交互しない場合を考える。連の骨格を色に入れ、$W_j$ と $W_{j'}$ の骨格が一致すれば連ごとの差が $z$ になることを示せば、定理Sが拡張される。
3. **断片が集められない下界の候補。**
   2-閉路の経路言語と §5 の交互交差テンプレートを組み合わせる。自由な因子の中の削除領域が $>f$ 個の断片に分かれ、どの arity $\le f$ の比較でも移せない言語族を構成し、$\mathcal C^{\rm mcf}_{2,c}$ に入ることを証明する。

---

## 9. 計算機検査（Python 3、標準ライブラリのみ、乱数は固定シード）

| ファイル | 内容 | 結果 |
|---|---|---|
| `check_typed_height_2026-11-13.py` | 反例の文法と、成分が移動する good MCFG 150個で、節点数最小の型付き導出に型付きラベルの重複がないことを確認 | 2175 ラベル。基底ラベルの重複は 1004 件あるが、型付きラベルの重複は 0 件。0.1秒 |
| `check_separated_pigeonhole_2026-11-13.py` | 定理Sの証明（印・S2・反鎖・色・S4 の $y$ 側と $F$ 側・最終の同値）を、N字型の半順序と鎖の二つの標的で、成分移動規則と交差テンプレートを含む12本の導出木上で実行 | 全 assert 通過。語長 4011 → 410 など。2穴の段階 177回、二つの比較不能な段にまたがる穴 78個。対照実験（重みのある自由文字を一つ消す）は検出された。約9秒 |
| `check_walk_lemmas_2026-11-13.py` | W1・W2（ランダムな歩道 334本・203本）と、隙間の数 G（$n\le12$） | 全 assert 通過。断片数は $1,2,2,3,\dots,7$ |
| 既存の `check_free_node_counterexample_2026-11-13.py` | 再実行 | 成功 |

検査の限界：標的は $L(G)\subseteq L$ となる言語で、証明に必要なのはこの包含だけである。文脈の網羅は固定部の長さ $\le3$ まで。どれも無限族の証明の代わりではない。

---

## 10. 参照した GitHub ファイル

`02-v2-lg-fanout-boundary/` 配下：
- `main.tex`
- `reviews/STATUS_fanout2_pigeonhole_2026-11-13.md`
- `reviews/PROMPT_FABLE_FANOUT2_ROUND2_2026-11-13.md`
- `reviews/claude_fanout2_local_pigeonhole_2026-11-13.md`
- `reviews/independent_review_local_pigeonhole_2026-11-13.md`
- `reviews/local_pigeonhole_repair_2026-11-13.md`
- `reviews/check_free_node_counterexample_2026-11-13.py`
- `reviews/astra_fanout2_map_2026-11-10.md`（§1–3 のみ）

未読：`fable_three_stages_2026-11-11.md`、`claude_fanout2_*_2026-11-09.md`、`parked/plan1_boundary_extensions_2026-11-11.tex` の本文。`prop:sl-reduction` の量化は依頼文と引き継ぎ書の記述に従い、独立には点検していない。

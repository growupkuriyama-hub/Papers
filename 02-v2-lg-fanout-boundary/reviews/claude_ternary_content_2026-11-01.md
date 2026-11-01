# 三文字の内容型付け $c_{\{a,b,c\}}$・ファンアウト2：$K_n$ は $n\ge3$ で脱落、修復による短縮定理、残る核は「除外された文字の消去」

**研究日**：2026年11月1日
**対象**：`growupkuriyama-hub/Papers/02-v2-lg-fanout-boundary`（clone 時の先頭 commit `1229090`）。依頼文 `reviews/prompt_claude_ternary_content_2026-11-01.md`。出発点は `reviews/claude_binary_case2_2026-11-01.md`（以下「二文字 II 報告」）、`reviews/claude_binary_content_core_2026-11-01.md`（以下「二文字核報告」）、`reviews/chatgpt_sl_positive_2026-11-01.md`（以下「ChatGPT 肯定報告」）。定義は `main.tex` §2–§4、`cor:distribution-representatives`、`lem:typing-monotone`、`prop:sl-reduction`、`op:fanout-two`、`prop:rare-type`、`lem:power-transfer`、`thm:doubling-no-lift`。参考に `parked/parked_u1_typing_level.tex` の `prop:three-letter-family`・`cor:typing-level-obstruction`、`archive-v1/revision/` の Astra・ChatGPT の S2 報告。
**判定の意味**：「証明済み」はこの報告の中に証明を書いたこと（または明示した既存の証明への還元）を指し、外部査読や文献上の新規性を意味しない。「観察」は有限の計算で、証明ではない。ただし有限言語についての全数検査と、述語で与えた言語で見つかった違反の組は、それ自体が証明である（§10 で区別する）。

---

## 0. 結論と判定

記号：$\Sigma=\{a,b,c\}$（§3・§5 の一般の補題では任意の有限 $\Sigma$、$m:=|\Sigma|$）、$c=c_\Sigma$、ファンアウト $\le2$、ランク $\le r$（$r\ge2$）、$v=|V|$、$g=\lVert G\rVert$、$\theta=\bar\theta_G$。型付き非終端 $X=A_{\mathbf S}$、$\mathbf S=(S_1,\dots,S_d)$、$d\le2$。$X$ の**成分の和** $U(X):=S_1\cup\dots\cup S_d$。「$x^4$ が現れる」は「$L$ のある語が因子 $x^4$ を持つ」の意味。

| 主張 | 判定 | 根拠 |
|---|---|---|
| **Q0**：$K_n$ は $n\ge3$ で $(2,c_\Sigma)$-組代入可能**でない**（$\Sigma\supseteq\{a,b,c\}$）。具体的な組は $\mathbf x=(b,\ baab)$、$\mathbf y=(bb,\ aab)$（内容はともに $(\{b\},\{a,b\})$）、共通の文脈 $b^{n-3}\square_1 b\square_2V_n[n{+}3:]$、食い違う文脈 $\square_1V_n[1{:}n{+}3]\square_2V_n[n{+}7:]$。$n=1,2$ では $K_n\in\mathcal C_{2,c}$。従って $K_n$ は否定の答えを与えない | **証明済み**（$n=1,2,3$ は全数検査でも確認） | §2 |
| Q0 の機構：`thm:doubling-no-lift` の冪の移行と同じ系統（二穴の間で周期を一つずらす）。ただし内容型付けは冪等なので、$u^5$ ではなく「$b^3$ の後に $b$ を含む語が続く」因子で足りる（共役移送、補題3.5） | **証明済み** | §2、§3.5 |
| ファンアウト1の下界：$K_n\in\mathcal C_{1,c_\Sigma}$、内容 $\{a,b\}$ の語は $V_n$ だけ。$\mathcal B^{\le r}_{1,c}$・$\mathcal B_{1,c}$・$\mathcal C_{1,c}$ 全体に特徴標本を持つ集合駆動作用素の全てで、特徴標本の長さ $\ge3\cdot2^n-1$（$\lVert G'_n\rVert=13n+7$、$\bar\theta=4n$、$r\ge2$、$\Sigma\supseteq\{a,b,c\}$） | **確認した**（既存の証明の検証） | §1.2 |
| 一般の道具（任意の $\Sigma$）：$x$ 塊の再配分、ブロックの交換、境界の交換 A′、**隙間の合流（新）**、**共役移送（新）** | **証明済み** | §3 |
| **Q1**：二文字の道具の移り方の表。再配分・補題A・挿入補題は移る。**補題B は移らない**：$(a\mid bc)^+$ は全ての $f$・全ての型付けで代入可能で、$a^4$・$aa$ を持ち、$b^2,c^2$ を持たず、Parikh 飽和でなく、どの文字の組も交換しないのに、$aa$ を含む語が内部の非 $a$ 隙間を任意個持つ | 移る部分は**証明済み**、補題B の三文字版は**反証** | §4 |
| 補題B の最後の矛盾の変化：合流そのものは三文字でも必ず起きる（補題3.4）。失われるのは「合流した隙間が禁止される」ことだけ。隙間が両方とも純な $y$ 塊なら矛盾は残る（補題4.2） | **証明済み** | §4 |
| **修復補題**：$x^4$ が現れ、語に $x$ の余り（長さ $\ge2$ の $x$ 塊）があれば、$x$ を許さない成分の中の $x$ 塊を全て消し、その $x$ を $x$ を許す成分へ移しても所属は保たれる | **証明済み** | 補題5.1 |
| **定理G（全体短縮と修復）**：$X$ の「悪い文字」の挿入の重複度が $k$ 以下なら $\tau_X\le49(r+1)v\theta(24+10k)$。悪い文字が無い（例：$U(X)=\Sigma$ で、外から入りうる文字が全て4乗を持ち余りがある）なら $\tau_X\le1176(r+1)v\theta$ | **証明済み** | 定理5.2、系5.3 |
| 二文字の場合 II（二文字 II 報告の定理C）は定理G の特別な場合（$k\le1$）として再現される | **証明済み** | 系5.4 |
| 一文字の和の型：重複度は「内部の隙間に入る悪い文字の数」$\iota$ で抑えられる | **証明済み** | 補題5.5 |
| 条件付き定理（Q2(c)）：除外された文字を含む語の中で、除外文字を含まない因子の長さが $\ell$ 以下なら $\tau_X\le\max\{6\ell,\ 1029(r+1)v\theta\}$ | **証明済み** | 命題5.6 |
| Q2(a)：内容 $\{a,b\}$ の成分を二文字の言語として扱う帰着。切片 $E^{-1}L\cap\{a,b\}^+$ は二文字の内容型付けで代入可能だが、その表示の $\bar\theta$ が制御できず、二文字の定理E は使えない | 帰着は**証明済み**、使えないことは例で**確認** | §6.1 |
| Q2(b)：文字の組ごとの交換の強制（$xxyx$ か $xyxx$ があれば $xy\equiv yx$）。三組全てで起きれば Parikh 飽和 | **証明済み**（既知の補題の再確認） | §6.2 |
| 純な $y$ の穴の**剛性補題**：最小の $P_y(C)$ の導出では、短縮の「符号」（差し替え後の骨格）が失う $y$ の数を決める（重み付き符号の構造） | **証明済み** | 補題6.3 |
| **三文字の全ての $L\in\mathcal C_{2,c}$ で $\tau$ が多項式か**（`op:fanout-two` の三文字の段） | **未解決**。残る核は「成分の和に入らない文字（除外文字）の消去」で、定理G・命題5.6・補題6.3 がその必要条件を与える | §8 |
| Q3：反例族の設計仕様、および試した候補（重み $2^i$ の符号族）の失敗 | 仕様は**証明済み**の必要条件の一覧、候補の失敗は具体的な違反の組（証明） | §7 |
| 新しい補題・定理が文献で既知か | **未確認** | §9 |

**今回の到達点を一文で**：$K_n$ はファンアウト2の内容型付けでは $n\ge3$ で脱落するので反例にならない。肯定の側では、二文字の証明を「導出の全体を一度に短縮し、入ってしまった他の文字を修復する」形に組み直すと、**成分の和が $\Sigma$ で4乗のある文字だけが外から入る型は線形**で、残る困難は**成分の和に入らない文字を成分の中から消す問題**だけに集約される（定理G）。その問題は、一文字の和では「隙間の重み付き符号」（補題6.3）、二文字の和では「除外文字を含まない長い因子」（命題5.6）という形で現れ、ここで止まった。

---

## 1. 設定と、使う既知の事実の検証

### 1.1 設定

$L\in\mathcal C_{2,c}$、$G$ は $L\cap\Sigma^+$ の reduced good な表示（ファンアウト $\le2$、ランク $\le r$）。各非終端 $B$ に $\lVert\omega_B\rVert_1\le\theta$ の生成組 $\omega_B\in L_B(G)$、各 $A$ に `lem:thickness-equivalence`(iv) の文脈 $E_A$（$\lvert E_A\rvert_{\rm fix}\le\theta$、$E_A[L_A(G)]\subseteq L$）を固定する。各規則が直接書く終端は $\le\theta$ 個。

内容型付けでは（二文字核報告の (1.1) と同じ理由で）

$$
\tau_X=\min\{\lVert\mathbf z\rVert_1:\ c(z_i)=S_i\ (i\le d),\ E_A[\mathbf z]\in L\}. \tag{1.1}
$$

`cor:distribution-representatives` と $N_{\rm typ}\le\lvert\mathcal P_+(\Sigma)^\sharp\rvert^{2r}g=8^{2r}g$（三文字では型が7種類、新しい単位元を足して8）から、$\tau(G,c)$ の上界は $\mathcal B^{\le r}_{2,c}$ と $\mathcal B_{2,c}$ に**共通の**特徴標本 $K$ の上界

$$
\lVert K\rVert_+\le8^{2r}g\,\bigl(1+2\theta+r\,\tau(G,c)\bigr)+\mathbf 1_{\{\varepsilon\in L\}} \tag{1.2}
$$

になる。

語 $w$ と文字 $x$ について、**$x$ 骨格** $\sigma_x(w)$ は $x$ の各極大な塊を一文字 $x$ に置き換えた語、$\rho_x(w)$ は $x$ の極大な塊の数。$x$ の塊の間の極大な $x$ を含まない因子を **$x$ 隙間**と呼ぶ。$x$ の塊が**内部**とは両隣が $x$ 以外の文字であること。語 $w$ が **$x$ の余り**を持つとは $\lvert w\rvert_x>\rho_x(w)$（長さ $\ge2$ の $x$ 塊がある）こと。

### 1.2 ファンアウト1の下界の推論の確認（依頼 §1）

- `prop:three-letter-family`：$K_n$ は Clark–Eyraud 代入可能（証明は退避ファイル付録。$n\le3$ では私の全数検査でも arity 1 の違反は無い、§10）。従って任意の型付け $s$ について $K_n\in\mathcal C_{1,s}$。有限なので CFL。
- $K_n$ の語のうち $c$ を含まないのは $V_n$ だけ（同命題。$n\le3$ で計算でも確認）。$V_n$ の内容は $\{a,b\}$（$n\ge1$）。他の語は $c$ を含む。従って $\mu_{\{a,b\}}(K_n,c_\Sigma)=\lvert V_n\rvert=3\cdot2^n-2$。
- `prop:rare-type`：$\mathcal B^{\le r}_{1,c}$（$r\ge1$）、$\mathcal B_{1,c}$、および $\mathcal C_{1,c}$ 全体に特徴標本を持つ任意の集合駆動作用素の、$K_n$ の全ての特徴標本 $F$ は $V_n$ を含み、$\lVert F\rVert_+\ge3\cdot2^n-1$。
- $G'_n$ は reduced good、ランク2、$\lVert G'_n\rVert=13n+7$、$\bar\theta_{G'_n}=4n$。従って $r\ge2$ では、$c_\Sigma$（$\Sigma\supseteq\{a,b,c\}$）は `def:uniform-polydata` の条件をファンアウト1で満たさない。

推論は正しい。下界はアルファベット $\Sigma\supseteq\{a,b,c\}$、ランク $\ge2$ の条件付きである。

### 1.3 前回までの報告と原稿の点検

- 二文字核報告の補題2.1・系2.2・系2.3・補題3.1、二文字 II 報告の補題A・補題B・定理C を、三文字への移植に使う部分について一行ずつ確かめた。数学的な誤りは見つからなかった。
- **小さな不正確さ（誤りではない）**：二文字 II 報告 §8 は「三文字では二つの $y$ 塊の間に $c$ が挟まり得るので、合流が起きない配置がある」と書くが、正確には**合流は三文字でも必ず起きる**（補題3.4）。失われるのは「合流した隙間が言語で禁止される」という矛盾の側である（§4）。
- **原稿 `lem:power-transfer` は鋭くない（誤りではない）**：証明の共通文脈 $p'u\square_1u\square_2q'$ の左の $u$ は不要で、$p'\square_1u\square_2q'$ でも $E[\mathbf x]=E[\mathbf y]=p'u^{a+d+b+1}q'$ になる。従って仮定は因子 $u^{a+d+b+1}$ で足りる（内容型付けでは $u^4$）。結論は変わらない。
- ChatGPT 肯定報告 §5「侵入した禁止文字を交換・削除する操作はより難しくなる」は、**成分の和に入る文字で4乗を持つもの**については逆に易しくなる（補題5.1の修復）。難しいのは和に入らない文字だけ、という形に精密化できる。

---

## 2. Q0：$K_n$ はファンアウト2で代入可能か

### 命題2.1【証明済み】

$\Sigma\supseteq\{a,b,c\}$、$n\ge3$ なら $K_n\notin\mathcal C_{2,c_\Sigma}$。$n=1,2$ なら $K_n\in\mathcal C_{2,c_\Sigma}$。

**証明（$n\ge3$）。** $V_1=baab$、$V_2=b\,V_1V_1\,b$ なので、$V_n=b^{n-2}V_2\cdots$ は $b^n\,aab\cdots$ で始まり、最も左の $V_2$ は位置 $n-2$ から始まって、その二つの $V_1=baab$ は位置 $n-1$ と $n+3$ にある。

$$
\mathbf x:=(b,\ baab),\qquad \mathbf y:=(bb,\ aab).
$$

成分の内容はともに $(\{b\},\{a,b\})$。

- **共通の文脈** $E:=b^{n-3}\,\square_1\,b\,\square_2\,V_n[n{+}3:]$（許容：穴の間は $b\ne\varepsilon$）。$E[\mathbf x]=b^{n-3}\cdot b\cdot b\cdot baab\cdot V_n[n{+}3:]=b^naab\cdots=V_n$、$E[\mathbf y]=b^{n-3}\cdot bb\cdot b\cdot aab\cdot V_n[n{+}3:]=V_n$。よって $(2,c)$-代入可能なら $\mathcal D^{(2)}(\mathbf x)=\mathcal D^{(2)}(\mathbf y)$。
- **食い違う文脈** $F:=\square_1\,V_n[1{:}n{+}3]\,\square_2\,V_n[n{+}7:]$（穴の間は空でない）。第一の穴は $V_n$ の最初の $b$、第二の穴は位置 $n+3$ の $baab$ なので $F[\mathbf x]=V_n\in K_n$。
- $F[\mathbf y]=bb\,V_n[1{:}n{+}3]\,aab\,V_n[n{+}7:]$ は $c$ を含まず、長さは $\lvert V_n\rvert$ で、$b^{n+1}a$ で始まる。$V_n$ は $b^na$ で始まるので $F[\mathbf y]\ne V_n$。$c$ を含まない $K_n$ の語は $V_n$ だけなので $F[\mathbf y]\notin K_n$。□

$n=1,2$ は有限言語の全数検査（arity 1 と 2、全ての組と全ての観察された文脈。有限言語では分布は観察された文脈の集合に等しいので、これは証明）で違反が無い（§10 Part 1）。$n=3$ の全数検査が最初に見つける違反も上と同じ組 $\mathbf x,\mathbf y$ である。

**機構。** これは補題3.5（共役移送）の $t=t'=b$、$v=b$ の場合で、`thm:doubling-no-lift` の冪の移行と同じ系統（二つの穴の間で周期 $b$ を一つずらす）である。違いは、内容型付けが冪等（$c(b)=c(bb)$）で、第二の成分が純である必要もない（$c(baab)=c(aab)$）ため、必要な因子が $u^5$ ではなく「$b^3$ の後に $b$ を含む語」で足りることにある。`thm:doubling-no-lift` をそのまま $K_n$ に当てはめると（$u=b$、指数と周期が1）$n\ge5$ でしか排除できないが、実際には $n\ge3$ で排除される。

**結論**：$K_n$ はファンアウト2の否定の答えを与えない。ファンアウト1の指数下界は $K_n$ による（§1.2）ので、`op:fanout-two` の三文字の段は、$K_n$ と別の族を探すか、肯定を証明するかのどちらかになる。

---

## 3. 一般の道具（任意の $\Sigma$）

この節の $L\in\mathcal C_{2,c_\Sigma}$ は任意、$\Sigma$ も任意の有限アルファベット。

### 補題3.1（$x$ 塊の再配分）【証明済み】

$x^4$ が現れれば、$w\in L$ かどうかは $(\sigma_x(w),\lvert w\rvert_x)$ だけで決まる。

**証明。** 二文字核報告の補題2.1と同じ。$pa^4q$ を $px^4q$、比べる組を $(x,xx)$ と $(xx,x)$（内容 $(\{x\},\{x\})$）、共通の許容文脈を $p\square_1x\square_2q$ にする。二つの $x$ 塊の間の $x$ 隙間は空でないので、塊から塊へ一文字ずつ移せる。第三の文字は使わない。□

### 系3.2（ブロックの交換と $x$ の個数の漏れ）【証明済み】

$x^4$ が現れるとする。

(i) ある語が因子 $xx\,z\,x$ または $x\,z\,xx$（$z$ は $x$ 隙間）を持てば $\mathcal D^{(1)}_L(xz)=\mathcal D^{(1)}_L(zx)$。特に $z$ が一文字 $y$ なら $xy$ と $yx$ は全ての文脈で交換できる。
(ii) $\mathcal D^{(1)}_L(xy)\ne\mathcal D^{(1)}_L(yx)$ なら、因子 $x\,y\,x$（隙間がちょうど $y$）を持つ語は $x$ の余りを持たない。
(iii) ある $x$ 骨格について $x$ の個数が $t$ と $t+\delta$（$\delta\ge1$）の二語が $L$ にあれば $\mathcal D^{(1)}_L(x)=\mathcal D^{(1)}_L(x^{1+\delta})$。

**証明。** (i) $UxxzxV\in L$ なら補題3.1で $UxzxxV\in L$。文脈 $(Ux,xV)$ は $xz$ と $zx$（内容は同じ）をともに受理する。(ii) 余りがあれば補題3.1で隙間 $y$ の左の塊を長さ $\ge2$ にでき、(i) が使える。(iii) 二文字核報告の系2.3の証明そのまま。□

### 補題3.3（境界の交換 A′）【証明済み】

$x^4$ が現れ、ある語が因子 $x\,z\,x^{j+1}$（$j\ge1$、$z$ は $x$ 隙間）を持てば $\mathcal D^{(1)}_L(xzx^j)=\mathcal D^{(1)}_L(x^{j+1}z)$。鏡像も同様。

**証明。** 二文字 II 報告の補題A の $b^e$ を任意の $x$ 隙間 $z$ に替えるだけ。$W=Uxzx^{j+1}V'$、文脈 $(U,xV')$ で $E[x^{j+1}z]=Ux^{j+1}zxV'$ は $W$ と同じ $x$ 骨格（$z$ の両隣は $x$）と同じ個数を持つ。内容 $c(xzx^j)=c(x^{j+1}z)$。□

### 補題3.4（隙間の合流）【証明済み・新】

$x^4$ が現れるとする。$w\in L$ が $x$ の余りを持ち、$x$ 骨格で $\cdots x\,z\,R\,z'\cdots$（$R$ は内部の $x$ 塊、$z,z'$ はその両側の $x$ 隙間、$R$ の左に別の $x$ 塊 $A_0$ がある）と書けるとする。このとき、$R$ を消して $z$ と $z'$ を一つの隙間 $zz'$ につなぎ、$R$ の $x$ を他の塊に移した語（同じ $x$ の個数、塊の長さは任意の正の配分）も $L$ に入る。鏡像（$R$ の右に別の塊がある場合）も同様。

**証明。** 補題3.1により、$R$ の長さが2で $A_0$ が長さ $\ge1$ の語 $W_2=Pxz\,xx\,Q$（$Px$ は $A_0$ の終わりまで）と、$R$ の長さが1の語 $W_1=P'x\,z\,x\,z'V'$ がともに $L$ に入る（$w$ に余りがあるので個数が足りる）。$W_2$ は因子 $xzxx$ を持つので補題3.3（$j=1$）で $\mathcal D(xzx)=\mathcal D(xxz)$。文脈 $(P',z'V')$ は $xzx$ を受理する（$W_1$）ので $P'xx\,zz'\,V'\in L$。これは $R$ を消し、$A_0$ を一つ伸ばし、隙間を $zz'$ につないだ語で、$x$ の個数は同じ。残りは補題3.1。□

この補題は余りを保つ（塊の数が減るので）ので、繰り返し使える。**どの内部の塊も、ほかに塊が一つ残る限り消せる。**

### 補題3.5（共役移送）【証明済み・新】

$x,y\in\Sigma^+$、$p\in\Sigma^+$、$q\in\Sigma^*$、$k\ge0$ とし、$t:=pq$、$t':=qp$、$v:=(pq)^kp$ とする。$c(t)\subseteq c(x)\cap c(y)$ で、$L$ のある語が因子 $x\,v\,t'\,y$ を持てば、全ての $w_{\rm L},w_{\rm R}\in\Sigma^*$、$w_{\rm M}\in\Sigma^+$ について

$$
w_{\rm L}\,x\,w_{\rm M}\,t'y\,w_{\rm R}\in L\iff w_{\rm L}\,xt\,w_{\rm M}\,y\,w_{\rm R}\in L.
$$

**証明。** $vt'=(pq)^{k+1}p=tv$ なので $xvt'y=xtvy$。組 $(x,t'y)$ と $(xt,y)$ は内容が等しく（$c(t)=c(t')\subseteq c(x)\cap c(y)$）、その語の位置で共通の許容文脈 $v_0\square_1v\square_2v_2$（$v\ne\varepsilon$）を持つ。□

特別な場合：$u^4$ が現れれば $(u,u^2)\equiv(u^2,u)$（$x=y=v=t=u$）。これは `lem:power-transfer` の内容型付け版で、因子は $u^4$ で足りる。§2 の $K_n$ の違反は $x=t=v=b$、$y=aab$ の場合である。§7 で反例の設計の制約として使う。

---

## 4. Q1：一文字の純な型への二文字の道具の移り方

| 二文字の道具 | 三文字（一般の $\Sigma$）での状態 | 根拠 |
|---|---|---|
| 二文字核 補題2.1（再配分） | **そのまま移る**（$x^4$ があれば $x$ について） | 補題3.1 |
| 二文字核 系2.2(i)（$aaba$ ⇒ 飽和） | 組 $\{x,y\}$ ごとの交換に**弱まる**。三組全てで起きて初めて Parikh 飽和（ChatGPT 肯定報告 補題5.2） | 系3.2(i) |
| 二文字核 系2.2(ii) | 「$xyx$ を持つ語は余りを持たない」として移る（$\{x,y\}$ が交換しないとき） | 系3.2(ii) |
| 二文字核 系2.3（個数の漏れ） | **そのまま移る** | 系3.2(iii) |
| 二文字 II 補題A（境界の交換） | **一般化して移る**（$b^e$ を任意の $x$ 隙間に） | 補題3.3 |
| 二文字 II 補題B（内部の $b$ 塊は一つ） | **移らない**（命題4.1）。証明の前半（合流）は移り（補題3.4）、最後の矛盾だけが失われる。隙間が純な $y$ 塊の場合だけ残る（補題4.2） | §4 |
| 二文字核 補題3.1（挿入補題） | **移る**。印は各成分の最初と最後の2文字と、$S_i$ の各文字を一つずつ（$\le4+m$）。異なる節点の挿入は、成分の文字で隔てられた別の「外来の塊」になる | 定理5.2の証明 |
| 二文字 II 定理C（場合 II の線形上界） | 定理G の特別な場合として再現（系5.4）。三文字の一文字の和の型には補題B が無いので直接は移らない | 系5.4、§6.3 |
| 二文字 II 定理D（$P_a(C)$ の直接の上界） | 段 (3) が補題B を使うので**移らない**。代わりに剛性補題6.3が得られる | 補題6.3 |

### 命題4.1（三文字で補題B が成り立たない例）【証明済み】

$L_\circ:=(a\mid bc)^+\subseteq\{a,b,c\}^+$ は、全ての $f\ge1$ と全ての型付け $s$ について $(f,s)$-組代入可能で（従って $L_\circ\in\mathcal C_{f,s}$）、次を満たす：$a^4$ と $aa$ が現れる。$b^2,c^2$ は現れない（特に $b^4,c^4$ も）。Parikh 飽和でない（$abc\in L_\circ$、$acb\notin L_\circ$）。$ba$ と $ac$ は現れないので、$\{a,b\}$・$\{a,c\}$ のどちらの組も交換しない。それなのに、$aa$ を含み内部の非 $a$ 隙間を $N$ 個持つ語 $aa(bca)^N$ が全ての $N$ について $L_\circ$ にある。

**証明。** $w\in L_\circ$ $\iff$ $w\ne\varepsilon$、$w$ は $c$ で始まらず $b$ で終わらず、因子 $ba,bb,ac,cc$ を持たない（$\Rightarrow$ は明らか。$\Leftarrow$：各 $b$ の次は $c$、各 $c$ の前は $b$ なので $(a\mid bc)$ に一意に区切れる）。

$\mathbf x,\mathbf y\in(\Sigma^+)^d$ が許容文脈 $E=v_0\square_1v_1\cdots\square_dv_d$ をともに受理するとする。各 $i$ について、$x_i,y_i$ は $L_\circ$ の語の因子なので禁止因子を持たない。また「$x_i$ が $c$ で始まる」は、$v_{i-1}\ne\varepsilon$ なら「$v_{i-1}$ の最後の文字が $b$」と同値（$L_\circ$ では $b$ の次は必ず $c$、$c$ の前は必ず $b$）、$v_{i-1}=\varepsilon$（$i=1$ のみ）なら偽。$y_i$ も同じなので、$x_i$ と $y_i$ は「$c$ で始まるか」が一致する。同様に「$b$ で終わるか」も一致する。

任意の許容文脈 $F$ について、$F[\mathbf x]\in L_\circ$ は、$F$ の各部分と各成分の内部に禁止因子が無いこと、各つなぎ目の二文字が禁止されないこと、最初と最後の文字の条件で決まる。左のつなぎ目（$F$ の文字 $\ell$、成分の最初の文字 $f$）が禁止される $\iff$ $[\ell=b]\ne[f=c]$、右のつなぎ目（成分の最後の文字 $g$、$F$ の次の文字 $n$）が禁止される $\iff$ $[g=b]\ne[n=c]$。どちらも成分については「$c$ で始まるか」「$b$ で終わるか」だけに依存するので、$F[\mathbf x]\in L_\circ\iff F[\mathbf y]\in L_\circ$。型付けは使っていない。$L_\circ$ は正則なので $f$-MCFL。□

長さ $\le11$ の観察（§10 Part 2）でも arity 1・2 の違反は無い。$L_\circ$ では、補題3.4が強制する合流 $a\,bc\,a\,bc\,a\to aa\,bcbc\,a$ は言語に入っており、矛盾が生じない。

### 補題4.2（隙間が純な $y$ 塊の場合の補題B）【証明済み】

$x^4$ が現れ、$y^4$ が現れず、$\mathcal D^{(1)}_L(xy)\ne\mathcal D^{(1)}_L(yx)$ とする。$x$ の余りを持つ $w\in L$ は、「どちらも純な $y$ 塊である、隣り合う二つの内部の $x$ 隙間」を持たない。

**証明。** 隙間 $y^e$、$y^{e'}$ が隣り合えば、系3.2(ii) により $e,e'\ge2$。補題3.4で合流させると $y^{e+e'}$（$\ge y^4$）を持つ語が $L$ に入る。□

**補題B の最後の矛盾はどう変わるか**（依頼 Q1 の問い）：二文字では、二つの $b$ 塊の合流が必ず $b^4$ を作った（隙間は $b$ だけからなり、系2.2(ii) で長さ $\ge2$）。三文字では隙間が $\{b,c\}$ 上の語になり、合流した隙間 $zz'$ が言語に許される場合があり、そのとき矛盾は生じない（$L_\circ$）。矛盾が残るのは、合流した隙間が言語の何らかの禁止に触れる場合だけで、その最も単純な形が補題4.2である。

---

## 5. Q2：全体短縮と修復

二文字の証明は「独立な短縮を二つ同時に行うと矛盾」という形だった。三文字ではこれが成り立たない（命題4.1）ので、考え方を逆にする：**印の無い重い部分木を全て一度に短縮し、入ってしまった他の文字を言語の側で修復する。** 修復できない文字の挿入だけを、二文字のような重複度の議論で数える。

### 5.1 修復補題

#### 補題5.1（修復）【証明済み・新】

$X=A_{\mathbf S}$、$W=E_A[\mathbf u']\in L$（$u'_i\in\Sigma^+$）、$x\in\Sigma$ とし、次を仮定する。

1. $x^4$ が現れる。
2. $W$ は $x$ の余りを持つ。
3. ある成分 $u'_j$ が $x$ を含み $x\in S_j$。
4. $x\notin S_i$ の成分 $u'_i$ の中の $x$（**外来の $x$**）は、$u'_i$ の最初と最後の文字ではない。

このとき、外来の $x$ を全て消し、同じ数の $x$ を $u'_j$ の中の $x$ の隣に足した組 $\mathbf u''$ について $E_A[\mathbf u'']\in L$。$\lVert\mathbf u''\rVert_1=\lVert\mathbf u'\rVert_1$。

**証明。** 仮定4により外来の $x$ の塊は全て $W$ の内部の塊である（両隣は $u'_i$ の文字で $x$ ではない）。仮定3により $W$ には外来でない $x$ の塊が少なくとも一つある。外来の塊を一つずつ、$x$ 塊の並びで隣にある塊へ補題3.4（左に塊があれば本体、無ければ鏡像）で合流させて消す。各段で余りは保たれる（仮定2と補題3.4の後の注意）。外来の塊が無くなった語 $W'$ は、$W$ から外来の塊を消して隙間をつないだ $x$ 骨格と、$\lvert W\rvert_x$ 個の $x$ を持つ。$E_A[\mathbf u'']$ も同じ骨格（$u'_j$ の $x$ の隣に足しても骨格は変わらない）と同じ個数を持つので、補題3.1により $L$ に入る。□

**この補題が意味すること**：成分の和に入る文字で、4乗が現れ、余りがあるものは、成分の中に勝手に入っても、それを許す成分へ移すことで**修復できる**。修復できないのは、(i) 成分の和に入らない文字（**除外文字**、$\Sigma\setminus U(X)$）、(ii) 4乗が現れない文字、(iii) 余りが無い文字、のどれかである。

### 5.2 定理G

**定義。** $X=A_{\mathbf S}$ と、$X$ の生成組 $\mathbf u\in L_X$ を固定する。文字 $x$ が $(X,\mathbf u)$ について**修復可能**とは、(a) $x\in U(X)$、(b) $x^4$ が現れる、(c) $E_A[\mathbf u]$ が因子 $xx$ を持ち、その二文字はどちらも $E_A$ の固定部分か $x$ を許す成分（$x\in S_j$）の中にある、の全てを満たすこと。**悪い文字**の集合を

$$
\mathrm{Bad}(X,\mathbf u):=\{x\in\Sigma:\ \text{ある } i \text{ で } x\notin S_i\}\setminus\{\text{修復可能な文字}\}
$$

とする。除外文字 $\Sigma\setminus U(X)$ は常に悪い。

**定義（重複度）。** 空でない $S\subseteq\Sigma$ と $B\subseteq\Sigma\setminus S$ について、$\kappa_S^B(L)$ を次の最大の $k$ とする（無ければ0、上限が無ければ $\infty$）：$L$ のある語が因子 $P\,z\,Q$（$P,Q\in S^2$、$z\in\Sigma^+$）を持ち、$z$ の極大な $(\Sigma\setminus S)$-因子のうち $B$ の文字を含むものが $k$ 個以上ある。

#### 定理5.2（全体短縮と修復）【証明済み】

$\Sigma$ を任意、$m:=|\Sigma|$、$P_m:=(2^m-1)^2$ とする。$X=A_{\mathbf S}$、$\mathbf u\in L_X$ を $X$ の導出 $T$（$\widetilde G_0$ の型付き導出で、一つのパス上で型付きラベルが繰り返さないもの）の生成組とし、$k:=\max_i\kappa_{S_i}^{\mathrm{Bad}(X,\mathbf u)\setminus S_i}(L)$ とする。このとき

$$
\tau_X\le(r+1)\,P_m\,v\,\theta\,(12+4m+10k).
$$

三文字（$m=3$）では $\tau_X\le49(r+1)v\theta(24+10k)$。

**証明。**
(0) **パス**：型付きラベル（非終端と成分の内容の組）は $\le P_mv$ 個。任意の生成組の導出から、繰り返すラベルの上を下に差し替える操作を繰り返せば繰り返しの無い導出が得られる（型は準同型で合成されるので、差し替えても $L_X$ に入る）ので、この仮定で一般性を失わない。パスの節点数は $\le P_mv$。

(1) **印**：各成分 $u_i$ の最初と最後の $\min\{2,|u_i|\}$ 文字、$S_i$ の各文字の出現を一つずつ、さらに各修復可能な文字 $x$ について (c) の $xx$ が成分の中にあればその二文字。印は $M\le2(4+m)+2m=8+4m$ 個。生成組が印を含む節点を**印付き**、総長 $>\theta$ の節点を**重い**と呼ぶ。印の無い節点の生成組の成分は、それぞれある $u_i$ の印の無い位置の区間（**ブロック**）に入る。

(2) **詰まる節点**：印の無い重い節点 $h$（非終端 $B_h$）で、$h$ の部分木だけを $\omega_{B_h}$ の導出に差し替えた組 $\mathbf u^h$ について、ある成分 $u^h_i$ が $\mathrm{Bad}(X,\mathbf u)\setminus S_i$ の文字を含むものを**詰まる**と呼ぶ。

(3) **短縮**：根から下へ、次の規則で残す節点を決める。印付きの節点は残す。残した節点の子 $h$ が印を持たなければ：軽いなら部分木をそのまま使う（生成組 $\le\theta$）。重く詰まらないなら $\omega_{B_h}$ の導出に差し替える（$\le\theta$）。重く詰まるなら $h$ を残し、その子に同じ規則を適用する。得られる組 $\mathbf u^{(1)}$ は $G$ の導出の生成組なので $\mathbf u^{(1)}\in L_A(G)$、$E_A[\mathbf u^{(1)}]\in L$。

(4) **内容の確認**：$\mathbf u^{(1)}$ の各成分は印の文字（$S_i$ の全ての文字、最初と最後の文字）を保つ。差し替えた節点は詰まらないので、各ブロックに入る文字は $S_i$ の文字か修復可能な文字だけ（ブロックの中身は単独の差し替えと同じ）。そのまま使った軽い部分木と残した節点が書く文字は元の成分の文字。従って外来の文字は全て修復可能で、成分の最初と最後の文字ではない（印）。

(5) **修復**：外来の文字が入っている修復可能な文字 $x$ ごとに補題5.1を適用する。仮定1は (b)、仮定3は (a) と印（$x\in S_j$ の成分には $x$ の出現が印として残る）、仮定4は (4)、仮定2は (c)（$E_A$ の固定部分は変わらず、成分の中の $xx$ は印として残る）による。一つの文字の修復は他の文字の位置関係を変えない（$x$ を消して隙間をつなぐだけ）ので、文字ごとに順に行える。結果の $\mathbf u''$ は $c(u''_i)=S_i$、$E_A[\mathbf u'']\in L$、$\lVert\mathbf u''\rVert_1=\lVert\mathbf u^{(1)}\rVert_1$。(1.1) により $\tau_X\le\lVert\mathbf u^{(1)}\rVert_1$。

(6) **詰まる節点の反鎖**：残した詰まる節点のうち同じ深さのもの $Q$ は反鎖である。各 $h$ のブロックは $\le2$ 個で、間に文字なしで隣り合うブロックの持ち主を辺で結ぶと最大次数 $\le4$ なので、$|I|\ge|Q|/5$ の独立集合 $I$ がある。**元の** $\mathbf u$ で $I$ の部分木を同時に $\omega$ に差し替えた $\mathbf u^I$ は $E_A[\mathbf u^I]\in L$ を満たし、各 $h\in I$ はある成分 $i$ に $\mathrm{Bad}\setminus S_i$ の文字を入れる（ブロックの中身は単独と同じ）。$I$ のブロックどうしは隣接しないので、二つの $I$ のブロックの間には元の成分の文字（$S_i$ の文字）が少なくとも一つ残る。従って成分 $i$ に悪い文字を入れる $h$ の数を $|I_i|$ とすれば、成分 $u^I_i=P\,z\,Q$（$P,Q$ は最初と最後の2文字で $S_i^2$ の元）の $z$ は、悪い文字を含む極大な $(\Sigma\setminus S_i)$-因子を $|I_i|$ 個以上持つ。よって $|I_i|\le k$、$|I|\le2k$、$|Q|\le10k+4$。

(7) **数え上げ**：印付きの節点は印へのパスの上にあり $\le MP_mv$ 個。残した詰まる節点は重く、各深さに $\le10k+4$ 個、深さは $\le P_mv$ なので $\le(10k+4)P_mv$ 個。$\mathbf u^{(1)}$ の各文字は、残した節点が直接書く（各 $\le\theta$）か、残した節点の残さなかった子（$\le r$ 個、各 $\le\theta$）に属する。よって

$$
\lVert\mathbf u^{(1)}\rVert_1\le(r+1)\theta\,P_mv\,(M+10k+4)\le(r+1)P_mv\theta(12+4m+10k).\qquad\square
$$

**注意**：この証明は $\mathbf u$ の長さの最小性を使わない（使うのはパス上のラベルの非反復だけ）。代入可能性を使うのは補題5.1（補題3.1・3.4を通して arity 1 と 2）だけで、$k$ の定義は言語の性質である。

#### 系5.3（悪い文字の無い型）【証明済み】

$U(X)=\Sigma$ で、$X$ のどれかの成分に入らない全ての文字 $x$ について $x^4$ が現れ、$E_A$ の固定部分が $xx$ を含むなら（または (c) を満たす $\mathbf u$ を持つ繰り返しの無い導出があれば）、$\mathrm{Bad}=\varnothing$、$k=0$ で

$$
\tau_X\le(r+1)P_mv\theta(12+4m),\qquad m=3\text{ で }\tau_X\le1176(r+1)v\theta .
$$

成分が全て $\Sigma$ の型（外来の文字が無い）は無条件にこの上界を持つ（ChatGPT 肯定報告 定理5.1の注意の場合）。ChatGPT 肯定報告 定理5.1（成分の和が $\Sigma$ の型に Parikh 飽和の下で $O(v\theta^3)$）とは仮定が補い合う：あちらは飽和、こちらは4乗と余り。

#### 系5.4（二文字の場合 II の再現）【証明済み】

$\Sigma=\{a,b\}$、$a^4$ が現れ $b^4$ が現れず非飽和（二文字 II 報告の場合 II）なら、全ての $X$ について $\tau_X\le9(r+1)v\theta\cdot30=270(r+1)v\theta$。

**証明。** $b$ は (b) を満たさないので、外来になりうるときは常に悪い。$a$ は悪い場合もある。成分 $\{b\}$ は長さ $\le3$（$b^4$ が無い）なので全ての位置が印で、挿入は起きない。成分 $\{a,b\}$ には外来の文字が無い。成分 $\{a\}$ に悪い文字 $b$ が入る窓 $P\,z\,Q$（$P,Q=aa$）で悪い塊が2個以上なら、その語は $aa$ と二つの内部の $b$ 塊を持ち、二文字 II 報告の補題B に反する。よって $k\le1$、$m=2$ で $(r+1)\cdot9v\theta(12+8+10)$。□

定数は二文字 II 報告の $117$ より悪いが、同じ結論が定理G の枠組みから出る。

### 5.3 一文字の和と、除外文字を含まない因子

#### 補題5.5（一文字の成分の重複度）【証明済み】

$y\in\Sigma$、$B\subseteq\Sigma\setminus\{y\}$ とし、$y^4$ が現れるとする。

$$
\kappa_{\{y\}}^B(L)\le\iota_y^B(L):=\sup\{\lvert z\rvert_B:\ z\ \text{は}\ y\ \text{隙間},\ L\ \text{のある語が因子}\ yzy\ \text{を持つ}\}.
$$

**証明。** 窓 $yy\,z\,yy$ の $z$ が、$B$ を含む極大な $y$ 隙間を $k$ 個持つとする。その語は余りを持つ（$yy$）。$z$ の中の $y$ 塊は全て内部で、左に $P$ の塊があるので、補題3.4で $z$ の隙間を全て一つに合流できる。合流した隙間 $Z$ は $L$ の語の因子 $yZy$ になり、$\lvert Z\rvert_B\ge k$。□

従って一文字の和の型（$\{y\}$、$(\{y\},\{y\})$）では、定理5.2の $k$ は「$y$ に挟まれた $y$ を含まない因子に入る悪い文字の数」で抑えられる。$L_\circ$（命題4.1）ではこれが無界である。

#### 命題5.6（除外文字を含まない因子が短い場合）【証明済み】

$X=A_{\mathbf S}$、$D:=\Sigma\setminus U(X)\ne\varnothing$（除外文字）とし、$\mathrm{Bad}(X,\mathbf u)=D$（成分の和に入る外来の文字は全て修復可能）と仮定する。さらに、$D$ の文字を含む $L$ の語の、$D$ を含まない因子の長さが全て $\le\ell$ だとする。このとき

$$
\tau_X\le\max\bigl\{6\ell,\ (r+1)P_mv\theta(9+4m)\bigr\},\qquad m=3\text{ で }\max\{6\ell,\ 1029(r+1)v\theta\}.
$$

**証明。** $W:=E_A[\mathbf u]$。

- $E_A$ の固定部分が $D$ の文字を含むなら、各成分 $u_i$（内容 $\subseteq U(X)$）は $W$ の $D$ を含まない因子なので $\lVert\mathbf u\rVert_1\le2\ell$。
- そうでなく $\lvert W\rvert\le6\ell$ なら $\tau_X\le\lVert\mathbf u\rVert_1\le6\ell$。
- 残りは $W$ が $D$ を含まず $\lvert W\rvert>6\ell$ の場合。詰まる節点 $h$ について、$W^h:=E_A[\mathbf u^h]$ は $D$ の文字を含み、それは $h$ のブロックの中にある。$W^h$ の最も左と最も右の $D$ の文字の外側、および（$h$ の二つのブロックがともに $D$ の文字を含むとき）二つのブロックの間は、$D$ を含まない因子なので各 $\le\ell$。$h$ のブロックの外の $W$ の文字はこのどれかに入るので $\le3\ell$。二つの比較できない詰まる節点はブロックが交わらないので $\lvert W\rvert\le6\ell$ となり矛盾。従って詰まる節点は全て比較可能（一本の鎖）で、$\le P_mv$ 個。定理5.2の (3)–(5)、(7) と同じ数え上げで $\lVert\mathbf u^{(1)}\rVert_1\le(r+1)\theta P_mv(M+1)$。□

これは依頼 Q2(c) の最初の条件付き定理の、証明できた形である。$\ell$ は言語の量で、$\ell$ が $g,\theta$ の多項式なら $\tau_X$ も多項式。$K_n$ では $cV_{n-1}c\in K_n$ なので $\ell\ge3\cdot2^{n-1}-2$ で、条件は満たされない（$K_n$ はそもそも $\mathcal C_{2,c}$ に入らないが、設計の目安として）。

#### 系5.7（条件付きの特徴標本）【証明済み】

全ての型付き非終端 $X$ について定理5.2の $k$ が $\le k_0$（または命題5.6の仮定が $\ell\le\ell_0$ で）成り立つなら、(1.2) により $\mathcal B^{\le r}_{2,c}$ と $\mathcal B_{2,c}$ に共通の特徴標本 $K$ で

$$
\lVert K\rVert_+\le8^{2r}g\bigl(1+2\theta+49r(r+1)v\theta(24+10k_0)\bigr)+\mathbf 1_{\{\varepsilon\in L\}}
$$

（命題5.6の場合は $49r(r+1)v\theta(24+10k_0)$ を $r\max\{6\ell_0,1029(r+1)v\theta\}$ に替える）のものがある。定数は $r$ と $k_0$（または $\ell_0$）だけに依存する。

---

## 6. Q2 の (a)(b) と、純な穴の剛性

### 6.1 (a) 内容 $\{a,b\}$ の成分を二文字の言語として扱う帰着

**命題6.1（切片の代入可能性）【証明済み】** 一穴文脈 $E=(U,V)$ について $L_E:=\{y\in\{a,b\}^+:UyV\in L\}$ は、$\{a,b\}$ の内容型付けについて $(2,c_{\{a,b\}})$-組代入可能である。

**証明。** $L_E$ の許容文脈 $F$ に $E$ を合成した $E\circ F$ は $L$ の許容文脈（内側の区切りは $F$ のまま空でない）。$\mathbf x,\mathbf y$ が $L_E$ で文脈を共有すれば $L$ でも共有し、$L$ での分布が等しいので、$E\circ F'$ の形の文脈についても等しい。□

$\tau_{A_{(\{a,b\})}}$ は $L_{E_A}$ の内容 $\{a,b\}$ の最短語の長さなので、二文字 II 報告の定理E を $L_{E_A}$ に使えば、と考えられる。**しかし使えない**：$L_{E_A}$ の表示（$G$ と $U,V$ を読む有限オートマトンの積から作る）の大きさは多項式だが、その $\bar\theta$ は、$c$ を含まない文の最短長で決まり、制御できない。$K_n$ の切片 $L_{(\varepsilon,\varepsilon)}=\{V_n\}$ の表示は $\bar\theta\ge3\cdot2^n-2$ を持つ。稀な型の問題は、切片では $\bar\theta$ の問題に移るだけである。

Astra の族 $P_{N,2}=\{(ab)^N,cabab,abcab,ababc\}$（`astra_s2_shortcontext` 命題5.1）は $\mathcal C_{2,c}$ に入る（S2 型付けで代入可能なので `lem:typing-monotone` の前の (a)。$N\le5$ の全数検査でも違反なし、§10 Part 3）。$abcab$ から $c$ を消した $abab$ は $N\ne2$ で $L$ に無い：**除外文字 $c$ の削除による修復は、内容型付けでも一般には不可能**。ただしこの族は $\theta\ge2N$ なので多項式上界への反例ではない（Astra 系6.3）。

### 6.2 (b) 文字の組ごとの場合分け

系3.2(i) により、$x^4$ があり $xxyx$ か $xyxx$ が現れれば $xy\equiv yx$（全ての文脈）。三組全てでこれが起きれば Parikh 飽和（ChatGPT 肯定報告 補題5.2）で、成分の和が $\Sigma$ の型は定理5.1により $O(v\theta^3)$。飽和の下でも、成分の和が真部分集合の型（例：$(\{a,b\})$）は「Parikh 像の二次元の切片の最小点」の問題になり、二文字の補題3.2（一次元の行剛性）の二次元版が要る。これは**未解決**で、ここでは扱わなかった。

一つの組 $\{a,b\}$ だけが交換する場合（$ab\equiv ba$）、$L$ は $c$ を含む文脈の中でも $a,b$ の隣接交換に閉じ、$c$ 隙間の中の $\{a,b\}$ 語は Parikh ベクトルだけで決まる。しかしこれは除外文字 $c$ を消す手段を与えない（交換は $c$ の位置を動かさない）。

### 6.3 純な $y$ の穴の剛性

二文字では、純な $a$ の穴 $P_a(C)$ の上界（二文字 II 報告 定理D）が補題B に依存していた。三文字では代わりに次が言える。

**定義**：一穴文脈 $C$ で $C[y^+]\cap L\ne\varnothing$ のものに $P_y(C):=\min\{k\ge1:C[y^k]\in L\}$。

#### 補題6.3（剛性）【証明済み】

$y^4$ が現れ、$k:=P_y(C)\ge5$ とする。$W:=C[y^k]$ の節点数最小の $G$ の導出を取り、$C$ の固定部分の全ての文字と穴の最初と最後の2文字に印を付ける。印の無い重い節点の集合を $H$ とする。

(i) $h\in H$（非終端 $B$）の生成組は純な $y$ の組で、$\omega_B$ は $y$ 以外の文字を含む。また $B$ の純な $y$ の組の総長は、$h$ の総長 $\ell_h$ に等しいか、$\ell_h+k$ 以上である。

(ii) $H$ の反鎖 $J,J'$ で、ブロックが互いに隣接しないものについて、$J$（$J'$）の部分木を同時に $\omega$ に差し替えた語 $W^J$、$W^{J'}$ の $y$ 骨格が等しければ

$$
\sum_{h\in J}\bigl(\ell_h-\lvert\omega_{B_h}\rvert_y\bigr)=\sum_{h\in J'}\bigl(\ell_h-\lvert\omega_{B_h}\rvert_y\bigr)\quad\text{または両者の差が }k\text{ 以上}.
$$

特に、同じ非終端を持つ $H$ の二つの比較できない節点は同じ総長を持つ。

**証明。** (i) 生成組は穴の中にあり純。$\omega_B$ が純なら差し替えで $C[y^{k'}]$（$1\le k'<k$）となり最小性に反する（$\omega_B$ は重くない）。$B$ の純な組で総長 $\ell'$ のものがあれば差し替えて $C[y^{k-\ell_h+\ell'}]\in L$。$\ell'<\ell_h$ なら最小性に反する。$0<\delta:=\ell'-\ell_h<k$ なら、$W$ とこの語は同じ $y$ 骨格（穴の中の純な部分の長さだけが違う）で個数が $\delta$ 違うので、系3.2(iii) により $\mathcal D(y)=\mathcal D(y^{1+\delta})$、穴の中の $y^{1+\delta}$ を $y$ に替えて $C[y^{k-\delta}]\in L$、矛盾。

(ii) $W^J,W^{J'}\in L$（$G$ の導出）で、$y$ の個数はそれぞれ $\lvert W\rvert_y$ から左辺の和を引いたもの。骨格が等しく個数の差 $\delta$ が $1\le\delta<k$ なら、(i) と同じく系3.2(iii) で矛盾。比較できない同じ $B$ の二節点は $J=\{h\}$、$J'=\{h'\}$ で骨格が等しい（$\omega_B$ が穴の内側の $y$ の間に入る）。□

**意味**：$P_y(C)$ が超多項式な族があれば、最小の導出の印の無い重い節点の非終端 $B$ は、$\omega_B$ の「符号」（差し替えた後の $y$ 骨格に現れる隙間の語）ごとに一定の**重み** $\ell_B-\lvert\omega_B\rvert_y$ を持ち、補題3.4で隙間を合流させた後の長い隙間の語からも、合計の重みが（$k$ 未満の誤差なしに）読み取れなければならない。つまり隙間の語の上に、指数的な重みを持つ**一意に復号できる重み付き符号**が要る。二文字では隙間が $b$ の塊だけなので、この符号が作れない（合流で $b^4$ ができる）ことが補題B だった。

---

## 7. Q3：反例族の設計仕様と、試した候補

### 7.1 必要条件（全て §2–§6 の証明済みの主張から）

$\Sigma=\{a,b,c\}$、固定の $r\ge2$ で、$\lVert G_n\rVert,\bar\theta_{G_n}=n^{O(1)}$ かつ $\tau(G_n,c)=n^{\omega(1)}$ の族 $(L_n,G_n)$ があれば、十分大きな $n$ で、ある型付き非終端 $X_n$ について：

1. **悪い文字がある**（系5.3）：$U(X_n)\ne\Sigma$、または $X_n$ のある成分に入らない和の文字で、4乗が現れないか余りが無いものがある。
2. **重複度が超多項式**（定理5.2）：$\kappa^{\rm Bad}_{S_i}(L_n)\ge\tau_{X_n}/(490(r+1)v\theta)-3$。一つの語の中で、$S_i$ だけの両端を持つ窓の中に、悪い文字を含む外来の塊が超多項式個並ぶ。
3. 成分の和が一文字 $\{y\}$ なら、$y$ に挟まれた $y$ を含まない因子に、悪い文字が超多項式個入る（補題5.5）。
4. **除外文字を含まない長い因子**（命題5.6）：除外文字を含む語の中に、除外文字を含まない長さ $\ge\tau_{X_n}/6$ の因子がある（修復可能な文字だけが外来になる型で）。
5. **剛性**（補題6.3）：一文字の純な穴が長いなら、隙間の語の上の指数的な重み付き符号。
6. **共役移送の回避**（補題3.5）：稀な型の語を一意にする設計で、その語の中に「$x\,v\,t'\,y$、$c(t)\subseteq c(x)\cap c(y)$」の因子と、同じ $t'y$ の別の出現があると、長さを保った別の語が強制される。$K_n$ はこれで $n=3$ から落ちる（§2）。倍増の二つの部分木 $V\,V$ や $V\,m\,V$ は、その左右に $V$ の文字を全て含む語があると $t=V$（または $Vm$）として移送の対象になる。従って「同じ部分木の対が、両側を全ての文字を含む語で挟まれる」配置は、稀な型の語が一つしか無い設計では使えない。
7. 過去の失敗（括弧付き倍増族、Thue–Morse、単一の繊維、並べ替えに閉じた繊維、二文字の場合 II の倍増）は全て 6 の形（または補題3.1・3.4の再配分・合流）の二穴交換で説明できる。

### 7.2 試した候補：重み $2^i$ の符号族（失敗）

条件5を直接満たそうとして、文字 $a$ に重み1、符号 $g_i\in\{b,c\}^+$ に重み $2^i$ を与え、$L_n:=\{w\in(a\mid g_0\mid\cdots\mid g_n)^+:\text{重み}=2^n\}$ とした（内容 $\{a\}$ の語は $a^{2^n}$ だけ。文法 $E_0\to a\mid g_0$、$E_i\to E_{i-1}E_{i-1}\mid g_i$ を閉包に広げたもの）。三つの符号の選び方（$\{bc,bcc,bbc,bbcc\}$ など）で $n=2,3$ の有限言語を全数検査した結果、**全て arity 1 で違反**した（§10 Part 4、具体的な組と文脈はそれ自体が非代入可能性の証明）。例えば $\{bc,bcc,\dots\}$ の $n=2$ では $aabc$ と $abca$ が文脈 $(a,\varepsilon)$ を共有するが、$(\varepsilon,c)$ で $aabcc$（$=aa\cdot bcc$）は入り $abcac$ は入らない。原因は符号の**切れ目**：内容型付けは粗いので、成分が符号の途中で切れているかどうかを型が区別せず、符号の延長（$bc\to bcc$）が一穴の交換で漏れる。重み付き符号を使う反例は、少なくとも「内容が同じ断片が、どの文脈でも同じ切れ目の状態を持つ」符号を要する。そのような符号で指数的な重みと多項式の $\bar\theta$ を両立できるかは**未解決**。

### 7.3 族の満たすべき証明の形

依頼の通り、候補族は $d=1$ と $d=2$ の両方の代入可能性の証明を要する。命題4.1の証明（成分の「境界の状態」だけで所属が決まることを示す）は、局所的な正則言語ではこの形の証明が書けることを示す。重み付きの族では、重みが Parikh ベクトルの線形関数でない限り `prop:abelian-coset-filter` が使えず、境界の状態と重みの両方を成分ごとに追う必要がある。

---

## 8. 三文字の場合の全体の結論と、止まった場所

### 言えたこと

- **Q0**：$K_n\in\mathcal C_{2,c_\Sigma}$ は $n\le2$ のときだけ（命題2.1）。従って $K_n$ はファンアウト1の指数下界（§1.2、$\mathcal B^{\le r}_{1,c}$・$\mathcal B_{1,c}$・クラス全体の集合駆動作用素、$\Sigma\supseteq\{a,b,c\}$、$r\ge2$）を与えるが、ファンアウト2の下界は与えない。
- **肯定の部分結果**（$\mathcal B^{\le r}_{2,c}$ と $\mathcal B_{2,c}$ に共通の特徴標本、(1.2) を通して）：
  - 悪い文字の無い型付き非終端は $\tau_X\le1176(r+1)v\theta$（系5.3）。定数は $r$ にだけ依存。
  - 一般に $\tau_X\le49(r+1)v\theta(24+10k)$、$k$ は悪い文字の挿入の重複度（定理5.2）。$k$ は言語の量で、定数は $r$ と $k$ に依存。
  - 除外文字を含まない因子の長さ $\ell$ による $\tau_X\le\max\{6\ell,1029(r+1)v\theta\}$（命題5.6）。
  - 全ての $X$ で $k\le k_0$ なら特徴標本は $O_{r,k_0}(g^2\theta)$（系5.7）。
- **否定の側の制約**：§7.1 の必要条件。

### 止まった場所（正確に）

$\Sigma=\{a,b,c\}$ の一般の $L\in\mathcal C_{2,c}$ で残るのは、**悪い文字（主に除外文字 $\Sigma\setminus U(X)$）が、一つの成分の窓の中に、印の無い重い部分木の短縮によって多数入る**場合だけである。具体的には：

1. **一文字の和**（$U(X)=\{a\}$ など）：$a$ に挟まれた $a$ を含まない因子に悪い文字が多数入る言語（$L_\circ$ のように）で、かつ $P_a(C)$ が長い場合。補題6.3により、これは隙間の語の上の指数的な重み付き符号を要する。符号が存在しない（従って肯定）ことも、存在する（反例）ことも示せていない。
2. **二文字の和**（$U(X)=\{a,b\}$ など）：除外文字 $c$ が内容 $\{a,b\}$ の成分の中に多数入り、かつ $c$ を含む語の中に $c$ を含まない長い因子がある場合。$c^4$ があり $E_A$ が $c$ の塊を持てば、補題5.1の合流で入った $c$ を全て $E_A$ の $c$ 塊へ押し出せるが、$E_A$ の $c$ の個数がずれ、それを戻す手段（$c$ の個数の漏れ、系3.2(iii)）は一般には無い。Astra の $P_{N,2}$ は、削除による修復が不可能な例が $\mathcal C_{2,c}$ にあることを示す（ただし $\theta$ が大きい）。
3. **成分の和に入るが4乗の無い文字**が外来になる場合（例：$(\{a\},\{b\})$ で $b^4$ が無い）。二文字ではこの場合に補題B が効いたが、三文字では隙間に第三の文字が入りうる。

**依存の注意**：定理5.2・系5.3・命題5.6・補題6.3 は、この報告の §3 の補題（再配分、境界の交換、合流）と `lem:witness-length-template`(i)、`cor:distribution-representatives` だけを使う。ChatGPT 肯定報告の定理には依存しない（比較として言及しただけ）。系5.4は二文字 II 報告の補題B に依存する。

### `op:fanout-two` と S2（手がかり4）との関係

- $c_{\{a,b,c\}}$ の肯定が証明できれば `lem:typing-monotone` により S2 も解けるが、今回はできていない。
- 逆向きの易しさ：S2 の型 1（$c$ を含まない）は内容型 $\{a\},\{b\},\{a,b\}$ の和集合である。代表の類は内容型の類より粗いので、各内容型の $\tau$ の上界はそのまま S2 の型の上界になる（`lem:typing-monotone` の前の (a) により $\mathcal C_{2,S2}\subseteq\mathcal C_{2,c}$）。しかし S2 の困難（型1の稀な語）は、まさに**除外文字 $c$ の消去**（§8 の 1・2）に当たり、内容型付けが細かいことで易しくなる部分は、成分の和に入る文字の修復（補題5.1）だけである。S2 の型1は和が $\{a,b\}$ 以下なので、この易しさは S2 には効かない。

---

## 9. 四文字以上への見通しと文献

**四文字以上**：§3 の補題、補題5.1、定理5.2、補題5.5、命題5.6、補題6.3 は全て任意の $\Sigma$ で成り立つ（定数は $P_m=(2^m-1)^2$、$M\le8+4m$ を通して $m$ に依存し、$8^{2r}$ は $2^{2mr}$ になる）。残る核は同じく「除外文字の消去」だが、成分の和の取り方が $2^m-2$ 通りに増え、隙間に使える文字が増えるので、補題6.3の重み付き符号を作る余地（反例の側）も広がる。$K_n$ 型の倍増族はどの $\Sigma$ でも共役移送で落ちる（命題2.1の証明は $\{a,b,c\}$ の外の文字を使わない）。四文字以上で三文字と本質的に違う現象があるかは調べていない。

**文献**：
- Yoshinaka, *Efficient learning of multiple context-free languages with multidimensional substitutability from positive data*, TCS 412 (2011) 1821–1831：組代入可能性と許容文脈。
- Clark–Eyraud, *Polynomial identification in the limit of substitutable context-free languages*, JMLR 8 (2007)：代入可能性の原型。
- 栗山 `main.tex`、退避 `parked/parked_u1_typing_level.tex`、二文字核報告、二文字 II 報告、ChatGPT 肯定報告、`archive-v1/revision/astra_s2_*`：直接の依存先・比較先。
- 補題3.4（合流）、補題3.5（共役移送）、補題5.1（修復）、定理5.2、命題5.6、補題6.3 と同じ形の結果が文献にあるか：**未確認**（網羅的な文献調査はしていない）。補題3.5は代入可能性の一回の適用で、技法としての新規性は主張しない。

---

## 10. 付録：スクリプト全文と出力

保存名 `ternary_content_check.py`、Windows では `py -3 ternary_content_check.py`。Python 3 の標準ライブラリだけを使う。実行時間は Linux で約3秒。

**何が証明で何が観察か**：`check_finite` は有限言語について、全ての組と全ての観察された文脈を調べる（有限言語では分布は観察された文脈の集合そのもの）ので、「違反なし」はその有限言語についての証明である（Part 1 の $n=1,2$、Part 3）。`check_pred` は述語で与えた無限言語について、長さ上限までの語から文脈を取るので「違反なし」は観察にすぎない（Part 2）。どちらの場合も、報告された違反（共通の文脈と食い違う文脈）はその言語が代入可能でないことの証明である（Part 1 の $n=3$、Part 4）。

```python
# ternary_content_check.py -- Python 3 standard library only.
# Run on Windows with:  py -3 ternary_content_check.py
#
# Finite OBSERVATIONS for reviews/claude_ternary_content_2026-11-01.md.
# Content typing c(w) = set of letters of w; fan-out <= 2 (arity 1 and 2).
#
# check_finite(L): for a FINITE language every distribution is the set of
#   observed contexts, so "no violation" is a proof for that finite language.
# check_pred(member, lmax): for an infinite language given by a predicate,
#   contexts are taken from accepted words of length <= lmax; a reported
#   violation is a genuine proof of non-substitutability (the predicate is
#   exact), while "no violation" is only an observation.
#
# Part 1 (Q0): K_n (E0 -> a, Ei -> b E E b | c E c).
# Part 2: (a|bc)^+ (three-letter failure of the binary "one internal run" lemma).
# Part 3: Astra's P_{N,2} = {(ab)^N, cabab, abcab, ababc} under content typing.
# Part 4: naive "weighted code" candidates for a negative family.

import re
from functools import lru_cache
from itertools import product
from collections import defaultdict


def content(w):
    return frozenset(w)


def occurrences(w, d):
    n = len(w)
    if d == 1:
        for i in range(n):
            for j in range(i + 1, n + 1):
                yield (w[i:j],), (w[:i], w[j:])
    else:
        for i in range(n):
            for i2 in range(i + 1, n):
                for j in range(i2 + 1, n):
                    for j2 in range(j + 1, n + 1):
                        yield (w[i:i2], w[j:j2]), (w[:i], w[i2:j], w[j2:])


def fill(ctx, x):
    if len(x) == 1:
        return ctx[0] + x[0] + ctx[1]
    return ctx[0] + x[0] + ctx[1] + x[1] + ctx[2]


def check_core(words, member, dmax=2):
    for d in range(1, dmax + 1):
        dist = defaultdict(set)
        for w in words:
            for x, ctx in occurrences(w, d):
                dist[x].add(ctx)
        groups = defaultdict(set)
        for x, cs in dist.items():
            t = tuple(content(p) for p in x)
            for c in cs:
                groups[(t, c)].add(x)
        done = set()
        for key, xs in groups.items():
            if len(xs) < 2:
                continue
            xs = sorted(xs)
            a = xs[0]
            for b in xs[1:]:
                if (a, b) in done:
                    continue
                done.add((a, b))
                for p, q in ((a, b), (b, a)):
                    for ctx in sorted(dist[p]):
                        if not member(fill(ctx, q)):
                            return {"arity": d, "accepted": p, "rejected": q,
                                    "common_context": key[1],
                                    "separating_context": ctx,
                                    "word_not_in_L": fill(ctx, q)}
    return None


def check_finite(L, dmax=2):
    S = set(L)
    return check_core(sorted(S), lambda w: w in S, dmax)


def words_upto(n, al):
    for m in range(1, n + 1):
        for t in product(al, repeat=m):
            yield "".join(t)


def check_pred(member, lmax, al="abc", dmax=2):
    return check_core([w for w in words_upto(lmax, al) if member(w)],
                      member, dmax)


# ---------------------------------------------------------------- Part 1
def K(i):
    if i == 0:
        return {"a"}
    P = K(i - 1)
    return {"b" + u + v + "b" for u in P for v in P} | {"c" + u + "c" for u in P}


@lru_cache(None)
def inK(w, i):
    if i == 0:
        return w == "a"
    if len(w) < 3:
        return False
    if w[0] == "c" and w[-1] == "c":
        return inK(w[1:-1], i - 1)
    if w[0] == "b" and w[-1] == "b":
        m = w[1:-1]
        return any(inK(m[:k], i - 1) and inK(m[k:], i - 1)
                   for k in range(1, len(m)))
    return False


def V(i):
    return "a" if i == 0 else "b" + V(i - 1) + V(i - 1) + "b"


def part1():
    print("=== Part 1: K_n at fan-out two, content typing")
    for n in (1, 2, 3):
        L = K(n)
        cfree = sorted(w for w in L if "c" not in w)
        print(" n=%d |K_n|=%d  c-free words == [V_n]: %s" % (n, len(L), cfree == [V(n)]))
        r = check_finite(L)
        print("   exhaustive (2,c) check:", "no violation" if r is None else r)
    print(" explicit witness of the report (x=(b,baab), y=(bb,aab)):")
    for n in range(3, 9):
        Vn = V(n)
        x, y = ("b", "baab"), ("bb", "aab")
        E = ("b" * (n - 3), "b", Vn[n + 3:])          # common context
        F = ("", Vn[1:n + 3], Vn[n + 7:])             # separating context
        assert fill(E, x) == Vn and fill(E, y) == Vn and fill(F, x) == Vn
        Fy = fill(F, y)
        print("  n=%d E[x]=E[y]=F[x]=V_n: True | F[y] c-free: %s, |F[y]|=|V_n|: %s,"
              " F[y]!=V_n: %s, F[y] in K_n: %s, prefix %s"
              % (n, "c" not in Fy, len(Fy) == len(Vn), Fy != Vn, inK(Fy, n), Fy[:n + 3]))


# ---------------------------------------------------------------- Part 2
def part2(lmax=11):
    print("=== Part 2: (a|bc)^+")
    mem = lambda w: re.fullmatch(r"(a|bc)+", w) is not None
    r = check_pred(mem, lmax)
    print("  arity<=2 check, words of length <=", lmax, ":",
          "no violation (observation)" if r is None else r)
    w = "aabcabca"
    print("  sample word", w, "in L:", mem(w), "| merged aaabcbca in L:", mem("aaabcbca"))


# ---------------------------------------------------------------- Part 3
def part3():
    print("=== Part 3: P_{N,2} = {(ab)^N, cabab, abcab, ababc}")
    for N in (1, 2, 3, 4, 5):
        L = {"ab" * N, "cabab", "abcab", "ababc"}
        r = check_finite(L)
        print("  N=%d exhaustive (2,c) check: %s; abab in L: %s"
              % (N, "no violation" if r is None else r, "abab" in L))


# ---------------------------------------------------------------- Part 4
def weighted(codes, N):
    toks = [("a", 1)] + [(g, 2 ** i) for i, g in enumerate(codes)]
    out = set()

    def rec(w, rem):
        if rem == 0:
            if w:
                out.add(w)
            return
        for t, v in toks:
            if v <= rem:
                rec(w + t, rem - v)
    rec("", N)
    return out


def part4():
    print("=== Part 4: weight-2^n code candidates (a has weight 1, code i weight 2^i)")
    for name, codes in (("A", ["bc", "bcc", "bbc", "bbcc"]),
                        ("B", ["bc", "bcbb", "bbc", "bbcb"]),
                        ("C", ["bcb", "bccb", "bbcb", "bbccb"])):
        for n in (2, 3):
            L = weighted(codes[:n + 1], 2 ** n)
            r = check_finite(L)
            print("  %s n=%d |L|=%d: %s" % (name, n, len(L),
                                            "no violation" if r is None else r))


if __name__ == "__main__":
    part1()
    part2()
    part3()
    part4()
```

**出力**：

```
=== Part 1: K_n at fan-out two, content typing
 n=1 |K_n|=2  c-free words == [V_n]: True
   exhaustive (2,c) check: no violation
 n=2 |K_n|=6  c-free words == [V_n]: True
   exhaustive (2,c) check: no violation
 n=3 |K_n|=42  c-free words == [V_n]: True
   exhaustive (2,c) check: {'arity': 2, 'accepted': ('b', 'baab'), 'rejected': ('bb', 'aab'), 'common_context': ('', 'b', 'baabbbcaccacbb'), 'separating_context': ('', 'bbaab', 'bbbaabbaabbb'), 'word_not_in_L': 'bbbbaabaabbbbaabbaabbb'}
 explicit witness of the report (x=(b,baab), y=(bb,aab)):
  n=3 E[x]=E[y]=F[x]=V_n: True | F[y] c-free: True, |F[y]|=|V_n|: True, F[y]!=V_n: True, F[y] in K_n: False, prefix bbbbaa
  n=4 E[x]=E[y]=F[x]=V_n: True | F[y] c-free: True, |F[y]|=|V_n|: True, F[y]!=V_n: True, F[y] in K_n: False, prefix bbbbbaa
  n=5 E[x]=E[y]=F[x]=V_n: True | F[y] c-free: True, |F[y]|=|V_n|: True, F[y]!=V_n: True, F[y] in K_n: False, prefix bbbbbbaa
  n=6 E[x]=E[y]=F[x]=V_n: True | F[y] c-free: True, |F[y]|=|V_n|: True, F[y]!=V_n: True, F[y] in K_n: False, prefix bbbbbbbaa
  n=7 E[x]=E[y]=F[x]=V_n: True | F[y] c-free: True, |F[y]|=|V_n|: True, F[y]!=V_n: True, F[y] in K_n: False, prefix bbbbbbbbaa
  n=8 E[x]=E[y]=F[x]=V_n: True | F[y] c-free: True, |F[y]|=|V_n|: True, F[y]!=V_n: True, F[y] in K_n: False, prefix bbbbbbbbbaa
=== Part 2: (a|bc)^+
  arity<=2 check, words of length <= 11 : no violation (observation)
  sample word aabcabca in L: True | merged aaabcbca in L: True
=== Part 3: P_{N,2} = {(ab)^N, cabab, abcab, ababc}
  N=1 exhaustive (2,c) check: no violation; abab in L: False
  N=2 exhaustive (2,c) check: no violation; abab in L: True
  N=3 exhaustive (2,c) check: no violation; abab in L: False
  N=4 exhaustive (2,c) check: no violation; abab in L: False
  N=5 exhaustive (2,c) check: no violation; abab in L: False
=== Part 4: weight-2^n code candidates (a has weight 1, code i weight 2^i)
  A n=2 |L|=30: {'arity': 1, 'accepted': ('aabc',), 'rejected': ('abca',), 'common_context': ('a', ''), 'separating_context': ('', 'c'), 'word_not_in_L': 'abcac'}
  A n=3 |L|=1118: {'arity': 1, 'accepted': ('aaaaaab',), 'rejected': ('aaabb',), 'common_context': ('a', 'c'), 'separating_context': ('', 'cc'), 'word_not_in_L': 'aaabbcc'}
  B n=2 |L|=30: {'arity': 1, 'accepted': ('aab',), 'rejected': ('bbab',), 'common_context': ('bc', 'c'), 'separating_context': ('', 'ca'), 'word_not_in_L': 'bbabca'}
  B n=3 |L|=1118: {'arity': 1, 'accepted': ('bbcaaaa',), 'rejected': ('aaaaaaabc',), 'common_context': ('', ''), 'separating_context': ('abcb', ''), 'word_not_in_L': 'abcbaaaaaaabc'}
  C n=2 |L|=30: {'arity': 1, 'accepted': ('aabc',), 'rejected': ('aabcbb',), 'common_context': ('', 'cb'), 'separating_context': ('', 'ba'), 'word_not_in_L': 'aabcbbba'}
  C n=3 |L|=1118: {'arity': 1, 'accepted': ('bbcbaaabc',), 'rejected': ('aaaaaaabc',), 'common_context': ('', 'b'), 'separating_context': ('aabc', 'b'), 'word_not_in_L': 'aabcaaaaaaabcb'}
```

Part 1 の $n=3$ の全数検査が見つけた共通の文脈は $(\varepsilon,b,baabbbcaccacbb)$（$c$ を含む語）で、命題2.1の文脈 $b^{n-3}\square_1b\square_2V_n[n{+}3:]$ とは別だが、組 $\mathbf x,\mathbf y$ と食い違う文脈は同じである。$n=1,2,3$ の arity 1 の検査は全て通っている（arity 1 の違反は arity 2 より先に探す）ので、$K_n$ の Clark–Eyraud 代入可能性とも整合する。

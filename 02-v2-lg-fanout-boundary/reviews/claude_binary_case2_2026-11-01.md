# 二文字の内容型付け・ファンアウト2の場合 II の決着：内部の b 塊は高々一つ、従って純な a の穴も線形

**研究日**：2026年11月1日
**対象**：`growupkuriyama-hub/Papers/02-v2-lg-fanout-boundary`（clone 時の先頭 commit `599a3e90`）。出発点は `reviews/claude_binary_content_core_2026-11-01.md`（以下「前回の報告」）。定義は `main.tex` の §2–§4、`lem:typing-monotone`、`prop:sl-reduction`、`op:fanout-two`、`cor:distribution-representatives`、`def:uniform-polydata`。参考に `reviews/chatgpt_sl_positive_2026-11-01.md`（以下「ChatGPT 肯定報告」）と退避 `parked/parked_fanout2_and_comparison.tex` の `lem:app-u1-identity`・`lem:app-u1-parikh`。
**判定の意味**：「証明済み」はこの報告の中に証明を書いたこと（または明示した既存の証明への還元）を指し、外部査読や文献上の新規性を意味しない。「観察」は有限の計算で、証明ではない。

---

## 0. 結論と判定

記号：$\Sigma=\{a,b\}$、$c=c_\Sigma$、ファンアウト $\le2$、ランク $\le r$、$v=|V|$、$g=\lVert G\rVert$、$\theta=\bar\theta_G$。「$a^4$ が現れる」は「$L$ のある語が因子 $a^4$ を持つ」の意味。b の塊が**内部**とは、その両隣が a であること。

| 主張 | 判定 | 根拠 |
|---|---|---|
| **境界の交換**：$a^4$ が現れ、ある語が因子 $ab^ea^{j+1}$ を持てば $\mathcal D^{(1)}_L(ab^ea^j)=\mathcal D^{(1)}_L(a^{j+1}b^e)$（鏡像も） | **証明済み** | 補題A |
| **内部の b 塊は高々一つ**：$a^4$ が現れ、$b^4$ が現れず、Parikh 飽和でなければ、$aa$ を含む全ての語は内部の b 塊を高々一つしか持たない。従って $aa$ を含む語の a 骨格は48種類以下、塊は5個以下 | **証明済み** | 補題B、系B′ |
| **場合 II の線形上界**：同じ仮定で $t_{\rm typ}(G,c)\le117(r+1)v\theta$（全ての型付き非終端。型 $(\{a\})$ 等の純な型も含む） | **証明済み** | 定理C |
| **問い（純な a の穴）**：同じ仮定で、任意の一穴文脈 $C$（固定部分の長さ $\lambda$）について $P_a(C)\le\max\{4,(r+1)v\theta(\lambda+5)(\lambda+9)\}$。$\lambda\le\theta+3$ なら $(r+1)v\theta(\theta+8)(\theta+12)$ 以下 | **証明済み**（肯定） | 定理D |
| $a^4$ も $b^4$ も現れなければ（飽和かどうか、代入可能かどうかを問わず）$t_{\rm typ}(G,c)\le72(r+1)v\theta$ | **証明済み** | 命題E.1 |
| **二文字の主定理**：$r\ge2$ を固定すると、全ての $L\in\mathcal C_{2,c_{\{a,b\}}}$ と全ての reduced good な表示 $G$ について、$\mathcal B^{\le r}_{2,c}$ と $\mathcal B_{2,c}$ に共通の特徴標本 $K$ で $\lVert K\rVert_+\le4^{2r}(3+rC_r)g^3\theta^5+\mathbf 1_{\{\varepsilon\in L\}}$（$C_r=42r(r+1)+50(r+1)$）のものがある。非飽和なら $\lVert K\rVert_+\le4^{2r}(3+117r(r+1))g^2\theta+\mathbf 1_{\{\varepsilon\in L\}}$ | **証明済み**（飽和の場合は ChatGPT 肯定報告の定理3.3に依存。その使う部分を §1.3 で再点検） | 定理E |
| 前回の報告 §6.2 の条件 1–7 を満たす族（否定の向き） | **存在しない**（条件1–3が定理Cと両立しない） | 定理C、§5.6 |
| 前回の報告・ChatGPT 肯定報告に数学的な誤り | 見つからなかった（前回の §5.1 の場合分けは「深い挿入」を使わずに簡約できる、という改善点のみ） | §1、§5 |
| 小さな「骨格言語」の全数検査で、arity 1 の検査を通る言語に「$aa$ を含み内部の b 塊が二つ」の骨格は無い | **観察** | §6、付録 |
| $\Sigma=\{a,b,c\}$ 以上 | **未解決**（見通しのみ） | §8 |
| 補題A・補題B・定理C・定理D が文献で既知か | **未確認** | §9 |

**今回の到達点**：前回の報告で残った唯一の穴（場合 II の純な a の穴 $P_a(C)$）は**肯定で閉じた**。鍵は、内容 $\{a,b\}$ の一穴の組 $ab^ea$ と $aab^e$ の交換（補題A）で、これにより場合 II の「$aa$ を含む語」は内部の b 塊を一つしか持てない（補題B）。前回の挿入補題（同補題3.1）は、短縮で純な a の成分に b の塊が二つ入ると必ず内部の b 塊が二つできることを示していたので、二つを合わせると場合 II は場合 I と同じ数え上げで線形になる。結果として

> **$\Sigma=\{a,b\}$ の内容型付けは、ファンアウト2・ランク $\le r$（$r\ge2$）で多項式の特徴データを持つ**（定理E）。

これは `op:fanout-two` の最初の段（二文字）だけの解決であり、$\mathbf{SL}$ 全体（全ての $\Sigma$）についての `prop:sl-reduction` の判定にはまだ届かない。

---

## 1. 設定と、使う既知の事実の検証

### 1.1 設定

前回の報告 §1.1 と同じ。$L\in\mathcal C_{2,c}$、$G$ は $L\cap\Sigma^+$ の reduced good な表示（ファンアウト $\le2$、ランク $\le r$）。各非終端 $B$ に $\lVert\omega_B\rVert_1\le\theta$ の生成組 $\omega_B\in L_B(G)$、各 $A$ に `lem:thickness-equivalence`(iv) の文脈 $E_A$（$\lvert E_A\rvert_{\rm fix}\le\theta$、$E_A[L_A(G)]\subseteq L$）を固定する。各規則が直接書く終端は $\le\theta$ 個（同 (i)）。`cor:distribution-representatives` と $N_{\rm typ}\le\lvert\mathcal P_+(\Sigma)^\sharp\rvert^{2r}g=4^{2r}g$ から、$\tau(G,c)$ の上界は $\mathcal B^{\le r}_{2,c}$ と $\mathcal B_{2,c}$ に**共通の**特徴標本 $K$ の上界

$$
\lVert K\rVert_+\le4^{2r}g\,\bigl(1+2\theta+r\,\tau(G,c)\bigr)+\mathbf 1_{\{\varepsilon\in L\}} \tag{1.1}
$$

になる（`cor:distribution-representatives` の式そのもの。$\tau\le t_{\rm typ}$）。

語 $w$ の **a 骨格** $\sigma(w)$ は a の各極大な塊を一文字 $a$ に置き換えた語、$\rho_a(w)$ は a の極大な塊の数。b の極大な塊は、語の端に無ければ必ず両隣が a なので、**内部でない b の塊は語の最初と最後の塊だけ**である。

### 1.2 前回の報告から使う事実（自分で確かめたもの）

- **前回の補題2.1（a 塊の再配分）**：$pa^4q\in L$ なら、$(a,aa)$ と $(aa,a)$ は内容 $(\{a\},\{a\})$ で共通の許容文脈 $p\square_1a\square_2q$ を持つので二穴の分布が等しい。これで a を塊から塊へ一つずつ移せ、正の分割はこの操作で連結。従って所属は $(\sigma(w),\lvert w\rvert_a)$ の関数。確認した。
- **前回の系2.2**：(i) $aaba$ か $abaa$ を持つ語があれば、文脈 $(Ua,aV)$ が $ab$ と $ba$ を共に受理するので隣接交換で Parikh 飽和。(ii) 非飽和なら、$aa$ を含む語の内部の b 塊は長さ $\ge2$。確認した。
- **前回の補題3.1（挿入補題）**：型付き非終端 $X=A_{\mathbf S}$ の、生成組の総長が最小でその中で節点数最小の $\widetilde G_0$ の導出 $T$ を取る。印（純な成分の最初と最後の $\min\{2,\lvert u_i\rvert\}$ 文字、内容 $\{a,b\}$ の成分の a と b を一つずつ、計 $\le8$）を書かない重い節点の反鎖 $Q_0$ から、$\lvert I\rvert\ge\lvert Q_0\rvert/5$ の $I$ を取って同時に $\omega$ に差し替えると、$W=E_A[\mathbf u^I]\in L$ で、各 $h\in I$ が**長さ $\ge5$ の純な成分の内部**に異文字の塊を作り、それらは互いに別の塊で、**両隣が元の文字**。その成分の最初の二文字と最後の二文字は保たれる。各段（単独の差し替えは $L_A(G)$ に入り総長が減る／内容が全て保たれれば `lem:witness-length-template`(i) で $L_X$ に入り矛盾／ブロックの隣接グラフの最大次数 $\le4$ で独立集合）を確認した。数え上げ（パス上の型付きラベルは $\le9v$、重い節点は祖先について閉じる、各重い節点は $\le\theta$ 文字を直接書き軽い子は $\le r$ 個）も確認した。
- **前回の補題4.1・定理4.2（場合 I）**：$a^4$ と $b^4$ がともに現れ非飽和なら $t_{\rm typ}\le117(r+1)v\theta$。補題4.1の「塊4個以上なら完全に交互」の証明（b の再配分で内部の b 塊を長さ1にし、a の塊に長さ2以上があれば $aaba$）を確認した。
- **前回の定理5.2の (b)（一穴の環の議論）**：一穴文脈の穴に入る文字だけからなる「環」を持つ同じ非終端の祖先・子孫は、上を下に差し替えても動く文字が穴の中だけ。穴の中身が全て a のとき（定理5.4）、結果は穴の a を減らしただけの語。確認した（定理Dで使う）。
- 退避 `lem:app-u1-identity`：同じ非終端の祖先・子孫の生成組の Parikh ベクトルが等しければ、間の規則は全て恒等で、差し替えで同じ語を少ない節点で導出できる。good の条件だけを使い、型付けに依らない。確認した。

### 1.3 ChatGPT 肯定報告の定理3.3（Parikh 飽和の場合）の再点検

主定理の飽和の場合はこれに依存する。

- 補題3.1（成分型の合併が $\Sigma$）：(3.1) の最小化、重い節点が少なくとも一座標で $q_{u,a}\ge c_a=n_a-t_a+1$ を持つこと、商ベクトル $(\lfloor q_{u,a}/c_a\rfloor)_a$ がパスに沿って非増加で同じ商の中で非終端が繰り返さないこと、$\lfloor(p_a+n_a)/c_a\rfloor\le p_a+t_a$（$n':=n_a-t_a+1\ge1$ とすると $(p_a+t_a-1+n')/n'\le p_a+t_a$）を一行ずつ確認した。正しい。
- 補題3.2（純な型）：(P1)（行剛性。使う代入可能性は $a$ と $a^{1+\delta}$ の一穴だけで、ともに内容 $\{a\}$）と (P2)（高さ）を確認した。(P3)–(P6) は退避 `lem:app-u1-parikh` の「Type 1 only」の写しで、この部分は 2026-10-31 に ChatGPT が段ごとに検証している（`reviews/chatgpt_verify_parikh_homogenize_2026-10-31.md`）。私は (P3)–(P6) の各不等式の向きと、使う比較が全て純な a の組どうし（内容 $\{a\}$）であることを確かめたが、定数 $42r(r+1)+5$ の算術は再計算していない。
- 定理3.3：$C_r=42r(r+1)+50(r+1)$ が $30(r+1)v\theta^3$ と $(42r(r+1)+5)v^2\theta^5$ を支配することは確かめた。

従って主定理の飽和の場合は「ChatGPT 肯定報告の定理3.3（退避 `lem:app-u1-parikh` の純な部分を含む）が正しい」ことに依存する。非飽和の場合はこの報告と前回の報告だけで閉じている。

---

## 2. 新しい道具：境界の交換と、内部の b 塊の個数

### 補題A（境界の交換）【証明済み】

$L\in\mathcal C_{2,c}$ で $a^4$ が現れるとする。$e\ge1$、$j\ge1$ とし、$L$ のある語が因子 $a\,b^e\,a^{j+1}$ を持つとする。このとき

$$
\mathcal D^{(1)}_L(a\,b^e\,a^j)=\mathcal D^{(1)}_L(a^{j+1}\,b^e).
$$

鏡像（ある語が $a^{j+1}b^ea$ を持てば $\mathcal D^{(1)}_L(a^jb^ea)=\mathcal D^{(1)}_L(b^ea^{j+1})$）も成り立つ。

**証明。** その語を $W=U\,a\,b^e\,a^{j+1}\,V'$ と書く。$x:=ab^ea^j$、$y:=a^{j+1}b^e$ はともに内容 $\{a,b\}$。文脈 $E:=(U,\ aV')$ は $E[x]=W\in L$。$E[y]=U\,a^{j+1}\,b^e\,a\,V'$ を $W$ と比べると、$b^e$ の左の a の塊は $j$ 文字長く、右の a の塊は $j$ 文字短いが空にはならない（$W$ では $j+1\ge2$ 文字、$E[y]$ では $1$ 文字以上）。よって a 骨格も a の個数も $W$ と同じで、前回の補題2.1により $E[y]\in L$。共通の受理文脈を持つ同じ内容の組なので、$(1,c)$-代入可能性により分布が等しい。鏡像も同様。□

使う代入可能性は arity 1 だけ（前回の補題2.1を通して arity 2 も使う）。前回の補題6.1（b の塊を2から3に伸ばす障害）は、この交換の特別な形として読める。

### 補題B（内部の b 塊は高々一つ）【証明済み】

$L\in\mathcal C_{2,c}$ が次を満たすとする：$a^4$ が現れる、$b^4$ を因子に持つ語は無い、Parikh 飽和でない。このとき、因子 $aa$ を持つ全ての $w\in L$ は、内部の b 塊を高々一つしか持たない。

**証明。** 反対に、$aa$ を持つ $w\in L$ が内部の b 塊を二つ以上持つとする。内部の b 塊の間にある b 塊は全て内部なので、隣り合う二つの内部の b 塊 $\beta_1=b^e$、$\beta_2=b^{e'}$ と、その間の a の塊 $R$ がある。$\beta_1$ の左隣の a の塊を $A_0$ とする。

(1) $w$ は $aa$ を持つので前回の系2.2(ii) により $e,e'\ge2$、従って $e+e'\ge4$。
(2) $\lvert w\rvert_a\ge\rho_a(w)+1$。前回の補題2.1で a を再配分して、次の二語を得る（どちらも骨格 $\sigma(w)$、a の個数 $\lvert w\rvert_a$ なので $L$ に入る）：
  - $W_2$：$R$ の長さが2（余りは $A_0$ へ）。$W_2$ は因子 $a\,b^e\,aa$（$A_0$ の最後の a、$\beta_1$、$R$）を持つ。
  - $W_1$：$R$ の長さが1（余りは $A_0$ へ）。$W_1=U_1\,a\,b^e\,a\,b^{e'}\,V_1$（$U_1a$ は $A_0$ までの接頭辞）。
(3) 補題A（$j=1$、$W_2$ を使う）により $\mathcal D^{(1)}_L(ab^ea)=\mathcal D^{(1)}_L(aab^e)$。
(4) 文脈 $F:=(U_1,\ b^{e'}V_1)$ は $F[ab^ea]=W_1\in L$。よって $F[aab^e]=U_1\,aa\,b^{e+e'}\,V_1\in L$。これは因子 $b^4$ を持ち、仮定に反する。□

**系B′（$aa$ を持つ語の形）【証明済み】** 同じ仮定で、$aa$ を持つ語の a 骨格は

$$
[\,b^{e_0}\,]\ a\ [\,b^{e}\,a\,]\ [\,b^{e_1}\,],\qquad e_0,e_1\in\{1,2,3\},\ e\in\{2,3\}
$$

（括弧は省略可）のどれかで、48種類以下。極大な塊は5個以下、a の塊は2個以下。$L$ のそれ以外の語は全ての a の塊が長さ1（「a 細い」）。

**証明。** 内部でない b 塊は最初と最後の塊だけ（長さ $\le3$、$b^4$ が無い）。内部の b 塊は補題B で高々一つ、長さは前回の系2.2(ii) で2か3。数えると $4\cdot3\cdot4=48$。□

**手がかり1との関係**：$N_\sigma:=\{\lvert w\rvert_a:w\in L,\ \sigma(w)=\sigma\}$ と置けば、前回の補題2.1により $L$ は組 $(\sigma,N)$ の集合で、a 剛 $\iff$ 全ての $N_\sigma$ が一点。$k\ge1$ について $\sigma(C[a^k])$ は $k$ に依らないので、$\sigma_C:=\sigma(C[a])$ として $P_a(C)=\min N_{\sigma_C}-\lvert C\rvert_a$（$N_{\sigma_C}$ が空でないとき）。系B′ は、$P_a(C)\ge2$ なら $\sigma_C$ が上の48種類のどれかであることを言う。ただし、以下の証明はこの「骨格の有限性」を直接は使わず、補題B だけを使う。

---

## 3. 場合 II の上界

以下この節では、$L\in\mathcal C_{2,c}$ が **$a^4$ を持ち、$b^4$ を持たず、Parikh 飽和でない**とする（これは前回の「場合 II」を含み、深い挿入の有無を問わない）。

### 定理C（場合 II の線形上界）【証明済み】

全ての型付き非終端について

$$
t_{\rm typ}(G,c)\le117(r+1)v\theta,\qquad \tau(G,c)\le117(r+1)v\theta .
$$

**証明。** 型付き非終端 $X=A_{\mathbf S}$ を任意に取り、前回の補題3.1を適用する。$Q$ を重い節点の反鎖、$Q_0\subseteq Q$ を部分木が印を書かないもの、$I\subseteq Q_0$ を補題3.1の独立集合（$\lvert I\rvert\ge\lvert Q_0\rvert/5$）とする。

$\lvert I\rvert\ge2$ と仮定する。$W:=E_A[\mathbf u^I]\in L$ では、各 $h\in I$ が長さ $\ge5$ の純な成分の内部に異文字の塊を作る。長さ $\ge5$ の純な成分は $W$ の因子なので、$b^4$ が無いことから内容 $\{a\}$ の成分であり、異文字の塊は **b の塊で両隣が a**、すなわち $W$ の内部の b 塊である。異なる $h$ の塊は別の塊なので、$W$ は内部の b 塊を二つ以上持つ。さらにその純な a の成分の最初の二文字 $aa$ は保たれるので、$W$ は $aa$ を持つ。これは補題B に反する。

よって $\lvert I\rvert\le1$、従って $\lvert Q_0\rvert\le5$（$\lvert Q_0\rvert\ge6$ なら $\lvert I\rvert\ge2$）、$\lvert Q\rvert\le8+5=13$。以下は前回の系3.2・定理4.2と同じ数え上げ：重い節点は祖先について閉じ、同じ深さの重い節点は反鎖で、深さは $\le9v$ なので重い節点は $\le117v$ 個。生成組の各文字は重い節点が直接書く（$\le\theta$）か、重い節点の軽い子（$\le r$ 個、各 $\le\theta$）に属する。根が軽ければ $\lVert\mathbf u\rVert_1\le\theta$。よって $\lVert\mathbf u\rVert_1\le117(r+1)v\theta$。□

**注意**：この証明は前回の報告の「$P_a(C)$ への帰着」（前回の補題5.3・定理5.4）を通らない。純な型 $(\{a\})$、$(\{a\},\{a\})$、$(\{a\},\{b\})$、$(\{b\},\{a\})$ の型付き非終端も、他の型と一括で処理される。前回の報告で止まっていたのは、「短縮で入る b の塊」を制御する言語側の制約が無かったからで、補題B がそれを与える。

### 定理D（純な a の穴の直接の上界）【証明済み】

一穴文脈 $C=v_0\square v_1$（$\lambda:=\lvert C\rvert_{\rm fix}$）で $C[a^+]\cap L\neq\varnothing$ のものについて

$$
P_a(C)\le\max\bigl\{4,\ (r+1)\,v\,\theta\,(\lambda+5)(\lambda+9)\bigr\}.
$$

特に前回の補題5.3の文脈（$\lambda\le\theta+3$）では $P_a(C)\le(r+1)v\theta(\theta+8)(\theta+12)$。

問いへの直接の答えとして述べる（定理C が既に $\tau$ を抑えるので、主定理には不要）。

**証明。** $k:=P_a(C)\ge5$ とする（そうでなければ終わり）。$W:=C[a^k]\in L=L(G)$ の節点数最小の導出 $T$ を取る。$C$ の固定部分の全ての文字と、穴の最初の二文字・最後の二文字に**印**を付ける（$M:=\lambda+4$ 個）。印の無い文字は全て穴の**内側**（穴から両端の二文字ずつを除いた区間、空でない）にあり、全て a。

(1) **一回の差し替え**：部分木が印を書かない節点 $h$（非終端 $B_h$）の生成組は穴の内側にあり、純な a。$h$ が重い（生成組の総長 $>\theta$）とき、$\omega_{B_h}$ が純な a なら、差し替えると $C[a^{k'}]$（$4\le k'<k$）で $k$ の最小性に反する。よって **$\omega_{B_h}$ は b を含む**。

(2) **パスの長さ**：一つのパス上で同じ非終端の祖先 $u$ と子孫 $u'$ の間の環（$u$ の生成組から $u'$ の生成組を除いた文字）が印を含まなければ、環は穴の内側にあり、前回の定理5.2(b) の場合分けにより、$u$ を $u'$ の部分木に差し替えて動く文字は全て穴の内側（a だけ）にある。結果は $C[a^{k''}]$（$k''=k-\lvert\text{環}\rvert\ge4$）で、環が空でなければ $k$ の最小性に、空なら `lem:app-u1-identity` により節点数の最小性に反する。従って同じ非終端の連続する出現の間の環は印を含み、環は互いに交わらないので、各パスの節点数は $\le v(M+1)$。

(3) **印の無い重い節点の反鎖は5個以下**：印の無い重い節点の反鎖 $Q$ を取る。各 $h\in Q$ のブロック（$h$ の生成組の成分が穴の中で占める区間、$\le2$ 個）について、間に文字なしで隣り合うブロックの持ち主を辺で結ぶと最大次数 $\le4$ なので、$\lvert I\rvert\ge\lvert Q\rvert/5$ の独立集合 $I$ がある。$I$ を同時に $\omega$ に差し替えた語 $W^I$ は $L(G)=L$ に入る（$\varepsilon\notin$ の部分。$W^I$ は空でない）。(1) により各 $h\in I$ のブロックに b が入り、その b の塊は、ブロックの外側の隣が元の穴の a（$I$ の別のブロックとは隣接しない）なので両隣が a、すなわち $W^I$ の内部の b 塊で、異なる $h$ の塊は少なくとも一つの元の a で隔てられて別の塊である。また $W^I$ は穴の最初の二文字 $aa$ を持つ。$\lvert I\rvert\ge2$ なら補題B に反する。よって $\lvert I\rvert\le1$、$\lvert Q\rvert\le5$。

(4) **数え上げ**：生成組が印を含む節点は印へのパスの上にあり、$\le Mv(M+1)$ 個。印の無い重い節点は、深さが $\le v(M+1)$ で同じ深さのものが反鎖なので $\le5v(M+1)$ 個。$W$ の各文字は、印を含むか重い節点が直接書く（各 $\le\theta$）か、そのような節点の、印も無く軽い子（$\le r$ 個、各 $\le\theta$）に属する（文字を直接書く節点から上へたどり、最初に現れる「印を含むか重い」節点の子を取る。根は印を含む）。よって

$$
k\le\lvert W\rvert\le(M+5)\,v\,(M+1)\,(r+1)\,\theta=(r+1)v\theta(\lambda+9)(\lambda+5).\qquad\square
$$

**注意**：前回の定理5.4の第二式では、印の無い節点を「純な組の最短の長さ $\Pi_G$」で抑えるしかなかった。ここでは (3) で、印の無い**重い**節点そのものの個数を補題B で抑えるので、$\Pi_G$ が現れない。

### 命題E.1（$a^4$ も $b^4$ も現れない場合）【証明済み】

$L$ のどの語も $a^4$ も $b^4$ も持たなければ（飽和・代入可能性を問わない）、$t_{\rm typ}(G,c)\le72(r+1)v\theta$。

**証明。** 前回の補題3.1で、$h\in Q_0$ があれば長さ $\ge5$ の純な成分があり、それは $E_A[\mathbf u]\in L$ の因子 $a^5$ か $b^5$ になる。よって $Q_0=\varnothing$、$\lvert Q\rvert\le8$、重い節点は $\le72v$ 個。□

（ChatGPT 肯定報告の系2.2（深い挿入が無ければ $252(r+1)v\theta$）でも足りる。）

---

## 4. 二文字の全体の結論

### 定理E（二文字の内容型付けのファンアウト2の多項式データ）【証明済み。飽和の場合は ChatGPT 肯定報告の定理3.3に依存】

$\Sigma=\{a,b\}$、$c=c_{\{a,b\}}$、$r\ge2$ を固定し、$C_r:=42r(r+1)+50(r+1)$ と置く。全ての $L\in\mathcal C_{2,c}$ と、$L\cap\Sigma^+$ の全ての reduced good なファンアウト $\le2$・ランク $\le r$ の表示 $G$（$g=\lVert G\rVert$、$v=|V|$、$\theta=\bar\theta_G$）について：

1. $L$ が Parikh 飽和でなければ $t_{\rm typ}(G,c)\le117(r+1)v\theta$。従って $\mathcal B^{\le r}_{2,c}$ と $\mathcal B_{2,c}$ に共通の特徴標本 $K$ があり
$$\lVert K\rVert_+\le4^{2r}\bigl(3+117r(r+1)\bigr)\,g^2\theta+\mathbf 1_{\{\varepsilon\in L\}}.$$
2. $L$ が Parikh 飽和なら $\tau(G,c)\le C_rv^2\theta^5$ で、共通の特徴標本 $K$ があり
$$\lVert K\rVert_+\le4^{2r}(3+rC_r)\,g^3\theta^5+\mathbf 1_{\{\varepsilon\in L\}}.$$
3. 従って全ての場合に、$\mathcal B^{\le r}_{2,c}$ と $\mathcal B_{2,c}$ に共通の特徴標本 $K$ で
$$\boxed{\ \lVert K\rVert_+\le4^{2r}(3+rC_r)\,g^3\theta^5+\mathbf 1_{\{\varepsilon\in L\}}\ }$$
のものがある。多項式 $p_r(g,\theta):=4^{2r}(3+rC_r)g^3\theta^5+1$ は $r$ だけに依存し、$L$ にも $G$ にも依存しない。すなわち $c_{\{a,b\}}$ は `def:uniform-polydata` の条件をファンアウト2・ランク $r$ で満たす。

**証明。**
- **場合分けの網羅性**：$L$ は飽和か否か。非飽和なら (a) $a^4$ も $b^4$ も現れない、(b) ともに現れる、(c) ちょうど一方が現れる、のどれか。(c) は $a,b$ を入れ替えて「$a^4$ あり・$b^4$ なし」としてよい（内容型付けは文字の入れ替えで不変）。
- 非飽和 (a)：命題E.1、$72(r+1)v\theta$。(b)：前回の定理4.2、$117(r+1)v\theta$。(c)：定理C、$117(r+1)v\theta$。
- 飽和：ChatGPT 肯定報告の定理3.3、$\tau\le C_rv^2\theta^5$。
- 特徴標本：(1.1) に代入。非飽和では $v\le g$、$\theta\ge1$ から $g(1+2\theta)\le3g^2\theta$、$g\cdot117r(r+1)v\theta\le117r(r+1)g^2\theta$。飽和では ChatGPT 肯定報告の (3.5)。3 は $r\ge2$ で $C_r\ge117(r+1)$、$g^3\theta^5\ge g^2\theta$ による。□

**系（二文字の半束型付け）【証明済み】** $\{a,b\}^+$ から有限の半束への任意の型付け $s$ は $s\preceq c_{\{a,b\}}$ を満たす（`prop:sl-reduction`(ii) の証明）。`lem:typing-monotone` と定理E により、全ての $L\in\mathcal C_{2,s}$ に同じ長さの $\mathcal B^{\le r}_{2,s}$ と $\mathcal B_{2,s}$ の特徴標本がある。

**言っていないこと**：
- 三文字以上の $\Sigma$ については何も言っていない。`prop:sl-reduction`(ii) は全ての $\Sigma$ を要求するので、`op:fanout-two` は未解決のまま。
- 下界は主張していない。指数 $g^3\theta^5$（飽和の場合）・$g^2\theta$（非飽和の場合）が最良かどうかは調べていない。
- 「最大の特徴標本」という量は使っていない。上界は「この長さ以下の特徴標本が存在する」の意味。

### 4.1 証明の依存関係

- 前回の補題2.1（a 塊の再配分；`lem:app-u1-transfer`(i) の繰り返し、arity 2）
  - → 前回の系2.2（$aaba$/$abaa$ ⇒ 飽和；非飽和なら $aa$ を持つ語の内部の b 塊は長さ $\ge2$。arity 1）
  - → **補題A**（境界の交換 $ab^ea^j\equiv a^{j+1}b^e$。arity 1）
  - → **補題B**（$a^4$ あり・$b^4$ なし・非飽和なら、$aa$ を持つ語の内部の b 塊は高々一つ）→ 系B′
- 前回の補題3.1（挿入補題；`lem:witness-length-template`(i)、good の性質）
  - ＋ 補題B → **定理C**（場合 II、$117(r+1)v\theta$）
  - ＋（$a^4$・$b^4$ なし）→ **命題E.1**（$72(r+1)v\theta$）
  - ＋ 前回の補題4.1 → 前回の定理4.2（場合 I、$117(r+1)v\theta$）
- 前回の定理5.2(b)、`lem:app-u1-identity` ＋ 補題B → **定理D**（$P_a(C)$ の直接の上界。主定理には不要）
- ChatGPT 肯定報告の補題3.1・3.2（退避 `lem:app-u1-parikh`）→ 同定理3.3（飽和、$C_rv^2\theta^5$）
- 網羅性（§4 の場合分け）＋ `cor:distribution-representatives` → **定理E** → `lem:typing-monotone` → 系

前回の報告の §5.2–§5.4（純な型の帰着、$\delta_L$・$\Pi_G$ による上界）と ChatGPT 肯定報告の定理2.1（浅い場合）は、主定理の証明には不要になった（正しいが、通らなくてよい）。

---

## 5. 手がかりの検討と、前回までの報告の点検

### 5.1 手がかり1（正規形）
正しい。$P_a(C)=\min N_{\sigma_C}-\lvert C\rvert_a$（§2 末尾）。補題B により、$P_a(C)\ge2$ となる $\sigma_C$ は系B′ の48種類に限られる。

### 5.2 手がかり2（内容 $\{a,b\}$ の組で骨格をまたぐ）
この方向が正解だった。ただし強制されたのは「$N_\sigma$ の加法的な形」ではなく、もっと強い「骨格の形の制限」である：一穴の組 $ab^ea$ と $aab^e$（b の塊の左右に a の塊を付け替える）が共通の文脈を持つことは再配分から自動的に従い（補題A）、別の文脈でこの付け替えが二つの b 塊を合流させて $b^4$ を作る。二穴の組は補題2.1の中でしか使わない。

### 5.3 手がかり3（a 剛の場合の構造）
不要になった。補題B は a 剛かどうかに依らない。なお、「内部の a の塊が二つの内部の b 塊に挟まれる」骨格はそもそも現れない（補題B）。

### 5.4 手がかり4（一文字の部分文法の半線形性）
使っていない。一文字の MCFG の生成する長さの集合の最短元・周期の文法の大きさによる上界は、この報告では調べておらず、文献も**未確認**。定理C の証明が $\Pi_G$ を避けるので、必要なかった。

### 5.5 手がかり5（長さの種類の定理）
使っていない。

### 5.6 手がかり6（否定の向き）と前回の §6.2
定理C は、前回の §6.2 の条件 1（場合 II）・3（純な型でだけ大きい）を満たす族が無いことを示す：場合 II なら全ての型で $\tau_X\le117(r+1)v\theta$。倍増 $A_i\to A_{i-1}A_{i-1}$ で純な a を作り、b を含む短い枝で $\theta$ を小さく保つ設計がなぜ必ず壊れるかは、定理D の (3) が示す：最小の導出には、純な a の長い部分を作る重い節点の反鎖が多数あり、そのうち二つを同時に b を含む短い枝に差し替えると、一つの a の塊の中に内部の b 塊が二つでき（両端の $aa$ は残る）、補題B に反する。過去の候補（括弧付き倍増族、Thue–Morse、単一の繊維、並べ替えに閉じた繊維）も同じ型の破綻である。前回の §6.3 の観察（「b の塊が全て2か3」、剛い玩具）の違反も、補題B の証明の交換そのもので再現できる（§6）。

### 5.7 前回の報告の点検
数学的な誤りは見つからなかった。補足：
- 前回の §5.1 の場合分けは「深い挿入」を軸にしていたが、定理E の通り「飽和／$a^4$・$b^4$ の有無」だけで網羅でき、深い挿入の概念は不要になる。
- 前回の補題6.1は補題A の特別な機構（$x=a^pbb$、$y=a^{p+\Delta}b$）である。結論は正しいが、補題B の方が強い。
- 前回の §7「止まった場所」の記述（文法の短縮と内容 $\{a,b\}$ の組の交換の二つだけでは抑えられない）は、言語側の構造（補題B）を一つ挟めば、まさにその二つで抑えられる、という形で解消した。
- 前回の §6.3 の表の「剛い玩具」二つと「b の塊が全て2/3」の違反は、§6 の再現でも違反のまま（言語が代入可能でないことの証明として正しい）。

ChatGPT 肯定報告については §1.3 の範囲で点検し、誤りは見つからなかった。

---

## 6. 有限の観察

付録のスクリプト（標準ライブラリのみ、約3分）は二つのことをする。**観察であって証明ではない**（ただし第一部の FAIL は具体的な違反の組と文脈なので、その言語が代入可能でないことの証明として読める）。

**第一部（補題B の交換の再現）**：述語で与えた言語から「$aa$ を持ち内部の b 塊が二つ」の語を探し、補題B の証明の $W_2,W_1,E,F$ を作って所属を表示する。

| 言語 | 出力 |
|---|---|
| $a^+bba^+bba^+$ | $W_2=abbaabba$, $W_1=aabbabba$；$E[x]=abbaabba$, $E[y]=aabbabba$ ともに受理；$F[x]=aabbabba$ 受理、$F[y]=aaabbbba$ 不受理 → 違反 |
| b の塊が全て長さ2か3 | 同じ組で違反（前回の §6.3 の違反と同じ機構） |
| $a^+bba^+bbba^+$ で $\lvert w\rvert_a=5$（剛い） | $F[y]=aaaabbbbba$ 不受理 → 違反（この言語には $a^4$ が無いので補題B の仮定外だが、違反の組そのものは有効） |

**第二部（小さな骨格言語の全数検査）**：所属が「a 骨格が選んだ集合に入るか」だけで決まる言語（再配分に閉じている）を全て作り、arity 1 の内容型付けの代入可能性を、長さ上限までの観察された文脈で検査した。

| 範囲 | 試した数 | 通った数 | 通った中で「内部の b 塊が二つの骨格」を含むもの |
|---|---|---|---|
| 長さ ≤6 の骨格の集合（大きさ ≤2）、語の長さ ≤8 | 903 | 92 | 0 |
| 長さ ≤5 の骨格の集合（大きさ ≤4）、語の長さ ≤7 | 20853 | 208 | 0 |

通った言語のうち内部の b 塊を一つ持つ骨格を含むのは 25 個で、例えば $\{abb,abba,bba\}$（＝ $a^*bba^*$ から $bb$ を除いたもの）や $\{ab,aba,ba\}$（後者は $aba$ に $aa$ を足すと $aaba$ で、飽和の場合）。補題B と整合する。この検査は「骨格だけで決まる」言語に限られ、a の個数に条件を付けた（剛い）言語は含まない。

---

## 7. 二文字の場合の全体の結論

**言えたこと（証明済み）**：$\Sigma=\{a,b\}$、内容型付け、ファンアウト2、ランク $\le r$（$r\ge2$）で、**全ての** $L\in\mathcal C_{2,c_{\{a,b\}}}$ と全ての reduced good な表示 $G$ について、$\mathcal B^{\le r}_{2,c}$ と $\mathcal B_{2,c}$ に共通の特徴標本で長さ $\le4^{2r}(3+rC_r)\lVert G\rVert^3\bar\theta_G^5+1$ のものがある（定理E）。非飽和の言語では $O_r(\lVert G\rVert^2\bar\theta_G)$。前回の報告で残った場合 II の純な a の穴 $P_a(C)$ は、肯定で $O_r(v\theta^3)$（定理D）、型付き非終端の代表は線形（定理C）。

**依存の注意**：飽和の場合は ChatGPT 肯定報告の定理3.3（退避 `lem:app-u1-parikh` の純な部分を含む）に依存する。§1.3 で使う部分を点検したが、(P3)–(P6) の定数の算術は再計算していない。この部分に誤りがあっても、非飽和の言語についての結論（定理E の 1）は影響を受けない。

**`op:fanout-two` との関係**：二文字の段は肯定で閉じた。ファンアウト1では `thm:fanout-one-data` により $\mathbf{SL}$ は性質を持たない（$r_{\max}\ge2$）ので、もし全ての $\Sigma$ で肯定なら、境界はファンアウトに依存する。三文字以上は未解決。

---

## 8. 三文字以上（$\Sigma=\{a,b,c\}$）への見通し

- **そのまま移るもの**：前回の補題2.1は各文字 $x$ について（$x^4$ が現れれば $x$ の塊の再配分）同じ形で成り立つ（比べる組の内容は $(\{x\},\{x\})$）。挿入補題（前回の補題3.1）は印を「各成分の内容の各文字を一つずつ」に増やせば成り立つ（ChatGPT 肯定報告の定理2.1の印と同じ考え方）。補題A も、二文字 $x,y$ の局所的な交換 $x\,y^e\,x\equiv xx\,y^e$ として、周りに第三の文字があっても成り立つ。
- **移らないもの**：(i) 補題B の最後の矛盾は「$y^{e+e'}$ が禁止」と「内部の $y$ 塊は長さ $\ge2$」（系2.2(ii)、つまり $\{x,y\}$ の局所的な非飽和）を使う。三文字では二つの $y$ 塊の間に $c$ が挟まり得るので、合流が起きない配置がある。(ii) 内容 $\{a,b\}$ の**二文字の純な成分**（$\{a,b,c\}$ の中では純）には再配分の補題が無い。短縮で $c$ が入った成分を、内容 $\{a,b\}$ のまま修復する手段が無く、ChatGPT 肯定報告 §5.3 の指摘はそのまま残る。
- **次の一歩の候補**：「各文字 $x$ について、$x^4$ が現れ他の文字の4乗が現れない」型の場合に、補題B の類似（$x$ の長い塊の中に他の文字の塊を二つ入れると矛盾）が成り立つかを調べる。二文字の純な成分（内容 $\{a,b\}$ で長い成分）の短縮は、二文字の場合の「Parikh 飽和」に当たる別の機構が要る見込み（未検証）。

---

## 9. 文献

- Yoshinaka, *Efficient learning of multiple context-free languages with multidimensional substitutability from positive data*, TCS 412 (2011) 1821–1831：組代入可能性と許容文脈。
- Clark–Eyraud, *Polynomial identification in the limit of substitutable context-free languages*, JMLR 8 (2007)：代入可能性の原型。
- 栗山 `main.tex`、退避 `lem:app-u1-identity`・`lem:app-u1-parikh`、`reviews/claude_binary_content_core_2026-11-01.md`、`reviews/chatgpt_sl_positive_2026-11-01.md`：直接の依存先。
- 補題A・補題B（再配分に閉じた代入可能言語の「内部の塊は一つ」）、定理C、定理D、定理E と同じ形の結果が文献にあるか：**未確認**（網羅的な文献調査はしていない）。補題A は代入可能性の一回の適用で、技法としての新規性は主張しない。

---

## 付録：スクリプト全文と出力

保存名 `binary_case2_check.py`、Windows では `py -3 binary_case2_check.py`。Python 3 の標準ライブラリだけを使う。実行時間は Linux で約3分（第二部の全数検査が大半）。

```python
# binary_case2_check.py -- Python 3 standard library only.
# Run on Windows with:  py -3 binary_case2_check.py
#
# Finite OBSERVATIONS (not proofs) for the report
# reviews/claude_binary_case2_2026-11-01.md.
#
# Part 1 replays, on concrete predicates, the exchange used in the proof of
#   Lemma B (one internal b-run):  x = a b^e a  and  y = a a b^e
# share the context E = (U, a V') of a word W2 = U a b^e a a V', and the
# context F = (U1, b^e' V1) of a word W1 = U1 a b^e a b^e' V1 separates them
# because F[y] contains b^(e+e').  Membership is decided by the predicate.
#
# Part 2 runs an arity-1 substitutability check (content typing, observed
# contexts, words of length <= LMAX) on all small "skeleton languages"
# (membership = the a-skeleton belongs to a chosen set; such languages are
# closed under a-redistribution by construction) and records whether any
# language that PASSES contains a word with factor aa and two internal
# b-runs.  Lemma B predicts: never.  PASS is only an observation.

import re
from collections import defaultdict
from itertools import product


def content(w):
    return "".join(sorted(set(w)))


def skeleton(w):
    return re.sub(r"a+", "a", w)


def b_runs_internal(w):
    """Number of b-runs with an a on both sides."""
    return len(re.findall(r"(?<=a)b+(?=a)", w))


def words_upto(n):
    for m in range(1, n + 1):
        for t in product("ab", repeat=m):
            yield "".join(t)


# ---------------------------------------------------------------- Part 1
def replay_exchange(member, lmax, name):
    """Find an accepted word with aa and two internal b-runs, build W2, W1
    by redistribution and report the four memberships of the proof."""
    for w in words_upto(lmax):
        if not member(w) or "aa" not in w or b_runs_internal(w) < 2:
            continue
        # runs of w
        runs = re.findall(r"a+|b+", w)
        # first internal b-run beta1 followed by a-run R and b-run beta2
        for i in range(1, len(runs) - 3):
            if (runs[i][0] == "b" and runs[i - 1][0] == "a"
                    and runs[i + 1][0] == "a" and runs[i + 2][0] == "b"
                    and i + 3 < len(runs)):
                break
        else:
            continue
        e, e2 = len(runs[i]), len(runs[i + 2])
        total_a = w.count("a")
        n_a_runs = sum(1 for r in runs if r[0] == "a")
        # W2: R has length 2, A0 (= runs[i-1]) keeps the rest of the extra
        def build(r_len):
            out = []
            rest = total_a - (n_a_runs - 2) - r_len  # length given to A0
            for k, r in enumerate(runs):
                if r[0] == "b":
                    out.append(r)
                elif k == i + 1:
                    out.append("a" * r_len)
                elif k == i - 1:
                    out.append("a" * rest)
                else:
                    out.append("a")
            return "".join(out)
        W2, W1 = build(2), build(1)
        pre = "".join(re.findall(r"a+|b+", W2)[:i])  # up to end of A0
        U = pre[:-1]
        x, y = "a" + "b" * e + "a", "aa" + "b" * e
        Vp = W2[len(pre) + e + 2:]
        E_x, E_y = U + x + "a" + Vp, U + y + "a" + Vp
        pre1 = "".join(re.findall(r"a+|b+", W1)[:i])
        U1 = pre1[:-1]
        V1 = W1[len(pre1) + e + 1 + e2:]
        F_x, F_y = U1 + x + "b" * e2 + V1, U1 + y + "b" * e2 + V1
        print(name)
        print("  witness word with aa and two internal b-runs:", w)
        print("  W2 =", W2, member(W2), "| W1 =", W1, member(W1))
        print("  E[x] =", E_x, member(E_x), "| E[y] =", E_y, member(E_y))
        print("  F[x] =", F_x, member(F_x), "| F[y] =", F_y, member(F_y))
        print("  => NOT (1,c)-substitutable:",
              member(E_x) and member(E_y) and member(F_x) != member(F_y))
        return
    print(name)
    print("  no accepted word with aa and two internal b-runs up to", lmax)


# ---------------------------------------------------------------- Part 2
def arity1_violation(member, lmax):
    words = [w for w in words_upto(lmax) if member(w)]
    dist = defaultdict(set)
    for w in words:
        n = len(w)
        for i in range(n):
            for j in range(i + 1, n + 1):
                dist[w[i:j]].add((w[:i], w[j:]))
    groups = defaultdict(list)
    for x, ctxs in dist.items():
        for c in ctxs:
            groups[(content(x), c)].append(x)
    for key in sorted(groups):
        xs = sorted(groups[key])
        lead = xs[0]
        for other in xs[1:]:
            for p, q in ((lead, other), (other, lead)):
                for (u, v) in sorted(dist[p]):
                    if not member(u + q + v):
                        return (p, q, key[1], (u, v))
    return None


def all_skeletons(maxlen):
    out = []
    for w in words_upto(maxlen):
        if "aa" in w or "bbbb" in w:
            continue
        out.append(w)
    return out


def exhaustive_skeleton_languages(sk_len, max_set, lmax):
    """All sets of at most max_set skeletons of length <= sk_len.
    Membership of w = skeleton(w) in the set."""
    from itertools import combinations
    sks = all_skeletons(sk_len)
    tried = passed = bad_passed = 0
    nontrivial = []
    for k in range(1, max_set + 1):
        for chosen in combinations(sks, k):
            chosen = frozenset(chosen)
            tried += 1
            member = lambda w, ch=chosen: skeleton(w) in ch
            if arity1_violation(member, lmax) is None:
                passed += 1
                if any(b_runs_internal(s) >= 2 for s in chosen):
                    bad_passed += 1
                if any(b_runs_internal(s) == 1 for s in chosen):
                    nontrivial.append(sorted(chosen))
    print("skeleton languages: all sets of <= %d skeletons of length <= %d,"
          " words <= %d" % (max_set, sk_len, lmax))
    print("  tried:", tried, "| passed arity-1 check:", passed)
    print("  passed AND some skeleton has two internal b-runs:", bad_passed)
    print("  passing sets with one internal b-run:", len(nontrivial), nontrivial[:8])


if __name__ == "__main__":
    two_internal = lambda w: re.fullmatch(r"a+bba+bba+", w) is not None
    free_23 = lambda w: all(len(r) in (2, 3) for r in re.findall(r"b+", w))
    rigid = lambda w: (re.fullmatch(r"a+bba+bbba+", w) is not None
                       and w.count("a") == 5)
    replay_exchange(two_internal, 9, "L = a+ bb a+ bb a+")
    replay_exchange(free_23, 9, "L = all b-runs of length 2 or 3")
    replay_exchange(rigid, 13, "L = a+ bb a+ bbb a+ with |w|_a = 5 (rigid)")
    exhaustive_skeleton_languages(sk_len=6, max_set=2, lmax=8)
    exhaustive_skeleton_languages(sk_len=5, max_set=4, lmax=7)
```


出力（Python 3、Linux、約3分）：

```text
L = a+ bb a+ bb a+
  witness word with aa and two internal b-runs: aabbabba
  W2 = abbaabba True | W1 = aabbabba True
  E[x] = abbaabba True | E[y] = aabbabba True
  F[x] = aabbabba True | F[y] = aaabbbba False
  => NOT (1,c)-substitutable: True
L = all b-runs of length 2 or 3
  witness word with aa and two internal b-runs: aabbabba
  W2 = abbaabba True | W1 = aabbabba True
  E[x] = abbaabba True | E[y] = aabbabba True
  F[x] = aabbabba True | F[y] = aaabbbba False
  => NOT (1,c)-substitutable: True
L = a+ bb a+ bbb a+ with |w|_a = 5 (rigid)
  witness word with aa and two internal b-runs: aaabbabbba
  W2 = aabbaabbba True | W1 = aaabbabbba True
  E[x] = aabbaabbba True | E[y] = aaabbabbba True
  F[x] = aaabbabbba True | F[y] = aaaabbbbba False
  => NOT (1,c)-substitutable: True
skeleton languages: all sets of <= 2 skeletons of length <= 6, words <= 8
  tried: 903 | passed arity-1 check: 92
  passed AND some skeleton has two internal b-runs: 0
  passing sets with one internal b-run: 0 []
skeleton languages: all sets of <= 4 skeletons of length <= 5, words <= 7
  tried: 20853 | passed arity-1 check: 208
  passed AND some skeleton has two internal b-runs: 0
  passing sets with one internal b-run: 25 [['ab', 'aba', 'ba'], ['abb', 'abba', 'bba'], ['abbab', 'abbb', 'bbab'], ['abbb', 'abbba', 'bbba'], ['babb', 'babba', 'bbba'], ['a', 'ab', 'aba', 'ba'], ['a', 'abb', 'abba', 'bba'], ['a', 'abbab', 'abbb', 'bbab']]
```

**検査の位置づけ**：第一部の三つの違反は、示された二組 $x,y$ が共通の受理文脈 $E$ を持ち、別の文脈 $F$ で所属が食い違うことの具体例で、その言語が $(1,c)$-代入可能でないことの証明として読める。第二部は観察された文脈と長さの範囲での観察に過ぎない。

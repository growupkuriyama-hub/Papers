# R13 報告：well-nested な提示の分裂型の対（根の型 $m=\{\mathtt a\}$）— 離れた配置は殻のアンカーで閉じ、入れ子の配置は「入れ替えで生じる交差した組み合わせ」で止まる（Claude Opus 5.5, 2026-11-22）

判定ラベル（VALID / CONDITIONAL / GAP / REFUTED / OPEN / CERTIFIED FINITE）はすべて**本報告の自己判定**である。同じモデル系列（R4〜R11）の推論の型を流用していないかは §8 で点検する。

**結論（3 行）。**
1. WN な提示では、比較できない同類の重い節点の対は「殻が離れている」か「一方が他方の隙間に入れ子」のどちらかである。**離れた分裂型の対は、短い方の殻を圧縮した語をアンカーにすれば一穴の溶解が成り立ち、使える**（定理 D-hull、VALID）。
2. **入れ子の分裂型の対では、二側の族の強制は通る**（DIS2-nest・WRAP・EX2、VALID）。しかし部分木の入れ替えで生じる語は、左右の成分の組み合わせが族の並べ方とずれ、言語の上では**交差した組み合わせ**になる。WN の木の幾何からはこれを評価する関係が出ず、R10 の W2 の障害が形を変えて残る（OPEN）。組み合わせの条件 (PP) を仮定すれば数え上げは閉じる（CONDITIONAL）。$G^{\rm nest}_{d,q}$ では (PP) が言語の定義から成り立つ。
3. 肯定方向については、$a$ に係数を持つ線形の不変量を一つでも満たす言語では、$\mu_{\{\mathtt a\}}\le\mathrm{poly}(\bar\theta_G)$ となる（定理 LIN、VALID）。したがって R15 の $L_{N,d}$ を「順序の不変量と線形等式」の方向に一般化しても、超多項式の族は作れない。WN の $m=\{\mathtt a\}$ は**閉じていない**。残る障害は、入れ子の分裂型の塔での (PP) の成否だけである。

---

## 1. 読了表

リポジトリは `growupkuriyama-hub/Papers`、ブランチ `main`。2026-11-22 に `git clone --depth 1` で取得した（先頭コミット `5210bbd`。RV1 を記録した `6b3f07d` より後）。

| 資料 | 読んだ範囲 | 未読・注記 |
|---|---|---|
| `research/README.md` | 全文 | — |
| `v2/reviews/PAUSE_FALSE_ROUTES_2026-11-16.md` | 全文 | リンク先の監査原本は未読 |
| RV1 `deliverable/report.md` | **全文**（§1〜§9） | 外部文献の主張は照合していない |
| RV1 `claude_check_RV1_2026-11-22.md` | 全文 | — |
| R12 `R12_STOPPED_2026-11-22.md` | 全文 | — |
| `main.tex` 第 IV 部 | `sec:p4-resume-R9`〜`sec:p4-resume-R11`、`sec:p4-resume-RV1`（`rr:RV1-crossing`, `rr:RV1-audit`, `rr:RV1-wn`, `rem:RV1-state`）、`sec:p4-open` の全文 | `sec:p4-resume-R1`〜`R8` は未読（台帳と RV1 の要約のみ） |
| `main.tex` 第 I 部 | `def:tuple-substitutable`（注記を含む）、`lem:thickness-equivalence`（主張）、`def:uniform-polydata`、`lem:power-transfer`（主張と証明）、`op:fanout-two` とその後の段落 | `lem:thickness-equivalence` の証明は未読 |
| R10 report | §2.0〜§2.3、§3.0〜§3.5（HΞ\*・補題 D2・Φ2・系 C・§3.4・NF2 と W2 の止まる場所）の全文 | §2.4、§4 以降は未読 |
| R11 report | §2.0、§3.1〜§3.3（PNF・命題 5・系 5a/5b・系 6）、§4.1 の全文 | §2.1〜§2.6 の証明は未読（RV1 の PNF の検算を使う） |
| R15 report | §4（補題 ST、$L_{N,d}$）、§5.1〜§5.4（両文法、厚さ、最小木）の全文 | §5.5 以降は未読 |
| R9 report | §2.0、§2.2（P1〜P7）、§2.3（NF）、§3.1（HΞ）の全文。依頼の指定外だが、HΞ の記述子と補題 S を確かめるために読んだ | §2.5（貪欲な一文）は未読。RV1 の指摘をそのまま採る |
| R5 report | 命題 B4・定理 B5 の主張の行（grep で該当行のみ） | 証明は未読。本報告の定理 LIN は B4 に依存せず、自前で証明した（§5） |

**R5〜R8 の結果の使用。** 使わない。R5 の鎖（長さが 4 分の 1 以下になる最初の節点 $\mathrm{nx}$）は RV1 §3 の再構成（「最重子をたどり、初めて親段の 1/4 以下になる所」）の形で引用し、補題 1 (i) $\ell_{\mathrm{nx}(w)}\ge\ell_w/(8r)$ だけを §5 で**自分で再確認した**（$\ell_p>\ell_w/4$、$\ell_p\le\theta+r\ell_{\mathrm{nx}}$ から直ちに従う）。

---

## 3. T2(a)：入れ子の分裂型の対

### 3.0 設定 $(\Gamma_{\rm WN})$ と記号

- $\Sigma$ は族の中で固定、$c=c_\Sigma$ は内容型付け、$L\in\mathcal C_{\rm mcf}(2,c_\Sigma)$ は $\mathtt a$ の冪を含む。比べる成分は空でなく、二穴の中央も空でない。外側文脈は空でよい。一穴の合同 $x\equiv y$ は「$c(x)=c(y)$ かつ一穴の分布が等しい」、二穴の合同 $\equiv_2$ も同様（R9 §2.0、R8 補題 0）。
- $G=(V,\Sigma,P,S)$ は $L$ の reduced good な **WN** 文法、fan-out $\le2$、rank $\le r$。$v_0:=|V|$、$\theta:=\bar\theta_G$（**元**の規則厚さ）。`lem:thickness-equivalence` の (T1)（各規則の明示終端 $\le\theta$）と (T2)（各 $B$ に総長 $\le\theta$ の生成 $\omega_B$）を使う。
- $N:=\mu_{\{\mathtt a\}}(L)$、$W:=\mathtt a^N$ は $L$ の**実際の**最短の $\mathtt a$ の冪。$T$ は長さ $N$ の内容 $\{\mathtt a\}$ の語の導出のうち節点数最小のもの。高さを $h$（$\le v_0$、RV1 §3）とする。
- 節点 $u$：生成の区間 $I^1_u<I^2_u$（fan-out 2）、総長 $\ell_u$、殻 $\mathrm{hull}(u)$、隙間 $\mathrm{gap}(u)$（$I^1_u$ と $I^2_u$ の間）。重い（$\ell_u>\theta$）、非境界（殻が語の両端に触れない）は R10 §2.0 のとおり。短い生成 $\omega_u=(\omega^1_u,\omega^2_u)$、逃げ道 $e_u=\omega^1_u\mathtt a\,\omega^2_u$（fan-out 2）、重み $p_u=\ell_u+d_u-1$、類 $\mathrm{cl}(u)=c(e_u)\cup\{\mathtt a\}$、成分の類 $\mathrm{cl}_i(u)=c(\omega^i_u)\cup\{\mathtt a\}$。
- **新しい記号。** $u$ の**型の組**を $\mathrm{prof}(u):=(\mathrm{cl}_1(u),\mathrm{cl}_2(u))$ と置く（順序つき）。$C$ を $\mathrm{gap}(u)$ の中の節点の反鎖とするとき、$\{u\}\cup C$ を逃がした生まれつきの語で $u$ の殻に当たる因子の、正の $\mathtt a$ の連をすべて 1 に滑らせた語を、$u$ の**圧縮した殻** $\widehat{\mathrm{hull}}_C(u)$ と呼ぶ。$C=\varnothing$ なら $e_u$ と一致する。

**補題 3.0（WN の幾何）［VALID］.** $(\Gamma_{\rm WN})$ の成功導出で、比較できない二節点 $x,y$ の殻は、互いに素であるか、一方が他方の隙間に含まれる。さらに、$v$ と比較できず $\mathrm{gap}(v)$ と交わる節点は、成分をすべて $\mathrm{gap}(v)$ の中に持つ（**隙間の閉性**）。

*証明。* 比較できない節点の生成は互いに素な位置を占める（線形・非削除）。殻が交わるなら、一方（$y$ とする）の成分 $y_i$ が $x$ の殻に入り、$x$ の成分と素なので、$x$ は fan-out 2 で $y_i\subseteq\mathrm{gap}(x)$ である。$y$ の別の成分 $y_j$ が $\mathrm{hull}(x)$ の外にあれば、$j>i$ のとき $x_1<y_i<x_2<y_j$、$j<i$ のとき $y_j<x_1<y_i<x_2$ となり、どちらも交差である。RV1 の命題（`rr:RV1-crossing`(i)：交差は最小共通祖先の規則が ill-nested であることを意味する）により、WN では起こらない。よって $y$ の成分はすべて $\mathrm{gap}(x)$ に入る。後半：$z$ が $v$ と比較できず $\mathrm{gap}(v)$ と交われば、$z$ のある成分は $v$ の成分と素な区間で隙間と交わるので、隙間に含まれる。前半の議論から全成分が隙間に入る。∎

（`run_all.py` [E]：無作為な WN の導出木 150 本、比較できない対 362,413 組で、交差 0、隙間の閉性の違反 0［CERTIFIED FINITE］。）

**入れ子の分裂型の対（NS 対）。** 比較できない重い非境界の $K$ 節点 $x,y$（$|K\setminus\{\mathtt a\}|\ge2$）で、$\mathrm{hull}(y)\subseteq\mathrm{gap}(x)$、かつ外側 $x$ が実質 fan-out 2 で
$$K\not\subseteq\mathrm{cl}_1(x),\qquad K\not\subseteq\mathrm{cl}_2(x)$$
を満たすもの。$K\subseteq\mathrm{cl}_i(x)$ なら R11 命題 5 の射影の基準（入れ子では生まれつきの射影 $\pi(\omega^1_x)\pi(e_y)\pi(\omega^2_x)$ が $\Pi_1=\Pi'_2$ と一致する）で使える。これは RV1 が具体的な成分アンカーで回復した範囲に入る。

### 3.1 二穴の強制：三つの合同

以下 $v$ を外側、$w$ を内側（$\mathrm{hull}(w)\subseteq\mathrm{gap}(v)$）、$\mathrm{cl}(v)=\mathrm{cl}(w)=K$、両者とも $\ell\le N/16$ とする。余白は「現れる $\mathtt a$ の総数が使う生まれつきの語の $\mathtt a$ の総数を超えない」ことで、各補題で式を明示する。

**補題 DIS2-nest（成分を保った二穴の溶解）［VALID］.** $w$ が fan-out 2 で、成分の類が**元の順序のまま**含まれる、すなわち $\mathrm{cl}_1(w)\subseteq\mathrm{cl}_1(v)$ かつ $\mathrm{cl}_2(w)\subseteq\mathrm{cl}_2(v)$ とする。$g,g',y_1,y_2\ge1$、$y_1+y_2=g+g'+\ell_w+2$、$g+g'+\ell_w+5\le N-\ell_v$ なら
$$X:=(\omega^1_v\mathtt a^g\omega^1_w\mathtt a,\ \mathtt a\,\omega^2_w\mathtt a^{g'}\omega^2_v)\ \equiv_2\ Y:=(\omega^1_v\mathtt a^{y_1},\ \mathtt a^{y_2}\omega^2_v).$$

*Rect。*
- 比較組 $X,Y$。成分ごとの型は $(\mathrm{cl}_1(v),\mathrm{cl}_2(v))$ で等しい。$X$ の第 1 成分の内容は $c(\omega^1_v)\cup c(\omega^1_w)\cup\{\mathtt a\}=\mathrm{cl}_1(v)$ で、包含の仮定による。第 2 成分も同様。
- 共有文脈 $E_0=(\mathtt a^s,\mathtt a^m,\mathtt a^t)$、$s,m,t\ge1$、$s+m+t=N-\ell_v-\ell_w-g-g'-2$。
- $E_0[X]=\mathtt a^s\omega^1_v\mathtt a^g\omega^1_w\mathtt a^{m+2}\omega^2_w\mathtt a^{g'}\omega^2_v\mathtt a^t$。これは $\{v,w\}$ を逃がした生まれつきの語から得る。$\mathtt a$ の連は P1′ で、成分と隣り合う零の連は R11 の PNF (i)（RV1 §3 が検算した $\mathtt a\beta\equiv\beta\mathtt a$）で整える。射影 $\pi(\omega^1_v)\pi(\omega^1_w)\pi(\omega^2_w)\pi(\omega^2_v)$ は生まれつきの語と同じである。$\mathtt a$ の総数は $N-\ell_v-\ell_w+|\omega_v|_{\mathtt a}+|\omega_w|_{\mathtt a}$ で、生まれつきの語と一致する（加法条件 (A) の二成分版。位置の数え上げによる）。
- $E_0[Y]=\mathtt a^s\omega^1_v\mathtt a^{y_1+m+y_2}\omega^2_v\mathtt a^t$。$\{v\}$ だけの生まれつきの語から P1′ で得る。総数 $N-\ell_v+|\omega_v|_{\mathtt a}$ から $y_1+y_2=g+g'+\ell_w+2$ が出る。
- 試験文脈 $E_1=(u_0,u_1,u_2)$（$u_1\ne\varepsilon$）は任意。四語は $E_0[X],E_0[Y],E_1[X],E_1[Y]$。∎

**補題 WRAP（内側の殻のまわりの一穴の溶解）［VALID］.** 型の組の仮定はない。$C_w$ を $\mathrm{gap}(w)$ の中の反鎖（空でよい）、$\pi_0:=\widehat{\mathrm{hull}}_{C_w}(w)$ とする。$g_1,g_2\ge0$、$g_1+g_2\ge1$、$h_1,h_2\ge0$、$h_1+h_2=g_1+g_2+\ell_v$ で、余白 $g_1+g_2+\ell_v+2\le A_w$（$A_w$ は $\{w\}\cup C_w$ の生まれつきの語の $\pi_0$ の外の $\mathtt a$ の数）を満たすなら
$$x:=\omega^1_v\,\mathtt a^{g_1}\,\pi_0\,\mathtt a^{g_2}\,\omega^2_v\ \equiv\ y:=\mathtt a^{h_1}\,\pi_0\,\mathtt a^{h_2}.$$

*Rect。*
- 型：$c(x)=c(\omega_v)\cup c(\pi_0)\cup\{\mathtt a\}$、$c(y)=c(\pi_0)\cup\{\mathtt a\}$（$h_1+h_2\ge\ell_v\ge1$）。$c(\pi_0)\supseteq c(\omega_w)$ と $\mathrm{cl}(v)=K=\mathrm{cl}(w)$ から $c(\omega_v)\subseteq c(\pi_0)\cup\{\mathtt a\}$ なので等しい。
- 共有文脈 $E_0=(\mathtt a^s,\mathtt a^t)$、$s,t\ge1$。
- $E_0[x]$ は $\{v,w\}\cup C_w$ の生まれつきの語である。補題 3.0 の隙間の閉性により $C_w$ は $\mathrm{gap}(w)$ の中にあり、$v$ の隙間の残りは $\mathtt a$ だけである。$v$ の隙間の連を P1′ と PNF (i) で $g_1,g_2$ に整える。
- $E_0[y]$ は $\{w\}\cup C_w$ の生まれつきの語である。
- (A) の会計：二語の $\mathtt a$ の差は $\ell_v-|\omega_v|_{\mathtt a}$ で、$h_1+h_2=g_1+g_2+\ell_v$ と一致する。
- 試験文脈 $E_1=(P,Q)$ は任意。∎

**補題 EX2（同じ型の組の二穴の取り替え）［VALID］.** $y,y'$ は fan-out 2 の重い非境界の節点、$\mathrm{prof}(y)=\mathrm{prof}(y')$、$\delta:=\ell_{y'}-\ell_y\ge0$、$\ell_y+\ell_{y'}\le N-6$ とする。このとき
$$(\mathtt a\,\omega^1_y\mathtt a^{1+\delta},\ \omega^2_y\mathtt a)\ \equiv_2\ (\mathtt a\,\omega^1_{y'}\mathtt a,\ \omega^2_{y'}\mathtt a).$$
*Rect。* 型は $\mathrm{prof}$ が等しいので一致する。共有文脈 $E_0=(\mathtt a^s,\mathtt a^m,\mathtt a^t)$、$s+m+t=N-\ell_{y'}-3$。二語は $y$、$y'$ の孤立した配置（隙間 $m+1+\delta$ と $m+1$）である。試験文脈は任意。∎

**命題 NF-nest（二側の族の強制）［VALID。仮定 (N1)〜(N4) のもと］.**
- (N1) $v\supset w$ は上の入れ子、$\pi_0=\widehat{\mathrm{hull}}_{C_w}(w)$。
- (N2) 族 $y_1,\dots,y_M$ は fan-out 2 の重い非境界の節点で、$\mathrm{prof}(y_j)=\mathrm{prof}(v)$。
- (N3) 原型 $\Phi_L\mathtt a^{q_L}\pi_0\mathtt a^{q_R}\Phi_R\in L$、$q_0:=q_L+q_R$。
- (N4) 余白：$q_0+\sum_jp_{y_j}+(2M+2)(\theta+1)+2\le A_w$。

並べ方 $\pi$ ごとに、$Z:=\mathtt a^{\theta+1}$ として
$$x_\pi:=\Phi_L\ \omega^1_{y_{\pi_1}}Z\cdots Z\,\omega^1_{y_{\pi_M}}Z\ \omega^1_v Z\,\pi_0\,Z\,\omega^2_v\ Z\,\omega^2_{y_{\pi_M}}Z\cdots Z\,\omega^2_{y_{\pi_1}}\ \mathtt a^{g_\ell}\,\Phi_R$$
と置く。ここで $g_\ell$ は、$\mathtt a$ の総数と $\ell_v+\sum_j\ell_{y_j}$ の和が原型の $q_0$ に合うように取る（$\pi$ によらない）。このとき、すべての $\pi$ について $x_\pi\in L$ である。

*証明（内側から）。*
1. WRAP で $\omega^1_vZ\pi_0Z\omega^2_v\to\mathtt a^{h_1}\pi_0\mathtt a^{h_2}$。
2. 層 $y=y_{\pi_M}$ では、因子 $\omega^1_yZ(\mathtt a^{h_1}\pi_0\mathtt a^{h_2})Z\omega^2_y$ に EX2 を二穴の置換として使い、$(\omega^1_y,\omega^2_y)$ を $(\omega^1_v,\omega^2_v)$ に替える。中央 $Z\mathtt a^{h_1}\pi_0\mathtt a^{h_2}Z$ は空でない。$\mathtt a$ の差 $|\ell_y-\ell_v|$ は外側の連に移す。
3. 次に WRAP を使う。
4. これを外側へ繰り返し、最後に P1′ で原型へ移す。

合同は対称なので、原型から $x_\pi$ が従う。各段の WRAP の $g_1+g_2$ は高々 $q_0+\sum_jp_j+(2M+2)(\theta+1)$ で、(N4) に入る。∎

**型の組の制約について（正直な注記）。** (N2) は、族と外側の $v$ が同じ型の組を持つことを要求する。鎖の上の $K$ 節点の型の組は $4^{|\Sigma|}$ 通り以下なので、鳩の巣で族の型の組はそろえられる。しかし、その型の組を持つ $v$ が内側の $K$ 節点を包むとは限らない。DIS2-nest を使う場合も、族と $w$ の型の組がそろう必要がある。この照合の損失は §3.3 の障害とは別の、二次的な義務として残す（§9）。

### 3.2 入れ替えの段：どこで止まるか

**トークンと分離節点。** $x_\pi$ を次のトークンの列として読む。
$$\Phi_L,\ L_1,Z,\dots,Z,L_M,\ Z,\omega^1_v,Z,\pi_0,Z,\omega^2_v,Z,\ R_M,Z,\dots,Z,R_1,\ \mathtt a^{g_\ell},\Phi_R$$
ここで $L_k=\omega^1_{y_{\pi_k}}$ は**左のスロット $k$**、$R_k=\omega^2_{y_{\pi_k}}$ は**右のスロット $k$** である。トークンは $4M+8$ 個。

**補題 Sep$_L$（左の分離節点）［VALID］.** $M\ge12r+6$ なら、$x_\pi$ の任意の導出木に、左のスロットのうち完全に生成に含まれる個数 $c_L(u)$ が $M/(3r)\le c_L(u)\le2M/3$ を満たす節点 $u$ がある。

*証明。* RV1 §3 の証明を左のスロットだけに適用する。$c_L>2M/3$ で、子がすべて $\le2M/3$ の最深の節点を取る。子に引き継がれない左のスロットは、明示終端の断片（$\le2r+2$ 個、各 $\le\theta<|Z|$）か子成分の境界（$\le2r$ 個）に触れる。スロットは連続した語で、親の二成分の間には空でない隙間があるので、二成分に分かれて完全に含まれることはない。∎

**類。** 記述子を（トークン番号、スロットなら中身の番号、オフセット）とする。$\lambda$ をトークン長の最大、$\Delta:=(4M+8)(M+1)\lambda+1$ とすれば、類 $(A,d,\text{端点の記述子})$ の数は $\le2v_0\Delta^4$ である。類は、$u$ に完全に入る左のスロットの集合 $J_L$ と右のスロットの集合 $J_R$ を決める。

**入れ替えで得られる語（文脈自由性による。代入可能性は使わない）。** $\pi,\pi'$ が同じ類なら、$x_{\pi'}$ の導出で $u_{\pi'}$ の部分木を $u_\pi$ の部分木に替えた語 $\xi\in L(G)=L$ が得られる。切れたトークンは記述子の一致から元通りに組み直される。$A:=J_L\setminus J_R$、$B:=J_R\setminus J_L$、$C:=J_L\cap J_R$、$D:=$ 残りと置くと、$\xi$ のスロットの中身は次のとおりである。

| スロット $k$ | 左 $L_k$ | 右 $R_k$ |
|---|---|---|
| $k\in A$ | $\pi_k$ | $\pi'_k$ |
| $k\in B$ | $\pi'_k$ | $\pi_k$ |
| $k\in C$ | $\pi_k$ | $\pi_k$ |
| $k\in D$ | $\pi'_k$ | $\pi'_k$ |

一般に、左の並び $\sigma$ と右の並び $\tau$ を持つ同じ枠の語を $\xi(\sigma,\tau)$ と書く。族の語は $x_\pi=\xi(\pi,\pi)$ である。

**止まる場所（正確に）［OPEN］.**
- $\sigma_k\ne\tau_k$ の層を**食い違った層**と呼ぶ。内側から正規化すると、WRAP・EX2 は**左右が同じ元の層**にしか使えない。最初の食い違った層では、因子
  $$\omega^1_{y}\,Z\,(\text{正規化済みの芯})\,Z\,\omega^2_{y'}\qquad(y\ne y')$$
  が残る。
- これを評価するには、たとえば $(\omega^1_y\mathtt a^\alpha,\ \mathtt a^\beta\omega^2_{y'})\equiv_2(\omega^1_v\mathtt a^{\alpha'},\ \mathtt a^{\beta'}\omega^2_v)$ のような関係が要る。その共有文脈には、$y$ の左成分と $y'$ の右成分を組にした受理語が必要である。そのような語は生まれつきの語にも孤立した配置にもない。$\xi$ 自身を使うのは循環である。
- **WN の幾何はこの語を与えない。** $\xi$ の導出木は $x_{\pi'}$ の木に $u_\pi$ の部分木を差し込んだものである。食い違った層の左右の成分は、どの節点の二成分にもなっていない。補題 3.0 は木の節点についての主張なので、$\xi$ の成分の組み合わせには何も言わない。
- **言語の上では交差になる。** $\sigma,\tau$ が同じ多重集合の異なる並びのとき、たとえば $\sigma=(y,y')$、$\tau=(y',y)$ なら、$\xi$ は $L_yL_{y'}\cdots R_yR_{y'}$ と読める。これは $y,y'$ の**交差した配置**である。すなわち、文法が WN でも、入れ替えは言語の上の交差した組み合わせを生む。R10 §3.5 の W2 が「左右の成分が別の族の元から来た語」で止まったのと、同じ障害である。WN は木の交差を消すが、入れ替えで生じる組み合わせの交差は消さない。
- （`run_all.py` [D]：$L_{4099,16}$ で、族の並べ方の異なる組み合わせ 552 通りがすべて受理される［CERTIFIED FINITE］。この言語は交差した組み合わせを受理する。）

**何が足りないか：組み合わせの条件 (PP)。** 族 $\mathcal F=\{y_1,\dots,y_M\}$ と枠について、次を (PP) と呼ぶ。各元を高々 2 回含む並び $\sigma,\tau$ で $\xi(\sigma,\tau)\in L$ なら、
- (PP-i) $\sigma$ と $\tau$ の多重集合が等しい。
- (PP-ii) $\sum_{\sigma}p=\sum_{\mathcal F}p$。

**定理 W2-nest［CONDITIONAL：命題 NF-nest の仮定と (PP)］.** 重み $p_{y_j}$ が相異なる部分和を持ち、$M\ge12r+6$ なら
$$v_0\ \ge\ \frac{\min_{M/(3r)\le k\le2M/3}\binom Mk}{2\Delta^4}\ \ge\ \frac{2^{M/(3r)}}{2\Delta^4}.$$

*証明。* 補題 Sep$_L$ の節点で類を作る。同じ類の $\pi,\pi'$ から上の $\xi$ を得る。$\sigma$ の多重集合は $\pi(A)+\pi(C)+\pi'(B)+\pi'(D)$、$\tau$ の多重集合は $\pi(B)+\pi(C)+\pi'(A)+\pi'(D)$ である。
- (PP-i) から $\pi(A)+\pi'(B)=\pi(B)+\pi'(A)$。$\pi(A)\cap\pi(B)=\varnothing$（$\pi$ は単射、$A\cap B=\varnothing$）なので、$x\in\pi(A)$ は $\pi'(A)$ に入る。大きさが等しいので $\pi(A)=\pi'(A)$。
- (PP-ii) から $\sum_{\pi(A)\cup\pi(C)}p+\sum_{\pi'(B\cup D)}p=\sum_{\mathcal F}p=\sum_{\pi'(A\cup B\cup C\cup D)}p$。$\pi(A)=\pi'(A)$ を引くと $\sum_{\pi(C)}p=\sum_{\pi'(C)}p$。相異なる部分和から $\pi(C)=\pi'(C)$。
- よって $\pi(J_L)=\pi(A)\cup\pi(C)=\pi'(J_L)$。$k:=|J_L|=c_L(u)$ とすると、一つの類の並べ方は $k!(M-k)!$ 通り以下である。類の数は $\ge\binom Mk\ge2^{M/(3r)}$（RV1 §3 と同じ評価）。∎

**注意。**
- (PP) が成り立つ二つの典型がある。
  - **鏡像型の言語**（左右の対応が言語の制約で強制される。たとえばブロックの長さが鏡像に一致するもの）では、$\sigma\ne\tau$ の語が受理されないので、(PP-i) は自明に成り立ち、(PP-ii) は正規化と剛性から出る。
  - **線形の不変量を持つ言語**（$L_{N,d}$ など）では、和の等式から出る。ただし後者は定理 LIN（§5）でもともと多項式なので、定理 W2-nest が新しく扱うのは前者の型である。
- (PP) は、代入可能性・WN・最短性から導けていない［OPEN］。

### 3.3 最初の試験：$G^{\rm nest}_{d,q}$ の $(\mathtt{bb},\mathtt{cc})$

- **文法と WN。** R15 §5.1 の全規則を `run_all.py` [B] で書き下した。平坦化した変数列は次のとおりである。
  - $A$ 部：$x_{1}$ だけ、または $\mathtt a x_1$、$x_1\mathtt a$、$\mathtt b x_1\mathtt c$
  - $B_i\to(X_1Y_1,\,Y_2X_2)$ の変数列は $X_1Y_1Y_2X_2$
  - 開始規則 $\mathtt aX_1\mathtt aX_2\mathtt a$ の変数列は $X_1X_2$
  
  すべて WN である。cross 版は $B_i$（$i\ge1$）の $q$ 本だけが ill-nested である。$(d,q)=(4,1),(6,1),(4,2)$ で $L(G)=L_{N,d}$ を全列挙で確かめ、元厚さ $\bar\theta_G=2^{q+1}+d+1$ を内側と外側の最短長から厳密に計算した［CERTIFIED FINITE］。
- **最小木の対。** $(d,q)=(64,4)$：$N=1027$、$\bar\theta_G=97$、最小木の節点 32。一つの $B_2$ の下の兄弟 $X,Y$（ともに $B_1$）について、
  - 区間は $X=[1,65)\cup[962,1026)$、$Y=[65,129)\cup[898,962)$（0 始まり）
  - 長さは各 $128>97$（重い）、非境界
  - $\mathrm{hull}(Y)=\mathrm{gap}(X)$（**内側が fan-out 2 でちょうど埋める入れ子**）
  - 短い生成はともに $(\mathtt{bb},\mathtt{cc})$
  - $\mathrm{prof}=(\{\mathtt a,\mathtt b\},\{\mathtt a,\mathtt c\})$（成分の類は元の順序のまま包含する。分裂型、$K=\{\mathtt a,\mathtt b,\mathtt c\}$）
  
  さらに、最小木の比較できない $B$ 節点の対は**すべて**隙間の入れ子で、殻は包含で全順序になる（塔。[B]）。
- **作った関係が言語の定義から成り立つこと［VALID：直接の証明］.** 任意の $d,q$ で、$X=(\mathtt{bb}\mathtt a^g\mathtt{bb}\mathtt a,\ \mathtt a\mathtt{cc}\mathtt a^{g'}\mathtt{cc})$、$Y=(\mathtt{bb}\mathtt a^{y_1},\ \mathtt a^{y_2}\mathtt{cc})$、$y_1+y_2=g+g'+2d+2$（$\ell_w=2d$）とする。任意の $E=(u_0,u_1,u_2)$ について、次の三つが成り立つ。
  - (1) $\pi(E[X])=\pi(u_0)\mathtt b^4\pi(u_1)\mathtt c^4\pi(u_2)$、$\pi(E[Y])=\pi(u_0)\mathtt b^2\pi(u_1)\mathtt c^2\pi(u_2)$。$k\ge1$ について $\pi(u_0)\mathtt b^k\pi(u_1)\mathtt c^k\pi(u_2)\in\mathtt b^*\mathtt c^*$ は「$\pi(u_0)\in\mathtt b^*$、$\pi(u_1)\in\mathtt b^*\mathtt c^*$、$\pi(u_2)\in\mathtt c^*$」と同値で、$k$ によらない。
  - (2) $|\cdot|_{\mathtt b}-|\cdot|_{\mathtt c}$ は $X,Y$ どちらでも文脈の値のまま。
  - (3) $|\cdot|_{\mathtt a}+d|\cdot|_{\mathtt b}$ への寄与は $g+g'+2+4d=y_1+y_2+2d$。
  
  よって $E[X]\in L\iff E[Y]\in L$ である。WRAP（$\mathtt{bb}\mathtt a^{g_1}\pi_0\mathtt a^{g_2}\mathtt{cc}\equiv\mathtt a^{h_1}\pi_0\mathtt a^{h_2}$、$h_1+h_2=g_1+g_2+2d$）と EX2 も同じ計算で成り立つ。
  
  補助として、$L_{19,4}$（$B_0$ の段、$(\mathtt b,\mathtt c)$）で、DIS2-nest 41 例・WRAP 40 例（$g_1=0$ または $g_2=0$、すなわちちょうど埋める形を含む）・EX2 3 例を、全文脈の分布の一致として確かめた。一穴の DIS は型が $\{\mathtt a,\mathtt b,\mathtt c\}\ne\{\mathtt a,\mathtt b\}$ で適用できないことも確かめた［CERTIFIED FINITE、[C]］。
- **(PP) の成否。** $L_{N,d}$ では、$\xi(\sigma,\tau)\in L\iff\sum_\sigma k=\sum_\tau k=\sum_{\mathcal F}k$（$k_y=|\omega^1_y|_{\mathtt b}$）である。比 $\ge4$ の族（RV1 の鎖はこの比を持つ）では、高々 2 回の多重集合が和で決まるので、(PP-i)(PP-ii) が成り立つ。[D] は比 4 の族 $\{2,8,32,128\}$ で、受理がちょうど和の条件で決まり、受理される並びの組は族の並べ方どうしだけであることを確かめた。比 2 の族では、和が等しく多重集合が異なる組が 288 組現れる（ただし和が $\sum_{\mathcal F}k$ と異なるので受理はされない）［CERTIFIED FINITE］。
- **この試験の意味。** $G^{\rm nest}$ では族の大きさが $M\le q=O(\log\bar\theta_G)$ なので、定理 W2-nest の下界は自明（負）で、矛盾は出ない。これは $N=O(\bar\theta_G^{\,2})$ と整合する。試験が示すのは「作った二穴の関係と (PP) が、実在する WN の分裂型の対で実際に成り立つ」ことまでである。

### 3.4 T2(a) の判定

| 項目 | 判定 |
|---|---|
| 補題 3.0（WN の幾何、隙間の閉性） | VALID |
| DIS2-nest・WRAP・EX2 | VALID（Rect・型・共有文脈・(A) を明示） |
| 命題 NF-nest（二側の族の強制） | VALID（仮定 (N1)〜(N4)。(N2) の型の組の照合は二次的な義務） |
| 入れ替えの段（W2-nest） | **OPEN**。止まる場所は食い違った層。入れ替えが言語の上の交差した組み合わせを生む |
| 定理 W2-nest | CONDITIONAL（(PP)） |
| $G^{\rm nest}$ での試験 | 関係は言語の定義から VALID、有限検査は CERTIFIED FINITE。(PP) は比 $\ge4$ の族で成り立つ |

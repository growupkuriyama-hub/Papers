# R13 報告：well-nested な提示の分裂型の対（根の型 $m=\{\mathtt a\}$）— 離れた配置は殻のアンカーで閉じ、入れ子の配置は「入れ替えで生じる交差した組み合わせ」で止まる（Claude Opus 5.5, 2026-11-22）

判定ラベル（VALID / CONDITIONAL / GAP / REFUTED / OPEN / CERTIFIED FINITE）はすべて**本報告の自己判定**である。同じモデル系列（R4〜R11）の推論の型を流用していないかは §8 で点検する。

**結論（3 行）。**
1. WN な提示では、比較できない同類の重い節点の対は「殻が離れている」か「一方が他方の隙間に入れ子」のどちらかである。**離れた分裂型の対は、短い方の殻を圧縮した語をアンカーにすれば一穴の溶解が成り立ち、使える**（定理 D-hull、VALID）。
2. **入れ子の分裂型の対では、二側の族の強制は通る**（DIS2-nest・WRAP・EX2、VALID）。しかし部分木の入れ替えで生じる語は、左右の成分の組み合わせが族の並べ方とずれ、言語の上では**交差した組み合わせ**になる。WN の木の幾何からはこれを評価する関係が出ず、R10 の W2 の障害が形を変えて残る（OPEN）。組み合わせの条件 (PP) を仮定すれば数え上げは閉じる（CONDITIONAL）。$G^{\rm nest}_{d,q}$ では (PP) が言語の定義から成り立つ。
3. 肯定方向については、$a$ に係数を持つ線形の不変量を一つでも満たす言語では、$\mu_{\{\mathtt a\}}\le\mathrm{poly}(\bar\theta_G)$ となる（定理 LIN、VALID）。したがって R15 の $L_{N,d}$ を「順序の不変量と線形等式」の方向に一般化しても、超多項式の族は作れない。WN の $m=\{\mathtt a\}$ は**閉じていない**。主な障害は、入れ子の分裂型の塔での (PP) の成否である（二次的に、型の組の照合が残る）。

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

## 2. T1：枠組みの確定

設定は §3.0 の $(\Gamma_{\rm WN})$ から WN を外したもの $(\Gamma)$ とする。定理 A′ に WN は要らない。WN は系 6′ でだけ使う。

### 2.1 定義：量化つきの使える対 $(\mathrm U^q)$

**定数。**
- $\lambda_*:=10(h+1)(r+1)(\theta+1)$ と置く。RV1 §3 の短い原型の補題は $|\Phi_L|+|\Phi_R|=O(hr(\theta+1)+\theta)$、$q_0-q_*=O(hr+h\theta)$ を与え、数えると $\le9(h+1)(r+1)(\theta+1)$ に収まる。圧縮した殻のアンカー（§4）はさらに $\theta$ を足しても $\lambda_*$ 以下である。
- $M_0$ を、$M\ge12r+6$ かつ $2^{M/(3r)}>2v_0\bigl[(4M+10)(M+1)\cdot3\lambda_*+1\bigr]^4$ を満たす最小の $M$ とする。$M_0=O_r(\log(v_0\theta+2))$ である。

**族。** $u$ を $\ell_u\le N/16$ の重い非境界の強制節点、$K$ を類とする。$u$ から始まる長さ 4 分の 1 の鎖（RV1 §3：最重子をたどり初めて親段の $1/4$ 以下になる節点）の上の $K$ 節点 $y_1,\dots,y_M$（$M=M_0$）を **$K$ 族** $\mathcal F$ と呼ぶ。鎖の上では $\ell_{y_{j+1}}\le\ell_{y_j}/4$ なので、$\ell\ge2M$ の範囲で重み $p_j=\ell_{y_j}+d_{y_j}-1$ は比 4 で超増加し、部分和は相異なる。族の元は互いに比較できてよい。

**目標の残差。** 比較できない重い非境界の $K$ 節点の組 $(v,w)$ に対し、
$$q_*:=p_w+(M+1)(\theta+1)+\textstyle\sum_jp_j+1,\qquad G_*:=q_*+\lambda_*+\textstyle\sum_jp_j$$
と置く。

**定義 $(\mathrm U^q)$。** $(v,w)$ が $\mathcal F$ に対して**使える**とは、次の (U1)〜(U4) をすべて満たすことをいう。
- **(U1) 短いアンカー。** 語 $\pi_0$ があって $|\pi_0|\le\lambda_*$、$c(e_w)\subseteq c(\pi_0)\cup\{\mathtt a\}$。$\pi_0$ は $v$ の**具体的な**部分（成分、または §4 の圧縮した殻）として与える。
- **(U2) DIS。** $1\le g\le G_*$ のすべての $g$ で $\pi_0\mathtt a^ge_w\mathtt a\equiv\pi_0\mathtt a^{g+p_w+1}$（鏡像でもよい）。各 $g$ は一つの Rect で与える。比較組 $x=\pi_0\mathtt a^ge_w\mathtt a$、$y=\pi_0\mathtt a^{g+p_w+1}$、型は $c(\pi_0)\cup\{\mathtt a\}$。共有文脈 $E_0$ の二語はどちらも生まれつきの語から P1′ と PNF (i)（必要なら COM）で得たもので、$\mathtt a$ の総数は加法条件 (A)（逃がした節点の長さを位置の数え上げで差し引く）を満たす。試験文脈は任意。
- **(U3) 短い原型。** $\Phi_L\pi_0\mathtt a^{q_0}\Phi_R\in L$、$q_*\le q_0\le q_*+\lambda_*$、$|\Phi_L|+|\Phi_R|\le\lambda_*$。
- **(U4) 余白。** $q_0+\sum_jp_j\le N-1$、すべての逃げ道で $N-p\ge3$、$p_j+p_w\le N-2$。

**仮定 $(\mathrm U^q)$。** 非 $\mathtt a$ の文字を二つ以上持つ類 $K$ と、上のような $u$ について、$u$ の部分木に比較できない重い $K$ 節点が二つあれば、$u$ の鎖の**任意の** $K$ 族 $\mathcal F$ に対して、$u$ の部分木に $\mathcal F$ に対して使える組 $(v,w)$ がある。

**入れ子の変種 $(\mathrm U^q_{\rm nest})$。** (U1)〜(U3) の代わりに、命題 NF-nest の (N1)〜(N4)（$\pi_0=\widehat{\mathrm{hull}}(w)$、$|\pi_0|\le\lambda_*$、原型の長さ $\le\lambda_*$、$q_0\le q_*+\lambda_*$）と、§3.2 の組み合わせの条件 (PP) が成り立つことをいう。

**R10 の (U) との違い。** R10 の (U) は (Ξ2\*)(Ξ3\*) の**存在**だけを要求し、$\Phi$ と $g_\ell$ の長さを量化していなかった（RV1 の GAP）。$(\mathrm U^q)$ は、族・残差・アンカー・原型・DIS の範囲をすべて固定してから存在を問う。

### 2.2 定理 A′［VALID（自己判定）。RV1 §3 の再構成を引用。変更点のみ証明］

> **定理 A′.** $(\Gamma)$（reduced good、fan-out $\le2$、rank $\le r$。WN は不要）で、非 $\mathtt a$ の文字を二つ以上持つ各類について $(\mathrm U^q)$ または $(\mathrm U^q_{\rm nest})$ が成り立てば、
> $$\mu_{\{\mathtt a\}}(L)\le(v_0\theta)^{O(b\,r\log r)}\qquad(b\le2^{|\Sigma|-1}\text{ は類の数})$$
> である。とくに固定した $r,\Sigma$ で $(\|G\|,\bar\theta_G)$ の多項式である。

*証明（RV1 §3「量化と帰納」からの変更点）。*
1. **単一文字の類。** RV1 の「使える対の構成」（射影がその文字の冪になり、具体的な成分アンカーが取れる）をそのまま使う。私は読み通しただけで、独立には再証明していない。
2. **非 $\mathtt a$ の文字を二つ以上持つ類。** 「その部分木に比較不能な同類対があれば上で作った短い原型・DIS と HΞ\*」の段を、$(\mathrm U^q)$ の組に置き換える。$(\mathrm U^q)$ の長さの量化により、記述子の長さの母数は $\lambda\le3\lambda_*$（$|\pi_0|$、$|\Phi|$、$g_\ell=q_0-p_w-(M+1)(\theta+1)-\sum p_j\le\lambda_*+1$、トークン）となる。RV1 の HΞ\* から $v_0\ge2^{M_0/(3r)}/(2\Delta^4)$ が出て、$M_0$ の定義に反する。
3. **入れ子の変種。** $(\mathrm U^q_{\rm nest})$ の場合は、HΞ\* の代わりに定理 W2-nest（§3.2）を使う。トークン数 $4M+8$ で $\Delta\le(4M+10)(M+1)\lambda+1$ となり、$M_0$ の定義にこの形を入れてある。
4. **残り。** 類の数による帰納、根からの評価、$\Lambda_{\{\mathtt a\}}\le N$ は RV1 と同じである。段の数は $b(M_0-1)+1$、一段の損失は $2hr$ 倍以下である。指数の評価は $(8r)^{O(bM_0)}(2hr)^b=(v_0\theta)^{O(br\log r)}$。∎

**(U^q) が自動的に成り立つ場合（以後のラウンドで引用してよい形）。**
- (a) 単一文字の類（R11 定理 1。RV1 が具体的なアンカーで回復）。
- (b) 組の一方が実質 fan-out 1、または入れ子で外側の成分が $K$ を含む（R10 D1/D2、R11 命題 5・系 5a。RV1 の「同射影・同型の対」への弱め）。
- (c) **WN で殻が互いに素な組**（本報告の定理 D-hull、§4）。

### 2.3 系 6′（WN 版の残り）［VALID（自己判定）。定理 A′、補題 3.0、定理 D-hull、R11 命題 5 に依存］

> **系 6′.** $(\Gamma_{\rm WN})$ で $\mu_{\{\mathtt a\}}$ が定理 A′ の上界を超えるなら、次をすべて満たす重い非境界の強制節点 $u$（$\ell_u\ge N/\mathrm{poly}$）と類 $K$ がある。
> 1. $|K\setminus\{\mathtt a\}|\ge2$ で、$K$ は $u$ の鎖の最初の $b(M_0-1)+1$ 節点に $M_0$ 回以上現れる。
> 2. $u$ の部分木に、比較できない重い $K$ 節点がある。
> 3. **（塔）** $u$ の部分木の重い $K$ 節点の殻は、包含について**全順序**をなす。比較できない二節点は、必ず一方が他方の隙間に入れ子である。殻が互いに素な比較できない対は一つもない。
> 4. **（分裂）** 入れ子の対 $\mathrm{hull}(y)\subseteq\mathrm{gap}(x)$ では、外側 $x$ が実質 fan-out 2 で、$K\not\subseteq\mathrm{cl}_1(x)$ かつ $K\not\subseteq\mathrm{cl}_2(x)$。内側 $y$ の fan-out と型の組には制約がない。
> 5. $(\mathrm U^q_{\rm nest})$ が成り立たない。すなわち、型の組の照合 (N2)、余白 (N4)、組み合わせの条件 (PP) のどれかが破れる。

**配置ごとに、どの成分の類が $K$ を含まないか。**

| 配置 | 残るか | 理由 |
|---|---|---|
| 離れた配置（兄弟） | 残らない | 定理 D-hull。圧縮した殻のアンカーは成分の類を使わない |
| 離れた配置（祖先が異なる） | 残らない | 同上。最小共通祖先の規則は使わない |
| 入れ子、外側のある成分が $K$ を含む | 残らない | R11 命題 5（$\Pi_1=\Pi'_2=$ 生まれつきの射影） |
| 入れ子、外側の両成分が $K$ を含まない | **残る** | $\mathrm{cl}_1(x)\not\supseteq K$、$\mathrm{cl}_2(x)\not\supseteq K$。§3 |
| 交差 | 起こらない | WN（`rr:RV1-crossing`） |

*証明。* 定理 A′ の証明で、使える組がないのに比較できない $K$ 対がある場所 $(u,K)$ を取る（R10 系 C・R11 系 6 と同じ）。補題 3.0 により、比較できない対は殻が互いに素か入れ子である。
- 互いに素なら定理 D-hull で使えるので、3 が従う。比較できる対では子孫の殻が祖先の殻に入るので、殻は全順序になる。
- 入れ子で外側の成分が $K$ を含めば使えるので、4 が従う。
- 5 は定理 A′ の仮定の否定である。∎

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

---

## 4. T2(b)：離れた配置

**結論：WN では、殻が互いに素な比較できない同類の対は、分裂型でも使える。** 道具は R10・RV1 の成分アンカーではなく、**殻を圧縮した語**をアンカーにすることである。成分の類が $K$ を含むかどうかは問題にならない。兄弟か、祖先が異なるかも関係しない。

> **定理 D-hull［VALID（自己判定）。RV1 の短い原型の補題、補題 3.0、R9 P1′・P3（COM）に依存］.** $(\Gamma_{\rm WN})$ で、$x,y$ を比較できない重い非境界の $K$ 節点とし、殻が互いに素で、$\ell_x,\ell_y\le N/16$ とする。$v\in\{x,y\}$ を $|\mathrm{hull}(v)|\le N/2$ を満たす方（どちらかは必ず満たす）、$w$ を他方とする。$N\ge N_1:=C(M_0+1)(\theta+1)+C\lambda_*$（$C$ は絶対定数）なら、$(v,w)$ は $u$ の鎖の任意の $K$ 族 $\mathcal F$ に対して $(\mathrm U^q)$ の意味で使える。

*証明。* $w$ が $v$ の右にあるとする（左なら鏡像）。

**(U3) と (U1)：アンカーの構成。**
- RV1 の短い原型の補題を、節点 $v$、成分 $i=d_v$（最後の成分）、守る位置 $\beta:=$ $\mathrm{hull}(v)$ の直後の位置に適用する。$\beta$ は非境界性により実在し、$v$ の枠の外にある。目標は $q_*$ で、$q_*+6hr+8\le N-\ell_v$ は $N\ge N_1$ から従う。
- 出力は $\Phi_L\,\omega^{d_v}_v\,\mathtt a^{q_0}\Phi_R\in L$、$0\le q_0-q_*\le\lambda_*$、$|\Phi_L|+|\Phi_R|\le\lambda_*$ である。
- $\Phi_L$ の末尾は $\omega^1_v\,\Gamma$ で、$\Gamma$ は $v$ の隙間に当たる部分である。補題の構成では、$\Gamma$ は次のものだけからなる。
  - 置き換えた木のうち隙間に入るもの（集合 $C_{\rm gap}$）の短い組の断片
  - 正の連ごとに 1 個残した $\mathtt a$（「ほかの正の連に各 1 字を残し」）
  
  置き換えた木はどれも $v$ と比較できない。補題 3.0 の隙間の閉性により、隙間と交わる木は全成分が隙間に入る。祖先の明示終端で隙間に落ちるものは $\mathtt a$ のまま連に入る。
- そこで $\pi_0:=\omega^1_v\Gamma\omega^{2}_v$（fan-out 1 なら $\pi_0=\omega_v$）、$\Phi'_L:=\Phi_L$ から末尾 $\omega^1_v\Gamma$ を除いたもの、と置く。原型は $\Phi'_L\pi_0\mathtt a^{q_0}\Phi_R\in L$ となる。
- $|\pi_0|\le|\Phi_L|+\theta\le\lambda_*$（この $\lambda_*$ は §2.1 の定義で $\theta$ の分を含めてある）。
- $c(\pi_0)\supseteq c(\omega_v)$ なので $c(\pi_0)\cup\{\mathtt a\}\supseteq\mathrm{cl}(v)=K\supseteq c(e_w)$。

**(U2)：DIS の共有文脈。**
- $\{v\}\cup C_{\rm gap}$ と $\{v,w\}\cup C_{\rm gap}$ は反鎖である。$C_{\rm gap}$ の木は $\mathrm{gap}(v)$ の中、$w$ は $\mathrm{hull}(v)$ の外にあるので、祖先関係はありえない。よって両方の生まれつきの語 $N_1,N_2\in L$ が得られる（文脈自由性）。
- $N_1$ で $\mathrm{hull}(v)$ に当たる因子の正の連を 1 に滑らせたものは、$\pi_0$ そのものである。$\Gamma$ の断片の位置と、連が正か零かは $W$ の位置だけで決まり、原型と同じだからである。`run_all.py` [G] はこの一致と (A) の会計を無作為な WN 木の 929 対で確かめた［CERTIFIED FINITE］。
- $N_2$ では、$\mathrm{hull}(v)$ と $\mathrm{hull}(w)$ の外はすべて $\mathtt a$ で、左外の連は $\ge1$、$w$ の右の連も $\ge1$ である（非境界）。$w$ の隙間は $\mathtt a$ だけなので、1 に滑らせて $e_w$ を連続にする。二つの殻の間の連が 0（隣接する兄弟など）なら、COM（$\mathtt ae_w\equiv e_w\mathtt a$、$w$ の孤立した配置から。$N-p_w\ge3$）で右から 1 個移す。
- こうして $E_0=(\mathtt a,\ \mathtt a^{t_0})$ に対し、次の二語が得られる。
  $$E_0[x]=\mathtt a\,\pi_0\,\mathtt a^ge_w\mathtt a\,\mathtt a^{t_0}\in L,\qquad E_0[y]=\mathtt a\,\pi_0\,\mathtt a^{g+p_w+1}\mathtt a^{t_0}\in L.$$
  $t_0\ge1$ は $\mathtt a$ の総数から決まる。二語の差は $\ell_w-|\omega_w|_{\mathtt a}=p_w+1-|e_w|_{\mathtt a}$ で、(A) を満たす。
- **範囲。** $N_2$ の $\mathtt a$ の総数 $A_2$ は、$\mathrm{hull}(v)$ の外で $w$ の成分以外の位置をすべて含むので、$A_2\ge N-|\mathrm{hull}(v)|-\ell_w\ge N/2-N/16=7N/16$ である。$g$ は $A_2-|\pi_0|_{\mathtt a}-|e_w|_{\mathtt a}-3$ まで取れる。
- 一方、RV1 の鎖の評価 $p_w\le N/16+1$、$\sum_jp_j\le N/12+M$ から
  $$G_*\le2\Bigl(\frac N{16}+\frac N{12}\Bigr)+2(M+1)(\theta+1)+2\lambda_*+O(M)=\frac{7N}{24}+O\bigl((M+1)(\theta+1)+\lambda_*\bigr)$$
  で、$7/24<7/16$ なので $N\ge N_1$ で収まる。
- 型は $c(\pi_0)\cup\{\mathtt a\}$ で等しい（上記）。試験文脈は任意。これで (U2) の各 Rect（比較組・型・$E_0$・$E_1$・四語）がそろう。

**(U4)。** RV1 と同じく、$q_0+\sum p_j\le N/2<N-1$ である。

**剛性の Rect（HΞ\* が使う）。** $x=(\mathtt a^{q'})$、$y=(\mathtt a^q)$、$E_0=(\Phi'_L\pi_0,\Phi_R)$、$E_1=(\varepsilon,\mathtt a^{N-q'})$、$q<q'\le N$。四語は仮定の二語、$W$、$\mathtt a^{N-q'+q}$ である。∎

**兄弟と祖先が異なる場合の区別。**
- 兄弟（同じ規則の二つの子で、殻が互いに素）では、二つの殻が直接隣接することがある（例：$(X_1\mathtt aX_2Y_1\mathtt aY_2)$）。このとき $N_2$ で間の連が 0 になり、COM が必要になる。上の証明はこれを含む。
- 祖先が異なる場合は、間に別の部分木の $\mathtt a$ が入るだけで、証明は同じである。
- 最小共通祖先の規則は一度も使わない。この点で R10 の D1/D2（成分の左右の順と内容を使う）と異なる。

**WN をどこで使うか。** 隙間の閉性（補題 3.0）だけである。non-WN では、$v$ の隙間と外にまたがる節点 $z$（$v$ と交差する）がありうる。その場合、$\pi_0$ に入る断片を作る木の他方の成分が $\mathrm{hull}(v)$ と $\mathrm{hull}(w)$ の間に落ち、$N_2$ の「外は $\mathtt a$ だけ」が崩れる。non-WN の離れた配置は本報告では扱わない（OPEN。交差の補修と組で扱うべき）。

**R10・R11 の分類との関係。** R10 系 C は「D で両方が実質 fan-out 2 で、$K\not\subseteq\mathrm{cl}_2(\text{左})$ かつ $K\not\subseteq\mathrm{cl}_1(\text{右})$」を (R2) として残し、R11 系 6・RV1 もこれを (R2\*) に含めた。定理 D-hull により、WN ではこの部分が消える。

---

## 5. T2(c)：肯定方向の候補

肯定の答え（LG が境界）には、WN の提示で、$\mu_{\{\mathtt a\}}$ が $(\|G\|,\bar\theta_G)$ の超多項式になる族が要る。系 6′ により、その族は §3 の入れ子の分裂型の塔で重みを運ばなければならない。R15 の $L_{N,d}$ の一般化を、二つの定理で検討した。

### 5.1 補題 S と定理 LIN［VALID（自己判定）。R5 B4/B5 に依存しない独立の証明］

> **補題 S.** $k,\theta'\ge1$、$\mathbf w\in\mathbb R^k$、$\mathbf n_1,\dots,\mathbf n_t\in\mathbb Z^k_{\ge0}$、$|\mathbf n_s|_1\le\theta'$ とする。$\Delta_s:=\mathbf w\cdot\mathbf n_s$ が $\Delta_1\ge1$、$\Delta_{s+1}\ge4\Delta_s$ を満たすなら、$t\le k\,g$ である。ここで $g$ は $4^g>\frac43\theta'^k$ を満たす最小の整数で、$g\le k\log_4\theta'+2$。

*証明。* $t\ge kg+1$ と仮定し、$s_i:=1+ig$（$0\le i\le k$）を取る。$k+1$ 個の $\mathbf n_{s_i}\in\mathbb Q^k$ は一次従属である。極小な従属部分集合 $I$ を取ると階数は $|I|-1=:\rho$ で、階数 $\rho$ の $\rho$ 行を選べる。余因子のベクトル（$\rho\times\rho$ 小行列式）が非零の整数の従属関係 $\sum_{i\in I}c_i\mathbf n_{s_i}=0$ を与え、すべての $c_i\ne0$ である。Hadamard の不等式から $|c_i|\le\prod\|\text{列}\|_2\le\theta'^{\rho}\le\theta'^k=:H$。内積を取ると $\sum c_i\Delta_{s_i}=0$。$j:=\max I$ とすると、
$$|c_j|\Delta_{s_j}\ge\Delta_{s_j}>H\Delta_{s_j}/(4^g-1)\ge H\sum_{i<j}\Delta_{s_i}\ge\Bigl|\sum_{i<j}c_i\Delta_{s_i}\Bigr|$$
となり矛盾する。$4^g>\frac43H$ は $H\ge1$ のとき $4^g>H+1$ を含む。∎
（[F]：$k=1,2$、$\theta'\le5$、整数の重み $[-4,4]^k$ の総当たりで、比 4 の最長鎖が上界以下［CERTIFIED FINITE］。）

> **定理 LIN.** $L\subseteq\Sigma^+$ に、$\mu\in\mathbb Q^\Sigma$（$\mu_{\mathtt a}\ne0$）と、内容ごとの定数 $z_{c}$ があって、
> $$\forall w\in L:\ \langle\mu,\Psi(w)\rangle=z_{c(w)}$$
> が成り立つとする（内容ごとの線形の不変量。$\Psi$ は Parikh 写像）。$G$ が $L$ の reduced good な任意の fan-out、rank $\le r$ の提示なら、
> $$\mu_{\{\mathtt a\}}(L)\le\theta+8r\theta(8r)^{T},\qquad T:=2^{|\Sigma|}(|\Sigma|+1)\bigl((|\Sigma|+1)\lceil\log_4(\theta+1)\rceil+2\bigr),\quad\theta=\bar\theta_G.$$
> とくに、固定した $\Sigma,r$ で $\bar\theta_G$ の多項式である（$\|G\|$ にもよらない）。

*証明。*
- $W=\mathtt a^N$ の任意の導出、任意の非根の節点 $u$ を取る。$W':=W[u\leftarrow\omega_u]\in L(G)=L$（文脈自由性）で、$\Psi(W')=\Psi(W)-\ell_u\mathbf e_{\mathtt a}+\Psi(\omega_u)$ である。不変量から
  $$\ell_u=\mathbf w\cdot\Psi(\omega_u)+\beta_{c(W')},\qquad\mathbf w:=\mu/\mu_{\mathtt a},\ \beta_c:=(z_{\{\mathtt a\}}-z_c)/\mu_{\mathtt a}.$$
  $\mathbf n_u:=(\Psi(\omega_u),1)\in\mathbb Z^{|\Sigma|+1}_{\ge0}$、$|\mathbf n_u|_1\le\theta+1$、$\mathbf w'_c:=(\mathbf w,\beta_c)$ と置けば $\ell_u=\mathbf w'_{c(W')}\cdot\mathbf n_u$。
- 根の子 $c_0$ から鎖 $w_0=c_0$、$w_{i+1}=\mathrm{nx}(w_i)$ を $\ell_{w_i}>8\theta$ の間続ける。補題 1 (i)：親 $p$ は $\ell_p>\ell_w/4$、$\ell_p\le\theta+r\ell_{\mathrm{nx}}$ なので、$\ell_{\mathrm{nx}(w)}\ge\ell_w/(8r)$（$\ell_w>8\theta$ で再確認）。
- $\ell_{w_i}\ge4\ell_{w_{i+1}}$ なので、$c(W'_{w_i})$ の値（$\le2^{|\Sigma|}$ 通り）ごとの部分列を逆順に並べると、比 4 の列になる。補題 S（$k=|\Sigma|+1$、$\theta'=\theta+1$）で、各部分列の長さは $\le(|\Sigma|+1)((|\Sigma|+1)\lceil\log_4(\theta+1)\rceil+2)$。よって鎖の長さは $\le T$。
- $\ell_{c_0}\le(8r)^T\cdot8\theta$。根は明示終端 $\le\theta$ と子 $\le r$ 本なので、$N\le\theta+8r\theta(8r)^T$。∎

**意味と範囲。**
- この定理は、代入可能性も WN も最短性も使わない。$a$ を含む内容ごとの線形の不変量だけで多項式になる。
- R15 の $L_{N,d}$（$\mu=(1,d,0)$）、RV1 §5 の交差する候補（$\mu=(1,d,d)$）、RV1 の P5 の反例 $\#\mathtt a+3\#\mathtt b=12+[\mathtt b\in c(w)]$（内容ごとの定数）は、どれもこの形である。$N=O(\bar\theta_G^{\,2})$ という以前の個別の計算は、この定理の特殊例として説明がつく。[F] は $G^{\rm nest}_{64,4}$ の全 $B$ 節点で $\ell_u=d|\omega_u|_{\mathtt b}$ を確かめた。
- R5 の定理 B5 は「一つの周期枠の中の逃げ道の欠損が符号付き加法的」という仮定から同種の結論を出していた（私は B5 の証明を再確認していない）。定理 LIN は、仮定を言語全体の内容ごとの不変量に置き、補題 S を自前で証明した版である。

### 5.2 命題 NL：順序の不変量のもとでは、非線形の会計は代入可能性と両立しない［VALID（自己判定）］

$f:\mathbb Z_{\ge0}\to\mathbb Z$、$f(0)=0$ とし、
$$L_f:=\{w\in\{\mathtt a,\mathtt b,\mathtt c\}^+:\pi(w)\in\mathtt b^*\mathtt c^*,\ |w|_{\mathtt b}=|w|_{\mathtt c}=k,\ |w|_{\mathtt a}=N-f(k)\}$$
と置く（$L_{N,d}$ は $f(k)=dk$）。

> **命題 NL.** $L_f$ が内容型付けで $(2,c)$ 組代入可能なら、$\Delta_k:=f(k+1)-f(k)$ について、$N-f(k+1)\ge|\Delta_k|+2$ かつ $N-f(k+2)\ge1$ を満たす各 $k\ge1$ で $\Delta_{k+1}=\Delta_k$ が成り立つ。

*Rect（$\Delta_k\ge0$ の場合。負なら $x,y$ の役を入れ替える）。*
- 比較組：$\alpha'\ge1$、$\alpha=\alpha'+\Delta_k$ として $x=(\mathtt a^\alpha\mathtt b,\ \mathtt c)$、$y=(\mathtt a^{\alpha'}\mathtt{bb},\ \mathtt{cc})$。型はともに $(\{\mathtt a,\mathtt b\},\{\mathtt c\})$。
- 共有文脈：$E_0=(\mathtt a^{A_0}\mathtt b^{k-1},\ \mathtt a,\ \mathtt c^{k-1})$、$A_0=N-f(k)-\alpha-1$。
  - $E_0[x]$ は $\mathtt b$ が $k$ 個で $\mathtt a$ が $N-f(k)$ 個。
  - $E_0[y]$ は $\mathtt b$ が $k+1$ 個で $\mathtt a$ が $A_0+\alpha'+1=N-f(k+1)$ 個。
  - どちらも射影は $\mathtt b^*\mathtt c^*$ で、$L_f$ に入る。
- 試験文脈：$E_1=(\mathtt a^{A_1}\mathtt b^{k},\ \mathtt a,\ \mathtt c^{k})$、$A_1=N-f(k+1)-\alpha-1$。$E_1[x]$ は $\mathtt b$ が $k+1$ 個で $L_f$ に入る。
- 結論の語：$E_1[y]$ は $\mathtt b$ が $k+2$ 個、$\mathtt a$ が $A_1+\alpha'+1=N-f(k+1)-\Delta_k$ 個である。$L_f$ に入るのは $\Delta_{k+1}=\Delta_k$ のときに限る。
- 中央は空でない。∎

[H] は $N=40$、$f(k)=4k+k(k-1)$ でこの四語のうち最後だけが外れ、$f(k)=4k$ では四語とも入ることを確かめた［CERTIFIED FINITE］。

**帰結。** R15 型の言語族（順序の不変量に Parikh で決まる会計を加えたもの）を代入可能のまま一般化すると、会計は余白のある範囲で線形になる。そうなれば定理 LIN の範囲に入り、多項式である。よって $L_{N,d}$ を「順序の不変量 ＋ $a$ を含む線形等式」の方向に一般化しても、超多項式の族は作れない。

### 5.3 肯定方向に残る設計空間（必要条件の一覧）

WN、$m=\{\mathtt a\}$ で超多項式の族があるなら、次をすべて満たす。

| 必要条件 | 根拠 |
|---|---|
| 重みは入れ子の分裂型の塔で運ばれる（離れた対・交差はない） | 系 6′（定理 D-hull、`rr:RV1-crossing`） |
| 最短語の導出の Strahler 数は族の中で非有界 | RV1 §4（CONDITIONAL VALID、Claude 手確認済み） |
| $\mathtt a$ を含む内容ごとの線形の不変量を一つも満たさない | 定理 LIN |
| R15 型（順序 ＋ Parikh の会計）なら会計が非線形になるが、それは代入可能性に反する | 命題 NL |
| 塔の族で組み合わせの条件 (PP) が破れる（または型の組の照合・余白が破れる） | 定理 W2-nest の対偶 |
| 定常な倍増・段依存のマーカー切片でない | R1 定理 2、R2 定理 B（Claude 確認範囲。本報告では再確認していない） |

**候補の探索の結果。** 上の条件をすべて満たす候補は作れなかった。(PP) を破るには、言語が「左成分 $y$ と右成分 $y'$ の交差した組み合わせ」を、族の重みの和に還元されない形で受理しなければならない。$L_{N,d}$ のように和で受理すれば (PP) が成り立つか LIN に入る。鏡像型なら (PP-i) が成り立つ。この中間の受理の型を Rect と両立させる例は得ていない［OPEN］。

---

## 6. T2(d)：判断（予想であることを明記する）

**WN の $m=\{\mathtt a\}$ は閉じていない。** 本ラウンドで閉じたのは次の三つである。
- 離れた配置（定理 D-hull）
- 入れ子の配置の強制（NF-nest）
- R15 型の一般化の排除（定理 LIN・命題 NL）

**残る障害（正確に）。** 系 6′ の塔（重い $K$ 節点の殻が包含で全順序、比較できない対はすべて隙間の入れ子で外側の両成分の類が $K$ を含まない）で、次の二つが残る。
- (i) **主障害：入れ替えの段。** 部分木の入れ替えで得られる語 $\xi(\sigma,\tau)$ は、言語の上の交差した組み合わせになる。それを評価する組み合わせの条件 (PP) が、代入可能性・WN・最短性から導けていない。
- (ii) **二次的な義務：型の組の照合 (N2)。** 族と包む節点の型の組がそろうこと。

**予想（確信は低い）。** 私はわずかに**否定の答え**（WN 版で多項式、すなわち WN の範囲では LG が境界でない側）に傾く。
- 理由：知られた例と試した設計（線形の会計、鏡像型、R15 型）はすべて (PP) を満たすか、定理 LIN に入る。(PP) を破る受理の型は、交差した組み合わせを和に還元しない形で受理しなければならない。命題 NL の型の議論は、そのような受理が Rect と衝突しやすいことを示唆する。
- 反対の理由：入れ替えは WN の木が制御できない組み合わせを作る。R10 の W2 と同じく、言語の側で何かが要る。そのような言語の存在を排除する定理はない。
- 同じモデル系列の R9〜R11 も否定に傾いていた。この傾きを根拠にはしていない。確信の度合いは RV1 と同じく低いままである。

**次の段階への進み方。**
1. **(PP) を直接攻める。** 塔の上で、交差した組み合わせの語 $\xi(\sigma,\tau)$ が受理されるなら、Rect と最短性から近道か和の等式が出るかを調べる。逆に、(PP) を破る WN 言語を、定理 LIN と命題 NL を避けて作る試みを同じ重みで行う。成功すれば WN 版、したがって一般の問題の**肯定の答え**になる。
2. **WN の $|m|\ge2$。** 定理 D-hull は $m$ の文字を壊さないので、離れた配置の閉じ方は周期的でない宿主へ持ち上がる見込みがある。塔の構造（殻の全順序）と RV1 の Strahler 数の上界の組合せが、次の自然な対象である。
3. **non-WN。** 交差 (R1\*) と離れた配置（隙間の閉性が崩れる）を一緒に扱う必要がある。WN 版の結論を待ってからでよい。

---

## 7. 既存結果との照合

| 出典 | 本報告での使い方・整合 |
|---|---|
| R9 HΞ・P1〜P7 | P1′・P3（COM）・P4（EX）を Rect の部品として使う。P5 は使わない。対の配置はすべて生まれつきの語から作り、(A) を位置の数え上げで確かめる（RV1 の修補に従う）。HΞ は RV1 の加法版で引用 |
| R10 定理 A | 定理 A′ が量化つきで置き換える（RV1 経由） |
| R10 HΞ\* | (U2)(U3) の形で使う。アンカーに殻を許す拡張（§4）は HΞ\* の証明を変えない（$\pi_0$ は固定語であればよい） |
| R10 D2・Φ2 | Φ2 は RV1 の短い原型の補題で置き換えて引用。D2 は入れ子で外側の成分が $K$ を含む場合にだけ使う |
| R10 NF2・W2 | NF2 の入れ子版が NF-nest（DIS2-nest・WRAP・EX2）。W2 が止まった「左右の成分が別の元」は、入れ子でも入れ替えで再び現れる（§3.2）。WN でも消えない |
| R11 PNF・命題 5・系 6・定理 4 | PNF (i) は零の連に $\mathtt a$ を入れるためだけに使う（RV1 の検算版）。命題 5 は入れ子で成分が $K$ を含む場合。系 6 は系 6′ に置き換わる（交差なし、離れた分裂型なし） |
| R15 $L_{N,d}$・補題 ST | [A] で全 Rect を再確認（$N=11,15$）。WN 判定・言語・厚さ・最小木を [B] で再計算し、R15・RV1 の数値と一致した。$L_{N,d}$ は (PP) を満たし、定理 LIN の範囲にある |
| RV1 LCA 命題・R15 の二提示 | 補題 3.0 の基礎。[B][E] と一致 |
| RV1 R4 補題 4・正規化の WN 保存 | 使っていない（WN 版の帰着の前提として引用のみ） |
| RV1 P5 の反例 | 定理 LIN の内容ごとの不変量の例として整合 |
| RV1 貪欲な一文の反証・短い原型の補題 | 補題を引用し、定理 D-hull で出力を組み直して使う。貪欲な一文は使わない |
| RV1 (U) の GAP | 定義 $(\mathrm U^q)$ で量化を補う |
| RV1 具体的な R10・R11 の漸近版 | 定理 A′ の (a)(b) の根拠として引用（読み通しのみ） |
| RV1 WN 版の定式化・Strahler 上界 | 系 6′ と §5.3 で引用 |
| RV1 pumping・倍増族の反証 | 使っていない。整合 |
| RV1 §5 交差する候補 | 線形の不変量 $\mu=(1,d,d)$ を持つので、定理 LIN が $N=O(\mathrm{poly}(\bar\theta_G))$ を一般に説明する |
| R1 定理 2、R2 定理 B | §5.3 の必要条件として引用（再確認していない） |
| R5 B4/B5 | 使っていない。定理 LIN は独立の証明。両者は整合する |

---

## 8. 自己監査

**同じ系列の推論の型の点検（依頼の三項目）。**
1. *一つの配置の受理から一般の配置を導いていないか。*
   - DIS2-nest・WRAP・EX2・定理 D-hull の共有文脈の二語は、どれも**実際の生まれつきの語**（反鎖を逃がしたもの）から、$\mathtt a$ の総数を変えない操作（P1′、PNF (i)、COM）だけで作った。
   - 各補題で、$\mathtt a$ の総数の式（(A)）を書き出した。異なる総数の配置を、一つの受理から導いた箇所はない。
   - 定理 D-hull の範囲 $1\le g\le G_*$ も、$N_2$ の実際の $\mathtt a$ の数 $A_2\ge7N/16$ から出した。
2. *予算の評価で親の終端を落としていないか。*
   - 短い原型は RV1 の補題（境界路の明示終端 $h\theta$ を数える版）を引用した。
   - 圧縮した殻の長さは、$\Phi_L$ の長さの評価に含まれる（祖先の明示終端で隙間に落ちたものは、$\mathtt a$ の連として 1 個に縮む）。
   - 自前の貪欲な選択はしていない。
3. *存在だけを仮定して長さを使っていないか。*
   - $(\mathrm U^q)$ は長さの上界を定義に含めた。
   - 定理 D-hull は (U1)〜(U4) を一つずつ確かめた。
   - NF-nest の (N3)(N4) は明示の仮定として残し、VALID の範囲をその仮定のもとに限った。

**弱い箇所（正直に）。**
- **定理 D-hull** は RV1 の短い原型の補題に依存する。この補題は Claude の確認メモで未確認とされていた。私は証明を読み、出力の組み直し（$\Phi_L$ の末尾を殻に含める）が補題の構成と整合することを確かめた。しかし、補題全体を独立に再構成してはいない。また $|\mathrm{hull}(v)|\le N/2$ の選択が予算の要である。**この定理は R10 系 C・R11 系 6・RV1 がいずれも残していた配置を消すので、最優先の独立監査の対象**とする。
- **補題 3.0** は RV1 の LCA 命題に依存する。LCA 命題は Claude の手確認がある。fan-out 1 の節点を含む場合分けも行った。
- **命題 NF-nest の (N2)**（型の組の照合）は、鳩の巣だけでは満たせない場合がある。強制の段が「VALID」なのは仮定つきである。
- **定理 W2-nest** の分離節点を左のスロットだけで数えた点は、RV1 の補題の直接の適用である。$\xi(\sigma,\tau)$ が各元を高々 2 回含むことは、表から確かめた。(PP) は族ごとの仮定で、言語全体の性質ではない。
- **定理 LIN** は強い主張（$\|G\|$ にもよらない）なので、反例の可能性を点検した。
  - $\{\mathtt a^N,\mathtt b\}$ と倍増の文法では、$\theta\ge N$ となって整合する。
  - 二文字の内容型付けの既知の上界（`thm:two-letter-content`）とも整合する。
  - 使ったのは、(T1)(T2)、文脈自由な置き換え、補題 S だけである。
  - 補題 S の Cramer・Hadamard の段は、極小な従属集合を取ることで、係数がすべて非零になるように直した。
- **命題 NL** は特定の言語族 $L_f$ についての主張である。「余白のある範囲で線形」から定理 LIN へつなぐ部分は、余白のない上端の $k$ を除くので、厳密な定理ではなく帰結の説明にとどめた。
- **有限検査**（[A]〜[H]）は全称の証明ではない。[E][G] は無作為な WN 木での簿記の確認で、定理の根拠は上の証明である。

**別の観点からの読み直し（入れ替えの段）。** 「入れ替えの語が交差した組み合わせになる」という主張を、$L_{N,d}$ で具体的に確かめた（[D]：族の並べ方の異なる組み合わせ 552 通りがすべて受理される）。したがって、これは私の構成の欠陥ではなく、言語の側の現象である。R10 §3.5 の判定（入れ替えは OPEN）と同じ場所に来ている。WN によって新しく閉じたと主張していない。

---

## 9. 次の最小義務（3 項目）

1. **(PP) の決着。** 系 6′ の塔で、交差した組み合わせの語が受理されるときに、Rect と最短性から (PP)（多重集合の一致と重みの等式）が出るかを調べる。反対に、定理 LIN・命題 NL を避けて (PP) を破る WN 言語を作る試みを、同じ重みで行う。
2. **独立監査。** 別系列のモデルで次を再構成してもらう。
   - 定理 D-hull（RV1 の短い原型の補題の出力の組み直し、隙間の閉性、予算 $A_2\ge7N/16$）
   - 定理 LIN（補題 S）
   - 系 6′ の網羅性
3. **型の組の照合 (N2)。** 塔の上で、族と包む節点の型の組をそろえる方法を作るか、そろわない場合を別の障害として分類する。

# R4 報告：fan-out 2 で IC は破れるか — 内部クラスから根の希少型への帰着（Claude Opus 5.5, 2026-11-21）

**結論（要約）**
- **T1（fan-out 2 で IC を破る族）は OPEN。** 構成は得られなかった。
- 代わりに、**内部クラスを根の希少型へ帰着する定理（定理 A）**を得た（自己判定 VALID。ただし原稿の `prop:pattern-thickness-transfer` に依存する）。$\Sigma$ の内容型付けでの IC は、拡大アルファベット $\Gamma_f(\Sigma)$（$|\Gamma_f|=f|\Sigma|+f+1$、$f=2,|\Sigma|=3$ なら 9 文字）の内容型付けでの希少型予想から従う。
- その帰結（系 B）として、各 $f,r_{\max}$ で次の三つは同値になる：(a) $\mathbf{SL}$ が一様多項式データを持つ、(b) すべての $c_\Sigma$ で希少型予想が成り立つ、(c) すべての $c_\Sigma$ で IC が成り立つ。したがって `op:fanout-two`（$f=2$）が肯定になるのは、**ある有限アルファベットの内容型付けで、根の希少型が超多項式になる族が存在するとき、かつそのときに限る**。R3 の付記が「一般の逆含意は出ない」とした方向を、文脈の長さに制限なしで閉じている。
- T2(b) は文字どおりの形では REFUTED（二穴 Rect から成分ごとの保存則は導けない。$\Sigma^+$ が反例）。T2(a) の新しい部分クラス定理は得られなかった。
- T3：否定（LG は fan-out 2 では境界でない）にやや傾く。**予想である。**

以下のラベル（VALID / CONDITIONAL / REFUTED / OPEN / CERTIFIED FINITE）はすべて報告者の**自己判定**であり、独立監査は受けていない。

---

## 1. 読了表

参照先：`growupkuriyama-hub/Papers` の `main` ブランチ（2026-11-21 に `git clone --depth 1`）、`02-v4-fixed-s-mcfg/` 以下。

| 資料 | 読んだ範囲 | 未読 |
|---|---|---|
| `research/README.md` | 全文 | — |
| `v2/reviews/PAUSE_FALSE_ROUTES_2026-11-16.md` | 全文（最初に読んだ） | リンク先の各監査原本（R13〜R16 の完全ソース）は未読 |
| R3：`astra_R3_internal_class_report_2026-11-21.md`、`claude_check_R3_2026-11-21.md` | 全文 | `run_all.py` は未実行（R3 のログ一致は確認メモの記載を信頼） |
| R1：`claude_check_R1_2026-11-21.md` | 全文 | 報告本体は §2.4（`L_M` と文法）と §3.1・§3.2 冒頭のみ。他の節は未読 |
| R2：`claude_check_R2_2026-11-21.md` | 全文 | 報告本体（`astra_R2_marker_slices_report…`）は**未読**。定理 B・C は main.tex `sec:p4-resume-R2` の要約と確認メモで把握した |
| `main.tex` 第 I 部の定義 | `def:characteristic-sample`, `def:semigroup-typing`, `def:standard-mcfg`, `def:grammar-properties`, `def:tuple-substitutable`, `prop:abelian-coset-filter`, `lem:filling-identity`〜`prop:completeness`（l.744–951）, `def:reconstruction`, `def:witness-set`, `lem:typed-homogeneity`（主張のみ。証明は付録で未読） | 付録の `app:typed-witness-aux-proofs` |
| `main.tex` 結果 | `lem:thickness-equivalence`, `lem:witness-length-template`, `thm:data-from-typed-thickness`, `prop:rare-type`, `lem:type-deletion`, `lem:distinguishing`, `prop:typed-thickness-exponential`, `cor:distribution-representatives`, `prop:three-letter-family`（主張）, `def:uniform-polydata`, `thm:fanout-one-data`（主張）, `lem:power-transfer`, `thm:doubling-no-lift`, `lem:typing-monotone`, `prop:sl-reduction`, `thm:two-letter-content` とその付録 `app:two-letter-content`（l.11078–11340 付近、命題 `app-two-nonsaturated` まで）, `prop:full-content-types`, `prop:u1-weight-all-fanout`（主張）, `op:fanout-two` と直後の段落, `conj:rare-types` とその注記, `prop:good-normalization`（主張）, `def:component-pattern-thickness`, `prop:pattern-thickness-transfer`（主張と $t_G$ 部分の証明） | `prop:three-letter-family` の付録証明、`thm:local-group-polydata` の証明、`lem:normalization-stages` の本体（`prop:pattern-thickness-transfer` の証明が引用する補題。主張は証明内の言及でのみ把握） |
| `main.tex` 第 IV 部 | `sec:p4-ptree`, `sec:p4-resume-R1`, `sec:p4-resume-R2`, `sec:p4-resume-R3` の全文、`rr:sl-early`, `rr:theorem-G` | 第 IV 部の他の節 |
| `main.pdf` | 開いていない（main.tex を直接読んだ） | 全体 |

---

## 2. T0 の結論：枠組みは正しい。ただし四点補足する

**判定：VALID（四つの但し書き付き）。**

1. **量化の順序。** `def:uniform-polydata` では、多項式 $p=p_{f,r_{\max},s,\Sigma}$ が $(f,r_{\max},s,\Sigma)$ に依存してよく、$L$ と $G$ には依存しない。R3 の IC も「固定した $\Sigma,s,r_{\max}$ ごとに $p$ が存在する」形なので、順序は一致する。`cor:distribution-representatives` は $\|K\|_+\le N_{\rm typ}(1+2\bar\theta_G+r_{\max}\tau(G,s))+1$ を与え、$N_{\rm typ}\le|\mathsf S^\sharp|^{fr_{\max}}\|G\|$ は固定パラメータで定数倍にすぎない。よって、各 $\Sigma$ で IC($c_\Sigma$) が成り立てば `prop:sl-reduction`(ii) の条件が成り立ち、(i) により否定の答えになる。逆向き（肯定の答えには、ある $\Sigma$ で IC($c_\Sigma$) が破れることが必要）も同じ系の対偶として正しい。
2. **$f$ と $r_{\max}$ は固定。** `op:fanout-two` は各 $(f,r_{\max})$ ごとの問いで、`prop:sl-reduction` も $(f,r_{\max})$ を固定する。R3 の IC は $f=2$ で、同じ $r_{\max}$ で述べるべきである。$f=2$ の答えから $f\ge3$ の答えは出ない（`def:class-cmcf` の後の (b)：クラスは $f$ について単調でない）。
3. **$s_U$ を使ってよい理由。** $s_U\preceq c_\Sigma$ なので $\Cmcf{2}{s_U}\subseteq\Cmcf{2}{c_\Sigma}$ である。同じ $G$ の $s_U$-型付き非終端 $A_{\mathbf t}$ と、$u\in L_{A_{\mathbf t}}$ に対する $c$-型付き非終端 $A_{c(u)}$（$E_A[u]$ を通る成功導出があるので trim 後にも残る）を比べると、分布が同じで型が細かいので $\mathrm{Cl}_{L,c}(A_{c(u)})\subseteq \mathrm{Cl}_{L,s_U}(A_{\mathbf t})$ となる。よって $\tau^{c}\ge\tau^{s_U}$。$s_U$ での IC の破れは $c_\Sigma$ での破れになる。
4. **「最小の未解決ケース Σ={a,b,c}」について。** 否定の答えには**すべての** $\Sigma$ で IC が要る。三文字で IC を証明しても問題は解けない。さらに本報告の定理 A により、三文字の IC は 9 文字の希少型予想から従う。アルファベットの大きさは、どの定式化を使うかで変わる。

その他の確認事項：$C_X=\{\mathbf z: s(\mathbf z)=\mathbf m,\ E_A[\mathbf z]\in L\}$ は、付録の `lem:app-two-basic`(i) と同じ論証（typed homogeneity と arity $d$ での代入可能性）で任意のアルファベットについて成り立つ。$\tau(G,s)=\max_X\tau_{C_X}$ は `cor:distribution-representatives` の直前の定義そのものである。$|\Sigma|=2$ では IC は既に定理である（`thm:two-letter-content` が $\tau(G,c)$ を直接抑える）。

---

## 3. 主結果

### 3.0 記号

$f\ge1$, $r\ge1$ を固定する。$L\in\Cmcf{f}{c_\Sigma}$、$G=(V,\Sigma,P,S,\mathrm{fan})$ は $L\cap\Sigma^+$ の reduced good な提示で、fan-out $\le f$、rank $\le r$ とする。$\theta:=\bar\theta_G$ と置く（**元**文法の厚さ）。$X=A_{\mathbf m}$ は trim 後の型付き非終端で、arity $d\le f$、$\mathbf m=(m_1,\dots,m_d)$（$m_j\subseteq\Sigma$ は非空）とする。$E_A=v_0\square_1v_1\cdots\square_dv_d$ は `lem:thickness-equivalence`(iv) の文脈で、$|E_A|_{\rm fix}\le\theta$、$v_1,\dots,v_{d-1}\ne\varepsilon$ である。

**拡大アルファベット。**
$$\Gamma_f(\Sigma):=(\Sigma\times\{1,\dots,f\})\ \uplus\ \{\#_0,\dots,\#_f\},\qquad |\Gamma_f|=f|\Sigma|+f+1 .$$
$(x,j)$ を「第 $j$ 穴の文字 $x$」と読む。$\#_i$ が**使用される**のは $v_i\ne\varepsilon$ のときとする（$1\le i\le d-1$ では常に使用される）。$U$ を使用される標識の集合とする。順位 $\kappa(\#_i)=2i$、$\kappa((x,j))=2j-1$ を置き、射 $\varphi$ を $\varphi((x,j))=x$、$\varphi(\#_i)=v_i$（$\#_i\in U$）で定める。使用されない文字の像は任意でよい（下の $R$ で排除される）。

$$R:=\{w\in\Gamma_f^+:\ \text{各}\ \#_i\in U\ \text{はちょうど一回現れる；} U\ \text{外の標識と色}\ j>d\ \text{の文字は現れない；}\ \kappa\ \text{は}\ w\ \text{に沿って非減少}\}.$$
$$L^X:=\varphi^{-1}(L)\cap R .$$

### 3.1 補題 1：$R$ は $(f,c_\Gamma)$-代入可能［VALID］

**主張。** $1\le d'\le f$ と $\mathbf x,\mathbf y\in(\Gamma^+)^{d'}$ について、成分ごとに $c_\Gamma(x_k)=c_\Gamma(y_k)$ であり、ある許容文脈 $E$ が両方を $R$ 内で受理するとする。このとき任意の許容文脈 $E'$ で $E'[\mathbf x]\in R\iff E'[\mathbf y]\in R$。

**証明。** $E'[\mathbf x]\in R$ の三条件を、$\mathbf x$ の内容型だけで決まる量で書き直す。
(1) **回数。** $\#_i$ の $E'[\mathbf x]$ での出現数は、$E'$ の固定部での出現数と $n_i(\mathbf x):=\sum_k|x_k|_{\#_i}$ の和である。$E[\mathbf x]\in R$ なので $n_i(\mathbf x)\le1$。したがって $n_i(\mathbf x)=[\#_i\in\bigcup_kc_\Gamma(x_k)]$ で、これは内容型で決まる。$\mathbf y$ も同じ。
(2) **禁止文字。** 禁止文字が現れるかどうかは、$E'$ の固定部の内容と $\bigcup_kc_\Gamma(x_k)$ で決まる。
(3) **単調性。** $E'[\mathbf x]$ を、空でない区片の列（$E'$ の固定部 $v'_0,\dots,v'_{d'}$ のうち空でないもの、および $x_1,\dots,x_{d'}$）に分ける。$\kappa$ が非減少であることは、「各区片の中で非減少」かつ「隣り合う区片の境界で（左の最後の順位）$\le$（右の最初の順位）」と同値である。$E[\mathbf x]\in R$ より各 $x_k$ の中では非減少なので、$x_k$ の最初の順位は $\min\kappa(c_\Gamma(x_k))$、最後の順位は $\max\kappa(c_\Gamma(x_k))$ になり、内容型で決まる。$E'$ の固定部の条件は $\mathbf x$ に依存しない。$\mathbf y$ にも同じ論証が成り立つ。∎

場合分けは、(1)(2)(3) の三条件が $R$ の定義を尽くすことで網羅的である。$d'=1$ では中央の区片がない。外側の空語はその区片を飛ばせば扱える。

### 3.2 補題 2：$L^X\in\Cmcf{f}{c_\Gamma}$［VALID］

**$\varphi^{-1}(L)$ の代入可能性。** $\mathbf x,\mathbf y$ を補題 1 と同様にとり、文脈 $E$ が両方を $\varphi^{-1}(L)$ 内で受理するとする。使用される文字の $\varphi$-像はすべて非空なので、$\varphi(\mathbf x),\varphi(\mathbf y)$ の成分は非空であり、$\varphi(E)$ は許容文脈になる（中央の固定部の像も非空）。$c_\Sigma(\varphi(x_k))=\bigcup_{\gamma\in c_\Gamma(x_k)}c_\Sigma(\varphi(\gamma))$ なので、成分ごとの $c_\Sigma$-型は一致する。$\varphi(E)[\varphi\mathbf x]=\varphi(E[\mathbf x])\in L$、$\varphi(\mathbf y)$ についても同様なので、$L$ の代入可能性から $\mathcal D_L(\varphi\mathbf x)=\mathcal D_L(\varphi\mathbf y)$。よって任意の $E'$ で $E'[\mathbf x]\in\varphi^{-1}(L)\iff\varphi(E')[\varphi\mathbf x]\in L\iff E'[\mathbf y]\in\varphi^{-1}(L)$。

**交わり。** `prop:abelian-coset-filter`(i)（代入可能な言語の交わりは代入可能）を $\varphi^{-1}(L)$ と $R$ に適用する。$L^X$ は MCFL の逆準同型像と正規言語の交わりなので $f$-MCFL である。いずれにせよ補題 4 で fan-out $\le f$ の提示を直接作る。∎

### 3.3 補題 3：$L^X$ の形と根の型［VALID］

$R$ の語は、$\kappa$ の非減少から次の形に限られる：
$$[\#_0]\ Y_1\ \#_1\ Y_2\ \cdots\ \#_{d-1}\ Y_d\ [\#_d],\qquad Y_j\in(\Sigma\times\{j\})^*,$$
ここで $[\#_i]$ は $\#_i\in U$ のときだけ現れる。$\varphi$ を施すと $v_0\pi(Y_1)v_1\cdots\pi(Y_d)v_d$ になる（$\pi$ は色を忘れる射）。したがって
$$L^X=\{[\#_0]Y_1\#_1\cdots Y_d[\#_d]:\ E_A[\pi(Y_1),\dots,\pi(Y_d)]\in L\}.$$
根の型 $m^X:=U\cup\bigcup_jm_j\times\{j\}$ を持つ語は、ちょうど各 $Y_j$ が非空で $c(\pi Y_j)=m_j$ を満たす語である。$C_X$ の特徴付け（§2）より、
$$\mu_{m^X}(L^X)=\tau_{C_X}+|U|,\qquad |U|\le f+1 .$$
$m^X$ は実現されている（$\mathbf u\in L_X$ を色付けた語がある）。

### 3.4 補題 4：小さく薄い提示［VALID、`prop:pattern-thickness-transfer` に依存］

**主張。** fan-out $\le f$、rank $\le r$ の reduced good な $G^X$ で $L(G^X)=L^X$ となるものがあり、$Q:=\theta+2f+1$ と置くと
$$\|G^X\|=O_{f,r}\bigl(\|G\|\,Q^{2rf+f}(\theta+1)^{f(f+1)}\bigr),\qquad
\bar\theta_{G^X}=O_{f,r}\bigl(\|G\|\,Q^{2rf+f}(\theta+1)^{f(f+1)}\cdot(r+1)\theta^2|V|Q^{2f}\bigr).$$
どちらも $(\|G\|,\theta)$ の多項式で、次数は $f,r$ だけで決まる。

**構成。** パターン $v_0Z_1v_1\cdots Z_dv_d$（$Z_j=\Sigma^*$）の NFA $\mathcal P$ をとる。状態は「$v_i$ を $k$ 文字読んだ」$(i,k)$（$0\le k\le|v_i|$）と「第 $j$ 穴の中」$Z_j$ で、合計 $\le|E_A|_{\rm fix}+2d+1\le Q$ 個である。これらはパターン上の位置で線形に順序付けられ、$\mathcal P$ の遷移は順序を下げない。遷移で出力するものを次のように決める（**圧縮**）。$Z_j$ で読んだ文字 $x$ は $(x,j)$、$v_i$ の第 1 文字は $\#_i$、$v_i$ の他の文字は $\varepsilon$。

標準 MCFG $H$ を次で定める。非終端は $\langle B;(p_1,q_1),\dots,(p_e,q_e)\rangle$（$B\in V$、$e=\mathrm{fan}(B)$）で、「$B$ の第 $i$ 成分を $\mathcal P$ が $p_i$ から $q_i$ へ読む」という意味である。規則は $G$ の各規則に、子の状態対と、各出力成分の上での $\mathcal P$ の走行（終端は遷移で、変数は子の状態対で進む）を注記したもので、テンプレートは圧縮後のものを使う。開始記号は $\langle S;(q_{\rm init},q)\rangle$（$q$ は受理状態。複数あれば恒等の開始規則を加える）。$H$ は線形・非削除で、fan-out と rank は $G$ と同じである。空成分や併合（merging）は生じうるが、標準 MCFG では許される。$L(H)=L^X$ は、$G$ の導出と $E_A$ の形の構文解析との対応から直ちに従う（この $G$ の導出は $\mathcal P$ の受理走行を持ち、圧縮像が $L^X$ の語になる。逆も同じ）。

**サイズ。** 子の状態対の選び方は $\le Q^{2rf}$ 通り。一つの出力成分の走行は、開始状態と、走行が穴の状態から $v$ の部分へ移る終端の位置（穴ごとに高々一回、高々 $f+1$ 回、各々 $\le\theta+1$ 箇所）で決まり、$\le Q(\theta+1)^{f+1}$ 通りある。成分は $\le f$ 個。よって規則あたりの注記は $\le Q^{2rf+f}(\theta+1)^{f(f+1)}$ 通り、テンプレートは元より長くならず、$\|H\|\le\|G\|\,Q^{2rf+f}(\theta+1)^{f(f+1)}+|V|Q^{2f}+1$。

**パターン厚さ。** $H_{\rm red}$ の各非終端 $\lambda=\langle B;\ldots\rangle$ の**台パターン**（どの成分が空か）は、状態対で決まる（成分が空になるのは、$v_i$ の第 2 文字以降だけを読む場合に限る）。よって $t_{\rm pat}$ は各 $\lambda$ の最短圧縮収率で抑えられる。$\lambda$ を根に持つ $G$-導出木の節点を二つに分ける。成分がすべて穴の文字だけを読む（状態対が「穴の始まり／内部」から「穴の内部」へ）節点を**自由**、それ以外を**拘束**と呼ぶ。拘束節点の収率は $v$ の文字を少なくとも一つ含む。
- 自由節点の部分木を、その非終端の最短収率 $\omega_{B'}$（$\|\omega_{B'}\|_1\le\theta$、`lem:thickness-equivalence`(ii)）の導出に置き換えても、状態対は変わらない（穴は任意の非空語を受け入れる）。
- 拘束節点の反鎖は、互いに素な収率がそれぞれ $v$ の文字を含むので、$\le|E_A|_{\rm fix}\le\theta$ 個である。
- 拘束節点の数を最小にした木では、一つの路の上で拘束節点のラベル（非終端と状態対）は繰り返さない。繰り返せば上の部分木を下の部分木で置き換えられ、それでもラベルは保たれ、拘束節点が減る。路の長さは $\le N_{\rm lab}:=|V|Q^{2f}$。

よって拘束節点は $\le\theta N_{\rm lab}$ 個。それぞれは $\le\theta$ 文字を書き（`lem:thickness-equivalence`(i)）、$\le r$ 個の子を持ち、自由な子の収率は $\le\theta$。圧縮は長さを増やさないので
$$t_{\rm pat}(H_{\rm red})\le(r+1)\theta^2|V|Q^{2f}$$
（根が自由なら $\le\theta$）。`prop:pattern-thickness-transfer` を $H$ に適用すると、reduced good な $G^X$ が得られ、$\|G^X\|=O_{f,r}(\|H\|)$、$\bar\theta_{G^X}=O_{f,r}(\|H\|\,\bar t_{\rm pat})$ で、fan-out と rank は保たれる。∎

### 3.5 定理 A（内部クラスから根の希少型へ）［VALID、補題 4 の但し書き付き］

> **定理 A.** $f,r\ge1$ と $\Sigma$ を固定し、$\Gamma:=\Gamma_f(\Sigma)$ とする。fan-out $f$、rank $r$ で $c_\Gamma$ について希少型の多項式上界 $\mu^\star(L',c_\Gamma)\le p(\|G'\|,\bar\theta_{G'})$（すべての $L'\in\Cmcf{f}{c_\Gamma}$ と reduced good な提示 $G'$ について）が成り立つとする。このとき、$(f,r)$ で $c_\Sigma$ について IC が成り立つ。すなわち、多項式 $p'$ があって、すべての $L\in\Cmcf{f}{c_\Sigma}$、すべての提示 $G$、すべての型付き非終端 $X$ について
> $$\tau_{C_X}\le\mu_{m^X}(L^X)\le p\bigl(\|G^X\|,\bar\theta_{G^X}\bigr)\le p'(\|G\|,\bar\theta_G).$$

**証明。** 補題 2 で $L^X\in\Cmcf{f}{c_\Gamma}$、補題 4 で $G^X$ が条件を満たし、補題 3 で $\tau_{C_X}\le\mu_{m^X}(L^X)\le\mu^\star(L^X,c_\Gamma)$。最後の不等号は補題 4 の多項式評価を $p$ に代入したもの。$p'$ は $f,r,\Sigma$ と $p$ だけに依存する。∎

$f=2$、$\Sigma=\{a,b,c\}$ では $|\Gamma|=9$ である。R3 の付記との違いは次のとおり。付記は文脈の固定部を色で区別したため、固定部の長さを定数 $K$ で抑える必要があり、さらに非半束の型付け $t$ を要した。本定理では、固定部 $v_i$ 全体を一つの標識 $\#_i$ に置き換え、$\varphi$ で元に戻す。固定部が「正確に $v_i$ である」ことは $\varphi^{-1}(L)$ が担い、「穴の順序と各標識が一回だけ現れる」ことは $R$ が担う。$R$ の受理を内容型だけで決められる（補題 1）ことが鍵である。厚さの問題（文脈とずれた導出）は、パターン厚さの変換（`prop:pattern-thickness-transfer`）と、拘束節点の反鎖・路の評価で処理した。

### 3.6 系 B（三条件の同値）［VALID、定理 A に依存］

> **系 B.** 各 $f\ge1$, $r\ge1$ について、次は同値である。
> (a) $\mathbf{SL}$ は $(f,r)$ で一様多項式特性データ長を持つ。
> (b) すべての $\Sigma$ で、$c_\Sigma$ について希少型の多項式上界が成り立つ（`conj:rare-types` を内容型付けに制限したもの。$f$ は一般）。
> (c) すべての $\Sigma$ で、$c_\Sigma$ について IC が成り立つ。

**証明。** (c)⇒(a)：`cor:distribution-representatives` と `prop:sl-reduction`(ii)。(a)⇒(b)：`prop:rare-type` により、どの特性標本も各実現型の語を含むので $\mu^\star\le\|F\|_+\le p$。(b)⇒(c)：定理 A（(b) を $\Gamma_f(\Sigma)$ に使う）。∎

**検算。** $f=1$ では三条件がすべて偽で、矛盾はない（$T_n$ が (b) を、R3 の $P_n$ が (c) を破り、`thm:fanout-one-data` で (a) は偽）。本定理の構成を $P_3$ に施すと、内部の単元クラス $\{W_2\}$ が根の希少型（唯一の語、長さ $|W_2|+2=12$）に変わる（コード [4]）。

**`op:fanout-two` への帰結（$f=2$）。** 答えが肯定 $\iff$ (a) が偽 $\iff$ ある $\Sigma$ と、$\Cmcf{2}{c_\Sigma}$ の族で、根の型の最短語が $(\|G\|,\bar\theta_G)$ について超多項式になるものが存在する。したがって：
- R1 の「希少型を超える」ルート B′ と、R3 の内部クラス路線は、**解決能力の点で希少型路線と同じ**である。どちらで族が得られても、定理 A によって（アルファベットを $\Gamma_2(\Sigma)$ に広げた）希少型の族に変わる。
- `conj:rare-types` の注記「成り立てば希少型の方法では問題は決まらない」は、内容型付けに関しては「成り立てば（全アルファベットで）答えは否定」と強めて読める。
- ただし、$\Sigma$ ごとの同値ではない。三文字の IC は 9 文字の希少型から従うが、三文字の希少型から従うとは示していない。

### 3.7 T1：構成は OPEN。障害の分析

**(i) $P_n$ が二穴 Rect に違反した仕組み（R3 §2 の分析）。** 四語は $x=(b,b^2)$、$y=(b^2,b)$。$E_0=c\square_1b\square_2R$ は $w=cW_kc$ の先頭の $b^4$ を切り、$E_1$ は第一コピーの先頭の $b$ の連と、第二コピーの $a$ の直前の $b$ の連を穴にする。$E_1[y]$ は $w$ から **$b$ を一つ別の $b$ の連へ移しただけの語**である（同じ Parikh ベクトル。コード [6] で $n=5..8$ を独立の認識器で確認：受理・受理・受理・不受理）。$T_n$ の $c$ を含まない語は一意で硬く、「$W_k$ は $b^k a$ で始まる」という**連の長さ**に深さの情報が載っている。そのため、連の長さを変える交換で $T_n$ の外に出る。

**(ii) 補題 R（連の再配分に対する閉性）［VALID、`lem:power-transfer` の直接の系］。** $L\in\Cmcf{2}{c_\Sigma}$、$u\in\Sigma^+$ とし、$L$ のある語が $u^4$ を含むとする。$u$ を一単位として、$u$ の連（最大の $u$-冪の出現）の間で $u$ を一つ移す操作（移す元の連は長さ $\ge2$、間の語は非空）は、$L$ の所属を保つ。**証明：** $i=\delta=j=1$、$i_0=p=1$（$c(u)$ は冪等）で `lem:power-transfer` を適用する。∎
系：$X$ が $E_A$ で特徴付けられる類 $C_X$ も、穴の内部で同じ操作をして成分ごとの内容が変わらない限り、この操作で閉じる。したがって IC を破る族では、**どの $u$ についても（$u^4$ が現れる限り）、類を区別する情報を $u$ の連の長さに載せてはいけない。** $P_n$ はこの制約に違反した。

**(iii) 設計の制約（既知の結果からまとめたもの。新しい no-go 定理ではない）。**
1. 型付き文法で最短導出が指数長なら、多項式個の型付き非終端のうち一つ $Y$ が互いに素な位置に超多項式個現れる（鳩の巣原理）。長さ最小のまま、それらの収率を同一にできる。$z$ は同じ長い成分の多数のコピーを含む。
2. 二つのコピーの間に $c$ があれば MS 系により、その Parikh 切片に $\ge(|z|-2)/18$ 語が要る。切片が疎な構成（完全二分木の純粋木と脱出）は R1 定理 2・R2 定理 B で排除される。よって**切片は密**でなければならない。
3. (ii) により、$u^4$ が現れるどの $u$ についても、連の長さによる符号化は使えない。
4. 全成分が全内容型なら `prop:full-content-types` が上界を与える。少なくとも一成分は文字を欠く必要がある。
5. 成分ごとの正の保存則があれば R3 定理 2 で上界が出る。どの実現支持でも (5) が必要。
6. **定理 A：** これらをすべて満たす三文字の族 $(L_n,G_n)$ が得られれば、$(L_n^X,G_n^X)$ は 9 文字の内容型付けでの希少型の反例になり、`op:fanout-two` を肯定的に解決する。T1 は、問題の肯定方向そのものと同等に難しい。

**(iv) 試した方向と止まった点（記録）。** 連の長さを避けるため、Zimin 型 $W_i=W_{i-1}\beta_iW_{i-1}$（左右の付加語なし）を考えた。区切り $\beta_i$ が固定なら $W_i$ は周期語 $(W_0\beta)^{2^i-1}W_0$ になり、(ii) が適用される。$\beta_i$ を段で変える（周期倍化列で $b,bb$ を交互にする）案は、$c$ の脱出を入れた時点で純粋木が完全二分木の層状倍増になり、R2 定理 B の仮定に入る。$c$ の脱出なしで内部クラスを長く保つ機構は見つからなかった。**有限検査はしていない。** これは障害の記録であり、不可能性の証明ではない。

### 3.8 T2

**(b) 二穴 Rect から成分ごとの正の保存則を導く。［文字どおりの形は REFUTED］** `prop:typed-thickness-exponential` の文法（$L=\Sigma^+$、fan-out 1 なので fan-out $\le2$、rank 2、reduced good）を $c_\Sigma$ で見る。$X=(A_n)_{\{a\}}$、$J=\{a\}$ とすると、$L_{A_n}$ は $c, cc, a^{2^n}$ を含む。$h$ が $L_{A_n}$ 上で一定なら $h_c=0$、よって $h_a=0$ である（コード [5]：$e_a$ が収率差の張る空間に入ることを有理数で確認）。$L=\Sigma^+$ は全 Rect を満たすので、Rect から保存則は導けない。正しく弱めた形「(5) と Rect から短い元が出る」は、R3 系 2.2 により ¬(5) の場合は既に解けているので、**IC そのもの**と同値になる。新しい内容はない。どの条件下なら導けるかについては、本ラウンドでは正の結果を得ていない（OPEN）。

**(a) 明示した部分クラスでの IC。［新しい結果なし、OPEN］** 定理 A により、部分クラス上の IC は、$L^X$ の根の型 $m^X$ についての希少型の主張と同値な問題に移る。既知の希少型の結果のうち、移した先で使えるのは全内容型（`prop:full-content-types`）だけで、これは $m_j=\Sigma$（全 $j$）に戻るので新しくない。「$X$ が arity 2 で両成分が $c$ なし」の部分クラスは、根の型 $\{a\}$ の最短冪 $a^N$（$X=S_{(\{a\})}$、$E=\square$。第 IV 部 O2 の $P_{\rm tree}$ 問題）を含み、停止時から未解決である。そのため、この部分クラスを本ラウンドで閉じることは見込めないと判断した。

---

## 4. T3 の判断（予想）

**否定（fan-out 2 では LG は境界でない）にやや傾く。これは予想であり、証明ではない。** 根拠：(1) 系 B により、問題は内容型付けでの希少型に集約された。根の型について知られている構成（倍増族、その文字非交差の像、定常・層状の倍増）は、すべて fan-out 2 の二穴条件で排除されている（`thm:doubling-no-lift`、R1 定理 2、R2 定理 B）。(2) 正の側では、二文字・全内容型・局所群・アーベル濾過・成分ごとの保存則で上界がある。(3) 二穴条件の中心にある機構（`lem:power-transfer`、MS 系、補題 R）は、どれも長さを保つ交換で、「長い連と疎な切片による符号化」を一様に壊す。指数長の最短語を作る既知の手段は、ほぼこの符号化に依存している。反対側の根拠：単一文字の $a^N$（$P_{\rm tree}$）すら一般には未解決である。長さを保つ交換だけでは短縮が出ないので、上界側の決め手もない。確信度は低い。

---

## 5. 既存結果との照合

| 結果 | 本報告との関係 |
|---|---|
| R13 原文 X1（反証済み） | 使っていない。補題 1・2 の比較は、受理された実際の語の上で成分ごとの実内容型を一致させたものだけ。正の padding の議論はしていない。 |
| R14 原文 CA（反証済み） | 使っていない。加法的な合成や初期 seed は扱わない。 |
| R15 一般 IH（反証済み） | 使っていない。連結宿主を作らない。補題 4 のポンピングは、同じラベル（非終端と状態対）の部分木の置き換えだけである。 |
| R2 の退化した短縮補題 | 使っていない。定理 A は短縮を主張せず、問題を移すだけである。 |
| `thm:doubling-no-lift` | §3.7(ii) の補題 R は、その証明で使われる `lem:power-transfer` の再配分形。新しい族は主張しない。 |
| R1 定理 2、R2 定理 B・C | 設計制約として引用（§3.7(iii)）。拡張は主張しない。定理 C（$L_t$）は希少型路線の弱い例で、定理 A とは独立。 |
| R3 定理 1（$P_n$） | 定理 A の $f=1$ での検算に使った（内部の単元クラスが根の希少型に変わる）。 |
| R3 定理 2（保存則） | T2(b) の反例は、その仮定が Rect から出ないことを示すだけで、定理 2 と両立する。 |
| R3 定理 3（IC ⇒ rare-types） | 系 B の (c)⇒(b) 側。定理 A はその逆（アルファベットを広げる）。 |
| R3 付記（有界文脈での逆還元） | 定理 A はこれを、文脈の長さの制限なし・非半束の型付けなしに置き換える。付記の「一般逆含意は出ない」は付記の証明についての注意で、定理 A と矛盾しない。 |
| `prop:pattern-thickness-transfer` | 補題 4 の最後の段階で使う。**本報告はその証明を独立に再検査していない**（§6）。 |
| `conj:rare-types` | 系 B により、内容型付け（全アルファベット）への制限が $\mathbf{SL}$ の一様多項式データと同値。 |

---

## 6. 自己監査

定理 A と系 B を、反例を探す立場で読み直した。

1. **最も弱い箇所：** 補題 4 は `prop:pattern-thickness-transfer`（`lem:normalization-stages` を経由する）に依存する。私はその主張と $t_G$ 部分の証明を読んだが、`lem:normalization-stages` の本体は読んでいない。この命題が原稿の主張どおりなら補題 4 は成り立つ。原稿の定理番号付きの命題として扱ったので、ラベルは VALID としたが、**この依存は独立監査の最優先項目**である。
2. **$\varphi(\#_i)$ の非空性。** $v_0$ や $v_d$ が空のときは、その標識を使わない（$U$ から外す）。そうしないと $\varphi(\mathbf x)$ に空成分が出て、$L$ の代入可能性が使えない。この処理を定義に入れた。
3. **$R$ の代入可能性で使っていること。** 受理された組の各成分は単調で、各標識の個数は $\le1$。これは共有された受理文脈から来るもので、内容型だけからは出ない。補題 1 はこの二つだけを使っている。検査 [1] は $|Y_1|+|Y_2|\le4$ 程度の有界な網羅で、全称証明ではない。
4. **拘束節点の定義。** 「収率が $v$ の文字を含む」ことは状態対で決まる。穴の状態から始まり、$v_{j}$ の最初の文字の直前で終わる成分は自由に分類される（$v$ の文字を含まない）。コードの NFA では、この境界を同一視する処理（$\varepsilon$ 閉包）を手で書いた。数学的には、状態を線形な位置で定義すれば曖昧さはない。コードのこの部分は一つの小さな例（$L_3$）でしか確かめていない。
5. **ポンピングで拘束節点の数が減ること。** 上の節点 $u$ を除く $u$ の部分木の拘束節点（少なくとも $u$ 自身）が消える。下の節点 $u'$ の部分木はそのまま残る。ラベルが等しいので、$u$ の祖先の状態対は変わらない。
6. **アルファベットの拡大。** 系 B は「全アルファベットについて」の同値であり、$\Sigma$ ごとの同値ではない。三文字の希少型予想から三文字の IC が出るとは主張していない。
7. **新規性は未確認。** 文献調査はしていない。原稿と R1〜R3 の範囲では、この同値は記録されていない（R3 は逆向きを条件付きとしている）。
8. **系 B (a)⇒(b)** は `prop:rare-type` の B$^{\le r}$ 版を使う。$\varepsilon$ の扱いは $L\cap\Sigma^+$ に移せば影響しない。
9. 有限検査はすべて CERTIFIED FINITE であり、どの全称主張の証明にも使っていない。

---

## 7. 次の最小義務（3 項目）

1. **定理 A の独立監査。** 特に補題 4：`lem:normalization-stages` を含めて `prop:pattern-thickness-transfer` を再検査し、$H$ の NFA と注記の数え上げを手で確かめる。通れば、R3 の付記を置き換える形で `sec:p4-resume-R4` に記録し、`conj:rare-types` の注記を系 B に合わせて更新する。
2. **アルファベットの縮小。** $\Gamma_2(\{a,b,c\})$（9 文字）の希少型を三文字（または固定の小さいアルファベット）の内容型付けへ戻す符号化があるかを調べる。あれば、問題は「三文字の $c_\Sigma$ での希少型」一本になる。
3. **最小の希少型の問題に集中する。** 系 B により、肯定・否定のどちらを狙っても、根の型での主張に集約される。手始めは単一文字の型 $\{a\}$ の最短冪 $a^N$（O2 の $P_{\rm tree}$）、ついで二文字の内容型を持つ三文字の根の型。

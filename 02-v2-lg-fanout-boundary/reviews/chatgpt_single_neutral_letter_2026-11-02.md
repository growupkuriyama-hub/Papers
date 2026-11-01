# 中立文字が一つの $U_1$ 型付け：任意のアルファベット・ファンアウト $f\ge2$ の検証報告

**作成日**：2026-11-02  
**判定**：一般の場合の多項式特徴データ上界 **未解決**。本報告では既存証明の移植可能範囲を特定し、条件付き上界を明示的な定数で証明する。  
**原稿正本**：[`02-v2-lg-fanout-boundary/main.tex`](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/main.tex)、取得 Git blob `52d568e72624bc58195761ba45c2d14312625bef`。参照した他の正本は末尾 §12 に記載。  
**重要**：以下の「証明済み」はこの報告内で証明した命題、または参照を明示した既存の完全な証明により帰結する命題を意味し、外部査読や文献上の新規性を意味しない。

## 0. 結論と判定表

| 主張 | 判定 | 根拠 |
|---|---|---|
| **T1**：$s(a)=1,\ s(\Gamma)=\zeta$, $\Gamma=\Sigma\setminus\{a\}$ のもと、任意の $L\in\mathcal C^{\rm mcf}_{f,s}$ に、$\|G\|,\bar\theta_G$ の多項式長の共通特徴標本がある | **未解決**（肯定証明・反例とも得ていない） | §§6, 9–10 |
| $|\Sigma|=2$、全 $f\ge2$・$r\ge2$ | **証明済み（既存）** | 現行 `cor:two-letter-semilattice`、§2 |
| $a^4$ が現れると、$a$ の塊の再配分は、非中立文字の種類を問わず可能 | **証明済み** | 補題 3.1 |
| $aa z a$（$z\in\Gamma^+$）が現れると $az\equiv_L za$ | **証明済み** | 補題 3.2 |
| 非中立文字を一文字 $b$ に潰した像は、一般には $(f,s_{U,2})$-組代入可能でない | **反証**（そのような還元は誤り） | 命題 3.4 |
| 「$a^4$ と深い $\zeta$ 挿入があるなら Parikh 飽和」 | **反証**（多文字での一般化は誤り） | §4、$(a\mid bc)^+$ |
| $c$-deep insertion がない場合、任意の $\Sigma,f,r$ で $\tau=O_{f,r}(c\,|V|\bar\theta_G)$ | **証明済み（既存）** | 退避 `lem:app-u1-shallow`、命題 5.1 |
| 全語の $\zeta$-run が高々 $k$ 個の場合、$t_{\rm typ}=O_{f,r}( (k+1)|V|\bar\theta_G)$ | **証明済み（既存）** | 退避 `lem:app-u1-runs`、命題 5.2 |
| **新たに明示する条件付き上界**：所属が $(|w|_a,|w|_\Gamma)$ だけで決まる場合、任意の $\Sigma,f\ge2,r\ge2$ に $\tau\le H_{f,r}|V|^2\bar\theta_G^5$ | **証明済み（本報告内の導出）** | 定理 7.1、完全な証明 §§7.2–7.5 |
| 付録 H の挿入補題の、非中立文字の種類に依存しない構造的帰結 | **証明済み** | 補題 6.1 |
| 多文字版の「内部の非中立の隙間は高々一つ」 | **反証** | §4、既存レビューの命題 4.1 |
| 多文字の一般証明を妨げるのは、非中立の隙間の**順序を保った処理**である | **分析・未解決** | §§8–10 |
| 新しい条件付き定理が既に文献にあるか | **未確認** | §12 |

## 1. 設定・測度・量化

$\Sigma$ は有限、$|\Sigma|\ge2$、$a\in\Sigma$、$\Gamma:=\Sigma\setminus\{a\}\ne\emptyset$ とする。
\[
 U_1=\{1,\zeta\},\qquad 1\zeta=\zeta1=\zeta^2=\zeta,
 \quad s(a)=1,\quad s(x)=\zeta\ (x\in\Gamma).
\]
正の語 $u$ が純（型 $1$）であることと $u\in a^+$ は同値である。型 $\zeta$ は「$\Gamma$ の文字を少なくとも一文字含む」を意味する。空語は**別の** fresh identity $\mathbf1_\sharp$ で区別する。従って $|U_1^\sharp|=3$。

原稿 §2–§4 の通り、非終端 $A$ のファンアウト $d$ と型付き非終端 $X=A_{\mathbf t}$ に対し、$E_A$ は長さ $\le\theta$ の導出的な $d$-穴文脈、$L_X$ は型付き生成組集合、$\mathrm{Cl}_{L,s}(X)$ は $X$ に相当する組の分布同値類とする。以下
\[
 g=\|G\|,\quad v=|V|,\quad\theta=\bar\theta_G\ge1,\quad
 \tau_X=\min_{\mathbf z\in\mathrm{Cl}_{L,s}(X)}\|\mathbf z\|_1,
 \quad \tau=\max_X\tau_X
\]
と記す。$G$ は reduced good かつ $\operatorname{fan}\le f$、規則ランク $\le r$ の $L\cap\Sigma^+$ の表示であり、$L\in\mathcal C^{\rm mcf}_{f,s}$ とする。$f,r\ge2$ は固定。定数は、別記がなければ **$f,r$ のみに依存し、$|\Sigma|$ には依存しない**。

`lem:thickness-equivalence` により、各規則の直接書込文字数は $\le\theta$、各非終端 $B$ には $\|\omega_B\|_1\le\theta$ の生成組が存在し、$|E_A|_{\rm fix}\le\theta$ とできる。また `lem:app-u1-fillers` または現行 `lem:app-two-basic` の証明は型付け $s$ に依存しないので
\[
 \boxed{\displaystyle
 \tau_X=\min\{\|\mathbf z\|_1:\mathbf z\in(\Sigma^+)^d,
   s^{(d)}(\mathbf z)=\mathbf t,\ E_A[\mathbf z]\in L\}.} \tag{1.1}
\]
実際、型付き生成組 $\mathbf u\in L_X$ と $\mathbf z$ は型と受理文脈 $E_A$ を共有するから、組代入可能性により分布も一致する。逆向きは、$E_A$ が $\mathrm{Cl}_{L,s}(X)$ の全要素を受理することで従う。

`cor:distribution-representatives` により、全ての $X$ で $\tau_X$ が有界なら、**同じ**特徴標本 $K$ を $\mathcal B^{\le r}_{f,s}$ と $\mathcal B_{f,s}$ の双方について選べ、
\[
 \boxed{\displaystyle \|K\|_+
 \le 3^{fr}g(1+2\theta+r\tau)+\mathbf1_{\{\varepsilon\in L\}}.} \tag{1.2}
\]
ここで $N_{\rm typ}\le 3^{fr}g$ を用いた。§5 と §7 での上界は**いずれも両作用素**についてのものである。記号 $\|K\|_+=\sum_{w\in K}(|w|+1)$ は総符号長であり、標本の要素数や学習器の収束時点とは異なる。

## 2. 現時点で既存の二文字定理

現行 `thm:two-letter-content` と `cor:two-letter-semilattice` は、$|\Sigma|=2$ について全 $f\ge2$ に
\[
 \|K\|_+\le4^{fr}\bigl(3+rC_{f,r}\bigr)g^3\theta^5+
 \mathbf1_{\{\varepsilon\in L\}},\quad
 C_{f,r}=(r+1)\bigl(6r(3f+1)+(6f+1)3^f\bigr)
 \tag{2.1}
\]
を与える（$s_{U,2}\preceq c_{\{a,b\}}$ と `lem:typing-monotone`）。これは既存原稿の帰結であって、本報告の新結果ではない。退避されたより直接的な $U_1$ の証明 `lem:app-u1-*` は途中で**二文字性**を使っているため、単純な記号置換によって任意の $\Sigma$ に拡張できない。

## 3. 任意のアルファベットで成立する交換と、成立しない還元

### 補題 3.1（$a$ 塊の再配分）【証明済み】

$L$ のある語に $a^4$ が因子として現れるとする。$\sigma_a(w)$ を $w$ の極大な $a$ 塊を一文字 $a$ に縮めた語（$\Gamma$ 文字の種類と**順序はそのまま残す**）とする。このとき
\[
 \sigma_a(w)=\sigma_a(w'),\quad |w|_a=|w'|_a
 \quad\Longrightarrow\quad [w\in L\iff w'\in L]. \tag{3.1}
\]

**証明**。$pa^4q\in L$ を取る。型 $(1,1)$ の二組 $(a,aa)$ と $(aa,a)$ は文脈 $p\square_1a\square_2q$ をともに受理されるので、全ての許容二穴文脈で交換できる。$w=U a Z aa V$ で $Z\in\Gamma^+$ の場合、文脈 $U\square_1Z\square_2V$ に適用して
\[
 U a Z aa V\in L\iff U aa Z a V\in L.
\]
これは二つの異なる $a$ 塊の間で一文字を移す操作である。同じ骨格を持つ語の $a$ 塊長は、塊の数を $h$ とすると、総和 $|w|_a$ の $h$ 個の正整数への分割である。この分割全体は、長さ $\ge2$ の塊から他の塊へ一単位を移す操作で連結である。各操作で所属は保たれる。□

### 補題 3.2（隙間全体の交換）【証明済み】

補題 3.1 の仮定のもと、$z\in\Gamma^+$ で $Uaa z aV\in L$ または $Ua z aaV\in L$ ならば、
\[
 \mathcal D_L^{(1)}(az)=\mathcal D_L^{(1)}(za). \tag{3.2}
\]

**証明**。前者を考える。補題 3.1 により $Ua z aaV\in L$。文脈 $(Ua,aV)$ が $az$ と $za$ をともに受理する。これらはどちらも型 $\zeta$ だから、一穴代入可能性により分布が等しい。後者も対称。□

重要な限定：式 (3.2) の $z$ は**語のまとまり**である。例えば $z=bc$ なら $a(bc)$ と $(bc)a$ の交換ができても、$ab\equiv_L ba$ や $ac\equiv_L ca$ は導けない。

### 補題 3.3（隣接する非中立の隙間の合流）【証明済み】

$L$ に $a^4$ が現れ、$w\in L$ が少なくとも一個の余分な $a$（すなわち $|w|_a$ が $a$ 塊数より大きい）を持つとする。隣接する二つの**内部** $a$-隙間が $z,z'\in\Gamma^+$ であり、その間の $a$ 塊の外にも $a$ 塊があるとき、中間の $a$ 塊を消し、その文字 $a$ を残る塊へ移して、隙間 $zz'$ を一つに結合した語も $L$ に入る（左右反転も可）。

**証明**。中間の $a$ 塊の左側に別の $a$ 塊がある場合を書けば足りる。補題 3.1 により、同じ骨格・$a$ 個数を持つ二語
\[
 W_2=P a z aa z'Q\in L,\qquad
 W_1=P' a z a z'Q'\in L
\]
を選べる（周囲の $a$ は $P,Q$ に吸収し、中間の塊を長さ 2 と 1 に配分する）。$W_2$ のほかに $Paaz a z'Q\in L$ も補題 3.1 により従う。よって文脈 $(P,az'Q)$ は $aza$ と $aaz$ をともに受理し、両者の型は $\zeta$ だから
$\mathcal D_L^{(1)}(aza)=\mathcal D_L^{(1)}(aaz)$。
これを $W_1=P'[aza]z'Q'$ の文脈 $(P',z'Q')$ に適用すると
$P'aa zz'Q'\in L$。全ての操作で $a$ の総数は保存される。右側にしか別の $a$ 塊がない場合は語を反転して同様に証明する。□

この合流自体は二文字でも多文字でも起きる。**合流した $zz'$ が禁止されるという結論は一般にはない**。

### 命題 3.4（$\zeta$ 文字の一文字への潰し込みは不正）【反例の完全な証明】

$\Sigma=\{a,b,c\}$、$s(a)=1$、$s(b)=s(c)=\zeta$ とし、
\[
 L=\{b,cc\}.
\]
この有限正則言語は全ての $f\ge1$ で $\mathcal C^{\rm mcf}_{f,s}$ に属する。一方、$\pi(a)=a$, $\pi(b)=\pi(c)=\beta$ とすると、$\pi(L)=\{\beta,\beta\beta\}$ は**一穴代入可能ですらない**。

**証明**。$L$ の正の因子は $b,c,cc$ のみ。型 $\zeta$ の一穴分布は
\[
 \mathcal D_L(b)=\{(\varepsilon,\varepsilon)\},\quad
 \mathcal D_L(cc)=\{(\varepsilon,\varepsilon)\},\quad
 \mathcal D_L(c)=\{(\varepsilon,c),(c,\varepsilon)\}.
\]
よって分布の共通部分を持つ異なる因子 $b,cc$ の分布は一致し、一穴条件を満たす。$L$ の語の長さは高々 2 なので、穴の間を非空にする許容文脈で二個以上の正の穴を持つ出現はなく、$d\ge2$ の条件は空虚である。$L$ は有限正則だから全ての $f$ の MCFL である。

一方、$\pi(L)$ では $\beta$ と $\beta\beta$ が空文脈でともに受理されるため型 $\zeta$ のもと同分布でなければならない。しかし $(\varepsilon,\beta)$ は $\beta$ を受理して $\beta\beta$ を受理しない。矛盾。□

これは**単純な射影・二文字化による T1 の帰着は存在しない**ことの反例である。より巧妙な符号化・部分言語への帰着を否定するものではない。

## 4. 二文字の補題 B は $U_1$ でも一般化できない

退避版 `lem:app-u1-deep` は二文字では $a^6b^ea^6$ から Parikh 飽和を強制する。しかし $\Gamma$ が複数文字のとき $z$ に異なる文字が現れると、元の証明で $b\cdot b^{e-1}=b^{e-1}\cdot b$ と置換する箇所が失われる。ここで必要なのは、文字をまとめた型が等しいという事実だけではなく、**積の語が同じ順序に並ぶ**という事実である。

具体的に $L_\circ=(a\mid bc)^+$ は、2026-11-01 の既存レビュー「三文字の内容型付け」§4・命題4.1 に**全ての型付けと全ファンアウト**に対する組代入可能性の完全証明が記されている。したがって $L_\circ\in\mathcal C^{\rm mcf}_{f,s_{U,\Sigma}}$ でもある。$L_\circ$ には $a^6bc a^6$ があり、$a^4$ もあり、内部の $\Gamma$-隙間を任意個持つ語 $aa(bca)^N$ が全ての $N$ について存在する。それにもかかわらず $acb\notin L_\circ$ かつ $abc\in L_\circ$ であるから Parikh 飽和でない。$a$ と $b$ の一文字交換も $a$ と $c$ の一文字交換も強制されない。

合流補題 3.3 はこの言語にも適用できる。しかし合流後の $(bc)^2$ は合法なので、元の二文字証明の「非中立の塊が長くなって矛盾」という最終段階は成立しない。さらに、**$|\Gamma|=2$ に絞ってもこの障害は残る**。

## 5. 一般アルファベットで既に証明できる無条件・条件付きの上界

### 命題 5.1（浅い挿入の場合：既存補題）【証明済み】

$c\ge1$ を整数とし、$L$ のどの語も因子 $a^c z a^c$（$z$ は型 $\zeta$）を持たないとする。このとき退避 `lem:app-u1-shallow` は**任意の $U_1$ 型付け**について証明されているので、$\Sigma$ の大きさを問わず
\[
 \tau\le 2^{f+1}cf(r+1)v\theta. \tag{5.1}
\]
従って (1.2) により両作用素の共通特徴標本は
\[
 \|K\|_+\le3^{fr}g\bigl[1+2\theta+
 r 2^{f+1}cf(r+1)v\theta\bigr]+\mathbf1_{\{\varepsilon\in L\}}. \tag{5.2}
\]
特に $a^4$ が一度も現れないなら $c=4$ とでき、$\tau\le2^{f+3}f(r+1)v\theta$ となる。

**既存証明が多文字で成立する理由の検査**。型 $1$ 成分の先頭・末尾の各 $c$ 文字、型 $\zeta$ 成分から一個の $\Gamma$ 文字を標識する。標識を書き込む節点の先祖経路 $H$ は、型付きラベル数の上界 $2^fv$ を用いて $|H|\le 2cf\cdot2^fv$ である。$H$ からぶら下がる部分木を長さ $\le\theta$ の $\omega_B$ に替えていく。$\zeta$ 成分は標識により型を失わない。純な成分が非純に変われば、固定した $a^c$ 接頭・接尾の間に型 $\zeta$ が入り、仮定した禁止因子を持つ合法語ができて矛盾。よって全置換が型を保ち、長さは $\le(r+1)\theta|H|$。ここに非中立文字の種類は使っていない。

### 命題 5.2（非中立文字の塊数が有界：既存補題）【証明済み】

$\zeta$-run を極大な $\Gamma^+$ 因子と呼ぶ。全ての $w\in L$ が $k$ 個以下の $\zeta$-run を持てば、退避 `lem:app-u1-runs` により
\[
 t_{\rm typ}(G,s)\le 2^f(r+1)\bigl(2f+(2f+1)k\bigr)v\theta. \tag{5.3}
\]
これは**代入可能性を仮定しない**文法的短縮補題であり、$t_{\rm typ}$ への上界であるから $\tau\le t_{\rm typ}$ と (1.2) より
\[
 \|K\|_+\le3^{fr}g\bigl[1+2\theta+
 r2^f(r+1)(2f+(2f+1)k)v\theta\bigr]
 +\mathbf1_{\{\varepsilon\in L\}}. \tag{5.4}
\]
証明は、純成分の両端・非純成分の非中立文字を標識し、重い部分木を一斉置換したとき現れる異なる $\zeta$-run の個数から重い節点の反鎖幅を $2f+(2f+1)k$ に抑え、型付きラベル数 $\le2^fv$ と組み合わせるもの。完全な証明は退避ファイルの同ラベルにある。

**適用範囲の注意**：$\zeta$-run 一個の長さや含む異なる文字の数が有界なだけでは、(5.3) の前提は満たされない。例えば $(a\mid bc)^+$ は各 $\Gamma$-run が長さ 2 以下である一方、$\zeta$-run の個数には上限がない。

## 6. 付録 H の移植表、および挿入補題の一般化

| 現行 Appendix H の項目 | $s_{U,\Sigma}$ に対する扱い | 判定の理由 |
|---|---|---|
| `lem:app-two-basic` (i) | **(i) そのまま** | 分布類 (1.1) の議論は型付けに依存しない |
| `lem:app-two-basic` (ii) | **(i) そのまま** | good grammar の線形性・非削除・非結合だけを用いる |
| `lem:app-two-runs` (i) | **(i) 任意の $x\in\Sigma$ でそのまま成立** | $(x,xx)$ と $(xx,x)$ は $s$-型が等しい。補題 3.1 は本問に必要な $x=a$ の場合を書いた |
| `lem:app-two-runs` (ii) | **(iii) 飽和結論を再構築要** | $a$ と**隙間全体** $z$ の交換は補題 3.2。全 Parikh 飽和は従わない |
| `lem:app-two-runs` (iii) | **(iii) 直接移植不可** | 内部の異なる文字から成る $\Gamma$-隙間は一文字 $y$-run ではない |
| `lem:app-two-runs` (iv) | **(iii) 反例あり** | $(a\mid bc)^+$ に内部の非中立隙間が任意個存在 |
| `lem:app-two-alternate` | **(iii) 再構築要** | 二文字の二種類の run だけでは多文字の並びを記述できない |
| `lem:app-two-insertion` | **(ii) 結論を弱めて成立** | 下の補題 6.1。二個の隙間ができるが矛盾にはならない |
| `prop:app-two-nonsaturated` | **(iii) 証明未完** | `runs`(iv) で必要な矛盾を作れず、重い節点の反鎖幅を有界にできない |
| `lem:app-two-saturated` | **(ii) 強い飽和仮定のもと拡張** | 二値計数飽和なら定理 7.1。一般の $L$ には適用不可 |
| `Proof of thm:two-letter-content` | **(iii) そのまま移植不可** | 非飽和枝が閉じておらず、両枝の合併で T1 を得られない |

### 補題 6.1（単一純文字の挿入反鎖補題）【証明済み】

$X=A_{\mathbf t}$ について $\widetilde G_0$ の型付き導出 $T$ を、生成組の総長が最短で、さらに節点数が最小なものとする。節点の生成組総長が $\theta$ を超えるとき重いと呼ぶ。重い節点の反鎖 $Q$ が
\[
 |Q|\ge 7f+2 \tag{6.1}
\]
を満たすなら、(a) $a^5$ は $L$ のある語の因子であり、(b) $L$ の別の語には、$a$ に挟まれた**相異なる二個以上の内部 $\Gamma^+$-run** がある。後者は元の純な成分の内部に生じ、同じ成分にある必要はない。

**証明**。$X$ の型 $1$ の成分ごとに最初の二文字・最後の二文字を標識し、型 $\zeta$ の成分ごとに $\Gamma$ 文字一個を標識する。標識総数は $\le5f$。各標識は導出木中のただ一個の書込節点に由来するので、互いに素な部分木を持つ $Q$ のうち、標識を一つも書き込まない節点の集合 $Q_0$ は
$|Q_0|\ge|Q|-5f\ge2f+2$。

$h\in Q_0$ を取る。型付けを忘れて $h$ の部分木を $\omega_{B_h}$ の導出に替えると、全体は $G$ の適法な導出であり、節点 $h$ の生成組総長が $\theta$ 超で $\|\omega_{B_h}\|_1\le\theta$ だから、根の生成組も短くなる。全ての $\zeta$ 成分は標識により $\zeta$ のままである。もし全ての純成分も純のままなら型付き導出に再び持ち上がり、$X$ の最短性に反する（`lem:witness-length-template`(i)）。従って、どれかの元の $a$-純成分の、$h$ に属する一つのブロックに $\Gamma$ 文字が入った。そのブロックは標識を含まないので、前後に元の $a$ が少なくとも二個ずつ残る。その元の純成分は長さ $\ge5$、$E_A$ に挿入すると $a^5$ は $L$ の因子となり、(a) が従う。

$Q_0$ の二節点を、ある根成分における両者のブロックが隣接するとき結ぶ。各節点が所有するブロック数は $\le f$、各ブロックには隣接するブロックが高々二つなので、このグラフの最大次数は $\le2f$。従って独立集合 $I$ があり、
$|I|\ge\lceil |Q_0|/(2f+1)\rceil\ge2$。$I$ の全部の部分木を同時に $\omega_{B_h}$ に替えた根の生成組 $\mathbf u'$ は $L_A(G)$ に属するので、$E_A[\mathbf u']\in L$。各 $h\in I$ は元の純な根成分内に少なくとも一つ $\Gamma$ 文字のブロックを作る。根成分の左右の標識された $a$ は保存される。二所有者のブロックが同一成分にある場合も、独立性のため、両ブロックの間に変更されない $a$ が存在する（間隙が非空なら元の文字、間隙が別所有者のブロックならその所有者は $I$ に入っていない）。従ってそれぞれの $\Gamma$ 文字は別々の極大 $\Gamma$-run に属し、その両側に $a$ が残る。これで (b)。□

**止まる場所**：二文字では、この (b) と `lem:app-two-runs`(iv) が衝突して反鎖数を抑える。今の $s_{U,\Sigma}$ では $L=(a\mid bc)^+$ が (b) を何個でも実現するので、同じ背理法を終結させられない。

## 7. 新しい条件付き定理：$(a,\Gamma)$-二値計数飽和

### 7.1 命題と定数

$L$ が **二値計数飽和**（binary-count saturated）であるとは
\[
 (|u|_a,|u|_\Gamma)=(|w|_a,|w|_\Gamma)
 \Longrightarrow (u\in L\iff w\in L)\qquad(u,w\in\Sigma^+)
 \tag{7.1}
\]
をいう。これは通常の Parikh 飽和**より強い**仮定である。$b\in\Gamma$ を一文字固定すると、どの許された二値計数も $a^p b^q$ で実現される。

**定理 7.1【証明済み、文献既知性は未確認】**。$f,r\ge2$、$L\in\mathcal C^{\rm mcf}_{f,s_{U,\Sigma}}$ が (7.1) を満たすとする。次の $f,r$ だけに依存する定数をおく：
\[
 H_{f,r}:=(r+1)\bigl(2^ff+(f+1)(f+2)+6r(3f+1)+10\bigr).
 \tag{7.2}
\]
任意の reduced good 表示 $G$ に対して
\[
 \boxed{\tau(G,s)\le H_{f,r}v^2\theta^5}. \tag{7.3}
\]
従って $\mathcal B^{\le r}_{f,s}$ と $\mathcal B_{f,s}$ の**共通**の特徴標本 $K$ に
\[
 \boxed{\displaystyle
 \|K\|_+\le3^{fr}(3+rH_{f,r})g^3\theta^5+
 \mathbf1_{\{\varepsilon\in L\}}.} \tag{7.4}
\]
$f,r$ 固定のとき、係数も次数も $|\Sigma|$ に依存しない。

### 7.2 型ごとの最適化と「すべて $\zeta$」の型

$X=A_{\mathbf t}$ のファンアウトを $d\le f$、型 $1$ 成分数を $h$、型 $\zeta$ 成分数を $j=d-h$ とする。$E_A$ の二値計数を $(p,q)$ とし、$p+q\le\theta$。$\mathcal P=\{(|w|_a,|w|_\Gamma):w\in L\cap\Sigma^+\}$ とおく。式 (1.1) と (7.1) より
\[
 \tau_X=\min\{n_a+n_\Gamma:
 n_a\ge h,\ n_\Gamma\ge j,\
 (p+n_a,q+n_\Gamma)\in\mathcal P\}. \tag{7.5}
\]
実際、$h$ 個の型 $1$ 成分にはそれぞれ $a$ が一個以上必要、$j$ 個の $\zeta$ 成分にはそれぞれ $\Gamma$ が一個以上必要で、これ以外の制約はない。与えられた計数をこれらの成分に分配した語の組を作れ、(7.1) により $E_A$ に挿入した語は受理される。

まず $h=0$ とする。$X$ の型付き導出のうち節点数最小のものを取り、各根成分の $\Gamma$ 文字を一個標識する。同じ型付きラベルを先祖と子孫に持つ導出があれば、下側の部分木で上側を置換して節点数を減らせるため、そのような繰返しはない。型付きラベル数は $\le2^fv$、各標識の先祖経路の節点数は $\le2^fv$。これらの経路の和集合 $H$ は $|H|\le d2^fv$。$H$ からぶら下がる各部分木を長さ $\le\theta$ の $\omega_B$ に置換する。根の各成分の標識 $\Gamma$ は残るので、全成分は引き続き型 $\zeta$ である。従って根の組は同じ分布類に属し、長さは $\le (r+1)\theta |H|$。よって
\[
 h=0\quad\Longrightarrow\quad \tau_X\le f2^f(r+1)v\theta. \tag{7.6}
\]
これは (7.3) に収まる。

### 7.3 混合型 $h,j\ge1$

(7.5) の最小計数を $(n_a,n_\Gamma)$ とし
\[
 c_a=n_a-h+1\ge1,\quad c_\Gamma=n_\Gamma-j+1\ge1.
\]
$W=a^{p+n_a}b^{q+n_\Gamma}\in L$ とする（$b$ は固定した $\Gamma$ の一文字）。$W$ の成功導出で節点数が最小のものを $T$ とする。節点 $u$ の生成組内の二値計数を $(a_u,z_u)$ と書く。重い節点は $a_u+z_u>\theta$ のものとする。

もし重い節点 $u$ について $a_u<c_a$ かつ $z_u<c_\Gamma$ なら、その部分木を $\omega_{B_u}$ に置換して成功語を短縮できる。新しい二値計数から固定文脈 $(p,q)$ を引いても、$a$ の個数は少なくとも $n_a-a_u\ge h$、$\Gamma$ の個数は少なくとも $n_\Gamma-z_u\ge j$ である。この語は $G$ から導出されるから $\mathcal P$ に属し、(7.5) の最小性に矛盾する。よって全ての重い節点は $a_u\ge c_a$ または $z_u\ge c_\Gamma$ を満たす。

同じ非終端を持つ真の先祖 $u$・子孫 $u'$ の生成組計数差を $(\delta_a,\delta_\Gamma)$ とする。非削除性により両差は非負である。両差が 0 なら、非削除性のため各 $\Gamma$ 文字の個数差も非負で総和 0、従って**各文字の**個数差が 0 である。よって現行 `lem:app-two-basic`(ii)（good grammar の同 Parikh 短縮）が節点最小性に反する。一方、差が非零かつ $\delta_a<c_a,\delta_\Gamma<c_\Gamma$ なら上側の部分木を下側のものに替えて (7.5) の最小値を減らせる。従って同じ非終端を二度見る間には、$\lfloor a_u/c_a\rfloor$ または $\lfloor z_u/c_\Gamma\rfloor$ が真に減少する。

根の二つの商の和は
\[
 \left\lfloor\frac{p+n_a}{n_a-h+1}\right\rfloor+
 \left\lfloor\frac{q+n_\Gamma}{n_\Gamma-j+1}\right\rfloor
 \le p+h+q+j\le\theta+f, \tag{7.7}
\]
ここで $\lfloor(P+n)/(n-t+1)\rfloor\le P+t$ ($n\ge t\ge1$) を使った。従って根から葉への任意の経路上の節点数は $\le v(\theta+f+1)$。同じ深さの重い節点は互いに素な生成組を持ち、各節点が少なくとも $c_a$ 個の $a$ または $c_\Gamma$ 個の $\Gamma$ を持つので、その数は (7.7) により $\le\theta+f$。重い節点は先祖に閉じているから、その総数は $\le v(\theta+f)(\theta+f+1)$。

重い節点がなければ $|W|\le\theta$。そうでなければ、全ての終端文字は重い節点の直接書込または重い節点に接する軽い子の生成組に含まれ、一つの重い節点の寄与は高々 $(r+1)\theta$。従って
\[
 \tau_X=n_a+n_\Gamma\le|W|
 \le(r+1)v\theta(\theta+f)(\theta+f+1)
 \le(r+1)(f+1)(f+2)v\theta^3. \tag{7.8}
\]

### 7.4 すべて純な型 $h=d,\ j=0$：行剛性と反鎖の計数

この場合 (7.5) から
\[
 K:=\tau_X=\min\{k\ge h:(p+k,q)\in\mathcal P\}.
\]
$K\le\theta+2(f-1)$ なら $K\le(2f-1)\theta$ でよい。以下 $K>\theta+2(f-1)\ge p+2h-2$ と仮定する。$W=b^q a^{p+K}\in L$ の**節点数最小**の成功導出 $T$ を選ぶ。$B$ の $\omega_B$ の二値計数を $(x_B,y_B)$ と書く。以下の六段階は、現行 Appendix H `lem:app-two-saturated` の「全成分が $\{a\}$」の証明を、$b$ の個数を $\Gamma$ 文字総数に置き換えて検査・展開したものである。

**(P1) 行剛性。** $\mathcal P$ に $(c_0,y)$ と $(c_0+\delta,y)$ があり $c_0\ge1$、$1\le\delta\le K-h$ と仮定する。(7.1) により $b^y a^{c_0}$ と $b^y a^{c_0+\delta}$ がともに $L$ に属する。一穴文脈 $(b^y a^{c_0-1},\varepsilon)$ が $a$ と $a^{1+\delta}$ をともに受理するから、双方の型 $1$ と代入可能性によって
$\mathcal D_L(a)=\mathcal D_L(a^{1+\delta})$。$b^q a^{p+K}$ の末尾の $a^{1+\delta}$ を $a$ に替えれば、$(p+K-\delta,q)\in\mathcal P$ で $h\le K-\delta<K$。これは $K$ の最小性に反する。従ってそのような二点は存在しない。

**(P2) 導出木の高さ。** 同じ非終端を持つ先祖 $u$・真の子孫 $u'$ の $\Gamma$ 計数が同じなら、その間で失われる $a$ の個数は $\ge K-h+1$ である。差が 0 なら非削除性により全ての文字の個数差も 0 となり節点最小性に反し、$1\le\delta\le K-h$ なら短縮後に $(p+K-\delta,q)\in\mathcal P$ が生じ、$K$ 最小性に反する。一つの経路上の $\Gamma$ 計数は $0,\ldots,q$ の $q+1$ 通り。もし同じ非終端かつ同じ $\Gamma$ 計数の節点が三個現れれば $p+K\ge2(K-h+1)$、すなわち $K\le p+2h-2$ となり矛盾。よって経路長は高々 $2v(q+1)$。$\Gamma$ 文字を生成する節点（「混合節点」）は、$W$ にある $q$ 個の $\Gamma$ 文字のいずれかを書き込む節点への経路上にあり、その総数 $M$ は
\[
 M\le2vq(q+1)\le4v\theta^2. \tag{7.9}
\]

**(P3) 重い純節点。** $\Gamma$ を一文字も生成しない節点 $u$ を純と呼び、$a_u>\theta+f-1$ なら重い純節点と呼ぶ。$g_u:=a_u-x_{B_u}\ge f$ とする。同じ非終端を持つ二つの比較可能な重い純節点 $u\succ u'$ は、(P2) より $a_u\ge a_{u'}+K-h+1>\theta+f-1+K-h+1\ge p+K$ となり矛盾する。従って同じ非終端の重い純節点は互いに比較不能。

重い純節点の反鎖 $J$ の全てを $\omega_{B_u}$ に替えると、二値計数は $(p+K-\sigma(J),q+Y(J))$ に変わる。ただし
$\sigma(J)=\sum_{u\in J}g_u$、$Y(J)=\sum_{u\in J}y_{B_u}$。二つの反鎖 $J,J'$ で $\sigma(J),\sigma(J')\le K-h$ かつ $Y(J)=Y(J')$ なら、(P1) を両者が生成する $\mathcal P$ の二点に適用して
\[
 \sigma(J)=\sigma(J'). \tag{7.10}
\]
両点の $a$ 計数は少なくとも $p+h\ge1$ なので (P1) の前提を満たす。

**(P4) 非終端の重複。** $B$ が二個以上の重い純節点に現れるなら、それらは反鎖で、各生成長は
$a_u\le p+K-(\theta+f)\le K-f$。従って $g_u\le K-f\le K-h$。式 (7.10) を一元反鎖に用いると、それらの $g_u$ は同じ $g_B$、ゆえに生成長も同じ $\ell_B=x_B+g_B$ となる。$y_B=0$ なら一つの節点を替えるだけで $K$ を減らすから $y_B\ge1$。

このような $B$ の出現回数 $m_B$ が $>\theta$ のとき **頻出** と呼ぶ。頻出 $B,C$ について、$y_C\le\theta$ 個の $B$ 節点と $y_B\le\theta$ 個の $C$ 節点を別々に選べる。両方とも反鎖で、総 $\Gamma$ 増分は $y_By_C$。さらに選ばなかった同種節点が少なくとも一個あるため $y_Cg_B,y_Bg_C\le K-h$。式 (7.10) により $y_Cg_B=y_Bg_C$。よって全ての頻出ラベルに共通の比
\[
 \alpha:=g_B/y_B>0,\qquad \ell_B=x_B+\alpha y_B\le(1+\alpha)\theta \tag{7.11}
\]
が存在する。

**(P5) 比 $\alpha$ の上界。**
\[
 \alpha_*:=(r+1)(\theta+f-1)(2\theta+1)v
 \le3f(r+1)v\theta^2. \tag{7.12}
\]
頻出ラベルがあれば $\alpha\le\alpha_*$ を示す。$\alpha\le\theta$ なら明白。$\alpha>\theta$ とし、頻出ラベル $B$ の重い純節点 $u$ の部分木で、重い純節点の個数を $H_u$ とする。それらは部分木内で先祖に閉じ、各節点は高々 $\theta$ 文字を直接書き、その軽い子は高々 $r$ 個、各長さは高々 $\theta+f-1$。ゆえに
\[
 \ell_B\le(r+1)(\theta+f-1)H_u. \tag{7.13}
\]
重い純祖先の個数で節点を分類すると、(P3) から高々 $v$ 層で、各層は反鎖である。各層で頻出ラベルの節点の生成長は (7.11) から $\ge\alpha$、それらは互いに素なので、個数は $\le\ell_B/\alpha\le(1+\alpha)\theta/\alpha<\theta+1$。非頻出ラベルの重い純節点は $T$ 全体でも高々 $v\theta$ 個。従って
$H_u\le v(\theta+1)+v\theta=v(2\theta+1)$。これを (7.13) に入れると
$\alpha\le g_B\le\ell_B\le\alpha_*$。

**(P6) 計数。** 純節点を、$a_u>T_*:=(\alpha_*+1)\theta$ のとき **巨大** と呼ぶ。式 (7.11) と (P5) から頻出ラベルは巨大節点に現れない。従って巨大節点の総数は高々 $v\theta$、かつ純部分木のなかでは先祖に閉じている。さらに
\[
 T_*\le(3f+1)(r+1)v\theta^3. \tag{7.14}
\]
$W$ の全ての $a$ は、(i) 混合節点の直接書込、(ii) 巨大節点の直接書込、(iii) 混合または巨大節点の子にある、巨大でも混合でもない極大純部分木、のいずれかに属する。根自身が (iii) の場合も考慮すると、極大純部分木の個数は高々 $rM+rv\theta+1$ である。よって
\[
 \begin{aligned}
 p+K&\le\theta M+\theta v\theta+(rM+rv\theta+1)T_*\\
 &\le5v\theta^3+6rv\theta^2(3f+1)(r+1)v\theta^3\\
 &\le[5+6r(3f+1)(r+1)]v^2\theta^5.
 \end{aligned} \tag{7.15}
\]
ただし $r\ge2,v\ge1,\theta\ge1$ を使った。$K\le p+K$ だから、純型の場合も多項式で抑えられた。

### 7.5 証明の完結と限界

(7.6)、(7.8)、(7.15)、および小さい $K$ の場合を比較すれば、明示した (7.2) は全ての右辺を支配する。型付き非終端 $X$ は任意だったので $\tau\le H_{f,r}v^2\theta^5$、すなわち (7.3)。式 (1.2) と $v\le g$、$1+2\theta\le3g^2\theta^5$ により (7.4) を得る。□

**この証明を一般の場合へ誤用してはならない**。混合型の (7.5) や純型の (P1) では、根の語・置換後の語の $\Gamma$ 文字の**順序を捨てて計数だけで扱う**ため、(7.1) が必須である。一般の $s_{U,\Sigma}$-組代入可能性は (7.1) を含意しない（§4）。

## 8. さらに移植できる補題と、その正確な到達範囲

**一文字 $a$ の run 交換**と**隙間の合流**は、$\Gamma$ の文字の並びを保存する（補題 3.1–3.3）。ただし、二値計数での短縮と違って、$\Gamma$ の並びを自由に置換する権利は得られない。特に、型 $\zeta$ の組同士が同じ型であることは、異なる固定文脈における受理の同一性を保証するわけではない。**共通の受理文脈が先に必要**である。

退避 `lem:app-u1-parikh` の「すべて $\zeta$ の型を標識で保つ」部分は §7.2 の通り無条件に成立する。しかし「型 $1$ だけの最小代表」を扱う P1–P6 では、ある語から部分木を短縮した後に増減する $\Gamma$ 文字の**総数**だけでは、同じ行の別の語を比較できない。そこが残る核である。具体的に、$y_B$ が一致しても、短縮で挿入された語 $\omega_B$ の非中立文字列が異なる位置に現れるので、$\Gamma$ 計数一致を根拠に $a$ の個数の剛性を導くことはできない。

現行付録 H の「飽和／非飽和」の二分もそのままでは役立たない。多文字では普通の Parikh 非飽和でも多くの隙間を持つ合法な語があり、普通の Parikh 飽和でも $\Gamma$ 内の文字ごとの計数が複数残る。§7 が処理したのは、さらに強い **$a$ と $\Gamma$ 総数だけへの依存**である。

## 9. もし一般上界が偽なら、どんな反例が必要か

(1.2) を考えると、ある固定 $f,r,\Sigma$ でデータ長が $g,\theta$ の多項式で**一様に**抑えられないことを示すには、まず $\tau$ の同様の上界が破れる事例を探す必要がある（$\tau$ は上界のための量であり、$\tau$ が大きいこと自体はデータ下界ではない）。より直接的な下界を得るには `prop:rare-type` を使い、例えば
\[
 \mu_1(L_n,s)=\min\{k\ge1:a^k\in L_n\}=n^{\omega(1)},\qquad
 g_n,\theta_n=n^{O(1)} \tag{9.1}
\]
とできれば、**両標準作用素**およびクラス全体で特徴標本を持つ任意の集合駆動作用素に、$n^{\omega(1)}$ の総符号長下界が得られる（$1$ 型が実現している場合）。これは**反例の十分条件の設計仕様**であり、そのような族は本報告で構成できていない。

特に $L_n$ が有限で型 $1$ の語を含む場合は、その純な語 $a^N$ は一個しか存在できない。実際、$a^p,a^q\in L_n$、$p<q$ なら、共通の空文脈から両者の分布が一致し、$a^q=a^{q-p}a^p\in L_n$ を利用して $a^{2q-p}\in L_n$、同様に無限個の純な語が得られ、有限性に矛盾する。この古典的な剛性は現行 `op:S1` にも明記されている。

§5 の二補題から、**有限言語を用いて (9.1) 型の大きな $\tau$ を狙うなら**、(i) $a^c z a^c$ が任意の多項式規模 $c$ で現れるような深い挿入が必要であり、(ii) $\Gamma$-run の最大数も任意の多項式規模を超える必要がある（いずれも $g,\theta$ に対する量化）。さらに §7 により、(iii) 二値計数飽和ではないことが必要である。これらは**必要な方向の制約**であって、満たしただけで反例になるわけではない。

二穴比較を生き残るための具体的な設計課題は次の通り。

1. 非中立語の順序を構文的に記録しつつ、同じ二穴文脈で型 $\zeta$ の組が二通り受理されるときの交差置換を全て閉じる。
2. 純な $a$ 成分への非中立部分木の置換によって、異なる長さの純語 $a^p,a^q$ が同じ分布に入るのを防ぐ。
3. しかし各規則は長さ $O(\operatorname{poly}(n))$ の成功文中で使えるようにし、$\theta_G$ を小さく保つ。
4. 非中立語を単純な単色塊 $b^e$ にすると二文字定理に捕まるので、少なくとも二色の**並び**を本質的に使う。
5. 反例候補を採用する前に、二穴型付き代入可能性の**全組・全文脈**を、有限言語なら厳密に検査する。短い長さの無違反だけでは無限族の証明にならない。

今のところ、上の設計を満たす $G_n,L_n$ は得られていない。したがって **「$|\Sigma|=3$ で指数下界」などとは主張しない**。ファンアウト 1 の三文字倍増族は $1$ 型の文字を二個使うから本問の $s_{U,\Sigma}$ へ直接移植できず、二穴の冪移行（現行 `lem:power-transfer` と `thm:doubling-no-lift`）も障害になる。

## 10. T1 を閉じるのに不足する補題

候補となる最小の欠落命題を、強い仮定に分けて記す。

> **未証明の短縮命題 U（必要な形の候補）**：固定 $f,r,\Sigma$ について、$L\in\mathcal C^{\rm mcf}_{f,s_{U,\Sigma}}$ の任意の reduced good 表示 $G$ と型付き非終端 $X$ に対し、$E_A$ に挿入可能な同型組で総長が $\operatorname{poly}(\|G\|,\bar\theta_G)$ のものがある。特に $X$ の全成分が $a$-純であっても成り立つ。

これは T1 を (1.2) から得るのに**十分**な形だが、T1 との同値は示していない。非純成分だけの型は §7.2 の標識短縮で制御できる。混合型は純成分が汚れることを防ぎつつ非純成分を短縮する問題へ帰着し、全純型では純成分へ入った $\Gamma$ の文字列全体を消さねばならない。補題 3.3 は挿入によって生じた $a$ 塊の移動には使えても、$\Gamma$ 文字列そのものを消去・並べ替える手段ではない。

**特に検証すべき新しい方向**：非中立語を分布同値な「トークン」として縮約し、それを保ったまま P1–P6 の比例関係を復元すること。ただし、トークンが語や導出ごとに異なり得るので、固定有限種類だと仮定してはならない。別の方向は、$\Gamma$ 列を不変に保った二穴交換の正規形を構成すること。どちらも**研究提案**であり、証明済みではない。

## 11. 正確な有限検査用 Python 3（標準ライブラリのみ）

次の全文は、有限言語に対して許容文脈と $1\le d\le f$ の**全ての正の穴の出現**を列挙し、同じ型・共通文脈を持つ組の分布集合が一致するかを**正確**に判定する。$\{b,cc\}$ とその射影の検証に使える。有限言語なら、受理文脈は言語の全語中の出現から尽くされるため、検査は有限で完全である。コマンドは Windows の `py -3 script.py`。

```python
# Python 3 standard library only. Save as script.py.
from collections import defaultdict
from itertools import combinations


def typ(w, neutral='a'):
    assert w
    return '1' if all(x == neutral for x in w) else 'z'


def appearances(word, d):
    # Generate nonempty disjoint intervals, strictly separated by nonempty gaps.
    n = len(word)
    for cuts in combinations(range(n + 1), 2 * d):
        if any(cuts[2*i] == cuts[2*i+1] for i in range(d)):
            continue
        if any(cuts[2*i+1] == cuts[2*i+2] for i in range(d-1)):
            continue
        tup = tuple(word[cuts[2*i]:cuts[2*i+1]] for i in range(d))
        ctx = [word[:cuts[0]]]
        for i in range(d-1):
            ctx.append(word[cuts[2*i+1]:cuts[2*i+2]])
        ctx.append(word[cuts[-1]:])
        yield tup, tuple(ctx)


def exact_test(language, f=2, neutral='a'):
    distributions = defaultdict(set)
    by_context = defaultdict(set)
    for w in language:
        for d in range(1, min(f, (len(w) + 1)//2) + 1):
            for tup, ctx in appearances(w, d):
                types = tuple(typ(x, neutral) for x in tup)
                distributions[(types, tup)].add(ctx)
                by_context[(types, ctx)].add(tup)
    for (types, ctx), tuples in by_context.items():
        if len(tuples) < 2:
            continue
        first = next(iter(tuples))
        for other in tuples:
            if distributions[(types, first)] != distributions[(types, other)]:
                return False, (types, ctx, first, other,
                    distributions[(types, first)] - distributions[(types, other)],
                    distributions[(types, other)] - distributions[(types, first)])
    return True, None


if __name__ == '__main__':
    L = {'b', 'cc'}
    projected = {'B', 'BB'}
    print('original', exact_test(L, f=2))
    print('projection', exact_test(projected, f=2))
    assert exact_test(L, f=2)[0]
    assert not exact_test(projected, f=2)[0]
```

**監査上の注意**：このコードは集合に対する受理文脈の完全列挙であり、有限言語に限れば厳密判定である。しかし小さい $n$ の検査結果を一般の $n$ や無限言語の証明に昇格させてはならない。本報告の一般命題はこのプログラムの出力には依存しない。

## 12. 出典、既知性、今後の定理監査

1. 現行原稿 [`main.tex`](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/main.tex)、blob `52d568e72624bc58195761ba45c2d14312625bef`。§2–§4、`lem:thickness-equivalence`、`lem:witness-length-template`、`cor:distribution-representatives`、`prop:rare-type`、`lem:typing-monotone`、`cor:two-letter-semilattice`、Appendix H、§9 を参照した。
2. 退避 [`parked_fanout2_and_comparison.tex`](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/parked/parked_fanout2_and_comparison.tex)、blob `ef9347fc62d348ff3b033a8de25782ad9394a98d`。特に `lem:app-u1-fillers`、`lem:app-u1-identity`、`lem:app-u1-shallow`、`lem:app-u1-runs`、`lem:app-u1-transfer`、`lem:app-u1-deep`、`lem:app-u1-parikh`。**「浅い挿入」「run 個数」上界はこのファイルの既存成果**であり新規性を主張しない。
3. 退避 [`parked_u1_typing_level.tex`](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/parked/parked_u1_typing_level.tex)、blob `38145cf3761f387adf88cc5c8801a6be402f8b13`。`prop:three-letter-family` と `cor:typing-level-obstruction` はファンアウト 1 の二中立文字に関する下界を与えるが、本問とは仮定が異なる。
4. [`reviews/claude_ternary_content_2026-11-01.md`](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/reviews/claude_ternary_content_2026-11-01.md)、blob `658f3744cfdeea54d2566cfbcac3d38049c21e1d`。特に §§3–5 に、$x$ 塊再配分、隙間の合流、$(a\mid bc)^+$ の全ファンアウト代入可能性証明、および修復型の部分結果がある。
5. Yoshinaka の multidimensional substitutability と positive-data learning に関する原著（博士論文統合資料 03、原稿参考文献 `Yoshinaka2011`）。既存の qualitative learning と特徴標本構成を新発見として扱わない。

**文献既知性の判定**：一般化の主命題 T1 の肯定・否定は未解決。定理 7.1 は現行 Appendix H の飽和枝を二値計数に合わせて本報告で詳述したものだが、2026-11-02 時点での先行文献との網羅的照合はできていないため **新規性未確認** とする。したがって独立した論文定理としての優先権を主張しない。投稿に使う場合は、(i) 計数飽和仮定の必要性、(ii) P1–P6 の元論法との対応、(iii) $G$ が reduced good である箇所、(iv) 参照した退避補題の現行原稿への移植可否を、人手で再監査すること。

---

### 最終判定

**T1 は解決していない。** しかし、任意の $\Sigma$・固定 $f,r$ において、(A) 深い挿入が無い、(B) 非中立 run 数が有界、(C) 二値計数飽和、の三条件では、$\mathcal B^{\le r}_{f,s_{U,\Sigma}}$ と $\mathcal B_{f,s_{U,\Sigma}}$ の両方について、多項式総符号長の**共通**特徴標本が得られる。未証明の核心は、非中立文字列の順序を保持しつつ、純な $a$ 成分への多数の挿入を制御することである。

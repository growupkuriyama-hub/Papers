# 末尾1文字窓における特徴データ長：一般CFGへの拡張（第7次報告）

**対象**：$s=s_{0,1}$、ファンアウト1、固定有限アルファベット $\Sigma$、固定ランク上限 $r=r_{\max}\ge1$。**作成日**：2026-10-31。記号 $M=\|G\|$、$\theta=\bar\theta_G\ge1$、$q=|\Sigma|$。標本長は $\|K\|_+=\sum_{w\in K}(|w|+1)$。

| 主張 | 判定 | 根拠の節 |
|---|---|---|
| 任意の非終端 $A$、実現する末尾文字 $t$ について、$t$ 終端の最短 yield 長は $(r+1)|V|\theta$ 以下 | **証明済み** | §2、補題2.1 |
| $s_{0,1}$ では、稀な**文全体の末尾型**の各最短長の総和は $O(M\theta)$ | **証明済み** | §2、系2.2 |
| 各 $A,t$ に長さ $D\theta$ 以下の $t$ 終端 yield があれば、両方の $\mathcal B$ に $\operatorname{cs}\le C_{D,r,\Sigma}M\theta$ | **証明済み**（「末尾が安い」という追加条件） | §3、定理3.1 |
| ユーザー指定の「**先頭が安い**」条件のみで $\operatorname{cs}=O(M\theta)$ | **未解決** | §3.4、§6 |
| 長い末尾型状態の*型付き標準証明書*に限った最小追加費用 $\Lambda_D^{\mathrm{tw}}(G)$ により、$\operatorname{cs}\le C_{D,r,q}M\theta+\Lambda_D^{\mathrm{tw}}(G)$ | **証明済み**（定義した証明書方式についての上界） | §4、定理4.1 |
| $\max_{X\text{ 長型}}(d_X+1)\le\Lambda_D^{\mathrm{tw}}(G)=O_{r,q}(M^2\theta)$；$F_n$ では下端が $\Omega(M\theta)$ | **証明済み** | §4.2–4.3 |
| 一般に $\Lambda_D^{\mathrm{tw}}(G)=O(M\theta)$、または一般CFGで $\operatorname{cs}=O(M\theta)$ | **未解決** | §4–§6 |
| 「右端の元文法規則は右端でそれぞれ実観測しなければならない」 | **反証**（既知の $F_n$） | §5 |
| $s_{0,1}$ で $\operatorname{cs}=\omega(M\theta)$ の代入可能CFG族を構成した | **未解決**（そのような族は今回得ていない） | §5–§6 |
| 単純な無限代入可能言語について、ランク2の完全な $\mathcal B$ が短い証拠から復元することを長さ7まで確認 | **観察**（有限計算、一般証明とは別） | §7 |

## 1. 資料と正確な対象

照合した現行原稿は `02-v2-lg-fanout-boundary/main.tex`、Git blob `d03710d94d0274df05b7b49e53e85b218e65d599`。特に `def:reconstruction`、`prop:reconstruction-soundness`、`prop:completeness`、`lem:thickness-equivalence`、`lem:heavy-node-count`、`thm:window-group-polydata`、`cor:trivial-exact` を用いた。第3・4次Astra報告およびChatGPT第2・6次報告も照合した。

$G=(V,\Sigma,P,S)$ は $L\setminus\{\varepsilon\}$ の reduced good CFG とする。規則 $R$ を使う文の最短長を $\theta_G(R)$、$\theta=\max(1,\max_R\theta_G(R))$ とする。$s_{0,1}(w)=\operatorname{last}(w)$（$w\ne\varepsilon$）であり、一文字語も自身が型である。$\widehat s$ は空語だけを新しい単位元で区別する。good 条件から非終端 yield は非空である。

$\mathcal B=\mathcal B_{1,s}$ は全ランク版、$\mathcal B^{\le r}=\mathcal B_{1,s}^{\le r}$ はランク制限版。両者の **特徴標本**とは $K\subseteq L$ かつ、すべての有限 $K\subseteq K'\subseteq L$ に対して $L(\mathcal B(K'))=L$ となるものをいう。以下の証明は元文法の各非終端を学習器へ与えるものではなく、観測文字列 $x$ に一意に結び付いた $[x]$ で再現する。

## 2. 末尾型付き最短導出の「一本鎖」補題

**補題2.1（末尾型の最短 yield、今回の直接証明）。** 任意の $A\in V$ と $t\in\Sigma$ について、$L_A\cap\Sigma^*t\ne\varnothing$ とする。$d(A,t)=\min\{|u|:A\Rightarrow_G^*u,\;\operatorname{last}(u)=t\}$ とすれば

\[
\boxed{d(A,t)\le (r+1)|V|\theta.}\tag{2.1}
\]

**証明。** $A$ から末尾 $t$ の語を導出する木 $T$ のうち、yield 長が最小、次に節点数が最小のものを選ぶ。各非終端 $B$ は reduced なので、成功導出中に現れる。特に $B$ の最短 yield 長は $\theta$ 以下である（原稿 `lem:thickness-equivalence(ii)`）。また各規則が直接書く端末数も $\theta$ 以下である（同 (i)）。

節点 $v$ を、その yield が $\theta$ より長いとき **重節点**と呼ぶ。もし重節点の yield が根の最終文字を含まないなら、その部分木を $v$ と同じ非終端の長さ $\le\theta$ の yield の導出木で置換できる。この置換は最後の文字 $t$ に触れず、根の長さを真に減らすので矛盾する。従って全重節点の yield は根の最後の位置を含む。導出木の異なる枝の yield は互いに重ならないため、**全重節点は一つの祖先―子孫鎖**に並ぶ。

この鎖に同じ非終端 $B$ が祖先 $u$、真の子孫 $v$ として二度現れたとする。両節点とも根の最終位置を含むので、$v$ の yield は $u$ の yield と同じ文字 $t$ で終わる。$u$ の部分木を $v$ の部分木で置換すれば、根の末尾文字は $t$ のままで、根の長さは増えず、節点数は真に減る。長さが減れば第一最小性に、等しければ第二最小性に反する。ゆえに重節点鎖のラベルはすべて異なり、節点数は $|V|$ 以下である。

根が軽ければ長さは $\theta$ 以下で終了する。根が重い場合、根 yield の各端末位置は、いずれかの重節点が直接書く端末か、重節点の**軽い**子部分木の端末に属する。各重節点が直接書く端末は高々 $\theta$ 個、子は高々 $r$ 個、各軽い子 yield は高々 $\theta$ 個である。重節点数を $h\le|V|$ とすると根の長さは $h(\theta+r\theta)\le(r+1)|V|\theta$。これで (2.1) を得る。$\square$

この証明は末尾窓・ファンアウト1に専用の簡約である。一般の `lem:heavy-node-count` の有限モノイドのラベル数を使わず、右端に接する重節点の**非終端名だけ**を区別すればよい。

**系2.2（末尾型の希少性による下界手法の限界）。** $\mu_t(L)=\min\{|w|:w\in L,\operatorname{last}(w)=t\}$ とし、実現しない型を除いて足すと

\[
\sum_{t\in\operatorname{last}(L)}(\mu_t(L)+1)
\le q\bigl((r+1)|V|\theta+1\bigr)=O_{r,q}(M\theta).\tag{2.2}
\]

**証明。** $A=S$ に補題2.1を適用し、実現する末尾型は高々 $q$ 個であると数える。$|V|\le M$、$\theta\ge1$ を使う。$\square$

したがって原稿 `prop:rare-type` の**型ごとに一語必要**という下界を合算するだけでは、$s_{0,1}$ における $\omega(M\theta)$ 下界は得られない。これは別の下界を不可能とする主張ではない。

## 3. 完全な線形上界が成立する追加条件

「先頭が安い」と区別するため、次を置く。

**定義3.1（末尾が $D$-安い）。** 固定定数 $D\ge1$ に対し、すべての実現する $(A,t)$ で
\[
d(A,t)\le D\theta.\tag{3.1}
\]

**定理3.1（末尾安価条件の下での線形証拠定理）。** $L\in\mathcal C_{1,s_{0,1}}$、$G$ が上記の reduced good CFG、ランクが $r$ 以下、かつ (3.1) が成り立つとする。このとき、無制限版とランク $r$ 版の双方に特徴標本 $K$ が存在し（$\varepsilon\in L$ なら最後に $\varepsilon$ を追加）、
\[
\boxed{\|K\|_+\le
q|V|\bigl(1+(1+D)\theta\bigr)
+q^r|P|\bigl(1+(2+rD)\theta\bigr)
\le C_{D,r,q}M\theta+\mathbf1_{\{\varepsilon\in L\}}.}\tag{3.2}
\]

**補助文法の記号と規則の完全な指定。** $\mathcal T(A)=\{t\in\Sigma:L_A\cap\Sigma^*t\ne\varnothing\}$。記号は $A_t$（$A\in V,t\in\mathcal T(A)$）と新開始記号 $\widetilde S$ のみとする。元規則
\[
R:A\to\alpha_0B_1\alpha_1\cdots B_k\alpha_k\quad(0\le k\le r)
\]
および各 $t_i\in\mathcal T(B_i)$ に対し、右辺最終文字（最後が非終端 $B_i$ なら $t_i$）を $t$ として
\[
A_t\to\alpha_0(B_1)_{t_1}\alpha_1\cdots(B_k)_{t_k}\alpha_k.\tag{3.3}
\]
定数規則は $A_{\operatorname{last}(\alpha_0)}\to\alpha_0$ とする。開始規則は $\widetilde S\to S_t$（$t\in\mathcal T(S)$）とする。空語生成規則はこの補助文法にはない。元文法がgoodで非空 yield を持つので (3.3) の右辺は非空であり、後端の文字は一意に定まる。すべての $A_t$ は実現可能で、規則 (3.3) は子 yield を独立に選べるため元文法に戻せば正確に $L\setminus\{\varepsilon\}$ を生成する。記号数は高々 $q|V|+1$、非開始規則数は高々 $q^r|P|$、端末出現と子出現も定数 $q^r$ 倍までなので補助文法サイズは $O_{r,q}(M)$ である。

**代表・文脈・標本の完全な指定。** 各 $A_t$ に $h_{A,t}\in L_A$ を末尾 $t$ の最短語として選ぶので $|h_{A,t}|=d(A,t)\le D\theta$。各 $A$ について、成功導出中の $A$ 出現を一つ抜いた導出文脈 $e_A=(u_A,v_A)$ を選び、$|u_A|+|v_A|\le\theta$ とする。これは原稿 `lem:thickness-equivalence(iv)` により存在し、$e_S=(\varepsilon,\varepsilon)$ とできる。文脈は全ての $L_A$ yield に共通である。

各 (3.3) の左辺を $X=A_t$、子の代表を右辺へ代入した語を $z_R$ とする。**標本を**
\[
K=\{u_Ah_{A,t}v_A:A_t\}\ \cup\
\{u_Az_Rv_A:R\text{ は (3.3) の非開始規則}\}\tag{3.4}
\]
と定義する（$\varepsilon\in L$ なら $\{\varepsilon\}$ を併合する）。重複は除く。両種類とも実際に $L$ に属する観測文である。$h_{A,t}$ と $z_R$ は末尾 $t$ なので同じ $s$ 型であり、同一文脈 $e_A$ に入る。従って $[h_{A,t}]\to[z_R]$ が Link で得られる。$[z_R]$ からは (3.3) の分割に従って Comp が得られ、各子の代表 $h_{B_i,t_i}$ は観測された $z_R$ の非空因子である。子の導出木の高さで帰納すると $[h_{A,t}]$ は $A_t$ のすべての yield を生成する。$S_t$ の代表は (3.4) にそのまま現れ、Start が到達する。逆包含は `prop:reconstruction-soundness`、標本拡張に対しては Comp/Link/Start の単調性で従う。これで両作用素に対する特徴性を証明した。

**長さの会計。** 状態証拠は $|u_Ah_{A,t}v_A|\le(1+D)\theta$。規則 $R$ の明示端末数は $\theta$ 以下（原稿厚さ補題）、子は $k\le r$ 個、外側文脈は $\theta$ 以下なので $|u_Az_Rv_A|\le(2+rD)\theta$。それぞれ高々 $q|V|$、$q^r|P|$ 個であり、各語の $+1$ と必要に応じた空語の符号長1まで入れると (3.2) になる。$\square$

### 3.4 指定された「先頭が安い」との差

$F_n$ の $E_i$ では、最短の $c$ 始まり語 $C_i=c^iar^i$ が長さ $2i+1$、最短の $l$ 始まり語 $D_i^l=lC_{i-1}C_{i-1}$ が長さ $4i-1$ である。$\theta=4n-1$ なので、**すべての実現する先頭条件が $\theta$ 以下**である。しかし末尾 $a$ の $E_n$ 最短語は $U_n$、長さ $n(n+1)+1=\Theta(n^2)$ である。

したがって「先頭が $D$-安い」から (3.1) は導けない。**これは依頼T1(a)の否定ではない**。実際、$F_n$ 自身は第3次の背骨共有により $\operatorname{cs}=\Theta(M\theta)$ である。未証明なのは、任意文法でその共有を組み立てる段階である。

## 4. 長い状態の証拠費用 $\Lambda_D^{\mathrm{tw}}(G)$

通常の「文法右端規則を実際の右端で被覆する費用」$R(G)$（Astra第4次）を使うと、$F_n$ において $R(G_n)=\Theta(n^3)$ なのに $\operatorname{cs}=\Theta(n^2)$ なので、$R$ はBが必要とする真の背骨費用ではない。以下は別の、**型付き標準証明書方式に限った**精密な追加費用である。これを $\mathcal B$ 全体の最適背骨費用と取り違えない。

**定義4.1（型付き証明書の長型追加費用）。** $D\ge1$ を固定し、§3 の精密化の状態 $X=A_t$ について $d_X=d(A,t)$ とする。
\[
\mathcal H_D=\{X:d_X>D\theta\}\quad\text{（長型状態）}.\tag{4.1}
\]
各状態に $h_X\in L_X$ を選ぶ。ただし $X\notin\mathcal H_D$ では $|h_X|\le D\theta$ とする。各 $A$ に導出文脈 $e_A$ を $|e_A|\le\theta$ で選ぶ（$e_S=\square$）。§3 の (3.4) により得られる標準証明書の各語を、(i) 状態証拠でその状態 $X$ が長型、または (ii) 規則証拠で**子の一つ**が長型である場合に「長型証拠」と呼び、その集合を $K_{\rm long}(h,e)$ とする。その他を $K_{\rm short}(h,e)$ とする。重複する文は集合として一度数える。
\[
\boxed{\Lambda_D^{\rm tw}(G)=\min_{(h,e)\text{ 上記の選択}}\|K_{\rm long}(h,e)\|_+.}\tag{4.2}
\]
許される選択は存在し、費用は非負整数なので最小値が存在する。この定義は $G,L,s,D$ のみから定まり、学習器が導出した語を追加観測したことにはしない。長型状態が一つもなければ $\Lambda_D^{\rm tw}(G)=0$ とする。

**定理4.1（明示的加法上界）。** §1の仮定のもと、$L\in\mathcal C_{1,s_{0,1}}$ なら
\[
\boxed{\operatorname{cs}_{\mathcal B}(L),\ 
\operatorname{cs}_{\mathcal B^{\le r}}(L)
\le C_{D,r,q}M\theta+\Lambda_D^{\rm tw}(G)+\mathbf1_{\{\varepsilon\in L\}},}\tag{4.3}
\]
例えば $C_{D,r,q}=q(2+D)+q^r(3+rD)$ を取れる。

**証明。** (4.2) を達成する $(h,e)$ を選び、(3.4) の全標準証明書を $K$ とする（必要なら空語も加える）。各代表は元の型付き非終端の実際の yield なので、§3 の Link/Comp/Start 帰納法は長さに無関係に適用でき、$K$ は特徴標本である。短型状態証拠は長さ $\le(1+D)\theta$、長型の子を含まない規則証拠は $\le(2+rD)\theta$。個数はそれぞれ高々 $q|V|$、$q^r|P|$ なので $\|K_{\rm short}\|_+\le C_{D,r,q}M\theta$。集合の和について $\|K\|_+\le\|K_{\rm short}\|_++\|K_{\rm long}\|_+$ であり、必要なら空語の符号長1を加えて (4.3) を得る。$\square$

### 4.2 $\Lambda$ の一般上界・下界

**命題4.2。** $\mathcal H_D\ne\varnothing$ なら
\[
\boxed{\max_{X\in\mathcal H_D}(d_X+1)
\le\Lambda_D^{\rm tw}(G)
\le(q|V|+q^r|P|)\bigl(1+2\theta+r(r+1)|V|\theta\bigr).}\tag{4.4}
\]
右端は $O_{q,r}(M^2\theta)$ である。さらに長型の開始状態 $S_t$ が複数あれば
\[
\Lambda_D^{\rm tw}(G)\ge
\sum_{t:S_t\in\mathcal H_D}\bigl(d(S,t)+1\bigr).\tag{4.5}
\]

**証明。** 長型状態 $X=A_t$ の $e_A[h_X]$ は定義上 $K_{\rm long}$ の要素であり、長さは $\ge d_X$ である。多くの長型状態で同じ観測文を共用する可能性があるので、和ではなく最大を下界に使う。開始状態の場合は $e_S=\square$ で、末尾文字 $t$ の異なる代表文字列は相異なるので和を取れる。これが左辺と (4.5) である。

上界では各 $A_t$ の**最短**の末尾型 yield を代表に選ぶ。補題2.1により全代表長は $H=(r+1)|V|\theta$ 以下。長型証拠は全標準証明書の部分集合で、その各文の長さは、状態用なら $\theta+H$、規則用なら $2\theta+rH$ 以下。総個数は $q|V|+q^r|P|$ 以下。全ての $+1$ を加えて (4.4) 右辺が従う。$\square$

### 4.3 $F_n$ における $\Lambda$ と真の特徴標本長

$M_n=12n+3$、$\theta_n=4n-1$、$d(E_n,a)=n(n+1)+1$。固定 $D$ に対し、十分大きな $n$ では $E_n{}_a$ は長型だから
\[
 n(n+1)+2\ \le\Lambda_D^{\rm tw}(G_n)
 \ \le O_D(n^3),\qquad
 \operatorname{cs}_{\mathcal B}(F_n)=\Theta(n^2).
\tag{4.6}
\]

(4.6) の $\Lambda$ 上端は粗い上界であり、$\Lambda=\Theta(n^3)$ を証明したものではない。Astra第3次の $O(n^2)$ 証拠はそもそも**この型付き標準証明書方式を迂回し、観測された部分文字列から生成した非終端を共有している**。従って $\Lambda_D^{\rm tw}$ が常に $O(M\theta)$ と示せなくても、$\operatorname{cs}$ の線形上界が偽だとは言えない。逆に (4.3) を一般の $O(M\theta)$ へ押し下げるには、この $\Lambda$ の上界を改良するか、型付き標準証明書を越える新しい共有証明が必要になる。

## 5. 下界候補を潰す既知の三つの迂回路

$F_n$ の文法を再掲する：
\[
 E_0\to a,\qquad E_i\to lE_{i-1}E_{i-1}\mid cE_{i-1}r,\quad S=E_n,
 \quad\Sigma=\{a,l,c,r\}.
\tag{5.1}
\]
この言語は **Clark–Eyraud代入可能**（第3次報告で参照された既証明結果）なので $s_{0,1}$ の対象クラスに属する。$\|G_n\|=12n+3$、$\theta=4n-1$、作用素は全ランク版およびランク2版の双方であり、既知の証明では
\[
\operatorname{cs}_{\mathcal B_{1,s_{0,1}}}(F_n)
=\operatorname{cs}_{\mathcal B_{1,s_{0,1}}^{\le2}}(F_n)
=\Theta(n^2)=\Theta(M_n\theta_n).\tag{5.2}
\]

- **境界をまたぐ Link**：第2次の反例が示すように、$[x]$ の連結を元の $E_i$ 構文境界に制限することはできない。
- **内部で生成した非終端の右端への持ち込み**：第3次では $[\partial C_i]$、$[\partial U_i]$ などを文中の Comp/Link によって確立し、その生成能力を別の Comp の右端へ使う。右端の元規則を右端で観測した証拠は不要である。
- **同一文字列を使う非終端の無条件共有**：$[h]$ はその因子の観測出現ごとに複製されない。同じ文字列が複数語に現れれば、その文字列に付く Comp はすべて同じ非終端へ集まる。各構文役割に別の証拠語が必要という課金は妥当でない。

事実、Astra第4次が定義した「元のCFGの文末節点で全規則ラベルを被覆する」費用は
\[
R(G_n)=\tfrac23n^3+2n^2+\tfrac{10}{3}n+2,
\]
であるが、(5.2) によってこれはBの特徴標本の下界ではない。従って今回は**$\omega(M\theta)$ の下界族を主張しない**。仮に作るなら、(i) 対象クラスへの所属、(ii) $M,\theta$ の計算、(iii) $\mathcal B$ に限る下界かクラス全域の集合駆動作用素への下界かの区別、さらに上の三迂回路すべてへの対処が必要となる。系2.2により、末尾型を一種類ずつ丸ごと削除する議論だけでも足りない。

## 6. 一般上界の停止点（証明していない主張）

**T1本命 $\operatorname{cs}\le c_{r,\Sigma}M\theta$ は未解決**。§3は「末尾が安い」ときの十分条件であり、依頼の「先頭が安い」だけの定理ではない。§4の $\Lambda_D^{\rm tw}$ は実際に定義し両側を評価したが、元の右端節点を必ず実観測するという誤った仮定は置かず、型付き標準証明書という**制限付き方式**を計量している。

第3次の一般化で本当に必要なのは、長い $h_C$ を使う多数の右端型維持規則の証明を、異なる観測文へ $|h_C|$ ずつ課金せずに済ませる原理である。一本の代表導出木の接尾辞を揃えても、各代替規則 $R$ の $z_R$ が共通文脈で観測されるとは限らない。また、観測語に共通の長い因子が現れるだけで、その因子に必要な別の Comp 規則が観測されたことにもならない。形式的には、型付き規則
\[
A_t\to\alpha_0B_{1,t_1}\alpha_1\cdots B_{k,t_k}\alpha_k
\]
に対する長型代表の出現回数 $\deg_{\rm in}(B_{j,t_j})$ を $O(1)$ に抑える根拠がなく、単純な標準証拠の費用は
\[
\sum_{A_t}(|e_A|+|h_{A,t}|+1)
 +\sum_R\left(|e_{\mathrm{lhs}(R)}|+1+\#\mathrm{terminal}(R)
 +\sum_{j}|h_{B_{j,t_j}}|\right).\tag{6.1}
\]
これを無条件に $O(M\theta)$ とするのは誤りである。第4次§5は、子代表費用の反復を単に無重みの先頭費用・文脈費用へ吸収する評価が破れる固定アルファベットの例を既に与えている。その例も、最短特徴標本そのものの超線形下界ではない。

**次に証明すべき命題は具体的に二択である**：(A) 先頭安価仮定から、型付き右端状態の代替規則を束ねる $O(M\theta)$ の観測文字列集合を構成すること（規則の分割・共通文脈をすべて列挙して確認する必要あり）、または (B) その束ね方が不可能な言語を作り、上記三迂回路を含む**全てのB導出**に対して課金可能な独立制約を示すこと。現状では双方とも未証明である。

## 7. 小さい $n$ の完全Comp検査：末尾安価な代入可能族

固定アルファベット $\Sigma=\{0,1,\#\}$、各 $n\ge1$ に対し
\[
L_n=\{w\#: w\in\{0,1\}^*,\ |w|\equiv0\pmod n\}.
\tag{7.1}
\]
$n$ 個の非終端 $A_0,\ldots,A_{n-1}$、開始 $A_0$、添字を $n$ で割った剰余として
\[
 A_0\to\#;\qquad A_i\to0A_{i+1}\mid1A_{i+1}\quad(0\le i<n)
\tag{7.2}
\]
とする。全ての非終端は到達可能・生産的、規則は good、ランク1。記号単位で
\[
M_n=n+2+2n(1+1+2)=9n+2,\qquad\theta_n=n+1.
\tag{7.3}
\]
$A_i$ の yield はすべて末尾 $\#$ で、最短長は $i=0$ で1、$i>0$ で $n-i+1\le n+1$。したがって $D=1$ の末尾安価条件が一様に成り立つ。

**補題7.1（クラス所属）。** $L_n$ は Clark–Eyraud 代入可能であり、従って $L_n\in\mathcal C_{1,s_{0,1}}$。

**証明。** $L_n$ に現れる非空因子は、(I) $\{0,1\}^+$ 内の語、(II) $u\#$（$u\in\{0,1\}^*$）のどちらかである。二因子 $x,y$ が共通文脈 $(\alpha,\beta)$ を持つとする。(I) と (II) は共通文脈を持てない。実際、(II) を含む全体語が $L_n$ に入るには、$\beta=\varepsilon$ が必要であり、これでは (I) を含む全体語は末尾 $\#$ にならない。

(I) 同士なら、共通文脈で両方が受理されるので $|x|\equiv|y|\pmod n$。任意の別の文脈でも、二進語の条件は両者同じで、全体の $\#$ が最後に一つあるかどうかは文脈のみで決まり、長さの剰余も等しい。従って両者は同じ全ての文脈で受理される。(II) 同士なら $x=u\#$、$y=v\#$ と書け、共通文脈を持つため $|u|\equiv|v|\pmod n$。任意の別の文脈で受理されるには右文脈が空、左文脈が二進語である必要があり、そのもとで長さの剰余条件は両者で同値である。よって両者も文脈同値。これは型制限さえ不要な Clark–Eyraud 代入可能性を証明する。$\square$

**命題7.2（全ての $n$ の明示的特徴標本）。**
\[
K_n=\{\#,0^n\#\}\cup
\{0^i1\,0^{n-i-1}\#:0\le i<n\}.
\tag{7.4}
\]
は、全ランクおよびランク1の $\mathcal B$ に対して特徴標本である。その総長は
\[
\boxed{\|K_n\|_+=2+(n+1)(n+2)=n^2+3n+4=O(M_n\theta_n).}
\tag{7.5}
\]

**証明。** $H_i=0^{n-i}\#$（$0\le i\le n$、$H_n=\#$）とし、全ての $H_i$ が (7.4) の観測因子であることに注意する。$0\le i<n$ では $0^n\#$ の分割から Comp $[H_i]\to0[H_{i+1}]$ が得られる。さらに $0^n\#$ と $0^i1 0^{n-i-1}\#$ は共通文脈 $(0^i,\varepsilon)$ で観測され、因子 $H_i$ と $1H_{i+1}$ の末尾型はともに $\#$ である。従って Link $[H_i]\to[1H_{i+1}]$ と Comp $[1H_{i+1}]\to1[H_{i+1}]$ を使える。これで
\[
 [H_i]\Rightarrow 0[H_{i+1}],\qquad
 [H_i]\Rightarrow^*1[H_{i+1}]
\tag{7.6}
\]
が成立する。$i=n$ で $[H_n]=[\#]$ とする帰納法から、$[H_0]$ はすべての長さ $n$ の二進語 $v$ に対して $v[\#]$ を導出できる。また $\#$ と $0^n\#$ は同一の空文脈で観測され、型が同じなので Link $[\#]\to[H_0]$ がある。これと (7.6) を繰り返すと、$[\#]$ は任意の $v\in\{0,1\}^{kn}$ を前置して最後に Const $[\#]\to\#$ を使える。Start は $\#$ を標本に持つので $L_n$ 全体へ到達する。逆包含は補題7.1とBの健全性、標本を大きくした場合の完全性は単調性による。$\square$

この補助文法の状態は (7.2) の $A_i$（$n$ 個）に加えた新しい型付き状態を必要としない。標本から実際に使用するBの非終端は観測済みの $[H_i]$ と $[1H_{i+1}]$ であり、文字列一致による共有を使っている。$K_n$ の $n+2$ 個の語は明示的である。

### Python 3標準ライブラリのみ：実行したスクリプト全文

ChatGPT第6次の `Grammar` と同じ、**全端末ギャップを含む単項 Comp と隣接二項 Comp** への正規化（第2・6次の既知の補題）を用いる。端末ギャップ付きの任意の二項 Comp は二項切断と単項端末付加に分解できるため、ランク2以下の完全なBに等価である。ランク1の本例の証明には (7.6) の単項規則だけで足りる。Windows ではコードを `round7_check.py` に UTF-8 で保存して `py -3 round7_check.py` で実行する。

```python
"""Exact fan-out-one rank-two B parser for short finite samples.
Python 3 standard library only. Run: py -3 round7_check.py
"""
from collections import defaultdict
from itertools import product


def window(x):
    assert x
    return x[-1]


class Grammar:
    def __init__(self, sample):
        self.sample = tuple(sorted(set(sample)))
        fac = {w[i:j] for w in self.sample
               for i in range(len(w)) for j in range(i + 1, len(w) + 1)}
        self.fac = sorted(fac)
        ids = {x: i for i, x in enumerate(self.fac)}
        par = list(range(len(ids)))

        def root(x):
            while par[x] != x:
                par[x] = par[par[x]]
                x = par[x]
            return x

        def unite(x, y):
            a, b = root(x), root(y)
            if a != b:
                par[b] = a

        contexts = defaultdict(list)
        for w in self.sample:
            for i in range(len(w)):
                for j in range(i + 1, len(w) + 1):
                    x = w[i:j]
                    contexts[(w[:i], w[j:], window(x))].append(ids[x])
        for bucket in contexts.values():
            for x in bucket[1:]:
                unite(bucket[0], x)
        self.state = {x: root(ids[x]) for x in self.fac}
        self.starts = {self.state[w] for w in self.sample}

        unary = defaultdict(set)
        binary = defaultdict(set)
        for z in self.fac:
            parent = self.state[z]
            for i in range(len(z)):
                for j in range(i + 1, len(z) + 1):
                    if i == 0 and j == len(z):
                        continue
                    unary[(z[:i], z[j:], self.state[z[i:j]])].add(parent)
            for i in range(1, len(z)):
                binary[(self.state[z[:i]], self.state[z[i:]])].add(parent)
        self.unary = dict(unary)
        self.binary = dict(binary)

    def accepts(self, w):
        n = len(w)
        if not n:
            return False
        chart = [[set() for _ in range(n + 1)] for _ in range(n)]
        for d in range(1, n + 1):
            for i in range(n - d + 1):
                j = i + d
                x = w[i:j]
                states = set()
                if x in self.state:
                    states.add(self.state[x])
                for k in range(i + 1, j):
                    for a in chart[i][k]:
                        for b in chart[k][j]:
                            states.update(self.binary.get((a, b), ()))
                for left in range(d):
                    for right in range(d - left):
                        if left == right == 0:
                            continue
                        if left + right >= d:
                            continue
                        prefix = x[:left]
                        suffix = x[d-right:] if right else ''
                        for child in chart[i + left][j - right]:
                            states.update(self.unary.get((prefix, suffix, child), ()))
                chart[i][j] = states
        return bool(self.starts.intersection(chart[0][n]))


def target(w, n):
    return (w.endswith('#') and
            all(c in '01' for c in w[:-1]) and
            (len(w) - 1) % n == 0)


def main():
    for n in range(1, 5):
        K = {'#', '0' * n + '#'}
        K.update('0' * i + '1' + '0' * (n - i - 1) + '#'
                 for i in range(n))
        g = Grammar(K)
        tested = 0
        discrepancies = []
        for length in range(1, 8):
            for tup in product('01#', repeat=length):
                w = ''.join(tup)
                tested += 1
                if g.accepts(w) != target(w, n):
                    discrepancies.append(w)
        print('n=%d sample_words=%d cost=%d factors=%d tested=%d mismatches=%d'
              % (n, len(K), sum(len(w) + 1 for w in K),
                 len(g.fac), tested, len(discrepancies)))
        assert not discrepancies, discrepancies[:10]


if __name__ == '__main__':
    main()
```

### 実行結果（2026-10-31、今回実測）

```text
n=1 sample_words=3 cost=8 factors=5 tested=3279 mismatches=0
n=2 sample_words=4 cost=14 factors=11 tested=3279 mismatches=0
n=3 sample_words=5 cost=22 factors=19 tested=3279 mismatches=0
n=4 sample_words=6 cost=32 factors=29 tested=3279 mismatches=0
```

各 $n=1,2,3,4$ について長さ1–7の $\{0,1,\#\}$ の非空語 $\sum_{i=1}^{7}3^i=3279$ 個を全て検査し、復元文法の受理結果と (7.1) の所属判定との不一致は0件だった（**観察**）。任意の $n$ と任意長に関する特徴性は、上の命題7.2の証明による。

## 8. まとめ・原稿への採用判定

本報告で自立した証明を与えたのは **末尾型付き最短導出の一本鎖補題（2.1）と、希少末尾型下界の限界（2.2）**である。「末尾が安い」CFGに対する $O(M\theta)$ 定理は現行原稿の型付き witness 原理を完全に特殊化した系であり、独立した新規の一般学習定理とは扱わない。$\Lambda_D^{\rm tw}$ は (4.2) で厳密に定義された、制限付き証明書の長型費用である。短い代表・文脈の選択と語長の会計が明示されており、加法上界 (4.3) は正しいが、一般のギャップ解消を主張しない。

**論文に直ちに入れるべきではないもの**：一般 $O(M\theta)$、先頭安価条件だけによる同上、$\Lambda_D^{\rm tw}=O(M\theta)$、$\omega(M\theta)$ の新下界。これらはいずれも今回証明していない。独立検算後に使用可能なのは (2.1)–(2.2) と、(3.1) を明記した条件付き定理である。

**照合先**：

- [現行 `main.tex`](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/main.tex)
- [Astra第3次（$F_n$ の二次標本、局所証明書）](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/reviews/astra_window_gap_round3_2026-10-31.md)
- [Astra第4次（右端被覆費用、反復課金の障害）](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/reviews/astra_window_gap_round4_2026-10-31.md)
- [ChatGPT第2次（構文境界をまたぐLink、ランク2正規化）](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/reviews/chatgpt_window_gap_round2_2026-10-31.md)
- [ChatGPT第6次（完全Compの区間DP）](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/reviews/chatgpt_window_gap_round6_2026-10-31.md)

原稿との対応は現行GitHub取得時の版に限る。既報の結果は本報告では「既知」、新たな数学的推論はそれぞれ「証明」、プログラムの出力は「観察」と区別した。

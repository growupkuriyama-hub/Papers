# ファンアウト2の半束型付け：内容型付けへの完全帰着と、Thue–Morse 背骨に対する二穴再分割障害

**調査日：2026年11月1日**  
**対象：** `Papers/02-v2-lg-fanout-boundary/main.tex`（調査時の Git blob `9734506fc09a520f90b7b37923f1b4f06905bccd`）、特に `def:uniform-polydata`, `prop:rare-type`, `thm:lg-characterization`, `lem:power-transfer`, `op:fanout-two`。  
**範囲：** 固定ファンアウト $f\ge2$、規則ランク上限 $r\ge2$、固定有限アルファベット。以下の「証明済み」は本報告内に完全な証明を示したことを意味し、文献上の新規性・外部査読を意味しない。

## 結論の要約表

| 主張 | 判定 | 根拠の節 |
|---|---|---|
| 任意の擬多様体について「多項式データ $\Longleftrightarrow\mathbf V\subseteq\mathbf{LG}$」という境界が成立することと、$\mathbf{SL}$ が多項式データを持たないことは同値 | **証明済み** | §1.1 |
| $\mathbf{SL}$ の一様多項式データは、すべての有限アルファベットの**内容型付け** $c_\Sigma$ だけで判定できる | **証明済み** | §1.2 |
| $s$ より細かい $c_\Sigma$ の特徴標本は、$s$ に対する同じ標本にもなる（$L\in\mathcal C_{f,s}$ のとき） | **証明済み** | §1.2 |
| 粗い半束型の稀な型下界は、適当な内容型の稀な型下界に移る | **証明済み** | §1.3 |
| 内容型付けにおける一般の**二穴再分割移送補題** | **証明済み** | §2 |
| 長さ16の Thue–Morse 語を因子に持つ $(2,s)$-代入可能言語（$s$ は任意の半束型付け）は、指定された別語を必ず含む | **証明済み** | §3.1–§3.2 |
| 上記の別語の一つは `bbb` を含む。したがって、長さ16の Thue–Morse 語を含む**立方自由**な $(2,s)$-代入可能言語は存在しない | **証明済み** | §3.2 |
| Thue–Morse を唯一の無印語とする自然な小型倍増文法は、$n\ge4$ で $\mathcal C_{2,c_\Sigma}$ に属さない | **反証（候補構成に対する反例）** | §3.1、§4 |
| 長さスペクトルの種類数 $k$ が一定なら、すべての固定型付けについて $\|G\|,\bar\theta_G$ の多項式特徴データが存在する | **証明済み** | §5 |
| 上記の長さスペクトル結果や再分割補題が先行文献に同一の形であるか | **未確認** | §6 |
| $\mathbf{SL}$ の fan-out 2 全体が多項式データを持つか、あるいは超多項式の反例族を持つか | **未解決** | §6 |

## 1. T0：擬多様体と内容型付けへの帰着

### 1.1 擬多様体境界を $\mathbf{SL}$ 一つに帰着する

固定 $f,r$ について、原稿 `def:uniform-polydata` の性質を $P_{f,r}(\mathbf V)$ と記す。すなわち、すべての非空有限アルファベット $\Sigma$ と、像が $\mathbf V$ に属するすべての全射 $s:\Sigma^+\twoheadrightarrow S$ に対して、**$L,G$ に依存しない**多項式 $p_{f,r,s,\Sigma}$ が存在し、すべての $L\in\mathcal C_{f,s}$ とすべての reduced good なランク $\le r$ 表示 $G$ に対して $\mathcal B^{\le r}_{f,s}$ の特徴標本 $F$ が $\|F\|_+\le p(\|G\|,\bar\theta_G)$ を満たす、という性質である。

**命題1（半束への境界帰着）。** 固定 $f\ge1,r\ge2$ について、

\[
\bigl[\forall\mathbf V:\ P_{f,r}(\mathbf V)\iff\mathbf V\subseteq\mathbf{LG}\bigr]
\quad\Longleftrightarrow\quad
\neg P_{f,r}(\mathbf{SL}).
\]

**証明。** $U_1=\{1,\zeta\}$、$1\zeta=\zeta1=\zeta^2=\zeta$ とする。$U_1$ の生成する擬多様体は有限半束全体 $\mathbf{SL}$ である。実際、任意の有限半束 $H$ を積 $\wedge$ で書き、各 $z\in H$ に対して $\chi_z(x)=1$（$z\le x$ の場合）、それ以外を $\zeta$ と定めれば、$\chi_z(x\wedge y)=\chi_z(x)\chi_z(y)$ であり、$x\mapsto(\chi_z(x))_{z\in H}$ は $H\hookrightarrow U_1^H$ という単射準同型である。逆に $U_1$ の部分半群・商・有限直積はすべて半束である。

原稿 `thm:lg-characterization(ii)` により、$S\notin\mathbf{LG}$ なら $S$ は $U_1$ と同型な部分半群を持つ。ゆえに $\mathbf V\not\subseteq\mathbf{LG}$ なら $U_1\in\mathbf V$、したがって $\mathbf{SL}\subseteq\mathbf V$。性質 $P$ は擬多様体に関して下向きに遺伝する：$\mathbf W\subseteq\mathbf V$ かつ $P(\mathbf V)$ なら、$\mathbf W$ で量化する型付けは $\mathbf V$ で既に量化されているので $P(\mathbf W)$ である。従って $\neg P(\mathbf{SL})$ なら $\mathbf{LG}$ の外のすべての $\mathbf V$ が $P$ を満たさない。一方、$\mathbf V\subseteq\mathbf{LG}$ なら `thm:local-group-polydata` により $P(\mathbf V)$。これで右辺から左辺が出る。

逆に左辺を仮定して $\mathbf V=\mathbf{SL}$ と取る。$U_1\notin\mathbf{LG}$ なので $\mathbf{SL}\not\subseteq\mathbf{LG}$、よって $\neg P(\mathbf{SL})$。$\square$

**量化上の注意。** これは「特定の $U_1$ 型付け $s$ での問題」が自動的に $\mathbf{SL}$ 全体の問題と同値という意味ではない。特定の型付けに対する上界と、擬多様体の全型付けに対する上界は区別する。

### 1.2 内容型付けは「下界だけ」でなく「上界」も判定する

$\Sigma$ 上の**内容型付け**を
\[
c_\Sigma:\Sigma^+\twoheadrightarrow\mathcal P_+(\Sigma),\qquad
c_\Sigma(w)=\{a\in\Sigma:a\text{ が }w\text{ に現れる}\},
\]
とし、右辺には和集合を積とする。任意の半束型付け $s:\Sigma^+\twoheadrightarrow S$ は、$h(A)=\prod_{a\in A}s(a)$ と置いて $s=h\circ c_\Sigma$ と因数分解される。積は可換・冪等なので $h$ は well-defined な半束準同型である。特に原稿の精密化順序で $s\preceq c_\Sigma$。

**命題2（標準再構成作用素の型単調性）。** $s\preceq t$ とし、$L\in\mathcal C_{f,s}$ とする。任意の有限 $K\subseteq L$、任意の $r\ge1$ について、
\[
L\bigl(\mathcal B^{\le r}_{f,t}(K)\bigr)
\subseteq L\bigl(\mathcal B^{\le r}_{f,s}(K)\bigr)
\subseteq L.
\tag{1}
\]
従って $\mathcal B^{\le r}_{f,t}$ の $L$ に対する特徴標本は、そのまま $\mathcal B^{\le r}_{f,s}$ の特徴標本である。無ランク制限版 $\mathcal B_{f,t},\mathcal B_{f,s}$ でも同様である。

**証明。** 原稿 `def:reconstruction` の四種類の規則を比較する。Start・Const・Comp は型付けに依存せず、同一 $K$ について同じである。Link 規則は、共通受理文脈をもつ観測組の**対応成分の型が等しい**場合に加わる。$s\preceq t$ なら $t$ 型の一致は $s$ 型の一致を含意する。したがって $t$ の全規則は $s$ の全規則に含まれ、両者の非終端記号集合と開始記号も同じなので左側の包含を得る。右側は原稿 `prop:reconstruction-soundness`：$L$ の $(f,s)$-代入可能性による soundness である。

$F\subseteq L$ が $t$ の特徴標本なら、任意の $F\subseteq K\subseteq L$ で最左辺は $L$ である。(1) の両包含から中央も $L$ となる。無制限版はランク上限 $\|K\|_+$ が型に依存しないため同様。$\square$

この命題により、原稿が注意する「**任意の型付けに対する一般的な**特徴データ長の単調性は主張しない」と矛盾することなく、**同じ $L$ が粗い型のクラスにも入る場合**に限って、標準作用素の特徴データ長を比較できる。

**定理3（$\mathbf{SL}$ の完全な内容型付け帰着）。** 次は同値である。

1. $P_{f,r}(\mathbf{SL})$。
2. すべての非空有限 $\Sigma$ について、多項式 $p_{f,r,\Sigma}$ が存在し、$\mathcal C_{f,c_\Sigma}$ のすべての対象 $L$ とすべての該当する reduced good 表示 $G$ に対し、$\mathcal B^{\le r}_{f,c_\Sigma}$ の特徴標本が $\|F\|_+\le p_{f,r,\Sigma}(\|G\|,\bar\theta_G)$ を満たす。

**証明。** $1\Rightarrow2$ は $c_\Sigma$ の像が有限半束であることから直接従う。逆向きは、半束型付け $s$ を任意に取る。$s\preceq c_\Sigma$ より $\mathcal C_{f,s}\subseteq\mathcal C_{f,c_\Sigma}$（原稿 `def:class-cmcf` 直後の包含）。仮定2で $L,G$ に対する $c_\Sigma$ の短い特徴標本 $F$ を得る。命題2により同じ $F$ が $s$ の特徴標本になる。$p_{f,r,s,\Sigma}:=p_{f,r,\Sigma}$ とすればよい。$\square$

**帰結。** 固定 $f,r$ で $\mathbf{SL}$ の一様多項式データが失敗することは、**ある一つの固定有限アルファベット $\Sigma$ 上の内容型付け $c_\Sigma$** について定義の多項式上界が失敗することと同値である。従って T1 を内容型付けに集中する方針は数学的に正当であり、単なる探索上の便法ではない。

### 1.3 稀な型下界の移送と作用素の範囲

**命題4（稀な型の精密化移送）。** $s=h\circ c_\Sigma$、$L\in\mathcal C_{f,s}$ とし、$m\in s(L\cap\Sigma^+)$ とする。$T_m=\{A\in c_\Sigma(L\cap\Sigma^+):h(A)=m\}$ と置くと、
\[
\mu_m(L,s)=\min_{A\in T_m}\mu_A(L,c_\Sigma),\qquad
\mu_A(L,c_\Sigma)\ge\mu_m(L,s)\quad(A\in T_m).
\tag{2}
\]
特に $m$ が実現しているなら $T_m$ の任意の元は実現した内容型であり、$c_\Sigma$ 型 $A$ を観測する必要のある特徴標本に、同じ長さ下界がかかる。

**証明。** $s^{-1}(m)\cap L=\bigsqcup_{A\in T_m}(c_\Sigma^{-1}(A)\cap L)$ という有限分割を取り、各集合の最短長を比較するだけである。また $L\in\mathcal C_{f,c_\Sigma}$ であり、原稿 `lem:type-deletion`・`prop:rare-type` はこの内容型付けにも適用できる。$\square$

**作用素に関する正確な範囲。** (2) と `prop:rare-type` の下界は $\mathcal B^{\le r}_{f,c_\Sigma}$、$\mathcal B_{f,c_\Sigma}$ の特徴標本に成り立つ。さらに $L$ と $L\setminus c_\Sigma^{-1}(A)$ の双方に特徴標本を持つ**集合駆動作用素**にも成り立つ。特に $\mathcal C_{f,c_\Sigma}$ 全体で特徴標本を持つ任意の集合駆動作用素に適用できる。任意の Gold 逐次学習器の収束時刻の下界は意味しない。

---

## 2. T2：冪を必要としない二穴の「再分割移送」

**補題5（共通錨による二穴再分割移送）。** $s$ を任意の型付け、$L\in\mathcal C_{2,s}$ とする。$x=(x_1,x_2),y=(y_1,y_2)\in(\Sigma^+)^2$ が成分ごとに同じ $s$ 型を持ち、ある $E\in\mathcal E_2$ について $E[x],E[y]\in L$ なら、すべての $E'\in\mathcal E_2$ について
\[
E'[x]\in L\quad\Longleftrightarrow\quad E'[y]\in L.
\tag{3}
\]
とくに $s$ が半束型付けである場合、仮定の型一致には $c_\Sigma(x_i)=c_\Sigma(y_i)$ $(i=1,2)$ で十分である。

**証明。** 共通の $E$ は $\mathcal D_L^{(2)}(x)\cap\mathcal D_L^{(2)}(y)\ne\varnothing$ を与える。$(2,s)$-代入可能性の定義により二つの distribution が等しいため、任意の $E'$ に対して (3) が従う。半束の場合は $s=h\circ c_\Sigma$ による。$\square$

補題自体は代入可能性の定義の厳密なインスタンスであり、一般原理としての独立新規性は主張しない。新しい内容は、次節で **同じ語の二つの異なる再分割から、冪因子を全く使わずに具体的な禁止パターンを作ること**にある。`lem:power-transfer` と異なり、$u^5$ は不要である。

## 3. T1・T2：Thue–Morse 背骨の決定的な障害

$A_0=\mathtt a$, $B_0=\mathtt b$, $A_i=A_{i-1}B_{i-1}$, $B_i=B_{i-1}A_{i-1}$ と置く。$A_i$ は Thue–Morse 語の長さ $2^i$ の接頭辞である。特に
\[
F:=A_4=\mathtt{abbabaabbaababba},\qquad |F|=16.
\]
Thue–Morse 無限語は overlap-free、従って cube-free である（古典的事実）。以下の二穴障害は、それでも存在する。

### 3.1 同じ内容型の別語を強制する

二組と二文脈を次のように取る（$\blank_1,\blank_2$ は穴）。

\[
\begin{aligned}
 x&=(\mathtt{abba},\mathtt{aab}), & y&=(\mathtt{ab},\mathtt{abaab}),\\
 E_0&=\blank_1\,\mathtt b\,\blank_2\,\mathtt{baababba},
 & E_1&=\blank_1\,\mathtt{baabb}\,\blank_2\,\mathtt{abba}.
\end{aligned}
\]

四つの成分はすべて $\{\mathtt a,\mathtt b\}$ の内容を持つ。直接連結すると、
\[
E_0[x]=E_0[y]=E_1[x]=F,
\quad
E_1[y]=F_1:=\mathtt{abbaabbabaababba}\ne F.
\tag{4}
\]
よって補題5から、任意の有限半束型付け $s$ と任意の $L\in\mathcal C_{2,s}$ について
\[
P F Q\in L\quad\Longrightarrow\quad P F_1 Q\in L
\qquad(P,Q\in\Sigma^*).
\tag{5}
\]
文脈 $E_0,E_1$ に同じ $P,Q$ を外側から付け足せばよい。$F$ と $F_1$ は長さも Parikh ベクトルも等しいので、$c_\Sigma(PFQ)=c_\Sigma(PF_1Q)$、従って $s(PFQ)=s(PF_1Q)$ である。

**系6（単一内容型の禁止因子）。** $L\in\mathcal C_{2,c_\Sigma}$ において、ある内容型 $A$ の繊維 $L\cap c_\Sigma^{-1}(A)$ が単元集合 $\{W\}$ なら、$W$ は $F$ を因子に持たない。実は半束型付け $s$ の単一 $s$ 型繊維についても同様である。

**証明。** $W=PFQ$ と仮定すると (5) により、$W'=PF_1Q\in L$。$W'\ne W$ であり、しかも $s(W')=s(W)$、特に内容型も等しい。単元性に反する。$\square$

### 3.2 さらに立方 `bbb` を強制する

別の二組を使う。
\[
\begin{aligned}
 u&=(\mathtt{abbabaa},\mathtt{ba}),
 &v&=(\mathtt{ab},\mathtt{abaabba}),\\
 D_0&=\blank_1\,\mathtt b\,\blank_2\,\mathtt{ababba},
 &D_1&=\blank_1\,\mathtt{bbaa}\,\blank_2\,\mathtt{bba}.
\end{aligned}
\]
すべての対応成分の内容は $\{\mathtt a,\mathtt b\}$。連結を実際に展開すると
\[
\begin{aligned}
D_0[u]&=\mathtt{abbabaa}\,\mathtt b\,\mathtt{ba}\,\mathtt{ababba}=F,\\
D_0[v]&=\mathtt{ab}\,\mathtt b\,\mathtt{abaabba}\,\mathtt{ababba}=F,\\
D_1[u]&=\mathtt{abbabaa}\,\mathtt{bbaa}\,\mathtt{ba}\,\mathtt{bba}=F,\\
D_1[v]&=\mathtt{ab}\,\mathtt{bbaa}\,\mathtt{abaabba}\,\mathtt{bba}
=F_2:=\mathtt{abbbaaabaabbabba}.
\end{aligned}
\tag{6}
\]
$F_2$ は先頭から第2–4文字が $\mathtt{bbb}$ である。従って次が成立する。

**定理7（Thue–Morse 因子から立方を強制）。** $\Sigma\supseteq\{\mathtt a,\mathtt b\}$ とし、$s:\Sigma^+\twoheadrightarrow S$ は任意の有限半束型付けとする。$L\in\mathcal C_{2,s}$ かつ $PFQ\in L$ なら $PF_2Q\in L$。したがって **$L$ の全語が立方自由なら、$L$ のどの語も $F$ を因子に持てない**。

**証明。** (6) は $D_0[u]=D_0[v]=D_1[u]=F$ を示している。補題5を $PD_0(\cdot)Q$ と $PD_1(\cdot)Q$ に適用すれば $PF_2Q\in L$。後者は $\mathtt b^3$ を因子に持ち、立方自由に反する。$\square$

これは `lem:power-transfer` が前提とする $u^5$ 因子からは導かれていない。むしろ入力語 $F$ 自体は立方自由である。$F_2$ の出現を強制するのは、同じ $F$ を二通りに切り分けられるという**二穴の非剛性**である。

**留保。** この定理は「$u^3$ をすべて避ける」という T1(iv) の強い版を否定するが、$u^5$ だけの回避を一般に否定しない（$F_2$ に現れると示したのは $\mathtt b^3$ である）。$u^5$ 回避の一般的不可能性は本報告では証明していない。

### 3.3 すべての $n\ge4$ への移行

$A_{i+1}=A_iB_i$ だから $A_n=F R_n$ となる $R_n\in\{a,b\}^*$ がすべての $n\ge4$ について存在する。従って系6と定理7は $A_n$ に適用できる。

**系8。** $n\ge4$ とする。$A_n$ がある半束型付けの**唯一の実現語**（その型の唯一の語）である言語は $\mathcal C_{2,s}$ に入らない。また $A_n$ を含む言語が $\mathcal C_{2,s}$ に属するなら、その言語は必ず立方を含む語も含む。

後半は $A_n=FR_n$ に定理7を使い、$F_2R_n\in L$ とするだけである。したがって **Thue–Morse の無印背骨と、全語立方自由という要求は、fan-out 2 の半束代入可能性と両立しない。**

---

## 4. 小型の自然な候補族はどこまで成功し、どこで失敗するか

固定アルファベット $\Sigma=\{\mathtt a,\mathtt b,\mathtt d,\mathtt e,\mathtt f\}$ とし、任意にマーカー列 $m_i\in\{\mathtt d,\mathtt e,\mathtt f\}$ を固定する。文法 $H_n$ を
\[
\begin{aligned}
 S_0&\to A_n, & A_0&\to\mathtt a, &B_0&\to\mathtt b,\\
 A_i&\to A_{i-1}B_{i-1}\mid m_i A_{i-1}
 &&(1\le i\le n),\\
 B_i&\to B_{i-1}A_{i-1}\mid m_i B_{i-1}
 &&(1\le i<n).
\end{aligned}
\tag{7}
\]
と定める。マーカー列を平方自由な三文字列に選べば、全段で短縮枝を選んだ**一本の鎖**にマーカーの平方は生じない。ただし、これだけで文法の全生成語の立方自由性を保証したことにはならない。

**命題9（自然な候補の厳密な評価）。** $n\ge1$ について、(7) は reduced good、fan-out 1、ランク2、$\|H_n\|=O(n)$、$\bar\theta_{H_n}=O(n)$ である。内容型 $T=\{\mathtt a,\mathtt b\}$ の実現語は $A_n$ ただ一つで、$\mu_T(L(H_n),c_\Sigma)=2^n$。しかし $n\ge4$ では
\[
L(H_n)\notin\mathcal C_{2,c_\Sigma}.
\]
実際、$L(H_n)$ はどの半束型付けについても二穴代入可能でない。

**証明。** すべての右辺テンプレートは $\lambda$-free、非削除、非置換、非結合である。$A_i$ は開始記号から単項規則で到達でき、$B_i$ はその一段上の $A_{i+1}\to A_iB_i$ を使えば到達できる。すべての非終端記号は終端語を生成するので reduced である。非終端記号・規則の数と各テンプレートのサイズは $O(n)$ である。

各 $A_i,B_i$ には、そこから全段で短縮枝を選んで長さ $i+1$ の導出語がある。任意の指定規則を使う成功導出は、開始記号からその規則までを単項規則で下降し（$B$ 系へ入るには一度だけ二分岐を用い、その兄弟は長さ $O(n)$ の短い導出にする）、指定規則の下の子もすべて短い導出にすれば、長さ $O(n)$ の文になる。従って規則厚さ $\bar\theta=O(n)$。

マーカーを含まない導出では、全段で二分岐を選ぶ以外にない。その導出語は $A_n$ で長さ $2^n$、$n\ge1$ なら内容は $T$。他方、短縮枝を一度でも使うと $\{d,e,f\}$ の文字が入るため、内容型 $T$ の語は他にない。最後に $n\ge4$ では $A_n$ が $F$ を因子に持ち、系6により単一内容型繊維が許されない。すべての半束型付けに対しても、(5) は $A_n$ とは異なる**同じ $s$ 型**の語を強制するが、その語はマーカーなしであり、(7) に存在しない。$\square$

**判定の意味。** (ii) と (iii) は達成されるのに、(i) が**反例によって失敗**する。純な長い語が Thue–Morse なので `lem:power-transfer` の前提が壊れていても、別の二穴障害が残る。三文字平方自由語や、別の立方自由形態素へ置換する案はこの反例だけでは排除されないが、少なくとも**二穴再分割で生じる局所書換えが新しい語を要求しないか**を最初に調べるべきである。

## 5. T3：長さスペクトルが薄い部分クラスに対する多項式上界

この節の結果は半束にも一般の有限半群型付けにも成り立ち、代入可能性を使うのは最後の特徴標本の結論だけである。長さスペクトルを
\[
\operatorname{Len}(L)=\{|w|:w\in L\cap\Sigma^+\},\quad k=|\operatorname{Len}(L)|
\]
とする。$k<\infty$ なら、有限アルファベット上で $L\cap\Sigma^+$ は有限集合である。

**定理10（有限長さスペクトルによる普遍短縮）。** $G$ を reduced good、ランク $\le r$、ファンアウト $\le f$ の文法とし、$L(G)=L\cap\Sigma^+$ は非空で、$k=|\operatorname{Len}(L)|<\infty$ とする。$g=\|G\|$, $v=|V|$, $\theta=\bar\theta_G$ とすれば、
\[
\max_{w\in L\cap\Sigma^+}|w|
\ \le\ \theta+k(k-1)v(g+r\theta).
\tag{8}
\]
特に任意の固定型付け $s$ について、
\[
t_{\mathrm{typ}}(G,s)\le \theta+k(k-1)v(g+r\theta).
\tag{9}
\]

**証明。** 各非終端記号 $A$ は、ある成功導出中で少なくとも一度出現する（reduced 性）。その出現箇所の規則を $\rho$ とする。$\rho$ を使う長さ $\le\theta$ の成功導出が規則厚さの定義から存在し、特にその導出の $A$ に対応するタプルの総長は $\le\theta$。従って**すべての $A$ に総長 $\le\theta$ の導出タプルがある**。

任意の $w\in L(G)$ を固定し、それを生成する導出木 $T$ のうちノード数が最少のものを取る。各ノード $z$ の部分木が生成するタプルの総長を $\ell(z)$ とし、$\ell(z)>\theta$ なら **大ノード** と呼ぶ。

**(a) 大ノードの反鎖の幅は $k-1$ 以下。** 互いに祖先関係にない $m$ 個の大ノードを選ぶ。各ノードを、同じ非終端記号から導出される総長 $\le\theta$ のタプルに差し替えると、各差替えで根の文長は**正の整数だけ**減少する。これは文法が非削除であり、各成分が最終文にちょうど一度使われるからである。選んだノードを一つずつ順に差し替えれば、$L$ に属する相異なる長さの語を $m+1$ 個作れる。従って $m+1\le k$。

**(b) 任意の根から葉へのパスは $kv$ ノード以下。** 同じ非終端記号 $A$ が一つのパス上で $k+1$ 回現れたと仮定する。これらの出現の部分木の総長は祖先から子孫へ非増加である。もし隣り合う二つの $A$ 出現で総長が等しければ、その間の各規則には余分な終端文字も、パス外の正の長さを持つ兄弟部分木も存在しない。各規則は単項・定数なしとなる。good なテンプレートでは、この場合、非結合性により一つの出力成分に同じ子の二成分を入れられず、$\lambda$-free 性と非削除性により出力成分数は子の成分数と等しく、非置換性により写像は各成分の恒等写像となる。従って二つの $A$ 出現の間の導出鎖を取り除いても**まったく同じタプル、従って同じ語 $w$** が生成され、$T$ のノード数最少性に反する。ゆえにこれら $A$ 出現の総長は厳密に減少する。祖先側の $A$ 部分木を、これら $k+1$ 箇所の $A$ の部分木で順次置き換えると、$L$ に属する $k+1$ 種類の長さの語を得て矛盾する。よって各 $A$ のパス上の出現数は $k$ 以下であり、パス長は高々 $kv$。

**(c) 大ノード数と文長。** 大ノードの集合は祖先について閉じている（非削除性）。同じ深さの大ノードは反鎖なので (a) により高々 $k-1$ 個であり、(b) により深さは高々 $kv$。従って大ノード数 $N$ は $N\le k(k-1)v$。根が大ノードでなければ $|w|\le\theta$。根が大ノードなら、導出木を大ノードのところまで展開し、それらの規則の終端部分と、その直下にある大ノードでない子の導出語を数える。大ノード一つの規則に現れる終端文字数は高々 $g$、子は高々 $r$ 個で、非大ノードの子が出すタプル総長は高々 $\theta$。よって $|w|\le N(g+r\theta)\le k(k-1)v(g+r\theta)$。両場合をまとめて (8) を得る。

最後に、型付きの各非終端記号は trimmed な生成文中のどこかに実現するので、そのタプル総長はその生成文長以下である。すべての生成文長に (8) が成り立つから、各型の最短タプル長も (8) 以下であり、(9) を得る。$\square$

**系11（固定したスペクトル幅での特徴データ上界）。** 定理10に加えて $L\in\mathcal C_{f,s}$ とする。原稿 `thm:data-from-typed-thickness` と $N_{\mathrm{typ}}(G,s)\le C_{f,r,s}g$ により、$\mathcal B^{\le r}_{f,s}$ および $\mathcal B_{f,s}$ は
\[
\|F\|_+\le C_{f,r,s}g\Bigl(1+2\theta+r[\theta+k(k-1)v(g+r\theta)]\Bigr)
+\mathbf 1_{\{\varepsilon\in L\}}.
\tag{10}
\]
を満たす特徴標本を持つ。特に $k\le k_0$ が**クラス全体に共通の定数**なら、固定 $f,r,s,\Sigma$ の下で $g,\theta$ の多項式上界である。これは内容型付け $c_\Sigma$、従って $\mathbf{SL}$ に対しても成り立つ。

**証明。** (9) を原稿の特徴標本上界 $N_{\mathrm{typ}}(1+2\theta+r\,t_{\mathrm{typ}})$ に代入する。$N_{\mathrm{typ}}\le |S^\sharp|^{fr}g$ は原稿の定数評価であり、$\varepsilon$ がある場合は標本中に一語加える。$\square$

**系12（超多項式稀型には長さの多様性が必要）。** 固定ランクで $g_n,\theta_n=n^{O(1)}$ なのに、ある実現内容型の $\mu_A(L_n,c_\Sigma)\ge2^{\Omega(n)}$ となる**有限**言語族が存在するなら、$|\operatorname{Len}(L_n)|=2^{\Omega(n)}$ でなければならない。

**証明。** $M_n:=\max\{|w|:w\in L_n\}\ge\mu_A(L_n,c_\Sigma)$ とし、$k_n=|\operatorname{Len}(L_n)|$ とする。(8) と $v_n\le g_n$ から
\[
M_n\le\theta_n+k_n^2g_n(g_n+r\theta_n).
\]
右辺の $k_n$ 以外は $n^{O(1)}$ なので、指数的な左辺を満たすには $k_n=2^{\Omega(n)}$ を要する。$\square$

**探索への意味。** 固定アルファベットでは内容型は高々 $2^{|\Sigma|}-1$ 個だから、系12の仮定のもとでは、少なくとも一つの内容型に**指数個の異なる長さ**が必要になる。これは原稿で既知の一つの加法量の値に各型が固定される部分クラスの上界とも整合するが、それらの証明を流用してはいない。逆に、長さの種類が指数個あることは下界族が代入可能になるための十分条件ではない。

---

## 6. 判定・次に狙うべき方向・文献照合

**T0 の結論は肯定。** 半束に対しては内容型付けへの帰着が完全に成立する。とくに $(f,s)$ の**標準的な集合駆動再構成作用素**については、細かい型の短い標本を粗い型へ持ち込めるため、上界の帰着にも穴はない。これは任意の集合駆動作用素相互の一般的比較を意味しない。

**T1 の結論は未達だが、自然な第一案には厳密な障害を得た。** Thue–Morse 背骨を一意な無印語にする設計は系6で失敗する。また、無印語の一意性を諦めても、全語立方自由という条件と二穴代入可能性は定理7で両立しない。ここで二穴移送は**冪の連続反復ではなく、同一語の異なる切断位置**に由来する。

**残る余地。** $u^5$ だけを避けることと、多数の長い無印語を許しつつその型の最短長を指数的に保つことは、今回の局所反例では排除されない。三文字平方自由背骨に移る際は、(a) 背骨の短い因子に対する再分割移送の強制先が平方・立方を持つか、(b) 強制先が稀な型の中に留まり、短い代表を生じないか、(c) その強制先を追加した言語が小さい good 文法を持てるか、の順で検査するのが合理的である。なお $\bar\theta=\mathrm{poly}(n)$ で指数稀型を目指す有限言語族には、系12による指数的長さスペクトルという別の必要条件もある。

**T3 の部分的な肯定結果。** $|\operatorname{Len}(L)|\le k_0$ のクラスでは、半束のみならず任意の固定有限半群型付けで多項式特徴データが成立する。しかしこれは $\mathbf{SL}$ **全体**の多項式性を証明したのではなく、ファンアウトによる境界移動の証明でもない。

**下界とアルファベットの注意。** 本報告の明示反例は $\Sigma\supseteq\{a,b\}$（候補文法では固定五文字）に対して成り立つ。定理7の強制書換えは任意の半束型付けに有効であり、特定の $\mathcal B$ の実装に依存しない。一方、特徴データ長の下界を実際に与える超多項式の**有効な** $(2,c_\Sigma)$-代入可能族は今回構成できていない。従って $\mathcal B$ に対する超多項式下界も、クラス全体で特徴標本を持つ任意の集合駆動作用素に対するその種の下界も、**未証明**である。

**先行研究との関係。** 有限半束の $U_1$ による生成、内容準同型の普遍性は標準的な半群論である。Thue–Morse 語の overlap-free 性は Thue に遡る古典的結果であり、例えば Allouche–Shallit の *Combinatorics on Words*、Brown–Rampersad–Shallit–Vasiga (2006) で扱われる。二穴の distribution による代入可能性の一般論は Yoshinaka (2011) にある。本報告の **(4)・(6) の具体的局所強制書換え**、**定理10の厚さ付き長さスペクトル評価**が同一の形で既知かは、今回の確認範囲では**未確認**。外部照合なしで「世界初」「新定理として公刊可能」とは主張しない。

参考入口：
- [対象 `main.tex`](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/main.tex) と [前回報告](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/archive-v1/revision/chatgpt_ternary_u1_fanout2_2026-10-30.md)。
- R. Yoshinaka, *Efficient learning of multiple context-free languages with multidimensional substitutability from positive data*, Theoretical Computer Science **412** (2011), 1821–1831, [doi:10.1016/j.tcs.2010.12.058](https://doi.org/10.1016/j.tcs.2010.12.058)。
- S. Brown, N. Rampersad, J. Shallit, T. Vasiga, *Squares and overlaps in the Thue-Morse sequence and some variants*, RAIRO-ITA **40** (2006), 473–484, [doi:10.1051/ita:2006030](https://doi.org/10.1051/ita:2006030)。
- Almeida–Margolis–Steinberg–Volkov (2009), *Representation Theory of Finite Semigroups, Semigroup Radicals and Formal Language Theory*, TAMS **361**, 1429–1461。半群の局所群判定は原稿 `thm:lg-characterization` の対応を基準にした。

## 7. 小規模計算の再現用スクリプト（Python 3 標準ライブラリのみ）

§3 の二つの具体的証明は表示した文字列の連結を直接検算でき、**計算結果に依存して真となる主張ではない**。反例を発見し文字列を照合するため、長さ16に限った次の小さな列挙を使用した。長さ $2^n$ の一般族の全数探索は行っていない。定理10の証明には計算を使っていない。

```python
from itertools import combinations
from collections import defaultdict


def thue(n):
    a, b = 'a', 'b'
    for _ in range(n):
        a, b = a + b, b + a
    return a


def fill(E, x):
    return E[0] + x[0] + E[1] + x[1] + E[2]


def cube(w):
    for k in range(1, len(w) // 3 + 1):
        for i in range(len(w) - 3 * k + 1):
            if w[i:i+k] * 3 == w[i:i+3*k]:
                return (i, w[i:i+3*k])
    return None


F = thue(4)
assert F == 'abbabaabbaababba'

# §3.1: singleton-fiber obstruction.
x = ('abba', 'aab')
y = ('ab', 'abaab')
E0 = ('', 'b', 'baababba')
E1 = ('', 'baabb', 'abba')
assert tuple(map(frozenset, x)) == tuple(map(frozenset, y))
assert fill(E0, x) == fill(E0, y) == fill(E1, x) == F
assert fill(E1, y) == 'abbaabbabaababba' != F

# §3.2: cubefree obstruction.
u = ('abbabaa', 'ba')
v = ('ab', 'abaabba')
D0 = ('', 'b', 'ababba')
D1 = ('', 'bbaa', 'bba')
assert tuple(map(frozenset, u)) == tuple(map(frozenset, v))
assert fill(D0, u) == fill(D0, v) == fill(D1, u) == F
assert fill(D1, v) == 'abbbaaabaabbabba'
assert cube(F) is None
assert cube(fill(D1, v)) == (1, 'bbb')

# Independent bounded enumeration of all two-hole cuts of F:
# i < j < k < l guarantees two nonempty components and
# a nonempty separator. This is not a large-scale search.
D = defaultdict(set)
by_context = defaultdict(list)
for i, j, k, l in combinations(range(len(F) + 1), 4):
    z = (F[i:j], F[k:l])
    E = (F[:i], F[j:k], F[l:])
    D[z].add(E)
    by_context[E].append(z)

found = False
for E, tuples in by_context.items():
    for z in tuples:
        for z2 in tuples:
            if tuple(map(frozenset, z)) != tuple(map(frozenset, z2)):
                continue
            for H in D[z]:
                w = fill(H, z2)
                if w != F and cube(w) is not None:
                    found = True
                    break
            if found:
                break
        if found:
            break
    if found:
        break
assert found
print('verified:', F, '=>', fill(D1, v), 'cube:', cube(fill(D1, v)))
```

**最終判定：** T0 は完成した帰着定理になる。T1 は Thue–Morse 第一案に対して、冪の移行とは独立の厳密な二穴障害を示して否定した。T3 では有限長さスペクトルという新たな十分条件と、その対偶として指数下界族に必要な長さの多様性を得た。**$\mathbf{SL}$ / fan-out 2 の一般境界は未解決のままである。**

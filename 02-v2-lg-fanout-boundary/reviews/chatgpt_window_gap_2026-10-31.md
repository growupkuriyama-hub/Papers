# 窓型付けにおける特徴データ長のギャップ：閉じ記号を一つ除いた倍増族の解析

**調査日：2026年10月31日**  
**対象原稿：** Takayuki Kuriyama, *Distributional Learning of Multiple Context-Free Languages under Fixed Finite-Semigroup Typing: Local Groups and the Length of Characteristic Data*, `02-v2-lg-fanout-boundary/main.tex`（調査時の Git blob `d03710d94d0274df05b7b49e53e85b218e65d599`）。  
**成果の区分：** 以下の「証明済み」は本報告に証明を記載した主張であり、査読済み・文献上新規という意味ではない。

## 結論の要約表

| 主張 | 判定 | 根拠の節 |
|---|---|---|
| すべての $n\ge1$ で $F_n=L(E_n)$ は Clark–Eyraud 代入可能であり、任意の有限半群型付け $s$ に対し $F_n\in\mathcal C_{1,s}$ | **証明済み** | §2–§4 |
| 元の括弧付き倍増族の「異なる閉じ括弧により分岐の途中で合流しない」という補題が、今回の解析器にもそのまま適用できる | **反証済み（補題の移植に反例あり）** | §3.2 |
| $|F_n|=q_n$, $q_0=1$, $q_i=q_{i-1}^2+q_{i-1}$、$\|G_n\|=12n+3$、$\bar\theta_{G_n}=4n-1$ | **証明済み** | §5 |
| $s_{0,1}$ の末尾 $a$ の最短語長 $\mu_a=n(n+1)+1$、末尾 $r$ の最短語長 $\mu_r=2n+1$ | **証明済み** | §5.2 |
| $s_{1,1}$ の実現型ごとの最短語長、および両窓型付けで $\tau(G_n,s)=t_{\mathrm{typ}}(G_n,s)=\mu^*(F_n,s)=n(n+1)+1$ | **証明済み** | §5.3–§5.4 |
| $s_{0,1}$ に対し、具体的に構成した標本 $K_n$ が $\mathcal B_{1,s}$ とランク2制限版の特徴標本で、$\|K_n\|_+=O(n^3)$ | **証明済み** | §6.1–§6.3 |
| $s_{1,1}$ に対しても具体的な有限手続きで特徴標本を構成でき、総長 $O(n^3)$ | **証明済み** | §6.4 |
| $s_{0,1}$ の任意の特徴標本は $\|F\|_+\ge n^2+3n+4$（対象作用素の限定あり） | **証明済み** | §7 |
| $s_{1,1}$ の任意の特徴標本は $\|F\|_+\ge n^2+7n+4$（$n\ge2$、作用素の限定あり） | **証明済み** | §7 |
| $F_n$ の最短特徴標本長は $\Theta(n^2)$ または $\Theta(n^3)$ のいずれかに確定できる | **未解決** | §8 |
| 任意の固定窓型付けと固定ファンアウトに対する一般上界 $O(\|G\|\bar\theta_G)$ | **未解決** | §9 |
| 上の一般線形積上界が可換群・任意の局所群に拡張する | **未解決** | §9 |
| $n\le4$ の全数検査、および $n\le5$ の有限解析器についての別形式の全状態検査 | **計算による観測（証明ではない）** | §10 |

## 1. 設定、記号、射程

$\Sigma=\{a,l,c,r\}$ とし、$n\ge1$ に対して
\[
 E_0\longrightarrow a,\qquad
 E_i\longrightarrow lE_{i-1}E_{i-1}\mid cE_{i-1}r
 \quad(1\le i\le n),
\]
を持ち、$E_n$ を開始記号とする文法を $G_n$、生成言語を $F_n$ と書く。$L_i=L(E_i)$ とおく。

非空語 $x$ の分布を
\[
 D_{F_n}(x)=\{(p,q)\in\Sigma^*\times\Sigma^*:pxq\in F_n\}
\]
とする。Clark–Eyraud の条件は、非空 $x,y$ について
\[
 D_{F_n}(x)\cap D_{F_n}(y)\ne\varnothing
 \quad\Longrightarrow\quad D_{F_n}(x)=D_{F_n}(y)
\tag{1}
\]
である。式 (1) は「特定の導出の非終端に整列した語」だけでなく、**あらゆる非空部分語**について証明する必要がある。

$\mathcal B_{1,s}(K)$ については、原稿の `def:reconstruction` の Const/Comp/Link/Start 規則を使う。$\|F\|_+=\sum_{w\in F}(|w|+1)$ であり、特徴標本は $F\subseteq K\subseteq F_n$ となるすべての有限 $K$ に対し正確な再構成を保証する有限集合である。

本報告では **(i)** $F_n$ 自身の代入可能性、**(ii)** この特定の提示 $G_n$ に対する尺度、**(iii)** 正確に指定した再構成作用素についての特徴データを区別する。集合駆動作用素一般への下界は、その作用素が対応するクラス全体に特徴標本を持つと仮定した場合に限る。

## 2. 修正した決定的スタック解析器

スタックの頂上を左端に記し、記号集合を
\[
 \{E_0,E_1,\ldots,E_n,R\}
\]
とする。$R$ は入力文字 $r$ の待機記号で、非終端ではない。任意の残余スタック $\psi$ に対し、許す遷移は以下のみとする。
\[
 \begin{aligned}
 E_0\psi&\xrightarrow{a}\psi,\\
 E_i\psi&\xrightarrow{c}E_{i-1}R\psi &(1\le i\le n),\\
 E_i\psi&\xrightarrow{l}E_{i-1}E_{i-1}\psi &(1\le i\le n),\\
 R\psi&\xrightarrow{r}\psi.
 \end{aligned}
\tag{2}
\]
空スタックからの遷移はない。$\sigma\xrightarrow{w}\eta$ は $w$ を順に読んだ遷移を意味する。

**補題 2.1（解析と言語の一致）。** $E_i\xrightarrow{w}\varepsilon$ と $w\in L_i$ は同値である。より一般に、
\[
 E_i\psi\xrightarrow{w}\psi\qquad(w\in L_i).
\tag{3}
\]

**証明。** $i=0$ では唯一の遷移は $a$ を読むものだから主張が成り立つ。$i\ge1$ とし、最初の文字が $c$ であれば $E_{i-1}R$ が積まれる。これを空にするためには、まず $E_{i-1}$ が一語 $u\in L_{i-1}$ を読み終え、次に $R$ が $r$ を読むしかない。したがってこの場合の語はちょうど $cur$ である。最初の文字が $l$ であれば $E_{i-1}E_{i-1}$ が積まれるので、帰納法から、語はちょうど $luv$（$u,v\in L_{i-1}$）である。いずれの場合も後続の $\psi$ を変更せず実行できるため、(3) が従う。□

**補題 2.2（文字ごとの決定性・単射性）。** 各文字 $b\in\Sigma$ の遷移はスタック全体の集合上で部分単射である。したがって任意の語 $w$ による遷移も部分単射である。

**証明。** $a$ の場合、終状態 $\psi$ と読んだ文字 $a$ から始状態 $E_0\psi$ が一意に復元できる。$r$ の場合も始状態は $R\psi$ と一意に復元できる。$c$ の場合、終状態の先頭は $E_{i-1}R$ であり、ここから $i$ と残余 $\psi$ を一意に復元できる。$l$ の場合、終状態の先頭は $E_{i-1}E_{i-1}$ であり、同じく復元できる。各文字の遷移が決定的で単射であるから、有限個の合成も決定的な部分単射である。□

**補題 2.3（完全な $E_i$ 語の交換）。** $u,v\in L_i$ ならば、任意の $p,q\in\Sigma^*$ に対し
\[
 puq\in F_n\quad\Longleftrightarrow\quad pvq\in F_n.
\tag{4}
\]

**証明。** $puq\in F_n$ の解析を
\[
 E_n\xrightarrow{p}\sigma\xrightarrow{u}\eta
 \xrightarrow{q}\varepsilon
\]
と分ける。補題 2.1 により $E_i\eta\xrightarrow{u}\eta$ である。補題 2.2 による $u$-遷移の単射性から $\sigma=E_i\eta$ が従う。補題 2.1 を $v$ に適用すれば $E_i\eta\xrightarrow{v}\eta$ であり、$pvq$ も受理される。$u,v$ を交換すれば逆向きも成立する。□

## 3. 旧「分岐同期」証明の破綻点と、それを補う不変量

### 3.1 長さを減らす重み

$\operatorname{wt}(E_i)=4^i$、$\operatorname{wt}(R)=1$ とし、スタックの重みを各記号の重みの和とする。式 (2) の全遷移は重みを**厳密に減らす**。特に $i\ge1$ で $4^i>2\cdot4^{i-1}$ かつ $4^i>4^{i-1}+1$ である。このため、非空入力を読んで同じスタックに戻ることはできない。

### 3.2 旧補題をそのまま使えないことの明示例

括弧付き倍増族の TCS R1 原稿 Appendix C の branch synchronization では、異なる最初の開き括弧を読んだ二つの解析の「まだ外側スタックに戻らない」場合を、異なる閉じ記号によって排除する。ところが今回の文法では次の二つの遷移が存在する。
\[
 E_2\psi\xrightarrow{\;ccar\;}R\psi,
 \qquad
 E_2\psi\xrightarrow{\;lcarca\;}R\psi.
\tag{5}
\]
第一は $E_2\to cE_1r$ の内部 $E_1\to car$ を読み終えた段階であり、第二は $E_2\to lE_1E_1$ の第一子 $car$ を読み終え、第二子 $E_1\to car$ の $ca$ を読んだ段階である。**両解析とも外側の $\psi$ に達する前に同じスタック $R\psi$ へ合流する。**

したがって旧証明の case (b) 排除は偽である。ただし (5) は $F_n$ の代入可能性の反例ではない。以下では case (b) を排除せず、そこで二つの語が**同一のスタック変換を実行する**ことを示す。

### 3.3 最初の $a$ を検出するスタック不変量

スタック $\zeta=Z_1\cdots Z_m$ に対し
\[
 H(\zeta):=\max\{j+(m-t):Z_t=E_j,\ 1\le t\le m\},
\quad\max\varnothing:=-\infty.
\tag{6}
\]
すなわち、非終端 $E_j$ の指数 $j$ と、その記号の**右側にあるスタック記号の個数**の和の最大値である。これは $R$ を区別するために水準付き記号を追加する必要がない不変量である。

**補題 3.1。** $E_i$ を初期スタックとする解析では、

1. 最初の入力 $a$ より前には $c,l$ しか読めず、$H=i$ である。また $H$ の最大値は先頭の非終端だけで達成される。
2. 一度でも $a$ を読むと、その後 $H<i$ が保たれる（解析が途中で停止する場合も含む）。
3. 最初の $a$ が現れる位置は、$E_i$ から開始した場合、先頭から **$i+1$ 番目**である。

**証明。** 初期状態は $E_i$ 一個で、$H=i$、最大値の達成者は先頭だけである。先頭 $E_j$ の右側に $b$ 個の記号があるとする。$c$ または $l$ を読むと、この $E_j$ は先頭 $E_{j-1}$ と、$R$ または第二の $E_{j-1}$ に置き換わる。新しい先頭の (6) の値は $(j-1)+(b+1)=j+b$、第二の非終端が存在する場合の値は $(j-1)+b=j+b-1$ である。後続に存在した非終端の右側記号数は変わらない。ゆえに $c,l$ の遷移は $H$ を変えず、先頭だけが最大であるという性質を保存する。先頭が $E_0$ に到達するまで $a$ は読めない。また、最初の $a$ の前に $r$ を読めることもない（先頭には常に非終端がある）。指数は $c,l$ を読むたびにちょうど一つ下がるため、$i$ 個の $c,l$ に続いて最初の $a$ が現れる。

その $a$ は先頭 $E_0$ を削除し、唯一の最大値達成者が消える。残存非終端の (6) の値は変化しないため $H<i$ になる。以後、$c,l$ は上述の計算から $H$ を増加させない。$a,r$ による先頭の削除は、残存非終端の右側記号数を変更しないため $H$ を増加させない。したがって最後まで $H<i$ である。□

**補題 3.2（未完了分岐の同期）。** $i\ge1$ とし、$E_i\psi$ から異なる先頭文字を持つ非空語 $x,y$ を読んで、同じ $\eta\psi$（$\eta\ne\varepsilon$）に到達するとする。二つの解析がいずれも途中で $\psi$ に達していなければ、$x$ と $y$ は、どの初期スタック上でも**同じ部分変換**を実行する。すなわち任意の $\xi$ について、$\xi\xrightarrow{x}\zeta$ が定義されることと $\xi\xrightarrow{y}\zeta$ が定義されることは同値である。

**証明。** 同じ初期スタックから異なる先頭文字が許されるのは、先頭が $E_i$（$i\ge1$）で、一方が $c$、他方が $l$ の場合だけである。両方とも $a$ を含まないと仮定する。すると両語は $c,l$ のみから成る。長さ $t$ のこのような語を $E_i$ から読むと、$t\le i$ で、結果は
\[
 E_{i-t}B_tB_{t-1}\cdots B_1,
\qquad B_j=\begin{cases}
 R,&\text{$j$ 番目の入力が $c$},\\
 E_{i-j},&\text{$j$ 番目の入力が $l$}
\end{cases}
\tag{7}
\]
である。結果の先頭指数から $t$ が分かり、$B_1,\dots,B_t$ から元の文字列が分かる。よって同じ結果なら $x=y$ となり、先頭文字が異なることに反する。

一方が $a$ を含み他方が含まないなら、補題 3.1 の $H$ の値がそれぞれ $i$ 未満と $i$ になって結果 $\eta$ が一致しない。したがって **両方とも $a$ を含む**。

次に $x$ が任意のスタック $\xi$ から実行可能とする。$x$ は $c$ または $l$ で始まるので、$\xi$ の先頭は $E_j$（$j\ge1$）でなければならない。補題 3.1(3) より、$x$ の最初の $a$ の位置は $j+1$ である。しかし元の $E_i\psi$ からの解析でも位置は $i+1$ だから $j=i$ である。したがって $\xi=E_i\chi$ と書ける。元の二つの実行は $\psi$ に触れないため、同じ遷移列を $E_i\chi$ 上でも実行でき、それぞれ $\eta\chi$ に至る。$y$ から始めた場合も同じ議論が成り立つ。ほかの先頭記号では両方とも実行不能なので、二つの部分変換は完全に一致する。□

## 4. 全 $n$ に対する Clark–Eyraud 代入可能性の証明

**定理 4.1。** すべての $n\ge1$ について $F_n$ は Clark–Eyraud 代入可能である。したがって、任意の全射有限半群型付け $s:\Sigma^+\twoheadrightarrow S$ に対し $F_n\in\mathcal C_{1,s}$ である。

**証明。** 最初に次のより強い主張を証明する。

> 任意のスタック $\sigma,\theta$ と任意の語 $x,y\in\Sigma^*$ について、$\sigma\xrightarrow{x}\theta$ かつ $\sigma\xrightarrow{y}\theta$ ならば、$x\equiv_{F_n}y$、すなわち任意の $p,q\in\Sigma^*$ について $pxq\in F_n\iff pyq\in F_n$ である。

$|x|+|y|$ に関する強い帰納法を用いる。片方が空語であれば、重みがすべての非空遷移で厳密に減ることからもう一方も空語となり、主張は自明である。

両方が非空で、先頭文字が同じ $b$ なら $x=bx'$, $y=by'$ と書ける。解析は決定的なので共通する第一遷移 $\sigma\xrightarrow{b}\sigma'$ があり、$\sigma'\xrightarrow{x'}\theta$ と $\sigma'\xrightarrow{y'}\theta$ である。帰納法より $x'\equiv_{F_n}y'$。構文的合同関係 $\equiv_{F_n}$ は左右の文字列の連接に閉じているから、$bx'\equiv_{F_n}by'$ である。

先頭文字が異なるとき、遷移 (2) により $\sigma=E_i\psi$（$i\ge1$）で、一方は $c$、他方は $l$ で始まる。$E_i\psi$ からの両実行において、最終状態 $\theta$ は同じである。外側スタック $\psi$ に初めて達するか否かで二つの場合を区別する。

**場合 A：$\psi$ に達する。** 実行が一度 $\psi$ に達すると、以後は $\psi$ から始まる実行であるため、$\operatorname{wt}(\theta)\le\operatorname{wt}(\psi)$ となる。二つの実行ともこの場合に属し、最初に $\psi$ に達する場所で
\[
 x=ux',\quad y=vy',\qquad
 u,v\in L_i,\qquad
 \psi\xrightarrow{x'}\theta,
 \quad\psi\xrightarrow{y'}\theta
\]
と分割できる。$u,v$ は $E_i$ を空にする完全語なので、補題 2.1 から $L_i$ に属する。$u,v$ は非空であるから、帰納法を短い組 $x',y'$ に適用して $x'\equiv_{F_n}y'$ を得る。一方、補題 2.3 で $u\equiv_{F_n}v$ が成り立つ。よって合同性から $ux'\equiv_{F_n}vy'$ である。

**場合 B：$\psi$ にまだ達しない。** この場合、最終状態は非空 $\eta$ を用いて $\theta=\eta\psi$ と書けるため、$\operatorname{wt}(\theta)>\operatorname{wt}(\psi)$ である。重みの大小が場合 A と排他的なので、片方のみ場合 A となることはない。両方が場合 B のとき、補題 3.2 により $x,y$ は任意のスタック上で同じ部分変換を行う。従って任意の $p,q$ に対し、$pxq$ が受理されれば $p$ の読後のスタックから $y$ でも同じ状態に至り、同じ $q$ を読んで受理される。逆向きも同じだから $x\equiv_{F_n}y$ である。

以上ですべてのケースが尽くされ、強い主張が示された。

ここで $x,y\in\Sigma^+$ が共通文脈を持ち、$pxq,pyq\in F_n$ とする。決定性により $p$ の後のスタック $\sigma$ は共通である。$x,y$ を読んだ後のスタックをそれぞれ $\theta_x,\theta_y$ とすると、両者から同じ $q$ を読んで空スタックに至る。補題 2.2 による $q$-遷移の単射性から $\theta_x=\theta_y$ となる。前段の強い主張から $x\equiv_{F_n}y$ が得られ、これが式 (1) である。

最後に、$s(x)=s(y)$ という条件を追加すれば比較する組が減るだけなので、任意の型付けに対する $(1,s)$-代入可能性も成立する。$G_n$ は CFG だから $F_n\in\mathcal C_{1,s}$ である。□

**証明の要点。** Appendix C の「場合 B は不可能」を捨て、代わりに (6) の不変量により **場合 B では二つの語が同じ部分スタック変換を行う**ことを証明した。式 (5) のような途中合流を許容する点が旧証明との差分である。

## 5. 正確なサイズ・厚さ・最短語長

### 5.1 $\|G_n\|$、$\bar\theta_{G_n}$ と語数

原稿が定義する記号単位のサイズは
\[
 \|G\|=|V|+\sum_{A\to\rho(B_1,\ldots,B_t)}
 (1+t+|\alpha|)
\tag{8}
\]
である。$G_n$ は $n+1$ 個の非終端、$E_0\to a$ による寄与 $2$、各 $i\ge1$ の二分岐規則の寄与 $6$、一分岐規則の寄与 $5$ を持つ。したがって
\[
 \boxed{\|G_n\|=(n+1)+2+11n=12n+3.}
\tag{9}
\]
各規則は $\lambda$-free・非削除・非置換・非併合であり、すべての非終端が到達可能・生成可能だから、$G_n$ は reduced good、ファンアウト1、ランク2である。

$L_i$ の最短語長を $m_i$ とすると $m_0=1$、$m_i=\min\{1+2m_{i-1},2+m_{i-1}\}=2i+1$（$i\ge1$）である。最短語は一意で
\[
 C_i:=c^i a r^i,\qquad |C_i|=2i+1.
\tag{10}
\]
規則 $E_i\to lE_{i-1}E_{i-1}$ を用いる最短の $E_n$ 語は、上位 $n-i$ 段を $c$ 分岐でたどればよく、長さは
\[
 2(n-i)+1+2(2i-1)=2n+2i-1.
\tag{11}
\]
上位を $l$ 分岐にすると、同じ深さでの最短の兄弟部分木長 $2j-1$ と $l$ 一文字を余分に必要とし、$c$ 分岐の追加長2より短くならない。従って (11) は最短である。一分岐規則 $E_i\to cE_{i-1}r$、および $E_0\to a$ を使う最短の $E_n$ 語長は、ともに $2n+1$ である。式 (11) の最大値は $i=n$ で達成されるため
\[
 \boxed{\bar\theta_{G_n}=\max\{2n+1,4n-1\}=4n-1\quad(n\ge1).}
\tag{12}
\]
最後の等号は $n=1$ でも成立する。

先頭の $l,c$ が異なり、各分岐の境界は補題 2.1 の決定的解析で区別できるので、語の重複はない。$q_i:=|L_i|$ とおくと
\[
 \boxed{q_0=1,\qquad q_i=q_{i-1}^2+q_{i-1}.}
\tag{13}
\]
特に $q_1=2,q_2=6,q_3=42,q_4=1806$ である。最長語長は $M_0=1$、$M_i=1+2M_{i-1}$ だから $M_i=2^{i+1}-1$ である。

### 5.2 $s_{0,1}$ の語長：二次の「稀な型」

$U_0=a$ とし
\[
 U_i:=lC_{i-1}U_{i-1}\quad(i\ge1).
\tag{14}
\]
$U_i$ は末尾 $a$ の語である。$i\ge1$ で末尾が $a$ になるには、最上位規則は必ず $l$ 分岐で、その**右子**も末尾 $a$ でなければならない。左子は任意の $L_{i-1}$ 語でよいが最短は $C_{i-1}$ である。従って末尾 $a$ の最短長 $A_i$ は
\[
 A_0=1,\qquad A_i=1+(2i-1)+A_{i-1}=2i+A_{i-1}.
\]
これを足し上げると
\[
 \boxed{\mu_a(F_n)=A_n=n(n+1)+1.}
\tag{15}
\]
式 (14) が実際にこの長さを達成する。末尾 $r$ で終わる最短の語は $C_n$ であり、
\[
 \boxed{\mu_r(F_n)=2n+1.}
\tag{16}
\]
末尾型として実現されるのは $a,r$ のみなので、$\mu^*(F_n,s_{0,1})=n(n+1)+1$ である。

### 5.3 $s_{1,1}$ の実現型

$L_n$ の語長は $n\ge1$ で3以上だから、$s_{1,1}$ は $L_n$ 上では最初と最後の文字の対で表される。$n\ge2$ の実現型は
\[
 (c,r),\qquad(l,a),\qquad(l,r)
\]
のみであり、それぞれの最短長は
\[
 \boxed{\begin{aligned}
 \mu_{(c,r)}&=2n+1,\\
 \mu_{(l,a)}&=n(n+1)+1,\\
 \mu_{(l,r)}&=4n-1.
 \end{aligned}}
\tag{17}
\]
最初は $C_n$、第二は $U_n$、第三は $lC_{n-1}C_{n-1}$ によって達成される。第三の最短性は、最上位が $l$ であるとき両子の最短長が $2n-1$ であることから従う。$n=1$ では $(l,r)$ が実現されず、$(c,r)$ と $(l,a)$ はともに長さ3である。

### 5.4 代表長 $\tau$ も正確に二次である

原稿の $t_{\mathrm{typ}}(G_n,s)$ は、実現される型付き非終端 $E_i^t$ の最短生成語長の最大値である。$s_{0,1}$ では (15)–(16)、$s_{1,1}$ では (17) を各 $i$ に適用する。$i\ge2$ に対して
\[
 i(i+1)+1-(4i-1)=(i-1)(i-2)\ge0
\]
なので、どちらの型付けでも最大値は開始非終端 $E_n$ の末尾 $a$／型 $(l,a)$ で達成される。従って
\[
 t_{\mathrm{typ}}(G_n,s_{0,1})
 =t_{\mathrm{typ}}(G_n,s_{1,1})=n(n+1)+1.
\tag{18}
\]
原稿の `cor:distribution-representatives` にある
$\mu^*(F_n,s)\le\tau(G_n,s)\le t_{\mathrm{typ}}(G_n,s)$ と (15)–(18) を合わせると、
\[
 \boxed{\tau(G_n,s)=t_{\mathrm{typ}}(G_n,s)=\mu^*(F_n,s)
 =n(n+1)+1}
\quad(s=s_{0,1},s_{1,1}).
\tag{19}
\]
従って「$\tau=O(\bar\theta)$ を直接証明する」という方針は、この二つの**窓型付け**に対してすでに偽である。一般データ長の $O(\|G\|\bar\theta)$ まで否定されたわけではない。

## 6. 具体的な特徴標本：両窓型付けで $O(n^3)$

### 6.1 $s_{0,1}$ 用の標本

$A$ を末尾 $a$、$R$ を末尾 $r$ の型の記号として使い、代表語を
\[
 u_i^A:=U_i,\quad u_i^R:=C_i\ (i\ge1),\qquad u_0^A:=a
\tag{20}
\]
とする。型集合を $T_0=\{A\}$、$T_i=\{A,R\}$（$i\ge1$）とする。語 $z\in L_i$ を開始 $E_n$ まで最短の一分岐鎖で埋め込む演算を
\[
 P_i(z):=c^{n-i}zr^{n-i}
\tag{21}
\]
と置く。以下の**集合** $K_n$ を定義する。重複した語は一回だけ採用する。

- **非終端代表：** すべての $0\le i\le n$、$t\in T_i$ に対し $P_i(u_i^t)$ を入れる。
- **一分岐規則：** すべての $1\le i\le n$、$t\in T_{i-1}$ に対し $P_i(cu_{i-1}^t r)$ を入れる。
- **二分岐規則：** すべての $1\le i\le n$、$t,v\in T_{i-1}$ に対し $P_i(lu_{i-1}^t u_{i-1}^v)$ を入れる。

これらはすべて $F_n$ の語である。$n=1$ では重複を除くと $K_1=\{laa,car\}=F_1$ である。

### 6.2 $K_n$ が確実に再構成することの直接証明

**命題 6.1。** $K_n$ は $\mathcal B_{1,s_{0,1}}$ と $\mathcal B_{1,s_{0,1}}^{\le2}$ の特徴標本である。

**証明。** $K_n\subseteq K\subseteq F_n$ を任意の有限集合とする。以下の推論は $K_n$ の語だけで証拠が成立するから、$K$ が増えても保存される。

まず、$P_i(u_i^t)$ は $K$ の語だから、その中に現れる $u_i^t$ に対応した非終端 $[u_i^t]$ が存在する。$P_i(u_i^t)$ と各規則証拠 $P_i(z)$ は、$z$ が型 $t$ の場合、同じ外側文脈 $c^{n-i}\square r^{n-i}$ にその型の語を入れた $K$ 内の二語である。従って Link 規則
\[
 [u_i^t]\longrightarrow[z]
\tag{22}
\]
が存在する（両方向の Link が作られるが、片方で十分である）。$z=cu_{i-1}^v r$ ならば Comp 規則 $[z]\to c[u_{i-1}^v]r$ が存在する。$z=lu_{i-1}^v u_{i-1}^{v'}$ ならばランク2の Comp 規則
\[
 [z]\longrightarrow l[u_{i-1}^v][u_{i-1}^{v'}]
\tag{23}
\]
が存在する。いずれも $z$ 自体が標本語の連続因子であるから、成分と規則の観測条件が満たされる。

$[u_0^A]\to a$ は Const 規則で生成できる。$i$ に関する帰納法により、各 $t\in T_i$ について $[u_i^t]$ から型 $t$ のすべての $L_i$ 語が生成できる。実際、任意の $w\in L_i$ の最上位規則が $c$ 型なら、対応する (22) の一分岐規則を選び、子語の型 $v$ に帰納法を適用する。最上位規則が $l$ 型なら、右子の型が親の末尾型を決める。左右の子の実際の型に対応する (22)–(23) を選び、両子に帰納法を適用する。これにより $w$ を生成できる。

$P_n(u_n^A)=u_n^A$ と $P_n(u_n^R)=u_n^R$ が $K_n$ に含まれるので、Start は両型の代表非終端を開始できる。以上より $F_n\subseteq L(\mathcal B(K))$ が従う。

逆向きは定理 4.1 を用いる。任意の $K\subseteq F_n$ について、各観測非終端 $[x]$ の生成語 $y$ は $x\equiv_{F_n}y$ を満たすことを導出木の高さに関する帰納法で示す。Const では $y=x$ である。Link では観測された共通文脈と同型条件から $x\equiv_{F_n}z$ となり、子の帰納法と推移性により結論を得る。Comp では各子の生成語が観測子と合同であり、合同関係の連接閉性により親の出力も観測親と合同である。Start の観測語 $w$ は $F_n$ に属するので、$[w]$ から得るすべての語も空の外側文脈で $F_n$ に属する。従って $L(\mathcal B(K))\subseteq F_n$ である。

両向きの包含と任意の $K$ に対する保存性から、$K_n$ は両作用素の特徴標本である。□

### 6.3 総符号長の明示上界

$K_n$ の作り方で使う語の個数は、重複を数えても $i=0$ に1個、$i=1$ に4個、$i=2,\ldots,n$ に各8個だから、$n\ge1$ で高々 $8n-3$ 個である。各語の長さは (15) と (21) から高々 $2n^2+2n+3$ と粗く抑えられる。従って
\[
 \boxed{\|K_n\|_+
 \le(8n-3)(2n^2+2n+4)=O(n^3).}
\tag{24}
\]
これは存在定理だけでなく、全ての語を式 (20)–(21) から書き出せる**具体的構成**である。一方、$K_n$ が最短であるという主張はしていない。

### 6.4 $s_{1,1}$ 用の同型の構成

各 $i$ について、$T_i^{(1,1)}$ を $L_i$ の実現型集合（$i=0$ では短語 $a$ の特別な窓型、$i=1$ では $(c,r),(l,a)$、$i\ge2$ では (17) の3型）とし、各型 $t$ の最短語 $u_i^t$ を一つ固定する。具体的には $u_i^{(c,r)}=C_i$、$u_i^{(l,a)}=U_i$、$u_i^{(l,r)}=lC_{i-1}C_{i-1}$ とできる。

(21) と同じ $P_i$ を使い、全ての型付き非終端の $P_i(u_i^t)$、すべての実現可能な型付き $c$ 規則の $P_i(cu_{i-1}^t r)$、すべての実現可能な型付き $l$ 規則の $P_i(lu_{i-1}^t u_{i-1}^{t'})$ を標本に入れる。型の組合せは一段あたり高々 $3^2$ 個、規則総数は $O(n)$、一語の長さは $O(n^2)$ である。実現型が等しい代表と規則出力は同じ $P_i$ 文脈で Link でき、Comp と Start についても §6.2 の証明がそのまま成立する。従ってこの明示的な有限手続きは **$O(n^3)$ の特徴標本**を作る。

## 7. データ長の無条件の二次下界と作用素の範囲

**命題 7.1（$s_{0,1}$）。** 次のいずれかの作用素について、$F_n$ の任意の特徴標本 $F$ は
\[
 \boxed{\|F\|_+\ge(\mu_a+1)+(\mu_r+1)
 =n^2+3n+4.}
\tag{25}
\]
を満たす。

1. 原稿の $\mathcal B_{1,s_{0,1}}$ と任意のランク上限1以上の対応する版。
2. $\mathcal C_{1,s_{0,1}}$ **全体**に特徴標本を持つ集合駆動作用素。

**証明。** 型 $m\in\{a,r\}$ を一つ固定する。$F_n$ から型 $m$ の語だけをすべて削除した言語 $F_n^{\setminus m}$ は有限なので CFG である。また、同型の部分語を同じ外側文脈に挿入した場合、完成語の半群型は等しい。定理 4.1 の代入可能性を使えば、元の $F_n$ で成立するすべての分布等式は、完成語の型を条件として削除した後にも成立する。従って $F_n^{\setminus m}\in\mathcal C_{1,s_{0,1}}$ である。

クラス全体に特徴標本を持つ集合駆動作用素 $A$ を考える。仮に $F_n$ の特徴標本 $F$ が型 $m$ の語を含まないなら、$F\subseteq F_n^{\setminus m}$ である。$F_n^{\setminus m}$ の特徴標本 $F'$ を一つ取ると、$F\cup F'\subseteq F_n^{\setminus m}$ である。集合駆動性および両特徴標本の定義から、同じ入力 $F\cup F'$ に対する出力は $F_n$ と $F_n^{\setminus m}$ の双方に等しくなければならないが、二言語は異なり矛盾する。従って $F$ は各実現型 $m$ の語を少なくとも一つ含み、その長さは $\mu_m$ 以上である。(15)–(16) を足すと (25) である。原稿の二つの $\mathcal B$ は、このクラス全体に特徴標本を持つので同じ結論が適用できる。□

**命題 7.2（$s_{1,1}$）。** 同じ作用素条件の下、$n\ge2$ ならば
\[
 \boxed{\|F\|_+
 \ge(2n+2)+(n^2+n+2)+(4n)
 =n^2+7n+4.}
\tag{26}
\]
$n=1$ では $\|F\|_+\ge8$ である。

**証明。** $F_n$ で実現される型は §5.3 の3型（$n=1$ では2型）である。型一つを削除しても代入可能性が保たれる理由は命題 7.1 と同じである。よって各型について異なる標本語が必要で、その $|w|+1$ を (17) に従って加算すると (26) を得る。□

**注意。** これらはアルファベットがちょうど4文字でも成り立つ。ただし**一般の** $\Omega(\|G\|\bar\theta)$ 標識族に付いた $|\Sigma|\ge4f+1$ という条件を、この証明から撤去できるわけではない。上の下界は具体的な4文字族と指定型付けに限られる。また、ある一つの対象についてのみ特徴標本の存在を要求する任意の集合駆動作用素には、命題 7.1–7.2 を適用していない。

## 8. Q2 の現状：二次と三次の間に厳密なギャップが残る

$\operatorname{cs}_{\mathcal B,s}(F_n)$ を $\mathcal B_{1,s}$ に対する最短特徴標本の総符号長と定義する。§6–§7 から、
\[
 \boxed{
 n^2+3n+4\le\operatorname{cs}_{\mathcal B,s_{0,1}}(F_n)
 \le(8n-3)(2n^2+2n+4)
 }
\tag{27}
\]
および $s_{1,1}$ についても
\[
 \boxed{n^2+7n+4\le\operatorname{cs}_{\mathcal B,s_{1,1}}(F_n)
 \le O(n^3)\quad(n\ge2).}
\tag{28}
\]
が**証明された範囲**である。この情報だけでは $\Theta(n^2)$ と $\Theta(n^3)$ を区別できない。

**三次上界が発生する場所。** (24) では、高さ $i$ の型付き $l$ 規則を証拠化するとき、左子・右子の末尾型がともに $a$ である規則にも証拠を用意する。このとき各子の最短長は $(i-1)i+1$ であり、個別に各高さの証拠を足すと $\sum_{i=1}^n\Theta(i^2)=\Theta(n^3)$ になる。これは**今回構成した証拠集合のコスト**であり、最短特徴標本の三次下界を意味しない。

**二次への償却の可能性。** 一本の $U_n$ は、その右の $l$-背骨に沿って $U_{n-1},\ldots,U_0$ を連続因子として含み、各段の左兄弟 $C_{i-1}$ も含む。したがって、各型付き非終端の代表を独立した文として観測する必要はない。実際 §6.1 の標本から独立に、$U_n$ 一語の長さは $n^2+n+1$ である。しかし $U_n$ に含まれる規則の**左子型**は主に末尾 $r$ であり、左子末尾 $a$ のすべての型付き規則を自動的に証拠化するわけではない。また、異なる大きな語を一語の因子として含めるだけでは、それらに必要な**共通の外側文脈による Link** が存在するとは限らない。

**三次下界に必要な未証明ステップ。** 少なくとも $\mathcal B_{1,s_{0,1}}$ に対し、各高さ $i$ の左子末尾 $a$ という構造を生成するには、標本内にどの形の規則・Link 証拠が強制されるかを示す必要がある。そのうえで、異なる高さの証拠を一語内に入れ子にしたときでも、合計 $\Omega(n^3)$ の新しい文字数が必要と証明しなければならない。今回の調査ではこの二段階を完遂できなかった。従って、**$\Omega(n^3)$ を主張しない**。

## 9. Q3 と Q4：一般問題への帰結と限界

**窓型付け $s\preceq s_{k,\ell}$、固定ファンアウト $f$。** 調査対象の `thm:window-group-polydata` が与える上界は
\[
 \operatorname{cs}_{f,s}(L;G)=O_{f,r_{\max},s}(\|G\|^2\bar\theta_G).
\tag{29}
\]
また `prop:linear-factor-all-fanout` は、$|\Sigma|\ge4f+1$ において、クラス全体に特徴標本を持つ集合駆動作用素にも及ぶ $\Omega(\|G\|\bar\theta_G)$ を与える。今回の定理 4.1 と式 (27) は、4文字・ファンアウト1・末尾窓という厳密な試験例をクラスに確定させるが、(29) の余分な $\|G\|$ が一般に必要かどうかを解決しない。

**可換群・一般の局所群。** 対象原稿 `thm:local-group-polydata` は一般の局所群についても $O(\|G\|^2\bar\theta_G)$ を保証する。群のゼロ和や局所群への短縮では、型付き語の代表が高々 $O(\|G\|\bar\theta_G)$ に収まることと、同一の長い語を複数の規則で共有できることとは異なる。今回の構成は群型付けに対する線形積上界も、その反例も与えない。

**現時点の回答。** Q3 および Q4 は**未解決**。$F_n$ で $\tau=\Theta(\|G\|\bar\theta)$ になっても、特徴標本そのものが三次であるとは限らない。強い結論を出すには、上界側では**共通文脈の再利用まで含めた償却**、下界側では**観測構造を強制する新しい不変量**が必要である。

## 10. 再現可能な計算検証（Python 3 標準ライブラリのみ）

以下は独立した補助検査であり、**§2–§4 の全 $n$ に対する数学的証明の代用品ではない**。第一の検査は $n\le4$ で言語の全語を列挙し、因子–外側文脈の二部グラフが各連結成分で完全二部グラフとなることを検証する。これは式 (1) と同値である。第二の検査は $n\le5$ について解析器の到達可能スタック全体を列挙し、「同じ元状態で同じ先状態に至る二語は、他の任意の状態からの遷移結果も一致する（未定義を含む）」という**より強い有限状態性質**を検証する。両方とも有限範囲の確認であり、有限窓の切断を一般証明に昇格させない。

以下のコードブロック全体を `script.py` に保存すれば、Windows で `py -3 script.py` により実行できる。外部パッケージは不要である。

```python
from collections import Counter, deque

ALPHABET = "aclr"


def words(n):
    current = ["a"]
    for _ in range(n):
        previous = current
        current = (["l" + u + v for u in previous for v in previous]
                   + ["c" + u + "r" for u in previous])
    return current


def find(parent, x):
    root = x
    while parent.get(root, root) != root:
        root = parent[root]
    while x != root:
        p = parent[x]
        parent[x] = root
        x = p
    return root


def check_substitutability_exhaustive(n):
    """全因子と全外側文脈の有限二部グラフを厳密に検査。"""
    first = {}
    parent = {}
    degree = Counter()

    for w in words(n):
        for i in range(len(w)):
            for j in range(i + 1, len(w) + 1):
                x = w[i:j]
                context = (w[:i], w[j:])
                degree[x] += 1
                if context not in first:
                    first[context] = x
                else:
                    px = find(parent, x)
                    py = find(parent, first[context])
                    if px != py:
                        parent[py] = px

    number_of_contexts = Counter()
    for x in first.values():
        number_of_contexts[find(parent, x)] += 1

    for x, deg in degree.items():
        if deg != number_of_contexts[find(parent, x)]:
            raise AssertionError((n, "not substitutable", x))
    print("exhaustive PASS", n, "words", len(words(n)),
          "factors", len(degree), "contexts", len(first))


def step(stack, ch):
    """E_i は整数 i、待機記号 R は -1 で表す。"""
    if not stack:
        return None
    head, rest = stack[0], stack[1:]
    if ch == "a":
        return rest if head == 0 else None
    if ch == "r":
        return rest if head == -1 else None
    if ch == "c":
        return (head - 1, -1) + rest if head > 0 else None
    if ch == "l":
        return (head - 1, head - 1) + rest if head > 0 else None
    raise ValueError(ch)


def reachable_automaton(n):
    initial = (n,)
    state_id = {initial: 0}
    states = [initial]
    queue = deque([initial])
    edges = []
    while queue:
        stack = queue.popleft()
        successors = []
        for ch in ALPHABET:
            nxt = step(stack, ch)
            if nxt is None:
                successors.append(-1)
                continue
            if nxt not in state_id:
                state_id[nxt] = len(states)
                states.append(nxt)
                queue.append(nxt)
            successors.append(state_id[nxt])
        edges.append(tuple(successors))
    return states, edges


def check_parser_coherence(n):
    """到達可能な全状態ペアについて経路ラベルの作用の整合性を検査。"""
    states, edges = reachable_automaton(n)
    total = len(states)
    for source in range(total):
        for alternate in range(total):
            # 写像 phi: source の到達状態 -> alternate の遷移結果。
            # -1 は未定義を表す吸収状態。
            phi = {source: alternate}
            todo = [source]
            while todo:
                a = todo.pop()
                b = phi[a]
                for letter_index, a_next in enumerate(edges[a]):
                    if a_next < 0:
                        continue
                    b_next = edges[b][letter_index] if b >= 0 else -1
                    if a_next not in phi:
                        phi[a_next] = b_next
                        todo.append(a_next)
                    elif phi[a_next] != b_next:
                        raise AssertionError(
                            (n, "parser action conflict", states[source],
                             states[alternate], states[a_next]))
    print("parser coherence PASS", n, "reachable stacks", total)


def verify_lengths(n):
    q = 1
    for i in range(1, n + 1):
        q = q * q + q
        if i <= 4:
            assert q == len(words(i))
    a = "a"
    for i in range(1, n + 1):
        c = "c" * (i - 1) + "a" + "r" * (i - 1)
        a = "l" + c + a
        assert len(a) == i * (i + 1) + 1
    assert len("c" * n + "a" + "r" * n) == 2 * n + 1
    print("length formulas PASS", n)


if __name__ == "__main__":
    for level in range(1, 5):
        check_substitutability_exhaustive(level)
    for level in range(1, 6):
        check_parser_coherence(level)
    verify_lengths(5)
```

**今回の実行結果（要約）。** 全数列挙の語数は順に $2,6,42,1806$、対応する因子種類数は $10,77,1126,73605$、外側文脈の種類数は $11,111,2251,246689$ で、すべて PASS。有限スタック検査の到達可能状態数は $n=1,2,3,4,5$ でそれぞれ $6,16,42,110,288$、すべて PASS。計算結果は**独立検証の記録**であり、無限個の $n$ の証明は §4 に置いた。

## 11. 文献・原稿との照合と新規性の扱い

1. **Clark and Eyraud (2007)**, *Polynomial Identification in the Limit of Substitutable Context-free Languages*, JMLR **8**, 1725–1745：代入可能性の定義および正例による文法推論の基本文献。<https://www.jmlr.org/papers/v8/clark07a.html>。
2. **Yoshinaka (2008)**, *Identification in the Limit of $k,l$-Substitutable Context-Free Languages*, ICGI 2008, LNCS 5278, 266–279：窓による代入可能性と特徴標本に関する既存の研究。<https://doi.org/10.1007/978-3-540-88009-7_21>。
3. **Kuriyama**, *Distributional Learning of Context-Free Languages under Fixed Finite-Semigroup Typing*, TCS R1 原稿 Appendix C：閉じ記号を両側に持つ括弧付き倍増族の証明を比較対象として使用。今回の (5) は**新しい文法への旧分岐同期補題の移植**に対する反例であって、Appendix C 自身に対する反例ではない。
4. **Kuriyama**, 対象 MCFG 原稿 `02-v2-lg-fanout-boundary/main.tex`：`def:reconstruction`、`prop:rare-type`、`cor:distribution-representatives`、`lem:heavy-node-count`、`thm:window-group-polydata`、`thm:local-group-polydata`、`prop:linear-factor-all-fanout` に照合。公開場所：<https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/main.tex>。
5. **Coste and Nicolas ほかの局所代入可能性研究**、**Eyraud–Heinz–Yoshinaka (2016)** による thick-data の議論は、計算量の比較モデルとして参照。今回の $F_n$ と不変量 (6) が既に発表済みかどうかは**未確認**。関連文献における非掲載を証明したわけではない。

### 最終的な研究判断

**論文に組み込む候補として確定できる部分**は、定理 4.1 の全 $n$ 代入可能性、式 (5) の旧証明移植への反例、(9)・(12)・(15)–(19) の厳密値、命題 6.1 の具体的 $O(n^3)$ 特徴標本、命題 7.1–7.2 の作用素を明記した二次下界である。これらは本報告内で証明したが、投稿前に第三者による独立した証明監査を推奨する。

**依然として未解決**なのは、$F_n$ の最短特徴標本長の二次対三次の決着、固定窓型付け一般での $O(\|G\|\bar\theta_G)$、ならびに可換群・一般局所群への同じ改善である。今回の結果は、これらの肯定・否定のどちらも確定しない。

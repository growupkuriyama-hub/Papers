# 窓型付け特徴データ長のギャップ：第2次調査

**対象：** $F_n=L(E_n)$、$s=s_{0,1}$、$\mathcal B_{1,s}$ および $\mathcal B_{1,s}^{\le2}$  
**調査日：** 2026年10月31日  
**原稿正本：** [Papers/02-v2-lg-fanout-boundary/main.tex](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/main.tex)、照合した Git blob `d03710d94d0274df05b7b49e53e85b218e65d599`。  
**前提：** 前回報告の全 $n$ に対する代入可能性の定理、$\|G_n\|=12n+3$、$\bar\theta_{G_n}=4n-1$、$\mu_a=n(n+1)+1$ は本報告では再証明せずに使用する。以下の新しい証明は原稿への採用前に独立監査が必要である。

## 結論の要約表

| 主張 | 判定 | 根拠の節 |
|---|---|---|
| ファンアウト1では、任意の有限標本 $K$ と任意の型付け $s$ に対し $L(\mathcal B_{1,s}(K))=L(\mathcal B_{1,s}^{\le2}(K))$ | **証明済み** | §2 |
| $F_n$ の構文的合同は、受理可能な接頭辞から到達するスタック上の部分変換の一致と同値 | **証明済み** | §3.1 |
| 「全スタック上の部分変換の一致」が構文的合同の必要条件である（因子でない語も含める主張） | **反証** | §3.2 |
| $u,v\in L_i$ に対し、$uc,vc$（または $ul,vl$）は同じ部分スタック変換を持ち、末尾型も一致する | **証明済み** | §3.3 |
| B が段 $j$ の「左子末尾 $a$」節点を生成するには、標本にもその段の節点が必要 | **反証**（すでに $j=n$, 全 $n\ge3$ で偽） | §4 |
| 全 $n\ge3$ に対し、**最上段の該当節点を全く含まない**有限集合 $K_n^{\neg\mathrm{top}}$ が、B の両版の特徴標本である | **証明済み** | §4.3 |
| 上記の「該当節点を持つ語を削除した言語」が必ず $\mathcal C_{1,s}$ に残る | **反証**（$n=3$） | §4.4 |
| 真の構文木における該当節点の重み $\sum_v A_{\mathrm{level}(v)-1}$ は、文の長さの4倍以下 | **証明済み** | §5 |
| 各段の該当節点が標本に必ず現れる、という**追加仮定の下**で $\Omega(n^3)$ | **証明済み（条件付き）**。追加仮定自体は偽 | §5.3 |
| $n=1,2$ での最短特徴データ長は順に $8,44$ | **観察**（全候補を有限検査） | §6 |
| $s_{0,1}$ で最短特徴データ長 $\Theta(n^2)$ または $\Theta(n^3)$ のどちらかが成立する | **未解決** | §7 |
| $\Omega(n^3)$ がクラス全体に特徴標本を持つ任意の集合駆動作用素に及ぶ | **未解決** | §7.2 |
| 前回の $H$ 不変量が下側スタック $\psi$ に依存しない部分の比較で十分 | **証明済み（補足）** | §8 |

**今回の決着点は「二次か三次か」の解決ではなく、三次下界のために提案された必須観測補題の明示的反証である。** しかも、反例は単なる1語の生成にとどまらず、各 $n\ge3$ について、最上段の該当節点を一つも観測しない特徴標本にまで拡張できる。一方、これらの特徴標本は巨大なので $O(n^2)$ 上界を証明しない。

## 1. 設定と区別すべき命題

$\Sigma=\{a,l,c,r\}$、$L_i=L(E_i)$ とし、
\[
E_0\to a,\qquad E_i\to lE_{i-1}E_{i-1}\mid cE_{i-1}r\quad(i\ge1).
\]
$F_n=L_n$ とする。語の末尾文字を型とする全射半群準同型 $s_{0,1}:\Sigma^+\to\Sigma$ を使用する（積は右側因子を返す右零半群の積）。

$C_i=c^ia r^i$、$U_0=a$、$U_i=lC_{i-1}U_{i-1}$ とし、末尾 $a$ の $L_i$ 語の最短長を
\[
A_i:=i(i+1)+1
\]
と書く。前回の結果は
\[
 n^2+3n+4\le \operatorname{cs}_{\mathcal B,s_{0,1}}(F_n)
 \le(8n-3)(2n^2+2n+4)
\tag{1}
\]
である。

段 $j$ の **$A$-左節点**とは、$E_j\to lE_{j-1}E_{j-1}$ を使用し、**左の子の完全な生成語が $a$ で終わる**導出木の節点をいう。これは実際の $G_n$ の決定的解析木に関する条件であり、観測された因子が偶然 `l` を含むという条件ではない。$j=n$ の場合だけを **最上段の $A$-左節点**という。

以後、$\operatorname{cs}_{\mathcal B,s}(F_n)$ は $\mathcal B_{1,s}$ に対する最短特徴標本の総符号長 $\sum_{w\in K}(|w|+1)$ とする。特徴標本の上方閉性、および $\mathcal B(K)$ の標本集合 $K$ に関する単調性を使用する。

## 2. 無制限 Comp とランク2 Comp の同値

**定理 2.1（ファンアウト1の Comp 二分化）。** 任意の言語上の有限標本 $K$ と任意の型付け $s$ に対し、
\[
\boxed{L(\mathcal B_{1,s}(K))=L(\mathcal B_{1,s}^{\le2}(K)).}
\tag{2}
\]
これは目標言語の代入可能性を必要としない。

**証明。** ランク2版の規則は無制限版の規則の一部なので、右辺が左辺に含まれる。逆向きには、無制限版の任意の Comp 規則
\[
[z]\longrightarrow c_0[u_1]c_1[u_2]\cdots c_{r-1}[u_r]c_r,
\qquad r\ge3,
\tag{3}
\]
を考える。$u_1,\ldots,u_r$ はすべて非空で、$c_h$ は空でもよい端末ギャップであり、文字列として
$z=c_0u_1c_1\cdots u_rc_r$ が観測されている。

$v=c_0u_1c_1\cdots u_{r-1}c_{r-1}$ と置く。$v$ は非空で $z$ の連続因子だから、$z$ が観測された $K$ の語の中に $v$ も観測され、$[v]$ が存在する。次のランク2規則がある：
\[
[z]\longrightarrow[v][u_r]c_r.
\tag{4}
\]
同様に $[v]$ には、$v$ の末尾の非空子 $u_{r-1}$ を切り出すランク2規則がある。この操作を繰り返し、最終的に
\[
[c_0u_1c_1]\longrightarrow c_0[u_1]c_1
\]
というランク1規則へ達する。すべての中間語は $z$ の非空連続因子なので観測条件を満たす。各規則は各子をちょうど一度使い、出力成分は非空なので、ファンアウト1の good-template 条件に違反しない。

この一連の規則で得られる端末出力と子非終端の順序は (3) と同じである。したがって無制限版の任意の有限導出木で各高ランク Comp 節点を置き換えれば、ランク2版に同じ生成語の導出木を得る。Link、Const、Start は両版で同一なので結論が従う。□

従って以下の上界・下界問題において、**B の無制限版とランク2版を区別する必要はない**。ただし、この定理はファンアウト $f\ge2$ の一般的なランク2化を主張しない。

## 3. スタック変換による合同類の正確な扱い

### 3.1 有限の到達可能スタック上では必要十分

前回の決定的解析器を $\delta$ と書き、初期スタック $E_n$ から **受理語の接頭辞**を読んで到達するスタックの集合を
\[
Q_n=\{\delta(E_n,p):\exists q,\;pq\in F_n\}
\tag{5}
\]
とする。$Q_n$ は有限である。実際、解析器の各遷移は前回の重み $\mathrm{wt}(E_i)=4^i$, $\mathrm{wt}(R)=1$ を厳密に下げ、初期重みは $4^n$ であり、各重み以下のスタックは有限個しかない。また、到達するスタックはすべて構成要素 $E_i,R$ からなり、それぞれを最後まで読み切れるため、$Q_n$ の各状態は空スタックまで補完可能である。

語 $x$ が $Q_n$ 上に誘導する部分変換を $T_x:Q_n\rightharpoonup Q_n$ とする。

**定理 3.1（到達可能状態による合同類の分類）。** 任意の $x,y\in\Sigma^*$ に対し、
\[
\boxed{x\equiv_{F_n}y\quad\Longleftrightarrow\quad T_x=T_y.}
\tag{6}
\]
従って非空因子についての $s_{0,1}$-型付き合同は、$T_x=T_y$ かつ最後の文字が等しいことにより必要十分に分類される。

**証明。** まず $x\equiv_{F_n}y$ とし、$\sigma\in Q_n$ で $T_x(\sigma)=\tau$ が定義されるとする。$\sigma=\delta(E_n,p)$ となる接頭辞 $p$ を選ぶ。$\tau$ は空スタックまで読めるので、ある $q$ に対し $pxq\in F_n$ である。合同性より $pyq\in F_n$ であり、$T_y(\sigma)$ も定義される。$q$ を読む部分変換は、前回の一文字遷移の単射性から単射である。$T_x(\sigma)$ と $T_y(\sigma)$ がともに $q$ で空スタックになるため、両者は等しい。$x,y$ を交換すれば両者の定義域も一致するので $T_x=T_y$ である。

逆に $T_x=T_y$ とする。任意の文脈 $(p,q)$ について、$pxq\in F_n$ なら $p$ の読後は $Q_n$ の状態であり、$x,y$ の読後のスタックが一致する。よって $pyq\in F_n$ である。$x,y$ の交換により逆向きも成立する。すなわち構文的合同である。□

### 3.2 「全スタック上の変換の一致」は必要でない

ここで (6) を、**到達不能な高い添字の $E_i$ まで含む全スタック**に拡張してはならない。例えば
\[
x=c^{n+1},\qquad y=l^{n+1}
\]
は、どちらも $F_n$ の因子ではない。$E_n$ から到達するどのスタックでも先頭の非終端指数は高々 $n$ なので、$n+1$ 文字の連続した $c$ または $l$ は処理できず、$T_x=T_y=\varnothing$ である。従って $x\equiv_{F_n}y$ だが、仮に高い添字 $E_{n+1}$ から読むと二つの入力の最終スタックは異なる。

これは **因子でない語も含めた全称命題**への反例である。$F_n$ の因子に限定した場合の「全スタック変換の一致」の必要性は、(6) だけからは結論できない。本研究で必要十分と確定したのは、あくまで $Q_n$ 上の作用である。

### 3.3 末尾型で隠れる境界：$ub$ と $vb$

**補題 3.2（次の開き記号による遮蔽）。** $i\ge1$、$u,v\in L_i$、$b\in\{c,l\}$ とする。$ub$ と $vb$ が全スタック上に誘導する部分変換は同じであり、$s_{0,1}(ub)=s_{0,1}(vb)=b$ である。

**証明。** $L_i$ の各語は最初の $a$ がちょうど $i+1$ 文字目に現れ、先頭は $c$ または $l$ である。従って $u$ でも $v$ でも、実行可能な初期スタックの先頭は必ず $E_i$ である（前回の最初の $a$ に関する補題を任意の下側スタックに適用する）。両語とも $E_i$ を完全に消費して下側スタックをそのまま残す。その後 $b$ が読めるのは下側スタックが $E_h\psi$（$h\ge1$）のときに限る。その場合の結果は、$b=c$ なら $E_{h-1}R\psi$、$b=l$ なら $E_{h-1}E_{h-1}\psi$ となり、$u,v$ の選択によらない。これ以外の初期スタックからは両者とも実行不能である。末尾型の一致は明らかである。□

特に $i=1$、$u=car$、$v=laa$ とすると
\[
\boxed{carc\equiv_{F_n,s_{0,1}}laac,\qquad
carl\equiv_{F_n,s_{0,1}}laal.}
\tag{7}
\]
ただし **B が実際に Link を作るには**、合同であるだけでなく、この二つの因子が $K$ 内で同じ外側文脈を共有する必要がある。次節ではその証拠を具体的に与える。

## 4. 「段 $j$ の実際の出現を標本に要する」は偽

### 4.1 最小の見やすい反例（$n=j=3$）

以下の2語はいずれも $F_3$ に属する：
\[
\begin{aligned}
X&=\texttt{lllaacarclaar}
  =l\,(l\,laa\,car)\,(c\,laa\,r),\\
Y&=\texttt{llcarcarclaar}
  =l\,(l\,car\,car)\,(c\,laa\,r).
\end{aligned}
\tag{8}
\]
**どちらも最上段の $A$-左節点を持たない。** なぜなら最上段の $l$ の左の $E_2$ 語は、それぞれ `llaacar` と `lcarcar` であり、ともに末尾 $r$ だからである。

$K=\{X,Y\}$ とする。次の共通文脈が $K$ 内に存在する：
\[
\begin{aligned}
Y&=\texttt{ll}\;\underline{\texttt{carc}}\;\texttt{arclaar},\\
X&=\texttt{ll}\;\underline{\texttt{laac}}\;\texttt{arclaar}.
\end{aligned}
\tag{9}
\]
`carc` と `laac` はともに末尾 `c` だから、B は **Link**
$[\texttt{carc}]\to[\texttt{laac}]$ を持つ。一方、$X$ 自体を別の位置で切ると
\[
X=\texttt{lllaa}\;\underline{\texttt{carc}}\;\texttt{laar}
\tag{10}
\]
である。ここで **ランク1 Comp** と Link と Const を順に使うと
\[
\begin{aligned}
\widehat S&\to[X]\\
&\to\texttt{lllaa}\,[\texttt{carc}]\,\texttt{laar}\\
&\to\texttt{lllaa}\,[\texttt{laac}]\,\texttt{laar}\\
&\to Z:=\texttt{lllaalaaclaar}.
\end{aligned}
\tag{11}
\]
$Z$ の決定的構文解析は
\[
Z=l\,(l\,laa\,laa)\,(c\,laa\,r)
\tag{12}
\]
である。従って **最上段の左子 `llaalaa` は $a$ で終わり、$Z$ は段3の $A$-左節点を持つ。** (8)–(12) は全て文字列の等式および原稿の Const／Comp／Link／Start 規則を使った有限の証明であり、計算探索結果に依存しない。

この反例により、提案された R1(a) の「全ての段の該当節点が標本語の決定的構文木に実際に現れる」という必要条件は、**B に対して偽**と確定する。

### 4.2 何が起きたか：本来の構文境界を跨ぐ Link

`carc` から `laac` への置換では、前半の `car`／`laa` が **一つの $E_1$ 語**で、最後の `c` は **次の非終端が生成する語の先頭**である。末尾型 $s_{0,1}$ が見るのは最後の `c` だけである。従って、置換は $E_1$ 語の末尾を $r$ から $a$ に変更しながらも、**Link を掛けた因子全体の型は変えない**。しかも (10) ではこの置換が $E_3$ の左右の子の境界を跨ぐため、親の左子が $r$ 終端から $a$ 終端へ変化する。

つまり「型付き合同類の成員は同じ型」という事実だけでは、**内部にある文法の子の境界での末尾型**を保存できない。これが文法準拠の出現を B に強制する下界戦略の破綻点である。

### 4.3 全ての $n\ge3$ への拡張：最上段の該当節点を一切含まない特徴標本

**定理 4.1（最上段 $A$-左節点の観測は不要）。** $n\ge3$ とし、
\[
K_n^{\neg\mathrm{top}}
=F_n\setminus\{l u v:u,v\in L_{n-1},\ u\text{ の末尾が }a\}
\tag{13}
\]
とする。すなわち、最上段が $c$ 分岐の語、または最上段が $l$ 分岐でその左子が末尾 $r$ の語を **すべて**集めた有限標本である。このとき $K_n^{\neg\mathrm{top}}$ は $\mathcal B_{1,s_{0,1}}$ と $\mathcal B_{1,s_{0,1}}^{\le2}$ の特徴標本である。しかし $K_n^{\neg\mathrm{top}}$ のどの語の構文木にも最上段の $A$-左節点はない。

**証明。** $b\in\{c,l\}$ に対し、$D_c=car$、$D_l=laa$ とおき、$x\in\{car,laa\}$ に対して
\[
W_b(x)=l\,C_{n-1}\,c^{n-3}\,(l\,x\,D_b)\,r^{n-3}
\tag{14}
\]
を作る。$l x D_b\in L_2$、$c^{n-3}(l x D_b)r^{n-3}\in L_{n-1}$ なので、$W_b(x)\in F_n$ である。最上段の左子は $C_{n-1}$ で末尾 $r$、従って
\[
W_b(car),W_b(laa)\in K_n^{\neg\mathrm{top}}.
\]
両語は、$x$ と $D_b$ の先頭文字 $b$ をひとまとめにして因子 $xb$ を取り出すと、**同じ外側文脈**
\[
\bigl(lC_{n-1}c^{n-3}l,\;D_b[2:]r^{n-3}\bigr)
\tag{15}
\]
に、`car`$b$ と `laa`$b$ を入れたものになっている（$D_b[2:]$ は $D_b$ の先頭1文字を除いた残余）。二つは同じ末尾文字 $b$ を持つので、B には
\[
[carb]\longrightarrow[laab]
\tag{16}
\]
という Link がある。ここで $carb$／$laab$ は、文字列 `car`／`laa` に文字 $b$ を連結した略記である。

さて任意の $w\in F_n\setminus K_n^{\neg\mathrm{top}}$ を取る。$w=luv$（$u,v\in L_{n-1}$）で $u$ は末尾 $a$ である。決定的構文木で $a$ に終わる $E_i$ 語は、その右端の経路で $E_i\to lE_{i-1}E_{i-1}$ を繰り返し、最後は $E_1\to laa$ になる。よって $u=t\,laa$ と書け、この最後の $E_1$ だけを $E_1\to car$ に替えた
\[
u^-:=t\,car\in L_{n-1}
\tag{17}
\]
は末尾 $r$ になる。$v=bv'$ と書くと $b\in\{c,l\}$ である（$n-1\ge2$）。したがって
\[
w^-=l u^-v=l\,t\,\underline{carb}\,v'
\tag{18}
\]
は $K_n^{\neg\mathrm{top}}$ に含まれ、Start 規則を持つ。(18) の下線部は観測された非空因子なので、ランク1 Comp を使って
\[
[w^-]\longrightarrow l\,t\,[carb]v'
\]
とし、(16) の Link を適用し、Const $[laab]\to laab$ を使えば
\[
[w^-]\Rightarrow^*l\,t\,laa\,b v'=w
\tag{19}
\]
を得る。$K_n^{\neg\mathrm{top}}$ に入っている語は Start と Const のみで生成される。したがって $F_n\subseteq L(\mathcal B_{1,s}^{\le2}(K_n^{\neg\mathrm{top}}))$ である。

逆向きは前回確定した $F_n$ の代入可能性と現行原稿 `prop:reconstruction-soundness` により従う。さらに任意の有限 $K$ が $K_n^{\neg\mathrm{top}}\subseteq K\subseteq F_n$ を満たすとき、B の全規則は観測データの追加に関して単調に増えるため、上の包含は保存される。健全性も保存される。以上より、(13) は両版の特徴標本である。□

**重要な限定。** (13) は $F_n$ の大きな部分集合であり、語数は指数的・超指数的に増える。そのため、この定理は短い特徴標本の構成ではない。証明されたのは、**三次下界のための「段ごとの標本内出現」という必要条件が、最上段ですでに失敗する**という点である。

### 4.4 節点を持つ語を削除した言語はクラス内とは限らない

$n=3$ で $L'=K_3^{\neg\mathrm{top}}$ と置く。式 (8) の $X,Y$ はともに $L'$ に含まれ、式 (9) により `carc` と `laac` は $L'$ の共通の文脈を持つ同型（末尾 `c`）の因子である。しかし式 (10) では
\[
\texttt{lllaa}\;\texttt{carc}\;\texttt{laar}=X\in L',
\]
その `carc` を `laac` に替えると式 (12) の $Z\notin L'$ になる。従って二因子の $L'$ における分布は一致せず、
\[
\boxed{K_3^{\neg\mathrm{top}}\notin\mathcal C_{1,s_{0,1}}.}
\tag{20}
\]
このことは、**「特定の段の出現を持つ語だけを削除する」操作を、稀な型の削除と同じように使えない**ことを示す明示反例である。

## 5. Claude の入れ子コストの厳密な償却定理

反例 §4 は「段ごとの構文木内の出現を観測することが必要」という主張を崩すが、**もし出現を観測すると仮定するなら総長が三次になる**、という組合せ論的主張は、より強い形で証明できる。

### 5.1 重みを定義する

$E_i$ からの決定的導出木 $T$ に対し、$\mathsf M(T)$ をその木のすべての $A$-左節点 $v$ について
\[
\mathsf M(T):=
\sum_{\substack{v\text{ は }A\text{-左節点}\\ \mathrm{level}(v)=j\ge1}}
 A_{j-1},\qquad A_{j-1}=j(j-1)+1
\tag{21}
\]
と定める。**同じ段の節点が複数あればすべて数える**。この重みは各印の左子の最短生成語長に等しい。

### 5.2 一文に載せられる印の合計は長さに比例する

**定理 5.1（全導出木の $A$-左重みの償却）。** $i\ge0$ の任意の $E_i$ 導出木 $T$ に対して
\[
\boxed{\mathsf M(T)\le4\,|\operatorname{yield}(T)|.}
\tag{22}
\]
より強く、$\varepsilon(T)=1$ を生成語が $a$ で終わる場合、そうでなければ $0$ とすると
\[
|\operatorname{yield}(T)|
-\tfrac14\mathsf M(T)
-\tfrac14 A_i\varepsilon(T)
\ge\tfrac12(i+1).
\tag{23}
\]

**証明。** (23) を $i$ に関して帰納法で示す。$i=0$ では生成語は `a`、印はなく、左辺は $1-\frac14=\frac34\ge\frac12$ である。

$i\ge1$ とする。根が $c$ 規則なら子木を $T_1$ として、根は $A$-左節点でなく、親の生成語は $r$ で終わる。左辺の量を $\Phi$ と書くと
\[
\Phi(T)=2+\Phi(T_1)+\tfrac14 A_{i-1}\varepsilon(T_1)
\ge2+\tfrac i2\ge\tfrac{i+1}{2}.
\]

根が $l$ 規則なら左右の子木を $T_1,T_2$ とする。親の末尾型は右子の末尾型と同じであり、根が新しい $A$-左節点になるのは $\varepsilon(T_1)=1$ の場合だけで、その重みは $A_{i-1}$ である。従って定義を代入すると、**左子の $A_{i-1}$ の寄与がちょうど相殺し**、
\[
\begin{aligned}
\Phi(T)
&=1+\Phi(T_1)+\Phi(T_2)
  -\tfrac14(A_i-A_{i-1})\varepsilon(T_2)\\
&=1+\Phi(T_1)+\Phi(T_2)-\tfrac i2\varepsilon(T_2)\\
&\ge1+i-\tfrac i2\ge\tfrac{i+1}{2},
\end{aligned}
\]
となる。ここで $A_i-A_{i-1}=2i$ と帰納法の $\Phi(T_h)\ge i/2$ を使った。これで (23) が帰納的に成立する。(23) の右辺と $\frac14A_i\varepsilon(T)$ は非負なので、両者を捨てれば (22) が従う。□

これは Claude の「重なりは入れ子の鎖だけである」という議論を、**同じ段の複数節点を含めて、一語にいくつ出現しても成立する普遍的な不等式**にしたものである。鎖の種類や相互位置を個別に場合分けする必要がない。

### 5.3 三次下界になるための、しかし偽である追加仮定

**系 5.2（条件付き三次下界）。** 有限標本 $K\subseteq F_n$ が、各段 $j=2,\ldots,n$ に対して少なくとも一つの語の構文木に段 $j$ の $A$-左節点を含むと仮定する。そのとき
\[
\begin{aligned}
4\|K\|_+
&\ge\sum_{w\in K}\mathsf M(T_w)
 \ge\sum_{j=2}^n A_{j-1}\\
&=\frac{n(n+1)(n-1)}{3}+n-1,
\end{aligned}
\]
すなわち
\[
\boxed{\|K\|_+\ge\frac{n(n+1)(n-1)}{12}+\frac{n-1}{4}
=\Omega(n^3).}
\tag{24}
\]

**証明。** 各 $j$ について選ばれた節点の重み $A_{j-1}$ を合計する。この合計は $K$ 全体の全印の重み以下である。定理 5.1 を各 $T_w$ に適用し、$|w|\le|w|+1$ を足し上げれば (24) を得る。最後の和は $\sum_{j=2}^n(j(j-1)+1)$ を展開したものである。□

**適用の限界：** 系 5.2 は「各段の印が標本の本当の構文木に現れる」という仮定を必要とする。しかし定理 4.1 は、その仮定が B の特徴標本に対してすら（$j=n$ で）保証されないことを示す。従って (24) を **無条件の $\operatorname{cs}_{\mathcal B,s}(F_n)$ の下界に流用することはできない**。新しい下界には、観測された構文木ではなく、Link による境界横断をも勘定する別の不変量が必要である。

## 6. 小さい $n$ の独立した有限検査

次のコードは Python 3 の標準ライブラリだけを使う。$n\le2$ に対し、観測した非空因子に対応する非終端を作り、共通文脈・末尾型の Link 連結成分を計算する。Comp をランク1・2の全分割で調べ、**生成される長さごとの動的計画法**で各 $F_n$ 語の導出可能性を判定する。長さを保つランク1 Comp は $[z]\to[z]$ という自明な自己規則だけなので、同長の非自明循環は Link 成分への縮約で除かれる。導出語は soundness により $F_n$ の因子なので、有限な因子集合だけを調べれば足りる。

さらに $n=3$ の反例 (8)–(12) と、最上段の $A$-左節点を持たない全語からの **1回の Link 置換**で $F_3$ の全42語が得られることを確認する。これは定理 4.1 の全 $n$ の証明に代わるものではない。

以下全体を `round2_check.py` として保存し、Windows では `py -3 round2_check.py` で実行できる。

```python
from collections import defaultdict


def words(n):
    ans = ["a"]
    for _ in range(n):
        ans = (["l" + u + v for u in ans for v in ans]
               + ["c" + u + "r" for u in ans])
    return ans


def contexts(data):
    result = defaultdict(set)
    for w in data:
        for a in range(len(w)):
            for b in range(a + 1, len(w) + 1):
                result[w[a:b]].add((w[:a], w[b:]))
    return result


def complete(data, target, cap=2):
    obs = contexts(data)
    if not obs:
        return False
    parent = {x: x for x in obs}

    def root(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    shared = defaultdict(list)
    for x, cs in obs.items():
        for c in cs:
            shared[(c, x[-1])].append(x)
    for xs in shared.values():
        for y in xs[1:]:
            parent[root(y)] = root(xs[0])
    group = {x: root(x) for x in obs}
    rules = defaultdict(list)
    for z, g in group.items():
        m = len(z)
        for a in range(m):
            for b in range(a + 1, m + 1):
                u = z[a:b]
                rules[g].append((z[:a], group[u], z[b:]))
                if cap >= 2:
                    for c in range(b, m):
                        for d in range(c + 1, m + 1):
                            v = z[c:d]
                            rules[g].append((z[:a], group[u],
                                             z[b:c], group[v], z[d:]))

    derivable = defaultdict(set)
    for y in sorted(contexts(target), key=lambda t: (len(t), t)):
        got = {group[y]} if y in group else set()
        for g, candidates in rules.items():
            if g in got:
                continue
            for rule in candidates:
                if len(rule) == 3:
                    p, a, q = rule
                    if not y.startswith(p) or not y.endswith(q):
                        continue
                    middle = y[len(p):len(y)-len(q) if q else len(y)]
                    if len(middle) < len(y) and a in derivable[middle]:
                        got.add(g)
                        break
                else:
                    p, a, q, b, r = rule
                    if not y.startswith(p) or not y.endswith(r):
                        continue
                    mid = y[len(p):len(y)-len(r) if r else len(y)]
                    for split in range(1, len(mid)):
                        if a not in derivable[mid[:split]]:
                            continue
                        tail = mid[split:]
                        if tail.startswith(q) and b in derivable[tail[len(q):]]:
                            got.add(g)
                            break
                    if g in got:
                        break
        derivable[y] = got
    starts = {group[w] for w in data}
    return all(derivable[w] & starts for w in target)


def mark_at_root(w, n):
    if not w.startswith("l"):
        return False
    # E_{n-1} の左子を決定的に完全に読み切る。
    def finish(i, p):
        if i == 0:
            assert w[p] == "a"
            return p + 1
        if w[p] == "c":
            q = finish(i - 1, p + 1)
            assert w[q] == "r"
            return q + 1
        assert w[p] == "l"
        q = finish(i - 1, p + 1)
        return finish(i - 1, q)
    boundary = finish(n - 1, 1)
    return w[boundary - 1] == "a"


def one_link_step(data):
    cx = contexts(data)
    linked = defaultdict(set)
    by_context = defaultdict(set)
    for x, cs in cx.items():
        for c in cs:
            by_context[(c, x[-1])].add(x)
    for xs in by_context.values():
        for x in xs:
            linked[x].update(xs)
    out = set(data)
    for w in data:
        for i in range(len(w)):
            for j in range(i + 1, len(w) + 1):
                for y in linked[w[i:j]]:
                    out.add(w[:i] + y + w[j:])
    return out


if __name__ == "__main__":
    for n in (1, 2):
        L = words(n)
        assert complete(L, L)
        for omitted in L:
            assert not complete([w for w in L if w != omitted], L)
        print("all words necessary", n,
              "count", len(L), "length", sum(len(w) + 1 for w in L))

    X = "lllaacarclaar"
    Y = "llcarcarclaar"
    Z = "lllaalaaclaar"
    assert X in words(3) and Y in words(3) and Z in words(3)
    assert not mark_at_root(X, 3) and not mark_at_root(Y, 3)
    assert mark_at_root(Z, 3)
    assert Y == "ll" + "carc" + "arclaar"
    assert X == "ll" + "laac" + "arclaar"
    assert X == "lllaa" + "carc" + "laar"
    assert Z == "lllaa" + "laac" + "laar"
    print("two-word crossing-Link counterexample PASS")

    L3 = words(3)
    K3 = [w for w in L3 if not mark_at_root(w, 3)]
    assert len(L3) == 42 and len(K3) == 30
    assert set(L3).issubset(one_link_step(K3))
    print("top-mark-free one-Link completeness PASS", len(K3), len(L3))
```

**実行結果（有限観測）：**

```text
all words necessary 1 count 2 length 8
all words necessary 2 count 6 length 44
two-word crossing-Link counterexample PASS
top-mark-free one-Link completeness PASS 30 42
```

$\mathcal B(K)$ は入力集合に関して単調なので、$n=1,2$ について各語を1個取り除いた $K$ が完全でなければ、すべての真部分集合も完全ではない。したがって上の有限検査は、この2段について最短標本が $F_1,F_2$ 自身であることを判定している。ただし、**有限計算は全 $n$ の漸近下界の証明ではない**。$n=3$ の一段 Link の網羅性も有限検査であり、一般 $n$ については §4.3 の数学的証明を根拠にする。

## 7. R1–R3 への回答と次の研究対象

### 7.1 R1：$\Theta(n^2)$ 対 $\Theta(n^3)$ はなお未解決

現在、無条件に主張できる数値境界は前回の (1) のままである。今回の定理 2.1 により **無制限 B とランク2版 B について、この問いの答えは必ず一致する**。また定理 4.1 により、三次下界を導くための「各段の本来の $l$ 節点は標本に現れる」という主張は **最上段からして偽**である。

したがって、次の二つを区別する必要がある。

1. **真の構文木の重みの償却：** 定理 5.1 により解決済み。印を持つ語を選んで観測する方式なら、段ごとの印に対して $\Omega(n^3)$ の支払いが生じる。
2. **B の非標準導出の観測コスト：** 未解決。§4 の Link は、標本に該当の印がなくても、**より小さな因子の合同を使って印を新しく生み出す**。この方式を各段で共用して $O(n^2)$ の特徴標本にできるのか、それとも各段に別の境界横断用証拠が必要で結局 $\Omega(n^3)$ なのか、証明していない。

ここで「$T_x=T_y$ の有限分類」は §3.1 で確定したが、それ単独では観測証拠の量を下から抑えられない。実際、$[carc]\to[laac]$ のような **短い合同因子が、長い非終端の末尾型を横断的に変える**からである。次に研究すべきは、個々の $A$-左節点ではなく、**どの境界で、どの型の終端を変更できる Link 証拠が標本から供給されるか**という、観測に依存する不変量である。

### 7.2 R2：クラス全体の集合駆動作用素への下界

今回は $\Omega(n^3)$ を証明していないため、その作用素一般への拡張も証明していない。さらに (20) により、$A$-左節点を持つ語の削除は $\mathcal C_{1,s_{0,1}}$ に閉じていない。稀な型の削除に使った「小さい対抗言語がクラスに残る」議論を、そのまま反復することはできない。

前回の **$n^2+3n+4$** の下界は、$\mathcal B_{1,s_{0,1}}$・ランク2版、またクラス全体に特徴標本を持つ集合駆動作用素に引き続き成立する。これより強い下界を後者にも主張するには、クラス内の**複数の対抗言語の族**と、それらを正例集合で区別するための長さの下界を新たに用意する必要がある。

### 7.3 R3：窓型付け上界の鋭さ・自明型付け・高ファンアウト

もし将来 $s_{0,1}$、4文字、ファンアウト1のこの $F_n$ に対して $\Omega(n^3)$ を証明できれば、$\|G_n\|=\Theta(n)$、$\bar\theta_{G_n}=\Theta(n)$ だから
\[
\operatorname{cs}(F_n)=\Omega(\|G_n\|^2\bar\theta_{G_n})
\]
となり、原稿 `thm:window-group-polydata` の $O(\|G\|^2\bar\theta)$ がその条件下で鋭いことを示す。自明な型付けでの一様上界 $O(\|G\|\bar\theta)$ との **上界次数の分離**も生じる。ただし、これは現時点では **条件文**であり、結果ではない。また自明型付けの $F_n$ 自身の最短標本長が $\Theta(n^2)$ であると別途証明したわけではない。

ファンアウト $f\ge2$ についても、ファンアウト1で代入可能な言語が自動的に $(f,s)$-組代入可能になるわけではない。原稿の `thm:doubling-no-lift` は別の倍増族についての障害を与える。従って $F_n$ を成分ごとに置いた族のクラス所属・サイズ・型付き組合同性を独立に検証しない限り、今回の結果を $f\ge2$ の下界へ移すことはできない。

## 8. 前回の補題 3.1–3.2 に対する $H$ の補足（R4）

下側スタックを $\psi$、まだ消費していない $E_i$ から生じた上側部分を $\eta$ とし、実行中は $\psi$ 自体を変更しないとする。前回の不変量 $H(\eta)$ は、**上側部分 $\eta$ の記号だけ**について各 $E_j$ の右側にある記号数を数えたものである。$\eta$ に $\psi$ を連結した全スタックでは
\[
H(\eta\psi)=\max\{H(\eta)+|\psi|,\ H(\psi)\},
\tag{25}
\]
となる（$\eta$ に非終端がないときは $H(\eta)=-\infty$）。全スタックの最大値は $H(\psi)$ に支配される可能性があるため、**全体の $H$ が最初の $a$ の前後で減るとは主張しない**。しかし、$E_i\psi$ から $\psi$ に達する前の各遷移は $\eta$ の中だけで行われ、前回の帰納的計算がそのまま $H(\eta)$ に適用される。すなわち最初の $a$ より前は $H(\eta)=i$、その後は $H(\eta)<i$ であり、共通終状態 $\eta\psi$ に到達した二実行については上側部分が同じなので、その値を直接比較できる。これが前回の補題 3.1 を下側スタック $\psi$ の上で使用する正確な理由である。

## 9. 文献位置付け・最終判定

- **対象原稿：** Kuriyama, *Distributional Learning of Multiple Context-Free Languages under Fixed Finite-Semigroup Typing: Local Groups and the Length of Characteristic Data*, [GitHub 現行ソース](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/main.tex)。照合したのは `def:reconstruction`、`prop:reconstruction-soundness`、`thm:window-group-polydata`、`cor:trivial-exact`。
- **Clark–Eyraud (2007)：** *Polynomial Identification in the Limit of Substitutable Context-free Languages*, JMLR 8, 1725–1745。基本となる構文的合同・弱代入可能性の定義：[公開誌面](https://www.jmlr.org/papers/v8/clark07a.html)。
- **Yoshinaka (2008)：** *Identification in the Limit of $k,l$-Substitutable Context-Free Languages*, ICGI 2008, LNCS 5278, 266–279：[出版情報](https://doi.org/10.1007/978-3-540-88009-7_21)。
- 本報告の **ランク2化、到達可能スタック上の合同分類、遮蔽 Link の反例、全 $n$ の最上段印なし特徴標本、および重み不等式** が文献で既知かどうかは **未確認**。簡易文献検索でこれらの同じ主張は確認できなかったが、未掲載・新規性を立証するものではない。

### 最終結論

**R1 は、指定された (a)・(b) のどちらも未決着である。** ただし、(a) のための中心的な提案「段 $j$ の $A$-左節点を生成するには、標本中の真の構文木にもその節点が存在する」は、**具体的な2語の反例により偽**であり、さらに **全 $n\ge3$ について最上段の該当節点を全く観測しない特徴標本**を構成した。一方、印を実際に観測する方式に対する $\Omega(n^3)$ は、厳密な償却不等式として証明できた。

現時点で論文へ安全に導入できるのは **定理 2.1、定理 3.1、補題 3.2、定理 4.1、定理 5.1** およびその明示的な限定である。特に **(24) を B の無条件の三次下界と書くことは誤り**である。最短特徴標本長については依然として (1) の二次下界と三次上界の間にギャップが残る。

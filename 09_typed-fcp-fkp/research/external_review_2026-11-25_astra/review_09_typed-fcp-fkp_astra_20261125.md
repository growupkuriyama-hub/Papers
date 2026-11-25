# 投稿前査読　Frames versus Exemplars

**対象**　Takayuki Kuriyama、コミット `673064fe7c4eb474f679404d06bc1a52a88a4f22`、2026年11月25日。以下の単独の行番号はすべて [09 の main.tex](https://github.com/growupkuriyama-hub/Papers/blob/673064f/09_typed-fcp-fkp/main.tex) の1始まりの番号である。KY は Kanazawa–Yoshinaka。$D(x)$ は当該ターゲットでの分布、$\overline K=K^{\rhd\lhd}$、$c[x]=uxv$ と書く。

## 1. 総合判定と採択見込み

**Major revision 相当。** 定理4.4の指数下界は、任意のCFG、任意の有限核、任意の型付けという量化を含めて成立する。定理4.5の三つの番号付き結論も成立する。  
最大の訂正は比較表の $L_n$ 側である。削除前でも観測器を $s_U$ に固定すれば、初期記号の核だけで長さ $3\cdot2^n-2$ が必要になる。「削除すると初めて差が出る」という読みは誤りである。  
命題6.6の原典依存部分を検査した。さらに同じ証人で $s_0$-typed weak 2-FCP も構成できる。したがって §8 の最初の未解決問題には否定解がある。  
主定理の撤回は不要。比較の量化、weak FCP の結論・未解決問題、学習器固有の下界の表記を改めてから投稿するのが妥当である。

## 2. 判定表

重大度はその行について必要な修正の優先度である。CORRECT は表示された命題への判定で、周辺の解説にまで及ばない。

|主張|番号|判定|根拠（行番号）|重大度|
|---|---|---|---|---|
|積の共通文脈の不変性|補題3.2|CORRECT|298–308, 442–456|低|
|型付き学習器の必要十分方向|命題3.5|CORRECT|492–533。reset と安定化の補足は §4|低|
|同じ文法・同じ核での縮約|補題3.7|CORRECT|558–579|低|
|レベル付き部分木の同定|補題4.1|CORRECT|593–603, 606–621|低|
|削除前の型なし上界|命題4.2(a)|CORRECT|623–627, 639–644|低|
|削除後の型付き上界|命題4.2(b)|CORRECT|628–636, 646–650, 716–723|低|
|核捕獲|補題4.3|CORRECT|653–670|低|
|任意の文法に対する積の下界|定理4.4|CORRECT|672–700|低|
|分離の三つの結論|定理4.5（A）|CORRECT|702–724。削除前の (iii) は型なし|低|
|全標識を覆う構成素|命題4.6|CORRECT|726–743|低|
|再構成文法の SPP と数え上げ|補題5.1|MINOR GAP|767–787。空ターゲットで最大値未定義|低|
|正例の符号長の三乗下界|系5.2|CORRECT|790–809|低|
|primal のデータ量|系5.4|CORRECT|826–844|低|
|dual の反駁に必要な因子|命題5.5|CORRECT|846–879, 900–904|低|
|観測器に依存しない学習器|系5.7|CORRECT|913–953。空言語の提示規約は §4|低|
|言語クラスの包含・等式|定理6.1（B の包含部）|CORRECT|983–1019|低|
|文脈側の真包含|命題6.3|CORRECT|1045–1074|低|
|核側の真包含|命題6.4|CORRECT|1076–1119|低|
|型なし weak FCP からの非保存|命題6.6(a),(b)|CORRECT|1133–1204。独立の補証は §3|中|
|「any typing」で $L_n$ の核も線形|比較表5.6の核の行|ERROR|883–890 対 473–481, 596–604, 625–627|高|
|この証人に対する $s_0$ 側の構成は未解決|問題8.1・考察・結論|ERROR|1206–1210, 1264–1273, 1317–1319。下記に構成|高|

## 3. 重大な指摘

### 3.1　削除前の線形上界では観測器を選んでいる

**箇所と問題。** 82–86, 184–186, 883–899, 1308–1316。表5.6の “kernel side (any $k$, any typing)” を左列にも適用すると偽。定理4.2(a) の短い核 $u_i$ は、異なる型の語も同じカテゴリに置けることを利用している。

**反証。** $L_n$ に対して $s_U$ を固定する。$w_n^*$ を導出する初期記号 $A$ の型は $1$。typed kernel SPP には
$$
 w_n^*\in L(G,A)\subseteq X_A=\overline{K_A}\cap F_1
 \subseteq L_n\cap F_1=\{w_n^*\},\qquad K_A\subseteq X_A
$$
が必要である。有限言語 $L_n$ の最長文より長い左文脈を取れば、その文脈はすべての $x$ を拒否する。ゆえに $\overline\varnothing=\varnothing$。従って $K_A=\{w_n^*\}$、すなわち **$\kappa\ge3\cdot2^n-2$**。$k$ を増やしても、文法を取り替えてもこの結論は変わらない。一方 $L_n$ の $s_U$-typed strong 1-FCP は4.2(a)の文法を補題2.5で分割すれば線形のまま。この観測器のもとでは、削除前にも指数差がある。#1 の系6.6は同じ孤立ファイバーを typed thickness に用いており、こちらの核についての証明は上の短い議論で足りる。

**差し替え案。** “Before deletion, the untyped (and trivially typed) grammars admit both presentations with linear grammar size and linear maximum witness length. Deletion makes the kernel lower bound hold even without typing, and hence under every typing.” 表は次のように分ける。上界は文法サイズと最大証人長を**別々**に評価したもの。

|核表示の条件|$L_n$|$M_n$|
|---|---|---|
|型なし、または $s_0$|strong 1、両尺度 $O(n)$|定理4.4の積下界|
|$s_U$ 固定|初期核に $w_n^*$ が必須|同じ積下界|
|任意の型付けを許して最良のものを選ぶ|$s_0$ が線形上界を達成|同じ積下界|

### 3.2　weak FCP の typed-to-typed 非保存まで示せる

**箇所と問題。** 1206–1210, 1264–1273, 1317–1319。一般には $\overline{Y\setminus\{\lambda\}}$ が縮み得るという1266–1268の注意は正しい。しかしこの例で調べる必要がある nullable な弱い成分は二つだけである。以下で $G^+$ は1146行の文法、閉包は $L^+$ 相対。記号 $P=[ab\#]^*$、$Z=[ab]^*$ は正規言語を表す。

**補証のための事実。** KY2017 §5の $L_2$ は $v c^i d^i e^j z$、$L_3$ は $v c^i d^j e^j z$。$v=w y$ で $w\in Z,\ y\in(\# Z)^*$、$z\in Z$。$w$ の $a,b$ の個数にはそれぞれ $|w|_a\ge |w|_b$, $|w|_a\le |w|_b$ の制約がある。$L_4=P\,\$\,Zc^*\%f^*$、$L_5$ は $v c^i d^i e^j z c^k\% f^l$ で $j\ne k$。$i,j,k,l\ge0$。特に $P\subset L^+$。任意の $v\in P$ をその最初のブロックの大小で $L_2,L_3$ の一方に入れ、中央の指数と末尾を空にすればよい。

**鍵となる等式。** $Y=L_2$ または $L_3$ なら、
$$
 (Y\setminus\{\lambda\})^\rhd=Y^\rhd\quad\text{（$L^+$ 相対）}.
$$
右から左は反単調性。逆向きに、$(u,v)$ が全非空 yield を受理するとする。次の証人はいずれも先頭が $\#$、末尾が $a$、中央に $d$ を持つ。このため、完成語が通常枝 $L_2,L_3$ のいずれかにあるなら $u\in P, v\in Z$。$\$$ または $@$ の鏡映枝や $L_4$ にはこの中央の $d$ は置けない。$\%$ を含む完成語なら $L_5$ で、$\%$ は穴の右、$v=z c^k\%f^l$ にある。末尾の $a$ が中央と末尾の $c^k$ とを分け、$k$ は $v$ だけで決まる。

- $Y=L_2$ では各 $t\ge0$ に対して $\#cd e^t a\in Y$。$\%$ 付き文脈なら $t=k$ を選ぶと $L_5$ の $j\ne k$ に反する。ここでは $u$ が最初の $\#$ の前に来るので、$u$ によって中央の $e$ 数をずらせない。
- $Y=L_3$ では $\#c d^2 e^2 a\in Y$。中央で $c,d$ の個数が異なるので、$L_5$ に入らない。

従って両方の場合で $u\in P,v\in Z$、したがって $u\lambda v\in P\subset L^+$。空語も受理されて等式が従う。

**型付き文法の構成。** 補題2.5を $G^+,s_0$ に適用し、無用コピーを除く。各 $(A,0)$ の言語は $Y_A\setminus\{\lambda\}$、各 $(A,\mathbf1_\sharp)$ は $\{\lambda\}$。空語専用コピーは到達文脈一つ（空文脈集合でもよい）で strong に特徴づけられる。非空コピーは次で尽きる。

1. $Q,F,H,E,C,J,T,U,S_{4,5}$ の元の yield は下記3.3の有限文脈で **strong** に表されるので、$\Sigma^+$ との交差がそのまま strong な特徴づけである。
2. $S_1$ はすべての yield に $\$$ または $@$ があり、元から非 nullable。yield 集合は同じであり、既存の弱い二文脈を $\Sigma^+$ に制限すればよい。
3. $S_2,S_3$ は上の等式により、非空部分の**通常閉包**が元の通常閉包と一致する。その後に $\Sigma^+$ と交差すれば、二つの旧文脈が typed weak 2-FCP を与える。

これで $L^+\in\mathrm{FCP}_{\rm w}^{2}[s_0]$。命題6.6(b)の $L^+\notin\bigcup_k\mathrm{FCP}_{\rm w}^k[h_{\{@\}}]$ および $s_0\preceq h_{\{@\}}$ と合わせ、問題8.1への反例となる。$k=2$ で普遍的包含を反証し、同じ証人は全 $k\ge2$ にも使える。$k=1$ の判定はこの議論からは出ない。

**具体的な改稿。** 6.6(a) に $s_0$ 版を加え、上の等式を補題にする。§8.1 は $k=1$ の問題に絞れる。Abstract 末尾は “Weak FCP can fail even under refinement from the trivial typing to a two-element indicator.” とすれば、証明との対応が明瞭になる。

### 3.3　6.6(a) の引用に埋もれた弱い特徴づけの検算

ここは査読の結果、命題の反例には至らなかった。追試可能にするには、1146–1184 に次の表か短い付録を置きたい。$L_0=L_1\cup L_2\cup L_3$, $L'=L_0\cup L_4\cup L_5$ とし、$J_0=P\{c^id^ie^i:i\ge0\}Z$ と置く。下表の積は言語の連接。$B=\{w\in Z:|w|_a=|w|_b\}$。$L_1^@$ は $L_1$ の区切りを置換したもの。

|非終端|診断用の文脈集合|$L^+$ で文脈が定める集合|特徴づけ|
|---|---|---|---|
|$Q$|$(\lambda,\#cd),(a,b\#de)$|$B$|strong|
|$F$|$(\lambda,cd),(\lambda,ade)$|$B\#P$|strong|
|$H,E$|順に $(a\#c,d)$, $(a\#cd,e)$|順に $\{c^id^i\}$, $e^*$|strong|
|$C,J$|順に $(b\#c,de)$, $(b\#d,e)$|順に $c^*$, $\{d^ie^i\}$|strong|
|$T,U$|順に $(\$,a\%)$, $(e,c\%)$|順に $Z$, $\{e^j zc^k:z\in Z,\ j\ne k\}$|strong|
|$S_{4,5}$|$(\lambda,f)$|$L_4\cup L_5$|strong|
|$S_2,S_3$|順に $\{(\lambda,\lambda),(a\#,b)\}$, $\{(\lambda,\lambda),(b\#,a)\}$|順に $L_2\cup J_0$, $L_3\cup J_0$|weak|
|$S_1$|$(a\#,a),(b\#,b)$|$L_1\cup L_1^@\cup J_0$|weak|

**段階1、旧診断の正確さ。** $Q$ の第一診断では先頭ブロックが非負差、第二では非正差になる。穴に $\#$ が既にあると第二では $a$ が先頭差を1増やし、両方は成立しない。$\#$ がなければ付加した $a,b$ が相殺して差0である。$F$ の二診断では、穴に $\#$ がなければ第二の $a$ が差を1だけ増やして不可能。あれば最初のブロックがちょうど差0。両診断の固定末尾 $cd,de$ の形が中央に余分な文字を許さない。$H,E$ は先頭 $a\#$ で $L_2$ の等数条件、$C,J$ は $b\#$ で $L_3$ の等数条件を強制し、残りの終端を左右から消去すれば表の言語になる。これらの診断は穴に $\%$ があれば末尾が $f^*$ になれず、$@$ があれば $c,d,e$ と共存できずに拒否する。強い特徴づけでは、生成言語 $Y=C^\lhd$ が分かれば $\overline Y=Y$ が直ちに従う。

**段階2、新しい三記号。** $\$xa\%$ は $L_4$ で、末尾の $a$ が $x$ に $c$ が入る可能性を消す。$exc\%$ は $L_5$ で中央の $i=0$、前後に加えた $e,c$ が指数を各1増やすので比較 $j\ne k$ が残る。$xf$ は $L_4,L_5$ の末尾の $f$ を一つ取り除ける場合に限る。それぞれ KY Lemma 12 の $T,U,S_{4,5}$ の規則がちょうどこの集合を生成する。とくに $U\to eUc$ は両指数を増やし、$EeT$ と $TcC$ が過剰分の両符号を実現する。

**段階3、旧 $S_2,S_3$ の「弱さ」。** $L_0$ から $L'$ へ移る際に診断集合の外延が変わらないことだけでは不十分である。全共通文脈による閉包も調べる。3.2 の証人を使うと、$S_2,S_3$ の全 yield を受ける共通文脈には $\%$ も $@$ も入らず $u\in P,v\in Z$。従って、旧 yield への共通文脈は $L_0$ のときと同じである。全共通文脈は $J_0$ を受ける。実際どの先頭差でも、等数の中央 $c^id^ie^i$ は該当する枝に入る。逆に、空文脈と $(a\#,b)$ の二診断は候補を $L_2\cup J_0$ に絞る。後者の診断で中央は $c,d$ 等数、空文脈により候補が $L_3\setminus L_2$ から来る場合にはさらに $d,e$ 等数が必要。$\$$/$@$ は鏡映の端 $a,b$ が合わず、$\%$ は末尾 $b$ で排除される。$S_3$ は先頭差と $c,d$／$d,e$ を交換する。これで KY Lemma 12 の証明中の旧非終端に関する省略を埋められる。

**段階4、$S_1$。** $L_1^@$ のすべてを受ける文脈は、特に $@$ 単独を受けるので $(v,\mathrm{erase}_\#(v)^R)$ に限られ、逆にその全てが鏡映を保存する。この集合 $M$ は $L_1$ も受けるから、和 $L_1\cup L_1^@$ の分布はちょうど $M$。$M$ の全要素は $J_0$ も受ける。$(a\#,a),(b\#,b)\in M$ を同時に通る通常枝の中央は三指数が等しく、鏡映枝では左右の文字を消せば元の鏡映条件が残る。$\%$ は末尾 $a,b$ で排除される。よって表の $S_1$ の外延と閉包が等しい。$@$ を生成する追加規則が他の非終端の yield を変えないのは、$S_1$ が自分の規則以外の右辺にないためである。

## 4. 中・低の指摘と証明の逐項監査

以下では、同じ包含を引用して済ませず、各段で必要な仮定を示す。CFG は通常の順序付き導出木を持ち、右辺の長さ $\rho$ は終端を含む記号数、学習器の $r$ は右辺の**非終端**の個数である。

### 閉包と学習器

- **3.2（442–456）。** 前提は同一の $L$ による閉包、$X_i\subseteq Y_i\subseteq\overline{X_i}$、終端片 $w_i$ の固定。$P_X\subseteq P_Y$ から $P_Y^\rhd\subseteq P_X^\rhd$。2.1 の積包含は、一つずつ同じ外側文脈に代入することで得られ、終端片には $w\in\overline{\{w\}}$ を使う。ゆえに $P_Y\subseteq\overline{P_X}$、極を取ると逆包含。空の $X_i$ についても全称量化は有効。$n=0$ は恒等式。型付きの場合は extensivity とファイバーへの交差だけを使う。
- **3.7（558–579）。** 規則ごとに生の核、型付き閉包、通常閉包の積を比較し、3.2 から三者の右極が等しい。左辺の型と右辺の積の型が等しいので、型付き積に対しては左辺のファイバー条件が自動的に成り立つ。この段で文法の型整合性と子核の均質性を両方使う。残る条件は三者に共通の $K_A^\rhd\subseteq P_0^\rhd$。各初期 $S$ について soundness の上側は $K_S\subseteq L$ と同値（空文脈、閉包の拡大性）。下側は最小前不動点性。規則妥当性と初期条件を別々に示しているので、多重初期記号、空核、共通文脈が空の核も含む。文法の yield をファイバーに入れるだけで規則の型整合性を落とす改変にはこの証明を使えない。
- **3.5（492–533）。** 前提は固定有限型付け、正整数 $r,k$、全ターゲット語が現れる正例列、正確な所属オラクル、KY Algorithms 1,2 の reset・候補・初期記号規則。dual は $J,H$ を reset 時に、$E=\mathrm{Sub}(D)$ を毎回更新する。primal は $E,H$ を reset 時に、$J=\mathrm{Con}(D)$ を毎回更新する。primal の初期条件は $K\subseteq L_*$。型を調べる費用は有限表の積で済む。3.7 の規則同値は真のターゲット相対のテストにも使える（規則部分に $L=L(G)$ は不要）。非空の文脈集合の外延は $\mathrm{Sub}(L_*)$ に含まれる。非空核の反駁文脈も $\mathrm{Con}(L_*)$ に属する。従って安定出力に無効な規則・初期記号は残らず、SPP は過生成を防ぐ。過少生成が永久に続けば、欠けた正例の到来後に reset される。reset 直後は各既見語 $d$ を直接生成する候補がある（dual は空文脈の singleton と $\widehat s(d)$、primal は $\{d\}$）。ゆえに安定出力は全ターゲット語を生成する。
- **3.5 の逆方向の補足案（515–527）。** trim 後の $A$ には yield $x$ と到達文脈 $c$ がある。空核なら $x\in\operatorname{cl}(\varnothing)$ なので $\operatorname{cl}(\{x\})=\operatorname{cl}(\varnothing)$。空診断集合なら到達文脈がファイバー全体を受ける。各非空核の全要素は $c$ に入るので観測可能、各診断文脈は $x$ を受けるので観測可能。各規則の終端タプルもその規則を使った完成導出から観測できる。有限個のこれらを含む標本の後に reset があれば、証人を添えた目標文法の像は全テストを通り続ける。以後 reset はない。もしその標本以降に reset が一度もなければ、もともと候補プールは固定されている。いずれも有限プールからの削除だけになり安定する。この場合分けを一文加えると「次の reset が存在する」との暗黙の仮定を避けられる。

### 括弧族の上界・捕獲・下界

- **4.1（606–621）。** 文字 $a$ は唯一の葉。二種類の開閉括弧が一意対応し、各対は一つの規則に由来する。$j>0$ のレベル $j$ 語は全体が一つの対で包まれ、真の非空接頭辞の深さは正。既存の語に現れたときの最初の開きに対応する閉じもその出現の末尾である。部分木の根から葉までの対の数が一定 $j$ なのでレベルを同定できる。同じ非終端の別の導出で部分木を置換すれば元の文法が受理する。任意の「平衡断片」が一つの節点だとは仮定していない。
- **4.2(a)（625–627, 639–644）。** 外側の天井対を $n-i$ 回消去すれば文脈の外延は $E_i$ の全 yield。$u_i$ はその中にあり、$u_i$ の任意の出現を4.1で別の $E_i$ 語に置換できる。よって $L(E_i)\subseteq\overline{\{u_i\}}$。先の外側文脈も $u_i$ の文脈なので逆包含。$i=0$ は葉、$i=n$ は空文脈。別の開始記号 $S_0$ にも $E_n$ の証人を流用する。$|u_i|=2i+1$、文脈長 $2(n-i)$。
- **4.2(b)（628–650）。** 型 $1$ は天井無しの一語だけ、型 $\zeta$ は残り。初期レベル0は $a$。床規則は子の型の論理和、天井規則は子の型にかかわらず $\zeta$ を返す。高さ帰納法で全語を過不足なく得る。$i<n$ の外側文脈には既に天井があるため $M_n$ と $L_n$ の受理が一致する。根では $M_n\subset F_\zeta$。初期記号の型 $1$ コピーも葉の $\zeta$ コピーも不要。型1の規則 $n$ 本、レベル1の標識規則1本、残り $5(n-1)$ 本で $6n-4$。非終端は $n+n$ 個、床右辺は4記号。文脈を全行に文字通り載せる符号化の総長は $O(n^2)$。
- **4.3（653–670）。** $n\ge2$ により右部分 $u_{n-1}$ は標識付き。出現を固定して $z=pxq$ とすると、実際の導出から $(p,q)$ は $B$ の到達文脈。2.2 と拡大性からすべての $k\in K_B$ に対して $pkq\in M_n$。$x$ の**出現位置**が接頭部内なので長さが変わっても $q$ の中の $u_{n-1}$ は壊れない。各 $pkq$ に4.1を適用して、その特定の出現を $w^*_{n-1}$ に替えると $pkq'\in L_n$。そこから消した語はただ一つで、$pkq'=pxq'$ は自由モノイドの左右消去により $k=x$ と同値。最後に $x\in\overline{K_B}$ と $(p,q')\notin D(x)$ から $(p,q')\notin K_B^\rhd$。従って拒否される核語が実在し、それは $x$。ここで量化しているのは元の到達文脈で受理される差替語である。任意の文字列 $k\ne x$ まで受理すると言い換えてはいけない。空 yield を切れ目とみなしても同じ消去が通る。
- **4.4（672–700）。** (1) $z$ の全導出木にわたり節点数を最小化する。$M_n$ は有限、$z\in M_n$ なので存在する。(2) 同一ラベル $A$ が祖先・子孫に反復すれば、側枝の終端化を固定して $A\Rightarrow^*\alpha A\beta$。$|\alpha\beta|>0$ なら反復ごとに長さが増え無限言語となる。ゼロなら下側の部分木を上に接ぎ同じ $z$ の木を小さくできる。従ってこの木の各道には高々 $|N|$ 個の非終端しかない。全導出木で反復がないとは言っていない。(3) 子の非空 yield 区間は互いに素で順序通り。隣接位置 $r,r+1$ をともに持つ子は高々一つ。祖先は全て両位置を持つから、境界節点は根からの道をなす。空 yield は両位置を持てない。(4) 各左側位置の担当を、それを含む最深の境界節点の右辺スロットに定める。そのスロットは単一終端か、右端が $r$ 以下の子。複数位置が同一スロットに属しても一断片と数える。従って高々 $\rho|N|$ 断片で左側を覆う。(5) 非空の子断片は4.3で核語、終端は長さ1。$\kappa=0$ でも終端で覆え、評価は $\max(\kappa,1)$。実際このターゲットでは全初期核が空または空語だけという場合は不可能。有限言語なので $\overline\varnothing=\varnothing$、かつ初期核は $M_n$ に含まれ、$M_n$ は非空で空語を含まない。全核の和は非空で、676行の最大値は定義される。(6) $r=1+(3\cdot2^{n-1}-2)$。型付きは3.7により同じ木・同じ記号数・同じ核で従う。
- **4.5（702–724）。** (i) は上記の列挙。(ii) は4.4であり、有限核・有限 $\kappa$ を前提に読む。(iii) は4.2(a)であり、4.5のどの段にも「任意の型付けで $L_n$ の核が短い」とは書かれていない。積の指数下界から三尺度の最大には少なくとも立方根の下界がある。個別に全尺度が指数的、または核の**個数**が指数的という結論は出ない。
- **4.6（726–743）。** 前提は型なしの文脈 SPP、全 $c$ に $|c|\le\ell$、節点 yield が特定の天井節点全体を包含すること。置換後 $px'q=w_n^*$ なので到達文脈健全性から $x'\notin C_A^\lhd$。一方 $x\in C_A^\lhd$、従って識別する $c$ が存在。$c[x]$ 内の $v$ は4.1の節点であり、$c[x']\in L_n$ かつ $\notin M_n$。従って $c[x']=w_n^*$。$|w_j^*|-|v|=|w_{j-1}^*|$ を代入すれば主張。$v$ の片括弧のみを含む節点、型で $x'$ を排除できる場合には拡張できない。

### 三種の学習器

- **5.1（753–788）。** 前提は非空因子に対する固定 $s$、$K\subseteq L$、同型・共通文脈から分布一致が従うこと、$\lambda\notin L$、正確な再構成。開始記号は右辺に現れず、空語の開始規則もない。元の導出は初手で標本語の記号に移るので、多重初期記号に置き換えて全く同じ言語を得る。(B) は2.1、(L) は拡大性、(U) は $D_K(x)\subseteq D_L(x)$ および $D_L(y)$ についての同じ包含から共通文脈を持ち、$D_L(x)=D_L(y)$ となる。単元規則の向きに必要な包含を等号が与える。初期の singleton 核は空文脈を受けるので閉包は $L$ 内、逆は最小前不動点性と正確再構成。$\|K\|=\sum_{w\in K}(|w|+1)$ なら $2|N|\le\sum |w|(|w|+1)\le(\sum(|w|+1))^2$。正確性の仮定はとくに $L(G_K)=L$ のために要る。**修正**　$K=L=\varnothing$ も768行の仮定を満たし得るのに、774行の最大値と無規則文法の $\rho$ が未定義。冒頭を “Let $L$ be nonempty …” とし、標本ノルムをここで初定義する。5.2に影響しない。
- **5.2（790–809）。** $M_n\ne\varnothing$、$s$ は $M_n\in\mathcal C_s^{\rm cf}$ を満たすものに量化。$s_U$ なら #1 Prop.6.4(iv)、その細分なら同型条件がより強くなる。5.1 から $\rho\le2$, $|N|\le\|K\|^2/2$, $\max(\kappa,1)\le\|K\|$ を4.4に代入する。特性標本は自分自身を有限の拡大標本に選べる。下界は指定の再構成演算子についてのもの。全正例学習器についての情報論的下界ではない。
- **5.4（826–844）。** 安定する**文法そのもの**が KY Thm.4／3.5 の SPP を持つ。型付きならまず3.7で通常の SPP にする。核は reset 時点に取得済みの非空な $k$ 個以下の部分文字列集合で、後の $D_i$ の因子でもある。$m=|\mathrm{Sub}(D_i)|\ge1$ に対し、各集合を整列後、末尾を繰り返す長さ $k$ の列に単射にできるので個数は $m^k$ 以下。非空核は一意の型に属し、型数の余分な乗数はない。空語因子込みで $m\le\|D_i\|^2$。最大右辺長は $r+(r+1)\|D_i\|$。4.4に代入して $(2r+1)\|D_i\|^{2k+2}$。$r,k$ 固定と明記するのは不可欠（同じ条件を205–206,1246–1250にも足す）。データ量は文字数に区切りを加えたもの。問合せ回数・異なる例の個数・経過時間に同じ下界は主張できない。
- **5.5（846–879）。** $n\ge2,r\ge2,k\ge1$、全候補を保つ Algorithm 1、極限文法への**構文的**安定が必要。最後の reset の $D_t$ は非空。そこから一語を選ぶ。根が天井なら空所の両側に天井一対、根が床なら標識付きの子を固定し他方を空所にする。どの $c$ も $J_t$ に属し外延は $E_{n-1}$。床の場合、固定した子の出現は4.1によりレベル $n-1$、根の直下なので逆包含も成立。極限文法は床を含む語を出すため、候補の終端片に床が要り、$D_t$ の語に床開きと後続の閉じがある。従って $(\lfloor,\lambda,\rfloor)\in H_t$（KY のタプルは間に部分文字列を挟んでよい）。空文脈も $J_t$ に属する。型なし規則の不正な組は唯一 $(w^*_{n-1},w^*_{n-1})$。型付き規則は型 $1\zeta=\zeta$ を満たすが、真の右辺には高さ $n$ の語があり、左辺外延の高さは $n-1$。これを落とすテストには型1の子が必要で、その唯一の値は $w^*_{n-1}$。安定時点に無効な候補が残ると KY Thm.3 と矛盾する。非連結・非生産に見える候補も除去してから出力する別実装には適用できない。
- **5.7（913–953）。** 二分化してから型積を取り、到達かつ生産的なコピーだけ残す。階数は2以下。各記号の一 yield $w$ と到達文脈 $c$ を取る。同じファイバーで $c$ を共有する語は分布が等しい。新単位のファイバーなら両方空語。逆に $D(x)\supseteq D(w)$ なら $c$ を共有するから、typed singleton 核閉包と一文脈の外延は等しい。規則の子の代表 yield をつないだ語は親の yield であり、親代表と同型・同分布。3.2 と型付きガロア接続が規則の包含を与える。初期記号は空文脈で健全。(ii) は3.7と KY Prop.10 の終端語規則追加（終端長が増えても**階数**は増えない）、(iii) は KY Thm.6。$L=\varnothing$ は $I=N=\varnothing$ で表示可能。実語のみの無限正例列は空言語に対して存在しないので、識別を非空言語に関して述べるか、#1 §2のように休止記号と空文法の規約を添えるのが明瞭。

### 細分化と分離

- **6.1（983–1019）。** (a) 弱い成分は3.3により SPP。逆に3.7で通常 SPP に移し、各核語を終端右辺として足す。新しい文法は同じ SPP の下にあり初期言語を変えず、各記号は核語を含むのでその yield の通常閉包は元の核閉包と一致。追加規則は核の均質性により型整合的。ファイバーとの交差で weak を得る。これは**ある文法が存在する言語クラス**の等式である。(b) $s=\pi h$ と同一文法での3.7を二度使う。核の均質性は粗い側にも残る。型を忘れれば通常の weak=very weak が使える。(c) 細分文法の $(A,\nu)$ に $X_A\cap F_\nu^h$ を与える。右辺積は元の $X_A$ と積の型の両方に入り、初期成分はファイバーごとの和で元に戻る。strong なら実 yield がこの交差と一致する（2.5）。weak のために必要な「交差と閉包の可換性」はこの証明にはない。strong FKP の反単調性も示していない。
- **6.3（1045–1074）。** 正方向は二つの初期記号に $c$ の有無を割り当てる既存文法。空文脈一個の外延を各ファイバーに切れば正確な yield。負方向は十分長い $a^pcb^{2p}$ の導出のポンプ。反復は $c$ を含めず、増分が片側だけなら比 $1:2$ を維持できない。ゆえに $i>0$, $j=2i$。$E$ の特定の yield を受ける有限文脈は $(a^{t-i_2},b^{2t-j_2})$。全ての $t$ に対し $m\ge2t$ と選ぶと $a^{3m}db^{2m}$ を受ける（左の総数が右の一倍以上二倍以下）。この語は非空なので $s_0$ も捨てられない。到達ポンプを繰り返すと右の増加 $2i$ が左の $i$ を追い越し矛盾。空の診断集合の場合も任意に大きい $m$ を取れる。
- **6.4（1076–1119）。** $S_+$ の二つの基底は $a,z$、再帰は左に $a$ 単独、または左右に $a,b$。従って非標識の正差全体、標識 $z$ の非負差全体を生成する。$S_-$ は対称。$D(z)$ は $p-q\ge0$ の外枠 $(a^p,b^q)$。空文脈でまず $L_K$ 内に絞り、負差の非標識語は差を相殺して拒否、$y$ 入りは十分大きな正差で拒否する。$y$ 側も対称。空語はいずれにもないので $s_0$ に制限しても strong。細分後に非標識語を出す初期記号の核はすべて $P=\{a^mb^n:m\ne n\}$ 内にある。全核が有限ゆえ絶対差の一様上界 $p$ があり、空核は何も覆わない。$|i-j|>p$ の枠は全核語を受理するが、差 $j-i$ の語を拒否する。特に $a^{p+1}$ がどの初期成分にも入らず矛盾。ここでいう $P$ は §3.2 の略記とは別の、命題6.4自身の記号である。
- **6.6(b)（1186–1204）。** $\zeta$ が吸収元なので、非標識・空語の親は標識付きの子や終端 $@$ を持てない。$\zeta$ 記号と関係規則を除けば他の yield は同じで、初期和は $L'$。KY Lemma 13 の証明を任意のこの文法に適用できる。Lemma 7 の木上のポンプを継承して $a^m\$a^l$ を出す $B$ と異なる先頭差の到達文脈を得る。末尾側の非空文字と二通りの差で $B$ の yield は $[ab\#]^*\,\$\,[ab]^*$ または $[ab\#]^* c^i d^i e^i [ab]^*$ の形に制約される。後者の指数が非有界なら、正則言語との交差と外側文字を消す準同型により $\{c^id^ie^i\}$ の無限部分言語が CFL になり、ポンプ補題に反する。従って上界 $k_1$ がある。全分布は任意の $i>k_1$ で $(\lambda,c^i\%)$ を含み、三重等数の大きい語を閉包から排除する。一方、有限 $W$ は $\%$ 前の $c$ 指数を有限個しか試せず、十分大きい $c^id^ie^i$ が全て通る（$\%$ 無しなら等数の両枝、$\%$ 有りなら $L_5$ の不等号）。$B$ は非空の $\$$-語を出すため型1で、$L^+$ における共通文脈に $@$ は入り得ない。$F_1=\Sigma_0^+$ 内では上の反証語を失わない。仮に有限 $C$ があれば yield 自身が $C^\lhd$ 内なので $C\subseteq L(G,B)^\rhd$、これを $W$ に取って矛盾。**注意**　著者版 KY p.11 の反証語は裸の $c^id^ie^i$。p.8–9 の Lemma 7 の囲い付きの語と区別した本稿1195–1197は正しい。

### 引用・計算・表現で直す箇所

|問題と箇所|なぜ問題か|具体的修正|
|---|---|---|
|Clark–Eyraud との同一視、406–410（中）|原著 Defs.4,5 は比較する二語から空語を除いていない。#1 自身はこの違いを明記する。$L=a^+$ は非空語が全て同分布なので $s_0$ 版を満たすが、$\lambda,a$ は $(a,\lambda)$ を共有し、空文脈では異なる。|“For $s=s_0$ this is the nonempty-fragment variant of Clark and Eyraud’s substitutability used in [#1].”|
|検証の型が本文と違う、593–604, 761–763、公開 deletion script 46–49, 134–145（中）|閉じ天井だけを含む因子を unmarked としている。計算した単元規則集合が違う。|開閉いずれかを検出するよう直す。修正後の実測と長さ切断の扱いは §5。|
|Abstract 88–91、1236–1243、1308–1319（中）|strong/vw FCP と vw=weak FKP の包含の方向自体は適切。Abstract の weak 非保存の出発点は現行の6.6だけからは型なし。結論冒頭の一般論は strong FKP や収束速度まで含むように読める。|3.2 の強化前なら “adding an observer to an untyped grammar need not preserve weak FCP”；採用後は3.2の英文へ。strong FKP は未解決と添え、B の冒頭にも strong FCP の包含（989行）を書く。|
|有限表示という包括的表現、71–76, 109–115（低）|一般の閉集合が有限生成または有限個の診断で特徴付けられるとは限らない。very weak では名指される集合が実際の yield より大きくてもよい。|“We compare two ways in which a grammar category may admit a finite description.” とし、SPP が近似する対象を1文で説明する。|
|認可条件・負のテスト、165–170, 1224–1236（中）|標識付きの子一つは受理に十分である。逆に標識なしの子一つでは全体の不受理は決まらない。FCP の文脈は全て正のテスト。4.3 は特定の $z,R$ の節点についての結論。|“An unmarked constituent can occur in both licensed and unlicensed completions.” とする。型なし同下界は4.6からは出ない。|
|パラメータと学習の単位、158–161, 195–208, 896–904（低）|文法サイズ、最大証人長、全証人の記述長、例の個数は異なる。|5.4は固定 $r,k$、5.5は $r\ge2,k\ge1$、全候補による安定出力段階の正例長、と序論にも明示する。|

## 5. 反例探索・コード・実行結果

**環境と版。** Linux x86_64、CPython 3.12.14、標準ライブラリ。対象 TeX の SHA-256 は `2dcc587c767ce9b4693bf37845d247e933e49562a591cd24496343b34ad793df`、PDF は `d0e3632242449951091f5e8bf903df7dd9249226102a7e4d88477f3badce805d`。以下の `sources/` は指定コミットから保存した入力用ディレクトリ。各コードブロックは記載した名前で同じ作業ディレクトリに保存すれば再実行できる。

**著者の三本。** 次を実行し、終了コードはいずれも0。引用元は[削除族](https://github.com/growupkuriyama-hub/Papers/blob/673064f/09_typed-fcp-fkp/tools/check_deletion_family.py)、[縮約](https://github.com/growupkuriyama-hub/Papers/blob/673064f/09_typed-fcp-fkp/tools/check_reduction_identity.py)、[一致の例](https://github.com/growupkuriyama-hub/Papers/blob/673064f/09_typed-fcp-fkp/tools/check_toy_example.py)。

```console
$ python3 -I sources/check_deletion_family.py 4
  (E) n=2: factors=100, U-pairs checked=15, Rec(M_n) generates M_n: True
n=2: |L_n|=6, |w*|=10, capture pairs tested=17, all checks passed
  (E) n=3: factors=1991, U-pairs checked=1732, Rec(M_n) generates M_n: True
n=3: |L_n|=42, |w*|=22, capture pairs tested=108, all checks passed
n=4: |L_n|=1806, |w*|=46, capture pairs tested=1204, all checks passed
```

```console
$ python3 -I sources/check_reduction_identity.py 4000 20261123
{'ident_ok': 4000, 'ident_bad': 0, 'rule_ok': 2230, 'rule_bad': 0, 'skipped': 0}
```

```console
$ python3 -I sources/check_toy_example.py
frame (_,barks): [('John',), ('the', 'dog')]
kernel {John}: [('John',), ('the', 'dog')]
frame (John saw,_): [('John',), ('the', 'dog'), ('the', 'dogs')]
kernel {the dog,the dogs}: [('John',), ('the', 'dog'), ('the', 'dogs')]
kernel {the dogs}: [('the', 'dogs')]  frame (_,bark): [('the', 'dogs')]
S: kernel {John barks}: True  frame (.,.): True
typed: (John saw,_) cap sg-fibre: [('John',), ('the', 'dog')]
kernel {John} closure contains a plural word? False
any single NP word with closure = NP? []
```

**何を検証したか。**

- deletion の (A) は $n=2,3,4$ で有限言語の該当する両閉包を正確に計算する。(B) は $E_i$ の外延の分割を調べ、$H_n$ の規則集合自体は生成しない。(C) は110行の範囲が $b>a$ で、空 yield を除くすべての区間で差替命題を検査。(D) は121行の三つの文脈のみで、標識付きの兄弟を全て動かしてはいない。(E) は $K=M_n$, $n=2,3$ のみ。139行以降の “U-pairs” は各同型・同文脈グループの代表との比較回数であり、異なる単元規則の総数ではない。分布の等号は推移的なのでこの圧縮自体はよい。閉じ天井単独の型が本文と逆で、(E) の因子には実際にこの入力がある。修正前後で比較数は $15\to20$, $1732\to1967$。145,165行では最長正例で打ち切るため、生成語集合についての表示単独では上限を超える過生成を排除できない。正しい型で (U) の分布一致と到達文脈を別証し、(B),(L) の SPP と併用すればこの懸念は消える。
- reduction は4000の試行であって、各言語に5種類すべてを適用する設計ではない。子数1または2、非空核、非空語、共通文脈あり。規則判定まで実施したのは2230件。105–112行の適格な左辺なし等で返る None は出力の skipped に加算されない。skipped=0 から全試行で規則同値まで検査したとは言えない。初期記号の健全性も元スクリプトの対象外。
- toy は12文を生成して比較値を表示するが assertion はない。14行では空語を候補から除く。例で使う各診断文脈（核なら一つの共通文脈）が空語を拒否するので、報告された名詞句の等式は全語上でも正しい。単一核で $NP$ を得るなら拡大性から核語自身が $NP$ にあるため、30行の3候補で尽くす。

**独立検査の設計と限界。**

|検査|母集団・評価方法|結果の意味|
|---|---|---|
|3.2, 3.7, 6.1 の核側|二文字、長さ2以下の7語の全128部分言語、ラベル付き二元半群の全8乗法表。各文字に別の元を与える。語を長さ2まで正確に保持し、超過後は型だけ記憶する有限商。全左右文脈を商上で厳密評価。階数0,1,2 の右辺は固定 seed で抽出し、左核・初期条件は全列挙。|空核、空語、非可換の左零・右零半群、群、閉包が全集合のケースを含む。規則・初期条件の不一致0。3.2の一般の挟み集合については §4 の証明と著者の積検査を併用。|
|4.1–4.6、5.1–5.5|$n=2,3,4$ の $H_n$ を規則から生成。全標識付き兄弟、空区間を含む捕獲位置。$n=2,3$ の単一天井の全該当位置・全包含区間の識別文脈。$n=2$ の $M_n$ の全32標本について正しい $s_U$ で長さ打切りなしの再構成。順序付き二分木は葉2–8の全形・全内部境界。|核捕獲の差替え、規則数、反駁ファイバー、4.6の長さ等式を再現。$n=2$ で正確な再構成をする標本は全標本自身のみ、符号長42。4.4の全CFG量化を木の列挙で代用していない。|
|3.5, 5.7、6.3, 6.4|階数・核数1の KY 両学習器、二種の型、3つの有限言語、各2順序。出力文法の membership を長さ4まで比較。$L_K$ の二つの singleton 核に $m,n\le9$, 外枠の指数 $\le11$、絶対差証人も検査。6.3の増分の算術、$s_U\times C_2$ の細ファイバーを別途検査。|安定化の無限時間検定や全言語での学習可能性の証明ではない。5.4については小さい値で下界が弱いため、主検査は §4 の counting。|
|6.6 と問題8.1|正規形から $L^+$ の厳密 membership 述語を実装。10文字アルファベットで長さ5以下の全111,111語と全12行の診断集合を照合。左右長各2以下の全12,321文脈を $S_2,S_3$ それぞれに照合。$L_5$ は末尾 $c$ の切り方を全て試す。|各診断の外延について不一致0。有限文脈で無限集合の右極を計算したわけではない。未解決問題への否定解は §3.2 の全称証明による。|

### 半群と規則妥当性

`audit_types.py`

```python
from itertools import product
from functools import reduce
from random import Random
rng=Random(673064)
words=['','a','b','aa','ab','ba','bb']
pairs=rules=initials=empty=top=0
for tab in product(range(2),repeat=4):
    def op(x,y):
        if x==2:return y
        if y==2:return x
        return tab[2*x+y]
    if any(op(op(x,y),z)!=op(x,op(y,z)) for x,y,z in product(range(2),repeat=3)):
        continue
    pairs+=1
    T=lambda w: reduce(op,(int(c=='b') for c in w),2)
    # Finite quotient: precise word through length 2, then overflow with its type.
    elements=[(w,T(w)) for w in words]+[(None,t) for t in {T(''.join(w))
        for n in (3,4,5) for w in product('ab',repeat=n)}]
    # Verify that this is the full generated quotient.
    def mul(x,y):
        w,t=x;v,u=y
        return ((w+v) if w is not None and v is not None and len(w+v)<=2 else None,op(t,u))
    assert all(mul(x,y) in elements for x,y in product(elements,repeat=2))
    allq=frozenset(range(len(elements)))
    mult=[[elements.index(mul(x,y)) for y in elements] for x in elements]
    fib={t:frozenset(i for i,x in enumerate(elements) if x[1]==t) for t in range(3)}
    kernels={t:[frozenset(i for b,i in enumerate(sorted(F)) if m>>b&1)
                for m in range(2**len(F))] for t,F in fib.items()}
    for m in range(128):
        L={i for i in range(7) if m>>i&1}
        contexts=[frozenset(x for x in allq if mult[mult[u][x]][v] in L)
                  for u,v in product(allq,repeat=2)]
        def closure(K):
            return frozenset.intersection(allq,*(c for c in contexts if K<=c))
        cl={K:closure(K) for fam in kernels.values() for K in fam}
        for t,fam in kernels.items():
            for K in fam:
                assert (cl[K]<=L)==((cl[K]&fib[t])<=L)==(K<=L)
                initials+=1
        for rank in (0,1,2):
            for _ in range(24):
                ks=[];fs=[];types=[]
                for j in range(2*rank+1):
                    if j%2:
                        t=rng.randrange(3);K=rng.choice(kernels[t]);ks.append(cl[K])
                        fs.append(cl[K]&fib[t]);types.append(t)
                        empty+=int(not K);top+=int(cl[K]==allq)
                    else:
                        x=rng.randrange(7);ks.append({x});fs.append({x});types.append(elements[x][1])
                def prod(parts):
                    return reduce(lambda A,B:{mult[a][b] for a in A for b in B},parts,{0})
                ordinary,typed=prod(ks),prod(fs)
                t=reduce(op,types,2)
                for K0 in kernels[t]:
                    assert (ordinary<=cl[K0])==(typed<=cl[K0]&fib[t])
                    rules+=1
print('semigroups; languages per table; rule tests; initial tests',pairs,128,rules,initials)
print('empty selected child kernels; universal child closures',empty,top)
```

```console
$ python3 -I audit_types.py
semigroups; languages per table; rule tests; initial tests 8 128 2119346 45568
empty selected child kernels; universal child closures 17919 33583
```

### 削除族・導出木・再構成

`audit_gap.py`

```python
from itertools import product, combinations
from functools import cache

def levels(n):
    rows = [{'a'}]
    for _ in range(n):
        row = rows[-1]
        rows.append({'['+x+y+']' for x in row for y in row} |
                    {'{'+x+'}' for x in row})
    return rows

def ws(i):
    return 'a' if not i else '['+ws(i-1)*2+']'

def fillings(L,p,q):
    return {w[len(p):len(w)-len(q)] for w in L
            if len(p)+len(q)<=len(w) and w.startswith(p) and w.endswith(q)}

def test(n):
    E=levels(n)
    M=E[n]-{ws(n)}
    Y={(0,0):{'a'}}
    rules=1
    for i in range(1,n+1):
        for a in (0,1):
            if (i-1,a) not in Y:
                continue
            Y.setdefault((i,1),set()).update('{'+x+'}' for x in Y[i-1,a])
            rules+=1
            for b in (0,1):
                if (i-1,b) not in Y or (i==n and a==b==0):
                    continue
                Y.setdefault((i,a|b),set()).update('['+x+y+']'
                    for x in Y[i-1,a] for y in Y[i-1,b])
                rules+=1
    assert (len(Y),rules,Y[n,1])==(2*n,6*n-4,M)
    # All level-(n-1) marked siblings, on either side of the hole.
    C={('{','}')}
    for sibling in E[n-1]-{ws(n-1)}:
        C.update([('[',sibling+']'),('['+sibling,']')])
    for p,q in C:
        assert fillings(M,p,q)==E[n-1]
    z='['+ws(n-1)+'{'*(n-1)+'a'+'}'*(n-1)+']'
    r=1+len(ws(n-1))
    count=0
    for i in range(r+1):
        for j in range(i,r+1):
            p,x,q=z[:i],z[i:j],z[j:]
            q2=ws(n)[j:]
            for k in fillings(M,p,q):
                assert p+k+q2 in E[n]
                assert (p+k+q2 in M)==(k!=x)
                count+=1
    assert {x for x in E[n] if not ({'{','}'}&set(x))}=={ws(n)}
    print(n,'N,rules,frames,capture cases,long initial kernel',
          len(Y),rules,len(C),count,len(ws(n)))
    if n<=3:
        # All singly marked words, intervals covering the full marked node,
        # all contexts distinguishing the restored interval, using a context index.
        D={}
        for w in M:
            for i in range(len(w)+1):
                for j in range(i,len(w)+1):
                    D.setdefault(w[i:j],set()).add((w[:i],w[j:]))
        cnt=0
        for w in M:
            if w.count('{')!=1: continue
            a,b=w.index('{'),w.index('}')+1
            if a==0: continue
            inner=w[a+1:b-1]
            for i in range(a+1):
                for j in range(b,len(w)+1):
                    x=w[i:j]
                    xx=w[i:a]+'['+inner*2+']'+w[b:j]
                    for p,q in D[x]-D.get(xx,set()):
                        assert p+xx+q==ws(n) and len(x)==len(ws(n))-len(p+q)-len(inner)
                        cnt+=1
        print('constituent distinguishing contexts',cnt)
    return M

def rec(M,K):
    factors={w[i:j] for w in K for i in range(len(w)) for j in range(i+1,len(w)+1)}
    typ=lambda x: bool(set(x)&set('{}'))
    D=lambda L,x: {(w[:i],w[i+len(x):]) for w in L for i in range(len(w)-len(x)+1)
                   if w.startswith(x,i)}
    obs={x:D(K,x) for x in factors}
    target={x:D(M,x) for x in factors}
    upper={x:{v for p,q in target[x] for v in fillings(M,p,q)
              if all(l+v+r in M for l,r in target[x])} for x in factors}
    Y={x:({x} if len(x)==1 else set()) for x in factors}
    while True:
        changed=False
        for x in factors:
            out=set(Y[x])
            for y in factors:
                if typ(x)==typ(y) and obs[x]&obs[y]:
                    assert target[x]==target[y]
                    out.update(Y[y])
            for j in range(1,len(x)):
                out.update(u+v for u in Y[x[:j]] for v in Y[x[j:]])
            assert out<=upper[x]  # no length cutoff
            if out!=Y[x]: changed=True; Y[x]=out
        if not changed: break
    return set().union(*(Y[w] for w in K))

@cache
def trees(leaves):
    if leaves==1:return ('a',)
    return tuple((l,r) for i in range(1,leaves)
                 for l in trees(i) for r in trees(leaves-i))

def cut(t,cutpoint):
    chain=pieces=covered=0
    def walk(t,pos):
        nonlocal chain,pieces,covered
        if t=='a':return pos+1
        # Python tuples stand for binary productions.
        size=lambda x: repr(x).count('a')
        end=pos+size(t)
        if pos<cutpoint<end:
            chain+=1
            for ch in t:
                nextpos=pos+size(ch)
                if nextpos<=cutpoint:
                    pieces+=1; covered+=nextpos-pos
                else:walk(ch,pos)
                pos=nextpos
        return end
    walk(t,0)
    assert covered==cutpoint and pieces<=2*chain

if __name__=='__main__':
    for n in (2,3,4):
        M=test(n)
        if n==2:
            sizes=[]
            for l in range(len(M)+1):
                for ks in combinations(sorted(M),l):
                    if rec(M,ks)==M:
                        size=sum(1+len(x) for x in ks)
                        assert size**3>=3*2**(n-1)-1
                        sizes.append(size)
            print('exact samples / 32; minimum norm',len(sizes),min(sizes))
    cnt=0
    for leaves in range(2,9):
        for t in trees(leaves):
            for r in range(1,leaves):
                cut(t,r);cnt+=1
    print('ordered binary tree cuts',cnt)
```

```console
$ python3 -I audit_gap.py
2 N,rules,frames,capture cases,long initial kernel 4 8 3 23 10
constituent distinguishing contexts 26
exact samples / 32; minimum norm 1 42
3 N,rules,frames,capture cases,long initial kernel 6 14 11 120 22
constituent distinguishing contexts 390
4 N,rules,frames,capture cases,long initial kernel 8 20 83 1228 46
ordered binary tree cuts 4081
```

### 学習器と厳密性の証人

`audit_learn.py`

```python
from itertools import combinations, product

def factors(w):
    return {w[i:j] for i in range(len(w)+1) for j in range(i,len(w)+1)}

def cuts(w):
    return {(w[:i],w[j:]) for i in range(len(w)+1) for j in range(i,len(w)+1)}

def run(L,text,ty,dual):
    # Algorithm 1/2, r=k=1, with all nullary and unary terminal tuples.
    D=set(); pool=set(); H=set(); I=set(); P=set()
    def derives(w):
        V=factors(w); Y=set()
        while True:
            Z=set(Y)
            for A,l,B,r in P:
                if B is None:
                    if l in V:Z.add((A,l))
                else:
                    Z.update((A,l+x+r) for T,x in Y if T==B and l+x+r in V)
            if Z==Y:return any((A,w) in Y for A in I)
            Y=Z
    def acc(c,x):return c[0]+x+c[1] in L
    def mul(l,t,r):
        if t==2:return ty(l+r)
        # Representative of the child's type is sufficient.
        return ty(l+next(w for w in ('a','b','aa','ab') if ty(w)==t)+r)
    for w in text:
        D.add(w);E=set.union(*(factors(d) for d in D))
        J=set.union(*(cuts(d) for d in D))
        if any(not derives(d) for d in D):
            pool=J if dual else E
            H={(w,) for w in E}
            for d in D:
                H.update((a,b) for i in range(len(d)+1)
                         for a in factors(d[:i]) for b in factors(d[i:]))
        N=([(c,t) for c in pool for t in types] if dual else [(x,ty(x)) for x in pool])
        I={A for A in N if (all(x in L for x in E if ty(x)==A[1] and acc(A[0],x))
                             if dual else A[0] in L)}
        P=set()
        for A in N:
            for h in H:
                for B in ([None] if len(h)==1 else N):
                    l=h[0];r='' if B is None else h[1]
                    t=ty(l) if B is None else mul(l,B[1],r)
                    if A[1]!=t:continue
                    if dual:
                        vals={''} if B is None else {x for x in E if ty(x)==B[1] and acc(B[0],x)}
                        ok=all(acc(A[0],l+x+r) for x in vals)
                    else:
                        v=l+('' if B is None else B[0])+r
                        ok=all(not acc(c,A[0]) or acc(c,v) for c in J)
                    if ok:P.add((A,l,B,r))
    # A finite target and a repeated full text leave the reset pools unchanged
    # once all positives derive; check rule validity separately in the report.
    for w in ['']+[''.join(x) for i in range(1,5) for x in product('ab',repeat=i)]:
        assert derives(w)==(w in L),(L,w,dual)

types=(0,1,2); runs=0
for ty in (lambda w: 2 if not w else w.count('a')%2,
           lambda w: 2 if not w else int(w[0]=='b')):
    for base in (['a','b'],['','a'],['a','ab']):
        for ts in (base,base[::-1]):
            for d in (True,False):
                run(set(base),ts*3,ty,d);runs+=1
print('typed learner runs; queried comparison length',runs,4)

def lk(m,n,letter):
    return (m!=n if not letter else m>=n if letter=='z' else m<=n)
def strict():
    count=0
    for m,n in product(range(10),repeat=2):
        for tag in ('','y','z'):
            for center in ('y','z'):
                accepted=all(lk(p+m,n+q,tag) for p,q in product(range(12),repeat=2)
                             if lk(p,q,center))
                expect=(((m>n or (m==n and tag=='z')) and tag!='y') if center=='z'
                        else ((m<n or (m==n and tag=='y')) and tag!='z'))
                assert accepted==expect;count+=1
    for p in range(9):
        for m,n in product(range(10),repeat=2):
            if abs(m-n)<=p:continue
            i,j=max(0,n-m),max(0,m-n)
            assert not lk(m+i,n+j,'')
            assert all(lk(a+i,b+j,'') for a,b in product(range(10),repeat=2) if 0<abs(a-b)<=p)
    print('strict kernel test cases',count)
strict()
```

```console
$ python3 -I audit_learn.py
typed learner runs; queried comparison length 24 4
strict kernel test cases 600
```

### KY の診断集合と nullable 分割

`audit_ky.py`

```python
import re
from itertools import product
from functools import lru_cache

def words(alphabet, limit):
    for length in range(limit + 1):
        for letters in product(alphabet, repeat=length):
            yield ''.join(letters)

def mirror(x, sep):
    if x.count(sep) != 1:
        return False
    v, z = x.split(sep)
    return set(v) <= set('ab#') and z == v.replace('#', '')[::-1]

def parts(x):
    return re.fullmatch(r'([ab#]*)(c*)(d*)(e*)([ab]*)', x)

def side(x, side2):
    m = parts(x)
    if not m:
        return False
    v, c, d, e, z = m.groups()
    first = v.split('#')[0]
    delta = first.count('a') - first.count('b')
    if not (c or d or e or '#' in v):
        delta = 0  # take the entire word as the free suffix
    return ((delta >= 0 and len(c) == len(d)) if side2 else
            (delta <= 0 and len(d) == len(e)))

def triple(x):
    m = parts(x)
    return bool(m and len(m[2]) == len(m[3]) == len(m[4]))

def suffix_piece(x):
    m = re.fullmatch(r'([^%]*)%f*', x)
    if not m:
        return False
    left = m[1]
    if re.fullmatch(r'[ab#]*\$[ab]*c*', left):
        return True
    for k in range(len(left) - len(left.rstrip('c')) + 1):
        b = parts(left[:len(left)-k])
        if b and len(b[2]) == len(b[3]) and len(b[4]) != k:
            return True
    return False

@lru_cache(maxsize=50000)
def lang(x):
    return (mirror(x, '$') or mirror(x, '@') or side(x, True)
            or side(x, False) or suffix_piece(x))

def full(pattern, x):
    return bool(re.fullmatch(pattern, x))

def diagnostic(x):
    eq = lambda w: w.count('a') == w.count('b')
    return {
        'Q': full('[ab]*',x) and eq(x),
        'F': full('[ab]*#[ab#]*',x) and eq(x.split('#')[0]),
        'H': full('c*d*',x) and x.count('c') == x.count('d'),
        'E': full('e*',x), 'C': full('c*',x),
        'J': full('d*e*',x) and x.count('d') == x.count('e'),
        'T': full('[ab]*',x),
        'U': full('e*[ab]*c*',x) and x.count('e') != x.count('c'),
        'S45': suffix_piece(x),
        'S1': mirror(x,'$') or mirror(x,'@') or triple(x),
        'S2': side(x,True) or triple(x),
        'S3': side(x,False) or triple(x)}

C = {'Q':[('','#cd'),('a','b#de')], 'F':[('','cd'),('','ade')],
     'H':[('a#c','d')], 'E':[('a#cd','e')], 'C':[('b#c','de')],
     'J':[('b#d','e')], 'S2':[('',''),('a#','b')],
     'S3':[('',''),('b#','a')], 'T':[('$','a%')], 'U':[('e','c%')],
     'S45':[('','f')], 'S1':[('a#','a'),('b#','b')]}

alphabet = 'abcde#$%f@'
cnt = 0
for w in words(alphabet,5):
    expect = diagnostic(w)
    for A, contexts in C.items():
        actual = all(lang(u+w+v) for u,v in contexts)
        assert actual == expect[A], (A,w,actual)
        cnt += 1
print('diagnostic tests',cnt)
# Can a context admit all sampled positive S2/S3 yields while rejecting epsilon?
samples = {s:[w for w in words(alphabet,3) if w and side(w,s)]
           for s in (True,False)}
# Force a delimiter on either side of the c,d,e block.
for k in range(5):
    samples[True].append('#cd'+'e'*k+'a')
samples[False].append('#cddeea')
n = 0
for u in words(alphabet,2):
    for v in words(alphabet,2):
        for s in samples:
            assert lang(u+v) or any(not lang(u+w+v) for w in samples[s]), (u,v,s)
            n += 1
print('nullable split tests',n)
```

```console
$ python3 -I audit_ky.py
diagnostic tests 1333332
nullable split tests 24642
```

### 著者コードの一行修正と追加検査

`audit_extra.py`

```python
from pathlib import Path
from itertools import product
import sys

# Rerun the original file with exactly one expression corrected.
p=Path('sources/check_deletion_family.py')
src=p.read_text()
old="return 'Z' if '{' in w else '1'"
assert src.count(old)==1
env={'__name__':'checked_variant'}
exec(compile(src.replace(old,"return 'Z' if ('{' in w or '}' in w) else '1'"),str(p),'exec'),env)
for n in (2,3):
    assert env['check'](n)

# Observe the unmarked/group-refined components of the grammar, including
# unreachable type combinations, on the finite family. The marked bit
# and the parity of a are recorded simultaneously.
def t(w):
    return bool(set(w)&set('{}')), w.count('a')%2
cnt=0
for n in (2,3,4):
    E=env['levels'](n); M=E[n]-{env['wstar'](n)}
    for i,R in enumerate(E):
        c=('{'*(n-i),'}'*(n-i))
        ext=env['ctx_closure'](M,[c])
        for bit,parity in product((False,True),repeat=2):
            fine={w for w in R if t(w)==(bit,parity) and (i<n or bit)}
            assert fine=={w for w in ext if t(w)==(bit,parity)}
            cnt+=1
print('strong context refinement cells',cnt)
# Actual counts in the inequalities of Prop. 6.3, with varying finite contexts.
checks=0
for i2,j2 in product(range(6),repeat=2):
    ts=[t for t in range(8) if t>=i2 and 2*t>=j2]
    m=2*max(ts)
    for t0 in ts:
        a,b=3*m+t0-i2,2*m+2*t0-j2
        assert b<=a<=2*b
        checks+=1
    for i in (1,2,3):
        l=m+1
        assert 2*i*l+2*m>i*l+3*m
print('pumping inequality instances',checks)
```

```console
$ python3 -I audit_extra.py
  (E) n=2: factors=100, U-pairs checked=20, Rec(M_n) generates M_n: True
n=2: |L_n|=6, |w*|=10, capture pairs tested=17, all checks passed
  (E) n=3: factors=1991, U-pairs checked=1967, Rec(M_n) generates M_n: True
n=3: |L_n|=42, |w*|=22, capture pairs tested=108, all checks passed
strong context refinement cells 48
pumping inequality instances 184
```

## 6. 新規性と関連研究

NEW は以下に列挙した範囲で同じ定理を発見しなかったという判定。言語の既知性、質的な包含、同じ対象での量的下界を区別した。

|番号|判定|既知部分と本稿で残る差分|
|---|---|---|
|3.2|KNOWN|Clark (2015) Props.3.26,3.28 と KY2017 §3 式(1) の積閉包から二つの包含を取るだけ。|
|3.5|PARTLY KNOWN|Yoshinaka (2015) §§6.2–6.4 は sorted 版の核・文脈・学習を扱い、KY2017 Thms.3–6 は型なしの双方向。固定ファイバー、複数の初期型、very weak の必要方向を同時に述べる部分は組合せ。sorted 論文に同文の必要十分定理が載るという帰属は避ける。|
|3.7|KNOWN|KY2017 §4 p.6 の核規則の妥当性は生の核の文脈包含で決まる。子核の型を揃えたときの同値と、開始核を空文脈で検査する議論はこの基準の直接の帰結。補題の独立した命名には説明上の価値がある。|
|4.1|PARTLY KNOWN|#1 §6 と Appendix C の同じ一意解析・同レベルの括弧族。任意の部分語出現をノードと同定する定式化は本稿。標準的な部分木置換を独立の主要結果として数えない。|
|4.2(a),(b)|PARTLY KNOWN|文法・唯一の無標識語・短い $u_i$ は #1 §6, Prop.6.4 の証明にある。同原典は $s_U$ でのフィルタも使う。本稿の両閉包の等式、$M_n$ の正確な frame 表示と規則数は付加部分。|
|4.3|NEW|#1 Prop.6.4 の特性標本や系6.6の typed thickness は、任意 CFG の任意の核 SPP の特定の節点 yield が核そのものに属するとは述べない。|
|4.4、4.5|NEW|KY2017 Prop.2 は無限言語の表示の有無を分離。本稿は両種の表示が存在する有限言語を対象に、任意の核基数・文法・観測器について積の下界を与える。#1 Remark 6.5 の有限言語の反復除去は既知部分で、境界上の個数と捕獲を組み合わせる点が異なる。|
|4.6|NEW|同じ一語差から短い**正の**診断文脈を持つ構成素の長さを制約する。型なし文脈表示全体の指数下界までは示さない。|
|5.1|PARTLY KNOWN|#1 §4.1, Thm.4.2 の因子ごとの分布と、Clark の積包含を、開始記号を外した文法の singleton 核 SPP としてまとめ直したもの。|
|5.2|NEW|#1 Prop.6.4(iii),(iv) の下界を受けるターゲットは $L_n$。$M_n$ 自身の、しかも任意の適格な $s$ に対するこの下界はそこにはない。|
|5.4|NEW|KY2017 Algorithm 2 の候補数は既知。4.4 と結合し $M_n$ の安定時点に必要な入力長を下から押さえる点が差分。|
|5.5|NEW|KY2017 Algorithm 1 の全候補検定を逆用し、一つの**無効**規則の反駁に不可避な因子を指定する。一般の問合せ学習の下界とは別問題。|
|5.7|KNOWN|#1 Prop.9.7 の証明に二分文法を入力し、Yoshinaka (2015) §6.3 と KY2017 Thm.6 を連結する。二つの typed SPP の具体表示は本稿に残してよい。|
|6.1|PARTLY KNOWN|KY2017 Prop.10、§4、文法と有限型の積構成、Yoshinaka (2015) §8 の signature 比較が先行。均質な核とファイバーで制限した文脈の逆向き包含を、同じ $k$ で明記した部分を区別する。|
|6.3|PARTLY KNOWN|言語、二つの生成枝、負の pumping 論証は KY2017 Prop.2(i) と同じ。$s_0$ でも排除が有効で、$c$ の一ビットで strong 1-FCP になるという対比が追加。|
|6.4|PARTLY KNOWN|$m\ne n$ 枝の有限核排除は KY2017 Prop.2(ii)の差相殺そのもの。$y,z$ の二枝で $s_0$ に strong 1-FKP を与え、その標識への細分で任意 $k$ の失敗を同時に実現する分離命題は NEW。|
|6.6|NEW|KY2017 Lemmas 8,12,13, Thm.14 は untyped の二つの強さを分離する。鏡映の区切りを複製し、$@$ のファイバーを取り去って矛盾する構成は異なる命題。本査読 §3.2 の $s_0$ 版は現行原稿に含まれない。|

**追加すべき比較。**

1. **表現長とデータ長。** Clark–Eyraud (2007) Example 2 は、線形サイズの倍化文法が唯一の指数長の正例を持つことを既に指摘する。同論文の特性集合と総長の議論も比較対象になる。本稿には長さ $2n+1$ の正例 $u_n$ があり、全語が長いせいで起こる自明な下界を超えている。Coste–Nicolas (2019) §1, §4 は局所代入可能言語、正規形、thickness と多項式データ量を結びつける。これらを §1/§5 に加えると、新規性を「指数的なデータは初めて」ではなく「どの表示に情報を持たせると指数化するか」に正確に置ける。[Clark–Eyraud](https://www.jmlr.org/papers/volume8/clark07a/clark07a.pdf)・[Coste–Nicolas](https://proceedings.mlr.press/v93/coste19a/coste19a.pdf)
2. **Leiß の修正。** Leiß (2014) Example 1 は Clark の旧方式の不正な branching rule 判定を扱い、Theorem 2 で修正版を与える。従って「dual learner 一般」への下界のような表題は避け、現行 KY Algorithm 1 の全候補・反駁規則に結び付けるべきである。Clark (2010) の Theorem 1 をそのまま正しさの根拠にしてはいけない。本稿の主要証明は KY の修正後の方式を使っている。[Leiß 本文](https://www.cis.lmu.de/~leiss/cfg-learning.FG-14.dyck.pdf)・[Clark 2010 本文](https://www.its.caltech.edu/~matilde/ClarkSyntacticConceptLattice.pdf)
3. **KY の中間段階。** KY2021 Thms.3,5–7 は正・負の文脈条件を使う学習器と階層を扱う。KY2023 §§3–4 は正規演算と Boolean 演算を持つ式の SPP にまで拡張する。本稿の $C^\lhd\cap F_\mu$ はその一形で、任意の EXREG 表現を核に翻訳する下界ではない。1227–1229の “negative test” を残すと、KY2021の負の文脈と混同する。[KY2021](https://proceedings.mlr.press/v153/kanazawa21a/kanazawa21a.pdf)・[KY2023](https://proceedings.mlr.press/v217/kanazawa23a/kanazawa23a.pdf)
4. **sorted と概念束。** Yoshinaka (2015) §8 は関数と sort の分割に対する言語クラス比較を明示する。§6 は学習に必要な具体的仮定も置く。Clark (2015) の構文概念束の積と Galois 閉包は2.1と3.2の原典になり、Clark–Yoshinaka (2016) §6.5.3 は分布包含による一方向の代入と核を区別する。この系譜を限定して記せば、観測による opposite inclusions の説明に独自性が残る。[Yoshinaka 2015](https://aclanthology.org/W15-2308.pdf)・[Clark 2015](https://alexc17.github.io/static/pdfs/JLC2013.pdf)・[Clark–Yoshinaka 2016](https://www.jeffreyheinz.net/classes/22F/materials/ClarkYoshinaka2016.pdf)

## 7. 引用照合

### 著者論文 #1 の二版

[指定版の LaTeX](https://github.com/growupkuriyama-hub/Papers/blob/673064f/01_fixed-h-cfg/main.tex) は節ごとの定理共通カウンタ（14–20行）を追い、[arXiv:1409.6247v5 の PDF](https://arxiv.org/pdf/1409.6247v5) は紙面上の番号・本文を照合した。v5 の第1頁には 22 Oct 2026 とある。以下の頁は印刷頁。

|09 の参照行|引用|#1 の TeX 行|v5 の箇所|判定と内容|
|---|---|---|---|---|
|406–410|Def.2.1|342–346|p.4 Def.2.1|VERIFIED。対象は非空因子。Clark–Eyraud 原著への次の一文は別件。|
|356–363|Lemma 2.2|347以下|p.4 Lemma 2.2|VERIFIED。既に単位元があっても新しい単位を加える。|
|963–965|Prop.3.1|439以下|p.5 Prop.3.1 と直後|VERIFIED。正則言語を型ファイバーの和で認識、等型は全外枠で同じ受理値なので相対代入可能。Gold は「全有限言語と少なくとも一つの無限言語」の条件を介する。|
|755–765|§4.1|760以下|p.8 §4.1|VERIFIED。(B),(U),(L),(S)、空語の場合、記号が存在する非空因子に限る条件が一致。|
|593–604|§6|1139以下、特に1254–1271|pp.12–14、族の定義はp.13|VERIFIED。括弧族、二元半束、完全二分語、サイズが一致。|
|255–258, 604, 793, 812–817, 887–888|Prop.6.4, (iv)|1272–1355|pp.13–14 Prop.6.4 と証明末|VERIFIED。(ii) は $L_n,s_0$ の多項式、(iii) は $L_n,s_U$ の再構成、(iv) は $M_n$ の所属と $L_n$ の特性標本。$M_n\notin\mathcal C_{s_0}^{\rm cf}$ は命題文でなく証明末の二文脈。|
|245–247, 909–912, 959–963|Prop.9.7|2080以下|pp.20–21 Prop.9.7・証明|VERIFIED。合同文法への包含が明示される。階数2はその証明に二分化を先行させる帰結。|
|800–808|§2 特性標本|268–305|pp.3–4、特性標本の定義|VERIFIED。全有限中間標本を量化、等号も許す。|

七つの指定番号はすべて一致する。#1 の審査状況は著者の申告で、定理の検証に用いていない。

### 外部文献の番号・実際に用いた方向

KY2017 の以下の VERIFIED は[著者版原論文](https://makotokanazawa.ws.hosei.ac.jp/publications/swvwfckp.pdf)の印刷頁に対するもの。[Springer 刊行版](https://doi.org/10.1007/978-3-319-53733-7_5)では書誌のみ確認できたため、刊行版との番号の完全同一性は **UNVERIFIED**。

|09 の行|引用と照合箇所|判定|
|---|---|---|
|332–353, 458–470|KY2017 §3 pp.3–5、Prop.1、Prop.2(i),(ii)、Prop.10 p.10、Thm.14 p.11|VERIFIED。Prop.10 は言語クラスの等式の非自明な向き。証明中の終端規則追加も一致。|
|439–455|KY2017 §3 式(1) p.3、Clark (2015) Props.3.26,3.28|VERIFIED。式(1)自体は両辺の閉包の等号。右極の等号はその帰結。|
|229–233, 342–351, 492–514, 532, 837–843, 855–859|KY2017 Algorithms 1,2 pp.6–7、Thms.3–6 pp.7–8|VERIFIED。3/4 は安定⇒正しさとSPP、5/6 は適格文法⇒安定。候補を追加で刈らないという5.5の条件とも合う。|
|245–247, 952, 959–962, 982|KY2017 Thm.6 p.8、§4 pp.5–7|VERIFIED。$r=2,k=1$ の使用、規則妥当性の核文脈テストとも一致。|
|968, 1045–1073, 1121–1127|KY2017 Prop.2(i),(ii) pp.4–5|VERIFIED。$(i)$ の $d$ 枝は $n\le m\le2n$。$(ii)$ は不等数言語。|
|1133–1149, 1161–1184|KY2017 §5 Lemma 8 pp.9–10、§6 Lemma 12 pp.10–11、Thm.14 p.11|VERIFIED。8に旧表、12に $T,U,S_{4,5}$、旧 $S_1$ の**実閉包** $L_1$ と別の SPP 成分 $X_{S_1}=M^\lhd$ が明記。1176–1178で必要なのは後者。文法に $@$ を加えた後に初めてこの成分が新しい実閉包の旧語部分になる。|
|1191–1203, 1278–1281|KY2017 Lemma 13 p.11、その参照先 Lemma 7 pp.8–9、Thm.14|VERIFIED。特定の証人 $D$ と有限 $W$ についての主張は13の**証明**にある。$\$$ を観測すると元の証明が使えないことと、全言語の不可能性が解消されることは区別が必要。|
|1192, 1399–1402|Ogden (1968) と KY Lemma 7 脚注3|VERIFIED は書誌と KY の脚注による「同じ導出木を順にマーク」の使用まで。Ogden 原著の全証明との直接照合は **UNVERIFIED**。[出版社](https://doi.org/10.1007/BF01694004)|
|238–243, 247, 528–533, 956–962|Yoshinaka (2015) §§6,6.3,8|VERIFIED。§6.3 は congruential ⇒ 1-FKP、§8 は signature の細分を扱う。§6.4 の文脈条件は weak。3.5 の very weak 必要性そのものの引用先にはならない。|
|537–550|KY2023 §3.1, §3.2, Lemmas 2,4, Thm.6|VERIFIED。query atom の長い $u,v$ も式サイズでは各一原子。$m$ 原子、内部交差 $m-1$、ファイバー式との交差1つ、$b_\mu$ で計 $2m+b_\mu$。左の被演算子が guarded なら交差は guarded。新開始記号には一原子、単元規則で階数 $\max(r,1)$。Lemma 2 は到達文脈、4 は guard 化、6 は EXREG 学習に対応。|
|959|Clark–Yoshinaka (2016) “Sec. 5.3”|**MISMATCH**。刊行章 p.155 の見出しは **6.5.3 Finite Kernel Property**、合同文法は §6.5.1。章を省いた節番号の意図は読めるが、刊行版に合わせる。同章の強い定義と Yoshinaka §6.3 の弱い主張も区別する。|
|409–410|Clark–Eyraud (2007), Defs.3–5 p.1728 と #1 §3 “Classical special cases”|**MISMATCH**。非空因子に限定する規約が脱落。反例は §4 の $a^+$。|
|103–116, 1345–1355|Harris (1954) p.146、Clark (2010) の概念束による候補、Clark (2015) の概念束・乗法|VERIFIED（動機と定義の系譜）。概念の外延が全て有限生成になるという記述はこれらからは従わない。[Harris 原論文](https://gwern.net/doc/psychology/linguistics/1954-harris.pdf)|

## 8. JoLLI への適合

- **対象読者。** 同誌の scope は論理・言語・情報の数理的基礎と相互関係。文法推論と統語分布の接点として適合する。Harris の environment、Clark の概念の外延、SPP の成分、CFG の実 yield を一度並べると、言語学寄りの読者にも very weak の意義が伝わる。とくに $x\in\overline{\{y\}}$ は $D(y)\subseteq D(x)$ を表し、一般に全く同じ環境を持つ必要はない。[JoLLI の aims and scope](https://link.springer.com/journal/10849/aims-and-scope)
- **例1.1（120–153）。** 3つの名詞句、3つの自動詞文、9つの他動詞文という内訳を残す。例えば John と the dogs を the object slot で置換できても、barks の主語では置換できない、という相違が核を一語にできない理由になる。英語一般の数一致は外部のどこかに複数形があれば成立する規則ではない。観測器はこの有限断片での有無特徴であり、$M_n$ の存在条件はその特徴を抽象化した人工言語だと近接して書く。現在265–268,1253–1259の限定は適切。自然言語への実証的拡張は要求しない。
- **要旨・索引語。** 70–92 の abstract の中身を空白で分割し221語（ハイフン複合語を1語、数式トークンを各1語）。94–96は6キーワード。公式の150–250語、4–6語を満たす。語数を増やすより、削除前の上界に “untyped” を加え、正例の下界に演算子名を残す方が重要。[JoLLI 投稿規定](https://link.springer.com/journal/10849/submission-guidelines)
- **所属と申告。** 62–64に氏名、Independent Researcher、都市・国、連絡先あり。1321–1337に競合利益、データ、生成AI利用と著者の責任を明記。AI は証明・コードにも使われたため、現在の独立した申告節を残す。1325 の “No data were used.” は計算を支える資料への案内として不十分。“The proofs use no empirical dataset. The finite languages are generated from the definitions; scripts reproducing the finite checks are available at [commit permalink].” とする。Funding の有無も事実に即して Declarations に追記する。1339–1341 の謝辞の位置は規定の title page 指示に合わせる。公表済み又は採択済みの文献を参考文献リストに置く規定があるため、#1 は査読中というステータスと公開 v5 を区別し、preprint の記載方法を確認する。[JoLLI 投稿規定](https://link.springer.com/journal/10849/submission-guidelines)
- **版面・構成。** 指定 PDF は Letter 判18頁。全頁をレンダリングし、本文・数式・表・宣言の配置を確認した。p.11 の比較表の最重要問題は列の量化、p.15 の6.6は原典の記号を知ることを前提とした密な一頁。証人一覧を置くなら §7 の反復説明を縮めるとよい。pp.1–3 の Theorems A,B と pp.9,12–13 の正式版は、Bの strong の行を揃えれば案内として機能する。英文は数式を追える水準。主な修正対象は言い切りの範囲である。[指定 PDF](https://github.com/growupkuriyama-hub/Papers/blob/673064f/09_typed-fcp-fkp/main.pdf)

## 9. 前回査読との照合

§§1–8の判定・証明・実験結果と誤記一覧を作成した後、指定の[前回査読ディレクトリ](https://github.com/growupkuriyama-hub/Papers/tree/673064f/09_typed-fcp-fkp/research/external_review_2026-11-24)を開いた。前回の [VERDICTS.csv](https://github.com/growupkuriyama-hub/Papers/blob/673064f/09_typed-fcp-fkp/research/external_review_2026-11-24/VERDICTS.csv) は29行、CORRECT 11、CORRECT-WITH-FIX 8、KNOWN 10。前回は数学的真偽と既知性を一列で判定している。本報告では §2 と §6 に分けた。旧 A は現 B、旧 B は現5.7、旧 C は現 A に対応し、同じアルファベットの定理を機械的に比較することはできない。

|前回の指摘／CSVラベル|現行版における照合|今回の判定との差|
|---|---|---|
|I-01、旧 main:B, thm:uniform, rem:uniform-known|244–247, 909–913, 955–974。#1 Prop.9.7 と既存結果の系に変更。厳密包含も別途説明。|既知性は同意。数学的判定 CORRECT。概説章の節番号はなお要訂正。|
|I-02、旧 main:A, thm:duality|227–243, 528–533。Yoshinaka §8 と KY の役割を区別。|包含そのものは同意。旧 weak 問題の残部は下記の通り新判断。|
|I-03、lem:product|383–403。390行で中間の終端片を含む型積に修正。|旧 CORRECT-WITH-FIX → 現 CORRECT。旧反例 $S\to AcB$ でも $h(c)$ が計上される。|
|I-04、旧 main:A, prop:strict-kernel|216–224, 1037–1043, 1085–1106。$S_+,S_-$ の各 singleton 核で全 $k\ge1$ をカバー。真包含の端点を明記。|修正済み。6.4の分離は同意、基礎の差相殺手法は KY Prop.2(ii) 由来。|
|I-05、prop:learners|515–533。trim、非空化、Sub/Con、出力 sort への埋込みを追加。|旧 CORRECT-WITH-FIX → 現 CORRECT。reset の場合分けを本報告 §4 で明示。|
|I-06、prop:deletion-upper|628–636, 717–722。存在する子だけに制限。|旧 CORRECT-WITH-FIX → 現 CORRECT。$6n-4$ を独立生成でも確認。|
|I-07、rem:deletion-table|896–899 は最大長と総長を明記。$S_0$ の証人は $E_n$ と同じだが証明に明記はない。|**実質的不一致。** 旧 CORRECT-WITH-FIX は尺度の区別を要求したが、現889行に残る “any typing” は尺度を区別しても ERROR。$s_U$ 初期核への指数下界は本報告 §3.1。|
|I-08、rem:exreg|536–551。guard、パラメータ、rank、単一開始記号まで反映。|同意。LEDGER の「パラメータ対応は未照合」は現本文の正確性を否定する根拠にはならない。|
|I-09、op:Mn-context|726–743 の命題4.6として具体化、1285–1290 は別の未解決問題として維持。|旧 CORRECT-WITH-FIX → 4.6 は CORRECT。型なし $M_n$ の文法全体の下界は本査読でも未決。|
|I-10、app:comp|縮約 script 14–17, 77–101, 123–138、seed とソートを確認。実測4000/2230。旧版の2186という数を現版に持ち込まない。|縮約に関する旧修正は反映。新たな5.1の検査に使う deletion script の閉じ天井判定、長さ切断は別件で未修正。|
|I-11、書誌と定性的な比較|1034–1035に速度を比較しない旨、1412は単数形タイトル。1380–1384はなお巻・頁を欠く。|一部反映。巻と頁は刊行メタデータで確認した。|
|旧 main:C、lem:nodes, lem:capture, thm:deletion, cor:primal-data, prop:dual-refutation|606–621, 653–724, 826–879。コアの文法下界・学習器の下界を再導出。|CORRECT で一致する。前回の main:C の肯定は、現比較表の左列の “any typing” を正当化しない。|
|lem:clark, lem:reach, fact:ky, lem:typed-galois, lem:star, prop:typed-prop1, lem:reduction|298–353, 422–471, 558–579。既知の積閉包・到達文脈・restricted polarity。|前回の KNOWN と整合。CORRECT と KNOWN は異なる軸。|
|cor:primal-dominated, prop:strict-context, cor:invariant|1021–1035, 1045–1074, 1121–1128。階数は同じ文法を保ち、負の結果は6.1(b)で型に依存しない。|数学的判定に実質差なし。|

**CSV に行のない結果。** [WEAK_FCP_PARTIAL.md](https://github.com/growupkuriyama-hub/Papers/blob/673064f/09_typed-fcp-fkp/research/external_review_2026-11-24/WEAK_FCP_PARTIAL.md) の型なし正側と $@$ 型付き負側は現6.6に正しく反映。前回は $s_0$-typed 正側を未証明とした。今回の §3.2 は $S_2,S_3$ の正長 yield を受ける全ての文脈が空語も受けることを示し、その不足を解消する。前回が「未証明」と報告したこと自体は誤りではない。現5.1、5.2も当時のCSVには独立行がなく、新たに審査した。名称変更で生じた見かけの不一致と、比較表・未解決性に関する実質的な違いは以上の通り。

## 10. 細かな誤記・表記

|行|修正|
|---|---|
|103–114|概念を extent として同一視するという約束を明記。Harris の相互置換と singleton 核による分布包含を同じ定義に見せない。|
|158–161, 675–676|文脈長を初出で $\lvert(u,v)\rvert=\lvert u\rvert+\lvert v\rvert$ と定義し、$\kappa$ は選んだ核族にも依存すると断る。$G$ だけで一意な量ではない。|
|214–225, 983–990|冒頭の Theorem B に strong FCP の包含も掲げる。strong FKP は列挙しない。|
|332–340, 352–353|上添字 $k$ を省いたクラスが全有限 $k$ にわたる和であると明記。|
|494–501, 508, 856|$D_i,E_i,J_i,H_i$, 特に $\mathrm{Sub}^{\le r+1}$ の「順序を保った非連続の終端タプル」を初出で定義する。|
|673–676, 708–710|4.5(ii) にも「有限核の SPP」を明記する。無限核だと最大長が存在しないことがある。|
|774, 786–787, 832|標本ノルムを最初の使用前に定義。空標本を含めるなら最大値規約も設ける。|
|968–971|$\ell\ge j$ のとき $\ell+i$ と $\ell+j$ がともに $[\ell,2\ell]$ に入るため共通文脈になり、$c$ 枝が区別すると一言補う。|
|1182|最後の集合の略記に $v,z,i$ の範囲を再掲するか、一度 $J_0$ と命名して参照する。|
|1270–1273|$L^+$ 自身に $\lambda$ がある。“nullable-free” は全非終端が非 nullable と読むと不可能。必要なのは空語専用記号と非空記号の分離。|
|1278–1282|“the witness … is destroyed” を「既存の二語による反証が別ファイバーに分かれて使えない」に限定。言語そのものが typed weak FCP を持つ証明はここにない。|
|1380–1390|KY2017 は LNCS 10168, pp.77–88、KY2023 は PMLR 217, pp.8–22。入手可能な DOI を出版規定の完全リンク形式で補う。|

## 11. 審査の限界

- 指定の GitHub 入力1–6は固定コミットで取得した。raw の本文 URL は最初のウェブ取得では DisabledError だったが、同一 URL への HTTP 取得に成功し、PDF も含めて検査できた。1–5 は前回査読フォルダを開く前に調べた。指定の LEDGER 自体には前回判定の総数・著者の対応歴が含まれており、その自己申告と独立な証明・計算を根拠にした。前回への照合は §9 のみ。
- [Ogden (1968)](https://link.springer.com/article/10.1007/BF01694004) の書誌ページは開いた。[PDF URL](https://link.springer.com/content/pdf/10.1007/BF01694004.pdf) は購読案内 HTML を返した。原著の逐語的な証明は **UNVERIFIED**。KY Lemmas 7,13 に実際に書かれているポンプの利用箇所を確認した。[KY2017 刊行版 PDF](https://link.springer.com/content/pdf/10.1007/978-3-319-53733-7_5.pdf) も章の案内 HTML まで。数学的検証は公開著者版の本文全体による。arXiv v5 は PDF 本文を直接確認できた。
- Clark 2010と2015、Yoshinaka 2015、Clark–Yoshinaka 2016、KY2017・2021・2023、#1、Leiß、Harris、Clark–Eyraud、Coste–Nicolas は上記の原文の該当箇所に基づく。その他の一般的な背景引用、とくに Yoshinaka (2011 DLT)、Kanazawa (1998) の全内容、de la Higuera (1997) の個別定理、Leiß 公刊短版と著者長版の定理番号同一性は **UNVERIFIED**。これらを新規性や真偽の決定的根拠には用いなかった。未発見は先行研究不存在の証明ではない。
- 実行した検査のコマンド・コード・出力は §5 に示した。著者の三本を実行できた。任意の CFG、無限言語上の全導出、無限に続く学習、あらゆる有限半群を列挙してはいない。KY13 の全 CFG に及ぶ量化や問題8.1の解決は解析的論証に依存する。前回査読のログは今回の実行回数に含めなかった。
- PDF は配布物18頁の版面と抽出テキストを確認した。LaTeX の再コンパイルによるバイナリ同一性、投稿システムの受付、査読結果は未検証。Major revision は現原稿の主張と誌面適合性に対する判断である。

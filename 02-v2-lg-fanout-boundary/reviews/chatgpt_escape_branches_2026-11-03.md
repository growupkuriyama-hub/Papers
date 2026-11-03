# 「安い逃げ道」と倍増節点：三文字内容型付け・fan-out 2 の検討

2026-11-03 ／ 栗山貴之論文 #2・`op:fanout-two` に対する検討報告（第三報）

## 0. 判定一覧

| 主張 | 判定 | 根拠・射程 |
|---|---|---|
| 補題Dの明示的不等式 \(k\le[1+r(v-1)]\theta r^D\) | **証明済み** | §2。\(v=|V|\)、\(\theta=\bar\theta_G\)、\(r\ge2\)。最長子経路上の倍増数 \(D\)。 |
| \(v,\theta=\mathrm{poly}(n)\)、固定 \(r\) で \(k=n^{\omega(1)}\) なら \(D=\omega(\log n)\) | **証明済み** | §2、上式の対数を取る。 |
| 重い節点には \(b\) または \(c\) を含む長さ \(\le\theta\) の代替生成組がある | **証明済み** | §2、最短純粋語の短縮を使う。 |
| 同じ逃げ道骨格を持つ、保護位置に触れない重い節点は、失われる \(a\) 個数が一致する | **再検証済み（先行報告の定理3.1）** | §3。異なる非終端・祖先子孫関係でも成立。 |
| 保護位置に触れない倍増節点と、その真下の重い節点は、同じ逃げ道骨格を持てない | **証明済み（上記からの直接系）** | §4。長さ差が \(>\theta\) になるため。 |
| 保護位置を除いた部分木について \(D_U\le M_U\)（\(M_U\) は逃げ道骨格の種類数） | **証明済み** | §4。倍増節点が一本の経路上で相異なる符号を使う。 |
| 全体の \(k\) に対する、\(M\) を用いた明示的な条件付き上界 | **証明済み** | §5、式 (5.1)。\(\theta=O(1)\) なら \(k=O_{r,\theta}(v^2)\)。 |
| \(3^{\theta}=O(\log(\|G\|+2))\) の厚さ領域で \(k\) が多項式 | **証明済み（条件付き範囲）** | §5。\(r\) 固定。この条件は一般の \(\theta\) を扱わない。 |
| 倍増規則の二つの混合 \(\rho(\omega_i,u_j)\)、\(\rho(u_i,\omega_j)\) が同型で共通の受理文脈を持つ場合の分布一致 | **証明済み（条件付き）** | §6。成分ごとの内容一致が必要。 |
| \(K_2\) の (1,c)、(2,c) 全数検査通過、\(K_3\) の arity 2 違反 | **有限集合について証明済み（計算）** | §7・付録。既報の一般 \(n\ge3\) の証明の代替ではない。 |
| 同一 `bc` 脱出、段階依存 `bc^i b` 脱出の小例 | **有限集合で反例検出** | §7。いずれも検査した \(n=2,3\) で arity 1 違反。 |
| すべての長い倍増列から比較可能な「異なる分布」を強制する | **未解決** | §6・§8。異なる骨格間の損失を結ぶ論証がない。 |
| \(\mu_a(L)\le\mathrm{poly}(\|G\|,\theta)\) の一般肯定または否定族 | **未解決** | §8。適法な超多項式下界は本報告では得ていない。 |

本報告の新しい数式は、既報の骨格剛性から導く倍増節点への制約と、これを用いた**明示的な条件付き上界**である。文献上の新規性・優先権は**未確認**。`op:fanout-two` 自体を解いたとは主張しない。

## 1. 正本・用語・利用する既出事実の監査

### 1.1 照合した資料

- [現行 `main.tex`](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/main.tex)：取得時 blob SHA `b72cd2ed648f802886f0ab7c60a72f9f40c0864b`。本文の `def:standard-mcfg`、`def:grammar-properties`、`def:class-cmcf`、`lem:thickness-equivalence`、`lem:no-insertion`、`prop:rare-type`、`lem:power-transfer`、`lem:unique-word-gap`、`op:fanout-two` を照合。
- [Claude 三文字報告](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/reviews/claude_ternary_content_2026-11-01.md)：補題3.1、系3.2(iii)、補題3.4、3.5。
- [ChatGPT 純粋文字・骨格報告](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/reviews/chatgpt_pure_letter_fanout2_2026-11-02.md)：定理3.1、補題4.1、定理4.2。
- [ChatGPT スペクトル報告](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/reviews/chatgpt_a_spectrum_2026-11-03.md)：定理S、命題5.1。

原稿・先行報告の引用を権威だけで採用せず、以下で**実際に使う部分の証明**を記す。論文全体の無条件の再査読、他のすべての補題の再証明、文献網羅調査はしていない。

### 1.2 厳密な設定

\(\Sigma=\{a,b,c\}\)、\(c(w)=\{x\in\Sigma:x\text{ が }w\text{ に現れる}\}\)（非空語の**内容**）。\(L\in\mathcal C_{2,c}\) は fan-out \(\le2\) の MCFL で、**arity 1 と arity 2 の双方**について、同じ成分内容の二組がある許容受理文脈を共有すれば全受理文脈が一致するものとする。arity 2 文脈は \(u\square_1 v\square_2 z\) で **\(v\in\Sigma^+\)** とする。空成分は比較しない。

\(G=(V,\Sigma,P,S,\mathrm{fan})\) は \(L\cap\Sigma^+\) の reduced good 表示。good は λ-free・nondeleting・nonpermuting・nonmerging。\(\mathrm{fan}\le2\)、規則ランク \(\le r\)（\(r\ge2\) は固定とする）、\(v=|V|\)、\(g=\|G\|\)、\(\theta=\bar\theta_G\ge1\)。

\[
 k=\mu_a(L)=\min\{j\ge1:a^j\in L\}<\infty.
\]

\(k\le4\) の場合は所望の上界が自明なので以下は \(k\ge5\)。\(T\) を \(a^k\) の成功導出で**節点数最小**のものとする。節点 \(h\) の生成組の全成分の総長を \(\ell_h\) とし、\(\ell_h>\theta\) のとき**重い**と呼ぶ。非削除性から親の長さは、明示終端の数と全子の長さの**和**に等しい。

原稿 `lem:thickness-equivalence` (i),(ii) の確認：各規則 \(R\) を使う長さ \(\theta_G(R)\le\theta\) の成功導出がある。nondeleting により、\(R\) が直接出す終端と、そこにある任意の子の非空生成組は成功語に消えずに現れる。よって **各規則の明示終端数 \(\le\theta\)**。また reduced 性から各 \(B\in V\) は何らかの成功導出に現れ、そのとき \(B\) 部分木は長さ \(\le\theta\) の規則 witness から選べるので、各 \(B\) に \(\omega_B\in L_B(G)\)、\(\|\omega_B\|_1\le\theta\) を固定できる。成功導出から部分木を除けば、原稿 (iv) の \(E_B\) は全固定部分 \(\le\theta\) の許容文脈となり、任意の \(B\) の生成組を受理する。この論理に型付き refinement の独立した仮定は不要である。

## 2. 補題D：厳密な倍増深さの上界

**補題D（明示版）。** \(T\) の根から、各内部節点で総長が最大の子を一つ選んで進む経路 \(\pi\) を固定する。\(\pi\) 上で「長さ \(>\theta\) の子が少なくとも二つある」節点数を \(D\) とする。このとき

\[
 \boxed{k\le [1+r(v-1)]\,\theta\,r^D
        \le (r+1)v\theta r^D.}\tag{2.1}
\]

**証明。** まず \(T\) の任意の祖先・真の子孫に**同じ非終端** \(B\) が現れたら、上側 \(B\) の部分木を下側の \(B\) 導出で置換できる。同一 arity を保ち、good の非削除・非空条件によって得られるのは正の \(a\) だけの語であり、長さは \(k\) 以下である。短ければ \(k\) の最小性に矛盾し、等しければ節点数が減って \(T\) の最小性に矛盾する。したがってどの根葉経路も**節点数が高々 \(v\)** である。

経路上の親 \(h\) の明示終端数を \(t_h\le\theta\)、最大子を \(u\)、その長さを \(x=\ell_u\) とする。子数 \(m\le r\)。重い子が高々一つの場合、それがあれば必ず最大子であり、ほかの子の長さは各 \(\le\theta\)。無ければ全子が軽い。いずれも

\[
 \ell_h\le x+r\theta.\tag{2.2}
\]

重い子が少なくとも二つの場合、どの子の長さも \(\le x\) なので

\[
 \ell_h\le rx+\theta\le rx+r\theta.\tag{2.3}
\]

経路の葉はランク0の規則で作られるので長さ \(\le\theta\)。経路を葉から上へ \(q\le v-1\) 段遡ると、各段は \(x\mapsto\alpha x+b\)、\(\alpha\in\{1,r\}\)、\(b\le r\theta\) で評価でき、\(\alpha=r\) の段はちょうど \(D\) 個だけである。初期の \(\theta\) に掛かる係数は \(r^D\)。各加算項に掛かる、当該段より上の係数積も \(\le r^D\) なので

\[
 k\le \theta r^D+q r\theta r^D
 \le[1+r(v-1)]\theta r^D.
\]

\(1+r(v-1)\le (r+1)v\)。□

特に

\[
 D\ge \max\!\left\{0,\log_r\frac{k}{[1+r(v-1)]\theta}\right\}.\tag{2.4}
\]

**量化への注意。** \(r\ge2\) が固定、\(v_n,\theta_n\le n^{O(1)}\)、\(k_n=n^{\omega(1)}\) の族なら \(D_n=\omega(\log n)\)。\(r\) 自体が \(n\) に依存する場合にこの結論を同じ形で述べてはならない。

**重い節点の逃げ道。** \(h\) が重いとする。先に固定した \(\omega_{B_h}\) が純粋な \(a\) だけなら、その総長は \(\le\theta<\ell_h\)。その短い導出に差し替えると、nondeleting により \(a^{k-\ell_h+\|\omega_{B_h}\|_1}\in L\)、かつ指数は \(1\) 以上 \(k-1\) 以下となる。\(k\) の最小性に矛盾。ゆえに **\(\omega_{B_h}\) は必ず \(b\) または \(c\) を含む**。これは倍増節点の両方の重い子に個別に適用される。

## 3. 用いる骨格剛性を再証明する

\(\sigma_a(w)\) を、\(w\) の各極大 \(a\)-塊を一文字 \(a\) に圧縮した語（\(b,c\) の並びは変更しない）とする。

### 3.1 代入可能性から得る \(a\) の再配分と個数の漏れ

**補題3.1。** \(k\ge5\) なら、受理語の所属は、同じ \(a\)-骨格を持つ語の間では \(a\) の総個数だけに依存する。さらに、同じ骨格を持つ二つの受理語の \(a\) 個数の差が \(\delta>0\) なら

\[
 \mathcal D_L^{(1)}(a)=\mathcal D_L^{(1)}(a^{1+\delta}).\tag{3.1}
\]

**証明。** \(a^k\in L\) が \(a^4\) を含むから、arity 2 の組 \((a,aa)\) と \((aa,a)\) は成分内容が両方 \((\{a\},\{a\})\) で、許容文脈 \(\square_1 a\square_2\) を共通に受理する（元語から外側を取ればよい）。したがって任意の非空の \(a\) 以外の隙間を隔てた二つの \(a\) 塊で、長さを正に保ったまま一単位を移しても所属は変わらない。各塊の長さの正整数組成はこの移動で連結されるため前半を得る。

後半は同じ骨格の二受理語について、第2塊以降の長さをすべて1にし、余剰を第1塊に集める。第1塊の長さだけ \(\delta\) 異なる二語を、同じ一穴文脈に \(a\) と \(a^{1+\delta}\) を入れた語として表示できる。両者の内容は \(\{a\}\) なので arity 1 の代入可能性を適用する。□

**系3.2（禁じられた差）。** \(1\le\delta<k\) について (3.1) は成り立たない。実際、\(a^k=a^{k-\delta-1}a^{1+\delta}\) の右側を \(a\) に差し替えると \(a^{k-\delta}\in L\) となってしまう。この系は先行報告の「個数の漏れ」・スペクトル定理Sの必要部分に相当し、ここでは独立に確認できた。

### 3.2 保護位置と逃げ道の骨格

\(a^k\) の最初の二文字・最後の二文字を**保護位置**とし、直接これらの位置に終端を書き込む節点とその祖先を「保護付き節点」とする。それ以外を「清浄節点」と呼ぶ。清浄節点の全成分は保護位置の間の純粋 \(a\) 列に配置される。\(h\) が清浄かつ重いなら、\(\omega_{B_h}=(\omega_1,\ldots,\omega_d)\) に対して

\[
 \kappa(B_h):=\sigma_a(a\omega_1 a\omega_2 a\cdots a\omega_d a),
 \qquad d=\mathrm{fan}(B_h)\le2\tag{3.2}
\]

を逃げ道の**骨格符号**とする（\(d=1\) の場合は \(\sigma_a(a\omega_1 a)\)）。どの成分の前後にも元の語の \(a\) が残り、\(d=2\) なら非空の \(a\) 区切りが残る。したがって \(h\) だけを \(\omega_{B_h}\) に差し替えた語 \(W^h\) の全体骨格は、\(h\) の**位置や非終端名に依存せず**、\(\kappa(B_h)\) だけで決まる。

**補題3.3（先行報告の骨格剛性を再証明）。** 二つの清浄かつ重い節点 \(h,u\)（祖先・子孫でも可）に対し \(\kappa(B_h)=\kappa(B_u)\) なら

\[
 \ell_h-|\omega_{B_h}|_a
 =\ell_u-|\omega_{B_u}|_a,
 \qquad |\ell_h-\ell_u|\le\theta.\tag{3.3}
\]

**証明。** \(w_h:=\ell_h-|\omega_{B_h}|_a\) とする。重いことと \(\|\omega_{B_h}\|_1\le\theta\) から \(w_h>0\)。\(h\) は保護位置を含まないから \(\ell_h\le k-4\)、よって \(w_h<k\)。\(u\) についても同じ。\(W^h,W^u\) は受理語で、(3.2) により同じ \(a\)-骨格を持ち、その \(a\) 個数はそれぞれ \(k-w_h\)、\(k-w_u\)。もし \(w_h\ne w_u\) なら、差 \(0<|w_h-w_u|<k\) は系3.2に矛盾。従って \(w_h=w_u\)。\(\omega\) の \(a\) 個数はいずれも \([0,\theta]\) にあるため、長さ差の上界も従う。□

**反鎖の加法性の確認。** 清浄重い節点の反鎖 \(J\) を一斉に短い \(\omega_{B_h}\) へ差し替えると、nondeleting により生成語の \(a\) 個数は \(k-\sum_{h\in J}w_h\)、かつ保護位置は残る。二つの反鎖で骨格が同じなら、その損失和が異なると差は正かつ \(<k\) なので系3.2に反する。これは先行スペクトル報告の命題5.1の、実際に使う範囲での再証明である。**反鎖以外への無制限な加法的拡張は認められない**。

## 4. 倍増節点は同じ骨格符号を再利用できない

**補題4.1（倍増と骨格衝突の排除）。** \(h\) を \(T\) の**清浄な倍増節点**とし、\(u\) を \(h\) の**清浄で重い真の子孫**とする。このとき

\[
 \boxed{\kappa(B_h)\ne\kappa(B_u).}\tag{4.1}
\]

**証明。** \(u\) は \(h\) の一つの子の部分木の中にある。\(h\) には重い子が少なくとも二つあるから、その部分木と**異なる**重い子 \(j\) が選べる（\(u\) の属する子が軽い場合でも同様）。good の非削除性より

\[
 \ell_h\ \ge\ \ell_u+\ell_j\ >\ \ell_u+\theta.
\]

一方、もし二節点の符号が同じなら補題3.3は \(\ell_h-\ell_u\le\theta\) と言うので矛盾する。□

**系4.2。** 清浄な部分木 \(U\) の根から、最長子を選んで下る一本の経路にある清浄な倍増節点数を \(D_U\)、同じ部分木内に現れる清浄重い節点の相異なる符号数を \(M_U\) とすれば

\[
 \boxed{D_U\le M_U.}\tag{4.2}
\]

実際、経路上の異なる倍増節点は祖先・真の子孫の関係にあり、補題4.1で符号が異なる。

ここで必要なのは単なる「逃げ道の文法非終端名が異なる」ではなく、その**\(b,c\) 配置と \(a\) 塊を記録した符号が異なる**ことである。同じ \(\kappa\) を二度使って指数成長を継続する構成は不可能。ただし \(M_U\) 自体が \(v\) に比例する可能性は依然ある。

## 5. 条件付き肯定定理と小さな厚さの領域

\(M(T)\) を \(T\) の全清浄重い節点に現れる相異なる \(\kappa\) の数とする。\(M(T)\le v\)。

**定理5.1（骨格種類数による明示上界）。** 上記の設定で

\[
 \boxed{
 k\ \le\ 4v\theta\bigl[1+r\{1+r(v-1)\}r^{M(T)}\bigr].}
 \tag{5.1}
\]

**証明。** 保護した4文字の各々を直接書く節点から根までの経路には、補題Dで証明した非終端非反復により高々 \(v\) 節点しかない。従って保護付き節点の個数は \(\le4v\)。各保護付き節点の直接出力する終端は \(\le\theta\) 文字なので、その全寄与は \(\le4v\theta\)。

保護付き節点から出る子のうち、保護位置を一つも含まない**極大清浄部分木**の根の個数は \(\le4rv\)。そのような各部分木 \(U\) の全節点は清浄であり、補題Dの証明を \(U\) の最大子経路に適用できる。すなわち

\[
 \ell(U)\le[1+r(v-1)]\theta r^{D_U}.
\]

補題4.2より \(D_U\le M_U\le M(T)\)。ゆえに各 \(U\) の総長は \(\le[1+r(v-1)]\theta r^{M(T)}\)。根の語のすべての文字は、保護付き節点で直接出たものか、いずれかの極大清浄部分木に属するので、それらを加えれば (5.1) になる。□

**注。** 先行する `chatgpt_pure_letter_fanout2` の定理4.2も \(M(T)\) を用いた条件付き上界を与える。(5.1) は、今回の補題Dと補題4.1による**別証明・より簡単な定数**である。一般の多項式上界を新たに得たわけではない。

**系5.2（対数個の逃げ道なら多項式）。** \(r\ge2\) 固定、ある定数 \(A\) について

\[
 M(T)\le A\log_r(g+\theta+2)
\]

を満たす場合、(5.1) は \(\mathrm{poly}_{r,A}(g,\theta)\) である。特に、清浄な倍増箇所で再利用される符号を含めた全レパートリーが対数個以下なら肯定できる。

**系5.3（厚さが十分小さい場合の無条件の肯定）。** \(d=\mathrm{fan}(B)\le2\) と \(\|\omega_B\|_1\le\theta\) から、符号 \(\kappa(B)=\sigma_a(a\omega_1a\cdots a\omega_d a)\) の長さは \(\le\theta+3\)。三文字の語の数を粗く数えるだけで

\[
 M(T)\le Q(\theta):=\sum_{j=1}^{\theta+3}3^j
     =\frac{3^{\theta+4}-3}{2}.\tag{5.2}
\]

従って、\(r\ge2\) 固定で

\[
 \boxed{k\le4v\theta\bigl[1+r\{1+r(v-1)\}r^{\min\{v,Q(\theta)\}}\bigr].}
 \tag{5.3}
\]

特に **\(\theta\) が絶対定数なら \(k=O_{r,\theta}(v^2)\)**。さらに、文法族について **\(3^{\theta}=O(\log(g+2))\)** が一つの固定定数で成立するなら、\(Q(\theta)=O(\log(g+2))\) なので、\(k\le\mathrm{poly}_{r}(g,\theta)\)（係数はその固定定数にも依存）となる。

この領域は、要求されている \(\theta=\mathrm{poly}(n)\) 全般とは全く別である。\(\theta\) が線形の場合、(5.2) は非常に粗く、指数的な種類数の上界にすぎない。

## 6. 混合逃げ道の「四角形」と証明が止まる点

倍増節点 \(h\) の規則を \(R_h:B\to\rho(C_1,\ldots,C_m)\) とし、重い子 \(i\ne j\) の元の純粋 \(a\) 生成組を \(u_i,u_j\)、短い逃げ道を \(\omega_i,\omega_j\) とする。他の子は元の生成組に固定する。四通りの親生成組

\[
 X_{00}=\rho(u_i,u_j),\quad
 X_{10}=\rho(\omega_i,u_j),\quad
 X_{01}=\rho(u_i,\omega_j),\quad
 X_{11}=\rho(\omega_i,\omega_j)
 \tag{6.1}
\]

を得る（省略した引数は同一に固定）。すべて \(B\) の生成組であり、原稿の厚さ補題 (iv) により、**同じ**許容受理文脈 \(E_B\)（固定部分 \(\le\theta\)）を持つ。

**補題6.1（混合四角形の条件付き分布一致）。** たとえば

\[
 c^{(\mathrm{fan}(B))}(X_{10})
  =c^{(\mathrm{fan}(B))}(X_{01})\tag{6.2}
\]

なら、定義から直ちに \(\mathcal D_L^{(\mathrm{fan}(B))}(X_{10})=\mathcal D_L^{(\mathrm{fan}(B))}(X_{01})\)。とくに \(L\) が有限で、各成分について \((X_{01})_h=p_h(X_{10})_h q_h\)、かつ \(\sum_h(|p_h|+|q_h|)>0\) なら、原稿 `lem:no-insertion` により矛盾する。後者は、比較した二組を囲む文字を繰り返し追加することにより任意に長い受理語が生まれるためである。

**ただし (6.2) 自体が自動的には成立しない。** たとえば \(B\) が fan-out 2 で、一方の逃げ道が第1成分だけへ \(b\) を導入し、他方が第2成分だけへ \(b\) を導入すれば、親組の**総内容**は同じ \(\{a,b\}\) でも、成分ごとの内容ベクトルは \((\{a,b\},\{a\})\) と \((\{a\},\{a,b\})\) で相異なる。この場合、arity 2 の定義は両組を比較させない。

また (6.2) が成立しても、\(X_{10},X_{01}\) の**\(a\)-骨格が異なる**と、§3 の「同じ骨格に対する \(a\) 個数の漏れ」は発動しない。非有限言語では `no-insertion` の帰結「言語が無限」だけでは矛盾にならない。したがって、\(\omega(\log n)\) 個の倍増節点が存在するだけから、現時点で \(a^{k'}\)（\(0<k'<k\)）を構成することはできない。

この箇所が**肯定側の厳密な停止位置**である。既報の隙間合流（Claude 補題3.4）と共役移送（補題3.5）は、二成分の内容が一致する場面や、ある同一骨格に到達する場面では有用だが、**すべての異なる符号の組合せについて** (6.2) と同骨格の衝突を保証する定理は得られていない。それらを暗黙に仮定して一般上界を結論することはできない。

一方、**否定側**は各レベルで新しい \(\kappa\) を用意し、かつ上の四角形から生じるすべての再配分・合流・共役移送を満たす言語を構成しなければならない。符号を異ならせるだけでは十分でない。

## 7. 有限全数検査と候補の脱落

付録の Python 3 標準ライブラリだけの検査器は、**有限言語の全受理語**から、すべての arity 1 部分語と arity 2 の非空区切りを持つ二部分語、および対応する全文脈を列挙する。共通受理文脈がある同内容組の全文脈集合を比較するので、有限集合に対しては**完全判定**である。言語が無限で、長さ上限で切って検査した場合には完全判定とはならないが、本報告の列挙対象はすべて**定義から有限**である。

検査した \(K_n\) は \(E_0\to a\)、\(E_i\to bE_{i-1}E_{i-1}b\mid cE_{i-1}c\)。二つの脱出型候補は \(A_0\to a\)、\(A_i\to A_{i-1}A_{i-1}\mid d_i\) で、\(d_i=bc\) または \(d_i=bc^i b\)。いずれもこの有限段階の生成語を集合として完全に求めた。

| 検査対象 | 語数 | 最大語長 | arity 1 | arity 2 | 判定 |
|---|---:|---:|---|---|---|
| \(K_2\) | 6 | 10 | PASS | PASS | 有限集合として (2,c) 成立 |
| \(K_3\) | 42 | 22 | PASS | **FAIL** | 二穴で違反 |
| \(\{aa,bc\}\) | 2 | 2 | PASS | PASS | 制御例 |
| \(d_i=bc,\ n=2\) | 5 | 4 | **FAIL** | 検査省略 | 一穴で違反 |
| \(d_i=bc,\ n=3\) | 24 | 8 | **FAIL** | 検査省略 | 一穴で違反 |
| \(d_i=bc^i b,\ n=2\) | 5 | 6 | **FAIL** | 検査省略 | 一穴で違反 |
| \(d_i=bc^i b,\ n=3\) | 26 | 12 | **FAIL** | 検査省略 | 一穴で違反 |

`d_i=bc` の \(n=2\) では \(bc,bcbc\in L\)、両方の内容は \(\{b,c\}\)、共通受理文脈は \(\square\)。しかも \(bcaa\in L\) に対し \(bcbcaa\notin L\)。したがって arity 1 違反が**手計算でも**確定する。

`d_i=bc^i b` の \(n=2\) では、組 \(bc\) と \(bcbb\) の内容が共に \(\{b,c\}\)、文脈 \(\square cb\) に対して \(bccb,bcbbcb\in L\) である一方、文脈 \(\square baa\) に対して \(bcbaa\in L\)、\(bcbbbaa\notin L\)。この候補も arity 1 ですでに破れる。

\(K_3\) の違反は arity 2 であり、付録スクリプトが**受理する共通の二穴文脈**と**受理結果が分かれる別の二穴文脈**を両方表示する。これは \(n=3\) の厳密な有限反例証明であって、すべての \(n\ge3\) の一般証明は指定の Claude 報告に依存する。本検査から未検査の \(n\) の挙動は推論しない。

## 8. 結論、下界の射程、次の一点

### 8.1 現時点で言えること

補題Dは明示定数まで確定した。さらに**同じ骨格符号を保ったまま、重い兄弟を繰り返し増やすことは不可能**（§4）。これにより、超多項式の \(a\) 語には、同じ清浄経路に多数の倍増が必要であるだけでなく、**多数の相異なる逃げ道骨格**が必要である。\(\theta\) が極小のときにはレパートリー数を文字数で数え上げて多項式上界を得た（§5）。

### 8.2 今回は得られていない下界

本報告は \(\Sigma=\{a,b,c\}\)、\(c=c_\Sigma\)、**fan-out \(\le2\)**、**rank \(\le2\)**、reduced good \(G_n\)、\(L_n\in\mathcal C_{2,c}\)、\(\|G_n\|,\bar\theta_{G_n}=n^{O(1)}\)、\(\mu_a(L_n)=n^{\omega(1)}\) を同時に満たす族を構成していない。したがって原稿 `prop:rare-type` を用いた**新たな超多項式の特徴標本下界を確立していない**。

もしそのような族が実際にできれば、内容 \(\{a\}\) を持つ標本は \(a\) の冪だけなので、`prop:rare-type` により、各 \(L_n\) の特徴標本は少なくとも長さ \(\mu_a(L_n)\) の語を含む。この結論の作用素は、固定 \(r\ge2\) に対する \(\mathcal B_{2,c}^{\le r}\)、ランク制限なしの \(\mathcal B_{2,c}\)、そして \(L_n\) と \(L_n\setminus c^{-1}(\{a\})\) の双方に特徴標本を持つ**集合駆動作用素**である。とくにクラス全体 \(\mathcal C_{2,c}\) に特徴標本を持つ集合駆動作用素に及ぶ。しかし**任意の Gold 型逐次学習器の収束時点や計算時間の下界ではない**。これらはすべて、必要な適法族を得られた場合の**条件付きの説明**である。

### 8.3 次に絞るべき一点

> **骨格衝突補題（未証明）。** 清浄な重い倍増節点が一本の経路に \(\omega(\log(g+\theta))\) 個並び、それぞれ異なる逃げ道骨格を使うとき、混合四角形 (6.1) を組み合わせた少なくとも二つの成功語を、同一 \(a\)-骨格で \(a\) 個数差が \(1,\ldots,k-1\) にある形へ、arity 1・2 の許容文脈を保って変形できるか。

**このままでは証明できなかった。** 隙間合流の後に残る \(b,c\) 配置を統一できないためである。たとえば \(\rho(\omega_i,u_j)\) と \(\rho(u_i,\omega_j)\) がともに内容 \(\{a,b,c\}\) を持っていても、異なる骨格をもつ場合、現状の補題は \(a\) 個数差を純粋 \(a^k\) に漏らせない。さらに fan-out 2 では成分別内容が違えば比較すらできない。この隙間を埋めること、あるいは**その障害を保存する具体的な reduced good 文法族**を作ることが、残る真の仕事である。

**文献上の既知性：未確認。** 本報告の補題4.1、定理5.1、系5.3の形が既存文献にあるかは網羅的に調べていない。Seki ほかの MCFG 基礎理論、Yoshinaka の多次元代入可能性、および本原稿の既存補題を背景としているが、新規定理として投稿原稿へ移す前に独立監査と優先権調査が必要である。

## 付録A：再現用 Python 3 コード全文

Windows では以下のコードを `escape_branches_check_2026-11-03.py` として保存し、`py -3 escape_branches_check_2026-11-03.py` を実行する。検査は arity 1 と arity 2 の**全**許容受理文脈に対して行う。違反が見つかった場合、それ以降の arity は省略する。

```python
#!/usr/bin/env python3
"""Finite (1,c)/(2,c)-substitutability checks, Python 3 standard library only.

For a finite L, every accepting tuple context occurs inside a word of L;
therefore exhaustive enumeration is an exact decision procedure.
"""
from collections import defaultdict
from itertools import combinations


def fill(context, parts):
    if len(parts) == 1:
        u, v = context
        return u + parts[0] + v
    u, mid, v = context
    return u + parts[0] + mid + parts[1] + v


def content_type(parts):
    return tuple("".join(sorted(set(x))) for x in parts)


def observations(words, arity):
    observed = defaultdict(set)
    for word in sorted(words):
        n = len(word)
        if arity == 1:
            for i, j in combinations(range(n + 1), 2):
                parts = (word[i:j],)
                context = (word[:i], word[j:])
                observed[parts].add(context)
        else:
            for i, j, k, ell in combinations(range(n + 1), 4):
                parts = (word[i:j], word[k:ell])
                context = (word[:i], word[j:k], word[ell:])
                assert j < k  # The separator is nonempty.
                observed[parts].add(context)
    return observed


def check_finite(words):
    words = set(words)
    assert all(w and set(w) <= set("abc") for w in words)
    counts = {}
    for arity in (1, 2):
        observed = observations(words, arity)
        counts[arity] = len(observed)
        # For each common accepting context, compare all tuples of one type.
        shared = defaultdict(set)
        for parts, contexts in sorted(observed.items()):
            typed = content_type(parts)
            for e in sorted(contexts):
                shared[(typed, e)].add(parts)
        for (typed, e), tuples in sorted(shared.items()):
            if len(tuples) < 2:
                continue
            base = min(tuples)
            for other in sorted(tuples):
                if other == base:
                    continue
                if observed[base] != observed[other]:
                    distinguishing = min(observed[base] ^ observed[other])
                    left, right = fill(distinguishing, base), fill(distinguishing, other)
                    return False, counts, {
                        "arity": arity,
                        "type": typed,
                        "pair": (base, other),
                        "shared_context": e,
                        "shared_words": (fill(e, base), fill(e, other)),
                        "different_context": distinguishing,
                        "different_words": (left, right),
                        "membership": (left in words, right in words),
                    }
    return True, counts, None


def doubling_language(n, exit_word):
    current = {"a"}
    for level in range(1, n + 1):
        current = {x + y for x in current for y in current} | {exit_word(level)}
    return current


def bracketed_language(n):
    current = {"a"}
    for _ in range(n):
        current = {"b" + x + y + "b" for x in current for y in current} | {"c" + x + "c" for x in current}
    return current


def print_case(title, words):
    good, counts, witness = check_finite(words)
    print(title)
    print("  |L| =", len(words), "maxlen =", max(map(len, words)),
          "tuples(d=1,2) =", (counts.get(1), counts.get(2)))
    if good:
        print("  exact finite verdict: (1,c) AND (2,c) PASS")
    else:
        print("  exact finite verdict: FAIL, first violation at arity", witness["arity"])
        print("  type =", witness["type"], "pair =", witness["pair"])
        print("  shared =", witness["shared_context"], witness["shared_words"])
        print("  differing =", witness["different_context"],
              witness["different_words"], witness["membership"])


def main():
    for n in (2, 3):
        print_case("K_n with b X X b / c X c, n=" + str(n), bracketed_language(n))
    print_case("Control L={aa,bc}", {"aa", "bc"})
    for n in (2, 3):
        print_case("A_i -> A_(i-1) A_(i-1) | bc, n=" + str(n),
                   doubling_language(n, lambda i: "bc"))
    for n in (2, 3):
        print_case("A_i -> A_(i-1) A_(i-1) | b c^i b, n=" + str(n),
                   doubling_language(n, lambda i: "b" + "c" * i + "b"))


if __name__ == "__main__":
    main()
```

## 付録B：実行時の主要出力（2026-11-03）

実行環境は Python 3。以下は再現性のため集合列挙順をソートした版の出力である。

```text
K_n with b X X b / c X c, n=2
  |L| = 6 maxlen = 10 tuples(d=1,2) = (93, 516)
  exact finite verdict: (1,c) AND (2,c) PASS
K_n with b X X b / c X c, n=3
  |L| = 42 maxlen = 22 tuples(d=1,2) = (1845, 45076)
  exact finite verdict: FAIL, first violation at arity 2
  type = ('ab', 'ab') pair = (('bbba', 'bbaabbbbaabb'), ('bbbaabbaabbbb', 'abb'))
  shared = ('', 'a', 'aabbb') ('bbbaabbaabbbbaabbaabbb', 'bbbaabbaabbbbaabbaabbb')
  differing = ('', 'aabba', 'b') ('bbbaaabbabbaabbbbaabbb', 'bbbaabbaabbbbaabbaabbb') (False, True)
Control L={aa,bc}
  |L| = 2 maxlen = 2 tuples(d=1,2) = (5, 0)
  exact finite verdict: (1,c) AND (2,c) PASS
A_i -> A_(i-1) A_(i-1) | bc, n=2
  |L| = 5 maxlen = 4 tuples(d=1,2) = (19, None)
  exact finite verdict: FAIL, first violation at arity 1
  type = ('bc',) pair = (('bc',), ('bcbc',))
  shared = ('', '') ('bc', 'bcbc')
  differing = ('', 'aa') ('bcaa', 'bcbcaa') (True, False)
A_i -> A_(i-1) A_(i-1) | bc, n=3
  |L| = 24 maxlen = 8 tuples(d=1,2) = (111, None)
  exact finite verdict: FAIL, first violation at arity 1
  type = ('a',) pair = (('a',), ('aaa',))
  shared = ('', 'aaabc') ('aaaabc', 'aaaaaabc')
  differing = ('', 'aaaaa') ('aaaaaa', 'aaaaaaaa') (False, True)
A_i -> A_(i-1) A_(i-1) | b c^i b, n=2
  |L| = 5 maxlen = 6 tuples(d=1,2) = (34, None)
  exact finite verdict: FAIL, first violation at arity 1
  type = ('bc',) pair = (('bc',), ('bcbb',))
  shared = ('', 'cb') ('bccb', 'bcbbcb')
  differing = ('', 'baa') ('bcbaa', 'bcbbbaa') (True, False)
A_i -> A_(i-1) A_(i-1) | b c^i b, n=3
  |L| = 26 maxlen = 12 tuples(d=1,2) = (248, None)
  exact finite verdict: FAIL, first violation at arity 1
  type = ('abc',) pair = (('aaaabcb',), ('bccbaa',))
  shared = ('', 'aa') ('aaaabcbaa', 'bccbaaaa')
  differing = ('aa', '') ('aaaaaabcb', 'aabccbaa') (True, False)
```

**検査の解釈上の制限**：`PASS` はその**有限言語だけ**について (1,c) および (2,c) の全数検査を通過したことを意味する。コードは MCFG の reduced good 性、文法サイズ、規則厚さを機械的に証明しない。したがって数値実験を用いて無限族の所属や特徴標本下界を主張していない。

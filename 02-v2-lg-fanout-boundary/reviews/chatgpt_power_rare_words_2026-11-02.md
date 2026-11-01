# ファンアウト2の唯一希少語：指数長構成の探索、二種類の失敗証明、および汚染語長のギャップ上界

**研究日**：2026-11-02  
**対象**：栗山貴之、論文 #2、`02-v2-lg-fanout-boundary/main.tex`  
**検証した作業正本の Git blob**：`ca7465d7e1b4d7376bc8fc2bc7068123809693bc`  
**主要な結論**：指定された超多項式長の反例族は**構成できなかった**。したがって `op:fanout-two` と `op:S1` は**未解決**のままである。一方、(i) 数値条件を満たすショートカット倍増文法が**1穴で失敗**すること、(ii) `a^k` と `bc` を混ぜるブロック族が**2穴で失敗**すること、(iii) **長い唯一型語には長い非純語が必要**というファンアウト非依存の定量補題、(iv) 非純語の型別計数が固定なら**二次上界**を証明した。

## 0. 主張の判定表

| ID | 主張 | 判定 | 根拠 |
|---|---|---|---|
| P1 | `\|G_n\|,\bar\theta_{G_n}=n^{O(1)}` かつ唯一型1語 `W_n` が `n^{\omega(1)}` の、`\mathcal C_{2,s_U}` の族を構成 | **未解決** | §9；候補は§4–5で失敗 |
| A | `A_0\to a\mid c`, `A_i\to A_{i-1}A_{i-1}\mid c`：`\|G_n\|=8n+5`, `\bar\theta=n+1`, 唯一の純語 `a^{2^n}` | **証明済み**（数値のみ）。代入可能性は**反証** | §4：全 `n\ge1` の1穴違反 |
| B | `L_{k,m}=\{a^k,bc\}^m`：`k\ge2,m\ge3` なら `(2,s_U)`-代入可能**でない** | **反証**（候補の所属） | §5：任意の `k,m` に明示した2穴違反 |
| B' | 倍増ブロック表示 `k=2^p,m=2^q` の `\|G\|=6(p+q)+10`, `\bar\theta=k+2m-2` | **証明済み** | §5；reduced good、ランク2、ファンアウト1 |
| G | 型別分布の貼合せ判定法（異なる出力型の部分言語を合併するときの必要十分条件） | **証明済み** | §2：全 `1\le d\le f` |
| T | 唯一語 `W=a^N` から誘導される1穴・2穴の長さ保存・`b` 禁止条件 | **証明済み** | §3：全 arity の明示的な分布式 |
| M | **汚染語長ギャップ**：唯一の型1語 `W`、他の語の最大長 `M`、ランク `\le r` なら `\boxed{|W|\le\bar\theta_G+(r+1)M}` | **証明済み** | §6：任意ファンアウト、非削除 MCFG、**代入可能性さえ不要** |
| Q | 全ての型 `\zeta` 語が同一の `(\#\{a,b\},\#c)` をもてば `|W|\le\lfloor(\bar\theta_G+1)^2/4\rfloor` | **証明済み**（既存の定重み上界に帰着） | §7；5形すべて、任意ファンアウト |
| C | `H_{k,m}=\{w:|w|_b=|w|_c,\ |w|_a+k|w|_c=km\}` は全 arity で代入可能、唯一の型1語 `a^{km}` | **証明済み**（ただし反例ではない） | §8；正の定重みにより二次上界 |
| E | 列挙した小さい候補の `(1,s_U)`・`(2,s_U)` 検査 | **観察**（個々のFAIL証明書は厳密な反例） | §10および付属の全文Python |
| L | もし真の P1 族があれば特徴データに超多項式下界、ファンアウト2で `\mathbf{LG}` 境界 | **条件付きの既存帰結** | §9；原稿 `prop:rare-type`・`prop:unique-word-route` |

**判定の意味**：「証明済み」は以下に自足的な論証があるという意味であり、独立査読や先行研究での初出性を意味しない。「観察」は有限全数検査からの実測である。新規性は**未確認**。

## 1. 正本と量化の固定

- 原稿：<https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/main.tex>（取得 blob は上記）。§2の `def:standard-mcfg`, `def:grammar-properties`, `def:tuple-substitutable`、§4の `lem:thickness-equivalence`, `lem:type-deletion`, `lem:no-insertion`, `lem:distinguishing`, `prop:rare-type`、§7–9の依頼指定事項と付録Jを照合した。
- 事前レビュー：`reviews/chatgpt_nolift_general_2026-11-02.md`、`reviews/chatgpt_singleton_classification_2026-11-02.md`、`reviews/chatgpt_single_neutral_letter_2026-11-02.md`、`reviews/chatgpt_problemG_2026-11-01.md`、`reviews/claude_ternary_content_2026-11-01.md`、および `parked/parked_u1_typing_level.tex` を参照した。過去レビューの証明を新発見として数え直していない。
- `\Sigma=\{a,b,c\}`、`U_1=\{1,\zeta\}`、`1\zeta=\zeta1=\zeta^2=\zeta`、`s_U(a)=s_U(b)=1,s_U(c)=\zeta`。語の型1は **`c` を含まない**ことと同値。
- 許容 `d`-文脈は `E=v_0\Box_1v_1\cdots v_{d-1}\Box_dv_d`、穴に代入する語はすべて非空、中間固定部 `v_i` (`1\le i<d`) は**非空**。前後端の `v_0,v_d` は空でもよい。成分ごとに `s(x_i)=s(y_i)` であり、`E[\mathbf x], E[\mathbf y]\in L` なら、すべての許容 `F` に対し `F[\mathbf x]\in L\iff F[\mathbf y]\in L` が必要。
- `G` は reduced good：reduced＝全非終端が到達可能・生成可能、good＝各テンプレートが `\lambda`-free・nondeleting・nonpermuting・nonmerging。ランクの上限 `r` は固定（原問題は `r\ge2`）。文法サイズは `\|G\|=|V|+\sum_R(1+\operatorname{rank}R+\text{テンプレート文字・変数数})`。`\bar\theta_G` は各規則 `R` が一度以上使われる成功導出で得られる**最短の文の長さ**の最大値（少なくとも1）。

ここでの新補題は代入可能性を仮定するか否かを明記する。**`\bar\theta` を最短導出木の節点数や文法サイズと混同しない。**

## 2. 型別分布の貼合せ補題（一般の arity）

`L=L_1\mathbin{\dot\cup}L_\zeta`、`L_1=L\cap\{a,b\}^+`、`L_\zeta=L\cap\{w:c\in\mathrm{alph}(w)\}` とおく。`D_i^{(d)}(\mathbf x)` を `L_i` に関する許容文脈の集合とする。

**補題 2.1（必要十分条件）。** `L_1,L_\zeta` がそれぞれ `(f,s_U)`-tuple-substitutable であるとする。このときその和 `L` が `(f,s_U)`-tuple-substitutable であるための必要十分条件は、全 `1\le d\le f` と成分型の一致する正のタプル `\mathbf x,\mathbf y` について、次の**二方向**がともに成立すること：

1. `D_1^{(d)}(\mathbf x)\cap D_1^{(d)}(\mathbf y)\ne\varnothing` なら `D_\zeta^{(d)}(\mathbf x)=D_\zeta^{(d)}(\mathbf y)`。
2. `D_\zeta^{(d)}(\mathbf x)\cap D_\zeta^{(d)}(\mathbf y)\ne\varnothing` なら `D_1^{(d)}(\mathbf x)=D_1^{(d)}(\mathbf y)`。

**証明。** 同じ型のタプルを同じ文脈 `E` に代入すると、半群準同型性から `s_U(E[\mathbf x])=s_U(E[\mathbf y])`。したがって共通受理文脈 `E` は両語を**同じ**型別部分言語へ送る。各型別部分言語の代入可能性がその側の分布一致を与え、上の交差条件が他方の分布一致を与えるので、二つの分布の和も一致する。逆に `L` が代入可能なら、どちらか一方の部分言語で共有された文脈は `L` でも共有される。従って `L` での分布一致を得る。型付けが一致するタプルについては、ある固定 `F` が両タプルを異なる出力型へ送ることはないので、その一致は型別分布の一致に分解する。`d` は最初から任意だった。□

また `L\in\mathcal C_{f,s_U}` のときは、原稿 `lem:type-deletion` と出力型による切出しから両部分言語も代入可能である。**出力型の異なる部分言語を単に合併しても安全、という意味ではない。** 必要なのは上記の*交差分布の整合性*である。多層構成に適用する際の実用的なチェックポイントとなる。

## 3. `W=a^N` の正確な分布と衝突禁止（全 arity）

`L_1=\{a^N\}` とする。任意の `d\ge1`、正のタプル `\mathbf x=(x_1,\ldots,x_d)` について

\[
D_{\{a^N\}}^{(d)}(\mathbf x)=
\begin{cases}
\{v_0\Box_1v_1\cdots\Box_dv_d:\ v_i\in a^*,\ v_i\ne\varepsilon\ (1\le i<d),\ \sum_i |v_i|=N-\sum_j|x_j|\},&x_j\in a^+\ \forall j,\\
\varnothing,&\text{それ以外}.
\end{cases}
\]

右辺の文脈集合は `\sum_j|x_j|+d-1\le N` のときに限り非空である。これは代入結果が全て `a` で長さ `N` となる条件を一文字ずつ読み下したものなので、**全 arity** で成立する。特に単語言語 `\{a^N\}` は全 `d`・全型付けで代入可能（型が一致して共通受理文脈があれば同じ総長をもつ `a`-タプルとなる）。

**系 3.1（短い純タプルの不可逆衝突）。** `L\in\mathcal C_{f,s_U}`、`L_1=\{a^N\}` とする。`d\le f`、`\mathbf x=(a^{i_1},\ldots,a^{i_d})`、`i_j\ge1`、`\sum i_j+d-1\le N` とする。もし成分ごとの型がすべて1である `\mathbf y\in\{a,b\}^{+d}` と、ある許容 `E` について `E[\mathbf x],E[\mathbf y]\in L_\zeta` が成り立つなら、**`\mathbf y` も全て `a` の冪で、成分長の総和は `\sum i_j` と等しい**。

**証明。** `D_\zeta(\mathbf x)\cap D_\zeta(\mathbf y)` は非空。補題2.1の第二条件により、`D_1(\mathbf x)=D_1(\mathbf y)`。左辺は上の式で非空だから、右辺も非空となる必要があり、`y_j\in a^+` 全成分、かつ総長が一致することが従う。□

これは `d=1` では `a^i` と `a^j`（`i\ne j`）や `a^i` と `b` を同じ `c`-文脈で受理できないこと、`d=2` では**総長の異なる**純な二組、あるいは `b` を混ぜた二組を `c`-文脈で共通受理できないことを意味する。ただし**同じ総長の二組は許されるとは限らない**。その逆方向の障害が次のブロック例である。

## 4. P1案A：ショートカット倍増は数値条件を満たすが1穴ですでに破綻

`n\ge1` とし、開始非終端を `A_n` とする CFG（したがってファンアウト1）

```text
A0 -> a | c
Ai -> Ai-1 Ai-1 | c       (1 <= i <= n)
```

を `G_n^{\mathrm{short}}`、言語を `L_n^{\mathrm{short}}` とする。

**命題 4.1（数値、全 n）。** `G_n^{\mathrm{short}}` は reduced good、最大ランク2、最大ファンアウト1で、

\[
\boxed{\|G_n^{\mathrm{short}}\|=8n+5,\quad
\bar\theta_{G_n^{\mathrm{short}}}=n+1,\quad
L_n^{\mathrm{short}}\cap\{a,b\}^+=\{a^{2^n}\}.}
\]

**証明。** `A_i` は全て到達可能・生成可能。テンプレートは非空・非削除・非置換・非結合である。非終端は `n+1` 個。`A_0` の二定数規則の費用は計4、各 `i\ge1` の二項規則は `1+2+2=5`、`c` 規則は2で、和は `4+7n`。よってサイズは `8n+5`。すべての規則の成功導出は、祖先の各段で片方の兄弟を `c` に短絡させれば構成できる。`A_0\to a` の使用には少なくとも `n+1` 文字必要で、長さ `n+1` が実現する。他の規則は各レベルの祖先への通過と最大2個の子で長さ `\le n+1` の文を作れるため厚さはちょうど `n+1`。`c` を全く使わない導出は全二項規則を選び、全葉を `a` とするものだけで、文は `a^{2^n}`。□

**命題 4.2（代入可能性の一様な反例）。** 全 `n\ge1` について、`L_n^{\mathrm{short}}\notin\mathcal C_{1,s_U}`、ゆえに `\mathcal C_{2,s_U}` にも属さない。

**証明。** `n=1` では `E=\Box`、`x=c`、`y=ac`、`F=\Box a` とする。`E[x]=c,E[y]=ac,F[x]=ca` は `L_1` にあり、`F[y]=aca` はない。しかも `s_U(x)=s_U(y)=\zeta`。

`n\ge2` では `x=aa,y=a` とし

\[
E_n=\Box ac\,c^{n-2},\qquad F_n=\Box a^{2^n-2}.
\]

`A_2` から `aaac` と `aac` が導出でき、各上位 `A_i` では右の兄弟を `c` にして1文字ずつ末尾に付加できる。よって `E_n[aa],E_n[a]\in L_n`。一方 `F_n[aa]=a^{2^n}\in L_n`、`F_n[a]=a^{2^n-1}\notin L_n`。`s_U(aa)=s_U(a)=1` なので1穴条件に反する。□

これは**指数長 `W`・線形サイズ・線形厚さを同時に達成したが、代入可能性だけが破れている**厳密な近接例である。`c` による再帰的ショートカットが1穴の純長衝突を生むことを示す。

## 5. P1案B：`a^k`/`bc` ブロックの掛け算は2穴で破綻

`k\ge2,m\ge3` とし

\[
L_{k,m}^{\mathrm{blk}}=(\{a^k,bc\})^m
\]

と定める。唯一の型1語は `W=a^{km}` である。

**命題 5.1（2穴反例、一般の k,m）。** `L_{k,m}^{\mathrm{blk}}` は `(2,s_U)`-tuple-substitutable でない。

**証明。** タプルと許容文脈を

\[
\begin{split}
\mathbf x&=(a^k,a^{k(m-2)}),\\
\mathbf y&=(a^{k+1},a^{k(m-2)-1}),\\
E&=a^{k-1}\Box_1a\Box_2,\qquad
F=\Box_1bc\Box_2
\end{split}
\]

とする。`k\ge2,m\ge3` なので各成分と二つの中間固定部 `a,bc` は非空。両タプルの成分型は `(1,1)`、`E[\mathbf x]=E[\mathbf y]=a^{km}\in L`。また `F[\mathbf x]=a^kbc\,a^{k(m-2)}\in L` だが、`F[\mathbf y]=a^{k+1}bc\,a^{k(m-2)-1}\notin L`。最後は `bc` がちょうど一ブロックである場合、その前後の `a` 連続長がいずれも `k` の倍数でなければならないため。□

**命題 5.2（倍増表示の厳密な数値）。** `k=2^p,m=2^q`（`p\ge1,q\ge1`）なら、開始非終端 `C_q` のCFG

```text
A0 -> a
Ai -> Ai-1 Ai-1       (1 <= i <= p)
C0 -> Ap | bc
Cj -> Cj-1 Cj-1       (1 <= j <= q)
```

は reduced good、ランク2、ファンアウト1で、

\[
\boxed{\|G_{p,q}^{\mathrm{blk}}\|=6(p+q)+10,
\qquad\bar\theta_{G_{p,q}^{\mathrm{blk}}}=2^p+2^{q+1}-2.}
\]

**証明。** 非終端は `p+q+2`、規則費用は `2+5p+3+3+5q=8+5(p+q)`。厚さは、`C_j` 二項規則と `C_0\to bc` を使う最短文で `2m`、`A_i` の規則や `C_0\to A_p` を使う最短文では長ブロック一個と残り `m-1` 個の `bc` が必要で `k+2(m-1)`。`k\ge2` より後者が最大。□

`p=q=n` だと `|W|=4^n` だが `\bar\theta\asymp2^n` であり、**数値的にもP1の要求（厚さが n の多項式）を満たさない**。さらに `q\ge2` なら命題5.1で2穴条件にも反する。なおファンアウト1での二値型付けブロック族 `\{a^{2^p},c\}^{2^q}` は原稿 `prop:binary-u1-quadratic` の既存例であり、下界は厚さの二次スケールまでである。

## 6. P2の新しい部分結果：長い唯一純語には長い汚染語が必要

**定理 6.1（汚染語長ギャップ）。** `G` を非削除で reduced な MCFG（任意ファンアウト、規則ランク `\le r`、各規則テンプレートの直接終端数 `\le\bar\theta_G`）とする。`L=L(G)\subseteq\{a,b,c\}^+` に `c` を含まない語がちょうど一つ `W` あるとする。`L\setminus\{W\}` の各語は `c` を含み、それらの長さの最大値を `M` とする（この集合が空なら `M=0`；最大値が存在しない場合は主張は適用しない）。このとき

\[
\boxed{|W|\le\bar\theta_G+(r+1)M.}\tag{6.1}
\]

特に `G` が reduced good なら、原稿 `lem:thickness-equivalence`(i) により直接終端数の仮定は自動的に満たされる。**`L\in\mathcal C_{f,s_U}` は仮定しない。** `W` が5形のどれかである必要もない。

**証明。** `N=|W|`、`\theta=\bar\theta_G` と置く。`N\le\theta` なら明らかなので `N>\theta` とする。`W` の任意の成功導出木 `T` を固定し、節点 `v` の非終端を `A_v`、そこから生成される非空タプルの全成分長の和を `t_v` とする。線形・非削除性により

\[
t_v=\text{（vの規則が直接書く終端数）}+\sum_{u:\,u\text{ は }v\text{ の子}}t_u.
\tag{6.2}
\]

**中間節点排除。** `M<t_v<N-M` の節点 `v` があると仮定する。`A_v` のどんな生成組 `\mathbf z` も、`T` 内のこの部分木を差し替えれば成功導出を与える。もし `\mathbf z` が `c` を含めば、差し替えた文は `c` を含み、長さ `N-t_v+\|\mathbf z\|_1>M` となる。これは `M` の定義に反する。よって **`A_v` の生成する全ての組が `c`-free** である。それを `T` に挿入した文は `c`-free であり、仮定から必ず唯一の `W` となる。従って `A_v` のすべての生成組は全成分長の和が `t_v` に等しい。

この節点で用いられた規則を `R` とする。任意の成功導出で `R` が使われると、そこでの `A_v` の生成組の全長は `t_v>M` である。従って、その成功文が `c` を含めば長さが `M` を超えて矛盾し、`c` を含まなければその文は `W` で長さ `N`。すなわち `\theta_G(R)=N`。これは `\theta<N` に反する。従って **木 `T` には `M<t_v<N-M` の節点が存在しない**。

**降下。** `N>\theta+(r+1)M` と仮定して矛盾を示す。根の `t=N` は `N-M` 以上である。`t_v\ge N-M` となる節点 `v` では

\[
t_v\ge N-M>\theta+rM.
\]

(6.2) と子の個数 `\le r`、直接終端数 `\le\theta` より、少なくとも一つの子 `u` は `t_u>M`。中間節点排除により `t_u\ge N-M` でなければならない。同じ議論をその子で繰り返せるが、**有限の導出木を無限に降下することはできない**。矛盾。よって (6.1)。□

**帰結。** ランク `r` 固定で、もし全ての `c` 入り語の長さが `M\le p(\|G\|,\bar\theta_G)` に抑えられる特別な族なら、唯一型1語は `|W|\le\bar\theta_G+(r+1)p(\|G\|,\bar\theta_G)` と多項式長になる。逆に P1 が成立し、`|W_n|=n^{\omega(1)}`、`\bar\theta_{G_n}=n^{O(1)}` なら、**少なくとも一つの `c` 入り語は**

\[
|v_n|\ \ge\ \frac{|W_n|-\bar\theta_{G_n}}{r+1}=n^{\omega(1)}.
\]

これは短い**規則証人**を使う構成を排除しない。単に、標的言語全体を短い `c`-語だけで覆う設計は不可能とする。`M` 自体が巨大な場合に (6.1) は一般の多項式上界を与えない。

## 7. P2の別の部分結果：非純語の計数プロフィールが一つなら二次上界

**命題 7.1。** `L\subseteq\{a,b,c\}^+` に型1の語がただ一つ `W`（長さ `N`）あり、全ての型 `\zeta` の語 `v` において

\[
(|v|_a+|v|_b,\ |v|_c)=(t,j),\qquad j\ge1
\]

が同じであるとする。`L` に reduced good MCFG `G`（任意ファンアウト、任意ランク）があるなら

\[
\boxed{N\le\left\lfloor\frac{(\bar\theta_G+1)^2}{4}\right\rfloor.}\tag{7.1}
\]

`W=a^N` に限らず、`a^{N-1}b`、`ba^{N-2}b`、交互形等にも適用できる。

**証明。** 型 `\zeta` の語が存在しなければ全ての成功文は `W` なので `\bar\theta_G\ge N`。存在する場合、`t\ge N` なら全ての文の長さは `\ge N`（型 `\zeta` 語の長さは `t+j`）、従って `\bar\theta_G\ge N`。`t<N` なら `\lambda=(N-t)/j>0` と置き、各語の正の重みを

\[
\psi_\lambda(w)=|w|_a+|w|_b+\lambda|w|_c
\]

とすると `\psi_\lambda\equiv N` が `L` 全体で成立する。退避稿 `parked/parked_u1_typing_level.tex` の既存の `prop:u1-weight-all-fanout`（正の定重みに対する全ファンアウト二次上界）から `\mu^\star(L,s_U)\le\lfloor(\bar\theta_G+1)^2/4\rfloor`、従って `N\le\mu^\star(L,s_U)` により結論。前二場合でも `N\le\bar\theta_G\le\lfloor(\bar\theta_G+1)^2/4\rfloor` である。□

**注意：** 既存の `prop:u1-weight-all-fanout` は `\psi_\lambda` が定数という仮定を必要とする。この命題は「計数プロフィールが1個」の場合にその仮定を作れる、という**帰着**であって、プロフィールが複数の一般の場合まで証明していない。指数的な `N` と多項式厚さを狙うなら、非純語の `(|w|_{a,b},|w|_c)` は単一プロフィールでも、一本の正の直線 `t+\lambda j=N` 上に全て乗るものでもいけない。

## 8. P1案の修復：全 arity で成立するが二次上界から逃れない言語

`k\ge2,m\ge1` について

\[
H_{k,m}=\{w\in\{a,b,c\}^+:\ |w|_b=|w|_c,\quad |w|_a+k|w|_c=km\}.
\]

**命題 8.1。** `H_{k,m}` は有限で、唯一の型1語は `a^{km}`、しかも**全ての arity `d\ge1`** に対して `(d,s_U)`-tuple-substitutable である。従って有限言語として任意の `f\ge1` で `\mathcal C_{f,s_U}` に属する（有限言語は fan-out1 の CFG をもつ）。

**証明。** `\Phi(w)=(|w|_b-|w|_c,\ |w|_a+k|w|_c)` は `\Sigma^*\to\mathbb Z^2` の加法的準同型であり、`H_{k,m}=\Phi^{-1}(0,km)\cap\Sigma^+`。任意の `d`、タプル `\mathbf x,\mathbf y` と共通受理文脈 `E` があれば、加法性から `\sum_i\Phi(x_i)=\sum_i\Phi(y_i)`。従って**任意の**許容 `F` について `\Phi(F[\mathbf x])=\Phi(F[\mathbf y])`、所属は一致する。型一致を使わないほど強い。`c` が0個なら `b` も0個で `a` がちょうど `km` 個となる。有限性は `0\le|w|_c=|w|_b\le m` と `0\le|w|_a\le km` から従う。□

ところが `\psi_{k-1}(w)=|w|_a+|w|_b+(k-1)|w|_c=km` が全語で一定で、`k-1>0`。したがって既存の定重み命題により、**どんな reduced good 表示にも** `\bar\theta_G\ge2\sqrt{km}-1` が必要である。`km` を指数長にしても多項式厚さの例にはならない。

別の陽性対照として、任意 `N,p,q\ge0, j\ge1` に対し `\{a^N\}\cup\{w:\operatorname{Parikh}(w)=(p,q,j)\}` も全 arity で代入可能。共通受理文脈から得る二語は成分型一致により同じ**出力型**に属し、その型に属する語の Parikh ベクトルは一種類だけだから、挿入タプルの総 Parikh が一致し、任意文脈で所属が保存される。ただし非純語の最大長は `p+q+j` なので、定理6.1により、短い非純語だけで `a^N` を大きな指数長にする**小厚さ表示は存在しない**。

## 9. 三つの未解決問題・作用素の範囲

| 対象 | 今回確定したこと | **確定していないこと** |
|---|---|---|
| `prop:unique-word-route`(ii) | 唯一型1語の長さに対する条件付き線形・二次上界、候補A/Bの全 n 反証 | 無条件の `N\le\operatorname{poly}(\|G\|,\bar\theta)` またはその反例 |
| `op:fanout-two` | 3文字・`s_U` のショートカット/ブロックは使えない。Parikh閉包は定重みに落ちる | `\mathbf{SL}`・`\mathbf{LG}` 境界の決着、ファンアウト2での上界一般論 |
| `op:S1` | ファンアウト1の二値型付けでは既存ブロック族が厚さの二次規模。ショートカットは1穴で失敗 | ファンアウト1の二値型付けで超多項式に達するか |

**もし**原問題どおり `L_n\in\mathcal C_{2,s_U}` と reduced good `G_n`（ファンアウト `\le2`、ランク `\le r_{\max}`、`r_{\max}\ge2`、アルファベットは**固定** `{a,b,c}`）を構成し、`L_n\cap\{a,b\}^+=\{W_n\}`、`|W_n|=n^{\omega(1)}`、`\|G_n\|,\bar\theta_{G_n}=n^{O(1)}` を満たせば、原稿 `lem:type-deletion` と `prop:rare-type` により**どの特徴標本も `W_n` を含む**。したがって総符号長 `\|F\|_+\ge|W_n|+1` が成立する範囲は次のとおり：

- `\mathcal B^{\le r_{\max}}_{2,s_U}`：成立。
- `\mathcal B_{2,s_U}`：成立。
- `L_n` と `L_n\setminus\{W_n\}` **双方**に特徴標本を持つ任意の集合駆動作用素：成立。特に `\mathcal C_{2,s_U}` 全体に特徴標本を持つ任意の集合駆動作用素には成立。

これは条件文であって、今回実際に達成した下界ではない。`L_n\setminus\{W_n\}` のクラス所属は**型1全体の削除**であることから保証される。学習器の計算時間・Gold収束時点・任意のGold学習器への下界は含まない。

`\mathbf{LG}` がファンアウト2でも境界であるか、「ファンアウトを上げると境界が動く」かを**今回証明したわけではない**。ファンアウト1への移植についても、真の2-MCFG構成自体が得られていないため、`op:S1` 否定を含意しない。既存のブロックCFGは比較用の二次例にとどまる。

## 10. 全数検査：実測と証明書

以下の Python 3 プログラムは有限 `L` の全ての語について、**全ての**正の連続部分語の1穴組、および**中間固定部が非空**の2穴組を列挙する。同じ成分型・同じ受理文脈を持つタプル二つについて、受理文脈集合が異なる場合に実際の `E,x,y,F` を返す。有限 `L` のこの判定は列挙範囲に欠落のない全数検査である。一方、有限の複数パラメータ例がPASSしたことは無限族の証明でない。

実行した主要結果：

| 言語 | `|L|` | arity1 | arity2 | 位置づけ |
|---|---:|---|---|---|
| ショートカット `n=1` | 5 | FAIL | FAIL | `c,ac` で衝突 |
| ショートカット `n=2` | 24 | FAIL | FAIL | `aa,a` で衝突 |
| ブロック `k=1,m=2` | 4 | PASS | PASS | 小例の観察 |
| ブロック `k=2,m=2` | 4 | PASS | PASS | 小例の観察 |
| ブロック `k=2,m=3` | 8 | PASS | FAIL | 2穴の明示反例 |
| ブロック `k=3,m=3` | 8 | PASS | FAIL | 2穴の明示反例 |
| `H_{2,2}` | 19 | PASS | PASS | 命題8.1で全長証明済み |
| `H_{3,2}` | 27 | PASS | PASS | 同上 |
| `\{a^8\}\cup\operatorname{Perm}(abc)` | 7 | PASS | PASS | §8の陽性対照 |
| `\{a^8\}` | 1 | PASS | PASS | 単語の分布式と整合 |

例えば `k=2,m=3` では計算機が別の簡単な証明書も出力する：

```text
arity=2, type=(1,1)
E=□a□aa,  x=(a,aa), y=(aa,a)
E[x]=E[y]=aaaaaa
F=□abc□
F[x]=aabcaa   (in L)
F[y]=aaabca   (not in L)
```

`E` の中間は `a`、`F` の中間は `abc` なので**穴間の非空条件を満たしている**。

### 全文コード：`rare_words_exhaustive.py`

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Exhaustive (1,s_U) and (2,s_U) checker; Python 3 stdlib only.
Run on Windows: py -3 rare_words_exhaustive.py

Do not extrapolate PASS from small test cases to infinite families.
"""
from itertools import combinations, product


def kind(word):
    assert word
    return 'z' if 'c' in word else '1'


def occurrences(word, d):
    """All positive d-tuples with strictly positive internal separators."""
    n = len(word)
    for cuts in combinations(range(n + 1), 2*d):
        parts = tuple(word[cuts[2*i]:cuts[2*i+1]] for i in range(d))
        gaps = ((word[:cuts[0]],) +
                tuple(word[cuts[2*i+1]:cuts[2*i+2]] for i in range(d-1)) +
                (word[cuts[-1]:],))
        assert all(parts) and all(gaps[1:-1])
        yield parts, gaps


def fill(gaps, parts):
    return ''.join(gaps[i] + (parts[i] if i < len(parts) else '')
                   for i in range(len(gaps)))


def show(gaps):
    return '□'.join(gaps)


def exhaustive(words, max_arity=2):
    """Return one fully checked violating (E,x,y,F), or None on exhaustive PASS.

    It suffices to enumerate positive tuple occurrences in accepted words:
    a shared accepting context implies both tuples arise that way.
    """
    L = set(words)
    for d in range(1, max_arity + 1):
        context_to_tuples = {}
        tuple_to_contexts = {}
        for w in sorted(L):
            for x, E in occurrences(w, d):
                context_to_tuples.setdefault((tuple(map(kind, x)), E), set()).add(x)
                tuple_to_contexts.setdefault(x, set()).add(E)
        for (types, E), group in context_to_tuples.items():
            seq = sorted(group)
            for i in range(len(seq)):
                for j in range(i + 1, len(seq)):
                    x, y = seq[i], seq[j]
                    dx, dy = tuple_to_contexts[x], tuple_to_contexts[y]
                    if dx == dy:
                        continue
                    F = sorted(dx ^ dy)[0]
                    if F in dy:
                        x, y = y, x
                    assert tuple(map(kind, x)) == tuple(map(kind, y)) == types
                    assert E in tuple_to_contexts[x] & tuple_to_contexts[y]
                    assert fill(E,x) in L and fill(E,y) in L
                    assert fill(F,x) in L and fill(F,y) not in L
                    return dict(d=d, type=types, E=show(E), x=x, y=y,
                                F=show(F), Ex=fill(E,x), Ey=fill(E,y),
                                Fx=fill(F,x), Fy=fill(F,y))
    return None


def shortcuts(n):
    """A0 -> a|c; Ai -> Ai-1 Ai-1 | c; language of An."""
    L = {'a', 'c'}
    for _ in range(n):
        L = {u + v for u in L for v in L} | {'c'}
    return L


def blocks(k, m):
    """All m-block concatenations using a^k and bc."""
    return {''.join(x) for x in product(('a'*k, 'bc'), repeat=m)}


def multiset_words(a, b, c):
    """All *distinct* permutations of a^a b^b c^c; no factorial duplicates."""
    def rec(prefix, counts):
        if sum(counts) == 0:
            yield prefix
            return
        for i, ch in enumerate('abc'):
            if counts[i]:
                nxt = list(counts)
                nxt[i] -= 1
                yield from rec(prefix + ch, tuple(nxt))
    return set(rec('', (a,b,c)))


def saturated(k, m):
    """|b|=|c|, |a|+k|c|=km; finite, all-arity substitutable."""
    return set().union(*(multiset_words(k*(m-j), j, j)
                         for j in range(m+1)))


def two_shell(N, a, b, c):
    """One c-free word and one c-bearing Parikh fiber; require c>=1."""
    assert c >= 1
    return {'a'*N} | multiset_words(a, b, c)


def check(label, L):
    pure = sorted(x for x in L if 'c' not in x)
    print('%s: |L|=%d, pure=%s' % (label, len(L), pure[:3]))
    for d in (1, 2):
        v = exhaustive(L, d)
        print('  arity<=%d:' % d, 'PASS' if v is None else 'FAIL '+str(v))


if __name__ == '__main__':
    for n in (1, 2):
        check('shortcut n=%d'%n, shortcuts(n))
    for k, m in ((1,2),(2,2),(2,3),(3,3)):
        check('block k=%d,m=%d'%(k,m), blocks(k,m))
    for k, m in ((2,2),(3,2)):
        check('saturated k=%d,m=%d'%(k,m), saturated(k,m))
    check('two shells N=8, (a,b,c)=(1,1,1)', two_shell(8,1,1,1))
    check('singleton a^8', {'a'*8})
```

Windows ではファイルとして保存した場合、同じディレクトリで `py -3 rare_words_exhaustive.py` を実行できる。標準ライブラリのみで外部パッケージは不要。計算は生成した有限言語を**完全に列挙**するため、`k,m,n` を大きくすると指数的に増える。`PASS` はその有限ケースに限る。

## 11. 最終評価と次の探索対象

今回、`W=a^N` という形の唯一型1語について、試みた最も自然な二つの圧縮機構の**正確な破綻箇所**を得た。

- **各階層で `c` に短絡**させれば `N=2^n` と `\theta=n+1` は両立するが、同じ `c` を外側文脈に置いたとき短い純部分語の総長が揺らぎ、**1穴でアウト**（§4）。
- **`bc` によるブロック代替**なら小さい1穴試験を通るものの、`a^k` のブロック境界は `W` 自身が誘導する二穴輸送と両立せず、**2穴でアウト**（§5）。
- **Parikh 閉包**に拡大すればすべての arity を証明できる。しかし冪の移行を吸収する最も単純な線形保存量は定重みに落ち、既存の**二次上界**から逃れない（§8）。
- **全ての補助語を短く保つ**設計も、文法の非削除性と規則厚さだけで定理6.1により排除される。真の反例があるなら、**短い規則証人と長い汚染語が同時に共存**し、かつ二穴輸送に閉じた**非線形の計数・順序制約**が必要である。

現時点で一般の P1 肯定構成も、`\mathcal C_{2,s_U}` 全体の多項式長上界も証明できていない。**次の有力なテスト設計**は、複数の `(|w|_{a,b},|w|_c)` プロフィールを持つ有限族について、型別分布の貼合せ補題（§2）と純タプルトレース（§3）で早期に不可能性を判定し、残った場合にだけ reduced good 文法と規則厚さを構築すること。多層化自体を成功の根拠にしない。

### 文献・研究ノートの位置づけ

- 現行 `main.tex`：`prop:rare-type`、`lem:power-transfer`、`thm:doubling-no-lift`、`prop:unique-two-letter-shapes`、`prop:unique-word-route`、`thm:two-letter-content`、付録J。
- 退避 `parked/parked_u1_typing_level.tex`：`prop:u1-weight-all-fanout`。本報告の§7–8の定重み二次上界は**同命題に依存**し、新しい無条件上界とは主張しない。
- R. Yoshinaka, *Efficient learning of multiple context-free languages with multidimensional substitutability from positive data*, *Theoretical Computer Science* **412** (2011), 1821–1831, DOI: `10.1016/j.tcs.2010.12.058`。許容複数穴文脈と学習の既存理論。
- Clark & Eyraud (2007), *Polynomial Identification in the Limit of Substitutable Context-free Languages*, *JMLR* **8**, 1725–1745。1穴代入可能性の基本的な先行研究。

**初出性監査：** §2・§3・§6 の定式化が既知定理と同一かどうかは十分な文献網羅調査を行えておらず、**未確認**。査読付き論文への転記には、定義の微差・既存補題への還元・定理6.1の非削除条件を再監査すること。

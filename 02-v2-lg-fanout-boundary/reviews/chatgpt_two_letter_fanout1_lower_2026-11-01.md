# 二文字・ファンアウト1の下界族設計：単項符号化の一般的不可能性と一穴文脈の剛性

**2026-11-01／第2回独立探索報告**  
**対象**：栗山貴之、`02-v2-lg-fanout-boundary/main.tex`（Git blob `20259d0959400d42cd07e04c40cb3cc38252ce22`）、前回報告 `reviews/chatgpt_two_letter_fanout1_2026-11-01.md`（blob `aa58c0b5c1cc019b8da7a8be4bf979bf632ae263`）、parked および archive の指定資料。  
**問題**：`Σ={a,b}`、内容型付け `c`、ファンアウト1、規則ランク2で、`‖G_n‖, θ̄_{G_n}=n^{O(1)}` かつ純型の最短受理語 `μ=n^{ω(1)}` となる `L_n∈C_{1,c}` を作る。

## 0. 結論・判定一覧

| 番号 | 主張 | 判定 | 根拠 |
|---|---|---|---|
| D1-a | `A↦a^p, B↦a^q, C↦u`（`p,q≥1`、`u` は `b` を含む任意の非空語）で符号化した `K_3` は **必ず** `(1,c)` と `(1,s_{U,2})` の双方に不所属 | **証明済み** | §2、定理2.1、具体的な真因子証明 |
| D1-b | 同じ不所属は **すべての `n≥3`** に成立し、`p,q,u` を `n` ごとに選び直しても回避不能 | **証明済み** | §2、定理2.2 |
| D1-c | `1≤p,q≤4`、`|u|≤4` かつ `b∈alph(u)` の416通りを `n=1,2,3,4` で完全判定 | **観察（全数計算による各固定例の判定）** | §3、スクリプトと実行ログ |
| D2-a | 「純語指数・小さい文法・小さい厚さ・`b` 個数指数種類・語長指数種類・定重量でない」を同時に満たす **未完成の下界候補** を構成 | **証明済み（列挙した量的性質に限る）** | §4.1、命題4.1 |
| D2-b | 上記候補は `n=3` では代入可能でない。段階マーカーとレベルカウンタの有限パラメータ空間を列挙 | **反証／観察** | §4.2–4.3、具体的証人・検査表 |
| D3-a | 有限 `(1,c)`-代入可能言語では、同じ内容の二因子が文脈を共有するとき、一方が他方の真因子ではあり得ない | **証明済み** | §1、補題1.1 |
| D3-b | 同じ外側文脈に異なる長さの純 `a`（または純 `b`）を挿して両方受理することは有限対象では不可能。無限対象では等差的に無限個が強制 | **証明済み** | §5、補題5.1 |
| D3-c | `b`-個数を固定した語の `a`-run 長ベクトルは、正の座標を**一箇所だけ**変えることができない。`a,b` 対称 | **証明済み** | §5、系5.2 |
| D3-d | 内容 `{a,b}` の重複因子 `x,y` の `b`-個数差は、共通の各一穴文脈で同じだけ移る。有限対象では最高・最低 `b` 層に出現禁止の向きが生じる | **証明済み** | §5、補題5.3 |
| 本問題 | `(L_n,G_n)` の超多項式下界族、または無条件多項式上界 | **未解決** | §6 |
| 新しい補題の既刊文献上の新規性 | **未確認** | §7 |

**今回の中心的進展は D1 の完全否定**である。深さ3の偶然の衝突ではない。三文字で異なる `A` と `B` を同じ単項自由半群 `a^+` に送ると、二つの構文木の内部語が *必ず同じ長さ* に潰れる。その結果、受理済み混合語の真因子包含が生じ、有限の一穴代入可能性と矛盾する。`u=b^t`、`u=b a^j b`、任意の複雑な二文字マーカーのすべてに一度で適用される。

## 1. 定義・資料確認と一般的な拒否補題

内容 `c(w)=alph(w)∈{{a},{b},{a,b}}` とし、`s=s_{U,2}` は `s(a)=1,s(b)=ζ` とする。空でない因子 `x` の一穴分布を

\[
D_L(x)=\{(p,q)\in Σ^*\times Σ^*:p x q\in L\}
\]

とする。`L` の `(1,c)`-代入可能性は、`c(x)=c(y)` かつ `D_L(x)∩D_L(y)≠∅` なら `D_L(x)=D_L(y)`、という性質である。`(1,s)` も `c` を `s` に替えた定義である（現行 `main.tex` の `def:class-cmcf`）。今回構成する各言語は**有限**なので文脈は観察された有限集合のままで完全に決まる。

**補題1.1（真因子・共通文脈禁止）。** 有限の `(1,c)`-代入可能言語 `L` と空でない因子 `x≠y` があり、`c(x)=c(y)`、`D_L(x)∩D_L(y)≠∅` なら、`x` は `y` の真の連続因子であってはならない。同様に `y` も `x` の真因子にならない。この主張は任意の型付け `s` で `s(x)=s(y)` を仮定した場合にも成り立つ。

*証明。* `y=p x q`、`|p q|>0` とし、共通文脈を `(U,V)` とする。代入可能性により `D_L(x)=D_L(y)`。まず `U y V=U p x q V∈L` なので `(U p,q V)∈D_L(x)=D_L(y)`、ゆえに `U p y q V=U p² x q² V∈L`。これを繰り返すと `U p^k x q^k V∈L` が全 `k≥0` に対して成立する（帰納的にその文脈を `x` から `y` に移す）。`|p q|>0` なので長さが無限に増え、有限性に反する。□

**系1.2（受理語の同型真因子禁止）。** 有限 `(1,c)`-代入可能言語の二つの相異なる受理語 `w,v∈L∩Σ^+` が同じ内容であるなら、一方を他方の真の連続因子にできない。とくに **混合受理語全体は連続因子順序について反鎖**である。なぜなら `(ε,ε)` が `D_L(w)∩D_L(v)` に入るからである。`(1,s_{U,2})` ではさらに、すべての `b` を含む受理語が同じ `ζ` 型なので、これら全体が反鎖になる。

この補題は、過去の報告で述べられた有限対象の混合語反鎖性を一般の「同型・共通文脈」の形に整理したもの。文献に対する新規定理とは主張しない。

前回までに確認した必要条件も維持する。混合内容の最短語は `≤3(r+1)|V|θ̄`（前回補題1）、長い純 `a^N` には `h_b≥N/((r+1)|V|θ̄)`（前回定理3）、定重量には `μ*≤⌊(θ̄+1)²/4⌋`（parked `prop:u1-weight-all-fanout`）、有限言語の `h_len` 種類には最長語 `≤h_len θ̄`（Astra 2026-10-30 §3.6）が必要。これらの既知の証明は本報告の新成果に数えない。

## 2. D1：すべての `p,q,u` に対する深さ3の厳密な拒否

`K_0={A}` とし、

\[
K_i=\{BxyB:x,y∈K_{i-1}\}\cup\{CxC:x∈K_{i-1}\}.
\]

`P_0=A`, `P_i=B P_{i-1}P_{i-1}B` を純枝の語とする。特に

\[
P_1=BAAB,\qquad P_2=B\,P_1\,P_1\,B.
\]

**定理2.1（一般単項符号化の不可能性）。** `p,q≥1`、`u∈{a,b}^+`、`b∈alph(u)` を**任意**に固定し、符号化準同型 `φ(A)=a^p,φ(B)=a^q,φ(C)=u` とする。このとき有限言語 `φ(K_3)` は `(1,c)`-代入可能でなく、`(1,s_{U,2})`-代入可能でもない。

*証明。* 次の二つの明示的な **`K_3` の語**を取る：

\[
\begin{aligned}
W&=C\,P_2\,C,\\
X&=B\,(CAC)\,P_1\,B,\\
Y&=B\,P_1\,(CAC)\,B,\\
T&=B\,X\,Y\,B.
\end{aligned}
\]

`CAC∈K_1` と `P_1∈K_1` なので `X,Y∈K_2`。したがって `T∈K_3`。また `P_2∈K_2` より `W∈K_3`。具体的な文字列は

```text
W = CBBAABBAABBC
T = BBCACBAABBBBAABCACBB
```

`φ(P_1)=a^{2p+2q}` および `φ(P_2)=a^{4p+6q}`。一方、`P_1 BB P_1` も `A` を4個、`B` を6個含むので

\[
φ(P_1 BB P_1)=a^{4p+6q}=φ(P_2).
\]

この単項像の一致によって、括弧を付けた以下の**厳密な等式**が成り立つ：

\[
\boxed{
φ(T)=\underbrace{a^{2q}u a^p}_{=:R}
\underbrace{(u a^{4p+6q}u)}_{=φ(W)}
\underbrace{a^p u a^{2q}}_{=:S}.}
\tag{D1}
\]

`R,S` は非空であり、`φ(W)` と `φ(T)` はともに `b` を含む（したがって内容 `{a,b}`、U₁ 型 `ζ`）。さらに `φ(W),φ(T)∈φ(K_3)` で前者が後者の**真因子**である。補題1.1または系1.2により、有限言語 `φ(K_3)` はどちらの型付けでも代入可能ではない。□

**注意。** 符号化は単射である必要がない。`u` の始め／終わりが `a` でも、`u` 内の `b` の並びが何であっても、式 (D1) は語の連結の等式として成立する。マーカーを非常に長い `b`-塊にする方法も、`b a^j b` にする方法も、この拒否を回避しない。これは深さ3での構成的反証であって、有限個のコードに対する実験結果の外挿ではない。

**定理2.2（`n≥3` への伝播）。** 定理2.1と同じ任意の符号化について、すべての `n≥3` で `φ(K_n)` は `(1,c)` と `(1,s_{U,2})` の双方に不所属である。特に `p=p_n,q=q_n,u=u_n` を深さごとに選んでも不所属。

*証明。* `W_3=W`, `T_3=T` とし、`i≥3` に対して

\[
W_{i+1}=B\,W_i\,P_i\,B,\qquad T_{i+1}=B\,T_i\,P_i\,B.
\]

各々 `K_{i+1}` の語である。帰納的に `φ(W_i)` は `φ(T_i)` の真因子であり、両者は `b` を含む。前後に共通の `a^q` と `φ(P_i)` を連結しても真因子性は保存される。系1.2から各 `i` で不所属である。証明は `φ` の数値に依存しないので、各 `n` で `φ_n` を選んだ場合にもそのまま適用できる。□

**設計上の教訓。** 失敗の本体は `u` というマーカーではなく、`A` と `B` の**可換な単項像**である。`P_2` と `P_1BBP_1` は三文字語として別物なのに、`A,B` の Parikh 数が一致するため `a^*` への像で識別不能になる。少なくともこの再帰形を保つなら、マーカーの改善ではなく、**純枝の内部構造がこの可換性崩壊を起こさない構成**を作り直す必要がある。

## 3. D1 の完全列挙（深さ1〜4）

指定範囲：`p,q∈{1,2,3,4}`、`u∈{a,b}^{≤4}` で `u` は非空、`b` を含む。`u` は `1+3+7+15=26` 個、従って深さごとに `4×4×26=416` 通り。

| 深さ | `|K_n|` | 試行した符号化 | `(1,c)` 合格 | `(1,s_{U,2})` 合格 |
|---:|---:|---:|---:|---:|
| 1 | 2 | 416 | 416 | 416 |
| 2 | 6 | 416 | 412 | 412 |
| 3 | 42 | 416 | **0** | **0** |
| 4 | 1806 | 416 | **0** | **0** |

`n=2` における不合格の4例は `(p,q,u)=(1,1,aaab),(1,1,aaba),(1,1,abaa),(1,1,baaa)` だけであった。`n=3,4` のゼロ件は計算でも確認し、さらに定理2.1–2.2が**探索範囲を超えて**すべての正整数 `p,q` とすべての `b` 入りマーカーを排除する。

検査は、すべての受理語のすべての**非空連続因子**とその正確な一穴文脈を用いる。異なる二因子の同型・共通文脈が現れたら分布の一致を要求し、不一致なら `(x,y,共有文脈,分離文脈)` を返す。有限言語に対してこれは定義通りの完全な判定である。検査プログラムの実装は §8 に全文掲載し、小さい事例について別実装の直接比較器と合否を突き合わせた。

## 4. D2：量的条件を通過しても一穴代入可能性に失敗する構成

### 4.1 必要条件1〜5を実際にすべて満たす失敗族

**命題4.1（段階マーカー倍増、量的条件の充足）。** `E_0→a`、`1≤i≤n` について

\[
\boxed{E_i\to E_{i-1}E_{i-1}\mid b a^i b,\qquad S=E_n.}
\tag{M}
\]

で定まる CFG `H_n` とその有限言語 `M_n=L(H_n)` は、以下を満たす。

1. `H_n` は rank 2、fan-out 1 の reduced good 文法であり、`‖H_n‖=O(n²)`、`θ̄_{H_n}=O(n²)`。
2. 唯一の純 `a` 受理語は `a^{2^n}` であり、`μ_{\{a\}}(M_n)=2^n`。
3. `M_n` は `b`-出現数 `2,4,…,2^n` をすべて実現するので、`h_b(M_n)≥2^{n-1}`。
4. `M_n` は少なくとも `2^{n-1}+1` 種類の語長を実現する（`E_1` の各葉を `aa` または `bab` にする）。
5. `n≥2` では正の加法重み `|w|_a+λ|w|_b` を全語で一定にする `λ>0` は存在しない。

*証明。* (1) 空収率、削除、置換、無駄な非終端はない。各右辺の明記端末数は `i+2≤n+2`、規則数は `O(n)`、文字列の明記長の総和が `O(n²)`。任意の規則を成功導出で一度使用するには、上位の深さ `≤n` の各段で当該子に進み、兄弟はマーカー枝 `b a^j b`（長さ `≤n+2`）に置けばよい。その規則自身の子にも長さ `≤n+2` の短い収率を入れられる。したがって、最短成功使用語長で定義される各規則厚さは `O(n²)`。

(2) `b` を含まない選択は毎段の二分規則だけなので、唯一の純語の長さは `2^n`。(3) 最上位から `E_1` が `2^{n-1}` 個現れる完全二分導出を固定し、そのうち `k=1,…,2^{n-1}` 個で `E_1→bab`、残りで `E_1→aa` を選ぶと `b` は `2k` 個になる。(4) 同じ導出で全語長は `2^n+k`（`0≤k≤2^{n-1}`）。(5) `E_1` の二収率の重み一致は `2=1+2λ`、すなわち `λ=1/2` を要求する。しかし `E_2` の純枝 `a^4` は重み4、マーカー `ba²b` は重み `2+2λ=3` で異なる。`n≥2` ではこれらを共通の上位導出に埋め込める。□

**しかし (M) は下界族ではない。** `n=3`、`(i=1,2,3)` のマーカーを `bab,baab,baaab` とすると、`M_3` は26語であり、以下の確定した違反がある：

\[
\begin{array}{c|c|c}
&x=\mathtt{aaaab}&y=\mathtt{baabb}\\\hline
\text{共有文脈 }(\varepsilon,\mathtt{abaa})&\mathtt{aaaababaa}\in M_3&\mathtt{baabbabaa}\in M_3\\
\text{分離文脈 }(\mathtt{bab},\mathtt{ab})&\mathtt{babaaaabab}\in M_3&\mathtt{babbaabbab}\notin M_3
\end{array}
\]

`x,y` はともに混合型 `{a,b}`（かつ U₁ 型 `ζ`）である。したがって `M_3∉C_{1,c}` かつ `M_3∉C_{1,s_{U,2}}`。**一般の `n≥3` における (M) の不所属は、この表だけからは主張しない。** 既に本題の (i) を `n=3` で落とすという厳密な失敗の記録である。

### 4.2 複数の候補テンプレートを全探索

`H_i` の別の設計として、同じ二分枝 `E_i→E_{i-1}E_{i-1}` と次の代替枝をそれぞれ試した。各行で `E_0→a`、深さ `n` のすべてのパラメータ列を列挙し、各対象を定義通りに両型付けで調べた。

| 代替枝の形式 | `d_i` 範囲 | `n=2`：合格 `c` / `s`（総数） | `n=3`：合格 `c` / `s`（総数） |
|---|---|---|---|
| `b a^{d_i} b` | 0〜4 | 2 / 1 （25） | **0 / 0** （125） |
| `a^{d_i} b a^{d_i}` | 0〜4 | 1 / 1 （25） | **0 / 0** （125） |
| `b^{d_i} E_{i-1}` | 1〜5 | 0 / 0 （25） | **0 / 0** （125） |
| `b^{d_i} E_{i-1} b^{d_i}` | 1〜5 | 10 / 10 （25） | **0 / 0** （125） |

これは**有限範囲の観察**であり、パラメータをもっと大きくした場合の一般的不可能性を証明しない。例えば `b^{d_i}` の左右の対称印を使えば第2段まで通るものも多いが、第3段で今回の指定範囲の全てが崩れた。これらの失敗を定理2.1の証明と混同してはいけない。

レベルカウンタ型 `E_i→E_{i-1}E_{i-1} | b^i E_{i-1}`（`i=1,2,3`）では、より単純な純型の衝突が出る。`L_3` に `bbbaaaa` と `bbbaaaaa` が両方あるため、`a` と `aa` は共通文脈 `(bbb,aaa)` をもつ。他方、`a^8∈L_3` かつ `a^9∉L_3` なので、文脈 `(ε,a^7)` が両者を区別する。この違反は `c` と `s` の双方に通用する。

### 4.3 乗算をそのまま反復する案と、長さを固定する案

`E_0→a`, `E_i→E_{i-1}E_{i-1} | b` は第2段から `b,bb` を同時に含むので、有限の純 `b` の一意性に反し、**すべての深さ `n≥2` で失敗**する。これは一般 `n` についての証明であり、`E_i→b` を選べば `b`、二分規則の二つの子でともに `b` を選べば `bb` が出るからである。

従来の `L_{m,n}=\{a^{2^m},b\}^{2^n}` は `(1,s)` と `(1,c)` に所属し、純語長 `2^{m+n}` と `θ̄=2^m+2^n-1` を持つ（parked の既知の定理）。`m=n` の二次下界を、追加段で `a`-ブロック内部に再帰的な代替枝を入れて指数積にする試みは、上記の `E_i` 型では一穴衝突を生む。**どんな積の多段化も不可能**とは証明していない。

一方、すべての受理語の長さを大きい一定値 `N` にそろえる方式は、有限でも無限でも `θ̄_G≥N`（すべての規則の最短成功使用語が長さ `N`）となるため、長い純語を**小さい** `θ̄` で維持する下界戦略にはならない。二進数の「値」を `a` の長さだけで表し、すべてを同じ大きさの枠に埋める案は、この単純な厚さ障害に直面する。可変長の符号はこの障害を逃れるが、今回は完全な正例族を構成できなかった。

## 5. D3：一穴文脈が純 run 長の位置をどこまで決定するか

**補題5.1（一穴での純 run 長の一意性）。** `L⊆{a,b}^*` を `(1,c)`-代入可能とする。任意の `P,Q∈{a,b}^*` と `1≤k<ℓ` に対し、もし

\[
P a^k Q\in L,\qquad P a^ℓ Q\in L
\]

なら、すべての `j≥0` について `P a^{k+j(ℓ-k)}Q∈L` が成り立つ。したがって、**有限** `L` では同じ `P,Q` に対して二つの異なる正の純 run 長を受理できない。`a,b` を交換した命題も成り立つ。同じ結論は `(1,s_{U,2})` の対象にも成り立つ。

*証明。* `a^k,a^ℓ` は同じ純型で、`(P,Q)` を共通文脈として持つので、その分布は等しい。`P a^ℓ Q=P a^{ℓ-k}a^k Q∈L` から `(P a^{ℓ-k},Q)∈D_L(a^k)=D_L(a^ℓ)`、従って `P a^{2ℓ-k}Q∈L`。帰納的に同じ文脈を一段ずつ長くして結論を得る。□

**系5.2（同じ `b` 層の run 座標の「一軸差分」禁止）。** 固定した `k≥0` に対し、受理語を `a^{m_0}b a^{m_1}b\cdots b a^{m_k}` という run 長ベクトル `(m_0,…,m_k)∈\mathbb N_0^{k+1}` で表す。有限 `L∈C_{1,c}` の同じ `k` 層に、**他の全座標が等しく、一つの座標だけが相異なる正整数**である二つのベクトルは存在しない。`a` と `b` を交換した文も成立する。

*証明。* 差がある一つの `a` run の外側を `P,Q` に取り、その二つの正の長さに補題5.1を適用する。□

この条件は単なる `h_b` の種類数より**位置情報を含む**。「同じ `b` 個数で複数の語を作る」ためには、他の run も同時に動かすか、run の出現・消滅（長さ0）を使わなければならない。したがって、独立した桁を一つずつ伸縮できる二進符号をそのまま置く設計には障害となる。これだけで `h_b` の上限は得られない。

**補題5.3（混合因子による `b` 層の輸送と端点排除）。** `L∈C_{1,c}` とし、同じ混合内容の因子 `x,y` が文脈を共有するとする。`δ=|y|_b−|x|_b>0` とすると、すべての `P,Q` について

\[
P x Q∈L\quad\Longleftrightarrow\quad P y Q∈L,
\qquad |P y Q|_b=|P x Q|_b+δ.
\]

特に有限 `L` で `B_{\max}=\max\{|w|_b:w∈L\}`、`B_{\min}=\min\{|w|_b:w∈L\}` とすれば、**`x` は最大 `b`-個数の受理語の因子になれず、`y` は最小 `b`-個数の受理語の因子になれない**。

*証明。* 分布一致と単純な計数から最初の主張。最大 `b` 層の語に `x` があれば、同じ文脈で `y` に置換して `B_max+δ` 個の `b` を持つ受理語が生じて矛盾。最小層で `y` を `x` に置換する議論も同様。□

**純語 `a^N` を位置の基準に使うときの限界。** `a^N` 内で `a^k` を切り出した純文脈 `(a^i,a^{N-i-k})` は、混合語の文脈と同じにはなり得ない。混合語を完成させる外側には必ず `b` があるからである。その純文脈で別の `a^ℓ` を受理できると、純語 `a^{N-k+ℓ}` が増え、有限性から `ℓ=k` でなければならない。従って **`a^N` の純文脈を混合の文脈に直接同一視して交換する議論は成立しない**。混合語の位置制御には、`b` を含む同一外側文脈での衝突（補題5.1）か、混合因子による層間輸送（補題5.3）を使わなければならない。

## 6. 到達点、作用素への帰結、残る問題

1. **反例族はまだ構成できていない。** 定理2.1–2.2は **D1型の全候補の否定**であって、`C_{1,c}` の全体を多項式上界で抑えたものではない。今回の D2 の候補も全て不成立または未証明である。`op:S1` は依然未解決。
2. **追加された必要条件。** 有限反例族には、前回の純長・種類数・非定重量の条件に加え、混合受理語が連続因子反鎖であること（系1.2）、正の run 長を一箇所だけ変更できないこと（系5.2）、混合型の同分布交換が `b` 個数層の両端に現れないこと（補題5.3）が必要になる。これらは位置を含む制約だが、まだ `h_b` または `μ_{\{a\}}` を文法サイズの多項式で抑えるものではない。
3. **下界が得られた場合の正確な作用素。** 将来 `L_n∈C_{1,c}`、`\mu_{\{a\}}(L_n)=N_n=n^{ω(1)}` と `‖G_n‖,θ̄_{G_n}=n^{O(1)}` が構成できれば、現行 `main.tex` の `prop:rare-type` により、`\mathcal B^{\le2}_{1,c}`、`\mathcal B_{1,c}` および **`C_{1,c}` 全体に特徴標本を持つ任意の集合駆動作用素**の全特徴標本 `F` に `‖F‖_+≥N_n+1` が成立する（アルファベットは厳密に `{a,b}`）。この主張は任意の Gold 学習器の収束時間の下界ではない。現段階では**仮定法**である。
4. **ファンアウト分離の論理。** そのような `c` の下界族があれば、現行 `thm:two-letter-content` の `f=2` での `O_{r_{max}}(‖G‖³ θ̄^5)` 上界と合わせ、一つの型付けでの分離になる。ただし `s_{U,2}` の否定解決には、別途 **`L_n∈C_{1,s_{U,2}}`** の証明が必要である。`s\preceq c` による包含は一方向のみ（`lem:typing-monotone`）。
5. **次の現実的な方向。** K型二分再帰の「単項像における Parikh 衝突」を最初から防ぐため、同じ `b` 層の run ベクトルを一軸差分から遠ざけながら、混合**全語の連続因子反鎖**を保つ CFG 再帰を設計する必要がある。部分木ごとの `b` 個数を多数実現しながら、ルート混合語の因子包含を予め構文的に禁止する方法が未発見である。

## 7. 参照文献と先行性について

- [現行 `main.tex`](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/main.tex)：`def:class-cmcf`、`prop:rare-type`、`lem:typing-monotone`、`thm:two-letter-content`、`cor:two-letter-semilattice`、`op:S1`、付録 H。確認 blob を冒頭に記した。`f=2` の上界を `f=1` の主張に流用していない。
- [前回の検証済み報告](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/reviews/chatgpt_two_letter_fanout1_2026-11-01.md)：補題1・2、定理3・5、旧 §6–7。README Change log (48) の検証記録も確認。
- [parked U₁ typing-level results](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/parked/parked_u1_typing_level.tex)：`prop:three-letter-family`、`prop:binary-u1-quadratic`、`prop:binary-u1-weight-slice`、`prop:u1-weight-all-fanout`。
- 過去の独立探索：[Astra §2, §3.4, §3.6](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/archive-v1/revision/astra_binary_u1_fanout1_2026-10-30.md)、[Astra exponent](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/archive-v1/revision/astra_binary_u1_fanout1_exponent_2026-10-30.md)、[DeepSeek](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/archive-v1/revision/deepseek_binary_u1_f1_search_2026-10-30.md)。DeepSeek 予想 `τ≤‖G‖θ̄` は反証済みで使用しない。
- A. Clark and R. Eyraud (2007), *Polynomial Identification in the Limit of Substitutable Context-free Languages*, JMLR **8**, 1725–1745, [原著](https://jmlr.org/papers/v8/clark07a.html)。その Definition 3–5 が一穴文脈と代入可能性の基礎を与える。`{a,aa}` の有限例は原著 §6.1 にあり、今回の純 run 補題と方向を共有する。ただし、**定理2.1の符号化禁制や補題5.3に完全に一致する既刊定理の存在は未確認**。本報告は文献上の独立した新規性を主張しない。

## 8. 完全な検証スクリプト（Python 3、標準ライブラリのみ）

以下は実際に実行した全文。ファイル名を `check_two_letter_lower.py` として保存し、Windows では `py -3 check_two_letter_lower.py`。直接比較する遅い参照実装 `check_reference` も含み、合否の一致を確認する。`check_finite` の高速化は、同型因子が一つの文脈を共有したときの分布集合の等しさだけを局所的に維持する方式で、**短い n の成功から一般 n を推論するものではない**。

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Binary content/U1 exhaustive tests. Python 3 standard library only.
Usage (Windows): py -3 check_two_letter_lower.py
"""
from collections import defaultdict
from itertools import product


def content_type(w):
    return (int('a' in w), int('b' in w))


def u1_type(w):
    return int('b' in w)


def check_finite(words, kind='c'):
    """Exact (1,type)-substitutability test for a finite set of nonempty words.

    Return (True, None) or (False, (x,y,common,separating)).
    Contexts are pairs (left,right); both common[x],common[y] must be words.
    At separating, x occurs but y does not.
    """
    L = set(words)
    typing = content_type if kind == 'c' else u1_type
    contexts = defaultdict(set)
    representative = {}
    edges = defaultdict(dict)  # edges[x][y] = common context
    for word in sorted(L, key=lambda w: (len(w), w)):
        for i in range(len(word)):
            left = word[:i]
            for j in range(i + 1, len(word) + 1):
                x = word[i:j]
                ctx = (left, word[j:])
                if ctx in contexts[x]:
                    continue
                for y, common in edges[x].items():
                    if left + y + word[j:] not in L:
                        return False, (x, y, common, ctx)
                key = (typing(x), ctx)
                y = representative.get(key)
                if y is None:
                    representative[key] = x
                elif x != y and y not in edges[x]:
                    # A new common context creates a required equality D(x)=D(y).
                    # Test all previously seen contexts in both directions.
                    for old in contexts[x]:
                        if old[0] + y + old[1] not in L:
                            return False, (x, y, ctx, old)
                    for old in contexts[y]:
                        if old[0] + x + old[1] not in L:
                            return False, (y, x, ctx, old)
                    edges[x][y] = ctx
                    edges[y][x] = ctx
                contexts[x].add(ctx)
    return True, None


def check_reference(words, kind='c'):
    """Slower independent definition-level check for small finite inputs."""
    L = set(words)
    typing = content_type if kind == 'c' else u1_type
    dist = defaultdict(set)
    for w in L:
        for i in range(len(w)):
            for j in range(i + 1, len(w) + 1):
                dist[w[i:j]].add((w[:i], w[j:]))
    factors = sorted(dist)
    for pos, x in enumerate(factors):
        for y in factors[pos + 1:]:
            if typing(x) != typing(y):
                continue
            overlap = dist[x] & dist[y]
            if overlap and dist[x] != dist[y]:
                common = sorted(overlap)[0]
                difference = dist[x] - dist[y]
                if difference:
                    return False, (x, y, common, sorted(difference)[0])
                return False, (y, x, common, sorted(dist[y] - dist[x])[0])
    return True, None


def verify_failure(L, witness, kind='c'):
    x, y, shared, separate = witness
    t = content_type if kind == 'c' else u1_type
    assert t(x) == t(y)
    assert shared[0] + x + shared[1] in L
    assert shared[0] + y + shared[1] in L
    assert separate[0] + x + separate[1] in L
    assert separate[0] + y + separate[1] not in L


def K(n):
    words = {'A'}
    for _ in range(n):
        words = ({'B' + x + y + 'B' for x in words for y in words}
                 | {'C' + x + 'C' for x in words})
    return words


def binary_encode(words, p, q, u):
    dictionary = {'A': 'a' * p, 'B': 'a' * q, 'C': u}
    return {''.join(dictionary[ch] for ch in w) for w in words}


def fixed_marker(n, ds, style):
    """E_0->a; E_i->E_(i-1) E_(i-1) | marker_i."""
    L = {'a'}
    for i in range(n):
        d = ds[i]
        if style == 'bab':
            marker = 'b' + 'a' * d + 'b'
        elif style == 'aba':
            marker = 'a' * d + 'b' + 'a' * d
        else:
            raise ValueError(style)
        L = {x + y for x in L for y in L} | {marker}
    return L


def level_counter(n, ds, style):
    """E_i->E_(i-1) E_(i-1) | b^d E_(i-1) [b^d]."""
    L = {'a'}
    for i in range(n):
        t = 'b' * ds[i]
        if style == 'left':
            alt = {t + x for x in L}
        elif style == 'both':
            alt = {t + x + t for x in L}
        else:
            raise ValueError(style)
        L = {x + y for x in L for y in L} | alt
    return L


def direct_K3_obstruction(p, q, u):
    """Proof certificate, independent of the exhaustive D calculation."""
    P1 = 'BAAB'
    P2 = 'B' + P1 + P1 + 'B'
    W = 'C' + P2 + 'C'
    X = 'B' + 'CAC' + P1 + 'B'
    Y = 'B' + P1 + 'CAC' + 'B'
    T = 'B' + X + Y + 'B'
    assert W in K(3) and T in K(3)
    w, t = [next(iter(binary_encode({v}, p, q, u))) for v in (W, T)]
    left = 'a' * (2 * q) + u + 'a' * p
    right = 'a' * p + u + 'a' * (2 * q)
    assert t == left + w + right and left and right and 'b' in w
    return W, T, len(w), len(t)


def main():
    universe = [''.join(chars)
                for k in range(1, 5)
                for chars in product('ab', repeat=k)
                if 'b' in chars]
    assert len(universe) == 26
    print('D1: p,q in 1..4; u length<=4 with b; 416 cases per n')
    for n in range(1, 5):
        raw = K(n)
        passed = {'c': 0, 's': 0}
        failed2 = []
        for p in range(1, 5):
            for q in range(1, 5):
                for u in universe:
                    L = binary_encode(raw, p, q, u)
                    for typ in ('c', 's'):
                        ok, cert = check_finite(L, typ)
                        if ok:
                            passed[typ] += 1
                        else:
                            verify_failure(L, cert, typ)
                            if n == 2 and typ == 'c':
                                failed2.append((p, q, u))
        print('n=', n, 'K_n size=', len(raw), 'c=', passed['c'],
              'U1=', passed['s'])
        if n == 2:
            print('n=2 failures in c:', failed2)
    print('K3 universal factor witness:', direct_K3_obstruction(2, 3, 'bab'))
    print('D2: explicit marker E_i->E_(i-1)^2 | M_i, d_i in 0..4')
    for style in ('bab', 'aba'):
        for n in (2, 3):
            passed = {'c': 0, 's': 0}
            for ds in product(range(5), repeat=n):
                L = fixed_marker(n, ds, style)
                for typ in ('c', 's'):
                    ok, cert = check_finite(L, typ)
                    if ok:
                        passed[typ] += 1
                    else:
                        verify_failure(L, cert, typ)
            print(style, 'n=', n, 'total=', 5 ** n, 'pass=', passed)
    print('D2: level counters d_i in 1..5')
    for style in ('left', 'both'):
        for n in (2, 3):
            passed = {'c': 0, 's': 0}
            for ds in product(range(1, 6), repeat=n):
                L = level_counter(n, ds, style)
                for typ in ('c', 's'):
                    ok, cert = check_finite(L, typ)
                    if ok:
                        passed[typ] += 1
                    else:
                        verify_failure(L, cert, typ)
            print(style, 'n=', n, 'total=', 5 ** n, 'pass=', passed)
    for name, L in [('marker (1,2,3)', fixed_marker(3, (1, 2, 3), 'bab')),
                    ('counter (1,2,3)', level_counter(3, (1, 2, 3), 'left'))]:
        ok, cert = check_reference(L)
        assert not ok
        verify_failure(L, cert)
        print('explicit counterexample', name, 'size=', len(L), 'witness=', cert)
    # Independent oracle comparison on small and medium cases.
    for p, q, u in ((1, 1, 'b'), (1, 2, 'ba'), (3, 4, 'bb')):
        for n in (1, 2, 3):
            L = binary_encode(K(n), p, q, u)
            for t in ('c', 's'):
                assert check_finite(L, t)[0] == check_reference(L, t)[0]
    print('independent reference cross-check: PASS')


if __name__ == '__main__':
    main()
```

### 実行結果（抜粋なしの主要計数）

```text
D1: p,q in 1..4; u length<=4 with b; 416 cases per n
n= 1 K_n size= 2 c= 416 U1= 416
n= 2 K_n size= 6 c= 412 U1= 412
n=2 failures in c: [(1, 1, 'aaab'), (1, 1, 'aaba'), (1, 1, 'abaa'), (1, 1, 'baaa')]
n= 3 K_n size= 42 c= 0 U1= 0
n= 4 K_n size= 1806 c= 0 U1= 0
K3 universal factor witness: ('CBBAABBAABBC', 'BBCACBAABBBBAABCACBB', 32, 54)
D2: explicit marker E_i->E_(i-1)^2 | M_i, d_i in 0..4
bab n= 2 total= 25 pass= {'c': 2, 's': 1}
bab n= 3 total= 125 pass= {'c': 0, 's': 0}
aba n= 2 total= 25 pass= {'c': 1, 's': 1}
aba n= 3 total= 125 pass= {'c': 0, 's': 0}
D2: level counters d_i in 1..5
left n= 2 total= 25 pass= {'c': 0, 's': 0}
left n= 3 total= 125 pass= {'c': 0, 's': 0}
both n= 2 total= 25 pass= {'c': 10, 's': 10}
both n= 3 total= 125 pass= {'c': 0, 's': 0}
explicit counterexample marker (1,2,3) size= 26 witness= ('aaaaba', 'aaaaaab', ('', 'ab'), ('', 'baa'))
explicit counterexample counter (1,2,3) size= 42 witness= ('a', 'aa', ('bbb', 'aaa'), ('', 'aaaaaaa'))
independent reference cross-check: PASS
```

**最終判定**：D1の指定した単項符号化には、深さ3での**全パラメータに通用する数学的反証**がある。D2では、超多項式に必要な既知の数量的条件のほとんどを同時に実現しても一穴代入可能性が壊れる族を確認した。D3では位置を含む障害を定理化した。しかし、二文字内容型付けのファンアウト1に超多項式データが必要か否か、および `op:S1` の決着は**引き続き未解決**である。

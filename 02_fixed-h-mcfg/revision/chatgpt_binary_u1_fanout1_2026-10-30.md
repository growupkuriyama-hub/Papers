# 二文字 U₁ 型付け・fan-out 1：特徴データ長境界の独立研究（2026-10-30）

**研究対象**：Takayuki Kuriyama, *Polynomial Upper Bounds on Characteristic-Data Length for Multiple Context-Free Languages under Fixed Finite-Semigroup Typing*。  
**正本の取得**：GitHub `growupkuriyama-hub/papers`, default branch `main`, `02_fixed-h-mcfg/main.tex`。  
**取得した main.tex の Git blob SHA**：`25e2d5fbb4cfdd40e15b29f3d5263d72011c887d`（4,051行）。この版の定義・label に基づく。  
**結論の確度**：主問題 (P) の肯定・否定の完全決着には至らなかった。以下に完全証明できた定理、実際の反例、有限計算の事実、未証明の十分条件を厳格に区別する。**文献上の新規性：未調査**。本報告の数学的独立性と先行研究に対する新規性は別問題である。

## 0. 結論要約表

| 主張 | 判定 | 根拠 |
|---|---|---|
| 主問題 (P)：二文字 U₁、f=1、rank≤固定 r≥2 で一様多項式特徴データが存在する | **未解決** | §1, §8 |
| 主問題 (P) の否定：所要の超多項式下界族が存在する | **未解決** | §1, §8 |
| 任意の reduced good CFG に対し、最短純語 a^N が N>θ なら、長さ N 未満の混合語が少なくとも N/((r+1)|V|θ) 個ある | **証明済み** | §3 定理1 |
| 上記混合語は各々 a^i z a^j（z は b を含み |z|≤θ）と書ける | **証明済み** | §3 定理1 |
| |L∩Σ*bΣ*|=M<∞ なら t_typ≤(r+1)|V|θ(M+2) | **証明済み** | §4 定理2 |
| 上記 M が入力サイズ・θ の固定多項式以下となる部分クラスで (P) 型の特徴標本上界がある | **証明済み（条件付き部分クラス）** | §4 系2.1 |
| 有限の置換可能な対象では、同じ一穴文脈に受理される純の異長 a^p,a^q は存在しない | **証明済み** | §5 補題3 |
| `{a^N,w}`（w に b を含む）は任意の N,w で (1,s)-代入可能 | **証明済み** | §5 定理4 |
| `H_{N,k}={a^N}∪{a^i b^k a^{N-k-i}:0≤i≤N-k}` は (1,s)-代入可能 | **証明済み** | §5 定理5 |
| 深い b 挿入と長い純語だけから fan-out 1 で Parikh 飽和が従う | **反証済み** | §5 定理4、例1 |
| 上記固定長族で θ を多項式に保ちつつ N を指数的に伸ばせる | **反証済み**（当該言語族について） | §5 注：どの reduced 表示でも θ=N |
| 小規模文法576候補のうち、完全列挙・検査できた347候補中40候補が代入可能だった | **観測**（普遍命題の証明ではない） | §7、ログ |
| 原稿の三文字倍増族の「中立文字2個」の負の結果を中立文字1個へ移植できる | **未解決／単純合併は失敗** | §6 |

## 1. 主問題と論理的境界

Σ={a,b}, S=U₁={1,ζ}, s(a)=1, s(b)=ζ。f=1、r_max=r≥2 固定。L∈C^{mcf}_{1,s} は (1,s)-代入可能で L∩Σ⁺ は CFL。G は L∩Σ⁺ の reduced good CFG、rank≤r。θ:=θ̄_G≥1、v:=|V|、g:=‖G‖。特徴標本は与えられた演算子 B^{≤r}_{1,s}（および B_{1,s}）に対して評価する。

求める命題 (P) は次の**全称**命題である：固定 r に対して、L と G に依存しない多項式 p_r(g,θ) が存在し、全ての上記 L,G に長さ ‖F‖₊≤p_r(g,θ) の特徴標本 F が存在する。したがって、稀な型の最短語 μ* だけを抑えても肯定は成立せず、原稿 `cor:distribution-representatives` の τ、または直接の標本構成を抑える必要がある。

**本報告では (P) の真偽を確定していない。** §3–§4 の定理は (P) を否定するための構成が必ず指数個の「短い b 欠陥語」を持つ必要を示す。ただし、指数個の混合語の存在自体は矛盾ではない。§5 の反例は fan-out 2 固有の「2穴移送→可換化」を fan-out 1 へ流用できないことを解析的に示す。

## 2. 原稿の定義・既存定理との照合

- `def:standard-mcfg`：CFG の規則 A→ρ(B₁,…,B_q) は rank q、サイズは `|V|+Σ_R(1+q+テンプレート中の端末・変数の出現数)`。本書で θ を計算する際も、右辺の非終端**出現**を変数として数える。
- `def:grammar-properties`：good は λ-free、nondeleting、nonpermuting、nonmerging。f=1 では、各子の単一成分は一度だけ使われ、生成語の連続する因子として残る。零長出力の成分は禁止。
- `def:tuple-substitutable`：d=1 のみ。x,y∈Σ⁺、s(x)=s(y)、共通受理文脈 (u,v) があれば D_L(x)=D_L(y)。**空語を因子として比較しない**。
- `def:reconstruction`：Start/Const/Comp/Link。集合駆動型、全ての有限 F⊆K⊆L について再構成が一致することが特徴標本の条件。非終端ランクの上限 r を超えない。
- `lem:thickness-equivalence`：(i) 各規則の明示端末数≤θ、(ii) 各非終端 B は全成分長≤θ の短い収率 ω_B を持つ、(iv) E_A=(u_A,□,v_A) の固定端末長≤θ、かつ E_A[L_A(G)]⊆L。
- `thm:data-from-typed-thickness`：最短型付き収率長 t_typ の上界から特徴標本を構成。`cor:distribution-representatives` は μ*≤τ≤t_typ および `‖F‖₊≤N_typ(1+2θ+rτ)+1_{ε∈L}` を与える。f=1 なので `N_typ≤3^r g` （fresh identity completion |S♯|=3）。
- `prop:rare-type`：実現型 m の語は全ての特徴標本で必要。集合駆動型のクラス全域作用素についても成立する。本報告はこの下界を勝手に強めない。
- `rem:fanout-one-data`：**中立文字1個の事例は未解決**と明記されている。`prop:three-letter-family`・`cor:typing-level-obstruction`・`app:three-letter-family` は中立文字が2個の事例であり本件へは直ちに移植できない。
- `thm:binary-u1-polydata` と `app:binary-u1`（`lem:app-u1-shallow`, `lem:app-u1-runs`, `lem:app-u1-transfer`, `lem:app-u1-deep`, `lem:app-u1-parikh`）：fan-out 2 では多項式。`lem:app-u1-shallow` と `lem:app-u1-runs` は f=1 へ適用可能だが、**transfer/deep の証明には arity-2 の文脈が必要で f=1 では使えない**。

原稿が L∩Σ⁺ の文法を要求する点に注意。ε∈L でも、以下の短語計数は正語 L⁺=L∩Σ⁺ に関する。特徴標本には ε を別途追加し、符号長に+1する。

## 3. 新たに完全証明した構造的必要条件

### 定理1（最短純語に伴う短い混合語の大量発生）

**主張。** 任意の reduced good CFG G（fan-out=1、rank≤r）が L⁺ を生成し、a^N∈L⁺ が最短の純語（N=μ₁(L,s)）であるとする。θ=θ̄_G、v=|V|。もし N>θ なら、L⁺ は、互いに異なる

\[w=a^i z a^j,\quad i,j\ge0,\quad b\in\mathrm{alph}(z),\quad 1\le|z|\le\theta,\quad |w|<N\]

なる語を**少なくとも**

\[\left\lceil\frac{N}{(r+1)v\theta}\right\rceil\]

個含む。この主張は (1,s)-代入可能性すら必要としない。

**証明。** G による a^N の導出木 T のうち節点数最小のものを選ぶ。T の全節点は純の a 連を導出する：nondeleting 性から子の全端末が根の収率に一回ずつ現れるためである。T の一つの根葉道で、同じ非終端 B が祖先 u と真の子孫 u′ の位置に現れたと仮定する。u の部分木を u′ の部分木で置き換えると、G の正当な導出木を得て、根の語は a^M（M≤N）である。M<N は a^N の最短性に反し、M=N は T の節点最小性に反する。従って道長は v 以下。

節点 u をその収率長 ℓ_u>θ のとき「重い」とする。`lem:thickness-equivalence`(ii) によってその非終端 B_u はある語 z_u∈L_{B_u}(G) を導出し、|z_u|≤θ<ℓ_u である。仮に z_u が純なら、T の u 部分木だけを置き換えた成功導出が a^{N−ℓ_u+|z_u|} を生み、それは a^N より短い純の受理語である。よって z_u は b を含む。

重い節点の反鎖 Q を任意に取る。u∈Q に対し T の u 部分木だけを z_u に置き換えて得る語は、a^N の当該区間だけを短い z_u に取り換えた `w_u=a^{i_u} z_u a^{j_u}` であり、全て L⁺ に属し |w_u|<N である。これらが u によって互いに異なることを示す。二つの区間が元の a^N で左から u、u′ の順に現れるとする。w_u の**最初の b** は、元の u 区間の右端より前に現れる（置換文字列自体が旧区間より短い）。一方 w_{u′} は旧 u 区間の全体を未変更の a のまま保つ。従って w_u≠w_{u′}。ゆえにどの重い反鎖も、その幅は上記の相異なる受理混合語数を超えない。

重い節点は祖先に関して上方閉である。末端の重い節点を F とすると、F は反鎖であり、全重節点は F のいずれかへの根葉道に含まれるので、重節点数 H≤v|F|。一方、根が重いとき、根の各端末は (a) 重節点が規則に明記した文字、または (b) 重節点の重くない子の収率、のいずれかに属する。重節点一つは明示文字を高々 θ 個書き、rank≤r なので重くない子を高々 r 個持ち、それらの長さは各 θ 以下。従って N≤(r+1)θH≤(r+1)θv|F|。よって |F|≥ceil(N/((r+1)vθ))。各 u∈F の異なる混合語 w_u が上記の条件を満たす。□

**重要な読替え。** N が superpolynomial、g・θ が polynomial の候補下界族では、**N より短い混合語だけでも superpolynomial 個**なければならず、それらの b はそれぞれ長さ≤θ の一箇所に収まる。これは下界の否定ではない。文法圧縮によって指数個の混合語を生成することは十分ありうる。

### 補題1.1（型 ζ の短い導出）

**主張。** fan-out 1、rank≤r の reduced good G において、b を含む語を導出する非終端 B は、b を含む長さ≤`2(r+1)vθ` の語を導出する。

**証明。** 完全な出力型精錬の非終端 B_ζ から節点数最小の終端導出木 T を選ぶ。根葉道で同じ「非終端・型」ラベルが繰り返されると、上位部分木を下位で置き換えて正しい型付き導出を短くできるので繰り返しはない。fan-out=1 の非終端・型ラベルは高々 2v 個。根に残る b の一文字を固定し、それを書く節点に至る一つの道だけを残して型を忘れ、道から外れる各子を元の G における長さ≤θ の最短導出で置き換える。残した b は消えない。道の各節点が書く明示端末は≤θ、外側の子は≤r 個かつ各収率≤θ。従って新しい B-収率長≤2v(r+1)θ、型は ζ である。□

## 4. 混合語が疎な場合の**特徴標本そのもの**の上界

### 定理2（有限個の混合語に依存する型付き収率上界）

**主張。** L⁺ は任意の reduced good CFG G（fan-out 1、rank≤r）で生成されるとする。L⁺ に b を含む語が M 個しかない（`M:=|L⁺∩Σ*bΣ*|<∞`）なら、型付き非終端 X の最短収率長の最大 t_typ について

\[ t_{\mathrm{typ}}(G,s)\le(r+1)v\theta(M+2). \]

ここは代入可能性を仮定しない。さらに L∈C^{mcf}_{1,s} なら、二つの原稿の演算子に共通の特徴標本 K があり

\[\boxed{\|K\|_+\le 3^r g\{1+2\theta+r(r+1)v\theta(M+2)\}+\mathbf 1_{\{\varepsilon\in L\}}.}\]

**証明。** 型 ζ の各非終端の短い収率は補題1.1から≤2(r+1)vθ。型1の収率を持つ各非終端 A について、その最短純収率 a^{ℓ_A} の節点数最小の導出木を選ぶ。定理1と**同じ証明**を「成功文脈を通した a^N」ではなく「A 自身の最短純収率」に適用する。途中の置換が純なら A の最短純収率を短縮して矛盾し、重い反鎖の各節点は、短い b 入りの収率をその位置に挿入した相異なる **A からの語**を与える。さらに `lem:thickness-equivalence`(iv) の単一固定文脈 E_A=(u_A,□,v_A) に挿入すると、全て L⁺ に属する相異なる b 入りの語を得る。相異性は E_A の同じ接頭辞・接尾辞を付けても失われない。従って幅≤M。原木の道長≤v、重節点数≤vM。ℓ_A≤θ（重節点0個）または ℓ_A≤(r+1)vθM（1個以上）。どちらも≤(r+1)vθ(M+1)。型ζと合併して `t_typ≤(r+1)vθ(M+2)`。

代入可能性がある場合だけ `thm:data-from-typed-thickness` を適用する。f=1 で精錬後の型付き非終端と規則の総数は `N_typ≤3^r g`。従って上式が得られる。ε の有無は最終 +1 以外の議論に影響しない。□

### 系2.1（多項式個の混合語をもつ部分クラスでの (P)）

**主張。** 固定 r と固定多項式 q について、全ての対象 L,G が `|L⁺∩Σ*bΣ*|≤q(g,θ)` を満たす部分クラスに限れば、`p(g,θ)=3^r g[1+2θ+r(r+1)gθ(q(g,θ)+2)]+1` は特徴標本の一様多項式上界である。

**証明。** 定理2で v≤g、M≤q(g,θ) を代入する。□

**注意。** 「混合語が M 個」は、有限標的そのものの語数が M 以下、という仮定より弱い（純語が無限個でもよい）。しかし一般の (P) は M が指数個または無限の場合も含むため、系2.1は一般の決着ではない。原稿の `cor:distribution-representatives` を使うなら τ≤t_typ があるので同じ結論になる。

## 5. 反例と解析的に決着した小族

### 補題3（有限置換可能言語の純一穴長剛性）

**主張。** L が有限かつ (1,s)-代入可能なら、任意の固定文脈 E=(u,□,v) について、異なる p,q≥1 が `E[a^p],E[a^q]∈L` を満たすことはない。

**証明。** p<q と仮定すると、両因子は型1で共通文脈 E を持つので D(a^p)=D(a^q)。d=q−p>0 とおく。E[a^q] を起点とし、E[a^{q+kd}]∈L が成り立つとき、一穴文脈 `(u a^{q+kd-p}, v)` に a^p を挿入すると E[a^{q+kd}]∈L である。同じ文脈に a^q を挿入すると E[a^{q+(k+1)d}]∈L。帰納的に無限の相異なる語を得るから L 有限に反する。□

特に E=(ε,□,ε) から、有限 L の純受理語は高々一つ。ただし**有限でない**対象ではこの結論を使えない。無限純切片には周期的な受理長が存在しうる。

### 定理4（二語の分離族）

**主張。** 任意の N≥1 および b を含む任意の語 w について、`L={a^N,w}` は (1,s)-代入可能である。

**証明。** 同型 x,y が一つの文脈 E を共有しているとする。x,y が ζ 型なら両 E[x],E[y] は純語 a^N になれないので、同じ唯一の混合語 w に等しい。固定 E に対し挿入語は一意なので x=y。型1なら、E に b が含まれるか否かによって E[x],E[y] は共に混合語側または共に純語側に属する。やはり共に同じ一語に等しいので x=y。従って等型・共通文脈を持つ因子は同一語であり、分布一致は自明。□

**例1（f=2 の深挿入論法の f=1 への移植は偽）。** `L={a^20,a^6ba^6}` は (1,s)-代入可能で、純の長い因子 a^20 と `a^6 b a^6`（6-deep insertion）を持つが、Parikh 飽和ではない（例えば `ba^12∉L`）。従って現行 `lem:app-u1-deep` の結論は f=1 には一般化できない。定理1により、この二語族を小さな θ で指数 N に圧縮することはできない（M=1）。

### 定理5（固定長・単一 b-run 族の完全な代入可能性）

**主張。** 整数 N≥k≥1 に対して

\[H_{N,k}:=\{a^N\}\cup\{a^i b^k a^{N-k-i}:0\le i\le N-k\}\]

は (1,s)-代入可能である。k<N なら H_{N,k} は一般に Parikh 飽和ではない（k≥2 なら b を離した位置の語は不受理）。

**証明。** 同型 x,y に対し共通受理文脈 E=(u,□,v) があるとする。全受理語は長さ N なので |x|=|y|。型1なら x=y=a^{|x|}。型ζの場合、u x v と u y v はともに b^k が一箇所に連続して現れる語である。固定された u または v に b が含まれるなら、総 b 個数は k に等しいから、x,y の b 個数 t も同じ正数であり、x,y はどちらも `a^p b^t a^q` の形である。u に b があれば受理語の唯一の b-run は左境界をまたぐ必要があり、x と y は b で始まる（p=0）；すると長さと t が固定なので x=y。同様、v に b があれば x,y は b で終わる（q=0）ので x=y。両側に b がなければ、x と y はそれぞれ b^k を全て含み、u,v は純語である。今度は**任意の**文脈 F=(p',□,q') について F[x]∈H_{N,k} なら、x が既に b を k 個持つため p',q' は純語でなくてはならず、かつ全語長=Nである。x と y は同じ長さで b^k を一箇所に含むので F[y] も H_{N,k} に属する。逆向きも対称。これで D(x)=D(y)。□

**固定長の注意。** H_{N,k} の全語は長さ N。したがってどの reduced good 表示 G においても、全規則が少なくとも一つ成功導出で使われ、全成功導出語長は N なので、全規則について θ_G(R)=N、従って θ̄_G=N。この族は「代入可能で非可換かつ深い挿入がある」という実在の障害を示すが、**N が大きいのに θ が小さいという下界族ではない**。

## 6. 失敗した構成・見落としてはならない条件

1. **単純倍増と b 短絡**：A₀→a, A_i→A_{i−1}A_{i−1}|b, S=A_n。n=2 では L={aaaa,aab,baa,bb,b}。型ζの x=aab と y=b は文脈 (ε,ε) を共有するが、文脈 (ε,aa) は b を受理して baa∈L、一方 aab を受理せず aabaa∉L。従って (1,s) 不成立。有限検査からでなくこの具体的反例で否定が確定する。
2. **レベル別の b^i**：A_i→A_{i−1}A_{i−1}|b^i。n=2 では代入可能なケースがあるが n=3 で厳密な有限チェックが違反を発見した。b-run を長さで分けるだけでは一般性を証明できない。
3. **全語同長に揃える**：定理5の族はむしろ (1,s) を満たすが、θ=N に固定されてしまう。指数下界には使えない。
4. **f=2 の二穴移送を流用**：a^m の一語中に切断位置が多くあることから、(a^i,a^j) の受理分布を同一視するには、**二つの非空の穴と中央の非空区切り**が必要。一穴ではそもそもその組を比較できない。定理4が深挿入→Parikh 飽和の偽な一般化を具体的に反証する。
5. **長い見かけの型付き収率だけから下界**：Σ⁺ のような言語では、生成木の純収率が指数的でも分布類の最短代表は短い。従って τ と t_typ を同一視して下界を宣言するのは誤り。下界には `prop:rare-type` の μ*、またはクラス全域の集合駆動作用素に対する厳密な識別標本論法が必要。

## 7. 計算検証：範囲・算出式・評価

Python 標準ライブラリのみ。実際のソース・実際のログは本書末尾 §10–§11 に**全文**収録する。

- **判定器**：有限 L の全単語 w と全 `0≤i<j≤|w|` から因子 x=w[i:j] および文脈 E=(w[:i],w[j:]) を列挙。各 D(x) と共有文脈の型別グループを作り、D が一致しない全ての「可能な衝突」に対して違反を探す。有限 L を丸ごと列挙したケースは本来の D と一致（打切りからの偽違反なし）。型は b の存在で判定。
- **解析的に定義した族**：H_{N,k} は N=4,…,11 と k=1,…,N−1 の全52組を再検査し違反なし。さらに二語族 L={a^12,a^3ba^3}, {a^20,a^6ba^6} の違反なしを確認。これらは定理4・5の証明の**補助**に過ぎない。
- **固定長の大きい例**：A₀→a|b, A_i→A_{i−1}A_{i−1}（i=1,2,3）の文法では256語（各長8）を**全て**列挙して検査し違反なし。正確な g=23, θ=8, τ=8, N_typ=22。100語以上の標的を一律に排除していない。
- **体系的な有限・非循環文法の部分カタログ**：非終端 A₀,…,A_{k−1}、k=2,3,4,5；各 i>0 で構造規則の形を8種類中 **0〜5の6種類**から選ぶ（(A_{i−1}A_{i−1}), aAA, AaA, AAa, bAA, AbA）、ただし同一 shape を全階層で使用。二番目の規則は全階層で同一 shortcut モードを用いて `b`, `b^{i+1}`, `ab`, `ba` の4種類。A₀ の代替候補は `{a}`, `{a,b}`, `{a,bb}` の3種類。最上位構造規則の先頭に ε または a のいずれかを付す2種類。**合計4×6×4×3×2=576表現**。各文法は深い側に向かう子しか使わないので有限言語、全非終端 productive/reachable、good、rank≤2、最大テンプレート記号数≤5。
- 各中間言語が3,500語ではなく **1,600語**を越えたら「容量超過」として未検査、残りでも全因子出現数 `Σ_w|w|(|w|+1)/2 >35,000` の場合は時間制限による未検査とした。**「違反」と数えた文法は、言語を完全生成したものだけ**。この制限は実験範囲の制限であって上界の証明ではない。
- 数値計算：最短非終端収率は底から動的計画、最短導出文脈 E_A は上からの動的計画、規則ごとの成功語最短長は `|u_A|+|v_A|+規則明示端末数+子の最短収率長の和` の最大値を θ として**正確に**計算する。置換可能と判定した L の τ_A は `E_A[x]∈L` を満たす x のうち、その A で生成される型と等しい最短長のものを正確に探索して得る（`lem:app-u1-fillers` の f=1 版）。N_typ は実現型付き非終端・各規則の実現する子型の直積から正確に計数。標本上界として N_typ(1+2θ+2τ) を報告。
- 追加の反証的実装テスト：言語の完全生成に成功した480表示全てで定理2の `t_typ≤3|V|θ(M+2)` をアサートし、そのうち `μ₁>θ` である184表示について、b の最初から最後までの区間長≤θ となる N 未満の混合語数が `N/(3|V|θ)` 以上であることをアサートした。どちらも成功したが、普遍的証明の代用ではない。
- 実行結果：576中、言語数上限で96、因子仕事量上限で133を**未検査**。完全検査347のうち307が不合格、40が合格。40のうち100語超のものは0（**別枠256語の完全検査を実施**）。合格表示で最大 τ/θ=1.0、最大 μ₁/(gθ)=0.090909。これら有限の観測から (P) を推論しない。

## 8. 現状の障害と次の検証者に渡す精密な命題

### 肯定に十分な未証明命題 (U)

> **(U)** 固定 r≥2 に対して多項式 q_r が存在し、全ての (1,s)-代入可能な L と全ての reduced good rank≤r 表示 G の各非終端 A について、型1を実現するなら、導出的文脈 E_A で受理される純因子の最短長
> `κ_A := min{k≥1:E_A[a^k]∈L}`
> は q_r(g,θ) 以下である。

ζ の最短収率は補題1.1で O((r+1)vθ)、従って ζ の τ は多項式。純の分布類については `lem:app-u1-fillers`（f=1）により τ_{A,1}=κ_A。よって (U) が真なら `cor:distribution-representatives` から (P) が従う。**(U) は本書では証明していない**。これは高価な型付き**生成**収率でなく分布代表を直接短縮する命題であり、Σ⁺ の反例を回避する形にしてある。

### 否定に十分な未証明命題 (N)

> **(N)** 固定のΣ={a,b}, s(a)=1,s(b)=ζ と rank≤2 の reduced good CFG G_n と有限 (1,s)-代入可能言語 L_n=L(G_n) が存在し、g_nθ_n=n^{O(1)} かつ `L_n∩a⁺={a^{N_n}}`、`N_n=n^{ω(1)}` となる。

(N) が示されれば `prop:rare-type` により全ての特徴標本の長さ≥N_n+1、しかも下界は二つの原稿の再構成演算子**および**クラス全域に特徴標本を持つ任意の集合駆動作用素に及ぶ。**(N) は未証明**（ただし (P) の否定のために純語の指数下界が唯一の方法だとは主張しない）。

**今後の検証ポイント**：純の最短語 a^N に関する定理1の「独立な短い欠陥」混合語が指数個あるとき、一穴代入可能性がどの受理分布の交差を強制するか。短い z による置換位置間の相互作用を、「中央の非空区切りを使う2穴の移送」に頼らずに扱う必要がある。この点は解決していない。

## 9. 論文挿入用 English LaTeX（完全証明した部分結果のみ）

以下の LaTeX は論文本文に別の `\label` を付けて挿入可能な下書きで、**主問題の決着を主張しない**。既存 `lem:thickness-equivalence`・`thm:data-from-typed-thickness` だけを引用する。主定理を追加したと主張する場合には原著者による独立検証を要する。

```latex
\begin{theorem}[Short mixed defects forced by a rare pure word]
\label{thm:binary-u1-short-defects}
Let $G$ be a reduced good CFG of rule rank at most $r$, with
$v$ nonterminals and ordinary thickness $\theta=\bar\theta_G$.
Suppose $L(G)$ contains $a^N$ and $N$ is the smallest length of a
pure word in $L(G)$. If $N>\theta$, then $L(G)$ contains at least
$\lceil N/((r+1)v\theta)\rceil$ distinct words of the form
$a^i z a^j$, where $z$ contains $b$, $|z|\le\theta$, and
$|a^i z a^j|<N$. Substitutability is not required.
\end{theorem}
\begin{proof}
Choose a derivation $T$ of $a^N$ with the fewest nodes. Every subtree
has an all-$a$ yield. No root-to-leaf path repeats a nonterminal:
replacing the upper occurrence by the lower one preserves the
all-$a$ property and cannot increase length (nondeletion); a strict
reduction violates the minimality of $N$, while equality violates
node-minimality. Thus each path has at most $v$ nodes.
Call a node heavy if its yield has length greater than $\theta$.
By Lemma~\ref{lem:thickness-equivalence}(ii), its nonterminal has a
terminal derivation of length at most $\theta$. This shorter yield
must contain $b$, since otherwise replacing the node would give a
pure accepted word shorter than $a^N$.
For an antichain $Q$ of heavy nodes, replace each node separately
by such a short mixed yield. Each replacement produces an accepted
word $a^i z a^j$ of length strictly below $N$. These words are
pairwise distinct: for two disjoint original intervals ordered from
left to right, the first newly introduced $b$ in the earlier
replacement precedes the right endpoint of the earlier interval,
whereas the later replacement preserves that entire interval as
$a$'s. In particular, $|Q|$ does not exceed the number of distinct
short mixed words specified in the theorem.
Heavy nodes are ancestor-closed. If $F$ is their bottom frontier,
then $F$ is an antichain and every heavy node is on one of at most
$|F|$ paths, each of length at most $v$. Thus the number $H$ of heavy
nodes is at most $v|F|$. Each terminal in the root yield is written
by a heavy node or belongs to a nonheavy child of a heavy node.
A heavy node writes at most $\theta$ terminals by
Lemma~\ref{lem:thickness-equivalence}(i) and has at most $r$
children, each nonheavy child having yield length at most $\theta$.
Consequently $N\le(r+1)\theta H\le(r+1)v\theta|F|$.
The distinct replacements at nodes of $F$ establish the claim.
\end{proof}

\begin{theorem}[Polynomial data for targets with few mixed words]
\label{thm:binary-u1-sparse-mixed}
Fix the binary typing $s(a)=1$, $s(b)=\zeta$ and a rule-rank cap
$r\ge2$. Let $L\in\mathcal C^{\mathrm{mcf}}_{1,s}$ and let $G$ be a
reduced good rank-$\le r$ CFG for $L\cap\Sigma^+$, with
$g=\|G\|$, $v=|V|$, $\theta=\bar\theta_G$. If
$M=|L\cap\Sigma^*b\Sigma^*|<\infty$, then
\[
 t_{\mathrm{typ}}(G,s)\le(r+1)v\theta(M+2).
\]
Consequently both $\mathcal B^{\le r}_{1,s}$ and $\mathcal B_{1,s}$
have a common characteristic sample $F$ satisfying
\[
 \|F\|_+\le 3^r g\bigl(1+2\theta+
 r(r+1)v\theta(M+2)\bigr)
 +\mathbf1_{\{\varepsilon\in L\}}.
\]
\end{theorem}
\begin{proof}
First, for a typed nonterminal of type $\zeta$, choose a node-minimal
typed derivation and retain the path to one occurrence of $b$.
No typed label repeats on this path, so it has at most $2v$ nodes.
Replace each off-path subtree by an untyped shortest derivation,
whose yield has length at most $\theta$ by
Lemma~\ref{lem:thickness-equivalence}(ii). The retained $b$ keeps
the root type $\zeta$; each path node writes at most $\theta$
terminals and has at most $r$ off-path children. The resulting
$\zeta$-yield has length at most $2(r+1)v\theta$.
For a nonterminal $A$ realizing type $1$, take a shortest pure yield
$a^\ell$, with a node-minimal derivation among shortest ones.
The path, heavy-node, and antichain arguments of
Theorem~\ref{thm:binary-u1-short-defects} apply at the root $A$.
A short replacement of any heavy node must contain $b$; otherwise
$A$ would have a shorter pure yield. Distinct disjoint-node
replacements remain distinct after filling the fixed derivational
context $E_A$ of Lemma~\ref{lem:thickness-equivalence}(iv), and all
such filled words belong to $L$. Hence the heavy frontier has size
at most $M$, and $\ell\le\max\{\theta,(r+1)v\theta M\}$.
Combining the two types gives
$t_{\mathrm{typ}}(G,s)\le(r+1)v\theta(M+2)$.
By Theorem~\ref{thm:data-from-typed-thickness}, the witness sample
has encoded length at most
$N_{\mathrm{typ}}(1+2\theta+r t_{\mathrm{typ}})
+\mathbf1_{\{\varepsilon\in L\}}$.
For fan-out one the refinement has
$N_{\mathrm{typ}}\le3^r\|G\|$; substitution gives the displayed bound.
\end{proof}
```

## 10. 再現用 Python ソース全文

```python
"""Binary U1 fan-out-one finite-language verifier / structured CFG survey.
Standard library only. Exact for every *retained* finite grammar.
Run: python3 binary_u1_f1_verify.py
"""
from __future__ import annotations
from collections import defaultdict
from itertools import product

CAP = 1600                  # exact-language enumeration cap (NOT a length cutoff)
MAX_TOTAL_FACTORS = 35000 # skip costly exact tests above this work threshold


def typ(w):
    assert w
    return 'z' if 'b' in w else '1'


def distributions(L):
    """ALL nonempty factors and ALL two-sided contexts in finite L."""
    ds, bycontext = defaultdict(set), defaultdict(set)
    for w in L:
        for i in range(len(w)):
            for j in range(i + 1, len(w) + 1):
                x = w[i:j]
                e = (w[:i], w[j:])
                ds[x].add(e)
                bycontext[(e, typ(x))].add(x)
    return ds, bycontext


def check_substitutable(L):
    ds, bycontext = distributions(L)
    for (e, t), members in bycontext.items():
        x = min(members)
        for y in sorted(members):
            if ds[x] != ds[y]:
                witness = min(ds[x] ^ ds[y])
                return False, (x, y, t, e, witness, witness in ds[x])
    return True, (len(ds), len(bycontext))


def rhs_term_count(rhs):
    return sum(len(x) for x in rhs if isinstance(x, str))


def make_grammar(k, shape, shortcut, base, wrap):
    """A0..A{k-1}, strictly decreasing child indices, hence acyclic.

    Base is a family of terminal productions. For i>0 one structural
    production plus one short 'shortcut'. Shapes have <=2 children
    and 2-4 tokens (terminals count by letters), rank <=2.
    """
    P = [[] for _ in range(k)]
    P[0] = [tuple([x]) for x in ('a',) if True]
    if base == 1:
        P[0].append(('b',))
    if base == 2:
        P[0].append(('bb',))
    for i in range(1, k):
        p, q = i - 1, max(0, i - 2)
        main = [
            (p, p), ('a', p, p), (p, 'a', p), (p, p, 'a'),
            ('b', p, p), (p, 'b', p), (p, q), (q, p)
        ][shape]
        if shortcut == 0: t = 'b'
        elif shortcut == 1: t = 'b' * (i + 1)
        elif shortcut == 2: t = 'ab'
        elif shortcut == 3: t = 'ba'
        elif shortcut == 4: t = 'bb'
        elif shortcut == 5: t = 'a' * i + 'b'
        elif shortcut == 6: t = 'b' + 'a' * i
        else: raise ValueError(shortcut)
        P[i] = [main, (t,)]
    # wrap is deliberately a rule-shape change at ROOT (not a new symbol).
    # replace structural rule by a template with an extra terminal at its edge
    if wrap:
        main = P[-1][0]
        P[-1][0] = (wrap,) + main
    return P


def emit_rhs(rhs, values):
    parts = [x if isinstance(x, str) else values[x] for x in rhs]
    return ''.join(parts)


def language(P, cap=CAP):
    L = []
    for i, rules in enumerate(P):
        out = set()
        for rhs in rules:
            options = [[x] if isinstance(x, str) else sorted(L[x]) for x in rhs]
            for pieces in product(*options):
                out.add(''.join(pieces))
                if len(out) > cap:
                    return None
        L.append(out)
    return L


def grammar_metrics(P, L):
    """Exact size, exact rule-thickness, and a shortest E_A=(u,v)."""
    k = len(P)
    size = k + sum(1 + sum(isinstance(x, int) for x in rhs)
                   + sum(1 if isinstance(x, int) else len(x) for x in rhs)
                   for rules in P for rhs in rules)
    smallest = [min(z, key=lambda x: (len(x), x)) for z in L]
    lens = list(map(len, smallest))
    ctx = [None] * k
    ctx[-1] = ('', '')
    for i in range(k - 1, 0, -1):
        if ctx[i] is None:
            continue
        u, v = ctx[i]
        for rhs in P[i]:
            pieces = [x if isinstance(x, str) else smallest[x] for x in rhs]
            for j, token in enumerate(rhs):
                if isinstance(token, int):
                    e = (u + ''.join(pieces[:j]), ''.join(pieces[j+1:]) + v)
                    if ctx[token] is None or (sum(map(len, e)), e) < (sum(map(len, ctx[token])), ctx[token]):
                        ctx[token] = e
    assert all(e is not None for e in ctx), 'not reduced/reachable'
    thickness = max(len(u) + len(v) + rhs_term_count(rhs) +
                    sum(lens[x] for x in rhs if isinstance(x, int))
                    for i, rules in enumerate(P) for rhs in rules
                    for u, v in [ctx[i]])
    return size, thickness, ctx


def exact_representatives(P, L, ctx, root_language):
    # This computes least E_A-filler of every type realized at A.
    # Only for a substitutable target: E_A-filler = distribution class.
    tau = 0
    for i, (u, v) in enumerate(ctx):
        for t in {typ(w) for w in L[i]}:
            vals = []
            for w in root_language:
                if (w.startswith(u) and w.endswith(v)
                        and len(w) > len(u) + len(v)):
                    x = w[len(u):len(w)-len(v) if v else len(w)]
                    if typ(x) == t:
                        vals.append(len(x))
            assert vals, ('missing filler', i, t)
            tau = max(tau, min(vals))
    return tau


def typed_witness_count(P, L):
    types = [{typ(x) for x in lang} for lang in L]
    n = sum(map(len, types))
    for i, rules in enumerate(P):
        for rhs in rules:
            children = [x for x in rhs if isinstance(x, int)]
            n += 1
            for ch in children:
                n *= 1  # no-op; explicit count below
            if children:
                combinations = 1
                for ch in children:
                    combinations *= len(types[ch])
                n += combinations - 1
    return n


def test_model_families():
    print('MODEL one-neutral, one-contiguous-b-run, all N=4..11, k=1..N-1')
    tests = 0
    for N in range(4, 12):
        for k in range(1, N):
            L = {'a' * N} | {'a' * i + 'b' * k + 'a' * (N-k-i)
                            for i in range(N-k+1)}
            assert check_substitutable(L)[0], (N, k)
            tests += 1
    print('MODEL PASS', tests)
    A = {'a' * 7} | {'a' * x + 'bb' + 'a' * (5-x) for x in range(6)}
    B = {'a' * 7} | {'a' * x + 'b' + 'a' * (6-x) for x in range(7)}
    assert check_substitutable(A)[0]
    assert check_substitutable(B)[0]
    print('KNOWN arity1: both 7-letter families PASS; arity2 not tested here')
    for N, c in [(12, 3), (20, 6)]:
        L = {'a'*N, 'a'*c+'b'+'a'*c}
        assert check_substitutable(L)[0]
        print('TWO_WORD_DEEP', N, c, 'PASS', 'Parikh_saturated=False')
    # Separate exact large finite-grammar test: A0 -> a | b,
    # Ai -> A{i-1} A{i-1}. 256 words at n=3 (four nonterminals).
    full = [[('a',),('b',)]]
    for j in range(1,4):
        full.append([(j-1,j-1)])
    lang = language(full)
    assert lang is not None and len(lang[-1]) == 256
    assert check_substitutable(lang[-1])[0]
    sz, th, e = grammar_metrics(full, lang)
    tau = exact_representatives(full, lang, e, lang[-1])
    print('FULL_SHIFT_256 PASS', 'size',sz,'theta',th,'tau',tau,
          'Ntyp',typed_witness_count(full,lang))
    for n in range(1,5):
        def fam(i):
            if i == 0: return {'a'}
            old = fam(i-1)
            return {x+y for x in old for y in old} | {'b'}
        L = fam(n)
        if n <= 3:
            verdict, info = check_substitutable(L)
            print('NAIVE', n, len(L), 'PASS' if verdict else 'FAIL',
                  '' if verdict else repr(info[:4]))


def main():
    test_model_families()
    print('GRAMMAR FAMILY k=2..5; shape=0..5; shortcut=0..3; base=0..2; wrap=(empty,a)')
    print('CAP', CAP, 'MAX_TOTAL_FACTORS', MAX_TOTAL_FACTORS)
    total = huge = heavy = rejected = passing = 0
    sparsity_checks = crowding_checks = 0
    gt100 = 0
    tops = []
    for k, shape, shortcut, base, wrap in product(range(2,6),range(6),range(4),range(3),('','a')):
        total += 1
        P = make_grammar(k,shape,shortcut,base,wrap)
        langs = language(P)
        if langs is None:
            huge += 1; continue
        L = langs[-1]
        g0, theta0, ctx0 = grammar_metrics(P, langs)
        M = sum('b' in w for w in L)
        ttyp0 = max(min(len(w) for w in lang if typ(w)==t)
                    for lang in langs for t in {typ(w) for w in lang})
        assert ttyp0 <= 3*k*theta0*(M+2) # r=2
        sparsity_checks += 1
        pure = [len(w) for w in L if 'b' not in w]
        if pure and min(pure)>theta0:
            N = min(pure)
            defects = sum(len(w)<N and 'b' in w and
                          w.rfind('b')-w.find('b')+1<=theta0 for w in L)
            assert defects*3*k*theta0 >= N, (k,shape,shortcut,base,wrap,N,defects,theta0)
            crowding_checks += 1
        work = sum(len(w) * (len(w)+1)//2 for w in L)
        if work > MAX_TOTAL_FACTORS:
            heavy += 1; continue
        verdict, _ = check_substitutable(L)
        if not verdict:
            rejected += 1; continue
        passing += 1
        if len(L)>100: gt100 += 1
        size,theta,contexts = grammar_metrics(P,langs)
        tau = exact_representatives(P,langs,contexts,L)
        mu1 = min((len(w) for w in L if typ(w)=='1'), default=None)
        muz = min((len(w) for w in L if typ(w)=='z'), default=None)
        Ntyp = typed_witness_count(P,langs)
        bound = Ntyp*(1+2*theta+2*tau)
        score = tau / (size*theta)
        tops.append((score,k,shape,shortcut,base,wrap,len(L),size,theta,tau,mu1,muz,Ntyp,bound))
    tops.sort(reverse=True)
    print('SPARSE_THEOREM_ASSERTIONS', sparsity_checks, 'CROWDING_ASSERTIONS', crowding_checks)
    print('TOTAL',total,'SKIPPED_CAP',huge,'SKIPPED_WORK',heavy,
          'REJECTED',rejected,'PASS',passing,'PASS_LANG_GT100',gt100)
    print('TOP 8 (tau/(size*theta),k,shape,shortcut,base,wrap,|L|,size,theta,tau,mu1,muz,Ntyp,witness_bound)')
    for item in tops[:8]: print(item)
    print('MAX_TAU_THETA', max((round(q[9]/q[8],6) for q in tops),default=0))
    print('MAX_MU1_SIZE_THETA',max((round(q[10]/(q[7]*q[8]),6) for q in tops if q[10] is not None),default=0))
    assert total==4*6*4*3*2
    assert total==huge+heavy+rejected+passing
    print('ALL_ASSERTIONS_PASSED')

if __name__=='__main__': main()

```

## 11. 実行ログ全文

以下は `python3 -u binary_u1_f1_verify.py` による一回の実行の全標準出力である。576候補のうち work/cap で未検査になったものは PASS / REJECTED に混ぜていない。

```text
MODEL one-neutral, one-contiguous-b-run, all N=4..11, k=1..N-1
MODEL PASS 52
KNOWN arity1: both 7-letter families PASS; arity2 not tested here
TWO_WORD_DEEP 12 3 PASS Parikh_saturated=False
TWO_WORD_DEEP 20 6 PASS Parikh_saturated=False
FULL_SHIFT_256 PASS size 23 theta 8 tau 8 Ntyp 22
NAIVE 1 2 PASS 
NAIVE 2 5 FAIL ('aab', 'b', 'z', ('', ''))
NAIVE 3 24 FAIL ('aab', 'b', 'z', ('', 'baa'))
GRAMMAR FAMILY k=2..5; shape=0..5; shortcut=0..3; base=0..2; wrap=(empty,a)
CAP 1600 MAX_TOTAL_FACTORS 35000
SPARSE_THEOREM_ASSERTIONS 480 CROWDING_ASSERTIONS 184
TOTAL 576 SKIPPED_CAP 96 SKIPPED_WORK 133 REJECTED 307 PASS 40 PASS_LANG_GT100 0
TOP 8 (tau/(size*theta),k,shape,shortcut,base,wrap,|L|,size,theta,tau,mu1,muz,Ntyp,witness_bound)
(0.09090909090909091, 2, 0, 0, 0, '', 2, 11, 2, 2, 2, 1, 6, 54)
(0.08333333333333333, 2, 3, 0, 0, '', 2, 12, 3, 3, 3, 1, 6, 78)
(0.08333333333333333, 2, 2, 0, 0, '', 2, 12, 3, 3, 3, 1, 6, 78)
(0.08333333333333333, 2, 1, 0, 0, '', 2, 12, 3, 3, 3, 1, 6, 78)
(0.08333333333333333, 2, 0, 3, 0, '', 2, 12, 2, 2, 2, 2, 6, 54)
(0.08333333333333333, 2, 0, 2, 0, '', 2, 12, 2, 2, 2, 2, 6, 54)
(0.08333333333333333, 2, 0, 1, 0, '', 2, 12, 2, 2, 2, 2, 6, 54)
(0.08333333333333333, 2, 0, 0, 0, 'a', 2, 12, 3, 3, 3, 1, 6, 78)
MAX_TAU_THETA 1.0
MAX_MU1_SIZE_THETA 0.090909
ALL_ASSERTIONS_PASSED
```
## 12. 自己点検表

| 確認項目 | 状態／根拠 |
|---|---|
| 現行 `main.tex` の SHA および全指定 label | 照合済み：§2、blob `25e2d5fbb4cfdd40e15b29f3d5263d72011c887d` |
| 型付け s と Σ は全族で固定 | はい（{a,b}、a→1、b→ζ） |
| fan-out 1 だけを用い、二穴の代入可能性を流用していない | はい。§3–§5 の全論証は一穴文脈のみ。|
| G の reduced/good、rank≤r と θ の元文法への依存 | はい。定理1–2では元の θ、列挙では非循環 good。|
| 普遍的 (P) に必要な全 L、全 G の量化を証明した | **いいえ（未解決）**。部分クラスの多項式上界のみ。|
| μ* と τ/t_typ の差を区別した | はい。§1, §4, §6。|
| 稀な型による下界は全特徴標本を対象とするか | 一般定理は原稿 `prop:rare-type` に従う。本報告から新たな下界族は示していない。|
| ε の扱い | G は L∩Σ⁺。ε∈L の場合は標本に ε を追加し +1。|
| 無限言語を有限打切りで偽判定しなかったか | はい。判定器は明示的な有限言語にのみ使用。列挙は全言語生成完了時のみ判定。|
| 100語超の言語を完全除外していないか | はい。256語の固定長文法を完全検査。|
| 正確な θ、サイズ、τ を計算したか | 完全に列挙した CFG について計算。式を §7 で明示。|
| 実験の制限範囲を正確に記載したか | はい。576候補、容量・仕事量除外数を明示。|
| 新規性の先行文献調査 | **未調査**。新規性を主張しない。|
| 主問題の結論 | **未解決**。肯定・否定をともに証明したと書いていない。|

**最終判断**：現段階では (P) の真偽を宣言しない。独立に確立したのは、定理1の短い混合欠陥語の大量発生、定理2の混合語数パラメータ付き特徴標本上界、有限対象の補題3、および反例定理4・5である。全ての普遍的結論は、それぞれ上記本文中に完全な証明を収めた。文献上の新規性は未調査。

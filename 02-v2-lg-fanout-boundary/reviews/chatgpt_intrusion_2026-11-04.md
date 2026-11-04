# 場合 I の τ：欠損文字の侵入を「短い安全代表の不存在」に還元する

**研究日**：2026-11-04／三文字の核・系列第十九報  
**対象**：栗山貴之論文 #2、`op:fanout-two`、**場合 I（a⁴,b⁴,c⁴ の因子がすべて出現）に限定**  
**正本**：`growupkuriyama-hub/Papers/02-v2-lg-fanout-boundary/main.tex`、Git blob `b72cd2ed648f802886f0ab7c60a72f9f40c0864b`。既報 `chatgpt_typed_case1_2026-11-04.md`、`claude_straddle_2026-11-04.md`、`chatgpt_double_shadow_2026-11-03.md`、`chatgpt_mixed_escapes_2026-11-03.md`、`chatgpt_weighted_codes_2026-11-02.md` を照合した。成果は独立査読前の研究ノートである。

## 0. 主張ごとの判定

| 主張 | 判定 | 根拠・射程 |
|---|---|---|
| **(I1) の正確な安全置換**：重い節点が根の文字証人を含まなければ、その節点の配置に適合する長さ≤θの短い代表は存在しない | **証明済み** | §2、定理2.1。任意の型・fan-out≤2、代入可能性不要。既存のマーク保存法の精密化 |
| 「侵入」の判定は B ラベルだけで十分 | **一般には不正確** | §2。fan-out2 の場合、B の各成分が根のどちらの成分に入るかという配置 `π` が必要 |
| 侵入反鎖幅 `q` による `t_X ≤49(r+1)vθ(3d+q)` | **証明済み／目的にはまだ足りない** | §3。`q` 自体に多項式上界を与える必要がある |
| 各配置 `(B,π)` の侵入反鎖が高々 h なら `t_X≤49(r+1)vθ(3d+4vh)` | **証明済み／条件付き** | §3。最大でも4v種類の配置に分割 |
| 配置ごとに、短い**型欠損を起こさない** B 代表が存在する場合の線形 τ 上界 | **証明済み／容易な特別な場合** | §3。前報の全成分 abc のマーク定理を包含 |
| 2文字影の厚さ θ_Γ が多項式なら、開始型 `{a,b}` の `μ_ab` は多項式 | **証明済み／既存二文字定理への帰着** | §4。`L∩{a,b}⁺∈C_{2,cΓ}`、既存 `thm:two-letter-content` を使用。θ_Γ≤poly(v,θ) は自動ではない |
| 2文字影 H に残る型付き X に対して `τ_L(X)≤τ_{LΓ}(X)` | **証明済み／条件付き** | §4。実際に Γ-only 成功導出内に X が現れることが必要 |
| ファンアウト1の倍増例で μ_ab が指数、θ が線形、侵入反鎖幅も大きい | **証明済み／対象クラス外** | §5。具体的な reduced good 文法を構成するが、**arity 1 の代入可能性に反する**。よって `op:fanout-two` の反例ではない |
| 定理 I の μ_a と短い文脈付き a 穴を同一視すること | **反証済み（既報の再証明）** | §6。全 f で代入可能な L_N における `□bc`。θ を含む上界の反例ではない |
| 一般の場合 I で侵入節点の反鎖幅 `poly(v,θ)`、全 τ の多項式上界 | **未解決** | §7。第三の文字を導入する重い節点の個数制御が残る |
| 今回の定式化の文献上の新規性 | **未確認** | §7。元になるマーク法と二文字定理は原稿にもある |

## 1. 型、代表、前提の監査

`Σ={a,b,c}`、`L∈C_{2,c}`、`G=(V,Σ,P,S,fan)` は `L∩Σ⁺` を生成する reduced good な表示、`fan≤2`、`rank≤r`、`v=|V|`、`θ=\bar θ_G≥1` とする。場合 I は `a⁴,b⁴,c⁴` がそれぞれ L のどこかの受理語の因子となること。`X=A_\mathbf t` は trimmed full yield-type refinement の型付き非終端、`\mathbf t=(t_1,…,t_d)`、`d∈{1,2}`、各 `t_i` は Σ の**空でない**部分集合である。d=1 で7型、d=2 で49型。

原稿 `lem:typed-homogeneity` により X の全導出組が一つの分布同値類 `Cl_L(X)` に入る。`t_X=min_{u∈L_X}||u||_1`、`τ_X=min_{z∈Cl_L(X)}||z||_1≤t_X`。本報で t_X を抑えられれば τ_X も抑えられるが、その逆は不要である。`cor:distribution-representatives` は全型 X の `τ(G,c)` から特徴標本総符号長

`≤ N_typ(1+2θ+rτ(G,c))+1_{ε∈L}`, `N_typ≤8^(2r)||G||`

を与える。逆に、μ_a 一つの上界だけでは τ を制御しない。

**ここで自分で再確認した文法上の事実**：reduced good なので (i) 全導出成分が非空、(ii) 各子成分が一度だけ親テンプレートに埋め込まれ、最後には**ちょうど一つの根成分**に現れる、(iii) 各規則が直接書く終端は θ 文字以下、(iv) 各非終端 B は総長≤θの無型導出組を少なくとも一つ持つ（規則の成功導出を短く取って当該 B の部分木を抜き出す）。同じ型付きラベルが X の最短導出の一つの経路で反復すると、その間の部分木を切除して短縮または節点数減少ができる。従って経路上の節点数≤49v。これらは原稿 `lem:thickness-equivalence` と二文字付録 `lem:app-two-basic(ii)` に含まれる構造事実で、新規の代入補題として扱わない。

## 2. (I1) を配置つきに訂正して厳密化する

### 定義 2.1（配置と短い安全代表）

X の最短組を導く節点数最小の型付き導出 T を固定する。各根成分 i に、その内容 `t_i` にある各文字 x の出現を一つ選んで**印**をつける。印の数は

`M_X = Σ_i |t_i| ≤3d≤6`。

T の節点 u の無型ラベルを B、fan(B)=e≤2 とする。B の各成分 j の文字は、good の非削除・成分ごとの連結規則により、最終根のただ一つの成分 `π_u(j)∈{1,…,d}` へ送られる。この写像 `π_u:{1,…,e}→{1,…,d}` を**根に対する配置**と呼ぶ。全ての π は任意に実現するとは限らないが、高々 `d^e≤4` 種類。

根の型 \mathbf t を固定し、

`β_X(B,π) := min{ ||z||_1 : z∈L_B(G), supp(z_j)⊆t_{π(j)} (1≤j≤e) }`

と定める。値がなければ無限大と約束する。ただし T に実際に現れる (B,π_u) では、元の部分木が条件を満たすので **β は有限**である。`β_X(B,π)>θ` を **θ-侵入配置**と呼ぶ。これは「ある一つの無型最短代表が侵入する」ではなく、**長さ≤θの全ての B 代表が少なくとも一つの禁じられた根成分文字を導入する**という定義である。短い候補が複数ある場合の量化を区別している。

### 定理 2.1（無印重節点の侵入強制）

T の節点 u が `ℓ_u>θ` で、u の部分木が根につけた M_X 個の印を**一つも含まない**とする。このとき

`β_X(B_u,π_u)>θ`。

**証明。** 逆に長さ≤θの安全な B_u の導出組 z があれば、u の部分木を z に置換する。無型文法 G では同じ B_u なので置換は合法。非削除により根全長は `ℓ_u−||z||_1>0` だけ厳密に減る。印はすべて u の外にあるので、各根成分 i は元の `t_i` の**全ての文字を少なくとも一つ**保つ。置換以前にあった無印の文字も元の t_i の範囲内であり、置換部分 z は安全性によってその範囲内だけを使用する。従って置換後の各根成分の内容はちょうど t_i のまま。`prop:output-invariants` の型付けの一意性から短い新導出は型付き X の導出になり、t_X の最短性に反する。∎

**重要な修正点**：侵入を「B が c を短く作れる」とラベルのみで一律に分類してはならない。例えば根の型が `({a,b},{a,c})` なら、短い候補 `(b,c)` は成分1→根1、成分2→根2 の配置では安全だが、配置が逆なら危険である。逆の候補 `(c,b)` なら判断は逆になる。したがって2成分の配置を記録する必要がある。これは論理的な配置例であり、その小文法自体を C_{2,c} の反例と主張していない。

## 3. 侵入反鎖への厳密な還元（ただし上界自体は未証明）

### 定理 3.1（侵入幅パラメータによる t_X 上界）

T の θ-重い節点で `β_X(B_u,π_u)>θ` を満たすものの集合を I とする。その**反鎖幅**を

`q_X(T) := max{|Q|: Q⊆I は T の祖先順序について反鎖}`

とする。このとき

`τ_X ≤ t_X ≤ 49(r+1)vθ (M_X+q_X(T)) ≤49(r+1)vθ(3d+q_X(T))`。

**証明。** θ-重い節点は祖先閉包である。任意の θ-重い反鎖 Q から、印を持つ節点を除く。反鎖の部分木は互いに重ならないので、除かれる節点は M_X 個以下。残る節点は定理2.1により全て I に属するから `|Q|≤M_X+q_X(T)`。前節の経路長上界 `49v` により、全 θ-重い節点数 H は `≤49v(M_X+q_X(T))`。根が θ-軽ければ t_X≤θ。重ければ全ての出力文字は、重い節点の規則が直接書いた終端（節点当たり≤θ）か、重い節点の θ-軽い子の導出（節点当たり高々 r 個、各総長≤θ）に分割される。従って `t_X≤(r+1)θH`。軽い場合も右辺は θ 以上なので同じ式。∎

### 系 3.2（配置別に数えれば十分）

`I` の中で**同じ (B,π)** を持つ節点からなる任意の反鎖の大きさが高々 h なら、配置は高々4v種類なので `q_X(T)≤4vh`、したがって

`τ_X ≤49(r+1)vθ(3d+4vh)`。

特に h が `poly_r(v,θ)` なら目的の τ_X も多項式。**この h の多項式上界は今回示せていない**。`I=∅` の場合は `τ_X≤147d(r+1)vθ` となり、前報の全成分 abc の上界を回収する。全成分 abc なら任意の配置で無型長さ≤θの代表は安全だから、実際 I=∅である。

**ファンアウト1の根 X への簡約。** d=1、根内容を `Γ=t_1` とすれば、配置 π は唯一。θ-侵入配置とは、B が各出力成分を Γ 上に保って導出する**最短の組**の長さ `β_Γ(B)` が θ より大きいことに他ならない。これにより開始型 `{a,b}` の未解決点は、`L_B(G)` の **Γ-only shadow の短い代表**を持たないラベルの反鎖幅に正確に絞られる。既報の補題 L1/M は純粋 a の最短導出のために二文字影の逃げ道を数えたものであり、一般の `X_{ab}` では背景に b が残るので、L1/M の「二つの内部 x-連」禁止や (R) の一次元損失は無条件には移植できない。

## 4. 2文字影 H の型付き代表が使える正確な範囲

### 補題 4.1（影の対象クラス所属）

`Γ⊆Σ` がちょうど二文字とし、`L_Γ=L∩Γ⁺` とする。G の規則のうち Γ 外の終端を直接書くものを削除し、成功導出に現れない部分を刈った文法 H を作る。非削除性により、Γ 上の成功導出は必ず全ての規則が Γ だけを書くので、`L(H)=L_Γ`。H は reduced good、fan-out≤2、rank≤r、`|V_H|≤v`。Γ 上の同内容の非空組が Γ 上の許容文脈を共有すれば、それらは元の L でも共有するので `(2,c)` 代入可能性によって Γ 内の全ての分布が一致する。ゆえに

`L_Γ ∈ C_{2,c_Γ}`。

**注意**：`θ_H=\barθ_H` は必ずしも元の `θ` 以下ではない。Γ-only の成功導出が大変長くなる場合がある。

### 定理 4.2（影に現れる型付き X の代表長移送）

X=A_\mathbf t の**全成分の内容が Γ に含まれ**、かつ G のある Γ-only 成功導出の中に型 X の A 節点が現れるとする。このとき

`τ_L(X)≤τ_{L_Γ,H}(X)≤C_{2,r}|V_H|² θ_H⁴ H_{θ_H}`、

ここで `H_m=Σ_{j=1}^m 1/j`、`C_{2,r}=(r+1)(28r+117)+3` は原稿 `thm:two-letter-content` の f=2 の定数である。

**証明。** 仮定の Γ-only 成功導出から、A の出現を除いた Γ-only の許容文脈 E を得る。good・非空成分により E の二穴間隔は空でない。E は H の型付き X の全導出組だけでなく、**G の無型 A の全導出組も受理する**（ただし Γ-only に限ったときは L_Γ 内で受理）。H における X の代表 z を、同じ内容型をもち H 内の型付き X の組 u と分布同値な最短組として取る。E[u]∈L_Γ、Γ 内での代入可能性により E[z]∈L_Γ。これを元の L で見れば、z は元の X の組 u と内容ベクトルを共有し、かつ同じ許容文脈 E に受理される。原稿の full `(2,c)` 代入可能性より `z∈Cl_L(X)`。ゆえに `τ_L(X)≤||z||=τ_{L_Γ,H}(X)`。後者への上界は、補題4.1で適用資格を確かめた**既刊原稿の二文字定理**そのものである。∎

**系 4.3（開始型 ab）**。`L` に内容 `{a,b}` の語があれば H に開始型 `S_{ab}` が存在し、原稿の開始文脈 `□` により `τ_{L,H}(S_{ab})=μ_{ab}(L)`。従って

`μ_{ab}(L)≤ C_{2,r} v² θ_{\{a,b\}}⁴ H_{θ_{\{a,b\}}}`。

**θ_{\{a,b\}} が poly(v,θ) なら**これは要求する多項式上界。θ_{\{a,b\}} を θ で直接抑えることこそ残る課題である。元の X の外部文脈に c が必須で、X が**どの Γ-only 成功導出にも現れない**場合は、影 H への帰着は使えない。これを隠して「Γ を二文字に制限すれば原稿の二文字定理で全 τ が解ける」とは言えない。

## 5. 指数的侵入の形式文法例と、所属失敗を示す明示証明書

### 例 5.1（tempting but invalid）

任意の n≥1 に対してファンアウト1、ランク2の文法 G_n を

```
S   → A_n b | aaaa | bbbb | cccc
A_0 → a | c
A_i → A_(i-1) A_(i-1) | c    (1≤i≤n)
```

とする。これは reduced good（規則は空でなく、非削除・非置換・非併合；全ラベルが成功導出に現れる）であり、`v=n+2`。正確な規則厚さは `θ_G=max(4,n+2)`。理由：G_n の任意の A_i には一文字 c への逃げ道があり、ある A_i の規則を行使する最短成功導出には上位の各二倍化規則で残る兄弟一文字 c と末尾 b だけが必要なので、A_0 の規則や A_1 の二倍化規則が `n+2`、定数規則が4の最大を達成する。

一方、開始内容 `{a,b}` の語を得るには A_n の c への逃げ道を一度も使えず、全ての A_i を二倍化し、全 A_0 を a にする必要がある。従って

`μ_ab(L(G_n))=2^n+1`。

全ての G_n は `a⁴,b⁴,c⁴` を受理するので、四乗の**出現条件だけ**は場合 I と同じである。根語 `a^{2^n}b` の中の A_i 型の大きな部分木は短い代表 c によって c を侵入させる。例えば n=10、i=5 なら同一深さに32個の A_5 節点があり、その各長さは32、`θ_G=12` より重い。根内容 ab の印が a 一つ、b 一つなら、この32個のうち少なくとも31個は印を含まず、侵入配置である。

**しかしこの言語は `C_{2,c}` に属さない。** 次の **arity 1 の完全な違反証明書**が任意の n≥1 に共通する：`cb,ccb∈L(G_n)`（A_n→c、A_n→A_{n−1}A_{n−1} の両子→c）。一穴文脈 `(ε,b)` は同内容 `{c}` の `c` と `cc` を共に受理する。一方、一穴文脈 `(ccc,ε)` は `c` を受理し `cccc∈L(G_n)` を得るが、`cc` は受理せず `ccccc∉L(G_n)`。ゆえに両者の分布は一致せず、**(1,c)-substitutability に違反**する。従ってこれは超多項式特徴データの下界でも、場合 I の `τ` に対する反例でもない。

なお Γ={a,b} に規則を制限した H_n は、c を書く全規則を失い、A_n の唯一の出力が `a^{2^n}` になるため `θ_{H_n}=max(4,2^n+1)`。補題4.1の `θ_H` を元の θ に置き換えられないことを、**非代入可能な模型で**数量的に示す。

## 6. (I2),(I3) の具体的な停止点

**(I2) について。** `a⁴` がある場合、原稿 `lem:power-transfer` によって異なる a の極大連間の1文字再配分ができる（arity2 の共有文脈を明示するなら `(a,aa)` と `(aa,a)` を `□₁ a □₂` に入れて、双方が `a⁴` を生成する）。しかし再配分は**全語の a 個数を保存**し、非 a 文字の順序も保存する。固定文脈 `E_A` の内部／外部をまたいで a を動かすと **E_A 自体が固定されない**ことがあり、逆に固定すれば侵入した c を消すことはできない。これを、同じ純粋 a 連の長さが短縮できるという主張に読み替えるのは誤り。

**具体的な所属可能言語による非含意の再証明。** `N≥4` として

`L_N = {a⁴,b⁴,c⁴} ∪ {w:Ψ(w)=(N,1,1)}`。

この L_N は有限正則、かつ全ての arity f に対して `(f,c)`-代入可能である。なぜなら異なる受理 Parikh ベクトルは異なる**内容集合**を持つので、同じ型の非空組がある許容文脈で共に受理されれば、その二つの受理語の内容集合が等しいことから Parikh ベクトルも等しい。従って穴の合計 Parikh ベクトルが等しく、任意の他の文脈でも所属は同じになるからである。場合 I の出現条件を満たし `μ_a=4` なのに、文脈 `E=□bc` は `a^N` を受理し、短い純粋 a の穴を一つも受理しない。これは **μ_a のみからの固定穴の短縮**を否定するが、θ に対する反例ではない（前報にも登場した模型）。

**(I3) について。** 場合 I の全文字の連の骨格＋Parikh による所属の決定性が使えても、c のない根成分へ c を導入する無型短縮は、元の語と新語の**骨格そのものを変える**。よって骨格一致を前提とする損失比較 (R) は直ちには使えない。侵入した c を他の場所へ移動する場合も、元の固定文脈と根成分の境界を跨いで c を消してよいという許可は代入可能性からは出ない。補題 F′、E、Q の参照は、それらの仮定に合わせた純粋 a 語または同型の核を構成した場合に限る。一般の X ではその共通核の構成が未達である。

## 7. 結論・先行研究・次に絞る一点

今回 **証明したもの**は、侵入が起こる正確な条件の `(B,π)` ごとの定義、重い反鎖に対する `49(r+1)vθ(3d+q)` 上界、配置ごとの個数に帰着する定量的な十分条件、二文字影への正確な移送範囲である。マーク保存法は前報と原稿の方法の特別な精密化、二文字影の上界は既存の `thm:two-letter-content` の応用なので、新しい学習定理の証明としては扱わない。

**止まった場所**は、場合 I で `(B,π)` ごとの θ-侵入節点が、最短型付き導出の同一深さに何個共存できるかという点。補題 L1/M は純粋語に第三の文字を入れる影の議論で、今回の一般型の背景文字を除去する補題にはなっていない。未所属の倍増文法を反例族に流用することはできない。**場合 I の全 τ 上界も `op:fanout-two` も未解決。** 場合 II・III には結論を拡張していない。今回の細分化と同じ定式化が刊行文献にあるかは**未確認**。

**次に絞るべき一点**：単一成分型 `{a,b}` の最短導出で、`β_{\{a,b\}}(B)>θ` を満たす**同一非終端 B** の θ-重い節点が、反鎖にいくつ現れるか。その節点を短い c-intruding 代表へ二つ同時に替えて得る語を、a⁴,b⁴,c⁴ による再配分と一穴／二穴代入から別の c-free 短縮へ戻せるか。まず「二つの侵入を合流させても c を完全に除去する共通許容文脈」が構成できるかを証明すべきである。

## 8. Python 3 標準ライブラリ：完全な動的計画検査

次は§5の**対象外模型**の支持集合別最短語、規則厚さ（各規則を最低一度使う成功導出の最短長さ）、Γ 影の厚さ、arity1 の反例語、同一深さの侵入節点の数を、有限文法の厳密な動的計画で検査する。`θ` の数値に関する assert は `max(4,n+2)`、影の assert は `max(4,2**n+1)` と説明文に一致させている。ここで得られるのは**対象外の具体文法**についての証明の補助検算であり、無限一般の `(2,c)`-所属判定ではない。

Windows: `py -3 intrusion_audit.py`。標準ライブラリのみ使用。

```python
#!/usr/bin/env python3
"""Exact dynamic program for a non-substitutable doubling obstruction.
Windows: py -3 intrusion_audit.py. Python 3 standard library only.
The model is deliberately OUTSIDE C_(2,c). No learning lower bound is implied.
"""
from functools import lru_cache
from itertools import product

SIGMA='abc'
TYPES=[frozenset(x for x,b in zip(SIGMA, bits) if b)
       for bits in product((0,1), repeat=3) if any(bits)]

def make_grammar(n):
    R={'S': [('A%d'%n, 'b'), ('a','a','a','a'),
             ('b','b','b','b'), ('c','c','c','c')],
       'A0':[('a',),('c',)]}
    for i in range(1,n+1):
        R['A%d'%i] = [('A%d'%(i-1), 'A%d'%(i-1)), ('c',)]
    return R

def profile(R):
    @lru_cache(None)
    def table(N):
        out={}
        for rule in R.get(N,[]):
            states={(frozenset(), 0)}
            for sym in rule:
                if sym in SIGMA:
                    opts={(frozenset((sym,)),1)}
                else:
                    opts=set(table(sym).items())
                nxt={}
                for support,len0 in states:
                    for s,length in opts:
                        key=support|s
                        cost=len0+length
                        nxt[key]=min(nxt.get(key,10**100),cost)
                states=set(nxt.items())
            for s,length in states:
                out[s]=min(out.get(s,10**100),length)
        return out
    return table

def thickness(R):
    @lru_cache(None)
    def shortest(N):
        return min((sum(1 if x in SIGMA else shortest(x) for x in rule)
                    for rule in R.get(N,[])),default=10**100)
    assert shortest('S')<10**100
    all_targets=[(N,i) for N,rs in R.items() for i in range(len(rs))]
    def witness(target):
        @lru_cache(None)
        def cost(N):
            best=10**100
            for j,rule in enumerate(R.get(N,[])):
                direct=sum(1 if x in SIGMA else shortest(x) for x in rule)
                if (N,j)==target:
                    best=min(best,direct)
                else:
                    for index,x in enumerate(rule):
                        if x not in SIGMA:
                            best=min(best,direct-shortest(x)+cost(x))
            return best
        return cost('S')
    return max(witness(target) for target in all_targets)

def is_member(R,w):
    @lru_cache(None)
    def accepts(N,word):
        for rule in R.get(N,[]):
            if test_rule(rule,word): return True
        return False
    def test_rule(rule,word):
        @lru_cache(None)
        def go(i,j):
            if i==len(rule):return j==len(word)
            t=rule[i]
            if t in SIGMA:return j<len(word) and word[j]==t and go(i+1,j+1)
            return any(accepts(t,word[j:k]) and go(i+1,k)
                       for k in range(j+1,len(word)+1))
        return go(0,0)
    return accepts('S',w)

def main():
    assert len(TYPES)==7 and len(TYPES)**2==49
    for n in (1,2,3,6,10):
        R=make_grammar(n)
        H={N:[r for r in rs if all(x!='c' for x in r)] for N,rs in R.items()}
        mu_ab=profile(R)('S')[frozenset(('a','b'))]
        theta=thickness(R)
        theta_H=thickness(H)
        assert mu_ab==2**n+1
        assert theta==max(4,n+2)
        assert theta_H==max(4,2**n+1)
        assert all(is_member(R,w) for w in ('cb','ccb','cccc'))
        assert not is_member(R,'ccccc')
        print('n=%2d v=%2d theta=%2d theta_H=%4d mu_ab=%4d violation=PASS' %
              (n,len(R),theta,theta_H,mu_ab))
    n,i=10,5
    theta=thickness(make_grammar(n))
    assert 2**i>theta
    print('intrusion antichain: n=10 i=5 nodes=%d unmarked >=%d' %
          (2**(n-i),2**(n-i)-1))
    print('ALL EXACT DP TESTS PASSED (candidate not in target class)')

if __name__=='__main__': main()
```

**実測した標準出力（そのまま）**

```text
n= 1 v= 3 theta= 4 theta_H=   4 mu_ab=   3 violation=PASS
n= 2 v= 4 theta= 4 theta_H=   5 mu_ab=   5 violation=PASS
n= 3 v= 5 theta= 5 theta_H=   9 mu_ab=   9 violation=PASS
n= 6 v= 8 theta= 8 theta_H=  65 mu_ab=  65 violation=PASS
n=10 v=12 theta=12 theta_H=1025 mu_ab=1025 violation=PASS
intrusion antichain: n=10 i=5 nodes=32 unmarked >=31
ALL EXACT DP TESTS PASSED (candidate not in target class)
```

**文献**：栗山 #2 現行原稿 `lem:thickness-equivalence`、`lem:typed-homogeneity`、`cor:distribution-representatives`、`thm:two-letter-content`、付録 `app:two-letter-content`。基礎的な分布学習の先行研究には Yoshinaka (2011, *Theoretical Computer Science* 412:1821–1831) 等がある。今回の個々の組合せ補題の公刊先取は未確認。

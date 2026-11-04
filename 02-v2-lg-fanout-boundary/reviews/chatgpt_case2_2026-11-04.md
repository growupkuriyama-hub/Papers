# 場合 II・III の純粋な `a` 語：重い節点の幅、損失の一意性、および残る障害

**2026-11-04／系列第十五報（ChatGPT）**  
対象：栗山貴之、論文 #2、`op:fanout-two`。原稿の自動改稿は行わない。以下の「証明済み」は本報告の明示的な論証についての判定であり、外部査読による認定ではない。

## 0. 判定表（最初に結論）

| 主張 | 判定 | 根拠・限定 |
|---|---|---|
| **最短純粋語の重い節点の幅補題**：`k>θ` なら、`b,c` を少なくとも `k/((r+1)vθ)` 個含む **一つの受理語**が存在する | **証明済み** | §2.2。`(2,c)` 代入可能性を使わない。現行原稿 `lem:unique-word-gap(ii)` の「その型の語が一意」という仮定を、**最短の Γ 語を選ぶ**ことで外した変形。原稿中に近い結果が既にある点に注意 |
| **部分的肯定**：全受理語の非 `a` 文字数が `M` 以下なら `μ_a(L)≤θ[1+(r+1)vM]` | **証明済み、ただし追加仮定付き** | §2.3。場合 II・III の双方、fan-out ≤2・rank ≤r に適用。`M=poly(v,θ)` なら目的の多項式上界。ただし一般の II・III では `M` は有界とは限らない |
| 単一の非 `a` 塊 `F` が異なる `a` 予算 `N<N'` で現れるなら `N'−N≥k` | **証明済み** | §3.1。arity 2 による再配分と arity 1 の代入可能性から直接証明 |
| 上記の二予算が現れるなら `a^{k+j(N'−N)}∈L` が全 `j≥0` で成立 | **証明済み** | §3.1。特に純粋 `a` 部分が有限なら `F` の予算は一意 |
| 観察 (λ) の **無限定義** `λ(F)=k−(F を挟む受理語の a の総数)` は場合 II・III で一意 | **反証** | §3.2。**無限正則言語** `L_k^{II}`, `L_k^{III}` を構成し、arity 1・2 の代入可能性を全称的に証明。同じ `F=bc` に `λ=2` と `2−k` が出る。`k≫θ` の領域の反証ではない |
| `2≤N≤k` の予算だけを使う正規化損失 `λ_k(F)` は一意 | **証明済み** | §3.3。これは元の無限定義より**弱い**。この範囲で `SB(F,d)` があれば `λ_k(F)=d` |
| `SB(P,d),SB(Q,e)` に基づく補題 E の詰め物交換 | **条件付きで再証明** | §3.4。`0≤d≤e≤k−3`、成分内容一致が必要。`λ_k` で置換してよいのもこの範囲のみ |
| 場合 III を「`b` の連だけ縮めた骨格」の定数個の細類で扱う | **未解決** | §4。`c` 配置の情報量は文字列としては任意に増える。34細類の議論をそのまま移すことはできない。代入可能言語内での圧縮不可能性までは示していない |
| 場合 II・III の一般 `μ_a≤poly_r(v,θ)` または反例族 | **未解決** | §5。今回の部分定理は**一般問題を解いていない** |
| {a,b} や {a,b,c} という複数文字の稀な内容型 `μ_m` | **未解決** | §5.2。§2 は最短の **部分アルファベット Γ 上の語**を扱い、内容がちょうど `m` の最短語を扱うわけではない |

## 1. 正本・記号・依存関係

GitHub コネクタで、2026-11-04 時点の `growupkuriyama-hub/Papers` の `02-v2-lg-fanout-boundary/` 以下を取得した。

| ファイル | Git blob SHA |
|---|---|
| `main.tex` | `b72cd2ed648f802886f0ab7c60a72f9f40c0864b` |
| `reviews/chatgpt_verify_case1_2026-11-04.md` | `404a6607a99a28ac138968a912e69f1f6c94f67e` |
| `reviews/claude_straddle_2026-11-04.md` | `7e200775e30a9c4fbfb1ffe78611bb0861d70ee4` |
| `reviews/claude_cross_core_2026-11-04.md` | `e7876722600cdd6741556320fab570ea9e1ea1f8` |
| `reviews/claude_f_branching_2026-11-04.md` | `8877e7151a35b5d9b65dc015dd63cde718101392` |
| `reviews/chatgpt_weighted_codes_2026-11-02.md` | `5b624c550441205ad46333e0f7c9c732d928e465` |
| `reviews/chatgpt_skeleton_diversity_2026-11-02.md` | `0d28618c520c2f470b3c72c7fac1158d67371baf` |

原稿で照合した箇所は `def:standard-mcfg`、`def:grammar-properties`、`def:tuple-substitutable`、`lem:thickness-equivalence`、`prop:abelian-coset-filter`、`prop:rare-type`、`lem:unique-word-gap`、`app:two-letter-content`、`op:fanout-two`。以前の報告の F′、E、E₂、T、N、Q、(R) を**新定理の公理として置かない**。今回は必要な交換を §3 で直接示し、厚さ補題の必要部分を §2.1 で再確認する。前報の定理 I は場合 I に限る既存の到達点として記録するが、本報告でその長大な証明を再度認証したと主張しない。

`Σ={a,b,c}`、`c(w)` は内容、`L∈C_{2,c}` は fan-out ≤2 の MCFL で arity 1 と 2 の内容型付き代入可能性を満たすこと。二穴文脈 `u□₁v□₂w` の固定中間部 `v` は**非空**。`G` は `L∩Σ⁺` の reduced good 表示、`r` はランク上限、`v=|V|`、`θ=\bar θ_G≥1`、`k=μ_a(L)≥5`。文法は `good`、すなわち λ-free、nondeleting、nonpermuting、nonmerging である。すべての新しい主張の証明ではこの定義に従う。

## 2. 新しい部分定理：最小導出の幅から `μ_a` を抑える

### 2.1 厚さについて実際に使用する二事実

**(i) 規則が直接書く終端数は `θ` 以下。** ある規則を一度以上使う成功導出の出力には、その規則が直接書いた終端が、非削除性によって全て残る。従ってその規則を使う成功文の最短長以上の終端は書けない。`θ_G` は規則別の最短成功文長の最大である。

**(ii) 各非終端 `A` には総長 `≤θ` の生成組 `ω_A` が存在。** reduced なので `A` を含む成功導出がある。`A` が子に現れる規則を一つ取り、その規則を使う最短成功文（長さ `≤θ`）の当該子の生成組を取ればよい。`A=S` には開始規則を用いる。非削除性から生成組の総長は成功文長を超えない。これは `lem:thickness-equivalence(i),(ii)` の独立した確認である。

### 2.2 定理 W（最短 Γ 語の幅）

**定理 W（証明済み）。** `Σ` の非空部分集合 `Γ` について `L(G)∩Γ⁺` が空でないとし、

\[
\mu_\Gamma:=\min\{|w|:w\in L(G)\cap\Gamma^+\}.
\]

`G` は reduced good、fan-out は任意の固定値（特に ≤2）、rank ≤r とする。`μ_Γ>θ` なら、ある `w∈L(G)` が存在して

\[
\boxed{|w|_{\Sigma\setminus\Gamma}\ \ge\
\left\lceil\frac{\mu_\Gamma}{(r+1)v\theta}\right\rceil.}\tag{W}
\]

ここで `|w|_{Σ\setminus Γ}` は Γ 外の終端文字数である。**代入可能性は不要。**

**証明。** `Γ⁺` 上の長さ最小の語の導出から、節点数最小の導出木 `T` を取る。すべての節点の出力組の全成分は Γ 上の語である（nondeleting により余分な終端が消えない）。節点 `u` の総出力長を `ℓ_u` とする。

同じ非終端ラベル `A` の節点 `u`、真の子孫 `u'` が一つの根から葉への道に現れたとする。同一ラベルなので `u` を `u'` の部分導出で置換できる。置換後も成功する Γ 語であり、その長さは `μ_Γ−ℓ_u+ℓ_{u'}`。非削除性から `ℓ_{u'}≤ℓ_u`。不等号が真なら `μ_Γ` の最小性に矛盾し、等号なら `μ_Γ` の導出の節点数最小性に矛盾する。よって **T の各道に同じラベルは二度出ず、高さは `v` 以下**。

`ℓ_u>θ` の節点を heavy とする。heavy の祖先は全て heavy である。`T` の出力中の各文字は、ある heavy 節点が規則中で直接書いた文字か、heavy 節点の non-heavy な直接の子の出力に属する。各 heavy 節点が書く終端は高々 `θ` 個、rank は高々 `r`、non-heavy 子の総長は各 `θ` 以下である。heavy 節点数を `H` とすると

\[
\mu_\Gamma\le (r+1)\theta H.\tag{1}
\]

`H` 個の heavy 節点を深さごとに数える。道の長さは `≤v` だから、ある深さに少なくとも `H/v ≥ μ_Γ/((r+1)vθ)` 個の **互いに比較不能**な heavy 節点がある。

これらの節点 `u` それぞれで、§2.1(ii) の `ω_{A_u}`（総長 `≤θ<ℓ_u`）に部分導出を置き換える。もし `ω_{A_u}` が Γ 上だけの組なら、元の最短 Γ 語を短くできてしまう。従って各 `ω_{A_u}` は Γ 外の文字を少なくとも一つ含む。節点は互いに比較不能、規則は nondeleting だから、**一斉置換した成功文には、これら Γ 外の文字が全て残る**。その数は `ceil(H/v)` 以上であり (W) が従う。□

**先行結果との関係。** 原稿 `lem:unique-word-gap(ii)` は `W` が `Γ⁺` に属する唯一の受理語である場合に同型の幅論法を使う。本定理の差分は、`Γ⁺` に他の語が存在しても **長さ最小・その中で節点数最小**を選べば、道上の同一ラベルを排除できる点である。従って「全く新しい幅の原理」ではなく、**既存原稿の補題の仮定を一つ外した拡張**である。文献上の独立新規性は未確認。

### 2.3 系：場合 II・III の有界 impurity 部分クラス

**系 W₂（証明済み）。** `a^k∈L`、`k=μ_a(L)` で、ある有限整数 `M≥0` に対し

\[
\forall w\in L:\quad |w|_b+|w|_c\le M
\]

なら

\[
\boxed{\mu_a(L)\le \theta\bigl(1+(r+1)vM\bigr).}\tag{2}
\]

従って、場合 II または III で **全受理語の非 `a` 文字数が `M=poly(v,θ)` に抑えられる**部分クラスでは、`μ_a(L)=poly_r(v,θ)`。fan-out 1 にも 2 にも適用できる。

**証明。** `k≤θ` なら直ちに (2)。`k>θ` なら定理 W に `Γ={a}` を適用して、少なくとも `k/((r+1)vθ)` 個の `b,c` を含む受理語を得る。一様上界 `M` と比較すれば `k≤(r+1)vθM`。□

**不足点。** `M` は **一つの塊の長さの上限**ではなく、**一つの受理語全体での**非 `a` 文字数の上限である。依頼の「各塊の長さ ≤θ」だけから `M≤poly(v,θ)` とは言えない（短い塊を多数並べられる）。この違いを曖昧にして一般の場合を解いたとはしない。

## 3. 観察 (λ) の精密化と、場合 II・III の反例

### 3.1 定理 Δ（同じ塊の二つの `a` 予算は k 以上離れる）

`F∈{b,c}⁺` とし、`B(F)={N≥2 : ある s,t≥1, s+t=N について a^sFa^t∈L}` とおく。

**定理 Δ（証明済み）。** `k=μ_a(L)≥5`、`L` が arity 1・2 の内容型付き代入可能性を満たすとき、異なる `N<N'` が `B(F)` にあれば `h=N'−N≥k`。さらに

\[
\forall j\ge0:\ a^{k+jh}\in L.\tag{3}
\]

**証明。** まず **二穴による `a` の再配分**を、以前の報告から借りずに確認する。二組 `(a,aa)` と `(aa,a)` は各成分内容 `{a}` が一致し、許容文脈 `□₁ a □₂ a^{k-4}` に代入するとどちらも `a^k∈L` になる。よって arity 2 により分布が等しい。`a^sFa^t∈L` で `s≥2,t≥1` なら、文脈 `a^{s-2}□₁F□₂a^{t-1}` に代入して `a^{s-1}Fa^{t+1}∈L` を得る。逆方向も同様。従って `s+t=N` を保つ全ての正の分配が受理される。

特に `aFa^{N-1}∈L` と `a^{h+1}Fa^{N-1}∈L` が成立する。共通の一穴文脈 `□Fa^{N-1}` は `a` と `a^{h+1}` をともに受理し、型も `{a}` で一致する。arity 1 により

\[
D_L(a)=D_L(a^{h+1}).\tag{4}
\]

`a^k∈L` において `a` 一個を `a^{h+1}` に交換すれば `a^{k+h}∈L`。これを繰り返すと (3)。もし `0<h<k` なら、(4) を逆向きに使い、`a^k=a^{k-h-1}a^{h+1}` から `a^{k-h}∈L` が従い、`k` の最小性に反する。従って `h≥k`。□

**帰結。** `L∩a⁺` が有限なら、どの `F` も `B(F)` は高々一要素。しかし `L∩a⁺` が無限なら、上記だけでは全ての予算が等しいとは言えない。

### 3.2 **場合 II と III の双方に属する反証模型**

任意の `k≥5` に対し、次の **無限正則言語**を定義する。

\[
\begin{aligned}
L_k^{\mathrm{II}}&=\{w\in\{a,b,c\}^+: |w|\equiv0\pmod{k},\ |w|_b\le1,\ |w|_c\le1\},\\
L_k^{\mathrm{III}}&=\{w\in\{a,b,c\}^+: |w|\equiv0\pmod{k},\ |w|_c\le1\}.
\end{aligned}\tag{5}
\]

これらは正則、従って fan-out 1 の CFG、ひいては fan-out 2 の MCFG で生成できる。正則表現／有限 DFA を右線形の λ-free 文法に変換し、到達不能・非生産的非終端を除去すれば reduced good の fan-out 1・rank ≤1 表示も存在する。**これは小さな厚さでの反例を作ったという主張ではない**。

**arity 1・2 の完全な証明（実は全 arity）。** `d≥1`、`x=(x₁,…,x_d)`、`y=(y₁,…,y_d)` の各成分は非空で内容が等しいとする。共通受理文脈 `E` があると仮定する。両方とも (5) に属するので、`|x|_\mathrm{tot}−|y|_\mathrm{tot}` は `k` の倍数である。場合 II では、全ての `x_i,y_i` における `b,c` の出現数は各文字ごとに `0` または `1`、しかも内容一致から**成分ごとに同数**である。場合 III では `c` について同じことが成り立つ。従って任意の別の許容文脈 `E'` について、`E'[x]` と `E'[y]` の必要な文字数制約は同値であり、全長も `k` を法として一致する。両者は同時に受理または同時に不受理となり、`D_L^{(d)}(x)=D_L^{(d)}(y)`。これは **全ての文脈**についての議論なので、arity 1・2 を省略せず証明している。□

場合 II は全受理語で `b,c` がそれぞれ高々1回なので `b⁴,c⁴` とも現れない。場合 III は `c⁴` が現れず `b^k∈L_k^{III}` なので `b⁴` は現れる。両者で `a^k∈L` かつ `μ_a=k`。

`F=bc` を取ると、任意の正の `s,t` で `s+t=k−2` のときも `s+t=2k−2` のときも `a^sbc a^t∈L` である。従って

\[
\underbrace{k-(k-2)}_{\lambda=2}\ne
\underbrace{k-(2k-2)}_{\lambda=2-k}.\tag{6}
\]

特に `k=5` では同じ `F=bc` に `λ=2` と `λ=−3` が現れる。`F` は `SB(F,2)` を持つ（`s+t=3` の全配分が受理される）。**したがって、観察 (λ) の無限定義は文字通りには関数ではない。** 差は正確に `k` で、定理 Δ の間隔下界は鋭い。

**重要な限定。** この例では全ての非空受理語の長さが少なくとも `k` だから、任意の reduced good 表示の規則厚さは `θ≥k`。従って `k≫θ` を仮定して動かす前報の型板・損失推論への反例ではない。また (5) は `μ_a` の超多項式反例族ではない。

### 3.3 正規化した損失は関数になる

定理 Δ から `B(F)∩[2,k]` は高々一つの整数である。存在するとき

\[
\lambda_k(F):=k-N\quad(N\in B(F)\cap[2,k])\tag{7}
\]

と定義すれば、**`0≤λ_k(F)≤k−2` の一意な部分関数**となる（定義されない `F` もある）。`F` が `SB(F,d)`、`0≤d≤k−2` を持てば `N=k−d` が (7) の範囲なので `λ_k(F)=d`。

従って前報の分岐 (B) で**既に証明された** `SB` 鎖の損失和 `d_1+…+d_m≤k−2`、分岐 (S) の**既に証明された** `SB` 入れ子の損失和 `e_1+…+e_m+d_P≤k−2` は、それぞれ `λ_k` の値として一意に読める。これは連結一般に対する無条件の加法性ではなく、**実際に SB が構成された範囲に限る**。前報の鎖・入れ子そのものを今回新規に証明したと主張しない。

### 3.4 補題 E の直接照合：交換は正規化された範囲で成立

`P,Q` が非 `a` 語で**同じ内容**を持ち、`SB(P,d)`、`SB(Q,e)`、`0≤d≤e≤k−3` とする。すると `a^{1+e-d}P`、`aQ` はともに内容 `{a}∪c(P)` を持ち、一穴文脈 `□a^{k-e-1}` において両方の像が受理される（`SB` で `s,t≥1`、および `k-e-1≥2`）。arity 1 から

\[
\boxed{D_L(a^{1+e-d}P)=D_L(aQ).}\tag{8}
\]

これが前報の補題 E。`d=λ_k(P)`、`e=λ_k(Q)` と書ける **定義済み・範囲内の場合**に限って、提案された交換式を結論できる。`λ` の無限定義を使って指数を負にするような式は意味を持たない。

## 4. 場合 III の骨格に関する到達点

`b⁴` だけが現れるなら、`b` 連の内部再配分に利用できる共通二穴文脈はあるが、`c⁴` が現れないので同じ論法で `c` 連を自由に縮められない。従って場合 I の補題 Q で使われた「先頭文字と連数による定数次元の指標」は、そのままでは `c` の**正確な配置**を記録できない。

例えば非 `a` 語 `F_m=(bc)^m`（`m≥1`）は全て `c⁴` を含まず、`b` 連を1文字に縮めた骨格 `σ_b(F_m)` は互いに異なる。`m` を動かすと、このような骨格は無限種類ある。これは**語の組合せ論の事実**であり、同一の `L∈C_{2,c}` でこれら全てを関係のある殻として実現したという主張ではない。したがって「場合 III でも細類が34個で済む」という直接移植は正当化できないが、別の不変量や作用で有限次元に圧縮できる可能性は残る。

また前報の「場合 II の殻の両側は二連以上」「同文字境界の連長和 ≤3」は、その殻・境界が**実際に構成される**場合にのみ適用する。本報告の (5) のような所属を自力で確かめた言語には、その条件を前提にする必要もない。

## 5. 残った問い、否定側の資格、新規性

### 5.1 一般問題は未解決／次に絞る一点

今回証明した幅の算術は、最小純粋語の導出 `T` に対し、

\[
W(T):=\max_j\#\{u\text{ at depth }j:\ell_u>\theta\},\qquad
k\le(r+1)v\theta\,W(T)\quad(k>\theta)\tag{9}
\]

という**単純な十分条件**を与える。`W(T)=poly_r(v,θ)` が示せれば、場合 II・III とも解ける。しかし (5) の例でも、`b,c` の4連を避けながら多数の非 `a` 文字を持つ語があるため、ただ「異なる heavy 節点を全部短い非 `a` 生成組に替える」だけでは矛盾は出ない。

**次に絞る一点**は次である：**場合 II・III の代入可能性（特に部分語をまたぐ二穴比較）を使って、純粋 `a` 最小導出の同一深さにある heavy 節点の反鎖幅 `W(T)` に、多項式上界を与えられるか。** 分岐 (B) の鎖・分岐 (S) の入れ子を生成して、その中の異なる置換群から `b⁴/c⁴` または短い純粋 `a` 語を強制する必要がある。

逆に否定側で超多項式 `k` を実現するなら、(9) から**超多項式の heavy 反鎖幅**が必須となる。この必要条件は普通の倍増木では自然に起きるが、以前の偶数塊の二穴違反を避ける生成語も同時に用意しなければならない。

### 5.2 複数文字の稀な型

定理 W を `Γ={a,b}` にすると「`a,b` **だけで書かれた**最短語」の長さは扱える。しかしそれが純 `a` 語でもよいため、`c(w)={a,b}` という**ちょうど両文字を持つ**最短語 `μ_{\{a,b\}}` の評価にはならない。これを同値と言い換えない。混合型の最短導出で短縮した際に `b` が消えて内容が `{a}` に落ちることが、残る本質的障害である。

### 5.3 特徴標本下界の条件（今回 **新しい下界なし**）

もし将来 `Σ={a,b,c}`、fan-out ≤2、rank ≤2 の reduced good `G_n` について、`‖G_n‖,\bar θ_{G_n}=n^{O(1)}`、`L_n∈C_{2,c}`、`μ_a(L_n)=n^{ω(1)}` を全て証明できれば、原稿 `prop:rare-type` によって、**`\mathcal B^{\le r}_{2,c}`（固定ランク上限 `r≥2`）、`\mathcal B_{2,c}`（ランク無制限）、およびクラス `C_{2,c}` 全体に特徴標本を持つ集合駆動作用素**には、内容 `{a}` の語が必要で総符号長は少なくとも `μ_a(L_n)+1` である。最後の作用素については `L_n\setminus c^{-1}({a})` にも特徴標本を持つという全クラス仮定を使う。任意の逐次 Gold 学習器の実行時間／収束時点の下界とは言わない。今回 (5) はこの前提に**適合しない**。

### 5.4 文献・今回の貢献の位置付け

定理 W は原稿 `lem:unique-word-gap(ii)` に極めて近く、部分的な仮定緩和と読むのが正確である。正則言語の有限カウンタ／長さ合同による模型は古典的な構成であり、新言語クラスの発見ではない。定理 Δ および正規化 `λ_k` と同一の定式化が既刊文献にあるかは **未確認**。前報の定理 I や原稿の半群／MCFG 学習境界に関する独立した新規性も、今回追加では主張しない。

**全三文字内容型の問題は解けていない。従って「境界がファンアウトで動く」とは言わない。**

## 6. Python 3 標準ライブラリによる独立計算

次のコードは**無限言語 (5) に対する正確な所属判定器**を持つ。`bounded_check` は、指定した上限までの全受理語から生じる arity 1・2 の全ての合法な tuple occurrence と、それらから得られる共通受理文脈の候補を列挙して、全ての比較対象を**正確な oracle**で判定する。**文脈探索は有界**なので、違反なしは無限族の代入可能性の証明とはならない。無限族の証明は §3.2 の独立した全称論証にある。

Windows: `py -3 case2_iii_verify.py`。本文を同名 `.py` に保存して実行できる。`assert` は説明のとおり `b/c` の高々1回制約、合同、両穴間非空を検査する。

```python
#!/usr/bin/env python3
"""Run on Windows: py -3 case2_iii_verify.py.
The membership oracle is exact for infinite II/III families.
Occurrence search is exhaustive only through the displayed word-length limit.
"""
from collections import defaultdict
from itertools import product

K=5

def member(w,case):
    if not w or any(ch not in 'abc' for ch in w) or len(w)%K:
        return False
    if w.count('c')>1:
        return False
    if case=='II' and w.count('b')>1:
        return False
    return True

def positives(case,limit):
    if case=='II':
        data=[]
        for n in range(K,limit+1,K):
            data.append('a'*n)
            for i in range(n):
                for x in ('b','c'):
                    data.append('a'*i+x+'a'*(n-i-1))
            for i in range(n):
                for j in range(n):
                    if i==j:continue
                    a=['a']*n;a[i]='b';a[j]='c';data.append(''.join(a))
        return sorted(set(data))
    return [''.join(x) for n in range(K,limit+1,K)
            for x in product('abc',repeat=n) if member(''.join(x),case)]

def occurrences(w,d):
    n=len(w)
    if d==1:
        for i in range(n):
            for j in range(i+1,n+1):
                yield (w[i:j],),(w[:i],w[j:])
    else:
        for i in range(n):
            for j in range(i+1,n):
                for p in range(j+1,n):
                    for q in range(p+1,n+1):
                        yield (w[i:j],w[p:q]),(w[:i],w[j:p],w[q:])

def plug(ctx,tup):
    return ''.join(a+b for a,b in zip(ctx,tup))+ctx[-1]

def bounded_check(case,limit):
    lang=positives(case,limit)
    grouped=defaultdict(set)
    contexts=defaultdict(set)
    occurrences_count=0
    for w in lang:
        assert member(w,case)
        for d in (1,2):
            for tup,ctx in occurrences(w,d):
                assert plug(ctx,tup)==w
                typ=tuple(frozenset(z) for z in tup)
                grouped[(d,typ,ctx)].add(tup)
                contexts[(d,tup)].add(ctx)
                occurrences_count+=1
    pairs=set()
    for (d,t,shared),tups in grouped.items():
        for x in tups:
            for y in tups:
                if x<y:pairs.add((d,x,y))
    for d,x,y in sorted(pairs):
        for u,v in ((x,y),(y,x)):
            for ctx in contexts[(d,u)]:
                assert member(plug(ctx,u),case)
                if not member(plug(ctx,v),case):
                    return len(lang),occurrences_count,len(pairs),(d,u,v,ctx)
    return len(lang),occurrences_count,len(pairs),None

def main():
    for case,lim in (('II',5),('II',10),('III',5)):
        print(case,lim,bounded_check(case,lim))
    for case in ('II','III'):
        small='a'+'bc'+'aa'
        large='a'*6+'bc'+'aa'
        assert member('a'*K,case)
        assert member(small,case) and member(large,case)
        assert not member('a'*(K-1),case)
        assert not member('b'*5,case) if case=='II' else member('b'*5,case)
        assert not member('c'*5,case)
        if case=='II':
            assert all('bbbb' not in w and 'cccc' not in w
                       for w in positives(case,10))
        else:
            assert all('cccc' not in w for w in positives(case,5))
        print('case',case,'mu_a=',K,'F=bc','a-counts=',small.count('a'),large.count('a'),'losses=',K-small.count('a'),K-large.count('a'))

if __name__=='__main__': main()
```

**実際の実行出力（2026-11-04、Python 3）**

```text
II 5 (31, 930, 422, None)
II 10 (142, 43665, 86602, None)
III 5 (112, 3360, 3630, None)
case II mu_a= 5 F=bc a-counts= 3 8 losses= 2 -3
case III mu_a= 5 F=bc a-counts= 3 8 losses= 2 -3
```

`None` は**指定された有限の証拠探索で反例が見つからなかった**という意味だけ。出力を「無限の族の完全検査」の証拠とはしない。一方、`F=bc` の二予算の例は `member` の厳密な所属判定で確認され、かつ §3.2 の一般的構成で全 `k≥5` に成立する。

---

## 7. 結了の三点

1. **証明できたこと**：最短 Γ 語に対する heavy 反鎖幅の下界（定理 W）、有界非 `a` 文字数の部分クラスにおける `μ_a` 多項式上界、同一 `F` の `a` 予算の `k`-分離と無限純粋語の強制（定理 Δ）、正規化損失の一意性。無限定義の観察 (λ) は、完全に所属を証明した場合 II・III の正則模型で反証。
2. **止まった場所**：全受理語の非 `a` 数が無制限の一般の II・III で、最小純粋導出の heavy 反鎖幅 `W(T)` を多項式に抑えられない。場合 III の `c` 配列の定数次元圧縮も未証明。
3. **次の一点**：分岐 (B) の鎖または分岐 (S) の殻の入れ子から、**同一深さの多数の heavy 節点**の存在を禁止する二穴部分語比較を構成する。幅の見積もり (9) に直接つなぐ。

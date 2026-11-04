# 両文字型の分岐と全文字の骨格による剛性：同じ核を持つラベルの線形化と尺度の数え上げ（三文字内容型付け・系列の十一本目、Claude 版）

**研究日**：2026-11-04
**対象**：栗山貴之、論文 #2、`op:fanout-two` の三文字の核（純粋 `a` 語の問い Q）
**資料**：公開リポジトリ `growupkuriyama-hub/Papers` を取得（commit `10f6e07f`、2026-11-04 15:12 JST）。`main.tex`（blob `b72cd2ed`）、第十報 `chatgpt_nested_bc_chain_2026-11-04.md`（blob `6ad25a47`）、`chatgpt_weighted_codes_2026-11-02.md`（`5b624c55`）、`chatgpt_skeleton_diversity_2026-11-02.md`（`0d28618c`）、`chatgpt_a_spectrum_2026-11-03.md`（`f26e671a`）を直接読んだ。
**立場**：独立査読の前の研究ノートである。**中心の問い Q は解決していない。** 新しく証明したのは、F 分岐の段数 s ではなく、**両文字型の代表の「核」の種類数 D** をパラメータとする μ_a の上界（定理B）である。

---

## 0. 主張ごとの判定

| 主張 | 判定 | 根拠・限定 |
|---|---|---|
| (R)：σ_X(w)=σ_X(w')、b・c の個数が等しく、0<\|w\|_a,\|w'\|_a<k なら \|w\|_a=\|w'\|_a | **証明済み** | §1.1。一般形：差は 0 か g の正の倍数（g≥k）。系2.2 と定理S を順に使うだけで、新しい道具は要らない |
| (R) の確認点①：X の文字の再配分が定理S の仮定を壊さない | **証明済み** | §1.2。再配分は a の個数も a の連の長さも変えない |
| (R) の確認点②：差し替えの塊が合流する場合 | **証明済み（注意として整理）** | §1.3。(R) は語そのものの骨格についての命題なので合流で壊れない。ただし差し替え語の骨格を「塊の骨格の連結」と計算するのは、塊が隣り合わず端が a で囲まれるときに限る。同じ節点の二成分は決して隣り合わない |
| 一つの塊と t 個の塊の比較（段の交換）から (R) で矛盾を出す | **(R) だけでは不可（観察）** | §1.4。骨格の塊の数が違う。第十報の補題5.1と整合 |
| **補題A**：同じ核 κ を持つ頻出の両文字型ラベル（出現 ≥ N₀=504θ²+4）の損失 d_X は、w_X=(e_X,β_X,γ_X) の**線形関数** | **証明済み** | §2。ファンアウト1では無条件、ファンアウト2では「代表の非自明な成分の核が全て κ」のとき |
| **補題3.1**（尺度の漸化式）：例外でない重い節点の長さの値を小さい順に並べると、隣どうしの比は K 以下 | **証明済み** | §3.2 |
| **補題3.2**（疎な鎖）：比 R 以上で上がる鎖の長さは 3D 未満 | **証明済み** | §3.3。部分和の単射性による |
| **定理B**：μ_a ≤ K^{3D+1}R^{3D}θ（K=(2v+E)(2r+1)、R=θ+2v+2、E=v(504θ²+θ+22)） | **証明済み** | §3.4。**D が有界なら多項式**。D は「核の種類」で決まる量で、F 分岐の段数 s にも入れ子の深さ h にも依らない |
| 定理B の D は自明に D ≤ 2+3v | **自明に成り立つが目的には足りない** | §4.3。全ての F ラベルの核が相異なると、D は F ラベルの数と同程度になり、(K) と同型の指数の上界に戻る |
| **系4.1**：場合 I、ファンアウト ≤ 2、ランク任意、入れ子の深さ任意で、頻出の両文字型の代表の非自明な成分の核が全て一つ（例：全て a\*b⁺c⁺a\*、核 abca）なら μ_a ≤ K¹⁶R¹⁵θ | **証明済み** | §4.1。依頼 §3-2 の「まず目標にしてよい場合」（ファンアウト1・ランク2・骨格が全て bc）を、入れ子二段の制限なしに含む |
| F 分岐の段数 s を O(1) に抑える | **未解決** | 定理B は s を抑えない。s ≤ h ≤ v は自明 |
| 場合 II・III でも定理B が同じ形で成り立つ（D の各類の寄与は 1+\|X\|） | **証明済み** | §5.1。場合 II では核に b・c の並びがそのまま残るので、同じ核のラベルは損失が等しい |
| (P)：一様な T の多段の分岐から a の連の長さの整除の不変量が生じるか | **否定的に整理（証明済みの部分と観察）** | §5.2。連ごとの整除の不変量は L の中には存在し得ない（系2.2）。残る不変量は (σ_X, b・c の個数) ごとの a の総数で、補題A がその同じ核の範囲での完全な帰結 |
| 反例族（三文字、ファンアウト ≤2、ランク ≤2、多項式サイズ・厚さ、超多項式の μ_a、C_{2,c} の所属を証明） | **未構成** | §6。定理B から、反例には **D = Ω(log k / log(KR))** 個の相異なる核が要る（k=2ⁿ なら Ω(n/log n)） |
| 有限の検査（Cramer の係数の上界、H 族の代入可能性と (R)、疎な鎖） | **有限の対象について完全な判定／有限の健全性検査** | §7。証明の代わりではない |
| 定理B・補題A の文献上の新規性 | **未確認** | §8 |

---

## 1. 記号と (R) の検証

Σ={a,b,c}、内容型付け c、L ∈ C_{2,c}。G は L∩Σ⁺ の reduced good な表示で、ファンアウト ≤ 2、ランク ≤ r（r≥1）。v=|V|、θ=θ̄_G、k=μ_a(L) ≥ 5。T は a^k の節点数最小の導出で、(U)（第九報・第十報 §2、別のスレッドで検証済み）により一様にとる：同じラベルの部分木は全て同じで、同じラベルの出現は反鎖、ラベルの依存グラフは非巡回、根から葉への道の節点は v 個以下。節点 u の総長を ℓ_u、ℓ_u>θ のとき重いと呼ぶ。原稿 `lem:thickness-equivalence` (i)(ii) により、各規則が直接書く終端は θ 文字以下、各非終端 B に総長 θ 以下の生成組がある。

重いラベルは、短い代表に {a,x}⁺（x∈{b,c}）のものがあれば**一色型**（色 x を一つ選んで固定）、なければ**両文字型**（集合 F。短い代表は全て b と c を含む）。両文字型の各ラベル X に短い代表 ρ_X を一つ選び、

- d_X := ℓ_X − |ρ_X|_a（損失。ρ_X が b と c を含むので |ρ_X|_a ≤ θ−2 < ℓ_X、よって d_X ≥ 3）
- β_X := |ρ_X|_b、γ_X := |ρ_X|_c

と書く。N_X は T の中の X の出現数（全て重い）。

X ⊆ {b,c} を、x⁴ が L のある語の因子として現れる文字 x の集合とする。σ_X(w) は w の a の極大連と X の文字の極大連をそれぞれ一文字に縮めた語。σ_a := σ_∅。

### 1.1 (R) の主張と証明

**命題1.1 (R)。** w, w' ∈ L が σ_X(w)=σ_X(w')、|w|_b=|w'|_b、|w|_c=|w'|_c、|w|_a, |w'|_a ≥ 1 を満たすとする。このとき |w|_a − |w'|_a は 0 か、g の正の倍数（g ≥ k は定理S の周期）である。特に 0<|w|_a,|w'|_a<k なら |w|_a=|w'|_a。

**証明。** σ_X(w)=σ_X(w')=:s と書く。s の各文字で a または X の文字であるものは、w でも w' でもちょうど一つの極大連に対応する（同じ文字の連は隣り合わないので、縮めた一文字と極大連は一対一）。X に入らない b, c は s にそのまま残るので、w と w' で同じ位置に同じ文字として現れる。

x ∈ X を一つとる。weighted_codes の補題2.1：p x⁴ q ∈ L をとると、二組 (x, xx) と (xx, x) は成分ごとの内容が ({x},{x}) で等しく、許容文脈 p□₁x□₂q（二穴の間 x は空でない）が両方を同じ語 px⁴q に写す。arity 2 の代入可能性で両者の分布は等しい。よって任意の u, v と空でない z について u·x z xx·v ∈ L ⇔ u·xx z x·v ∈ L。これを、二つの隣接する x の連（間の z は x を含まず空でない）の間で一文字ずつ x を動かす操作として使う（系2.2）。正の整数の組成は、2以上の部分から1を他へ移す操作で連結しているので、w' の x の連の長さを、x の総数を保ったまま w の x の連の長さに一致させられる。この間、所属は保たれ、x 以外の文字（a の連の長さを含む）は一切変わらない。X の各文字について順に行った結果を w'' とする。

w'' と w は、X の文字の連の長さも、X に入らない文字の位置も一致し、違うのは a の連の長さだけである（連の数は s で決まるので同じ）。よって σ_a(w'')=σ_a(w)、かつ |w''|_a=|w'|_a。定理S（a_spectrum §2.3）により、同じ a 骨格の語の a の個数の差は Δ に属し、Δ は空か gℤ_{>0}（g ≥ k）。□

**定理S の検証**（a_spectrum §2 を段ごとに確かめた）。補題2.2：同じ a 骨格で a の個数が n と n+δ の二語から、a の余りを最初の連に集めて Ua V と Ua^{1+δ}V を作ると、一穴文脈 U□V を共有し内容 {a} が等しいので D_L(a)=D_L(a^{1+δ})。0<δ<k なら a^k の中の a^{1+δ} を a に替えて a^{k−δ} ∈ L、最小性に反する。正の差が骨格をまたいで加法と差に閉じること（補題2.3、定理S(ii)）も確認した。

### 1.2 確認点①：再配分は定理S の仮定を壊さない

再配分で動くのは X の文字だけである。a の個数も a の連の長さも、連の数も変わらない。したがって、仮定 0<|w'|_a<k は w'' でもそのまま成り立つ。定理S が要求するのは「a を含む同じ a 骨格」だけで、§1.1 の w'' はそれを満たす。a⁴ の出現は a^k（k ≥ 5）から従う。**問題はない。**

ついでに一点。命題1.1 は「0<|·|_a<k」がなくても成り立つ一般形（差 ∈ {0} ∪ gℤ_{>0}）で述べた。上の区間の仮定は、差が g の倍数になる可能性を消すためだけに使う。

### 1.3 確認点②：合流の扱い

(R) は語そのものの σ_X についての命題なので、**合流によって (R) が壊れることはない**。注意が要るのは、差し替えで作った語の σ_X を計算する段階である。

各語 u の**核**を κ(u) := σ_X(a u a) と定める（a で始まり a で終わる）。a で始まり a で終わる二つの骨格 κ, κ' に対し、κ∘κ' を、κ の末尾の a と κ' の先頭の a を一つにした連結とする。

**補題1.2（差し替え語の骨格）。** a^k の中の、互いに素で隣り合わない区間 I₁,…,I_n（左から順）を、語 u₁,…,u_n に置き換えた語を W とする。最初の文字と最後の文字がどの区間にも入らないなら

σ_X(W) = κ(u₁) ∘ κ(u₂) ∘ ⋯ ∘ κ(u_n)。

**証明。** W = a^{x₀}u₁a^{x₁}⋯u_n a^{x_n}、全ての x_i ≥ 1。σ_X は連の構造だけで決まるので、σ_X(W)=σ_X(a u₁ a u₂ a ⋯ a u_n a)。区切りの a の連は両隣の u_i の端の a と合わさって一つの a の連になり、u_i の内部の X の文字の連は区切りの a を越えて合流しない。□

隣り合う区間があると、この式は誤る。例えば bc と cb を隣り合わせると σ(aabccbaa)=abcba、間に a を置くと σ(aabcacbaa)=abcacba（§7 の Part 1）。また u_i が a で始まる・終わるときは、その a は区切りの a と合流するので、核は変わらない（κ(abc)=κ(bc)=abca）。

**補題1.3（同じ節点の二成分は隣り合わない）。** good な文法の導出で、ファンアウト2の節点 u の二成分は、根の語の中で必ず空でない語に隔てられる。

**証明。** u の親の規則で u の二つの変数が同じ成分に入るなら、nonmerging により間に終端か他の変数があり、λ-free により他の変数の成分は空でない。別々の成分に入るなら、親の二成分の間の隔たりに帰着する。根はファンアウト1なので、ある祖先で同じ成分に入り、そこで空でない語に隔てられる。□

したがって、以下で差し替える節点の集合は「互いに素で、成分どうしが隣り合わず、最初と最後の文字を含まない」ように選ぶ。これで補題1.2 が使え、合流の問題は起こらない。

### 1.4 (R) だけでは段の交換は矛盾しない

F の節点 w（ラベル B）を ρ_B に替えた語と、w の中の F の子孫 z₁,…,z_t を替えた語は、補題1.2 により核の個数が 1 と t で違う。(R) は σ_X の一致を要求するので、この二語を直接比べても何も出ない。これは第十報の補題5.1（「各一文字」の交換対は同じ a 骨格を作らない）と整合する。以下では、**塊の数が同じで、同じ核の塊だけからなる**差し替えどうしを比べる。

---

## 2. 補題A：同じ核を持つ頻出ラベルの損失の線形化

### 2.1 定義

両文字型ラベル X が**頻出**とは N_X ≥ N₀ のこと。ここで

M := 12θ²、 N₀ := 42M+4 = 504θ²+4。

ρ_X の成分のうち、純粋な a でないものを**非自明な成分**と呼び、その個数を e_X ∈ {1,2} とする（ρ_X は b を含むので e_X ≥ 1）。核 κ を固定する。頻出の両文字型ラベル X が**類 κ に属する**とは、ρ_X の非自明な成分の核が全て κ であること。ファンアウト1では e_X=1 で、各 X はちょうど一つの類（κ(ρ_X)）に属する。ファンアウト2では、二つの非自明な成分の核が違う X はどの類にも属さない（**非一様**と呼ぶ）。

X が類 κ に属するとき、w_X := (e_X, β_X, γ_X) ∈ ℤ³ とおく。

### 2.2 主張

**補題A。** 類 κ に属する頻出の両文字型ラベル全体を 𝒳_κ とする。ある φ_κ ∈ ℚ³ があって、全ての X ∈ 𝒳_κ について

d_X = ⟨φ_κ, w_X⟩。

場合 I（X={b,c}）ではこれが d_X = λe_X + μβ_X + νγ_X の形になる。場合 II・III では β, γ の一部が e で決まるので、次元が下がる（§5.1）。

### 2.3 証明

**(a) 配置語。** 𝒳_κ のラベルの出現の多重集合 J（互いに素、成分どうし隣り合わない、a^k の最初と最後の文字を含まない）をとり、各出現 u を ρ_{lab(u)} の導出に替えた語を W_J とする。W_J ∈ L（成功導出のまま）。補題1.2 と補題1.3 により（純粋な a の成分は核 a で ∘ の単位元）

σ_X(W_J) = κ^{∘n}、 n = Σ_{u∈J} e_{lab(u)}、

|W_J|_b = Σ β、|W_J|_c = Σ γ、|W_J|_a = k − Σ_{u∈J} d_{lab(u)}。最初と最後の a が残るので |W_J|_a ≥ 1、J が空でなく d ≥ 3 なので |W_J|_a < k。

**(b) 関係から等式へ。** 整数ベクトル c=(c_X) が Σ_X c_X w_X = 0 を満たし、正の部分 c⁺ と負の部分 c⁻ が配置として実現できる（X の出現を c_X⁺ 個、別の語で c_X⁻ 個とれる）とする。二つの配置語は、第一座標により塊の数 n が等しく、σ_X が κ^{∘n} で等しい。第二・第三座標により b, c の個数が等しい。a の個数はどちらも (0,k) にある。命題1.1 により a の個数が等しく、Σ c_X d_X = 0。

**(c) 小さい係数の関係で十分。** 行列 W（列 w_X、X ∈ 𝒳_κ）の有理数上の核は、**回路**（極小な一次従属集合）の関係で張られる。列の基底 ℬ をとり、ℬ に入らない各列 j について ℬ∪{j} の中の基本回路の関係をとれば、それらは独立で核の次元だけあるからである。回路の大きさ s は rank+1 ≤ 4。回路の関係の係数は、Cramer の公式により、rank s−1 の (s−1)×s 部分行列の (s−1) 次小行列式（で割った原始的な整数ベクトル）であり、e ≤ 2、β, γ ≤ θ から

|c_X| ≤ 3!·2·θ·θ = 12θ² = M（s=4）、s ≤ 3 ではさらに小さい。

（θ ≤ 4 で全ての回路を数え上げ、最大の係数が 5, 16, 33 で 12θ² 以下であることを確かめた。§7 Part 2。これは確認であって、証明は上の Cramer の議論。）

**(d) 実現できること。** 一つの回路の片側は、ラベル 4 個以下、各 M 個以下、計 4M 個以下の出現を要する。出現を一つずつ選んでいく。ラベル X の出現 u を選ぶと、ラベル Y の出現のうち次のものが使えなくなる。

- u 自身（Y = X のとき）
- u の祖先（同じラベルの出現は反鎖なので、ラベル Y の祖先は高々1個）
- u の子孫（一様な T では t_{X,Y} 個。X の出現どうしは素なので t_{X,Y}·N_X ≤ N_Y、よって t_{X,Y} ≤ N_Y/N₀）
- u の成分と隣り合う出現（u の二成分の左右に高々一つずつ、計4個以下）

加えて、最初または最後の文字を含む Y の出現は2個以下。よって使えない Y の出現は

2 + 4M·5 + 4M·N_Y/N₀ ≤ 2 + 20M + N_Y/2（N₀ ≥ 8M を使った）

以下。N_Y ≥ N₀ = 42M+4 なら残りは N_Y/2 − 2 − 20M ≥ M 個以上で、必要な M 個を選べる。

**(e) 線形代数。** (b)–(d) により、核 ker W の生成系の全ての c について Σ c_X d_X = 0。よって d は ker W の直交補空間、すなわち W の行空間に入り、d = φ_κᵀW となる φ_κ ∈ ℚ³ がある。□

**注意。** 補題A は (R) の「同じ核の頻出ラベルの範囲での完全な帰結」である。逆に、損失が線形なら、同じ核の配置語どうしでは (R) から新しい制約は出ない。異なる核をまたぐ制約は、塊の順序（ファンアウト2では成分の入り組み方）が一致する配置を要するので、この補題には入れていない。

---

## 3. 尺度の数え上げ

### 3.1 群と例外

重い節点を次のように分ける（(K) の §3.1–3.2 は、引用する前に次のとおり確かめた：非飽和の色の論法は二文字の `lem:app-two-runs`(iv) と `lem:app-two-alternate` を L_x=L∩{a,x}⁺ に使い、10個の同じ深さの節点から最大次数4の隣接グラフで独立な二点を選ぶ。飽和の色の比の等式は、q_C 個の B と q_B 個の C の差し替えを L_x の Parikh 剛性で比べる。どちらも F の節点を差し替えないので、F の多さに影響されない）。

- **例外**：非飽和の色の一色型（全体で 18v 個以下）、頻出でない一色型（出現 ≤ θ のラベル、全体で vθ 個以下）、頻出でない両文字型（出現 < N₀、全体で vN₀ 個以下）。合計

  E := 18v + vθ + vN₀ = v(504θ² + θ + 22)。

- **一色型の群**：飽和の色 x の頻出ラベル B は、(K) の式 (3.2) により ℓ_B = p_B + α_x q_B（p_B = |ω_B|_a ≤ θ、1 ≤ q_B ≤ θ）。群 (x, q) の値を D := α_x q とおくと ℓ ∈ [D, D+θ]。
- **両文字型の群**：類 κ の頻出ラベル X は、補題A により d_X = ⟨φ_κ, w_X⟩。群 (κ, w) の値を D := ⟨φ_κ, w⟩ とおくと ℓ_X = |ρ_X|_a + D ∈ [D, D+θ]。非一様な頻出ラベル X は、それ自体を一つの群とし D := ℓ_X。

**区分**（後で使う）：値の出どころを次の**区分**に分ける。各区分 π は、線形写像 f_π(p) = ⟨φ_π, p⟩ と、0 ≤ p ≤ θ の整数点の集合で値を与える。

| 区分 | 点 p | 次元 dim π |
|---|---|---|
| 一色型、色 x（2個） | q ∈ [1,θ] | 1 |
| 両文字型、類 κ（場合 I） | (e, β, γ) | 3 |
| 両文字型、非一様なラベル X | 1（φ = ℓ_X） | 1 |

D := Σ_π dim π と定める（場合 I では D = 2 + 3m_u + m_n。m_u は使った類の数、m_n は非一様な頻出ラベルの数）。代表の選び方と類への分け方は自由なので、D はそれらについての最小をとってよい。

群の値は全てで v 個以下（各群は少なくとも一つのラベルを含む）。重い節点は ℓ > θ なので、D̂ := max(D, θ) とおくと、群の節点は ℓ ∈ [D̂, D̂+θ] ⊆ [D̂, 2D̂] を満たす。

### 3.2 尺度の漸化式

群の値 D̂ の相異なるものを D̂₁ < D̂₂ < ⋯ < D̂_m とし、D̂₀ := θ とおく。

**補題3.1。** K := (2v+E)(2r+1) とおく。全ての 1 ≤ j ≤ m について D̂_j ≤ K·D̂_{j−1}。また k ≤ K·D̂_m（m=0 なら k ≤ Kθ）。

**証明。** 値 D̂_j の群の節点 u をとる。ℓ_u ≤ 2D̂_j。u の部分木の中で ℓ_z > 2D̂_{j−1} の節点 z の集合を**芯**とする。長さは子孫へ向かって増えないので、芯は u を根とする部分木である。

- 芯の、例外でない節点 z：z の群の値 D̂' は ℓ_z ≤ 2D̂' を満たすので D̂' > D̂_{j−1}、よって D̂' ≥ D̂_j、ℓ_z ≥ D̂_j。同じ深さの節点は出力が素なので、一つの深さにこれらは ℓ_u/D̂_j ≤ 2 個以下。深さは v 以下なので計 2v 個以下。
- 芯の例外の節点：全体で E 個以下。

芯の各節点は終端を θ 文字以下書き、芯でない子は r 個以下で、各々 ℓ ≤ 2D̂_{j−1}。よって

D̂_j ≤ ℓ_u ≤ (2v+E)(θ + 2rD̂_{j−1}) ≤ (2v+E)(2r+1)D̂_{j−1}

（θ ≤ D̂_{j−1}）。根については、ℓ > 2D̂_m の節点は全て例外なので、同じ計算で k ≤ max{2, E(2r+1)}D̂_m ≤ K D̂_m。□

この漸化式だけでは D̂_m ≤ K^m θ で、m（群の数、v まで）が指数に入る。(K) の三段の議論はこれの m=2 の場合にあたる。次の補題で、指数を m ではなく D にする。

### 3.3 疎な鎖

**補題3.2。** R' := θ + 2v、R := R'+2 とする。y₁ := D̂₁、y_{i+1} := min{D̂_j : D̂_j ≥ R y_i} として、とれる限り続けた鎖を y₁ < ⋯ < y_n とする。このとき n ≤ 3D であり、

D̂_m < R(KR)^{n−1} y₁ ≤ (KR)^{3D} θ。

**証明。** y_{i+1} の一つ前の値は R y_i 未満なので、補題3.1 により y_{i+1} < K R y_i。鎖が止まるのは R y_n 以上の値がないときなので D̂_m < R y_n。y₁ = D̂₁ ≤ Kθ（補題3.1、j=1）と合わせて後半を得る。

n を抑える。z_i := y_{i+1}（1 ≤ i ≤ N := n−1）とおく。z_i ≥ Rθ > θ なので z_i は D̂ ではなく群の値 D そのもので、ある区分 π(i) と点 p_i により z_i = ⟨φ_{π(i)}, p_i⟩ と書ける。z_{i+1} ≥ R z_i から

R' Σ_{i'≤i} z_{i'} ≤ R' z_i · R/(R−1) < R z_i ≤ z_{i+1}

（R' < R−1 による）。よって係数 c ∈ {0,1,…,R'}^N に対する Σ c_i z_i は相異なる（最大の違う番号を比べればよい）。一方

Σ_i c_i z_i = Σ_π ⟨φ_π, P_π⟩、 P_π := Σ_{π(i)=π} c_i p_i ∈ [0, N R' θ]^{dim π}

なので、この値は (P_π)_π で決まり、その組は (NR'θ+1)^D 通り以下。したがって

(R'+1)^N ≤ (NR'θ+1)^D。

群の値は v 個以下なので N ≤ v−1 ≤ R'/2、また θ ≤ R'。よって NR'θ+1 ≤ R'³、R'^N < (R'+1)^N ≤ R'^{3D}、N < 3D、n ≤ 3D。□

### 3.4 定理B

**定理B。** §1 の条件の下で（Σ={a,b,c}、内容型付け、L ∈ C_{2,c}、ファンアウト ≤ 2、ランク ≤ r、k=μ_a(L) ≥ 5）、§3.1 の D について

**k ≤ K^{3D+1} R^{3D} θ**、 K = (2v+E)(2r+1)、 R = θ+2v+2、 E = v(504θ²+θ+22)。

**証明。** 補題3.1 の k ≤ K D̂_m と補題3.2。□

K と R は (r, v, θ) の多項式なので、**D が定数で抑えられる族では μ_a ≤ poly_r(v, θ)**。F 分岐の段数 s、入れ子の深さ h、両文字型ラベルの数は、D を通してしか入らない。

---

## 4. 場合 I の帰結と、依頼の目標の場合

### 4.1 骨格が一つの場合

**系4.1。** 場合 I（b⁴ と c⁴ が現れる）、ファンアウト ≤ 2、ランク ≤ r とする。各頻出の両文字型ラベルの代表を、非自明な成分が全て一つの核 κ を持つように選べるなら（例えば全ての非自明な成分が a\*b⁺c⁺a\* の形で κ = abca）、D = 2+3 = 5 で

μ_a(L) ≤ K¹⁶R¹⁵θ。

依頼 §3-2 で「まず目標にしてよい」とされた場合（ファンアウト1、ランク2、両文字型の代表の骨格が全て bc、入れ子が二段）は、これに含まれる。**入れ子が二段という制限は要らない**（二段なら (K) だけでも多項式になる）。また、頻出でない両文字型ラベルの代表の骨格は何でもよい（例外として数えている）。

次数は大きく（K¹⁶R¹⁵ は v について 31 次程度）、鋭さは追っていない。

### 4.2 段数 s について

定理B は F 骨格木の形を一切使わない。したがって **s は抑えていない**。s ≤ h ≤ v は自明に成り立つが、それは目的に足りない（第十報 §4.4 と同じ）。定理B が言うのは、「F 分岐が何段起こっても、それが μ_a を超多項式に押し上げるには、相異なる核が多数要る」ということである。依頼の目標「s=O(1)、または P を掛けない形」に対しては、後者の形（P^s を経由しない上界）を、D が有界という条件の下で得た、と読むのが正確である。

### 4.3 弱さの明記

- D は自明に D ≤ 2 + 3v（類はラベルの数以下）。全ての頻出の両文字型ラベルの核が相異なると D ≈ 3·(ラベル数) になり、定理B は (K) と同型の「ラベル数が指数に入る上界」に戻る。**定理B の中身は「同じ核のラベルは一つの線形な区分にまとまる」ことに尽きる。**
- 区分 3 次元の「3」は、点 (e, β, γ) の座標の数から来ている。異なる核どうしの関係（順序がそろった配置）が取れれば、類ごとの線形部分を共有させて D の係数を下げられる見込みがあるが、証明していない（§9）。
- 一色型の群は (K) の §3.2 の結果（比 α_x の共通性）をそのまま使っている。

---

## 5. 場合 II・III と (P)

### 5.1 場合 II・III

命題1.1 も補題A も、X を一般の部分集合として証明した。違うのは区分の次元だけである。

- **場合 III**（例えば X={b}）：核 σ_X(aρa) には c がそのまま残る。類 κ のラベルの各非自明な成分は c を |κ|_c 個持つので γ_X = e_X|κ|_c は e_X で決まる。点は (e, β) で、区分の次元は 2。
- **場合 II**（X=∅）：核には b, c の並びがそのまま残り、β_X, γ_X は e_X で決まる。点は e だけで、次元は 1。ファンアウト1では e=1 なので、**同じ核（b, c の並びが同じ）の頻出ラベルは損失が等しい**。

いずれも D = 2 + (1+|X|)m_u + m_n として定理B がそのまま成り立つ。場合 II の既報の候補 D → bc | bcD（arity 1 で破れる）は、両文字型ラベルが一つなので (K) でも定理B でも多項式の側に入る。

場合 II・III に固有の追加の道具（b, c の連が長さ 3 以下であることの利用）は見つけていない。核の種類が多い場合の扱いは場合 I と同じく未解決である。

### 5.2 (P)：偶数の塊の障害の一般化

**整理（証明済みの部分）。** a⁴ が現れる L ∈ C_{2,c} では、系2.2 により、a の連が二つ以上ある語の a の連の長さは、総数を保てば自由に配り直せる。したがって「全ての受理語で、ある個々の a の連の長さが d ≥ 2 の倍数」といった連ごとの整除の不変量は、L の中には存在し得ない（skeleton_diversity の補題3.1 はこの特別の場合）。定理3.2 の障害は、**文法がそのような連ごとの不変量を強制してしまう候補**にだけ効く。

**観察。** 一様な T の中の配置語の a の連の長さは、差し替える節点の位置で決まる隙間の長さで、文法の側からの制約はない。系2.2 によりそれらは所属に影響しない。残る不変量は (σ_X, b・c の個数) ごとの a の総数で（命題1.1）、同じ核の範囲でのその完全な帰結が補題A の線形性である。線形性は「損失が全て偶数」のような整除と両立する（例：φ_κ が全て偶数）。したがって、(P) を「多段の分岐が整除の不変量を生み、再配分と矛盾する」という形で一般化することはできない、と考える。これは観察で、「一般化できない」ことの証明ではない。

---

## 6. 否定側：反例に要る条件

**新しい反例族は作れなかった。** 定理B の対偶から、次が言える（証明済み）。

**系6.1。** 定理B の条件で k > K^{3D'+1}R^{3D'}θ なら D > D'。特に ‖G_n‖, θ̄_{G_n} = poly(n) で μ_a(L_n) = 2ⁿ の族があれば、D = Ω(n / log n)：頻出の両文字型ラベルの代表に、Ω(n/log n) 個の相異なる核（ファンアウト2では非一様なラベルも数える）が要る。

将来の候補が満たすべきことを、既報の失敗と合わせてまとめる。

| 避けるべきもの | 何が要るか |
|---|---|
| □ と □a による a の個数の漏れ（第七報、D → bc \| bcD） | 同じ内容の一穴の組 bcbc, bc が共通の文脈を持たないこと。核を変えるだけでは足りず、arity 1 の分布を分ける必要がある |
| 偶数の塊の障害（定理3.2） | 文法が連ごとの不変量を強制しないこと。倍増 E_i → E_{i−1}E_{i−1} だけで a を作る型は、d_i をどう選んでも壊れる |
| (R)・補題A | 同じ核の頻出ラベルの損失は (e, β, γ) の線形関数。倍増の各段に**別々の核**を割り当てる必要がある（同じ核では比 R 以上の鎖は 9 段以下：補題3.2 を区分一つに使う） |
| 定理B | 核の種類 D が Ω(log k / log(KR)) |

例えば倍増に核 a(bc)^i a の札 (bc)^i を付ける案は、核の数の条件は満たすが、定理3.2 で壊れる。偶数の塊を壊すために a の葉の出し方を増やすと、短い純粋 a 語が生じないこと、arity 1・2 の代入可能性の両方を示す必要があり、そこまでは届かなかった。**下界は主張しない。** 将来下界を述べるときの量化は、第十報 §7.2 のとおり（作用素 B^{≤r}_{2,c}、B_{2,c}、クラス全体に特徴標本を持つ集合駆動作用素；Σ={a,b,c}、ファンアウト ≤ 2、ランク ≤ 2；L_n ∈ C_{2,c} を直接証明）。

---

## 7. 計算

Python 3 の標準ライブラリだけで書いた。Windows では `py -3 claude_f_branching_check.py`。この環境で実際に実行し、出力をそのまま載せる。

- Part 1：σ_X と合流の例、補題1.2 の連結の規則（文字列の恒等式）。
- Part 2：e ∈ {1,2}、1 ≤ β, γ ≤ θ のベクトルの全ての回路（θ = 2, 3, 4）の係数の最大値が 12θ² 以下であること。**有限の確認**で、証明は §2.3(c)。
- Part 3：有限言語 H(重み, N) = {w ∈ a\*b\*c\* : 重み N} の (1,c)・(2,c) 代入可能性の**完全な判定**（全ての受理語を列挙して全ての許容文脈を比べる）と、通ったものでの (R) の結論の確認。H では a の個数が重みで決まるので (R) は自明に成り立つ。**健全性の確認にすぎない。**
- Part 4：補題3.2 の鎖の長さ ≤ 3D を、乱数と大きな係数 (1, T, T²) の区分で確認。**証明の代わりではない。**

```python
#!/usr/bin/env python3
"""Checks for claude_f_branching_2026-11-04.md (Python 3 standard library only).

Windows: py -3 claude_f_branching_check.py

Part 1  skeletons sigma_X and the merging pitfall (string identities only).
Part 2  circuit coefficients of vectors (e, beta, gamma), e in {1,2},
        1 <= beta, gamma <= theta: exhaustive check of max |coef| <= 12 theta^2
        for theta = 2, 3, 4 (a finite check of the Cramer bound used in Lemma A;
        the bound itself is proved in the report).
Part 3  exact (1,c),(2,c) substitutability test of FINITE languages, applied to
        H(weights, N) = {w in a*b*c* : weight(w) = N}; then the conclusion of (R)
        is checked on each language that passes.  Finite languages only: every
        accepted word is enumerated, so the test is a complete decision for
        that language, not a length-bounded observation.
Part 4  the lacunary chain bound n <= 3D of Lemma 3.2 on random and adversarial
        linear pieces (a sanity check of a proved statement, not a proof).
"""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations, product
import random


# ---------------------------------------------------------------- Part 1
def sigma(word, X):
    """Collapse maximal runs of 'a' and of the letters in X to one letter."""
    out = []
    for ch in word:
        if out and out[-1] == ch and (ch == 'a' or ch in X):
            continue
        out.append(ch)
    return ''.join(out)


def part1():
    X = {'b', 'c'}
    # two blocks bc and cb, adjacent versus separated by a
    adjacent = 'aa' + 'bc' + 'cb' + 'aa'
    separated = 'aa' + 'bc' + 'a' + 'cb' + 'aa'
    print('Part 1: sigma(aabccbaa) =', sigma(adjacent, X),
          '; sigma(aabcacbaa) =', sigma(separated, X))
    assert sigma(adjacent, X) == 'abcba'
    assert sigma(separated, X) == 'abcacba'
    # a block that begins with a merges with the a-gap: core is unchanged
    assert sigma('a' + 'abc' + 'a', X) == sigma('a' + 'bc' + 'a', X) == 'abca'
    # composition rule: sigma(a u a v a) = core(u) o core(v)
    for u, v in [('bc', 'cb'), ('bbc', 'abcc'), ('cab', 'b')]:
        lhs = sigma('a' + u + 'a' + v + 'a', X)
        cu, cv = sigma('a' + u + 'a', X), sigma('a' + v + 'a', X)
        assert lhs == cu + cv[1:], (u, v)
    # with X = {b} the c's are kept exactly
    assert sigma('abbccab', {'b'}) == 'abccab'
    print('Part 1: PASS (merging pitfall and composition rule)')


# ---------------------------------------------------------------- Part 2
def rank(rows):
    m = [[Fraction(x) for x in r] for r in rows]
    rk, col, ncol = 0, 0, len(m[0]) if m else 0
    while rk < len(m) and col < ncol:
        piv = next((i for i in range(rk, len(m)) if m[i][col] != 0), None)
        if piv is None:
            col += 1
            continue
        m[rk], m[piv] = m[piv], m[rk]
        for i in range(len(m)):
            if i != rk and m[i][col] != 0:
                f = m[i][col] / m[rk][col]
                m[i] = [a - f * b for a, b in zip(m[i], m[rk])]
        rk += 1
        col += 1
    return rk


def kernel_vector(cols):
    """Primitive integer kernel vector of the 3 x s matrix with these columns,
    assuming the kernel is one-dimensional."""
    s = len(cols)
    rows = [[cols[j][i] for j in range(s)] for i in range(3)]
    m = [[Fraction(x) for x in r] for r in rows]
    piv_cols, r = [], 0
    for c in range(s):
        piv = next((i for i in range(r, 3) if m[i][c] != 0), None)
        if piv is None:
            continue
        m[r], m[piv] = m[piv], m[r]
        m[r] = [x / m[r][c] for x in m[r]]
        for i in range(3):
            if i != r and m[i][c] != 0:
                f = m[i][c]
                m[i] = [a - f * b for a, b in zip(m[i], m[r])]
        piv_cols.append(c)
        r += 1
    free = [c for c in range(s) if c not in piv_cols]
    assert len(free) == 1
    f = free[0]
    vec = [Fraction(0)] * s
    vec[f] = Fraction(1)
    for i, pc in enumerate(piv_cols):
        vec[pc] = -m[i][f]
    den = 1
    for x in vec:
        den = den * x.denominator // gcd(den, x.denominator)
    ints = [int(x * den) for x in vec]
    g = 0
    for x in ints:
        g = gcd(g, abs(x))
    return [x // g for x in ints]


def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)


def part2():
    for theta in (2, 3, 4):
        vecs = [(e, b, c) for e in (1, 2) for b in range(1, theta + 1)
                for c in range(1, theta + 1)]
        worst, circuits = 0, 0
        for s in (2, 3, 4):
            for sub in combinations(vecs, s):
                if rank(list(sub)) != s - 1:
                    continue
                # circuit iff every proper subset is independent
                if any(rank(list(sub[:i] + sub[i + 1:])) != s - 1
                       for i in range(s)):
                    continue
                kv = kernel_vector(list(sub))
                assert all(x != 0 for x in kv)
                circuits += 1
                worst = max(worst, max(abs(x) for x in kv))
        print('Part 2: theta', theta, 'circuits', circuits,
              'max |coef|', worst, 'bound 12*theta^2 =', 12 * theta * theta)
        assert worst <= 12 * theta * theta
    print('Part 2: PASS (finite check of the Cramer bound)')


# ---------------------------------------------------------------- Part 3
def occurrences(word, arity):
    n = len(word)
    if arity == 1:
        for i in range(n):
            for j in range(i + 1, n + 1):
                yield (word[i:j],), (word[:i], word[j:])
    else:
        for i in range(n):
            for j in range(i + 1, n):
                for p in range(j + 1, n):          # nonempty separator
                    for q in range(p + 1, n + 1):
                        yield ((word[i:j], word[p:q]),
                               (word[:i], word[j:p], word[q:]))


def finite_failure(lang):
    """Exact (1,c),(2,c) decision for a finite language given in full."""
    for arity in (1, 2):
        dist = defaultdict(set)
        for w in lang:
            for tup, ctx in occurrences(w, arity):
                dist[tup].add(ctx)
        by_key = {}
        for tup, ctxs in dist.items():
            typ = tuple(frozenset(x) for x in tup)
            for ctx in ctxs:
                other = by_key.setdefault((typ, ctx), tup)
                if other != tup and dist[other] != dist[tup]:
                    return arity, other, tup, ctx
    return None


def H(weights, N):
    wa, wb, wc = weights
    out = set()
    for i in range(N // wa + 1):
        for j in range((N - i * wa) // wb + 1):
            rest = N - i * wa - j * wb
            if rest % wc == 0:
                w = 'a' * i + 'b' * j + 'c' * (rest // wc)
                if w:
                    out.add(w)
    return out


def check_R(lang):
    pure = sorted(len(w) for w in lang if set(w) == {'a'})
    if not pure:
        return 'no pure a-word'
    k = pure[0]
    X = {x for x in 'bc' if any(x * 4 in w for w in lang)}
    if not any('aaaa' in w for w in lang):
        return 'no a^4'
    cell = defaultdict(set)
    for w in lang:
        na = w.count('a')
        if 0 < na < k:
            cell[(sigma(w, X), w.count('b'), w.count('c'))].add(na)
    bad = {key: v for key, v in cell.items() if len(v) > 1}
    assert not bad, bad
    return 'k=%d X=%s cells=%d (R) holds' % (k, ''.join(sorted(X)), len(cell))


def part3():
    for weights, N in [((1, 2, 2), 8), ((1, 2, 3), 12), ((1, 3, 2), 12),
                       ((1, 1, 1), 6), ((1, 2, 2), 10)]:
        lang = H(weights, N)
        fail = finite_failure(lang)
        print('Part 3: H', weights, N, '|L| =', len(lang),
              'substitutability:', 'PASS' if fail is None else 'FAIL ' + str(fail))
        if fail is None:
            print('        ', check_R(lang))
    print('Part 3: done (finite languages, exact decisions)')


# ---------------------------------------------------------------- Part 4
def greedy_chain(values, R):
    vals = sorted(values)
    chain = [vals[0]]
    while True:
        nxt = [x for x in vals if x >= R * chain[-1]]
        if not nxt:
            return chain
        chain.append(nxt[0])


def part4(seed=20261104):
    rnd = random.Random(seed)
    worst_ratio = 0.0
    for trial in range(3000):
        theta = rnd.randint(2, 6)
        v = rnd.randint(2, 40)
        dims = [rnd.randint(1, 3) for _ in range(rnd.randint(1, 4))]
        D = sum(dims)
        Rp = theta + 2 * v
        R = Rp + 2
        values = set()
        for d in dims:
            if rnd.random() < 0.5:   # adversarial: phi = (1, T, T^2) with huge T
                T = rnd.choice([10 ** 6, 10 ** 12, 3 ** 40])
                phi = [T ** i for i in range(d)]
            else:
                phi = [rnd.randint(1, 10 ** rnd.randint(1, 15)) for _ in range(d)]
            for _ in range(rnd.randint(1, v)):
                p = [rnd.randint(1, theta) for _ in range(d)]
                values.add(sum(a * b for a, b in zip(phi, p)))
        values = sorted(values)[:v]           # at most v groups
        n = len(greedy_chain(values, R))
        assert n <= 3 * D + 1, (n, D)
        worst_ratio = max(worst_ratio, n / (3 * D + 1))
    print('Part 4: 3000 random/adversarial trials, max chain/(3D+1) = %.3f'
          % worst_ratio)
    print('Part 4: PASS (sanity check of a proved bound)')


if __name__ == '__main__':
    part1()
    part2()
    part3()
    part4()
```

**実行結果（2026-11-04、この環境で `python3 -I` により実行、約8秒）**

```text
Part 1: sigma(aabccbaa) = abcba ; sigma(aabcacbaa) = abcacba
Part 1: PASS (merging pitfall and composition rule)
Part 2: theta 2 circuits 38 max |coef| 5 bound 12*theta^2 = 48
Part 2: theta 3 circuits 2192 max |coef| 16 bound 12*theta^2 = 108
Part 2: theta 4 circuits 26779 max |coef| 33 bound 12*theta^2 = 192
Part 2: PASS (finite check of the Cramer bound)
Part 3: H (1, 2, 2) 8 |L| = 15 substitutability: PASS
         k=8 X=bc cells=9 (R) holds
Part 3: H (1, 2, 3) 12 |L| = 19 substitutability: PASS
         k=12 X=bc cells=15 (R) holds
Part 3: H (1, 3, 2) 12 |L| = 19 substitutability: PASS
         k=12 X=bc cells=15 (R) holds
Part 3: H (1, 1, 1) 6 |L| = 28 substitutability: PASS
         k=6 X=bc cells=20 (R) holds
Part 3: H (1, 2, 2) 10 |L| = 21 substitutability: PASS
         k=10 X=bc cells=14 (R) holds
Part 3: done (finite languages, exact decisions)
Part 4: 3000 random/adversarial trials, max chain/(3D+1) = 0.308
Part 4: PASS (sanity check of a proved bound)
```

有限の H 族はいずれも μ_a が小さく、Q の反例ではない。無限の族の所属をこれらの検査から推定することはしていない。

---

## 8. 文献

- 代入可能性と正例からの学習：Clark–Eyraud, *JMLR* 8 (2007) 1725–1745；Yoshinaka, *TCS* 412 (2011) 1821–1831, doi:10.1016/j.tcs.2010.12.058（多次元代入可能性による MCFG の学習）。
- 補題A の「回路が核を張る」「回路の係数は小行列式」は線形代数・マトロイドの標準事実。補題3.2 の「疎な（R 進的に離れた）数列の部分和が相異なる」は、Erdős–Moser 型の相異なる部分和の議論として標準的な手法。
- これらを型付き分布学習の純粋 a 語の問いに組み合わせた定理B・補題A が文献に既にあるかは**未確認**（短い検索では見つけていないが、網羅的な調査はしていない）。原稿に入れる前に、著者による再検証と先行研究の確認が要る。

---

## 9. 結了の三点

1. **証明できたこと。** (R) を一般形（差は 0 か g ≥ k の倍数）で証明し、再配分が定理S の仮定を壊さないこと、合流は差し替え語の骨格の計算の問題で、非隣接に選べば避けられること（同じ節点の二成分は隣り合わない）を示した。(R) から、同じ核の頻出の両文字型ラベルの損失が (e, β, γ) の線形関数になること（補題A）を導き、尺度の漸化式と疎な鎖の部分和の議論で **μ_a ≤ K^{3D+1}R^{3D}θ**（定理B）を得た。D は核の種類で決まる量で、s・h・ラベル数に依らない。特に、場合 I で頻出の両文字型の代表の核が一つなら、ファンアウト ≤ 2・任意ランク・任意の入れ子の深さで μ_a は多項式（系4.1）。場合 II・III も同じ形。
2. **止まった場所。** 核の種類 D が有界でない場合。異なる核をまたぐ (R) の制約は、塊の順序（ファンアウト2では成分の入り組み方）がそろった配置を要し、一般には取れない。F 分岐の段数 s そのものは抑えていない。反例族も作れていない。
3. **次に絞るべき一点。** **異なる核 κ ≠ κ' の頻出ラベルどうしの関係を作れるか。** 具体的には、核 κ の塊どうしが隣り合うと別の核に合流する（例：bc と bc が隣り合うと核 abcbca）ことを逆に利用して、核の異なるラベルを同じ骨格の配置にそろえ、区分の線形部分を共有させる（D の中の類の数への依存を消す）こと。逆に否定側では、Ω(n/log n) 個の相異なる核に倍増の各段を割り当て、かつ定理3.2 の偶数の塊と □/□a の漏れの両方を避ける文法を設計し、arity 1・2 の代入可能性を直接証明すること。
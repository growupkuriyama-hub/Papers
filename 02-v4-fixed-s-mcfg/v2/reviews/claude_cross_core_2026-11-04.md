# 異なる核をまたぐ関係と塊の融合：場合 I での多項式上界（三文字内容型付け・系列の十二本目、Claude 版）

**研究日**：2026-11-04
**対象**：栗山貴之、論文 #2、`op:fanout-two` の三文字の核（純粋 a 語の問い Q）
**資料**：公開リポジトリ `growupkuriyama-hub/Papers` を取得（commit `96b71cc`、2026-11-04 15:47 JST）。`main.tex`、前回の報告 `claude_f_branching_2026-11-04.md`（README (122)）、`chatgpt_nested_bc_chain_2026-11-04.md`、`chatgpt_weighted_codes_2026-11-02.md`、`chatgpt_skeleton_diversity_2026-11-02.md`、`chatgpt_a_spectrum_2026-11-03.md` を直接読んだ。
**立場**：独立査読の前の研究ノートである。**Q は全体としては解決していない。** ただし今回、**場合 I（b⁴ と c⁴ が現れる）では、条件 (S1) の下で μ_a ≤ poly_r(v, θ)** を証明した（定理D）。(S1) はファンアウト1の表示では N_bc が小さいとき以外は自動的に成り立つので、**場合 I・ファンアウト1の表示では Q は肯定的に解ける**（系D）。鍵は二つの新しい移送、詰め物付きの交換（補題E）と、a の移送による塊の融合（補題F）である。

---

## 0. 主張ごとの判定

| 主張 | 判定 | 根拠・限定 |
|---|---|---|
| **補題E**（詰め物付きの交換）：内部の両文字型ラベル X, Y の融合した塊 F_X, F_Y について D(a^{1+d_Y−d_X}F_X) = D(aF_Y)（d_X ≤ d_Y ≤ k−3） | **証明済み** | §2.1。arity 1 と a の連の再配分だけを使う。場合 I–III・ファンアウト ≤ 2 で成り立つ。頻出性は要らない |
| **補題F**（a の移送・融合）：先頭と末尾が a でない u が、ある語で左が長さ2以上の a の極大連と a の極大連に挟まれていれば D(a²u) = D(aua) | **証明済み** | §2.2。帰結：塊の間の一文字の a は自由に取り除け（融合）、また入れられる（分離） |
| 系2.3：各内部の両文字型ラベル X の代表は、a を含まない一つの塊 F_X に融合でき、損失 d_X はそのまま | **証明済み** | §2.3。ファンアウト2の二成分も一つにまとまる |
| **(O)**（順序をそろえた配置による核をまたぐ関係） | **正しい（ただし定式化を直した）** | §3。(i) 順序は補題E で常に実現できる。(ii)「両方の類に共通の差」だけでは足りず、3類以上にまたがる関係（差の空間が1次元のとき）も要る。正しい形は定理C |
| **定理C**：(S_M) の下で、低い内部の両文字型ラベル全てについて d_X = Λ(κ_X) + μβ_X + νγ_X（μ, ν は核によらない） | **証明済み** | §3。D を 2+3m_u+m_n から **m+4** に改良（m は融合した核の種類）。頻出性・一様性の条件は不要 |
| 定理C だけでは核の種類 m が指数に入る | **自明に成り立つが目的には足りない** | §3.4。(O) の改良はここまで |
| **(M)**（合流による核どうしの関係） | **正しく、しかも条件なしに起こる** | §4。補題F により、二つの塊が分離した語があれば、隣り合わせた（合流した）語も必ず L に入る。λ(κ⋈κ') = λ_κ + λ_κ'（定数の欠損なし） |
| **補題P**（場合 I、偶奇類の線形性）：同じ先頭文字・同じ連の数の偶奇の類 P の中で、d_X = ⟨φ_P, (n'_X, β_X, γ_X)⟩ | **証明済み（(S1) の下）** | §5.2。融合した鎖の核は (先頭文字, Σn') だけで決まる。場合 I に固有（b と c の連を両方縮めるので、核は交代語になる） |
| **定理D**：場合 I、(S1) の下で μ_a ≤ max{4θ+8, K_D^{43}R^{42}θ} | **証明済み** | §5.3。K_D = (2v+E_D)(2r+1)、E_D = v(48θ³+θ+20)、R = θ+2v+2。**核の種類にもラベル数にも依らない** |
| **系D**：場合 I で G がファンアウト1なら μ_a ≤ poly_r(v, θ)（無条件） | **証明済み** | §5.4。(S1) が成り立たなければ N_bc ≤ 3v で、第十報の (4.2) |
| 場合 I・ファンアウト2で (S1) が成り立たない場合（全ての内部の両文字型節点の範囲が一点を共有する「跨ぎ」の場合） | **未解決** | §5.5。二穴の組による同じ議論の筋は書いたが、証明していない |
| **(N)**（入れ子の類の尺度） | **補題E・F に吸収された。「二段の比を poly で抑える」は自明に成り立つが目的には足りない** | §6。隣り合う群の値の比は既に K 以下（前回の補題3.1）。問題は段の数 |
| 場合 II・III | **定理C（D = m+2, m+3）まで。偶奇類の線形性に当たるものは不成立の見込み（観察）** | §7。鎖の核が一致するのは、原始的な語の冪どうしなどに限られる |
| 反例族 | **未構成。場合 I・ファンアウト1では存在しない（系D）** | §8。残る候補の形を絞った |
| 有限の検査 | **有限の対象について完全な判定／有限の健全性検査** | §9。強制閉包による短い純粋 a 語の証明書を含む |
| 補題E・F・定理C・D の文献上の新規性 | **未確認** | §10 |

---

## 1. 記号と引用の確認

Σ={a,b,c}、内容型付け c、L ∈ C_{2,c}。G は L∩Σ⁺ の reduced good な表示で、ファンアウト ≤ 2、ランク ≤ r。v = |V|、θ = θ̄_G、k = μ_a(L) ≥ 5。T は a^k の節点数最小の一様な導出（第十報 §2、前回 §1）。X ⊆ {b,c} は x⁴ が L の語に現れる文字の集合、σ_X は a と X の文字の連を縮める写像。場合 I は X = {b,c}。

両文字型ラベル X に短い代表 ρ_X（総長 ≤ θ）を一つ選び、d_X = ℓ_X − |ρ_X|_a（≥ 3）、β_X = |ρ_X|_b、γ_X = |ρ_X|_c。

**節点・ラベルの言葉づかい。** 節点の**範囲**は、その出力の最初の文字から最後の文字までの a^k の区間（ファンアウト2では二成分とその間）。節点が**内部**とは、範囲が a^k の最初の文字も最後の文字も含まないこと。ラベルが**内部**とは、内部の出現を持つこと。内部でないラベルの出現は2個以下（同じラベルの出現は反鎖なので、最初の文字を含むものと最後の文字を含むものが一つずつ）。

**引用し、改めて確かめたもの。**

- 命題1.1 (R)（前回）：σ_X が等しく、b, c の個数が等しく、a の個数が正の二語は、a の個数の差が 0 か g ≥ k の倍数。証明は系2.2（x⁴ による x の連の再配分）と定理S。前回の段ごとの検証をもう一度追った。
- 系2.2（weighted_codes）の a についての場合：a⁴ が現れる（a^k、k ≥ 5）ので、**a の極大連の長さは、総数を保てば自由に配り直せる**（各連は正の長さ）。以下「再配分」はこれを指す。
- (K) の §3.1–3.2（第十報）：非飽和の色の一色型は全体で 18v 以下、出現 ≤ θ の一色型は vθ 以下、飽和の色の頻出の一色型は ℓ = p + α_x q（p ≤ θ、1 ≤ q ≤ θ）。前回の §3.1 で確かめたとおり。
- 補題3.1・3.2（前回）：群の値が窓 [D, D+θ] を持てば、隣どうしの値の比は K 以下、比 R 以上で上がる鎖は 3D 段以下。これらは「群の値が、各区分で整数点の線形関数」であることしか使わない。
- 第十報の (4.2)：k ≤ 19(r+1)³v³θ³(θ+N_bc+20)³。

---

## 2. 二つの新しい移送

### 2.1 補題E：詰め物付きの交換

a を含まない語 P（b と c を共に含む）が**単一塊の性質** SB(P, d) を持つとは、全ての s, t ≥ 1、s+t = k−d について a^s P a^t ∈ L であること。

**補題E。** P, Q が SB(P, d_P)、SB(Q, d_Q) を持ち、d_P ≤ d_Q ≤ k−3 なら

D_L(a^{1+d_Q−d_P} P) = D_L(a Q)。

**証明。** 二つの語の内容はどちらも {a,b,c}。文脈 □·a^{k−d_Q−1}（左は空）は、a^{1+d_Q−d_P}P を a^{1+d_Q−d_P}P a^{k−d_Q−1}（a の個数の和 k−d_P）に、aQ を aQa^{k−d_Q−1}（和 k−d_Q）に写し、SB によりどちらも L に入る。arity 1 の代入可能性で分布は等しい。□

**読み方。** 「a のどの位置でも、塊 Q とその前の a 一つを、塊 P とその前の a^{1+d_Q−d_P} に置き換えてよい（逆も）」。値（a に直した長さ）の帳尻が合っていれば、塊の種類はどれでも交換できる。

### 2.2 補題F：a の移送と融合

**補題F。** u ∈ Σ⁺ の最初と最後の文字は a でないとする。L のある語が w = P' a^i u a^t Q'（i ≥ 2、t ≥ 1、a^i と a^t は極大連）の形をしているなら、D_L(a²u) = D_L(aua)。

**証明。** 内容はどちらも {a} ∪ c(u)。文脈 E = P'a^{i−2} □ a^t Q' について E[a²u] = w ∈ L、E[aua] = P'a^{i−1}ua^{t+1}Q' は w の再配分（a^i から a^t へ一文字。間の u は空でなく a 以外の文字を含むので、二つの連は別の連）なので L に入る。arity 1 の代入可能性による。□

**系F（融合と分離）。** 補題F の u について、L の語 P'' a^p u a v Q''（p ≥ 1、v は a 以外の文字で始まる）があれば P'' a^{p+1} u v Q'' ∈ L（**融合**：u と次の塊の間の一文字の a を左へ移す）。逆に P'' a^{p} u v Q''（p ≥ 2）があれば P'' a^{p−1} u a v Q'' ∈ L（**分離**）。

**証明。** 融合：文脈 P''a^{p−1}□vQ'' は aua を受理するので a²u も受理する。分離はその逆。□

これは**場合 I–III のどれにも依らない**（a⁴ と arity 1 だけを使う）。σ_X は融合で変わる（例：abcabca → abcbca）が、a の個数は変わらない。

### 2.3 融合した塊

**系2.3。** X を内部の両文字型ラベル、ρ_X の a を含まない極大な部分を左から s_1, …, s_m（ファンアウト2では第一成分のもの、続いて第二成分のもの）とし、F_X := s_1 s_2 ⋯ s_m（連結）とおく。k − ℓ_X ≥ θ + 2 なら SB(F_X, d_X)。

**証明。** X の内部の出現 x をとり、x だけを ρ_X に替えた語 W_x ∈ L（a の個数 k − d_X）を考える。範囲が内部なので両端に a があり、ファンアウト2の二成分の間にも a がある（前回の補題1.3）。W_x の a の連は全て極大で、再配分で自由に変えられる。j に関する帰納法で、「s_1⋯s_j が一つにつながり、残りの間の a は一文字ずつ、左端の連は任意に ≥ 1」の語が L に入ることを示す。j から j+1 へ：u = s_1⋯s_j は補題F の仮定を満たす（左端の連を ≥ 2 にした同じ語が証拠）。系F の融合で s_{j+1} とつなぐ。a の個数は変わらない。必要な a の数は連の数 + 1 以下（≤ θ+2）で、k − ℓ_X ≥ θ+2 から足りる。最後に a^s F_X a^t の形に再配分する。□

F_X は b と c を含む a のない語で、損失は d_X、b, c の個数は β_X, γ_X のまま。

---

## 3. (O) の検証と定理C

### 3.1 (O) の各点

**(i) 順序の実現。** (O) は、核 κ の出現 x_i が核 κ' の出現 y_i の左にある配置を二組要求する。T の中でそれが取れる保証はない（例えば X₁ の出現が全て Y₁ の出現の右にあることはありうる）。しかし補題E により、T の中で**範囲が互いに素な**内部の両文字型節点が n 個あれば、それらの塊をどのラベルの融合した塊にも、**どの順序でも**置き換えられる（次の補題V）。したがって順序の問題は消える。

**補題V（仮想の配置語）。** T に、範囲が互いに素な内部の両文字型節点 z_1, …, z_n があるとする。内部の両文字型ラベル Y_1, …, Y_n（重複・順序は任意）が k − ℓ_{Y_i} ≥ θ+2 と Σ_i d_{Y_i} ≤ k − 2n − 2 を満たすなら、全ての x_0, …, x_n ≥ 1、Σx_i = k − Σd_{Y_i} について

a^{x_0} F_{Y_1} a^{x_1} F_{Y_2} ⋯ F_{Y_n} a^{x_n} ∈ L。

**証明。** z_i を全て ρ に替えた語は L に入る。各 z_i の範囲の中で系2.3 の融合を行う（補題F の D の等式はどの文脈でも使えるので、証拠は各ラベルの単一塊の語でよい）。範囲が隣り合っているものは系F の分離で a を一つ入れる。こうして a^{x}F_{Z_1}a⋯F_{Z_n}a^{x'} の形の語を得る。次に補題E で F_{Z_i} を F_{Y_i} に一つずつ替える。a の個数が増える交換を先に、減る交換を後に行い、減る交換の前には再配分でその塊の左の連を 1+d_{Y_i}−d_{Z_i} 以上にしておく。途中の a の個数は常に最終の値 k − Σd_{Y_i} ≥ 2n+2 以上なので、必要な長さは確保できる。□

**(ii) 「共通の差」の条件。** (O) の結論 ⟨φ_κ − φ_κ', Δ⟩ = 0 は、Δ が二つの類の差の空間 V_κ, V_κ' の共通部分にあるとき正しい（e の座標が等しく、σ_X が両方 κ∘κ'、b, c の個数が等しいので (R)）。しかしそれだけでは足りない。V_κ が1次元の類が三つあり、互いの共通部分が 0 でも、δ₁ + δ₂ + δ₃ = 0（δ_i ∈ V_{κ_i}）という関係がありうる。この三類の関係も同じく (R) で使える（下の証明 (c)）。正しい形は「全ての V_κ をまとめた和の写像の核の上で消える」であり、それが次の定理C になる。

**(iii) ファンアウト2の入り組み。** 系2.3 で二成分を一つの塊に融合するので、成分の入り組み方は問題にならない。ただし補題V には**範囲が互いに素な**節点が要る（§5.5）。

### 3.2 定理C

**定理C。** M_C := 24θ² とし、ℓ_X ≤ k/(2M_C) のラベルを**低い**と呼ぶ。k ≥ 4M_C+4θ+8、かつ T に範囲が互いに素な内部の両文字型節点が M_C 個ある（条件 (S_{M_C})）とする。融合した核 κ_X := σ_X(aF_Xa) とおく。このとき、核の関数 Λ と有理数 μ, ν があって、全ての低い内部の両文字型ラベル X について

d_X = Λ(κ_X) + μβ_X + νγ_X。

**証明。** (a) **比較の道具。** 低いラベルの列 Y_1, …, Y_n（n ≤ M_C）の仮想の配置語は補題V により L に入る（Σd ≤ k/2）。二つの多重集合 𝒜, ℬ が、各核について同じ個数のラベルを含み、Σβ, Σγ が等しいとき、どちらも核ごとに並べた配置語を作ると、前回の補題1.2 により σ_X は同じ（核の ∘ 積）、b, c の個数も同じ、a の個数は (0,k) にある。(R) により Σ_{𝒜} d = Σ_{ℬ} d。

(b) **類の中。** 核 κ の類で、ベクトル (1, β_X, γ_X) の回路の関係（大きさ ≤ 4、係数は 3×3 以下の小行列式で ≤ 6θ²、片側 ≤ 24θ² 個）に (a) を使い、前回の補題A と同じ線形代数で d_X = λ_κ + ψ_κ(β_X, γ_X)（ψ_κ は V_κ 上の線形形式として定まる）。

(c) **類をまたぐ関係。** 各類 κ で、差 v_X − v_{X₀}（v = (β, γ)、成分の絶対値 ≤ θ−1）からなる V_κ の基底を選び、全ての類の基底ベクトルを並べた 2×B 行列 U をとる。⊕_κ V_κ → ℚ²（和）の核は、基底の座標では ker U そのものであり、U の回路（大きさ ≤ 3、係数は 2×2 小行列式で ≤ 2θ²）で張られる。回路 Σ_i c_i(v_{X_i} − v_{X_{0,i}}) = 0 に対し、片側に「c_i > 0 なら X_i を c_i 個、c_i < 0 なら X_{0,i} を |c_i| 個」、もう片側に残りを置くと、各類の個数は両側で等しく（各 i が両側に |c_i| 個ずつ寄与する）、b, c の総数も等しい。片側 ≤ 6θ² 個。(a) により Σ_i c_i ψ_{κ(i)}(u_i) = 0。したがって ⊕ψ_κ は和の写像の核で消え、ℚ² 上の線形形式 (μ, ν) に延びる：ψ_κ = (μ,ν)|_{V_κ}。Λ(κ) := d_{X₀} − μβ_{X₀} − νγ_{X₀} とおけばよい。□

### 3.3 定理C から出る上界

**系C。** 定理C の条件の下で、例外を「一色型の例外（18v + vθ）、内部でないラベルの節点（≤ 2v）、高い両文字型の節点（一つの深さに ≤ 2M_C 個、計 ≤ 2M_C v）」とし、E_C := v(48θ² + θ + 20)、K_C := (2v+E_C)(2r+1) とおく。m を低い内部の両文字型ラベルの融合した核の種類の数とすると、D := m + 4 で

k ≤ K_C^{3D+1} R^{3D} θ、 R = θ+2v+2。

**証明。** 低い内部の両文字型ラベルの群の値 d_X = Λ(κ_X) + μβ_X + νγ_X は、点 (e_κ, β, γ) ∈ {0,1}^m × [1,θ]² の一つの線形形式（次元 m+2）。一色型の二つの区分（次元1ずつ）と合わせて D = m+4。前回の補題3.1・3.2 をそのまま使う。□

ファンアウト1で (S_{M_C}) が成り立たないなら、各深さの内部の両文字型節点は M_C 個未満（同じ深さの節点は範囲が素）で、N_bc < v(M_C + 2)、(4.2) で多項式。

### 3.4 定理C の弱さ

D = m+4 は前回の 2+3m_u+m_n より小さく、頻出性・一様性の条件も消えた。しかし **m（核の種類）がそのまま指数に入る**ことは変わらない。全ての核が異なれば m はラベル数と同程度である。(O) だけでは、核ごとの定数項 Λ(κ) の間に関係が生じないからである。これを解くのが次の §4–5 の融合である。

---

## 4. (M)：合流による関係は条件なしに起こる

依頼の (M) は「二つの塊を隣り合わせて置ければ」と仮定していた。補題F により、**分離した二塊の語があれば、隣り合わせた語は自動的に L に入る**（系F の融合）。a の個数は変わらないので、融合した塊 F_X F_Y の損失はちょうど d_X + d_Y（**欠損なし**）。

**命題4.1。** 補題V の条件（n=2）の下で、低い内部の両文字型ラベル X, Y について SB(F_X F_Y, d_X + d_Y)。さらに鎖 F_{X_1} ⋯ F_{X_t}（t ≤ 24θ³、各 ℓ ≤ k/(2·24θ³)、k ≥ 4θ+8）も SB(⋯, Σd)。

**証明。** 補題V で a^p F_X a F_Y a^q ∈ L（間の a は一文字）。u = F_X に補題F（証拠は SB(F_X) の語で左の連を 2 にしたもの）、系F で融合して a^{p+1}F_X F_Y a^q。再配分で SB。鎖は帰納法：既に作った鎖 C も SB を持つので補題E で交換でき、C と F_X の分離した二塊の語を作ってから融合する。a の予算は Σd ≤ k/2 から足りる。□

依頼の例：bc と bc を隣り合わせると σ(abcbca) = abcbca で κ∘κ = abcabca とは別の核になり、**その核のラベル Z が b, c を同じ個数持てば d_Z = 2d_{bc}** が (R) から出る。§9 の Part D はこの機構を有限の言語で確かめたもの：{a¹²} と、bc の単一塊の語（損失3）、bc が二つ離れた語、bcbc の単一塊の語（損失9 ≠ 6）を含む L ∈ C_{2,c} は存在しない（強制閉包が a³ を生む）。損失を 6 にすると閉包は 59 語で止まり、それ自体が代入可能な有限言語になる。二塊の語を除くと矛盾は生じない（融合には分離した二塊の語が要る）。

---

## 5. 場合 I：偶奇類の線形性と多項式上界

### 5.1 場合 I での核の形

場合 I では σ_X は b と c の連を両方縮めるので、a を含まない語 F の核 σ(aFa) は a·(b と c の交代語)·a であり、**先頭の文字 f ∈ {b,c} と連の数 n ≥ 1** だけで決まる。最後の文字は n が奇数なら f、偶数なら f の反対。二つの語の連結の連の数は n(F) + n(G) − [F の最後 = G の最初]（§9 Part A）。

両文字型の X の**型**を F_X の (f_X, n_X)（n_X ≥ 2）、**偶奇類** P(X) := (f_X, n_X mod 2)、n'_X := n_X（偶数）または n_X − 1（奇数）と定める。同じ偶奇類の語の連結では：偶数なら最後の文字 ≠ 次の最初の文字で連は足し算、奇数なら毎回一つずつ合わさる。したがって**同じ偶奇類の鎖の核は (f, Σn') だけで決まる**（偶数類の連の数 Σn'、奇数類 Σn' + 1）。ラベルの個数にも順序にも依らない。

### 5.2 補題P

**条件 (S1)。** T に、範囲が互いに素な内部の両文字型節点が二つある。

**補題P。** 場合 I、(S1)、k ≥ 4θ+8 とし、N_c := 24θ³、ℓ_X ≤ k/(2N_c) のラベルを低いと呼ぶ。各偶奇類 P について φ_P ∈ ℚ³ があり、P に属する全ての低い内部の両文字型ラベル X について

d_X = ⟨φ_P, (n'_X, β_X, γ_X)⟩。

**証明。** P のラベルの多重集合 𝒜, ℬ（各 ≤ N_c 個）が Σn', Σβ, Σγ を共有するとする。命題4.1 により、𝒜 の鎖 C と ℬ の鎖 C' は SB(C, Σ_𝒜 d)、SB(C', Σ_ℬ d) を持つ（命題4.1 の二塊の語には (S1) の二節点を使う）。§5.1 により σ(aCa) = σ(aC'a)、b, c の個数は等しく、a の個数 k − Σd は (0,k) にある。(R) により Σ_𝒜 d = Σ_ℬ d。ベクトル (n', β, γ) ∈ [1,θ]³ の回路（大きさ ≤ 4、係数 ≤ 3!θ³ = 6θ³、片側 ≤ 24θ³ = N_c 個）は核を張るので、d はこの行列の行空間に入る。□

**注意。** 関係は**ラベルの個数が違う**多重集合どうしでも成り立つ（鎖の核は個数によらない）。そのため φ_P には定数項がない。前回の定理B・今回の定理C で核ごとに必要だった定数項 Λ(κ) が、ここで全て φ_P の第一成分 × n' にまとまる。これが核の種類への依存を消す点である。

### 5.3 定理D

**定理D。** 場合 I、ファンアウト ≤ 2、ランク ≤ r、条件 (S1) の下で

μ_a(L) ≤ max{4θ+8, K_D^{43} R^{42} θ}、 K_D := (2v+E_D)(2r+1)、 E_D := v(48θ³+θ+20)、 R := θ+2v+2。

**証明。** k ≥ 4θ+8 とする。重い節点を次のように分ける。
- 例外：一色型の例外 18v + vθ、内部でないラベルの節点 ≤ 2v、高い（ℓ > k/(2N_c)）両文字型の節点（一つの深さに ≤ 2N_c 個、計 ≤ 2N_c v = 48θ³v）。合計 E_D。
- 群：飽和の色の頻出の一色型（値 α_x q、窓 [α_x q, α_x q+θ]）と、低い内部の両文字型（値 d_X、窓 [d_X, d_X+θ]、ℓ_X = d_X + |ρ_X|_a）。

補題P により、両文字型の群の値は四つの区分（偶奇類）それぞれで、点 (n', β, γ) ∈ [1,θ]³ の線形形式。一色型は二つの区分（点 q）。D = 4·3 + 2 = 14。前回の補題3.1（K = K_D）と補題3.2（n ≤ 3D）により k ≤ K_D·D̂_m ≤ K_D^{3D+1}R^{3D}θ = K_D^{43}R^{42}θ。□

### 5.4 系D：ファンアウト1の表示

**系D。** 場合 I で G がファンアウト1（CFG）なら

μ_a(L) ≤ max{4θ+8, 19(r+1)³v³θ³(θ+3v+20)³, K_D^{43}R^{42}θ}。

**証明。** (S1) が成り立てば定理D。成り立たないとき、ファンアウト1では祖先関係にない二節点の範囲は素なので、内部の両文字型節点は全て祖先関係で比べられ、一本の根からの道に乗る（≤ v 個）。範囲が最初か最後の文字を含む節点は各深さに ≤ 2 個。よって N_bc ≤ 3v で、第十報の (4.2)。□

**範囲の明記。** これは Σ={a,b,c}、内容型付け、L ∈ C_{2,c}（arity 1 と 2 の代入可能性）、**b⁴ と c⁴ が L の語に現れる場合**で、L の**ファンアウト1の** reduced good な表示 G についての上界である。L がファンアウト2の小さい表示しか持たない場合は、定理D の (S1) が要る。**op:fanout-two の三文字の核の全体を解いたわけではない。**

### 5.5 残る場合：ファンアウト2の跨ぎ

(S1) が成り立たないとき、内部の両文字型節点の範囲（区間）は互いに交わる。区間の族が互いに交われば共通の点を持つので（一次元の Helly の性質）、**全ての内部の両文字型節点の範囲が、a^k のある一つの位置 p を含む**。反鎖の中で p を成分の中に含む節点は一つ以下なので、ほとんどの節点は「第一成分が p の左、第二成分が p の右」に跨ぐ。これは a^n b^n 型の入れ子・交差である。

ここでは塊が連続しないので補題E の一穴の交換が使えない。二穴の組 (a^i ρ^1, ρ^2 a^j) で同じ交換を行い、左右の成分をそれぞれ融合する「二穴の鎖」を作れば、補題P と同じ議論の筋が通ると考えている：入れ子・交差の対から左半分どうし・右半分どうしをつなぎ、型は (左の型, 右の型) の偶奇類で 16 通り程度、成分ごとの内容の型で 9 通り程度に分かれる。**証明は書いていない（未解決）。**

---

## 6. (N) について

(N) が狙っていた「分布の等式を別の出現の文脈や配置語の中に運ぶ」ことは、補題E（任意の塊どうしの交換）と補題F（融合と分離）が一般的な形で実現している。段の交換 (L) は、その特別な場合（内容が一致する組の分布の等式）にあたる。

依頼 §3-2 の「鎖の隣り合う二段の尺度の比を poly で抑える」は、**前回の補題3.1 で既に成り立っている**（隣り合う群の値の比 ≤ K、疎な鎖の一段は ≤ KR）。自明に成り立つが目的には足りない。問題は比ではなく**段の数**であり、段の数は区分の次元の和 D で抑えられる（補題3.2）。今回の定理D は D を定数 14 にすることで段の数を抑えた。

---

## 7. 場合 II・III

補題E・F・V と定理C は場合によらない（定理C の D は場合 II で m+2、場合 III で m+3。β, γ の一部が核で決まるため）。偶奇類の線形性（補題P）は場合 I に固有である。

- **場合 II**（X=∅）：核は a を含まない部分の**語そのもの**。鎖 F_X^t と F_Y^{t'} の核が一致するのは F_X^t = F_Y^{t'} のときで、Lyndon–Schützenberger の定理により F_X, F_Y が同じ原始的な語の冪のとき。したがって鎖から出る関係は「原始根 u ごとに d が冪の指数に比例」までで、ラベルの融合した語が符号（一意分解）をなせば、それ以上の関係は鎖からは出ない（観察）。
- **場合 III**（X={b}）：b の連だけを縮めるので、中間の状況。未検討。

場合 II の既報の候補 (bc)^i bb（weighted_codes）は arity 1 で破れていた。補題F は、反例の言語が**全ての塊の対の融合**（例えば (bc)^i bb (bc)^j bb、b の連が 3）も含むことを要求する。

---

## 8. 否定側

**新しい候補は作れなかった。** 今回の結果から、反例（三文字、多項式サイズ・厚さ、超多項式の μ_a、L_n ∈ C_{2,c}）が満たすべきことは次のとおり（証明済みの部分）。

1. **場合 I なら**：L_n のどのファンアウト1の表示でもない（系D）。ファンアウト2の表示 G_n では、内部の両文字型節点が全て一点を跨ぐ（§5.5）。
2. **場合 II・III なら**：融合した核の種類 m = Ω(log k / log(K_C R))（系C の対偶）。かつ L_n は、全ての塊の任意の順序の配置（補題V）と、その全ての融合・分離（補題F）を含む。したがって文法は、塊の任意の並べ替えと、隣接・分離の全ての組み合わせを、一定の a の帳尻のもとで生成しなければならない。
3. 既報の障害（□/□a の漏れ、偶数の塊、(R)）に加えて、補題F が新しい漏れの型を与える：a²u と aua の同値。融合した対の損失が足し算にならない設計は全て壊れる（§9 Part D）。

2 の「任意の並べ替えを小さい文法で生成する」ことには、置換言語の CFG の大きさの下界（例えば全ての置換の言語は指数サイズの CFG を要する）と似た障害がありそうだが、**これは観察で、証明していない**。

将来下界を述べるときの量化は第十報 §7.2 のとおり：作用素 B^{≤r}_{2,c}、B_{2,c}、クラス全体に特徴標本を持つ集合駆動作用素；Σ={a,b,c}、ファンアウト ≤ 2、ランク ≤ 2；L_n ∈ C_{2,c} を直接証明。**今回は下界を主張しない。**

---

## 9. 計算

Python 3 の標準ライブラリだけで書いた。Windows では `py -3 claude_cross_core_check.py`。この環境で `python3 -I` により実行し（約4秒）、出力をそのまま載せる。説明文の不等式と assert の不等式はそろえた（前回の指摘：今回 Part C は n ≤ 3D をそのまま検査する）。

- Part A：交代語の連結の連の数、冪の連の数、同じ偶奇類での核の一致（§5.1）。連の数 ≤ 8、連の長さ 1–2 の全ての語で総当たり。
- Part B：(n', β, γ) ∈ [1,θ]³ の全ての回路の係数の最大値（θ = 2, 3, 4）が 6θ³ 以下。Cramer の上界の**有限の確認**で、証明は §5.2。
- Part C：前回の補題3.2 の鎖の長さ n ≤ 3D の健全性検査（乱数と大きな係数）。**証明の代わりではない。**
- Part D：有限の種の集合の、(1,c)・(2,c) 代入可能性による**強制閉包**。加える語は全て「種が L ∈ C_{2,c} に含まれれば L に入る」語なので、a^j（j < k）が出れば、それは「μ_a(L)=k で種を含む L ∈ C_{2,c} はない」ことの**証明書**である。閉包が止まれば、その有限言語は代入可能（別の判定器で再確認）。§4 の手書きの証明書も段ごとに確かめた：(1) 文脈 (aaa, aaaa) が aabc と abca を受理するので D(aabc) = D(abca)；(2) 二塊の語 aabcabcaaa に文脈 (a, bcaaa) で abca が現れるので、融合した aaabcbcaaa（a の個数 6）が入る；(3) 単一塊の abcbcaa（a の個数 3）と同じ a 骨格で差 3 < 12 なので、定理S により a⁹ ∈ L、矛盾。

```python
#!/usr/bin/env python3
"""Checks for claude_cross_core_2026-11-04.md (Python 3 standard library only).

Windows: py -3 claude_cross_core_check.py

Part A  run counts of concatenations of alternating {b,c}-words (case I cores):
        sigma(a F G a) has n(F)+n(G)-[last(F)=first(G)] runs; for a parity class
        the t-fold power has t*n runs (n even) or t*(n-1)+1 runs (n odd).
        Brute force over all words with <= 8 runs and run lengths 1..2.
Part B  circuits of vectors (n', beta, gamma) in [1, theta]^3: max |coef| <= 6 theta^3
        (theta = 2, 3, 4).  A finite check of the Cramer bound of Lemma 5.3.
Part C  the lacunary chain bound n <= 3D of Lemma 3.2 of the previous report
        (the assert now checks exactly n <= 3D).
Part D  forced closure of FINITE seed sets under (1,c),(2,c)-substitutability.
        Every word added is forced: if the seed lies in some L in C_{2,c}, so does
        the word.  Finding a pure a^j with j < k is therefore a certificate that no
        L in C_{2,c} with mu_a(L) = k contains the seed.  A fixpoint is an exactly
        (1,c),(2,c)-substitutable finite language (re-checked independently).
"""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations, product
import random


# ---------------------------------------------------------------- Part A
def runs(word):
    out = []
    for ch in word:
        if not out or out[-1] != ch:
            out.append(ch)
    return ''.join(out)


def alt_words(max_runs):
    for n in range(2, max_runs + 1):
        for first in 'bc':
            other = 'c' if first == 'b' else 'b'
            letters = [first if i % 2 == 0 else other for i in range(n)]
            for lens in product((1, 2), repeat=n):
                yield ''.join(x * l for x, l in zip(letters, lens))


def partA():
    ws = list(alt_words(6))
    for F in ws:
        for G in ws:
            r = runs(F + G)
            assert len(r) == len(runs(F)) + len(runs(G)) - (F[-1] == G[0])
    for F in alt_words(8):
        n = len(runs(F))
        for t in range(1, 5):
            m = len(runs(F * t))
            assert m == (t * n if n % 2 == 0 else t * (n - 1) + 1), (F, t)
    # equal cores inside one parity class: (first letter, sum of n')
    for F in alt_words(5):
        for G in alt_words(5):
            if F[0] != G[0] or len(runs(F)) % 2 != len(runs(G)) % 2:
                continue
            nf, ng = len(runs(F)), len(runs(G))
            pf = nf if nf % 2 == 0 else nf - 1
            pg = ng if ng % 2 == 0 else ng - 1
            g = gcd_list([pf, pg])
            assert runs(F * (pg // g)) == runs(G * (pf // g))
    print('Part A: PASS (fusion run counts, powers, equal cores in a parity class)')


# ---------------------------------------------------------------- Part B
def det3(u, v, w):
    return (u[0] * (v[1] * w[2] - v[2] * w[1]) - u[1] * (v[0] * w[2] - v[2] * w[0])
            + u[2] * (v[0] * w[1] - v[1] * w[0]))


def gcd_list(xs):
    g = 0
    for x in xs:
        a, b = abs(x), g
        while b:
            a, b = b, a % b
        g = a
    return g


def rank_vecs(vs):
    m = [[Fraction(x) for x in v] for v in vs]
    rk, col = 0, 0
    while rk < len(m) and col < 3:
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


def three_circuit(u, v, w):
    """Primitive relation of three pairwise independent coplanar vectors."""
    for (i, j) in ((0, 1), (0, 2), (1, 2)):
        d = lambda x, y: x[i] * y[j] - x[j] * y[i]
        c = (d(v, w), -d(u, w), d(u, v))
        if any(c) and all(c[0] * u[r] + c[1] * v[r] + c[2] * w[r] == 0 for r in range(3)):
            g = gcd_list(c)
            return [x // g for x in c]
    return None


def partB():
    for theta in (2, 3, 4):
        vecs = list(product(range(1, theta + 1), repeat=3))
        worst = 0
        for u, v in combinations(vecs, 2):          # size-2 circuits: parallel
            if rank_vecs([u, v]) == 1:
                worst = max(worst, max(max(u), max(v)))
        for u, v, w in combinations(vecs, 3):
            if det3(u, v, w) == 0 and all(rank_vecs([x, y]) == 2
                                          for x, y in ((u, v), (u, w), (v, w))):
                c = three_circuit(u, v, w)
                assert c is not None and all(c)
                worst = max(worst, max(abs(x) for x in c))
        for quad in combinations(vecs, 4):
            ds = [det3(*[quad[j] for j in range(4) if j != i]) for i in range(4)]
            if all(ds):
                c = [(-1) ** i * ds[i] for i in range(4)]
                g = gcd_list(c)
                worst = max(worst, max(abs(x) // g for x in c))
        print('Part B: theta', theta, 'max |circuit coef|', worst,
              'bound 6*theta^3 =', 6 * theta ** 3)
        assert worst <= 6 * theta ** 3
    print('Part B: PASS (finite check of the Cramer bound)')


# ---------------------------------------------------------------- Part C
def greedy_chain(values, R):
    vals = sorted(values)
    chain = [vals[0]]
    while True:
        nxt = [x for x in vals if x >= R * chain[-1]]
        if not nxt:
            return chain
        chain.append(nxt[0])


def partC(seed=20261104):
    rnd = random.Random(seed)
    worst = 0.0
    for _ in range(3000):
        theta = rnd.randint(2, 6)
        v = rnd.randint(2, 40)
        dims = [rnd.randint(1, 3) for _ in range(rnd.randint(1, 4))]
        D = sum(dims)
        R = theta + 2 * v + 2
        values = set()
        for d in dims:
            if rnd.random() < 0.5:
                T = rnd.choice([10 ** 6, 10 ** 12, 3 ** 40])
                phi = [T ** i for i in range(d)]
            else:
                phi = [rnd.randint(1, 10 ** rnd.randint(1, 15)) for _ in range(d)]
            for _ in range(rnd.randint(1, v)):
                p = [rnd.randint(1, theta) for _ in range(d)]
                values.add(sum(a * b for a, b in zip(phi, p)))
        values = sorted(values)[:v]
        n = len(greedy_chain(values, R))
        assert n <= 3 * D, (n, D)
        worst = max(worst, n / (3 * D))
    print('Part C: 3000 trials, max chain/(3D) = %.3f; PASS (n <= 3D)' % worst)


# ---------------------------------------------------------------- Part D
def occ(word, arity):
    n = len(word)
    if arity == 1:
        for i in range(n):
            for j in range(i + 1, n + 1):
                yield (word[i:j],), (word[:i], word[j:])
    else:
        for i in range(n):
            for j in range(i + 1, n):
                for p in range(j + 1, n):            # nonempty separator
                    for q in range(p + 1, n + 1):
                        yield ((word[i:j], word[p:q]),
                               (word[:i], word[j:p], word[q:]))


def fill(ctx, tup):
    return ''.join(c + t for c, t in zip(ctx, tup)) + ctx[-1]


def forced_closure(S, k, maxlen, rounds=12):
    S = set(S)
    for rd in range(rounds):
        new = set()
        for ar in (1, 2):
            dist = defaultdict(set)
            for w in S:
                for t, c in occ(w, ar):
                    dist[t].add(c)
            parent = {}

            def find(x):
                while parent.get(x, x) != x:
                    x = parent[x]
                return x
            by_key = {}
            for t, cs in dist.items():
                typ = tuple(frozenset(x) for x in t)
                for c in cs:
                    o = by_key.setdefault((typ, c), t)
                    ro, rt = find(o), find(t)
                    if ro != rt:
                        parent[rt] = ro
            groups = defaultdict(list)
            for t in dist:
                groups[find(t)].append(t)
            for g in groups.values():
                if len(g) < 2:
                    continue
                ctxs = set().union(*(dist[t] for t in g))
                for t in g:
                    for c in ctxs - dist[t]:
                        w = fill(c, t)
                        if len(w) <= maxlen and w not in S:
                            new.add(w)
        short = sorted((w for w in S | new if set(w) == {'a'} and len(w) < k), key=len)
        if short:
            return 'SHORT PURE WORD', short[0], S | new
        if not new:
            return 'FIXPOINT', None, S
        S |= new
    return 'ROUND LIMIT', None, S


def finite_failure(lang):
    for arity in (1, 2):
        dist = defaultdict(set)
        for w in lang:
            for tup, ctx in occ(w, arity):
                dist[tup].add(ctx)
        by_key = {}
        for tup, ctxs in dist.items():
            typ = tuple(frozenset(x) for x in tup)
            for ctx in ctxs:
                other = by_key.setdefault((typ, ctx), tup)
                if other != tup and dist[other] != dist[tup]:
                    return arity, other, tup, ctx
    return None


def block_words(k, block, d):
    return {'a' * s + block + 'a' * (k - d - s) for s in range(1, k - d)}


def seed(k, d_bcbc, pair=True):
    S = {'a' * k} | block_words(k, 'bc', 3) | block_words(k, 'bcbc', d_bcbc)
    if pair:
        S |= {'a' * p + 'bc' + 'a' * q + 'bc' + 'a' * (k - 6 - p - q)
              for p in range(1, k - 6) for q in range(1, k - 6 - p)}
    return S


def partD():
    k = 12
    cases = [('d(bcbc)=9 with a separated pair', seed(k, 9)),
             ('d(bcbc)=6 with a separated pair', seed(k, 6)),
             ('d(bcbc)=9 without a pair', seed(k, 9, pair=False))]
    for name, S in cases:
        status, word, final = forced_closure(S, k, maxlen=k + 2)
        line = 'Part D: %-34s seed %3d -> %s' % (name, len(S), status)
        if word:
            line += ' ' + word
        if status == 'FIXPOINT':
            line += ' (%d words, exact recheck: %s)' % (
                len(final), 'substitutable' if finite_failure(final) is None else 'FAIL')
        print(line)
    # the hand certificate of section 4 for d(bcbc)=9, k=12, checked step by step
    L = seed(k, 9)
    single_bc = block_words(k, 'bc', 3)
    # context (aaa, aaaa) accepts both aabc and abca (single-block bc words, a-count 9)
    assert 'aaa' + 'aabc' + 'aaaa' in single_bc and 'aaa' + 'abca' + 'aaaa' in single_bc
    assert 'aa' + 'bc' + 'a' + 'bc' + 'aaa' in L          # a . (abca) . bcaaa
    fused = 'a' + 'aabc' + 'bc' + 'aaa'                     # forced by D(aabc)=D(abca)
    assert fused == 'aaabcbcaaa' and fused.count('a') == k - 6
    assert 'a' + 'bcbc' + 'aa' in L and ('a' + 'bcbc' + 'aa').count('a') == k - 9
    print('Part D: certificate steps checked (D(aabc)=D(abca); fused a^3 bcbc a^3; '
          'Lemma S on a^3bcbca^3 vs abcbcaa gives a^9)')


if __name__ == '__main__':
    partA()
    partB()
    partC()
    partD()
```

**実行結果（2026-11-04、この環境で実行）**

```text
Part A: PASS (fusion run counts, powers, equal cores in a parity class)
Part B: theta 2 max |circuit coef| 5 bound 6*theta^3 = 48
Part B: theta 3 max |circuit coef| 22 bound 6*theta^3 = 162
Part B: theta 4 max |circuit coef| 69 bound 6*theta^3 = 384
Part B: PASS (finite check of the Cramer bound)
Part C: 3000 trials, max chain/(3D) = 0.333; PASS (n <= 3D)
Part D: d(bcbc)=9 with a separated pair    seed  21 -> SHORT PURE WORD aaa
Part D: d(bcbc)=6 with a separated pair    seed  24 -> FIXPOINT (59 words, exact recheck: substitutable)
Part D: d(bcbc)=9 without a pair           seed  11 -> FIXPOINT (21 words, exact recheck: substitutable)
Part D: certificate steps checked (D(aabc)=D(abca); fused a^3 bcbc a^3; Lemma S on a^3bcbca^3 vs abcbcaa gives a^9)
```

Part D の有限言語は場合 II（b⁴ も c⁴ も現れない）の小さい例で、補題F の機構（場合によらない）を示すためのものである。μ_a = 12 で厚さも小さくないので、Q の反例や証拠ではない。有限の検査から無限の族の所属を推定することはしていない。場合 I の同様の閉包は、arity 2 の分布の数が大きすぎてこの環境のメモリに収まらなかった（未実行ではなく、途中で停止した）。

---

## 10. 文献

- Clark–Eyraud, *JMLR* 8 (2007) 1725–1745；Yoshinaka, *TCS* 412 (2011) 1821–1831, doi:10.1016/j.tcs.2010.12.058。
- 補題F の「a の移送」は、代入可能性と冪の再配分の組み合わせとして、原稿の `lem:app-two-runs`(ii)（xy と yx の分布の等式）と同じ型の議論である。回路・Cramer の公式・一次元の Helly の性質・Lyndon–Schützenberger の定理は標準的な道具。
- 補題E・F・定理C・定理D・系D が型付き分布学習の文献に既にあるかは**未確認**（短い検索では見つけていない。網羅的な調査はしていない）。原稿に入れる前に、著者による再検証と先行研究の確認が要る。

---

## 11. 結了の三点

1. **証明できたこと。** 詰め物付きの交換（補題E）と a の移送による融合（補題F）を、場合によらず証明した。(O) は順序の実現と三類以上の関係を補って定理C の形で正しく、D は m+4 に下がる。(M) の合流は条件なしに起こり、融合した塊の損失は足し算になる。場合 I では、同じ偶奇類の鎖の核がラベルの個数によらないことから、損失が (n', β, γ) の線形関数になり（補題P）、**(S1) の下で μ_a ≤ max{4θ+8, K_D^{43}R^{42}θ}**（定理D）。ファンアウト1の表示では無条件（系D）。
2. **止まった場所。** 場合 I・ファンアウト2で、全ての内部の両文字型節点の範囲が一点を共有する「跨ぎ」の場合（§5.5）。場合 II・III では偶奇類の線形性に当たる関係がなく、定理C（D = m+2, m+3）止まり。反例は作れていない。
3. **次に絞るべき一点。** **跨ぎの場合の二穴版の補題E・F。** 二穴の組 (a^i ρ^1, ρ^2 a^j) の交換と、左右の成分ごとの融合で「二穴の鎖」を作り、補題P と同じく損失を (n'_左, n'_右, β, γ) の線形関数にできるか。できれば場合 I は（ファンアウト ≤ 2 の全ての表示で）解ける。並行して、場合 II で、融合した語が符号をなす（一意分解する）ときに、補題V・F が要求する「全ての並べ替えと融合を含む」言語が多項式サイズの文法を持ちうるかを調べること。
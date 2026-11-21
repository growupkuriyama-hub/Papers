# 段が3つ以上の 𝒦 ∩ C_{2,c_Σ}：t ≤ 4 までの上界、各段一文字の場合の上界、残る場合の特定

（2026-11-11 の依頼 README (259) への回答。Claude Fable 5.2。スクリプト `fable_three_stages_2026-11-11.py` を同時に提出。リポジトリの `main.tex` と前回の報告 `reviews/fable_content_values_2026-11-10.md` を読んだうえで書いた。）

## 0. 要約と判定の表

### 0.1 要約（5行）

1. **多項式データの方向で二つ進んだ。反例は作れなかった。** 決着はついていない。残る場合を「t ≥ 5、かつ二文字以上の段がある、かつ移動の支持が隣接する段の対 2 個で覆えない」まで狭めた。
2. **定理 A⁺** [証明済み（前回の定理 A の証明に依存）]：定理 A の仮定 t ≤ f は **t ≤ 2f** に緩められる。f = 2 では **t ≤ 4 の 𝒦 ∩ C_{2,c_Σ} で τ ≤ τ_k**（上界の式は前回と同じ）。変更は補題 M を補題 M*（一つの成分に隣接する二つの段を入れる）に替える一点だけである。
3. **系 M\*** [証明済み]：有限指数では、SUB_1,…,SUB_d が成り立てば、面の格子は「隣接する段の対 d 個で覆える S」の上で一致する。特に t ≤ 2d なら全ての arity で代入可能。Ex1（t = 3、d = 1）と Ex2（t = 5、d = 2）はこの境界のちょうど外にある。
4. **定理 B** [証明済み]：**各段が一文字（k = t）なら**、𝒦 も代入可能性も仮定せずに、任意の good な文法の全ての型付き非終端が長さ 2fkD(1+r)θ 以下の生成組を持つ（D = v(2^k−1)^f）。従って Ex2 とその族（課題1(c)）は t がいくつでも反例にならない。Ex2 の族 Ex2⁰_m では τ = 3m、文法の大きさは m の二次だった。
5. **課題2**：反例の族は作れなかった。その代わり、反例が満たすべき必要条件を四つ証明した（§6.1）：二文字以上の段がある、t ≥ 2f+1、ある arity f < d ≤ t で代入可能でない、型の文字のうち一文字の周期が 0 か超多項式のものがある。

### 0.2 判定の表

| 主張 | ラベル | 判定 | 根拠 |
|---|---|---|---|
| 補題 M*：支持が隣接対 d 個で覆える移動は arity d で戻せる | [証明済み] | 成立 | §2.1 |
| **定理 A⁺：t ≤ 2f なら τ ≤ τ_k。f = 2 なら t ≤ 4** | **[証明済み（定理 A に依存）]** | 成立 | §2.2 |
| 系 M*：有限指数で SUB_{≤d} なら、d 対で覆える S の上で格子が一致。t ≤ 2d なら全 arity | [証明済み] | 成立 | §2.3、S2（違反 0） |
| 補題 S（骨格）：段の塊の内側にない節点は 2ftD 個以下。内側の節点の詰め物は同じ段、規則差分は f 段以下 | [証明済み] | 成立 | §3.1 |
| **定理 B：k = t なら全ての型付き非終端の最短の生成組 ≤ 2fkD(1+r)θ（𝒦 も SUB も不要）** | **[証明済み]** | 成立 | §3.2 |
| 課題1(c)：Ex2 とその族で τ は小さい。理由は定理 B | [証明済み]＋[観察（計算）] | 多項式 | §4、S3 |
| 補題 M2：三つ以上の段にまたがる移動の二穴版（内側の段で個数が一致するとき） | [証明済み] | 成立 | §5.1 |
| 課題1(a)：二段以下の生成元だけで短縮が足りる | — | 示せず | §5.3 |
| 課題1(b)：三段以上の移動を二段以下の実現された差に分解 | [条件付き（補題 M2 の一致条件）] | 部分的 | §5.2、§5.3 |
| t ≥ 5 の 𝒦 ∩ C_{2,c_Σ} での τ の多項式上界 | [予想] | 未解決 | §5.3 |
| 課題2：超多項式の族 | — | 作れず | §6 |
| 反例の必要条件 N1〜N4 | [証明済み] | 成立 | §6.1 |
| 課題3：「凸な部分集合の上で一致」「指数が poly(θ)」の下での上界 | [証明済み]（ただし前者は実質的に定理 A′） | 成立 | §7 |
| 課題4：v の除去 | — | 未着手 | §8 |

- [証明済み] は本報告の中の証明を指す。書いたのも点検したのも同じモデルである。別のモデルで確認してほしい箇所を §2.4 と §3.3 に挙げた。
- 定理 A⁺ は前回の定理 A の証明の (6) 以外をそのまま使う。定理 A が正しいことが前提である。

---

## 1. 記法

前回の報告（§1）と同じものを使う。追加は次のとおり。

- 段は 1, 2, …, t と番号を付ける（Σ に文字のある段だけを数える）。文字 a の段を s(a) と書く。
- 文字の集合 S の**段の集合**を st(S) := {s(a) : a ∈ S} と書く。
- **隣接対**は {u, u+1} の形の段の集合。st(S) が**隣接対 d 個で覆える**とは、段の区間 P₁ < P₂ < ⋯ < P_{d′}（d′ ≤ d、各 P_i は {u_i} か {u_i, u_i+1}、互いに交わらない）で st(S) ⊆ ⋃P_i となること。必要な対の最小数を π(S) と書く。t ≤ 2d なら全ての S で π(S) ≤ d。d = 2 で覆えない最小の例は t = 5 の st(S) = {1,3,5}（S1）。
- 文 w の**段の塊**は、一つの段の文字だけからなる極大な因子。ND な語は段の順に高々 t 個の塊に分かれる。
- p_a（一文字の周期）：N_M ∩ ℤ^{a} = p_a ℤ（p_a ≥ 0）。面 M に依存するときは p_a(M) と書く。

---

## 2. 定理 A⁺：t ≤ 2f

### 2.1 補題 M*（隣接対による移動）

**補題 M\*** [証明済み]。L ∈ 𝒦、z ∈ ℤ^k ∖ {0}、S := supp z とし、π(S) = m とする。L が arity m で代入可能とする。q, α ∈ ℕ^k が
- q ∈ Q、q − z ∈ Q、q ≥ z⁺ + 2·𝟙_S、
- α ∈ Q、α ≥ z⁺ + 2·𝟙_S

を満たすなら α − z ∈ Q。

*証明。* st(S) を覆う区間 P₁ < ⋯ < P_m を、どの P_i も S の文字の段を含むように取る。ξ_i を「パリクが (z⁺ + 𝟙_S) の P_i の段の部分」の語を段の順に並べたもの、ξ′_i を (z⁻ + 𝟙_S) について同じものとする。どちらも空でなく、内容は S ∩ Γ_{P_i}。組 ξ, ξ′ は同じ型である。

γ := q − z⁺ − 𝟙_S とする。γ ≥ 0 で、S の上では γ ≥ 𝟙_S。語 w を次のように作る。各 P_i について、σ_i を P_i の中で S の文字を持つ最大の段とする。段の順に文字を並べ、
- P_i のどれにも入らない段では、γ のその段の文字を置く。
- P_i = {u, u+1} で σ_i = u+1 のとき：γ の段 u の文字、ξ_i、γ の段 u+1 の文字、の順に置く。
- それ以外（P_i が一つの段、または σ_i = u）のとき：ξ_i は段 σ_i の文字だけからなる。γ の段 σ_i より前の P_i の文字（あれば）、ξ_i、γ の段 σ_i の文字、γ の P_i の残りの段の文字（あれば）、の順に置く。

P_i が二つの段を含むとき、その間に段はない。従って w は ND で、w = v₀ξ₁v₁⋯ξ_m v_m と書ける。v_i（0 < i < m）は γ の段 σ_i の S の文字を含むので空でない。つまり文脈は許容的である。Ψ(w) = q なので w ∈ L。ξ を ξ′ に替えた語は、各 ξ′_i が ξ_i と同じ段の文字を同じ段の順に並べたものなので ND で、パリクは q − z ∈ Q。従って L に入る。arity m の代入可能性から D_L(ξ) = D_L(ξ′)。

γ′ := α − z⁺ − 𝟙_S で同じ並べ方をした文脈を F とする。F[ξ] は ND でパリク α、従って L に入る。よって F[ξ′] ∈ L で、そのパリクは α − z。∎

前回の補題 M は、全ての P_i が一つの段からなる場合である。違いは、一つの成分に隣接する二つの段の文字を入れてよい、という点だけである。隣接する二つの段の間には段がないので、成分の「内側の段」が生じない。

### 2.2 定理 A⁺

**定理 A⁺** [証明済み（定理 A の証明に依存）]。L ∈ 𝒦（段の数 t）とし、G を L の既約 good な表示（ファンアウト ≤ f、ランク ≤ r、非終端 v 個）とする。**t ≤ 2f** で L ∈ C_{f,c_Σ} なら

  τ(G, c_Σ) ≤ τ_k = O_{k,f,r}(θ^{k²+2k} + v·θ^{k²+k+1})

（τ_k は前回の §3.1 の漸化式で定まる同じ量）。**特に f = 2 では t ≤ 4 の全ての 𝒦 ∩ C_{2,c_Σ} の言語に当てはまる。**

*証明。* 前回の定理 A の証明の (1)〜(5) と (7) をそのまま使う。(6) の最後の行「S は高々 t ≤ f 個の段にまたがるので、補題 M から α − z ∈ Q」を次に替える：「t ≤ 2f なので π(S) ≤ ⌈t/2⌉ ≤ f。補題 M* と arity π(S) ≤ f の代入可能性から α − z ∈ Q」。補題 M* の仮定（q, q − z, α ∈ Q と深さ）は補題 M の仮定と同じで、(6) で確かめてあるものである。∎

系（特徴データ）も同じ形で成り立つ：t ≤ 2f なら特徴データは N_typ(1 + 2θ̄_G + r_max·τ_k) 以下。

### 2.3 系 M*（有限指数での形）

**系 M\*** [証明済み]。L ∈ 𝒦 が有限指数で、arity 1, …, d の全てで代入可能とする。このとき、全ての M, M′ ∈ 𝓜* と、π(S) ≤ d を満たす全ての ∅ ≠ S ⊆ M ∩ M′ について

  N_M ∩ ℤ^S = N_{M′} ∩ ℤ^S。

特に t ≤ 2d なら系1a の仮定が成り立ち、L は全ての arity で代入可能である。

*証明。* z ∈ N_{M′} ∩ ℤ^S、z ≠ 0 とする。supp z ⊆ S なので π(supp z) ≤ d。N_M, N_{M′} は有限指数なので、ある c ≥ 1 で c·e_a ∈ N_M（a ∈ M）、c·e_a ∈ N_{M′}（a ∈ M′）。Q_M, Q_{M′} の点に c·𝟙 の倍数を足して、α ∈ Q_M、q ∈ Q_{M′} を α, q ≥ z⁺ + 2·𝟙_{supp z} となるように取る。q − z ∈ Π_{M′} ∩ (q + N_{M′}) = Q_{M′}（飽和）。補題 M* から α − z ∈ Q。α − z の支持は M なので α − z ∈ Q_M、従って z ∈ Q_M − Q_M ⊆ N_M。逆の包含は対称。∎

**境界の例。**
- d = 1：Ex1（t = 3）は SUB₁ を満たし、N_{ac} ≠ N_{abc} ∩ ℤ^{ac}。st({a,c}) = {1,3} は一つの隣接対で覆えない。
- d = 2：Ex2（t = 5）は SUB₁・SUB₂ を満たし、N_{ace} ≠ N_{abcde} ∩ ℤ^{ace}。st({a,c,e}) = {1,3,5} は二つの隣接対で覆えない。

どちらも系 M* の仮定のちょうど外にある。t ≤ 4 には「SUB₂ だが SUB₃ でない」有限指数の例は存在しない。

スクリプト S2 は、乱数の有限指数の例 4000 個（k = 5、t = 2〜5、法 2 か 3）で、判定条件（系1b）が SUB₁（または SUB₁・SUB₂）を認めた全ての例について、覆える S の上で格子が一致することを確かめた（「覆えるのに一致しない」は 0 件）。

### 2.4 確認してほしい箇所

1. 補題 M* の語 w が ND であること（P_i が二段のとき、その間に段がないこと）と、内側の v_i が空でないこと。
2. 定理 A⁺ が定理 A から変えたのは (6) の最後の一行だけであること。特に、補題 O′ の移動 z の支持 S は I₀ ⊆ J に入り、q と α の深さの条件は S の全ての文字で成り立っていること。
3. 系 M* の「深い点が取れる」は有限指数を使う。無限指数では T_n のように成り立たない。

---

## 3. 定理 B：各段が一文字の場合

### 3.1 補題 S（骨格）

L ⊆ ND、G を L の既約 good な文法とする（𝒦 も代入可能性も仮定しない）。非終端 A の生成組 x の導出木と、A の導出文脈 E を固定する。E[x] ∈ L は ND である。x の各成分は高々 t 個の段の塊に分かれる。節点 ω が**内側**であるとは、y_ω の全ての成分が、x のある成分のある塊の中にあり、その塊の最初の文字も最後の文字も含まないこととする。

**補題 S** [証明済み]。
- (S1) 内側でない節点は、木の深さを D′ として 2f·t·D′ 個以下。
- (S2) ω が内側なら、B_ω の任意の生成組 u（特に短い生成組 u_{B_ω}）の各成分は、対応する y_ω の成分が入っている塊の段の文字だけからなる。
- (S3) ω が内側なら、規則差分 d_{R_ω} の支持は高々 f 個の段にまたがる（y_ω の成分が入っている塊の段）。

*証明。* (S1) 内側でない節点の生成組は、ある塊の最初か最後の位置を含む。そのような位置は 2ft 個以下（成分 f 個、塊 t 個、両端）。一つの位置を含む節点は、根からの一本の道の上にある。
(S2) 部分木を u の導出に取り替えると、A の生成組 x′ が得られ、E[x′] ∈ L は ND。y_ω の成分は塊の内側にあったので、取り替えた成分の両隣は同じ段 s の文字である。ND から、その成分の文字の段は全て s。
(S3) 内側の節点の子は内側で、規則が直接書く終端も同じ塊の中にある。(S2) を ω と子に使う。∎

### 3.2 定理 B

**定理 B** [証明済み]。各段が一文字（k = t、すなわち L ⊆ a₁*a₂*⋯a_k*）とし、G を L の既約 good な表示（ファンアウト ≤ f、ランク ≤ r、非終端 v 個）とする。このとき、全ての型付き非終端 X = A_T は

  ‖x‖₁ ≤ 2fk·D·(1 + r)·θ、D = v(2^k − 1)^f

を満たす生成組 x を持つ。従って τ(G, c_Σ) ≤ 2fkD(1+r)θ で、特徴データは ‖G‖ と θ の多項式である。**L ∈ 𝒦 も代入可能性も使わない。**

*証明。* A の型 T の生成組の導出のうち、(‖x‖₁, 節点の数) が辞書式に最小のものを取る。

- **深さ。** 根から葉への道の上に同じ型付き非終端が二度現れれば、上の部分木を下の部分木に取り替えると、型 T のままで（先祖の成分の内容は変わらない）、長さが増えず、節点が減る。最小性に反する。従って深さは D 以下。
- **内側の節点は短い。** ω が内側なら、(S2) から u_{B_ω} の各成分は塊の文字 a だけからなる（段が一文字なので）。部分木を u_{B_ω} の導出に取り替えた x′ は、取り替えた成分の両隣に a が残るので、x と同じ型 T を持つ。‖x′‖₁ = ‖x‖₁ − ‖y_ω‖₁ + ‖u_{B_ω}‖₁。最小性から ‖y_ω‖₁ ≤ ‖u_{B_ω}‖₁ ≤ θ。
- **数える。** 内側でない節点は (S1) から 2fkD 個以下（根はこれに入る）。x の各位置は、内側でない節点の規則が直接書く終端（節点ごとに θ 個以下）か、極大な内側の節点の生成組（内側でない節点の子、節点ごとに r 個以下、それぞれ長さ θ 以下）に入る。∎

**なぜ各段一文字が要るか。** 同じ段に二文字あると、内側の節点の詰め物が内容を変えられる。前回の G1(n)（a と c が同じ段）では、(A_n, {a}) の最短の生成語は a^{2^{n+1}} である。S4 が H(n)（各段一文字）と G1(n) を並べて確かめた：H(n) では最短の生成語は長さ 1、G1(n) では 2^{n+1}。

### 3.3 確認してほしい箇所

1. 取り替えた組 x′ が型 T を保つこと（成分が塊の内側にあるので、塊の文字が残る）。
2. 深さの議論で、取り替えが長さを増やさないこと（下の節点の生成組は上の節点の生成組の一部）。
3. good な文法で、節点の生成組の各成分が x の成分の因子になること（線形・nondeleting から従う）。

---

## 4. 課題1(c)：Ex2 とその族

**結論** [証明済み]：Ex2 は各段一文字（k = t = 5）なので、定理 B により、どの good な表示でも全ての型付き非終端が長さ 2fkD(1+r)θ 以下の生成組を持つ。τ は多項式である。これは Ex2 の骨格で各段一文字のまま法や段の数を変えた全ての族に当てはまる。**Ex2 の現象（面の格子が二穴で比べられない方向にずれる）は、各段一文字のままでは τ を大きくしない。**

理由は一般化できる形で言える。面 {a,c,e} の文を長くするには長い塊が要る。長い塊を作る節点の大部分は塊の内側にあり、内側の節点の詰め物は同じ文字に限られる（補題 S）。詰め物に取り替えた文は同じ内容で短くなるので、最短の文は短い。面 {a,b,c,d,e} に逃げられるのは、b と d の位置に同時に触れる節点だけで、それは骨格の上の O(D) 個しかない。

**族 Ex2⁰_m** [所属は証明済み、文法と τ は観察（計算）]。段 a < b < c < d < e、

  L_m = {a^i c^j e^l : i ≡ j ≡ l ≡ 0 (mod m)} ∪ {a^i b^p c^j d^q e^l : i ≡ j ≡ l (mod m)、p, q ≥ 1}（i, j, l ≥ 1）。

- 所属：N_{ace} = mℤ³、N_{abcde} ∩ ℤ^{ace} = mℤ³ + ℤ(1,1,1)。真部分集合 J ⊊ {a,c,e} の上ではどちらも mℤ^J。J = {a,c,e} で arity ≤ 2 の型は、ある成分が二つの段にまたがり、その内側の b か d を文脈に置けないので、二つの面を同時に受け入れない。J が b か d を含めば面は一つ。従って系1b の条件が d = 1, 2 で成り立つ（Ex2 と同じ議論。全ての m について手の証明。m = 2, 3 は判定条件でも確認）。SUB₃ は破れる（証明書 E = □b□d□、F = a^{m−1}□c^{m−1}□e^{m−1}、x = (a,c,e)、y = (aa,cc,ee)）。
- 文法：最小の決定性オートマトンから作った右線形文法（f = 1、r = 1）。L(G) = L は有界に照合した。
- τ：型付き非終端 (q, M) の同値類は「q から受理される内容 M の語」の全体（決定性と SUB₁ による）で、その最短の長さを幅優先で求めた。

| m | v | 規則 | 厚さ θ̄ | μ_{ace} | max τ | 定理 B の上界 |
|---|---|---|---|---|---|---|
| 2 | 15 | 27 | 10 | 6 | 6 | 93000 |
| 3 | 25 | 41 | 14 | 9 | 9 | 217000 |
| 4 | 37 | 57 | 18 | 12 | 12 | 412920 |
| 5 | 51 | 75 | 22 | 15 | 15 | 695640 |
| 6 | 67 | 95 | 26 | 18 | 18 | 1080040 |
| 8 | 105 | 141 | 34 | 24 | 24 | 2213400 |

τ = 3m、v は m の二次、θ̄ = 4m + 2。τ は厚さより小さい。この表は右線形の表示についてのものだが、定理 B は全ての good な表示（ファンアウト 2 を含む）についての上界である。

---

## 5. 課題1(a)(b)：移動を二つ以下の段に分解できるか

### 5.1 補題 M2（内側の段で個数が一致するときの二穴の移動）

**補題 M2** [証明済み]。L ∈ 𝒦 が arity 2 で代入可能とする。z ≠ 0、S := supp z、st(S) = {s₁ < ⋯ < s_r}（r ≥ 2）、1 ≤ j < r とし、段の開区間の合併 Int_j := (s₁, s_j) ∪ (s_{j+1}, s_r) を考える。q, α ∈ ℕ^k が
- q ∈ Q、q − z ∈ Q、α ∈ Q、q, α ≥ z⁺ + 2·𝟙_S、
- **段が Int_j に入る全ての文字 a で q_a = α_a**

を満たすなら α − z ∈ Q。

*証明。* ξ₁ を次の語とする：段 s₁ と s_j では (z⁺ + 𝟙_S) のその段の部分、段が (s₁, s_j) に入る文字については q の全部を、段の順に並べる。ξ₂ を [s_{j+1}, s_r] について同じに作る。ξ′ は、端の段では (z⁻ + 𝟙_S)、内側の段では q − z を使う。q ≥ z⁺ + 2·𝟙_S から内側の段でも支持は変わらず、ξ と ξ′ は同じ型である。γ := q − Ψ(ξ) は Int_j の段で 0、端の段の S の文字で 1 以上。γ の文字を、段 ≤ s₁ は ξ₁ の前、段 s_j から s_{j+1} までは ξ₁ と ξ₂ の間（j = 1 なら段 s₁ の文字もここに置く）、段 ≥ s_r は ξ₂ の後に並べると、許容的な文脈 E で E[ξ] は ND、パリク q。E[ξ′] は ND でパリク q − z。どちらも L に入るので D_L(ξ) = D_L(ξ′)。
α について γ′ := α − Ψ(ξ) を取ると、Int_j の段では仮定から 0、他は 0 以上で、端の段の S の文字で 1 以上。同じ並べ方の文脈 F で F[ξ] は ND でパリク α。従って F[ξ′] ∈ L、パリクは α − z。∎

補題 M* は Int_j に段が一つもない場合にあたる。

### 5.2 一歩の取り替えで戻せる場合と戻せない場合

二つの文 w, w′ ∈ L のパリク α, q が、段の集合 Δ の文字でしか違わないとする。補題 M2 は、ある j で Δ ∩ Int_j = ∅ なら使える。Δ が二つの段 {p, p′}（p ≤ p′）のとき、どの j でも使えないのは

> st(S) が s < p、p < s′ < p′、p′ < s″ を満たす段 s, s′, s″ を含む

ときに限る（**三方型**と呼ぶ）。[証明済み（組合せの確認）]：三方型でなければ、p と p′ は同じ閉区間 [s_j, s_{j+1}] に入るか、片方が st(S) の凸包の外にある。前者はその j、後者は残る一方を含む j を取ればよい。

三方型には五つの段が要る。これが定理 A⁺ の t ≤ 4 と対応している。Ex2 は三方型の最小の例である（S = {a,c,e}、p = s(b)、p′ = s(d)）。

### 5.3 どこで止まるか

**(a) 二段以下の生成元だけでは足りない理由** [観察]。補題 S(S3) から、内側の良い節点の規則差分 d_{R_ω} は f = 2 個以下の段にしかまたがらない。しかし補題 O′ が使う移動 z は、深い座標 I₀ に支持を持つ H′ の元で、生成元の和である。生成元は詰め物の文字（I₀ の外、多くは面 M の外）の座標を持ち、それが和の中で打ち消し合って初めて I₀ に入る。前回の G1(n) でも (4,0) = d_{R₁} + d_{R₂} で、c の座標が打ち消し合っている。従って「二段以下の生成元を一つずつ面 M に戻す」ことは、支持が M に入らないのでできない。和を取った z は三つ以上の段にまたがりうる。

**(b) 仮想の葉を一つずつ戻す連鎖** [条件付き（補題 M2 の一致条件）]。定理 A の (6) で、V = {κ₁,…,κ_m} の元を一つずつ u_κ から ỹ_κ に戻した文の列 w_m = s_V, w_{m−1}, …, w_0 = E_ν[ŷ] を考える。途中の文も L に入る（s_{κ₁…κ_i} の中の y_κ を、分布同値な ỹ_κ に替えたものだから）。隣り合う二つの文は κ_i の生成組の中でしか違わない。κ_i が内側の節点なら、違いは κ_i の成分が入っている二つ以下の段に限られる（補題 S(S2)）。従って、z の支持と κ_i の段が三方型でなければ、補題 M2 で z を一歩ずつ戻せる。
- 三方型になるのは、κ_i がファンアウト 2 で、その二つの成分の段 p < p′ が st(S) を三つに分けるときだけである。
- κ_i が内側でないとき（骨格の節点）は、違いが三つ以上の段に及びうる。これは別に扱う必要がある。

**(c) 残る場合。** 以上から、f = 2 で定理 A の方法が止まるのは次の全てが同時に起きるときに限られる。
1. t ≥ 5。
2. 仮想の葉 κ（補題 P の詰め物）がファンアウト 2 で、成分の段 p < p′ の両方で、詰め物 u_κ と代表 ỹ_κ の個数が違う（または κ が骨格の節点）。
3. 補題 O′ の移動 z の支持が、p より下、p と p′ の間、p′ より上の段を全て含む。

これは前回の §5 の3（「b の塊をまたぐファンアウト 2 の非終端」）を、証明の中の一点に絞ったものである。この場合に上界が成り立つかどうかは分からなかった。[予想]：成り立つ。根拠は §6.2 の失敗の形（三方型の z は、またぐ節点の生成元が二つの段に閉じているために、二段以下の純粋な部分に分かれる）だが、証明ではない。

---

## 6. 課題2：反例の族

**結論：作れなかった。** 以下は、反例が満たすべき必要条件と、試した設計が壊れた形である。

### 6.1 必要条件

𝒦 ∩ C_{f,c_Σ} の言語の族で、文法の大きさと厚さが poly(n)、τ が超多項式のものがあるとする（k, f, r は固定）。このとき次が全て成り立つ。

- **N1** [証明済み（定理 B）]：二文字以上の段がある（k > t）。
- **N2** [証明済み（定理 A⁺）]：t ≥ 2f + 1。f = 2 なら t ≥ 5。
- **N3** [証明済み（定理 A′）]：ある arity f < d ≤ t で代入可能でない（f = 2 なら 3 ≤ d ≤ t）。有限指数なら、系 M* と合わせて、ある面の対 M, M′ と、隣接対 f 個で覆えない S ⊆ M ∩ M′ で N_M ∩ ℤ^S ≠ N_{M′} ∩ ℤ^S。
- **N4** [証明済み]：τ_X が大きい型付き非終端 X = A_T と、その面 M ∈ Acc_T(n) について、ある a ∈ J_T で p_a(M) = 0 か p_a(M) が超多項式。
  *証明。* 定理1 の系から、X の同値類は総量が (n + N_M) ∩ (b_T + ℕ^{J_T}) に入る組の全体。全ての a ∈ J_T で p_a := p_a(M) > 0 なら、各 a で n_a から p_a の倍数を引いて b_a ≤ n′_a ≤ b_a + p_a − 1 にできる。従って τ_X ≤ Σ_{a∈J_T}(b_a + p_a − 1) ≤ k(f − 1 + max_a p_a)。∎

N4 の帰結として、**面の格子の指数が poly(θ) の族は反例にならない**（指数 ι なら p_a ≤ ι）。Ex2 の型の「法が小さい有限群」の設計は、段の構造をどう変えても反例にならない。反例には、ある文字の個数が「固い」（周期が 0 か巨大）ことが要る。

§2.5 の二つの障害との関係：
- 「純粋な詰め物」は補題 S(S2) として証明した。各段一文字ならこれだけで上界が出る（定理 B）。避けるには同じ段に別の文字が要る（N1）。
- 「窓の補題」は、同じ段の別の文字を詰め物にして正の重みの水準集合を作る設計を止める。これを避ける設計は見つからなかった。

### 6.2 試した設計と壊れた形 [観察]

**設計。** 段 1〜5、文字 a | c, ψ | e | g, χ | i（ψ は段 2、χ は段 4 の詰め物用の文字）。基本の面 M = {a,c,e,g,i}、広い面 U = M ∪ {ψ, χ}。段 2 と 4 の塊をまたぐファンアウト 2 の非終端（生成組は (c の語, g の語)、短い生成組は (ψ, χ)）を使い、z = (a,e,i の方向) が N_U に入り N_M に入らないようにする。三方型（§5.2）なので、SUB₂ は z を M に戻すことを強制しない、というのが狙いである。

**壊れた形。**
1. **ψ と χ がまたぐ節点からしか出ない場合。** ψ, χ の座標を持つ生成元は、またぐ節点の規則差分だけで、それは段 2 と 4 に閉じている（補題 S(S3)）。すると I₀ ⊆ M に入る z は「またぐ節点の寄与（段 2 と 4 だけ、ψ と χ の座標は 0）」と「その他の節点の寄与（ψ, χ を含まない）」の和になり、前者は二段の純粋なベクトルである。二段のベクトルは補題 M* で常に戻せる。z を三方型にしたまま戻せなくすることができない。
2. **ψ か χ が、またがない節点（たとえば (a, c) 型の節点）からも出る場合。** その節点だけを詰め物に替えた文が L に入るので、中間の面 M ∪ {ψ} が存在する。M と M ∪ {ψ} の文は段 1, 2 でしか違わず、三方型でないので z は戻せる（補題 M2）。中間の面を一つずつ経由して U から M まで戻せてしまう。Ex2 では中間の面（b だけ、d だけを持つ内容）が存在しないことが効いていたが、導出木から来る面は中間のものを必ず伴う。
3. **固い個数（N4）との両立。** 周期 0 の文字 a の長い塊は、a の塊の内側の節点で作るしかなく、その詰め物は a と同じ段の文字である（補題 S）。純粋な詰め物なら周期が小さくなる。別の文字なら窓の補題が効く。相手の成分を別の段に持つファンアウト 2 の節点（(a の語, 別の段の語) 型）は二段の生成元しか作らず、二段の方向は常に戻せる。

1〜3 は反例がないことの証明ではない。特に、三つ以上の詰め物の文字が段 2 と 4 にあり、中間の面の間の比較が「内側の段の個数の不一致」（補題 M2 の一致条件の否定）で全て妨げられる設計は、排除できていない。

### 6.3 `op:fanout-two` との関係

反例は得ていないので、`op:fanout-two` の YES（下界の方向）についての新しい情報はない。本報告の結果は多項式データの方向だが、𝒦 の中の、t ≤ 2f または各段一文字の場合に限られる。`prop:sl-reduction` が求める一様な多項式データには、𝒦 の外の言語と、𝒦 の中の t ≥ 5 の場合が残る。

---

## 7. 課題3：十分条件

- **「面の格子の指数が θ の多項式」** [証明済み（N4）]：指数が ι 以下なら τ ≤ k(f − 1 + ι)。t によらない。SUB_f だけを使う。有限指数の言語では指数は有限の計算で求まる。ただし、これは言語の側の量についての仮定で、文法から指数の上界が出るわけではない。
- **「どの二つの面の格子も、段の凸な部分集合の上で一致する」** [証明済み。ただし実質的に定理 A′]：凸な部分集合として全ての段を取れば系1a の仮定そのものになり、全ての arity で代入可能、従って定理 A′ が使える。より弱い次の形で足りる。
  > **(H)**：全ての M, M′ ∈ 𝓜* と、隣接対 f 個で覆えない全ての S ⊆ M ∩ M′ について N_M ∩ ℤ^S = N_{M′} ∩ ℤ^S。
  
  **定理 C** [証明済み]。L ∈ 𝒦 ∩ C_{f,c_Σ} が (H) を満たせば、t によらず τ ≤ τ_k。
  *証明。* 定理 A の (6) で、π(S) ≤ f なら補題 M*。π(S) > f なら、S ⊆ M ∩ U（α と q は S の上で深い）なので (H) から z ∈ N_M。α − z ∈ Π_M（(6) の深さの条件）と飽和から α − z ∈ Q_M。∎
  有限指数では (H) は有限の計算で判定できる（S2 の `lattice_table` が、必要な対の数と一致・不一致の表を出す）。ただし有限指数では、SUB_f と (H) を合わせると系 M* により系1a の仮定と同値になるので、定理 C は定理 A′ の言い換えである。新しい内容があるのは無限指数の場合だけである。
- **「受け入れる内容の族が段について区間的」**：これだけでは足りるとも足りないとも言えなかった。Ex2 では受け入れる内容は {a,c,e} と {a,b,c,d,e} で、どちらも段の集合としては {1,3,5} と {1,…,5} である。障害は内容の形ではなく、中間の内容がないことにある。次の形なら (b) の連鎖が通る見込みがあるが、証明していない [予想]：「M ⊂ U が面で、U ∖ M の文字が二つ以上の段にあるなら、段ごとに文字を足した中間の内容も面で、隣り合う面が内側の段の個数の一致する深い点を持つ」。

---

## 8. 課題4：v の除去

取り組んでいない。定理 B の上界も v に一次で依存する（深さ D を通して）。

---

## 9. 計算の要約

スクリプトは標準ライブラリだけを使い、乱数の種は 20261111。出力の全文は付録 B。実行時間は約 80 秒。

| 節 | 内容 | 結果 |
|---|---|---|
| S1 | t = 1〜7、d = 1, 2, 3 で、隣接対 d 個で覆えない段の集合を列挙 | t ≤ 2d で 0 個。d = 2 の最初の例は {1,3,5} |
| S2 | Ex1、Ex2、Ex2⁰_2、Ex2⁰_3：判定条件と、面の対・S ごとの格子の一致 | 一致しないのは覆えない S だけ |
| S2 | Ex2⁰_2：語の段階（長さ ≤ 11）で arity 1, 2 の違反なし。arity 3 の証明書を真の述語で確認 | 一致 |
| S2 | 乱数の例 4000 個：SUB_{≤d}（判定条件）なら、覆える S の上で格子が一致 | 違反 0 |
| S2 | 判定条件で SUB₁・SUB₂ が成り立つ乱数の例のうち最初の 25 個を、語の段階（長さ ≤ 6、arity 1, 2）で検査 | 違反 0 |
| S3 | Ex2⁰_m（m = 2〜8）：最小 DFA、右線形文法、厚さ、τ、定理 B の上界。L(G) = L を有界に照合 | τ = 3m、不一致 0 |
| S4 | H(n) と G1(n)（n = 1〜8）：(A_n, {a}) の最短の生成語 | H(n) は 1、G1(n) は 2^{n+1} |

S2 の乱数の例では、t = 5・d = 2 で「覆えない S」は 12 件あり、全て一致していた。SUB₂ を満たしつつ覆えない S で格子がずれる例は、乱数では出ず、Ex2 の型の作った例だけである。

---

## 10. 主張していないこと

- t ≥ 5 の 𝒦 ∩ C_{2,c_Σ} は未解決である。定理 A⁺ は t ≤ 4、定理 B は各段一文字の場合だけを覆う。
- 定理 B は生成組の長さの上界で、L ⊆ ND かつ各段一文字という強い仮定の下のものである。一般の有界言語や、同じ段に二文字ある場合には当てはまらない（G1(n) が反例）。
- μ の結果を τ の結果として書いていない。§4 の表の μ_{ace} は τ の一つの値として載せた。
- 𝒦 の結果を、一般の正則言語や `op:fanout-two` の解決として書いていない。
- 上界は各 k について示した。定数は k に指数的に依存する。
- §5.3(c) と §6.2 は観察で、反例がないことの証明ではない。
- 定理 A⁺ は前回の定理 A に依存する。定理 A の独立な確認が済んでいることを前提にしている。

---

## 11. 次の一手（見込み順）

1. **定理 A⁺ と定理 B の独立な確認と、原稿への入れ方。** 確認する箇所は §2.4 と §3.3。f = 2 の場合、𝒦 で残るのは「t ≥ 5 かつ二文字以上の段がある」場合だけになる。
2. **t = 5 の三方型を直接調べる。** §5.3(c) の三条件が同時に起きる最小の状況（段 1〜5、段 2 と 4 に詰め物の文字、またぐファンアウト 2 の非終端）で、(i) §6.2 の1 の議論（またぐ節点の生成元は二つの段に閉じる）を、骨格の節点と複数の詰め物の文字を含めて証明にする、または (ii) 中間の面の比較が全て「内側の段の個数の不一致」で妨げられる言語を、無限指数（T_n の型）で探す。(ii) は定理1 の (★) を小さな箱の中で全数検査する形で機械的に探索できる。
3. **固い個数の排除。** N4 から、反例には周期が 0 か巨大な文字が要る。「厚さ θ の good な文法が、ある面で文字 a の個数を poly(θ) を超えて大きくできるなら p_a ≤ poly(θ)」を、二段以下の移動だけ（補題 M*）で示せれば、t によらない上界が N4 から直接出る。倍増型の木については、窓の補題を任意の可換群の商に延ばす形（短い関係の格子の階数で場合分けする）で示せる見込みがある。

---

## 付録 A：スクリプト `fable_three_stages_2026-11-11.py`（全文）

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fable_three_stages_2026-11-11.py
報告 fable_three_stages_2026-11-11.md の検査スクリプト（Python 3、標準ライブラリのみ）。

規約
- 乱数の種は固定（20261111）。
- 無限の言語についての主張は報告書の中で手で証明する。有界な検査は反例探しと照合のためだけに使う。
- 「違反」として出力する語の四つ組は、必ず真の所属述語 member() で判定し直す。
- StageLang、criterion などの部品は前回のスクリプト（2026-11-10）と同じもの。

節
 S1  隣接する段の対による被覆（補題 M* の組合せ部分）
 S2  系 M*（有限指数）：SUB_d なら、d 個の隣接対で覆える S の上で面の格子が一致する
 S3  Ex2 の族 Ex2^0_m：所属、文法、厚さ、tau、定理 B の上界
 S4  定理 B の対比：段が一文字の H(n) と、同じ段に二文字ある G1(n)
"""
import itertools
import math
import random
import time

random.seed(20261111)


# ----------------------------------------------------------------------------
# 0. 言語の記述と定理1 の判定条件（前回と同じ）
# ----------------------------------------------------------------------------
class StageLang:
    """クラス K の言語。cond(M) は内容 M の条件のリスト [(重み, 法, 剰余)]。
    法 0 は等式を表す。cond(M) が None なら M は受理されない内容。"""

    def __init__(self, name, letters, stage, cond):
        self.name = name
        self.letters = letters
        self.k = len(letters)
        self.stage = stage
        self.idx = {a: i for i, a in enumerate(letters)}
        self.faces = {}
        for r in range(1, self.k + 1):
            for M in itertools.combinations(letters, r):
                c = cond(frozenset(M))
                if c is not None:
                    self.faces[frozenset(M)] = c

    def accept(self, m):
        M = frozenset(a for a, x in zip(self.letters, m) if x > 0)
        c = self.faces.get(M)
        if c is None:
            return False
        for w, mod, res in c:
            v = sum(w.get(a, 0) * x for a, x in zip(self.letters, m))
            if mod == 0:
                if v != res:
                    return False
            elif (v - res) % mod:
                return False
        return True

    def in_lattice(self, M, h):
        for w, mod, _res in self.faces[M]:
            v = sum(w.get(a, 0) * x for a, x in zip(self.letters, h))
            if mod == 0:
                if v != 0:
                    return False
            elif v % mod:
                return False
        return True

    def nd(self, w):
        s = [self.stage[c] for c in w]
        return all(s[i] <= s[i + 1] for i in range(len(s) - 1))

    def parikh(self, w):
        return tuple(w.count(a) for a in self.letters)

    def member(self, w):
        return len(w) > 0 and self.nd(w) and self.accept(self.parikh(w))


def nd_words(lang, L):
    res, frontier = [], ['']
    for _ in range(L):
        new = []
        for w in frontier:
            last = lang.stage[w[-1]] if w else -1
            for a in lang.letters:
                if lang.stage[a] >= last:
                    new.append(w + a)
        res += new
        frontier = new
    return res


def factorizations(w, d):
    """w = v0 x1 v1 ... xd vd。x_i は空でなく、内側の v_i も空でない。"""
    n = len(w)

    def rec(i, start, xs, vs):
        if i == d:
            yield tuple(xs), tuple(vs + [w[start:]])
            return
        lo = start if i == 0 else start + 1
        for p in range(lo, n):
            for q in range(p + 1, n + 1):
                yield from rec(i + 1, q, xs + [w[p:q]], vs + [w[start:p]])

    yield from rec(0, 0, [], [])


def fill(ctx, x):
    s = ctx[0]
    for xi, v in zip(x, ctx[1:]):
        s += xi + v
    return s


def typ(x):
    return tuple(frozenset(c) for c in x)


def brute_sub(lang, d, L):
    """長さ L 以下の文から SUB_d の違反 (E, F, x, y) を探す。
    E[x], E[y], F[x] は L に入り、F[y] は入らない（全て member で判定）。"""
    words = [w for w in nd_words(lang, L) if lang.member(w)]
    D, byctx = {}, {}
    for w in words:
        for x, E in factorizations(w, d):
            D.setdefault(x, set()).add(E)
            byctx.setdefault((E, typ(x)), []).append(x)
    for (E, _T), xs in byctx.items():
        x0 = xs[0]
        for y in xs[1:]:
            for F in D[x0]:
                if not lang.member(fill(F, y)):
                    return (E, F, x0, y)
            for F in D[y]:
                if not lang.member(fill(F, x0)):
                    return (E, F, y, x0)
    return None


def check_certificate(lang, cert):
    E, F, x, y = cert
    return (lang.member(fill(E, x)) and lang.member(fill(E, y))
            and lang.member(fill(F, x)) and not lang.member(fill(F, y)))


# ----------------------------------------------------------------------------
# 1. 定理1 の判定条件（全ての法が正の場合の厳密な形）
# ----------------------------------------------------------------------------
def type_info(lang, T):
    los = [min(lang.stage[a] for a in M) for M in T]
    his = [max(lang.stage[a] for a in M) for M in T]
    d = len(T)
    for i in range(d - 1):
        if his[i] > los[i + 1]:
            return None
    J = frozenset().union(*T)
    b = tuple(sum(1 for M in T if a in M) for a in lang.letters)
    pos = {}
    for a in lang.letters:
        s = lang.stage[a]
        P = []
        if s <= los[0]:
            P.append(0)
        for i in range(1, d):
            if his[i - 1] <= s <= los[i]:
                P.append(i)
        if s >= his[d - 1]:
            P.append(d)
        pos[a] = P
    return J, b, pos


def place_inner(lang, e, pos, d):
    """内側の区切り 1..d-1 に文字を一つずつ置けるか。置ければ残りと配置を返す。"""
    rem = list(e)
    slots = [[] for _ in range(d + 1)]

    def rec(i):
        if i == d:
            return True
        for j, a in enumerate(lang.letters):
            if rem[j] > 0 and i in pos[a]:
                rem[j] -= 1
                slots[i].append(a)
                if rec(i + 1):
                    return True
                slots[i].pop()
                rem[j] += 1
        return False

    if not rec(1):
        return None
    return rem, slots


def build_ctx(lang, e, pos, d):
    rem, slots = place_inner(lang, e, pos, d)
    for j, a in enumerate(lang.letters):
        if rem[j] > 0:
            slots[pos[a][0]] += [a] * rem[j]
    key = lambda a: (lang.stage[a], a)
    return tuple(''.join(sorted(s, key=key)) for s in slots)


def build_tuple(lang, T, n):
    rem = list(n)
    comps = [[] for _ in T]
    for i, M in enumerate(T):
        for a in M:
            comps[i].append(a)
            rem[lang.idx[a]] -= 1
    for j, a in enumerate(lang.letters):
        if rem[j] > 0:
            i = next(i for i, M in enumerate(T) if a in M)
            comps[i] += [a] * rem[j]
    assert min(rem) >= 0
    key = lambda a: (lang.stage[a], a)
    return tuple(''.join(sorted(c, key=key)) for c in comps)


def criterion(lang, d, Lcm):
    """定理1（有限指数の形）：全ての型 T（arity d）、n、M, M' in Acc_T(n) について
    N_M ∩ Z^J = N_M' ∩ Z^J。破れていれば証人を返す。"""
    letters, k = lang.letters, lang.k
    contents = [frozenset(c) for r in range(1, k + 1)
                for c in itertools.combinations(letters, r)]
    top = Lcm if d <= 2 else 2 * Lcm
    for T in itertools.product(contents, repeat=d):
        info = type_info(lang, T)
        if info is None:
            continue
        J, b, pos = info
        faces = [M for M in lang.faces if J <= M]
        if len(faces) < 2:
            continue
        Jidx = [i for i, a in enumerate(letters) if a in J]
        ranges = [range(0, top + 1) if pos[a] else range(0, 1) for a in letters]
        es = []
        for e in itertools.product(*ranges):
            if d > 1 and place_inner(lang, e, pos, d) is None:
                continue
            M = J | frozenset(a for a, x in zip(letters, e) if x > 0)
            if M in lang.faces:
                es.append((e, M))
        if not es:
            continue
        latt = {}
        for M in faces:
            S = set()
            for hJ in itertools.product(range(Lcm), repeat=len(Jidx)):
                h = [0] * k
                for i, v in zip(Jidx, hJ):
                    h[i] = v
                if lang.in_lattice(M, h):
                    S.add(tuple(h))
            latt[M] = S
        for nJ in itertools.product(range(Lcm), repeat=len(Jidx)):
            n = list(b)
            for i, v in zip(Jidx, nJ):
                n[i] += v
            acc = {}
            for e, M in es:
                if M not in acc and lang.accept(tuple(x + y for x, y in zip(e, n))):
                    acc[M] = e
            Ms = list(acc)
            for M1 in Ms:
                for M2 in Ms:
                    diff = latt[M1] - latt[M2]
                    if diff:
                        return dict(T=T, n=tuple(n), M1=M1, M2=M2, h=min(diff),
                                    e1=acc[M1], e2=acc[M2], pos=pos)
    return None


def witness_to_certificate(lang, wit):
    T, n, h, pos = wit['T'], wit['n'], wit['h'], wit['pos']
    d = len(T)
    x = build_tuple(lang, T, n)
    y = build_tuple(lang, T, tuple(a + c for a, c in zip(n, h)))
    E = build_ctx(lang, wit['e1'], pos, d)
    F = build_ctx(lang, wit['e2'], pos, d)
    return (E, F, x, y)


def show(M):
    return ''.join(sorted(M))


# ----------------------------------------------------------------------------
# S1. 隣接する段の対による被覆
# ----------------------------------------------------------------------------
def pairs_needed(stages):
    """段の集合を {u,u+1} の形の対で覆うのに必要な対の最小数（貪欲で最適）。"""
    st = sorted(set(stages))
    cnt, i = 0, 0
    while i < len(st):
        if i + 1 < len(st) and st[i + 1] == st[i] + 1:
            i += 2
        else:
            i += 1
        cnt += 1
    return cnt


def section1():
    print('=' * 78)
    print('S1  隣接する段の対による被覆（補題 M*）')
    print('=' * 78)
    for t in range(1, 8):
        row = []
        for d in (1, 2, 3):
            bad = [S for r in range(1, t + 1)
                   for S in itertools.combinations(range(1, t + 1), r)
                   if pairs_needed(S) > d]
            minimal = [S for S in bad
                       if not any(set(B) < set(S) for B in bad)]
            row.append((d, len(bad), minimal[:4]))
        print('  t=%d:' % t, ' / '.join(
            'd=%d 覆えない集合 %d 個%s' % (d, n, ('（極小: %s）' % mn) if n else '')
            for d, n, mn in row))
    print('  （t ≤ 2d なら覆えない集合は 0 個。d=2 では t=5 の {1,3,5} が最初の例）')


# ----------------------------------------------------------------------------
# S2. 系 M*：SUB_d なら d 対で覆える S の上で格子が一致
# ----------------------------------------------------------------------------
def rank_stage(stage):
    vals = sorted(set(stage.values()))
    return {a: vals.index(s) + 1 for a, s in stage.items()}


def agree(lang, M1, M2, S, Lcm):
    idx = [lang.idx[a] for a in S]
    for hs in itertools.product(range(Lcm), repeat=len(idx)):
        h = [0] * lang.k
        for i, v in zip(idx, hs):
            h[i] = v
        if lang.in_lattice(M1, h) != lang.in_lattice(M2, h):
            return False
    return True


def lattice_table(lang, Lcm, dmax=2):
    """SUB_1..SUB_dmax の判定と、面の対・部分集合 S ごとの一致の表。"""
    rk = rank_stage(lang.stage)
    ok = {}
    prev = True
    for d in range(1, dmax + 1):
        prev = prev and criterion(lang, d, Lcm) is None
        ok[d] = prev
    rows = []
    for M1, M2 in itertools.combinations(list(lang.faces), 2):
        I = sorted(M1 & M2)
        for r in range(1, len(I) + 1):
            for S in itertools.combinations(I, r):
                rows.append((M1, M2, S, pairs_needed([rk[a] for a in S]),
                             agree(lang, M1, M2, S, Lcm)))
    return ok, rows


def ex2_family(m, res):
    """段 a<b<c<d<e。面 ace: i≡j≡l≡res (m)。面 abcde: i≡j≡l (m)。"""
    def cond(M):
        if M == frozenset('ace'):
            return [({'a': 1}, m, res), ({'c': 1}, m, res), ({'e': 1}, m, res)]
        if M == frozenset('abcde'):
            return [({'a': 1, 'c': -1}, m, 0), ({'c': 1, 'e': -1}, m, 0)]
        return None
    return StageLang('Ex2^%d_%d' % (res, m), 'abcde',
                     {c: i + 1 for i, c in enumerate('abcde')}, cond)


def section2():
    print('=' * 78)
    print('S2  系 M*（有限指数）の検査')
    print('=' * 78)

    def cond1(M):
        if M == frozenset('ac'):
            return [({'a': 1, 'c': 1}, 2, 0)]
        if M == frozenset('abc'):
            return [({'a': 1}, 2, 1), ({'c': 1}, 2, 1)]
        return None
    ex1 = StageLang('Ex1', 'abc', {'a': 1, 'b': 2, 'c': 3}, cond1)
    named = [(ex1, 2), (ex2_family(2, 1), 2), (ex2_family(2, 0), 2), (ex2_family(3, 0), 3)]
    for lang, Lcm in named:
        ok, rows = lattice_table(lang, Lcm)
        dis = [(show(M1), show(M2), ''.join(S), p) for M1, M2, S, p, ag in rows if not ag]
        print('  %-8s SUB_1=%s SUB_1&2=%s  格子が一致しない (面,面,S,必要な対の数): %s'
              % (lang.name, ok[1], ok[2], dis))
        for d in (1, 2):
            if ok[d]:
                assert all(ag for _, _, _, p, ag in rows if p <= d)
    # 語の段階の照合（Ex2^0_2）
    e20 = ex2_family(2, 0)
    print('  Ex2^0_2 語の段階（長さ≤11）: arity1 違反 %s / arity2 違反 %s'
          % (brute_sub(e20, 1, 11), brute_sub(e20, 2, 11)))
    cert = (('', 'b', 'd', ''), ('a', 'c', 'e', ''), ('a', 'c', 'e'), ('aa', 'cc', 'ee'))
    print('  Ex2^0_2 arity3 の証明書 E=□b□d□, F=a□c□e□, x=(a,c,e), y=(aa,cc,ee):',
          check_certificate(e20, cert))

    # ランダムな例
    letters = 'abcde'
    contents = [frozenset(c) for r in range(2, 6) for c in itertools.combinations(letters, r)]
    stats = {}
    brute = {'checked': 0, 'viol': 0}
    N = 0
    t0 = time.time()
    while N < 4000:
        t = random.choice((2, 3, 4, 5))
        cuts = sorted(random.sample(range(1, 5), t - 1))
        stage, s = {}, 1
        for i, a in enumerate(letters):
            if i in cuts:
                s += 1
            stage[a] = s
        mod = random.choice((2, 2, 3))
        table = {}
        base = random.choice(contents)
        fs = [base]
        for _ in range(random.randint(1, 2)):
            if random.random() < 0.5:
                extra = [a for a in letters if a not in base]
                if extra:
                    fs.append(base | frozenset(random.sample(extra, random.randint(1, len(extra)))))
                    continue
            fs.append(random.choice(contents))
        for M in fs:
            cs = []
            for _ in range(random.randint(0, 3)):
                w = {a: random.randint(0, mod - 1) for a in sorted(M)}
                cs.append((w, mod, random.randint(0, mod - 1)))
            table[M] = cs
        lang = StageLang('rnd', letters, stage, lambda M: table.get(M))
        for M in list(lang.faces):
            if not any(lang.accept(m) for m in itertools.product(range(mod + 2), repeat=5)
                       if frozenset(a for a, x in zip(letters, m) if x > 0) == M):
                del lang.faces[M]
        if len(lang.faces) < 2:
            continue
        N += 1
        ok, rows = lattice_table(lang, mod)
        for d in (1, 2):
            if not ok[d]:
                continue
            for _, _, S, p, ag in rows:
                key = (t, d, 'covered' if p <= d else 'not covered', 'agree' if ag else 'DISAGREE')
                stats[key] = stats.get(key, 0) + 1
        if ok[2] and rows and brute['checked'] < 25:
            brute['checked'] += 1
            if brute_sub(lang, 1, 6) is not None or brute_sub(lang, 2, 6) is not None:
                brute['viol'] += 1
    print('  ランダムな例 %d 個（k=5、t=2..5、法 2 か 3）。(t, d, 被覆, 一致) ごとの (面の対, S) の数:' % N)
    for key in sorted(stats):
        print('   ', key, stats[key])
    bad = sum(v for k, v in stats.items() if k[2] == 'covered' and k[3] == 'DISAGREE')
    print('  「覆えるのに一致しない」の数 = %d（系 M* が正しければ 0）' % bad)
    print('  判定条件で SUB_1・SUB_2 が成り立つ例のうち最初の %d 個を語の段階（長さ≤6、arity 1,2）で検査: 違反 %d'
          % (brute['checked'], brute['viol']))
    print('  （%.1f 秒）' % (time.time() - t0))


# ----------------------------------------------------------------------------
# S3. Ex2 の族：文法、厚さ、tau
# ----------------------------------------------------------------------------
def build_dfa(m):
    """Ex2^0_m の決定性オートマトン（到達可能かつ受理に届く状態だけ、最小化済み）。"""
    letters = 'abcde'
    st = {c: i for i, c in enumerate(letters)}
    start = ('s', 0, 0, 0, 0, 0)

    def step(q, x):
        ph, i, j, l, hb, hd = q
        if ph != 's' and st[x] < st[ph]:
            return None
        if x == 'a':
            return ('a', (i + 1) % m, j, l, hb, hd)
        if x == 'b':
            return ('b', i, j, l, 1, hd)
        if x == 'c':
            return ('c', i, (j + 1) % m, l, hb, hd)
        if x == 'd':
            return ('d', i, j, l, hb, 1)
        return ('e', i, j, (l + 1) % m, hb, hd)

    def acc(q):
        ph, i, j, l, hb, hd = q
        if ph != 'e':
            return False
        if hb and hd:
            return i == j == l
        if not hb and not hd:
            return i == j == l == 0
        return False

    # 文字 a, c, e を全て含むことは ph の進み方では保証されないので、個数 0 を区別する
    def step2(q, x):
        base, seen = q
        nb = step(base, x)
        if nb is None:
            return None
        return (nb, seen | {x})

    def acc2(q):
        base, seen = q
        return acc(base) and {'a', 'c', 'e'} <= seen and \
            (seen == {'a', 'c', 'e'} or seen == set(letters))

    start2 = (start, frozenset())
    reach, frontier = {start2}, [start2]
    trans = {}
    while frontier:
        q = frontier.pop()
        for x in letters:
            n = step2(q, x)
            if n is None:
                continue
            n = (n[0], frozenset(n[1]))
            trans[(q, x)] = n
            if n not in reach:
                reach.add(n)
                frontier.append(n)
    # 受理に届く状態
    good = {q for q in reach if acc2(q)}
    changed = True
    while changed:
        changed = False
        for (q, x), n in trans.items():
            if n in good and q not in good:
                good.add(q)
                changed = True
    states = sorted(good, key=repr)
    # Moore の最小化
    part = {q: (1 if acc2(q) else 0) for q in states}
    while True:
        sig = {q: (part[q], tuple(part.get(trans.get((q, x))) if trans.get((q, x)) in good else None
                                  for x in letters)) for q in states}
        ids = {}
        new = {q: ids.setdefault(sig[q], len(ids)) for q in states}
        if len(ids) == len(set(part.values())):
            part = new
            break
        part = new
    nst = len(set(part.values()))
    delta, final = {}, set()
    for q in states:
        if acc2(q):
            final.add(part[q])
        for x in letters:
            n = trans.get((q, x))
            if n in good:
                delta[(part[q], x)] = part[n]
    return part[start2], nst, delta, final


def dfa_accepts(dfa, w):
    q0, _n, delta, final = dfa
    q = q0
    for c in w:
        q = delta.get((q, c))
        if q is None:
            return False
    return q in final


def section3():
    print('=' * 78)
    print('S3  Ex2 の族 Ex2^0_m：L = {a^i c^j e^l : i≡j≡l≡0 (m)} ∪ {a^i b^+ c^j d^+ e^l : i≡j≡l (m)}')
    print('=' * 78)
    letters = 'abcde'
    k, f, r = 5, 1, 1
    print('  右線形文法（最小 DFA から。非終端 = 状態、規則 q -> x q\' と q -> x）。f=1, r=1。')
    print('  %3s %5s %6s %7s %9s %10s %12s %14s' %
          ('m', 'v', '規則', 'thick', 'mu_ace', 'max tau', '定理Bの上界', 'SUB_1&2(判定)'))
    for m in (2, 3, 4, 5, 6, 8):
        lang = ex2_family(m, 0)
        dfa = build_dfa(m)
        q0, nst, delta, final = dfa
        # L(G) = L の有界な照合（長さ ≤ Lb。先頭 4 文字は任意、その後は段非減少に伸ばした語）
        Lb = 9 if m <= 3 else 8
        mism = 0
        frontier = ['']
        for _ in range(Lb):
            frontier = [w + c for w in frontier for c in letters
                        if (not w) or lang.stage[c] >= lang.stage[w[-1]] or len(w) < 4]
            for w in frontier:
                if dfa_accepts(dfa, w) != lang.member(w):
                    mism += 1
        # 長い語の照合（ND な語を乱数で）
        for _ in range(3000):
            cnt = [random.randint(0, 3 * m) for _ in letters]
            w = ''.join(c * n for c, n in zip(letters, cnt))
            if w and dfa_accepts(dfa, w) != lang.member(w):
                mism += 1
        # 距離
        INF = 10 ** 9
        dist = {q0: 0}
        frontier = [q0]
        while frontier:
            nf = []
            for q in frontier:
                for x in letters:
                    n = delta.get((q, x))
                    if n is not None and n not in dist:
                        dist[n] = dist[q] + 1
                        nf.append(n)
            frontier = nf
        togo = {q: 0 for q in final}
        changed = True
        while changed:
            changed = False
            for (q, x), n in delta.items():
                if n in togo and togo[n] + 1 < togo.get(q, INF):
                    togo[q] = togo[n] + 1
                    changed = True
        nrules, thick = 0, 0
        for (q, x), n in delta.items():
            nrules += 1                      # q -> x n
            thick = max(thick, dist[q] + 1 + togo[n])
            if n in final:
                nrules += 1                  # q -> x
                thick = max(thick, dist[q] + 1)
        # tau: 型付き非終端 (q, M) ごとに、q から受理される内容ちょうど M の最短の語
        # （決定性なので、文脈 u□（u は q に届く語）を共有する語の全体が q の言語。
        #   SUB_1 の下で、これが同値類になる）
        best = {}
        start_items = [(q, frozenset()) for q in range(nst)]
        seen = set(start_items)
        layer = [(q, q, frozenset()) for q in range(nst)]
        length = 0
        while layer:
            length += 1
            nl = []
            for src, q, M in layer:
                for x in letters:
                    n = delta.get((q, x))
                    if n is None:
                        continue
                    M2 = M | {x}
                    if (src, n, M2) in seen:
                        continue
                    seen.add((src, n, M2))
                    if n in final and (src, M2) not in best:
                        best[(src, M2)] = length
                    nl.append((src, n, M2))
            layer = nl
        tau = max(best.values())
        mu_ace = best[(q0, frozenset('ace'))]
        theta = max(1, thick)
        D = nst * (2 ** k - 1) ** f
        boundB = 2 * f * k * D * (1 + r) * theta
        if m <= 3:
            s12 = criterion(lang, 1, m) is None and criterion(lang, 2, m) is None
        else:
            s12 = '(手の証明)'
        assert mism == 0
        assert tau <= boundB
        print('  %3d %5d %6d %7d %9d %10d %12d %14s' %
              (m, nst, nrules, thick, mu_ace, tau, boundB, s12))
    print('  L(G) = L の照合：長さ ≤ 8〜9 の語（先頭 4 文字は任意、その後は ND）と、乱数の長い ND な語 3000 個で不一致 0。')
    print('  tau は m について一次、文法の大きさは m の二次。超多項式ではない。')


# ----------------------------------------------------------------------------
# S4. 定理 B の対比
# ----------------------------------------------------------------------------
def shortest_typed(rules, letters):
    """CFG（ファンアウト 1）。rules: {A: [右辺のリスト]}、右辺は記号の列。
    best[(A, M)] = A から導出される、内容がちょうど M の最短の語の長さ。"""
    best = {}
    changed = True
    while changed:
        changed = False
        for A, rhss in rules.items():
            for rhs in rhss:
                opts = [{(frozenset(), 0)}]
                cur = {frozenset(): 0}
                for X in rhs:
                    nxt = {}
                    if X in rules:
                        items = [(M, l) for (B, M), l in best.items() if B == X]
                    else:
                        items = [(frozenset(X), 1)]
                    for M0, l0 in cur.items():
                        for M1, l1 in items:
                            M2 = M0 | M1
                            if l0 + l1 < nxt.get(M2, 10 ** 18):
                                nxt[M2] = l0 + l1
                    cur = nxt
                for M, l in cur.items():
                    if l < best.get((A, M), 10 ** 18):
                        best[(A, M)] = l
                        changed = True
    return best


def cfg_thickness(rules, start):
    inside = {}
    changed = True
    while changed:
        changed = False
        for A, rhss in rules.items():
            for rhs in rhss:
                if all((X not in rules) or X in inside for X in rhs):
                    l = sum(inside[X] if X in rules else 1 for X in rhs)
                    if l < inside.get(A, 10 ** 18):
                        inside[A] = l
                        changed = True
    outside = {start: 0}
    changed = True
    while changed:
        changed = False
        for A, rhss in rules.items():
            if A not in outside:
                continue
            for rhs in rhss:
                tot = sum(inside[X] if X in rules else 1 for X in rhs)
                for X in rhs:
                    if X in rules:
                        o = outside[A] + tot - inside[X]
                        if o < outside.get(X, 10 ** 18):
                            outside[X] = o
                            changed = True
    th = 0
    for A, rhss in rules.items():
        for rhs in rhss:
            th = max(th, outside[A] + sum(inside[X] if X in rules else 1 for X in rhs))
    return th


def section4():
    print('=' * 78)
    print('S4  定理 B の対比：型付き非終端 (A_n, {a}) の最短の生成語')
    print('=' * 78)
    print('  H(n)  : S -> A_n c,  A_i -> A_{i-1} A_{i-1} | a,  A_0 -> aa   （段 a<c、各段一文字）')
    print('  G1(n) : S -> b A_n,  A_i -> A_{i-1} A_{i-1} | c,  A_0 -> aa   （段 b<{a,c}、a と c が同じ段）')
    print('  %3s | %5s %6s %14s %12s | %5s %6s %14s' %
          ('n', 'v', 'thick', '最短(A_n,{a})', '定理Bの上界', 'v', 'thick', '最短(A_n,{a})'))
    for n in range(1, 9):
        out = []
        for kind in ('H', 'G1'):
            rules = {'A0': [['a', 'a']]}
            for i in range(1, n + 1):
                rules['A%d' % i] = [['A%d' % (i - 1), 'A%d' % (i - 1)], ['a' if kind == 'H' else 'c']]
            rules['S'] = [['A%d' % n, 'c']] if kind == 'H' else [['b', 'A%d' % n]]
            best = shortest_typed(rules, 'abc')
            th = cfg_thickness(rules, 'S')
            out.append((len(rules), th, best[('A%d' % n, frozenset('a'))]))
        (v1, th1, s1), (v2, th2, s2) = out
        k, f, r = 2, 1, 2
        boundB = 2 * f * k * (v1 * (2 ** k - 1) ** f) * (1 + r) * max(1, th1)
        assert s1 <= boundB
        print('  %3d | %5d %6d %14d %12d | %5d %6d %14d' % (n, v1, th1, s1, boundB, v2, th2, s2))
    print('  H(n) では最短の生成語が定数、G1(n) では 2^(n+1)。定理 B は「各段一文字」を本当に使う。')
    print('  （G1(n) でも代表は aa で tau = 2。これは前回の報告の S3 の結果）')


if __name__ == '__main__':
    t0 = time.time()
    section1()
    section2()
    section3()
    section4()
    print('=' * 78)
    print('完了（%.1f 秒）' % (time.time() - t0))
```

## 付録 B：出力（全文）

```
==============================================================================
S1  隣接する段の対による被覆（補題 M*）
==============================================================================
  t=1: d=1 覆えない集合 0 個 / d=2 覆えない集合 0 個 / d=3 覆えない集合 0 個
  t=2: d=1 覆えない集合 0 個 / d=2 覆えない集合 0 個 / d=3 覆えない集合 0 個
  t=3: d=1 覆えない集合 2 個（極小: [(1, 3)]） / d=2 覆えない集合 0 個 / d=3 覆えない集合 0 個
  t=4: d=1 覆えない集合 8 個（極小: [(1, 3), (1, 4), (2, 4)]） / d=2 覆えない集合 0 個 / d=3 覆えない集合 0 個
  t=5: d=1 覆えない集合 22 個（極小: [(1, 3), (1, 4), (1, 5), (2, 4)]） / d=2 覆えない集合 4 個（極小: [(1, 3, 5)]） / d=3 覆えない集合 0 個
  t=6: d=1 覆えない集合 52 個（極小: [(1, 3), (1, 4), (1, 5), (1, 6)]） / d=2 覆えない集合 20 個（極小: [(1, 3, 5), (1, 3, 6), (1, 4, 6), (2, 4, 6)]） / d=3 覆えない集合 0 個
  t=7: d=1 覆えない集合 114 個（極小: [(1, 3), (1, 4), (1, 5), (1, 6)]） / d=2 覆えない集合 64 個（極小: [(1, 3, 5), (1, 3, 6), (1, 3, 7), (1, 4, 6)]） / d=3 覆えない集合 8 個（極小: [(1, 3, 5, 7)]）
  （t ≤ 2d なら覆えない集合は 0 個。d=2 では t=5 の {1,3,5} が最初の例）
==============================================================================
S2  系 M*（有限指数）の検査
==============================================================================
  Ex1      SUB_1=True SUB_1&2=False  格子が一致しない (面,面,S,必要な対の数): [('ac', 'abc', 'ac', 2)]
  Ex2^1_2  SUB_1=True SUB_1&2=True  格子が一致しない (面,面,S,必要な対の数): [('ace', 'abcde', 'ace', 3)]
  Ex2^0_2  SUB_1=True SUB_1&2=True  格子が一致しない (面,面,S,必要な対の数): [('ace', 'abcde', 'ace', 3)]
  Ex2^0_3  SUB_1=True SUB_1&2=True  格子が一致しない (面,面,S,必要な対の数): [('ace', 'abcde', 'ace', 3)]
  Ex2^0_2 語の段階（長さ≤11）: arity1 違反 None / arity2 違反 None
  Ex2^0_2 arity3 の証明書 E=□b□d□, F=a□c□e□, x=(a,c,e), y=(aa,cc,ee): True
  ランダムな例 4000 個（k=5、t=2..5、法 2 か 3）。(t, d, 被覆, 一致) ごとの (面の対, S) の数:
    (2, 1, 'covered', 'agree') 574
    (2, 2, 'covered', 'agree') 574
    (3, 1, 'covered', 'agree') 652
    (3, 1, 'not covered', 'DISAGREE') 17
    (3, 1, 'not covered', 'agree') 110
    (3, 2, 'covered', 'agree') 715
    (4, 1, 'covered', 'agree') 666
    (4, 1, 'not covered', 'DISAGREE') 37
    (4, 1, 'not covered', 'agree') 200
    (4, 2, 'covered', 'agree') 754
    (5, 1, 'covered', 'agree') 544
    (5, 1, 'not covered', 'DISAGREE') 55
    (5, 1, 'not covered', 'agree') 267
    (5, 2, 'covered', 'agree') 665
    (5, 2, 'not covered', 'agree') 12
  「覆えるのに一致しない」の数 = 0（系 M* が正しければ 0）
  判定条件で SUB_1・SUB_2 が成り立つ例のうち最初の 25 個を語の段階（長さ≤6、arity 1,2）で検査: 違反 0
  （39.8 秒）
==============================================================================
S3  Ex2 の族 Ex2^0_m：L = {a^i c^j e^l : i≡j≡l≡0 (m)} ∪ {a^i b^+ c^j d^+ e^l : i≡j≡l (m)}
==============================================================================
  右線形文法（最小 DFA から。非終端 = 状態、規則 q -> x q' と q -> x）。f=1, r=1。
    m     v     規則   thick    mu_ace    max tau       定理Bの上界    SUB_1&2(判定)
    2    15     27      10         6          6        93000           True
    3    25     41      14         9          9       217000           True
    4    37     57      18        12         12       412920         (手の証明)
    5    51     75      22        15         15       695640         (手の証明)
    6    67     95      26        18         18      1080040         (手の証明)
    8   105    141      34        24         24      2213400         (手の証明)
  L(G) = L の照合：長さ ≤ 8〜9 の語（先頭 4 文字は任意、その後は ND）と、乱数の長い ND な語 3000 個で不一致 0。
  tau は m について一次、文法の大きさは m の二次。超多項式ではない。
==============================================================================
S4  定理 B の対比：型付き非終端 (A_n, {a}) の最短の生成語
==============================================================================
  H(n)  : S -> A_n c,  A_i -> A_{i-1} A_{i-1} | a,  A_0 -> aa   （段 a<c、各段一文字）
  G1(n) : S -> b A_n,  A_i -> A_{i-1} A_{i-1} | c,  A_0 -> aa   （段 b<{a,c}、a と c が同じ段）
    n |     v  thick    最短(A_n,{a})       定理Bの上界 |     v  thick    最短(A_n,{a})
    1 |     3      5              1          540 |     3      5              4
    2 |     4      6              1          864 |     4      6              8
    3 |     5      7              1         1260 |     5      7             16
    4 |     6      8              1         1728 |     6      8             32
    5 |     7      9              1         2268 |     7      9             64
    6 |     8     10              1         2880 |     8     10            128
    7 |     9     11              1         3564 |     9     11            256
    8 |    10     12              1         4320 |    10     12            512
  H(n) では最短の生成語が定数、G1(n) では 2^(n+1)。定理 B は「各段一文字」を本当に使う。
  （G1(n) でも代表は aa で tau = 2。これは前回の報告の S3 の結果）
==============================================================================
完了（79.4 秒）
```

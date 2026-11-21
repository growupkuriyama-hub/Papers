# 内容ごとに値が変わる可換群の模型 𝒦：所属の特徴づけと、全ての型の τ

（2026-11-10 の依頼 README (257) への回答。Claude Fable 5.2。スクリプト `fable_content_values_2026-11-10.py` を同時に提出。）

## 0. 要約と判定の表

### 0.1 要約（5行）

1. **課題1** [証明済み]：𝒦 の言語が arity d で内容型付きの代入可能であることの必要十分条件を得た（定理1）。条件は「同じ総量 n を受け入れる二つの内容 M, M′ について、差の格子 N_M と N_{M′} が、n から動ける範囲の上で一致する」。有限群なら閉包報告の定理2.5 に戻る。
2. **段の効果** [証明済み]：t ≥ 2 では SUB₁ ⇏ SUB₂、SUB₂ ⇏ SUB₃ となる 𝒦 の言語がある（例 Ex1・Ex2）。段が内容の違う語どうしの移動を止めるのは、「成分の内側の段」に文脈の文字を置けないからである。
3. **課題2（主）** [証明済み]：**t ≤ f（特に f = 2 で t ≤ 2、一頂点 t = 1 を含む）なら、𝒦 ∩ C_{f,c_Σ} の任意の既約 good な表示で τ(G, c_Σ) = O_{k,f,r}(θ^{k²+2k} + v·θ^{k²+k+1})**（定理 A）。全ての型付き非終端についての上界で、μ だけの上界ではない。v には一次で依存する。v によらない形は、文脈が十分に豊かな場合だけ得た（系 A2）。
4. **届かなかった所**：t ≥ 3 で SUB₂ しか使えない場合（三つ以上の段にまたがる移動を戻せない。定理1 の Ex2 と同じ現象）、および v の除去。どちらも失敗する箇所を一か所に特定した（§3.6）。
5. **課題3・4**：定理 A の証明が 𝒦 を使うのは「深い点での局所的な飽和」(WS) だけである。命題7.4 の例 F₄・E₁・F_n は (WS) を破り、「p_S + H の短い ab の点が Q₂ に入る」という狙いの形は偽になる（具体的な点を出力）。課題4 の反例は作れなかった。t ≤ f では定理 A により存在しない。

### 0.2 判定の表

| 主張 | ラベル | 判定 | 根拠 |
|---|---|---|---|
| 定理1：𝒦 の SUB_d の必要十分条件 (★) | [証明済み] | 成立 | §2.2。全ての arity、手の証明 |
| 系1a：全ての N_M が一つの格子の制限なら全ての arity で代入可能 | [証明済み] | 成立 | §2.3 |
| 系1b：有限指数（有限群）での形。t = 1 なら定理2.5(ii) と一致 | [証明済み] | 成立 | §2.3 |
| T_n ∈ 𝒦（無限群では一致は「受け入れる範囲」でだけ要る） | [証明済み]（有限集合の全数検査） | 成立 | §2.4、S1 |
| Ex1：SUB₁ だが SUB₂ でない（t = 3、有限群） | [証明済み] | 成立 | §2.5、四語の証明書 |
| Ex2：SUB₁・SUB₂ だが SUB₃ でない（t = 5、有限群） | [証明済み] | 成立 | §2.5、四語の証明書 |
| 補題 M（移動）、補題 O′（しきい値つきの短縮）、補題 P（詰め物） | [証明済み] | 成立 | §3.2〜3.4 |
| **定理 A：t ≤ f なら τ ≤ τ_k = O(θ^{k²+2k} + vθ^{k²+k+1})** | **[証明済み]** | 成立 | §3.5 |
| 定理 A′：全ての d ≤ max(f,t) で代入可能なら t は任意 | [証明済み] | 成立 | §3.5（同じ証明） |
| 系 A2：文脈が詰め物と J の文字を全て含めば v によらない | [証明済み] | 成立 | §3.5 |
| t ≥ 3 かつ SUB₂ だけ、での τ の多項式上界 | [予想] | 未解決 | §3.6。戻しが失敗する箇所を特定 |
| v によらない上界（一般の場合） | [予想] | 未解決 | §3.6 |
| 定理 A は (WS) を満たす (T)-集合にそのまま延びる | [証明済み] | 成立 | §4.1 |
| F₄・E₁・F_n は (WS) を破り、狙いの形は偽 | [証明済み]（有限集合の全数検査） | この方法では届かない | §4.2、S4 |
| 課題4：𝒦 の中の超多項式の族 | — | 作れず。t ≤ f では存在しない | §5 |
| 小さな文法での代表と上界の比 | [観察（計算のみ）] | 比は 10⁻²⁶ 以下 | §6、S3 |

- [証明済み] は本報告の中の証明を指す。書いたのも点検したのも同じモデルなので、別のモデルによる確認はまだである。特に確認してほしい箇所を §3.7 に挙げた。
- 本報告は 𝒦 についての結果である。一般の正則言語、`op:fanout-two`、全ての Σ についての主張は含まない（§7）。

---

## 1. 記法と正規化

- Σ = Γ₁ ⊔ ⋯ ⊔ Γ_t、k = |Σ|。文字 a の段を s(a) と書く。ND は段非減少な語の全体。
- Π_M = {m ∈ ℕ^k : supp m = M}。語の組 x の**総量**は n = Σ_i Ψ(x_i)。
- 型 T = (M₁,…,M_d) について J_T = ⋃ M_i、b_T ∈ ℕ^k を (b_T)_a = #{i : a ∈ M_i} とする。型 T の組の総量は b_T + ℕ^{J_T} をちょうど動く。lo_i, hi_i は M_i の文字の段の最小と最大。
- 型付き非終端の文脈について：X = A_T の生成組は A の生成組なので、G の中の A の導出文脈（good な規則から誘導されるので許容的）がそのまま X の文脈になる。**以下の証明は文脈の短さを使わない。** 使うのは、各非終端 B の短い生成組 u_B（‖u_B‖₁ ≤ θ、p_B := Ψ(u_B)）と、規則が直接書く終端の個数 ≤ θ だけである。

**補題 K0（正規化）** [証明済み]。L ∈ 𝒦 とし、Q_M := {m ∈ Π_M : Φ(m) ∈ g_M + H_M}、𝓜* := {M : Q_M ≠ ∅}、N_M := ⟨Q_M − Q_M⟩ ≤ ℤ^M とする。このとき
- (a) L = {w ∈ ND : Ψ(w) ∈ Q}、Q = ⨆_{M∈𝓜*} Q_M。
- (b) **飽和**：q ∈ Q_M なら Q_M = Π_M ∩ (q + N_M)。

*証明。* (a) は定義。(b) の ⊆ は明らか。m ∈ Π_M、m − q ∈ N_M とする。N_M の生成元 q₁ − q₂ は Φ(q₁ − q₂) ∈ H_M を満たすので Φ(m) − Φ(q) ∈ H_M、従って m ∈ Q_M。∎

逆に、各 M に格子 N_M ≤ ℤ^M と点 q_M を与えて Q_M = Π_M ∩ (q_M + N_M) と置いたものは、A = ℤ^k、Φ = id で 𝒦 に入る。以下 𝒦 の言語は (Q_M, N_M)_{M∈𝓜*} で表す。

**型と文脈。** 型 T の組 x の成分が全て ND であるとする（そうでなければ D_L(x) = ∅）。許容的な文脈 E = v₀□v₁⋯□v_d について、E[x] ∈ ND かどうかは E と T だけで決まる：v₀ は ND で段 ≤ lo₁、v_i（0 < i < d）は ND で段が [hi_i, lo_{i+1}] の中、v_d は ND で段 ≥ hi_d。この条件を満たす E の全体を Comp(T) と書く。E ∈ Comp(T) なら

  E[x] ∈ L ⟺ Ψ(E) + n ∈ Q。

**受け入れる内容。** n ∈ b_T + ℕ^{J_T} について

  Acc_T(n) := {supp(Ψ(E) + n) : E ∈ Comp(T)、Ψ(E) + n ∈ Q}。

---

## 2. 課題1：𝒦 の所属の特徴づけ

### 2.1 主張

**定理1** [証明済み]。L ∈ 𝒦、d ≥ 1 とする。L が arity d で内容型付きの代入可能であることは、次の (★) と同値である。

> (★) arity d の全ての型 T、全ての n ∈ b_T + ℕ^{J_T}、全ての M, M′ ∈ Acc_T(n) について
> N_M ∩ O_T(n) = N_{M′} ∩ O_T(n)、ただし O_T(n) := {h ∈ ℤ^{J_T} : n + h ≥ b_T}。

L ∈ C_{2,c_Σ} は (★) が d = 1, 2 で成り立つこと（と L が 2-MCFL であること）である。

**系（同値類の形）** [証明済み]。(★) が arity d で成り立つとき、型 T の ND な組 x（総量 n、D_L(x) ≠ ∅）の分布同値類は、総量が (n + N_M) ∩ (b_T + ℕ^{J_T}) に入る型 T の ND な組の全体である（M ∈ Acc_T(n) は任意）。従って τ_X は、この集合の ℓ₁ ノルムの最小値に等しい。

### 2.2 証明

(⇐) x, y を型 T の組、総量を n, n′ とし、E ∈ D_L(x) ∩ D_L(y) とする。成分は全て ND で E ∈ Comp(T)。e := Ψ(E)、M := supp(e + n) = supp(e + n′)（どちらも supp(e) ∪ J_T）。h := n′ − n ∈ Q_M − Q_M ⊆ N_M、h ∈ O_T(n)、M ∈ Acc_T(n)。
- F ∈ D_L(x) を取る。f := Ψ(F)、M′ := supp(f + n) ∈ Acc_T(n)。(★) から h ∈ N_{M′}。f + n′ = (f + n) + h は Π_{M′} に入るので、補題 K0(b) から f + n′ ∈ Q_{M′}。F ∈ Comp(T) なので F[y] ∈ L。
- F ∈ D_L(y) なら、M ∈ Acc_T(n′) でもあるので、n′ と −h ∈ N_M ∩ O_T(n′) に同じ議論を使う。

(⇒) T, n, M, M′ ∈ Acc_T(n)、h ∈ N_M ∩ O_T(n) とする。n′ := n + h。総量 n, n′ の型 T の ND な組 x, y を取る（各 (a,i)、a ∈ M_i に一文字ずつ配り、残りを a を含む成分に配り、成分の中を段の順に並べる）。M の証人 E（e + n ∈ Q_M）について e + n′ ∈ Π_M ∩ (e + n + N_M) = Q_M なので E ∈ D_L(x) ∩ D_L(y)。代入可能性から D_L(x) = D_L(y)。M′ の証人 F について f + n、f + n′ ∈ Q_{M′}、従って h ∈ N_{M′}。逆の包含は M と M′ を入れ替える。∎

系は (⇐) の議論そのものである（同値なら文脈を共有し差は N_M に入る。逆に差が N_M に入れば M の証人を共有する）。

### 2.3 特別な場合

**系1a（共通の格子）** [証明済み]。全ての M, M′ ∈ 𝓜* と ∅ ≠ J ⊆ M ∩ M′ について N_M ∩ ℤ^J = N_{M′} ∩ ℤ^J なら、L は全ての arity で代入可能である。特に、一つの格子 K ≤ ℤ^k があって N_M = K ∩ ℤ^M（全ての M ∈ 𝓜*）なら全ての arity で代入可能。これは「H は共通で、値の剰余類 g_M だけが内容で変わる」場合（定理 H の (16) の形）を含む。

*証明。* Acc_T(n) の元は J_T を含むので (★) が成り立つ。∎

**系1b（有限指数）** [証明済み]。全ての M ∈ 𝓜* で N_M が ℤ^M の有限指数の部分群とする（A が有限ならそうなる。そのとき N_M = Φ⁻¹(H_M) ∩ ℤ^M）。このとき (★) は次と同値である。

> 全ての T、n、M, M′ ∈ Acc_T(n) について N_M ∩ ℤ^{J_T} = N_{M′} ∩ ℤ^{J_T}。

さらに t = 1 なら、Acc_T(n) = {M ∈ 𝓜* : M ⊇ J_T}（n によらない）で、条件は「全ての M, M′ ∈ 𝓜* で N_M ∩ ℤ^{M∩M′} = N_{M′} ∩ ℤ^{M∩M′}」となる。これは閉包報告の定理2.5(ii) である（(i) は 𝒦 の定義に含まれている）。この条件は d によらないので、t = 1・有限指数では SUB₁ ⟺ 全ての SUB_d。

*証明。* Λ := N_M ∩ ℤ^J は ℤ^J の有限指数なので、狭義に正の u ∈ Λ がある。λ ∈ Λ について、大きな N で λ + Nu, Nu ∈ O_T(n)（O_T(n) は十分に正のベクトルを全て含む）。従って Λ = ⟨Λ ∩ O_T(n)⟩ で、O_T(n) の上の一致は格子の一致と同値。
t = 1 では Comp(T) の制約がない。M ⊇ J、M ∈ 𝓜* とする。N_M は ℤ^M の有限指数なので、supp(e) = M で e ≡ q_M − n (mod N_M) の e ≥ 0 がある。従って M ∈ Acc_T(n)。J は M ∩ M′ の空でない部分集合を全て動く。∎

### 2.4 無限群で変わること

有限指数でなければ、(★) が要求するのは次の二つに限られる。
1. **同じ n を受け入れる** 内容どうしの比較だけ（Acc_T(n) は n によって変わる）。
2. 格子の全体ではなく、**n から動ける範囲** O_T(n) の上の一致だけ。

**例（T_n）** [証明済み（有限集合の全数検査、S1）]。閉包報告の例2.8 の T_n は 𝒦 に入る：Q₂ = {(1+3n,1,0), (1,1+3n,0)} は Π₂ ∩ (q + ℤ(3n,−3n,0)) に等しく、Q₃ = {(3,2,1),(1,3,2),(2,1,3)} は Π₃ ∩ (q + ⟨(−2,1,1),(−1,−1,2)⟩) に等しい（どちらも総和が一定なので有限。箱の中の全数で確認）。N_{abc} ∩ ℤ^{ab} = ℤ(3,−3,0) と N_{ab} = ℤ(3n,−3n,0) は n ≥ 2 で一致しないが、(★) は成り立つ。J = {a,b} の型で両方の内容に受け入れられる総量 (i, j) は i, j ≤ 3 を満たし（abc の点の座標は 3 以下）、そこから動ける範囲 O_T(n) には ℤ(3,−3,0) の零でない元がない（i − 3 ≥ 1 も j − 3 ≥ 1 も成り立たない）。J が一文字の型では、どちらの格子も ℤ^a、ℤ^b との交わりが 0 である。

### 2.5 段が移動を制限する仕組み

型 T の文脈は、成分 x_i の「内側の段」（lo_i < s < hi_i）の文字を持てない。従って
- 内容 M と M′ が、J_T のある成分の内側の段の文字で異なるなら、型 T を通して比べられることはない。
- arity を上げると成分が細かく分かれ、内側の段が減るので、比べられる内容の組が増える。t = 1 では内側の段がなく、この効果は消える。

**例 Ex1（SUB₁ だが SUB₂ でない）** [証明済み]。段 a < b < c、

  L = {a^i c^l : i ≡ l (mod 2)} ∪ {a^i b^j c^l : i, l は奇数、j ≥ 1}。

- N_{ac} = {(i,l) : i ≡ l}、N_{abc} ∩ ℤ^{ac} = 2ℤ × 2ℤ。
- SUB₁：型 ({a,c}) の語 a^i c^l の文脈は a*□c* だけで、内容 {a,b,c} に届かない。J が一文字なら両方の格子の制限は 2ℤ で一致。J が b を含めば内容は {a,b,c} だけ。従って (★) が d = 1 で成り立つ。
- SUB₂ の違反：x = (a, c)、y = (aa, cc)、E = □ac□、F = □b□。E[x] = aacc、E[y] = a³c³、F[x] = abc は L に入り、F[y] = aabcc は入らない。

**例 Ex2（SUB₂ だが SUB₃ でない）** [証明済み]。段 a < b < c < d < e、

  L = {a^i c^j e^l : i, j, l は奇数} ∪ {a^i b^p c^j d^q e^l : i ≡ j ≡ l (mod 2)、p, q ≥ 1}。

- N_{ace} = 2ℤ³、N_{abcde} ∩ ℤ^{ace} = 2ℤ³ + ℤ(1,1,1)。座標平面との交わりはどちらも 2ℤ²。
- SUB₁・SUB₂：arity ≤ 2 の型で両方の内容を受け入れるには、文脈が b と d の両方を持てなければならない。J = {a,c,e} で arity ≤ 2 なら、ある成分が二つの段にまたがり、その内側の b か d が置けない。従って両方に届くのは |J| ≤ 2 の型だけで、そこでは格子の制限が一致する。系1b の条件が d = 1, 2 で成り立つ。
- SUB₃ の違反：x = (a,c,e)、y = (aa,cc,ee)、E = □b□d□、F = □aa□cc□。E[x] = abcde、E[y] = aabccdee、F[x] = a³c³e は L に入り、F[y] = a⁴c⁴e² は入らない。

どちらの例も、スクリプト S1 が判定条件（系1b の厳密な形）と語の段階の検査の両方で確認した。四語の証明書は真の所属述語で判定している。

**帰結。** t ≥ 3 の 𝒦 ∩ C_{2,c_Σ} は「全ての arity で代入可能」より真に広い。この差が §3.6 の障害になる。

---

## 3. 課題2（主）：全ての型の τ

### 3.1 結果

B := (r+2)θ、T₀ := k!·B^k、D := v·(2^k − 1)^f とし、τ_{−1} := 0、j = 0, 1, …, k について

- K_j := (j + k)·D + 1
- C_j := θ + f + K_j·B + j·(τ_{j−1} + θ)
- T₁ := T₀ + j·τ_{j−1} + 2
- τ_j := kf + k·C_j + k²·T₀·(T₁ + C_j)

と定める。

**定理 A** [証明済み]。L ∈ 𝒦（段の数 t）とし、G を L の既約 good な表示（ファンアウト ≤ f、ランク ≤ r、非終端 v 個）とする。**t ≤ f** で L ∈ C_{f,c_Σ} なら

  τ(G, c_Σ) ≤ τ_k = O_{k,f,r}(θ^{k²+2k} + v·θ^{k²+k+1})。

特に f = 2 では t ≤ 2 の全ての 𝒦 ∩ C_{2,c_Σ} の言語（一頂点 t = 1 を含む）に当てはまる。k = 3 なら θ の 15 次で、v に一次。群の大きさにはよらない。

**定理 A′** [証明済み]。t が任意でも、L が全ての d ≤ max(f, t) で (d, c_Σ)-代入可能なら同じ上界が成り立つ。

**系 A2（v によらない場合）** [証明済み]。X = A_T の生成組 x と、G の中の A の導出文脈 E（長さは問わない）で、cont(E) が J_T と、A から到達できる全ての非終端 B の cont(u_B) を含むものがあるとする。このとき（定理 A か A′ の仮定の下で）

  τ_X ≤ kf + kC + k²T₀(T₀ + 2 + C)、C = θ + f + B

で、v によらない。次数は定理 S と同じ 2k。

**系（特徴データ）** [証明済み（`cor:distribution-representatives` による）]。定理 A の仮定の下で、特徴データは N_typ(1 + 2θ̄_G + r_max·τ_k) 以下、すなわち固定した k, f, r で ‖G‖ と θ の多項式である。

### 3.2 補題 M（移動）

**補題 M** [証明済み]。L ∈ 𝒦、z ∈ ℤ^k ∖ {0}、S := supp z とし、S が m 個の段にまたがるとする。L が arity m で代入可能とする。q, α ∈ ℕ^k が
- q ∈ Q、q − z ∈ Q、q ≥ z⁺ + 2·𝟙_S、
- α ∈ Q、α ≥ z⁺ + 2·𝟙_S

を満たすなら α − z ∈ Q。

*証明。* S の文字の段を σ₁ < ⋯ < σ_m とする。ξ_i を「パリクが (z⁺ + 𝟙_S) の段 σ_i の部分」の語、ξ′_i を「(z⁻ + 𝟙_S) の段 σ_i の部分」の語とする。どちらも内容は S ∩ Γ_{σ_i} で、組 ξ, ξ′ は同じ型である。
γ := q − z⁺ − 𝟙_S ≥ 𝟙_S。段の順に、段 σ_i では「ξ_i、次に γ の段 σ_i の文字」、他の段では γ のその段の文字を並べた語を w とする。w = v₀ξ₁v₁⋯ξ_m v_m で、v_i（0 < i < m）は γ の段 σ_i の S の文字を含むので空でない。w は ND でパリクは q、従って w ∈ L。ξ を ξ′ に替えた語も ND でパリクは q − z ∈ Q、従って L に入る。代入可能性から D_L(ξ) = D_L(ξ′)。
γ′ := α − z⁺ − 𝟙_S ≥ 𝟙_S で同じ並べ方をすると、文脈 F について F[ξ] は ND でパリク α、従って L に入る。よって F[ξ′] ∈ L で、そのパリクは α − z。∎

t = 1 では m = 1 で、閉包報告の補題2.3 にあたる。**定理 A が t ≤ f を仮定するのは、この補題で m ≤ t ≤ f としたいからである。**

### 3.3 補題 O′（しきい値つきの短縮）

**補題 O′** [証明済み]。H ≤ ℤ^k が各座標の絶対値 ≤ B の整数ベクトルで生成され、‖c‖_∞ ≤ C、T₀ = k!B^k、T₁ ≥ T₀ + 2 とする。y ∈ (c + H)、y ≥ 0、J の外で y = 0 とする。このとき、次の形の移動を高々 k 回行って ‖y′‖₁ ≤ kC + k²T₀(T₁ + C) の点 y′ に移れる。

> 移動：I := {i : y_i ≥ T₁} とし、0 ≠ z ∈ H、supp z ⊆ I、‖z‖_∞ ≤ T₀ を取って y を y − qz に替える（q ≥ 1）。途中の y − sz（0 ≤ s ≤ q）は全て ≥ 0 で、z_i > 0 の座標では y_i − sz_i ≥ 1。

*証明。* Astra の補題 O の証明と同じで、変更は二点。(1) I のしきい値を T₁ にする。(2) q := min_{z_i>0} ⌊(y_i − 1)/z_i⌋ とする（y_i ≥ T₁ > z_i なので q ≥ 1）。最小を与える座標は移動の後 z_i ≤ T₀ < T₁ 以下になり I から外れる。I の外の座標は変わらない。span_ℝ(H の生成元) ∩ ℝ^I = {0} になったとき、Cramer の公式で I の外の |y_i − c_i| ≤ T₁ + C から y_i ≤ C + kT₀(T₁ + C)。∎

スクリプト S2 が 400 個の乱数の例（k = 3）で、移動の回数 ≤ k と上界を確かめた。

### 3.4 導出木の中の詰め物

L(G) の文の導出木を一つ固定する。節点 ω のラベルを B_ω、生成組を y_ω、規則を R_ω、ω の外側の文脈（文全体から y_ω を除いたもの）のパリクを e_ω と書く。規則差分 d_R = Ψ(t_R) + Σ_j p_{B_j} − p_A は ‖d_R‖₁ ≤ B を満たす。

互いに比較できない節点の集合 Z について、s_Z を「各 ω ∈ Z の y_ω を短い生成組 u_{B_ω} に取り替えた文」とする。s_Z ∈ L。

節点 ν について
- Fill(ν) := ν の真の子孫 ω の cont(u_{B_ω}) の合併、
- j(ν) := |Fill(ν) ∖ supp(e_ν)|。

**補題 P（詰め物）** [証明済み]。節点 ν について、ν の真の子孫からなる集合 V で次を満たすものがある。
- (P1) V の元は互いに比較できない。|V| ≤ j(ν)。各 κ ∈ V で j(κ) ≤ j(ν) − 1。
- (P2) St := supp(e_ν) ∪ ⋃_{κ∈V} cont(u_{B_κ}) とする。ν の真の子孫 ω が、V の元でも、V の元の子孫でも先祖でもないなら、cont(u_{B_ω}) ⊆ St。

*証明。* V := ∅ から始める。(P2) を破る ω があれば、c ∈ cont(u_{B_ω}) ∖ St を取り、ω 以下の節点で詰め物が c を含むもののうち最も深いもの κ を V に加える。
- ω は V の元と比較できないので、ω の部分木に V の元はなく、κ も V の元と比較できない。
- κ の真の子孫の詰め物は c を含まない。c ∈ Fill(ν) ∖ supp(e_ν)、Fill(κ) ⊆ Fill(ν) ∖ {c}、supp(e_κ) ⊇ supp(e_ν) から j(κ) ≤ j(ν) − 1。
- 加えるたびに、Fill(ν) ∖ supp(e_ν) の新しい文字が St に入る。従って高々 j(ν) 回で止まる。∎

### 3.5 定理 A の証明

X = A_T とする。X の生成組の導出木のうち節点の数が最小のものを取る。根から葉への道の上に、同じ型付き非終端（ラベルと、生成組の成分の内容の組）は二度現れない。現れれば上の部分木を下の部分木に取り替えられ、先祖の成分の内容は変わらないので、X のより小さい導出木が得られるからである。従って木の深さは D = v(2^k − 1)^f 以下。この生成組を x、A の導出文脈を E とし、文 E[x] の導出木を固定する。

**主張(j)**：この木の節点 ν が j(ν) ≤ j を満たすなら、y_ν と同じ型で分布同値な組 y′ で ‖y′‖₁ ≤ τ_j のものがある。

根（x）に主張(k) を使えば定理が従う。j についての帰納法で示す（j = 0 も同じ議論で、V = ∅ になる）。

**(1) 詰め物と仮想の葉。** 補題 P の V を取る。各 κ ∈ V に主張(j−1) を使い、y_κ と同じ型で分布同値な ỹ_κ（‖ỹ_κ‖₁ ≤ τ_{j−1}）を取る。ŷ を「y_ν の中の各 y_κ を ỹ_κ に取り替えた組」とする。good なテンプレートへの代入は分布同値を保つ（`lem:witnessed-composition`）ので、ŷ は y_ν と同じ型で分布同値。n̂ := ŷ の総量。

**(2) 面 U。** U := supp(Ψ(s_V))。葉のうち V の部分木の外にあるものを「残る葉」と呼ぶ。U = St ∪ {残る葉の文字}。

**(3) 良い節点。** ν の部分木の節点 ω（V の元とその子孫を除く）が**悪い**とは、次のどれかを満たすこととする。
- ω = ν。
- ω は V の元の先祖。
- ある文字 a ∉ St について、a を持つ残る葉が全て ω の部分木に入る（そのような ω は、ν から「a の残る葉の最小共通先祖」までの一本の道の上にある）。

悪い節点は K_j = (j + k)D + 1 個以下。悪くない節点を良いと呼ぶ。

良い ω について、Z₁ := {ω} ∪ V と Z₂ := (ω の子) ∪ V は互いに比較できない集合で、**s_{Z₁} と s_{Z₂} の内容はどちらも U** である。
- 詰め物の文字は (P2) から St に入る（ω の子も良い節点の条件のうち (P2) の仮定を満たす）。
- St の外の文字 a は、ω の部分木の外に残る葉を持つ。

Ψ(s_{Z₂}) − Ψ(s_{Z₁}) = d_{R_ω} なので d_{R_ω} ∈ Q_U − Q_U ⊆ N_U。H′ := ⟨d_{R_ω} : ω は良い⟩ ⊆ N_U と置く。

**(4) 総量の式。** V を葉とみなした木で d_R を足し合わせると

  n̂ = p_{B_ν} + Σ_{良い ω} d_{R_ω} + Σ_{悪い ω} d_{R_ω} + Σ_{κ∈V}(Ψ(ỹ_κ) − p_{B_κ})。

従って n̂ − b ∈ c + H′、‖c‖_∞ ≤ C_j（b は y_ν の型の b_T）。

**(5) 短縮。** y := n̂ − b に補題 O′ を H′、T₁ = T₀ + jτ_{j−1} + 2 で使う。移動に使う z は H′ ⊆ N_U に入り、supp z ⊆ I₀ := {i : y_i ≥ T₁} ⊆ J、‖z‖_∞ ≤ T₀。

**(6) 一歩ずつ戻す。** α := e_ν + n₁（n₁ は現在の総量）が Q に入るとして、α − z ∈ Q を示す。
- q := Ψ(s_V) ∈ Q_U。a ∈ I₀ では q_a ≥ n̂_a − Σ_κ Ψ(ỹ_κ)_a ≥ T₁ − jτ_{j−1} = T₀ + 2。従って q ≥ z⁺ + 2·𝟙_S、q − z ∈ Π_U。**飽和（補題 K0(b)）**と −z ∈ N_U から q − z ∈ Q_U。
- α ≥ z⁺ + 2·𝟙_S：z_a > 0 では補題 O′ から (n₁ − z)_a ≥ b_a + 1 ≥ 2。z_a < 0 では α_a ≥ T₁。
- S は高々 t ≤ f 個の段にまたがるので、補題 M から α − z ∈ Q。

最初の α = e_ν + n̂ は Q に入る（ŷ は y_ν と分布同値）。従って最後の総量 n′ = y′ + b についても e_ν + n′ ∈ Q。

**(7) 結論。** 総量 n′ の、y_ν と同じ型の ND な組 y′ を作る（§2.2 の配り方）。ν の導出文脈 E_ν は Comp に入り、E_ν[y′] は ND でパリクが Q に入るので L に入る。ŷ と y′ は文脈 E_ν を共有し、arity ≤ f の代入可能性から分布同値。‖y′‖₁ ≤ kf + kC_j + k²T₀(T₁ + C_j) = τ_j。∎

**定理 A′** は (6) の「高々 t ≤ f 個の段」を「高々 t 個の段、arity ≤ t の代入可能性」に替えるだけである。

**系 A2 の証明。** 文 E[x] の導出木の根 ν（x の節点）で、supp(e_ν) = cont(E) が Fill(ν) と J を含むので j(ν) = 0、V = ∅、St ⊇ J。悪い節点は ν だけで、C ≤ θ + f + B、T₁ = T₀ + 2。木の深さを使わないので、節点の数が最小の木を取る必要もない。∎

**次数。** τ_j ≈ 2jk²T₀·τ_{j−1}、τ₀ ≈ k²T₀(T₀ + kDB) から τ_k = O(T₀^{k+2} + T₀^{k+1}DB)。スクリプト S3 が漸化式を計算し、k = 3 で θ について 15.00 次、v について 1.00 次と読んだ。

### 3.6 どこで止まるか

**(a) t ≥ 3 で SUB₂ だけの場合** [予想：上界は成り立つ／未解決]。証明の (6) で、補題 O′ の移動 z の支持が三つ以上の段にまたがると、補題 M が arity 3 以上の代入可能性を要求する。これは技術的な不足ではない。Ex2 では U = {a,b,c,d,e}、M₀ = {a,c,e}、z = (1,1,1) ∈ N_U ∩ ℤ^{ace} が N_{M₀} に入らず、言語は SUB₂ を満たす。つまり「U の中で実現された小さな移動を、詰め物のない面 M₀ に戻す」ことは、𝒦 ∩ C_{2,c_Σ} では一般に偽である。上界を示すには、そのような z が補題 O′ の移動として現れないことを文法の側から示す必要がある。

**(b) v の除去** [予想／未解決]。v が入るのは悪い節点の数 K_j ≤ (j+k)D + 1 だけで、原因は二種類の「鎖」である：詰め物の先祖の鎖と、ある文字の残る葉を全て抱える節点の鎖。鎖の上の d_R は一つの面 U に入らない。系 A2 はどちらの鎖も生じない場合である。

**(c) 依頼文の方向との対応。**
- 「型付き非終端 X ごとに、内容を保つ短い規則差分だけから格子を作る」：そのままでは足りない。倍増型の文法（S3 の G1(n)）では、内容 {a} を保つ短い差分が存在しない。内容を保たない詰め物（c を含む）を使い、詰め物の文字を別の枝の詰め物で補って面を固定する（補題 P）のが、今回の解決である。
- 「同じ内容の面の中の差分が θ で有界な生成系を持つか」：N_{M₀} 自体については分からない。証明が使うのは、より大きい面 U の中の部分格子 H′（生成元 ≤ (r+2)θ）と、その小さな元を M₀ に戻す補題 M である。
- 「型付きの積の厚さ」は使っていない。代表 y′ は一般に X の生成組ではない。

### 3.7 確認してほしい箇所

1. (3) の「s_{Z₁} と s_{Z₂} の内容がどちらも U」。悪い節点の三つの条件で尽くされているか。
2. (6) の q − z ∈ Q_U。仮想の葉 ỹ_κ を短くしてあるので、I₀ の座標は V の外で深い、という点。
3. 補題 P の j(κ) ≤ j(ν) − 1（κ の外側の文脈は ν の外側の文脈を含む）。
4. 補題 M の文脈の許容性（内側の区切りが空でないこと）。

---

## 4. 課題3：一頂点の命題7.4 への応用

### 4.1 定理 A が 𝒦 を使う場所

定理 A の証明で 𝒦 の定義（剰余類の形）を使うのは、(6) の q − z ∈ Q_U の一か所だけである。他は L = ND ∩ Ψ⁻¹(Q) という形と代入可能性しか使わない。従って次が成り立つ。

**(WS)（深い点での局所的な飽和）**：全ての U、q ∈ Q_U、z ∈ ⟨Q_U − Q_U⟩ について、‖z‖_∞ ≤ T₀ かつ q ≥ |z| + 2·𝟙_{supp z} なら q − z ∈ Q_U。

**命題4.1** [証明済み]。L = ND ∩ Ψ⁻¹(Q)（Q は任意）が定理 A（または A′）の代入可能性の仮定と、T₀ = k!((r+2)θ)^k についての (WS) を満たせば、定理 A の上界が成り立つ。

**系4.2** [証明済み]。一頂点（t = 1）で 𝒦 に入る SUB₁ の言語では、全ての内容 M について μ_M ≤ τ_{S_{(M)}} ≤ τ_k。特に μ_{ab} = O(θ^{15} + vθ^{13})（k = 3）。τ から μ への向きだけを使っている。

（X = S_{(M)} の同値類は内容 M の文の全体なので、τ_X = μ_M。）

### 4.2 命題7.4 の例では届かない

F₄ ∪ {P}、E₁ ∪ {(6,5)}、F_n ∪ {P}（n = 3, 4, 5）について、スクリプト S4 が次を全数で確かめた [証明済み（有限集合の全数検査）]。

| 例 | (T) | ⟨Q₃−Q₃⟩ の指数 | (WS) を破る組 (q, z) | q − z | P より短い ab の点（p_S + ⟨Q−Q⟩ の中） |
|---|---|---|---|---|---|
| F₄ ∪ {(14,26)} | 成立 | 59 | (6,4,4)、(−3,−1,0) | (9,5,4) ∉ Q₃ | 14 個。最短 (1,2) |
| E₁ ∪ {(6,5)} | 成立 | 7 | (4,4,2)、(−1,0,0) | (5,4,2) ∉ Q₃ | 5 個。最短 (1,5) |
| F₃ ∪ {(15,16)} | 成立 | 121 | (11,6,4)、(−1,−4,0) | (12,10,4) ∉ Q₃ | 3 個。最短 (12,4) |
| F₄ ∪ {(20,21)} | 成立 | 171 | (14,6,6)、(−1,−4,0) | (15,10,6) ∉ Q₃ | 5 個。最短 (15,1) |
| F₅ ∪ {(25,26)} | 成立 | 221 | (17,6,8)、(−1,−4,0) | (18,10,8) ∉ Q₃ | 6 個。最短 (19,2) |

読み取れること。
1. **狙いの形は偽。** どの例でも、補題 S2(c) の格子の最小のもの p_S + ⟨Q − Q⟩ は、P より短い ab の点を含む。それらは Q₂ = {P} に入らない。任意の表示の H はこの格子を含むので、「p_S + H の中の短い ab の点が Q₂ に入る」は、(T) と格子だけからは導けない。
2. **(T) の移動が効かない理由。** ⟨Q₃ − Q₃⟩ は小さな平面ベクトル（(3,1,0)、(1,0,0)、(1,4,0)）を含むが、それは Q₃ の点の差の整数結合であって、Q₃ の二点の差ではない。(T) は実現された差しか動かさない。𝒦 では飽和によって、深い点の近くで格子の小さな元が全て実現される。命題7.4 の例はちょうどこの性質を欠く。
3. **従って** 補題 S2(c) の格子と (T) の組み合わせで届くのは (WS) を満たす集合までで、命題7.4 の残りは (WS) の外にある。これは「剰余類の形でない」という依頼文の観察を、証明が使う一点に絞ったものである。

**命題7.4 への含意（書きすぎない）。** F_n は補題 C で既に落ちている。本報告は命題7.4 を解いていない。分かったのは、今回の方法を命題7.4 に延ばすには (6) を「実現された差の列で、途中の点が全て有効なもの」に替える必要がある、ということである（§8 の3）。

---

## 5. 課題4：否定の向き

**結論：作れなかった。** t ≤ f では作れないことが定理 A から従う。

**命題5.1** [証明済み（定理 A の系）]。𝒦 ∩ C_{f,c_Σ} の言語の族で t ≤ f、文法の大きさと厚さが poly(n) のものは、τ も特徴データも poly(n) である（k, f, r は固定）。全ての arity で代入可能な族なら t によらず同じ。

残る場所は「t ≥ 3、SUB₂ は成り立つが SUB₃ は成り立たない」だけである。そこで試した設計と、止まった理由を記す。

**設計（Ex2 の骨格）** [観察]。内容 M₀ = {a,c,e} の語だけからなる部分 L₀（長い語だけ）と、内側の段の文字 b, d を持つ部分 L₁（短い語を持つ）を合わせる。arity ≤ 2 の型が比べるのは二文字の平面の上の格子だけなので、N_{M₀} と N_U ∩ ℤ^{ace} を平面の外でずらせる。τ ≥ μ_{ace} を大きくするのが狙いである。

**止まった理由** [観察。証明ではない]。
1. **塊の内側の節点は純粋な詰め物しか持てない。** a の塊の途中にある節点の詰め物は、ND であるために a だけからなる。すると取り替えた文は内容 M₀ のままで、差は N_{M₀} に直接入る。倍増型の木では大部分の節点が塊の内側にあるので、N_{M₀} が小さな元を持ち、長い語だけの L₀ と両立しない。
2. **水準集合にすると重みが足りない。** L₀ を正の重みの一水準（全ての語が長い）にすると、長い部分木を持つ節点は、同じ重みの短い詰め物を必要とする。次の数え上げがこれを妨げる。

  **補題（窓）** [証明済み]。λ ∈ ℕ^k、θ ≥ 1 とする。2^i = λ·m（m ∈ ℕ^k、‖m‖₁ ≤ θ）と書ける i は高々 k(⌊log₂(kθ)⌋ + 1) 個。
  *証明。* 2^i = λ·m なら、ある a で λ_a m_a ≥ 2^i/k、従って 2^i/(kθ) ≤ λ_a ≤ 2^i。各 a について、この不等式を満たす i は ⌊log₂(kθ)⌋ + 1 個以下。∎

  倍増型の木は n 個の相異なる大きさ 2^i の節点を持つので、n ≤ k(log₂(kθ) + 1)、すなわち 2^n ≤ (2kθ)^k となり、長さは θ の多項式に収まる。
3. 1 と 2 を同時に避ける設計（ファンアウト 2 の非終端が b の塊をまたいで (c, c′) 型の詰め物を持つもの）は、三つの塊の個数を同時に合わせる必要があり、ファンアウト 2 の倍増では書けなかった。

これらは反例がないことの証明ではない。t ≥ 3 の場合は開いている。

---

## 6. 計算の要約

スクリプトは標準ライブラリだけを使い、乱数の種は 20261110。出力の全文は付録 B。実行時間は約 100 秒。

| 節 | 内容 | 結果 |
|---|---|---|
| S1 | Ex1：判定条件 arity 1 は成立、arity 2 は破れ。四語の証明書を真の述語で確認 | 一致 |
| S1 | Ex2：判定条件 arity 1, 2 は成立。語の段階（長さ ≤ 11）で arity 1, 2 の違反なし、arity 3 の違反あり | 一致 |
| S1 | T_n（n = 1, 2, 3）：剰余類の形と (T) を全数で確認 | 成立 |
| S1 | 乱数の 𝒦 の例 60 個 × arity 1, 2：判定条件が破れた 104 件は全て四語の証明書を構成でき、成立した 16 件は語の段階（長さ ≤ 7）で違反なし | 定理1 と整合 |
| S2 | 補題 O′：400 例で移動 ≤ k 回、上界との比の最大 0.035 | 成立 |
| S3 | 定理 A の漸化式：k = 3 で θ の 15 次、v の 1 次 | — |
| S3 | 文法 G1(n)（n = 1, 2, 3）、G2、G3、G3⁺：L(G) = L を有界に照合、型付き非終端ごとに代表を構成し、全ての短い文脈で分布を比較 | 全て一致 |
| S4 | F₄、E₁、F_n：§4.2 の表 | — |

**S3 の文法** [観察（計算のみ）。L(G) = L の一致は有界な照合]。
- **G1(n)**（v = n + 3、t = 2）：L = b·{w ∈ {a,c}⁺ : |w|_a は偶数}。A_i → A_{i−1}A_{i−1} | c、A_0 → aa。型付き非終端 (A_n, {a}) の生成組は a^{2^{n+1}} だけ（n = 3 で長さ 16）だが、代表は aa（τ = 2）。**最短の生成は指数的、代表は定数**という罠の状況を再現している。ここでは内容 {a} を保つ短い規則差分はなく、c を含む詰め物を使う §3 の議論が必要になる。
- **G2**（v = 4、t = 2）：L = {pw : p ∈ {b,e}⁺ に b が一つ、w ∈ {a,c}⁺、|w|_a ≡ [e ∈ p] (mod 2)}。内容（e の有無）で値が変わる。
- **G3**（v = 4、ファンアウト 2、t = 2、値群 ℤ）：L = {a^p u : c ∈ u、|u|_b = p} ∪ {a^p b^{p+1}}。内容（c の有無）で値が変わり、格子は共通（系1a）。
- **G3⁺**（v = 6、参考）：G3 に倍増の非終端 D₁（(aa, bb) だけを生成）を加えたもの。代表は (a, b)。

どの文法でも max τ_X = 4 で、定理 A の上界（10²⁷〜10⁴⁶）との比は 10⁻²⁶ 以下。上界の定数と次数は粗い。代表は「定理1 の系の同値類の中の最短の点」として構成し、全ての文脈（arity 1 は長さ ≤ 3〜4、arity 2 は長さ ≤ 3）で所属が一致することを真の述語で確かめた。

---

## 7. 主張していないこと

- μ の結果を τ の結果として書いていない。定理 A は全ての型付き非終端の代表の長さについての結果で、系4.2 だけが τ から μ を導いている。
- 定理 A は 𝒦（と (WS) を満たす集合）についての結果である。一般の正則言語、一文字が複数の辺を持つ経路の言語、`op:fanout-two` については何も主張しない。
- 上界は各 k について示した（次数は k² + 2k）。三文字の結果を全ての Σ の結果として書いていない。`prop:sl-reduction` が求める「全ての固定した Σ での一様な多項式データ」には、𝒦 の外の言語が残る。
- t ≥ 3 の 𝒦 ∩ C_{2,c_Σ} は未解決である。
- 定理 S（Astra）との関係：定理 S の言語は内容ごとの剰余類が全て同じ場合にあたる。定理 A は値が内容で変わる場合を含むが、t ≤ f を仮定し、v に依存し、次数が高い。定理 S を含んではいない。

---

## 8. 次の一手（見込み順）

1. **定理 A の独立な確認と、原稿への入れ方の検討。** §3.7 の四点を別のモデルで確認する。f = 2 で t ≤ 2（一頂点を含む）の 𝒦 は、三文字以上で「値が内容で変わる」場合に全ての型の τ が多項式になった最初のクラスになる。
2. **t ≥ 3 の場合。** (a) 補題 O′ の移動を、二つ以下の段にまたがるものに限れるかを調べる（詰め物が塊の境界にしか置けないこと、§5 の1 を使う）。(b) できなければ、Ex2 の骨格で、三つ以上の段にまたがる移動が補題 O′ に実際に現れる文法を作り、τ を計算する。どちらに転んでも `op:fanout-two` の向きの情報になる。
3. **(WS) の外（命題7.4）。** 証明の (6) を「実現された差 d_{R_ω} の列で、途中の点が全て有効」に替える。そのためには、詰め物で外字の座標を深くする必要がある（別の枝に同じ詰め物を複数置く）。F_n 型の Q に対して、厚さの小さい倍増型の文法が存在しえないことを、この形で示せるかを試す。あわせて、悪い節点の鎖の上の d_R を望遠鏡式にまとめて v を除けるかを見る。

---

## 付録 A：スクリプト `fable_content_values_2026-11-10.py`（全文）

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fable_content_values_2026-11-10.py
報告 fable_content_values_2026-11-10.md の検査スクリプト（Python 3、標準ライブラリのみ）。

規約
- 乱数の種は固定（20261110）。
- 無限の言語の所属は報告書の中で手で証明する。ここでの有界な検査は反例を探すためだけに使う。
- 「違反」として出力する語の四つ組は、必ず真の所属述語 member() で判定し直す。
- 有限の集合（T_n、F_4、E_1、F_n）は全数で検査する。

節
 S1  定理1（所属の判定条件）と語の段階の有界な検査の照合、例 Ex1・Ex2・T_n
 S2  補題 O'（しきい値つきの象限内短縮）の数値検査
 S3  定理 A の上界と、小さな文法での分布代表
 S4  課題3：F_4、E_1、F_n での格子と飽和の欠け
"""
import itertools
import math
import random
from fractions import Fraction

random.seed(20261110)


# ----------------------------------------------------------------------------
# 0. 言語の記述
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


class FiniteParikhLang:
    """一頂点（t=1）のパリク飽和な言語 π^{-1}(Q)、Q は有限集合。"""

    def __init__(self, name, letters, Q):
        self.name = name
        self.letters = letters
        self.k = len(letters)
        self.stage = {a: 1 for a in letters}
        self.Q = set(Q)

    def parikh(self, w):
        return tuple(w.count(a) for a in self.letters)

    def member(self, w):
        return len(w) > 0 and self.parikh(w) in self.Q


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


def section1():
    print('=' * 78)
    print('S1  定理1 の判定条件と語の段階の検査')
    print('=' * 78)

    # --- 例 Ex1：段 a<b<c。SUB_1 は成り立ち SUB_2 は破れる ---
    def cond1(M):
        if M == frozenset('ac'):
            return [({'a': 1, 'c': 1}, 2, 0)]
        if M == frozenset('abc'):
            return [({'a': 1}, 2, 1), ({'c': 1}, 2, 1)]
        return None
    ex1 = StageLang('Ex1', 'abc', {'a': 1, 'b': 2, 'c': 3}, cond1)
    c1, c2 = criterion(ex1, 1, 2), criterion(ex1, 2, 2)
    print('Ex1  L = {a^i c^l : i≡l (2)} ∪ {a^i b^j c^l : i, l 奇数}（段 a<b<c）')
    print('  判定条件 arity1:', 'OK' if c1 is None else '破れ',
          '/ arity2:', 'OK' if c2 is None else '破れ')
    cert = witness_to_certificate(ex1, c2)
    print('  arity2 の証人: 型', [show(M) for M in c2['T']], 'n', c2['n'], 'h', c2['h'],
          '面', show(c2['M1']), show(c2['M2']))
    print('  四つ組 (E,F,x,y) =', cert, ' 真の述語で確認:', check_certificate(ex1, cert))
    hand = (('', 'ac', ''), ('', 'b', ''), ('a', 'c'), ('aa', 'cc'))
    print('  手の証明書 E=□ac□, F=□b□, x=(a,c), y=(aa,cc):', check_certificate(ex1, hand))
    print('  語の段階（長さ≤9）arity1 の違反:', brute_sub(ex1, 1, 9))
    b2 = brute_sub(ex1, 2, 9)
    print('  語の段階（長さ≤9）arity2 の違反:', b2, '確認:', check_certificate(ex1, b2))

    # --- 例 Ex2：段 a<b<c<d<e。SUB_1, SUB_2 は成り立ち SUB_3 は破れる ---
    def cond2(M):
        if M == frozenset('ace'):
            return [({'a': 1}, 2, 1), ({'c': 1}, 2, 1), ({'e': 1}, 2, 1)]
        if M == frozenset('abcde'):
            return [({'a': 1, 'c': 1}, 2, 0), ({'c': 1, 'e': 1}, 2, 0)]
        return None
    ex2 = StageLang('Ex2', 'abcde', {c: i for i, c in enumerate('abcde')}, cond2)
    c1, c2 = criterion(ex2, 1, 2), criterion(ex2, 2, 2)
    print('Ex2  L = {a^i c^j e^l : 全て奇数} ∪ {a^i b^+ c^j d^+ e^l : i≡j≡l (2)}（段 a<b<c<d<e）')
    print('  判定条件 arity1:', 'OK' if c1 is None else '破れ',
          '/ arity2:', 'OK' if c2 is None else '破れ')
    hand3 = (('', 'b', 'd', ''), ('', 'aa', 'cc', ''), ('a', 'c', 'e'), ('aa', 'cc', 'ee'))
    print('  arity3 の手の証明書 E=□b□d□, F=□aa□cc□, x=(a,c,e), y=(aa,cc,ee):',
          check_certificate(ex2, hand3))
    print('  語の段階（長さ≤11）arity1 の違反:', brute_sub(ex2, 1, 11))
    print('  語の段階（長さ≤11）arity2 の違反:', brute_sub(ex2, 2, 11))
    b3 = brute_sub(ex2, 3, 11)
    print('  語の段階（長さ≤11）arity3 の違反:', b3, '確認:',
          None if b3 is None else check_certificate(ex2, b3))

    # --- T_n は K に入る（剰余類の形）ことの全数検査と、SUB の語の段階の検査 ---
    print('T_n（閉包報告の例2.8）: Q_M = Π_M ∩ (q + <Q_M - Q_M>) の全数検査')
    for n in (1, 2, 3):
        Q2 = [(1 + 3 * n, 1, 0), (1, 1 + 3 * n, 0)]
        Q3 = [(3, 2, 1), (1, 3, 2), (2, 1, 3)]
        ok = True
        for Qm, supp in ((Q2, (1, 1, 0)), (Q3, (1, 1, 1))):
            basis = echelon([tuple(a - b for a, b in zip(q, Qm[0])) for q in Qm[1:]])
            box = 3 * n + 8
            sat = set()
            for m in itertools.product(range(box), repeat=3):
                if tuple(1 if x > 0 else 0 for x in m) != supp:
                    continue
                if in_lat(tuple(a - b for a, b in zip(m, Qm[0])), basis):
                    sat.add(m)
            ok = ok and sat == set(Qm)
        lang = FiniteParikhLang('T%d' % n, 'abc', Q2 + Q3)
        L = 3 * n + 2
        v1 = brute_sub(lang, 1, L) if n <= 2 else 'skip'
        v2 = brute_sub(lang, 2, L) if n <= 1 else 'skip'
        print('  n=%d: 剰余類の形（箱 %d）=%s, (T)=%s, 語の段階 arity1 違反=%s, arity2 違反=%s'
              % (n, box, ok, check_T(set(Q2 + Q3)), v1, v2))

    # --- ランダムな K の例で、判定条件と語の段階の検査を照合 ---
    print('ランダムな例（k=3、段はランダム、法は 2,3）: 判定条件 vs 語の段階（長さ≤7）')
    stats = {'crit_fail_cert_ok': 0, 'crit_fail_cert_bad': 0,
             'crit_ok_brute_none': 0, 'crit_ok_brute_viol': 0}
    samples = 0
    letters = 'abc'
    stage_choices = [{'a': 1, 'b': 1, 'c': 1}, {'a': 1, 'b': 1, 'c': 2},
                     {'a': 1, 'b': 2, 'c': 2}, {'a': 1, 'b': 2, 'c': 3},
                     {'a': 1, 'b': 2, 'c': 1}]
    contents = [frozenset(c) for r in range(1, 4) for c in itertools.combinations(letters, r)]
    while samples < 60:
        stage = random.choice(stage_choices)
        table = {}
        mods = set()
        for M in contents:
            if random.random() < 0.6:
                cs = []
                for _ in range(random.randint(0, 2)):
                    mod = random.choice((2, 3))
                    w = {a: random.randint(0, mod - 1) for a in M}
                    cs.append((w, mod, random.randint(0, mod - 1)))
                    mods.add(mod)
                table[M] = cs
        lang = StageLang('rnd', letters, stage, lambda M: table.get(M))
        # 空の面を除く
        for M in list(lang.faces):
            if not any(lang.accept(m) for m in itertools.product(range(8), repeat=3)
                       if frozenset(a for a, x in zip(letters, m) if x > 0) == M):
                del lang.faces[M]
        if len(lang.faces) < 2:
            continue
        samples += 1
        Lcm = 1
        for m in mods:
            Lcm = Lcm * m // math.gcd(Lcm, m)
        for d in (1, 2):
            wit = criterion(lang, d, Lcm)
            if wit is not None:
                cert = witness_to_certificate(lang, wit)
                if check_certificate(lang, cert):
                    stats['crit_fail_cert_ok'] += 1
                else:
                    stats['crit_fail_cert_bad'] += 1
            else:
                viol = brute_sub(lang, d, 7)
                if viol is None:
                    stats['crit_ok_brute_none'] += 1
                else:
                    stats['crit_ok_brute_viol'] += 1
    print('  例の数 %d（各 arity 1,2）:' % samples, stats)
    print('  （crit_fail_cert_bad と crit_ok_brute_viol が 0 なら定理1 と整合）')


# ----------------------------------------------------------------------------
# 整数格子の道具
# ----------------------------------------------------------------------------
def echelon(gens):
    gens = [list(g) for g in gens if any(g)]
    if not gens:
        return []
    ncol = len(gens[0])
    rows, basis = gens, []
    for col in range(ncol):
        while True:
            nz = [r for r in rows if r[col] != 0]
            if len(nz) <= 1:
                break
            nz.sort(key=lambda r: abs(r[col]))
            p = nz[0]
            for r in nz[1:]:
                q = r[col] // p[col]
                for i in range(ncol):
                    r[i] -= q * p[i]
        nz = [r for r in rows if r[col] != 0]
        if nz:
            basis.append(nz[0])
            rows = [r for r in rows if r is not nz[0]]
        rows = [r for r in rows if any(r)]
    return basis


def in_lat(v, basis):
    v = list(v)
    for p in basis:
        c = next(i for i, x in enumerate(p) if x)
        if any(v[i] for i in range(c)):
            return False
        if v[c] % p[c]:
            return False
        q = v[c] // p[c]
        v = [a - q * b for a, b in zip(v, p)]
    return not any(v)


def rank(rows):
    rows = [[Fraction(x) for x in r] for r in rows]
    rk = 0
    ncol = len(rows[0]) if rows else 0
    for col in range(ncol):
        piv = next((i for i in range(rk, len(rows)) if rows[i][col] != 0), None)
        if piv is None:
            continue
        rows[rk], rows[piv] = rows[piv], rows[rk]
        for i in range(len(rows)):
            if i != rk and rows[i][col] != 0:
                f = rows[i][col] / rows[rk][col]
                rows[i] = [a - f * b for a, b in zip(rows[i], rows[rk])]
        rk += 1
    return rk


def check_T(Q):
    """有限の Q について条件 (T) を全数で検査する（厳密）。"""
    Q = set(Q)
    for q in Q:
        for q2 in Q:
            if q == q2:
                continue
            if tuple(x > 0 for x in q) != tuple(x > 0 for x in q2):
                continue
            h = tuple(b - a for a, b in zip(q, q2))
            lo = tuple(max(-x, 0) + (1 if x else 0) for x in h)   # h^- + 1_S
            hi = tuple(max(x, 0) + (1 if x else 0) for x in h)    # h^+ + 1_S
            for al in Q:
                if all(a >= l for a, l in zip(al, lo)):
                    if tuple(a + x for a, x in zip(al, h)) not in Q:
                        return False
                if all(a >= l for a, l in zip(al, hi)):
                    if tuple(a - x for a, x in zip(al, h)) not in Q:
                        return False
    return True


# ----------------------------------------------------------------------------
# 2. 補題 O'
# ----------------------------------------------------------------------------
def find_z(D, I, k, h, B):
    R = math.factorial(max(h - 1, 0)) * B ** max(h - 1, 0)
    for lam in itertools.product(range(-R, R + 1), repeat=h):
        if not any(lam):
            continue
        z = [sum(lam[j] * D[j][i] for j in range(h)) for i in range(k)]
        if any(z) and all(z[i] == 0 for i in range(k) if i not in I):
            return z
    return None


def section2():
    print('=' * 78)
    print('S2  補題 O\'（しきい値 T1 つき）の数値検査')
    print('=' * 78)
    k, done, worst, maxsteps = 3, 0, 0.0, 0
    while done < 400:
        B = random.randint(1, 3)
        h = random.randint(1, 2)
        D = [[random.randint(-B, B) for _ in range(k)] for _ in range(h)]
        if rank(D) < h:
            continue
        c = [random.randint(-3, 3) for _ in range(k)]
        C = max(1, max(abs(x) for x in c))
        y = None
        for _ in range(60):
            lam = [random.randint(-300, 300) for _ in range(h)]
            cand = [c[i] + sum(lam[j] * D[j][i] for j in range(h)) for i in range(k)]
            if min(cand) >= 0:
                y = cand
                break
        if y is None:
            continue
        T0 = math.factorial(k) * B ** k
        T1 = T0 + random.randint(0, 6) + 2
        steps = 0
        while True:
            I = [i for i in range(k) if y[i] >= T1]
            z = find_z(D, I, k, h, B)
            if z is None:
                break
            assert max(abs(t) for t in z) <= T0
            if sum(z) < 0 or all(t <= 0 for t in z):
                z = [-t for t in z]
            q = min((y[i] - 1) // z[i] for i in range(k) if z[i] > 0)
            assert q >= 1
            y = [a - q * b for a, b in zip(y, z)]
            assert min(y) >= 0
            steps += 1
            assert steps <= k
        I = [i for i in range(k) if y[i] >= T1]
        rest = [[row[i] for i in range(k) if i not in I] for row in D]
        assert (rank(rest) if rest and rest[0] else 0) == h
        bound = k * C + k * k * T0 * (T1 + C)
        assert sum(y) <= bound
        worst = max(worst, sum(y) / bound)
        maxsteps = max(maxsteps, steps)
        done += 1
    print('  試行 %d 回（k=3、生成元 1〜2 本、B≤3）: 全て上界 kC + k^2 T0 (T1+C) 以下。' % done)
    print('  最大の比 = %.4f、移動の回数の最大 = %d（≤ k）' % (worst, maxsteps))


# ----------------------------------------------------------------------------
# 3. 定理 A の上界と小さな文法
# ----------------------------------------------------------------------------
def tau_bound(k, f, r, theta, v):
    """定理 A の漸化式。tau_{-1} = 0、j = 0..k。"""
    B = (r + 2) * theta
    T0 = math.factorial(k) * B ** k
    Dp = v * (2 ** k - 1) ** f
    tau = 0
    for j in range(0, k + 1):
        K = (j + k) * Dp + 1
        C = theta + f + K * B + j * (tau + theta)
        T1 = T0 + j * tau + 2
        tau = k * f + k * C + k * k * T0 * (T1 + C)
    return tau


def V(j, kappa):
    return (j, kappa)


def enum_grammar(rules, arity, caps):
    lang = {A: set() for A in arity}
    changed = True
    while changed:
        changed = False
        for (A, comps, kids) in rules:
            for choice in itertools.product(*[sorted(lang[B]) for B in kids]):
                tup = tuple(''.join(it if isinstance(it, str) else choice[it[0]][it[1]]
                                    for it in comp) for comp in comps)
                if sum(map(len, tup)) <= caps[A] and tup not in lang[A]:
                    lang[A].add(tup)
                    changed = True
    return lang


def thickness(rules, arity):
    INF = 10 ** 9
    mn = {A: INF for A in arity}
    tl = lambda comps: sum(len(it) for comp in comps for it in comp if isinstance(it, str))
    ch = True
    while ch:
        ch = False
        for A, comps, kids in rules:
            val = tl(comps) + sum(mn[B] for B in kids)
            if val < mn[A]:
                mn[A] = val
                ch = True
    out = {A: INF for A in arity}
    out['S'] = 0
    ch = True
    while ch:
        ch = False
        for A, comps, kids in rules:
            for j, B in enumerate(kids):
                val = out[A] + tl(comps) + sum(mn[C] for i, C in enumerate(kids) if i != j)
                if val < out[B]:
                    out[B] = val
                    ch = True
    return max(out[A] + tl(comps) + sum(mn[B] for B in kids) for A, comps, kids in rules)


def all_words(letters, L):
    res, frontier = [''], ['']
    for _ in range(L):
        frontier = [w + a for w in frontier for a in letters]
        res += frontier
    return res


def all_contexts(letters, d, Lc):
    ws = all_words(letters, Lc)
    out = []

    def rec(i, cur, used):
        if i == d + 1:
            out.append(tuple(cur))
            return
        for w in ws:
            if used + len(w) > Lc:
                continue
            if 0 < i < d and not w:
                continue
            rec(i + 1, cur + [w], used + len(w))

    rec(0, [], 0)
    out.sort(key=lambda E: sum(map(len, E)))
    return out


def representative(lang, x, ctxs):
    T = typ(x)
    n = tuple(sum(c) for c in zip(*[lang.parikh(xi) for xi in x]))
    E0 = next(E for E in ctxs if lang.member(fill(E, x)))
    M0 = frozenset(fill(E0, x))
    b = tuple(sum(1 for M in T if a in M) for a in lang.letters)
    J = frozenset().union(*T)
    Jidx = [i for i, a in enumerate(lang.letters) if a in J]
    total = sum(n)
    for norm in range(sum(b), total + 1):
        extra = norm - sum(b)
        for add in itertools.product(range(extra + 1), repeat=len(Jidx)):
            if sum(add) != extra:
                continue
            n2 = list(b)
            for i, v in zip(Jidx, add):
                n2[i] += v
            if lang.in_lattice(M0, tuple(p - q for p, q in zip(n2, n))):
                x2 = build_tuple(lang, T, tuple(n2))
                agree = all(lang.member(fill(F, x)) == lang.member(fill(F, x2)) for F in ctxs)
                npos = sum(1 for F in ctxs if lang.member(fill(F, x)))
                return x2, E0, agree, npos
    raise AssertionError


def run_grammar(name, lang, rules, arity, caps, Lcheck, Lc1, Lc2, f, r, note=''):
    print('-' * 78)
    print(name, note)
    k, v = lang.k, len(arity)
    gl = enum_grammar(rules, arity, caps)
    gen = {w[0] for w in gl['S'] if len(w[0]) <= Lcheck}
    true = {w for w in nd_words(lang, Lcheck) if lang.member(w)}
    theta = max(1, thickness(rules, arity))
    bound = tau_bound(k, f, r, theta, v)
    print('  k=%d, v=%d, r=%d, f=%d, 厚さ θ=%d, L(G) と L の一致（長さ≤%d、%d 語）: %s'
          % (k, v, r, f, theta, Lcheck, len(true), gen == true))
    print('  定理 A の上界 τ_k ≈ 10^%.1f' % math.log10(bound))
    ctxs = {1: all_contexts(lang.letters, 1, Lc1), 2: all_contexts(lang.letters, 2, Lc2)}
    worst = 0
    rows = []
    for A in sorted(arity):
        bytype = {}
        for tup in gl[A]:
            bytype.setdefault(typ(tup), []).append(tup)
        for T, tups in sorted(bytype.items(), key=lambda p: [show(M) for M in p[0]]):
            x = min(tups, key=lambda t: (sum(map(len, t)), t))
            x2, E0, agree, npos = representative(lang, x, ctxs[len(x)])
            tau = sum(map(len, x2))
            worst = max(worst, tau)
            rows.append((A, '(' + ','.join(show(M) for M in T) + ')', sum(map(len, x)),
                         x2, tau, agree, npos))
    print('  %-4s %-12s %-8s %-18s %-4s %-6s %s'
          % ('非終', '型', '最短生成', '代表', 'τ_X', '同値', '（受理する文脈の数）'))
    for A, T, g, x2, tau, agree, npos in rows:
        print('  %-4s %-12s %-8d %-18s %-4d %-6s %d' % (A, T, g, x2, tau, agree, npos))
    print('  max τ_X = %d、上界との比 ≈ 10^%.1f' % (worst, math.log10(worst) - math.log10(bound)))
    return worst


def section3():
    print('=' * 78)
    print('S3  定理 A の上界と、小さな文法での分布代表')
    print('=' * 78)
    print('上界 τ_k の例: (k,f,r,θ,v)=(3,2,2,4,4) → 10^%.1f、(3,2,2,8,4) → 10^%.1f、'
          '(3,2,2,8,40) → 10^%.1f'
          % tuple(math.log10(tau_bound(3, 2, 2, t, v)) for t, v in ((4, 4), (8, 4), (8, 40))))
    print('  （θ を 2 倍にしたときの増え方から読む次数: %.2f、v を 10 倍: %.2f）'
          % (math.log2(tau_bound(3, 2, 2, 2 ** 21, 4) / tau_bound(3, 2, 2, 2 ** 20, 4)),
             math.log10(tau_bound(3, 2, 2, 8, 10 ** 9) / tau_bound(3, 2, 2, 8, 10 ** 8))))

    # ---- G1(n)：段 {b} < {a,c}。L = b・{w in {a,c}+ : |w|_a 偶数}。型付きの生成が長い ----
    def condG1(M):
        if 'b' not in M or M == frozenset('b'):
            return None
        return [({'b': 1}, 0, 1), ({'a': 1}, 2, 0)]
    for n in (1, 2, 3):
        lang = StageLang('G1', 'abc', {'b': 1, 'a': 2, 'c': 2}, condG1)
        rules = [('S', (('b', V(0, 0)),), ('W',)),
                 ('W', ((V(0, 0), V(1, 0)),), ('W', 'W')),
                 ('W', (('c',),), ()),
                 ('W', (('aa',),), ()),
                 ('W', (('a', V(0, 0), 'a'),), ('W',)),
                 ('W', ((V(0, 0),),), ('A%d' % n,)),
                 ('A0', (('aa',),), ())]
        arity = {'S': 1, 'W': 1, 'A0': 1}
        caps = {'S': 7, 'W': 6, 'A0': 99}
        for i in range(1, n + 1):
            rules.append(('A%d' % i, ((V(0, 0), V(1, 0)),), ('A%d' % (i - 1), 'A%d' % (i - 1))))
            rules.append(('A%d' % i, (('c',),), ()))
            arity['A%d' % i] = 1
            caps['A%d' % i] = 99
        run_grammar('G1(n=%d)' % n, lang, rules, arity, caps, 7, 4, 3, 1, 2,
                    '  S→bW, W→WW|c|aa|aWa|A_n, A_i→A_{i-1}A_{i-1}|c, A_0→aa')

    # ---- G2：段 {b,e} < {a,c}。内容（e の有無）で値が変わる ----
    def condG2(M):
        if 'b' not in M or not (M & frozenset('ac')):
            return None
        return [({'b': 1}, 0, 1), ({'a': 1}, 2, 1 if 'e' in M else 0)]
    lang = StageLang('G2', 'abce', {'b': 1, 'e': 1, 'a': 2, 'c': 2}, condG2)
    rules = [('S', (('b', V(0, 0)),), ('W',)),
             ('S', ((V(0, 0), V(1, 0)),), ('P', 'X')),
             ('P', (('eb',),), ()), ('P', (('be',),), ()),
             ('P', (('e', V(0, 0)),), ('P',)), ('P', ((V(0, 0), 'e'),), ('P',)),
             ('W', ((V(0, 0), V(1, 0)),), ('W', 'W')),
             ('W', (('c',),), ()), ('W', (('aa',),), ()),
             ('W', (('a', V(0, 0), 'a'),), ('W',)),
             ('X', (('a',),), ()),
             ('X', ((V(0, 0), V(1, 0)),), ('X', 'W')),
             ('X', ((V(0, 0), V(1, 0)),), ('W', 'X'))]
    arity = {'S': 1, 'P': 1, 'W': 1, 'X': 1}
    caps = {'S': 6, 'P': 5, 'W': 5, 'X': 5}
    run_grammar('G2', lang, rules, arity, caps, 6, 3, 3, 1, 2,
                '  L = {p w : p∈{b,e}+ に b が一つ, w∈{a,c}+, |w|_a ≡ [e∈p] (2)}')

    # ---- G3：ファンアウト 2、段 {a} < {b,c}、無限群。内容（c の有無）で値が変わる ----
    def condG3(M):
        if M == frozenset('ab'):
            return [({'b': 1, 'a': -1}, 0, 1)]
        if M == frozenset('abc'):
            return [({'b': 1, 'a': -1}, 0, 0)]
        return None
    lang = StageLang('G3', 'abc', {'a': 1, 'b': 2, 'c': 2}, condG3)
    grow = lambda X: [(X, ((V(0, 0),), (V(0, 1), 'c')), (X,)),
                      (X, ((V(0, 0),), ('c', V(0, 1))), (X,)),
                      (X, (('a', V(0, 0)), (V(0, 1), 'b')), (X,)),
                      (X, (('a', V(0, 0)), ('b', V(0, 1))), (X,))]
    rules = [('S', ((V(0, 0), 'c', V(0, 1)),), ('R',)),
             ('S', ((V(0, 0), 'b', V(0, 1)),), ('Q',)),
             ('S', ((V(0, 0), 'b', V(0, 1)),), ('Z',)),
             ('R', (('a',), ('b',)), ()),
             ('Q', (('a',), ('c',)), ()),
             ('Q', (('a', V(0, 0)), (V(0, 1), 'c')), ('R',)),
             ('Q', (('a', V(0, 0)), ('c', V(0, 1))), ('R',)),
             ('Z', (('a',), ('b',)), ()),
             ('Z', (('a', V(0, 0)), (V(0, 1), 'b')), ('Z',))] + grow('R') + grow('Q')
    arity = {'S': 1, 'R': 2, 'Q': 2, 'Z': 2}
    caps = {'S': 8, 'R': 7, 'Q': 7, 'Z': 7}
    run_grammar('G3', lang, rules, arity, caps, 8, 4, 3, 2, 1,
                '  L = {a^p u : c∈u, |u|_b = p} ∪ {a^p b^{p+1}}（ファンアウト 2、値群 Z）')

    # ---- G3+：G3 に倍増の非終端 D1 を加える（v=6、参考）----
    rules2 = rules + [('Z', ((V(0, 0),), (V(0, 1),)), ('D1',)),
                      ('R', ((V(0, 0),), (V(0, 1),)), ('D1',)),
                      ('D1', ((V(0, 0), V(1, 0)), (V(0, 1), V(1, 1))), ('D0', 'D0')),
                      ('D0', (('a',), ('b',)), ())]
    # D1 は (aa,bb) だけを生成する。Z と R の両方から呼ばれる。
    arity2 = dict(arity, D1=2, D0=2)
    caps2 = dict(caps, D1=7, D0=7)
    run_grammar('G3+', lang, rules2, arity2, caps2, 8, 4, 3, 2, 2,
                '  G3 に D1→(ξ1ξ1\',ξ2ξ2\')(D0,D0), D0→(a,b), Z→D1, R→D1 を追加（v=6、参考）')


# ----------------------------------------------------------------------------
# 4. 課題3：F_4, E_1, F_n
# ----------------------------------------------------------------------------
def section4():
    print('=' * 78)
    print('S4  課題3：命題7.4 の例での格子と飽和の欠け')
    print('=' * 78)
    examples = [('F4 ∪ {(14,26)}', [(1, 3, 12), (4, 8, 1), (6, 4, 4), (12, 1, 3)], (14, 26, 0)),
                ('E1 ∪ {(6,5)}', [(1, 8, 1), (2, 3, 4), (4, 4, 2), (8, 1, 1)], (6, 5, 0))]
    for n in (3, 4, 5):
        Fn = [(3 * n + 2 * j, 1 + 5 * j, 2 * (n - j)) for j in range(n)]
        Fn += [(1, 10 * n - 8, 1), (10 * n - 4, 1, 1)]
        examples.append(('F_%d ∪ {P}' % n, Fn, (5 * n, 5 * n + 1, 0)))
    for name, Q3, P in examples:
        Q = set(Q3) | {P}
        N3 = echelon([tuple(a - b for a, b in zip(q, Q3[0])) for q in Q3[1:]])
        idx = abs(N3[0][0] * N3[1][1] * N3[2][2]) if len(N3) == 3 else None
        Hall = echelon([tuple(a - b for a, b in zip(q, Q3[0])) for q in Q3[1:]]
                       + [tuple(a - b for a, b in zip(P, Q3[0]))])
        idx_all = abs(Hall[0][0] * Hall[1][1] * Hall[2][2]) if len(Hall) == 3 else None
        box = max(max(q) for q in Q3) + 1
        sat = [m for m in itertools.product(range(1, box), repeat=3)
               if in_lat(tuple(a - b for a, b in zip(m, Q3[0])), N3)]
        missing = sorted(set(sat) - set(Q3), key=lambda m: (sum(m), m))
        normP = sum(P)
        short_ab = sorted(((i, j) for i in range(1, normP) for j in range(1, normP - i)
                           if in_lat((i - P[0], j - P[1], 0), Hall)),
                          key=lambda p: (sum(p), p))
        plane = sorted(((x, y) for x in range(-60, 61) for y in range(-60, 61)
                        if (x, y) != (0, 0) and in_lat((x, y, 0), N3)),
                       key=lambda p: (abs(p[0]) + abs(p[1]), p))
        print(name)
        print('  (T)（全数）: %s、|Q3|=%d、<Q3-Q3> の指数=%s、<Q-Q> の指数=%s'
              % (check_T(Q), len(Q3), idx, idx_all))
        print('  Π3 ∩ (q + <Q3-Q3>) の箱 [1,%d]^3 の点 %d 個のうち Q3 に入らないもの %d 個。最短: %s'
              % (box - 1, len(sat), len(missing), missing[:3]))
        print('  P=%s（長さ %d）。p_S + <Q-Q> の中の、P より短い ab の点: %d 個。最短: %s'
              % (P[:2], normP, len(short_ab), short_ab[:3]))
        print('  <Q3-Q3> の中の最短の平面ベクトル: %s。P に足した点は Q2 に入るか: %s'
              % (plane[:2], [((P[0] + x, P[1] + y, 0) in Q) for x, y in plane[:2]]))
        # (WS) を破る組：q in Q3、z は格子の小さな元、q >= |z| + 2（z の支持の上）、q - z は Q3 の外
        ws = None
        for q in sorted(Q3):
            for x, y in plane[:6]:
                z = (x, y, 0)
                if all(a >= abs(c) + 2 for a, c in zip(q, z) if c):
                    qz = tuple(a - c for a, c in zip(q, z))
                    if qz not in Q:
                        ws = (q, z, qz)
                        break
            if ws:
                break
        print('  (WS) を破る組 (q, z, q-z): %s' % (ws,))


if __name__ == '__main__':
    section1()
    section2()
    section3()
    section4()
    print('=' * 78)
    print('完了')
```

## 付録 B：出力（全文）

```text
==============================================================================
S1  定理1 の判定条件と語の段階の検査
==============================================================================
Ex1  L = {a^i c^l : i≡l (2)} ∪ {a^i b^j c^l : i, l 奇数}（段 a<b<c）
  判定条件 arity1: OK / arity2: 破れ
  arity2 の証人: 型 ['a', 'c'] n (1, 0, 1) h (1, 0, 1) 面 ac abc
  四つ組 (E,F,x,y) = (('', 'cc', ''), ('', 'b', ''), ('a', 'c'), ('aa', 'cc'))  真の述語で確認: True
  手の証明書 E=□ac□, F=□b□, x=(a,c), y=(aa,cc): True
  語の段階（長さ≤9）arity1 の違反: None
  語の段階（長さ≤9）arity2 の違反: (('', 'aa', ''), ('a', 'aaabb', ''), ('a', 'c'), ('aa', 'cc')) 確認: True
Ex2  L = {a^i c^j e^l : 全て奇数} ∪ {a^i b^+ c^j d^+ e^l : i≡j≡l (2)}（段 a<b<c<d<e）
  判定条件 arity1: OK / arity2: OK
  arity3 の手の証明書 E=□b□d□, F=□aa□cc□, x=(a,c,e), y=(aa,cc,ee): True
  語の段階（長さ≤11）arity1 の違反: None
  語の段階（長さ≤11）arity2 の違反: None
  語の段階（長さ≤11）arity3 の違反: (('', 'b', 'd', ''), ('', 'aa', 'cccccc', ''), ('a', 'c', 'e'), ('aa', 'cc', 'ee')) 確認: True
T_n（閉包報告の例2.8）: Q_M = Π_M ∩ (q + <Q_M - Q_M>) の全数検査
  n=1: 剰余類の形（箱 11）=True, (T)=True, 語の段階 arity1 違反=None, arity2 違反=None
  n=2: 剰余類の形（箱 14）=True, (T)=True, 語の段階 arity1 違反=None, arity2 違反=skip
  n=3: 剰余類の形（箱 17）=True, (T)=True, 語の段階 arity1 違反=skip, arity2 違反=skip
ランダムな例（k=3、段はランダム、法は 2,3）: 判定条件 vs 語の段階（長さ≤7）
  例の数 60（各 arity 1,2）: {'crit_fail_cert_ok': 104, 'crit_fail_cert_bad': 0, 'crit_ok_brute_none': 16, 'crit_ok_brute_viol': 0}
  （crit_fail_cert_bad と crit_ok_brute_viol が 0 なら定理1 と整合）
==============================================================================
S2  補題 O'（しきい値 T1 つき）の数値検査
==============================================================================
  試行 400 回（k=3、生成元 1〜2 本、B≤3）: 全て上界 kC + k^2 T0 (T1+C) 以下。
  最大の比 = 0.0348、移動の回数の最大 = 2（≤ k）
==============================================================================
S3  定理 A の上界と、小さな文法での分布代表
==============================================================================
上界 τ_k の例: (k,f,r,θ,v)=(3,2,2,4,4) → 10^27.6、(3,2,2,8,4) → 10^32.0、(3,2,2,8,40) → 10^32.3
  （θ を 2 倍にしたときの増え方から読む次数: 15.00、v を 10 倍: 1.00）
------------------------------------------------------------------------------
G1(n=1)   S→bW, W→WW|c|aa|aWa|A_n, A_i→A_{i-1}A_{i-1}|c, A_0→aa
  k=3, v=4, r=2, f=1, 厚さ θ=5, L(G) と L の一致（長さ≤7、63 語）: True
  定理 A の上界 τ_k ≈ 10^28.9
  非終   型            最短生成     代表                 τ_X  同値     （受理する文脈の数）
  A0   (a)          2        ('aa',)            2    True   25
  A1   (a)          4        ('aa',)            2    True   25
  A1   (c)          1        ('c',)             1    True   25
  S    (ab)         3        ('baa',)           3    True   16
  S    (abc)        4        ('baac',)          4    True   16
  S    (bc)         2        ('bc',)            2    True   16
  W    (a)          2        ('aa',)            2    True   25
  W    (ac)         3        ('aac',)           3    True   25
  W    (c)          1        ('c',)             1    True   25
  max τ_X = 4、上界との比 ≈ 10^-28.3
------------------------------------------------------------------------------
G1(n=2)   S→bW, W→WW|c|aa|aWa|A_n, A_i→A_{i-1}A_{i-1}|c, A_0→aa
  k=3, v=5, r=2, f=1, 厚さ θ=6, L(G) と L の一致（長さ≤7、63 語）: True
  定理 A の上界 τ_k ≈ 10^30.1
  非終   型            最短生成     代表                 τ_X  同値     （受理する文脈の数）
  A0   (a)          2        ('aa',)            2    True   25
  A1   (a)          4        ('aa',)            2    True   25
  A1   (c)          1        ('c',)             1    True   25
  A2   (a)          8        ('aa',)            2    True   25
  A2   (ac)         5        ('aac',)           3    True   25
  A2   (c)          1        ('c',)             1    True   25
  S    (ab)         3        ('baa',)           3    True   16
  S    (abc)        4        ('baac',)          4    True   16
  S    (bc)         2        ('bc',)            2    True   16
  W    (a)          2        ('aa',)            2    True   25
  W    (ac)         3        ('aac',)           3    True   25
  W    (c)          1        ('c',)             1    True   25
  max τ_X = 4、上界との比 ≈ 10^-29.5
------------------------------------------------------------------------------
G1(n=3)   S→bW, W→WW|c|aa|aWa|A_n, A_i→A_{i-1}A_{i-1}|c, A_0→aa
  k=3, v=6, r=2, f=1, 厚さ θ=7, L(G) と L の一致（長さ≤7、63 語）: True
  定理 A の上界 τ_k ≈ 10^31.1
  非終   型            最短生成     代表                 τ_X  同値     （受理する文脈の数）
  A0   (a)          2        ('aa',)            2    True   25
  A1   (a)          4        ('aa',)            2    True   25
  A1   (c)          1        ('c',)             1    True   25
  A2   (a)          8        ('aa',)            2    True   25
  A2   (ac)         5        ('aac',)           3    True   25
  A2   (c)          1        ('c',)             1    True   25
  A3   (a)          16       ('aa',)            2    True   25
  A3   (ac)         6        ('aac',)           3    True   25
  A3   (c)          1        ('c',)             1    True   25
  S    (ab)         3        ('baa',)           3    True   16
  S    (abc)        4        ('baac',)          4    True   16
  S    (bc)         2        ('bc',)            2    True   16
  W    (a)          2        ('aa',)            2    True   25
  W    (ac)         3        ('aac',)           3    True   25
  W    (c)          1        ('c',)             1    True   25
  max τ_X = 4、上界との比 ≈ 10^-30.5
------------------------------------------------------------------------------
G2   L = {p w : p∈{b,e}+ に b が一つ, w∈{a,c}+, |w|_a ≡ [e∈p] (2)}
  k=4, v=4, r=2, f=1, 厚さ θ=4, L(G) と L の一致（長さ≤6、99 語）: True
  定理 A の上界 τ_k ≈ 10^45.8
  非終   型            最短生成     代表                 τ_X  同値     （受理する文脈の数）
  P    (be)         2        ('be',)            2    True   16
  S    (ab)         3        ('baa',)           3    True   12
  S    (abc)        4        ('baac',)          4    True   12
  S    (abce)       4        ('beac',)          4    True   15
  S    (abe)        3        ('bea',)           3    True   15
  S    (bc)         2        ('bc',)            2    True   12
  W    (a)          2        ('aa',)            2    True   13
  W    (ac)         3        ('aac',)           3    True   13
  W    (c)          1        ('c',)             1    True   13
  X    (a)          1        ('a',)             1    True   17
  X    (ac)         2        ('ac',)            2    True   17
  max τ_X = 4、上界との比 ≈ 10^-45.2
------------------------------------------------------------------------------
G3   L = {a^p u : c∈u, |u|_b = p} ∪ {a^p b^{p+1}}（ファンアウト 2、値群 Z）
  k=3, v=4, r=1, f=2, 厚さ θ=5, L(G) と L の一致（長さ≤8、78 語）: True
  定理 A の上界 τ_k ≈ 10^27.2
  非終   型            最短生成     代表                 τ_X  同値     （受理する文脈の数）
  Q    (a,bc)       4        ('aa', 'bc')       4    True   19
  Q    (a,c)        2        ('a', 'c')         2    True   19
  R    (a,b)        2        ('a', 'b')         2    True   22
  R    (a,bc)       3        ('a', 'bc')        3    True   19
  S    (ab)         3        ('abb',)           3    True   8
  S    (abc)        3        ('abc',)           3    True   12
  Z    (a,b)        2        ('a', 'b')         2    True   22
  max τ_X = 4、上界との比 ≈ 10^-26.6
------------------------------------------------------------------------------
G3+   G3 に D1→(ξ1ξ1',ξ2ξ2')(D0,D0), D0→(a,b), Z→D1, R→D1 を追加（v=6、参考）
  k=3, v=6, r=2, f=2, 厚さ θ=5, L(G) と L の一致（長さ≤8、78 語）: True
  定理 A の上界 τ_k ≈ 10^29.0
  非終   型            最短生成     代表                 τ_X  同値     （受理する文脈の数）
  D0   (a,b)        2        ('a', 'b')         2    True   22
  D1   (a,b)        4        ('a', 'b')         2    True   22
  Q    (a,bc)       4        ('aa', 'bc')       4    True   19
  Q    (a,c)        2        ('a', 'c')         2    True   19
  R    (a,b)        2        ('a', 'b')         2    True   22
  R    (a,bc)       3        ('a', 'bc')        3    True   19
  S    (ab)         3        ('abb',)           3    True   8
  S    (abc)        3        ('abc',)           3    True   12
  Z    (a,b)        2        ('a', 'b')         2    True   22
  max τ_X = 4、上界との比 ≈ 10^-28.4
==============================================================================
S4  課題3：命題7.4 の例での格子と飽和の欠け
==============================================================================
F4 ∪ {(14,26)}
  (T)（全数）: True、|Q3|=4、<Q3-Q3> の指数=59、<Q-Q> の指数=59
  Π3 ∩ (q + <Q3-Q3>) の箱 [1,12]^3 の点 28 個のうち Q3 に入らないもの 24 個。最短: [(1, 7, 1), (3, 3, 4), (2, 3, 8)]
  P=(14, 26)（長さ 40）。p_S + <Q-Q> の中の、P より短い ab の点: 14 個。最短: [(1, 2), (4, 3), (7, 4)]
  <Q3-Q3> の中の最短の平面ベクトル: [(-3, -1), (3, 1)]。P に足した点は Q2 に入るか: [False, False]
  (WS) を破る組 (q, z, q-z): ((6, 4, 4), (-3, -1, 0), (9, 5, 4))
E1 ∪ {(6,5)}
  (T)（全数）: True、|Q3|=4、<Q3-Q3> の指数=7、<Q-Q> の指数=7
  Π3 ∩ (q + <Q3-Q3>) の箱 [1,8]^3 の点 80 個のうち Q3 に入らないもの 76 個。最短: [(1, 1, 1), (2, 1, 1), (3, 1, 1)]
  P=(6, 5)（長さ 11）。p_S + <Q-Q> の中の、P より短い ab の点: 5 個。最短: [(1, 5), (2, 5), (3, 5)]
  <Q3-Q3> の中の最短の平面ベクトル: [(-1, 0), (1, 0)]。P に足した点は Q2 に入るか: [False, False]
  (WS) を破る組 (q, z, q-z): ((4, 4, 2), (-1, 0, 0), (5, 4, 2))
F_3 ∪ {P}
  (T)（全数）: True、|Q3|=5、<Q3-Q3> の指数=121、<Q-Q> の指数=121
  Π3 ∩ (q + <Q3-Q3>) の箱 [1,26]^3 の点 146 個のうち Q3 に入らないもの 141 個。最短: [(10, 2, 4), (11, 3, 2), (6, 1, 14)]
  P=(15, 16)（長さ 31）。p_S + <Q-Q> の中の、P より短い ab の点: 3 個。最短: [(12, 4), (13, 8), (14, 12)]
  <Q3-Q3> の中の最短の平面ベクトル: [(-1, -4), (1, 4)]。P に足した点は Q2 に入るか: [False, False]
  (WS) を破る組 (q, z, q-z): ((11, 6, 4), (-1, -4, 0), (12, 10, 4))
F_4 ∪ {P}
  (T)（全数）: True、|Q3|=6、<Q3-Q3> の指数=171、<Q-Q> の指数=171
  Π3 ∩ (q + <Q3-Q3>) の箱 [1,36]^3 の点 276 個のうち Q3 に入らないもの 270 個。最短: [(13, 2, 6), (14, 3, 4), (15, 4, 2)]
  P=(20, 21)（長さ 41）。p_S + <Q-Q> の中の、P より短い ab の点: 5 個。最短: [(15, 1), (16, 5), (17, 9)]
  <Q3-Q3> の中の最短の平面ベクトル: [(-1, -4), (1, 4)]。P に足した点は Q2 に入るか: [False, False]
  (WS) を破る組 (q, z, q-z): ((14, 6, 6), (-1, -4, 0), (15, 10, 6))
F_5 ∪ {P}
  (T)（全数）: True、|Q3|=7、<Q3-Q3> の指数=221、<Q-Q> の指数=221
  Π3 ∩ (q + <Q3-Q3>) の箱 [1,46]^3 の点 447 個のうち Q3 に入らないもの 440 個。最短: [(18, 1, 2), (16, 2, 8), (17, 3, 6)]
  P=(25, 26)（長さ 51）。p_S + <Q-Q> の中の、P より短い ab の点: 6 個。最短: [(19, 2), (20, 6), (21, 10)]
  <Q3-Q3> の中の最短の平面ベクトル: [(-1, -4), (1, 4)]。P に足した点は Q2 に入るか: [False, False]
  (WS) を破る組 (q, z, q-z): ((17, 6, 8), (-1, -4, 0), (18, 10, 8))
==============================================================================
完了
```

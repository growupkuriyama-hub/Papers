# 独立探索報告：`op:fanout-two` — 段付きパリク言語の全体で τ は多項式（局所鳩の巣法）

（2026-11-13、Claude Fable 5.2。依頼「MCFG の fan-out 2 で LG は正確な境界か」への回答。検査スクリプト `check_local_pigeonhole_2026-11-13.py` を同時に提出。`main.tex`・`main` ブランチ・PDF には触れていない。）

**YES/NO の規約**：YES = 「LG が境界のまま（SL は多項式データを持たない）」、NO = 「SL が多項式データを持つ」。

**読んだ資料**：`HANDOFF_CURRENT.md`（全文）、`main.tex` の §2・§3.1・§5（`def:class-cmcf`、`def:reconstruction`、`prop:rare-type`、`cor:distribution-representatives`）・`def:uniform-polydata`・`thm:fanout-one-data`・`lem:power-transfer`・`thm:doubling-no-lift`・`op:fanout-two`、`parked/plan1_boundary_extensions_2026-11-11.tex`（全文）、`reviews/STATUS_sl_fanout2_2026-11-01.md`（全文）、`reviews/fable_three_stages_2026-11-11.md`（全文）、`reviews/fable_content_values_2026-11-10.md`（𝒦 の定義・定理 A の主張・(WS)・命題4.1 の箇所だけ）。
**読んでいない資料**：`astra_fanout2_map_2026-11-10.md`、`claude_fanout2_*_2026-11-09.md` の5本、`claude_binary_case2_2026-11-01.md`、`parked/plan1_small_alphabet_2026-11-11.tex`（二文字の定理の証明本体）、`README.md`。これらの内容は STATUS と依頼文の要約を通してしか知らない。該当箇所にはその旨を書く。

---

## §1 結論の要約

1. `op:fanout-two` は**未解決のまま**。YES も NO も証明していない。
2. **新しい定理（定理1）** [証明済み]：段付きパリク言語のクラス 𝒩（L ∩ Σ⁺ = ND ∩ Ψ⁻¹(Q)、**Q は任意**、段の数 t も一段の文字数も任意）について、L ∈ 𝒩 ∩ C_{f,c_Σ} なら、任意の reduced good 表示（ファンアウト ≤ f、ランク ≤ r）で **全ての型付き非終端の代表長 τ(G, c_Σ) ≤ 2kf(kf+1)·vθ̄·(1 + rv(rvθ̄+1)^k) = O(v^{k+2} θ̄^{k+1})**。特徴標本は ‖G‖ と θ̄ の多項式。
3. これは既存の部分結果を一つの短い証明で覆い、残っていた穴を二つ閉じる。
   - Fable の 𝒦 で残っていた「t ≥ 5、同じ段に二文字以上、三方型」の場合（定理 A・A⁺・B の和集合の外）。
   - 一頂点（パリク飽和）で残っていた命題7.4（(WS) を破る Q）。しかも μ_ab ではなく τ で、f = 1 でも成り立つ。
4. 証明は格子も飽和も使わない。鍵は文法の側の新しい手法「**局所鳩の巣法**」：自由な部分木の葉を DFS 順に並べ、接頭反鎖の詰め物の Parikh 和を色とすると、同じ色の二つの切り口の間の領域は、**その部分木が入っている f 個以下の段の塊の中だけ**の移動として消せる。三段にまたがる移動（Fable の三方型）を一度も必要としない。
5. 三方型の障害そのものは言語の側では本物である（Ex2 で三段移動の結論が偽になることを T1 で再確認）。障害が効かないのは、文法の導出木が「骨格（多項式個）＋ f 個以下の塊に閉じた自由部分木」に分解されるからである。
6. 一般の言語（非可換）への小さな副産物（命題2）[証明済み]：最短の内容 M の語の導出で、入れ子になった自由なファンアウト1の節点の非終端は**共通の生成語を一つも持てない**。ファンアウト2の節点では三つの隙間（左・中・右）が同時に伸びる場合だけが残る。これが非可換な場合の「三方型」である。
7. 課題A：`prop:sl-reduction` は量化・証明とも正しい。補題 M\* は正しい（𝒦 でなく 𝒩 で成り立つ形に一般化できる）。二文字の定理は核の一つ（x⁴ ⇒ 連の再配分）だけを独立に導き直した。**付録の証明本体は読んでおらず、点検していない。**
8. 定理1 は書いたのも点検したのも同じモデルである。スクリプトは証明の手順の照合で、定理の証明ではない。別系統のモデルによる確認が要る。

---

## §2 正確な定理・補題

記法：k = |Σ|、st: Σ → {1,…,t}（段）、Σ_s = st⁻¹(s)。ND = 段が非減少の語の全体。Ψ = Parikh 写像。c = c_Σ（内容型付け）。v = |V|、θ = θ̄_G。位置の集合 R ⊆ pos(x) に対し x∖R は R の位置を消した組。x ≡ y は `def:class-cmcf` の ≡_{L,c}。

**定義（クラス 𝒩_st）**。L ∈ 𝒩_st ⟺ ある Q ⊆ ℕ^Σ があって L ∩ Σ⁺ = {w ∈ ND ∩ Σ⁺ : Ψ(w) ∈ Q}。t = 1 ならパリク飽和な言語の全体。Fable の 𝒦 は 𝒩 の部分クラス（各面が格子の剰余類と正の象限の交わり）。命題7.4 の例（F₄、E₁、F_n）は t = 1 の 𝒩 に入る。

| # | 主張 | ラベル |
|---|---|---|
| 補題1 | 局所移動補題（言語の側、§3.1） | [証明済み] |
| 補題2 | 最小導出の骨格と自由節点（文法の側、§3.2） | [証明済み] |
| 補題3 | DFS 接頭反鎖と色（§3.3） | [証明済み] |
| **定理1** | L ∈ 𝒩_st ∩ C_{f,c}、G が reduced good（ファンアウト ≤ f、ランク ≤ r）なら τ(G,c) ≤ 2kf(kf+1)vθ(1 + rv(rvθ+1)^k) | **[証明済み]** |
| 系1a | 同じ仮定で、𝓑^{≤r}_{f,c} と 𝓑_{f,c} の共通の特徴標本 K で ‖K‖₊ ≤ 2^{kfr}‖G‖(1 + 2θ + rτ) + 1 | [証明済み]（`cor:distribution-representatives` に依存） |
| 系1b | 𝒦 ∩ C_{f,c} は全ての t・k で τ が多項式。N1〜N4 を満たす反例は 𝒦（より広く 𝒩）に存在しない | [証明済み] |
| 系1c | パリク飽和な L ∈ C_{f,c}（f ≥ 1）は τ が多項式。命題7.4 は肯定（v に依存する形で） | [証明済み] |
| 命題2 | 入れ子の自由なファンアウト1節点は共通の生成語を持たない（一般の L ∈ C_{2,c}、§3.5） | [証明済み] |
| 観察3 | ファンアウト2の入れ子節点では三つの隙間が全て伸びる場合だけ命題2 の議論が止まる | [証明済み]（止まることの確認ではなく、止まらない場合の証明） |
| A-1 | `lem:typing-monotone`、`prop:sl-reduction` (i)(ii) | [証明済み]（独立に確認、穴なし） |
| A-2 | 二文字：x⁴ が L の語に現れれば、x の連の間で x を自由に移せる | [証明済み]（`lem:power-transfer` から独立に導出） |
| A-2′ | `thm:two-letter-content` の残り（飽和の二分法、節点の数え上げ、定数） | **未点検** |
| A-3 | 補題 M\*（Fable §2.1） | [証明済み]（確認。𝒩 で成立） |
| A-3′ | 定理 A⁺（定理 A に依存） | 定理 A は未点検。ただし定理1 が A・A⁺・B の τ の主張を別証明で含む（指数は異なる） |
| 候補D1 | 同期した二成分倍増（§4.3）は L(G_n) ∉ C_{2,c} | [反例]（手の証明） |
| — | `op:fanout-two` | [未解決] |

---

## §3 新しい証明

### 3.1 補題1（局所移動補題）

**補題1**。L ∈ 𝒩_st ∩ C_{f,c}。1 ≤ e ≤ f、段 s₁ ≤ ⋯ ≤ s_e、z_κ ∈ ℕ^{Σ_{s_κ}} ∖ {0}、T_κ = supp z_κ、z = Σ z_κ、𝟙 = Σ_κ 𝟙_{T_κ} とする。**P′ ∈ Q、P′ + z ∈ Q、P′ ≥ 2·𝟙** とする。y = (y₁,…,y_d)（d ≤ f）を空でない ND な語の組とし、b₁,…,b_e を y の相異なる塊（b_κ は ある成分の段 s_κ の極大な因子）で、組の中での位置の順に並んでいて、**Ψ(b_κ) ≥ z_κ + 2·𝟙_{T_κ}** を満たすとする。y⁻ を、各 b_κ から Parikh が z_κ の文字を消した組とする。このとき **y ≡ y⁻**。

*証明。* 語 ẑ_κ（Parikh z_κ）、1̂_κ（Parikh 𝟙_{T_κ}）を固定し、t = (ẑ_κ1̂_κ)_κ、t′ = (1̂_κ)_κ と置く。どちらも e 成分で、型は (T_κ)_κ で等しい。

(共通の文脈) c := P′ − 𝟙 ≥ 𝟙。c の文字を段の順に並べ、段 s の部分を「その他の文字、続いて s_κ = s の各 κ について □_κ g_κ」（g_κ ∈ T_κ は c から取った予備の一文字）とした語を F とする。穴の間には g_κ があるので F ∈ ℰ_e。F[t′] は ND で Parikh は P′、F[t] は ND で Parikh は P′ + z。𝒩 の定義から両方 L に入る。(f,c)-代入可能性（arity e ≤ f）から D(t) = D(t′)。

(組への適用) 各 b_κ を「残り・ẑ_κ1̂_κ・g_κ」の順に並べ替えた組を y^π とする（仮定 Ψ(b_κ) ≥ z_κ + 2·𝟙_{T_κ} から可能）。任意の E ∈ ℰ_d について、E[y] と E[y^π] は Parikh が同じで、各成分の段の集合が同じなので ND であることも同値。従って y ≡ y^π（型も同じ）。y′ を y^π の各 ẑ_κ を消した組とする。E[y^π] の因子 ẑ_κ1̂_κ を穴に替えた語 F_E は、穴の間に g_κ があるので ℰ_e に入り、E[y^π] = F_E[t]、E[y′] = F_E[t′]。D(t) = D(t′) から E[y^π] ∈ L ⟺ E[y′] ∈ L。y′ の各成分の内容は y と同じ（T_κ の文字は 1̂_κ に残る）。最後に y′ と y⁻ は成分ごとに Parikh が同じ ND な語なので y′ ≡ y⁻。∎

注：Fable の補題 M\* の「一段ずつ」の場合を、𝒦 を使わず、Q − Q の格子も使わない形で述べ直したものである。使うのは「ND な語の所属は Parikh で決まる」ことだけ。

### 3.2 補題2（最小導出の骨格）

X = A_T を型付き非終端（arity d ≤ f、T = (T₁,…,T_d)）とする。**(x, 𝒯) を、x ∈ L_X とその A からの導出木 𝒯 の対のうち、節点の数が最小のもの**に取る。E_A[x] ∈ L ⊆ ND なので各 x_i は ND。
**印**：各成分 i、各 a ∈ T_i について、x_i の中の a の最初と最後の出現。印の数 ≤ 2kf。節点 ν の生成組が占める位置の集合を pos(ν) と書き、印を含まない節点を**自由**と呼ぶ。自由な節点の子孫は自由。

**補題2**。
- (a) 根から葉への道の上で、自由な節点のラベルは全て異なる。
- (b) 自由でない節点は N_sk := 2kf(kf+1)v 個以下。
- (c) ν が自由なら、その各成分は一つの段の文字だけからなり（x のある成分の一つの塊に入る）、その成分に現れる各文字 a は、同じ塊の中で pos(ν) の外に 2 回以上現れる。

*証明。* 同じラベルの ν > ν′ について、ν の部分木を ν′ の部分木に替えると、節点の少ない A の導出が得られ、その生成組 x° は x から殻 pos(ν)∖pos(ν′) を消したもの（G は ε-free なので成分は空でない）。最小性から x° ∉ L_X、すなわち型が変わる。消しただけなので、ある (i, a) の出現が全て殻に入る。特に a の x_i での最初の出現（印）が殻に入る。
(a) ν が自由なら殻は印を含まないので矛盾。
(b) 一つの印を含む節点は鎖をなす。同じラベルがこの鎖に p 回現れると、p − 1 個の互いに交わらない殻がそれぞれ別の (i, a) の最初の出現を含むので p − 1 ≤ Σ|T_i| ≤ kf。鎖の長さ ≤ (kf+1)v。印は 2kf 個以下。
(c) ν の成分が段 s < s′ の文字 a, b を含むとする。x_i は ND なので a の最後の出現は、この成分の中の a の位置と b の位置の間にあり、成分に入る。これは印なので矛盾。後半：a の最初と最後の出現は印で pos(ν) の外にあり、pos(ν) の中にも a があるので二つは異なる位置。同じ段の塊は成分ごとに一つなので同じ塊にある。∎

### 3.3 補題3（DFS 接頭反鎖と色）

η\* を極大な自由節点（親は自由でない）とし、その部分木の葉（ランク 0 の規則の節点）を DFS 順に λ₁,…,λ_q とする。0 ≤ j ≤ q について、I_j を「葉の子孫が全て {λ₁,…,λ_j} に入る節点」のうち極大なものの集合、U_j := ⋃_{ν∈I_j} pos(ν) とする。各非終端 B に ‖u_B‖₁ ≤ θ の生成組 u_B を固定し（`lem:thickness-equivalence`(ii)）、**色** col(j) := Σ_{ν∈I_j} Ψ(u_{B_ν}) ∈ ℕ^Σ と置く。

**補題3**。
- (a) I_j は反鎖で |I_j| ≤ rv。従って col(j) の各座標は rvθ 以下、色の数は C := (rvθ+1)^k 以下。
- (b) ∅ = U₀ ⊊ U₁ ⊊ ⋯ ⊊ U_q = pos(η\*)、|U_{j+1} ∖ U_j| ≤ vθ。
- (c) **j < j′ で col(j) = col(j′) なら、R := U_{j′} ∖ U_j について x ≡ x∖R。** より強く、補題1 の仮定 (P′, z_κ) が成り立つ。

*証明。* (a) I_j の節点の親は、葉 λ_j と λ_{j+1} の共通の先祖で、これは一本の鎖（長さ ≤ v、補題2(a)）。各々の子は r 個以下。
(b) j で条件を満たす節点は j+1 でも満たす。λ_{j+1} は j+1 で初めて満たし、その位置は U_j に入らない（入れば λ_{j+1} の先祖が j で条件を満たすことになる）。新たに条件を満たす節点は λ_{j+1} と、λ_{j+1} を最後の葉とする先祖で、合わせて v 個以下。U_{j+1}∖U_j はこれらの規則が直接書く終端で、規則ごとに θ 個以下（`lem:thickness-equivalence`(i)）。
(c) 反鎖 I の各節点 ν の部分木を u_{B_ν} の導出に替えた組を x_I とすると x_I ∈ L_A(G)、E_A[x_I] ∈ L(G) ⊆ L。e_A := Ψ(E_A) として
  P := Ψ(E_A[x_{I_j}]) = e_A + Ψ(x) − Ψ(U_j) + col(j) ∈ Q、 P′ := Ψ(E_A[x_{I_{j′}}]) = e_A + Ψ(x) − Ψ(U_{j′}) + col(j′) ∈ Q。
色が等しいので P − P′ = Ψ(R) =: z ≥ 0、z ≠ 0。R ⊆ pos(η\*) で、η\* の成分は fan(B_{η\*}) ≤ f 個以下の塊に入る（補題2(c)）。R と交わる塊を位置の順に b₁,…,b_e（e ≤ f）、z_κ := Ψ(R ∩ b_κ) とすると、z_κ は一つの段の文字のベクトルで、段は非減少（成分の中では ND、成分の間では E_A[x] が ND）。補題2(c) から、T_κ の各文字は b_κ の中で pos(η\*) の外に 2 回以上現れるので、Ψ(b_κ) ≥ z_κ + 2·𝟙_{T_κ}、かつ P′ ≥ Ψ(x) − Ψ(U_{j′}) ≥ 2·𝟙。補題1 を y = x に使う。∎

### 3.4 定理1 の証明

各極大自由節点 η\* で、切り口 0,…,q を左から貪欲に処理する：現在の j に対し、col(j) の最後の出現 j′ を取り、j′ > j なら領域 U_{j′}∖U_j を「消す領域」に加えて j ← j′。その後 j < q なら段 (j, j+1] を残して j ← j+1。残す段は、その左端の色の最後の出現に対応し、以後その色は現れないので、**残す段は C 個以下**。残る位置は補題3(b) から C·vθ 個以下。

消す領域の全体（全ての η\* にわたる）は互いに交わらず、印を含まない。各領域は補題3(c) により補題1 の仮定 (P′, z_κ) を持つ。補題1 は言語の側の主張なので、領域を一つずつ消していった途中の組にも使える（塊の条件 Ψ(b_κ) ≥ z_κ + 2·𝟙_{T_κ} は、他の領域と印が交わらないので保たれる）。従って、全ての領域を消した組 x″ は x ≡ x″ を満たし、x″ ∈ Cl_{L,c}(X)。

長さ：x の位置は「自由でない節点の規則が直接書く終端」（N_sk·θ 以下）と「極大自由節点の pos」（極大自由節点は r·N_sk 個以下）に分かれる。従って

  τ_X ≤ ‖x″‖₁ ≤ N_sk·θ + r·N_sk·C·vθ = 2kf(kf+1)·vθ·(1 + rv(rvθ+1)^k)。 ∎

**系1a**：`cor:distribution-representatives` に代入。|𝖲^♯| = 2^k なので N_typ ≤ 2^{kfr}‖G‖。
**系1b・1c**：𝒦 ⊆ 𝒩、パリク飽和 = 𝒩 の t = 1。
**使った仮定の一覧**：(1) ND な語の所属が Parikh で決まる、(2) arity ≤ fan(G) ≤ f の代入可能性、(3) G が reduced・ε-free・nondeleting・nonpermuting（導出文脈 E_A、殻の削除、成分が因子になること）、(4) `lem:thickness-equivalence`(i)(ii)(iv)。格子の飽和、有限指数、t ≤ 2f、各段一文字のどれも使わない。

**定理 A・A⁺・B との比較**：θ の指数は k²+2k から k+1 に下がる。v の指数は 1 から k+2 に上がる。定理 B の「生成組そのものが短い」（t_typ の上界）は定理1 からは出ない。定理1 は τ（同値な代表）の上界である。

### 3.5 命題2（一般の言語：入れ子の自由節点）

**命題2**。Σ は任意、f ≥ 2、L ∈ C_{f,c}、G は reduced good。x ∈ L_X の導出木で、印を §3.2 と同じに取る。ν > ν′ がともに**ファンアウト1の自由な節点**で、L_{B_ν}(G) ∩ L_{B_{ν′}}(G) ∋ u とする。y_ν = p·y_{ν′}·s と書くと **x ≡ x∖(p, s の位置)**。特に X が開始記号の型付き非終端で x が内容 M の最短の語なら、そのような ν, ν′ は存在しない（ps ≠ ε なので）。

*証明。* ν を含む成分を x_i = α·y_ν·β と書く。ν は自由なので y_ν の各文字の最初の出現は α、最後の出現は β にある。従って alph(p) ⊆ alph(α)、alph(s) ⊆ alph(β)、α, β ≠ ε。E_A[x] で y_ν を u に、または y_{ν′} を u に替えた語はどちらも L に入り、それぞれ ℓ·α·u·β·ρ、ℓ·αp·u·sβ·ρ の形（ℓ, ρ は残りの部分）。組 (α, β) と (αp, sβ) は型が同じで、許容的な文脈 ℓ□u□ρ を共有するので分布が等しい。任意の E について E[x] は (αp, sβ) を y_{ν′} ≠ ε を挟んで含むので、E[x] ∈ L ⟺ E[x∖(p,s)] ∈ L。型は印が残るので同じ。∎

**観察3**。ν, ν′ がファンアウト2で共通の生成組 (u¹, u²) を持つとき、同じ議論は三つの隙間（u¹ の左、u¹ と u² の間、u² の右）の組の比較になる。殻が三つの隙間のうち二つ以下にしか入らなければ、同じ証明で殻は消せる。**三つの隙間が全て伸びる場合だけ arity 3 が要る。** これは 𝒦 の三方型（段 1・3・5）と同じ形で、非可換な場合に下界の候補が満たすべき条件である：文法のファンアウト2は「三つの隙間」を作るが、代入可能性の arity 2 は「二つの因子」しか比べない。

---

## §4 反例・失敗した候補

### 4.1 可換な符号化（パリク飽和・𝒦）で稀な型を長くする設計

倍増木の各段の詰め物に異なる Parikh ベクトル v_e を割り当て、「詰め物の和が重みの和を決める」ようにする設計。定理1 により、どの Q・どの文法でも不可能。直観的な理由：段が一つずつ違う反鎖は 2ⁿ 個あり重みの和が全て異なるが、詰め物の和は [0, nθ]^k に入るので (nθ+1)^k ≥ 2ⁿ、つまり θ ≥ 2^{n/k}/n が要り、μ = 2ⁿ は θ^k の多項式に収まる。定理1 の証明は、この数え上げを一般の木で行ったものである。

### 4.2 𝒦 の三方型の設計（Fable §6.2 の続き）

段 2・4 に外字を置き、段 1・3・5 にまたがる移動 z を N_U に入れて N_M に入れない設計。言語の側では可能（Ex2）。しかし文法の導出木では、葉の大部分は f 個以下の塊に閉じた自由部分木に入り、その中の鳩の巣が二段以下の移動だけで領域を消す。骨格の節点は 2kf(kf+1)v 個しかない。従って「中間の面の比較を全て妨げる」設計を作っても τ は長くならない。Fable が排除できなかった「三つ以上の詰め物の文字が段 2 と 4 にある」設計も同じ理由で失格。

### 4.3 候補 D1：同期した二成分倍増 [反例]

S → (P ξ¹ Q ξ² R)(A_n)、A_i → (ξ₁¹ξ₂¹, ξ₁²ξ₂²)(A_{i−1}, A_{i−1}) | (e_i¹, e_i²)、A₀ → (a, c)。純な語は P a^N Q c^N R（N = 2ⁿ）。狙い：命題2・観察3 の「三つの隙間が全て伸びる」形で、同じ詰め物を固定した M 型の比較が arity 2 に収まらない。

*破れ*（n ≥ 3、詰め物 e_i¹ が a を、e_i² が c を含まない場合）：純な語が a⁴ を含むので、`lem:power-transfer`（i = δ = j = 1）から、(a, a²) と (a², a) は分布が等しい。語 P a^k e_i¹ a^{k′} Q c^k e_i² c^{k′} R（k ≥ 1、k′ ≥ 2。たとえば i = 0、k = 2）に文脈 P a^{k−1}□e_i¹□a^{k′−2}Q⋯ で使うと、P a^{k+1} e_i¹ a^{k′−1} Q c^k e_i² c^{k′} R が強制される。第一成分だけ a が一つ移り、第二成分と同期しないので L(G_n) に入らない。従って L(G_n) ∉ C_{2,c}。
この候補が 11/9 の「二成分の交錯型」と同じものかは、その報告を読んでいないので分からない。同期を外した閉包が小さい文法を持つかは調べきれなかった（§6 の補題β）。

### 4.4 この探索の中で捨てた方針

- 定理1 を「反鎖の和の線形化」（V_I = V_J ⇒ ℓ(I) = ℓ(J)）から線形汎関数の存在に持ち込む方針。接頭反鎖の単調性を使えば汎関数は不要だった。
- 色を塊ごとに分ける版。全体の Parikh 和で足りる（P − P′ = Ψ(R) は詰め物の位置によらない）。
- 補題 S(S2)（自由節点の詰め物が同じ段に入る）。定理1 の証明では不要。

---

## §5 研究上の到達点

`op:fanout-two` の量化「全ての Σ、全ての L ∈ C_{2,c_Σ}、全ての表示 G」のうち：

- **解決した部分**：L を 𝒩（全ての Σ、全ての段の分け方、全ての Q）に限れば、全ての f ≥ 1 で多項式。これは 𝒦 全体、一頂点のクラス全体（命題7.4 を含む）を含む。
- **残る部分**：𝒩 の外の L。すなわち、ND な語の中で Parikh が同じでも所属が変わる言語（非有界な言語、同じ段の中の並び順に依存する言語、一文字が複数の辺を持つ経路言語、一般の正則言語・MCFL）。
- **方向についての情報**：f = 1 では C_{1,c} 全体で指数下界がある（`thm:fanout-one-data`）のに、𝒩 ∩ C_{1,c} は多項式である。つまり指数下界には並び順の非可換性が本質的に要る。f ≥ 2 で二穴の移送が並び順の自由度を削ることと合わせると NO 寄りの状況証拠だが、証明ではない。
- 定理1 は τ の上界なので、`cor:distribution-representatives` を通して特徴標本の上界になる。μ だけの結果ではない。

---

## §6 次に攻めるべき補題

**補題α（経路言語への拡張）**。D を一文字一辺の有向グラフ、L = Path_D(s,t) ∩ Ψ⁻¹(Q)（Q 任意）、L ∈ C_{2,c} とする。「自由な節点の領域の差 z を、同じ Parikh の歩道の並べ替えで 2 個以下の因子に集められる」形の局所移動補題が成り立つか。成り立てば、定理1 の証明がそのまま通り、定理 H・閉包報告・Astra の系3.6(b) のクラスが Q 任意・τ の形で一度に閉じる。偽なら、集められない最小のグラフが新しい障害の型になる。𝒩 は D が自己ループの鎖の場合である。

**補題β（三つの隙間）**。L ∈ C_{2,c}、内容 M の最短の語の最小導出で、共通の生成組を持つ入れ子の自由なファンアウト2節点の列 ν₁ > ⋯ > ν_m が、どの隣り合う対でも三つの隙間全てに空でない殻を持つとする。m ≤ poly(v, θ) か。真なら、命題2 と合わせて「同じ詰め物の入れ子」は反例の資源にならず、反例は全ての段で異なる詰め物を持つ場合に絞られる。偽なら、その族（D1 の同期を外した閉包が第一候補）が `op:fanout-two` の YES の候補になる。

**補題γ（部分可換への拡張）**。L ∈ C_{2,c}、|Σ| = 3、全ての文字 x について x⁴ が L の語に現れる（STATUS の場合 I）とする。このとき語の所属は「骨格と各文字の個数」で決まる（A-2）。自由部分木の接頭反鎖の語 E_A[x_{I_j}] の骨格が、色（Parikh 和）と多項式個の付加情報で決まることを示せば、定理1 の証明が場合 I の τ に通る。真なら三文字・場合 I が τ で閉じ（定理 I は μ_a だけ）、二文字の定理と定理1 の共通の一般化になる。

---

## §7 検証コード

`check_local_pigeonhole_2026-11-13.py`（Python 3、標準ライブラリのみ、乱数不使用、実行時間 約9分。大部分は T1 の全数検査）。

- **T1**：Ex2⁰_m（m = 2, 3）で、箱の中の全ての (P, P′, β) について補題1 の結論を検査。支持が二段以下の z では違反 0。三段の z では結論が偽になる組がある（三方型の障害は言語の側では本物）。
- **T2**：定理1 の証明の手順（印、自由節点、接頭反鎖、色、貪欲削除）を完全二分木の導出の上で実行し、|I_j| の上界、領域の狭義単調性、残す段 ≤ 色の数、E_A[x_I] ∈ L、型の保存、x″ ≡ x（文脈の Parikh ベクトルを [0,4]^k で全数）を assert。(A) 一頂点、(B) 段付き・ファンアウト2。
- **限界**：T2 の言語は可換群の剰余類なので、x″ ≡ x は構成から従う。T2 が確かめるのは木の上の組合せ（反鎖・領域・色）の記帳で、定理の正しさの独立な証拠ではない。面ごとに条件が変わる言語での確認は T1（言語の側）だけである。

出力：

```
========================================================================
T1  局所移動補題（補題1）: Ex2^0_m での照合
========================================================================
  m=2 箱[0,6]^5: 3段 結論不成立=197568, 3段 結論成立=107581292, local(<=2段) 結論成立=98019342
    三段移動の反例 (P, P', beta, beta-z): ((2, 1, 2, 1, 2), (3, 1, 3, 1, 3), (2, 0, 2, 0, 2), (3, 0, 3, 0, 3))
  m=3 箱[0,7]^5: 3段 結論不成立=95452, 3段 結論成立=87844597, local(<=2段) 結論成立=111628521
    三段移動の反例 (P, P', beta, beta-z): ((2, 1, 2, 1, 2), (3, 1, 3, 1, 3), (3, 0, 3, 0, 3), (4, 0, 4, 0, 4))
========================================================================
T2  定理の証明の手順を導出木の上で実行（x'' ≡ x と各段の主張を assert）
========================================================================
  A: 一頂点 n=8 m=5                 |x|=   256 -> |x''|= 146 骨格= 17 極大自由木= 14 max|I_j|= 6 色<= 47 残した段=144 theta=6
  A: 一頂点 n=10 m=7                |x|=  1024 -> |x''|= 128 骨格= 21 極大自由木= 18 max|I_j|= 8 色<= 48 残した段=126 theta=6
  A: 一頂点 n=12 m=11               |x|=  4096 -> |x''|= 686 骨格= 25 極大自由木= 22 max|I_j|=10 色<=373 残した段=684 theta=12
  A: 一頂点 n=13 m=13               |x|=  8192 -> |x''|= 756 骨格= 27 極大自由木= 24 max|I_j|=11 色<=520 残した段=754 theta=14
  B: 段付き f=2 n=8 m=5             |x|=   512 -> |x''|= 212 骨格= 17 極大自由木= 14 max|I_j|= 6 色<= 36 残した段=104 theta=7
  B: 段付き f=2 n=10 m=7            |x|=  2048 -> |x''|= 368 骨格= 21 極大自由木= 18 max|I_j|= 8 色<=109 残した段=182 theta=9
  B: 段付き f=2 n=11 m=9            |x|=  4096 -> |x''|= 388 骨格= 23 極大自由木= 20 max|I_j|= 9 色<=122 残した段=192 theta=10
  B: 段付き f=2 n=12 m=11           |x|=  8192 -> |x''|= 668 骨格= 25 極大自由木= 22 max|I_j|=10 色<=460 残した段=332 theta=12
========================================================================
全ての assert を通過
```

（T2 の表の「色」は部分木ごとの色の数の最大、「残した段」は全部分木の合計。）

### 別のモデルに確認してほしい箇所

1. 補題1：F と F_E が許容的であること（予備の文字 g_κ）、同じ段に二つの穴がある場合。
2. 補題2：最小性の取り方（L_X の全ての生成組と導出にわたる節点数の最小）と、殻が印を含むことの導出。
3. 補題3(c)：P′ ≥ 2·𝟙（同じ文字が二つの成分の塊に現れる場合を含む）と、E_A が開始記号のとき（e_A = 0）。
4. 定理1：領域を順に消すとき、補題1 の塊の条件が保たれること。
5. 𝒦 ⊆ 𝒩 と、命題7.4 の Q が 𝒩（t = 1）に入ること。私は `fable_content_values` の該当箇所しか読んでいない。

### スクリプト全文

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
check_local_pigeonhole_2026-11-13.py   (Python 3, 標準ライブラリのみ、乱数不使用)

報告「段付きパリク言語の多項式上界（局所鳩の巣法）」の検査スクリプト。
無限族についての主張は報告書の中で手で証明してある。ここでの検査は
(T1) 局所移動補題（補題1）の言語側の照合と、三段移動では結論が偽になることの確認
(T2) 定理の証明の手順（印・自由節点・DFS 接頭反鎖・色・貪欲削除）を具体的な
     文法の導出木の上で実行し、各段の主張（領域の狭義単調性、反鎖の大きさ、
     残る段の数 <= 色の数、W_I in L、最終的な組 x'' ≡ x）を確かめる
だけを目的とする。
"""
import itertools
from collections import Counter

# ---------------------------------------------------------------- T1
def ex2(m):
    """Fable の Ex2^0_m。段 a<b<c<d<e（各段一文字）。Parikh ベクトル (a,b,c,d,e)。"""
    def member(v):
        a, b, c, d, e = v
        if min(a, c, e) < 1:
            return False
        if b == 0 and d == 0:
            return a % m == 0 and c % m == 0 and e % m == 0
        if b >= 1 and d >= 1:
            return (a - c) % m == 0 and (c - e) % m == 0
        return False
    return member

def t1():
    print('=' * 72)
    print('T1  局所移動補題（補題1）: Ex2^0_m での照合')
    print('=' * 72)
    for m, B in ((2, 6), (3, 7)):
        mem = ex2(m)
        box = [v for v in itertools.product(range(B + 1), repeat=5) if mem(v)]
        stats = Counter()
        cert = None
        for P in box:
            for P2 in box:
                z = tuple(x - y for x, y in zip(P, P2))
                T = [i for i in range(5) if z[i] != 0]
                if not T or len(T) > 3:
                    continue
                if any(min(P[i], P2[i]) < 2 for i in T):
                    continue
                kind = 'local(<=2段)' if len(T) <= 2 else '3段'
                for beta in box:
                    if all(beta[i] >= max(z[i], 0) + 2 for i in T):
                        tgt = tuple(x - y for x, y in zip(beta, z))
                        ok = mem(tgt)
                        stats[(kind, ok)] += 1
                        if kind == '3段' and not ok and cert is None:
                            cert = (P, P2, beta, tgt)
        print('  m=%d 箱[0,%d]^5: ' % (m, B) +
              ', '.join('%s 結論%s=%d' % (k, '成立' if ok else '不成立', n)
                        for (k, ok), n in sorted(stats.items())))
        assert stats[('local(<=2段)', False)] == 0
        print("    三段移動の反例 (P, P', beta, beta-z):", cert)

# ---------------------------------------------------------------- T2
class Node:
    __slots__ = ('label', 'kids', 'yld', 'lo', 'hi')
    def __init__(self, label, kids):
        self.label, self.kids = label, kids

def build(n, fan, letters_leaf, ids):
    """A_n の完全二分木。葉 A_0 -> letters_leaf（成分ごとに一文字）。"""
    if n == 0:
        nd = Node(0, [])
        comp = []
        for ch in letters_leaf:
            ids.append(ch)
            comp.append([len(ids) - 1])
        nd.yld = tuple(comp)
        return nd
    l = build(n - 1, fan, letters_leaf, ids)
    r = build(n - 1, fan, letters_leaf, ids)
    nd = Node(n, [l, r])
    nd.yld = tuple(l.yld[c] + r.yld[c] for c in range(fan))
    return nd

def number_leaves(root):
    cnt = [0]
    def rec(nd):
        if not nd.kids:
            cnt[0] += 1
            nd.lo = nd.hi = cnt[0]
        else:
            for k in nd.kids:
                rec(k)
            nd.lo, nd.hi = nd.kids[0].lo, nd.kids[-1].hi
    rec(root)
    return cnt[0]

def antichain(root, j):
    """I_j: 葉が全て {1..j} に入る極大な節点の反鎖。"""
    out = []
    def rec(nd):
        if nd.hi <= j:
            out.append(nd)
        elif nd.lo <= j:
            for k in nd.kids:
                rec(k)
    rec(root)
    return out

def evaluate(nd, repl, esc, ids, fan):
    """nd の生成組。repl に入る節点は詰め物 esc[label] に取り替える。"""
    if id(nd) in repl:
        return esc[nd.label]
    if not nd.kids:
        return tuple(''.join(ids[i] for i in comp) for comp in nd.yld)
    parts = [evaluate(k, repl, esc, ids, fan) for k in nd.kids]
    return tuple(''.join(p[c] for p in parts) for c in range(fan))

def run(name, n, fan, leaf, esc, ctx, member, letters, rank=2):
    ids = []
    root = build(n, fan, leaf, ids)
    x = tuple(''.join(ids[i] for i in comp) for comp in root.yld)
    assert member(ctx(x)), 'x 自体が L に入らない'
    theta = max(sum(len(c) for c in e) for e in esc.values())
    marks = set()                      # 各成分・各文字の最初と最後の出現
    for comp in root.yld:
        for ch in set(ids[i] for i in comp):
            occ = [i for i in comp if ids[i] == ch]
            marks.add(occ[0]); marks.add(occ[-1])
    def free(nd):
        return not any(i in marks for comp in nd.yld for i in comp)
    maxfree, skeleton = [], []
    def rec(nd):
        if free(nd):
            maxfree.append(nd)
        else:
            skeleton.append(nd)
            for k in nd.kids:
                rec(k)
    rec(root)
    deleted = set()
    max_colors = max_I = kept_steps = checked = 0
    for eta in maxfree:
        q = number_leaves(eta)
        depth = eta.label + 1
        cuts, sizes = [], []
        for j in range(q + 1):
            I = antichain(eta, j)
            max_I = max(max_I, len(I))
            assert len(I) <= (rank - 1) * depth + 1
            sizes.append(sum(len(comp) for nd in I for comp in nd.yld))
            V = Counter()
            for nd in I:
                for comp in esc[nd.label]:
                    V.update(comp)
            cuts.append(tuple(V[ch] for ch in letters))
        assert all(sizes[j] < sizes[j + 1] for j in range(q))   # 領域の狭義単調性
        colors = set(cuts)
        max_colors = max(max_colors, len(colors))
        last = {}
        for j, col in enumerate(cuts):
            last[col] = j
        j = steps = 0
        while j < q:
            j2 = last[cuts[j]]
            if j2 > j:
                U1 = set(i for nd in antichain(eta, j) for comp in nd.yld for i in comp)
                U2 = set(i for nd in antichain(eta, j2) for comp in nd.yld for i in comp)
                assert U1 < U2
                if checked < 60:       # 照合: W_I, W_J in L
                    for jj in (j, j2):
                        repl = set(id(nd) for nd in antichain(eta, jj))
                        assert member(ctx(evaluate(root, repl, esc, ids, fan))), (name, jj)
                    checked += 1
                deleted |= (U2 - U1)
                j = j2
            if j < q:
                steps += 1             # 段 j -> j+1 は残す
                j += 1
        assert steps <= len(colors)
        kept_steps += steps
    x2 = tuple(''.join(ids[i] for i in comp if i not in deleted) for comp in root.yld)
    assert all(x2) and tuple(set(c) for c in x2) == tuple(set(c) for c in x)   # 型の保存
    bad = 0                            # x'' ≡ x の照合（文脈の Parikh ベクトルを箱で全数）
    for e in itertools.product(range(5), repeat=len(letters)):
        pad = ''.join(ch * k for ch, k in zip(letters, e))
        if member(ctx(x) + pad) != member(ctx(x2) + pad):
            bad += 1
    assert bad == 0
    print("  %-30s |x|=%6d -> |x''|=%4d 骨格=%3d 極大自由木=%3d max|I_j|=%2d 色<=%3d 残した段=%3d theta=%d"
          % (name, sum(map(len, x)), sum(map(len, x2)), len(skeleton), len(maxfree),
             max_I, max_colors, kept_steps, theta))

def t2():
    print('=' * 72)
    print("T2  定理の証明の手順を導出木の上で実行（x'' ≡ x と各段の主張を assert）")
    print('=' * 72)
    # (A) 一頂点（パリク飽和）: L = {w in {a,c}+ : #a + 3#c ≡ 2^n (mod m)}
    #     S->A_n, A_i->A_{i-1}A_{i-1} | u_i, A_0->a。u_i は c を含む短い語。
    for n, m in ((8, 5), (10, 7), (12, 11), (13, 13)):
        esc = {}
        for i in range(n + 1):
            c = 1 + (i % 3)
            esc[i] = ('a' * ((pow(2, i, m) - 3 * c) % m) + 'c' * c,)
        tgt = pow(2, n, m)
        member = lambda w, m=m, tgt=tgt: len(w) > 0 and (w.count('a') + 3 * w.count('c')) % m == tgt
        run('A: 一頂点 n=%d m=%d' % (n, m), n, 1, ('a',), esc, lambda t: t[0], member, 'ac')
    # (B) 段付き・ファンアウト2: 段1={a,p} < 段2={b} < 段3={c,q}
    #     L = ND ∩ {b を含み #a + #c + 2#p + 5#q ≡ 2^{n+1} (mod m)}
    #     S->(xi^1 b xi^2)(A_n), A_i->(xx',yy')(A_{i-1},A_{i-1}) | (a^e p, q^beta), A_0->(a,c)
    stage = {'a': 1, 'p': 1, 'b': 2, 'c': 3, 'q': 3}
    for n, m in ((8, 5), (10, 7), (11, 9), (12, 11)):
        esc = {}
        for i in range(n + 1):
            beta = 1 + (i % 2)
            esc[i] = ('a' * ((pow(2, i + 1, m) - 2 - 5 * beta) % m) + 'p', 'q' * beta)
        tgt = pow(2, n + 1, m)
        def member(w, m=m, tgt=tgt):
            w = ''.join(sorted(w, key=lambda ch: stage[ch]))   # 詰め物は段の順に整列して置く
            if 'b' not in w:
                return False
            return (w.count('a') + w.count('c') + 2 * w.count('p') + 5 * w.count('q')) % m == tgt
        run('B: 段付き f=2 n=%d m=%d' % (n, m), n, 2, ('a', 'c'), esc,
            lambda t: t[0] + 'b' + t[1], member, 'apbcq')

if __name__ == '__main__':
    t1()
    t2()
    print('=' * 72)
    print('全ての assert を通過')
```

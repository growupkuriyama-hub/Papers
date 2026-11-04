# 場合 I の独立検証と跨ぎの場合の解決：二穴の殻の入れ子による線形化（三文字内容型付け・系列の十三本目、Claude 版）

**研究日**：2026-11-04
**対象**：栗山貴之、論文 #2、`op:fanout-two` の三文字の核（純粋 a 語の問い Q）
**依頼文**：`reviews/prompt_chatgpt_straddle_2026-11-04.md`（ChatGPT 宛ての依頼文を、別のスレッドの Claude が受けた）。依頼のファイル名は `chatgpt_straddle_2026-11-04.md` だが、書き手が Claude なので系列の慣例に合わせて `claude_straddle_2026-11-04.md` とした。
**資料**：公開リポジトリ `growupkuriyama-hub/Papers` を取得（commit `8a055ae`、2026-11-04 16:40 JST）。`main.tex`（blob `b72cd2ed`）、`claude_cross_core_2026-11-04.md`（`e7876722`）、`claude_f_branching_2026-11-04.md`（`8877e715`）、`chatgpt_weighted_codes_2026-11-02.md`（`5b624c55`）、`chatgpt_a_spectrum_2026-11-03.md`（`f26e671a`）、`chatgpt_nested_bc_chain_2026-11-04.md`（`6ad25a47`）を直接読んだ。
**立場**：独立査読の前の研究ノートである。直前の二本と同じモデル（Claude）が書いているので、§2 の検証は反例を探す立場で行ったが、**同じモデルによる検証であることに変わりはない**。原稿に入れる前に、別の読み手による検証が要る。

**要点。** 第十二報の主張は全て独立に確認できた（誤りは見つからなかった）。そのうえで、**場合 I（b⁴ と c⁴ が現れる）の Q を、ファンアウト ≤ 2 の全ての表示で、条件 (S1) なしに肯定的に解いた**（定理 I）。鍵は、跨ぎの場合でも「同じラベルの二つの内部の出現」から二穴の型板（a A a A a B a B a の形の語）が必ず得られ、殻 (A, B) を任意の深さに入れ子にできること（補題 N）、そして入れ子の核が「殻の偶奇の細類」と Σn' だけで決まること（補題 Q）である。場合 II・III は未解決のまま。

---

## 0. 主張ごとの判定

| 主張 | 判定 | 根拠・限定 |
|---|---|---|
| 補題E（詰め物付きの交換） | **独立に確認** | §2.1 |
| 補題F（a の移送）の「再配分」の段 | **独立に確認** | §2.2。補題2.1 を x=a、z=u として使うだけ。さらに、u の端が a でないこと・連の極大性・別の証拠語は**いずれも要らない**（今の語自身が証拠になる。§3.1 の補題 F′） |
| 系F・系2.3 | **独立に確認** | §2.3。a の予算は「a の個数 ≥ a の連の数 + 1」で足りる |
| 補題V と、Claude の補足（差し替え元の節点 z_i の k−ℓ ≥ θ+2 は自動的） | **独立に確認** | §2.4。隣り合う範囲の分離も確認 |
| 命題4.1（鎖の帰納法） | **独立に確認** | §2.5 |
| 補題P（個数の違う多重集合の比較、定数項なし） | **独立に確認** | §2.6。n' ∈ [2, θ] |
| 定理D（(S1) の下、D=14） | **独立に確認** | §2.7。補題3.1・3.2 は「区分ごとに整数点の線形関数」しか使わず、偶奇類の区分にそのまま使える |
| 系D（ファンアウト1） | **独立に確認** | §2.8。N_bc は (4.2) の定義（重い両文字型節点の数）で ≤ 3v |
| 定理C | **独立に確認。さらに (S_{M_C}) は (S1) に弱められる** | §2.9。鎖を作ってから分離すればよい |
| 報告 §5.5 の観察（入れ子の対で L₁ a^p F_{X₂} a^q R₁、F_{X₂} は任意の F_Y に替えられる） | **独立に確認** | §5 |
| **補題 F′（自己融合）・系 C（収縮）**：a⁴ が現れる L ∈ C_{2,c} では、a で始まり a の個数が「連の数 + 1」以上の受理語の a を含まない部分は、全て一つの塊にまとめられる | **証明済み** | §3.1。場合 I–III のどれにも依らない |
| **補題E₂（二穴の交換）**：同じ成分ごとの内容を持つ二穴の殻どうしの交換 | **証明済み** | §3.2。場合によらない |
| **補題T（型板）**：内部の出現を二つ持つ低いラベル X は、(i) 二塊の語 a⁺F_X a⁺F_X a⁺ を与えるか、(ii) 二穴の型板 a⁺A a⁺A a⁺B a⁺B a⁺ を与える | **証明済み** | §3.3。範囲が交わる二出現の成分の順は必ず [1][1][2][2]（§8 Part A で全数確認） |
| **補題N（入れ子）**：型板のある型 τ の殻を、任意の塊のまわりに任意の深さで入れ子にできる | **証明済み** | §3.4。場合によらない |
| **補題Q**（場合 I、殻の細類での線形性、定数項なし） | **証明済み** | §4.2。細類は 34 個 |
| **定理 I**：場合 I、ファンアウト ≤ 2、ランク ≤ r、**追加の条件なし**で μ_a ≤ max{4θ+12, K_I^{313}R^{312}θ} | **証明済み** | §4。K_I = (2v+E_I)(2r+1)、E_I = v(50θ³+θ+23)、R = θ+2v+2。定理D・系D を含む（指数は悪い） |
| 跨ぐ節点が poly(v,θ) 個以下なら (4.2) で片付く | **自明に成り立つが目的には足りない** | §5。定理 I で不要になった |
| 「二つの完全な塊が離れて並ぶ語」を跨ぎの場合に一般に作ること | **確認できず（不要）** | §5。作れない場合（分岐 (S)）は殻の入れ子で代わりを果たす |
| 場合 II・III | **未解決** | §6。自己融合・入れ子・鎖は場合によらず成り立つ。小さな帰結（場合 II で、関係のある殻の片側は一つの連であり得ない）は証明済み |
| 反例族 | **未構成** | §7。反例は場合 II か III でなければならない（定理 I） |
| 有限の検査 | **有限の対象についての完全な判定／機械的に検査した証明書** | §8。Part D は、非線形な殻の損失から a^{39}（k=40）を導く 76 段の証明書で、二つの規則だけを使う独立の検査器で全段を再検査した |
| 新しい結果（補題 F′、E₂、T、N、Q、定理 I）の文献上の新規性 | **未確認** | §9 |

**報告のスクリプトについて。** この環境では、リポジトリから取ったスクリプトの実行が許可されなかった。そこで第十二報のスクリプトは**再実行していない**。代わりに、検証と新しい主張に要る点を、独自に書いたスクリプト（§8）で確かめた。

---

## 1. 記号と引用の確認

Σ={a,b,c}、内容型付け c（語の型はその文字の集合、組の型は成分ごとの型）、L ∈ C_{2,c}。原稿 `def:tuple-substitutable` により、arity d=1,2 で、型が等しく分布が交わる組は分布が等しい。arity 2 の文脈 v₀□₁v₁□₂v₂ は v₁ ≠ ε のものだけ（`def:tuple-occurrence` の前の定義）。G は L∩Σ⁺ の reduced good な表示で、ファンアウト ≤ 2、ランク ≤ r。v = |V|、θ = θ̄_G、k = μ_a(L) ≥ 5。T は a^k の節点数最小の導出で、一様（同じラベルの部分木は全て同じ、同じラベルの出現は反鎖、根から葉への道は v 節点以下。第十報 §2 で検証済み、今回も最小性の二つの段を読み直した）。

両文字型ラベル X に短い代表 ρ_X（総長 ≤ θ、`lem:thickness-equivalence` (ii)）を固定し、d_X = ℓ_X − |ρ_X|_a ≥ 3、β_X = |ρ_X|_b、γ_X = |ρ_X|_c。**範囲**・**内部**の定義は第十二報 §1 のとおり。

**引用して、今回改めて確かめたもの。**

- **補題2.1**（weighted_codes）：x⁴ が L の語に現れれば、任意の u, v と空でない z について u·x z xx·v ∈ L ⇔ u·xx z x·v ∈ L。証明：p x⁴ q ∈ L に対し、組 (x, xx) と (xx, x) は型 ({x},{x}) が等しく、許容文脈 p□₁x□₂q がどちらも p x⁴ q に写す。z が x を含むか、二つの x の連が隣の連かどうかは関係しない。**系2.2**（総数を保った x の連の長さの自由な再配分。連は全て正の長さのまま）も確認した。a については a^k（k ≥ 5）から a⁴ が現れる。
- **定理S**（a_spectrum）の使う部分：同じ a 骨格（σ_a が等しい）の二語の a の個数の差 δ は、0 < δ < k にならない。余りの a を一つの連に集めて Ua V と Ua^{1+δ}V とし、文脈 U□V で D(a) = D(a^{1+δ})、a^k の中の a^{1+δ} を a に替えて a^{k−δ} ∈ L となるからである。
- **命題1.1 (R)**（第十一報）：σ_X(w) = σ_X(w')、b, c の個数が等しく、a の個数がともに (0, k) にあれば、a の個数は等しい。場合 I（X = {b,c}）では、b と c の連を系2.2 で w の長さにそろえてから定理S を使う。段ごとに追い直した。
- 第十報 §3.1–3.2：非飽和の色の一色型は全体で 18v 以下、出現 ≤ θ の一色型は vθ 以下、飽和の色の頻出の一色型は ℓ = p + α_x q（p ≤ θ、1 ≤ q ≤ θ）。いずれも両文字型の節点を差し替えないので、両文字型の節点の多さに影響されないことを確かめた。
- 第十一報の**補題3.1・3.2**：例外の節点が全体で E 個以下で、例外でない重い節点のラベルに「区分 π の線形形式 ⟨φ_π, p⟩（p は [0,θ]^{dim π} の整数点）」の値があり ℓ がその値の窓 [D, D+θ] に入るなら、K = (2v+E)(2r+1)、R = θ+2v+2、D = Σ dim π について k ≤ K^{3D+1}R^{3D}θ。補題3.1 の芯の議論（同じ深さの芯の節点は ≤ 2 個、深さ ≤ v）と、補題3.2 の部分和の単射性（(R'+1)^N ≤ (NR'θ+1)^D から N < 3D）を読み直した。使っているのは「区分ごとに整数点の線形関数で、定数項なし（必要なら座標として入れる）」ことだけである。
- 第十報の **(4.2)**：k ≤ 19(r+1)³v³θ³(θ+N_bc+20)³。N_bc は重い両文字型節点の数（第十報 §1）。証明の最後で r ≥ 2 を使って 1+rE ≤ 2rvq としているが、r = 1 でも 1+E ≤ 2vq なので同じ式が成り立つ。

---

## 2. 第十二報の独立の検証

### 2.1 補題E

文脈 □·a^{k−d_Q−1} は a^{1+d_Q−d_P}P を a の個数 (1+d_Q−d_P) + (k−d_Q−1) = k−d_P の語（左の連 ≥ 1、右の連 ≥ 2）に、aQ を a の個数 k−d_Q の語に写す。SB により両方とも L に入る。型は両方 {a,b,c}。arity 1 の代入可能性で分布は等しい。**独立に確認。** 使っているのは「P と Q の内容が等しい」ことだけなので、b と c の両方を含む塊どうしに限れば、そのまま正しい。

### 2.2 補題F の「再配分」の段

w = P' a^i u a^t Q'（i ≥ 2、t ≥ 1）から P' a^{i−1} u a^{t+1} Q' を得る段は、補題2.1 を x = a、z = u（空でない）、左の部分を P'a^{i−2}、右の部分を a^{t−1}Q' として、u·xx z x·v → u·x z xx·v と読むだけである。u が b と c を含むかどうか、a^i と a^t が極大かどうかは関係しない。**独立に確認。**

反例を探す立場で見た点：(1) u が a で始まる・終わる場合も補題2.1 は使えるので、補題F の仮定「u の端は a でない」は不要。(2) 補題F の結論 D(a²u) = D(aua) の「証拠の語」は、**融合したい語そのもの**でよい（§3.1 の補題 F′）。第十二報が証拠を別に用意している箇所（系2.3 の帰納法、補題V、命題4.1）は、どれも今の語で代用でき、議論が短くなる。誤りではない。

### 2.3 系F・系2.3

融合（P'' a^p u a v Q'' → P'' a^{p+1} u v Q''）は、文脈 P''a^{p−1}□vQ'' が aua を受理し、D(a²u) = D(aua) から a²u も受理するというもの。分離はその逆向きで、こちらは D(a²u) = D(aua) の証拠（a^{≥2} u a^{≥1} を含む語）が別に要る。**独立に確認。**

系2.3 の帰納法：W_x（内部の出現 x を ρ_X に替えた語）は a で始まり a で終わり、ファンアウト2の二成分の間にも a がある（第十一報の補題1.3）。各段で「左の連 ≥ 2、間の連 = 1」に再配分してから融合する。必要なのは a の個数（k−d_X）が a の連の数 + 1 以上であることで、連の数 ≤ θ+1 なので k − ℓ_X ≥ θ+2 で足りる。融合の途中で b の連どうし・c の連どうしが合わさることがあるが、F_X は語として定義されているので問題ない（n_X は融合後の F_X で数える）。**独立に確認。**

### 2.4 補題V と Claude の補足

z_i を全て ρ に替えた語は、範囲が互いに素（したがって祖先関係もない）なので同時に差し替えられ、L に入る。各 z_i の範囲の中での融合は §2.3 と同じ。範囲が隣り合い、ρ_{z_i} の末尾と ρ_{z_{i+1}} の先頭がともに a でないと、二つの塊が直接つながる。このときは左の塊の直前の連を 2 以上に再配分し、分離する。分離の証拠（a^{≥2} u a^{≥1}）は、ラベル Z_i の系2.3 の途中の語にある。ファンアウト1で a を含まない ρ が両側と隣り合う場合も、左から順に分離すれば足りる。交換の順序（増える交換を先に）で、途中の a の個数は常に最終の値 k−Σd_{Y_i} ≥ 2n+2 以上になる。**独立に確認。**

**補足（差し替え元の節点 z_i にも k−ℓ_{z_i} ≥ θ+2 が要る）。** 補足のとおり要る。また、自動的に成り立つ：n ≥ 2 なら、範囲が互いに素な内部の重い節点 z₁, z₂ について ℓ₁+ℓ₂ ≤ k−2（最初と最後の a はどちらにも属さない）、ℓ₂ > θ なので k−ℓ₁ ≥ θ+3。**独立に確認。**

### 2.5 命題4.1

二塊の語 a^p F_X a F_Y a^q から融合で a^{p+1}F_X F_Y a^q（a の個数は不変、損失 d_X+d_Y）。鎖の帰納法では、既に SB(C, Σd) を持つ鎖 C と F_{X_{t+1}} を、補題V の二塊の語の二つの塊と補題E で交換して離れた二塊の語を作り、融合する。補題E は P, Q の内容が等しいことと SB しか使わないので、C（a を含まず b, c を含む）にも使える。予算は Σd ≤ k/2 から足りる。**独立に確認。**

### 2.6 補題P（個数の違う多重集合）

同じ偶奇類（先頭の文字 f、連の数の偶奇）の語の連結は、偶数類では接合で合わさらず連の数が足し算、奇数類では毎回一つ合わさる。よって t 個の鎖の連の数は Σn（偶数類）、Σn − (t−1) = Σn' + 1（奇数類）で、**t によらない**。先頭の文字も f。したがって Σn', Σβ, Σγ が等しい二つの多重集合の鎖は、個数が違っても σ(aCa) が等しく、b, c の個数が等しく、a の個数は (0,k) にある。(R) により Σd が等しい。回路の関係 Σc_X v_X = 0 の正の部分と負の部分は、ベクトルの成分が正なのでどちらも空でなく、個数が違ってよい。よって d は行列 (v_X) の行空間に入り、定数項はない。

点の範囲：n_X ≥ 2（b と c を含む）なので n' ∈ [2, θ]、β, γ ∈ [1, θ]。回路の係数は 3×3 小行列式で ≤ 6θ³、一つの回路は ≤ 4 本なので片側 ≤ 24θ³ 個。**独立に確認。**

### 2.7 定理D

例外：一色型 18v + vθ、内部でないラベルの節点 ≤ 2v（内部でないラベルの出現は、最初の文字を含むものと最後の文字を含むものが反鎖の中に一つずつ）、高い（ℓ > k/(2N_c)）両文字型の節点（一つの深さで出力が互いに素なので < 2N_c 個、計 ≤ 2N_c v = 48θ³v）。合計 E_D = v(48θ³+θ+20) で一致。群：低い内部の両文字型ラベルは、値 d_X、窓 [d_X, d_X+θ]（ℓ_X = d_X + |ρ_X|_a）。区分は四つの偶奇類（各 3 次元）と一色型二つ（各 1 次元）で D = 14、3D+1 = 43、3D = 42。**独立に確認。**

### 2.8 系D

ファンアウト1では範囲 = 出力なので、範囲が交わる二節点は祖先関係にある。(S1) が成り立たなければ内部の両文字型節点は全て互いに祖先関係で比べられ、一本の根からの道に乗る（≤ v 個）。内部でない両文字型節点は各深さ ≤ 2 個で ≤ 2v 個。重い両文字型節点の数 N_bc ≤ 3v で、(4.2) に入れて (θ+3v+20)³。**独立に確認。**

### 2.9 定理C（注意：(S_{M_C}) は (S1) に弱められる）

定理C の (a)–(c) を読み直した（(c) の、各類の個数と b, c の総数が両側で等しいことの計算を含む）。**独立に確認。** さらに、条件 (S_{M_C}) は (S1) で足りる：(S1) の下で命題4.1 により鎖 C = F_{Y_1}⋯F_{Y_n} が SB を持つ。a^s C a^t（s ≥ 2）で F_{Y_1} の直後に分離で a を入れる（証拠は SB(F_{Y_1}) の語 a²F_{Y_1}a^{…}）。これを順に繰り返すと、補題V の仮想の配置語が n 個の節点なしに得られる。定理C は定理 I に含まれるので、この改良は記録だけにとどめる。

### 2.10 反例を探した点（見つからなかった）

- ρ_X の成分が純粋な a の場合（F_X は他方の成分だけから成る）、ρ_X が a で始まる・終わる場合（周りの連に合わさるだけ）。
- 融合で b の連や c の連が合わさり、n_X が因子の連の数の和より小さくなる場合（定義が F_X に基づくので整合）。
- 差し替え元の節点が大きく（ℓ が k/2 に近い）、予算が足りない場合（§2.4 の補足で、n ≥ 2 なら k−ℓ ≥ θ+3）。
- 補題P で、鎖の長さが違う比較が (R) の仮定（σ の一致）を壊す場合（§2.6 で連の数が t によらないことを確認）。

---

## 3. 新しい道具（場合 I–III のどれにも依らない）

以下 §3 では、L ∈ C_{2,c} で a⁴ がある語の因子として現れることだけを仮定する（a^k、k ≥ 5 から従う）。

### 3.1 自己融合と収縮

**補題 F′（自己融合）。** W = P a^p u a^q v Q ∈ L、u は空でない語、a^p と a^q は a の連（p, q ≥ 1）で、v は a で始まらない（空でもよい）。W の a の個数が W の a の極大連の数 + 1 以上なら、W の a の連の長さを適当に配り直したうえで a^q を取り除いた語 P a^{p'} u v Q（他の連の長さも配り直してよい）が L に入る。

**証明。** 系2.2 で、a^p を 2 以上、a^q を 1 にする（連の数 + 1 以上の a があるので可能）。この語 W₁ = P₁ a^{p₁} u a v Q₁ は、補題F の証拠の形 a^{p₁}ua^1（p₁ ≥ 2）を含む。補題F の証明どおり、文脈 E₀ = P₁a^{p₁−2}□ a v Q₁ は a²u（W₁ を与える）と aua（W₁ の a を一つ右へ移した語。補題2.1 で L に入る）を受理し、型は {a}∪c(u) で等しいので D(a²u) = D(aua)。文脈 P₁a^{p₁−1}□vQ₁ は aua を受理する（W₁ を与える）ので a²u も受理し、P₁ a^{p₁+1} u v Q₁ ∈ L。□

**系 C（収縮）。** w ∈ L が a で始まり a で終わり、a の個数 N が w の a の極大連の数 + 1 以上とする。w の a を含まない極大な因子を左から順につないだ語を F(w) とすると、全ての s, t ≥ 1、s+t = N について a^s F(w) a^t ∈ L。

**証明。** 補題 F′ を、最初の因子と次の因子の間の連に繰り返し使う。各段で連の数は一つ減るので、「a の個数 ≥ 連の数 + 1」は保たれる。最後に二つの連を系2.2 で配り直す。□

系 C は、第十二報の系2.3・補題V の融合の部分と、命題4.1 の融合の部分を一つにしたものである。**分離（a を入れる向き）は別の証拠が要る**ことに注意する。

### 3.2 二穴の単一塊と二穴の交換

a を含まない空でない語 A, B の組 S = (A, B) を**殻**と呼ぶ。殻が性質 SB₂(S, e) を持つとは、全ての s, g, t ≥ 1、s+g+t = k−e について a^s A a^g B a^t ∈ L であること。殻の**型**は τ(S) = (c(A), c(B))。

**補題 SB₂。** X を両文字型ラベル、x をその内部の出現でファンアウト2、ρ_X の二成分がどちらも a 以外の文字を含むとする（X を**両側型**と呼ぶ）。A_X、B_X を ρ_X の第一・第二成分の a を含まない因子をそれぞれつないだ語とする。k − ℓ_X ≥ θ+2 なら SB₂((A_X, B_X), d_X)。

**証明。** W_x = a^{…} ρ¹ a^{gap} ρ² a^{…} ∈ L（間の a の連は空でない）。第一成分の因子どうし、第二成分の因子どうしの間の連だけに補題 F′ を使い、間の連 a^{gap} は残す。a^s A_X a^g B_X a^t の形になり、系2.2 で三つの連を配り直す。□

二成分の一方が純粋な a のラベルを**片側型**と呼ぶ。片側型では、系2.3 の F_X が a を含まない部分の全てである。

**補題 E₂（二穴の交換）。** 殻 S = (A, B)、S' = (A', B') が SB₂(S, e)、SB₂(S', e') を持ち、τ(S) = τ(S')、e ≤ e' ≤ k−4 とする。このとき二穴の分布について

D^{(2)}(a^{1+e'−e}A, B) = D^{(2)}(aA', B')。

**証明。** g, t ≥ 1、g+t = k−e'−1 の文脈 □₁ a^g □₂ a^t は許容的（中央の a^g は空でない）。(a^{1+e'−e}A, B) を a の個数 (1+e'−e)+g+t = k−e の語に、(aA', B') を a の個数 k−e' の語に写し、SB₂ によりどちらも L に入る。型は成分ごとに ({a}∪c(A), c(B)) = ({a}∪c(A'), c(B'))。arity 2 の代入可能性による。□

### 3.3 型板

**補題 T（型板）。** X を両文字型ラベルとし、T の中に X の内部の出現が二つ x, x' あるとする。k − 2ℓ_X ≥ 2θ+4 とする。

- (i) x と x' の範囲が互いに素なら、ある s₀, s₁, s₂ ≥ 1 について a^{s₀} F_X a^{s₁} F_X a^{s₂} ∈ L（**二塊の語**）。
- (ii) 範囲が交わり、X が片側型なら、同じく二塊の語がある。
- (iii) 範囲が交わり、X が両側型なら、ある y₀, …, y₄ ≥ 1 について
  a^{y₀} A_X a^{y₁} A_X a^{y₂} B_X a^{y₃} B_X a^{y₄} ∈ L（**型板**、a の個数 k−2d_X）。

**証明。** 同じラベルの出現は反鎖なので、x と x' を同時に ρ_X に替えた語 W ∈ L がある。W は a で始まり a で終わり、a の個数 k−2d_X ≥ k−2ℓ_X ≥ 2θ+4 は連の数（≤ 2θ+1）+ 1 以上である。

(i) 範囲が互いに素なら、各範囲の中の因子を補題 F′ でまとめる。二つの範囲が隣り合い、塊が直接つながる場合は、左の塊の直後に分離で a を入れる（証拠は W_x を系 C で収縮した語 a^{≥2}F_X a^{≥1}）。

(ii)(iii) 範囲が交わる場合。出力は互いに素なので、x' の成分の少なくとも一つが x の成分の間（隙間）にあるか、その逆である。全ての場合を数えると（入れ子：x₁ < x'₁ < x'₂ < x₂、交差：x₁ < x'₁ < x₂ < x'₂ とその左右逆、x が x' の隙間に入る場合）、左から並べた成分の順は**必ず「第一成分、第一成分、第二成分、第二成分」**になる（§8 Part A で長さ 12 の線上の全ての配置を確かめた）。したがって W の a を含まない因子は、左から ρ¹ の因子、ρ¹ の因子、ρ² の因子、ρ² の因子の順に並ぶ。各成分の中の因子を補題 F′ でまとめ（成分が直接つながる場合は (i) と同じく分離する。分離の証拠は SB₂ の語 a^{≥2}A_X a^{≥1}、a^{≥2}B_X a^{≥1}）、片側型なら二つの F_X、両側型なら A_X, A_X, B_X, B_X が a の連で隔てられた語を得る。□

### 3.4 入れ子

**補題 N（入れ子）。** 型 τ の両側型ラベル X₀ が補題 T (iii) の型板を持つとする。S₁, …, S_m（m ≥ 0）を型 τ の殻で SB₂(S_i, e_i) を持つもの、P を b と c を含み a を含まない語で SB(P, d_P) を持つものとし、Λ := Σe_i + d_P ≤ k/2、d_{X₀} ≤ k/8、k ≥ 4θ+12 とする。このとき

SB(A₁A₂⋯A_m P B_m⋯B₂B₁, Λ)。

**証明。** m に関する帰納法。m = 0 は仮定。Q := A₂⋯A_m P B_m⋯B₂ について SB(Q, Λ−e₁) が成り立つとする。型板 a^{y₀}A₀a^{y₁}A₀a^{y₂}B₀a^{y₃}B₀a^{y₄}（S₀ = (A₀, B₀) = (A_{X₀}, B_{X₀})、e₀ = d_{X₀}）で、二つ目の A₀ と一つ目の B₀ の間の連を補題 F′ で取り除き、

a^{y₀} A₀ a^{y'} F₀ a^{y₃} B₀ a^{y₄}、 F₀ = A₀B₀（系 C により SB(F₀, e₀)）

を得る。補題E で「a F₀」を「a^{1+(Λ−e₁)−e₀}Q」に（Λ−e₁ < e₀ なら逆向きに）替える。必要な詰め物の a は、交換の前の a の個数 k−2e₀ が交換後の値 k−e₀−(Λ−e₁) より詰め物の分だけ多いので確保できる。次に補題 E₂ で、外側の組 (a A₀, B₀) を（e₁ と e₀ の大小に応じて詰め物を付けて）(aA₁, B₁) に替える。中央の部分は F₀ の位置の Q を含み空でないので、文脈は許容的。こうして a^{z₀}A₁a^{z₁}Q a^{z₂}B₁ a^{z₃} ∈ L（a の個数 k−Λ ≥ k/2 ≥ 2θ+6）を得て、系 C で収縮する。補題E は d ≤ k−3、補題 E₂ は e ≤ k−4 を要るが、どちらも Λ ≤ k/2 から成り立つ。□

**注意。** 型板があれば、殻の型 τ の中では、殻と塊を**自由に入れ子にできる**。二つの塊を横に並べる語（(S1) の代わり）は作っていないし、作る必要もない（§5）。

---

## 4. 定理 I：場合 I の多項式上界（追加の条件なし）

### 4.1 ラベルの分類と二つの分岐

N := 25θ³ とし、ℓ_X ≤ k/(2N) の両文字型ラベルを**低い**と呼ぶ。低い両文字型ラベルで、T の中に内部の出現を二つ以上持つものを**関係のある**ラベルと呼ぶ。k ≥ 4θ+12 とする。このとき低いラベルは k − 2ℓ_X ≥ k(1−1/N) ≥ 2θ+4 と k−ℓ_X ≥ θ+2 を満たし、補題 T・SB₂・系2.3 が使える。

**分岐 (B)**：二塊の語 a^{s₀}P a^{s₁} Q a^{s₂} ∈ L で、P, Q が b と c を含み a を含まず、SB(P, d_P)、SB(Q, d_Q)、d_P, d_Q ≤ k/(2N) となるものがある。
**分岐 (S)**：そうでない。

補題 T により、関係のあるラベル X は、補題 T (i)(ii) なら分岐 (B) を成り立たせ（P = Q = F_X）、そうでなければ両側型で型板を持つ。したがって**分岐 (S) では、関係のあるラベルは全て両側型で、自分の型の型板を持つ。** なお、(S1)（範囲が互いに素な内部の両文字型節点が二つある）が成り立ち、低い内部の両文字型ラベルが一つでもあれば、補題V（n=2）により分岐 (B) である（低い内部のラベルがなければ、両文字型の節点は全て例外に数えられ、どちらの分岐でも同じ上界になる）。

### 4.2 二つの線形性

**補題 P*（分岐 (B)）。** 分岐 (B) では、各偶奇類 𝒫 について φ_𝒫 ∈ ℚ³ があり、𝒫 に属する全ての低い内部の両文字型ラベル X について d_X = ⟨φ_𝒫, (n'_X, β_X, γ_X)⟩。

**証明。** 第十二報の補題P の証明で、命題4.1 の二塊の語を分岐 (B) の語に替えるだけである。分岐 (B) の語の二つの塊は補題E で任意の塊（鎖を含む）に替えられ、補題 F′ で融合できるので、命題4.1 の鎖（≤ 24θ³ 個、Σd ≤ k/2）が全て SB を持つ。残りは §2.6 のとおり。□

**殻の細類。** 両側型ラベル X の殻 (A_X, B_X) の各側について、(内容, 先頭の文字, 末尾の文字) を記述子とする。内容が {b} なら (b, b) だけ、{c} なら (c, c) だけ、{b,c} なら四通りで、片側 6 通り。両側で 36 通りのうち、両側とも b だけ、両側とも c だけの 2 通りは両文字型にならないので、**細類は 34 個**（§8 Part B で確認）。細類は型 τ を決める。細類 π の殻について

n'_X := n(A_X) + n(B_X) − [l(A_X) = f(A_X)] − [l(B_X) = f(B_X)] ∈ [0, θ]

とおく（n は連の数、f は先頭、l は末尾の文字）。

**補題 Q（分岐 (S)、場合 I）。** 場合 I・分岐 (S) では、各細類 π について φ_π ∈ ℚ³ があり、π に属する全ての関係のあるラベル X について d_X = ⟨φ_π, (n'_X, β_X, γ_X)⟩。

**証明。** π に関係のあるラベル X₀ を一つ固定し、P := F_{X₀}（SB(P, d_{X₀})、系2.3）とおく。X₀ は自分の型 τ(π) の型板を持つ（§4.1）。

(a) **入れ子の核。** π の殻 S₁, …, S_m（m ≥ 1）と P の入れ子の語 F = A₁⋯A_m P B_m⋯B₁ は、先頭の文字が π の f_A で、連の数は

n(F) = Σ_i n'(S_i) + c_π(P)、 c_π(P) := n(P) − [l_A = f(P)] − [l(P) = f_B] + [l_A = f_A] + [l_B = f_B]。

接合は A_i|A_{i+1}（合わさるのは l_A = f_A のとき）、A_m|P、P|B_m、B_{i+1}|B_i（l_B = f_B のとき）だけで、いずれも π と P だけで決まるからである（§8 Part B で、連 ≤ 3・長さ ≤ 2 の全ての語、m ≤ 2 の入れ子 811104 通りを確かめた）。

(b) **比較。** π の関係のあるラベルの多重集合 𝒜、ℬ（各 1 個以上 24θ³ 個以下、個数は違ってよい）が Σn', Σβ, Σγ を共有するとする。補題 N により、𝒜 の殻を（任意の順で）P のまわりに入れ子にした語 F_𝒜 は SB(F_𝒜, Σ_𝒜 d + d_P) を持つ（Σ ≤ (24θ³+1)·k/(2N) ≤ k/2）。ℬ も同じ。場合 I では σ(a^s F a^t) = a·(先頭の文字と連の数で決まる b, c の交代語)·a なので、(a) により σ が等しく、b, c の個数も等しく、a の個数 k − Σd − d_P は [k/2, k) にある。(R) により Σ_𝒜 d = Σ_ℬ d。

(c) **線形代数。** ベクトル (n', β, γ) ∈ [0,θ]×[1,θ]² の回路の関係（≤ 4 本、係数は 3×3 小行列式で ≤ 6θ³、§8 Part C で θ ≤ 4 の全数を確認）は核を張り、片側は 1 個以上 24θ³ 個以下（β > 0 なので両側とも空でない）。(b) により d は核に直交し、行空間に入る。□

**注意。** 補題 Q の証明は、二つの塊を横に並べることを一度も使わない。殻の入れ子は「外の殻・中の殻・中心の塊」と一次元的に積み重なり、同じ細類の殻の接合が全て同じ形になる。これが補題P の「同じ偶奇類の鎖の核は個数によらない」に当たる。

### 4.3 定理 I

**定理 I。** Σ = {a,b,c}、内容型付け c、L ∈ C_{2,c}、b⁴ と c⁴ がともに L の語に現れる（場合 I）とする。G を L∩Σ⁺ の reduced good な、ファンアウト ≤ 2、ランク ≤ r の表示とし、v = |V|、θ = θ̄_G とする。このとき

μ_a(L) ≤ max{4θ+12, K_I^{313} R^{312} θ}、
K_I := (2v+E_I)(2r+1)、 E_I := v(50θ³ + θ + 23)、 R := θ+2v+2。

**証明。** k := μ_a(L) ≥ 4θ+12 とし、T を一様な最小導出とする。重い節点を次のように分ける。

- **例外**
  - 一色型の例外：18v + vθ（第十報 §3.1–3.2）。
  - 内部でないラベルの両文字型節点：ラベルごとに ≤ 2 個、計 ≤ 2v。
  - 高い（ℓ > k/(2N)）両文字型節点：一つの深さに < 2N 個、計 ≤ 2Nv = 50θ³v。
  - 低い両文字型ラベルで内部の出現がちょうど一つのものの節点：ラベルごとに ≤ 3 個（内部 1、内部でない ≤ 2）、計 ≤ 3v。分岐 (B) ではこれらも群に入れてよいが、上界は変えずにおく。

  合計 E_I。
- **群**
  - 飽和の色の頻出の一色型：値 α_x q（点 q ∈ [1,θ]、窓 [α_x q, α_x q+θ]）。
  - 分岐 (B)：低い内部の両文字型ラベル X（値 d_X、窓 [d_X, d_X+θ]）。補題 P* により、四つの偶奇類それぞれで (n', β, γ) ∈ [2,θ]×[1,θ]² の線形形式。D = 2 + 4·3 = 14。
  - 分岐 (S)：関係のあるラベル X（値 d_X、窓は同じ）。補題 Q により、34 個以下の細類それぞれで (n', β, γ) ∈ [0,θ]×[1,θ]² の線形形式。D ≤ 2 + 34·3 = 104。

内部の出現が二つ以上ある低いラベルは全て群に入り、それ以外の両文字型節点は全て例外に数えたので、分類はもれがない。第十一報の補題3.1（K = K_I）と補題3.2（n ≤ 3D）により k ≤ K_I^{3D+1}R^{3D}θ ≤ K_I^{313}R^{312}θ。□

**範囲の明記。** これは三文字・内容型付け・L ∈ C_{2,c}（arity 1 と 2 の代入可能性）で、**b⁴ と c⁴ がともに L の語に現れる場合**に、L の**任意の** reduced good なファンアウト ≤ 2・ランク ≤ r の表示 G について、純粋な a 語の最小の長さ μ_a(L) を poly_r(v, θ) で抑えたものである。

- 場合 II（b⁴ も c⁴ も現れない）・場合 III（どちらか一方だけ）は扱っていない。
- 他の稀な型の最短語（`prop:rare-type` の μ_m のうち m ≠ {a} のもの）も扱っていない。
- 次数（v について 600 次程度）は鋭さを追っていない。
- **`op:fanout-two` の三文字の核の全体を解いたわけではない。**

**定理D・系D との関係。** (S1) の下では分岐 (B) で D = 14 となり、定理D（K_D^{43}R^{42}θ、E は今回より少し小さい）がそのまま成り立つ。系D（ファンアウト1）も定理 I に含まれる。

---

## 5. 跨ぎの場合についての依頼の各点

- **Claude の観察（入れ子の対 x₁ ⊃ x₂ で L₁ a^p F_{X₂} a^q R₁、F_{X₂} を任意の F_Y に）**：**独立に確認。** x₂ の二成分の融合は補題 F′ で行え（今の語自身が証拠になる）、補題E による F_{X₂} → F_Y の交換も正しい。これは補題 N の中段（型板の中の塊の交換）と同じ操作である。
- **二つの完全な塊が離れて並ぶ語を作れるか**：一般には作れなかった（**確認できず**）。跨ぎの場合に、殻 (A, B) の片側だけを単独の SB の塊として取り出す手段が見つからなかった。ただし定理 I には不要である。作れる場合が分岐 (B)、作れない場合が分岐 (S) で、分岐 (S) では補題 Q が補題P の代わりをする。
- **二穴版の補題E・F と二穴の鎖**（報告 §5.5 の筋）：二穴版の補題E は補題 E₂ として証明した。二穴版の補題F は要らない。殻の成分の中の融合は一穴の補題 F′ で行えるからである。「二穴の鎖」は、横に並べる鎖ではなく、**入れ子**（補題 N）として実現した。報告 §5.5 の「型は 16 通り程度」は、成分ごとの内容まで区別すると 34 細類になる（細類が内容を決めないと、補題 E₂ が使えない）。
- **なぜ同じラベルの二出現を使うのか**：異なるラベルの入れ子の対は、T の中にあるとは限らない。一方、低いラベルで内部の出現が二つ以上あれば、その二出現は必ず、範囲が互いに素（二塊の語）か、成分の順が [1][1][2][2]（型板）になる（補題 T）。内部の出現が一つ以下のラベルは、節点が ≤ 3 個なので例外に数えられる。この二点で、跨ぎの場合の構造の問題が消える。
- **跨ぐ節点が少ない場合**：跨ぐ節点が poly(v,θ) 個以下なら N_bc ≤ poly(v,θ) + 2v で (4.2) が多項式を与える。**自明に成り立つが目的には足りない。** 定理 I でこの場合分けは不要になった。

---

## 6. 場合 II・III

**場合によらず成り立つもの。** 補題 F′・系 C（収縮）・補題 SB₂・補題 E₂・補題 T・補題 N は a⁴ だけを使うので、場合 II・III でも成り立つ。分岐 (B) では命題4.1 の鎖も全て SB を持つ。場合に固有なのは (R) だけで、場合 II では σ = σ_a、すなわち (R) は「a を含まない部分の語 F そのものが一致する」ときにしか関係を与えない（第十二報 §7 の観察と同じ）。

**証明済みの小さな帰結（場合 II）。** 場合 II の分岐 (S) で、関係のある両側型ラベル X の殻の片側 A_X が一つの連（x^j、x ∈ {b,c}）なら、補題 N により入れ子 S_X⁴[F_X] は SB を持ち、その語は x^{4j} を含む。これは x⁴ が現れないことに反する。よって**場合 II の分岐 (S) では、関係のある殻の両側はどちらも二つ以上の連を持つ。** 場合 III（X = {b}）でも、c の一つの連だけから成る側について同じことが言える。同様に分岐 (B) では鎖 F_X^t が SB を持つので、F_X の先頭の連と末尾の連が同じ文字 x で、長さの和が 4 以上なら矛盾する。

**観察（証明していない）。** 場合 II では、λ(F) := k − (a^s F a^t ∈ L の a の個数) が、SB の塊の語 F の関数として定まる。それは鎖・入れ子の連結について加法的である（分岐 (B) では λ(F_X F_Y) = λ(F_X) + λ(F_Y)、分岐 (S) では λ(A P B) = e_S + λ(P)）。塊の語が符号（一意に分解できる）をなせば、(R) からはそれ以上の関係は出ない。反例を作るなら、arity 1 の代入可能性が、塊の部分語（例えば F の中の bc や cb）を通じて λ に課す制約を避ける必要がある。第十二報の観察 (Lyndon–Schützenberger) を超える進展はない。**場合 II・III は未解決。**

---

## 7. 否定側

**新しい候補は作れなかった。下界は主張しない。** 定理 I から、反例の族（三文字、‖G_n‖, θ̄_{G_n} が多項式、μ_a(L_n) が超多項式、L_n ∈ C_{2,c}）が満たすべきことは次のとおり（いずれも証明済み）。

1. **場合 II か III でなければならない**（場合 I なら、ファンアウト ≤ 2 のどの表示でも μ_a は多項式）。
2. L_n は、関係のある各ラベルについて、次を全て含む。
   - 分岐 (B) なら、全ての鎖とその融合
   - 分岐 (S) なら、型ごとの全ての入れ子
   - どちらの場合も、全ての受理語の収縮（系 C）
3. 依頼にある既報の障害（□ と □a による a の個数の漏れ、偶数の塊の障害、(R)・補題F の融合、定理C）に加え、次の三つにも耐えること。
   - 補題 F′：a の連の一つを、両隣の材料をつなげて消せる
   - 補題 E₂：同じ型の殻は交換できる
   - §6 の連の長さの制約

将来下界を述べるときの量化は第十報 §7.2 のとおり：作用素 B^{≤r}_{2,c}、B_{2,c}、クラス全体に特徴標本を持つ集合駆動作用素；Σ = {a,b,c}、ファンアウト ≤ 2、ランク ≤ 2；L_n ∈ C_{2,c} を直接証明すること。

---

## 8. 計算

Python 3 の標準ライブラリだけで書いた。Windows では `py -3 claude_straddle_check.py`。この環境で `python3 -I` により実行した（約6秒）。説明文の不等式と assert の不等式はそろえてある。

- **Part A**：範囲が交わり出力が互いに素な、ファンアウト2の二節点の成分の順が常に [1,1,2,2] であること（長さ 12 の線上の全ての配置。補題 T）。区間の組合せだけの確認。
- **Part B**：殻の細類が 34 個であることと、入れ子の連の数の式 n(F) = Σn' + c_π(P)・先頭の文字（補題 Q (a)）。文字列の恒等式で、連 ≤ 3・長さ ≤ 2 の語について m ≤ 2 で全数。
- **Part C**：(n', β, γ) ∈ [0,θ]×[1,θ]² の回路の係数 ≤ 6θ³（θ = 2, 3, 4）。Cramer の上界の**有限の確認**で、証明は §4.2。
- **Part D**：**機械的に検査した証明書。** 種は次の六語である。
  - a^{40}
  - 四つの殻 (b,c)、(bb,c)、(b,cc)、(bb,cc) の SB₂ の語を一つずつ（損失 e₁, …, e₄）
  - 殻 (b,c) の型板 a b a b a c a c a^{30}

  証明器は本報告の証明（補題 F′、補題E、補題 E₂、補題 N、定理S）に従って進み、各段を次の二つの規則のどちらかの具体例として書き出す。
  - R1：E₀[x], E₀[y], E₁[x] ∈ S、c(x) = c(y) なら E₁[y] ∈ S
  - R2：同じことを二穴の組で行う（許容文脈、成分ごとの内容が等しい）

  別の関数がそのログを種から再生し、全段を検査する。二つの規則は、S を含む全ての L ∈ C_{2,c} で健全なので、最後に a^j（j < 40）が出れば「μ_a(L) = 40 でこれらの種を含む L ∈ C_{2,c} はない」ことの**証明書**になる。e₂+e₃ ≠ e₁+e₄（非線形）では証明書 a^{39} が出て、e₂+e₃ = e₁+e₄ では出ない（後者は何の証明でもない）。
  - この例では二つの入れ子 S₂[S₃[bc]] と S₄[S₁[bc]] がどちらも語 b⁴c⁴ になるので、(R) の b, c の再配分は使わず、定理S だけで矛盾が出る。補題 Q の一般の場合は、(R) を通して同じ結論になる。
  - 有限の検査から無限の族の所属を推定することはしていない。

```python
#!/usr/bin/env python3
"""Checks for claude_straddle_2026-11-04.md (Python 3 standard library only).

Windows: py -3 claude_straddle_check.py

Part A  Interleavings.  For two fan-out-2 nodes with disjoint outputs whose
        ranges intersect, the left-to-right order of their components is
        always [first][first][second][second] (exhaustive over positions on a
        line of length 12).  Pure combinatorics of intervals.
Part B  Run count of shell nests.  For shells S_i=(A_i,B_i) of one subclass
        (same content and same first/last letter on each side) and an inner
        block P, the word A_1..A_m P B_m..B_1 has first letter f(A) and
        n = sum_i n'(S_i) + c(P), n'(S) = n(A)+n(B)-[l_A=f_A]-[l_B=f_B].
        Exhaustive over all {b,c}-words with <= 3 runs of length <= 2, m <= 2.
Part C  Circuit coefficients of vectors (n', beta, gamma) in [0,theta]x[1,theta]^2:
        max |coef| <= 6 theta^3 (theta = 2, 3, 4).  Finite check of the
        Cramer bound; the bound itself is proved in the report.
Part D  A mechanised certificate.  Seeds: a^k, one two-hole word for each of
        four shells (b,c),(bb,c),(b,cc),(bb,cc) with losses e1..e4, and one
        "template" word a b a b a c a c a^* of the shell (b,c).  A prover
        follows the proof of the report (self-fusion, one- and two-hole
        exchange, nests) and writes every step as an instance of the two rules
          R1: E0[x],E0[y],E1[x] in S, c(x)=c(y)            => E1[y] in S
          R2: same for 2-tuples, admissible contexts,
              componentwise equal contents                 => E1[y] in S
        An independent replay re-checks every step from the seeds.  Both rules
        are sound for every L in C_{2,c} containing S, so a pure word a^j with
        j < k at the end is a CERTIFICATE that no L in C_{2,c} with
        mu_a(L) = k contains the seeds.  With e2+e3 != e1+e4 the certificate
        appears; with e2+e3 = e1+e4 the final step finds equal a-counts and
        produces nothing (this is not a proof of anything).
"""
from fractions import Fraction
from itertools import combinations, product


def content(w):
    return frozenset(w)


def runs_bc(w):
    out = []
    for ch in w:
        if not out or out[-1] != ch:
            out.append(ch)
    return ''.join(out)


# ---------------------------------------------------------------- Part A
def partA(N=12):
    count = 0
    for a1, b1, a2, b2 in combinations(range(N + 1), 4):          # node x
        x = [(a1, b1), (a2, b2)]
        for c1, d1, c2, d2 in combinations(range(N + 1), 4):      # node y
            y = [(c1, d1), (c2, d2)]
            # outputs disjoint: no overlap of any two component intervals
            if any(not (p[1] <= q[0] or q[1] <= p[0]) for p in x for q in y):
                continue
            rx, ry = (a1, b2), (c1, d2)                          # ranges
            if rx[1] <= ry[0] or ry[1] <= rx[0]:
                continue                                         # disjoint ranges
            comps = sorted([(a1, 'x', 1), (a2, 'x', 2), (c1, 'y', 1), (c2, 'y', 2)])
            pattern = [c[2] for c in comps]
            assert pattern == [1, 1, 2, 2], (x, y, pattern)
            count += 1
    print('Part A: %d interleaved pairs, pattern always [1,1,2,2]; PASS' % count)


# ---------------------------------------------------------------- Part B
def bc_words(max_runs=3, max_len=2):
    out = []
    for n in range(1, max_runs + 1):
        for first in 'bc':
            other = 'c' if first == 'b' else 'b'
            letters = [first if i % 2 == 0 else other for i in range(n)]
            for lens in product(range(1, max_len + 1), repeat=n):
                out.append(''.join(x * l for x, l in zip(letters, lens)))
    return out


def side(w):
    return (content(w), w[0], w[-1])


def nprime(A, B):
    return (len(runs_bc(A)) + len(runs_bc(B))
            - (A[-1] == A[0]) - (B[-1] == B[0]))


def partB():
    words = bc_words()
    shells = [(A, B) for A in words for B in words
              if content(A + B) == frozenset('bc')]
    classes = {}
    for S in shells:
        classes.setdefault((side(S[0]), side(S[1])), []).append(S)
    checked = 0
    for (sa, sb), members in classes.items():
        fA, lA, fB, lB = sa[1], sa[2], sb[1], sb[2]
        for P in words:
            cP = (len(runs_bc(P)) - (lA == P[0]) - (P[-1] == fB)
                  + (lA == fA) + (lB == fB))
            for m in (1, 2):
                for nest in product(members, repeat=m):
                    F = (''.join(S[0] for S in nest) + P
                         + ''.join(S[1] for S in reversed(nest)))
                    assert F[0] == fA
                    assert len(runs_bc(F)) == sum(nprime(*S) for S in nest) + cP
                    checked += 1
    print('Part B: %d subclasses, %d nests checked; PASS' % (len(classes), checked))
    assert len(classes) == 34


# ---------------------------------------------------------------- Part C
def det3(u, v, w):
    return (u[0] * (v[1] * w[2] - v[2] * w[1]) - u[1] * (v[0] * w[2] - v[2] * w[0])
            + u[2] * (v[0] * w[1] - v[1] * w[0]))


def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)


def rank(vs):
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


def partC():
    for theta in (2, 3, 4):
        vecs = [(n, b, c) for n in range(0, theta + 1)
                for b in range(1, theta + 1) for c in range(1, theta + 1)]
        worst = 0
        for u, v in combinations(vecs, 2):
            if rank([u, v]) == 1:
                g = 0
                for x in u + v:
                    g = gcd(g, x)
                # u, v parallel: primitive relation coefficients are |v|/g', |u|/g'
                worst = max(worst, max(max(u), max(v)))
        for u, v, w in combinations(vecs, 3):
            if det3(u, v, w) != 0:
                continue
            if any(rank([p, q]) < 2 for p, q in ((u, v), (u, w), (v, w))):
                continue
            for (i, j) in ((0, 1), (0, 2), (1, 2)):
                d = lambda x, y: x[i] * y[j] - x[j] * y[i]
                c = (d(v, w), -d(u, w), d(u, v))
                if any(c) and all(c[0] * u[r] + c[1] * v[r] + c[2] * w[r] == 0
                                  for r in range(3)):
                    g = 0
                    for x in c:
                        g = gcd(g, x)
                    worst = max(worst, max(abs(x) // g for x in c))
                    break
        for quad in combinations(vecs, 4):
            ds = [det3(*[quad[j] for j in range(4) if j != i]) for i in range(4)]
            if all(ds):
                g = 0
                for x in ds:
                    g = gcd(g, x)
                worst = max(worst, max(abs(x) // g for x in ds))
        print('Part C: theta %d  max |circuit coef| %d  bound 6*theta^3 = %d'
              % (theta, worst, 6 * theta ** 3))
        assert worst <= 6 * theta ** 3
    print('Part C: PASS (finite check of the Cramer bound)')


# ---------------------------------------------------------------- Part D
def fill1(E, x):
    return E[0] + x + E[1]


def fill2(E, x):
    return E[0] + x[0] + E[1] + x[1] + E[2]


def check_step(S, step):
    """The two closure rules.  Returns the new word or raises."""
    kind, x, y, E0, E1 = step
    if kind == 'R1':
        assert x and y and content(x) == content(y)
        assert fill1(E0, x) in S and fill1(E0, y) in S and fill1(E1, x) in S
        return fill1(E1, y)
    assert kind == 'R2'
    assert all(x) and all(y) and E0[1] and E1[1]          # admissible contexts
    assert content(x[0]) == content(y[0]) and content(x[1]) == content(y[1])
    assert fill2(E0, x) in S and fill2(E0, y) in S and fill2(E1, x) in S
    return fill2(E1, y)


def a_runs(w):
    out, i = [], 0
    while i < len(w):
        if w[i] == 'a':
            j = i
            while j < len(w) and w[j] == 'a':
                j += 1
            out.append((i, j))
            i = j
        else:
            i += 1
    return out


class Prover:
    def __init__(self, k, seeds):
        self.k, self.S, self.log = k, set(seeds), []

    def apply(self, step):
        w = check_step(self.S, step)
        self.S.add(w)
        self.log.append(step)
        return w

    # one a from run j to run i (Lemma 2.1 with x = a)
    def transfer(self, w, j, i):
        R = a_runs(w)
        E0 = ('', 'a', 'a' * (self.k - 4))
        if i < j:                       # right run j (>=2) gives one to left run i
            (si, ei), (sj, ej) = R[i], R[j]
            assert ej - sj >= 2
            E1 = (w[:ei - 1], w[ei:sj], w[sj + 2:])
            return self.apply(('R2', ('a', 'aa'), ('aa', 'a'), E0, E1))
        (sj, ej), (si, ei) = R[j], R[i]  # left run j (>=2) gives one to right run i
        assert ej - sj >= 2
        E1 = (w[:ej - 2], w[ej:si], w[si + 1:])
        return self.apply(('R2', ('aa', 'a'), ('a', 'aa'), E0, E1))

    def redistribute(self, w, target):
        cur = [e - s for s, e in a_runs(w)]
        assert len(cur) == len(target) and sum(cur) == sum(target)
        assert min(target) >= 1
        while cur != target:
            i = next(t for t in range(len(cur)) if cur[t] < target[t])
            j = next(t for t in range(len(cur)) if cur[t] > target[t])
            w = self.transfer(w, j, i)
            cur[i] += 1
            cur[j] -= 1
        assert [e - s for s, e in a_runs(w)] == target
        return w

    # self-fusion: remove the a-run between non-a factor f and factor f+1
    def fuse(self, w, f):
        cur = [e - s for s, e in a_runs(w)]
        t = cur[:]
        t[f] += t[f + 1] - 1
        t[f + 1] = 1
        if t[f] < 2:
            j = next(q for q in range(len(t)) if q not in (f, f + 1) and t[q] >= 2)
            t[j] -= 1
            t[f] += 1
        w = self.redistribute(w, t)
        R = a_runs(w)
        re_, fe = R[f][1], R[f + 1][0]
        u = w[re_:fe]
        moved = self.transfer(w, f, f + 1)           # P a^{p-1} u a a v Q
        E0 = (w[:re_ - 2], w[fe:])
        E1 = (w[:re_ - 1], w[fe + 1:])
        assert fill1(E0, 'a' + u + 'a') == moved
        return self.apply(('R1', 'a' + u + 'a', 'aa' + u, E0, E1))

    def collapse(self, w):
        while len(a_runs(w)) > 2:
            w = self.fuse(w, 0)
        return w

    def factor_pos(self, w):
        R = a_runs(w)
        return [(R[i][1], R[i + 1][0]) for i in range(len(R) - 1)]

    # one-hole exchange (Lemma E): block at factor f, from (F, d) to (F2, d2)
    def exchange1(self, w, f, F, d, F2, d2, sbw):
        k = self.k
        lo, hi = (d, d2) if d <= d2 else (d2, d)
        Plo, Phi = (F, F2) if d <= d2 else (F2, F)
        x = 'a' * (1 + hi - lo) + Plo          # small-loss block with a padding
        y = 'a' + Phi
        E0 = ('', 'a' * (k - hi - 1))
        self.redistribute(sbw[Plo], [1 + hi - lo, k - hi - 1])
        self.redistribute(sbw[Phi], [1, k - hi - 1])
        if d <= d2:                          # current block is the small-loss one
            cur = [e - s for s, e in a_runs(w)]
            need = 1 + hi - lo
            if cur[f] < need:
                t = cur[:]
                t[-1] -= need - cur[f]
                t[f] = need
                w = self.redistribute(w, t)
            s, e = self.factor_pos(w)[f]
            E1 = (w[:s - need], w[e:])
            return self.apply(('R1', x, y, E0, E1))
        s, e = self.factor_pos(w)[f]
        E1 = (w[:s - 1], w[e:])
        return self.apply(('R1', y, x, E0, E1))

    # two-hole exchange: shell occupying factors fa, fb
    def exchange2(self, w, fa, fb, Sh, e, Sh2, e2, sb2w):
        k = self.k
        lo, hi = (e, e2) if e <= e2 else (e2, e)
        Slo, Shi = (Sh, Sh2) if e <= e2 else (Sh2, Sh)
        x = ('a' * (1 + hi - lo) + Slo[0], Slo[1])
        y = ('a' + Shi[0], Shi[1])
        E0 = ('', 'a', 'a' * (k - hi - 2))
        self.redistribute(sb2w[Slo], [1 + hi - lo, 1, k - hi - 2])
        self.redistribute(sb2w[Shi], [1, 1, k - hi - 2])
        if e <= e2:
            cur = [q - p for p, q in a_runs(w)]
            need = 1 + hi - lo
            if cur[fa] < need:
                t = cur[:]
                t[-1] -= need - cur[fa]
                t[fa] = need
                w = self.redistribute(w, t)
            pos = self.factor_pos(w)
            (sa, ea), (sb, eb) = pos[fa], pos[fb]
            E1 = (w[:sa - need], w[ea:sb], w[eb:])
            return self.apply(('R2', x, y, E0, E1))
        pos = self.factor_pos(w)
        (sa, ea), (sb, eb) = pos[fa], pos[fb]
        E1 = (w[:sa - 1], w[ea:sb], w[eb:])
        return self.apply(('R2', y, x, E0, E1))


def certificate(k, e):
    e1, e2, e3, e4 = e
    S1, S2, S3, S4 = ('b', 'c'), ('bb', 'c'), ('b', 'cc'), ('bb', 'cc')
    loss = {S1: e1, S2: e2, S3: e3, S4: e4}
    sb2w = {S: 'a' + S[0] + 'a' + S[1] + 'a' * (k - loss[S] - 2) for S in loss}
    template = 'a' + 'b' + 'a' + 'b' + 'a' + 'c' + 'a' + 'c' + 'a' * (k - 2 * e1 - 4)
    seeds = {'a' * k, template} | set(sb2w.values())
    pr = Prover(k, seeds)
    sbw = {}
    # block P = bc (closure of the shell S1)
    sbw['bc'] = pr.collapse(sb2w[S1])
    # template -> S1[P]: fuse the second b with the first c
    T = pr.fuse(template, 1)                        # factors: b | bc | c
    # Q3 = S3[P] = b bc cc
    w = pr.exchange2(T, 0, 2, S1, e1, S3, e3, sb2w)
    sbw['bbccc'] = pr.collapse(w)
    # Q = S2[Q3] = bb bbccc c
    w = pr.exchange1(T, 1, 'bc', e1, 'bbccc', e1 + e3, sbw)
    w = pr.exchange2(w, 0, 2, S1, e1, S2, e2, sb2w)
    W1 = pr.collapse(w)
    # Q1 = S1[P] = b bc c, then Q' = S4[Q1] = bb bbcc cc
    sbw['bbcc'] = pr.collapse(T)
    w = pr.exchange1(T, 1, 'bc', e1, 'bbcc', 2 * e1, sbw)
    w = pr.exchange2(w, 0, 2, S1, e1, S4, e4, sb2w)
    W2 = pr.collapse(w)
    F = 'bbbbcccc'
    assert W1.strip('a') == F and W2.strip('a') == F
    n1, n2 = W1.count('a'), W2.count('a')
    assert n1 == k - (e1 + e2 + e3) and n2 == k - (e4 + 2 * e1)
    result = None
    if n1 != n2:                                   # Theorem S, done with R1
        lo, hi = sorted((n1, n2))
        delta = hi - lo
        wlo = pr.redistribute(W1 if n1 == lo else W2, [1, lo - 1])
        whi = pr.redistribute(W2 if n1 == lo else W1, [1, hi - 1])
        U = 'a' + F + 'a' * (lo - 2)
        assert wlo == U + 'a' and whi == U + 'a' * (1 + delta)
        # E0 = U.[] accepts a^{1+delta} and a; E1 = a^{k-1-delta}.[] accepts
        # a^{1+delta} (giving a^k), hence accepts a: a^{k-delta}
        result = pr.apply(('R1', 'a' * (1 + delta), 'a', (U, ''),
                           ('a' * (k - 1 - delta), '')))
    # independent replay of the whole log from the seeds
    S = set(seeds)
    for st in pr.log:
        S.add(check_step(S, st))
    return result, len(pr.log), (n1, n2), S


def partD():
    k = 40
    for e in [(3, 5, 6, 7), (3, 5, 6, 8)]:
        res, steps, counts, S = certificate(k, e)
        line = ('Part D: k=%d losses e1..e4=%s  a-counts of the two a^s b^4c^4 a^t '
                'words %s, %d checked steps' % (k, e, counts, steps))
        if res is not None:
            assert set(res) == {'a'} and len(res) < k and res in S
            line += ' -> CERTIFICATE a^%d' % len(res)
        else:
            line += ' -> equal a-counts, no short word (no conclusion)'
        print(line)


if __name__ == '__main__':
    partA()
    partB()
    partC()
    partD()
```

**実行結果（2026-11-04、この環境で `python3 -I` により実行）**

```text
Part A: 38610 interleaved pairs, pattern always [1,1,2,2]; PASS
Part B: 34 subclasses, 811104 nests checked; PASS
Part C: theta 2  max |circuit coef| 8  bound 6*theta^3 = 48
Part C: theta 3  max |circuit coef| 36  bound 6*theta^3 = 162
Part C: theta 4  max |circuit coef| 96  bound 6*theta^3 = 384
Part C: PASS (finite check of the Cramer bound)
Part D: k=40 losses e1..e4=(3, 5, 6, 7)  a-counts of the two a^s b^4c^4 a^t words (26, 27), 76 checked steps -> CERTIFICATE a^39
Part D: k=40 losses e1..e4=(3, 5, 6, 8)  a-counts of the two a^s b^4c^4 a^t words (26, 26), 71 checked steps -> equal a-counts, no short word (no conclusion)
```

Part C の最大値（8, 36, 96）は、n' = 0 を許すので第十二報の Part B（n' ≥ 1、5, 22, 69）より大きいが、上界 6θ³ の内側にある。Part D の種は場合 I を満たす言語の一部として置いたもので、e₂+e₃ = e₁+e₄ のときに C_{2,c} の言語へ延びるかどうかは調べていない。

---

## 9. 文献

- Clark–Eyraud, *JMLR* 8 (2007) 1725–1745；Yoshinaka, *TCS* 412 (2011) 1821–1831, doi:10.1016/j.tcs.2010.12.058（多次元代入可能性による MCFG の学習）。
- 補題 F′ と系 C は、補題2.1（weighted_codes）と arity 1 の代入可能性の組み合わせで、原稿 `lem:app-two-runs`(ii)（xy と yx の分布の等式）と同じ型の議論である。補題 E₂ はその二穴版。回路が核を張ること、Cramer の公式、疎な数列の部分和の議論は標準的な道具である。
- 補題 F′・E₂・T・N・Q と定理 I が型付き分布学習の文献に既にあるかは**未確認**（網羅的な調査はしていない）。原稿に入れる前に、著者による再検証と先行研究の確認が要る。

---

## 10. 結了の三点

1. **検証の結論。** 第十二報の補題E・F、系F、系2.3、補題V（と Claude の補足）、定理C、命題4.1、補題P、定理D、系D、§5.5 の観察を全て独立に確かめ、誤りは見つからなかった。補題F の仮定（u の端が a でない、別の証拠語）は不要で、今の語自身が証拠になる（補題 F′）。定理C の条件 (S_{M_C}) は (S1) に弱められる。
2. **証明できたこと。** 跨ぎの場合を含め、**場合 I の Q を、ファンアウト ≤ 2・ランク ≤ r の全ての表示で肯定的に解いた**：μ_a ≤ max{4θ+12, K_I^{313}R^{312}θ}（定理 I）。内部の出現を二つ持つ低いラベルは、二塊の語か二穴の型板を必ず与える（補題 T）。型板があれば殻を任意の深さに入れ子にでき（補題 N）、同じ細類の殻の入れ子の核は Σn' だけで決まるので、損失が (n', β, γ) の線形関数になる（補題 Q）。
3. **止まった場所と次に絞るべき一点。** 場合 II・III。ここでは (R) が「a を含まない部分の語の一致」しか与えず、補題P・Q に当たる線形性がない。**次の一点は、場合 II で、塊の語の加法的な損失 λ に、arity 1 の代入可能性が塊の部分語を通じてどんな制約を課すか**である。例えば、二つの塊に共通の部分語 bc が、異なる a の詰め物の文脈で現れるとき、何が強制されるか。否定側では、反例は場合 II か III に限られ、全ての鎖・入れ子・収縮を含む言語を多項式サイズの文法で作る必要がある。
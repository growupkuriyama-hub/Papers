# 文字の欠けた稀な型 {a,b} の最短の語 μ_{ab}：侵入への帰着の確認、トークン模型の障壁、近道を生む「逃げ道の一致」

**研究日**：2026-11-05　**依頼**：`reviews/prompt_claude_mu_ab_2026-11-05.md`（README (152)、系列の二十六本目）　**実行者**：Claude（Opus 5.5）
**資料**：公開リポジトリ `growupkuriyama-hub/Papers` を 2026-11-05 に複製して読んだ（`02-v2-lg-fanout-boundary/`）。原稿・README は変更していない。
**計算**：`check_claude_mu_ab_2026-11-05.py`（本体）と `search_m3_escapes.py`（本体の関数を使う補助の探索）。どちらも標準ライブラリだけで、実際に実行した。出力は付録 B にそのまま載せる。

**結論を先に。** μ_{ab} の多項式上界も反例も得ていない。得たのは次の四つである。

1. 侵入への帰着を確かめ、印の代わりに「保持者の道」を使う形にして、定数を μ_{ab} ≤ 3(r+1)vθ(q+2) とした（q は c で強制された重い節点の反鎖の最大幅）。(138) の特別な場合である。
2. **仮説 (H) は、逃げ道の近傍の情報だけからは導けない**（命題5、証明済み）。逃げ道をそれぞれ一つの抽象的な文字（トークン）とみなすと、種を含む「加法的な重みの一水準の集合」が全ての arity と全ての型付けで閉じており、その中の c を含まない語は全て長さ |W| である。だから侵入節点がいくら多くても（反鎖の幅 2^m でも）、トークンの段階の証明書では W より短い ab 語は出ない。計算した全ての模型（ファンアウト1・2、入れ子の倍増）で、閉包は実際に閉じ、近道はなかった。
3. 近道は、**文字の段階の一致**から生じる。近道の証明書の最後の段は必ず補題3の形をとる：c を含む共通の枠 E が、内容の同じ c を含まない長さの違う二つの埋め草を受け入れ、その一方が W の因子になっている。逃げ道の因子の一致 e_C = s·e_B（補題7, 7′）はその典型で、(150) の近道を一般化する。トークンの証明書を準同型で L_3,…,L_7 に持ち上げて再生した。
4. 具体的な倍増族（A_i → A_{i−1}A_{i−1} | e_i）を m = 2, 3 で調べた。名前を付けた七つの逃げ道の設計は、m = 3 では全て1段か2段の近道を持つ。m = 3 の網羅探索（2525 通り）で閉包が閉じたのは 17 通りだけで、全て e_2 = e_1e_1 = cc という、独立な逃げ道を持つ段が実質一つの退化した場合だった（打ち切り 1159 通りは判定なし）。

---

## 0. 主張ごとの判定

**検証した既存の主張**

| 主張 | 判定 | 根拠・注意 |
|---|---|---|
| `def:class-cmcf`：二穴の文脈は中央が空でない、空の成分は比べない | 独立に確認 | `main.tex` l.712 付近。計算でも全ての二穴の段で中央が空でないことを再生関数が確かめる |
| `prop:rare-type`：所属する L では、各型の最短の語が特徴標本に要る | 独立に確認（所属が前提） | 本報では所属を示した新しい言語はないので、使っていない |
| 依頼文 §1 の侵入への帰着（印のない重い節点は侵入節点、侵入反鎖が多項式なら μ_{ab} も多項式） | 独立に確認 | §2。(138) の特別な場合。印を保持者の道に替えると定数が 3(r+1)vθ(q+2) になる |
| (143) 補題2.1：一段の SUB は語全体の支持集合を変えない | 独立に確認 | §2.5 で証明を書き直した |
| (149)：L_n は ab 型の唯一の語 (ab)^{2^n} を持ち、全ての n ≥ 2 で C_{2,c} に入らない | n = 2 は独立に確認（総当たりの閉性検査が原報と同じ二穴の違反を見つけ、F[y] ∉ L_2 を文法で判定）。一般の n は原報の証明を読んで確認 | 付録 B の Part A |
| (150)：n ≥ 3 で a(ab)^{2^{n−1}} が強制される | 独立に確認 | Part A（閉包が自力で同じ形の2段を見つける）と Part E（トークンの証明書の持ち上げ、n = 3..7、前提は文法で厳密に所属判定） |
| `lem:app-two-insertion` は三文字の型 {a,b} に使えるか | 数える部分は成り立つ（補題4、証明済み）。矛盾を出す部分は移らない | §2.5。二文字では連の交換で矛盾を出すが、三文字では置き換えた語の支持集合が {a,b,c} のまま |

**新しい主張**

| 主張 | 判定 | 注意 |
|---|---|---|
| 補題1（帰着）：重い節点は「c で強制される」か「a か b の全ての出現を含む（保持者）」。μ_{ab} ≤ 3(r+1)vθ(q+2) | 証明済み | (138) の特別な場合。保持者の道の形と定数が新しい |
| 補題2：保持者でない重い節点のうち、比較不能で非終端が同じものは、生成の総長が等しい | 証明済み | (114) 補題2.1 の類似 |
| 補題3（最小性の伝播）：W = F[x] で、x と内容の同じ y が x と共通の文脈を持てば ‖y‖ ≥ ‖x‖ | 証明済み | **自明に成り立つが目的には足りない**。近道の証明書の最後の段は必ずこの形 |
| 補題4：c で強制された重い節点の反鎖 Q から、\|Q\|/5 個以上の、互いに文字で隔てられた c の連を持つ L の語が作れる | 証明済み | **自明な移植で、目的には足りない**（`lem:app-two-insertion` の前半の特別な場合） |
| **命題5（トークンの障壁）**：逃げ道の近傍の種は加法的な重みの一水準に入り、その集合は閉じている。よってトークンの段階の証明書は近道を作れない | **証明済み** | (H) を「侵入節点の多さ」だけから導く道を閉じる。原理は初等的 |
| 模型 M1（ファンアウト1、同名の穴2・3個）、M3（ファンアウト2、三つの配置）、M4（倍増、深さ ≤ 3）：近道なし、閉包は閉じている | 観察（有限の模型の全数計算。閉性は総当たりで確認） | 全ての m については命題5が与える |
| 命題6：M4 の閉包は重み 2^m の全ての並べ方の集合 T(2^m) に等しい（m ≤ 3） | m ≤ 3 で証明済み（計算）。一般の m は ⊆ だけ証明済み（命題5）、= は未解決 | 「任意のずれの位置に逃げ道がある」ことを言語が含まねばならない |
| **補題7・7′（逃げ道の因子の一致による近道）**：親の逃げ道が e_C = s·e_B（または e_B·s）で s が c を含まないとき、1段（内容がそろう場合）または2段で近道 | 証明済み（トークンの証明書、任意の内容を保つ非消去準同型で持ち上がる） | (150) の一般化。L_3..L_7 で持ち上げて再生 |
| 具体的な倍増族 m = 3 の七つの設計は全て近道を持つ | 観察（証明書は再生済み） | 一つ一つの近道は正しい（証明書は健全）。「近道がない」側の主張はしていない |
| 具体的な倍増族 m = 2 の全ての (e_1, e_2)（長さ ≤ 3）：625 組中 431 組は閉包が閉じ近道なし、66 組は近道、124 組は切った範囲で近道なし、4 組は打ち切り | 観察 | m = 2 は小さすぎて漸近の情報はない |
| m = 3 の網羅探索（\|e_1\| ≤ 2、\|e_2\|, \|e_3\| ≤ 3）：閉じたのは 17 通りで全て退化（e_2 = e_1e_1）、近道 1349、打ち切り 1159 | 観察 | §5.3。打ち切りがあるので「非退化の閉じた設計はない」とは主張しない |
| (H)「侵入節点が多いと近道が強制される」を逃げ道の近傍だけから導くこと | **反証**（命題5） | 言語についての (H) そのものは反証していない |
| 言語についての (H)、μ_{ab} ≤ poly_r(v,θ) | 未解決 | |
| 反例（所属・下界・文法の大きさ） | 構成していない | |
| 文献上の新規性 | 未確認 | 命題5の原理（加法的な重みの水準集合は代入可能）は初等的で、既知の可能性が高い |

範囲の注意：以下の結果は全て**開始の型 {a,b}**（μ_{ab}）についてで、成分の一方だけが ab の型付き非終端や、他の欠けた型、τ には広げない。

---

## 1. 設定と記号

Σ = {a,b,c}、c は内容型付け、L ∈ C_{2,c}、G は L∩Σ⁺ の reduced good な表示（ファンアウト ≤ 2、ランク ≤ r）、v = |V|、θ = θ̄_G。原稿 `lem:thickness-equivalence` により、各規則が直接書く終端は θ 個以下で、各非終端 B は総長 θ 以下の生成 ω_B を持つ。

W を内容がちょうど {a,b} の最短の語、T を W の導出のうち節点数が最小のものとする。節点 u の生成の総長を ℓ_u、非終端を B_u と書き、ℓ_u > θ のとき u は**重い**。

**SUB 規則**（d = 1, 2）：E[x], E[y], F[x] ∈ L、x, y ∈ (Σ⁺)^d の成分ごとの内容が等しく、E, F が許容（d = 2 なら中央が空でない）なら F[y] ∈ L。L ∈ C_{2,c} なら健全（`def:class-cmcf` からすぐ）。

**定義。** 重い節点 u が **c で強制される**とは、B_u の生成 z で ‖z‖_1 < ℓ_u のものが全て、どれかの成分に c を含むことをいう。u が **a の保持者**とは、W の a の出現が全て u の生成の中にあることをいう（b も同様）。

c で強制される重い節点は、依頼文の「侵入節点」（長さ θ 以下の生成が全て c を含む）でもある（ℓ_u > θ だから）。だから下の q は侵入反鎖の幅以下である。

---

## 2. 侵入への帰着の確認（依頼 3-1）

### 2.1 補題1（帰着）

**補題1（証明済み）。** (i) 重い節点は、c で強制されるか、a か b の保持者である。(ii) 保持者は根から下る高々二本の道に並ぶ。(iii) T の一本の道の節点は 3v 個以下。(iv) q を c で強制される重い節点の反鎖の最大の大きさとすると、
\[ \mu_{ab}(L)=|W|\le 3(r+1)\,v\,\theta\,(q+2). \]

*証明。* (i) u が c で強制されないなら、B_u の生成 z で c を含まず ‖z‖_1 < ℓ_u のものがある。u の部分木を z の導出に替えた導出は成功し（文脈自由な置き換え）、語 W′ ∈ L を作る。非削除性により W′ の文字は W の u の外の文字と z の文字なので c を含まず、|W′| < |W|。W は最短の ab 語なので W′ の内容は {a} か {b} であり、例えば b が消えたなら W の b は全て u の中にあった。

(ii) 比較不能な二つの節点の生成は W の位置の互いに素な集合を占める（線形・非削除）。a の出現は一つ以上あるので、a の保持者は互いに比較可能で、祖先に閉じている。よって一本の道をなす。b も同様。

(iii) 節点に状態 σ(u) = (u が a の保持者か, u が b の保持者か) ∈ {0,1}² を付ける。u が u′ の真の祖先で、B_u = B_{u′}、σ(u) = σ(u′) とする。u の部分木を u′ の部分木に替えると W″ ∈ L(G)、|W″| ≤ |W|、節点は減り、c は現れない。a について：u が a の保持者でなければ u の外に a が残り、保持者なら u′ も保持者なので a は u′ の中に残る。b も同様。よって W″ は ab 語で、T の選び方（最短、その中で節点数最小）に反する。下る道の上で σ の各成分は 1 から 0 へ一度しか変わらないので、道は σ が一定の区間高々 3 個に分かれ、各区間で非終端は繰り返さない。よって 3v 個以下。

(iv) 重い節点は祖先に閉じ、同じ深さの重い節点は反鎖をなす。その中の保持者は (ii) により高々 2 個、残りは (i) により c で強制される。よって重い節点は 3v(q+2) 個以下。根が重くなければ |W| ≤ θ。重ければ、W の各文字は重い節点が書くか、重い節点の重くない子（各々 r 個以下、総長 θ 以下）の中にある。各節点が直接書く文字は θ 以下なので |W| ≤ (r+1)θ·3v(q+2)。∎

**(138) との関係。** (138) は型付き非終端一般について τ_X ≤ 49(r+1)vθ(3d+q_X) を出した。開始の型（d = 1、π は自明）では補題1はその特別な場合で、印を使わず保持者の道を使うので定数が小さい。**新しい上界ではなく、残る量 q の定式化を確かめたもの**である。

### 2.2 補題2（同名の等長）

**補題2（証明済み）。** u, u′ が比較不能な重い節点で、どちらも保持者でなく、B_u = B_{u′} なら ℓ_u = ℓ_{u′}。

*証明。* u の部分木を u′ の部分木の写しに替える。u は保持者でないので u の外に a と b が残り、結果は c を含まない ab 語、長さ |W| − ℓ_u + ℓ_{u′}。W の最短性から ℓ_{u′} ≥ ℓ_u。対称に ≤。∎

よって q ≤ v·h（h：同じ非終端の、c で強制される重い節点の反鎖の最大の大きさ）。

### 2.3 配置 π とファンアウト2の二成分

開始記号はファンアウト1なので、根の成分は一つで、配置 π は自明である。T の中のファンアウト2の節点は、二つの成分がどちらも W の中に置かれる。補題1・2の議論は「生成の文字が占める位置の集合」と「総長」しか使わないので、二成分でもそのまま通る。逃げ道 ω_B が一方の成分だけ c を含む（他方は c を含まない短い語）場合も、「どれかの成分が c を含む」ので c で強制される。成分ごとの長さは同名の節点で違ってよい（補題2は総長だけを言う）。この点は命題5で使う重みの分け方に影響しない（§4.1）。

一方、**型付き非終端で d = 2 の場合**（τ の問い）は π が本当に要る。本報の範囲外である。

### 2.4 補題3（最小性の伝播）

**補題3（証明済み、自明）。** d ∈ {1,2}、W = F[x]（F は W から作った許容文脈）とする。許容文脈 E と、x と成分ごとに内容の等しい y について E[x], E[y] ∈ L なら ‖y‖_1 ≥ ‖x‖_1。

*証明。* SUB により F[y] ∈ L。F の固定部分は W の一部なので c を含まず、F[y] の内容は W の内容 {a,b} に等しい。長さは |W| − ‖x‖ + ‖y‖ なので、W の最短性から従う。∎

支持集合の不変性（§2.5）と合わせると、**W より短い ab 語を強制する証明書の最後の段は必ず補題3に反する形**、つまり「c を含みうる共通の枠 E が、内容の同じ二つの c を含まない埋め草を受け入れ、長い方が ab 語の因子になっている」。依頼文の言う「橋」はこの枠 E である。

### 2.5 `lem:app-two-insertion` の移植と、支持集合の不変性

**補題4（証明済み、移植）。** Q を c で強制される重い節点の反鎖とする。Q の部分集合 I で |I| ≥ ⌈|Q|/(2f+1)⌉（f = 2 なら |Q|/5）のものがあって、I の全ての節点を同時に ω に替えた語 W_I ∈ L は、I の節点の数以上の c の連を持ち、違う節点が作った c の連の間には W の文字（a か b）が少なくとも一つある。

*証明。* 付録の証明と同じく、二つの節点の「塊」（根の成分の中で一つの節点の成分が占める区間）が間に文字なしで隣り合うとき辺を引くと、次数は 2f 以下なので、大きさ |Q|/(2f+1) 以上の独立集合 I がある。c で強制されるので ‖ω‖ ≤ θ < ℓ_h から各 ω は c を含み、各節点は c の連を少なくとも一つ作る。I の違う節点の塊の間は、空でない隙間か、I の外の節点の塊（置き換えず、c を含まず、λ-free で空でない）で隔てられる。印は要らない（W_I の内容を保つ必要がない）。∎

**移らない部分。** 二文字の付録は、W_I（同じ二文字の上の語）に連の交換（`lem:app-two-runs`）を当てて矛盾を出す。三文字では W_I の内容は {a,b,c} で、次の補題により、W_I から始めて c を含む語だけを渡る段では ab 語に戻れない。

**(143) 補題2.1（独立に確認）。** 一段の SUB で F[x] から F[y] を得るとき、supp(F[y]) = supp(F[x])。*証明*：穴の外は同じ、各成分の内容も同じなので、和集合も同じ。∎

したがって ab 語の強制には、F[x] が ab 語である段（補題3の形）が必ず要る。さらに c^4 が現れなければ c の連を融合する道具もなく、W_I に c の連が多いこと自体は L の性質と矛盾しない（例えば (abc)^n 型の語は c の連をいくらでも持つ）。

---

## 3. 計算の方法（依頼 3-2）

- **規則**：§1 の SUB_1、SUB_2 だけ。トークンには意図する内容（{a,b,c} の部分集合）を付け、語の内容は和集合とする。
- **閉包**：長さの上限（cap）以下の語だけを加える。同じ (文脈, 型) を共有する組を「相手」として記録し、相手の文脈を全て移す。各新語に一段の証明書 (d, E, x, y, F) を残す。近道（W より短い ab 語）が出たら止める。
- **再生**：別の関数 `replay` が、種から順に、各段の三つの前提が既にあること、成分が空でないこと、二穴の中央が空でないこと、内容が等しいことを確かめる。報告する全ての近道は、必要な段だけを取り出して再生した。
- **閉性**：`is_closed` は上限なしの総当たりで、有限集合 S が全ての SUB_1・SUB_2 の段で閉じているかを調べる（S の全ての出現を数え上げ、同じ (文脈, 型) の組の文脈の集合が包含し合うかを見る）。「閉じている」と書いたものは全てこの関数で確かめた。閉じた S は (2,c) 代入可能な有限言語そのものなので、その種からはどんな長さの証明書でも S の外の語は出ない。
- **区別**：「近道が強制された」は上限で切っても正しい（証明書を再生した）。「近道がない」は、閉性を確かめた場合だけ全ての証明書についての主張で、閉じていない場合（表の capped / stopped）は切った範囲での観察にすぎない。
- **持ち上げ**：トークンの証明書は、各トークン t を内容が cont(t) にちょうど等しい空でない語に写す準同型 h で持ち上がる（内容が等しい組は等しいまま、空でない成分と中央は空でないまま）。必要なのは h(種) ⊆ L だけ。Part E では、持ち上げた前提が L_n に入ることを文法で厳密に判定した（長さで切った集合は使わない）。

---

## 4. トークンの障壁（依頼 3-4 の否定の側）

### 4.1 命題5

**命題5（証明済み）。** トークンの字母 Γ = Γ₀ ⊔ Γ₁ に、内容 cont(t)（Γ₀ では c を含まない、Γ₁ では含む）と正の重み λ(t) を与え、加法的な φ: Γ* → ℕ を作る。W_tok ∈ Γ₀⁺ と種の集合 𝒮 ⊆ Γ⁺ が φ(s) = φ(W_tok) (s ∈ 𝒮) を満たすとする。

(i) Λ := φ^{−1}(φ(W_tok)) は、全ての arity と全ての型付けについて代入可能である。特に SUB_1・SUB_2 で閉じ、𝒮 の閉包は Λ に含まれる。
(ii) h を持ち上げの準同型とし、t ∈ Γ₀ では λ(t) = |h(t)| とする。Λ の c を含まない語 w は |h(w)| = φ(w) = |W| を満たす。
(iii) よって、Γ の上で 𝒮 から始まる証明書は、持ち上げても W より短い ab 語を作らない。

*証明。* (i) x, y が共通の文脈 E を持ち E[x], E[y] ∈ Λ なら、φ の加法性から Σφ(x_i) = Σφ(y_i)。すると任意の F について F[x] ∈ Λ ⇔ F[y] ∈ Λ。型の条件は使わない。(ii) は定義から。(iii) 証明書の全ての語は 𝒮 の閉包の中、つまり Λ の中にある。∎

**逃げ道の近傍は仮定を満たす。** 種を「W の互いに素な、保持者でない重い節点の生成を、それぞれその非終端の別の生成（逃げ道など）で置き換えた語」とする。生成ごとにトークンを一つ割り当て、置き換えた節点の総長 ℓ_u をそのトークン（ファンアウト2なら二つのトークンに任意に分けて）の重みにする。同じトークンが違う ℓ の節点に使われないことは、補題2（同名なら同じ ℓ）が保証する。入れ子の置き換え（反鎖の選び方）も同じ。

**意味。** 侵入節点がいくら多くても（M4 では反鎖の幅 2^m）、**逃げ道を中身の見えない記号として扱う議論では近道は出ない**。依頼の仮説 (H) の前半「c を含む短い逃げ道どうしが共通の文脈を持つ組が現れる」は実際に起きる（M4 では閉包が種より大きくなる。二穴のスロット移送）。しかしそれらの比較は全て重みを保つので、後半「近道の二段で短い ab 語」は起きない。近道には、**重み（長さの帳尻）が一つの語の二通りの読み方で食い違う、文字の段階の一致**が要る。

### 4.2 計算による確認（Part B, C, D）

| 模型 | 内容 | 結果 |
|---|---|---|
| M1：W = s₀ y s₁ y s₂ (y s₃)、同名の穴 2・3 個、逃げ道 e | 区切りの有無・内容・y と e の内容の全ての組 | 4272 通り全てで近道なし、全て閉じている（区切りを一つのトークンにした k = 3 の 24 通りでは、同じ長さの別の ab 語が現れる） |
| M3：ファンアウト2の節点 (y,z)、逃げ道 (e,f)、二つの同名節点を seq / cross / nest に配置 | 一方の成分の逃げ道が c を含まない場合も含む | 8920 通り全てで近道なし、全て閉じている |
| M4：一様な倍増木、各段に逃げ道 E_i、葉 z | 逃げ道の内容 {c} と {a,b,c}、深さ m = 1,2,3 | 近道なし、閉じている。ab 語は z^{2^m} だけ |

### 4.3 命題6（M4 の閉包は全てのずれを含む）

**命題6。** M4（重み λ(z) = λ(E_0) = 1、λ(E_i) = 2^i）の種の閉包は、重み 2^m のトークン列全体 T(2^m) に等しい（m = 1, 2, 3 で計算により証明。大きさは 5, 30, 1118）。一般の m では閉包 ⊆ T(2^m) だけが証明済み（命題5）。

T(2^m) の語は、各段の逃げ道を**木の区切りにそろわない任意の位置**に置いたものを含む（例：m = 2 で zFz、F は二つの葉の逃げ道）。したがって、この近傍を持つ C_{2,c} の言語は（トークンの写しとして）任意のずれの位置の逃げ道を含まねばならない。(149) の二穴のスロット移送の一般形である。

---

## 5. 近道を生む一致（依頼 3-3, 3-4 の肯定の側）

### 5.1 補題7・7′（逃げ道の因子の一致）

**補題7（証明済み、1段）。** T に節点 v（非終端 C）があり、その生成が隣り合う二つの子 u, u′ の生成 Y, Y′ からなり（ファンアウト1）、W = l·Y·Y′·r とする。β を B_{u′} の生成（例えば逃げ道）とし、L が l·s·β·r を含むとする（s ∈ {a,b}⁺、例えば親の逃げ道が e_C = s·β のとき、v を e_C に替えた語）。content(l s) = content(l Y) かつ |s| < |Y| なら、l·s·Y′·r ∈ L は W より短い ab 語である。

*証明。* E = (□, β r) は l Y（u′ を β に替えた語）と l s を受け入れる。内容が等しいので SUB_1 により、F = (□, Y′ r)（F[lY] = W）から F[ls] = l s Y′ r ∈ L。長さは |W| − |Y| + |s|。∎ 鏡像（β を左の子 u の生成とし、L が l·β·s·r を含む場合、例えば e_C = β·s）は、content(s) = content(Y′) なら枠 (l β, r) が Y′ と s を受け入れるので l·Y·s·r ∈ L（長さ |W| − |Y′| + |s|）。e_C が長さ θ 以下の生成なら |s| < |e_C| ≤ θ < ℓ_u なので、u が重ければ長さの条件は自動的に成り立つ。

**補題7′（証明済み、2段。(150) の一般化）。** l = r = 空で、content(s) ≠ content(Y) のとき（(150) では s = a、Y の内容は {a,b}）。W = U Z U Z で、二つの子 u, u′ の生成がどちらも U·Z、Z が右の子 u′ の子孫 w（非終端 D、逃げ道 e_D）の生成、β が u, u′ の非終端の生成（逃げ道）とし、次を仮定する：content(β) = content(U e_D)、content(sU) = content(UZU)、|s| < |UZ|。前提の語 ββ, βUe_D, UZUZ, UZUe_D, sβ が L に入るなら、sUZ ∈ L（W より短い ab 語）。

*証明（トークンの証明書、Part E）。* 段1：E = (β, □) は β と U e_D を受け入れる（内容が等しい）。F = (s, □) で F[β] = sβ ∈ L から sUe_D ∈ L。段2：E = (□, e_D) は UZU と sU を受け入れる（内容が等しい）。F = (□, Z) で F[UZU] = W から sUZ ∈ L。∎

L_n（(149)）は i = n−1、U = (ab)^{2^i−2}、Z = abab、e_D = abc、β = a^i cb、s = a の場合で、持ち上げた前提が L_n に入ることを n = 3..7 で文法から厳密に確かめ、再生した（付録 B、Part E）。強制された ab 語の長さは 2^n + 1 で、(150) と一致する。外側の文脈 l, r（内容 {a,b}）がある場合は、内容がそろうので補題7の1段で済む。補題7の二つの向き（e_C = e_B·s と s·e_B、content(s) = content(Y)）も、トークンの1段の証明書として Part E で再生した（トークン列の長さでは近道に見えないので、Y を重いトークンとして重みで判定した）。

逆に、Part E で e_C を β と無関係なトークンにすると、同じ種の閉包は 10 語で閉じ、近道はない（命題5の通り）。**近道の原因は e_C = s·β という文字の段階の一致そのもの**である。

### 5.2 具体的な倍増族の逃げ道の設計（Part F, G）

文法 A_0 → ab、A_i → A_{i−1}A_{i−1} | e_i（1 ≤ i ≤ m）、開始は A_m。L(G) は有限なので種は L(G) 全体、上限は |W|+1。

| 設計 e_i | m = 2 | m = 3 | m = 3 の最後の段（E, x, y） | 一致の種類 |
|---|---|---|---|---|
| c^i | 閉 | 近道（2段） | (□, abcc), ababab, ab | c の連の重なり（cc と c の比較） |
| a^{i−1}c | 閉 | 近道（1段） | (cab, c), ababab, aba | e_2 = a·e_1（補題7） |
| c a^{i−1} | 閉 | 近道（1段） | (c, abc), ababab, aab | e_2 = e_1·a（補題7の鏡像） |
| c b^{i−1} | 閉 | 近道（1段） | (c, babc), ababa, ba | e_2 = e_1·b |
| b^{i−1}c | 閉 | 近道（1段） | (cab, bc), ababa, ab | e_2 = b·e_1 |
| c(ab)^{i−1} | 近道（1段） | 近道（1段） | (c, cc), abab, ab | e_2 = e_1·ab（m = 2 で既に） |
| a c^i b | 閉 | 近道（2段） | (ac, cbaccb), baba, ba | 段1で c の連がそろい、段2で枠が共有される |

「閉」は閉包が閉じて近道がないことを総当たりで確かめたもの（m = 2 は小さく、漸近の情報はない）。m = 3 の近道は全て証明書を再生した。

**m = 2 の網羅（Part G）。** |e_1|, |e_2| ≤ 3 の c を含む語の全 625 組で、閉じて近道なし 431、近道 66、切った範囲で近道なし 124、語数の上限で打ち切り 4。

### 5.3 m = 3 の網羅探索（`search_m3_escapes.py`）

手順：|e_1| ≤ 2、|e_2| ≤ 3 の c を含む語の全 150 組を m = 2 で調べ、閉包が閉じたもの 101 組を残す。その各組に |e_3| ≤ 3 の全 25 語を付けて m = 3（|W| = 16）で調べた（計 2525 通り、上限 |W|+1、1 回あたり 1500 語または 20 秒で打ち切り）。

| 結果 | 数 | 意味 |
|---|---|---|
| 近道（証明書を再生） | 1349 | W より短い ab 語が強制される |
| 閉じていて近道なし | 17 | 種の閉包が閉じている（総当たりで確認）。これらの種からはどんな証明書でも近道は出ない |
| 打ち切り | 1159 | 判定できない（観察なし） |

閉じた 17 通りは**全て (e_1, e_2) = (c, cc)** で、e_3 だけが違う。このとき e_2 = e_1e_1 は「A_2 の二つの子を両方逃がした語」と同じ語なので、A_2 の逃げ道は新しい枠を作らない。また最上段の逃げ道 e_3 は語全体としてしか現れない。つまり**独立な逃げ道を持つ段は実質的に一つ**で、漸近の情報はない（e_i = e_{i−1}e_{i−1} を続けると逃げ道の長さが 2^{i−1} になり、θ = poly(m) に反する）。

したがって、この範囲では「二つ以上の段が独立な逃げ道を持ち、閉包が閉じる」設計は見つからなかった。打ち切りが 1159 通りあるので、これは**探索した範囲での観察**にすぎず、そのような設計が存在しないことの証明ではない。

---

## 6. (H) の判定と、反例の設計図（依頼 3-4）

**(H) の判定。**
- 「侵入節点（反鎖）が多い」ことと、逃げ道の近傍の情報（どの節点をどの生成に替えても L に入る）**だけから** (H) を導くことは**できない**（命題5）。これは反鎖の幅や、ファンアウト、入れ子の深さによらない。
- したがって (H) を証明するなら、逃げ道や生成の**文字の並び**を見る議論（語の組合せ論）か、近傍の外の L の語を使う議論が要る。見つかった近道は全て、一つの語が二通りに読めて長さの帳尻が合わない形（補題3の違反）だった。その典型は逃げ道の因子の一致（補題7・7′）、c の連の重なり、段をまたいだ逃げ道の接頭・接尾の一致である。
- 言語についての (H) は未解決。多項式の閾値も出ていない。

**反例の設計図（命題5・6から）。** 近道を生まない配置の骨格は、トークンの段階では「加法的な重みの一水準」で、倍増なら T(2^m)（任意のずれの位置に逃げ道を置いた語全体）である。これを反例にするには、次の三つが全て要る。

- (D1) **符号化**：各段の逃げ道を長さ θ 以下の具体的な c を含む語にし、文字の段階の一致（補題7・7′の形、c の連の重なり、段をまたぐ接頭・接尾の一致）を一つも起こさないこと。言い換えると、L の c を含む語の全てに「仮想の長さ」（それが置き換えている ab 語の長さ）を矛盾なく割り当てられ、どの c を含む枠でも、内容の同じ c を含まない埋め草の長さが仮想の長さで決まること。
- (D2) **ずれの位置の逃げ道**：T(2^m) の写し（スロット移送が強制する全ての位置の逃げ道）を含むこと。
- (D3) **小さい文法**：ファンアウト ≤ 2、規則の厚さ θ = poly(m)、大きさ poly(m) の表示を持つこと。所属（C_{2,c}）は文法から証明すること。

**壊れる場所（現時点で分かっていること）。**
- (D1)：単純な逃げ道の族は m = 3 で全て (D1) に反した（§5.2）。短い逃げ道の網羅（§5.3）でも、二つ以上の段が独立な逃げ道を持って閉包が閉じる設計は見つからなかった（打ち切りを除く）。
- (D1) と加法性（初等的に証明済み）：仮想の長さが文字の加法的な重み λ で与えられるとする。c を含まない語では長さに一致するので λ(a) = λ(b) = 1。段 i の逃げ道 e_i（c を含み、長さ θ 以下）は λ(e_i) = 2^i ℓ_0（ℓ_0 ≥ 1 は葉の長さ）を満たさねばならない。λ(c) ≥ 1 なら λ(c) ≤ λ(e_1) = 2ℓ_0 かつ 2^m ℓ_0 = λ(e_m) ≤ θλ(c) なので 2^{m−1} ≤ θ。λ(c) < 1 なら 2^m ℓ_0 = λ(e_m) ≤ |e_m| ≤ θ。いずれも m ≤ log₂θ + 1。だから深い倍増では仮想の長さは文字の上で加法的でありえず、非加法性が文字の段階の一致を生みやすい（これは動機であって証明ではない）。関連する厳密な結果に (100) の定理3.1（加法的な重みの一水準では純粋な a 語が多項式）がある。**その ab 語版は本報では確かめていない。**
- (D3)：T(2^m) の写しを含む小さい低い厚さの文法があるかは未解決。

---

## 7. まとめ（依頼 3-5）

**証明できたこと。**
1. 補題1：μ_{ab} ≤ 3(r+1)vθ(q+2)（(138) の特別な場合、保持者の道で印を不要にした）。補題2：q ≤ v·h。
2. 補題3・(143) 補題2.1：近道の証明書の最後の段は、c を含みうる共通の枠が長さの違う c を含まない埋め草を受け入れる形しかない。
3. 補題4：`lem:app-two-insertion` の数える部分の移植（矛盾を出す部分は移らない）。
4. **命題5：トークンの障壁。** (H) を逃げ道の近傍だけから導く道は閉じている。命題6：倍増の近傍は任意のずれの位置の逃げ道を強制する（m ≤ 3）。
5. **補題7・7′：逃げ道の因子の一致による近道**（(150) の一般化、L_3..L_7 で持ち上げて再生）。

**止まった場所。** 侵入節点が多いとき、三文字の上で文字の段階の一致（補題3の違反）が**必ず**起きることを示す議論がない。逆に、(D1)–(D3) を満たす族も見つけていない。

**次に絞るべき一点。** **c を含む枠の長さの剛性 (R)**：「L ∈ C_{2,c} の c を含む語の全てに、仮想の長さを矛盾なく割り当てられる」という性質を、三文字・θ 以下の長さの逃げ道で、深さ m の倍増の近傍（命題6の T(2^m) の写しを含む）について調べること。
- 肯定：(R) が m > poly(θ) で必ず破れることを示せば、補題3により近道が出て、倍増型の μ_{ab} は多項式になる。(100) の定理3.1 の「非加法・ab 語」版が候補の道具。
- 否定：(R) を全ての m で保つ逃げ道の族を、m = 4 以上の閉包で確かめる。ただし現在の総当たりの閉包は m = 4（|W| = 32）では重いので、二穴の出現を制限した速い閉包が要る。

---

## 8. 文献

命題5の原理（加法的な重みの水準集合は、どの型付けでも代入可能）と補題3は初等的で、既知の可能性が高い。補題7・7′、命題6の形での記述が文献にあるかは**未確認**（文献検索はしていない）。

---

## 付録 A：スクリプト全文

### `check_claude_mu_ab_2026-11-05.py`

```python
#!/usr/bin/env python3
"""Claude (README (152)): exploration of mu_ab for the rare type {a,b} (content typing, Sigma={a,b,c}).

Single sound rule (SUB_d, d = 1, 2), valid in every L in C_{2,c}:
    E[x], E[y], F[x] in L;  x, y in (Sigma^+)^d with componentwise equal contents;
    E, F admissible (d = 2: the middle fixed part is nonempty)            ==>  F[y] in L.
Abstract letters ("tokens") carry an intended content (a subset of {a,b,c}); the content of a word is
the union.  A certificate over tokens lifts through every nonerasing morphism h with
content(h(t)) = cont[t] for each token t (equal token contents give equal concrete contents,
nonempty components and middles stay nonempty), provided h(seeds) lies in L.

Parts
  A  L_n of reviews/chatgpt_negative_design_2026-11-04.md: closure finds a shorter ab-word (n=3).
  B  token model M1: fan-out 1, k = 2, 3 same-label c-forced slots, all separator patterns.
  C  token model M3: fan-out 2, two same-label nodes, layouts seq / cross / nest.
  D  token model M4: uniform doubling tree with an abstract escape on every level; the closure is
     exactly the weight-level set T(2^m) (m = 1, 2, 3), which is closed.
  E  bridge lemma P (escape of the parent = s . escape of the child): 2-step token certificate,
     lifted to L_n (n = 3..7, exact grammar membership of every lifted premise).
  F  concrete doubling A_0 -> ab, A_i -> A_{i-1}A_{i-1} | e_i: named escape designs, m = 2, 3.
  G  (--full) all escape pairs (e_1, e_2), |e_1| <= 3, |e_2| <= 3, m = 2.
"Closed" is certified by is_closed (brute force, no length cap).  "No shortcut" for a capped
closure that is not closed is only an observation within the cap.
Windows: py -3 check_claude_mu_ab_2026-11-05.py [--full]
"""
import sys
import time
from itertools import product
from functools import lru_cache
from collections import Counter

AB = frozenset('ab')


# ----------------------------------------------------------------------------- engine
def content(w, cont):
    s = set()
    for ch in w:
        s |= cont[ch]
    return frozenset(s)


def fill(E, t):
    return ''.join(e + s for e, s in zip(E, t)) + E[-1]


def occurrences(w):
    n = len(w)
    for i in range(n):
        for j in range(i + 1, n + 1):
            yield (w[i:j],), (w[:i], w[j:])
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                for l in range(k + 1, n + 1):
                    yield (w[i:j], w[k:l]), (w[:i], w[j:k], w[l:])


def closure(seeds, cont, cap, stop=None, max_words=20000, time_limit=None):
    """Saturate under SUB_1/SUB_2, keeping words of length <= cap.  Returns (S, cert, hit);
    hit is the stop word, 'MAX_WORDS' (word or time limit reached) or None (fixpoint under cap)."""
    t_end = None if time_limit is None else time.time() + time_limit
    S, cert, queue = set(seeds), [], sorted(seeds, key=lambda z: (len(z), z))
    ctxs, at, partners = {}, {}, {}
    typ = lambda t: tuple(content(s, cont) for s in t)
    hit = [None]

    def add(w, step):
        if w in S or len(w) > cap:
            return
        S.add(w)
        cert.append(step)
        queue.append(w)
        if stop is not None and stop(w) and hit[0] is None:
            hit[0] = w
        elif len(S) > max_words and hit[0] is None:
            hit[0] = 'MAX_WORDS'

    while queue and hit[0] is None:
        w = queue.pop(0)
        if t_end is not None and time.time() > t_end:
            return S, cert, 'MAX_WORDS'
        for t, E in occurrences(w):
            group = at.setdefault((E, typ(t)), set())
            tc = ctxs.setdefault(t, set())
            tp = partners.setdefault(t, {})
            for t2 in sorted(x for x in group if x != t and x not in tp):
                tp[t2] = E
                partners.setdefault(t2, {})[t] = E
                for F in sorted(tc):
                    add(fill(F, t2), (len(t), E, t, t2, F))
                for F in sorted(ctxs.get(t2, ())):
                    add(fill(F, t), (len(t), E, t2, t, F))
            if E not in tc:
                tc.add(E)
                for t2, E2 in sorted(tp.items()):
                    add(fill(E, t2), (len(t), E2, t, t2, E))
            group.add(t)
            if hit[0] is not None:
                break
    return S, cert, hit[0]


def replay(seeds, cert, cont):
    """Independent re-check of every step from the seeds."""
    S = set(seeds)
    for d, E, x, y, F in cert:
        assert len(E) == len(F) == d + 1 and len(x) == len(y) == d
        assert all(x) and all(y)
        if d == 2:
            assert E[1] and F[1]
        for u, v in zip(x, y):
            assert content(u, cont) == content(v, cont)
        for prem in (fill(E, x), fill(E, y), fill(F, x)):
            assert prem in S, prem
        S.add(fill(F, y))
    return S


def trace(cert, target, seeds):
    produced = {}
    for i, st in enumerate(cert):
        produced.setdefault(fill(st[4], st[3]), i)
    need, idx, seen = [target], set(), set()
    while need:
        w = need.pop()
        if w in seen or w in seeds:
            continue
        seen.add(w)
        i = produced[w]
        idx.add(i)
        d, E, x, y, F = cert[i]
        need += [fill(E, x), fill(E, y), fill(F, x)]
    return [cert[i] for i in sorted(idx)]


def is_closed(S, cont):
    """Brute force, no cap: None iff every SUB_1/SUB_2 step with premises in S concludes in S."""
    ctx = {}
    for w in S:
        for t, E in occurrences(w):
            ctx.setdefault(t, set()).add(E)
    groups = {}
    for t, Es in ctx.items():
        ty = tuple(content(s, cont) for s in t)
        for E in Es:
            groups.setdefault((E, ty), []).append(t)
    for (E, ty), ts in groups.items():
        for x in ts:
            for y in ts:
                if x != y and not ctx[x] <= ctx[y]:
                    return (len(x), E, x, y, min(ctx[x] - ctx[y]))
    return None


def shorter_ab(W, cont):
    return lambda w: content(w, cont) == AB and len(w) < len(W)


def lift(cert, h):
    H = lambda s: ''.join(h[c] for c in s)
    return [(d, tuple(map(H, E)), tuple(map(H, x)), tuple(map(H, y)), tuple(map(H, F)))
            for d, E, x, y, F in cert]


CONC = {ch: frozenset(ch) for ch in 'abc'}


# ----------------------------------------------------------------------------- part A
def ln_escape(i):
    return 'abc' if i == 1 else 'a' * i + 'cb'


def ln_member(n, word):
    @lru_cache(None)
    def inside(i, w):
        if i == 0:
            return w == 'ab'
        if w == ln_escape(i):
            return True
        return any(inside(i - 1, w[:k]) and inside(i - 1, w[k:]) for k in range(1, len(w)))
    return inside(n, word)


def ln_words(n):
    lev = {'ab'}
    for i in range(1, n + 1):
        lev = {ln_escape(i)} | {p + q for p in lev for q in lev}
    return lev


def part_A():
    print('== A: L_n (README (149)); L_2 is not closed; closure of the finite language L_3')
    L2 = ln_words(2)
    viol = is_closed(L2, CONC)
    d, E, x, y, F = viol
    print('   L_2 violation d=%d E=%s x=%s y=%s F=%s: F[y]=%s in L_2: %s'
          % (d, E, x, y, F, fill(F, y), ln_member(2, fill(F, y))))
    assert all(ln_member(2, w) for w in (fill(E, x), fill(E, y), fill(F, x)))
    n = 3
    L, W = ln_words(n), 'ab' * 2 ** n
    S, cert, hit = closure(L, CONC, cap=len(W), stop=shorter_ab(W, CONC))
    tr = trace(cert, hit, L)
    replay(L, tr, CONC)
    for d, E, x, y, F in tr:
        print('   step d=%d E=%s x=%s y=%s F=%s -> %s (in L_3: %s)'
              % (d, E, x, y, F, fill(F, y), ln_member(n, fill(F, y))))
    print('   forced ab-word %s of length %d < |W| = %d' % (hit, len(hit), len(W)))


# ----------------------------------------------------------------------------- part B
def slot_seeds(seps, slots, esc):
    W = ''.join(s + y for s, y in zip(seps, slots)) + seps[-1]
    seeds = set()
    for ch in product((0, 1), repeat=len(slots)):
        seeds.add(''.join(s + (esc if c else y) for s, y, c in zip(seps, slots, ch)) + seps[-1])
    return W, seeds


C1 = {'a': frozenset('a'), 'b': frozenset('b'), 'ab': frozenset('ab')}
CE = {'c': frozenset('c'), 'ac': frozenset('ac'), 'bc': frozenset('bc'), 'abc': frozenset('abc')}


def part_B():
    print('== B: token model M1 (fan-out 1, k same-label slots y, escape e)')
    for k in (2, 3):
        for same in (False, True):
            tot = hit = closed = other = 0
            for pres in product((0, 1), repeat=k + 1):
                for sc in product(('a', 'b', 'ab'), repeat=sum(pres)):
                    for yc in C1:
                        for ec in CE:
                            cont, seps, it, bad = {}, [], iter(sc), False
                            for i, p in enumerate(pres):
                                if not p:
                                    seps.append('')
                                    continue
                                L = 'p' if same else 'pqrs'[i]
                                c = C1[next(it)]
                                if L in cont and cont[L] != c:
                                    bad = True
                                cont[L] = c
                                seps.append(L)
                            if bad:
                                continue
                            cont['y'], cont['e'] = C1[yc], CE[ec]
                            W, seeds = slot_seeds(seps, ['y'] * k, 'e')
                            if content(W, cont) != AB:
                                continue
                            S, cert, h = closure(seeds, cont, cap=2 * len(W) + 2,
                                                 stop=shorter_ab(W, cont))
                            tot += 1
                            if h:
                                hit += 1
                                continue
                            closed += is_closed(S, cont) is None
                            other += sum(1 for w in S if content(w, cont) == AB) > 1
            print('   k=%d separators %-9s configs=%4d shortcut=%d closed=%4d '
                  'with another ab-word (same length)=%d'
                  % (k, 'one token' if same else 'distinct', tot, hit, closed, other))


# ----------------------------------------------------------------------------- part C
LAYOUTS = {'seq': ['y1', 'z1', 'y2', 'z2'], 'cross': ['y1', 'y2', 'z1', 'z2'],
           'nest': ['y1', 'y2', 'z2', 'z1']}


def part_C():
    print('== C: token model M3 (fan-out 2: node yields (y,z), escape (e,f), two same-label nodes)')
    allc = dict(C1)
    allc.update(CE)
    for lay, order in LAYOUTS.items():
        tot = hit = closed = 0
        for pres in [(1, 1, 1, 1, 1), (0, 1, 1, 1, 0), (0, 0, 1, 0, 0), (0, 0, 0, 0, 0), (1, 0, 0, 0, 1)]:
            if any(order.index('z' + i) == order.index('y' + i) + 1 and not pres[order.index('z' + i)]
                   for i in '12'):
                continue                      # components of one node are never adjacent
            for sc in {('ab',) * sum(pres), ('a',) * sum(pres),
                       tuple(('a', 'b')[i % 2] for i in range(sum(pres)))}:
                for yc, zc in product(C1, repeat=2):
                    for ec, fc in product(allc, repeat=2):
                        if ec in C1 and fc in C1:
                            continue          # a c-forced node: every short yield contains c
                        cont = {'y': C1[yc], 'z': C1[zc], 'e': allc[ec], 'f': allc[fc]}
                        seps, it = [], iter(sc)
                        for i, p in enumerate(pres):
                            if p:
                                cont['pqrst'[i]] = C1[next(it)]
                                seps.append('pqrst'[i])
                            else:
                                seps.append('')
                        W = ''.join(s + b[0] for s, b in zip(seps, order)) + seps[-1]
                        if content(W, cont) != AB:
                            continue
                        seeds = set()
                        for ch in product((0, 1), repeat=2):
                            seeds.add(''.join(s + ((('e' if b[0] == 'y' else 'f')
                                                     if ch[int(b[1]) - 1] else b[0]))
                                              for s, b in zip(seps, order)) + seps[-1])
                        S, cert, h = closure(seeds, cont, cap=2 * len(W) + 2,
                                             stop=shorter_ab(W, cont))
                        tot += 1
                        if h:
                            hit += 1
                        else:
                            closed += is_closed(S, cont) is None
        print('   layout=%-5s configs=%4d shortcut=%d closed=%d' % (lay, tot, hit, closed))


# ----------------------------------------------------------------------------- part D
def tree_words(level, leaf, esc):
    if level == 0:
        return {leaf, esc[0]}
    sub = tree_words(level - 1, leaf, esc)
    return {esc[level]} | {p + q for p in sub for q in sub}


def weight_level(N, weights):
    out = {''}
    res = set()
    frontier = {('', 0)}
    while frontier:
        nxt = set()
        for w, s in frontier:
            for t, wt in weights.items():
                if s + wt == N:
                    res.add(w + t)
                elif s + wt < N:
                    nxt.add((w + t, s + wt))
        frontier = nxt
    return res


def part_D():
    print('== D: token model M4 (uniform doubling, escapes E_i of level i, leaf z)')
    for ec in ('c', 'abc'):
        cont = {'z': AB}
        esc = 'EFGH'
        for t in esc:
            cont[t] = frozenset(ec)
        for m in (1, 2, 3):
            seeds = tree_words(m, 'z', esc)
            W = 'z' * 2 ** m
            S, cert, h = closure(seeds, cont, cap=len(W) + 1, stop=shorter_ab(W, cont))
            T = weight_level(2 ** m, dict({'z': 1}, **{esc[i]: 2 ** i for i in range(m + 1)}))
            print('   escapes content %-3s m=%d seeds=%4d closure=%4d shortcut=%s '
                  'closure==T(2^m): %s closed: %s ab-words: %s'
                  % (ec, m, len(seeds), len(S), h, S == T, is_closed(S, cont) is None,
                     sorted(w for w in S if content(w, cont) == AB)))


# ----------------------------------------------------------------------------- part E
def part_E():
    print('== E: bridge lemma P (escape of parent = s . escape of left child)')
    cont = {'U': AB, 'Z': AB, 'e': frozenset('abc'), 'B': frozenset('abc'),
            's': frozenset('a'), 'K': frozenset('abc')}
    W = 'UZUZ'
    gram = {l + r for l in ('UZ', 'Ue', 'B') for r in ('UZ', 'Ue', 'B')}
    for coinc in (False, True):
        seeds = gram | ({'sB'} if coinc else {'K'})
        S, cert, h = closure(seeds, cont, cap=4 * len(W), stop=shorter_ab(W, cont))
        if not h:
            print('   e_C unrelated token K: closure=%d shortcut=None closed=%s'
                  % (len(S), is_closed(S, cont) is None))
            continue
        tr = trace(cert, h, seeds)
        replay(seeds, tr, cont)
        print('   e_C = s.e_B: forced %s in %d steps:' % (h, len(tr)))
        for st in tr:
            print('     ', st)
        prem = set()
        for d, E, x, y, F in tr:
            prem |= {fill(E, x), fill(E, y), fill(F, x)}
        prem &= seeds
        print('   token premises used:', sorted(prem))
        lr = {'l': AB, 'r': AB, 'U': AB, 'Z': AB, 'e': frozenset('abc'), 'B': frozenset('abc'),
              's': frozenset('a')}
        sd = {'l' + a + b + 'r' for a in ('UZ', 'Ue', 'B') for b in ('UZ', 'Ue', 'B')} | {'lsBr'}
        S2, c2, h2 = closure(sd, lr, cap=14, stop=shorter_ab('lUZUZr', lr))
        t2 = trace(c2, h2, sd)
        replay(sd, t2, lr)
        print('   with outer context l, r (content ab): forced %s in %d step: %s' % (h2, len(t2), t2[0]))
        wt = lambda w: sum(10 if ch == 'Y' else 1 for ch in w)   # Y heavy: |s| < |Y|
        p1 = {'l': AB, 'r': AB, 'Y': AB, 'B': frozenset('c'), 's': AB}
        for nm, extra in (('e_C = e_B.s', 'lBsr'), ('e_C = s.e_B', 'lsBr')):
            sd = {'l' + a + b + 'r' for a in ('Y', 'B') for b in ('Y', 'B')} | {extra}
            S3, c3, h3 = closure(sd, p1, cap=12,
                                 stop=lambda w: content(w, p1) == AB and wt(w) < wt('lYYr'))
            t3 = trace(c3, h3, sd)
            replay(sd, t3, p1)
            print('   lemma 7, %s, content(s)=content(Y): forced %s in %d step: %s'
                  % (nm, h3, len(t3), t3[0]))
        for n in range(3, 8):
            i = n - 1
            hm = {'U': 'ab' * (2 ** i - 2), 'Z': 'abab', 'e': 'abc', 'B': ln_escape(i), 's': 'a'}
            for t, w in hm.items():
                assert content(w, CONC) == cont[t], t
            hseeds = {''.join(hm[c] for c in w) for w in prem}
            assert all(ln_member(n, w) for w in hseeds)
            out = replay(hseeds, lift(tr, hm), CONC)
            last = fill(lift(tr, hm)[-1][4], lift(tr, hm)[-1][3])
            assert last in out and content(last, CONC) == AB
            print('   lifted to L_%d: premises in L_%d (exact), forced ab-word length %d < %d'
                  % (n, n, len(last), 2 ** (n + 1)))


# ----------------------------------------------------------------------------- part F / G
def doubling(m, esc):
    lev = {'ab'}
    for i in range(1, m + 1):
        lev = {esc[i]} | {p + q for p in lev for q in lev}
    return lev


def classify(m, esc, max_words, time_limit=None):
    W = 'ab' * 2 ** m
    seeds = doubling(m, esc)
    S, cert, h = closure(seeds, CONC, cap=len(W) + 1, stop=shorter_ab(W, CONC), max_words=max_words,
                         time_limit=time_limit)
    if h == 'MAX_WORDS':
        return 'stopped', None
    if h:
        tr = trace(cert, h, seeds)
        replay(seeds, tr, CONC)
        return 'shortcut', tr
    return ('closed' if is_closed(S, CONC) is None else 'capped'), None


DESIGNS = {'c^i': lambda i: 'c' * i, 'a^(i-1)c': lambda i: 'a' * (i - 1) + 'c',
           'ca^(i-1)': lambda i: 'c' + 'a' * (i - 1), 'cb^(i-1)': lambda i: 'c' + 'b' * (i - 1),
           'b^(i-1)c': lambda i: 'b' * (i - 1) + 'c', 'c(ab)^(i-1)': lambda i: 'c' + 'ab' * (i - 1),
           'ac^ib': lambda i: 'a' + 'c' * i + 'b'}


def part_F():
    print('== F: concrete doubling, named escape designs e_i (cap |W|+1)')
    for m in (2, 3):
        for name, f in DESIGNS.items():
            esc = {i: f(i) for i in range(1, m + 1)}
            r, tr = classify(m, esc, 6000)
            msg = '   m=%d %-12s %s' % (m, name, r)
            if tr:
                last = tr[-1]
                msg += ' in %d step(s); last step E=%s x=%s y=%s F=%s' % (len(tr), *last[1:])
            print(msg)


def part_G():
    print('== G: concrete doubling m=2, all pairs (e_1, e_2) of c-words of length <= 3 (cap |W|+1)')
    cw = [''.join(p) for n in (1, 2, 3) for p in product('abc', repeat=n) if 'c' in p]
    st = Counter()
    for e1, e2 in product(cw, repeat=2):
        r, tr = classify(2, {1: e1, 2: e2}, 1500)
        st[r] += 1
    print('  ', dict(sorted(st.items())))


if __name__ == '__main__':
    part_A()
    part_B()
    part_C()
    part_D()
    part_E()
    part_F()
    if '--full' in sys.argv:
        part_G()
    print('ALL CERTIFICATES REPLAYED; ALL "closed" CLAIMS CHECKED BY BRUTE FORCE')
```

### `search_m3_escapes.py`

```python
#!/usr/bin/env python3
"""Companion search to check_claude_mu_ab_2026-11-05.py (same engine, imported from it).
Concrete doubling A_0 -> ab, A_i -> A_{i-1}A_{i-1} | e_i.  Step 1: all (e_1, e_2) with |e_1| <= 2,
|e_2| <= 3 at depth m = 2, keeping those whose closure is closed (brute force).  Step 2: for those,
all e_3 with |e_3| <= 3 at depth m = 3.  'shortcut' = a shorter ab-word is forced (certificate
replayed); 'closed' = closure is genuinely closed (no shortcut at all from these seeds);
'capped'/'stopped' = observation within the cap / word limit (1500 words or 20 s per run) only.
Windows: py -3 search_m3_escapes.py   (both files in one folder)"""
import os
import time
import importlib.util
from itertools import product
from collections import Counter

here = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location(
    'chk', os.path.join(here, 'check_claude_mu_ab_2026-11-05.py'))
chk = importlib.util.module_from_spec(spec)
spec.loader.exec_module(chk)

cw = lambda n: [''.join(p) for p in product('abc', repeat=n) if 'c' in p]
t0 = time.time()
pairs = [(e1, e2) for e1 in cw(1) + cw(2) for e2 in cw(1) + cw(2) + cw(3)]
ok2 = [p for p in pairs if chk.classify(2, {1: p[0], 2: p[1]}, 1500)[0] == 'closed']
print('m=2: %d pairs, closed: %d (%.0fs)' % (len(pairs), len(ok2), time.time() - t0), flush=True)
st, surv = Counter(), []
for k, (e1, e2) in enumerate(ok2):
    for e3 in cw(1) + cw(2) + cw(3):
        r, tr = chk.classify(3, {1: e1, 2: e2, 3: e3}, 1500, time_limit=20)
        st[r] += 1
        if r != 'shortcut':
            surv.append((e1, e2, e3, r))
            print('  survivor', (e1, e2, e3, r), flush=True)
    if k % 10 == 9:
        print('  progress %d/%d %s (%.0fs)' % (k + 1, len(ok2), dict(st), time.time() - t0), flush=True)
print('m=3 (|e_3| <= 3): %s (%.0fs)' % (dict(sorted(st.items())), time.time() - t0))
print('closed:', [s[:3] for s in surv if s[3] == 'closed'])
print('capped/stopped:', [s for s in surv if s[3] != 'closed'])
```

## 付録 B：実際の出力（転載、推測なし）

### `py -3 check_claude_mu_ab_2026-11-05.py --full`（Linux の python3 で実行）

```text
== A: L_n (README (149)); L_2 is not closed; closure of the finite language L_3
   L_2 violation d=2 E=('', 'ab', '') x=('ab', 'abab') y=('abab', 'ab') F=('', 'c', ''): F[y]=ababcab in L_2: False
   step d=1 E=('aacb', '') x=('aacb',) y=('abcabc',) F=('a', '') -> aabcabc (in L_3: False)
   step d=1 E=('', 'cabc') x=('ababababab',) y=('aab',) F=('', 'ababab') -> aabababab (in L_3: False)
   forced ab-word aabababab of length 9 < |W| = 16
== B: token model M1 (fan-out 1, k same-label slots y, escape e)
   k=2 separators distinct  configs= 704 shortcut=0 closed= 704 with another ab-word (same length)=0
   k=2 separators one token configs= 200 shortcut=0 closed= 200 with another ab-word (same length)=0
   k=3 separators distinct  configs=2944 shortcut=0 closed=2944 with another ab-word (same length)=0
   k=3 separators one token configs= 424 shortcut=0 closed= 424 with another ab-word (same length)=24
== C: token model M3 (fan-out 2: node yields (y,z), escape (e,f), two same-label nodes)
   layout=seq   configs=2080 shortcut=0 closed=2080
   layout=cross configs=4080 shortcut=0 closed=4080
   layout=nest  configs=2760 shortcut=0 closed=2760
== D: token model M4 (uniform doubling, escapes E_i of level i, leaf z)
   escapes content c   m=1 seeds=   5 closure=   5 shortcut=None closure==T(2^m): True closed: True ab-words: ['zz']
   escapes content c   m=2 seeds=  26 closure=  30 shortcut=None closure==T(2^m): True closed: True ab-words: ['zzzz']
   escapes content c   m=3 seeds= 677 closure=1118 shortcut=None closure==T(2^m): True closed: True ab-words: ['zzzzzzzz']
   escapes content abc m=1 seeds=   5 closure=   5 shortcut=None closure==T(2^m): True closed: True ab-words: ['zz']
   escapes content abc m=2 seeds=  26 closure=  30 shortcut=None closure==T(2^m): True closed: True ab-words: ['zzzz']
   escapes content abc m=3 seeds= 677 closure=1118 shortcut=None closure==T(2^m): True closed: True ab-words: ['zzzzzzzz']
== E: bridge lemma P (escape of parent = s . escape of left child)
   e_C unrelated token K: closure=10 shortcut=None closed=True
   e_C = s.e_B: forced sUZ in 2 steps:
      (1, ('B', ''), ('B',), ('Ue',), ('s', ''))
      (1, ('', 'e'), ('UZU',), ('sU',), ('', 'Z'))
   token premises used: ['BB', 'BUe', 'UZUZ', 'UZUe', 'sB']
   with outer context l, r (content ab): forced lsUZr in 1 step: (1, ('', 'Br'), ('lUZ',), ('ls',), ('', 'UZr'))
   lemma 7, e_C = e_B.s, content(s)=content(Y): forced lsYr in 1 step: (1, ('lB', 'r'), ('Y',), ('s',), ('l', 'Yr'))
   lemma 7, e_C = s.e_B, content(s)=content(Y): forced lsYr in 1 step: (1, ('', 'Br'), ('lY',), ('ls',), ('', 'Yr'))
   lifted to L_3: premises in L_3 (exact), forced ab-word length 9 < 16
   lifted to L_4: premises in L_4 (exact), forced ab-word length 17 < 32
   lifted to L_5: premises in L_5 (exact), forced ab-word length 33 < 64
   lifted to L_6: premises in L_6 (exact), forced ab-word length 65 < 128
   lifted to L_7: premises in L_7 (exact), forced ab-word length 129 < 256
== F: concrete doubling, named escape designs e_i (cap |W|+1)
   m=2 c^i          closed
   m=2 a^(i-1)c     closed
   m=2 ca^(i-1)     closed
   m=2 cb^(i-1)     closed
   m=2 b^(i-1)c     closed
   m=2 c(ab)^(i-1)  shortcut in 1 step(s); last step E=('c', '') x=('abab',) y=('ab',) F=('', 'abab')
   m=2 ac^ib        closed
   m=3 c^i          shortcut in 2 step(s); last step E=('', 'abcc') x=('ababab',) y=('ab',) F=('', 'ababababab')
   m=3 a^(i-1)c     shortcut in 1 step(s); last step E=('cab', 'c') x=('ababab',) y=('aba',) F=('', 'ababababab')
   m=3 ca^(i-1)     shortcut in 1 step(s); last step E=('c', 'abc') x=('ababab',) y=('aab',) F=('', 'ababababab')
   m=3 cb^(i-1)     shortcut in 1 step(s); last step E=('c', 'babc') x=('ababa',) y=('ba',) F=('', 'bababababab')
   m=3 b^(i-1)c     shortcut in 1 step(s); last step E=('cab', 'bc') x=('ababa',) y=('ab',) F=('', 'bababababab')
   m=3 c(ab)^(i-1)  shortcut in 1 step(s); last step E=('c', 'cc') x=('abab',) y=('ab',) F=('', 'abababababab')
   m=3 ac^ib        shortcut in 2 step(s); last step E=('ac', 'cbaccb') x=('baba',) y=('ba',) F=('a', 'bababababab')
== G: concrete doubling m=2, all pairs (e_1, e_2) of c-words of length <= 3 (cap |W|+1)
   {'capped': 124, 'closed': 431, 'shortcut': 66, 'stopped': 4}
ALL CERTIFICATES REPLAYED; ALL "closed" CLAIMS CHECKED BY BRUTE FORCE
```

### `py -3 search_m3_escapes.py`（Linux の python3 で実行）

```text
m=2: 150 pairs, closed: 101 (115s)
  survivor ('c', 'cc', 'c', 'stopped')
  survivor ('c', 'cc', 'ac', 'closed')
  survivor ('c', 'cc', 'bc', 'closed')
  survivor ('c', 'cc', 'ca', 'closed')
  survivor ('c', 'cc', 'cb', 'closed')
  survivor ('c', 'cc', 'aac', 'closed')
  survivor ('c', 'cc', 'aca', 'closed')
  survivor ('c', 'cc', 'acb', 'closed')
  survivor ('c', 'cc', 'acc', 'closed')
  survivor ('c', 'cc', 'bbc', 'closed')
  survivor ('c', 'cc', 'bca', 'stopped')
  survivor ('c', 'cc', 'bcb', 'closed')
  survivor ('c', 'cc', 'bcc', 'closed')
  survivor ('c', 'cc', 'caa', 'closed')
  survivor ('c', 'cc', 'cac', 'closed')
  survivor ('c', 'cc', 'cbb', 'closed')
  survivor ('c', 'cc', 'cbc', 'closed')
  survivor ('c', 'cc', 'cca', 'closed')
  survivor ('c', 'cc', 'ccb', 'closed')
  survivor ('c', 'aca', 'c', 'stopped')
  survivor ('c', 'aca', 'ac', 'stopped')
  survivor ('c', 'aca', 'ca', 'stopped')
  survivor ('c', 'aca', 'aac', 'stopped')
  survivor ('c', 'aca', 'aca', 'stopped')
  survivor ('c', 'aca', 'caa', 'stopped')
  survivor ('c', 'aca', 'cac', 'stopped')
  progress 10/101 {'shortcut': 224, 'stopped': 9, 'closed': 17} (152s)
  survivor ('c', 'bcb', 'c', 'stopped')
  survivor ('c', 'bcb', 'bc', 'stopped')
  survivor ('c', 'bcb', 'cb', 'stopped')
  survivor ('c', 'bcb', 'bbc', 'stopped')
  survivor ('c', 'bcb', 'bcb', 'stopped')
  survivor ('c', 'bcb', 'cbb', 'stopped')
  survivor ('c', 'bcb', 'cbc', 'stopped')
  survivor ('c', 'cac', 'ac', 'stopped')
  survivor ('c', 'cac', 'ca', 'stopped')
  survivor ('c', 'cac', 'acc', 'stopped')
  survivor ('c', 'cac', 'cca', 'stopped')
  survivor ('c', 'cac', 'ccc', 'stopped')
  survivor ('c', 'cbc', 'bc', 'stopped')
  survivor ('c', 'cbc', 'cb', 'stopped')
  survivor ('c', 'cbc', 'bcc', 'stopped')
  survivor ('c', 'cbc', 'ccb', 'stopped')
  survivor ('c', 'cbc', 'ccc', 'stopped')
  progress 20/101 {'shortcut': 457, 'stopped': 26, 'closed': 17} (169s)
  survivor ('ac', 'cc', 'ac', 'stopped')
  survivor ('ac', 'cc', 'ca', 'stopped')
  survivor ('ac', 'cc', 'acc', 'stopped')
  survivor ('ac', 'cc', 'cac', 'stopped')
  survivor ('ac', 'bca', 'ca', 'stopped')
  survivor ('ac', 'bca', 'aac', 'stopped')
  survivor ('ac', 'bca', 'aca', 'stopped')
  survivor ('ac', 'bca', 'acb', 'stopped')
  survivor ('ac', 'bca', 'acc', 'stopped')
  survivor ('ac', 'bca', 'bca', 'stopped')
  survivor ('ac', 'bca', 'cab', 'stopped')
  survivor ('ac', 'bca', 'cac', 'stopped')
  survivor ('ac', 'bcb', 'aac', 'stopped')
  survivor ('ac', 'bcb', 'acc', 'stopped')
  survivor ('ac', 'bcb', 'cab', 'stopped')
  survivor ('ac', 'bcb', 'cba', 'stopped')
  survivor ('ac', 'caa', 'c', 'stopped')
  survivor ('ac', 'caa', 'ac', 'stopped')
  survivor ('ac', 'caa', 'bc', 'stopped')
  survivor ('ac', 'caa', 'ca', 'stopped')
  survivor ('ac', 'caa', 'cb', 'stopped')
  survivor ('ac', 'caa', 'cc', 'stopped')
  survivor ('ac', 'caa', 'aac', 'stopped')
  survivor ('ac', 'caa', 'aca', 'stopped')
  survivor ('ac', 'caa', 'acb', 'stopped')
  survivor ('ac', 'caa', 'acc', 'stopped')
  survivor ('ac', 'caa', 'bbc', 'stopped')
  survivor ('ac', 'caa', 'bca', 'stopped')
  survivor ('ac', 'caa', 'bcb', 'stopped')
  survivor ('ac', 'caa', 'bcc', 'stopped')
  survivor ('ac', 'caa', 'caa', 'stopped')
  survivor ('ac', 'caa', 'cab', 'stopped')
  survivor ('ac', 'caa', 'cac', 'stopped')
  survivor ('ac', 'caa', 'cba', 'stopped')
  survivor ('ac', 'caa', 'cbb', 'stopped')
  survivor ('ac', 'caa', 'cbc', 'stopped')
  survivor ('ac', 'caa', 'cca', 'stopped')
  survivor ('ac', 'caa', 'ccb', 'stopped')
  survivor ('ac', 'caa', 'ccc', 'stopped')
  progress 30/101 {'shortcut': 668, 'stopped': 65, 'closed': 17} (202s)
  survivor ('ac', 'cca', 'c', 'stopped')
  survivor ('ac', 'cca', 'ac', 'stopped')
  survivor ('ac', 'cca', 'bc', 'stopped')
  survivor ('ac', 'cca', 'ca', 'stopped')
  survivor ('ac', 'cca', 'cb', 'stopped')
  survivor ('ac', 'cca', 'cc', 'stopped')
  survivor ('ac', 'cca', 'aac', 'stopped')
  survivor ('ac', 'cca', 'aca', 'stopped')
  survivor ('ac', 'cca', 'acb', 'stopped')
  survivor ('ac', 'cca', 'acc', 'stopped')
  survivor ('ac', 'cca', 'bbc', 'stopped')
  survivor ('ac', 'cca', 'bca', 'stopped')
  survivor ('ac', 'cca', 'bcb', 'stopped')
  survivor ('ac', 'cca', 'bcc', 'stopped')
  survivor ('ac', 'cca', 'caa', 'stopped')
  survivor ('ac', 'cca', 'cab', 'stopped')
  survivor ('ac', 'cca', 'cac', 'stopped')
  survivor ('ac', 'cca', 'cba', 'stopped')
  survivor ('ac', 'cca', 'cbb', 'stopped')
  survivor ('ac', 'cca', 'cbc', 'stopped')
  survivor ('ac', 'cca', 'cca', 'stopped')
  survivor ('ac', 'cca', 'ccb', 'stopped')
  survivor ('ac', 'cca', 'ccc', 'stopped')
  survivor ('ac', 'ccb', 'c', 'stopped')
  survivor ('ac', 'ccb', 'ac', 'stopped')
  survivor ('ac', 'ccb', 'bc', 'stopped')
  survivor ('ac', 'ccb', 'ca', 'stopped')
  survivor ('ac', 'ccb', 'cb', 'stopped')
  survivor ('ac', 'ccb', 'cc', 'stopped')
  survivor ('ac', 'ccb', 'aac', 'stopped')
  survivor ('ac', 'ccb', 'aca', 'stopped')
  survivor ('ac', 'ccb', 'acb', 'stopped')
  survivor ('ac', 'ccb', 'acc', 'stopped')
  survivor ('ac', 'ccb', 'bbc', 'stopped')
  survivor ('ac', 'ccb', 'bca', 'stopped')
  survivor ('ac', 'ccb', 'bcb', 'stopped')
  survivor ('ac', 'ccb', 'bcc', 'stopped')
  survivor ('ac', 'ccb', 'caa', 'stopped')
  survivor ('ac', 'ccb', 'cab', 'stopped')
  survivor ('ac', 'ccb', 'cac', 'stopped')
  survivor ('ac', 'ccb', 'cba', 'stopped')
  survivor ('ac', 'ccb', 'cbb', 'stopped')
  survivor ('ac', 'ccb', 'cbc', 'stopped')
  survivor ('ac', 'ccb', 'cca', 'stopped')
  survivor ('ac', 'ccb', 'ccb', 'stopped')
  survivor ('ac', 'ccb', 'ccc', 'stopped')
  survivor ('ac', 'ccc', 'c', 'stopped')
  survivor ('ac', 'ccc', 'ac', 'stopped')
  survivor ('ac', 'ccc', 'bc', 'stopped')
  survivor ('ac', 'ccc', 'ca', 'stopped')
  survivor ('ac', 'ccc', 'cb', 'stopped')
  survivor ('ac', 'ccc', 'cc', 'stopped')
  survivor ('ac', 'ccc', 'aac', 'stopped')
  survivor ('ac', 'ccc', 'aca', 'stopped')
  survivor ('ac', 'ccc', 'acb', 'stopped')
  survivor ('ac', 'ccc', 'acc', 'stopped')
  survivor ('ac', 'ccc', 'bbc', 'stopped')
  survivor ('ac', 'ccc', 'bca', 'stopped')
  survivor ('ac', 'ccc', 'bcb', 'stopped')
  survivor ('ac', 'ccc', 'bcc', 'stopped')
  survivor ('ac', 'ccc', 'caa', 'stopped')
  survivor ('ac', 'ccc', 'cab', 'stopped')
  survivor ('ac', 'ccc', 'cac', 'stopped')
  survivor ('ac', 'ccc', 'cba', 'stopped')
  survivor ('ac', 'ccc', 'cbb', 'stopped')
  survivor ('ac', 'ccc', 'cbc', 'stopped')
  survivor ('ac', 'ccc', 'cca', 'stopped')
  survivor ('ac', 'ccc', 'ccb', 'stopped')
  survivor ('ac', 'ccc', 'ccc', 'stopped')
  survivor ('bc', 'ac', 'c', 'stopped')
  survivor ('bc', 'ac', 'bc', 'stopped')
  survivor ('bc', 'ac', 'ca', 'stopped')
  survivor ('bc', 'ac', 'cb', 'stopped')
  survivor ('bc', 'ac', 'cc', 'stopped')
  survivor ('bc', 'ac', 'aca', 'stopped')
  survivor ('bc', 'ac', 'acb', 'stopped')
  survivor ('bc', 'ac', 'bbc', 'stopped')
  survivor ('bc', 'ac', 'bca', 'stopped')
  survivor ('bc', 'ac', 'bcb', 'stopped')
  survivor ('bc', 'ac', 'bcc', 'stopped')
  survivor ('bc', 'ac', 'caa', 'stopped')
  survivor ('bc', 'ac', 'cab', 'stopped')
  survivor ('bc', 'ac', 'cba', 'stopped')
  survivor ('bc', 'ac', 'cbb', 'stopped')
  survivor ('bc', 'ac', 'cbc', 'stopped')
  survivor ('bc', 'ac', 'cca', 'stopped')
  survivor ('bc', 'ac', 'ccb', 'stopped')
  survivor ('bc', 'ac', 'ccc', 'stopped')
  survivor ('bc', 'ca', 'abc', 'stopped')
  survivor ('bc', 'ca', 'bbc', 'stopped')
  survivor ('bc', 'ca', 'bca', 'stopped')
  survivor ('bc', 'ca', 'bcc', 'stopped')
  survivor ('bc', 'ca', 'cab', 'stopped')
  survivor ('bc', 'cc', 'c', 'stopped')
  survivor ('bc', 'cc', 'bc', 'stopped')
  survivor ('bc', 'cc', 'cb', 'stopped')
  survivor ('bc', 'cc', 'abc', 'stopped')
  survivor ('bc', 'cc', 'bbc', 'stopped')
  survivor ('bc', 'cc', 'bca', 'stopped')
  survivor ('bc', 'cc', 'bcb', 'stopped')
  survivor ('bc', 'cc', 'bcc', 'stopped')
  survivor ('bc', 'cc', 'cab', 'stopped')
  survivor ('bc', 'cc', 'cbc', 'stopped')
  survivor ('bc', 'cc', 'ccb', 'stopped')
  survivor ('bc', 'aac', 'c', 'stopped')
  survivor ('bc', 'aac', 'ac', 'stopped')
  survivor ('bc', 'aac', 'bc', 'stopped')
  survivor ('bc', 'aac', 'ca', 'stopped')
  survivor ('bc', 'aac', 'cb', 'stopped')
  survivor ('bc', 'aac', 'cc', 'stopped')
  survivor ('bc', 'aac', 'aac', 'stopped')
  survivor ('bc', 'aac', 'aca', 'stopped')
  survivor ('bc', 'aac', 'acb', 'stopped')
  survivor ('bc', 'aac', 'acc', 'stopped')
  survivor ('bc', 'aac', 'bac', 'stopped')
  survivor ('bc', 'aac', 'bbc', 'stopped')
  survivor ('bc', 'aac', 'bca', 'stopped')
  survivor ('bc', 'aac', 'bcb', 'stopped')
  survivor ('bc', 'aac', 'bcc', 'stopped')
  survivor ('bc', 'aac', 'caa', 'stopped')
  survivor ('bc', 'aac', 'cab', 'stopped')
  survivor ('bc', 'aac', 'cac', 'stopped')
  survivor ('bc', 'aac', 'cba', 'stopped')
  survivor ('bc', 'aac', 'cbb', 'stopped')
  survivor ('bc', 'aac', 'cbc', 'stopped')
  survivor ('bc', 'aac', 'cca', 'stopped')
  survivor ('bc', 'aac', 'ccb', 'stopped')
  survivor ('bc', 'aac', 'ccc', 'stopped')
  progress 40/101 {'shortcut': 790, 'stopped': 193, 'closed': 17} (246s)
  survivor ('bc', 'aca', 'c', 'stopped')
  survivor ('bc', 'aca', 'ac', 'stopped')
  survivor ('bc', 'aca', 'bc', 'stopped')
  survivor ('bc', 'aca', 'ca', 'stopped')
  survivor ('bc', 'aca', 'cb', 'stopped')
  survivor ('bc', 'aca', 'cc', 'stopped')
  survivor ('bc', 'aca', 'aac', 'stopped')
  survivor ('bc', 'aca', 'abc', 'stopped')
  survivor ('bc', 'aca', 'aca', 'stopped')
  survivor ('bc', 'aca', 'acb', 'stopped')
  survivor ('bc', 'aca', 'acc', 'stopped')
  survivor ('bc', 'aca', 'bac', 'stopped')
  survivor ('bc', 'aca', 'bbc', 'stopped')
  survivor ('bc', 'aca', 'bca', 'stopped')
  survivor ('bc', 'aca', 'bcb', 'stopped')
  survivor ('bc', 'aca', 'bcc', 'stopped')
  survivor ('bc', 'aca', 'caa', 'stopped')
  survivor ('bc', 'aca', 'cab', 'stopped')
  survivor ('bc', 'aca', 'cac', 'stopped')
  survivor ('bc', 'aca', 'cba', 'stopped')
  survivor ('bc', 'aca', 'cbb', 'stopped')
  survivor ('bc', 'aca', 'cbc', 'stopped')
  survivor ('bc', 'aca', 'cca', 'stopped')
  survivor ('bc', 'aca', 'ccb', 'stopped')
  survivor ('bc', 'aca', 'ccc', 'stopped')
  survivor ('bc', 'acb', 'c', 'stopped')
  survivor ('bc', 'acb', 'ac', 'stopped')
  survivor ('bc', 'acb', 'bc', 'stopped')
  survivor ('bc', 'acb', 'ca', 'stopped')
  survivor ('bc', 'acb', 'cb', 'stopped')
  survivor ('bc', 'acb', 'cc', 'stopped')
  survivor ('bc', 'acb', 'aac', 'stopped')
  survivor ('bc', 'acb', 'abc', 'stopped')
  survivor ('bc', 'acb', 'aca', 'stopped')
  survivor ('bc', 'acb', 'acb', 'stopped')
  survivor ('bc', 'acb', 'acc', 'stopped')
  survivor ('bc', 'acb', 'bbc', 'stopped')
  survivor ('bc', 'acb', 'bca', 'stopped')
  survivor ('bc', 'acb', 'bcb', 'stopped')
  survivor ('bc', 'acb', 'bcc', 'stopped')
  survivor ('bc', 'acb', 'caa', 'stopped')
  survivor ('bc', 'acb', 'cab', 'stopped')
  survivor ('bc', 'acb', 'cac', 'stopped')
  survivor ('bc', 'acb', 'cba', 'stopped')
  survivor ('bc', 'acb', 'cbb', 'stopped')
  survivor ('bc', 'acb', 'cbc', 'stopped')
  survivor ('bc', 'acb', 'cca', 'stopped')
  survivor ('bc', 'acb', 'ccb', 'stopped')
  survivor ('bc', 'acb', 'ccc', 'stopped')
  survivor ('bc', 'acc', 'c', 'stopped')
  survivor ('bc', 'acc', 'ac', 'stopped')
  survivor ('bc', 'acc', 'bc', 'stopped')
  survivor ('bc', 'acc', 'ca', 'stopped')
  survivor ('bc', 'acc', 'cb', 'stopped')
  survivor ('bc', 'acc', 'cc', 'stopped')
  survivor ('bc', 'acc', 'aac', 'stopped')
  survivor ('bc', 'acc', 'abc', 'stopped')
  survivor ('bc', 'acc', 'aca', 'stopped')
  survivor ('bc', 'acc', 'acb', 'stopped')
  survivor ('bc', 'acc', 'acc', 'stopped')
  survivor ('bc', 'acc', 'bac', 'stopped')
  survivor ('bc', 'acc', 'bbc', 'stopped')
  survivor ('bc', 'acc', 'bca', 'stopped')
  survivor ('bc', 'acc', 'bcb', 'stopped')
  survivor ('bc', 'acc', 'bcc', 'stopped')
  survivor ('bc', 'acc', 'caa', 'stopped')
  survivor ('bc', 'acc', 'cab', 'stopped')
  survivor ('bc', 'acc', 'cac', 'stopped')
  survivor ('bc', 'acc', 'cba', 'stopped')
  survivor ('bc', 'acc', 'cbb', 'stopped')
  survivor ('bc', 'acc', 'cbc', 'stopped')
  survivor ('bc', 'acc', 'cca', 'stopped')
  survivor ('bc', 'acc', 'ccb', 'stopped')
  survivor ('bc', 'acc', 'ccc', 'stopped')
  survivor ('bc', 'caa', 'c', 'stopped')
  survivor ('bc', 'caa', 'ac', 'stopped')
  survivor ('bc', 'caa', 'bc', 'stopped')
  survivor ('bc', 'caa', 'ca', 'stopped')
  survivor ('bc', 'caa', 'cb', 'stopped')
  survivor ('bc', 'caa', 'cc', 'stopped')
  survivor ('bc', 'caa', 'aac', 'stopped')
  survivor ('bc', 'caa', 'abc', 'stopped')
  survivor ('bc', 'caa', 'aca', 'stopped')
  survivor ('bc', 'caa', 'acb', 'stopped')
  survivor ('bc', 'caa', 'acc', 'stopped')
  survivor ('bc', 'caa', 'bac', 'stopped')
  survivor ('bc', 'caa', 'bbc', 'stopped')
  survivor ('bc', 'caa', 'bca', 'stopped')
  survivor ('bc', 'caa', 'bcb', 'stopped')
  survivor ('bc', 'caa', 'bcc', 'stopped')
  survivor ('bc', 'caa', 'caa', 'stopped')
  survivor ('bc', 'caa', 'cab', 'stopped')
  survivor ('bc', 'caa', 'cac', 'stopped')
  survivor ('bc', 'caa', 'cba', 'stopped')
  survivor ('bc', 'caa', 'cbb', 'stopped')
  survivor ('bc', 'caa', 'cbc', 'stopped')
  survivor ('bc', 'caa', 'cca', 'stopped')
  survivor ('bc', 'caa', 'ccb', 'stopped')
  survivor ('bc', 'caa', 'ccc', 'stopped')
  survivor ('bc', 'cac', 'c', 'stopped')
  survivor ('bc', 'cac', 'ac', 'stopped')
  survivor ('bc', 'cac', 'bc', 'stopped')
  survivor ('bc', 'cac', 'ca', 'stopped')
  survivor ('bc', 'cac', 'cb', 'stopped')
  survivor ('bc', 'cac', 'cc', 'stopped')
  survivor ('bc', 'cac', 'aac', 'stopped')
  survivor ('bc', 'cac', 'abc', 'stopped')
  survivor ('bc', 'cac', 'aca', 'stopped')
  survivor ('bc', 'cac', 'acb', 'stopped')
  survivor ('bc', 'cac', 'acc', 'stopped')
  survivor ('bc', 'cac', 'bac', 'stopped')
  survivor ('bc', 'cac', 'bbc', 'stopped')
  survivor ('bc', 'cac', 'bca', 'stopped')
  survivor ('bc', 'cac', 'bcb', 'stopped')
  survivor ('bc', 'cac', 'bcc', 'stopped')
  survivor ('bc', 'cac', 'caa', 'stopped')
  survivor ('bc', 'cac', 'cab', 'stopped')
  survivor ('bc', 'cac', 'cac', 'stopped')
  survivor ('bc', 'cac', 'cba', 'stopped')
  survivor ('bc', 'cac', 'cbb', 'stopped')
  survivor ('bc', 'cac', 'cbc', 'stopped')
  survivor ('bc', 'cac', 'cca', 'stopped')
  survivor ('bc', 'cac', 'ccb', 'stopped')
  survivor ('bc', 'cac', 'ccc', 'stopped')
  survivor ('bc', 'cbb', 'c', 'stopped')
  survivor ('bc', 'cbb', 'ac', 'stopped')
  survivor ('bc', 'cbb', 'bc', 'stopped')
  survivor ('bc', 'cbb', 'ca', 'stopped')
  survivor ('bc', 'cbb', 'cb', 'stopped')
  survivor ('bc', 'cbb', 'cc', 'stopped')
  survivor ('bc', 'cbb', 'aac', 'stopped')
  survivor ('bc', 'cbb', 'abc', 'stopped')
  survivor ('bc', 'cbb', 'aca', 'stopped')
  survivor ('bc', 'cbb', 'acb', 'stopped')
  survivor ('bc', 'cbb', 'acc', 'stopped')
  survivor ('bc', 'cbb', 'bac', 'stopped')
  survivor ('bc', 'cbb', 'bbc', 'stopped')
  survivor ('bc', 'cbb', 'bca', 'stopped')
  survivor ('bc', 'cbb', 'bcb', 'stopped')
  survivor ('bc', 'cbb', 'bcc', 'stopped')
  survivor ('bc', 'cbb', 'caa', 'stopped')
  survivor ('bc', 'cbb', 'cab', 'stopped')
  survivor ('bc', 'cbb', 'cac', 'stopped')
  survivor ('bc', 'cbb', 'cba', 'stopped')
  survivor ('bc', 'cbb', 'cbb', 'stopped')
  survivor ('bc', 'cbb', 'cbc', 'stopped')
  survivor ('bc', 'cbb', 'cca', 'stopped')
  survivor ('bc', 'cbb', 'ccb', 'stopped')
  survivor ('bc', 'cbb', 'ccc', 'stopped')
  survivor ('bc', 'cca', 'c', 'stopped')
  survivor ('bc', 'cca', 'ac', 'stopped')
  survivor ('bc', 'cca', 'bc', 'stopped')
  survivor ('bc', 'cca', 'ca', 'stopped')
  survivor ('bc', 'cca', 'cb', 'stopped')
  survivor ('bc', 'cca', 'cc', 'stopped')
  survivor ('bc', 'cca', 'aac', 'stopped')
  survivor ('bc', 'cca', 'abc', 'stopped')
  survivor ('bc', 'cca', 'aca', 'stopped')
  survivor ('bc', 'cca', 'acb', 'stopped')
  survivor ('bc', 'cca', 'acc', 'stopped')
  survivor ('bc', 'cca', 'bac', 'stopped')
  survivor ('bc', 'cca', 'bbc', 'stopped')
  survivor ('bc', 'cca', 'bca', 'stopped')
  survivor ('bc', 'cca', 'bcb', 'stopped')
  survivor ('bc', 'cca', 'bcc', 'stopped')
  survivor ('bc', 'cca', 'caa', 'stopped')
  survivor ('bc', 'cca', 'cab', 'stopped')
  survivor ('bc', 'cca', 'cac', 'stopped')
  survivor ('bc', 'cca', 'cba', 'stopped')
  survivor ('bc', 'cca', 'cbb', 'stopped')
  survivor ('bc', 'cca', 'cbc', 'stopped')
  survivor ('bc', 'cca', 'cca', 'stopped')
  survivor ('bc', 'cca', 'ccb', 'stopped')
  survivor ('bc', 'cca', 'ccc', 'stopped')
  survivor ('bc', 'ccb', 'c', 'stopped')
  survivor ('bc', 'ccb', 'ac', 'stopped')
  survivor ('bc', 'ccb', 'bc', 'stopped')
  survivor ('bc', 'ccb', 'ca', 'stopped')
  survivor ('bc', 'ccb', 'cb', 'stopped')
  survivor ('bc', 'ccb', 'cc', 'stopped')
  survivor ('bc', 'ccb', 'aac', 'stopped')
  survivor ('bc', 'ccb', 'abc', 'stopped')
  survivor ('bc', 'ccb', 'aca', 'stopped')
  survivor ('bc', 'ccb', 'acb', 'stopped')
  survivor ('bc', 'ccb', 'acc', 'stopped')
  survivor ('bc', 'ccb', 'bac', 'stopped')
  survivor ('bc', 'ccb', 'bbc', 'stopped')
  survivor ('bc', 'ccb', 'bca', 'stopped')
  survivor ('bc', 'ccb', 'bcb', 'stopped')
  survivor ('bc', 'ccb', 'bcc', 'stopped')
  survivor ('bc', 'ccb', 'caa', 'stopped')
  survivor ('bc', 'ccb', 'cab', 'stopped')
  survivor ('bc', 'ccb', 'cac', 'stopped')
  survivor ('bc', 'ccb', 'cba', 'stopped')
  survivor ('bc', 'ccb', 'cbb', 'stopped')
  survivor ('bc', 'ccb', 'cbc', 'stopped')
  survivor ('bc', 'ccb', 'cca', 'stopped')
  survivor ('bc', 'ccb', 'ccb', 'stopped')
  survivor ('bc', 'ccb', 'ccc', 'stopped')
  survivor ('bc', 'ccc', 'c', 'stopped')
  survivor ('bc', 'ccc', 'ac', 'stopped')
  survivor ('bc', 'ccc', 'bc', 'stopped')
  survivor ('bc', 'ccc', 'ca', 'stopped')
  survivor ('bc', 'ccc', 'cb', 'stopped')
  survivor ('bc', 'ccc', 'cc', 'stopped')
  survivor ('bc', 'ccc', 'aac', 'stopped')
  survivor ('bc', 'ccc', 'abc', 'stopped')
  survivor ('bc', 'ccc', 'aca', 'stopped')
  survivor ('bc', 'ccc', 'acb', 'stopped')
  survivor ('bc', 'ccc', 'acc', 'stopped')
  survivor ('bc', 'ccc', 'bac', 'stopped')
  survivor ('bc', 'ccc', 'bbc', 'stopped')
  survivor ('bc', 'ccc', 'bca', 'stopped')
  survivor ('bc', 'ccc', 'bcb', 'stopped')
  survivor ('bc', 'ccc', 'bcc', 'stopped')
  survivor ('bc', 'ccc', 'caa', 'stopped')
  survivor ('bc', 'ccc', 'cab', 'stopped')
  survivor ('bc', 'ccc', 'cac', 'stopped')
  survivor ('bc', 'ccc', 'cba', 'stopped')
  survivor ('bc', 'ccc', 'cbb', 'stopped')
  survivor ('bc', 'ccc', 'cbc', 'stopped')
  survivor ('bc', 'ccc', 'cca', 'stopped')
  survivor ('bc', 'ccc', 'ccb', 'stopped')
  survivor ('bc', 'ccc', 'ccc', 'stopped')
  progress 50/101 {'shortcut': 816, 'stopped': 417, 'closed': 17} (301s)
  survivor ('ca', 'bc', 'ac', 'stopped')
  survivor ('ca', 'bc', 'bc', 'stopped')
  survivor ('ca', 'bc', 'ca', 'stopped')
  survivor ('ca', 'bc', 'abc', 'stopped')
  survivor ('ca', 'bc', 'aca', 'stopped')
  survivor ('ca', 'bc', 'bbc', 'stopped')
  survivor ('ca', 'bc', 'bca', 'stopped')
  survivor ('ca', 'bc', 'caa', 'stopped')
  survivor ('ca', 'bc', 'cab', 'stopped')
  survivor ('ca', 'bc', 'cac', 'stopped')
  survivor ('ca', 'bc', 'cca', 'stopped')
  survivor ('ca', 'cb', 'c', 'stopped')
  survivor ('ca', 'cb', 'ac', 'stopped')
  survivor ('ca', 'cb', 'bc', 'stopped')
  survivor ('ca', 'cb', 'ca', 'stopped')
  survivor ('ca', 'cb', 'cb', 'stopped')
  survivor ('ca', 'cb', 'cc', 'stopped')
  survivor ('ca', 'cb', 'aac', 'stopped')
  survivor ('ca', 'cb', 'abc', 'stopped')
  survivor ('ca', 'cb', 'aca', 'stopped')
  survivor ('ca', 'cb', 'acb', 'stopped')
  survivor ('ca', 'cb', 'acc', 'stopped')
  survivor ('ca', 'cb', 'bac', 'stopped')
  survivor ('ca', 'cb', 'bbc', 'stopped')
  survivor ('ca', 'cb', 'bca', 'stopped')
  survivor ('ca', 'cb', 'bcb', 'stopped')
  survivor ('ca', 'cb', 'bcc', 'stopped')
  survivor ('ca', 'cb', 'caa', 'stopped')
  survivor ('ca', 'cb', 'cac', 'stopped')
  survivor ('ca', 'cb', 'cbc', 'stopped')
  survivor ('ca', 'cb', 'cca', 'stopped')
  survivor ('ca', 'cb', 'ccc', 'stopped')
  survivor ('ca', 'cc', 'c', 'stopped')
  survivor ('ca', 'cc', 'ac', 'stopped')
  survivor ('ca', 'cc', 'ca', 'stopped')
  survivor ('ca', 'cc', 'cc', 'stopped')
  survivor ('ca', 'cc', 'abc', 'stopped')
  survivor ('ca', 'cc', 'aca', 'stopped')
  survivor ('ca', 'cc', 'acc', 'stopped')
  survivor ('ca', 'cc', 'bca', 'stopped')
  survivor ('ca', 'cc', 'caa', 'stopped')
  survivor ('ca', 'cc', 'cab', 'stopped')
  survivor ('ca', 'cc', 'cac', 'stopped')
  survivor ('ca', 'cc', 'cca', 'stopped')
  survivor ('ca', 'cc', 'ccc', 'stopped')
  survivor ('ca', 'aac', 'c', 'stopped')
  survivor ('ca', 'aac', 'ac', 'stopped')
  survivor ('ca', 'aac', 'bc', 'stopped')
  survivor ('ca', 'aac', 'ca', 'stopped')
  survivor ('ca', 'aac', 'cb', 'stopped')
  survivor ('ca', 'aac', 'cc', 'stopped')
  survivor ('ca', 'aac', 'aac', 'stopped')
  survivor ('ca', 'aac', 'abc', 'stopped')
  survivor ('ca', 'aac', 'aca', 'stopped')
  survivor ('ca', 'aac', 'acb', 'stopped')
  survivor ('ca', 'aac', 'acc', 'stopped')
  survivor ('ca', 'aac', 'bac', 'stopped')
  survivor ('ca', 'aac', 'bbc', 'stopped')
  survivor ('ca', 'aac', 'bca', 'stopped')
  survivor ('ca', 'aac', 'bcb', 'stopped')
  survivor ('ca', 'aac', 'bcc', 'stopped')
  survivor ('ca', 'aac', 'caa', 'stopped')
  survivor ('ca', 'aac', 'cab', 'stopped')
  survivor ('ca', 'aac', 'cac', 'stopped')
  survivor ('ca', 'aac', 'cba', 'stopped')
  survivor ('ca', 'aac', 'cbb', 'stopped')
  survivor ('ca', 'aac', 'cbc', 'stopped')
  survivor ('ca', 'aac', 'cca', 'stopped')
  survivor ('ca', 'aac', 'ccb', 'stopped')
  survivor ('ca', 'aac', 'ccc', 'stopped')
  survivor ('ca', 'acb', 'c', 'stopped')
  survivor ('ca', 'acb', 'ac', 'stopped')
  survivor ('ca', 'acb', 'bc', 'stopped')
  survivor ('ca', 'acb', 'ca', 'stopped')
  survivor ('ca', 'acb', 'cb', 'stopped')
  survivor ('ca', 'acb', 'cc', 'stopped')
  survivor ('ca', 'acb', 'aac', 'stopped')
  survivor ('ca', 'acb', 'abc', 'stopped')
  survivor ('ca', 'acb', 'aca', 'stopped')
  survivor ('ca', 'acb', 'acb', 'stopped')
  survivor ('ca', 'acb', 'acc', 'stopped')
  survivor ('ca', 'acb', 'bac', 'stopped')
  survivor ('ca', 'acb', 'bbc', 'stopped')
  survivor ('ca', 'acb', 'bca', 'stopped')
  survivor ('ca', 'acb', 'bcb', 'stopped')
  survivor ('ca', 'acb', 'bcc', 'stopped')
  survivor ('ca', 'acb', 'caa', 'stopped')
  survivor ('ca', 'acb', 'cab', 'stopped')
  survivor ('ca', 'acb', 'cac', 'stopped')
  survivor ('ca', 'acb', 'cbb', 'stopped')
  survivor ('ca', 'acb', 'cbc', 'stopped')
  survivor ('ca', 'acb', 'cca', 'stopped')
  survivor ('ca', 'acb', 'ccb', 'stopped')
  survivor ('ca', 'acb', 'ccc', 'stopped')
  survivor ('ca', 'acc', 'c', 'stopped')
  survivor ('ca', 'acc', 'ac', 'stopped')
  survivor ('ca', 'acc', 'bc', 'stopped')
  survivor ('ca', 'acc', 'ca', 'stopped')
  survivor ('ca', 'acc', 'cb', 'stopped')
  survivor ('ca', 'acc', 'cc', 'stopped')
  survivor ('ca', 'acc', 'aac', 'stopped')
  survivor ('ca', 'acc', 'abc', 'stopped')
  survivor ('ca', 'acc', 'aca', 'stopped')
  survivor ('ca', 'acc', 'acb', 'stopped')
  survivor ('ca', 'acc', 'acc', 'stopped')
  survivor ('ca', 'acc', 'bac', 'stopped')
  survivor ('ca', 'acc', 'bbc', 'stopped')
  survivor ('ca', 'acc', 'bca', 'stopped')
  survivor ('ca', 'acc', 'bcb', 'stopped')
  survivor ('ca', 'acc', 'bcc', 'stopped')
  survivor ('ca', 'acc', 'caa', 'stopped')
  survivor ('ca', 'acc', 'cab', 'stopped')
  survivor ('ca', 'acc', 'cac', 'stopped')
  survivor ('ca', 'acc', 'cba', 'stopped')
  survivor ('ca', 'acc', 'cbb', 'stopped')
  survivor ('ca', 'acc', 'cbc', 'stopped')
  survivor ('ca', 'acc', 'cca', 'stopped')
  survivor ('ca', 'acc', 'ccb', 'stopped')
  survivor ('ca', 'acc', 'ccc', 'stopped')
  survivor ('ca', 'bbc', 'c', 'stopped')
  survivor ('ca', 'bbc', 'ac', 'stopped')
  survivor ('ca', 'bbc', 'bc', 'stopped')
  survivor ('ca', 'bbc', 'ca', 'stopped')
  survivor ('ca', 'bbc', 'cb', 'stopped')
  survivor ('ca', 'bbc', 'cc', 'stopped')
  survivor ('ca', 'bbc', 'aac', 'stopped')
  survivor ('ca', 'bbc', 'abc', 'stopped')
  survivor ('ca', 'bbc', 'aca', 'stopped')
  survivor ('ca', 'bbc', 'acb', 'stopped')
  survivor ('ca', 'bbc', 'acc', 'stopped')
  survivor ('ca', 'bbc', 'bac', 'stopped')
  survivor ('ca', 'bbc', 'bbc', 'stopped')
  survivor ('ca', 'bbc', 'bca', 'stopped')
  survivor ('ca', 'bbc', 'bcb', 'stopped')
  survivor ('ca', 'bbc', 'bcc', 'stopped')
  survivor ('ca', 'bbc', 'caa', 'stopped')
  survivor ('ca', 'bbc', 'cab', 'stopped')
  survivor ('ca', 'bbc', 'cac', 'stopped')
  survivor ('ca', 'bbc', 'cba', 'stopped')
  survivor ('ca', 'bbc', 'cbb', 'stopped')
  survivor ('ca', 'bbc', 'cbc', 'stopped')
  survivor ('ca', 'bbc', 'cca', 'stopped')
  survivor ('ca', 'bbc', 'ccb', 'stopped')
  survivor ('ca', 'bbc', 'ccc', 'stopped')
  survivor ('ca', 'bcb', 'c', 'stopped')
  survivor ('ca', 'bcb', 'ac', 'stopped')
  survivor ('ca', 'bcb', 'bc', 'stopped')
  survivor ('ca', 'bcb', 'ca', 'stopped')
  survivor ('ca', 'bcb', 'cb', 'stopped')
  survivor ('ca', 'bcb', 'cc', 'stopped')
  survivor ('ca', 'bcb', 'aac', 'stopped')
  survivor ('ca', 'bcb', 'abc', 'stopped')
  survivor ('ca', 'bcb', 'aca', 'stopped')
  survivor ('ca', 'bcb', 'acb', 'stopped')
  survivor ('ca', 'bcb', 'acc', 'stopped')
  survivor ('ca', 'bcb', 'bac', 'stopped')
  survivor ('ca', 'bcb', 'bbc', 'stopped')
  survivor ('ca', 'bcb', 'bca', 'stopped')
  survivor ('ca', 'bcb', 'bcb', 'stopped')
  survivor ('ca', 'bcb', 'bcc', 'stopped')
  survivor ('ca', 'bcb', 'caa', 'stopped')
  survivor ('ca', 'bcb', 'cab', 'stopped')
  survivor ('ca', 'bcb', 'cac', 'stopped')
  survivor ('ca', 'bcb', 'cba', 'stopped')
  survivor ('ca', 'bcb', 'cbb', 'stopped')
  survivor ('ca', 'bcb', 'cbc', 'stopped')
  survivor ('ca', 'bcb', 'cca', 'stopped')
  survivor ('ca', 'bcb', 'ccb', 'stopped')
  survivor ('ca', 'bcb', 'ccc', 'stopped')
  progress 60/101 {'shortcut': 897, 'stopped': 586, 'closed': 17} (346s)
  survivor ('ca', 'bcc', 'c', 'stopped')
  survivor ('ca', 'bcc', 'ac', 'stopped')
  survivor ('ca', 'bcc', 'bc', 'stopped')
  survivor ('ca', 'bcc', 'ca', 'stopped')
  survivor ('ca', 'bcc', 'cb', 'stopped')
  survivor ('ca', 'bcc', 'cc', 'stopped')
  survivor ('ca', 'bcc', 'aac', 'stopped')
  survivor ('ca', 'bcc', 'abc', 'stopped')
  survivor ('ca', 'bcc', 'aca', 'stopped')
  survivor ('ca', 'bcc', 'acb', 'stopped')
  survivor ('ca', 'bcc', 'acc', 'stopped')
  survivor ('ca', 'bcc', 'bac', 'stopped')
  survivor ('ca', 'bcc', 'bbc', 'stopped')
  survivor ('ca', 'bcc', 'bca', 'stopped')
  survivor ('ca', 'bcc', 'bcb', 'stopped')
  survivor ('ca', 'bcc', 'bcc', 'stopped')
  survivor ('ca', 'bcc', 'caa', 'stopped')
  survivor ('ca', 'bcc', 'cab', 'stopped')
  survivor ('ca', 'bcc', 'cac', 'stopped')
  survivor ('ca', 'bcc', 'cba', 'stopped')
  survivor ('ca', 'bcc', 'cbb', 'stopped')
  survivor ('ca', 'bcc', 'cbc', 'stopped')
  survivor ('ca', 'bcc', 'cca', 'stopped')
  survivor ('ca', 'bcc', 'ccb', 'stopped')
  survivor ('ca', 'bcc', 'ccc', 'stopped')
  survivor ('ca', 'cbb', 'c', 'stopped')
  survivor ('ca', 'cbb', 'ac', 'stopped')
  survivor ('ca', 'cbb', 'bc', 'stopped')
  survivor ('ca', 'cbb', 'ca', 'stopped')
  survivor ('ca', 'cbb', 'cb', 'stopped')
  survivor ('ca', 'cbb', 'cc', 'stopped')
  survivor ('ca', 'cbb', 'aac', 'stopped')
  survivor ('ca', 'cbb', 'abc', 'stopped')
  survivor ('ca', 'cbb', 'aca', 'stopped')
  survivor ('ca', 'cbb', 'acb', 'stopped')
  survivor ('ca', 'cbb', 'acc', 'stopped')
  survivor ('ca', 'cbb', 'bac', 'stopped')
  survivor ('ca', 'cbb', 'bbc', 'stopped')
  survivor ('ca', 'cbb', 'bca', 'stopped')
  survivor ('ca', 'cbb', 'bcb', 'stopped')
  survivor ('ca', 'cbb', 'bcc', 'stopped')
  survivor ('ca', 'cbb', 'caa', 'stopped')
  survivor ('ca', 'cbb', 'cac', 'stopped')
  survivor ('ca', 'cbb', 'cba', 'stopped')
  survivor ('ca', 'cbb', 'cbb', 'stopped')
  survivor ('ca', 'cbb', 'cbc', 'stopped')
  survivor ('ca', 'cbb', 'cca', 'stopped')
  survivor ('ca', 'cbb', 'ccb', 'stopped')
  survivor ('ca', 'cbb', 'ccc', 'stopped')
  survivor ('ca', 'cbc', 'c', 'stopped')
  survivor ('ca', 'cbc', 'ac', 'stopped')
  survivor ('ca', 'cbc', 'bc', 'stopped')
  survivor ('ca', 'cbc', 'ca', 'stopped')
  survivor ('ca', 'cbc', 'cb', 'stopped')
  survivor ('ca', 'cbc', 'cc', 'stopped')
  survivor ('ca', 'cbc', 'aac', 'stopped')
  survivor ('ca', 'cbc', 'abc', 'stopped')
  survivor ('ca', 'cbc', 'aca', 'stopped')
  survivor ('ca', 'cbc', 'acb', 'stopped')
  survivor ('ca', 'cbc', 'acc', 'stopped')
  survivor ('ca', 'cbc', 'bac', 'stopped')
  survivor ('ca', 'cbc', 'bbc', 'stopped')
  survivor ('ca', 'cbc', 'bca', 'stopped')
  survivor ('ca', 'cbc', 'bcb', 'stopped')
  survivor ('ca', 'cbc', 'bcc', 'stopped')
  survivor ('ca', 'cbc', 'caa', 'stopped')
  survivor ('ca', 'cbc', 'cab', 'stopped')
  survivor ('ca', 'cbc', 'cac', 'stopped')
  survivor ('ca', 'cbc', 'cba', 'stopped')
  survivor ('ca', 'cbc', 'cbb', 'stopped')
  survivor ('ca', 'cbc', 'cbc', 'stopped')
  survivor ('ca', 'cbc', 'cca', 'stopped')
  survivor ('ca', 'cbc', 'ccb', 'stopped')
  survivor ('ca', 'cbc', 'ccc', 'stopped')
  survivor ('ca', 'ccb', 'c', 'stopped')
  survivor ('ca', 'ccb', 'ac', 'stopped')
  survivor ('ca', 'ccb', 'bc', 'stopped')
  survivor ('ca', 'ccb', 'ca', 'stopped')
  survivor ('ca', 'ccb', 'cb', 'stopped')
  survivor ('ca', 'ccb', 'cc', 'stopped')
  survivor ('ca', 'ccb', 'aac', 'stopped')
  survivor ('ca', 'ccb', 'abc', 'stopped')
  survivor ('ca', 'ccb', 'aca', 'stopped')
  survivor ('ca', 'ccb', 'acb', 'stopped')
  survivor ('ca', 'ccb', 'acc', 'stopped')
  survivor ('ca', 'ccb', 'bac', 'stopped')
  survivor ('ca', 'ccb', 'bbc', 'stopped')
  survivor ('ca', 'ccb', 'bca', 'stopped')
  survivor ('ca', 'ccb', 'bcb', 'stopped')
  survivor ('ca', 'ccb', 'bcc', 'stopped')
  survivor ('ca', 'ccb', 'caa', 'stopped')
  survivor ('ca', 'ccb', 'cab', 'stopped')
  survivor ('ca', 'ccb', 'cac', 'stopped')
  survivor ('ca', 'ccb', 'cba', 'stopped')
  survivor ('ca', 'ccb', 'cbb', 'stopped')
  survivor ('ca', 'ccb', 'cbc', 'stopped')
  survivor ('ca', 'ccb', 'cca', 'stopped')
  survivor ('ca', 'ccb', 'ccb', 'stopped')
  survivor ('ca', 'ccb', 'ccc', 'stopped')
  survivor ('ca', 'ccc', 'c', 'stopped')
  survivor ('ca', 'ccc', 'ac', 'stopped')
  survivor ('ca', 'ccc', 'ca', 'stopped')
  survivor ('ca', 'ccc', 'cc', 'stopped')
  survivor ('ca', 'ccc', 'abc', 'stopped')
  survivor ('ca', 'ccc', 'aca', 'stopped')
  survivor ('ca', 'ccc', 'acc', 'stopped')
  survivor ('ca', 'ccc', 'bca', 'stopped')
  survivor ('ca', 'ccc', 'caa', 'stopped')
  survivor ('ca', 'ccc', 'cab', 'stopped')
  survivor ('ca', 'ccc', 'cac', 'stopped')
  survivor ('ca', 'ccc', 'cca', 'stopped')
  survivor ('ca', 'ccc', 'ccc', 'stopped')
  survivor ('cb', 'cc', 'c', 'stopped')
  survivor ('cb', 'cc', 'bc', 'stopped')
  survivor ('cb', 'cc', 'cb', 'stopped')
  survivor ('cb', 'cc', 'cc', 'stopped')
  survivor ('cb', 'cc', 'abc', 'stopped')
  survivor ('cb', 'cc', 'bcb', 'stopped')
  survivor ('cb', 'cc', 'bcc', 'stopped')
  survivor ('cb', 'cc', 'cbb', 'stopped')
  survivor ('cb', 'cc', 'cbc', 'stopped')
  survivor ('cb', 'cc', 'ccb', 'stopped')
  survivor ('cb', 'cc', 'ccc', 'stopped')
  progress 70/101 {'shortcut': 1024, 'stopped': 709, 'closed': 17} (397s)
  survivor ('cb', 'aca', 'abc', 'stopped')
  survivor ('cb', 'aca', 'acb', 'stopped')
  survivor ('cb', 'aca', 'bac', 'stopped')
  survivor ('cb', 'acc', 'c', 'stopped')
  survivor ('cb', 'acc', 'ac', 'stopped')
  survivor ('cb', 'acc', 'bc', 'stopped')
  survivor ('cb', 'acc', 'ca', 'stopped')
  survivor ('cb', 'acc', 'cb', 'stopped')
  survivor ('cb', 'acc', 'cc', 'stopped')
  survivor ('cb', 'acc', 'aac', 'stopped')
  survivor ('cb', 'acc', 'abc', 'stopped')
  survivor ('cb', 'acc', 'aca', 'stopped')
  survivor ('cb', 'acc', 'acb', 'stopped')
  survivor ('cb', 'acc', 'acc', 'stopped')
  survivor ('cb', 'acc', 'bac', 'stopped')
  survivor ('cb', 'acc', 'bbc', 'stopped')
  survivor ('cb', 'acc', 'bca', 'stopped')
  survivor ('cb', 'acc', 'bcb', 'stopped')
  survivor ('cb', 'acc', 'bcc', 'stopped')
  survivor ('cb', 'acc', 'caa', 'stopped')
  survivor ('cb', 'acc', 'cac', 'stopped')
  survivor ('cb', 'acc', 'cbb', 'stopped')
  survivor ('cb', 'acc', 'cbc', 'stopped')
  survivor ('cb', 'acc', 'cca', 'stopped')
  survivor ('cb', 'acc', 'ccb', 'stopped')
  survivor ('cb', 'acc', 'ccc', 'stopped')
  survivor ('cb', 'bbc', 'c', 'stopped')
  survivor ('cb', 'bbc', 'ac', 'stopped')
  survivor ('cb', 'bbc', 'bc', 'stopped')
  survivor ('cb', 'bbc', 'ca', 'stopped')
  survivor ('cb', 'bbc', 'cb', 'stopped')
  survivor ('cb', 'bbc', 'cc', 'stopped')
  survivor ('cb', 'bbc', 'aac', 'stopped')
  survivor ('cb', 'bbc', 'abc', 'stopped')
  survivor ('cb', 'bbc', 'aca', 'stopped')
  survivor ('cb', 'bbc', 'acb', 'stopped')
  survivor ('cb', 'bbc', 'acc', 'stopped')
  survivor ('cb', 'bbc', 'bac', 'stopped')
  survivor ('cb', 'bbc', 'bbc', 'stopped')
  survivor ('cb', 'bbc', 'bca', 'stopped')
  survivor ('cb', 'bbc', 'bcb', 'stopped')
  survivor ('cb', 'bbc', 'bcc', 'stopped')
  survivor ('cb', 'bbc', 'caa', 'stopped')
  survivor ('cb', 'bbc', 'cac', 'stopped')
  survivor ('cb', 'bbc', 'cbb', 'stopped')
  survivor ('cb', 'bbc', 'cbc', 'stopped')
  survivor ('cb', 'bbc', 'cca', 'stopped')
  survivor ('cb', 'bbc', 'ccb', 'stopped')
  survivor ('cb', 'bbc', 'ccc', 'stopped')
  survivor ('cb', 'bca', 'bc', 'stopped')
  survivor ('cb', 'bca', 'abc', 'stopped')
  survivor ('cb', 'bca', 'acb', 'stopped')
  survivor ('cb', 'bca', 'bca', 'stopped')
  survivor ('cb', 'bca', 'bcb', 'stopped')
  survivor ('cb', 'bca', 'cbb', 'stopped')
  survivor ('cb', 'bca', 'cbc', 'stopped')
  survivor ('cb', 'bca', 'ccb', 'stopped')
  survivor ('cb', 'bcc', 'c', 'stopped')
  survivor ('cb', 'bcc', 'ac', 'stopped')
  survivor ('cb', 'bcc', 'bc', 'stopped')
  survivor ('cb', 'bcc', 'ca', 'stopped')
  survivor ('cb', 'bcc', 'cb', 'stopped')
  survivor ('cb', 'bcc', 'cc', 'stopped')
  survivor ('cb', 'bcc', 'aac', 'stopped')
  survivor ('cb', 'bcc', 'abc', 'stopped')
  survivor ('cb', 'bcc', 'aca', 'stopped')
  survivor ('cb', 'bcc', 'acb', 'stopped')
  survivor ('cb', 'bcc', 'acc', 'stopped')
  survivor ('cb', 'bcc', 'bac', 'stopped')
  survivor ('cb', 'bcc', 'bbc', 'stopped')
  survivor ('cb', 'bcc', 'bca', 'stopped')
  survivor ('cb', 'bcc', 'bcb', 'stopped')
  survivor ('cb', 'bcc', 'bcc', 'stopped')
  survivor ('cb', 'bcc', 'caa', 'stopped')
  survivor ('cb', 'bcc', 'cac', 'stopped')
  survivor ('cb', 'bcc', 'cbb', 'stopped')
  survivor ('cb', 'bcc', 'cbc', 'stopped')
  survivor ('cb', 'bcc', 'cca', 'stopped')
  survivor ('cb', 'bcc', 'ccb', 'stopped')
  survivor ('cb', 'bcc', 'ccc', 'stopped')
  progress 80/101 {'shortcut': 1194, 'stopped': 789, 'closed': 17} (437s)
  survivor ('cb', 'ccc', 'c', 'stopped')
  survivor ('cb', 'ccc', 'ac', 'stopped')
  survivor ('cb', 'ccc', 'bc', 'stopped')
  survivor ('cb', 'ccc', 'ca', 'stopped')
  survivor ('cb', 'ccc', 'cb', 'stopped')
  survivor ('cb', 'ccc', 'cc', 'stopped')
  survivor ('cb', 'ccc', 'aac', 'stopped')
  survivor ('cb', 'ccc', 'abc', 'stopped')
  survivor ('cb', 'ccc', 'aca', 'stopped')
  survivor ('cb', 'ccc', 'acb', 'stopped')
  survivor ('cb', 'ccc', 'acc', 'stopped')
  survivor ('cb', 'ccc', 'bac', 'stopped')
  survivor ('cb', 'ccc', 'bbc', 'stopped')
  survivor ('cb', 'ccc', 'bca', 'stopped')
  survivor ('cb', 'ccc', 'bcb', 'stopped')
  survivor ('cb', 'ccc', 'bcc', 'stopped')
  survivor ('cb', 'ccc', 'caa', 'stopped')
  survivor ('cb', 'ccc', 'cac', 'stopped')
  survivor ('cb', 'ccc', 'cbb', 'stopped')
  survivor ('cb', 'ccc', 'cbc', 'stopped')
  survivor ('cb', 'ccc', 'cca', 'stopped')
  survivor ('cb', 'ccc', 'ccb', 'stopped')
  survivor ('cb', 'ccc', 'ccc', 'stopped')
  survivor ('cc', 'ac', 'c', 'stopped')
  survivor ('cc', 'ac', 'ac', 'stopped')
  survivor ('cc', 'ac', 'bc', 'stopped')
  survivor ('cc', 'ac', 'ca', 'stopped')
  survivor ('cc', 'ac', 'cb', 'stopped')
  survivor ('cc', 'ac', 'cc', 'stopped')
  survivor ('cc', 'ac', 'aca', 'stopped')
  survivor ('cc', 'ac', 'acb', 'stopped')
  survivor ('cc', 'ac', 'bbc', 'stopped')
  survivor ('cc', 'ac', 'bca', 'stopped')
  survivor ('cc', 'ac', 'bcb', 'stopped')
  survivor ('cc', 'ac', 'bcc', 'stopped')
  survivor ('cc', 'ac', 'caa', 'stopped')
  survivor ('cc', 'ac', 'cab', 'stopped')
  survivor ('cc', 'ac', 'cac', 'stopped')
  survivor ('cc', 'ac', 'cba', 'stopped')
  survivor ('cc', 'ac', 'cbb', 'stopped')
  survivor ('cc', 'ac', 'cbc', 'stopped')
  survivor ('cc', 'ac', 'ccb', 'stopped')
  survivor ('cc', 'ac', 'ccc', 'stopped')
  survivor ('cc', 'bc', 'c', 'stopped')
  survivor ('cc', 'bc', 'ac', 'stopped')
  survivor ('cc', 'bc', 'bc', 'stopped')
  survivor ('cc', 'bc', 'ca', 'stopped')
  survivor ('cc', 'bc', 'cb', 'stopped')
  survivor ('cc', 'bc', 'cc', 'stopped')
  survivor ('cc', 'bc', 'aac', 'stopped')
  survivor ('cc', 'bc', 'abc', 'stopped')
  survivor ('cc', 'bc', 'aca', 'stopped')
  survivor ('cc', 'bc', 'acb', 'stopped')
  survivor ('cc', 'bc', 'acc', 'stopped')
  survivor ('cc', 'bc', 'bca', 'stopped')
  survivor ('cc', 'bc', 'bcb', 'stopped')
  survivor ('cc', 'bc', 'bcc', 'stopped')
  survivor ('cc', 'bc', 'caa', 'stopped')
  survivor ('cc', 'bc', 'cab', 'stopped')
  survivor ('cc', 'bc', 'cac', 'stopped')
  survivor ('cc', 'bc', 'cba', 'stopped')
  survivor ('cc', 'bc', 'cbb', 'stopped')
  survivor ('cc', 'bc', 'cbc', 'stopped')
  survivor ('cc', 'bc', 'cca', 'stopped')
  survivor ('cc', 'bc', 'ccc', 'stopped')
  survivor ('cc', 'ca', 'c', 'stopped')
  survivor ('cc', 'ca', 'ac', 'stopped')
  survivor ('cc', 'ca', 'bc', 'stopped')
  survivor ('cc', 'ca', 'ca', 'stopped')
  survivor ('cc', 'ca', 'cb', 'stopped')
  survivor ('cc', 'ca', 'cc', 'stopped')
  survivor ('cc', 'ca', 'aac', 'stopped')
  survivor ('cc', 'ca', 'abc', 'stopped')
  survivor ('cc', 'ca', 'aca', 'stopped')
  survivor ('cc', 'ca', 'acb', 'stopped')
  survivor ('cc', 'ca', 'bac', 'stopped')
  survivor ('cc', 'ca', 'bbc', 'stopped')
  survivor ('cc', 'ca', 'bcb', 'stopped')
  survivor ('cc', 'ca', 'bcc', 'stopped')
  survivor ('cc', 'ca', 'cab', 'stopped')
  survivor ('cc', 'ca', 'cbb', 'stopped')
  survivor ('cc', 'ca', 'cbc', 'stopped')
  survivor ('cc', 'ca', 'ccb', 'stopped')
  survivor ('cc', 'ca', 'ccc', 'stopped')
  survivor ('cc', 'cb', 'c', 'stopped')
  survivor ('cc', 'cb', 'ac', 'stopped')
  survivor ('cc', 'cb', 'bc', 'stopped')
  survivor ('cc', 'cb', 'ca', 'stopped')
  survivor ('cc', 'cb', 'cb', 'stopped')
  survivor ('cc', 'cb', 'cc', 'stopped')
  survivor ('cc', 'cb', 'aac', 'stopped')
  survivor ('cc', 'cb', 'abc', 'stopped')
  survivor ('cc', 'cb', 'aca', 'stopped')
  survivor ('cc', 'cb', 'acb', 'stopped')
  survivor ('cc', 'cb', 'acc', 'stopped')
  survivor ('cc', 'cb', 'bac', 'stopped')
  survivor ('cc', 'cb', 'bbc', 'stopped')
  survivor ('cc', 'cb', 'bca', 'stopped')
  survivor ('cc', 'cb', 'bcb', 'stopped')
  survivor ('cc', 'cb', 'caa', 'stopped')
  survivor ('cc', 'cb', 'cac', 'stopped')
  survivor ('cc', 'cb', 'cbb', 'stopped')
  survivor ('cc', 'cb', 'cca', 'stopped')
  survivor ('cc', 'cb', 'ccc', 'stopped')
  survivor ('cc', 'aac', 'c', 'stopped')
  survivor ('cc', 'aac', 'ac', 'stopped')
  survivor ('cc', 'aac', 'bc', 'stopped')
  survivor ('cc', 'aac', 'ca', 'stopped')
  survivor ('cc', 'aac', 'cb', 'stopped')
  survivor ('cc', 'aac', 'cc', 'stopped')
  survivor ('cc', 'aac', 'abc', 'stopped')
  survivor ('cc', 'aac', 'aca', 'stopped')
  survivor ('cc', 'aac', 'acb', 'stopped')
  survivor ('cc', 'aac', 'acc', 'stopped')
  survivor ('cc', 'aac', 'bac', 'stopped')
  survivor ('cc', 'aac', 'bbc', 'stopped')
  survivor ('cc', 'aac', 'bca', 'stopped')
  survivor ('cc', 'aac', 'bcb', 'stopped')
  survivor ('cc', 'aac', 'bcc', 'stopped')
  survivor ('cc', 'aac', 'caa', 'stopped')
  survivor ('cc', 'aac', 'cab', 'stopped')
  survivor ('cc', 'aac', 'cac', 'stopped')
  survivor ('cc', 'aac', 'cba', 'stopped')
  survivor ('cc', 'aac', 'cbb', 'stopped')
  survivor ('cc', 'aac', 'cbc', 'stopped')
  survivor ('cc', 'aac', 'cca', 'stopped')
  survivor ('cc', 'aac', 'ccb', 'stopped')
  survivor ('cc', 'aac', 'ccc', 'stopped')
  survivor ('cc', 'aca', 'c', 'stopped')
  survivor ('cc', 'aca', 'ac', 'stopped')
  survivor ('cc', 'aca', 'bc', 'stopped')
  survivor ('cc', 'aca', 'ca', 'stopped')
  survivor ('cc', 'aca', 'cb', 'stopped')
  survivor ('cc', 'aca', 'cc', 'stopped')
  survivor ('cc', 'aca', 'aac', 'stopped')
  survivor ('cc', 'aca', 'abc', 'stopped')
  survivor ('cc', 'aca', 'aca', 'stopped')
  survivor ('cc', 'aca', 'acb', 'stopped')
  survivor ('cc', 'aca', 'acc', 'stopped')
  survivor ('cc', 'aca', 'bac', 'stopped')
  survivor ('cc', 'aca', 'bbc', 'stopped')
  survivor ('cc', 'aca', 'bca', 'stopped')
  survivor ('cc', 'aca', 'bcb', 'stopped')
  survivor ('cc', 'aca', 'bcc', 'stopped')
  survivor ('cc', 'aca', 'caa', 'stopped')
  survivor ('cc', 'aca', 'cab', 'stopped')
  survivor ('cc', 'aca', 'cac', 'stopped')
  survivor ('cc', 'aca', 'cba', 'stopped')
  survivor ('cc', 'aca', 'cbb', 'stopped')
  survivor ('cc', 'aca', 'cbc', 'stopped')
  survivor ('cc', 'aca', 'cca', 'stopped')
  survivor ('cc', 'aca', 'ccb', 'stopped')
  survivor ('cc', 'aca', 'ccc', 'stopped')
  survivor ('cc', 'acb', 'c', 'stopped')
  survivor ('cc', 'acb', 'ac', 'stopped')
  survivor ('cc', 'acb', 'bc', 'stopped')
  survivor ('cc', 'acb', 'ca', 'stopped')
  survivor ('cc', 'acb', 'cb', 'stopped')
  survivor ('cc', 'acb', 'cc', 'stopped')
  survivor ('cc', 'acb', 'aac', 'stopped')
  survivor ('cc', 'acb', 'abc', 'stopped')
  survivor ('cc', 'acb', 'aca', 'stopped')
  survivor ('cc', 'acb', 'acc', 'stopped')
  survivor ('cc', 'acb', 'bac', 'stopped')
  survivor ('cc', 'acb', 'bbc', 'stopped')
  survivor ('cc', 'acb', 'bca', 'stopped')
  survivor ('cc', 'acb', 'bcb', 'stopped')
  survivor ('cc', 'acb', 'bcc', 'stopped')
  survivor ('cc', 'acb', 'caa', 'stopped')
  survivor ('cc', 'acb', 'cab', 'stopped')
  survivor ('cc', 'acb', 'cac', 'stopped')
  survivor ('cc', 'acb', 'cba', 'stopped')
  survivor ('cc', 'acb', 'cbb', 'stopped')
  survivor ('cc', 'acb', 'cbc', 'stopped')
  survivor ('cc', 'acb', 'cca', 'stopped')
  survivor ('cc', 'acb', 'ccb', 'stopped')
  survivor ('cc', 'acb', 'ccc', 'stopped')
  survivor ('cc', 'bac', 'c', 'stopped')
  survivor ('cc', 'bac', 'ac', 'stopped')
  survivor ('cc', 'bac', 'bc', 'stopped')
  survivor ('cc', 'bac', 'ca', 'stopped')
  survivor ('cc', 'bac', 'cb', 'stopped')
  survivor ('cc', 'bac', 'cc', 'stopped')
  survivor ('cc', 'bac', 'aac', 'stopped')
  survivor ('cc', 'bac', 'abc', 'stopped')
  survivor ('cc', 'bac', 'aca', 'stopped')
  survivor ('cc', 'bac', 'acb', 'stopped')
  survivor ('cc', 'bac', 'acc', 'stopped')
  survivor ('cc', 'bac', 'bbc', 'stopped')
  survivor ('cc', 'bac', 'bca', 'stopped')
  survivor ('cc', 'bac', 'bcb', 'stopped')
  survivor ('cc', 'bac', 'bcc', 'stopped')
  survivor ('cc', 'bac', 'caa', 'stopped')
  survivor ('cc', 'bac', 'cab', 'stopped')
  survivor ('cc', 'bac', 'cac', 'stopped')
  survivor ('cc', 'bac', 'cba', 'stopped')
  survivor ('cc', 'bac', 'cbb', 'stopped')
  survivor ('cc', 'bac', 'cbc', 'stopped')
  survivor ('cc', 'bac', 'cca', 'stopped')
  survivor ('cc', 'bac', 'ccb', 'stopped')
  survivor ('cc', 'bac', 'ccc', 'stopped')
  progress 90/101 {'shortcut': 1243, 'stopped': 990, 'closed': 17} (513s)
  survivor ('cc', 'bbc', 'c', 'stopped')
  survivor ('cc', 'bbc', 'ac', 'stopped')
  survivor ('cc', 'bbc', 'bc', 'stopped')
  survivor ('cc', 'bbc', 'ca', 'stopped')
  survivor ('cc', 'bbc', 'cb', 'stopped')
  survivor ('cc', 'bbc', 'cc', 'stopped')
  survivor ('cc', 'bbc', 'aac', 'stopped')
  survivor ('cc', 'bbc', 'abc', 'stopped')
  survivor ('cc', 'bbc', 'aca', 'stopped')
  survivor ('cc', 'bbc', 'acb', 'stopped')
  survivor ('cc', 'bbc', 'acc', 'stopped')
  survivor ('cc', 'bbc', 'bac', 'stopped')
  survivor ('cc', 'bbc', 'bbc', 'stopped')
  survivor ('cc', 'bbc', 'bca', 'stopped')
  survivor ('cc', 'bbc', 'bcb', 'stopped')
  survivor ('cc', 'bbc', 'bcc', 'stopped')
  survivor ('cc', 'bbc', 'caa', 'stopped')
  survivor ('cc', 'bbc', 'cab', 'stopped')
  survivor ('cc', 'bbc', 'cac', 'stopped')
  survivor ('cc', 'bbc', 'cba', 'stopped')
  survivor ('cc', 'bbc', 'cbb', 'stopped')
  survivor ('cc', 'bbc', 'cbc', 'stopped')
  survivor ('cc', 'bbc', 'cca', 'stopped')
  survivor ('cc', 'bbc', 'ccb', 'stopped')
  survivor ('cc', 'bbc', 'ccc', 'stopped')
  survivor ('cc', 'bca', 'c', 'stopped')
  survivor ('cc', 'bca', 'ac', 'stopped')
  survivor ('cc', 'bca', 'bc', 'stopped')
  survivor ('cc', 'bca', 'ca', 'stopped')
  survivor ('cc', 'bca', 'cb', 'stopped')
  survivor ('cc', 'bca', 'cc', 'stopped')
  survivor ('cc', 'bca', 'aac', 'stopped')
  survivor ('cc', 'bca', 'abc', 'stopped')
  survivor ('cc', 'bca', 'aca', 'stopped')
  survivor ('cc', 'bca', 'acb', 'stopped')
  survivor ('cc', 'bca', 'acc', 'stopped')
  survivor ('cc', 'bca', 'bac', 'stopped')
  survivor ('cc', 'bca', 'bbc', 'stopped')
  survivor ('cc', 'bca', 'bcb', 'stopped')
  survivor ('cc', 'bca', 'bcc', 'stopped')
  survivor ('cc', 'bca', 'caa', 'stopped')
  survivor ('cc', 'bca', 'cab', 'stopped')
  survivor ('cc', 'bca', 'cac', 'stopped')
  survivor ('cc', 'bca', 'cba', 'stopped')
  survivor ('cc', 'bca', 'cbb', 'stopped')
  survivor ('cc', 'bca', 'cbc', 'stopped')
  survivor ('cc', 'bca', 'cca', 'stopped')
  survivor ('cc', 'bca', 'ccb', 'stopped')
  survivor ('cc', 'bca', 'ccc', 'stopped')
  survivor ('cc', 'bcb', 'c', 'stopped')
  survivor ('cc', 'bcb', 'ac', 'stopped')
  survivor ('cc', 'bcb', 'bc', 'stopped')
  survivor ('cc', 'bcb', 'ca', 'stopped')
  survivor ('cc', 'bcb', 'cb', 'stopped')
  survivor ('cc', 'bcb', 'cc', 'stopped')
  survivor ('cc', 'bcb', 'aac', 'stopped')
  survivor ('cc', 'bcb', 'abc', 'stopped')
  survivor ('cc', 'bcb', 'aca', 'stopped')
  survivor ('cc', 'bcb', 'acb', 'stopped')
  survivor ('cc', 'bcb', 'acc', 'stopped')
  survivor ('cc', 'bcb', 'bac', 'stopped')
  survivor ('cc', 'bcb', 'bbc', 'stopped')
  survivor ('cc', 'bcb', 'bca', 'stopped')
  survivor ('cc', 'bcb', 'bcb', 'stopped')
  survivor ('cc', 'bcb', 'bcc', 'stopped')
  survivor ('cc', 'bcb', 'caa', 'stopped')
  survivor ('cc', 'bcb', 'cab', 'stopped')
  survivor ('cc', 'bcb', 'cac', 'stopped')
  survivor ('cc', 'bcb', 'cba', 'stopped')
  survivor ('cc', 'bcb', 'cbb', 'stopped')
  survivor ('cc', 'bcb', 'cbc', 'stopped')
  survivor ('cc', 'bcb', 'cca', 'stopped')
  survivor ('cc', 'bcb', 'ccb', 'stopped')
  survivor ('cc', 'bcb', 'ccc', 'stopped')
  survivor ('cc', 'caa', 'c', 'stopped')
  survivor ('cc', 'caa', 'ac', 'stopped')
  survivor ('cc', 'caa', 'bc', 'stopped')
  survivor ('cc', 'caa', 'ca', 'stopped')
  survivor ('cc', 'caa', 'cb', 'stopped')
  survivor ('cc', 'caa', 'cc', 'stopped')
  survivor ('cc', 'caa', 'aac', 'stopped')
  survivor ('cc', 'caa', 'abc', 'stopped')
  survivor ('cc', 'caa', 'aca', 'stopped')
  survivor ('cc', 'caa', 'acb', 'stopped')
  survivor ('cc', 'caa', 'acc', 'stopped')
  survivor ('cc', 'caa', 'bac', 'stopped')
  survivor ('cc', 'caa', 'bbc', 'stopped')
  survivor ('cc', 'caa', 'bca', 'stopped')
  survivor ('cc', 'caa', 'bcb', 'stopped')
  survivor ('cc', 'caa', 'bcc', 'stopped')
  survivor ('cc', 'caa', 'caa', 'stopped')
  survivor ('cc', 'caa', 'cab', 'stopped')
  survivor ('cc', 'caa', 'cac', 'stopped')
  survivor ('cc', 'caa', 'cba', 'stopped')
  survivor ('cc', 'caa', 'cbb', 'stopped')
  survivor ('cc', 'caa', 'cbc', 'stopped')
  survivor ('cc', 'caa', 'cca', 'stopped')
  survivor ('cc', 'caa', 'ccb', 'stopped')
  survivor ('cc', 'caa', 'ccc', 'stopped')
  survivor ('cc', 'cac', 'c', 'stopped')
  survivor ('cc', 'cac', 'ac', 'stopped')
  survivor ('cc', 'cac', 'ca', 'stopped')
  survivor ('cc', 'cac', 'cc', 'stopped')
  survivor ('cc', 'cac', 'abc', 'stopped')
  survivor ('cc', 'cac', 'acc', 'stopped')
  survivor ('cc', 'cac', 'bca', 'stopped')
  survivor ('cc', 'cac', 'cab', 'stopped')
  survivor ('cc', 'cac', 'cac', 'stopped')
  survivor ('cc', 'cac', 'cca', 'stopped')
  survivor ('cc', 'cac', 'ccc', 'stopped')
  survivor ('cc', 'cba', 'c', 'stopped')
  survivor ('cc', 'cba', 'ac', 'stopped')
  survivor ('cc', 'cba', 'bc', 'stopped')
  survivor ('cc', 'cba', 'ca', 'stopped')
  survivor ('cc', 'cba', 'cb', 'stopped')
  survivor ('cc', 'cba', 'cc', 'stopped')
  survivor ('cc', 'cba', 'aac', 'stopped')
  survivor ('cc', 'cba', 'abc', 'stopped')
  survivor ('cc', 'cba', 'aca', 'stopped')
  survivor ('cc', 'cba', 'acb', 'stopped')
  survivor ('cc', 'cba', 'acc', 'stopped')
  survivor ('cc', 'cba', 'bac', 'stopped')
  survivor ('cc', 'cba', 'bbc', 'stopped')
  survivor ('cc', 'cba', 'bca', 'stopped')
  survivor ('cc', 'cba', 'bcb', 'stopped')
  survivor ('cc', 'cba', 'bcc', 'stopped')
  survivor ('cc', 'cba', 'caa', 'stopped')
  survivor ('cc', 'cba', 'cab', 'stopped')
  survivor ('cc', 'cba', 'cac', 'stopped')
  survivor ('cc', 'cba', 'cbb', 'stopped')
  survivor ('cc', 'cba', 'cbc', 'stopped')
  survivor ('cc', 'cba', 'cca', 'stopped')
  survivor ('cc', 'cba', 'ccb', 'stopped')
  survivor ('cc', 'cba', 'ccc', 'stopped')
  survivor ('cc', 'cbb', 'c', 'stopped')
  survivor ('cc', 'cbb', 'ac', 'stopped')
  survivor ('cc', 'cbb', 'bc', 'stopped')
  survivor ('cc', 'cbb', 'ca', 'stopped')
  survivor ('cc', 'cbb', 'cb', 'stopped')
  survivor ('cc', 'cbb', 'cc', 'stopped')
  survivor ('cc', 'cbb', 'aac', 'stopped')
  survivor ('cc', 'cbb', 'abc', 'stopped')
  survivor ('cc', 'cbb', 'aca', 'stopped')
  survivor ('cc', 'cbb', 'acb', 'stopped')
  survivor ('cc', 'cbb', 'acc', 'stopped')
  survivor ('cc', 'cbb', 'bac', 'stopped')
  survivor ('cc', 'cbb', 'bbc', 'stopped')
  survivor ('cc', 'cbb', 'bca', 'stopped')
  survivor ('cc', 'cbb', 'bcb', 'stopped')
  survivor ('cc', 'cbb', 'bcc', 'stopped')
  survivor ('cc', 'cbb', 'caa', 'stopped')
  survivor ('cc', 'cbb', 'cab', 'stopped')
  survivor ('cc', 'cbb', 'cac', 'stopped')
  survivor ('cc', 'cbb', 'cba', 'stopped')
  survivor ('cc', 'cbb', 'cbc', 'stopped')
  survivor ('cc', 'cbb', 'cca', 'stopped')
  survivor ('cc', 'cbb', 'ccb', 'stopped')
  survivor ('cc', 'cbb', 'ccc', 'stopped')
  survivor ('cc', 'cbc', 'c', 'stopped')
  survivor ('cc', 'cbc', 'bc', 'stopped')
  survivor ('cc', 'cbc', 'cb', 'stopped')
  survivor ('cc', 'cbc', 'cc', 'stopped')
  survivor ('cc', 'cbc', 'abc', 'stopped')
  survivor ('cc', 'cbc', 'bca', 'stopped')
  survivor ('cc', 'cbc', 'bcc', 'stopped')
  survivor ('cc', 'cbc', 'cab', 'stopped')
  survivor ('cc', 'cbc', 'cbc', 'stopped')
  survivor ('cc', 'cbc', 'ccb', 'stopped')
  survivor ('cc', 'cbc', 'ccc', 'stopped')
  progress 100/101 {'shortcut': 1324, 'stopped': 1159, 'closed': 17} (584s)
m=3 (|e_3| <= 3): {'closed': 17, 'shortcut': 1349, 'stopped': 1159} (586s)
closed: [('c', 'cc', 'ac'), ('c', 'cc', 'bc'), ('c', 'cc', 'ca'), ('c', 'cc', 'cb'), ('c', 'cc', 'aac'), ('c', 'cc', 'aca'), ('c', 'cc', 'acb'), ('c', 'cc', 'acc'), ('c', 'cc', 'bbc'), ('c', 'cc', 'bcb'), ('c', 'cc', 'bcc'), ('c', 'cc', 'caa'), ('c', 'cc', 'cac'), ('c', 'cc', 'cbb'), ('c', 'cc', 'cbc'), ('c', 'cc', 'cca'), ('c', 'cc', 'ccb')]
capped/stopped: [('c', 'cc', 'c', 'stopped'), ('c', 'cc', 'bca', 'stopped'), ('c', 'aca', 'c', 'stopped'), ('c', 'aca', 'ac', 'stopped'), ('c', 'aca', 'ca', 'stopped'), ('c', 'aca', 'aac', 'stopped'), ('c', 'aca', 'aca', 'stopped'), ('c', 'aca', 'caa', 'stopped'), ('c', 'aca', 'cac', 'stopped'), ('c', 'bcb', 'c', 'stopped'), ('c', 'bcb', 'bc', 'stopped'), ('c', 'bcb', 'cb', 'stopped'), ('c', 'bcb', 'bbc', 'stopped'), ('c', 'bcb', 'bcb', 'stopped'), ('c', 'bcb', 'cbb', 'stopped'), ('c', 'bcb', 'cbc', 'stopped'), ('c', 'cac', 'ac', 'stopped'), ('c', 'cac', 'ca', 'stopped'), ('c', 'cac', 'acc', 'stopped'), ('c', 'cac', 'cca', 'stopped'), ('c', 'cac', 'ccc', 'stopped'), ('c', 'cbc', 'bc', 'stopped'), ('c', 'cbc', 'cb', 'stopped'), ('c', 'cbc', 'bcc', 'stopped'), ('c', 'cbc', 'ccb', 'stopped'), ('c', 'cbc', 'ccc', 'stopped'), ('ac', 'cc', 'ac', 'stopped'), ('ac', 'cc', 'ca', 'stopped'), ('ac', 'cc', 'acc', 'stopped'), ('ac', 'cc', 'cac', 'stopped'), ('ac', 'bca', 'ca', 'stopped'), ('ac', 'bca', 'aac', 'stopped'), ('ac', 'bca', 'aca', 'stopped'), ('ac', 'bca', 'acb', 'stopped'), ('ac', 'bca', 'acc', 'stopped'), ('ac', 'bca', 'bca', 'stopped'), ('ac', 'bca', 'cab', 'stopped'), ('ac', 'bca', 'cac', 'stopped'), ('ac', 'bcb', 'aac', 'stopped'), ('ac', 'bcb', 'acc', 'stopped'), ('ac', 'bcb', 'cab', 'stopped'), ('ac', 'bcb', 'cba', 'stopped'), ('ac', 'caa', 'c', 'stopped'), ('ac', 'caa', 'ac', 'stopped'), ('ac', 'caa', 'bc', 'stopped'), ('ac', 'caa', 'ca', 'stopped'), ('ac', 'caa', 'cb', 'stopped'), ('ac', 'caa', 'cc', 'stopped'), ('ac', 'caa', 'aac', 'stopped'), ('ac', 'caa', 'aca', 'stopped'), ('ac', 'caa', 'acb', 'stopped'), ('ac', 'caa', 'acc', 'stopped'), ('ac', 'caa', 'bbc', 'stopped'), ('ac', 'caa', 'bca', 'stopped'), ('ac', 'caa', 'bcb', 'stopped'), ('ac', 'caa', 'bcc', 'stopped'), ('ac', 'caa', 'caa', 'stopped'), ('ac', 'caa', 'cab', 'stopped'), ('ac', 'caa', 'cac', 'stopped'), ('ac', 'caa', 'cba', 'stopped'), ('ac', 'caa', 'cbb', 'stopped'), ('ac', 'caa', 'cbc', 'stopped'), ('ac', 'caa', 'cca', 'stopped'), ('ac', 'caa', 'ccb', 'stopped'), ('ac', 'caa', 'ccc', 'stopped'), ('ac', 'cca', 'c', 'stopped'), ('ac', 'cca', 'ac', 'stopped'), ('ac', 'cca', 'bc', 'stopped'), ('ac', 'cca', 'ca', 'stopped'), ('ac', 'cca', 'cb', 'stopped'), ('ac', 'cca', 'cc', 'stopped'), ('ac', 'cca', 'aac', 'stopped'), ('ac', 'cca', 'aca', 'stopped'), ('ac', 'cca', 'acb', 'stopped'), ('ac', 'cca', 'acc', 'stopped'), ('ac', 'cca', 'bbc', 'stopped'), ('ac', 'cca', 'bca', 'stopped'), ('ac', 'cca', 'bcb', 'stopped'), ('ac', 'cca', 'bcc', 'stopped'), ('ac', 'cca', 'caa', 'stopped'), ('ac', 'cca', 'cab', 'stopped'), ('ac', 'cca', 'cac', 'stopped'), ('ac', 'cca', 'cba', 'stopped'), ('ac', 'cca', 'cbb', 'stopped'), ('ac', 'cca', 'cbc', 'stopped'), ('ac', 'cca', 'cca', 'stopped'), ('ac', 'cca', 'ccb', 'stopped'), ('ac', 'cca', 'ccc', 'stopped'), ('ac', 'ccb', 'c', 'stopped'), ('ac', 'ccb', 'ac', 'stopped'), ('ac', 'ccb', 'bc', 'stopped'), ('ac', 'ccb', 'ca', 'stopped'), ('ac', 'ccb', 'cb', 'stopped'), ('ac', 'ccb', 'cc', 'stopped'), ('ac', 'ccb', 'aac', 'stopped'), ('ac', 'ccb', 'aca', 'stopped'), ('ac', 'ccb', 'acb', 'stopped'), ('ac', 'ccb', 'acc', 'stopped'), ('ac', 'ccb', 'bbc', 'stopped'), ('ac', 'ccb', 'bca', 'stopped'), ('ac', 'ccb', 'bcb', 'stopped'), ('ac', 'ccb', 'bcc', 'stopped'), ('ac', 'ccb', 'caa', 'stopped'), ('ac', 'ccb', 'cab', 'stopped'), ('ac', 'ccb', 'cac', 'stopped'), ('ac', 'ccb', 'cba', 'stopped'), ('ac', 'ccb', 'cbb', 'stopped'), ('ac', 'ccb', 'cbc', 'stopped'), ('ac', 'ccb', 'cca', 'stopped'), ('ac', 'ccb', 'ccb', 'stopped'), ('ac', 'ccb', 'ccc', 'stopped'), ('ac', 'ccc', 'c', 'stopped'), ('ac', 'ccc', 'ac', 'stopped'), ('ac', 'ccc', 'bc', 'stopped'), ('ac', 'ccc', 'ca', 'stopped'), ('ac', 'ccc', 'cb', 'stopped'), ('ac', 'ccc', 'cc', 'stopped'), ('ac', 'ccc', 'aac', 'stopped'), ('ac', 'ccc', 'aca', 'stopped'), ('ac', 'ccc', 'acb', 'stopped'), ('ac', 'ccc', 'acc', 'stopped'), ('ac', 'ccc', 'bbc', 'stopped'), ('ac', 'ccc', 'bca', 'stopped'), ('ac', 'ccc', 'bcb', 'stopped'), ('ac', 'ccc', 'bcc', 'stopped'), ('ac', 'ccc', 'caa', 'stopped'), ('ac', 'ccc', 'cab', 'stopped'), ('ac', 'ccc', 'cac', 'stopped'), ('ac', 'ccc', 'cba', 'stopped'), ('ac', 'ccc', 'cbb', 'stopped'), ('ac', 'ccc', 'cbc', 'stopped'), ('ac', 'ccc', 'cca', 'stopped'), ('ac', 'ccc', 'ccb', 'stopped'), ('ac', 'ccc', 'ccc', 'stopped'), ('bc', 'ac', 'c', 'stopped'), ('bc', 'ac', 'bc', 'stopped'), ('bc', 'ac', 'ca', 'stopped'), ('bc', 'ac', 'cb', 'stopped'), ('bc', 'ac', 'cc', 'stopped'), ('bc', 'ac', 'aca', 'stopped'), ('bc', 'ac', 'acb', 'stopped'), ('bc', 'ac', 'bbc', 'stopped'), ('bc', 'ac', 'bca', 'stopped'), ('bc', 'ac', 'bcb', 'stopped'), ('bc', 'ac', 'bcc', 'stopped'), ('bc', 'ac', 'caa', 'stopped'), ('bc', 'ac', 'cab', 'stopped'), ('bc', 'ac', 'cba', 'stopped'), ('bc', 'ac', 'cbb', 'stopped'), ('bc', 'ac', 'cbc', 'stopped'), ('bc', 'ac', 'cca', 'stopped'), ('bc', 'ac', 'ccb', 'stopped'), ('bc', 'ac', 'ccc', 'stopped'), ('bc', 'ca', 'abc', 'stopped'), ('bc', 'ca', 'bbc', 'stopped'), ('bc', 'ca', 'bca', 'stopped'), ('bc', 'ca', 'bcc', 'stopped'), ('bc', 'ca', 'cab', 'stopped'), ('bc', 'cc', 'c', 'stopped'), ('bc', 'cc', 'bc', 'stopped'), ('bc', 'cc', 'cb', 'stopped'), ('bc', 'cc', 'abc', 'stopped'), ('bc', 'cc', 'bbc', 'stopped'), ('bc', 'cc', 'bca', 'stopped'), ('bc', 'cc', 'bcb', 'stopped'), ('bc', 'cc', 'bcc', 'stopped'), ('bc', 'cc', 'cab', 'stopped'), ('bc', 'cc', 'cbc', 'stopped'), ('bc', 'cc', 'ccb', 'stopped'), ('bc', 'aac', 'c', 'stopped'), ('bc', 'aac', 'ac', 'stopped'), ('bc', 'aac', 'bc', 'stopped'), ('bc', 'aac', 'ca', 'stopped'), ('bc', 'aac', 'cb', 'stopped'), ('bc', 'aac', 'cc', 'stopped'), ('bc', 'aac', 'aac', 'stopped'), ('bc', 'aac', 'aca', 'stopped'), ('bc', 'aac', 'acb', 'stopped'), ('bc', 'aac', 'acc', 'stopped'), ('bc', 'aac', 'bac', 'stopped'), ('bc', 'aac', 'bbc', 'stopped'), ('bc', 'aac', 'bca', 'stopped'), ('bc', 'aac', 'bcb', 'stopped'), ('bc', 'aac', 'bcc', 'stopped'), ('bc', 'aac', 'caa', 'stopped'), ('bc', 'aac', 'cab', 'stopped'), ('bc', 'aac', 'cac', 'stopped'), ('bc', 'aac', 'cba', 'stopped'), ('bc', 'aac', 'cbb', 'stopped'), ('bc', 'aac', 'cbc', 'stopped'), ('bc', 'aac', 'cca', 'stopped'), ('bc', 'aac', 'ccb', 'stopped'), ('bc', 'aac', 'ccc', 'stopped'), ('bc', 'aca', 'c', 'stopped'), ('bc', 'aca', 'ac', 'stopped'), ('bc', 'aca', 'bc', 'stopped'), ('bc', 'aca', 'ca', 'stopped'), ('bc', 'aca', 'cb', 'stopped'), ('bc', 'aca', 'cc', 'stopped'), ('bc', 'aca', 'aac', 'stopped'), ('bc', 'aca', 'abc', 'stopped'), ('bc', 'aca', 'aca', 'stopped'), ('bc', 'aca', 'acb', 'stopped'), ('bc', 'aca', 'acc', 'stopped'), ('bc', 'aca', 'bac', 'stopped'), ('bc', 'aca', 'bbc', 'stopped'), ('bc', 'aca', 'bca', 'stopped'), ('bc', 'aca', 'bcb', 'stopped'), ('bc', 'aca', 'bcc', 'stopped'), ('bc', 'aca', 'caa', 'stopped'), ('bc', 'aca', 'cab', 'stopped'), ('bc', 'aca', 'cac', 'stopped'), ('bc', 'aca', 'cba', 'stopped'), ('bc', 'aca', 'cbb', 'stopped'), ('bc', 'aca', 'cbc', 'stopped'), ('bc', 'aca', 'cca', 'stopped'), ('bc', 'aca', 'ccb', 'stopped'), ('bc', 'aca', 'ccc', 'stopped'), ('bc', 'acb', 'c', 'stopped'), ('bc', 'acb', 'ac', 'stopped'), ('bc', 'acb', 'bc', 'stopped'), ('bc', 'acb', 'ca', 'stopped'), ('bc', 'acb', 'cb', 'stopped'), ('bc', 'acb', 'cc', 'stopped'), ('bc', 'acb', 'aac', 'stopped'), ('bc', 'acb', 'abc', 'stopped'), ('bc', 'acb', 'aca', 'stopped'), ('bc', 'acb', 'acb', 'stopped'), ('bc', 'acb', 'acc', 'stopped'), ('bc', 'acb', 'bbc', 'stopped'), ('bc', 'acb', 'bca', 'stopped'), ('bc', 'acb', 'bcb', 'stopped'), ('bc', 'acb', 'bcc', 'stopped'), ('bc', 'acb', 'caa', 'stopped'), ('bc', 'acb', 'cab', 'stopped'), ('bc', 'acb', 'cac', 'stopped'), ('bc', 'acb', 'cba', 'stopped'), ('bc', 'acb', 'cbb', 'stopped'), ('bc', 'acb', 'cbc', 'stopped'), ('bc', 'acb', 'cca', 'stopped'), ('bc', 'acb', 'ccb', 'stopped'), ('bc', 'acb', 'ccc', 'stopped'), ('bc', 'acc', 'c', 'stopped'), ('bc', 'acc', 'ac', 'stopped'), ('bc', 'acc', 'bc', 'stopped'), ('bc', 'acc', 'ca', 'stopped'), ('bc', 'acc', 'cb', 'stopped'), ('bc', 'acc', 'cc', 'stopped'), ('bc', 'acc', 'aac', 'stopped'), ('bc', 'acc', 'abc', 'stopped'), ('bc', 'acc', 'aca', 'stopped'), ('bc', 'acc', 'acb', 'stopped'), ('bc', 'acc', 'acc', 'stopped'), ('bc', 'acc', 'bac', 'stopped'), ('bc', 'acc', 'bbc', 'stopped'), ('bc', 'acc', 'bca', 'stopped'), ('bc', 'acc', 'bcb', 'stopped'), ('bc', 'acc', 'bcc', 'stopped'), ('bc', 'acc', 'caa', 'stopped'), ('bc', 'acc', 'cab', 'stopped'), ('bc', 'acc', 'cac', 'stopped'), ('bc', 'acc', 'cba', 'stopped'), ('bc', 'acc', 'cbb', 'stopped'), ('bc', 'acc', 'cbc', 'stopped'), ('bc', 'acc', 'cca', 'stopped'), ('bc', 'acc', 'ccb', 'stopped'), ('bc', 'acc', 'ccc', 'stopped'), ('bc', 'caa', 'c', 'stopped'), ('bc', 'caa', 'ac', 'stopped'), ('bc', 'caa', 'bc', 'stopped'), ('bc', 'caa', 'ca', 'stopped'), ('bc', 'caa', 'cb', 'stopped'), ('bc', 'caa', 'cc', 'stopped'), ('bc', 'caa', 'aac', 'stopped'), ('bc', 'caa', 'abc', 'stopped'), ('bc', 'caa', 'aca', 'stopped'), ('bc', 'caa', 'acb', 'stopped'), ('bc', 'caa', 'acc', 'stopped'), ('bc', 'caa', 'bac', 'stopped'), ('bc', 'caa', 'bbc', 'stopped'), ('bc', 'caa', 'bca', 'stopped'), ('bc', 'caa', 'bcb', 'stopped'), ('bc', 'caa', 'bcc', 'stopped'), ('bc', 'caa', 'caa', 'stopped'), ('bc', 'caa', 'cab', 'stopped'), ('bc', 'caa', 'cac', 'stopped'), ('bc', 'caa', 'cba', 'stopped'), ('bc', 'caa', 'cbb', 'stopped'), ('bc', 'caa', 'cbc', 'stopped'), ('bc', 'caa', 'cca', 'stopped'), ('bc', 'caa', 'ccb', 'stopped'), ('bc', 'caa', 'ccc', 'stopped'), ('bc', 'cac', 'c', 'stopped'), ('bc', 'cac', 'ac', 'stopped'), ('bc', 'cac', 'bc', 'stopped'), ('bc', 'cac', 'ca', 'stopped'), ('bc', 'cac', 'cb', 'stopped'), ('bc', 'cac', 'cc', 'stopped'), ('bc', 'cac', 'aac', 'stopped'), ('bc', 'cac', 'abc', 'stopped'), ('bc', 'cac', 'aca', 'stopped'), ('bc', 'cac', 'acb', 'stopped'), ('bc', 'cac', 'acc', 'stopped'), ('bc', 'cac', 'bac', 'stopped'), ('bc', 'cac', 'bbc', 'stopped'), ('bc', 'cac', 'bca', 'stopped'), ('bc', 'cac', 'bcb', 'stopped'), ('bc', 'cac', 'bcc', 'stopped'), ('bc', 'cac', 'caa', 'stopped'), ('bc', 'cac', 'cab', 'stopped'), ('bc', 'cac', 'cac', 'stopped'), ('bc', 'cac', 'cba', 'stopped'), ('bc', 'cac', 'cbb', 'stopped'), ('bc', 'cac', 'cbc', 'stopped'), ('bc', 'cac', 'cca', 'stopped'), ('bc', 'cac', 'ccb', 'stopped'), ('bc', 'cac', 'ccc', 'stopped'), ('bc', 'cbb', 'c', 'stopped'), ('bc', 'cbb', 'ac', 'stopped'), ('bc', 'cbb', 'bc', 'stopped'), ('bc', 'cbb', 'ca', 'stopped'), ('bc', 'cbb', 'cb', 'stopped'), ('bc', 'cbb', 'cc', 'stopped'), ('bc', 'cbb', 'aac', 'stopped'), ('bc', 'cbb', 'abc', 'stopped'), ('bc', 'cbb', 'aca', 'stopped'), ('bc', 'cbb', 'acb', 'stopped'), ('bc', 'cbb', 'acc', 'stopped'), ('bc', 'cbb', 'bac', 'stopped'), ('bc', 'cbb', 'bbc', 'stopped'), ('bc', 'cbb', 'bca', 'stopped'), ('bc', 'cbb', 'bcb', 'stopped'), ('bc', 'cbb', 'bcc', 'stopped'), ('bc', 'cbb', 'caa', 'stopped'), ('bc', 'cbb', 'cab', 'stopped'), ('bc', 'cbb', 'cac', 'stopped'), ('bc', 'cbb', 'cba', 'stopped'), ('bc', 'cbb', 'cbb', 'stopped'), ('bc', 'cbb', 'cbc', 'stopped'), ('bc', 'cbb', 'cca', 'stopped'), ('bc', 'cbb', 'ccb', 'stopped'), ('bc', 'cbb', 'ccc', 'stopped'), ('bc', 'cca', 'c', 'stopped'), ('bc', 'cca', 'ac', 'stopped'), ('bc', 'cca', 'bc', 'stopped'), ('bc', 'cca', 'ca', 'stopped'), ('bc', 'cca', 'cb', 'stopped'), ('bc', 'cca', 'cc', 'stopped'), ('bc', 'cca', 'aac', 'stopped'), ('bc', 'cca', 'abc', 'stopped'), ('bc', 'cca', 'aca', 'stopped'), ('bc', 'cca', 'acb', 'stopped'), ('bc', 'cca', 'acc', 'stopped'), ('bc', 'cca', 'bac', 'stopped'), ('bc', 'cca', 'bbc', 'stopped'), ('bc', 'cca', 'bca', 'stopped'), ('bc', 'cca', 'bcb', 'stopped'), ('bc', 'cca', 'bcc', 'stopped'), ('bc', 'cca', 'caa', 'stopped'), ('bc', 'cca', 'cab', 'stopped'), ('bc', 'cca', 'cac', 'stopped'), ('bc', 'cca', 'cba', 'stopped'), ('bc', 'cca', 'cbb', 'stopped'), ('bc', 'cca', 'cbc', 'stopped'), ('bc', 'cca', 'cca', 'stopped'), ('bc', 'cca', 'ccb', 'stopped'), ('bc', 'cca', 'ccc', 'stopped'), ('bc', 'ccb', 'c', 'stopped'), ('bc', 'ccb', 'ac', 'stopped'), ('bc', 'ccb', 'bc', 'stopped'), ('bc', 'ccb', 'ca', 'stopped'), ('bc', 'ccb', 'cb', 'stopped'), ('bc', 'ccb', 'cc', 'stopped'), ('bc', 'ccb', 'aac', 'stopped'), ('bc', 'ccb', 'abc', 'stopped'), ('bc', 'ccb', 'aca', 'stopped'), ('bc', 'ccb', 'acb', 'stopped'), ('bc', 'ccb', 'acc', 'stopped'), ('bc', 'ccb', 'bac', 'stopped'), ('bc', 'ccb', 'bbc', 'stopped'), ('bc', 'ccb', 'bca', 'stopped'), ('bc', 'ccb', 'bcb', 'stopped'), ('bc', 'ccb', 'bcc', 'stopped'), ('bc', 'ccb', 'caa', 'stopped'), ('bc', 'ccb', 'cab', 'stopped'), ('bc', 'ccb', 'cac', 'stopped'), ('bc', 'ccb', 'cba', 'stopped'), ('bc', 'ccb', 'cbb', 'stopped'), ('bc', 'ccb', 'cbc', 'stopped'), ('bc', 'ccb', 'cca', 'stopped'), ('bc', 'ccb', 'ccb', 'stopped'), ('bc', 'ccb', 'ccc', 'stopped'), ('bc', 'ccc', 'c', 'stopped'), ('bc', 'ccc', 'ac', 'stopped'), ('bc', 'ccc', 'bc', 'stopped'), ('bc', 'ccc', 'ca', 'stopped'), ('bc', 'ccc', 'cb', 'stopped'), ('bc', 'ccc', 'cc', 'stopped'), ('bc', 'ccc', 'aac', 'stopped'), ('bc', 'ccc', 'abc', 'stopped'), ('bc', 'ccc', 'aca', 'stopped'), ('bc', 'ccc', 'acb', 'stopped'), ('bc', 'ccc', 'acc', 'stopped'), ('bc', 'ccc', 'bac', 'stopped'), ('bc', 'ccc', 'bbc', 'stopped'), ('bc', 'ccc', 'bca', 'stopped'), ('bc', 'ccc', 'bcb', 'stopped'), ('bc', 'ccc', 'bcc', 'stopped'), ('bc', 'ccc', 'caa', 'stopped'), ('bc', 'ccc', 'cab', 'stopped'), ('bc', 'ccc', 'cac', 'stopped'), ('bc', 'ccc', 'cba', 'stopped'), ('bc', 'ccc', 'cbb', 'stopped'), ('bc', 'ccc', 'cbc', 'stopped'), ('bc', 'ccc', 'cca', 'stopped'), ('bc', 'ccc', 'ccb', 'stopped'), ('bc', 'ccc', 'ccc', 'stopped'), ('ca', 'bc', 'ac', 'stopped'), ('ca', 'bc', 'bc', 'stopped'), ('ca', 'bc', 'ca', 'stopped'), ('ca', 'bc', 'abc', 'stopped'), ('ca', 'bc', 'aca', 'stopped'), ('ca', 'bc', 'bbc', 'stopped'), ('ca', 'bc', 'bca', 'stopped'), ('ca', 'bc', 'caa', 'stopped'), ('ca', 'bc', 'cab', 'stopped'), ('ca', 'bc', 'cac', 'stopped'), ('ca', 'bc', 'cca', 'stopped'), ('ca', 'cb', 'c', 'stopped'), ('ca', 'cb', 'ac', 'stopped'), ('ca', 'cb', 'bc', 'stopped'), ('ca', 'cb', 'ca', 'stopped'), ('ca', 'cb', 'cb', 'stopped'), ('ca', 'cb', 'cc', 'stopped'), ('ca', 'cb', 'aac', 'stopped'), ('ca', 'cb', 'abc', 'stopped'), ('ca', 'cb', 'aca', 'stopped'), ('ca', 'cb', 'acb', 'stopped'), ('ca', 'cb', 'acc', 'stopped'), ('ca', 'cb', 'bac', 'stopped'), ('ca', 'cb', 'bbc', 'stopped'), ('ca', 'cb', 'bca', 'stopped'), ('ca', 'cb', 'bcb', 'stopped'), ('ca', 'cb', 'bcc', 'stopped'), ('ca', 'cb', 'caa', 'stopped'), ('ca', 'cb', 'cac', 'stopped'), ('ca', 'cb', 'cbc', 'stopped'), ('ca', 'cb', 'cca', 'stopped'), ('ca', 'cb', 'ccc', 'stopped'), ('ca', 'cc', 'c', 'stopped'), ('ca', 'cc', 'ac', 'stopped'), ('ca', 'cc', 'ca', 'stopped'), ('ca', 'cc', 'cc', 'stopped'), ('ca', 'cc', 'abc', 'stopped'), ('ca', 'cc', 'aca', 'stopped'), ('ca', 'cc', 'acc', 'stopped'), ('ca', 'cc', 'bca', 'stopped'), ('ca', 'cc', 'caa', 'stopped'), ('ca', 'cc', 'cab', 'stopped'), ('ca', 'cc', 'cac', 'stopped'), ('ca', 'cc', 'cca', 'stopped'), ('ca', 'cc', 'ccc', 'stopped'), ('ca', 'aac', 'c', 'stopped'), ('ca', 'aac', 'ac', 'stopped'), ('ca', 'aac', 'bc', 'stopped'), ('ca', 'aac', 'ca', 'stopped'), ('ca', 'aac', 'cb', 'stopped'), ('ca', 'aac', 'cc', 'stopped'), ('ca', 'aac', 'aac', 'stopped'), ('ca', 'aac', 'abc', 'stopped'), ('ca', 'aac', 'aca', 'stopped'), ('ca', 'aac', 'acb', 'stopped'), ('ca', 'aac', 'acc', 'stopped'), ('ca', 'aac', 'bac', 'stopped'), ('ca', 'aac', 'bbc', 'stopped'), ('ca', 'aac', 'bca', 'stopped'), ('ca', 'aac', 'bcb', 'stopped'), ('ca', 'aac', 'bcc', 'stopped'), ('ca', 'aac', 'caa', 'stopped'), ('ca', 'aac', 'cab', 'stopped'), ('ca', 'aac', 'cac', 'stopped'), ('ca', 'aac', 'cba', 'stopped'), ('ca', 'aac', 'cbb', 'stopped'), ('ca', 'aac', 'cbc', 'stopped'), ('ca', 'aac', 'cca', 'stopped'), ('ca', 'aac', 'ccb', 'stopped'), ('ca', 'aac', 'ccc', 'stopped'), ('ca', 'acb', 'c', 'stopped'), ('ca', 'acb', 'ac', 'stopped'), ('ca', 'acb', 'bc', 'stopped'), ('ca', 'acb', 'ca', 'stopped'), ('ca', 'acb', 'cb', 'stopped'), ('ca', 'acb', 'cc', 'stopped'), ('ca', 'acb', 'aac', 'stopped'), ('ca', 'acb', 'abc', 'stopped'), ('ca', 'acb', 'aca', 'stopped'), ('ca', 'acb', 'acb', 'stopped'), ('ca', 'acb', 'acc', 'stopped'), ('ca', 'acb', 'bac', 'stopped'), ('ca', 'acb', 'bbc', 'stopped'), ('ca', 'acb', 'bca', 'stopped'), ('ca', 'acb', 'bcb', 'stopped'), ('ca', 'acb', 'bcc', 'stopped'), ('ca', 'acb', 'caa', 'stopped'), ('ca', 'acb', 'cab', 'stopped'), ('ca', 'acb', 'cac', 'stopped'), ('ca', 'acb', 'cbb', 'stopped'), ('ca', 'acb', 'cbc', 'stopped'), ('ca', 'acb', 'cca', 'stopped'), ('ca', 'acb', 'ccb', 'stopped'), ('ca', 'acb', 'ccc', 'stopped'), ('ca', 'acc', 'c', 'stopped'), ('ca', 'acc', 'ac', 'stopped'), ('ca', 'acc', 'bc', 'stopped'), ('ca', 'acc', 'ca', 'stopped'), ('ca', 'acc', 'cb', 'stopped'), ('ca', 'acc', 'cc', 'stopped'), ('ca', 'acc', 'aac', 'stopped'), ('ca', 'acc', 'abc', 'stopped'), ('ca', 'acc', 'aca', 'stopped'), ('ca', 'acc', 'acb', 'stopped'), ('ca', 'acc', 'acc', 'stopped'), ('ca', 'acc', 'bac', 'stopped'), ('ca', 'acc', 'bbc', 'stopped'), ('ca', 'acc', 'bca', 'stopped'), ('ca', 'acc', 'bcb', 'stopped'), ('ca', 'acc', 'bcc', 'stopped'), ('ca', 'acc', 'caa', 'stopped'), ('ca', 'acc', 'cab', 'stopped'), ('ca', 'acc', 'cac', 'stopped'), ('ca', 'acc', 'cba', 'stopped'), ('ca', 'acc', 'cbb', 'stopped'), ('ca', 'acc', 'cbc', 'stopped'), ('ca', 'acc', 'cca', 'stopped'), ('ca', 'acc', 'ccb', 'stopped'), ('ca', 'acc', 'ccc', 'stopped'), ('ca', 'bbc', 'c', 'stopped'), ('ca', 'bbc', 'ac', 'stopped'), ('ca', 'bbc', 'bc', 'stopped'), ('ca', 'bbc', 'ca', 'stopped'), ('ca', 'bbc', 'cb', 'stopped'), ('ca', 'bbc', 'cc', 'stopped'), ('ca', 'bbc', 'aac', 'stopped'), ('ca', 'bbc', 'abc', 'stopped'), ('ca', 'bbc', 'aca', 'stopped'), ('ca', 'bbc', 'acb', 'stopped'), ('ca', 'bbc', 'acc', 'stopped'), ('ca', 'bbc', 'bac', 'stopped'), ('ca', 'bbc', 'bbc', 'stopped'), ('ca', 'bbc', 'bca', 'stopped'), ('ca', 'bbc', 'bcb', 'stopped'), ('ca', 'bbc', 'bcc', 'stopped'), ('ca', 'bbc', 'caa', 'stopped'), ('ca', 'bbc', 'cab', 'stopped'), ('ca', 'bbc', 'cac', 'stopped'), ('ca', 'bbc', 'cba', 'stopped'), ('ca', 'bbc', 'cbb', 'stopped'), ('ca', 'bbc', 'cbc', 'stopped'), ('ca', 'bbc', 'cca', 'stopped'), ('ca', 'bbc', 'ccb', 'stopped'), ('ca', 'bbc', 'ccc', 'stopped'), ('ca', 'bcb', 'c', 'stopped'), ('ca', 'bcb', 'ac', 'stopped'), ('ca', 'bcb', 'bc', 'stopped'), ('ca', 'bcb', 'ca', 'stopped'), ('ca', 'bcb', 'cb', 'stopped'), ('ca', 'bcb', 'cc', 'stopped'), ('ca', 'bcb', 'aac', 'stopped'), ('ca', 'bcb', 'abc', 'stopped'), ('ca', 'bcb', 'aca', 'stopped'), ('ca', 'bcb', 'acb', 'stopped'), ('ca', 'bcb', 'acc', 'stopped'), ('ca', 'bcb', 'bac', 'stopped'), ('ca', 'bcb', 'bbc', 'stopped'), ('ca', 'bcb', 'bca', 'stopped'), ('ca', 'bcb', 'bcb', 'stopped'), ('ca', 'bcb', 'bcc', 'stopped'), ('ca', 'bcb', 'caa', 'stopped'), ('ca', 'bcb', 'cab', 'stopped'), ('ca', 'bcb', 'cac', 'stopped'), ('ca', 'bcb', 'cba', 'stopped'), ('ca', 'bcb', 'cbb', 'stopped'), ('ca', 'bcb', 'cbc', 'stopped'), ('ca', 'bcb', 'cca', 'stopped'), ('ca', 'bcb', 'ccb', 'stopped'), ('ca', 'bcb', 'ccc', 'stopped'), ('ca', 'bcc', 'c', 'stopped'), ('ca', 'bcc', 'ac', 'stopped'), ('ca', 'bcc', 'bc', 'stopped'), ('ca', 'bcc', 'ca', 'stopped'), ('ca', 'bcc', 'cb', 'stopped'), ('ca', 'bcc', 'cc', 'stopped'), ('ca', 'bcc', 'aac', 'stopped'), ('ca', 'bcc', 'abc', 'stopped'), ('ca', 'bcc', 'aca', 'stopped'), ('ca', 'bcc', 'acb', 'stopped'), ('ca', 'bcc', 'acc', 'stopped'), ('ca', 'bcc', 'bac', 'stopped'), ('ca', 'bcc', 'bbc', 'stopped'), ('ca', 'bcc', 'bca', 'stopped'), ('ca', 'bcc', 'bcb', 'stopped'), ('ca', 'bcc', 'bcc', 'stopped'), ('ca', 'bcc', 'caa', 'stopped'), ('ca', 'bcc', 'cab', 'stopped'), ('ca', 'bcc', 'cac', 'stopped'), ('ca', 'bcc', 'cba', 'stopped'), ('ca', 'bcc', 'cbb', 'stopped'), ('ca', 'bcc', 'cbc', 'stopped'), ('ca', 'bcc', 'cca', 'stopped'), ('ca', 'bcc', 'ccb', 'stopped'), ('ca', 'bcc', 'ccc', 'stopped'), ('ca', 'cbb', 'c', 'stopped'), ('ca', 'cbb', 'ac', 'stopped'), ('ca', 'cbb', 'bc', 'stopped'), ('ca', 'cbb', 'ca', 'stopped'), ('ca', 'cbb', 'cb', 'stopped'), ('ca', 'cbb', 'cc', 'stopped'), ('ca', 'cbb', 'aac', 'stopped'), ('ca', 'cbb', 'abc', 'stopped'), ('ca', 'cbb', 'aca', 'stopped'), ('ca', 'cbb', 'acb', 'stopped'), ('ca', 'cbb', 'acc', 'stopped'), ('ca', 'cbb', 'bac', 'stopped'), ('ca', 'cbb', 'bbc', 'stopped'), ('ca', 'cbb', 'bca', 'stopped'), ('ca', 'cbb', 'bcb', 'stopped'), ('ca', 'cbb', 'bcc', 'stopped'), ('ca', 'cbb', 'caa', 'stopped'), ('ca', 'cbb', 'cac', 'stopped'), ('ca', 'cbb', 'cba', 'stopped'), ('ca', 'cbb', 'cbb', 'stopped'), ('ca', 'cbb', 'cbc', 'stopped'), ('ca', 'cbb', 'cca', 'stopped'), ('ca', 'cbb', 'ccb', 'stopped'), ('ca', 'cbb', 'ccc', 'stopped'), ('ca', 'cbc', 'c', 'stopped'), ('ca', 'cbc', 'ac', 'stopped'), ('ca', 'cbc', 'bc', 'stopped'), ('ca', 'cbc', 'ca', 'stopped'), ('ca', 'cbc', 'cb', 'stopped'), ('ca', 'cbc', 'cc', 'stopped'), ('ca', 'cbc', 'aac', 'stopped'), ('ca', 'cbc', 'abc', 'stopped'), ('ca', 'cbc', 'aca', 'stopped'), ('ca', 'cbc', 'acb', 'stopped'), ('ca', 'cbc', 'acc', 'stopped'), ('ca', 'cbc', 'bac', 'stopped'), ('ca', 'cbc', 'bbc', 'stopped'), ('ca', 'cbc', 'bca', 'stopped'), ('ca', 'cbc', 'bcb', 'stopped'), ('ca', 'cbc', 'bcc', 'stopped'), ('ca', 'cbc', 'caa', 'stopped'), ('ca', 'cbc', 'cab', 'stopped'), ('ca', 'cbc', 'cac', 'stopped'), ('ca', 'cbc', 'cba', 'stopped'), ('ca', 'cbc', 'cbb', 'stopped'), ('ca', 'cbc', 'cbc', 'stopped'), ('ca', 'cbc', 'cca', 'stopped'), ('ca', 'cbc', 'ccb', 'stopped'), ('ca', 'cbc', 'ccc', 'stopped'), ('ca', 'ccb', 'c', 'stopped'), ('ca', 'ccb', 'ac', 'stopped'), ('ca', 'ccb', 'bc', 'stopped'), ('ca', 'ccb', 'ca', 'stopped'), ('ca', 'ccb', 'cb', 'stopped'), ('ca', 'ccb', 'cc', 'stopped'), ('ca', 'ccb', 'aac', 'stopped'), ('ca', 'ccb', 'abc', 'stopped'), ('ca', 'ccb', 'aca', 'stopped'), ('ca', 'ccb', 'acb', 'stopped'), ('ca', 'ccb', 'acc', 'stopped'), ('ca', 'ccb', 'bac', 'stopped'), ('ca', 'ccb', 'bbc', 'stopped'), ('ca', 'ccb', 'bca', 'stopped'), ('ca', 'ccb', 'bcb', 'stopped'), ('ca', 'ccb', 'bcc', 'stopped'), ('ca', 'ccb', 'caa', 'stopped'), ('ca', 'ccb', 'cab', 'stopped'), ('ca', 'ccb', 'cac', 'stopped'), ('ca', 'ccb', 'cba', 'stopped'), ('ca', 'ccb', 'cbb', 'stopped'), ('ca', 'ccb', 'cbc', 'stopped'), ('ca', 'ccb', 'cca', 'stopped'), ('ca', 'ccb', 'ccb', 'stopped'), ('ca', 'ccb', 'ccc', 'stopped'), ('ca', 'ccc', 'c', 'stopped'), ('ca', 'ccc', 'ac', 'stopped'), ('ca', 'ccc', 'ca', 'stopped'), ('ca', 'ccc', 'cc', 'stopped'), ('ca', 'ccc', 'abc', 'stopped'), ('ca', 'ccc', 'aca', 'stopped'), ('ca', 'ccc', 'acc', 'stopped'), ('ca', 'ccc', 'bca', 'stopped'), ('ca', 'ccc', 'caa', 'stopped'), ('ca', 'ccc', 'cab', 'stopped'), ('ca', 'ccc', 'cac', 'stopped'), ('ca', 'ccc', 'cca', 'stopped'), ('ca', 'ccc', 'ccc', 'stopped'), ('cb', 'cc', 'c', 'stopped'), ('cb', 'cc', 'bc', 'stopped'), ('cb', 'cc', 'cb', 'stopped'), ('cb', 'cc', 'cc', 'stopped'), ('cb', 'cc', 'abc', 'stopped'), ('cb', 'cc', 'bcb', 'stopped'), ('cb', 'cc', 'bcc', 'stopped'), ('cb', 'cc', 'cbb', 'stopped'), ('cb', 'cc', 'cbc', 'stopped'), ('cb', 'cc', 'ccb', 'stopped'), ('cb', 'cc', 'ccc', 'stopped'), ('cb', 'aca', 'abc', 'stopped'), ('cb', 'aca', 'acb', 'stopped'), ('cb', 'aca', 'bac', 'stopped'), ('cb', 'acc', 'c', 'stopped'), ('cb', 'acc', 'ac', 'stopped'), ('cb', 'acc', 'bc', 'stopped'), ('cb', 'acc', 'ca', 'stopped'), ('cb', 'acc', 'cb', 'stopped'), ('cb', 'acc', 'cc', 'stopped'), ('cb', 'acc', 'aac', 'stopped'), ('cb', 'acc', 'abc', 'stopped'), ('cb', 'acc', 'aca', 'stopped'), ('cb', 'acc', 'acb', 'stopped'), ('cb', 'acc', 'acc', 'stopped'), ('cb', 'acc', 'bac', 'stopped'), ('cb', 'acc', 'bbc', 'stopped'), ('cb', 'acc', 'bca', 'stopped'), ('cb', 'acc', 'bcb', 'stopped'), ('cb', 'acc', 'bcc', 'stopped'), ('cb', 'acc', 'caa', 'stopped'), ('cb', 'acc', 'cac', 'stopped'), ('cb', 'acc', 'cbb', 'stopped'), ('cb', 'acc', 'cbc', 'stopped'), ('cb', 'acc', 'cca', 'stopped'), ('cb', 'acc', 'ccb', 'stopped'), ('cb', 'acc', 'ccc', 'stopped'), ('cb', 'bbc', 'c', 'stopped'), ('cb', 'bbc', 'ac', 'stopped'), ('cb', 'bbc', 'bc', 'stopped'), ('cb', 'bbc', 'ca', 'stopped'), ('cb', 'bbc', 'cb', 'stopped'), ('cb', 'bbc', 'cc', 'stopped'), ('cb', 'bbc', 'aac', 'stopped'), ('cb', 'bbc', 'abc', 'stopped'), ('cb', 'bbc', 'aca', 'stopped'), ('cb', 'bbc', 'acb', 'stopped'), ('cb', 'bbc', 'acc', 'stopped'), ('cb', 'bbc', 'bac', 'stopped'), ('cb', 'bbc', 'bbc', 'stopped'), ('cb', 'bbc', 'bca', 'stopped'), ('cb', 'bbc', 'bcb', 'stopped'), ('cb', 'bbc', 'bcc', 'stopped'), ('cb', 'bbc', 'caa', 'stopped'), ('cb', 'bbc', 'cac', 'stopped'), ('cb', 'bbc', 'cbb', 'stopped'), ('cb', 'bbc', 'cbc', 'stopped'), ('cb', 'bbc', 'cca', 'stopped'), ('cb', 'bbc', 'ccb', 'stopped'), ('cb', 'bbc', 'ccc', 'stopped'), ('cb', 'bca', 'bc', 'stopped'), ('cb', 'bca', 'abc', 'stopped'), ('cb', 'bca', 'acb', 'stopped'), ('cb', 'bca', 'bca', 'stopped'), ('cb', 'bca', 'bcb', 'stopped'), ('cb', 'bca', 'cbb', 'stopped'), ('cb', 'bca', 'cbc', 'stopped'), ('cb', 'bca', 'ccb', 'stopped'), ('cb', 'bcc', 'c', 'stopped'), ('cb', 'bcc', 'ac', 'stopped'), ('cb', 'bcc', 'bc', 'stopped'), ('cb', 'bcc', 'ca', 'stopped'), ('cb', 'bcc', 'cb', 'stopped'), ('cb', 'bcc', 'cc', 'stopped'), ('cb', 'bcc', 'aac', 'stopped'), ('cb', 'bcc', 'abc', 'stopped'), ('cb', 'bcc', 'aca', 'stopped'), ('cb', 'bcc', 'acb', 'stopped'), ('cb', 'bcc', 'acc', 'stopped'), ('cb', 'bcc', 'bac', 'stopped'), ('cb', 'bcc', 'bbc', 'stopped'), ('cb', 'bcc', 'bca', 'stopped'), ('cb', 'bcc', 'bcb', 'stopped'), ('cb', 'bcc', 'bcc', 'stopped'), ('cb', 'bcc', 'caa', 'stopped'), ('cb', 'bcc', 'cac', 'stopped'), ('cb', 'bcc', 'cbb', 'stopped'), ('cb', 'bcc', 'cbc', 'stopped'), ('cb', 'bcc', 'cca', 'stopped'), ('cb', 'bcc', 'ccb', 'stopped'), ('cb', 'bcc', 'ccc', 'stopped'), ('cb', 'ccc', 'c', 'stopped'), ('cb', 'ccc', 'ac', 'stopped'), ('cb', 'ccc', 'bc', 'stopped'), ('cb', 'ccc', 'ca', 'stopped'), ('cb', 'ccc', 'cb', 'stopped'), ('cb', 'ccc', 'cc', 'stopped'), ('cb', 'ccc', 'aac', 'stopped'), ('cb', 'ccc', 'abc', 'stopped'), ('cb', 'ccc', 'aca', 'stopped'), ('cb', 'ccc', 'acb', 'stopped'), ('cb', 'ccc', 'acc', 'stopped'), ('cb', 'ccc', 'bac', 'stopped'), ('cb', 'ccc', 'bbc', 'stopped'), ('cb', 'ccc', 'bca', 'stopped'), ('cb', 'ccc', 'bcb', 'stopped'), ('cb', 'ccc', 'bcc', 'stopped'), ('cb', 'ccc', 'caa', 'stopped'), ('cb', 'ccc', 'cac', 'stopped'), ('cb', 'ccc', 'cbb', 'stopped'), ('cb', 'ccc', 'cbc', 'stopped'), ('cb', 'ccc', 'cca', 'stopped'), ('cb', 'ccc', 'ccb', 'stopped'), ('cb', 'ccc', 'ccc', 'stopped'), ('cc', 'ac', 'c', 'stopped'), ('cc', 'ac', 'ac', 'stopped'), ('cc', 'ac', 'bc', 'stopped'), ('cc', 'ac', 'ca', 'stopped'), ('cc', 'ac', 'cb', 'stopped'), ('cc', 'ac', 'cc', 'stopped'), ('cc', 'ac', 'aca', 'stopped'), ('cc', 'ac', 'acb', 'stopped'), ('cc', 'ac', 'bbc', 'stopped'), ('cc', 'ac', 'bca', 'stopped'), ('cc', 'ac', 'bcb', 'stopped'), ('cc', 'ac', 'bcc', 'stopped'), ('cc', 'ac', 'caa', 'stopped'), ('cc', 'ac', 'cab', 'stopped'), ('cc', 'ac', 'cac', 'stopped'), ('cc', 'ac', 'cba', 'stopped'), ('cc', 'ac', 'cbb', 'stopped'), ('cc', 'ac', 'cbc', 'stopped'), ('cc', 'ac', 'ccb', 'stopped'), ('cc', 'ac', 'ccc', 'stopped'), ('cc', 'bc', 'c', 'stopped'), ('cc', 'bc', 'ac', 'stopped'), ('cc', 'bc', 'bc', 'stopped'), ('cc', 'bc', 'ca', 'stopped'), ('cc', 'bc', 'cb', 'stopped'), ('cc', 'bc', 'cc', 'stopped'), ('cc', 'bc', 'aac', 'stopped'), ('cc', 'bc', 'abc', 'stopped'), ('cc', 'bc', 'aca', 'stopped'), ('cc', 'bc', 'acb', 'stopped'), ('cc', 'bc', 'acc', 'stopped'), ('cc', 'bc', 'bca', 'stopped'), ('cc', 'bc', 'bcb', 'stopped'), ('cc', 'bc', 'bcc', 'stopped'), ('cc', 'bc', 'caa', 'stopped'), ('cc', 'bc', 'cab', 'stopped'), ('cc', 'bc', 'cac', 'stopped'), ('cc', 'bc', 'cba', 'stopped'), ('cc', 'bc', 'cbb', 'stopped'), ('cc', 'bc', 'cbc', 'stopped'), ('cc', 'bc', 'cca', 'stopped'), ('cc', 'bc', 'ccc', 'stopped'), ('cc', 'ca', 'c', 'stopped'), ('cc', 'ca', 'ac', 'stopped'), ('cc', 'ca', 'bc', 'stopped'), ('cc', 'ca', 'ca', 'stopped'), ('cc', 'ca', 'cb', 'stopped'), ('cc', 'ca', 'cc', 'stopped'), ('cc', 'ca', 'aac', 'stopped'), ('cc', 'ca', 'abc', 'stopped'), ('cc', 'ca', 'aca', 'stopped'), ('cc', 'ca', 'acb', 'stopped'), ('cc', 'ca', 'bac', 'stopped'), ('cc', 'ca', 'bbc', 'stopped'), ('cc', 'ca', 'bcb', 'stopped'), ('cc', 'ca', 'bcc', 'stopped'), ('cc', 'ca', 'cab', 'stopped'), ('cc', 'ca', 'cbb', 'stopped'), ('cc', 'ca', 'cbc', 'stopped'), ('cc', 'ca', 'ccb', 'stopped'), ('cc', 'ca', 'ccc', 'stopped'), ('cc', 'cb', 'c', 'stopped'), ('cc', 'cb', 'ac', 'stopped'), ('cc', 'cb', 'bc', 'stopped'), ('cc', 'cb', 'ca', 'stopped'), ('cc', 'cb', 'cb', 'stopped'), ('cc', 'cb', 'cc', 'stopped'), ('cc', 'cb', 'aac', 'stopped'), ('cc', 'cb', 'abc', 'stopped'), ('cc', 'cb', 'aca', 'stopped'), ('cc', 'cb', 'acb', 'stopped'), ('cc', 'cb', 'acc', 'stopped'), ('cc', 'cb', 'bac', 'stopped'), ('cc', 'cb', 'bbc', 'stopped'), ('cc', 'cb', 'bca', 'stopped'), ('cc', 'cb', 'bcb', 'stopped'), ('cc', 'cb', 'caa', 'stopped'), ('cc', 'cb', 'cac', 'stopped'), ('cc', 'cb', 'cbb', 'stopped'), ('cc', 'cb', 'cca', 'stopped'), ('cc', 'cb', 'ccc', 'stopped'), ('cc', 'aac', 'c', 'stopped'), ('cc', 'aac', 'ac', 'stopped'), ('cc', 'aac', 'bc', 'stopped'), ('cc', 'aac', 'ca', 'stopped'), ('cc', 'aac', 'cb', 'stopped'), ('cc', 'aac', 'cc', 'stopped'), ('cc', 'aac', 'abc', 'stopped'), ('cc', 'aac', 'aca', 'stopped'), ('cc', 'aac', 'acb', 'stopped'), ('cc', 'aac', 'acc', 'stopped'), ('cc', 'aac', 'bac', 'stopped'), ('cc', 'aac', 'bbc', 'stopped'), ('cc', 'aac', 'bca', 'stopped'), ('cc', 'aac', 'bcb', 'stopped'), ('cc', 'aac', 'bcc', 'stopped'), ('cc', 'aac', 'caa', 'stopped'), ('cc', 'aac', 'cab', 'stopped'), ('cc', 'aac', 'cac', 'stopped'), ('cc', 'aac', 'cba', 'stopped'), ('cc', 'aac', 'cbb', 'stopped'), ('cc', 'aac', 'cbc', 'stopped'), ('cc', 'aac', 'cca', 'stopped'), ('cc', 'aac', 'ccb', 'stopped'), ('cc', 'aac', 'ccc', 'stopped'), ('cc', 'aca', 'c', 'stopped'), ('cc', 'aca', 'ac', 'stopped'), ('cc', 'aca', 'bc', 'stopped'), ('cc', 'aca', 'ca', 'stopped'), ('cc', 'aca', 'cb', 'stopped'), ('cc', 'aca', 'cc', 'stopped'), ('cc', 'aca', 'aac', 'stopped'), ('cc', 'aca', 'abc', 'stopped'), ('cc', 'aca', 'aca', 'stopped'), ('cc', 'aca', 'acb', 'stopped'), ('cc', 'aca', 'acc', 'stopped'), ('cc', 'aca', 'bac', 'stopped'), ('cc', 'aca', 'bbc', 'stopped'), ('cc', 'aca', 'bca', 'stopped'), ('cc', 'aca', 'bcb', 'stopped'), ('cc', 'aca', 'bcc', 'stopped'), ('cc', 'aca', 'caa', 'stopped'), ('cc', 'aca', 'cab', 'stopped'), ('cc', 'aca', 'cac', 'stopped'), ('cc', 'aca', 'cba', 'stopped'), ('cc', 'aca', 'cbb', 'stopped'), ('cc', 'aca', 'cbc', 'stopped'), ('cc', 'aca', 'cca', 'stopped'), ('cc', 'aca', 'ccb', 'stopped'), ('cc', 'aca', 'ccc', 'stopped'), ('cc', 'acb', 'c', 'stopped'), ('cc', 'acb', 'ac', 'stopped'), ('cc', 'acb', 'bc', 'stopped'), ('cc', 'acb', 'ca', 'stopped'), ('cc', 'acb', 'cb', 'stopped'), ('cc', 'acb', 'cc', 'stopped'), ('cc', 'acb', 'aac', 'stopped'), ('cc', 'acb', 'abc', 'stopped'), ('cc', 'acb', 'aca', 'stopped'), ('cc', 'acb', 'acc', 'stopped'), ('cc', 'acb', 'bac', 'stopped'), ('cc', 'acb', 'bbc', 'stopped'), ('cc', 'acb', 'bca', 'stopped'), ('cc', 'acb', 'bcb', 'stopped'), ('cc', 'acb', 'bcc', 'stopped'), ('cc', 'acb', 'caa', 'stopped'), ('cc', 'acb', 'cab', 'stopped'), ('cc', 'acb', 'cac', 'stopped'), ('cc', 'acb', 'cba', 'stopped'), ('cc', 'acb', 'cbb', 'stopped'), ('cc', 'acb', 'cbc', 'stopped'), ('cc', 'acb', 'cca', 'stopped'), ('cc', 'acb', 'ccb', 'stopped'), ('cc', 'acb', 'ccc', 'stopped'), ('cc', 'bac', 'c', 'stopped'), ('cc', 'bac', 'ac', 'stopped'), ('cc', 'bac', 'bc', 'stopped'), ('cc', 'bac', 'ca', 'stopped'), ('cc', 'bac', 'cb', 'stopped'), ('cc', 'bac', 'cc', 'stopped'), ('cc', 'bac', 'aac', 'stopped'), ('cc', 'bac', 'abc', 'stopped'), ('cc', 'bac', 'aca', 'stopped'), ('cc', 'bac', 'acb', 'stopped'), ('cc', 'bac', 'acc', 'stopped'), ('cc', 'bac', 'bbc', 'stopped'), ('cc', 'bac', 'bca', 'stopped'), ('cc', 'bac', 'bcb', 'stopped'), ('cc', 'bac', 'bcc', 'stopped'), ('cc', 'bac', 'caa', 'stopped'), ('cc', 'bac', 'cab', 'stopped'), ('cc', 'bac', 'cac', 'stopped'), ('cc', 'bac', 'cba', 'stopped'), ('cc', 'bac', 'cbb', 'stopped'), ('cc', 'bac', 'cbc', 'stopped'), ('cc', 'bac', 'cca', 'stopped'), ('cc', 'bac', 'ccb', 'stopped'), ('cc', 'bac', 'ccc', 'stopped'), ('cc', 'bbc', 'c', 'stopped'), ('cc', 'bbc', 'ac', 'stopped'), ('cc', 'bbc', 'bc', 'stopped'), ('cc', 'bbc', 'ca', 'stopped'), ('cc', 'bbc', 'cb', 'stopped'), ('cc', 'bbc', 'cc', 'stopped'), ('cc', 'bbc', 'aac', 'stopped'), ('cc', 'bbc', 'abc', 'stopped'), ('cc', 'bbc', 'aca', 'stopped'), ('cc', 'bbc', 'acb', 'stopped'), ('cc', 'bbc', 'acc', 'stopped'), ('cc', 'bbc', 'bac', 'stopped'), ('cc', 'bbc', 'bbc', 'stopped'), ('cc', 'bbc', 'bca', 'stopped'), ('cc', 'bbc', 'bcb', 'stopped'), ('cc', 'bbc', 'bcc', 'stopped'), ('cc', 'bbc', 'caa', 'stopped'), ('cc', 'bbc', 'cab', 'stopped'), ('cc', 'bbc', 'cac', 'stopped'), ('cc', 'bbc', 'cba', 'stopped'), ('cc', 'bbc', 'cbb', 'stopped'), ('cc', 'bbc', 'cbc', 'stopped'), ('cc', 'bbc', 'cca', 'stopped'), ('cc', 'bbc', 'ccb', 'stopped'), ('cc', 'bbc', 'ccc', 'stopped'), ('cc', 'bca', 'c', 'stopped'), ('cc', 'bca', 'ac', 'stopped'), ('cc', 'bca', 'bc', 'stopped'), ('cc', 'bca', 'ca', 'stopped'), ('cc', 'bca', 'cb', 'stopped'), ('cc', 'bca', 'cc', 'stopped'), ('cc', 'bca', 'aac', 'stopped'), ('cc', 'bca', 'abc', 'stopped'), ('cc', 'bca', 'aca', 'stopped'), ('cc', 'bca', 'acb', 'stopped'), ('cc', 'bca', 'acc', 'stopped'), ('cc', 'bca', 'bac', 'stopped'), ('cc', 'bca', 'bbc', 'stopped'), ('cc', 'bca', 'bcb', 'stopped'), ('cc', 'bca', 'bcc', 'stopped'), ('cc', 'bca', 'caa', 'stopped'), ('cc', 'bca', 'cab', 'stopped'), ('cc', 'bca', 'cac', 'stopped'), ('cc', 'bca', 'cba', 'stopped'), ('cc', 'bca', 'cbb', 'stopped'), ('cc', 'bca', 'cbc', 'stopped'), ('cc', 'bca', 'cca', 'stopped'), ('cc', 'bca', 'ccb', 'stopped'), ('cc', 'bca', 'ccc', 'stopped'), ('cc', 'bcb', 'c', 'stopped'), ('cc', 'bcb', 'ac', 'stopped'), ('cc', 'bcb', 'bc', 'stopped'), ('cc', 'bcb', 'ca', 'stopped'), ('cc', 'bcb', 'cb', 'stopped'), ('cc', 'bcb', 'cc', 'stopped'), ('cc', 'bcb', 'aac', 'stopped'), ('cc', 'bcb', 'abc', 'stopped'), ('cc', 'bcb', 'aca', 'stopped'), ('cc', 'bcb', 'acb', 'stopped'), ('cc', 'bcb', 'acc', 'stopped'), ('cc', 'bcb', 'bac', 'stopped'), ('cc', 'bcb', 'bbc', 'stopped'), ('cc', 'bcb', 'bca', 'stopped'), ('cc', 'bcb', 'bcb', 'stopped'), ('cc', 'bcb', 'bcc', 'stopped'), ('cc', 'bcb', 'caa', 'stopped'), ('cc', 'bcb', 'cab', 'stopped'), ('cc', 'bcb', 'cac', 'stopped'), ('cc', 'bcb', 'cba', 'stopped'), ('cc', 'bcb', 'cbb', 'stopped'), ('cc', 'bcb', 'cbc', 'stopped'), ('cc', 'bcb', 'cca', 'stopped'), ('cc', 'bcb', 'ccb', 'stopped'), ('cc', 'bcb', 'ccc', 'stopped'), ('cc', 'caa', 'c', 'stopped'), ('cc', 'caa', 'ac', 'stopped'), ('cc', 'caa', 'bc', 'stopped'), ('cc', 'caa', 'ca', 'stopped'), ('cc', 'caa', 'cb', 'stopped'), ('cc', 'caa', 'cc', 'stopped'), ('cc', 'caa', 'aac', 'stopped'), ('cc', 'caa', 'abc', 'stopped'), ('cc', 'caa', 'aca', 'stopped'), ('cc', 'caa', 'acb', 'stopped'), ('cc', 'caa', 'acc', 'stopped'), ('cc', 'caa', 'bac', 'stopped'), ('cc', 'caa', 'bbc', 'stopped'), ('cc', 'caa', 'bca', 'stopped'), ('cc', 'caa', 'bcb', 'stopped'), ('cc', 'caa', 'bcc', 'stopped'), ('cc', 'caa', 'caa', 'stopped'), ('cc', 'caa', 'cab', 'stopped'), ('cc', 'caa', 'cac', 'stopped'), ('cc', 'caa', 'cba', 'stopped'), ('cc', 'caa', 'cbb', 'stopped'), ('cc', 'caa', 'cbc', 'stopped'), ('cc', 'caa', 'cca', 'stopped'), ('cc', 'caa', 'ccb', 'stopped'), ('cc', 'caa', 'ccc', 'stopped'), ('cc', 'cac', 'c', 'stopped'), ('cc', 'cac', 'ac', 'stopped'), ('cc', 'cac', 'ca', 'stopped'), ('cc', 'cac', 'cc', 'stopped'), ('cc', 'cac', 'abc', 'stopped'), ('cc', 'cac', 'acc', 'stopped'), ('cc', 'cac', 'bca', 'stopped'), ('cc', 'cac', 'cab', 'stopped'), ('cc', 'cac', 'cac', 'stopped'), ('cc', 'cac', 'cca', 'stopped'), ('cc', 'cac', 'ccc', 'stopped'), ('cc', 'cba', 'c', 'stopped'), ('cc', 'cba', 'ac', 'stopped'), ('cc', 'cba', 'bc', 'stopped'), ('cc', 'cba', 'ca', 'stopped'), ('cc', 'cba', 'cb', 'stopped'), ('cc', 'cba', 'cc', 'stopped'), ('cc', 'cba', 'aac', 'stopped'), ('cc', 'cba', 'abc', 'stopped'), ('cc', 'cba', 'aca', 'stopped'), ('cc', 'cba', 'acb', 'stopped'), ('cc', 'cba', 'acc', 'stopped'), ('cc', 'cba', 'bac', 'stopped'), ('cc', 'cba', 'bbc', 'stopped'), ('cc', 'cba', 'bca', 'stopped'), ('cc', 'cba', 'bcb', 'stopped'), ('cc', 'cba', 'bcc', 'stopped'), ('cc', 'cba', 'caa', 'stopped'), ('cc', 'cba', 'cab', 'stopped'), ('cc', 'cba', 'cac', 'stopped'), ('cc', 'cba', 'cbb', 'stopped'), ('cc', 'cba', 'cbc', 'stopped'), ('cc', 'cba', 'cca', 'stopped'), ('cc', 'cba', 'ccb', 'stopped'), ('cc', 'cba', 'ccc', 'stopped'), ('cc', 'cbb', 'c', 'stopped'), ('cc', 'cbb', 'ac', 'stopped'), ('cc', 'cbb', 'bc', 'stopped'), ('cc', 'cbb', 'ca', 'stopped'), ('cc', 'cbb', 'cb', 'stopped'), ('cc', 'cbb', 'cc', 'stopped'), ('cc', 'cbb', 'aac', 'stopped'), ('cc', 'cbb', 'abc', 'stopped'), ('cc', 'cbb', 'aca', 'stopped'), ('cc', 'cbb', 'acb', 'stopped'), ('cc', 'cbb', 'acc', 'stopped'), ('cc', 'cbb', 'bac', 'stopped'), ('cc', 'cbb', 'bbc', 'stopped'), ('cc', 'cbb', 'bca', 'stopped'), ('cc', 'cbb', 'bcb', 'stopped'), ('cc', 'cbb', 'bcc', 'stopped'), ('cc', 'cbb', 'caa', 'stopped'), ('cc', 'cbb', 'cab', 'stopped'), ('cc', 'cbb', 'cac', 'stopped'), ('cc', 'cbb', 'cba', 'stopped'), ('cc', 'cbb', 'cbc', 'stopped'), ('cc', 'cbb', 'cca', 'stopped'), ('cc', 'cbb', 'ccb', 'stopped'), ('cc', 'cbb', 'ccc', 'stopped'), ('cc', 'cbc', 'c', 'stopped'), ('cc', 'cbc', 'bc', 'stopped'), ('cc', 'cbc', 'cb', 'stopped'), ('cc', 'cbc', 'cc', 'stopped'), ('cc', 'cbc', 'abc', 'stopped'), ('cc', 'cbc', 'bca', 'stopped'), ('cc', 'cbc', 'bcc', 'stopped'), ('cc', 'cbc', 'cab', 'stopped'), ('cc', 'cbc', 'cbc', 'stopped'), ('cc', 'cbc', 'ccb', 'stopped'), ('cc', 'cbc', 'ccc', 'stopped')]
```

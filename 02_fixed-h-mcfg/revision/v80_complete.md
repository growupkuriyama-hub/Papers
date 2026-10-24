# #2 MCFG v80 完全版：fan-out 2 における短い分布同値代表元（統合文書）

- 作成日：2026-10-18（JST）
- ブランチ：`mcfg2-v80-short-distribution-representatives`／Draft PR #49（マージ不可）
- 基準：`origin/main` = `7ef2cb1`（`PAPER.yaml` は正本 **v79**＝rule-only witness 版、コミット `edc6b4a`）。PR #46 の「v79 研究草稿」とは別物。
- この文書は v80 の研究メモ・証明草稿（`v80_short_representatives.tex`）・走査結果・再現コードを **1つの Markdown にまとめたもの**です。
- `main.tex`・`main_JP.tex`・`PAPER.yaml` は**一切変更していません**。

---

## 目次

0. 結論の要約
1. 監査した資料と版
2. 記号と予想E
3. 補題R（緩和証人）の敵対的査読
4. 定理D（アーベル型フィルタ）の敵対的査読
5. 補題P：同一語内交換の Parikh 剛性
6. 定理 F1-sl：半束分割アーベル和集合（新規）
7. 有限走査による証拠
8. 失敗した原理（区分B）
9. 予想Eの到達度（区分D）
10. 次に必要な補題（区分F）
11. GitHub 成果物（区分E）
12. 再現方法
- 付録 A：走査出力
- 付録 B：ソースコード全文

---

## 0. 結論の要約

**予想Eは未解決です。** ただし証明済みの場合を一つ増やしました。

| 区分 | 内容 | 状態 |
|---|---|---|
| C | 補題R（緩和証人）の再監査 | **成立**。v79 正本の rule-only 最適化とは併用不可 |
| C | 定理D（アーベル型フィルタ）の再監査 | **成立**。群・φ・H・γ・Acc に一様 |
| A | 補題P：同一語内で文脈を共有する交換対は Parikh 同値 | **証明済み** |
| A | 定理 F1-sl：半束分割アーベル和集合の多項式データ | **証明済み（新規、独立監査待ち）** |
| B | 「局所可動性 ⇒ 短縮」「分岐整合 ⇒ 単一フィルタ」「分岐別部分群でも同じ証明」 | **不成立** |
| D | 予想E | **未解決**（証明済みの場合：LG・D・F1-sl） |
| 実験 | h_U 上の巡回群和集合（k≤6）、2マーカー内容型付け（k≤3、全関係） | 前者は非自明な所属 1,364 個すべてが F1-sl 型。後者は 6,958 個が「捻り共通部分群型」6,894＋「分岐別部分群型」64 |

---

## 1. 監査した資料と版

**開いたもの**
- `PAPER.yaml`（internal_version v79）
- `main.tex`：v79 で追加された `prop:rule-only-witnesses`、`prop:computed-witness-budget` の差分を含む
- `revision/v79_rule_only_witness_budget.md`
- PR #46 の研究ファイル（`v79_fanout2_results.tex` ほか）
- `appendix_local_group.tex`：前回監査分（主張と `lem:local-group-shortest`）

**開いていないもの（確認済みとして扱わない）**
- `appendix_window_group.tex`：今回は通読していません。本研究の証明はこれに依存しません。
- `main_JP.tex`：未読。
- Papadimitriou (1981) の一次資料：MIT DSpace に技術報告 MIT/LCS/TM-152 があることは確認しましたが、本環境からは PDF 取得がアクセスエラーで不可でした。小解定理の上界 n(ma)^{2m+1} は Fomin–Panolan–Ramanujan–Saurabh, arXiv:1607.05342 第1節の再掲で照合しています。

---

## 2. 記号と予想E

v79 正本の定義をそのまま使います。
- sentence context の内部区切りは非空、タプル成分は非空。
- D_L(x)：x と同じ arity の受理文脈の集合。
- x ≡_{L,h} y：成分ごとの h 型が等しく、分布も等しい。
- C^mcf_{f,h}：(f,h)-tuple-substitutable な f-MCFL 全体。B^{≤r}_{f,h}：capped 再構成器。
- G = (V,Σ,P,S) は reduced good 表現、G̃₀ は刈り込み済み yield-type refinement、L_X は型付き記号 X のタプル言語。
- t_G：非終端記号の厚さ、θ_G：規則の厚さ（t_G ≤ θ_G）。ψ：Parikh 写像、Ψ(u) = Σ_i ψ(u_i)。

開始記号でない型付き記号 X について、L_X を含む ≡_{L,h} 類を [X] とし、

$$\kappa_G(X)=\min\{\|v\|_1 : v\in[X]\},\qquad \kappa_G=\max_X \kappa_G(X).$$

**代表元 v は L_X にも、G のどのタプル言語にも属さなくてよい**ことに注意します。必要なのは、X と同じ型を持ち、**すべての**文脈について同じ分布を持つことだけです。

**予想E.** Σ, h, r を固定すると、ある多項式 p があって、fan-out ≤ 2・rank ≤ r の reduced good な G で L(G) ∈ C^mcf_{2,h} を満たすものはすべて

$$\kappa_G\le p\bigl(\|G\|\max\{1,\theta_G\}\bigr)$$

を満たす。

---

## 3. 補題R（緩和証人）の敵対的査読

**監査した主張.** 開始記号でない各型付き記号 X = A_𝐭 について次を選ぶ。
- 任意の ω′(X) ∈ [X]
- χ′(X)：G̃₀ に規則 S̃ → X があれば □₁、なければ G における**型なし**記号 A の任意の導出文脈

K* を次の語の集合とする：χ′(X)[ω′(X)]、型付き規則 X → ρ(Y₁,…,Y_q)（q ≥ 1）について χ′(X)[ρ(ω′(Y₁),…,ω′(Y_q))]、型付き定数規則 X → c について χ′(X)[c]。このとき K* は B^{≤r}_{f,h} と B_{f,h} の characteristic sample である。

**確認した点**
- **(R1) [X] は1つの類.** L_X のタプルは型 𝐭 を持ち、型付き導出文脈を共有します。arity fan(A) ≤ f の代入可能性から、1つの ≡_{L,h} 類に入ります。
- **(R2) 所属.**
  - A の導出文脈は L_A(G) ⊇ L_X のすべてを受理するので、[X] 全体も受理します。この文脈は G が good なので 𝓔_{fan(A)} に属します（v79 の補題「Induced child context」を経路に沿って反復）。
  - start-link の X では、□₁ が L_X ⊆ L を受理するので [X] 全体も受理します。
  - 規則語：ω′(Y_j) ≡_{L,h} u_j ∈ L_{Y_j} なので、v79 の補題「Composition preserves equivalence」から ρ(ω′(Y₁),…) ≡_{L,h} ρ(u₁,…) ∈ L_X。後者は χ′(X) に受理されます。
  - 定数規則は L_X の元を生成します。
- **(R3) Link 規則.** ω′(X) と z_R = ρ(ω′(Y₁),…) はどちらも型 𝐭（子の型の out_ρ）を持ち、観測文脈 χ′(X) を共有します。よって Rule (Link) [ω′(X)] → [z_R] が生成されます。
- **(R4) 合成証人.** χ′(X) ∈ 𝓔_d、子成分は非空です。good 性（非置換・非併合）により、同じ子の連続成分は終端記号・非空の兄弟成分・χ′(X) の内部区切りのいずれかで隔てられます。よって各 ω′(Y_j) は観測されたタプル出現で、その分割は rank q ≤ r の合成証人です。
- **(R5) start・rank 0・ε・生産性.** start-link 記号は S̃ → [ω′(X)]（ω′(X) ∈ K*）を使います。rank 0 は第3の語族で扱います。ε は good 言語の外で、再構成器が別に扱います。G̃₀ は刈り込み済みなので全記号が生産的かつ到達可能です。重複語は集合なので無害です。
- **(R6) v79 rule-only 証人との相互作用.** v79 正本の命題「Rule-only characteristic witnesses」は最小重み導出に対する恒等式 ω(X) = ρ_X(ω(Y₁),…) を使います。この恒等式は緩和代表元では**偽**です。したがって非終端記号用の語 χ′(X)[ω′(X)] は残す必要があり、補題Rの個数上界は |V||M|^f + |P||M|^{fr}（|𝓡| ではない）です。**二つの最適化を併用してはいけません。**

**判定：成立.** v79 の完全性の証明は ι(X) := [ω′(X)] としてそのまま使え、健全性に必要なのは K* ⊆ L だけです。

---

## 4. 定理D（アーベル型フィルタ）の敵対的査読

**監査した主張.** L = h⁻¹(Acc) ∩ φ⁻¹(γ + 𝓗)（𝔸 は任意のアーベル群、φ は準同型、𝓗 は部分群）が fan-out ≤ f・rank ≤ r の reduced good 表現 G を持つなら、κ_G ≤ poly(T)（T = (r+1)t_G + ‖G‖）であり、総長 C(‖G‖max{1,θ_G})^e の characteristic sample が存在する。C, e は Σ, h, f, r のみに依存する。

**確認した点**
- **(D1) 不変性（Step 1）.** 型なしの各 A に導出文脈が1つあれば十分で、reduced 性がそれを保証します。非削除性と線形性を使います。
- **(D2) 短い欠損（Step 2–3）.** ω_A と ρ(ω_{B₁},…) はともに A の yield なので δ_R ∈ Λ、‖δ_R‖₁ ≤ T。任意の導出について、ノード全体（rank 0 を含む）にわたる分解 Ψ(u) − Ψ(ω_A) = −Σ_ν δ_{R_ν} は厳密です。
- **(D3) 整数計画（Step 4）.**
  - 未知数：ψ(h⁻¹(m) ∩ Σ⁺) の固定した半線形表現の周期係数（高々 fC_h 個）と、λ ∈ Γ_T に対する μ^±_λ（高々 2(2T+1)^{|Σ|} 個）。
  - 方程式：|Σ| 本。係数と右辺 Ψ(ω_A) − Σ_i c_i の成分は T + fC_h 以下。
  - 任意の u ∈ L_X が解なので解は存在し、小解定理から成分が n(ma)^{2m+1}（m = |Σ|）以下の解があります。これは poly(T) で、次数は O(|Σ|) です。
- **(D4) 一様性.** Γ_T は Λ に依存しますが、上界に入るのはその大きさだけで、**どの** Λ についても |Γ_T| ≤ (2T+1)^{|Σ|} です。よって定数は 𝔸・φ・𝓗・γ・Acc（特に 𝓗 の指数）に依存しません。
- **(D5) 同値性（Step 5）.** 𝔸 の可換性は φ = φ̄∘ψ を通じてのみ使います。
- **(D6) ε.** ε ∈ h⁻¹(Acc) ∩ φ⁻¹(γ+𝓗) の場合、good 表現は L∖{ε} を生成します。Step 5 は非空語 E[v] しか評価しないので影響しません。
- **(D7) 外部資料.** 小解定理は Papadimitriou, J. ACM 28 (1981) 765–768 および MIT/LCS/TM-152 (1980)。一次 PDF は本環境から取得できず、arXiv:1607.05342 の再掲で照合しました。Parikh の定理は正規集合 h⁻¹(m) に適用しており、初等的です。

**判定：成立（群・φ・𝓗・γ に一様）.** 一次資料で未確認の外部依存は小解定理だけで、これは標準的な結果です。

---

## 5. 補題P：同一語内交換の Parikh 剛性

**補題P.** E ∈ 𝓔_d、x, y ∈ (Σ⁺)^d が E[x] = E[y] を満たすなら Ψ(x) = Ψ(y)、特に ‖x‖₁ = ‖y‖₁。

*証明.* ψ(E[x]) = ψ(E) + Ψ(x)（ψ(E) は固定部分を数える）で、y についても同様。∎

**系.**
- v79 の冪移送補題（B）と局所シフト対補題（B′）が与える交換対はすべて Parikh 同値です。どの文脈にどう適用しても、語やタプルの Parikh ベクトルは変わりません。局所可動性だけでは、分布類のより短い元は決して得られません。
- 短い代表元 y ≡_{L,h} x（‖y‖₁ < ‖x‖₁）には、E[x] ≠ E[y] となる共有受理文脈 E、すなわち L の**異なる2語**が必要です。

**意味.** Ramsey 型のシフト対は**閉包**制約（言語をブロック移動で閉じさせる）を生むものであって、**短縮**を生むものではありません。これまでに証明できた短縮論法（D と F1-sl）はいずれも、閉包制約と文法を組み合わせています。文法が型なし記号の短い yield を与え、閉包制約がそれを正しい型の短い代表元に変換します。

---

## 6. 定理 F1-sl：半束分割アーベル和集合（新規）

### 6.1 設定

空でないマーカー文字集合 Σ_c ⊆ Σ を固定します。
- 語 w について c(w) = 1（w がマーカーを含む）、0（含まない）。タプルでは c(u) = max_i c(u_i)、文脈 E では固定部分がマーカーを含むとき c(E) = 1。
- 型付け h_U: Σ* → ({0,1}, max), w ↦ c(w) は2元半束型付けで、**LG に属しません**。

**定義（半束分割アーベル和集合）.** アーベル群 𝔸、準同型 φ: Σ* → 𝔸、𝓗 ≤ 𝔸、γ₀, γ₁ ∈ 𝔸 に対して

$$L=\{w\in\Sigma^+ : \varphi(w)\in\gamma_{c(w)}+\mathcal H\}.$$

g := γ₁ − γ₀、φ = φ̄∘ψ、Λ := {v ∈ ℤ^Σ : φ̄(v) ∈ 𝓗} と置きます。

- g ∈ 𝓗 なら L = Σ⁺ ∩ φ⁻¹(γ₀+𝓗) は単一のアーベルフィルタで、定理Dが適用できます。
- g ∉ 𝓗 なら、L は一般に h⁻¹(Acc) ∩ φ′⁻¹(γ+𝓗′) の形ではありません。例：Σ = {a,c}、Σ_c = {c}、φ(w) = |w|_a ∈ ℤ/Nℤ、γ₀ = 0、γ₁ = 1。この場合、オフセットはモノイド写像 {0,1} → ℤ/Nℤ（1 ↦ 1）でなければなりませんが、1+1 ≠ 1 なので不可能です。

### 6.2 所属

**補題（所属）.** h を h_U ⪯ h を満たす有限型付け、f ≥ 1 とする。半束分割アーベル和集合は (f,h)-tuple-substitutable である。したがって f-MCFL であれば C^mcf_{f,h} に属する。

*証明.*
- x, y が同じ h 型を持ち、受理文脈 E₀ を共有するとします。h 型が等しいので成分ごとの h_U 型も等しく、どの文脈 E についても c(E[x]) = c(E[y]) です。
- E₀ から φ(x) − φ(y) ∈ 𝓗（両方の充填が同じ分岐 γ_β + 𝓗 に入る）。
- 任意の E について、二つの充填は同じ分岐に入り、φ 値の差は 𝓗 の元なので、同時に受理されます。∎

以下 g ∉ 𝓗 とし、G を L の fan-out ≤ f・rank ≤ r の reduced good 表現とします。

**用語.**
- 記号 A の**導出文脈**：成功導出から A の部分木を1つ取り除いて得られる文脈。L_A := L_A(G) のすべてのタプルを受理します。
- A が**二型**：L_A が c(u) = 0 のタプルと c(u) = 1 のタプルの両方を含む。
- A が**マーカー専用**：L_A 上で c ≡ 1。**マーカーなし**：L_A 上で c ≡ 0。
- A が**開いている**：c(E) = 0 の導出文脈 E を持つ。

### 6.3 オフセット補題

**補題（オフセット）.** E を A の導出文脈、u, u′ ∈ L_A とする。
- (a) c(E) = 1 なら φ(u) − φ(u′) ∈ 𝓗。
- (b) c(E) = 0 なら φ(u) − φ(u′) ∈ (c(u) − c(u′))g + 𝓗。
- (c) 開いた二型記号は、c(E) = 1 の導出文脈を持たない。
- (d) A が「二型かつ開いている」でなければ、すべての u, u′ ∈ L_A について Ψ(u) − Ψ(u′) ∈ Λ。二型かつ開いているなら、c(u) = c(u′) のときに限ってこれが成り立つ。

*証明.*
- E[u] ∈ L は分岐 c(E) ∨ c(u) に入るので、φ(E) + φ(u) ∈ γ_{c(E)∨c(u)} + 𝓗。u′ についての同じ関係を引けば (a)(b)。
- (c)：c = 0, 1 の u₀, u₁ を取ると、(a)(b) から φ(u₁) − φ(u₀) ∈ 𝓗 ∩ (g + 𝓗) となり g ∈ 𝓗、矛盾。
- (d)：reduced 性からどの A も導出文脈を持ちます。
  - A が二型でなければ c は L_A 上で一定で、(a) か (b) から主張が出ます。
  - A が二型で開いていなければ、導出文脈はすべて c(E) = 1 なので (a) を使います。
  - A が二型で開いているなら、c(u) = c(u′) のとき (b) を使います。∎

V₁ を「二型かつ開いた」記号の集合とします。

### 6.4 オフセット剛性（核心）

**補題（オフセット剛性）.** A ∈ V₁ とし、規則 R: A → ρ(B₁,…,B_q) のテンプレートがマーカーを書かず、どの子もマーカー専用でないとする。このとき二型の B_k は高々1つであり、二型の B_k は V₁ に属する。

*証明.*
- E_A を A の開いた導出文脈とし、B_{k₁}, B_{k₂}（k₁ ≠ k₂）がともに二型だと仮定します。
- c 値が 0, 1 の x₀, x₁ ∈ L_{B_{k₁}} と y₀, y₁ ∈ L_{B_{k₂}} を選びます。他の各 k については c = 0 のタプルを選びます（B_k はマーカー専用でないので存在する）。
- これらの選択に ρ を適用し、x_a, y_b を入れた A の yield を z_{ab} とします。ρ はマーカーを書かないので c(z_{ab}) = a ∨ b。
- E_A に補題（オフセット）(b) を適用すると

$$\varphi(x_1)-\varphi(x_0)=\varphi(z_{10})-\varphi(z_{00})\in g+\mathcal H,\qquad \varphi(x_1)-\varphi(x_0)=\varphi(z_{11})-\varphi(z_{01})\in\mathcal H,$$

  よって g ∈ 𝓗 となり矛盾。∨ の冪等性（1∨1 = 1）が効いています。
- 後半：二型の B_k の兄弟を E_A と ρ の中でマーカーなしのタプルで埋めると、マーカーを含まない B_k の導出文脈が得られます（成功導出から来る）。good 性により 𝓔_{fan(B_k)} に属します。よって B_k は開いています。∎

### 6.5 短い正準 yield

**補題（短い正準 yield）.** T₀ := |V|(‖G‖ + r·t_G) と置く。どの A ∈ V も ‖ω_A‖₁ ≤ t_G の yield ω_A を持つ。どの A ∈ V₁ も、c(ω^b_A) = b かつ ‖ω^b_A‖₁ ≤ T₀ を満たす yield ω⁰_A, ω¹_A を持つ。

*証明.* 前半は t_G の定義です。b ∈ {0,1}、A ∈ V₁ について、λ_b(A) を c(u) = b となる u ∈ L_A の ‖u‖₁ の最小値とし、それを実現し（yield 長, ノード数）で辞書式最小の導出を選びます。根の規則を R: A → ρ(B₁,…,B_q) とします。最適部分構造により、根の c 値を変えずに c 値を変えられる子の部分導出は、その子の最短 yield になっています。

- **b = 0.** テンプレートはマーカーを書かず、子の yield はすべて c = 0 なので、マーカー専用の子はありません。補題（オフセット）とオフセット剛性により二型の子は高々1つで、それは V₁ に属します。他の子はマーカーなしで、部分 yield は最短（≤ t_G）。二型の子 B の部分 yield は λ₀(B) を実現します。よって λ₀(A) ≤ ‖G‖ + (r−1)t_G + λ₀(B)、二型の子がなければ ≤ ‖G‖ + r·t_G。
- **b = 1.**
  - テンプレートがマーカーを書くか、マーカー専用の子があるなら、子の部分 yield をすべて最短 yield に替えてもマーカーは失われないので、λ₁(A) ≤ ‖G‖ + r·t_G。
  - そうでなければオフセット剛性が使えます。二型の子は高々1つで、他の子はマーカーなしです。したがってマーカーは唯一の二型の子 B ∈ V₁ から来て、その部分 yield は λ₁(B) を実現します。λ₁(A) ≤ ‖G‖ + (r−1)t_G + λ₁(B)。
- **連鎖の停止.** どちらの場合も A ↦ B の移行で、選んだ最小導出の（長さ, ノード数）が辞書式に真に減少します。よって連鎖は各記号を高々1回しか通らず、λ_b(A) ≤ |V|(‖G‖ + r·t_G)。∎

**帰結.** 倍化 A_i → A_{i−1}A_{i−1} は、開いた二型記号の下のマーカーなし経路上に現れ得ません。これが、小さい通常厚さのままマーカーなしの指数的に希少な語を作れない理由です。

A ∈ V と b ∈ {0,1} について、A ∈ V₁ なら ω^{(b)}_A := ω^b_A、そうでなければ ω^{(b)}_A := ω_A と置きます。

### 6.6 短い Λ 欠損

**補題（短い Λ 欠損）.** T₁ := (r+1)T₀ + ‖G‖、Γ := {λ ∈ Λ : ‖λ‖₁ ≤ T₁}、Λ₁ を Γ が生成する部分群とする。すべての A ∈ V と u ∈ L_A について

$$\Psi(u)-\Psi\bigl(\omega^{(c(u))}_A\bigr)\in\Lambda_1.$$

*証明.*
- 規則 R: A → ρ(B₁,…,B_q) と、各 b_k が L_{B_k} で実現される b ∈ {0,1}^q について、z := ρ(ω^{(b₁)}_{B₁},…,ω^{(b_q)}_{B_q}) ∈ L_A と置きます。c(u_k) = b_k の子に R を適用して得られる A の任意の yield を u′ とします。
- **主張：A ∈ V₁ なら c(z) = c(u′).**
  - ρ がマーカーを書くか、マーカー専用の子があれば、どちらも 1。
  - そうでなければ、オフセット剛性によって二型の子はすべて V₁ に属します。したがってどの子についても c(ω^{(b_k)}_{B_k}) = b_k です（V₁ 外の子はこのときマーカーなしで b_k = 0）。どちらの値も max_k b_k に等しくなります。
- β := c(u′)、δ_{R,b} := Ψ(ω^{(β)}_A) − Ψ(z) と置きます。
  - A ∈ V₁ なら、主張により ω^{(β)}_A と z は同じ c 値を持つ A の yield です。
  - A ∉ V₁ なら補題（オフセット）(d) の前半が使えます。
  - どちらの場合も δ_{R,b} ∈ Λ で、‖δ_{R,b}‖₁ ≤ T₀ + ‖G‖ + r·T₀ = T₁。
- u ∈ L_A の導出（根の規則 R、子の yield u_k）について帰納法を使います。b_k = c(u_k) と置けば u′ = u、β = c(u) で、

$$\Psi(u)-\Psi\bigl(\omega^{(c(u))}_A\bigr)=\sum_k\Bigl(\Psi(u_k)-\Psi\bigl(\omega^{(b_k)}_{B_k}\bigr)\Bigr)-\delta_{R,b}\in\Lambda_1 .$$

  子については帰納法の仮定を使います（rank 0 の規則が基底で、和は空）。∎

### 6.7 主定理

**定理 F1-sl.** Σ、Σ_c、h_U ⪯ h を満たす有限型付け h: Σ* → M、f ≥ 1、r ≥ 1 を固定する。(Σ, h, f, r) のみに依存する C, e があって、任意の半束分割アーベル和集合 L（𝔸, φ, 𝓗, γ₀, γ₁ は任意）と、その fan-out ≤ f・rank ≤ r の任意の reduced good 表現 G について

$$\kappa_G\le C\bigl(\|G\|\max\{1,\theta_G\}\bigr)^e .$$

さらに B^{≤r}_{f,h} は、|K*| ≤ |V||M|^f + |P||M|^{fr}、‖K*‖₊ ≤ C′(‖G‖max{1,θ_G})^{e′} を満たす characteristic sample K* ⊆ L を持つ。特に、すべての m ∈ h(L) について μ_m(L) は多項式で抑えられる。

*証明.*
1. g ∈ 𝓗 なら定理Dを使います。以下 g ∉ 𝓗。
2. X = A_𝐭 を arity d の開始記号でない型付き記号とし、u ∈ L_X を固定し、β := c(u) と置きます。h_U ⪯ h なので β は 𝐭 で決まります。
3. m ∈ M について ψ(h⁻¹(m) ∩ Σ⁺) の半線形表現を固定します（線形集合は高々 C_h 個、周期と定数のノルムは C_h 以下）。
4. 「h(v_i) = t_i かつ Ψ(v) − Ψ(ω^{(β)}_A) ∈ Λ₁」を求める整数計画を、選んだ線形集合の周期係数と係数 μ^±_λ（λ ∈ Γ）で書きます。方程式 |Σ| 本、未知数 ≤ fC_h + 2(2T₁+1)^{|Σ|}、係数 ≤ T₁ + fC_h。補題（短い Λ 欠損）により解を持ち（証人 u）、したがって成分 poly(T₁) の解を持ちます。これから h^{(d)}(v) = 𝐭、‖v‖₁ ≤ poly(T₁) の v が得られます。
5. **v ≡_{L,h} u.** どちらも型 𝐭 なので、任意の文脈 E で二つの充填は同じ分岐 c(E) ∨ β に入ります。また Ψ(v) − Ψ(u) ∈ Λ₁ ⊆ Λ なので、φ 値の差は 𝓗 の元です。**ここで両分岐に共通の部分群 𝓗 を使います。**
6. よって κ_G(X) ≤ poly(T₁)。t_G ≤ θ_G より T₁ ≤ (r+1)|V|(‖G‖ + r·θ_G) + ‖G‖。
7. 標本の上界は補題Rとその系から、μ_m の上界は v79 研究草稿の型削除命題から従います。∎

### 6.8 新規性と範囲

- (i) h_U ∉ LG なので v79 の局所群定理は使えません。g ∉ 𝓗 なら標的はアーベルフィルタでないので、定理Dも直接は使えません。
- (ii) 証明は L の代入可能性を補題（所属）以上には使いません。決定的な入力は**オフセット剛性**で、これは L の**すべての**表現が持つ性質です。
- (iii) 倍化文法 A_i → A_{i−1}A_{i−1} は、開いた二型記号の下のマーカーなし経路上には現れ得ません。
- (iv) 定理は両分岐で一つの部分群 𝓗 を使う形で述べています。有限走査（第7節）では、h_U 上の非自明な所属言語 1,364 個すべてが、各分岐で実現可能な値に制限すると共通部分群の和集合になりました。ただしこれは k ≤ 6 を超えては何も証明しません。

---

## 7. 有限走査による証拠（定理ではない）

### 7.1 h_U 上の2分岐和集合（`v80_branch_union_scan.py`）
- 設定：Σ = {a, c}、マーカー c、h = h_U、φ: Σ* → ℤ/k（k ≤ 6）、分岐値集合 S₁, S₂ のすべての組。
- 判定：モノイドが可換なので、タプルと文脈は和に帰着し、(2,h_U) 代入可能性を厳密に判定できます。
- 結果：単一フィルタでない所属言語 1,364 個（重複除去後）が**すべて**、共通部分群 𝓗 と γ₀, γ₁ によって F1-sl 型に正規化できました。

### 7.2 2マーカー内容型付けのブール結合（`v80_content_union_scan.py`）
- 設定：Σ = {a, c, d}、内容型付け h(w) ⊆ {c, d}（半束で、LG の外）、φ: Σ* → ℤ/k（k ≤ 3）、**任意の関係** R ⊆ P({c,d}) × ℤ/k、L = {w ∈ Σ⁺ : (h(w), φ(w)) ∈ R}。
- 結果：81,456 関係のうち 6,958 が C(2,h) に所属。
  - 6,894：捻り共通部分群フィルタ（ある 𝓗 とオフセット g_S について R_S = (g_S + 𝓗) ∩ W_S）
  - 64：分岐別の部分群 𝓗_S を持つ分岐別フィルタ
  - それ以外の形は出現しませんでした。

**予想 F1-gen（形）.** h が内容型付けで φ がアーベル群への写像のとき、L = {w ∈ Σ⁺ : (h(w), φ(w)) ∈ R} が C^mcf_{2,h} に属するなら、実現される各内容 S について分岐 R_S は部分群 𝓗_S の剰余類（実現値に制限）であり、𝓗_S と 𝓗_{S′} は、S と S′ の両方に到達できる型パターンのタプルの差の上で一致する。

**予想 F1-tw（データ）.** (Σ, h, f, r) を固定し h を内容型付けとすると、予想 F1-gen の形の標的で reduced good 表現 G を持つものはすべて κ_G ≤ poly(‖G‖max{1,θ_G}) を満たす。

**根拠（証明ではない）.**
- 定理 F1-sl はマーカー1つ・共通部分群の場合です。
- 証明の着想は次のように拡張できる見込みです。オフセットは内容 S_E の文脈に対して o(T) = g_{S_E ∪ T} になります。オフセット剛性の長方形恒等式は、∪ の冪等性により、非零のオフセット増分をもつマーカーで変動が重なる二つの子を禁止します。変動が互いに素な子は許されます（相異なるマーカー間でオフセットは加法的）。したがって最小導出の「変動木」の葉は高々 |Σ_c| 個になり、正準 yield は |Σ_c|·|V|(‖G‖ + r·t_G) で抑えられるはずです。
- 欠けているのは「変動」の厳密化と、分岐別部分群の扱いです。

---

## 8. 失敗した原理（区分B）

- **(F1)「局所可動性 ⇒ 短縮」.** 方法として不成立です。補題Pにより、1語の内部で証拠づけられる交換はすべて Parikh 同値です。
- **(F2)「分岐が整合する和集合は単一フィルタに帰着する」.** 偽です。g ∉ 𝓗 の半束分割和集合はアーベルフィルタではありません（6.1 の例：Σ = {a,c}、φ = #a mod N、γ₀ = 0、γ₁ = 1）。それでもデータ上界は別の理由（オフセット剛性）で成り立ちます。
- **(F3)「分岐ごとに部分群が違っても同じ証明が通る」.** 定理 F1-sl の証明は手順5で共通部分群を使います。走査では h_U 上の2分岐和集合はすべて共通部分群に正規化できましたが、2マーカー内容型付けでは 64 個の所属言語が分岐別部分群を本当に必要とし、**未カバー**です。

---

## 9. 予想Eの到達度（区分D）

- **証明済み：**
  - h(Σ⁺) ∈ LG（v79 局所群定理。L_X ⊆ [X] なので）
  - すべての h に対するアーベルフィルタ（定理D）
  - h ⪰ h_U に対する半束分割共通部分群和集合（定理 F1-sl）
- **反証：** fan-out 1 のみ（TCS #1）。
- **反例候補：** 生き残ったものはありません。反例設計はどれも、剛体的な語（冪移送とシフト対の補題で壊れる）か、型可換な標的（アーベル・分割の場合と予想 F1-tw）に帰着しました。
- **総合：未解決。**

---

## 10. 次に必要な補題（区分F、量化つき）

- **N1（分岐別部分群）.** 任意の Σ, Σ_c, h ⪰ h_U, f, r について、ある C, e が存在し、次が成り立つ：任意の 𝔸, φ, 𝓗₀, 𝓗₁, γ₀, γ₁ で、Λ₀ ∩ ℤ^{Σ∖Σ_c} = Λ₁ ∩ ℤ^{Σ∖Σ_c} を満たし、L = {w : φ(w) ∈ γ_{c(w)} + 𝓗_{c(w)}} ∈ C(f,h) が good 表現 G を持つなら、κ_G ≤ C(‖G‖θ_G)^e。
- **N2（変動木）.** 内容型付けで、文脈内容 S_E をもつ導出文脈を持つ記号 A について、Var(A) ⊆ Σ_c を「ある実現可能な内容差について g_{S∪{c}} ≠ g_S となるマーカー c の集合」と定義する。各規則で Var ≠ ∅ の子どうしの Var が互いに素であることを示す。これで予想 F1-tw が従う見込みです。
- **N3（型可換正規形）.** L ∈ C(2,h) で、マーカー部分が豊かなアーベルフィルタ（すべての剰余類がマーカー文脈で実現される）なら、マーカーなし部分は (h(w), φ(w) + 𝓗) で決まることを示し、N1・N2 に帰着させる。
- **N4（非可換の壁）.** 大域的に「型＋アーベル不変量」で類が決まらない C(2,h) の元を構成する、または存在しないことを示す。後者と N1・N2 を合わせると予想Eが従います。

---

## 11. GitHub 成果物（区分E）

- ブランチ：`mcfg2-v80-short-distribution-representatives`
- コミット：`5a85109`（この統合文書の追加は後続コミット）
- Draft PR #49：https://github.com/growupkuriyama-hub/Papers/pull/49
- ファイル（すべて `02_fixed-h-mcfg/revision/`）：
  - `v80_short_distribution_representatives.md`（研究メモ）
  - `v80_short_representatives.tex` / `.pdf`（証明草稿、7頁）
  - `v80_branch_union_scan.py`、`v80_content_union_scan.py` と出力 `*_output.txt`
  - `v80_complete.md`（本文書）
  - PR #46 の研究ファイル（`v79_fanout2_*`, `v79_lib.py` など）の同一コピー（参照用）

---

## 12. 再現方法

```
python3 revision/v80_branch_union_scan.py 6      # h_U、k<=6（約1時間）
python3 revision/v80_content_union_scan.py 3     # 内容型付け、k<=3
pdflatex revision/v80_short_representatives.tex  # 監査・補題P・定理F1-sl・予想
```

参考：
- Papadimitriou, *On the Complexity of Integer Programming*, MIT/LCS/TM-152 (1980)：https://dspace.mit.edu/handle/1721.1/148979
- Fomin et al., arXiv:1607.05342（小解定理の再掲の確認に使用）

---

## 付録 A：走査出力

### `v80_branch_union_scan_output.txt`（k ≤ 6）

```
{'tested': 177792, 'in_class': 38506, 'nontrivial': 10572}
nontrivial members covered by F1-sl (common H, branch may be empty): 1364 ; not covered: 0
```

### `v80_content_union_scan_output.txt`（k ≤ 3）

```
k=2: {'tested': 1296, 'in_class': 572, 'twisted': 564, 'other': 8, 'other_branchwise': 8}
k=3: {'tested': 80160, 'in_class': 6386, 'twisted': 6330, 'other': 56, 'other_branchwise': 56}
  NOT TWISTED-COMMON-H: (2, (0, 1, 1), [(['c'], 0), (['c'], 1), (['d'], 0)])
  NOT TWISTED-COMMON-H: (2, (0, 1, 1), [([], 0), (['c'], 0), (['c'], 1), (['d'], 0)])
  NOT TWISTED-COMMON-H: (2, (0, 1, 1), [(['c'], 0), (['c'], 1), (['d'], 1)])
  NOT TWISTED-COMMON-H: (2, (0, 1, 1), [([], 0), (['c'], 0), (['c'], 1), (['d'], 1)])
  NOT TWISTED-COMMON-H: (2, (0, 1, 1), [(['c'], 0), (['d'], 0), (['d'], 1)])
  NOT TWISTED-COMMON-H: (2, (0, 1, 1), [([], 0), (['c'], 0), (['d'], 0), (['d'], 1)])
  NOT TWISTED-COMMON-H: (2, (0, 1, 1), [(['c'], 1), (['d'], 0), (['d'], 1)])
  NOT TWISTED-COMMON-H: (2, (0, 1, 1), [([], 0), (['c'], 1), (['d'], 0), (['d'], 1)])
  NOT TWISTED-COMMON-H: (3, (0, 1, 1), [(['c'], 0), (['c'], 1), (['c'], 2), (['d'], 0)])
  NOT TWISTED-COMMON-H: (3, (0, 1, 1), [([], 0), (['c'], 0), (['c'], 1), (['c'], 2), (['d'], 0)])
  NOT TWISTED-COMMON-H: (3, (0, 1, 1), [(['c'], 0), (['c'], 1), (['c'], 2), (['d'], 1)])
  NOT TWISTED-COMMON-H: (3, (0, 1, 1), [([], 0), (['c'], 0), (['c'], 1), (['c'], 2), (['d'], 1)])
  NOT TWISTED-COMMON-H: (3, (0, 1, 1), [(['c'], 0), (['c'], 1), (['c'], 2), (['d'], 2)])
  NOT TWISTED-COMMON-H: (3, (0, 1, 1), [([], 0), (['c'], 0), (['c'], 1), (['c'], 2), (['d'], 2)])
  NOT TWISTED-COMMON-H: (3, (0, 1, 1), [(['c'], 0), (['d'], 0), (['d'], 1), (['d'], 2)])
  NOT TWISTED-COMMON-H: (3, (0, 1, 1), [([], 0), (['c'], 0), (['d'], 0), (['d'], 1), (['d'], 2)])
  NOT TWISTED-COMMON-H: (3, (0, 1, 1), [(['c'], 1), (['d'], 0), (['d'], 1), (['d'], 2)])
  NOT TWISTED-COMMON-H: (3, (0, 1, 1), [([], 0), (['c'], 1), (['d'], 0), (['d'], 1), (['d'], 2)])
  NOT TWISTED-COMMON-H: (3, (0, 1, 1), [(['c'], 2), (['d'], 0), (['d'], 1), (['d'], 2)])
  NOT TWISTED-COMMON-H: (3, (0, 1, 1), [([], 0), (['c'], 2), (['d'], 0), (['d'], 1), (['d'], 2)])
  NOT TWISTED-COMMON-H: (3, (0, 1, 2), [(['c'], 0), (['c'], 1), (['c'], 2), (['d'], 0)])
  NOT TWISTED-COMMON-H: (3, (0, 1, 2), [([], 0), (['c'], 0), (['c'], 1), (['c'], 2), (['d'], 0)])
  NOT TWISTED-COMMON-H: (3, (0, 1, 2), [(['c'], 0), (['c'], 1), (['c'], 2), (['d'], 1)])
  NOT TWISTED-COMMON-H: (3, (0, 1, 2), [([], 0), (['c'], 0), (['c'], 1), (['c'], 2), (['d'], 1)])
  NOT TWISTED-COMMON-H: (3, (0, 1, 2), [(['c'], 0), (['c'], 1), (['c'], 2), (['d'], 2)])
  NOT TWISTED-COMMON-H: (3, (0, 1, 2), [([], 0), (['c'], 0), (['c'], 1), (['c'], 2), (['d'], 2)])
  NOT TWISTED-COMMON-H: (3, (0, 1, 2), [(['c'], 0), (['d'], 0), (['d'], 1), (['d'], 2)])
  NOT TWISTED-COMMON-H: (3, (0, 1, 2), [([], 0), (['c'], 0), (['d'], 0), (['d'], 1), (['d'], 2)])
  NOT TWISTED-COMMON-H: (3, (0, 1, 2), [(['c'], 1), (['d'], 0), (['d'], 1), (['d'], 2)])
  NOT TWISTED-COMMON-H: (3, (0, 1, 2), [([], 0), (['c'], 1), (['d'], 0), (['d'], 1), (['d'], 2)])
```

## 付録 B：ソースコード全文

### `revision/v80_branch_union_scan.py`

```python
#!/usr/bin/env python3
"""v80: which type-disjoint unions of cyclic-group filters are in C(2,h_U)?

Setting (exact, finite algebra; no string enumeration needed).
  Sigma = {a, c},  h = h_U (c |-> zeta, a |-> 1),
  phi : Sigma* -> Z_k,  phi(a) = alpha, phi(c) = beta,
  L = { w in Sigma^+ : h(w) = 1 and phi(w) in S1 }
    U { w in Sigma^+ : h(w) = zeta and phi(w) in S2 },   S1, S2 subsets of Z_k.

Membership of E[x] depends only on (OR of types, sum of values), because
the monoid {1,zeta} x Z_k is commutative.  A 2-tuple x is described by
(t1,v1),(t2,v2) realisable by NONEMPTY words; a 2-hole context by
(type, value) realisable by u0 u1 u2 with u1 nonempty.  We test exact
(2,h_U)- and (1,h_U)-tuple substitutability and classify each L as
  * EMPTY-branch / SINGLE filter (S1 = S2 coset of the same subgroup, or one
    branch empty and the other a coset), or
  * NONTRIVIAL union in the class.
Nontrivial members are printed: they are the test cases for Lemma F1.
"""
from __future__ import annotations

import itertools
import sys


def realisable(k, alpha, beta, nonempty=True, maxlen=None):
    """(type, value) pairs of words over {a,c}; type 0 = c-free."""
    maxlen = maxlen or 3 * k + 2
    out = set()
    for i in range(0, maxlen + 1):
        for j in range(0, maxlen + 1):
            if nonempty and i + j == 0:
                continue
            out.add((1 if j else 0, (i * alpha + j * beta) % k))
    return out


def in_L(t, v, S1, S2):
    return v in (S2 if t else S1)


def check(k, alpha, beta, S1, S2):
    W = realisable(k, alpha, beta)              # nonempty words
    C = W                                        # contexts: middle part nonempty
    # (prefix/suffix may be empty; they can only add elements of W or nothing,
    #  and W is closed under addition, so contexts = W)
    for d in (1, 2):
        tuples = list(itertools.product(W, repeat=d))
        sig = {}
        for x in tuples:
            tx = tuple(t for t, _ in x)
            vt = 1 if any(tx) else 0
            vs = sum(v for _, v in x) % k
            acc = frozenset(c for c in C if in_L(c[0] | vt, (c[1] + vs) % k, S1, S2))
            sig[x] = (tx, acc)
        by_type = {}
        for x, (tx, acc) in sig.items():
            by_type.setdefault(tx, []).append(acc)
        for tx, accs in by_type.items():
            for A, B in itertools.combinations(set(accs), 2):
                if A & B and A != B:
                    return False, d
    return True, None


def is_coset(S, k):
    if not S:
        return True
    s0 = next(iter(S))
    H = {(s - s0) % k for s in S}
    return all((x + y) % k in H for x in H for y in H) and \
        all({(s + h) % k for h in H} <= S for s in S)


def main(kmax=6):
    found = []
    stats = {"tested": 0, "in_class": 0, "nontrivial": 0}
    for k in range(2, kmax + 1):
        subsets = [frozenset(s) for r in range(0, k + 1)
                   for s in itertools.combinations(range(k), r)]
        for alpha in range(k):
            for beta in range(k):
                for S1 in subsets:
                    for S2 in subsets:
                        stats["tested"] += 1
                        ok, _ = check(k, alpha, beta, S1, S2)
                        if not ok:
                            continue
                        stats["in_class"] += 1
                        # reduce to what is actually realisable
                        W = realisable(k, alpha, beta)
                        R1 = frozenset(v for (t, v) in W if t == 0 and v in S1)
                        R2 = frozenset(v for (t, v) in W if t == 1 and v in S2)
                        single = (not R1 or not R2) or (R1 == R2)
                        if single and is_coset(R1, k) and is_coset(R2, k):
                            continue
                        stats["nontrivial"] += 1
                        found.append((k, alpha, beta, tuple(sorted(R1)), tuple(sorted(R2))))
    print(stats)
    # classify nontrivial members: is L a semilattice-split union with a
    # COMMON subgroup H (Theorem F1-sl), i.e. are there H <= Z_k and g0,g1
    # with R_b = (g_b + H) intersected with the values realisable in branch b?
    covered = 0
    uncovered = []
    for (k, al, be, R1, R2) in sorted(set(found)):
        W = realisable(k, al, be)
        W0 = {v for (t, v) in W if t == 0}
        W1 = {v for (t, v) in W if t == 1}
        subgroups = {frozenset((d * i) % k for i in range(k)) for d in range(k)}
        ok = False
        for H in subgroups:
            o0 = [g for g in range(k) if {(g + x) % k for x in H} & W0 == set(R1)] \
                if R1 else [None]
            o1 = [g for g in range(k) if {(g + x) % k for x in H} & W1 == set(R2)] \
                if R2 else [None]
            if o0 and o1:
                ok = True
                break
        if ok:
            covered += 1
        else:
            uncovered.append((k, al, be, R1, R2))
    print("nontrivial members covered by F1-sl (common H, branch may be empty):",
          covered, "; not covered:", len(uncovered))
    for e in uncovered[:20]:
        print("  NOT COVERED:", e)


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 6)
```

### `revision/v80_content_union_scan.py`

```python
#!/usr/bin/env python3
"""v80: Boolean combinations of a cyclic filter under a CONTENT typing.

Setting (exact; commutative, so 2-tuples reduce to sums).
  Sigma = {a, c, d};  markers c, d;  h = content typing
      h(w) = set of markers occurring in w  (a semilattice, not in LG);
  phi: Sigma* -> Z_k, letter values (va, vc, vd);
  L = { w in Sigma^+ : (h(w), phi(w)) in R }   for an arbitrary relation
      R subset of P({c,d}) x Z_k.
A tuple of arity d<=2 is described by its componentwise (content, value);
a context by (content, value) of its fixed material (middle part nonempty).

For every R we decide exactly whether L is (2,h)-tuple-substitutable, and
if so whether L is a TWISTED COMMON-SUBGROUP FILTER:
    there are H <= Z_k and offsets g_S (S a realisable content) such that
    for every realisable content S, R_S (restricted to realisable values)
    is either empty or equal to (g_S + H) restricted to realisable values.
This is the shape of Conjecture F1-tw.  Members of the class that are NOT
of this shape would be candidates for new phenomena; the script prints them.
A finite scan proves nothing in general.

Run:  python3 revision/v80_content_union_scan.py [kmax]
"""
from __future__ import annotations

import itertools
import sys

CONTENTS = [frozenset(), frozenset("c"), frozenset("d"), frozenset("cd")]


def realisable(k, va, vc, vd, maxrep=None):
    maxrep = maxrep or k + 1
    out = set()
    for i in range(maxrep + 1):
        for j in range(maxrep + 1):
            for l in range(maxrep + 1):
                if i + j + l == 0:
                    continue
                S = frozenset(("c" if j else "") + ("d" if l else ""))
                out.add((S, (i * va + j * vc + l * vd) % k))
    return out


def check(k, W, R):
    """exact (2,h)-substitutability; W = realisable (content,value) of
    nonempty words (also = realisable contexts, closed under +)."""
    def acc(S, v):
        return (S, v) in R
    for d in (1, 2):
        sig = {}
        for x in itertools.product(W, repeat=d):
            types = tuple(S for S, _ in x)
            Sx = frozenset().union(*types)
            vx = sum(v for _, v in x) % k
            A = frozenset(c for c in W if acc(c[0] | Sx, (c[1] + vx) % k))
            sig.setdefault(types, set()).add(A)
        for accs in sig.values():
            for A, B in itertools.combinations(accs, 2):
                if A & B:
                    return False
    return True


def twisted_shape(k, W, R):
    by_S = {}
    for S, v in W:
        by_S.setdefault(S, set()).add(v)
    subgroups = {frozenset((dd * i) % k for i in range(k)) for dd in range(k)}
    for H in subgroups:
        ok = True
        for S, vals in by_S.items():
            RS = {v for v in vals if (S, v) in R}
            if not RS:
                continue
            if not any({(g + x) % k for x in H} & vals == RS for g in range(k)):
                ok = False
                break
        if ok:
            return True
    return False


def branchwise_shape(k, W, R):
    """each branch R_S is (g_S + H_S) restricted to realisable values,
    with its OWN subgroup H_S (the shape of Conjecture F1-gen)."""
    by_S = {}
    for S, v in W:
        by_S.setdefault(S, set()).add(v)
    subgroups = {frozenset((dd * i) % k for i in range(k)) for dd in range(k)}
    for S, vals in by_S.items():
        RS = {v for v in vals if (S, v) in R}
        if RS and not any({(g + x) % k for x in H} & vals == RS
                          for H in subgroups for g in range(k)):
            return False
    return True


def main(kmax=3):
    stats = {"tested": 0, "in_class": 0, "twisted": 0, "other": 0,
             "other_branchwise": 0}
    others = []
    for k in range(2, kmax + 1):
        for va, vc, vd in itertools.product(range(k), repeat=3):
            W = realisable(k, va, vc, vd)
            Wl = sorted(W, key=lambda t: (sorted(t[0]), t[1]))
            n = len(Wl)
            for mask in range(1 << n):
                R = {Wl[i] for i in range(n) if mask >> i & 1}
                stats["tested"] += 1
                if not check(k, W, R):
                    continue
                stats["in_class"] += 1
                if twisted_shape(k, W, R):
                    stats["twisted"] += 1
                else:
                    stats["other"] += 1
                    if branchwise_shape(k, W, R):
                        stats["other_branchwise"] += 1
                    others.append((k, (va, vc, vd),
                                   sorted((sorted(S), v) for S, v in R)))
        print(f"k={k}: {stats}", flush=True)
    for o in others[:30]:
        print("  NOT TWISTED-COMMON-H:", o)


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 3)
```


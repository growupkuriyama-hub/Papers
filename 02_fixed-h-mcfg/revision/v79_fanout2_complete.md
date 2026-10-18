# #2 MCFG v79 完全版：fan-out 2 における超多項式特徴データ下界の探索（統合文書）

- 作成日：2026-10-18（JST）
- ブランチ：`mcfg2-v79-fanout2-lower-bound-search`／Draft PR #46（マージ不可）
- 監査した基準：Papers HEAD `2f2754deedc17e539e8ecbec9f923f40fae3fbea`（`PAPER.yaml` は内部版 **v78**）
- この文書は、v79 の研究メモ・証明草稿・候補族の実験結果・列挙探索の結果・再現用コードを**1つの Markdown にまとめたもの**です。
  - 分割版：`v79_fanout2_lower_bound_research.md`（メモ）、`v79_fanout2_results.tex/.pdf`（証明草稿）、`v79_*.py`（スクリプト）、`v79_*_output.txt`（出力）
- `main.tex` と `main_JP.tex` は**一切変更していません**。

---

## 目次

0. 結論の要約
1. Phase 1：原稿監査と問題の厳密な再定式化
2. 準備（記号と定義）
3. 定理 A：型削除と区別対（任意の f）
4. 補題 B：冪移送（fan-out 2）
5. 補題 B′：局所シフト対（Ramsey）
6. 定理 C：どの有限型付けも倍化族を救えない
7. 補題 R：緩和証人（データ長が本当に測っているもの）
8. 定理 D：アーベル型フィルタ言語は多項式データを持つ
9. 予想
10. 候補族と失敗例（Phase 2–3）
11. 文法スキーマの全列挙
12. 新しい洞察
13. 次に解くべき補題
14. 原稿への影響（未適用）
15. 再現方法
- 付録 A：候補族テストの全出力
- 付録 B：スキーマ列挙の出力
- 付録 C：ソースコード全文

---

## 0. 結論の要約

**Open Problem `op:fanout-two` は未解決です。** 超多項式の下界を与える言語族は構成できませんでした。代わりに、下界が可能な範囲を縛る結果を証明しました。証拠は全体として**否定的な方向（一般上界の可能性）**を示しています。

| 項目 | 内容 | 状態 |
|---|---|---|
| A | 1つの型を削除しても C(f,h) に残る。超多項式的に希少な型があれば下界が出る（任意の f、演算子非依存版も） | 証明済み |
| B | fan-out 2 の冪移送補題 | 証明済み |
| B′ | 長さ R_c(5) 以上のすべての語に有界な交換可能シフト対がある | 証明済み（Ramsey） |
| C | TCS #1 の括弧付き倍化族は、**すべての**有限型付け h で n ≥ 2\|M\|+3 なら C(2,h) の外 | 証明済み（v78 の命題を強化） |
| R | B^{≤r} のデータ長は poly(‖G‖, θ_G, κ_G) で抑えられる。κ_G は型付き分布類の最短元 | 証明済み |
| D | アーベル型フィルタ言語 h⁻¹(Acc)∩φ⁻¹(γ+H) は、**すべての** h, f, r で多項式データを持つ | 証明済み（Parikh＋Papadimitriou） |
| E | 予想：fan-out 2 では κ_G ≤ poly(‖G‖θ_G)。成り立てば答えは否定的 | 未解決 |
| 実験 | 手作りの6族＋列挙した 28,642 スキーマ | すべて (2,h) 代入可能性が破綻 |

証明はいずれも草稿で、**独立監査は未了**です。計算機による確認は有限範囲のみで、一般定理とはみなしていません。

---

## 1. Phase 1：原稿監査と問題の再定式化

### 1.1 実際に開いた資料

- `02_fixed-h-mcfg/PAPER.yaml`、`main.tex`
  - Preliminaries、第3–4節、比較の節、Conclusion（`op:fanout-two` と `prop:fixed-window-doubling-fanout-two` を含む）
- `appendix_local_group.tex`（定理の主張と `lem:local-group-shortest`）
- `revision/v76_stage1_lg_dichotomy.md`、`revision/v78_fanout2_window1_negative_finding.md`
- `revision/check_fixed_window_general_obstruction.py`
- `01_fixed-h-cfg/main.tex`
  - Proposition `prop:typed-thickness-gap`（(i)–(iv) の主張と証明、L_n と L_n^- の構成）
  - Corollary `cor:typed-gap-intrinsic`
- Papadimitriou (1981) の小解定理：Fomin–Panolan–Ramanujan–Saurabh, arXiv:1607.05342 の第1節にある再掲で確認しました。**J. ACM の原論文は開いていません。**

### 1.2 開いていない資料（確認済みとして扱わないこと）

- `japanese/main_JP.tex` は行単位で読み直していません（`PAPER.yaml` の sha のみ確認）。変更もしていません。
- ChatGPT 側のソース合本 第02/03/07巻は、この Claude Project にありません（Project にあるのは Core B/F/L/N の抜粋）。
- Yoshinaka (2011, 2015)、Clark–Yoshinaka、Seki et al. (1991)、Almeida et al. (2009) は、**`main.tex` に引用された主張を通じてのみ**使いました。原典は開いていません。使った事実は標準的なもの（MCFL は正規言語との共通部分で閉じる、good 形の約束）だけです。
- TCS #1 付録の括弧付き族の代入可能性の証明は再監査していません。本研究の結果はすべて arity 2 に関するもので、この証明は不要です。

### 1.3 問題の厳密な再定式化

f ≥ 2、r ≥ 2、有限型付け h: Σ* → M を固定します。次を満たす reduced good な文法 G_n（fan-out ≤ f、rank ≤ r）が欲しい：

- L(G_n) ∈ C^mcf_{f,h}
- ‖G_n‖·max{1, θ_{G_n}} = poly(n)
- B^{≤r}_{f,h} のすべての characteristic sample の総長が超多項式

本研究で導いた条件は次の3つです。

1. **十分条件**：希少な型 m_n があり、μ_{m_n}(L(G_n)) が超多項式であること（定理 A）。このとき、L と L∖h⁻¹(m) の両方に characteristic sample を持つ任意の set-driven operator にも下界が及びます。
2. **必要条件**：G_n のある型付き分布類 [X] の元がすべて超多項式的に長いこと、すなわち κ_{G_n} = n^{ω(1)}（系 R）。
3. **禁止される形**：
   - どこかの語に長い冪 u^K があると、u ブロック間の移送が強制される（補題 B）
   - R_c(5) より長いすべての語が、有界な交換可能シフト対を持つ（補題 B′）
   - アーベル型フィルタ言語は不可能（定理 D）

---

## 2. 準備（記号と定義）

定義は v78 原稿のものをそのまま使います。

- **arity d の sentence context** E = v₀□₁v₁⋯□_d v_d：内部区切り v₁, …, v_{d−1} は**空でない**。v₀, v_d は空でもよい。
- **タプル**の成分はすべて空でない。
- **分布** D_L^{(d)}(x) = {E ∈ 𝓔_d : E[x] ∈ L}。
- **(f,h)-tuple-substitutable**：d ≤ f について、成分ごとの h 型が等しく、受理文脈を1つ共有すれば、分布が等しい。
- **C^mcf_{f,h}**：(f,h)-tuple-substitutable な f-MCFL 全体。
- **再構成器**：B^{≤r}_{f,h}（capped）と B_{f,h}（uncapped）。
- ‖K‖₊ = Σ_{w∈K}(|w|+1)。
- θ_G は規則の厚さ、t_G は非終端記号の厚さ。reduced good な G では t_G ≤ θ_G。
- **型付き同値** x ≡_{L,h} y ⇔ 型が等しく、かつ D_L(x) = D_L(y)。

型 m ∈ M の最短語長を次で定めます：

$$\mu_m(L) := \min\{|w| : w\in L,\ h(w)=m\}\qquad(\min\emptyset=\infty).$$

---

## 3. 定理 A：型削除と区別対（任意の f）

**補題 A.1（型削除）.** f ≥ 1、L ∈ C^mcf_{f,h}、m ∈ M とする。このとき

$$L^{\setminus m} := L\setminus h^{-1}(m) \in \mathcal C^{\mathrm{mcf}}_{f,h}.$$

*証明.*
- h⁻¹(M∖{m}) は正規言語なので、L^{∖m} は f-MCFL です（MCFL は正規言語との共通部分で閉じる。Seki et al. 1991）。
- h⁻¹(M∖{m}) は (f,h)-tuple-substitutable です。成分の型が等しければ、どの文脈でも語全体の型が同じになるからです。
- (f,h)-tuple-substitutable な言語どうしの共通部分は (f,h)-tuple-substitutable です（v78、命題「Intersection and abelian filtering」(i)）。∎

**命題 A.2（希少な型は長い特徴データを強制する）.** L ∈ C^mcf_{f,h}、m ∈ h(L) とする。

(i) 有限な K ⊆ L が型 m の語を含まなければ、すべての r ≥ 1 について

$$L(\mathcal B^{\le r}_{f,h}(K)) \subseteq L^{\setminus m} \subsetneq L,$$

uncapped の B_{f,h} についても同様です。したがって、どちらの再構成器についても L の characteristic sample 𝓕 は型 m の語を含み、‖𝓕‖₊ ≥ μ_m(L)+1 となります。

(ii) Op が L^{∖m} の characteristic sample を持つ任意の set-driven operator なら、Op に対する L の characteristic sample はすべて型 m の語を含みます。

*証明.*
- (i) K ⊆ L^{∖m} ∈ C^mcf_{f,h} なので、v78 の健全性（Proposition「Soundness of every capped hypothesis」）を標的 L^{∖m} に適用すれば包含が得られます。L ∩ h⁻¹(m) ≠ ∅ なので包含は真です。
- (ii) 𝓕 が L の characteristic sample で型 m を避け、𝓕′ が L^{∖m} の characteristic sample だとします。すると 𝓕∪𝓕′ ⊆ L^{∖m} ⊆ L です。よって Op(𝓕∪𝓕′) は L と L^{∖m} の両方を生成しなければならず、矛盾します。∎

**系 A.3（`op:fanout-two` の十分条件）.** 固定した h と、reduced good な文法 G_n（fan-out ≤ f、rank ≤ r）が次を満たすとする：
- L(G_n) ∈ C^mcf_{f,h}
- ‖G_n‖·max{1, θ_{G_n}} = n^{O(1)}
- ある型 m_n について μ_{m_n}(L(G_n)) = n^{ω(1)}

このとき `op:fanout-two` は肯定的に解決します。しかも L(G_n) と L(G_n)^{∖m_n} の両方に characteristic sample を持つすべての set-driven operator に対して下界が成り立ちます。

**注.**
- これは TCS #1 の Prop. `prop:typed-thickness-gap`(iii)–(iv) を、任意の fan-out f に移した形そのものです。
- つまり、超多項式的に希少な型を持つ C(f,h) の元が存在しさえすれば、TCS の論法はそのまま通ります。**残る問題はクラスへの所属だけ**です。
- 命題 A.2 は下界の**必要**条件ではありません。型削除ではない部分標的 L′ ⊊ L（L′ ∈ C(f,h)）が長いデータを強制する可能性は残ります。

---

## 4. 補題 B：冪移送（fan-out 2）

**補題 B（Power transfer）.** 次を仮定する：
- L ∈ C^mcf_{f,h}（f ≥ 2）、u ∈ Σ⁺、g := h(u)
- i₀ ≥ 1, π ≥ 1 が、すべての i ≥ i₀ について g^i = g^{i+π} を満たす
- s, r ≥ i₀、d ∈ πℤ_{>0}

L のある語が因子 u^{s+d+r+2} を含むなら、すべての X, Z ∈ Σ* と Y ∈ Σ⁺ について

$$X\,u^{s}\,Y\,u^{d+r}\,Z\in L \iff X\,u^{s+d}\,Y\,u^{r}\,Z\in L.$$

*証明.*
- 与えられた語を P u^{s+d+r+2} Q と書きます。
- x = (u^s, u^{d+r})、y = (u^{s+d}, u^r)、E = (Pu) □₁ u □₂ Q と置きます。
- s, r ≥ 1 なので成分はすべて空でなく、E の区切り u も空ではありません。
- E[x] = E[y] = P u^{s+d+r+2} Q ∈ L です。
- s, r ≥ i₀ かつ π | d なので、h(u^s) = h(u^{s+d})、h(u^{d+r}) = h(u^r) です。
- arity 2 の代入可能性から D_L(x) = D_L(y) が従います。示すべき同値は、文脈 X□₁Y□₂Z の所属そのものです。∎

**注.**
- g が単位元（例：型が自明な文字）なら i₀ = π = 1 です。このとき、u⁵ を含む語が1つでもあれば、u の1コピーを、空でない任意の材料をまたいで u ブロック間で移せます。
- 有限モノイドでは i₀ + π ≤ |M|+1 なので、常に u^{2|M|+3} があれば十分です。

---

## 5. 補題 B′：局所シフト対（Ramsey）

**補題 B′（Local shift pairs）.** Σ と h: Σ* → M を固定し、c := |M|²|Σ|、R := R_c(5)（単色 K₅ に対する c 色 Ramsey 数）とする。|w| ≥ R のすべての w は次のように分解できる：

$$w = P\,x_1\,p\,q\,p\,y_2\,Q,\qquad x_1,p,y_2\in\Sigma^+,\ q\in\Sigma^*,\ |p|=1,$$

ここで h(x₁) = h(x₁pq)、h(qpy₂) = h(y₂)。したがって、w を含む任意の L ∈ C^mcf_{2,h} において、

- x = (x₁, qpy₂)、y = (x₁pq, y₂) は D_L(x) = D_L(y) を満たします。
- すなわち、すべての X, Z と Y ≠ ε について X x₁ Y qpy₂ Z ∈ L ⇔ X x₁pq Y y₂ Z ∈ L です。

*証明.*
1. 位置 {0, …, |w|−1} の対 i < j を (h(w[i:j]), h(w[i+1:j]), w[i]) で彩色します。w[i:j] は v78 のカット位置番号での w_{i+1}⋯w_j、w[i] はカット i の直後の文字です。
2. Ramsey の定理により、10個の対すべてが同色となる i₁ < ⋯ < i₅ が存在します。
3. x₁ = w[i₁:i₂]、p = w[i₂] = w[i₃]、q = w[i₂+1:i₃]、y₂ = w[i₃+1:i₅] と置きます。
   - p の等式は、(i₂,i₅) と (i₃,i₅) の第3座標が等しいことから従います。
   - i₅ ≥ i₃+2 なので y₂ は空ではありません。
4. 型の等式：
   - (i₁,i₂) と (i₁,i₃) の第1座標から h(x₁) = h(x₁pq)。
   - (i₂,i₅) と (i₃,i₅) の第2座標から h(qpy₂) = h(y₂)。
5. 文脈 E = P □₁ p □₂ Q（P = w[0:i₁]、Q = w[i₅:|w|]）の区切り p は空でなく、E[x] = E[y] = w です。∎

**意味.**
- fan-out 2 では、標的の長い語はどれも、有界な大きさの交換可能対を運んでいます。その対の成分は、言語内の**他の任意の出現位置**へ運び直せます。
- この「局所可動性」に fan-out 1 の類似はありません。arity 1 の文脈 P□Q は、その充填を決定してしまうからです。

---

## 6. 定理 C：どの有限型付けも倍化族を救えない

設定：
- Γ = {a, ⌊, ⌋, ⌈, ⌉}、W₀ = a、W_i = ⌊ W_{i−1} W_{i−1} ⌋
- L_n は E_n から E₀ → a、E_i → ⌊E_{i−1}E_{i−1}⌋ | ⌈E_{i−1}⌉ で生成される
- 天井括弧を含まない L_n の語は W_n = ⌊ⁿ a ⋯ だけ

**定理 C.** h: Γ* → M を任意の有限モノイド準同型とし、i₀ ≥ 1、π ≥ 1 を正の冪における g = h(⌊) の指数と周期とする。すべての n ≥ 2i₀+π+2（特に n ≥ 2|M|+3）について L_n ∉ C^mcf_{2,h} であり、したがってすべての f ≥ 2 について L_n ∉ C^mcf_{f,h}。

*証明.*
1. L_n ∈ C^mcf_{2,h} と仮定し、s = i₀、d = π、r = n−s−d−2 ≥ i₀ と置きます。
2. W_n は ⌊ⁿ で始まるので、u = ⌊ として補題 B が使えます。
3. W_n = ⌊ W_{n−1} W_{n−1} ⌋ と書きます。W_{n−1} の2番目のコピーは ⌊^{n−1} a で始まり、d+r = n−s−2 ≤ n−1 です。
4. W_n = X ⌊^s Y ⌊^{d+r} Z と分解します：
   - X = ⌊ とし、⌊^s を先頭ランの位置 1..s に置きます。
   - ⌊^{d+r} は、2番目のコピーの先頭ランの最後の d+r 個の床括弧とします。
   - Y は最初の a を含むので空ではありません。
5. 補題 B から W′ := X ⌊^{s+d} Y ⌊^r Z ∈ L_n が従います。
6. しかし W′ は天井括弧を含まず、最初の a の前の床括弧は n+d ≠ n 個です。よって W′ ≠ W_n となり矛盾します。
7. 閾値について：i₀ + π ≤ |M|+1 かつ i₀ ≤ |M| から、2i₀+π+2 ≤ 2|M|+3。∎

**注.**
- v78 が示したのは特殊な場合 h = h^{k,ℓ}_Γ と h = (h^{k,ℓ}_Γ, h_U) で、閾値は n ≥ max{3, k+ℓ+1} とより鋭いものでした。
- 定理 C の閾値は粗いですが、**すべての**有限型付けを量化します。窓・群・半束、それらの積など、どの型付けでもこの族は fan-out 2 で救えません。
- 障害の原因は長いラン ⌊ⁿ であり、h の選び方ではありません。
- 公式の数値確認：`v79_check_all_typing_obstruction.py`（≤5 状態のランダム DFA 型付け 3000 個 × 3 オフセットで PASS）。

---

## 7. 補題 R：緩和証人（データ長が本当に測っているもの）

設定：
- L ∈ C^mcf_{f,h} の reduced good な表現を G とし、G̃₀ をその刈り込み済み yield-type refinement（v78）とする。
- 開始記号でない型付き非終端記号 X = A_𝐭 について、L_X のタプルが属す共通の ≡_{L,h} 類を [X] と書く。型が 𝐭 で正準文脈を共有するので、これは1つの類になる（v78）。

次を定義します：

$$\kappa_G(X) := \min\{\|v\|_1 : v\in[X]\},\qquad \kappa_G := \max_X \kappa_G(X).$$

**補題 R（Relaxed witnesses）.** L ∈ C^mcf_{f,h}、G を fan-out ≤ f、rank ≤ r の reduced good 表現とする。開始記号でない各型付き非終端記号 X = A_𝐭 について次を選ぶ：
- 任意の ω′(X) ∈ [X]
- χ′(X)：G̃₀ に規則 S̃ → X があれば □₁、なければ G における**型なし**非終端記号 A の任意の導出文脈

K* を次の語からなる集合とする：
- 各 X について χ′(X)[ω′(X)]
- 開始記号でない各型付き規則 X → ρ(Y₁,…,Y_q) について χ′(X)[ρ(ω′(Y₁),…,ω′(Y_q))]
- 開始記号でない各 rank 0 の型付き規則 X → c について χ′(X)[c]

このとき K* ⊆ L であり、K* は B^{≤r}_{f,h} と B_{f,h} に対する L の characteristic sample である。

*証明.*
1. **文脈の受理.** A の導出文脈は L_A(G) ⊇ L_X のすべてのタプルを受理するので、[X] のすべてのタプルも受理します。good 性から、この文脈は 𝓔_{fan(A)} に属します（v78、補題「Canonical contexts」）。
2. **開始リンクの場合.** S̃ → X があれば、L_X のタプルはすべて L の1成分語なので、□₁ ∈ D_L(ω′(X)) です。以上から χ′(X)[ω′(X)] ∈ L。
3. **規則の語.**
   - 型付き規則では、u_j ∈ L_{Y_j} について ω′(Y_j) ≡_{L,h} u_j です。
   - v78 の補題「Composition preserves equivalence」から ρ(ω′(Y₁),…) ≡_{L,h} ρ(u₁,…) ∈ L_X。
   - rank 0 の規則は L_X の元を生成します。
   - よって K* の語はすべて L に属します。また ω′(X) は X の各規則タプルと同じ型を持ち、文脈 χ′(X) を共有します。
4. **完全性の再利用.** v78 の完全性の証明（Proposition「Completeness from a target presentation」と Lemma「Target rule words occur in the enumeration」）が使うのは、次の性質だけです：
   - 証人語が標本にあること
   - タプルの成分が空でないこと
   - テンプレートが good であること
   - χ′(X) ∈ 𝓔_d であり、子タプルが観測された出現になっていること

   ω′(X) ∈ L_X は使われていません。完全性と健全性から主張が従います。∎

**系 R.1（類の代表元による上界）.**

$$|K^\star|\le |V||M|^f+|P||M|^{fr},\qquad \|K^\star\|_+\le \bigl(|V||M|^f+|P||M|^{fr}\bigr)\bigl(1+\theta_G+\|G\|+(r+1)\kappa_G\bigr).$$

したがって、h, f, r を固定するとき、文法族 G_n について `op:fanout-two` が肯定的に解決するには κ_{G_n} = n^{ω(1)} が**必要**です。つまり G_n のある型付き分布類が、超多項式的に長い元しか持たない必要があります。

*証明.* 左辺が A の規則を使う最小の成功導出からは、固定部分の長さが θ_G 以下の導出文脈が得られます。各証人語は、そのような文脈1つ、高々 ‖G‖ 個の明示的な終端記号、総長 κ_G 以下の高々 r 個のタプル（ω′(X) を最短に選ぶ）からなります。∎

**注.**
- 命題 A.2 は、開始リンクを持つ型付き記号 S_{(m)} における長い類の特殊例です。その類は L の型 m の語からなるので、κ_G(S_{(m)}) ≥ μ_m(L) です。
- v78 の「完全精密化の指数的爆発」（`prop:typed-thickness-exponential`、L = {a,c}⁺）は、それ自体ではデータ下界を生みません。そこでは L_X は短いタプルを含みませんが、[X] は1文字のタプル `a` を含みます。

---

## 8. 定理 D：アーベル型フィルタ言語は多項式データを持つ

**定理 D.** 有限な Σ、有限型付け h: Σ* → M、f ≥ 1、r ≥ 1 を固定する。Σ, h, f, r のみに依存する定数 C, e があって、次が成り立つ。

𝔸 を任意のアーベル群、φ: Σ* → 𝔸 を準同型、𝓗 ≤ 𝔸、γ ∈ 𝔸、Acc ⊆ M とし、

$$L := h^{-1}(\mathsf{Acc})\cap\varphi^{-1}(\gamma+\mathcal H)$$

が fan-out ≤ f、rank ≤ r の reduced good な表現 G = (V, Σ, P, S) を持つとする。このとき L ∈ C^mcf_{f,h} であり、B^{≤r}_{f,h} は次を満たす characteristic sample K* ⊆ L を持つ：

$$|K^\star|\le|V||M|^f+|P||M|^{fr},\qquad \|K^\star\|_+\le C\bigl(\|G\|\max\{1,\theta_G\}\bigr)^e.$$

特に、すべての m ∈ h(L) について μ_m(L) ≤ C(‖G‖ max{1, θ_G})^e。

**使う外部結果.**
- **Parikh の定理.** 各 m について、h⁻¹(m) と h⁻¹(m)∩Σ⁺ の Parikh 像は半線形です。その表現を一度固定すれば、線形集合の個数・定数・周期は h のみに依存する定数 C_h で抑えられます。
- **Papadimitriou (J. ACM 28 (1981) 765–768).** Az = b, z ≥ 0 が整数解を持ち、A が m 行 n 列で A, b の成分がすべて [−a, a] に入るなら、全成分が n(ma)^{2m+1} 以下の整数解が存在します。

*証明.*

**所属.**
- L は仮定より f-MCFL です。
- h⁻¹(Acc) は (f,h)-tuple-substitutable です。
- 任意のアーベル群 𝔸 について φ⁻¹(γ+𝓗) は (f, h_triv)-tuple-substitutable です。
- 共通部分は代入可能性を保ちます（v78 の命題「Intersection and abelian filtering」）。よって L ∈ C^mcf_{f,h}。

**記号.**
- ψ: Σ* → ℕ^Σ を Parikh 写像とし、タプルについては Ψ(u) = Σ_i ψ(u_i) と書きます。
- 𝔸 はアーベル群なので、群準同型 φ̄: ℤ^Σ → 𝔸 があって φ = φ̄∘ψ です。
- Λ := {v ∈ ℤ^Σ : φ̄(v) ∈ 𝓗} と置きます。
- 文脈 E について ψ(E[u]) = ψ(E) + Ψ(u) です（ψ(E) は固定部分を数える）。

**Step 1（値の不変性）.** A ∈ V と u, u′ ∈ L_A(G) について Ψ(u) − Ψ(u′) ∈ Λ。
- A はある成功導出に現れます。その部分木を除くと、E[u], E[u′] ∈ L となる導出文脈 E が得られます（線形かつ非削除のテンプレート）。
- 両方の値は γ+𝓗 に入ります。

**Step 2（小さな生成元）.**
- 各 A について、‖ω_A‖₁ ≤ t_G となる ω_A ∈ L_A(G) を固定します。
- 規則 R: A → ρ(B₁,…,B_q) について、c_R ∈ ℕ^Σ をその終端記号の個数とし、δ_R := Ψ(ω_A) − c_R − Σ_j Ψ(ω_{B_j}) と置きます。
- ρ(ω_{B₁},…,ω_{B_q}) ∈ L_A(G) なので、Step 1 から δ_R ∈ Λ。また ‖δ_R‖₁ ≤ T := (r+1)t_G + ‖G‖。
- Γ_T := {λ ∈ Λ : ‖λ‖₁ ≤ T} とし、それが生成する部分群を Λ_T とします。|Γ_T| ≤ (2T+1)^{|Σ|} です。

**Step 3.** すべての u ∈ L_A(G) について Ψ(u) − Ψ(ω_A) ∈ Λ_T。
- 導出に関する帰納法で示します。根の規則が R で子の yield が u_j なら、

$$\Psi(u)-\Psi(\omega_A)=\sum_j\bigl(\Psi(u_j)-\Psi(\omega_{B_j})\bigr)-\delta_R.$$

**Step 4（短い型付きタプル）.**
- X = A_𝐭 を G̃₀ の開始記号でない型付き非終端記号、d = fan(A) とし、u ∈ L_X を固定します。
- 各 i ≤ d について、ψ(h⁻¹(t_i)∩Σ⁺) の固定表現から、ψ(u_i) を含む線形集合 {c_i + Σ_{p∈P_i} ν_p p} を選びます。
- 次の連立系を考えます：

$$\sum_i\Bigl(c_i+\sum_{p\in P_i}\nu_{i,p}\,p\Bigr)-\sum_{\lambda\in\Gamma_T}(\mu^+_\lambda-\mu^-_\lambda)\lambda=\Psi(\omega_A),\qquad \nu,\mu^\pm\ge 0\ \text{整数}.$$

- この系は |Σ| 本の方程式からなり、u に Step 3 を適用すれば解を持ちます。
- 成分は a := T + fC_h で抑えられ、未知数は高々 fC_h + 2(2T+1)^{|Σ|} 個です。
- Papadimitriou の上界から、全成分が poly(T) 以下の解が存在します（次数は |Σ| のみに依存、O(|Σ|)）。
- 各ベクトル c_i + Σ ν_{i,p} p は、ある ω′_i ∈ h⁻¹(t_i)∩Σ⁺ の Parikh ベクトルです。
- ω′(X) := (ω′₁, …, ω′_d) と置けば、次が成り立ちます：
  - h^{(d)}(ω′(X)) = 𝐭
  - Ψ(ω′(X)) − Ψ(ω_A) ∈ Λ_T
  - ‖ω′(X)‖₁ ≤ poly(T)

**Step 5（同値性）.** 2つのタプル v, v′ が成分ごとに同じ型を持ち、Ψ(v) − Ψ(v′) ∈ Λ なら、すべての文脈 E について E[v] ∈ L ⇔ E[v′] ∈ L。
- 語全体の型が一致します。
- φ(E[v]) − φ(E[v′]) = φ̄(Ψ(v) − Ψ(v′)) ∈ 𝓗 です。

**Step 6（緩和証人による結論）.**
- Step 4 と Step 5 から、すべての u ∈ L_X について ω′(X) ≡_{L,h} u です。実際、

$$\Psi(\omega'(X))-\Psi(u)=(\Psi(\omega'(X))-\Psi(\omega_A))-(\Psi(u)-\Psi(\omega_A))\in\Lambda_T\subseteq\Lambda.$$

- これらの ω′(X) で補題 R を適用します。系 R.1 から

$$\|K^\star\|_+\le\bigl(|V||M|^f+|P||M|^{fr}\bigr)\bigl(1+\theta_G+\|G\|+(r+1)\max_X\|\omega'(X)\|_1\bigr).$$

- max_X ‖ω′(X)‖₁ ≤ poly(T) であり、t_G ≤ θ_G より T ≤ (r+1)θ_G + ‖G‖ です。
- 最後に、命題 A.2(i) から K* はすべての型 m ∈ h(L) の語を含むので、μ_m(L) ≤ ‖K*‖₊。∎

**注.**
- 定理 D は **LG 外**の型付け（h_U を含む）でも、fan-out 1 を含むすべての fan-out でも成り立ちます。
- 括弧付き CFG 族はアーベル型フィルタではありません。
- v78 が示した C(f,h) の元の多く（例：MIX₂⁺、L_intr）は、アーベル型フィルタによって作られています。したがって `op:fanout-two` を肯定的に解くには、**型とアーベル不変量だけではタプル分布が決まらない**標的が必要です。
- 型で互いに素な分岐をもつアーベルフィルタの有限和（L_⋆ など）も、分岐ごとに同じ議論が通ると予想されます（補題 F1 として未証明）。

**整合性チェック.**
- L = {a,c}⁺（φ 自明）では、完全精密化の厚さは 2ⁿ です。しかし [X] には `a` が入るので、データは短くなります。v78 の命題と矛盾しません。
- 一方、L = {c, a^N} のような「型 1 の語が長いアーベル言語」には、厚さが小さい文法がありません。倍化の中間記号の値が短い語で実現できないからです。

---

## 9. 予想

**予想 E（fan-out 2 における類代表元の短さ）.** 有限な Σ、有限型付け h、r ≥ 1 に対し、ある多項式 p があって、fan-out ≤ 2、rank ≤ r、L(G) ∈ C^mcf_{2,h} を満たすすべての reduced good 表現 G について

$$\kappa_G\le p(\|G\|\max\{1,\theta_G\}).$$

- 系 R.1 により、予想 E は、すべての固定 h について B^{≤r}_{2,h} に関する `op:fanout-two` の**否定的**解決を**導きます**（逆は主張しません）。
- fan-out 1 では偽です（TCS #1 の族）。
- h(Σ⁺) ∈ **LG** なら真です。v78 の `lem:local-group-shortest` が型付き yield の最短長を抑え、L_X ⊆ [X] だからです。
- アーベル型フィルタ標的についても真です（定理 D）。

**予想 E′（希少な型の短さ）.** 同じ設定で、すべての m ∈ h(L(G)) について μ_m(L(G)) ≤ p(‖G‖ max{1, θ_G})。
- E′ は E から従います。
- E′ が成り立てば、命題 A.2 の型削除の方法では `op:fanout-two` は解けません。

---

## 10. 候補族と失敗例（Phase 2–3）

**判定方法.**
- `v79_lib.py` は、有限言語について、arity 1/2 のすべての出現とすべての文脈を列挙し、分布を比較します。
- 有限言語では、空でない分布を持つタプルは必ずどこかの語に出現するので、この判定は**厳密**です。
- 違反が見つかれば独立に再検証します。小さい n での PASS を定理とはみなしません。
- 型付けは h_U（マーカー文字 ↦ ζ）と、窓(1,1)×h_U の2種類です。

| # | 構成原理 | 希少（マーカーなし）語 | 最初の失敗（h_U ／ 窓×h_U） | 根本原因 |
|---|---|---|---|---|
| P1 | 剛体括弧の倍化（TCS #1） | W_n、長さ 3·2ⁿ−2 | n=2 arity2 ／ n=3 arity2 | 冪 ⌊ⁿ（定理 C） |
| P2 | 単項希少語 a^{2ⁿ}＋水準カウンタ `c dⁱ` | a^{2ⁿ} | n=2 arity1 ／ n=3 arity1 | 近道の曖昧性、d ラン（補題 B） |
| P3 | 希少部を自由化 {a,b}^{2ⁿ}＋天井括弧の近道 | {a,b}^{2ⁿ} の全語 | n=2 arity1 ／ n=3 arity1 | 二進整列と移送の衝突 |
| P4 | fan-out 2 分離（葉文字列, 単一 a ラン） | c^{2ⁿ} m a^{2ⁿ} | n=2 arity1 ／ n=2 arity1 | λ-free 性が第2の長い領域を強制 |
| P5 | 同期した2成分括弧（2種の括弧） | 長さ 2^{n+2}−1 | n=2 arity2 ／ n=3 arity2 | 成分をまたぐシフト対（B′） |
| P6 | Thue–Morse 希少語（重複なし、高い冪なし） | T_n # T̄_n | n=2 arity2 ／ n=3 arity1 | シフト対 (b,ac)~(ba,c)、包み込みの曖昧性 |

**各族の文法**（すべて good・reduced で、サイズ O(n)、厚さ O(n)。検査はスクリプトで実施）：

- **P1**：E₀ → a；E_i → ⌊E_{i−1}E_{i−1}⌋ | ⌈E_{i−1}⌉。
- **P2**：A₀ → a；A_i → A_{i−1}A_{i−1} | c dⁱ。
- **P3**：E₀ → a | b；E_i → E_{i−1}E_{i−1} | ⌈E_{i−1}⌉。
- **P4**：
  - B₀ → (c, a)
  - B_i → (ξ₁¹ξ₂¹, ξ₁²ξ₂²)(B_{i−1}, B_{i−1}) | (d, a)
  - S → (ξ¹ m ξ²)(B_n)
- **P5**：
  - E₀ → (a, b)
  - E_i → ( `(` ξ₁¹ξ₂¹, ξ₂²ξ₁² `)` )(E_{i−1}, E_{i−1}) | ( `[` ξ¹, ξ² `]` )(E_{i−1})
  - S → (ξ¹ # ξ²)
- **P6**：
  - X₀ → (a, b)、Y₀ → (b, a)
  - X_i → (ξ₁¹ξ₂¹, ξ₁²ξ₂²)(X_{i−1}, Y_{i−1}) | (c ξ¹, ξ² c)(X_{i−1})
  - Y_i → (ξ₁¹ξ₂¹, ξ₁²ξ₂²)(Y_{i−1}, X_{i−1}) | (c ξ¹, ξ² c)(Y_{i−1})（i < n のみ）
  - S → (ξ¹ # ξ²)(X_n)

**代表的な最小違反**（全出力は付録 A）：
- **P1**（n=2, h_U）：x = (`⌊`, `a⌋`)、y = (`⌊a`, `⌋`) が文脈 `⌊⌊aa⌋□a□⌋` を共有します。しかし F = `□⌈a⌉⌊a□⌋` は x だけを受理します。
- **P5**（n=2, h_U）：x = (`[`, `]`)、y = (`([a`, `b])`) が `□(aa#bb)□` を共有します。しかし `□[a#b□]` は x だけを受理します。
- **P6**（n=2, h_U）：x = (`b`, `ac`)、y = (`ba`, `c`) が `abcb#□a□` を共有します。しかし `ca□#b□` は x だけを受理します。これはまさに補題 B′ のシフト対です（x₁ = b, p = a, q = ε）。

### 3つの「逃げ道」がふさがる理由

1. **剛体的（木構造的）な希少語.** 長い冪を含めば補題 B が、重複なし語なら定数サイズのシフト対（B′）が働きます。どちらでもブロックが無関係な出現位置の間で運ばれ、剛体性が破れます（P1, P5, P6）。
2. **可換的な希少語（単項または自由）.** 運ばれる量子が無害であるためには、所属が個数だけで決まる必要があります。すると指数的な圧縮には、1次元・2次元のすべての代入と整合する「近道」符号が必要になります。厳密なアーベルフィルタでは定理 D によりこれは不可能です。非アーベルの試作 P2–P3 では、値の符号化が arity 1 の段階で代入可能性を壊します。
3. **単一ラン設計**（長い材料を1ブロックに集め、移送を自明にする）. good 文法の λ-free 性と衝突します。純導出の各葉が**各**成分に1文字ずつ寄与するので、2番目の長い領域が現れます（P4）。

---

## 11. 文法スキーマの全列挙（`v79_schema_search.py`）

**スキーマ空間.**
- X₀：{a, b} 上の定数。
- 倍化規則 X_i → τ(X_{i−1}, X_{i−1})：fan-out d ∈ {1,2} の good な rank 2 テンプレートすべてに、{a,b} の文字を高々1つ挿入したもの。
- 近道規則 X_i → σ(X_{i−1}) または定数：マーカー c を含む文字を高々2つ挿入。
- d = 2 の根：S → (x¹ t x²)、t ∈ {a, b}。

**性質.** どの文法も reduced・good で、|G| = O(n)、θ = O(n)。c を含まない唯一の語の長さは Θ(2ⁿ) です。

| 空間 | スキーマ数 | 型付け | 結果 |
|---|---:|---|---|
| fan-out 1（S1） | 322 | h_U | 全部 n=2 で失敗 |
| fan-out 1（S1） | 322 | 窓(1,1)×h_U | n=2 で 214、n=3 で 108 失敗 |
| fan-out 2（S2） | 28,320 | h_U | n=1 で 24,152、n=2 で 4,168 失敗 |
| fan-out 2（S2） | 28,320 | 窓(1,1)×h_U | n=2 で 28,132、n=3 で 188 失敗 |

**n=3 まで生き残ったスキーマは 0 個**です。これは有限探索なので、除外されるのはこのスキーマ空間だけです。

---

## 12. 新しい洞察

- **局所可動性が fan-out 2 特有の現象.**
  - 補題 B′ により、(Σ,h) のみで決まる定数より長い語は、すべて有界な交換可能対を含みます。
  - その成分は言語内のどこへでも置き直せます。
  - fan-out 1 の代入可能性にはこの帰結がないので、TCS #1 の剛体族はそこでは機能します。
- **B^{≤r} のデータ長の真の量は κ_G**（補題 R）であり、完全精密化の型付き厚さではありません。下界には長い類が必要です。希少な型は、開始リンクを持つ型付き記号における長い類の一例です。
- **アーベル不変量は長い類を作れない**（定理 D）。これは型付けが LG に入るかどうかと無関係です。したがって v76 の半束障害は、fan-out ≥ 2 では必要条件ではあっても、十分条件にはほど遠いことになります。
- **予想される全体像（E）.** 局所可動性と有限型付けによって、大きなスケールでは類の所属が「型＋加法的不変量」で決まり、κ_G が多項式になる。そうであれば、B^{≤r}_{2,h} に関する `op:fanout-two` の答えは**否定的**です。

---

## 13. 次に解くべき補題（正確な定式化）

1. **予想 E（κ 有界性）.** Σ, h, r を固定すると、ある多項式 p があって、fan-out ≤ 2・rank ≤ r の reduced good な G で L(G) ∈ C(2,h) を満たすものすべてについて κ_G ≤ p(‖G‖·max{1, θ_G})。否定的解決を導き、f = 1 では偽です。
2. **補題 F1（分岐アーベル標的）.** 定理 D を有限和 L = ⋃_j h⁻¹(Acc_j) ∩ φ_j⁻¹(γ_j + H_j)（Acc_j は互いに素）へ拡張する。v78 の L_⋆ を含みます。想定する証明：分岐ごとに Step 1–5 を行い、文脈に充填したタプルの分岐を成分の型で決める。
3. **補題 F2（スキーマ）.** fan-out ≤ 2 の任意の固定 good 倍化スキーマ (β, τ, σ) と任意の有限 h について、十分大きい n で L_n ∉ C(2,h)。
   - 方針1：純導出の yield が u^{K(h)} を含むことを示し、補題 B を使う。
   - 方針2：Thue–Morse 型スキーマでは、近道をまたいで運ぶと L_n から外れる B′ 対を構成する。
4. **補題 F3（冪正規形）.** L ∈ C(2,h) で、ある語が u^{2|M|+3} を含むとする。このとき、長さ i₀ 以上の極大 u ブロックの長さベクトルは、補題 B の移送を法としてその和を通じてのみ効くこと、ならびに長い u ブロックを含む類 [X] が「1つを除き u ブロックがすべて i₀+π 未満」の代表元を持つことを示す。
5. **問題 G（肯定方向）.** 文法サイズを無視して、すべての元が超多項式長であるような型付き分布類を1つでも持つ L ∈ C(2,h) を見つける。固定 h でこれすら不可能なら、予想 E は文法表現によらない強い形で成り立ちます。

---

## 14. 原稿への影響（未適用）

- **定理 C**：`prop:fixed-window-doubling-fanout-two` を置き換えるか、その後に置く候補です。すべての型付けを量化します。窓の場合の v78 の鋭い閾値は引き続き有効です。
- **補題 R＋定理 D**：第5節の新しい小節の候補です。R は `prop:typed-thickness-exponential` の解釈も変えます（完全精密化の爆発はデータ下界ではない）。
- **`op:fanout-two` の本文**：必要条件 κ_{G_n} = n^{ω(1)} を追記する候補です。

いずれも採用前に独立監査が必要で、英語版と日本語版の同期も必要です。

---

## 15. 再現方法

```
python3 revision/v79_check_all_typing_obstruction.py       # 定理 C の公式チェック
python3 revision/v79_candidate_families.py 3                # P1–P6（出力：v79_candidate_families_output.txt）
python3 revision/v79_schema_search.py --d 1 [--window]      # S1
python3 revision/v79_schema_search.py --d 2 [--window]      # S2（2コアで約10分）
pdflatex revision/v79_fanout2_results.tex                   # 証明 A, B, B′, C, R, D
```

GitHub：
- ブランチ `mcfg2-v79-fanout2-lower-bound-search`
- コミット `dca7cc9c5f1cf14fbaa6e79b65de89892384c531`
- Draft PR https://github.com/growupkuriyama-hub/Papers/pull/46

参考：Fomin et al., *On the Optimality of Pseudo-polynomial Algorithms for Integer Programming*, arXiv:1607.05342（Papadimitriou 1981 の小解定理の再掲の確認に使用）。


---

## 付録 A：候補族テストの全出力（`v79_candidate_families_output.txt`）

```
========================================================================
P1 rigid bracket doubling
 n=1: good=True |G|=14 theta=4 |L|=2 min-len-by-U-type=[(frozenset(), 4), (frozenset({'⌈', '⌉'}), 3)]
   [U(⌈⌉)] PASS (exact, finite) in 0.0s
   [win1,1xU(⌈⌉)] PASS (exact, finite) in 0.0s
 n=2: good=True |G|=26 theta=8 |L|=6 min-len-by-U-type=[(frozenset(), 10), (frozenset({'⌈', '⌉'}), 5)]
   [U(⌈⌉)] FAIL d=2: x=('⌊', 'a⌋') y=('⌊a', '⌋')
       shared=('⌊', 'a', '⌈a⌉⌋')  F=('', '⌈a⌉⌊a', '⌋')  F[x]∈L=True F[y]∈L=False
   [win1,1xU(⌈⌉)] PASS (exact, finite) in 0.0s
 n=3: good=True |G|=38 theta=12 |L|=42 min-len-by-U-type=[(frozenset(), 22), (frozenset({'⌈', '⌉'}), 7)]
   [U(⌈⌉)] FAIL d=2: x=('⌈', '⌊a') y=('⌈⌊', 'a')
       shared=('', '⌊', 'a⌋⌊aa⌋⌋⌉')  F=('', '⌈', 'a⌋⌉⌉')  F[x]∈L=True F[y]∈L=False
   [win1,1xU(⌈⌉)] FAIL d=2: x=('⌊⌊aa⌋⌈', '⌉⌋') y=('⌊⌈', '⌉⌊aa⌋⌋')
       shared=('⌊⌊⌊aa⌋⌊aa⌋⌋', 'a', '⌋')  F=('', '⌈a⌉⌉⌊⌈a', '⌋')  F[x]∈L=False F[y]∈L=True
========================================================================
P2 unary rare + level counter
 n=1: good=True |G|=10 theta=2 |L|=2 min-len-by-U-type=[(frozenset(), 2), (frozenset({'c', 'd'}), 2)]
   [U(cd)] PASS (exact, finite) in 0.0s
   [win1,1xU(cd)] PASS (exact, finite) in 0.0s
 n=2: good=True |G|=19 theta=4 |L|=5 min-len-by-U-type=[(frozenset(), 4), (frozenset({'c', 'd'}), 3)]
   [U(cd)] FAIL d=1: x=('cd',) y=('cdc',)
       shared=('', 'd')  F=('', 'aa')  F[x]∈L=True F[y]∈L=False
   [win1,1xU(cd)] PASS (exact, finite) in 0.0s
 n=3: good=True |G|=29 theta=7 |L|=26 min-len-by-U-type=[(frozenset(), 8), (frozenset({'c', 'd'}), 4)]
   [U(cd)] FAIL d=1: x=('cd',) y=('cdc',)
       shared=('cdd', 'd')  F=('', 'dd')  F[x]∈L=True F[y]∈L=False
   [win1,1xU(cd)] FAIL d=1: x=('cdcd',) y=('cdd',)
       shared=('cdd', '')  F=('', 'd')  F[x]∈L=False F[y]∈L=True
========================================================================
P3 free rare part {a,b}^(2^n)
 n=1: good=True |G|=14 theta=3 |L|=6 min-len-by-U-type=[(frozenset(), 2), (frozenset({'⌈', '⌉'}), 3)]
   [U(⌈⌉)] PASS (exact, finite) in 0.0s
   [win1,1xU(⌈⌉)] PASS (exact, finite) in 0.0s
 n=2: good=True |G|=24 theta=5 |L|=42 min-len-by-U-type=[(frozenset(), 4), (frozenset({'⌈', '⌉'}), 4)]
   [U(⌈⌉)] FAIL d=1: x=('⌈a',) y=('ab⌈',)
       shared=('', 'a⌉')  F=('', '⌉aa')  F[x]∈L=True F[y]∈L=False
   [win1,1xU(⌈⌉)] PASS (exact, finite) in 0.0s
 n=3: good=True |G|=34 theta=8 |L|=1806 min-len-by-U-type=[(frozenset(), 8), (frozenset({'⌈', '⌉'}), 6)]
   [U(⌈⌉)] FAIL d=1: x=('ab⌈',) y=('⌈b',)
       shared=('aaba', 'a⌉')  F=('', 'aaa⌉')  F[x]∈L=False F[y]∈L=True
   [win1,1xU(⌈⌉)] FAIL d=1: x=('aab⌈b',) y=('a⌈bb',)
       shared=('⌈b⌉a', '⌉')  F=('a', 'a⌉')  F[x]∈L=True F[y]∈L=False
========================================================================
P4 fan-out-2 split (single a-run)
 n=1: good=True |G|=18 theta=5 |L|=2 min-len-by-U-type=[(frozenset(), 5), (frozenset({'d'}), 3)]
   [U(d)] PASS (exact, finite) in 0.0s
   [win1,1xU(d)] PASS (exact, finite) in 0.0s
 n=2: good=True |G|=28 theta=7 |L|=5 min-len-by-U-type=[(frozenset(), 9), (frozenset({'d'}), 3)]
   [U(d)] FAIL d=1: x=('dm',) y=('ddma',)
       shared=('', 'a')  F=('d', 'aa')  F[x]∈L=True F[y]∈L=False
   [win1,1xU(d)] FAIL d=1: x=('dma',) y=('ddmaa',)
       shared=('', '')  F=('d', 'a')  F[x]∈L=True F[y]∈L=False
 n=3: good=True |G|=38 theta=9 |L|=24 min-len-by-U-type=[(frozenset(), 17), (frozenset({'d'}), 3)]
   [U(d)] FAIL d=1: x=('ccmaa',) y=('m',)
       shared=('ddcc', 'aaaa')  F=('d', 'a')  F[x]∈L=False F[y]∈L=True
   [win1,1xU(d)] FAIL d=1: x=('dma',) y=('dccmaaa',)
       shared=('dcc', 'aaa')  F=('', '')  F[x]∈L=True F[y]∈L=False
========================================================================
P5 synchronised fan-out-2 brackets
 n=1: good=True |G|=23 theta=7 |L|=2 min-len-by-U-type=[(frozenset(), 7), (frozenset({'[', ']'}), 5)]
   [U([])] PASS (exact, finite) in 0.0s
   [win1,1xU([])] PASS (exact, finite) in 0.0s
 n=2: good=True |G|=38 theta=11 |L|=6 min-len-by-U-type=[(frozenset(), 15), (frozenset({'[', ']'}), 7)]
   [U([])] FAIL d=2: x=('[', ']') y=('([a', 'b])')
       shared=('', '[a#b]', '')  F=('', '[a#b', ']')  F[x]∈L=True F[y]∈L=False
   [win1,1xU([])] PASS (exact, finite) in 0.0s
 n=3: good=True |G|=53 theta=15 |L|=42 min-len-by-U-type=[(frozenset(), 31), (frozenset({'[', ']'}), 9)]
   [U([])] FAIL d=2: x=('[', '(a') y=('[(', 'a')
       shared=('', '(', 'a(aa#bb)bb))]')  F=('', '[', 'a#bb)]]')  F[x]∈L=True F[y]∈L=False
   [win1,1xU([])] FAIL d=2: x=('[(aa', 'bb)]') y=('[[a', 'b]]')
       shared=('(', '([a[a#b]b])', ')')  F=('(', '[[a#', 'b]])')  F[x]∈L=False F[y]∈L=True
========================================================================
P6 Thue-Morse rare word (overlap-free)
 n=1: good=True |G|=24 theta=5 |L|=2 min-len-by-U-type=[(frozenset(), 5), (frozenset({'c'}), 5)]
   [U(c)] PASS (exact, finite) in 0.0s
   [win1,1xU(c)] PASS (exact, finite) in 0.0s
 n=2: good=True |G|=50 theta=9 |L|=6 min-len-by-U-type=[(frozenset(), 9), (frozenset({'c'}), 7)]
   [U(c)] FAIL d=2: x=('b', 'ac') y=('ba', 'c')
       shared=('abcb#', 'a', '')  F=('ca', '#b', '')  F[x]∈L=True F[y]∈L=False
   [win1,1xU(c)] PASS (exact, finite) in 0.0s
 n=3: good=True |G|=76 theta=15 |L|=42 min-len-by-U-type=[(frozenset(), 17), (frozenset({'c'}), 9)]
   [U(c)] FAIL d=1: x=('cb#b',) y=('ccb#bc',)
       shared=('cca', 'cacc')  F=('cab', 'aacc')  F[x]∈L=True F[y]∈L=False
   [win1,1xU(c)] FAIL d=1: x=('cb#bc',) y=('ccb#bcc',)
       shared=('cca', 'acc')  F=('ccac', 'cacc')  F[x]∈L=True F[y]∈L=False
```

## 付録 B：スキーマ列挙の出力（各実行の最終行）

**`v79_schema_search_d1_hU_output.txt`**

```
schemas: 322  (window=False)
failures by first failing n: {2: 322}
survivors through n = 3 : 0
```

**`v79_schema_search_d1_win11xhU_output.txt`**

```
schemas: 322  (window=True)
failures by first failing n: {2: 214, 3: 108}
survivors through n = 3 : 0
```

**`v79_schema_search_d2_hU_output.txt`**

```
schemas: 28320  (window=False)
failures by first failing n: {1: 24152, 2: 4168}
survivors through n = 3 : 0
```

**`v79_schema_search_d2_win11xhU_output.txt`**

```
schemas: 28320  (window=True)
failures by first failing n: {2: 28132, 3: 188}
survivors through n = 3 : 0
```

## 付録 C：ソースコード全文

### `revision/v79_lib.py`

```python
#!/usr/bin/env python3
"""v79 research library: finite MCFG evaluation and exact (f,h)-tuple
substitutability checking for FINITE languages.

Conventions follow main.tex (v78):
  * tuple components are nonempty;
  * an arity-d sentence context u0 [] u1 [] ... [] ud has nonempty
    internal separators u1..u_{d-1}; outer parts may be empty;
  * (f,h)-substitutability: for every d<=f and all x,y in (Sigma^+)^d,
    equal componentwise h-types and one shared accepting context imply
    equal distributions D_L(x)=D_L(y).

For a FINITE language L every tuple with nonempty distribution occurs in
some word of L, so enumerating all occurrences is an EXACT decision
procedure (optionally restricted to tuples with bounded component length;
the restriction is then reported and the check is only a partial test).

Nothing here proves a general theorem; the scripts only test finite
instances and symbolic formulas.
"""
from __future__ import annotations

from collections import defaultdict
from functools import lru_cache
from typing import Callable, Dict, Iterable, List, Optional, Sequence, Tuple

# ---------------------------------------------------------------------------
# Finite monoids / typings
# ---------------------------------------------------------------------------


class Typing:
    """A finite-monoid homomorphism given by letter images and a product.

    `mul(a,b)` must be associative with identity `one`.  Types of words are
    computed left to right; results are memoised per word.
    """

    def __init__(self, name: str, letter: Callable[[str], object],
                 mul: Callable[[object, object], object], one: object):
        self.name = name
        self.letter = letter
        self.mul = mul
        self.one = one
        self._cache: Dict[str, object] = {}

    def __call__(self, w: str):
        c = self._cache.get(w)
        if c is not None:
            return c
        t = self.one
        for ch in w:
            t = self.mul(t, self.letter(ch))
        self._cache[w] = t
        return t


def trivial_typing() -> Typing:
    return Typing("triv", lambda c: 0, lambda a, b: 0, 0)


def content_typing(markers: Iterable[str], name: str = "content") -> Typing:
    """Semilattice of subsets: h(w) = set of marker letters occurring in w.
    With a single marker this is the two-element semilattice h_U."""
    ms = frozenset(markers)
    return Typing(name, lambda c: frozenset([c]) if c in ms else frozenset(),
                  lambda a, b: a | b, frozenset())


def window_typing(k: int, l: int, name: Optional[str] = None) -> Typing:
    """Prefix-suffix typing h^{k,l}_Sigma realised directly on words."""
    m0 = max(1, k + l)

    class _W(Typing):
        def __call__(self, w: str):
            if len(w) < m0:
                return ("s", w)
            return ("l", w[:k], w[len(w) - l:] if l else "")

    t = _W(name or f"win{k},{l}", None, None, None)
    return t


def product_typing(*ts: Typing) -> Typing:
    class _P(Typing):
        def __call__(self, w: str):
            return tuple(t(w) for t in ts)

    return _P("x".join(t.name for t in ts), None, None, None)


def transformation_typing(n_states: int, maps: Dict[str, Tuple[int, ...]],
                          name: str = "trans") -> Typing:
    """Transition monoid of a DFA: letters act on {0..n-1} (left-to-right
    composition f then g)."""
    ident = tuple(range(n_states))

    def mul(f, g):
        return tuple(g[f[i]] for i in range(n_states))

    return Typing(name, lambda c: maps[c], mul, ident)


# ---------------------------------------------------------------------------
# Tuple occurrences and the exact check
# ---------------------------------------------------------------------------

Ctx = Tuple[str, ...]          # (u0, u1, ..., ud)
Tup = Tuple[str, ...]          # (x1, ..., xd)


def occurrences(w: str, d: int, max_comp: Optional[int] = None):
    """Yield (x, E) for every arity-d tuple occurrence in w.
    Components and internal separators are nonempty."""
    n = len(w)
    if d == 1:
        for i in range(n):
            top = n if max_comp is None else min(n, i + max_comp)
            for j in range(i + 1, top + 1):
                yield (w[i:j],), (w[:i], w[j:])
        return
    if d == 2:
        for i1 in range(n):
            top1 = n if max_comp is None else min(n, i1 + max_comp)
            for j1 in range(i1 + 1, top1 + 1):
                x1 = w[i1:j1]
                u0 = w[:i1]
                for i2 in range(j1 + 1, n):
                    top2 = n if max_comp is None else min(n, i2 + max_comp)
                    sep = w[j1:i2]
                    for j2 in range(i2 + 1, top2 + 1):
                        yield (x1, w[i2:j2]), (u0, sep, w[j2:])
        return
    raise ValueError("only d in {1,2} implemented")


def fill(E: Ctx, x: Tup) -> str:
    out = [E[0]]
    for i, xi in enumerate(x):
        out.append(xi)
        out.append(E[i + 1])
    return "".join(out)


class Violation:
    def __init__(self, d, x, y, shared, F, accepts_x, accepts_y):
        self.d, self.x, self.y, self.shared, self.F = d, x, y, shared, F
        self.accepts_x, self.accepts_y = accepts_x, accepts_y

    def size(self):
        return sum(map(len, self.x)) + sum(map(len, self.y)) + sum(map(len, self.F))

    def __repr__(self):
        return (f"Violation(d={self.d}, x={self.x}, y={self.y}, "
                f"shared={self.shared}, F={self.F}, F[x] in L={self.accepts_x}, "
                f"F[y] in L={self.accepts_y})")


def check_substitutable(L: Iterable[str], h: Typing, f: int = 2,
                        max_comp: Optional[int] = None,
                        find_min: bool = True,
                        arities: Optional[Sequence[int]] = None):
    """Exact test of (f,h)-tuple substitutability for a finite language.

    Returns (ok, violation_or_None, stats).  If max_comp is given, only
    tuples whose components all have length <= max_comp are compared
    (a partial test)."""
    Ls = set(L)
    stats = {}
    best: Optional[Violation] = None
    for d in (arities or range(1, f + 1)):
        dist: Dict[Tup, set] = defaultdict(set)
        for w in Ls:
            for x, E in occurrences(w, d, max_comp):
                dist[x].add(E)
        stats[d] = len(dist)
        sig = {x: frozenset(Es) for x, Es in dist.items()}
        # invert: context -> tuples
        by_ctx: Dict[Ctx, List[Tup]] = defaultdict(list)
        for x, Es in dist.items():
            for E in Es:
                by_ctx[E].append(x)
        for E, xs in by_ctx.items():
            groups: Dict[object, List[Tup]] = defaultdict(list)
            for x in xs:
                groups[tuple(h(c) for c in x)].append(x)
            for _, g in groups.items():
                if len(g) < 2:
                    continue
                first = sig[g[0]]
                for y in g[1:]:
                    if sig[y] != first:
                        x0 = g[0]
                        diff = first ^ sig[y]
                        # pick the smallest distinguishing context
                        F = min(diff, key=lambda c: (sum(map(len, c)), c))
                        v = Violation(d, x0, y, E, F, F in first, F in sig[y])
                        if not find_min:
                            return False, v, stats
                        if best is None or v.size() < best.size():
                            best = v
        if best is not None and find_min:
            # report the smallest violation at the lowest failing arity
            return False, best, stats
    return best is None, best, stats


def minimize_violation(L, h, v: Violation):
    """Given a violation, verify it independently (membership + types)."""
    Ls = set(L)
    assert tuple(h(c) for c in v.x) == tuple(h(c) for c in v.y)
    assert all(v.x) and all(v.y)
    assert all(v.shared[1:-1]) and all(v.F[1:-1])
    assert fill(v.shared, v.x) in Ls and fill(v.shared, v.y) in Ls
    assert (fill(v.F, v.x) in Ls) != (fill(v.F, v.y) in Ls)
    return True


# ---------------------------------------------------------------------------
# Finite (acyclic) MCFG evaluation, goodness and thickness
# ---------------------------------------------------------------------------
# A rule is (lhs, children, template) where template is a tuple of
# components; each component is a list of items, an item being either a
# terminal string or a pair (j, k) meaning component k of child j
# (0-based).


class MCFG:
    def __init__(self, fan: Dict[str, int], rules: List[tuple], start: str):
        self.fan = fan
        self.rules = rules
        self.start = start

    # -- structural checks ---------------------------------------------
    def check_good(self) -> List[str]:
        problems = []
        for (A, ch, tpl) in self.rules:
            if len(tpl) != self.fan[A]:
                problems.append(f"fan-out mismatch in {A}->{tpl}")
            seen = []
            for comp in tpl:
                if not comp or all(isinstance(it, str) and it == "" for it in comp):
                    problems.append(f"empty component (not lambda-free) in {A}")
                prev = None
                for it in comp:
                    if isinstance(it, tuple):
                        seen.append(it)
                        if prev is not None and prev[0] == it[0] and it[1] == prev[1] + 1:
                            problems.append(f"merging {A}: {prev}{it}")
                        prev = it
                    else:
                        if it != "":
                            prev = None
            need = [(j, k) for j, B in enumerate(ch) for k in range(self.fan[B])]
            if sorted(seen) != sorted(need):
                problems.append(f"deleting/nonlinear rule for {A}: {seen} vs {need}")
            for j in range(len(ch)):
                order = [k for (jj, k) in seen if jj == j]
                if order != sorted(order):
                    problems.append(f"permuting rule for {A}, child {j}")
        return problems

    def size(self) -> int:
        s = 0
        for (A, ch, tpl) in self.rules:
            s += 1 + len(ch)
            for comp in tpl:
                for it in comp:
                    s += len(it) if isinstance(it, str) else 1
        return s

    # -- evaluation (assumes acyclic dependency) -----------------------
    def topo(self) -> List[str]:
        deps = defaultdict(set)
        for (A, ch, _) in self.rules:
            deps[A] |= set(ch)
        order, state = [], {}

        def visit(A):
            if state.get(A) == 2:
                return
            if state.get(A) == 1:
                raise ValueError("cyclic grammar; finite evaluation not supported")
            state[A] = 1
            for B in deps[A]:
                visit(B)
            state[A] = 2
            order.append(A)

        for A in self.fan:
            visit(A)
        return order

    @staticmethod
    def apply(tpl, kids):
        out = []
        for comp in tpl:
            parts = []
            for it in comp:
                parts.append(it if isinstance(it, str) else kids[it[0]][it[1]])
            out.append("".join(parts))
        return tuple(out)

    def tuples(self, limit: int = 2_000_000) -> Dict[str, set]:
        from itertools import product
        T: Dict[str, set] = {A: set() for A in self.fan}
        for A in self.topo():
            for (B, ch, tpl) in self.rules:
                if B != A:
                    continue
                for kids in product(*[T[c] for c in ch]):
                    T[A].add(self.apply(tpl, kids))
                    if len(T[A]) > limit:
                        raise MemoryError("tuple language too large")
        return T

    def language(self, **kw) -> set:
        return {t[0] for t in self.tuples(**kw)[self.start]}

    # -- thickness (min successful sentence length using each rule) ----
    def thickness(self) -> Tuple[int, Dict[int, int]]:
        INF = float("inf")
        lam = {A: INF for A in self.fan}
        order = self.topo()
        for A in order:
            for (B, ch, tpl) in self.rules:
                if B == A:
                    c = sum(len(it) for comp in tpl for it in comp if isinstance(it, str))
                    lam[A] = min(lam[A], c + sum(lam[x] for x in ch))
        mu = {A: INF for A in self.fan}
        mu[self.start] = 0
        for A in reversed(order):
            if mu[A] == INF:
                continue
            for (B, ch, tpl) in self.rules:
                if B != A:
                    continue
                c = sum(len(it) for comp in tpl for it in comp if isinstance(it, str))
                for j, X in enumerate(ch):
                    val = mu[A] + c + sum(lam[Y] for i, Y in enumerate(ch) if i != j)
                    mu[X] = min(mu[X], val)
        th = {}
        for idx, (A, ch, tpl) in enumerate(self.rules):
            c = sum(len(it) for comp in tpl for it in comp if isinstance(it, str))
            th[idx] = mu[A] + c + sum(lam[x] for x in ch)
        return max(th.values()), th


def rare_type_profile(L: Iterable[str], h: Typing) -> Dict[object, int]:
    """For each realised type m, the minimum length of a word of type m."""
    best: Dict[object, int] = {}
    for w in L:
        t = h(w)
        if t not in best or len(w) < best[t]:
            best[t] = len(w)
    return best
```

### `revision/v79_candidate_families.py`

```python
#!/usr/bin/env python3
"""v79: candidate families for Open Problem op:fanout-two and their
exact finite (2,h)-substitutability tests.

Each candidate is a family of FINITE languages L_n generated by an acyclic
MCFG G_n of size O(n) (or O(n^2)); exactness of the finite check is
discussed in v79_lib.py.  A PASS at small n is NOT a theorem; a FAIL
prints an explicit violation which is independently re-verified.

Run:  python3 revision/v79_candidate_families.py
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from v79_lib import (MCFG, check_substitutable, content_typing,  # noqa: E402
                     minimize_violation, product_typing, rare_type_profile,
                     window_typing)

FLOOR, FCLOSE, CEIL, CCLOSE = "⌊", "⌋", "⌈", "⌉"


# ---------------------------------------------------------------------------
# P1  rigid bracket doubling (TCS #1 family) -- reference failure
# ---------------------------------------------------------------------------
def p1_bracket(n: int) -> MCFG:
    fan = {f"E{i}": 1 for i in range(n + 1)}
    rules = [("E0", [], (["a"],))]
    for i in range(1, n + 1):
        p = f"E{i-1}"
        rules.append((f"E{i}", [p, p], ([FLOOR, (0, 0), (1, 0), FCLOSE],)))
        rules.append((f"E{i}", [p], ([CEIL, (0, 0), CCLOSE],)))
    return MCFG(fan, rules, f"E{n}")


# ---------------------------------------------------------------------------
# P2  unary rare word + counter skeleton:  A_i -> A_{i-1}A_{i-1} | c d^i
#     rare (c-free) word a^(2^n); shortcut encodes the level in unary.
# ---------------------------------------------------------------------------
def p2_unary_counter(n: int) -> MCFG:
    fan = {f"A{i}": 1 for i in range(n + 1)}
    rules = [("A0", [], (["a"],))]
    for i in range(1, n + 1):
        p = f"A{i-1}"
        rules.append((f"A{i}", [p, p], ([(0, 0), (1, 0)],)))
        rules.append((f"A{i}", [], (["c" + "d" * i],)))
    return MCFG(fan, rules, f"A{n}")


# ---------------------------------------------------------------------------
# P3  free rare part: all words of {a,b}^(2^n) are rare (ceiling-free),
#     shortcut by ceiling brackets without floor brackets.
# ---------------------------------------------------------------------------
def p3_free_rare(n: int) -> MCFG:
    fan = {f"E{i}": 1 for i in range(n + 1)}
    rules = [("E0", [], (["a"],)), ("E0", [], (["b"],))]
    for i in range(1, n + 1):
        p = f"E{i-1}"
        rules.append((f"E{i}", [p, p], ([(0, 0), (1, 0)],)))
        rules.append((f"E{i}", [p], ([CEIL, (0, 0), CCLOSE],)))
    return MCFG(fan, rules, f"E{n}")


# ---------------------------------------------------------------------------
# P4  fan-out-two split design: B_i yields (leaf-letter sequence, a-run);
#     the a-run is a single block, leaves are c (pure) or d (shortcut).
#     S -> (x1 m x2) uses a separator m (nonmerging forbids x1 x2).
# ---------------------------------------------------------------------------
def p4_split(n: int) -> MCFG:
    fan = {f"B{i}": 2 for i in range(n + 1)}
    fan["S"] = 1
    rules = [("B0", [], (["c"], ["a"]))]
    for i in range(1, n + 1):
        p = f"B{i-1}"
        rules.append((f"B{i}", [p, p], ([(0, 0), (1, 0)], [(0, 1), (1, 1)])))
        rules.append((f"B{i}", [], (["d"], ["a"])))
    rules.append(("S", [f"B{n}"], ([(0, 0), "m", (0, 1)],)))
    return MCFG(fan, rules, "S")


# ---------------------------------------------------------------------------
# P5  synchronised fan-out-two brackets: the two halves of every node are
#     emitted into two components with distinct bracket alphabets and glued
#     at the root, so that internal separators are always cross-component.
# ---------------------------------------------------------------------------
def p5_sync_brackets(n: int) -> MCFG:
    fan = {f"E{i}": 2 for i in range(n + 1)}
    fan["S"] = 1
    rules = [("E0", [], (["a"], ["b"]))]
    for i in range(1, n + 1):
        p = f"E{i-1}"
        rules.append((f"E{i}", [p, p],
                      (["(", (0, 0), (1, 0)], [(1, 1), (0, 1), ")"])))
        rules.append((f"E{i}", [p], (["[", (0, 0)], [(0, 1), "]"])))
    rules.append(("S", [f"E{n}"], ([(0, 0), "#", (0, 1)],)))
    return MCFG(fan, rules, "S")


# ---------------------------------------------------------------------------
# P6  Thue-Morse rare word (overlap-free, so the power-transfer lemma does
#     not apply directly): X_i yields (T_i, Tbar_i), Y_i yields
#     (Tbar_i, T_i); root word T_n # Tbar_n.  Shortcuts wrap with c.
# ---------------------------------------------------------------------------
def p6_thue_morse(n: int) -> MCFG:
    fan = {}
    rules = []
    for i in range(n + 1):
        fan[f"X{i}"] = 2
        if i < n:
            fan[f"Y{i}"] = 2
    fan["S"] = 1
    rules += [("X0", [], (["a"], ["b"])), ("Y0", [], (["b"], ["a"]))]
    for i in range(1, n + 1):
        X, Y = f"X{i-1}", f"Y{i-1}"
        rules.append((f"X{i}", [X, Y], ([(0, 0), (1, 0)], [(0, 1), (1, 1)])))
        rules.append((f"X{i}", [X], (["c", (0, 0)], [(0, 1), "c"])))
        if i < n:   # Y_n would be unreachable; keep the grammar reduced
            rules.append((f"Y{i}", [Y, X], ([(0, 0), (1, 0)], [(0, 1), (1, 1)])))
            rules.append((f"Y{i}", [Y], (["c", (0, 0)], [(0, 1), "c"])))
    rules.append(("S", [f"X{n}"], ([(0, 0), "#", (0, 1)],)))
    return MCFG(fan, rules, "S")


FAMILIES = {
    "P1 rigid bracket doubling": (p1_bracket, CEIL + CCLOSE),
    "P2 unary rare + level counter": (p2_unary_counter, "cd"),
    "P3 free rare part {a,b}^(2^n)": (p3_free_rare, CEIL + CCLOSE),
    "P4 fan-out-2 split (single a-run)": (p4_split, "d"),
    "P5 synchronised fan-out-2 brackets": (p5_sync_brackets, "[]"),
    "P6 Thue-Morse rare word (overlap-free)": (p6_thue_morse, "c"),
}


def main(nmax: int = 3) -> None:
    for name, (fam, markers) in FAMILIES.items():
        print("=" * 72)
        print(name)
        hU = content_typing(markers, "U(" + markers + ")")
        typings = [hU, product_typing(window_typing(1, 1), hU)]
        for n in range(1, nmax + 1):
            G = fam(n)
            probs = G.check_good()
            L = G.language()
            th, _ = G.thickness()
            prof = rare_type_profile(L, hU)
            line = (f" n={n}: good={not probs} |G|={G.size()} theta={th} "
                    f"|L|={len(L)} min-len-by-U-type={sorted(prof.items(), key=str)}")
            print(line)
            if probs:
                print("   goodness problems:", probs[:3])
            for h in typings:
                t0 = time.time()
                ok, v, st = check_substitutable(L, h, 2)
                dt = time.time() - t0
                if ok:
                    print(f"   [{h.name}] PASS (exact, finite) in {dt:.1f}s")
                else:
                    minimize_violation(L, h, v)
                    print(f"   [{h.name}] FAIL d={v.d}: x={v.x} y={v.y}")
                    print(f"       shared={v.shared}  F={v.F}  "
                          f"F[x]∈L={v.accepts_x} F[y]∈L={v.accepts_y}")


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 3)
```

### `revision/v79_schema_search.py`

```python
#!/usr/bin/env python3
"""v79: exhaustive search over small "doubling + shortcut" schemas.

A schema fixes, for every level i>=1, two rules
    X_i -> tau(X_{i-1}, X_{i-1})      (doubling, terminals from {a,b})
    X_i -> sigma(X_{i-1})  or  X_i -> const   (shortcut, contains c)
with a base constant X_0 -> beta over {a,b}, fan-out d in {1,2}
(d=2: start S -> (x^1 t x^2), t in {a,b}).  Every grammar is good and
reduced, has size O(n) and ordinary thickness O(n); the unique c-free word
is the pure doubling yield, of length Theta(2^n).  Typing: h_U with
c |-> zeta (optionally times the (1,1)-window).

The question tested: is any such L_n (2,h)-tuple-substitutable for
n=1,2,3?  Exact finite check (see v79_lib).  Survivors would be
candidates for op:fanout-two and are printed.  This is a FINITE search; a
survivor at n<=3 proves nothing in general, and the absence of survivors
only rules out this schema space.

Run:  python3 revision/v79_schema_search.py [--window] [--d 1|2|both]
"""
from __future__ import annotations

import argparse
import itertools
import sys
from multiprocessing import Pool
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from v79_lib import (MCFG, check_substitutable, content_typing,  # noqa: E402
                     product_typing, window_typing)

LET = ["a", "b"]


def insert_letters(items, max_letters, alphabet, require=None):
    """Insert up to max_letters single letters into the gaps of `items`
    (a list of components, each a list of variable tuples)."""
    slots = []
    for ci, comp in enumerate(items):
        for p in range(len(comp) + 1):
            slots.append((ci, p))
    out = set()
    for k in range(0, max_letters + 1):
        for chosen in itertools.combinations_with_replacement(range(len(slots)), k):
            for letters in itertools.product(alphabet, repeat=k):
                if require and require not in letters:
                    continue
                comps = [list(c) for c in items]
                # insert from the back so indices stay valid
                ins = sorted(zip(chosen, letters), key=lambda t: (slots[t[0]][0], -slots[t[0]][1]))
                adds = {}
                for s, l in zip(chosen, letters):
                    adds.setdefault(slots[s], []).append(l)
                newc = []
                for ci, comp in enumerate(comps):
                    nc = []
                    for p in range(len(comp) + 1):
                        if (ci, p) in adds:
                            nc.append("".join(adds[(ci, p)]))
                        if p < len(comp):
                            nc.append(comp[p])
                    newc.append(tuple(nc))
                out.add(tuple(newc))
    return sorted(out, key=str)


def good_template(tpl, nchild, fan_child):
    g = MCFG({"A": len(tpl), **{f"B{j}": fan_child for j in range(nchild)}},
             [("A", [f"B{j}" for j in range(nchild)], tuple(list(c) for c in tpl))], "A")
    return not g.check_good()


def doubling_templates(d):
    vs = [(0, k) for k in range(d)] + [(1, k) for k in range(d)]
    res = set()
    for perm in itertools.permutations(vs):
        # nonpermuting order per child
        if [v for v in perm if v[0] == 0] != [(0, k) for k in range(d)]:
            continue
        if [v for v in perm if v[0] == 1] != [(1, k) for k in range(d)]:
            continue
        if d == 1:
            splits = [[list(perm)]]
        else:
            splits = [[list(perm[:s]), list(perm[s:])] for s in range(1, len(perm))]
        for comps in splits:
            for t in insert_letters(comps, 1, LET):
                if good_template(t, 2, d):
                    res.add(t)
    return sorted(res, key=str)


def shortcut_templates(d):
    res = set()
    comps = [[(0, k)] for k in range(d)]
    for t in insert_letters(comps, 2, ["a", "b", "c"], require="c"):
        if good_template(t, 1, d):
            res.add(("R1", t))
    consts = ["c", "ca", "ac", "cb", "bc", "cc"] if d == 1 else None
    if d == 1:
        for c in consts:
            res.add(("R0", ((c,),)))
    else:
        for c1 in ["c", "a", "b"]:
            for c2 in ["c", "a", "b"]:
                if "c" in c1 + c2:
                    res.add(("R0", ((c1,), (c2,))))
    return sorted(res, key=str)


def bases(d):
    if d == 1:
        return [(("a",),), (("b",),)][:1]
    return [(("a",), ("a",)), (("a",), ("b",))]


def build(d, base, dbl, sc, start_t, n):
    fan = {f"X{i}": d for i in range(n + 1)}
    rules = [("X0", [], tuple(list(c) for c in base))]
    for i in range(1, n + 1):
        p = f"X{i-1}"
        rules.append((f"X{i}", [p, p], tuple(list(c) for c in dbl)))
        kind, t = sc
        if kind == "R1":
            rules.append((f"X{i}", [p], tuple(list(c) for c in t)))
        else:
            rules.append((f"X{i}", [], tuple(list(c) for c in t)))
    if d == 1:
        return MCFG(fan, rules, f"X{n}")
    fan["S"] = 1
    rules.append(("S", [f"X{n}"], ([(0, 0), start_t, (0, 1)],)))
    return MCFG(fan, rules, "S")


H_U = content_typing("c", "hU")
H_WU = product_typing(window_typing(1, 1), H_U)


def test(args):
    d, base, dbl, sc, st, use_window, nmax = args
    h = H_WU if use_window else H_U
    for n in range(1, nmax + 1):
        G = build(d, base, dbl, sc, st, n)
        L = G.language()
        ok, v, _ = check_substitutable(L, h, 2, find_min=False)
        if not ok:
            return (args, n, v)
    return (args, None, None)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--window", action="store_true")
    ap.add_argument("--d", default="both")
    ap.add_argument("--nmax", type=int, default=3)
    a = ap.parse_args()
    ds = [1, 2] if a.d == "both" else [int(a.d)]
    jobs = []
    for d in ds:
        for base in bases(d):
            for dbl in doubling_templates(d):
                for sc in shortcut_templates(d):
                    for st in (["a", "b"] if d == 2 else [None]):
                        jobs.append((d, base, dbl, sc, st, a.window, a.nmax))
    print(f"schemas: {len(jobs)}  (window={a.window})", flush=True)
    fail_at = {}
    survivors = []
    with Pool(2) as pool:
        for i, (args, n, v) in enumerate(pool.imap_unordered(test, jobs, chunksize=8)):
            if n is None:
                survivors.append(args)
            else:
                fail_at[n] = fail_at.get(n, 0) + 1
            if (i + 1) % 500 == 0:
                print(f"  {i+1} done; fails by n={fail_at}; survivors={len(survivors)}", flush=True)
    print("failures by first failing n:", dict(sorted(fail_at.items())))
    print("survivors through n =", a.nmax, ":", len(survivors))
    for s in survivors[:50]:
        print("  SURVIVOR", s)


if __name__ == "__main__":
    main()
```

### `revision/v79_check_all_typing_obstruction.py`

```python
#!/usr/bin/env python3
"""v79: executable check of the explicit witnesses in
  * Lemma (power-transfer)   and
  * Theorem (no finite typing rescues the bracketed doubling family at
    fan-out two),
see revision/v79_fanout2_lower_bound_research.md, Sections 4.2-4.3.

For a finite typing h let g=h(floor) and let (i0,p) be the index and
period of g on POSITIVE powers: g^i = g^(i+p) for all i >= i0 >= 1.
Witness (s=r=i0, d=p, n=2*i0+p+2 or larger):
    x=(F^s, F^(d+r) a),  y=(F^(s+d), F^r a),
    E=(F, F, rest-after-first-a)      shared:  E[x]=E[y]=W_n,
    F-context: x1 kept at positions 1..s, x2 moved to the second half.
The script draws random transformation monoids (random DFAs) and checks
(i) componentwise equality of h-types, (ii) E[x]=E[y]=Fc[x]=W_n,
(iii) Fc[y] is ceiling-free and != W_n, hence not in L_n.
The proof is symbolic; this only tests the formula implementation.
"""
from __future__ import annotations

import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from v79_lib import transformation_typing  # noqa: E402

FL, FC, CL, CC = "⌊", "⌋", "⌈", "⌉"
ALPH = ["a", FL, FC, CL, CC]


def wstar(n: int) -> str:
    w = "a"
    for _ in range(n):
        w = FL + w + w + FC
    return w


def index_period(h, letter: str, bound: int = 400):
    vals = {}
    for i in range(1, bound):
        v = h(letter * i)
        if v in vals:
            i0 = vals[v]
            return i0, i - i0
        vals[v] = i
    raise RuntimeError("no period found")


def witness(n: int, s: int, d: int, r: int):
    assert n == s + d + r + 2
    W = wstar(n)
    first_a = W.index("a")
    assert first_a == n
    x = (FL * s, FL * (d + r) + "a")
    y = (FL * (s + d), FL * r + "a")
    E = (FL, FL, W[first_a + 1:])
    # second half W_{n-1} starts right after FL + W_{n-1}
    half = wstar(n - 1)
    start2 = 1 + len(half)
    assert W[start2:start2 + n] == FL * (n - 1) + "a"
    end_x2 = start2 + (n - 1) + 1          # position after the a
    beg_x2 = end_x2 - len(x[1])
    Fc = (FL, W[1 + s:beg_x2], W[end_x2:])
    return W, x, y, E, Fc


def fill(E, z):
    return E[0] + z[0] + E[1] + z[1] + E[2]


def check_typing(h, extra: int = 0) -> int:
    i0, p = index_period(h, FL)
    s = r = i0
    d = p
    n = s + d + r + 2 + extra
    r += extra
    W, x, y, E, Fc = witness(n, s, d, r)
    assert all(x) and all(y) and E[1] and Fc[1]
    assert tuple(h(c) for c in x) == tuple(h(c) for c in y), "types differ"
    assert fill(E, x) == W and fill(E, y) == W and fill(Fc, x) == W
    Fy = fill(Fc, y)
    assert Fy != W and CL not in Fy and CC not in Fy
    assert Fy.index("a") == n + d          # first floor-run lengthened by d
    return n


def main(trials: int = 3000, seed: int = 79) -> None:
    rnd = random.Random(seed)
    worst = 0
    for t in range(trials):
        k = rnd.randint(1, 5)
        maps = {c: tuple(rnd.randrange(k) for _ in range(k)) for c in ALPH}
        h = transformation_typing(k, maps, f"rand{t}")
        msize_bound = k ** k
        for extra in (0, 1, 3):
            n = check_typing(h, extra)
            worst = max(worst, n - extra)
            assert n - extra <= 2 * msize_bound + 3
    print(f"PASS: {trials} random typings (DFAs with <=5 states), "
          f"3 offsets each; largest threshold n used = {worst}.")


if __name__ == "__main__":
    main()
```


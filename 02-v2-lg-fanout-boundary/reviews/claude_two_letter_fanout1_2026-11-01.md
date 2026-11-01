# 二文字の内容型付け・ファンアウト1：群の語問題という障壁と、整列の強制

**調査日**：2026-11-01（Claude、別スレッド）
**対象**：`02-v2-lg-fanout-boundary/`（commit `2104e55` 時点の `main.tex`、`parked/parked_u1_typing_level.tex`、`reviews/chatgpt_two_letter_fanout1_2026-11-01.md`、`reviews/chatgpt_two_letter_fanout1_lower_2026-11-01.md`、`README.md` の Change log (48)(49)）
**問い**：Σ={a,b}、内容型付け c、ファンアウト1、ランク r≥2。全ての L∈C_{1,c} と全ての reduced good な表示 G について、作用素 B^{≤r}_{1,c} の特徴データの長さは ‖G‖ と θ̄_G の多項式で抑えられるか。

**結論（要約）**：本題は**未解決**のままである。ただし、問題の位置が一段はっきりした。

1. **無限の標的には、有限群の語問題が丸ごと入っている（定理A）。** 群への単項準同型 φ の原像 φ^{-1}(1)∖{ε} は、**全ての**型付けについて C_{1,s} に属し、純な語の最短の長さは φ(a) の位数に等しい。したがって本題を肯定で解く証明は、必ず「有限群の語問題を生成する文脈自由文法は、生成元の位数を ‖H‖ と θ̄_H の多項式で抑えるほど大きい」（§2 の**問題G**）の証明を含む。逆に問題G が否定なら、本題も `op:S1` も否定で解決し、`thm:two-letter-content` と合わせてファンアウトの分離が二文字で得られる。
2. このため、依頼文 §3 P1 の道具 (a)(c) と、§2 の項目 4〜7（有限性に依存する制約）は、**無限の標的に対しては単独では決着をつけられない**（§2.4）。有限の標的では障壁は働かず、有限の場合は別途未解決である。
3. **否定の向き**では、下界の族の設計が崩れる一般の仕組みを「整列の強制」として定式化し、二重化＋印の族（命題C.1）と三段の積（命題C.2）で、崩れる条件を証明付きで与えた。有限の全数検査では、試した全ての非退化な族がこの条件または別の違反で崩れる（観察）。
4. 肯定の部分結果は、純な部分の重い分岐が無い場合の多項式上界（命題B.2、代入可能性を使わない）にとどまる。

---

## 0. 主張ごとの判定

| # | 主張 | 判定 | 根拠 |
|---|---|---|---|
| 0 | 本題（B^{≤r}_{1,c} の特徴データが ‖G‖, θ̄ の多項式か） | **未解決** | §6 |
| A | 群 G への単項準同型 φ と g∈G について、φ^{-1}(g)∩Σ^+ は全ての型付け s で (1,s)-代入可能。G が有限なら C_{1,s} に属する | **証明済み** | §2.1 定理A(i) |
| A′ | G 有限、α=φ(a) の位数 N なら、L=φ^{-1}(1)∩Σ^+ の内容 {a} の最短語は a^N。B^{≤r}_{1,c}、B_{1,c}、B^{≤r}_{1,s_{U,2}}、B_{1,s_{U,2}}、およびクラス全体で特徴標本を持つ任意の集合駆動作用素の全ての特徴標本 F は ‖F‖_+ ≥ N+1 | **証明済み** | §2.1 定理A(ii)(iii) |
| A1 | 問題G が否定なら、本題は否定、`op:S1` も否定、s_{U,2} でファンアウト1と2が分離 | **証明済み（含意）** | §2.2 系A1 |
| A2 | 本題が肯定なら問題G は肯定 | **証明済み（含意）** | §2.2 系A2 |
| A3 | 無限の標的では、項目4〜7の結論は一般には成り立たず、h_a, h_b, ψ_λ の値の種類は全て無限になりうる。P1(a) の交換式はこの場合すべて矛盾なく成り立つ | **証明済み（具体例）** | §2.4 |
| A4 | 問題G の候補：G_n = Z/(2^n−1) ⋊ ⟨×2⟩ で a^{2^j} = b^{n−j} a b^j（長さ n+1）。語問題に小さい文法があるかは不明 | **候補の性質は証明済み／文法の存在は未解決** | §2.3 |
| B1 | 重い節点 u<v（互いに素）について、u だけ・v だけ・両方を差し替えた3語から得られる交換式（3本） | **証明済み** | §3.1 補題B.1 |
| B2 | 「二つの a-重い子を持つ規則が無い」（b も同様）なら t_typ(G,c) ≤ 3(r+1)|V|θ̄、両作用素に O_r(‖G‖²θ̄) の特徴データ | **証明済み（代入可能性不要）** | §3.2 命題B.2 |
| B3 | 重みの種類 k を使う上界（P1(c)）は、無限の標的では k=∞ となり空 | **証明済み** | §3.3 |
| C0 | 整列の強制：同じ型付き非終端の同じ内容の生成物は、導出に由来しない出現でも互いに置き換えられる | **証明済み（`lem:typed-homogeneity` の言い換え）** | §4.1 |
| C1 | 二重化＋印の族で、μ_{j+1} が混合なら a^{p2^j} μ_{j+1} a^{N−3p2^j} ∈ L_n が必要（1≤j≤n−2）。非退化で n≥4 なら j∈{1,2} のどちらかで必ず適用される | **証明済み** | §4.2 命題C.1・系C.1′ |
| C2 | 三段の積 (D∪{γ})^{M3}, D={a^k,β}^{M2}（M2≥3, M3≥2）で γ が混合なら a^kγa^{kM2(M3−1)−k} ∈ L が必要 | **証明済み** | §4.3 命題C.2 |
| C3 | 印の長さ ≤5（葉 a）・≤5（葉 aa）の非退化な二重化族は全て n=3 で C_{1,c} に入らない。μ_2 が混合の 5622 例は全て命題C.1 で説明される | **観察（有限の全数検査）** | §4.4、§7 |
| C4 | 三段の積 2423 例（k≤2, M2∈{3,4}, M3=2, |β|≤3, |γ|≤5）は全て不合格、うち 2190 例は命題C.2 で説明される | **観察（有限の全数検査）** | §4.4、§7 |
| V | 依頼文 §2 の項目 1〜9、README (49) の訂正 | **確認（項目6・7 に有限性の注記）** | §1 |
| L | 定理A・命題B.2・C.1・C.2 の文献上の新規性 | **未確認** | §8 |

上界はすべて B^{≤r_max}_{1,c} と B_{1,c} の両方についてで、定数は r_max だけに依存する（アルファベットは {a,b} に固定、|S^♯|=4）。

---

## 1. 既知事項の確認（依頼文 §2）

使う部分は自分で証明を追った。結論のみ記す。

- **項目1（混合の型は短い）**：確認。二つの標識（a と b の端末出現）を保つ導出で長さ・節点数を最小にし、骨格外を長さ ≤θ の生成物に替える（`lem:thickness-equivalence`(ii)）。骨格の各区間（共有幹、a 枝、b 枝）で (非終端, 標識集合) が繰り返せば祖先を子孫で置き換えられるので骨格は ≤3|V| 節点、各節点は ≤θ の端末（同 (i)）と ≤r 個の軽い子を持つ。上界 3(r+1)|V|θ̄。代入可能性は使わない。
- **項目2・3（出現数・重みの種類）**：確認。重い節点の反鎖を左から順に差し替えると b の個数（重み）が狭義単調に変わる。ψ_λ 版の λ 依存も原報告どおり。
- **項目4（純な語は一つ）**：確認。同じ文脈 (P,Q) に a^k, a^l (k<l) が入れば P a^{k+j(l−k)} Q ∈ L（全 j≥0）。**有限**の標的でのみ「一つ」。
- **項目5（反鎖）**：確認（有限の標的）。
- **項目6（一か所だけの違いの禁止）**：確認。ただし**有限の標的が必要**で、依頼文ではこの条件が落ちている。無限の反例：φ(a)=1, φ(b)=0 ∈ Z/2 の原像 L={w : |w|_a 偶数} は C_{1,c} に属し（定理A）、aab と aaaab は b の個数が同じで a の塊の並びが (2,0) と (4,0)。
- **項目7（層の端）**：確認。b の個数の最大・最小が存在すること（有限、または b の個数が有界）が必要。
- **項目8**：ChatGPT の2本のスクリプトの結論と整合する（§4.4 でさらに広い範囲を全数検査した）。
- **項目9**：確認（aabaaaa ∈ {aa,b}^4、aaabaaa ∉）。
- **README (49) の訂正**：確認。W, T ∈ K_3 は K_n の語の同じ位置に入るので φ(W), φ(T) は φ(K_n) で文脈を共有し、φ(W) は φ(T) の真の因子なので補題1.1 が適用できる。

---

## 2. 群の語問題という障壁

### 2.1 定理A

φ: Σ^* → G を群（有限でも無限でもよい）への単項準同型、g∈G とし、L_{φ,g} := φ^{-1}(g) ∩ Σ^+ とおく。

**定理A.**
(i) 全ての型付け s について、L_{φ,g} は (1,s)-代入可能である。G が有限なら L_{φ,g} は正則なので、L_{φ,g} ∈ C_{1,s}。
(ii) G が有限、g=1、α:=φ(a) の位数を N とすると、a^k ∈ L_{φ,1} ⇔ N | k。従って μ_{\{a\}}(L_{φ,1}) = N（内容型付け c）、s_{U,2} では型 1 の最短語の長さが N。
(iii) (ii) の L について、B^{≤r}_{1,c}（r≥1）、B_{1,c}、B^{≤r}_{1,s_{U,2}}、B_{1,s_{U,2}}、および C_{1,c}（または C_{1,s_{U,2}}）全体で特徴標本を持つ任意の集合駆動作用素について、L の全ての特徴標本 F は ‖F‖_+ ≥ N+1。

*証明.* (i) x, y が文脈 (u,v) を共有すれば φ(u)φ(x)φ(v) = g = φ(u)φ(y)φ(v)、群なので φ(x)=φ(y)。すると任意の (p,q) で φ(pxq)=φ(pyq) となり分布が一致する。型の一致は使っていないので、全ての s で成り立つ（自明型付けでも）。有限群の原像は正則、従って文脈自由。(ii) 明らか。(iii) `prop:rare-type` を型 {a}（s_{U,2} では型 1）に適用する。□

**注意.** (a) 同じ L は自明型付けでも代入可能なので、自明型付けの特徴データは Yoshinaka の評価 |P|θ_G で多項式である。内容型付けの下界はもっぱら「純な語 a^N が必要」から来る。(b) ファンアウト2 では、二つの成分の寄与を非可換群で分離できないので、L_{φ,1} は一般に C_{2,c} に属さない。`thm:two-letter-content` とは矛盾しない。

### 2.2 問題G と二つの含意

**問題G.** r≥2 を固定する。有限群 G と全射な単項準同型 φ: {a,b}^* → G、および L_{φ,1} の reduced good なランク ≤r の文脈自由文法 H の全てについて、ord(φ(a)) ≤ p(‖H‖, θ̄_H) となる多項式 p は存在するか。

**系A1（問題G が否定なら）.** 族 (G_n, φ_n, H_n) で ‖H_n‖, θ̄_{H_n} が n の多項式、ord(φ_n(a)) が超多項式なら、定理A(iii) により B^{≤r}_{1,c} と B^{≤r}_{1,s_{U,2}} の特徴データは超多項式。特に `op:S1` は否定で、`cor:two-letter-semilattice`（ファンアウト2 で多項式）と合わせて、同じ型付け s_{U,2} がファンアウト1では超多項式・ファンアウト2では多項式になる。□

**系A2（本題が肯定なら）.** 本題の肯定（多項式 p_c の存在）は、L_{φ,1} ∈ C_{1,c} と定理A(iii) により ord(φ(a)) ≤ ‖F‖_+ ≤ p_c(‖H‖, θ̄_H) を与える。従って問題G は肯定。□

すなわち、**本題の肯定の証明は、有限群の語問題の文脈自由文法による表示についての下界の証明を含まなければならない**。

### 2.3 群がどんな性質を持てば反例になりうるか

L=L_{φ,1}、H をその reduced good な表示とする。

- **各非終端は一つの値を持つ.** 非終端 X の生成物は全て文脈 E_X を共有するので、定理A(i) の証明と同じく φ の値が一つに決まる（g_X と書く）。
- **重い節点の値は短い語で書ける必要がある.** a^N の節点数最小の最短導出で、重い節点 u（ラベル B）の値 α^{n_B} は、B の長さ ≤θ̄ の生成物 ω_B でも実現される。従って α の多数のべき α^{n} が {a,b} 上の長さ ≤θ̄ の**正の**語で書けなければならない。G が可換で生成元が二つなら、値は Parikh ベクトルにしか依らず、短い語の値は高々 (θ̄+1)^2 個なので、これはおそらく二次の障害（`prop:binary-u1-weight-slice` と同種）になる。可換の場合の多項式上界は本報告では**証明していない**。
- **候補.** n≥2、N_n := 2^n − 1、G_n := Z/N_n ⋊ Z/n をアフィン写像の群とし、a ↦ (x ↦ x+1)、b ↦ (x ↦ 2x)（語は左から順に作用）とする。b^n = 1 で α の位数は N_n = 2^n−1、そして

  a^{2^j} = b^{n−j} a b^{j}（G_n の中で、0≤j<n）

  が成り立つ（x ↦ 2^{n−j}x ↦ 2^{n−j}x+1 ↦ 2^n x + 2^j ≡ x + 2^j）。§7 のスクリプトの最後の部分で n=2..8 について数値確認した（これは群の等式の検算で、証明は上の一行）。従って二重化の各段の値は長さ n+1 の語で書ける。**L_{φ,1} が ‖H‖, θ̄_H = n^{O(1)} の文法を持つかは分からない**。持てば系A1 により本題は否定で決着する。
- 無限群に広げても状況は変わらない：群の原像が文脈自由なのは（対称な生成系の語問題について）仮想自由群に限られ（Muller–Schupp）、α が大きい位数を持つなら α を含む大きい有限部分群が要る。

### 2.4 証明の方針への帰結

L_{φ,1}（G 有限、α の位数 N、混合の語を含む）では次が成り立つ。

1. 純な a の語は a^N, a^{2N}, … と無限にあり、項目4〜6 の「有限なら」の結論は成り立たない（§1 の例）。
2. 混合の語 w があれば w b^{M}（M = ord φ(b)）も L に入るので h_b = ∞、同様に h_a = ∞（w a^N）。任意の λ>0 で ψ_λ の値も無限種類。従って項目2・3 と P1(c) の上界は空になる。
3. §3.1 の交換式（P1(a) の三語の議論）は全て成り立ち、矛盾を生まない（L が代入可能で、交換式は L の真の性質だから）。

よって、**無限の標的まで含めた肯定の証明は、代入可能性と導出木の局所的な交換だけでは完結しない**。どこかで「H が L の**全ての**語を生成する」という完全性を、問題G の形で使う必要がある。依頼文 P1(b) の「まず有限の標的で」は、この障壁を避けるという意味で筋がよいが、有限の場合の結果は無限の場合を含意しない。

---

## 3. 肯定の向き（P1）

以下 G は reduced good、ファンアウト1、ランク ≤r、θ := θ̄_G、L(G)=L∩Σ^+、L∈C_{1,c}。A は純な a の生成物を持つ非終端、E_A=(P,Q) はその導出に由来する文脈（`lem:thickness-equivalence`(iv)、|PQ| ≤ θ）、a^N は A の最短の純な a の生成物、T はその節点数最小の導出。T の各節点 u（ラベル B_u）の生成物 a^{n_u} は B_u の最短の純な a の生成物である（そうでなければ部分木を替えて短くできる）。n_u > θ の節点を**重い**と呼び、ω_B を B の長さ ≤θ の生成物とする（重い B では ω_B は b を含む）。

### 3.1 補題B.1（二つの重い節点の交換式）

u が v より左にある互いに素な重い節点で、ラベル B, C、T の生成物を a^N = a^x · a^{n_B} · a^g · a^{n_C} · a^z と分けたとする（間の a^g には他の部分木の生成物も含まれてよい）。次の3語は全て L に入る：

- W_u = P a^x ω_B a^{g+n_C+z} Q、W_v = P a^{x+n_B+g} ω_C a^z Q、W_{uv} = P a^x ω_B a^g ω_C a^z Q。

このとき（≡ は分布の一致）

1. a^x ω_B a^{g+n_C} ≡ a^{x+n_B+g} ω_C（文脈 (P, a^z Q) を共有、どちらも内容 {a,b}）；
2. ω_B a^g ω_C が a を含むなら、ω_B a^{g+n_C} ≡ ω_B a^g ω_C ≡ a^{n_B+g} ω_C（文脈 (P a^x, a^z Q) を共有）。

*証明.* W_u, W_v, W_{uv} は T の部分木を同じ非終端の生成物に替えたものに E_A をかぶせたものなので L に入る。示した因子の組は示した文脈を共有し、内容が等しいので C_{1,c} の定義から分布が等しい。□

**評価.** これが依頼文 P1(a) の「三つの語がどの文脈を共有するか」の答えである。しかし得られる置き換えは全て、T の部分木を差し替えた語の族 {W_S} の中で閉じている（ω を純な a の塊の上で滑らせるだけ）。矛盾を得るには、左辺がこの族の**外の位置**に現れる必要がある（§4 の整列の強制）。そして群の原像では、そうした位置でも置き換えが成り立ってしまう（§2.4）。この補題だけでは重い節点の反鎖の幅を抑えられない。

### 3.2 命題B.2（重い分岐が無い場合）

非終端 B が純な a の生成物を持ち、その最短のものの長さが θ より大きいとき、B を **a-重い** と呼ぶ（b も同様）。

**命題B.2.** G のどの規則も、a-重い非終端の子の出現を二つ以上持たないとする（同じ非終端の二回の出現も二つと数える）。b についても同様とする。このとき（代入可能性を使わずに）

- 純な a、純な b の型付き非終端は長さ ≤ (r+1)|V|θ の生成物を持ち、t_typ(G,c) ≤ 3(r+1)|V|θ；
- L∈C_{1,c} なら、B^{≤r_max}_{1,c} と B_{1,c} の共通の特徴標本 K で
  ‖K‖_+ ≤ 4^{r_max}‖G‖ (1 + 2θ + 3r_max(r_max+1)|V|θ) + 1_{\{ε∈L\}}。
- L ∈ C_{1,s_{U,2}} なら同じ K が B^{≤r_max}_{1,s_{U,2}}, B_{1,s_{U,2}} の特徴標本（`lem:typing-monotone`）。

*証明.* T で u が重い ⇔ B_u が a-重い（上の注意）。仮定から各節点の重い子は高々一つなので、重い節点は根からの一本の鎖をなし、鎖の上でラベルは繰り返さない（繰り返せば祖先を子孫で置き換えて節点数が減る）ので ≤|V| 個。根が軽ければ N ≤ θ。重ければ a^N の各文字は、重い節点が直接書くか（規則ごとに ≤θ、`lem:thickness-equivalence`(i)）、重い節点の軽い子（≤r 個、各 ≤θ）にある。よって N ≤ |V|(r+1)θ。純な a の型付き非終端 A_{(\{a\})} の生成物は A の純な a の生成物全体なので、t_typ への寄与はこの N。b も同様、混合は項目1。最後の評価は `thm:data-from-typed-thickness` に N_typ ≤ |S^♯|^{r_max}‖G‖ = 4^{r_max}‖G‖ を入れたもの。□

これは依頼文 P1(d) の「純な部分文法が線形なら」を少し広げたものにすぎず、二重化（L_{m,n} の自然な表示を含む）を除外する。弱い結果である。

### 3.3 重みの種類（P1(c)）について

λ を文法から選んでも、無限の標的では §2.4(2) により k=∞ となりうるので、ChatGPT 定理5 の形の上界は一般には何も与えない。有限の標的に限れば k は有限だが、k を ‖G‖, θ̄ で抑える方法は見つからなかった。

### 3.4 有限の標的について（止まった場所）

有限の標的では群の障壁は働かない（群の原像は空でなければ無限）。項目4〜7 と補題B.1 が使えるが、補題B.1 の評価で述べた理由で、重い節点の反鎖の幅を抑える議論には至らなかった。有限の標的に限った本題は**未解決**。

---

## 4. 否定の向き（P2）：整列の強制

### 4.1 原理

**補題C.0.** L∈C_{1,c}、G を L∩Σ^+ の reduced good な表示とする。非終端 X の生成物 y, z が同じ内容なら、**任意の** U, V について U y V ∈ L ⇔ U z V ∈ L。

*証明.* y, z は E_X を共有するので分布が等しい（`lem:typed-homogeneity`）。□

U y V は X の導出に由来する出現である必要がない。下界の族の設計では、上の段の単位の混合の生成物が「下の段の幅だけずれた位置」に因子として現れると、そこに同じ単位の別の生成物（上の段の印）を置いた語が L に入らねばならない。これが積や二重化を重ねた族が崩れる一般の仕組みで、言い換えると、段の構造が語の上で見えてはならない。群の原像はちょうどこの「全てのずれで置き換えが成り立つ」言語であり、§2 と §4 は同じ現象の裏表である。

### 4.2 命題C.1（二重化＋印の族）

p≥1、n≥1、b を含む語 μ_1,…,μ_n について G_n を
  E_0 → a^p、E_i → E_{i−1}E_{i−1} | μ_i（1≤i≤n）、開始記号 E_n
とし、L_n := L(G_n)、N := p·2^n とする（有限で、唯一の純な語は a^N）。

**命題C.1.** 1 ≤ j ≤ n−2 とし、μ_{j+1} が内容 {a,b} を持つとする。L_n ∈ C_{1,c} なら
  a^{p2^j} μ_{j+1} a^{N − 3p2^j} ∈ L_n。
従ってこの語が L_n に入らなければ、L_n ∉ C_{1,c}、かつ L_n ∉ C_{1,s_{U,2}}。

*証明.* E_{j+1} の生成物 y := a^{p2^j} μ_j（左の子は純、右の子は μ_j）と μ_{j+1} は、文脈 (ε, a^{N − p2^{j+1}})（段 j+1 の位置0 に E_{j+1}、他は全て純）を共有し、どちらも内容 {a,b}。よって y ≡ μ_{j+1}。一方、段 j の位置2（n ≥ j+2 なので存在する）だけを μ_j にした語 W = a^{2p2^j} μ_j a^{N − 3p2^j} ∈ L_n は W = a^{p2^j} · y · a^{N−3p2^j} と書けるので、補題C.0 で y を μ_{j+1} に替えた語が L_n に入る。内容が等しい因子は s_{U,2} の型も等しいので、c での違反は s_{U,2} での違反でもある。□

**系C.1′.** 非退化（全ての i で μ_i ∉ E_{i−1}E_{i−1} の生成物）なら、μ_i と μ_{i+1} がともに純な b であることは無い。従って n ≥ 4 なら j ∈ {1,2} のどちらかで命題C.1 の仮定が成り立ち、L_n ∈ C_{1,c} は「段 j+1 の印が、段 j の幅の奇数倍の位置に現れた語」a^{p2^j}μ_{j+1}a^{N−3p2^j} を含むことを要求する。

*証明.* μ_i, μ_{i+1} が純な b なら、μ_iμ_i と μ_{i+1} はともに E_{i+1} の純な b の生成物で、文脈を共有する。有限なので項目4 により μ_{i+1} = μ_iμ_i ∈ E_iE_i で退化。μ_2 が純なら μ_3 は混合。□

例（§7 Part E）：p=1、μ=(b, aba, bb)、n=3。y = aab と μ_2 = aba は文脈 (ε, aaaa) を共有、W = aaaabaa = aa·aab·aa ∈ L_3 だが aa·aba·aa = aaabaaa ∉ L_3。

### 4.3 命題C.2（三段の積）

k≥1、M2≥3、M3≥2、b を含む β, γ について D := {a^k, β}^{M2}、L := (D ∪ {γ})^{M3}（有限で文脈自由、唯一の純な語は a^{kM2M3}）。

**命題C.2.** γ が内容 {a,b} を持ち L ∈ C_{1,c} なら a^k γ a^{kM2(M3−1) − k} ∈ L。従ってこの語が L に入らなければ L ∉ C_{1,c}（かつ ∉ C_{1,s_{U,2}}）。

*証明.* y := a^kβa^{k(M2−2)} ∈ D は混合で、y·a^{kM2(M3−1)} と γ·a^{kM2(M3−1)} はともに L に入るので y ≡ γ。W := a^{2k}βa^{k(M2−3)} · a^{kM2(M3−1)} ∈ L（M2≥3）は W = a^k · y · a^{kM2(M3−1)−k}。補題C.0 と同じ置き換えで結論。□

γ が純な b のときは、β も純な b なら β^{M2} と γ が D∪{γ} の純な b の生成物として文脈を共有し、有限性から γ = β^{M2} ∈ D（退化）。β が混合で γ が純な b の場合はこの命題の範囲外で、有限の検査では全て別の違反で崩れた（観察）。

**多段化の一般の形.** L_{m,n} = {a^{2^m}, b}^{2^n} が通るのは、段が一つで、所属が「a の塊の長さが 2^m の倍数」と一定の重み ψ だけで決まり、ずれた置き換えが全て許されるからである（`prop:binary-u1-quadratic` の証明）。二段目を重ねると、命題C.2 のように上の段の印を下の段の幅だけずらした語が強制され、段の境界が語から読めなくなる。段の境界を見えなくしたまま長い純な語を保つ言語は、可換な重みでは二次で止まる（`prop:u1-weight-all-fanout`）ので、非可換な不変量（§2 の群）が必要になる。これは設計の指針としての解釈で、一般の定理としては主張しない。

### 4.4 有限の全数検査（観察）

§7 のスクリプトの結果：

| 族 | 範囲 | n=1 合格 | n=2 合格 | n=3 合格 | 命題で説明 |
|---|---|---:|---:|---:|---|
| 二重化＋印、葉 a | 非退化、|μ_i| ≤ 4 | 26 | 52 | **0** | μ_2 混合の 408 例は全て C.1、残り 918 例は μ_2 が純な b |
| 二重化＋印、葉 a | 非退化、|μ_i| ≤ 5 | 57 | 195 | **0** | μ_2 混合の 5622 例は全て C.1、残り 5327 例は μ_2 が純な b |
| 二重化＋印、葉 aa | 非退化、|μ_i| ≤ 5 | 57 | 660 | **0** | （内訳は数えていない） |
| 三段の積 | k∈{1,2}, M2∈{3,4}, M3=2, |β|≤3, |γ|≤5, γ∉D | — | — | 2423 中 **0** | 2190 例は C.2 |

これらは有限の範囲の観察であり、範囲外の族の不可能性は主張しない。ただし、個々の不合格は有限言語の全数検査による証明である。

---

## 5. s_{U,2} との関係（P3）

- 命題B.2 の上界は、L ∈ C_{1,s_{U,2}} ⊆ C_{1,c} なら `lem:typing-monotone` により s_{U,2} の両作用素に移る（向き：c で特徴標本なら s_{U,2} でも特徴標本）。
- 定理A の言語は全ての型付けで代入可能なので、C_{1,s_{U,2}} にも入る。問題G の否定の族は、そのまま `op:S1` の否定解決とファンアウトの分離を与える（系A1）。この点で、群の原像は ChatGPT 報告で問題になった「c にしか属さない族」の心配が無い。
- 命題C.1・C.2 の違反は内容の等しい因子の組なので、s_{U,2} でも違反である。

---

## 6. 結論と止まった場所

**どこまで言えたか.**

1. 二文字・ファンアウト1 の本題（B^{≤r}_{1,c}、r≥2）は肯定・否定とも**未解決**。
2. 無限の標的では、本題は問題G（有限群の語問題の文脈自由文法による表示で、生成元 a の位数が文法の大きさと厚さの多項式で抑えられるか）を含む。本題の肯定 ⇒ 問題G の肯定（系A2）。問題G の否定 ⇒ 本題の否定、`op:S1` の否定、s_{U,2} でのファンアウト分離（系A1）。
3. 肯定の部分結果は命題B.2（重い分岐が無い場合、O_{r_max}(‖G‖²θ̄)、両作用素、代入可能性不要）のみ。
4. 否定の向きでは、二重化と多段の積が崩れる一般の仕組み（整列の強制、補題C.0）を与え、二つの典型的な設計で崩れる条件を証明した（命題C.1・C.2、系C.1′）。

**止まった場所（正確に）.**

- (S1) 問題G。候補 G_n = Z/(2^n−1) ⋊ ⟨×2⟩ は「二重化の各段の値が長さ n+1 の語で書ける」という必要条件（§2.3）を満たすが、L_{φ,1} の文法が ‖H‖, θ̄_H = n^{O(1)} で書けるかは分からない。素朴な「各値 g ∈ V について値 g の語を全て生成する非終端」では、V を2のべきに限るとランクが有界にならない（各 a の寄与 2^{(後ろの b の個数) mod n} の列が 1,2,4,…,2^k,1 なら和は 2^{k+1} だが、連続する部分に分けて各部分の和を2のべきにする方法は全て一つずつに分けるものしかなく、k+2 個の部分が要る）。V を広げてどこまで小さくできるかが未検討。
- (S2) 有限の標的。障壁は無いが、補題B.1 の交換式は差し替えの族の中で閉じており、重い節点の反鎖の幅を抑えるには、族の外の位置への置き換え（§4 の整列の強制）を、任意の文法について引き出す方法が要る。それが見つかっていない。

**次に試す価値があるもの.** (i) 問題G の文献調査（有限群の語問題の文法の大きさ）と、上の候補についての小さい n での文法の探索；(ii) 二元生成の可換群について問題G の肯定を証明すること（Parikh 格子による二次の評価が期待される）；(iii) 有限の標的に限った肯定の証明。

---

## 7. 検証スクリプト（Python 3 標準ライブラリのみ）

ファイル名 `claude_two_letter_fanout1_check.py`。Windows では `py -3 claude_two_letter_fanout1_check.py`（引数 5 で印の長さ ≤5、約30秒）。有限言語の代入可能性の判定は定義どおりの全数検査で、返す証人（x, y, 共有文脈, 分離文脈）はそれ自体が証明になる。

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Two letters, content typing, fan-out one: exact finite checks.

Python 3 standard library only.  Windows:  py -3 claude_two_letter_fanout1_check.py [M]
M = maximal marker length in Part C (default 4; M=5 takes about 10 s more).

For a FINITE language L the test below is the definition of
(1,s)-substitutability: for every pair of nonempty factors x,y of words of L
with s(x)=s(y) and a common one-hole context, their context sets in L must be
equal.  A returned witness (x, y, shared context, separating context) is a
complete, independently checkable proof of non-membership.
"""
import itertools
import sys
from collections import defaultdict


def content(w):
    return ('a' in w, 'b' in w)


def u1(w):
    return 'b' in w


def contexts(L):
    D = defaultdict(set)
    for w in L:
        n = len(w)
        for i in range(n):
            for j in range(i + 1, n + 1):
                D[w[i:j]].add((w[:i], w[j:]))
    return D


def check(L, typing=content):
    """None if L is (1,typing)-substitutable, else a witness."""
    D = contexts(set(L))
    first = {}                      # (context, type) -> first factor seen
    for x in sorted(D, key=lambda z: (len(z), z)):
        t = typing(x)
        for c in D[x]:
            y = first.setdefault((c, t), x)
            if y != x and D[x] != D[y]:
                sep = min(D[x] ^ D[y], key=lambda q: (len(q[0]) + len(q[1]), q))
                return (x, y, c, sep, 'x' if sep in D[x] else 'y')
    return None


def concat(A, B):
    return {x + y for x in A for y in B}


def seqs(units, k):
    S = {''}
    for _ in range(k):
        S = concat(S, units)
    return S


def b_words(lo, hi):
    for n in range(lo, hi + 1):
        for t in itertools.product('ab', repeat=n):
            w = ''.join(t)
            if 'b' in w:
                yield w


def show(name, L):
    for tn, ty in (('content c', content), ('s_U2', u1)):
        r = check(L, ty)
        print('  %-28s %-10s %s' % (name, tn, 'PASS' if r is None else 'FAIL ' + repr(r)))


def part_b():
    print('Part B: sanity checks')
    show('{b,ab}', {'b', 'ab'})
    show('L_{1,2}={aa,b}^4', seqs({'aa', 'b'}, 4))


def part_c(M):
    """E_0 -> a, E_i -> E_{i-1}E_{i-1} | mu_i, nondegenerate (mu_i not in E_{i-1}E_{i-1})."""
    print('Part C: doubling with markers, markers of length <= %d containing b' % M)
    ws = list(b_words(1, M))
    level = [({'a'}, ())]
    for n in (1, 2, 3):
        new = []
        crit = mu_pure = 0
        for E, mus in level:
            EE = concat(E, E)
            for mu in ws:
                if mu in EE:
                    continue
                L = EE | {mu}
                ok = check(L) is None
                if n == 3:
                    # criterion of Proposition C.1 with j = 1 (N = 8)
                    if 'a' in mus[1] and 'aa' + mus[1] + 'aa' not in L:
                        crit += 1
                        assert not ok, 'criterion contradicted'
                    elif 'a' not in mus[1]:
                        mu_pure += 1
                if ok:
                    new.append((L, mus + (mu,)))
        print('  n=%d: tested families passing for content c: %d' % (n, len(new)))
        if n == 3:
            print('  n=3: failures explained by Prop. C.1 (mu_2 mixed): %d;'
                  ' failures with mu_2 pure b: %d' % (crit, mu_pure))
        level = new
        if not new:
            break


def part_d():
    """Three-level products (D | gamma)^M3, D = {a^k, beta}^M2."""
    print('Part D: three-level products')
    tot = passed = crit = 0
    for k in (1, 2):
        for M2 in (3, 4):
            M3 = 2
            for beta in b_words(1, 3):
                D = seqs({'a' * k, beta}, M2)
                for gamma in b_words(1, 5):
                    if gamma in D:
                        continue
                    L = seqs(D | {gamma}, M3)
                    tot += 1
                    ok = check(L) is None
                    passed += ok
                    forced = 'a' * k + gamma + 'a' * (k * M2 * (M3 - 1) - k)
                    if 'a' in gamma and forced not in L:
                        crit += 1
                        assert not ok, 'criterion contradicted'
    print('  tested %d, passing %d, excluded by Prop. C.2: %d' % (tot, passed, crit))


def part_e():
    print('Part E: an explicit instance of Proposition C.1 (n=3, mu=(b,aba,bb))')
    E = {'a'}
    for mu in ('b', 'aba', 'bb'):
        E = concat(E, E) | {mu}
    y1, z = 'aab', 'aba'                  # a^2 mu_1 and mu_2, both yields of E_2
    W2 = 'aaaa' + 'b' + 'aa'              # mu_1 at level-1 slot 2
    forced = 'aa' + 'aba' + 'aa'
    print('  common context of y1,z:', ('', 'aaaa'), ('' + y1 + 'aaaa') in E, (z + 'aaaa') in E)
    print('  W2 in L:', W2 in E, ' W2 = aa + y1 + aa:', W2 == 'aa' + y1 + 'aa')
    print('  forced word', forced, 'in L:', forced in E, ' -> violation')


if __name__ == '__main__':
    M = int(sys.argv[1]) if len(sys.argv) > 1 else 4
    part_b()
    part_c(M)
    part_d()
    part_e()
```

実行結果（既定 M=4）：

```text
Part B: sanity checks
  {b,ab}                       content c  PASS
  {b,ab}                       s_U2       FAIL ('ab', 'b', ('', ''), ('a', ''), 'y')
  L_{1,2}={aa,b}^4             content c  PASS
  L_{1,2}={aa,b}^4             s_U2       PASS
Part C: doubling with markers, markers of length <= 4 containing b
  n=1: tested families passing for content c: 26
  n=2: tested families passing for content c: 52
  n=3: tested families passing for content c: 0
  n=3: failures explained by Prop. C.1 (mu_2 mixed): 408; failures with mu_2 pure b: 918
Part D: three-level products
  tested 2423, passing 0, excluded by Prop. C.2: 2190
Part E: an explicit instance of Proposition C.1 (n=3, mu=(b,aba,bb))
  common context of y1,z: ('', 'aaaa') True True
  W2 in L: True  W2 = aa + y1 + aa: True
  forced word aaabaaa in L: False  -> violation
```

引数 5 では Part C が `n=1: 57`、`n=2: 195`、`n=3: 0`、`explained by Prop. C.1: 5622; mu_2 pure b: 5327`。葉を aa にした変種（同じ判定関数、葉だけ変更）は `n=1: 57`、`n=2: 660`、`n=3: 0` だった（このスクリプトには含めていない。Part C の `{'a'}` を `{'aa'}` に替えれば再現できる）。

§2.3 の等式 a^{2^j} = b^{n−j}ab^j の検算（n=2..8）は次の数行で行った：

```python
for n in range(2, 9):
    N = 2**n - 1
    def val(w):                      # affine map x -> m x + c, letters applied left to right
        m, c = 1, 0
        for ch in w:
            if ch == 'a': c = (c + 1) % N
            else: m, c = (2*m) % N, (2*c) % N
        return m, c
    print(n, all(val('b'*(n-j) + 'a' + 'b'*j) == val('a'*2**j) for j in range(n)), val('a'*N))
```

全て `True`、`val('a'*N) = (1, 0)`。

---

## 8. 文献と新規性

- 原稿 `main.tex`：`def:class-cmcf`、`lem:typed-homogeneity`、`lem:thickness-equivalence`、`lem:witness-length-template`、`thm:data-from-typed-thickness`、`prop:rare-type`、`cor:distribution-representatives`、`lem:typing-monotone`、`thm:two-letter-content`、`cor:two-letter-semilattice`、`op:S1`。parked：`prop:binary-u1-quadratic`、`prop:binary-u1-weight-slice`、`prop:u1-weight-all-fanout`。
- A. Clark, R. Eyraud, Polynomial identification in the limit of substitutable context-free languages, JMLR 8 (2007) 1725–1745（一穴の代入可能性）。
- D. E. Muller, P. E. Schupp, Groups, the theory of ends, and context-free languages, J. Comput. System Sci. 26 (1983) 295–310（§2.3 の注意で、文脈自由な語問題を持つ群が仮想自由群であることに言及した）。
- 群の原像が代入可能であること（定理A(i)）は一行で示せる事実で、文献に既にある可能性が高いが、出典は**未確認**。問題G（有限群の語問題の文脈自由文法の大きさと元の位数の関係）が既知かどうかも**未確認**。命題B.2・C.1・C.2 の新規性も**未確認**。

他の報告への訂正：依頼文 §2 の項目6・7 は有限の標的（または b の個数が有界）を必要とする（§1）。ChatGPT 報告の主張に誤りは見つからなかった。

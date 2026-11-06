# 「外側の c」：最短 `ab` 語の文法文脈、侵入反鎖、c-個数スペクトル

**研究日**：2026-11-06　**対象**：栗山論文 #2 / `op:fanout-two`　**結論**：問題全体は未解決。

**判定規則**：各定理・補題・命題を **[証明済み]**、**[条件付き（仮定明記）]**、**[予想]**、**[計算機による観察（範囲明記）]** で分類する。既報の再提示は新成果に算入しない。本文中の「新しい」は、今回の報告で得た定式化・証明という意味に限り、文献上の先取権・新規性を主張しない。

## 0. 参照資料・再現条件

以下を GitHub 接続で直接取得して照合した（`growupkuriyama-hub/Papers`, default branch）。

- [59頁凍結原稿](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/parked/2026-11-06_focus/main_before_focus_59pp.tex)（blob `1bc97358a49b4e80eef96abb0eee6de4ca10eecf`）：`def:standard-mcfg`、`def:grammar-properties`、`def:class-cmcf`、`lem:thickness-equivalence`、`prop:rare-type`、`thm:two-letter-content`、`prop:full-content-types`、`op:fanout-two`。
- [README Change log](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/README.md)（blob `1c4dd9e6b2dab47ff1548921d0aa945c2d119a19`）：特に (54)、(57)、(138)、(153)、(155)。
- [(138) `chatgpt_intrusion_2026-11-04.md`](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/reviews/chatgpt_intrusion_2026-11-04.md)：定理2.1、定理3.1、例5.1。
- [(153) `claude_mu_ab_2026-11-05.md`](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/reviews/claude_mu_ab_2026-11-05.md)：補題1–4・7・7′、命題5。
- [(155) `chatgpt_virtual_length_2026-11-05.md`](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/reviews/chatgpt_virtual_length_2026-11-05.md)：定理5.1、定理6.1。
- [(54) `chatgpt_problemG_2026-11-01.md`](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/reviews/chatgpt_problemG_2026-11-01.md)：可換群の定理1。

**取得上の限界**：指定の `chatgpt_shortcut_classification_2026-11-06.md`、`chatgpt_negative_design_2026-11-06.md`、`chatgpt_frame_equivalence_2026-11-06.md` は、このブランチの指定パスではいずれも **404 NOT_FOUND**、コード検索でも発見できなかった。したがってそれらの**本文や Claude の独立検証過程を読んだとは主張しない**。今回の依頼文に記載された「枠の同値 F」「定理 A4」「N9–N13」の要約は、ユーザー提供の検証済み前提として区別して採用する。本文を取得できない三報への厳密な補題番号付き照合は未実施。

以下、`Σ={a,b,c}`、`c_Σ(w)=supp(w)`、`G` は reduced good、fan-out ≤2、rank ≤r、`v=|V|`、`θ=\bar θ_G≥1`。`W∈L(G)` は内容 `{a,b}` の最短語、`N=|W|=μ_ab`、`T` はそのような導出の中で節点数最小の成功導出。節点 `t` のラベルを `X_t`、生成組を `x_t`、総長を `ℓ_t`、arity を `d_t` とする。節点の生成文字位置は非削除性から互いに交わらないか、一方が他方を含む。

文法文脈 `E` は **実際の成功導出から部分木を除去して得る許容文脈**とし、その固定長を `|E|_fix` と書く。arity 2 なら `E=u □₁ m □₂ v`、必ず `m∈Σ⁺`、`u,v∈Σ*`。`x_t=(x_t¹,x_t²)` の順序は規則の nonpermuting 条件で保存される。

## 1. 課題0：O・O′・N13 の監査

### 補題 O [証明済み／既報 (153) 補題3の文法的特例]

任意の節点 `t` とそのラベル `X_t` の任意の**文法由来**の成功文脈 `E` について、`supp(E[x_t])={a,b}` なら

\[
  N\le |E|_{\rm fix}+\ell_t. \tag{O}
\]

**証明**：`X_t⇒* x_t` は実在する導出木。文法文脈 `E` は、成功導出の同じ非終端 `X_t` の部分木を取り除いてできたものである。よってその穴に `x_t` の導出木を入れれば、型付けや言語の代入可能性と無関係に `E[x_t]∈L(G)`。非削除・非置換・非併合により各成分を一度だけ、正しい順で挿入する。固定部と穴成分の長さが加算されるから `|E[x_t]|=|E|_fix+ℓ_t`。この語が `{a,b}` 内容なら、`W` の最短性から (O)。∎

**量化の注意**：`E` を任意の *言語論的な許容枠* にまで拡げると `E[x_t]∈L` は従わない。ここでは文法由来であることが不可欠。`T` の節点数最小性、SUB₁、SUB₂は (O) に不要。

### 補題 O0：厚さの文脈を `θ-d` に改善 [証明済み／厚さ補題(iv)の容易な強化]

任意の非終端 `B`（arity `d`）に、文法由来の成功文脈 `E_B` が存在して

\[
 |E_B|_{\rm fix}\le\theta-d <\theta. \tag{O0}
\]

**証明**：`G` は reduced なので `B` は少なくとも一つの規則 `R` の左辺であり、その `R` を使う成功導出がある。`θ_G(R)≤θ_G≤θ` を達成する成功導出を選び、その中の `R` の使用箇所（ラベル `B`）の部分木を削除する。`G` は good、特に λ-free かつ nondeleting だから、削除した `d` 個の生成成分はそれぞれ非空で総長が少なくとも `d`。外側に残った終端数は高々 `θ_G(R)-d≤θ-d`。nonpermuting・nonmerging および内部の兄弟生成の非空性から、arity 2 の中間固定部は非空（原稿の `lem:thickness-equivalence(iv)` の証明と同じ許容文脈）。∎

原稿の補題(iv)が述べる `≤θ` を誤りと見なすものではない。より鋭い境界を取り出しただけである。

### 系 O′ [条件付き（任意の短い文脈が ab-compatible な場合のみ）]

`Q` を `T` の比較不能な `q≥2` 節点の集合とする。各節点の `ℓ_t>0` で、互いの生成文字位置が交わらないため `∑_{t∈Q}ℓ_t≤N`。したがって最小総長の `t₀` は `ℓ_{t₀}≤N/q`。その `X_{t₀}` に長さ `≤θ-d_{t₀}` で `supp(E[x_{t₀}])={a,b}` の文法文脈があれば、

\[
 N\le \theta-d_{t₀}+N/q,
 \qquad N\le\frac q{q-1}(\theta-d_{t₀})\le2(\theta-d_{t₀})<2\theta. \tag{O′}
\]

**証明**：O と O0 を代入し、`1−1/q≥1/2` で割る。∎

この仮定が欠ける場合に O′ を適用することはできない。実際、下記 A1 により **q≥2 の重い c 強制反鎖では O′ の ab-compatible 短文脈は存在しない**。したがって `q` の多項式上界はここからは出ない。

### N13 [証明済み／O と同値、独立成果ではない]

\[
 \forall t\ \forall E\in\mathrm{Ctx}_G(X_t),\quad
 \mathrm{supp}(E[x_t])=\{a,b\}\Longrightarrow
 |E|_{\rm fix}\ge N-\ell_t. \tag{N13}
\]

これは (O) を移項したものに過ぎない。さらに既報 (153) 補題3は、文法由来に限らない共通の *言語論的* 文脈で、成分ごとの内容が一致する穴を比較するため、O 自体は既報より弱い。既報 (138) の侵入判定は**内側**の短い安全代表の有無を調べるが、N13は**外側**の ab-compatible 文脈の長さを調べる。着眼点は異なっても最短性以上の制約を追加しない。

## 2. 課題A：c に挟まれた節点

### A1：Q の全節点と、Q 外の節点 [証明済み]

`Q` を c 強制かつ `ℓ_t>θ` の節点からなる反鎖とし、`q≥2` とする。**このとき Q の全節点は例外なく「c に挟まれている」**。実は別途 `N>2θ` を仮定する必要さえない。

**証明**：任意の `t∈Q` について、他の `q−1` 個の節点の生成位置は t と交わらず、それぞれ総長が整数で少なくとも `θ+1`。したがって

\[
 \ell_t+(q-1)(\theta+1)\le\sum_{s\in Q}\ell_s\le N,
 \quad \ell_t\le N-(q-1)(\theta+1)\le N-\theta-1. \tag{A1}
\]

もし `X_t` に長さ `<θ` の文法文脈 E が存在して `supp(E[x_t])={a,b}` なら、`|E|_fix≤θ−1` なので
`|E[x_t]|≤N−θ−1+θ−1=N−2<N`。これは O に矛盾。内側 c 強制は Q の定義。従って全節点が二条件を満たす。しかも `N≥q(θ+1)≥2θ+2` が自動的に従う。∎

さらに、`Q` の任意の節点に対し短い ab-compatible 文法文脈は存在しないことが証明できたので、**O′ の追加仮定はこの重い反鎖の設定では満たされない**。O′ は正しい条件付き不等式だが、Q の上界に使う道具にはならない。

Q 外の非 c 強制節点・保持者についても N13 は成立するが、例えば `ℓ_t≤N−θ` の場合、短い文脈が c 無しなら差し替え語が単色（`a` のみ、または `b` のみ）になる必要がある、ということしか言えない。保持者の節点には `ℓ_t` が N に近い場合もあり、そのような節点では短い c 無しの W 文脈が実際に存在しても N13 に抵触しない。

### A2：短い文脈の正確な三分岐 [証明済み]

`E` が文法文脈で `|E|_fix<N−ℓ_t` なら、`E[x_t]∈L` は `N` より短い。この語は元の `x_t` が c 無しなので、

\[
 \boxed{\ c\in\mathrm{supp}(E)
 \quad\text{または}\quad
 \mathrm{supp}(E[x_t])=\{a\}
 \quad\text{または}\quad
 \mathrm{supp}(E[x_t])=\{b\}.\ } \tag{A2}
\]

**証明**：`E` に c がなければ `E[x_t]` も c 無し。空語でないので内容は `{a}`、`{b}`、`{a,b}` のいずれか。最後は最短性に反する。∎

特に `supp(x_t)={a,b}` なら、すべてのこうした短文脈に c が必要。一方 `x_t` が a だけの場合、短い文脈の固定部分も a だけ、あるいは空でよい。「c に挟まれる」は、**外側に必ず c がある**ことと同義ではない。

### A3：同名非終端に共通の c-free 文脈がある場合 [証明済み]

`B` の短い固定文法文脈 `E_B` を一つ選ぶ（O0）。ある `W` の反鎖 `Q_B` の全節点 `t` が `X_t=B` かつ `ℓ_t≤N−θ` なら、もし `E_B` に c がなければ、(A2) より全ての `x_t` は単色。さらに `E_B` の固定部が a を含めば全て `x_t` は純 a、b を含めば純 b。したがって fan-out 2 では中間 `m_B` が非空であるため、`E_B` が c-free なら **同じ B の全ての該当節点が同一文字による単色生成**となる。fan-out 1 の `E_B=□` では、別の出現が純 a と純 b になる余地は残る。

**証明**：`E_B[x_t]∈L` と (A2)。`supp(E_B)` に a,b の両方があれば矛盾。一方があれば `x_t` も同じ文字だけでなくてはならない。fan-out 2 では非空の中間固定部が該当する文字を供給する。∎

### A4：短い内外を合わせても W に直結しない [証明済み／非含意]

`B` が c 強制なら、厚さ補題(ii)から短い `ω_B∈L_B(G)` が存在し、`|ω_B|≤θ` かつその少なくとも一成分に c がある。O0の `E_B` と結合して

\[
 E_B[\omega_B]\in L,\quad |E_B[\omega_B]|\le2\theta-d.
\]

短い外側にも c がある場合でも、`W` に現れる穴の値 `x_t` は全成分が c-free、`ω_B` は一成分以上が c を含むので、**成分ごとの内容型が一致しない**。したがって `SUB_d` による `x_t↔ω_B` の代入はできない。また `W` の実際の枠の固定部は c-free なのに、`E_B` の固定部が c を持つなら、依頼文の枠同値 F の「同じ輪郭」も満たさない。両者の間に一段の SUB や F を適用して短い ab 語が出るとは言えない。各 SUB の前後では語全体の内容が保存される（既報 (153)、(143) 補題2.1）。

これは **どんな多段 SUB 連鎖も不可能**という定理ではない。異なる穴・枠の文字列が交差する「最後の ab 枠」が必要だという既報 (153) 補題3の障害は残る。

### A5：一本の道と反鎖での c の位置 [証明済み／限定された主張]

同じ成功導出の中で祖先 `s` と子孫 `t` の実際の枠を比較すると、祖先の**全成分より左**にあった固定 c は子孫の全成分より左、全成分より右にあった固定 c は子孫の全成分より右に残る。これは非置換・非削除と「子孫の各成分は祖先の生成成分内に入る」から従う。祖先が arity 2 でその二成分間に固定 c があるときは、子孫の両成分が祖先の両側へまたがれば c は子孫の `m` に残るが、子孫が一方の祖先成分内に収まればその c は子孫の右側または左側に移り得る。

**証明**：祖先の出力成分が占める区間を実際の語の座標に置く。子孫の各出力成分はこれら区間のどれかの内部にある（線形・非削除）。祖先より左・右にある文字はその区間の外を越えて移動できない。祖先の中間文字については子孫成分が占める区間との相対順序で場合分けすれば上記の三通り。∎

**重要な適用制限**：これは一つの成功導出に沿った包含関係の話であり、`T` とは別の短い成功導出から各 `E_B` を独立に選んだ場合の「c の位置の単調性」を与えない。比較不能な反鎖節点については、短文脈の c の左右・中央位置に一般的な連動は導けない。

### A6：課題Cに含まれる不可能条件 [証明済み]

「`T` の**全**節点の非終端が、**全ての**短い文法文脈で必ず c に囲まれる」は不可能。開始記号 `S` には `□` という長さ0の文法文脈がある。また任意の `t` で `N−ℓ_t<θ` なら、`W` から得る実際の文法文脈が短く c-free である。よって実現可能な設計条件は「適切な**内部の重い節点、かつ `ℓ_t≤N−θ`** に限定して c の外側を強制する」である。

## 3. 課題B：新しい c-個数スペクトル帰着

### 定義 [証明済み／純粋な定義]

\[
 S_c^{abc}(L):=\{\,|w|_c:\ w\in L,\ \mathrm{supp}(w)=\{a,b,c\}\,\}\subseteq\mathbb N_{>0},
\quad K_c(L):=|S_c^{abc}(L)|\in\mathbb N\cup\{0,\infty\}.
\]

さらに `θ≥1` に対し

\[
 A_\theta(L):=\sup\{m\ge0:\exists h\in\{1,\dots,\theta\},\ \{h,2h,\dots,mh\}\subseteq S_c^{abc}(L)\}.
\]

`A_θ` は全文字を含む語の **c-個数だけ**を見る算術的な量であり、`μ_ab` を定義に含まない。

### 定理 S1：反鎖からのスイッチ立方体 [証明済み]

`T` の反鎖 `Q` に対し、各 `t∈Q` の非終端が **少なくとも一つ c を含む生成組** `ω_t` を持つとする。この生成が短い必要はない。すると

\[
 \boxed{\ K_c(L)\ge\max\{0,|Q|-2\}.\ } \tag{S1}
\]

**証明**：`W` に a と b の出現を各1つ印付けする。反鎖の各節点の生成位置は交わらず、したがって印を含む Q 節点は高々2つ。印を含まないものを `t₁,…,t_m` とし、`m≥|Q|−2`。各 `j=1,…,m` に対し、**先頭の j 個だけ**を、それぞれ `ω_{t_i}` の導出木で同時に置き換える。Q は反鎖であり、good 文法は変数を一度だけ用いるので、得られる `W_j` は全て G の成功導出語。印を付けた a,b は置換領域の外に残る。元の W には c が存在せず、各 `ω_{t_i}` は c を少なくとも一つ持つので

\[
 |W_j|_c=\sum_{i=1}^{j}|\omega_{t_i}|_c,
 \quad 0<|W_1|_c<\cdots<|W_m|_c.
\]

各 W_j は a,b,c の全てを含み、c の個数が相異なる。従って `K_c(L)≥m≥|Q|−2`。∎

**この定理は SUB₁・SUB₂を使わず、arity 1/2 の区別も不要**。既報 (153) 補題4の「c の連の数」を数えるのとは違い、**全内容語の c 個数の異なる値**を得る。論理的には部分木の独立置換という既知の道具の直接帰結であり、外部文献に対する新規性は未調査。

### 定理 S2：短い c 逃げ道による算術進行 [証明済み]

`Q` が c 強制の重い節点の反鎖なら、

\[
 \boxed{q\le K_c(L)+2,\qquad q\le v A_\theta(L)+2.} \tag{S2}
\]

さらに `q≥3` なら、ある非終端 B と `1≤h≤θ` に対し、`S_c^{abc}(L)` は `h,2h,…,mh` を全て含み、

\[
 m\ge\left\lceil\frac{q-2}{v}\right\rceil. \tag{S2′}
\]

**証明**：S1により第1の不等式。S1の印を除いた集合 `Q₀` は `q−2` 個以上。ラベル B ごとに分割すると、ある B が `m≥ceil((q−2)/v)` 回現れる。この B は c 強制だから、厚さ補題(ii)で取った **B に共通の一つの**短い代表 `ω_B` は c を含む。`h=|ω_B|_c` は `1≤h≤|ω_B|≤θ`。B の m 個の出現から任意に j 個選び、全て `ω_B` に置換した語は、印の a,b が残り、c の個数が正確に `jh`。`j=1,...,m` の全てが L の full-content 語になる。従って `A_θ(L)≥m`、`q−2≤v A_θ(L)`。∎

### 系 S3：実際の多項式上界 [条件付き（full-content c スペクトルの有界性）]

既報 (153) 補題1（(138) 定理3.1の開始型での改良定数）と S2 より

\[
 \boxed{\mu_{ab}(L)\le 3(r+1)v\theta\,[K_c(L)+4],} \tag{S3a}
\]
\[
 \boxed{\mu_{ab}(L)\le 3(r+1)v\theta\,[vA_\theta(L)+4].} \tag{S3b}
\]

従って `K_c(L)≤p_r(v,θ)` **または** `A_θ(L)≤p_r(v,θ)` が別途示される部分クラスでは、要求する多項式上界が成立する。特に `K_c(L)≤1` なら `μ_ab≤15(r+1)vθ`。この結論は **Q が fan-out 1 だけのときも、短い c が左側にだけあるときも**有効。ただしその2条件**だけ**では K も A も有界だとは証明していない。その無条件の特別場合も未解決。

**既報の上界を使った完全な証明**：`T` の θ-重い節点は祖先に閉じている。任意の重い節点 t が c 強制でなければ、長さ≤θの c-free 生成組に置換できる。`ℓ_t>θ` なので語は短くなり、最短 ab 語ではなくなるため、元の a または b の全出現を t が保持していたことになる。各文字の保持者は祖先関係で一本の道をなすので、各深さの非 c 強制の重い節点は高々2個。Tの一本の道では `(a の保持者か,b の保持者か)` が降下に伴って高々二度だけ真から偽に変化する。同一状態で同じ非終端が2回現れれば、上側部分木を下側部分木で置換して ab 内容を保ち、長さを増やさず節点を減らせる。T の選択に矛盾。従って道の節点数は高々 `3v`。各深さの重い節点は反鎖で、c 強制のもの高々 q、保持者高々2、すなわち全重い節点は `3v(q+2)` 個以下。各重い節点が直接書く終端は高々 θ、各重くない子の総長は高々 θ、子は高々 r。W の全文字は重い節点の直接終端か重くない子に属するから `N≤3(r+1)vθ(q+2)`。重い節点が皆無なら `N≤θ` で同じ評価を満たす。これに S2 を代入して S3。∎

**H との非同値性の明示**：S3の追加仮定 `K_c≤poly` は、結論 `μ_ab≤poly` と同値ではない。例えば `L=Σ⁺` はすべての arity に関して c-content substitutable で、`S→a|b|c|SS` という reduced good ランク2文法を持ち、`θ=2`、`μ_ab=2` である。しかし `abc^k∈L` が全 `k≥1` に成立するので `K_c(L)=A_θ(L)=∞`。したがって **小さい μ は有界 K/A を含意しない**。また K/A は全内容語という別の層の可観測量であり、その定義自体に N も Q も含まない。前回の Bridge(P) と異なり、S3 は単なる代数的な言い換えではない。

**有限 C₂ でも K は μ の関数ではない [証明済み]**：任意の整数 `M≥3` に対し

\[
 L_M^*=\{\mathtt{ab},\mathtt{ba}\}
 \cup\{w\in\Sigma^M:\mathrm{supp}(w)=\{a,b,c\}\}
\]

と定める。この言語は有限・Parikh-saturated で、`μ_ab(L_M^*)=2`、しかし `K_c(L_M^*)=M−2`（c を1文字から M−2文字まで含む full-content 語がある）。しかも **全 arity で c-content substitutable**：同成分内容の組 x,y が同一枠 E で受理されれば、E[x],E[y] の全内容は一致する。受理される内容は `{a,b}` または `{a,b,c}` だけで、各内容について許容される **全語長は一つ**（2または M）なので、共通枠の固定長を消去すると穴の総長も一致する。任意の別枠 F において F[x],F[y] は同じ全内容かつ同じ全語長となるため、必ず同時に受理・不受理である。∎

この例は K と μ が別の量であることを**有限 C₂ の内部でも**示す。ただし定数規則を全部列挙する自明な文法では `θ=M`、文法サイズも大きいので、`K_c` と `v,θ` の多項式関係への反例では**ない**。N12型の「内容ごとに一つの**長さ**層」がなぜ定量的に難しいかとも整合する。

### 系 S4：反例設計の必要条件 N14 [証明済み]

`v_n θ_n=poly(n)` で `μ_ab(L_n)=n^{ω(1)}` となる族が存在したら、S3a により

\[
 K_c(L_n)\ge \frac{\mu_{ab}(L_n)}{3(r+1)v_n\theta_n}-4=n^{\omega(1)}.
\]

さらに S2′ により、full-content 語の c 個数スペクトルは**公差 `h_n≤θ_n` の、超多項式長の等差数列 `h_n,2h_n,…` を含む**。これを **N14（full-content c-スペクトル障害）** と呼ぶ。c を含む語の total length が一つの値に固定されていることと、c-count が一つに固定されていることは別である。したがって N14 だけで既報 N12（内容ごとに**長さ**一層）の全モデルを排除したとは主張しない。

## 4. 課題C：order-sensitive 倍増候補と完全な破綻証明書

### 候補 D_n：既報 (138) 例5.1 [証明済み／**対象クラス外**]

`n≥1` に対して fan-out 1、ランク2：

```text
S   → A_n b | aaaa | bbbb | cccc
A_0 → a | c
A_i → A_(i−1) A_(i−1) | c       (1≤i≤n)
```

`G_n` は reduced good：各成分・生成が非空、子変数は一度だけ順序どおりに現れ、全非終端は開始語 `A_n b` の導出中に現れ、全て生成可能。`v=n+2`。任意の `A_i` は `c` と `a^{2^i}` を生成する。`S→A_n b` の c-free ab 語は `a^{2^n}b` だけであり、他の S 規則は内容 `{a,b}` を持たないから

\[
 \mu_{ab}=2^n+1.
\]

所属は**並び順依存**：`a^{2^n}b∈L(G_n)` だが `ba^{2^n}∉L(G_n)`。各 `A_i` の `c` 逃げ道は1文字なので、`A_i` の各規則を成功導出で行使する最短長は、上位の兄弟を `c` にして、残りの各上位階層につき1文字＋末尾 b、そして自分の規則の最短生成長（1または2）で計算できる。従って正確に

\[
 \theta=\max\{4,n+2\}.
\]

`W=a^{2^n}b` の深さ n−i にある `A_i` の節点は総長 `2^i`、幅 `2^{n-i}`。`2^i>θ` なら全て c 強制の重い節点で、両端以外の任意部分木を `c` に替えれば c 侵入する。これらの `A_i` の**c-free 文法文脈**は、上位の各二倍化規則で兄弟を c-free の `a^{2^j}` にする必要がある。よって最短の c-free 外側は正確に

\[
 1+\sum_{j=i}^{n-1}2^j=2^n-2^i+1=N-\ell_t.
\]

特に `N−2^i>θ` の深さに限れば、**全ての長さ `<θ` の文法文脈が c を含む**。したがって root 不可能条件を内部節点に限定すれば「短い文脈は外側 c」という設計は文法上実現できる。S2の条件も満たす：同じ `A_i` のうち a の印を含まないものを順に `c` に置換すると、`c` 個数が1,2,...,`2^{n-i}−1` の full-content 語が実際に導出できる。

**しかし**、この候補は `C_{2,c_Σ}` に**属さない**。以下は `n≥1` に共通する arity 1 の完全な証明書：

\[
 \begin{aligned}
 &cb,ccb\in L(G_n),\
 &\mathrm{supp}(c)=\mathrm{supp}(cc)=\{c\},\
 &E_0=(\varepsilon,b):E_0[c],E_0[cc]\in L(G_n),\
 &E_1=(ccc,\varepsilon):E_1[c]=cccc\in L(G_n),\
 &E_1[cc]=ccccc\notin L(G_n).
 \end{aligned}
\]

`ccccc` は末尾 b の `A_n b` ではなく、長さ4の定数でもない。従って SUB₁ の共通枠・同内容・分布不一致という三条件がそろい、対象クラスから失格。既報 (138) の証明書を再使用したもので、**新しい反例族の発見ではない**。

この文法を形だけ拡張しても、C₂の証明になることはない。壊れた箇所はすでに C₁。追加の設計必要条件は、例えば c-only 同内容の `c,cc` に共通枠があるなら、全ての受理枠で双方を同時に受理しなければならない、という **SUB₁分布一致条件**。これは既知条件の具体的な使い方であり、新規定理と数えない。これに加え、上の N14 は別系統の**新しい定量的な必要条件**となる。

### 課題Cの到達度

候補 D_n は (i) order sensitivity、(ii) `||G_n||,θ=O(n)`、(iii) `μ_ab=2^n+1`、(iv) N13、(v) 多数の内部節点の全短文脈への c 侵入、(vi) N14 の全てを満たすが、`L(G_n)∈C_1` の時点で失格。N9、F、スロット移送への全対応を完成した、とは述べない。**完全な C₁・C₂所属証明を持つ超多項式族は得られなかった。**

## 5. 課題D：Parikh-saturated クラス

### 補題 D1 [証明済み／既報 README (57) の再証明]

`L` が Parikh-saturated なら、`(1,c_Σ)`-substitutability は `(d,c_Σ)`-substitutability を任意 `d≥1` に対して含意する。

**証明**：`d` 成分の正の組 `x=(x₁,…,x_d)`、`y=(y₁,…,y_d)` が各成分同内容で、ある d-hole 許容文脈 E で両方受理されるとする。`x^*=x₁…x_d`、`y^*=y₁…y_d` とし、E の固定部分を全て連結して一つの語 `z` とする。Parikh-saturationにより `zx^*`,`zy^*` は L に属する。`x^*,y^*` の内容は一致するから、SUB₁ によりそれらの一穴分布は一致する。任意の別の d-hole 文脈 F で `F[x]∈L` とし、その固定部分を連結した語を `z'` とする。再び Parikh-saturationで `z'x^*∈L`。SUB₁により `z'y^*∈L`。同じ Parikh ベクトルを持つ `F[y]` も L に属する。逆も対称である。∎

従って D の検討では、言語の並び替え閉性を仮定した上で arity2 の追加条件そのものは障害にならない。しかし **それだけでは `μ_ab` の上界を出せない**。

### 既存の二次上界と、その適用範囲 [条件付き（有限可換群の原像）]

README (54) と報告書 `chatgpt_problemG_2026-11-01.md` 定理1は、**有限可換群 H への全射の正の単位元原像** `L=φ^{-1}(1)∩Σ⁺` を生成する reduced good **CFG** について

\[
 |H|\le(r+2)\theta^2,
\]

従って `ord(φ(a))≤(r+2)θ²` とする。これは特別な Parikh-saturated（群の原像）言語についての定理であり、任意の Parikh-saturated `C_{2,c}` 言語へは拡張されていない。群の値が単位元という条件や arity 1 CFG の仮定を省いて使ってはならない。

別の既報 (155) 定理6.1は **任意の fan-out** の reduced good G に対し、非負加法写像 `λ` で `λ(a)=λ(b)>0` かつ `L(G)⊆λ^{-1}(Q)` なら

\[
 \mu_{ab}\le(r+1)\theta^2
\]

を証明している。この「全言語が加法的一水準」は任意の Parikh-saturated 言語には仮定できない。例えば `Σ⁺` は Parikh-saturated かつ `C_{2,c}` だが、`ab` と `aab` の λ 値が異なるため `λ(a)=λ(b)>0` の一水準ではない。

**D の一般命題は未証明・反例なし。** S3 は `K_c` が有界な場合の真の部分結果を与えるが、Parikh-saturation は `K_c` の有界性を含意しない（再び `Σ⁺` では `K_c=∞`）。

## 6. 計算機検査と限界

`chatgpt_outer_c_2026-11-06.py` は Python 3 の**標準ライブラリのみ**を使う。有限 L について長さ制限を別途設けず全ての正成分・許容一穴／二穴文脈を列挙し、同内容で共通文脈を持ちながら分布の異なる組を厳密に検出する。`L={ab,cb}` の C₁,C₂（後者の二穴出現は長さ不足のため空）を全列挙して検証した。さらに有限層言語 `L_M^*` の M=3,4 について C₁,C₂、`μ_ab=2`、`K_c=M−2` を全列挙で確認した。D_n の n=1,2 を完全列挙し、C₁失敗の証明書、`μ_ab`、`θ` を照合した。さらに n=6,8,10,12 の式で q、外側 c-free 文脈の最小長を計算し、n≤8 について構成的な c スイッチ後の語を生成して異なる c-count を検査した。

**[計算機による観察（有限層 M=3,4、倍増 n=1,2 および n=6,8,10,12）]**：上記の assert は全て通過した。`n≥1` の失格証明、`θ` 式、S1/S2、O 等の一般結論は**計算でなく本文の数学的証明**に依拠する。探索は一般の無限 MCFG の SUB 判定器ではないし、完全な C₂反例構成器でもない。

再現：`python chatgpt_outer_c_2026-11-06.py --check`。外部パッケージ、通信、GitHubへの書き込みは不要。

## 7. 最終結果表

| 結果 | 状態 | 数値・射程 | 既報との関係 |
|---|---|---|---|
| 補題 O / N13 | [証明済み] | `|E|_fix≥N−ℓ_t`（ab-compatible 時） | (153) 補題3の弱い特例／同値変形 |
| O0 | [証明済み] | `|E_B|_fix≤θ−fan(B)` | 原稿厚さ補題(iv)の定数改善 |
| O′ | [条件付き] | 最小 Q 節点に ab-compatible 短文脈があれば `N≤q(θ−d)/(q−1)` | 未検証 Bridge を回避するが幅を抑えない |
| Q の挟まれ方 | [証明済み] | `q≥2` の重い c 強制反鎖の **全 q 節点**が挟まれる（`N>2θ` は自動） | 本報の訂正 |
| 短文脈三分岐 | [証明済み] | 外側に c または結果が単色 | O の直接帰結 |
| S1 | [証明済み] | `K_c≥q−2` | 独立部分木置換からの c-count 下界 |
| S2 | [証明済み] | `q≤K_c+2`、`q≤vA_θ+2` | full-content の等差数列証明 |
| S3 | [条件付き] | `N≤3(r+1)vθ(K_c+4)` | (153) 補題1 + S2、K 有界なら多項式 |
| N14 | [証明済み] | 反例には多項式より多い c-count と短公差の長い AP が必要 | 負の設計の新しい検査項目 |
| D_n | [証明済み] | `v=n+2`, `θ=max(4,n+2)`, `N=2^n+1`、SUB₁失敗 | (138) 例5.1の再検証 |
| Parikh-saturated の C₁⇒C₂ | [証明済み] | 全 arity に拡張 | README (57) の再証明 |
| fan-out1 Q／左側だけの短 c | [未解決] | K/A 条件抜きでの q 上界は得られず | 元の特殊場合も未解決 |
| `op:fanout-two` | **未解決** | 一般の上界も所属証明付き反例もなし | 変更なし |

## 8. 残る穴を一つの命題で・次に試すこと

### 命題 R（有限 full-content c スペクトルの多項式幅） [予想／未証明]

**有限言語に限定した、元の問題とは異なる独立の研究命題**として次を提案する。

> 各固定 `r≥2` に多項式 `P_r` が存在し、有限の `L∈C_{2,c_Σ}` と reduced good fan-out≤2・rank≤r の表示 G に対して、`S_c^{abc}(L)` が空でなければ `K_c(L)≤P_r(v,θ)` が成り立つ。

これが証明されれば、S3により**有限ターゲット**の `μ_ab` は多項式になる。**ただし無限のターゲットに関しては何も証明しない**。この命題は全内容の c-count の種類数を制限するもので、`μ_ab` の上界そのものを仮定しないし、Q や N を定義に含まない。**条件が結論と同じではない具体例**として、上記 `L_M^*` は有限 C₂ で `μ_ab=2` を固定したまま `K_c=M−2` を任意に大きくできる。よって K の制御は μ の値を別名で書き直したものではない。ただしこの例で `θ=M` のため、**固定した v,θ に関する多項式上界命題同士の形式的な独立性まで証明したわけではない**。R は *有限 L 全体* に対する別の強い主張であり、有限 L の `μ_ab` の上界から `K_c` の上界を導く証明は得ていない。R の真偽は現状不明である。

**次に試すこと（3件）**：

1. **算術進行と枠同値 F の交点**：S2′ の `h,2h,…,mh` について、各語の `c` の入り位置が異なる場合に arity2 の同輪郭・中身交差を強制できるか。特に同名 fan-out1 の反鎖、短い c が左側だけのケースから始める。
2. **有限スペクトル幅 R の監査**：小さい有限 Parikh-saturated / order-sensitive `C₂` 言語を厳密に作り、`K_c` が `v,θ` と独立に大きくなる族を探す。失敗すれば飽和により c-run の長さ層が自動的に潰れる補題を探す。
3. **無限言語への別ルート**：`K_c=∞` または `A_θ=∞` の場合は S3 が使えないので、(155) の加法的一水準に入らない例を優先し、有限群的な保存量または c 侵入後の同輪郭衝突を明示する。

**最終判定**：補題 O、N13 自体は新しい橋ではない。今回得た実質的な部分結果は S1/S2 の **full-content c-count spectrum / bounded-step arithmetic progression** と、それを使う明示定数付き S3/N14 である。`q≤poly_r(v,θ)` の無条件証明はなく、`op:fanout-two` は未解決。

---

## 付録：検証スクリプト全文 `chatgpt_outer_c_2026-11-06.py`

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Finite checks for the outer-c research note (standard library only).

This is NOT a decision procedure for arbitrary MCFGs or infinite languages.
It checks all arity-1/2 contexts of explicitly enumerated FINITE languages,
and constructs checkable derivation-tree witnesses for a failed doubled family.
"""

from __future__ import annotations
from collections import defaultdict
from itertools import combinations, product
import argparse

ALPHABET = 'abc'


def supp(s: str) -> frozenset[str]:
    return frozenset(s)


def c_signature(tup: tuple[str, ...]) -> tuple[frozenset[str], ...]:
    return tuple(supp(x) for x in tup)


def fill(context: tuple[str, ...], holes: tuple[str, ...]) -> str:
    assert len(context) == len(holes) + 1
    return ''.join(context[i] + holes[i] for i in range(len(holes))) + context[-1]


def distributions(language: set[str], d: int):
    """Complete d-hole distributions over positive tuple occurrences in L.

    Each recorded context is admissible: d=2 has a nonempty internal gap.
    There is no arbitrary length truncation (language itself is finite).
    """
    assert d in (1, 2)
    distributions_by_tuple = defaultdict(set)
    for w in language:
        n = len(w)
        if d == 1:
            for i in range(n):
                for j in range(i + 1, n + 1):
                    x = (w[i:j],)
                    context = (w[:i], w[j:])
                    assert fill(context, x) == w
                    distributions_by_tuple[x].add(context)
        else:
            for i in range(n):
                for j in range(i + 1, n + 1):
                    for k in range(j + 1, n):  # nonempty fixed middle
                        for l in range(k + 1, n + 1):
                            x = (w[i:j], w[k:l])
                            context = (w[:i], w[j:k], w[l:])
                            assert context[1]
                            assert fill(context, x) == w
                            distributions_by_tuple[x].add(context)
    return dict(distributions_by_tuple)


def find_failure(language: set[str], d: int):
    """Return a complete C_d failure certificate, or None if C_d holds."""
    ds = distributions(language, d)
    by_type = defaultdict(list)
    for tup in ds:
        by_type[c_signature(tup)].append(tup)
    for signature, tuples in by_type.items():
        for x, y in combinations(sorted(tuples), 2):
            common = ds[x] & ds[y]
            if common and ds[x] != ds[y]:
                if ds[x] - ds[y]:
                    witness_x, witness_y = x, y
                    distinguish = sorted(ds[x] - ds[y])[0]
                else:
                    witness_x, witness_y = y, x
                    distinguish = sorted(ds[y] - ds[x])[0]
                shared = sorted(common)[0]
                assert fill(shared, witness_x) in language
                assert fill(shared, witness_y) in language
                assert fill(distinguish, witness_x) in language
                assert fill(distinguish, witness_y) not in language
                return {
                    'arity': d,
                    'type': signature,
                    'x': witness_x,
                    'y': witness_y,
                    'shared': shared,
                    'distinguishing': distinguish,
                    'shared_x': fill(shared, witness_x),
                    'shared_y': fill(shared, witness_y),
                    'yes': fill(distinguish, witness_x),
                    'no': fill(distinguish, witness_y),
                }
    return None


def fixed_content_layer(m: int) -> set[str]:
    """All length-m words of full abc support, plus the two ab words.

    This is C_d for every arity d by the equal-(support,length)-layer proof.
    Enumeration is intended only for small m (tested m=3,4).
    """
    assert m >= 3
    return {'ab', 'ba'} | {
        ''.join(t) for t in product(ALPHABET, repeat=m)
        if supp(''.join(t)) == supp('abc')
    }


def doubled_A(n: int) -> set[str]:
    """Exact finite A_n language for n<=3 (size rises doubly exponentially)."""
    assert 0 <= n <= 3
    lang = {'a', 'c'}
    for _ in range(1, n + 1):
        lang = {'c'} | {u + v for u in lang for v in lang}
    return lang


def doubled_L(n: int) -> set[str]:
    """Example (138) from 2026-11-04, enumerated exactly."""
    return {'aaaa', 'bbbb', 'cccc'} | {x + 'b' for x in doubled_A(n)}


def theta_doubled(n: int) -> int:
    """Rule-successful shortest lengths, minimized analytically per rule.

    S -> A_n b: 2. S -> zzzz: 4.
    A_i -> c: shortest outside path costs 1+(n-i), plus 1.
    A_i -> A_(i-1) A_(i-1): shortest outside costs 1+(n-i), plus 2.
    A_0 -> a|c: shortest outside cost 1+n, plus 1.
    """
    assert n >= 1
    costs = [2, 4]
    costs += [1 + (n - i) + 1 for i in range(n + 1)]
    costs += [1 + (n - i) + 2 for i in range(1, n + 1)]
    costs += [1 + n + 1]
    assert max(costs) == max(4, n + 2)
    return max(costs)


def best_antichain_level(n: int):
    """Choose a level A_i with heavy yield 2^i>theta and maximal width."""
    theta = theta_doubled(n)
    choices = [i for i in range(n) if 2 ** i > theta]
    if not choices:
        return None
    i = min(choices)
    q = 2 ** (n - i)
    ell = 2 ** i
    n_word = 2 ** n + 1
    min_c_free_outer = n_word - ell
    return (i, q, ell, theta, min_c_free_outer)


def cube_words(n: int, i: int) -> list[str]:
    """Explicit legal simultaneous A_i->c substitutions in a^2^n b.

    The FIRST A_i block is never touched, keeping an a-witness outside.
    At least one c is introduced; b always remains at the last position.
    """
    assert 0 <= i < n
    q = 2 ** (n - i)
    block = 'a' * (2 ** i)
    result = []
    for k in range(1, q):
        blocks = [block] + ['c'] * k + [block] * (q - 1 - k)
        w = ''.join(blocks) + 'b'
        assert supp(w) == supp('abc')
        assert w.count('c') == k
        result.append(w)
    return result


def run_checks():
    print('== exact finite C_1,C_2 tester ==')
    good = {'ab', 'cb'}
    for d in (1, 2):
        fail = find_failure(good, d)
        assert fail is None
        print(f'L={{ab, cb}} arity {d}: PASS; enumerated tuples={len(distributions(good, d))}')
    assert 'ab' in good and 'ba' not in good

    for m in (3, 4):
        finite = fixed_content_layer(m)
        assert find_failure(finite, 1) is None
        assert find_failure(finite, 2) is None
        assert min(len(w) for w in finite if supp(w) == supp('ab')) == 2
        k_c = len({w.count('c') for w in finite if supp(w) == supp('abc')})
        assert k_c == m - 2
        print(f'finite layer m={m}: C1,C2 PASS, mu_ab=2, K_c={k_c}, |L|={len(finite)}')

    for n in (1, 2):
        L = doubled_L(n)
        expected_mu = 2 ** n + 1
        min_ab = min(len(w) for w in L if supp(w) == supp('ab'))
        assert min_ab == expected_mu
        assert theta_doubled(n) == max(4, n + 2)
        certificate = find_failure(L, 1)
        assert certificate is not None
        print(f'bad family n={n}: |L|={len(L)}, theta={theta_doubled(n)}, '
              f'mu_ab={min_ab}, C1 fails')
        print('  witness:', certificate)
        # A fixed certificate valid for every n>=1 from (138):
        assert {'cb', 'ccb', 'cccc'} <= L
        assert 'ccccc' not in L

    print('== spectrum and antichain stress tests ==')
    for n in (6, 8, 10, 12):
        info = best_antichain_level(n)
        assert info is not None
        i, q, ell, theta, outer = info
        assert ell > theta
        assert outer > theta
        assert q <= 2 ** n
        # Short contexts of A_i MUST contain c, because a c-free
        # context costs at least outer > theta.
        # In this grammar all A_i also derive the one-letter word c.
        print(f'n={n}: v={n+2}, theta={theta}, mu_ab={2**n+1}, '
              f'level={i}, ell={ell}, q={q}, min-c-free-outer={outer}, '
              f'lower-bound K_abc >= {q-1}')
        # q-1 is sharper than the general q-2 because b is always outside.
        if n <= 8:
            samples = cube_words(n, i)
            assert len({w.count('c') for w in samples}) == q - 1
            assert all(w.endswith('b') for w in samples)
            print('  c-switch counts:', [w.count('c') for w in samples])
    print('ALL CHECKS PASSED')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='run exhaustive finite checks')
    args = parser.parse_args()
    run_checks()

```

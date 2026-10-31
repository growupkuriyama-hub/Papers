<!-- PART 1/1 START -->

| 主張 | 判定 | 根拠の節 |
|---|---|---|
| 一般の命題 MR：三文字偶奇型付け・fan-out 1・rank 2 で全ての導出的文脈の最短代表が `C θ̄_G` 以下 | **未解決** | §1, §8 |
| クラス全域の集合駆動作用素について `Ω(‖G‖² θ̄_G)` を要する固定群型付けの漸近的最小 CFG 族 | **未解決** | §1, §6, §8 |
| **長さスペクトル補題**：有限 `L(G)` の受理語長が h 種類なら、最大語長 `W ≤ μ+(h−1)(θ−μ) ≤ h θ` | **証明済み** | §3.1 |
| **部分的 MR**：上の仮定なら全 A,t,E_A に `κ_{A,t}≤h θ`、従って `τ≤h θ` | **証明済み** | §3.2 |
| **特徴データ上界**：`‖F‖₊≤9‖G‖[1+(2+2h)θ]+1_{ε∈L}` | **証明済み（原稿の復元定理を使用）** | §3.3 |
| **二次下界の障害**：有限の二次下界族は `h=Ω(‖G‖)` を必要とする | **証明済み（必要条件）** | §3.4 |
| 有限の同型受理語について、一方が他方の真の因子なら標的は無限 | **証明済み** | §4.1 |
| 「有限の代入可能言語では同型受理語の長さが同じ」という推論 | **反証済み** | §4.2：`{b,cc}` |
| 群型付けでも `t_typ≥n+1` と `τ=1, θ=2` が同時に起きる | **証明済み** | §5 |
| 三文字の既存族で `Ω(‖G‖θ)`、削除下界と全表示に対する `‖G‖≥q+1` | **証明済み（既存命題の具体化）** | §6 |
| 小規模非循環 CFG 720 表示のうち 545 を完全検査、66 合格、合格例の最大 `τ/θ=1` | **観測** | §7、付録 A/B |

# 多文字の偶奇型付けにおける特徴データ長の指数一致問題

**調査日**：2026-10-30。**文献上の新規性：未調査。** 研究上の独立発見・優先権は主張しない。解析的に証明した節と、既存原稿の定理を使った帰結と、有限計算による観測を明確に区分する。**結論：MR と二次下界のいずれも決着していない。**

## 1. 正本の取得と問題の量化

原稿：[GitHub main.tex](https://github.com/growupkuriyama-hub/papers/blob/main/02_fixed-h-mcfg/main.tex)、`growupkuriyama-hub/papers` の default branch `main` を本調査で改めて取得した。取得したファイルの **Git blob SHA は `8a19aee7d6d6a279c6af6e4b3f71c97f5ba324bf`**、約 228,862 文字・4,258 行。Git blob SHA は commit SHA ではない。内容を引いた箇所はこの版に照合した。

`Σ={a,b,c}`、`g(w)=|w|_a mod 2∈ℤ₂`、`f=1`、規則 rank≤2。`L∈C^{mcf}_{1,g}`、`G` は `L∩Σ⁺` を生成する reduced good CFG。`v=|V|`、`s=‖G‖`（以下の式で混同を避けるときは `gsize`）、`θ=θ̄_G=max(1,max_R θ_G(R))` とする。最短成功使用の定義は

\[
\theta_G(R)=\min\{|w|:w\in L(G),\ \text{some successful derivation of }w\text{ uses }R\}.
\]

各規則ごとに **別の** 最短成功導出を用いる。`‖G‖=|V|+Σ_R(1+rank(R)+template-symbol-count(R))`。`good` は λ-free, nondeleting, nonpermuting, nonmerging、reduced は全ての非終端が reachable/productive（`def:standard-mcfg`, `def:grammar-properties`）。

`def:tuple-substitutable`, `def:class-cmcf`：全ての非空因子 `x,y` に対し、`g(x)=g(y)` で二側文脈 `(p,q)` の共有受理があれば `D_L(x)=D_L(y)`。**空語因子は比較しない**。fan-out≥2 の定義では d 穴文脈の隣り合う穴の間の固定区切りは非空である。本調査の証明は d=1 のみを使用し、二穴交換は使わない。

`def:reconstruction` の二つの作用素 `B^{≤2}_{1,g}` と `B_{1,g}` は Start/Const/Comp/Link からなる集合駆動再構成。特徴標本とは、`F⊆K⊆L` なる任意の有限正例集合 K が十分である、という強い意味で使う。`lem:app-u1-fillers` の型付けに依存しない証明により、実現型 t の typed nonterminal `X=A_t` に対し

\[
\tau_X=\min\{|z|:z\in\Sigma^+,\ g(z)=t,\ E_A[z]\in L\}=: \kappa_{A,t}.
\tag{1.1}
\]

`E_A` は `lem:thickness-equivalence`(iv) の短い **導出的な一穴文脈** で `|E_A|_{fix}≤θ`。`τ=max_X τ_X` は分布類の最短代表長。型付き **生成** 収率 `t_typ` と混同しない。

`thm:data-from-typed-thickness`, `cor:distribution-representatives` の既存結果は、今回 `|S^#|=3`, rank 2 なので

\[
 \|F\|_+\le N_{typ}(1+2\theta+2\tau)+\mathbf1_{\{\varepsilon\in L\}},
 \qquad N_{typ}\le9\|G\|.
\tag{1.2}
\]

と与える。MR を `τ≤Cθ` と示せれば `O(‖G‖θ)`。一方 `thm:window-group-polydata`, `thm:local-group-polydata` は `O(‖G‖²θ)` を既に与える。この版の `lem:heavy-node-count`, `prop:block-replacement-interface` は零和集合により、重い反鎖の幅を制御するが、その後の根葉道長 `|V||H|^f` を消していない。

**調査対象外にしないが誤用もしない事項**：`prop:rare-type` は実現した**完成語の型**を各一つ必要にするだけであり、型数 2 のここでは直接 `Ω(gsize²θ)` を導かない。`prop:linear-factor-sharp`, `prop:linear-factor-all-fanout` は全削除閉包を使う既知の `Ω(gsize θ)`。`prop:unary-cyclic-linear` と `lem:app-lf-descent` は単項言語の算術周期性を利用し、文字 c,b を含む対象に直接は適用できない。

## 2. 完全検査の方法と限界

有限で非循環の CFG `A_0,...,A_n` の全生成語を**打切りなしで**列挙できた例について、全 `w∈L` の全区間 `0≤i<j≤|w|` から非空因子 `x=w[i:j]` と文脈 `(w[:i],w[j:])` を登録した。これらは有限 L における `D_L(x)` を厳密に尽くす。全ての共有文脈を parity 別にまとめ、共有文脈があっても分布集合が異なる二因子を探した。偽判定のときは共有文脈および区別文脈を返す。

同じプログラムで非終端の最短生成長 `d_A` と最短成功外文脈 `o_A` を計算し、各規則 `R:A→ρ(B_1,...,B_j)` の厳密値を `θ_G(R)=o_A+端末数(R)+Σ_i d_{B_i}` とした。`E_A` は `o_A` を実現する実際の文字列文脈として復元する。代入可能な場合だけ、各 typed class について `E_A[z]∈L` を満たす最短 `z` を検索した（これは式 (1.1) の厳密な有限計算）。

列挙中に 500 語を超えた表現、または総因子出現数が 28,000 を超えた表現は**未検査**として除外し、反例数に加えなかった。演習範囲も出力ログも付録に全文を記録する。どの有限観測も MR の普遍証明ではない。

## 3. 証明した部分結果：長さスペクトルの障害

### 3.1 定理：最長語長と受理長の種類数

**定理 3.1（証明済み）。** `G` を非空で有限な `L(G)⊆Σ⁺` の reduced good MCFG（ファンアウトや rank は任意）とする。`μ=min{|w|:w∈L(G)}`、`θ=θ̄_G` とし、`H={|w|:w∈L(G)}` は相異なる長さ h 個、`W=max H` とする。このとき

\[
W\le\mu+(h-1)(\theta-\mu)\le h\theta.
\tag{3.1}
\]

**証明。** 最初に原稿 `lem:app-lf-descent` の下降命題を確認する。各非終端 B の最短生成収率総長を `d_B`、成功導出内で B 一出現を穴にした外側の最短固定長を `o_B` とする。任意の規則 `R:B→ρ(B_1,...,B_j)` が明示的に書く端末の数を `c_R` とすると、nondeleting と独立な子・外側の導出の組合せによって

\[
\theta_G(R)=o_B+c_R+\sum_i d_{B_i},\qquad o_B+d_B\ge\mu.
\tag{3.2}
\]

任意の `w∈L(G)` で `|w|>μ` とし、導出木でその収率長が `d_B` を超える節点のうち最も深い節点 u を取る。子は全て各自の最短収率長に達しているから、u が用いる規則 R の現在の長さは `c_R+Σ_i d_{B_i}`。u の部分木だけを長さ `d_B` の導出に替えれば新しい成功語 `w'` が得られ、短縮量は

\[
\delta=|w|-|w'|=c_R+\sum_i d_{B_i}-d_B
 =\theta_G(R)-o_B-d_B\in[1,\theta-\mu].
\tag{3.3}
\]

`H={n_1<...<n_h}` と置けば `n_1=μ`。それぞれ `n_j` (`j≥2`) に (3.3) を適用すると、新しい長さは `n_j` 未満の H の元であり、したがって `n_j-n_{j-1}≤θ-μ`。これを j=2,...,h で足すと (3.1) の前半を得る。後半は `μ≤θ` と `h≥1` から従う。□

この証明は代入可能性も偶奇も使っていない。**従って「長さの種類が少ない有限下界候補」は一般に θ が最長語を押し上げる**という制限を、明示的に式で表す。

### 3.2 系：h-長さ標的における MR

**系 3.2（証明済み）。** 今回の偶奇型付けに限らず、任意の型付け・任意の fan-out の reduced good G と、有限の `L(G)` に対して、長さスペクトルが h 種類なら、各実現 typed nonterminal X とその導出的文脈 E_A に

\[
\tau_X\le t_{typ}(G,s)\le W\le h\theta.
\tag{3.4}
\]

特に今回の MR の式は `C=h` で成立する。固定定数 h をあらかじめ与える部分クラスでは、**G と L によらない C=h** である。

**証明。** 縮約・生産的であるため各 typed X に終端生成 tuple `u∈L_X` がある。`lem:thickness-equivalence`(iv) の文脈 `E_A` は `E_A[u]∈L(G)` を保証する。非削除性と λ-free から収率の全端末はその成功語に含まれるため、`||u||_1`≤|E_A[u]|≤W`。よって全 typed X の最短生成収率も高々 W。分布代表は生成 tuple を候補にできるので `τ_X≤t_typ`。定理 3.1 を適用して (3.4)。fan-out 1 では `u` 自身が `g(u)=t`、`E_A[u]∈L` という MR の条件を満たす。□

### 3.3 系：標本長の明示上界

**系 3.3（証明済み；原稿既存の再構成定理を使用）。** `L∈C^{mcf}_{1,g}` とする。`L∩Σ⁺` が有限で受理長 h 種類を持つなら、両再構成作用素に共通の特徴標本 F が存在して

\[
\|F\|_+\le9\|G\|\bigl[1+(2+2h)\theta\bigr]
   +\mathbf1_{\{\varepsilon\in L\}}
\le9\|G\|(3+2h)\theta+1.
\tag{3.5}
\]

**証明。** (3.4) の `τ≤hθ` と `r=2`、`N_typ≤3²‖G‖` を原稿 `cor:distribution-representatives`（その完全証明は `main.tex` の同ラベルの箇所）の式 (1.2) に代入する。最後の不等式は `θ≥1`。ε は主たる非空文法の外で 1 個の標本として加える。□

### 3.4 系：有限二次下界族には h=Ω(gsize) が必要

**系 3.4（証明済み；必要条件のみ）。** 各 n について有限 `L_n∈C^{mcf}_{1,g}`、reduced good rank≤2 表示 `G_n` を取り、`g_n=‖G_n‖`、`θ_n=θ̄_{G_n}`、受理長種類数 `h_n` とする。ある `c>0` で、**クラス全域に特徴標本を持つあらゆる集合駆動作用素**の `L_n` の特徴標本長が `c g_n²θ_n` 以上なら

\[
h_n\ge\frac{c}{18}g_n-\frac32-\frac{1}{18g_n\theta_n}.
\tag{3.6}
\]

特に `g_n→∞` なら `h_n=Ω(g_n)`。

**証明。** 仮定の量化には、クラス全域に特徴標本をもつ原稿の固定作用素 `B^{≤2}_{1,g}` も含まれる。これについて系 3.3 により、同じ標的のある特徴標本は `9g_n(3+2h_n)θ_n+1` 以下である。一方仮定によればそれも `c g_n²θ_n` 以上。両辺を `g_nθ_n>0` で除して変形すれば (3.6)。□

**解釈**：全語同長に揃える既知の削除構成では h=1 だから、二次下界の族としては使えない。これは二次下界が一般に偽であるという意味ではない。

## 4. 受理語の因子包含と、誤った長さ分類

### 4.1 定理：有限な同型受理語の因子反鎖

**定理 4.1（証明済み）。** 任意の `(1,s)`-代入可能言語 L について、非空の `u,v∈L` が同型で、`v=p u q`、`|p|+|q|>0` を満たすなら L は無限である。従って有限 L の各型ごとの受理語集合は、**真の連続因子関係**に関して反鎖をなす。

**証明。** `u,v` は同型で、同じ空外文脈 `(ε,ε)` に受理されるので `D_L(u)=D_L(v)`。`v=p u q∈L` から `(p,q)∈D_L(u)` なので `p v q∈L` である。同じ置換を再帰的に繰り返せば、`p^k v q^k∈L` が全ての k≥0 に対して成立する。実際 `p^k v q^k=p^{k+1}u q^{k+1}` を同型因子交換で `p^{k+1}v q^{k+1}` に変えられる。これらの語長は `|v|+k(|p|+|q|)` と厳密に増大するので無限。□

### 4.2 反例：同型だけでは受理長は一致しない

**反証済み。** `L={b,cc}` は固定された `g(b)=g(c)=0` の下で `(1,g)`-代入可能であり、受理長は 1 と 2、両語の型は同じ 0。

**完全な確認。** 同じ文脈 E が二つの **異なる非空因子** x,y を受理すると仮定する。もし E が非空の固定文字を持てば、同一の受理語（b または cc）しか生成できない。b と cc は文字が異なるので、一方の語から他方への非自明な共通文脈は空外文脈しかなく、そのとき因子は b と cc である。両因子は自分自身の語に一回だけ（語全体として）出現するので、いずれの分布も `{(ε,ε)}` である。文脈が同一語内で二つの異なる因子を得るには文字列の長さが変わるはずであるが、固定の語と固定の外文脈から穴の長さが一意に定まる；cc 内の長さ1因子はともに c で等しい。従って共通文脈を持つ相異なる因子では分布が一致する。□

**重要**：一文字の場合の「同じ型の異長受理語から周期化」は、短い語が長い語の因子として現れることに依存していた。多文字でこの条件を省く推論は偽。

## 5. 型付き生成長と代表長の差：この偶奇型付けでの完全な例

**命題 5.1（証明済み）。** 各 n≥1 に対し次の rank≤2、fan-out 1 の reduced good CFG `H_n` を定める（開始記号 S）：

```text
S -> SS | a | b | c | A_0 | A_1 | ... | A_n
A_0 -> a
A_i -> c A_(i-1) | b      (1 <= i <= n)
```

このとき `L(H_n)=Σ⁺`、`‖H_n‖=10n+18`、`θ̄_{H_n}=2` であり、偶奇型付けについて `t_typ(H_n,g)≥n+1` なのに `τ(H_n,g)=1`。

**証明。** `S→SS|a|b|c` のみで `Σ⁺` の全てが生成され、他の規則も非空語しか生成しないので `L(H_n)=Σ⁺`。全規則は good、`S→A_i` で各 A_i は到達可能、全 A_i は `b`（i≥1）または `a`（i=0）を生成するので生産的。`S→SS` の最短成功使用は長さ2、`A_i→c A_(i-1)` の最短成功使用も長さ2（`S→A_i` から直接達成する）。残る規則はいずれも長さ1の成功使用がある。よって θ=2。

サイズは非終端数 `n+2`、規則寄与 `S→SS`:5、`S→a|b|c`:6、`S→A_0,...,A_n`:3(n+1)、`A_0→a`:2、`A_i→c A_(i-1)`:4n、`A_i→b`:2n なので、`n+2+5+6+3(n+1)+2+4n+2n=10n+18`。

`A_n` が奇型（a の個数が奇数）の語を導出するには、各 `A_i` で選択肢 `b` を避けて最深の `A_0→a` まで進まなければならない。したがって唯一の奇型収率は `c^n a`、長さ n+1 である。`t_typ≥n+1`。一方 `L=Σ⁺` は全ての非空因子の分布が同じ（全ての二側文脈に受理される）であり、同型の任意の二語は分布同値である。実現する偶型には b、奇型には a という長さ1の代表がある。全 typed nonterminal に当てはまり、`τ=1`。□

従って `t_typ≤Cθ` という生成語ベースの一様主張は**反証済み**だが、ユーザーの MR は生成語でない代表を許すため、この例は MR の反例**ではない**。この差を越える理論が必要。

## 6. 既存の一次下界、削除論法、そして二次下界に不足するもの

### 6.1 全部分集合の明示族

原稿 `prop:linear-factor-sharp` を今回の固定アルファベット `Σ={a,b,c}` に具体化する。`q≥k≥1`、`M=2^k`、`W=2q+M+2`、

\[
w_i=a^i b a^{q-i}c^M a^{q-i} b a^i\quad(0\le i\le q),\qquad
L_{q,k}=\{w_0,\ldots,w_q\}.
\tag{6.1}
\]

全語の a 個数は 2q なので、偶奇型は全て 0 である。

**補題 6.1（証明済み）。** 任意の `J⊆L_{q,k}` は無型でも一穴代入可能であり、従って今回の `(1,g)`-代入可能性を満たす。

**証明。** `uxv,uyv∈J` とする。全語長 W なので `|x|=|y|`。各 `w_i` の二つの b の位置は 1-indexed で `i+1` と `W-i`、それぞれの取り得る位置区間は互いに交わらない。`u` に b があるならその b の絶対位置、`v` に b があるなら末尾からの相対距離が固定され、どちらも添字 i を一意に決める。したがって `uxv=uyv=w_i` となり `x=y`。もし `u,v` のどちらも b を持たなければ二つの b はともに穴因子 x（および y）にある。その距離 `W-2i-1` は i を決定し、x 内での最初の b の位置は穴の開始位置を決定する。従って x の受理分布はただ一つの文脈 `{(u,v)}` であり、y についても同じである。どちらの場合も共通文脈を持つ二因子の分布は一致する。有限言語は CFL なので結論。□

### 6.2 普遍的な削除補題

**補題 6.2（証明済み）。** L が有限、かつ `L\{w}` が同じ学習対象クラスに属する場合、そのクラス全域に特徴標本を持つ任意の集合駆動型作用素の L の特徴標本 F は w を含む。

**証明。** `w∉F` と仮定する。`L'=L\{w}` の特徴標本 F' を取り、`K=F∪F'⊆L'` と置く。K は有限。F の特性から作用素の K 上の出力は L、F' の特性から同じ K 上の出力は L' となるが、`L≠L'`。矛盾。□

このため (6.1) の全 q+1 語は任意のクラス全域集合駆動作用素の任意の特徴標本に含まれ、

\[
\|F\|_+\ge(q+1)(W+1).
\tag{6.2}
\]

原稿に示された具体的な reduced good rank-two 表示は

```text
A_j -> b H_j b                (0 <= j <= q)
A_j -> a A_(j-1) a            (1 <= j <= q)
H_0 -> C_k
H_j -> a H_(j-1) a            (1 <= j <= q)
C_0 -> c
C_t -> C_(t-1) C_(t-1)      (1 <= t <= k)
start = A_q
```

で、数学的帰納法により `L(C_t)={c^{2^t}}`、`L(H_j)={a^j c^M a^j}`、`L(A_q)=L_{q,k}`。全規則は good、全非終端は生産的かつ A_q から到達可能。記号単位で数えると `‖G_{q,k}‖=17q+6k+13≤23(q+1)`。全成功語が長さ W であるため、この表示だけでなく **任意の reduced good 表示** の全規則について `θ_G(R)=W`、したがって θ=W。

全表示のサイズ下界には原稿の **既知の** `thm:data-from-typed-thickness` を `s_triv` に適用する。この定理は、任意の reduced good G から高々 `|V|+|P|≤‖G‖` 語の特徴標本を構成する。補題 6.1 と補題 6.2 からその標本には q+1 語の全てが必要なので、任意の reduced good G に `‖G‖≥q+1`。従って具体的 G は最小表現サイズの定数倍以内。式 (6.2) は既存の `Ω(‖G_{q,k}‖θ)` を再現する。

**二次下界ではない理由**：この族は長さの種類 h=1。§3.4 の必要条件に違反するため `Ω(‖G‖²θ)` を達成できない。さらに定数 c を固定した任意の大きい q について `‖F‖₊/(‖G_{q,k}‖²θ)=O(1/q)`。

### 6.3 型付けを変えても避けられない量化

`prop:rare-type` は根に実現する型 0 と 1 の少なくとも一語ずつ（存在する場合）を必要にする。ただし **２語だけの強制は二次データ下界を意味しない**。一次族の削除下界は出力としての言語の各語を必要とするため、**あらゆる集合駆動型作用素** に及ぶ。`B_{1,g}` についてのみサンプルを大きく作ったという主張とは異なる。

## 7. 実験結果と失敗する構成の具体的証明書

付録 A の Python は標準ライブラリだけで実行でき、付録 B にログ全文を付した。

* 非循環 rank≤2 のカタログ：n=1,...,4、各階層の structural rule 6 種、shortcut 6 種、底の選択 5 種で 720 文法。500 語および因子総数 28,000 の資源上限内で **完全生成・完全判定した 545** 文法のうち 66 文法が代入可能、479 不適合。175 文法は未検査。合格文法の最大語数は 5、観測された `max τ/θ=1`。**この狭いカタログは普遍命題 MR を証明しない**。
* 二段短絡 `A_0→a|b; A_i→b A_{i-1} A_{i-1} b | c A_{i-1} c` は n=1 で失敗する。`x=baa` と `y=bbb` はともに偶型、共通文脈 `E=(ε,b)` で `baab,bbbb∈L`。しかし `F=(b,ε)` は `F[y]=bbbb∈L` で `F[x]=bbaa∉L`。これは純粋な**一穴の解析的反例証明書**であって計算による推測ではない。
* `A_0→a|b; A_i→A_{i−1}A_{i−1}|a|b` も n=2 で失敗。共有文脈 `E=(ε,ε)` は偶型の `aa` と `aaaa` を受理するが、`F=(ε,a)` は `aaa∈L` で `aaaaa∉L`（プログラムの実出力を別途参照）。
* 既存一次下界族について `q=1,...,4`、`k=min(q,2)`、**各族の全 2^{q+1} 個の部分集合**を全分解で判定し全件合格。これは §6.1 の普遍的解析証明を独立確認する有限観測である。
* `L={b,cc}` は同型異長の反例であり、完全判定も合格。

## 8. 残された正確な十分命題

### 8.1 上界を決着させるのに十分な命題（未証明）

**(U) one-context parity descent**：ある絶対定数 C が存在して、今回の全ての対象 L,G、各導出的 E_A と実現型 t について、`E_A[u]∈L` かつ `g(u)=t` なる u が一つでも存在し `|u|>Cθ` なら、同じ型の非空語 v で `|v|<|u|`、`E_A[v]∈L` となるものが存在する。

この命題が成立すると、正整数長の最小元 `κ_{A,t}` が Cθ を超えることはできないため MR が直ちに成り立つ。元の typed nonterminal による **生成** を v に課してはいけない。§5 は生成語を要求する強化が偽であることを示す。候補証明方法は、異なる重いノードから得た型差分が ℤ₂ で相殺する際の**共通一穴文脈**の構築であるが、その共通文脈は現時点で得られていない。これは MR とほぼ同じ難しさの局所下降形式であり、**証明済みの削減とは呼ばない**。

### 8.2 下界を決着させるのに十分な命題（未証明）

**(N) length-diverse deletion family**：定数 `c,C>0` と rank≤2 の reduced good CFG `G_n` および有限 `(1,g)`-代入可能 `L_n=L(G_n)` が存在し、`g_n=‖G_n‖=Θ(n)`、`θ_n=θ̄_{G_n}=n^{O(1)}` で、`L_n` に少なくとも `cn` 個の相異なる語 `w_{n,i}` があり、各 `|w_{n,i}|≥cnθ_n` かつ **全ての** `L_n\{w_{n,i}}` も `C^{mcf}_{1,g}` に属する。さらに `‖G_n‖=Ω(n)` は全ての reduced good 表示について成り立つ（これは別途証明すること）。

この条件なら補題 6.2 から任意のクラス全域集合駆動作用素の特徴標本は各語を含むため、総長は `Ω(n²θ_n)=Ω(g_n²θ_n)`。**ただし §3.4 により、この族は少なくとも Ω(n) 種類の受理語長を持たねばならない。** 実現例は未発見。

### 8.3 一文字・他の群・高ファンアウトへの射程

長さスペクトル定理 (§3.1) とその分布代表への帰結 (§3.2) は **全ての有限 semigroup/monoid typing と fan-out** にそのまま通用する。削除補題 (§6.2) も同様。一方で偶奇型付けの MR は一般有限アーベル群や fan-out 2 にも証明できていない。`prop:unary-cyclic-linear` の `τ≤2mθ` は、厳密に一文字の場合に成立する既存定理としてのみ使用する。

## 9. 論文に挿入する English LaTeX 案

以下は **証明済みの新しい帰結として記述できる部分** に限る。必要な元の manuscript lemma の label は現在の Git blob に一致する。文献上の新規性は未調査。

```latex
\begin{proposition}[A length-spectrum obstruction to quadratic data]
\label{prop:parity-length-spectrum-obstruction}
Let $G$ be a reduced good grammar with finite nonempty
$L(G)\subseteq\Sigma^+$, and let $h$ be the number of distinct
lengths occurring in $L(G)$. Put $\mu=\min\{|w|:w\in L(G)\}$ and
$\theta=\bar\theta_G$. Then
\[
  \max\{|w|:w\in L(G)\}
  \le \mu+(h-1)(\theta-\mu)\le h\theta.
\]
Consequently, for any typing $s$, every realized typed
nonterminal has a representative of length at most $h\theta$.
For the typing $g:\{a,b,c\}^+\to\mathbb Z_2$ with
$g(a)=1$ and $g(b)=g(c)=0$, if $L\in\mathcal C^{\rm mcf}_{1,g}$
and $G$ has rule rank at most two, the capped and uncapped
reconstruction operators have a common characteristic sample
$F$ such that
\[
 \|F\|_+\le9\|G\|[1+(2+2h)\theta]
        +\mathbf1_{\{\varepsilon\in L\}}.
\]
In particular, if the minimum characteristic-data length
for every class-wide set-driven operator is at least
$c\|G\|^2\theta$, then
\[
 h\ge\frac{c\|G\|}{18}-\frac32
              -\frac{1}{18\|G\|\theta}.
\]
\end{proposition}
\begin{proof}
For each nonterminal $B$ let $d_B$ be the least total
length of a derived tuple and $o_B$ the least successful
outside-context length. If $R:B\to\rho(B_1,\ldots,B_j)$
writes $c_R$ terminals, then
$\theta_G(R)=o_B+c_R+\sum_i d_{B_i}$ and
$o_B+d_B\ge\mu$. Given a derivation of a sentence of
length greater than $\mu$, choose a deepest node whose
subtree yield exceeds $d_B$. Its children have shortest
yields, and replacing the node by a shortest $B$-derivation
strictly decreases sentence length by
$\theta_G(R)-o_B-d_B\in[1,\theta-\mu]$.
Thus the gap between consecutive realized sentence lengths
is at most $\theta-\mu$. Summing the $h-1$ gaps proves
the length bound. Every typed nonterminal has a terminal
yield that embeds in some successful sentence, so its
shortest typed yield has length at most the longest sentence.
Hence $\tau\le t_{\rm typ}\le h\theta$. Apply
Corollary~\ref{cor:distribution-representatives} with
$N_{\rm typ}\le3^2\|G\|$ and rank cap two to obtain the
sample estimate. If all class-wide set-driven operators
have the displayed quadratic lower bound, then so does
the capped reconstruction operator. Comparing the two
estimates and rearranging gives the stated lower bound
on $h$.
\end{proof}

\begin{lemma}[Factor-antichain property of finite typed targets]
\label{lem:finite-typed-factor-antichain}
Let $L$ be finite and $(1,s)$-substitutable. There do
not exist $u,v\in L\cap\Sigma^+$ of the same type such
that $u$ is a proper contiguous factor of $v$.
\end{lemma}
\begin{proof}
Otherwise $v=p u q$ with $|pq|>0$. Since $u,v\in L$
have the same type, the empty outer context gives
$D_L(u)=D_L(v)$. From $puq\in L$ it follows that
$pvq\in L$, and repeating the substitution yields
$p^k v q^k\in L$ for every $k\ge0$. Their lengths
strictly increase, contradicting finiteness.
\end{proof}
```

## 10. 自己点検

| チェック項目 | 結果・箇所 |
|---|---|
| τ と t_typ の区別 | §1 式 (1.1)、§5 に明示的な巨大ギャップの完全証明 |
| 上界は τ に対するものか | §3.2 の τ、§3.3 で既存代表定理に代入。MR 一般は未証明 |
| 下界は実際の特徴標本に対するものか | §6.2 の任意集合駆動作用素に対する削除補題 |
| 最小 `‖G‖` が全ての表示について下から抑えられているか | 既存一次族 §6.2 では原稿の無型特徴標本定理から `‖G‖≥q+1`。未解決の二次族では未証明条件として残した |
| 各規則の最短成功使用を個別に計算したか | §2、§5、実験の `rule-theta` 出力 |
| d 穴内部区切りは非空、一穴/二穴を混同していないか | §1。全ての新証明は d=1；fan-out 一般化部分は原稿の既存定理のみ |
| 有限検査を普遍命題に使用していないか | §2/§7 は「観測」。定理の証明は §3–§6 に別記 |
| ε の扱い | 全て `L∩Σ⁺` の文法を使用。特徴データのみ `+1_{ε∈L}` |
| 定数と依存関係 | §3 で `9,18` を明示。`h` は固定されなければ MR の絶対定数 C を与えない |
| 新規性 | **文献上の新規性：未調査**。本調査は先行文献への独立な優先権調査を実施していない |

## 付録 A：再現用 Python ソース全文

実行例：`PYTHONHASHSEED=0 python parity_experiment.py`。全出力は付録 B のとおり。**外部ライブラリ不使用**。`PYTHONHASHSEED=0` は再現性のためであり、数学的判定を変えない。

```python
#!/usr/bin/env python3
"""Finite, acyclic three-letter CFG audit (standard library only)."""
from itertools import product
from collections import defaultdict

ALPHABET = 'abc'
# A rule is an alternating string of terminal characters and integer child labels.
# Rule rank is the number of integer child occurrences, at most two.

def typ(w):
    return w.count('a') % 2

def gen(rule, Y):
    chunks = ['']
    for symbol in rule:
        choices = [symbol] if isinstance(symbol, str) else Y[symbol]
        chunks = [s+x for s in chunks for x in choices]
    return chunks

def yields(rules, cap=500):
    Y = {}
    for i, choices in enumerate(rules):
        s = set()
        for rule in choices:
            for w in gen(rule, Y):
                s.add(w)
                if len(s)>cap: return None
        Y[i] = sorted(s)
    return Y

def exact_substitutability(L):
    dist = defaultdict(set)
    bycontext = defaultdict(lambda: [set(),set()])
    for w in L:
        for i in range(len(w)):
            for j in range(i+1,len(w)+1):
                x = w[i:j]
                ctx = (w[:i], w[j:])
                dist[x].add(ctx)
                bycontext[ctx][typ(x)].add(x)
    for ctx,groups in bycontext.items():
        for group in groups:
            if len(group)<2: continue
            xx = sorted(group)
            anchor = xx[0]
            for x in xx[1:]:
                if dist[anchor]!=dist[x]:
                    smaller, larger = sorted([dist[anchor],dist[x]],key=len)
                    witness=sorted(larger-smaller)[0] if larger-smaller else sorted(smaller-larger)[0]
                    return False, (anchor,x,ctx,witness,anchor in dist and witness in dist[anchor],witness in dist[x])
    return True, None

def min_yield_and_context(rules, Y):
    n=len(rules)
    lengths=[min(map(len,Y[i])) for i in range(n)]
    shortest=[min(Y[i],key=lambda w:(len(w),w)) for i in range(n)]
    # E_i=(prefix,suffix), initially start A_{n-1}.
    outer=[None]*n
    outer[-1]=('', '')
    for i in range(n-1,-1,-1):
        if outer[i] is None: continue
        pre,suf=outer[i]
        for rule in rules[i]:
            for j,x in enumerate(rule):
                if not isinstance(x,int): continue
                before = ''.join(shortest[y] if isinstance(y,int) else y for y in rule[:j])
                after = ''.join(shortest[y] if isinstance(y,int) else y for y in rule[j+1:])
                candidate=(pre+before,after+suf)
                if outer[x] is None or (len(candidate[0])+len(candidate[1]),candidate)<(len(outer[x][0])+len(outer[x][1]),outer[x]):
                    outer[x]=candidate
    theta=0
    values=[]
    for i,choices in enumerate(rules):
        for rule in choices:
            inside=sum(len(x) if isinstance(x,str) else lengths[x] for x in rule)
            val=len(outer[i][0])+len(outer[i][1])+inside
            theta=max(theta,val)
            values.append((i,repr(rule),val))
    return lengths,shortest,outer,theta,values

def tau_of_finite(rules,Y,contexts, L):
    # For each realized A-type, take shortest positive v with E_A[v] in L.
    kappa={}
    for i in range(len(rules)):
        p,s=contexts[i]
        for t in {typ(x) for x in Y[i]}:
            accepted=[]
            for w in L:
                if w.startswith(p) and w.endswith(s) and len(w)>len(p)+len(s):
                    v=w[len(p):len(w)-len(s) if s else len(w)]
                    if typ(v)==t: accepted.append((len(v),v))
            assert accepted,(i,t,p,s)
            kappa[i,t]=min(accepted)
    return max(x[0] for x in kappa.values()),kappa

def fixed_family(n):
    # A0 -> a | b, Ai -> b Ai-1 Ai-1 b | c Ai-1 c
    rules=[[('a',),('b',)]]
    for i in range(1,n+1):
        rules.append([('b',i-1,i-1,'b'),('c',i-1,'c')])
    return rules

def sparse_family(n):
    # Ai -> Ai-1 Ai-1 | a | b  (n small)
    rules=[[('a',),('b',)]]
    for i in range(1,n+1): rules.append([(i-1,i-1),('a',),('b',)])
    return rules

def study(rules):
    Y=yields(rules,cap=500)
    if Y is None: return None
    L=Y[len(rules)-1]
    if sum(len(w)*(len(w)+1)//2 for w in L)>28000: return None
    ok,cert=exact_substitutability(L)
    lengths,shortest,outer,theta,values=min_yield_and_context(rules,Y)
    tau,kappa=tau_of_finite(rules,Y,outer,L) if ok else (None,None)
    size=len(rules)+sum(1+sum(isinstance(x,int) for x in r)+sum(len(x) if isinstance(x,str) else 1 for x in r) for ch in rules for r in ch)
    return dict(L=L,ok=ok,cert=cert,theta=theta,tau=tau,gram_size=size,rule_theta=values,kappa=kappa)

def catalog():
    # Finite acyclic binary/unary construction sweep; each A_i has a
    # composed rule and a shortcut; some A_0 choices mix types.
    shapes=[lambda i:(i-1,i-1),lambda i:('a',i-1,i-1),lambda i:(i-1,'b',i-1),
            lambda i:('c',i-1,i-1,'b'),lambda i:('a',i-1,'b'),lambda i:('b',i-1,'c')]
    short=[('a',),('b',),('c',),('aa',),('ab',),('bc',)]
    bases=[[('a',)],[('b',)],[('a',),('b',)],[('b',),('c',)],[('a',),('c',)]]
    tested=passed=skipped=0
    best=(0,None)
    max_m=0
    examples=[]
    for n in range(1,5):
      for mode in range(len(shapes)):
       for shortcut in short:
        for base in bases:
         rules=[base]+[[shapes[mode](i),shortcut] for i in range(1,n+1)]
         out=study(rules)
         if out is None:
            skipped+=1; continue
         tested+=1
         if out['ok']:
            passed+=1
            ratio=out['tau']/out['theta']
            if ratio>best[0]:best=(ratio,(n,mode,shortcut,base,len(out['L']),out['theta'],out['tau'],out['gram_size']))
            max_m=max(max_m,len(out['L']))
            if len(examples)<6 and ratio>=1:examples.append((n,mode,shortcut,base,len(out['L']),out['theta'],out['tau']))
    return tested,passed,skipped,best,max_m,examples

def lower_family(q,k):
    M=2**k
    return {"a"*i+"b"+"a"*(q-i)+"c"*M+"a"*(q-i)+"b"+"a"*i for i in range(q+1)}

def lower_subset_audit():
    for q in range(1,5):
        k=min(2,q)
        words=sorted(lower_family(q,k))
        inspected=0
        for choice in product([0,1],repeat=len(words)):
            subset={w for flag,w in zip(choice,words) if flag}
            good,cert=exact_substitutability(subset)
            if not good: raise AssertionError((q,k,subset,cert))
            inspected+=1
        print(f'lower_family(q={q},k={k}) |L|={len(words)} W={len(words[0])}, all {inspected} subsets exact substitutable: YES')

def main():
    print('Python standard-library exact finite-CFG validator')
    print('Alphabet={a,b,c}; parity g(w)=#a modulo 2; empty factors excluded')
    for name,rule in [('three-letter layered n=1',fixed_family(1)),
                      ('three-letter layered n=2',fixed_family(2)),
                      ('binary shortcuts n=2',sparse_family(2))]:
        x=study(rule)
        if x is None: print(name,'SKIPPED (resource cap)'); continue
        print(name, 'words=',len(x['L']), 'substitutable=',x['ok'], 'g=',x['gram_size'], 'theta=',x['theta'], 'tau=',x['tau'])
        print(' rule-theta=',x['rule_theta'])
        if not x['ok']:
            print(' counterexample=',repr(x['cert']))
    print('catalog: n=1..4; 6 production shapes, 6 shortcut words, 5 bases = 720 grammars')
    tested,passed,skipped,best,max_m,examples=catalog()
    print('exactly-tested=',tested,'substitutable=',passed,'skipped=',skipped)
    print('largest subst-language word count=',max_m)
    print('max tau/theta in tested substitutable grammars=',best)
    print('examples with tau/theta>=1=',examples)
    # A counterexample to the tempting claim "same-type words have same length".
    L={'b','cc'}
    print('L={b,cc}:',exact_substitutability(L),'lengths=',sorted(map(len,L)),'types=',sorted(typ(w) for w in L))
    lower_subset_audit()
if __name__=='__main__':main()

```

## 付録 B：実行ログ全文

```text
Python standard-library exact finite-CFG validator
Alphabet={a,b,c}; parity g(w)=#a modulo 2; empty factors excluded
three-letter layered n=1 words= 6 substitutable= False g= 18 theta= 4 tau= None
 rule-theta= [(0, "('a',)", 3), (0, "('b',)", 3), (1, "('b', 0, 0, 'b')", 4), (1, "('c', 0, 'c')", 3)]
 counterexample= ('baa', 'bbb', ('', 'b'), ('b', ''), False, True)
three-letter layered n=2 words= 42 substitutable= False g= 31 theta= 8 tau= None
 rule-theta= [(0, "('a',)", 5), (0, "('b',)", 5), (1, "('b', 0, 0, 'b')", 6), (1, "('c', 0, 'c')", 5), (2, "('b', 1, 1, 'b')", 8), (2, "('c', 1, 'c')", 5)]
 counterexample= ('bbaa', 'bbbb', ('', 'bbaabb'), ('b', 'baabb'), False, True)
binary shortcuts n=2 words= 30 substitutable= False g= 25 theta= 3 tau= None
 rule-theta= [(0, "('a',)", 3), (0, "('b',)", 3), (1, '(0, 0)', 3), (1, "('a',)", 2), (1, "('b',)", 2), (2, '(1, 1)', 2), (2, "('a',)", 1), (2, "('b',)", 1)]
 counterexample= ('aa', 'aaaa', ('', ''), ('', 'a'), True, False)
catalog: n=1..4; 6 production shapes, 6 shortcut words, 5 bases = 720 grammars
exactly-tested= 545 substitutable= 66 skipped= 175
largest subst-language word count= 5
max tau/theta in tested substitutable grammars= (1.0, (1, 0, ('a',), [('a',)], 2, 2, 2, 11))
examples with tau/theta>=1= [(1, 0, ('a',), [('a',)], 2, 2, 2), (1, 0, ('a',), [('b',)], 2, 2, 2), (1, 0, ('a',), [('b',), ('c',)], 5, 2, 2), (1, 0, ('b',), [('a',), ('c',)], 5, 2, 2), (1, 0, ('c',), [('a',), ('b',)], 5, 2, 2), (1, 0, ('aa',), [('a',)], 1, 2, 2)]
L={b,cc}: (True, None) lengths= [1, 2] types= [0, 0]
lower_family(q=1,k=1) |L|=2 W=6, all 4 subsets exact substitutable: YES
lower_family(q=2,k=2) |L|=3 W=10, all 8 subsets exact substitutable: YES
lower_family(q=3,k=2) |L|=4 W=12, all 16 subsets exact substitutable: YES
lower_family(q=4,k=2) |L|=5 W=14, all 32 subsets exact substitutable: YES
```

<!-- PART 1/1 END -->
<!-- END OF FILE -->

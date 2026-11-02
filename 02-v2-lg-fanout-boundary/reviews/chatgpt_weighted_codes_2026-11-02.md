# 重み付き符号は三文字の `(2,c)`-組代入可能言語内で実現できるか

**研究日**：2026-11-02  
**対象**：栗山貴之論文 #2、`op:fanout-two`、`Σ={a,b,c}` の純粋 `a` 語問題  
**立場**：原稿の定義を使用し、必要な代入可能性の移送は本報告内で再証明する。有限探索と一般定理を区別する。

## 0. 判定一覧

| 主張 | 判定 | 根拠 |
|---|---|---|
| 場合I（`a⁴,b⁴,c⁴` が現れる）：所属は全文字の極大塊の骨格 `σ(w)` と Parikh ベクトル `Ψ(w)` だけで決まる | **証明済み** | §2.1–2.2 |
| 場合Iで `μ_a(L) ≤ poly(‖G‖, θ̄_G)` が一般に成り立つ | **未解決** | §2.3、§6 |
| 三文字の加法的非負重みの単一レベル集合に含まれる言語では、代入可能性を仮定せず `μ_a(L)≤(r+1)² θ̄_G³` | **証明済み（本報告の独立証明）** | §3、定理3.1 |
| 一般の `m` 文字では上記の長さは `(r+1)^{m−1} θ̄_G^m` 以下 | **証明済み** | §3、定理3.1 |
| 場合Iで4乗の存在から Parikh 飽和・全ての隣接交換が従う | **反証**：非減少語と加法的重みの交叉例 | §2.3 |
| 場合IIで `d_i=(bc)^i bb` は接頭符号、`b,c` の最大ランはそれぞれ3,1以下 | **証明済み** | §4.1 |
| 上記符号に重み `2^i` をつけた、全重み `2^n` の連結言語は、全 `n≥3` で arity 1 の代入可能性に違反 | **証明済み（明示的な一穴証明書）** | §4.2 |
| 場合IIIで `d_i=bc^i b`、重み `2^i` の全連結言語は `n≥4` で arity 2 に違反 | **証明済み（明示的な二穴証明書）** | §5 |
| 小さな有限例の `(1,c),(2,c)` 全文脈検査結果 | **有限対象について厳密な全数検査** | §4.3、§5、付録A |
| 一般の指数重み符号を使った `(2,c)` の反例族の実現 | **未達成** | §6 |
| 定理3.1等の文献上の新規性 | **未確認**。短い検索では同定できず、独創性の確定はしない | §7 |

**結論を先に述べる**：中心の問い `Q` も `op:fanout-two` も解決していない。ただし今回、任意の良い文法に対して通用する**非負線形 Parikh 重みの三次上界**を独立に証明できた。これは、文字そのものに指数的な価値を持たせる反例設計を排除する。さらに、符号の内部に4乗が無い設計でも、**接頭符号の境界に対する一穴交換**が指数重みを壊す例を一般の `n` に対して与えた。

## 1. 正本・前提・検証範囲

### 1.1 照合対象

- [現行 `main.tex`](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/main.tex)、今回取得した blob SHA `b72cd2ed648f802886f0ab7c60a72f9f40c0864b`。使用した定義：`def:standard-mcfg`, `def:grammar-properties`, `def:tuple-substitutable`, `lem:thickness-equivalence`, `def:characteristic-sample`, `def:reconstruction`。論文の未解決問題は `op:fanout-two`。
- [Claude 2026-11-01 三文字報告](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/reviews/claude_ternary_content_2026-11-01.md)、SHA `658f3744cfdeea54d2566cfbcac3d38049c21e1d`。補題3.1、系3.2、補題3.3–3.5、補題6.3と照合した。**本報告で論理的に使用する4乗移送については§2に独立の証明を記す**。他の補題は新定理の未証明の公理として使用しない。
- [ChatGPT 2026-11-02 純粋文字報告](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/reviews/chatgpt_pure_letter_fanout2_2026-11-02.md)、SHA `063ca391af87e82c5153779b22ecf7d65f09192a`。重みの骨格剛性と上界 `r^M` の背景。
- [ChatGPT 2026-11-02 骨格多様性報告](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/reviews/chatgpt_skeleton_diversity_2026-11-02.md)、SHA `0d28618c520c2f470b3c72c7fac1158d67371baf`。重み packing と、`bc^i b` に対する離散アフィン制約の背景。

注意：本報告の定理3.1の証明は**先行報告の骨格剛性、隙間合流、共役移送には依存しない**。使用する文法上の補題は `lem:thickness-equivalence` (i),(ii) であり、下の§3.2にその利用を説明する。§4–5の不成立証明は直接定義から確認できる。

### 1.2 記号

`Σ={a,b,c}`、`c(w)` は現れる文字の集合。`L∈C_{2,c}` は fan-out `≤2` の MCFL で、**全ての arity `d=1,2`** において次を満たす：各成分が非空、成分ごとの内容が等しい二つの組 `u,v` が共通の許容受理文脈を持てば、その全受理文脈が一致する。二穴文脈

`p □₁ q □₂ r`

では `q∈Σ⁺`、すなわち**穴間の固定部分は非空**とする。

`G` は `L∩Σ⁺` の reduced good 表示、fan-out `≤2`、ランク `≤r` (`r≥1` を定理3.1で許す)、`θ:=θ̄_G≥1`、`g:=‖G‖`。`good` は非削除・非交換・非合流（原稿の *nonmerging*）・λ-free。規則が直接書く終端数は `≤θ`、各非終端 `B` には総長 `≤θ` の生成組 `ω_B` が存在する（原稿の厚さ補題）。

`μ_a(L)=min{k≥1 : a^k∈L}` は該当する純粋 `a` 語が存在する場合のみ定義する。一般に `Q` は `μ_a(L)` の `poly(g,θ)` 上界を問う。

## 2. 場合I：3文字すべての4乗がある場合

### 2.1 4乗からの基本移送を直接証明する

**補題2.1（一般の文字 `x` に対する一単位移送）**。`L∈C_{2,c}` に因子 `x⁴` が現れたとする。このとき任意の `u,v∈Σ*` と非空の `z∈Σ⁺` について

\[
 u\,xzx^2\,v\in L\quad\Longleftrightarrow\quad u\,x^2zx\,v\in L. \tag{2.1}
\]

**証明**。`p x⁴ q∈L` を一つとる。二組 `(x,xx)` と `(xx,x)` は成分ごとに同じ内容 `({x},{x})` を持つ。許容文脈 `p □₁ x □₂ q` は両者を同じ `px⁴q` に写す。したがって arity 2 の組代入可能性より両者の分布は等しい。任意の文脈 `u □₁ z □₂ v`（`z≠ε`）に適用すると(2.1)が得られる。□

**系2.2（再配分と正規形）**。`x⁴` がどこかに現れるなら、`w` の極大 `x` ランの**数と位置を表す `x` 骨格**を固定し、`|w|_x` を固定したまま、ランの正の長さを任意に再配分しても `w∈L` は不変である。従って `a⁴,b⁴,c⁴` がすべて現れるなら

\[
 \boxed{\sigma(w)=\sigma(w'),\quad \Psi(w)=\Psi(w')
        \ \Longrightarrow\ (w\in L\iff w'\in L)}. \tag{2.2}
\]

ここで `σ` は極大同字ランを一文字に圧縮した**全文字のラン骨格**であり、`Ψ(w)=(|w|_a,|w|_b,|w|_c)` である。

**証明**。二つの隣接した `x` ランの間の `x` を含まない隙間を `z` とする。長さが `(p,q)` のランを `(p+1,q−1)` に変える操作は、`q≥2` なら(2.1)とその前後の `x` を文脈に吸収して実行できる。正の整数組成の集合はこの隣接単位移送で連結なので、任意の再配分ができる。異なる文字 `a,b,c` のラン長を順に目標の値に合わせる操作は**別の文字のラン長を変えず**、全文字の骨格を保つ。よって(2.2)。□

従って依頼文の「骨格＋Parikh 正規形」は**正しい**。ただしそれは「Parikh ベクトルだけで所属が決まる」の意味ではない。

### 2.2 正規形で重み付き符号に生じる制約

一つの受理語 `w` の全文字骨格を固定している限り、各文字のラン長の再配分は完全に自由になる。例えば

\[
 bc^i b\;bc^j b \longleftrightarrow bc^{i+1}b\;bc^{j-1}b
 \qquad(j\ge2)\tag{2.3}
\]

は、`c⁴` が**言語中のどこかに**あれば、どちらか一方が受理されると他方も受理される（両者の `c` 骨格が一致し `c` の総数が同じ）。

もし `d_i=bc^i b` を独立のトークンとし、トークンの整数重み `t_i` の**合計がちょうど `N`** である全連結を受理するなら、上の両辺が復号可能で範囲内にあるたびに

\[
 t_i+t_j=t_{i+1}+t_{j-1} \tag{2.4}
\]

が必要になる。特に `j=i≥2` の場合は `2t_i=t_{i-1}+t_{i+1}`。指数列 `t_i=2^i` はこれに反する。これは前回報告のアフィン剛性と整合するが、**符号語の出現と、変換後が有効なトークン列となること**を仮定している。任意の文法の全生成組に(2.4)を適用したわけではない。

### 2.3 なぜ場合Iの一般証明にはまだならないか

`L` が(2.2)の正規形を持っても、**異なる全文字骨格の間の交換や合流は一切保証されない**。以下の明示例が示す。

\[
 H_8=\{w\in a^*b^*c^*:\ |w|_a+2|w|_b+2|w|_c=8\}.\tag{2.5}
\]

この言語は有限で正則（従って fan-out 1・rank 1 以下の MCFG 表示を持つ）。`a⁸,b⁴,c⁴∈H₈` なので3文字の4乗を全て持ち、かつ `aabbc∈H₈`、`bbaac∉H₈` と Parikh ベクトルの一致だけでは所属が決まらない。

**`H₈∈C_{2,c}` の直接証明**：`a* b* c*` の受理語の任意の非空因子は非減少で、最初の文字と最後の文字はその内容集合から一意に決まる。このため、同内容の非空因子組が一つの許容文脈を共有すれば、その組を入れ替えても各成分内部・接合部の非減少性は変化しない。また、加法的重み `λ(a)=1, λ(b)=λ(c)=2` に関し、共通の受理文脈で両方が重み8なら二組の**成分重みの合計**は等しい。したがって、他の任意の許容文脈での非減少性と重み8の条件は同時に成否が一致する。これは arity 1,2 の両方に通用する。□

この例自体は `μ_a(H₈)=8` と短いので `Q` の反例ではない。示すのは**4乗の存在だけから全交換可能性を補う論法が誤り**という点である。場合Iの未解決部分は、**異なる骨格を持つ長い短縮代替の間の重み比較を、文法のすべての実現可能な配置において強制する**ことである。

## 3. 新しい部分定理：非負加法重みの単一レベルは多項式長

この節は **場合I・II・IIIを同時に含む構成排除定理**であり、代入可能性さえ必要ない。

### 3.1 定理と意味

**定理3.1（正の `a` 重みを持つ非負加法レベルの純粋語上界）【証明済み】**。

アルファベット `Σ` の大きさを `m≥1`、`a∈Σ` とする。`λ:Σ*→(ℝ_{≥0},+)` は文字上の非負重みから定まる加法写像で、`λ(a)>0` とする。`G` は reduced good MCFG（fan-outは任意、規則ランク `≤r`, `r≥1`）、`θ=θ̄_G≥1` とする。

ある定数 `Q≥0` について

\[
 L(G)\subseteq\lambda^{-1}(\{Q\}),\qquad a^k\in L(G),\quad k\ge1
\tag{3.1}
\]

ならば

\[
 \boxed{k\le (r+1)^{m-1}\theta^{m}.}\tag{3.2}
\]

特に `Σ={a,b,c}` では

\[
 \boxed{\mu_a(L(G))\le (r+1)^2\bar\theta_G^{\,3}.}\tag{3.3}
\]

これは**文法サイズに依存しない**（その代わり「全ての受理語が同じ非負加法重みに属する」という強い仮定がある）。文字重みは文法族ごとに変わってよく、指数的に大きくてもよい。`L(G)∈C_{2,c}` は仮定しない。

### 3.2 証明

`λ(a)` で割り、以下 `λ(a)=1` とする。残る `m−1` 個の文字の重みを昇順に

\[
0\le t_1\le t_2\le\cdots\le t_{m-1}
\]

と書く。`a^k` の成功導出木 `T` を任意に固定する。`G` は good、特に非削除なので、`T` のどの節点 `h` の生成組も**全成分が `a` のみ**である。その総長を `ℓ_h` と書く。

**(A) 各節点長の短い非負重み表現**。`h` の非終端を `B` とする。厚さ補題によって `B` は総長 `≤θ` の生成組 `ω_B` を持つ。`h` を `ω_B` の導出に置き換えても成功導出を得る。置き換え前と後の文はどちらも `L(G)` に入り、いずれも `λ` 値は `Q` である。非削除性と加法性によって外側の寄与は同じだから

\[
 \ell_h=\lambda(\omega_B),\qquad
       \|\omega_B\|_1\le\theta.\tag{3.4}
\]

特に、`ℓ_h<t_j` なら `ω_B` には重み `≥t_j` の文字は現れない（全重みが非負であるため）。また、導出の一つの規則が直接書く終端は `≤θ` 文字であり、今回の木では全て `a` なので、親節点長は

\[
 \ell_{\rm parent}\le\theta+\sum_{\rm children}\ell_{\rm child}
 \le\theta+r\max_{\rm children}\ell_{\rm child}.\tag{3.5}
\]

定数規則の節点（葉）の長さは `≤θ`。

**(B) 重い文字を初めて使う際の閾値交差**。`t_j≤k` を満たす重みだけを順に検討する。`q=#\{j:t_j≤k\}` とする。`B_0:=θ`、`j=1,...,q` に対し

\[
 B_j:=\theta\max\{1,t_1,\ldots,t_j\}.\tag{3.6}
\]

`B_{j−1}≥θ` であり、帰納的に

\[
 B_j\le(r+1)\theta B_{j-1}\tag{3.7}
\]

を示す。`t_j≤B_{j−1}` なら、(3.6)から `B_j≤θ B_{j−1}` であり、これは(3.7)より強い。

`t_j>B_{j−1}` なら、根節点の長さ `k≥t_j`、すべての葉は `ℓ≤θ<t_j` である。そこで木において、**自分の長さが `≥t_j`、すべての子の長さが `<t_j`** である節点 `h` をとれる（該当する節点を根から下へ降りて選ぶ）。その各子 `z` には(3.4)の短い代表があるが、`ℓ_z<t_j` だからその代表に重み `≥t_j` の文字は出現できない。しかも `t_j>B_{j−1}≥t_{j−1}` なので、使える文字の最大重みは `max(1,t_1,...,t_{j−1})`。従って

\[
 \ell_z\le\theta\max(1,t_1,\ldots,t_{j-1})=B_{j-1}.\tag{3.8}
\]

(3.5)により

\[
 t_j\le\ell_h\le rB_{j-1}+\theta.\tag{3.9}
\]

`B_{j−1}≥θ` だから、(3.6)から

\[
 B_j\le\theta(rB_{j-1}+\theta)
       \le(r+1)\theta B_{j-1},
\]

これで帰納法が完成する。

**(C) 根の上界**。根 `S` にも(3.4)の短い代表がある。その重みは `k` であり、重み `>k` の文字は使われない。よって

\[
 k\le\theta\max\{1,t_1,\ldots,t_q\}=B_q.
\]

(3.7)を `q` 回反復して

\[
 k\le B_q\le (r+1)^q\theta^{q+1}
 \le(r+1)^{m-1}\theta^m,
\]

を得る。`q=0` の場合も `k≤θ` となり同様である。□

### 3.3 定理の正確な射程

単一のスカラー重み `λ` の**同一レベルに言語全体が含まれる**ことが本質的である。例えば全ての連結に対して

\[
 \lambda(w)=|w|_a+T_b|w|_b+T_c|w|_c=N
\]

を課して指数長の純粋 `a` 語を稀にする方法は、`T_b,T_c` を指数にしても、`θ=poly(n)` の reduced good 文法では実現できない。非負性を外した重み（正負の相殺）、語の位置に依存する重み、トークンの切れ目を認識してから符号に重みを与えるもの、複数の別レベルの和集合には定理を適用できない。

とりわけ、`d_i∈{b,c}^+` に対して `t_i=2^i` とする**トークン重み**は、通常 `λ(b),λ(c)` の線形結合 `t_i=λ(d_i)` では表現できない。従って§4–5は定理3.1を迂回しようとする自然な試みである。

## 4. 場合II：`b⁴,c⁴` を両方避ける接頭符号を試す

### 4.1 抽象模型

`n≥3`、`N=2^n` とし

\[
 d_i=(bc)^i bb\ (1\le i\le n),\qquad
 D_n=\{d_1,\ldots,d_n\},\qquad
 \mathrm{wt}(a)=1,\quad\mathrm{wt}(d_i)=2^i.\tag{4.1}
\]

`D_n` は接頭符号である。`i<j` のとき、先頭 `2i+1` 文字は一致するが、`d_i` の次の文字は `b`、`d_j` の同位置の文字は `c` で区別できる。トークン `a` も `b` で始まる符号とは区別でき、`\{a\}\cup D_n` は一意復号可能。

連結では `c` ランは長さ1、`b` ランは各トークン内部で最大2、トークン接続部で最大3。したがって**どの語も `b⁴,c⁴` を含まない**。`bc` の交互パターンの長さで指数重みを識別しようとする、場合II用の抽象模型である。

実際の有限言語を

\[
 F_n=\{t_1\cdots t_s:\ s\ge1,\quad t_j\in\{a\}\cup D_n,
\quad\sum_j\mathrm{wt}(t_j)=2^n\}.\tag{4.2}
\]

とする。トークン集合は有限で正の重みなので `F_n` は有限・正則、`a^{2^n}∈F_n` であり、これ以外に純粋な `a` 語はない。従って `μ_a(F_n)=2^n`。**ただし `F_n` は下で代入可能性に失敗する。**

### 4.2 全 `n≥3` の明示的な arity 1 違反

**命題4.1（接頭符号の境界漏れ）【証明済み】**。`F_n` は全 `n≥3` で `(1,c)`-代入可能でない。従って `F_n∉C_{2,c}`。

**証明**。`d_1=bcbb`、`d_2=bcbcbb=bc\,d_1` とする。一成分の比較語

\[
 x=d_1a^4,\qquad y=a^4d_1
\]

は共に内容 `{a,b,c}` を持つ。共通の一穴文脈

\[
 E=\square\,a^{N-6}
\]

では `E[x]=d_1a^{N-2}∈F_n`、`E[y]=a^4d_1a^{N-6}∈F_n` である。両者とも重みは `N`。

しかし別の一穴文脈

\[
 P=bc\,\square\,a^{N-8}
\]

では `P[x]=d_2a^{N-4}∈F_n`、一方 `P[y]=bc\,a^4d_1a^{N-8}∉F_n`。後者は先頭が `bca` であり、どの許容トークンも `a` 以外は `bcb` で始まるため、トークン分解不能だからである。`N≥8` なので全指数は非負。共通文脈があり分布が異なるので代入可能性に反する。□

**重要点**：この違反には `b⁴` や `c⁴` は一切不要。トークンが接頭符号で、`b,c` のランが一様に短く、完全に復号可能であっても、**内容型付けはトークンの途中の境界状態を記録しない**。この模型の障害は共役移送を持ち出す前の arity 1 で生じる。

### 4.3 反例候補と「成功例」の計算

標準ライブラリのみのスクリプト（付録A）は、有限言語の**全語**を実際に生成し、各 arity `1,2` の全ての非空成分の出現と許容文脈を列挙する。

- `F_3` は **56語**、`μ_a=8`、接頭符号であり、実際に arity 1 の違反が出る（上記命題が全 `n` に拡張する）。
- 対照として `L_5=(a|bc)^5` は **32語**。`a⁵` を含み `b⁴,c⁴` を含まないが、arity 1・2 とも違反なし。これは有限言語全体の判定であって、無限族を自動的に証明するものではない。`(a|bc)^+` 自身の代入可能性は前のClaude報告§4の別証明に対応する。
- 場合Iの `H_8`（式(2.5)）は **15語**、arity 1・2 とも違反なし。重みのみの全レベル集合 `\{w:|w|_a+2|w|_b+2|w|_c=8\}` は **171語**で同様に違反なし。

ここまでで**場合IIに指数重みの一意復号可能符号を作ること**と、**組代入可能な言語を作ること**が別問題であると厳密に切り分けられた。ただし、他の符号すべてが失敗するとは示していない。

## 5. 場合III：`c⁴` だけがある指数重みトークンの二穴違反

`n≥4`、`N=2^n` とし

\[
 d_i=bc^i b\quad(1\le i\le n),\quad
 D_n=\{d_i\},\quad
 \mathrm{wt}(d_i)=2^i,\ \mathrm{wt}(a)=1,\tag{5.1}
\]

および `J_n` を重み合計 `N` の全てのトークン連結語からなる有限言語とする。`D_n` は接頭符号、`μ_a(J_n)=N`。`d_4` が言語の語に現れるので `c⁴` は現れるが、どの連結語でも `b` ランは長さ2以下なので `b⁴` は現れない。

**命題5.1（場合IIIの明示的 arity 2 違反）【証明済み】**。`J_n` は全ての `n≥4` で `(2,c)`-代入可能でない。

**証明**。組

\[
 X=(c,cc),\quad Y=(cc,c)
\]

はいずれも成分内容が `({c},{c})`。まず

\[
 E=b\,\square_1\,c\,\square_2\,b\,a^{N-16}
\]

は許容二穴文脈で、`E[X]=E[Y]=d_4a^{N-16}∈J_n`。別の許容二穴文脈

\[
 F=b\,\square_1\,ccbbc\,\square_2\,b\,a^{N-16}
\]

を考えると

\[
 F[X]=d_3d_3a^{N-16}\in J_n,
 \qquad F[Y]=d_4d_2a^{N-16}\notin J_n.
\]

なぜなら前者のトークン重みは `8+8+(N−16)=N` だが、後者は `16+4+(N−16)=N+4`。接頭符号なので後者に別の復号はない。`E,F` の穴間部分はそれぞれ `c` と `ccbbc` で**確実に非空**。よって分布が等しくない。□

この命題は §2 の `c` 再配分が `d_3d_3` と `d_4d_2` を同じ `c` 骨格と総数で結ぶことを、有限の許容二穴文脈によって直接証明書にしたもの。前回の離散アフィン制約の一般形より強いとは主張しない。

小例 `n=4` では全言語に **5,272語**ある。上の4つの充填語の所属・非所属をコードで確認した。これは一般の `n` に対する上の記号的証明とは独立の実装確認である。

## 6. 未解決の部分と、次に絞るべき一点

### 6.1 何がまだ足りないか

**場合I**：正規形(2.2)は証明できたが、それは「同一骨格内で各文字の長さを動かせる」という**条件付き自由度**である。任意の短い代替生成組 `ω_B` に対し、異なる骨格にまたがって重みを足し合わせる比較が可能とは限らない。`H_8` は、4乗が全てあっても隣接交換が全て成立するわけではないことを示す。従って現時点では `μ_a(L)≤poly(g,θ)` の**無条件の証明はない**。

**場合II**：`(bc)^i bb` という、4乗を完全に回避する二進符号でも失敗することが分かった。しかし失敗原因は符号の一般的な不可能性ではなく、`d_2=bc d_1` と `a` との並置が作る**境界状態の非整合**である。他の接頭符号あるいは境界状態を埋め込んだ文法が全て失敗するとは証明していない。

**場合III**：`bc^i b` の指数重みが `c` 再配分で壊れるのは明白になったが、これだけでは一般の混合4乗場合の肯定も否定も解決しない。

### 6.2 次の一点（推奨）

純粋 `a^k` の最小導出から得る各短縮代替の**隙間符号**について、**同じ内容型の因子が「トークン境界の前後」で共通文脈を持てる条件**を定式化し、次の二択を狙う。

1. 長い重みを担う二つの代替符号の間で、arity 1 の境界交換（§4型）か arity 2 のラン再配分（§5型）が生じ、`a` の個数差が `0<δ<μ_a` になることを証明する。
2. そのいずれも避ける**実現可能な**重み付き符号と小さい reduced good 文法を構成する。

単なる抽象的な一意復号・加法性・ラン長制限だけでは結論に届かない。**文脈がどの短縮代替を共有するか**という分布上の実現可能性を、符号の定義に最初から組み込むべきである。

### 6.3 下界・作用素についての厳密な声明

本報告には `Σ={a,b,c}`、fan-out `≤2`、rank `≤2` で、`‖G_n‖,θ̄_{G_n}=poly(n)` かつ `μ_a(L_n)=n^{ω(1)}` を満たす `L_n∈C_{2,c}` **の構成はない**。従って以下のどれについても、今回新しい超多項式・指数下界を証明したとは主張しない。

- ランク上限つき作用素 `\mathcal B^{\le r}_{2,c}`（特に `r=2`）。
- ランク上限なし作用素 `\mathcal B_{2,c}`。
- `C_{2,c}` のクラス全体で特徴標本を持つ、任意の集合駆動作用素。

`prop:rare-type` を使うための前提、すなわち**代入可能で小さな文法を持つ稀な型の族**が得られていない。逆に §3 の上界は **`μ_a` という一つの長さの上界**に過ぎず、全型付き非終端の代表長や上記作用素の全特徴標本長まで直接は主張しない。「境界がファンアウトで動く」という結論も主張しない。

## 7. 先行研究と新規性の状態

定義・学習モデルの直接の出典は Yoshinaka, *Efficient learning of multiple context-free languages with multidimensional substitutability from positive data*, *Theoretical Computer Science* 412(19) (2011), 1821–1831, DOI `10.1016/j.tcs.2010.12.058`、および原稿 `main.tex`。4乗移送は添付のClaude 2026-11-01報告§3.1を独立に再証明したもの。符号 `bc^i b` の離散アフィン障害は前回ChatGPT報告 §4 と重なる。

**定理3.1**（任意の reduced good MCFG・非負加法重みの単一レベル・厚さの `m` 次上界）と**命題4.1**の具体的な接頭符号スキーマの文献上の新規性は**未確認**。限られた公開検索から同一の定理は特定できなかったが、既知の結果の特殊化である可能性を否定しない。「新定理」という表現は、この**報告内で新たに証明した定理**という意味に限定する。

## 付録A. Python 3 標準ライブラリによる検査・抽象模型（全文）

以下を `weighted_codes_check_2026-11-02.py` に保存し、Windows では `py -3 weighted_codes_check_2026-11-02.py`。`check_finite` は**有限言語の全語を列挙できている場合に限り** arity 1・2 の完全判定となる。`code_collision` はトークン列の Parikh／骨格と重みの衝突だけを見る**別個の抽象模型検査**で、言語の代入可能性判定ではない。`check_parametric_certificates` は個別の `n` について一般証明書をコードで点検するものであり、有限個の実行そのものは一般証明にならない。一般証明は§4.2、§5に書いた。

```python
#!/usr/bin/env python3
"""Exact finite arity-1/arity-2 content-substitution tests and code checks.
Windows: py -3 weighted_codes_check_2026-11-02.py
Pure Python 3 standard library. Between arity-2 holes a nonempty separator
is required. No negative tests are restricted to bounded observations:
finite languages are generated in full and exhaustively checked.
"""
from collections import defaultdict
from functools import lru_cache
from itertools import product


def occurrences(w, arity):
    n = len(w)
    if arity == 1:
        for i in range(n):
            for j in range(i + 1, n + 1):
                yield (w[i:j],), (w[:i], w[j:])
    elif arity == 2:
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    for ell in range(k + 1, n + 1):
                        yield (w[i:j], w[k:ell]), (w[:i], w[j:k], w[ell:])
    else:
        raise ValueError('arity must be 1 or 2')


def fill(context, tup):
    if len(tup) == 1:
        return context[0] + tup[0] + context[1]
    return context[0] + tup[0] + context[1] + tup[1] + context[2]


def type_of(tup):
    return tuple(frozenset(x) for x in tup)


def check_finite(words, max_arity=2):
    """Exact iff ALL words of a finite language are provided. Return witness or None."""
    language = set(words)
    for arity in range(1, max_arity + 1):
        dist = defaultdict(set)
        for w in sorted(language):
            for tup, ctx in occurrences(w, arity):
                dist[tup].add(ctx)
        common = defaultdict(list)
        for tup, contexts in dist.items():
            for ctx in contexts:
                common[(type_of(tup), ctx)].append(tup)
        checked = set()
        for (typ, ctx), ts in sorted(common.items(), key=str):
            ts = sorted(set(ts))
            for i, x in enumerate(ts):
                for y in ts[i+1:]:
                    if (x,y) in checked:
                        continue
                    checked.add((x,y))
                    if dist[x] == dist[y]:
                        continue
                    for src, dst in ((x,y),(y,x)):
                        for context in sorted(dist[src]):
                            reject = fill(context,dst)
                            if reject not in language:
                                return {
                                    'arity': arity, 'type': typ, 'x': src, 'y': dst,
                                    'common': ctx, 'separating': context,
                                    'accepted': fill(context,src), 'rejected': reject,
                                }
        print('  arity', arity, 'checked; distinct tuples', len(dist))
    return None


def additive_fiber(N, weights):
    alphabet = tuple(sorted(weights))
    @lru_cache(None)
    def go(left):
        if left == 0:
            return ('',)
        return tuple(x+s for x in alphabet if weights[x]<=left for s in go(left-weights[x]))
    return tuple(w for w in go(N) if w)


def prefix_free(tokens):
    return all(not y.startswith(x) for i,x in enumerate(tokens)
               for j,y in enumerate(tokens) if i != j)


def weighted_code_fiber(N, code_and_weights):
    tokens = tuple(sorted(code_and_weights))
    @lru_cache(None)
    def go(left):
        if left == 0:
            return ('',)
        return tuple(t+s for t in tokens if code_and_weights[t]<=left
                     for s in go(left-code_and_weights[t]))
    return tuple(w for w in go(N) if w)


def code_collision(tokens, weights):
    """Abstract equality of Parikh vectors of two-token concatenations,
    but inequality of prescribed weights. This is NOT an L-membership test."""
    seen = {}
    for x,y in product(tokens, repeat=2):
        w=x+y
        key=(tuple(w.count(ch) for ch in 'bc'),
             ''.join(ch for i,ch in enumerate(w) if i==0 or ch!=w[i-1]))
        weight=weights[x]+weights[y]
        if key in seen and seen[key][2] != weight:
            return (seen[key], (x,y,weight),key)
        seen[key]=(x,y,weight)
    return None


def decode_weight(w, token_weights):
    """Exact sum for prefix-free tokens (or None for malformed input)."""
    tokens=sorted(token_weights, key=len, reverse=True)
    i=0
    weight=0
    while i<len(w):
        match=[t for t in tokens if w.startswith(t,i)]
        if len(match)!=1:
            return None
        t=match[0]
        weight+=token_weights[t]
        i+=len(t)
    return weight


def check_parametric_certificates():
    for n in range(3,8):
        N=2**n
        tokens={'a':1,**{('bc'*i+'bb'):2**i for i in range(1,n+1)}}
        d1='bcbb'
        x=(d1+'aaaa',)
        y=('aaaa'+d1,)
        E=('','a'*(N-6))
        F=('bc','a'*(N-8))
        assert decode_weight(fill(E,x),tokens)==N
        assert decode_weight(fill(E,y),tokens)==N
        assert decode_weight(fill(F,x),tokens)==N
        assert decode_weight(fill(F,y),tokens) is None
    print('  CASE II arity-1 analytic certificates checked n=3..7')
    for n in range(4,8):
        N=2**n
        tokens={'a':1,**{('b'+'c'*i+'b'):2**i for i in range(1,n+1)}}
        x=('c','cc'); y=('cc','c')
        E=('b','c','b'+'a'*(N-16))
        F=('b','ccbbc','b'+'a'*(N-16))
        assert decode_weight(fill(E,x),tokens)==N
        assert decode_weight(fill(E,y),tokens)==N
        assert decode_weight(fill(F,x),tokens)==N
        assert decode_weight(fill(F,y),tokens)==N+4
    print('  CASE III arity-2 analytic certificates checked n=4..7')

def main():
    # Case I: all a^4, b^4, c^4 occur.
    L=additive_fiber(8,{'a':1,'b':2,'c':2})
    print('CASE I: |L|=',len(L),'a^8,b^4,c^4 present=',all(x in L for x in ('a'*8,'b'*4,'c'*4)))
    print('  exact check:',check_finite(L))
    L_sorted=tuple(w for w in L if w == ''.join(sorted(w)))
    print('CASE I ordered intersection: |L|=',len(L_sorted),
          'contains a^8,b^4,c^4=', all(x in L_sorted for x in ('a'*8,'b'*4,'c'*4)))
    print('  exact check:',check_finite(L_sorted))

    # Case II: a finite token-count slice of (a|bc)^+; b,c runs <=1.
    L=weighted_code_fiber(5,{'a':1,'bc':1})
    print('CASE II, (a|bc)^5: |L|=',len(L))
    print('  exact check:',check_finite(L))

    # Bounded-run prefix codes; concatenating tokens gives b-runs <=3, c-runs <=1.
    d={i:'bc'*i+'bb' for i in range(1,4)}
    weights={'a':1, **{d[i]:2**i for i in d}}
    L=weighted_code_fiber(8,weights)
    print('CASE II exponential prefixes: prefix free=',prefix_free(list(d.values())))
    print('  |L|=',len(L),'min pure a=',min(len(w) for w in L if set(w)=={'a'}))
    print('  exact check:',check_finite(L))

    # Mixed case: d_i=bc^i b; c^4 occurs, b^4 does not.
    d={i:'b'+'c'*i+'b' for i in range(1,5)}
    weights={'a':1, **{d[i]:2**i for i in d}}
    L=weighted_code_fiber(16,weights)
    print('CASE III: prefix free=',prefix_free(list(d.values())))
    print('  |L|=',len(L), 'c^4 witness=',d[4] in L,
          'b^4 anywhere=',any('bbbb' in w for w in L))
    assert 'bccccb' in L and 'bcccbbcccb' in L
    E=('b','c','b')
    F=('b','ccbbc','b') # gives d3d3 for (c,cc)
    x=('c','cc');y=('cc','c')
    print('  arity2 explicit E[x,y]=',fill(E,x),fill(E,y))
    print('  arity2 explicit F[x,y]=',fill(F,x),fill(F,y))
    print('  acceptance=',fill(E,x) in L,fill(E,y) in L,fill(F,x) in L,fill(F,y) in L)
    print('  abstract Parikh/skeleton collision:',code_collision(tuple(d.values()),weights))
    check_parametric_certificates()

if __name__=='__main__':
    main()
```

### 実行記録（2026-11-02）

```text
CASE I: |L|= 171 a^8,b^4,c^4 present= True
  arity 1 checked; distinct tuples 340
  arity 2 checked; distinct tuples 533
  exact check: None
CASE I ordered intersection: |L|= 15 contains a^8,b^4,c^4= True
  arity 1 checked; distinct tuples 54
  arity 2 checked; distinct tuples 90
  exact check: None
CASE II, (a|bc)^5: |L|= 32
  arity 1 checked; distinct tuples 139
  arity 2 checked; distinct tuples 637
  exact check: None
CASE II exponential prefixes: prefix free= True
  |L|= 56 min pure a= 8
  exact check: arity=1 の違反を検出（実際の完全な辞書形式の出力は実行により異なることがある）
CASE III: prefix free= True
  |L|= 5272 c^4 witness= True b^4 anywhere= False
  arity2 explicit E[x,y]= bccccb bccccb
  arity2 explicit F[x,y]= bcccbbcccb bccccbbccb
  acceptance= True True True False
  abstract Parikh/skeleton collision: (('bcb', 'bcccb', 10), ('bccb', 'bccb', 8), ((4, 4), 'bcbcb'))
  CASE II arity-1 analytic certificates checked n=3..7
  CASE III arity-2 analytic certificates checked n=4..7
```

**最終判定**：場合Iの（骨格, Parikh）正規形は肯定、非負加法的一定重み族の純粋語には `O_r(θ³)` の新しい**部分上界**が得られた。場合II/IIIの指数重み接頭符号候補は明示的文脈で失敗した。三文字 `C_{2,c}` 全体の `μ_a` 上界と `op:fanout-two` は**未解決**。

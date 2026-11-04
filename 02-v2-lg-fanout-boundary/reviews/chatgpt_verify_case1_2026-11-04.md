# 場合 I の多項式上界（定理 I）の独立検証と、場合 II・III への帰結

**研究日**：2026-11-04  
**位置づけ**：系列第十四報、ChatGPT による独立検証。論文 #2 の中心問題 `op:fanout-two` の三文字内容型付けに関する検証ノート。  
**判定上の約束**：「独立に確認」は、参照報告の結論を採用したという意味ではなく、定義から証明の必要な交換を再構成したという意味である。ただし、この報告は形式証明支援系による原稿全体の機械検証ではない。

## 0. 主張ごとの判定

| 主張 | 判定 | 内容・限界 |
|---|---|---|
| 原稿の許容文脈、非空成分、good 表示、一様な最小導出 (U) | **独立に確認** | 原稿の定義と、最短純粋語の最小節点導出から再導出。 |
| 補題2.1、正の `a`-連の再配分 | **独立に確認** | arity **2** の共有文脈 `□₁a□₂` を必ず使用する。 |
| 補題 F′ と系 C | **独立に確認** | arity 2 から得た再配分と arity 1 を使用。有限言語での追加検査あり。 |
| 補題 E、SB₂、補題 E₂ | **独立に確認** | 証拠文脈と各成分の内容・中央の非空性を点検。 |
| 補題 T | **独立に確認** | 同名節点の反鎖性、区間順、分離の証拠を点検。区間38,610例を独立全数検査。 |
| 補題 N | **独立に確認** | 中央の一穴交換→外殻の二穴交換→収縮の順で再証明し、詰め物の予算を算出。 |
| 定理 S と命題 (R)（場合 I） | **独立に確認** | 各文字の4乗から連長を移送し、`0<|w|_a<k` の差を排除。 |
| 補題 P*、補題 Q | **独立に確認** | 異なる個数の多重集合の比較、回路の係数、34細類と `n'` の式を点検。798,000個の小さな入れ子を独立検査。 |
| 一色型の例外計数、補題3.1・3.2 | **独立に確認** | `18v+vθ`、次の例外 `2v+50θ³v+3v`、疎な尺度の数え上げを確認。 |
| **定理 I（場合 I の純粋 `a` 語の上界）** | **独立に確認** | 下記の全依存関係に対する数学的検証。形式証明全体を機械化したという意味ではない。 |
| Part D の76段の `a³⁹` 証明書 | **独立に確認** | 新しく書いた推論生成器と、種だけから始める別の全段再生による確認。非線形／線形の両設定を確認。 |
| 同一内容の殻が同じ細類に属するなら型 `τ` が等しい | **独立に確認** | 細類の第1座標に各成分の内容が含まれる。 |
| 場合 I の他の単一文字型 `{b}`, `{c}` の最短純粋語 | **証明済み（定理 I の系）** | 各純粋語が存在する場合、文字名を置換して同じ上界。 |
| 場合 I の複数文字型 `m` の `μ_m` への適用 | **未解決** | 純粋最小導出、一様な単一文字 `a`-連、(R) に代わる不変量が欠ける。 |
| 場合 II・III の一般の多項式上界／超多項式反例族 | **未解決** | 後述の局所制約と有限候補の失敗のみ。 |
| `L_n=(a\mid bc\mid cb)^n` (`n≥2`) が `(2,c)`-tuple-substitutable という候補 | **反証** | 全ての `n≥2` で arity 1 に反する4語証明書。 |
| 「補題 F′ は arity 1 だけから得られる」という強化 | **反証** | `{a⁶,b⁴,c⁴,aabacaa}` は arity 1 を満たすが F′ に反する。arity 2 は満たさない。 |
| `h≤v`、跨ぐ節点が少なければ既知の個数上界が使える | **自明に成り立つが目的には足りない** | `h` が指数に入るままでは多項式上界は出ない。 |
| 新しい補題・定理 I の文献上の新規性 | **確認できず** | 既存の代入可能性／MCFG substitution lemma と同一とは確認されていない。 |

## 1. 照合した正本と量化

GitHub の `growupkuriyama-hub/Papers` の `02-v2-lg-fanout-boundary/main.tex` を GitHub 接続から取得した。**Git blob SHA は `b72cd2ed648f802886f0ab7c60a72f9f40c0864b`**。`claude_straddle_2026-11-04.md` (`7e200775...`)、`claude_cross_core_2026-11-04.md` (`e7876722...`)、`claude_f_branching_2026-11-04.md` (`8877e715...`)、`chatgpt_weighted_codes_2026-11-02.md`、`chatgpt_a_spectrum_2026-11-03.md`、`chatgpt_nested_bc_chain_2026-11-04.md` をそれぞれ取得した。原稿の `def:tuple-occurrence`、`def:tuple-substitutable`、`lem:thickness-equivalence`、`prop:rare-type`、`op:fanout-two`、`app:two-letter-content` を照合した。これは先行報告の「検証済み」という評価を根拠として再利用したものではない。

原稿の `d`-穴文脈は `v₀□₁v₁⋯□_d v_d` で、**内部の固定部分 `v₁,...,v_{d−1}` は非空**である。比較される成分も非空。`good` は λ-free、nondeleting、nonpermuting、nonmerging である。したがってファンアウト2の各成分は非空、二成分の間には導出後も少なくとも1文字が残る。これらは T・E₂・N で必須となる。

以降 `Σ={a,b,c}`、内容型付け `c`、`L∈C_{2,c}`、`G` は `L∩Σ⁺` の reduced good なファンアウト `≤2`、ランク `≤r` の表示、`v=|V|`、`θ=θ̄_G≥1`、`k=μ_a(L)≥5`。`T` は `a^k` の成功導出で節点数最小のものとする。以下で得る結論は**指定された純粋語の最小長**に関するものであり、一般の特徴標本長を抑える定理ではない。

### 1.1 一様化の最小性を確認

同ラベル `X` の二出現で純粋 `a` の総出力長が異なるなら、長い出現を短い出現の部分導出に替えて、`0<k'<k` の `a^{k'}` が生成できる。これは `k` の最小性に反する。よって総長 `ℓ_X` は同名出現間で一定。総長が等しく節点数が異なるなら、節点数の多い方の交換は `T` の最小性に反する。各ラベルで最小節点形を固定し、子の節点数の厳密減少で非巡回に統一できる。**成分ごとの `a` 長の一致までは不要**。同名出現は祖先関係を持てず、反鎖となる。根葉経路長は `v` 以下。

## 2. 補題2.1・F′・C の検証

`p a⁴q∈L` を一語選ぶ。組 `x=(a,aa)` と `y=(aa,a)` はどちらも成分内容 `({a},{a})`。許容文脈 `p□₁a□₂q` が両者を `pa⁴q` に写すので、arity 2 の代入可能性からその分布が等しい。したがって `z≠ε` に対し

`U a z aa V ∈ L  ⇔  U aa z a V ∈ L`。

隣接する極大 `a`-連の正の長さは、この一文字移送で任意の正整数組成へ変換できる。この構成は **arity 1 だけでは出ない**。

**F′ の一段を具体的に再構成する。** `W=P a^p u a^q v Q` の総 `a` 数が連数より少なくとも1多いなら、まず再配分して左連を `p≥2`、消す右連を `q=1` とできる。ここで `u` は非空で、当該連を隔てる部分、`v` は `a` で始まらない。`a²u` と `aua` は同内容を持つ。文脈

`E₀=P a^{p−2} □ a v Q`

は `a²u` を `W` に、`aua` を一文字移送後の受理語に写す。よって `D(a²u)=D(aua)`。次の文脈

`E₁=P a^{p−1} □ v Q`

は `aua` を `W` に写すので、`a²u` にも適用できて `P a^{p+1}uvQ∈L` を得る。これで間の `a`-連を一本消した。最初の総 `a` 数は不変で連数のみ減るから、同じ操作を繰り返すと系 C が従う。最後の二連を任意の正長に再配分して `a^s F(w) a^t∈L` (`s+t=|w|_a`) が得られる。

**反例探索の重要な境界**：`L₀={a⁶,b⁴,c⁴,aabacaa}` は有限なので正則であり、コードで全許容一穴文脈を確認すると `(1,c)`-substitutable である。しかし `aabacaa` の3本の `a`-連は長さ `(2,1,2)` で、総数5、連数3。F′なら間の連を消して `a^sbc a^{5−s}` (`1≤s≤4`) のいずれかが入るはずだが、いずれも `L₀` にない。実際 `L₀` は arity 2 を満たさない。組 `(a,aa)` と `(aa,a)` が `□₁aa□₂a` を共有し、`□₁b□₂caa` が後者の `aabacaa` だけを受理する。したがって **F′ の正しい仮定は arity 2 を含むもの**であり、Claude の元の定理にはこの仮定があるから、これは定理 I の反例ではない。

## 3. SB₂・E₂・T・N の検証

`SB₂((A,B),e)` は `A,B∈{b,c}⁺` に対し、`s,g,t≥1`、`s+g+t=k−e` の全てで `a^s A a^g B a^t∈L` となる性質。内部の両側型ラベルを短い代表に替え、各成分の内部の `a`-連だけを F′ で消して、二成分間の `a`-連は残せば SB₂ が従う。必要な正の `a`-連と余剰は `k−ℓ_X≥θ+2` で確保できる。

### 3.1 E₂ の許容文脈

`e≤e'≤k−4`、`c(A)=c(A')`、`c(B)=c(B')`、各殻の SB₂ を仮定する。`g+t=k−e'−1`、`g,t≥1` と選び

`E=□₁ a^g □₂ a^t`

とする。内部固定部分 `a^g` は非空。`E[(a^{1+e'−e}A,B)]` の総 `a` 数は `k−e`、`E[(aA',B')]` は `k−e'`。双方 SB₂ により受理され、組の**成分ごとの内容**は一致する。したがって

`D²(a^{1+e'−e}A,B)=D²(aA',B')`。

同じ「全体の内容」だけでは不十分であり、細類が成分内容を保持することが Q で必要である。

### 3.2 T の区間配置、同時置換、分離

同名2出現は T 上で反鎖なので、代表 `ρ_X` への同時置換が文法上正当である。出力成分が互いに素で、範囲が重なる2個のファンアウト2出現を左から並べると、4成分の **成分番号** は `1,1,2,2` となる（節点番号は混在してよい）。これは手で6通りの節点別並べ方を分け、さらに独立プログラムで切断位置13点上の38,610配置を全数照合した。

置換後の非 `a` 文字数は高々 `2θ`。`k−2ℓ_X≥2θ+4` なので、`a`-連を分けるための余剰がある。隣接した非 `a` 因子の間に `a` を**挿入する**ときには F′ を逆向きに勝手に使ってはいけない。必要な証拠 `D(a²U)=D(aUa)` は、対象の短い塊 `U=F_X` には SB、`U=A_X` または `B_X` には SB₂ から、余剰 `a` を左に集めて得られる。ここを独立に点検した。結果として範囲が素または片側型なら二塊の語、両側型かつ範囲が交われば `a A a A a B a B a` 型板が得られる。

### 3.3 N の交換順と `a` の予算

`S₀=(A₀,B₀)` の型板から、まず中の **2番目の A₀ と1番目の B₀ の間の `a`-連**を F′ で消し、`A₀ | F₀ | B₀` (`F₀=A₀B₀`) を作る。`F₀` 自身は SB₂ を収縮すれば `SB(F₀,e₀)` を持つ。

帰納法の内側 `Q=A₂…A_m P B_m…B₂` は `SB(Q,d_Q)`、`d_Q=Λ−e₁`。**先に一穴交換 E** で中央の `F₀` を `Q` に替える。**その後、二穴交換 E₂** で外殻 `(A₀,B₀)` を `(A₁,B₁)` に替える。最後に系 C で区切り `a` を消し、`SB(A₁QB₁,e₁+d_Q)` とする。

必要な詰め物も明示できる。`e₀≤k/8`、`Λ=e₁+d_Q≤k/2`、`k≥4θ+12≥16`。中央交換の前は `k−2e₀` 個の `a` があり、`d_Q>e₀` なら追加で `d_Q−e₀` 個を中央の左連に集める。残りは

`(k−2e₀)−(d_Q−e₀)=k−e₀−d_Q≥3k/8≥6`。

外殻交換の前は `k−e₀−d_Q` 個あり、`e₁>e₀` なら追加で `e₁−e₀` 個を外殻の左連に集める。残りは

`(k−e₀−d_Q)−(e₁−e₀)=k−Λ≥k/2≥8`。

追加詰め物が不要な向きでは、上記以上の余裕がある。したがって各時点の4本の正の `a`-連を確保でき、両方向の交換を正しく実行できる。E₂ で必要な `e,e'≤k−4`、E で必要な `d,d'≤k−3` も満たす。**任意の型の殻を交換するのではなく、型 `τ` が同じ殻のみ**。帰納法に隠れた arity 2 の非許容文脈は見つからなかった。

## 4. (R)、P*、Q の再構成

### 4.1 場合 I の (R)

`a⁴,b⁴,c⁴` が L の語の因子として現れるとき、各文字について連長再配分が可能。同じ全文字連骨格 `σ` と Parikh ベクトルを持つ2語は受理が一致する。2語の `σ` と `b,c` 個数が等しく、`a` 個数だけ δ 違うなら、b・c の連長をそれぞれの正整数組成により合わせてから定理 S を適用できる。定理 S の初歩部分は、`0<δ<k` なら `D(a)=D(a^{1+δ})` から `a^{k−δ}∈L` となる矛盾である。よって `0<|w|_a,|w'|_a<k` では **δ=0**。この結論が (R) であり、場合 II・III にそのまま強化できるわけではない。

### 4.2 P*、多重集合の個数が違ってもよい理由

分岐 (B) の二塊の語と E・F′ を使い、損失総和が `≤k/2` の任意の短い鎖を SB にする。`F_X` の先頭 `f` と連数 `n` の偶奇が同じ類にあれば、鎖の連数は偶数類で `Σ n_X`、奇数類で `Σ(n_X−1)+1`。**鎖の因子数は式に残らない**。ゆえに `(n',β,γ)` の和が等しい多重集合を、因子数の違いに関係なく (R) で比較できる。

### 4.3 Q、34細類、定数項の消失

一つの殻の側の記述子は `(内容,先頭,末尾)`。`{b}` 側1通り、`{c}` 側1通り、`{b,c}` 側4通り、計6。二側で36、両側が `{b}` の組と両側が `{c}` の組を除き34細類。これは**型 `τ=(c(A),c(B))` を決める**。

ある細類 π の殻 `S=(A,B)` について

`n'(S)=n(A)+n(B)−[last(A)=first(A)]−[last(B)=first(B)]`。

同一細類の `S₁,…,S_m` を `P` のまわりに入れ子にした `F=A₁…A_m P B_m…B₁` (`m≥1`) の先頭は `first(A)`。接合の連が融合する個数を一つずつ数えると

`n(F)=Σ_i n'(S_i)+c_π(P)`、

`c_π(P)=n(P)−[last(A)=first(P)]−[last(P)=first(B)]+[last(A)=first(A)]+[last(B)=first(B)]`。

**個数 m に依存する補正項は残らない。** 特に `P` を固定した二つの（個数が違ってもよい）非空殻多重集合で、`Σ(n',β,γ)` が等しければ、入れ子語の `(σ,|.|_b,|.|_c)` は等しくなる。両方の損失総和と中心損失を足して `≤k/2` として N を使い、(R) から両側の損失和が一致する。

線形代数の点も補強した。各ベクトルは `u_X=(n'_X,β_X,γ_X)∈[0,θ]×[1,θ]²∩ℤ³`。有理数体上の核は最小従属集合（回路）により張られ、各回路の台は高々4、整数係数の絶対値は行列式の展開で高々 `6θ³`。`β,γ>0` だから、非零回路の正側・負側はいずれも空でなく、片側の多重集合の要素数は高々 `4·6θ³=24θ³`。中心の1殻相当と合わせて `24θ³+1≤25θ³=N`、かつ各損失は `≤k/(2N)` なので N の予算 `Λ≤k/2` に収まる。回路の全てに損失線形汎関数が0となるため、損失ベクトルは行空間に入り、**各細類で定数項なしの** `d_X=⟨φ_π,u_X⟩` が得られる。

これは三文字で `b,c` の両方が飽和している場合の証明であって、場合 II の `σ_a` には使えない。

## 5. 定理 I の例外、二分岐、数え上げ

`N=25θ³`、低い両文字型ラベルを `ℓ_X≤k/(2N)`、関係のあるラベルを「低く、内部出現を2個以上持つ」とする。二塊の SB 語があるか否かで (B)/(S) は**排他的かつ網羅的**に分かれる。(S) なら T により関係のある全ラベルは両側型で型板を持つ。内部出現が1個以下の低いラベルは、内部1個と両端に触れる高々2個を合わせ **高々3出現**で例外にできる。

| 例外 | 節点数の上界 |
|---|---:|
| 一色型・非飽和（各深さ、各色9個、深さ≤v） | `18v` |
| 一色型・飽和だが非頻出 | `vθ` |
| 両文字型・内部でない出現 | `2v` |
| 両文字型・高い出現（各深さ `<2N`） | `2Nv=50θ³v` |
| 低い内部出現が1個以下のラベル | `3v` |
| **合計** | **`E_I=v(50θ³+θ+23)`** |

「同じラベルの出現は反鎖」を使うので内部でない出現の個数はそのラベルにつき左右端の各1個以下。高い節点は同一深さでは互いの出力が素で、その出力長 `ℓ_X>k/(2N)` のため個数 `<2N`。一色型の `18v` は `L_x=L∩{a,x}⁺` に元の arity 1・2 代入可能性が継承されることと、原稿の二文字補題に依存する。飽和色で頻出の損失比は `d_B/q_B=α_x` という各色共通値になり、その値は1次元の格子点 `q_B∈[1,θ]` で記述できる。両文字型と交換しない論法なので混合型の多さに依存しない。

非例外の重い節点の長さ `ℓ_X` は、それぞれ整数格子点における線形関数 `d_X` または `α_x q_X` の窓 `[D,D+θ]` にある。前報の補題3.1の「芯」数え上げから、隣接尺度比は `K=(2v+E_I)(2r+1)` 以下。補題3.2では尺度が `R=θ+2v+2` 倍以上で増える鎖の非先頭値 `z_i` に対して、`0,…,R'` (`R'=θ+2v`) の係数による部分和が全て異なる。他方、各区分の格子点座標和だけでその値が決まり、`(R'+1)^M≤(MR'θ+1)^D`、`M≤v−1` より `M<3D` （`M=0` は別途自明に処理）。従って `k≤K^{3D+1}R^{3D}θ`。

- (B)：一色型2区分＋偶奇4区分各3次元、`D=2+4·3=14`。
- (S)：一色型2区分＋殻34細類各3次元、`D≤2+34·3=104`。

したがって **場合 I** に限り、全ての表示 `G` に対して

`μ_a(L) ≤ max{4θ+12, K_I^{313}R^{312}θ}`、

`K_I=(2v+E_I)(2r+1)`, `E_I=v(50θ³+θ+23)`, `R=θ+2v+2`。

境界 `k≤4θ+12` は自明な側として処理する。`k>4θ+12` で上の証明を適用する。この検証の範囲では、定理 I に致命的な反例または条件の欠落は見つからなかった。なお定理を **全ての content type の `μ_m` や特徴標本長**に言い換えることは許されない。

## 6. 他の稀な内容型への射程

内容型の非空集合は `{a}`,`{b}`,`{c}`,`{a,b}`,`{a,c}`,`{b,c}`,`{a,b,c}`。場合 I で `a^k` があるため、`a⁴,b⁴,c⁴` は全て L の語の因子として現れる。ここで単一文字 `x∈{a,b,c}` の純粋語が L に存在すれば、`x^j` の最小長 `j≥5` に対して残り2文字の4乗があるため、文字を置換した定理 I が適用できる。`j≤4` は自明。したがって**存在する単一文字型の最短語は3種類とも同じ多項式で抑えられる**（新しい複雑な証明を要しない系）。

一方、`m={a,b}` などの複数文字型は未解決。最小の `m`-型語の導出は純粋な同一文字ではないため、(i) ラベルごとの出力を単一の `a` 長 `ℓ` にまとめて比較すること、(ii) `a` の連に余剰を集めること、(iii) 混合型代表から生じる殻を `k−Σd` 一つで比較すること、がそのまま成立しない。二文字部分言語への制限は代入可能性を保つが、元文法の**通常厚さ `θ̄_G` を多項式で保った reduced good 表示**が得られることはここでは証明していない。ゆえに原稿 `prop:rare-type` に必要な全ての `μ_m` の評価が済んだとは言えない。

## 7. 場合 II・III：新たに絞れた点、反例候補の排除

`b⁴,c⁴` がどちらも現れないのが場合 II、ちょうど一方だけが現れるのが場合 III。F′・E₂・T・N は `a⁴` と2穴代入可能性からできるので、形としては引き続き使用できる。ただし場合 II では `b,c` のラン長を移送できないため、(R) は**`a` を消した部分語の文字列自体が一致**する場合に限られる。34細類で `n'` が等しいことから語が一致するとは言えず、Q の橋は切れる。

### 7.1 損失の局所的な必要条件（証明済み、ただし上界ではない）

N により同じ殻 `(A,B)` を4層入れ子にできる低い関係ラベルを考える。場合 II において A または B が `x^j` (`x∈{b,c}`) 一連だけなら、4層の同一側に `x^{4j}` が現れてしまう。よって両側とも複数連を持つ必要がある。さらに同一側 `U` の末尾と先頭が同じ `x` で、末尾連長 `p` と先頭連長 `q` が `p+q≥4` なら、2層の `UU` の境界に `x⁴` が現れる。したがって **`p+q≤3` が必要**。分岐 (B) でも、任意に並べられる鎖の連続した塊 `P,Q` が同じ文字 `x` で接続する場合には `suffix_x(P)+prefix_x(Q)≤3` が必要である。場合 III では、4乗を欠く側の文字についてのみこの制限が適用される。

これらは `λ` の線形性ではなく、構成可能な局所境界への制約である。いくら多くの核があっても `bc`/`cb` など交代形なら全ての境界に矛盾するとは限らない。**ここから `μ_a` の多項式上界を出したわけではない**。

### 7.2 直接検査した失敗候補

`H_n=(a|bc|cb)^n` は任意の `n≥2` で有限・正則であり、純粋 `a^n` を含み、`b,c` の4乗は現れない。しかし **全ての `n≥2` で arity 1 を満たさない**。実際 `bc` と `cb` は同内容 `{b,c}`。文脈 `a^{n−2}□cb` は `a^{n−2}bccb, a^{n−2}cbcb∈H_n` を与える。一方 `a^{n−2}b□c` は `a^{n−2}bcbc∈H_n` を与えるが `a^{n−2}bbcc∉H_n`。よって全 `n` に対する代入可能性違反の明示的証明書である。コードは特に **`n=5` (`μ_a=5`)** の有限対象を完全判定した。この正則候補には `L_n∈C_{2,c}` の資格がなく、超多項式下界に流用できない。

対照として `H_n=(a|bc)^n` (`n=4,7`) は有限対象の**完全な所属判定**で arity 1 と2を満たした。これは無限族についての代入可能性を証明していない（この報告では `n=4,7` の結果のみ）。短い純粋 `a` 語を持つため、これらは下界候補ではない。

### 7.3 否定側の未達成条件を明示

超多項式特徴データ下界へ進むには、少なくとも `Σ={a,b,c}`、**ファンアウト≤2、ランク≤2** の reduced good 表示 `G_n` で `‖G_n‖,θ̄_{G_n}=n^{O(1)}`、`L_n∈C_{2,c}`（**arity 1 と2双方を省略せず証明**）および `μ_a(L_n)=n^{ω(1)}` が必要。小さい `n` の正確な所属判定器は補助であり、全 `n` の所属証明を代替しない。`□`/`□a` の漏れ、偶数塊、F′、E₂、鎖／入れ子、場合 I の (R) の各障害を同時に越える候補は今回構成できなかった。

仮にこの条件の族が構成できれば、`prop:rare-type` の量化は **`\mathcal B^{\le r}_{2,c}`、`\mathcal B_{2,c}`、およびクラス `C_{2,c}` 全体に特徴標本を持つ集合駆動作用素**に対して適用できる。これは「全ての学習器の計算時間」や「Gold 学習器の収束時点」の下界を意味しない。ファンアウト1や別アルファベットの下界も意味しない。したがって本報告は**新たな特徴データ下界を主張しない**。

## 8. 独立計算、再生可能性と結果

下のコードは Python 3 の標準ライブラリのみ使用。**`py -3 chatgpt_verify_case1_checks_2026-11-04.py`** で実行できる。全ての `assert` は説明した「arity 1・2 の内容一致」「二穴内部の固定部分は非空」「認識語・非認識語」「ラン数の恒等式」「証明規則の三前提」を直接判定している。

有限言語の検査は**全受理語の全許容文脈**を列挙し、共有文脈を持つ同内容組の分布が完全一致するかを判定する。検査語長を打ち切った「探索」ではなく、列挙した有限対象についての完全な判定である。`all_len6`、`sorted_weight8`、`all_order_weight8` は場合 I の例、`token4`,`token7` は場合 II の例。F′・C の実例は `all_len6`,`all_order_weight8`,`token7` で合計36個の局所収縮確認となった。これを無限言語の証明と呼ばない。

Part D は単なる出力照合ではなく、`k=40` の6つの初期種（純粋語、4つの殻の各1語、型板）から、**自作の推論生成器**が一穴・二穴交換に分解した履歴を作り、別のループが**初期種から各段の3前提と結論を再生**する。`(e₁,e₂,e₃,e₄)=(3,5,6,7)` は76段で `a³⁹` を証明する。`(3,5,6,8)` は71段で比較対象の `a` 数が等しいためこの経路から短語を得ない。後者は「短い純粋語が存在しない」の証明ではない。証明書は**これらの6種を全て含む任意の `C_{2,c}` 言語に対する条件付きの否定証明**であり、任意の非線形殻が必ずこの具体的な種を持つとの主張ではない。

### 実際の標準出力

```text
LANGUAGE all_len6 words 729 tuple1 (1092, 15309, 7798) tuple2 (1278, 25515, 12942) contractions 12 PASS
LANGUAGE sorted_weight8 words 15 tuple1 (54, 265, 238) tuple2 (90, 456, 289) contractions 0 PASS
LANGUAGE all_order_weight8 words 171 tuple1 (340, 3048, 1805) tuple2 (533, 4486, 2588) contractions 12 PASS
LANGUAGE token4 words 16 tuple1 (67, 344, 279) tuple2 (205, 681, 611) contractions 0 PASS
LANGUAGE token7 words 128 tuple1 (571, 7840, 4747) tuple2 (4489, 57624, 33727) contractions 12 PASS
NEGATIVE_CONTROL one-hole only: F-prime fails, arity-2 fails; PASS
NEGATIVE_CONTROL (a|bc|cb)^5: one-hole countercertificate; PASS
FORMAL_CERT k40 (3, 5, 6, 7) counts (26, 27) replayed steps 76 shorter pure word 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa' PASS
FORMAL_CERT k40 (3, 5, 6, 8) counts (26, 26) replayed steps 71 shorter pure word None PASS
CASE_T strict interval pairs 38610 PASS
CASE_Q shell classes 34 tested nests 798000 PASS
```

### 検査用ソース全文

```python
#!/usr/bin/env python3
"""Independent finite checks for chatgpt_verify_case1_2026-11-04.md.
Python 3 standard library only. Windows: py -3 chatgpt_verify_case1_checks_2026-11-04.py
All substitutability checks are exact for the enumerated *finite* languages.
No finite check proves any infinite language family belongs to C_(2,c).
"""
from collections import defaultdict
from itertools import combinations, product
from math import comb

ALPHA = "abc"

def typ(x):
    return frozenset(x)

def all_contexts(words, arity):
    """All observed positive tuples and their exact admissible distributions."""
    dist = defaultdict(set)
    for w in words:
        n = len(w)
        if arity == 1:
            for i in range(n):
                for j in range(i+1, n+1):
                    dist[(w[i:j],)].add((w[:i], w[j:]))
        else:
            # 0<=i<j<k<l<=n; j<k guarantees a nonempty fixed middle.
            for i in range(n):
                for j in range(i+1, n):
                    for k in range(j+1, n):
                        for l in range(k+1, n+1):
                            dist[(w[i:j],w[k:l])].add((w[:i],w[j:k],w[l:]))
    return dist

def exact_substitutable(words, arity):
    dist = all_contexts(words, arity)
    by_context = defaultdict(list)
    for tup, contexts in dist.items():
        sig = tuple(typ(x) for x in tup)
        for ctx in contexts:
            by_context[(sig, ctx)].append(tup)
    for (_,ctx), ts in by_context.items():
        x = ts[0]
        for y in ts[1:]:
            if dist[x] != dist[y]:
                witness = next(iter(dist[x] ^ dist[y]))
                return False, (x,y,ctx,witness)
    return True, (len(dist),sum(len(c) for c in dist.values()),len(by_context))

def factor_and_a_runs(w):
    factors = []
    runs = []
    i = 0
    while i<len(w):
        if w[i]=='a':
            j=i
            while j<len(w) and w[j]=='a': j+=1
            runs.append(j-i)
        else:
            j=i
            while j<len(w) and w[j]!='a': j+=1
            factors.append(w[i:j])
        i=j
    return factors,runs

def compositions(n,r):
    if r==1:
        if n>=1: yield (n,)
    elif 1<=r<=n:
        for cuts in combinations(range(1,n),r-1):
            q=(0,)+cuts+(n,)
            yield tuple(q[i+1]-q[i] for i in range(r))

def verify_contraction(words):
    """Checks the existential positive-run version of Corollary C exactly."""
    setwords = set(words)
    instances = 0
    for w in words:
        if not (w.startswith('a') and w.endswith('a')): continue
        factors,runs = factor_and_a_runs(w)
        N=sum(runs)
        if N<len(runs)+1 or len(factors)<2: continue
        for j in range(1,len(runs)-1):
            joined=factors[:j-1]+[factors[j-1]+factors[j]]+factors[j+1:]
            count=0
            for s in range(1,N):
                candidate='a'*s + ''.join(factors) + 'a'*(N-s)
                assert candidate in setwords,(w,candidate)
                count+=1
            assert count==N-1
            # Removing one internal a-run and redistributing all N a's.
            possible=False
            for lens in compositions(N,len(runs)-1):
                out='a'*lens[0]
                for j2,fac in enumerate(joined): out+=fac+'a'*lens[j2+1]
                if out in setwords:
                    possible=True;break
            assert possible,(w,j,joined)
            instances+=1
    return instances

def case_T_order():
    # strict endpoint order for each of two nonempty 2-component occurrences
    tested=0
    for x in combinations(range(13),4):
        (x1,y1,x2,y2)=x
        for z in combinations(range(13),4):
            (u1,v1,u2,v2)=z
            ints=((x1,y1),(x2,y2),(u1,v1),(u2,v2))
            if any(max(ints[i][0],ints[j][0]) < min(ints[i][1],ints[j][1])
                   for i in range(2) for j in range(2,4)):
                continue
            if y2<=u1 or v2<=x1:continue
            order=sorted(((x1,1),(x2,2),(u1,1),(u2,2)))
            assert [b for _,b in order]==[1,1,2,2],(x,z,order)
            tested+=1
    return tested

def runs(w):
    return sum(i==0 or w[i]!=w[i-1] for i in range(len(w)))

def side(w):
    return (typ(w),w[0],w[-1])

def nprime(A,B):
    return runs(A)+runs(B)-int(A[0]==A[-1])-int(B[0]==B[-1])

def shell_classes():
    allw=[''.join(xs) for z in range(1,5) for xs in product('bc',repeat=z)]
    shells=[(A,B) for A in allw for B in allw if typ(A+B)==frozenset('bc')]
    classes=defaultdict(list)
    for A,B in shells: classes[(side(A),side(B))].append((A,B))
    assert len(classes)==34
    checked=0
    for cls,shs in classes.items():
        fA,lA=cls[0][1:]; fB,lB=cls[1][1:]
        for P in allw:
            constant=runs(P)-int(lA==P[0])-int(P[-1]==fB)+int(lA==fA)+int(lB==fB)
            # no reuse of Claude's original code; explicit one- and two-shell checks
            for A,B in shs:
                F=A+P+B
                assert F[0]==fA
                assert runs(F)==nprime(A,B)+constant,(cls,P,F)
                checked+=1
            for A,B in shs:
                for C,D in shs:
                    F=A+C+P+D+B
                    assert F[0]==fA
                    assert runs(F)==nprime(A,B)+nprime(C,D)+constant,(cls,P,F)
                    checked+=1
    return len(classes),checked

def language_token(k):
    return {''.join(t) for t in product(('a','bc'),repeat=k)}

def language_sorted_weight(N,wb=2,wc=2):
    return {a*'a'+b*'b'+c*'c'
            for a in range(N+1) for b in range(N//wb+1)
            for c in range(N//wc+1)
            if a+wb*b+wc*c==N}

def language_weight(N):
    return {''.join(tup) for length in range(N+1) for tup in product(ALPHA,repeat=length)
            if sum(1 if ch=='a' else 2 for ch in tup)==N}



# Independent *generative* formal certificate.  Each generated word is checked
# as exactly one instance of the two distribution-substitution inference rules.
# Unlike bounded search, the resulting a^(k-1) is a proof against every
# (2,c)-substitutable language containing these finitely many premises.
def a_positions(w):
    ans=[]; i=0
    while i<len(w):
        if w[i]=='a':
            j=i
            while j<len(w) and w[j]=='a': j+=1
            ans.append((i,j));i=j
        else: i+=1
    return ans

def plug1(E,x): return E[0]+x+E[1]
def plug2(E,x): return E[0]+x[0]+E[1]+x[1]+E[2]

class Formal:
    def __init__(self,k,seeds):
        self.k=k;self.words=set(seeds);self.steps=[]
    def infer(self,arity,x,y,E0,E1):
        assert arity in (1,2)
        assert len(x)==arity and len(y)==arity
        assert all(x) and all(y)
        assert all(typ(u)==typ(v) for u,v in zip(x,y))
        if arity==2: assert E0[1] and E1[1]
        fill=plug1 if arity==1 else plug2
        a=fill(E0,x[0]) if arity==1 else fill(E0,x)
        b=fill(E0,y[0]) if arity==1 else fill(E0,y)
        c=fill(E1,x[0]) if arity==1 else fill(E1,x)
        d=fill(E1,y[0]) if arity==1 else fill(E1,y)
        assert a in self.words and b in self.words and c in self.words,(arity,x,y,E0,E1,a,b,c)
        self.steps.append((arity,x,y,E0,E1,a,b,c,d))
        self.words.add(d)
        return d
    def unit(self,w,src,dst):
        R=a_positions(w);assert src!=dst and R[src][1]-R[src][0]>=2
        base=('', 'a', 'a'*(self.k-4))
        if dst<src:
            ix,jx=R[dst],R[src]
            E1=(w[:ix[1]-1],w[ix[1]:jx[0]],w[jx[0]+2:])
            assert plug2(E1,('a','aa'))==w
            return self.infer(2,('a','aa'),('aa','a'),base,E1)
        ix,jx=R[src],R[dst]
        E1=(w[:ix[1]-2],w[ix[1]:jx[0]],w[jx[0]+1:])
        assert plug2(E1,('aa','a'))==w
        return self.infer(2,('aa','a'),('a','aa'),base,E1)
    def tune(self,w,goal):
        sizes=[e-s for s,e in a_positions(w)]
        assert len(sizes)==len(goal) and sum(sizes)==sum(goal) and min(goal)>0
        while sizes!=list(goal):
            dst=next(i for i in range(len(goal)) if sizes[i]<goal[i])
            src=next(i for i in range(len(goal)) if sizes[i]>goal[i])
            w=self.unit(w,src,dst)
            sizes[src]-=1;sizes[dst]+=1
        assert [e-s for s,e in a_positions(w)]==list(goal)
        return w
    def fuse(self,w,index):
        R=a_positions(w);sizes=[e-s for s,e in R];assert 0<=index<len(sizes)-1
        goal=sizes[:]
        goal[index]+=goal[index+1]-1;goal[index+1]=1
        if goal[index]<2:
            donor=next(i for i,n in enumerate(goal) if n>=2 and i not in (index,index+1))
            goal[donor]-=1;goal[index]+=1
        w=self.tune(w,goal);R=a_positions(w)
        u=w[R[index][1]:R[index+1][0]]
        assert u and 'a' not in u
        moved=self.unit(w,index,index+1)
        e0=(w[:R[index][1]-2], w[R[index+1][0]:])
        e1=(w[:R[index][1]-1], w[R[index+1][0]+1:])
        assert plug1(e0,'a'+u+'a')==moved
        assert plug1(e1,'a'+u+'a')==w
        return self.infer(1,('a'+u+'a',),('aa'+u,),e0,e1)
    def collapse(self,w):
        while len(a_positions(w))>2: w=self.fuse(w,0)
        return w
    def inner_bounds(self,w):
        R=a_positions(w)
        return [(R[i][1], R[i+1][0]) for i in range(len(R)-1)]
    def swap_block(self,w,ind,F,d,F2,d2,samples):
        low,high=sorted((d,d2))
        L,H=(F,F2) if d==low else (F2,F)
        X='a'*(high-low+1)+L;Y='a'+H
        E0=('', 'a'*(self.k-high-1))
        # make both E0 witnesses from their SB positive words
        self.tune(samples[L],[high-low+1,self.k-high-1])
        self.tune(samples[H],[1,self.k-high-1])
        if d==low:
            cur=[e-s for s,e in a_positions(w)]
            required=high-low+1
            if cur[ind]<required:
                need=required-cur[ind];cur[ind]=required;cur[-1]-=need
                assert cur[-1]>=1
                w=self.tune(w,cur)
            start,end=self.inner_bounds(w)[ind]
            E1=(w[:start-required],w[end:])
            assert plug1(E1,X)==w
            return self.infer(1,(X,),(Y,),E0,E1)
        start,end=self.inner_bounds(w)[ind]
        E1=(w[:start-1],w[end:])
        assert plug1(E1,Y)==w
        return self.infer(1,(Y,),(X,),E0,E1)
    def swap_shell(self,w,i,j,S,e,S2,e2,samples):
        low,high=sorted((e,e2))
        L,H=(S,S2) if e==low else (S2,S)
        X=('a'*(high-low+1)+L[0],L[1]);Y=('a'+H[0],H[1])
        E0=('', 'a', 'a'*(self.k-high-2))
        self.tune(samples[L],[high-low+1,1,self.k-high-2])
        self.tune(samples[H],[1,1,self.k-high-2])
        if e==low:
            cur=[f-s for s,f in a_positions(w)]
            required=high-low+1
            if cur[i]<required:
                need=required-cur[i];cur[i]=required;cur[-1]-=need
                assert cur[-1]>=1
                w=self.tune(w,cur)
            bounds=self.inner_bounds(w);a,b=bounds[i];c,d=bounds[j]
            E1=(w[:a-required],w[b:c],w[d:])
            assert plug2(E1,X)==w
            return self.infer(2,X,Y,E0,E1)
        bounds=self.inner_bounds(w);a,b=bounds[i];c,d=bounds[j]
        E1=(w[:a-1],w[b:c],w[d:])
        assert plug2(E1,Y)==w
        return self.infer(2,Y,X,E0,E1)

def formal_certificate(k=40,losses=(3,5,6,7)):
    e1,e2,e3,e4=losses
    S1=('b','c');S2=('bb','c');S3=('b','cc');S4=('bb','cc')
    shloss=dict(zip((S1,S2,S3,S4),losses))
    shell_samples={z:'a'+z[0]+'a'+z[1]+'a'*(k-shloss[z]-2)
                   for z in shloss}
    template='a'+'b'+'a'+'b'+'a'+'c'+'a'+'c'+'a'*(k-2*e1-4)
    seed={'a'*k,template}|set(shell_samples.values())
    pr=Formal(k,seed)
    block_samples={'bc':pr.collapse(shell_samples[S1])}
    T=pr.fuse(template,1)
    # Branch 1: S2[S3[bc]]
    w=pr.swap_shell(T,0,2,S1,e1,S3,e3,shell_samples)
    block_samples['bbccc']=pr.collapse(w)
    w=pr.swap_block(T,1,'bc',e1,'bbccc',e1+e3,block_samples)
    w=pr.swap_shell(w,0,2,S1,e1,S2,e2,shell_samples)
    W1=pr.collapse(w)
    # Branch 2: S4[S1[bc]]
    block_samples['bbcc']=pr.collapse(T)
    w=pr.swap_block(T,1,'bc',e1,'bbcc',2*e1,block_samples)
    w=pr.swap_shell(w,0,2,S1,e1,S4,e4,shell_samples)
    W2=pr.collapse(w)
    assert W1.strip('a')==W2.strip('a')=='bbbbcccc'
    m1,m2=W1.count('a'),W2.count('a')
    assert m1==k-e1-e2-e3 and m2==k-2*e1-e4
    conclusion=None
    if m1!=m2:
        low,high=sorted((m1,m2));delta=high-low
        WL=pr.tune(W1 if m1==low else W2,[1,low-1])
        WH=pr.tune(W2 if m1==low else W1,[1,high-1])
        fixed='a'+'bbbbcccc'+'a'*(low-2)
        assert WL==fixed+'a' and WH==fixed+'a'*(1+delta)
        conclusion=pr.infer(1,('a'*(1+delta),),('a',),
                            (fixed,''),('a'*(k-1-delta),''))
        assert conclusion=='a'*(k-delta)
    # REPLAY: explicitly validate every logged inference *from the seeds only*.
    known=set(seed)
    for arity,x,y,E0,E1,a,b,c,d in pr.steps:
        fill=plug1 if arity==1 else plug2
        assert all(typ(u)==typ(v) for u,v in zip(x,y))
        if arity==2:assert E0[1] and E1[1]
        px=x[0] if arity==1 else x;py=y[0] if arity==1 else y
        assert a==fill(E0,px) and b==fill(E0,py) and c==fill(E1,px) and d==fill(E1,py)
        assert a in known and b in known and c in known
        known.add(d)
    return conclusion,len(pr.steps),(m1,m2)

def main():
    samples=[('all_len6',set(map(''.join,product(ALPHA,repeat=6)))),
             ('sorted_weight8',language_sorted_weight(8)),
             ('all_order_weight8',language_weight(8)),
             ('token4',language_token(4)),
             ('token7',language_token(7))]
    for name,L in samples:
        results={}
        for arity in (1,2):
            results[arity]=exact_substitutable(L,arity)
        assert results[1][0] and results[2][0],(name,results)
        count=verify_contraction(L)
        print('LANGUAGE',name,'words',len(L),'tuple1',results[1][1],
              'tuple2',results[2][1],'contractions',count,'PASS')
    # Negative controls: arity 2 is genuinely needed for transfer/F'.
    L1={'aaaaaa','bbbb','cccc','aabacaa'}
    assert exact_substitutable(L1,1)[0]
    assert not exact_substitutable(L1,2)[0]
    assert 'abaacaa' not in L1 and 'aabacaa' in L1
    assert all(('a'*s+'bc'+'a'*(5-s)) not in L1 for s in range(1,5))
    print('NEGATIVE_CONTROL one-hole only: F-prime fails, arity-2 fails; PASS')
    # Case II token language fails for every n>=2; n=5 meets mu_a>=5.
    n=5;B={''.join(ts) for ts in product(('a','bc','cb'),repeat=n)}
    pref='a'*(n-2)
    assert pref+'cbcb' in B and pref+'bccb' in B
    assert pref+'bcbc' in B and pref+'bbcc' not in B
    assert not exact_substitutable(B,1)[0]
    print('NEGATIVE_CONTROL (a|bc|cb)^5: one-hole countercertificate; PASS')
    for e in ((3,5,6,7),(3,5,6,8)):
        word,steps,counts=formal_certificate(40,e)
        if e[-1]==7: assert word=='a'*39
        else: assert word is None
        print('FORMAL_CERT k40',e,'counts',counts,'replayed steps',steps,
              'shorter pure word',repr(word),'PASS')
    t=case_T_order()
    print('CASE_T strict interval pairs',t,'PASS')
    c,b=shell_classes()
    print('CASE_Q shell classes',c,'tested nests',b,'PASS')

if __name__=='__main__': main()
```


## 9. 文献の位置づけ、新規性、最終判断

Clark–Eyraud (2007, *JMLR* 8:1725–1745) は一穴代入可能性による正例学習の先行研究であり、Yoshinaka (2011, *TCS* 412:1821–1831, DOI [10.1016/j.tcs.2010.12.058](https://doi.org/10.1016/j.tcs.2010.12.058)) は多次元代入可能性による MCFG 学習の先行研究である。Duncan–Elder–Frenkel–Lyu (2026, *International Journal of Algebra and Computation*, DOI [10.1142/S0218196726500463](https://doi.org/10.1142/S0218196726500463)) は MCFG の *Substitution Lemma* と名付けた別種の非所属判定用必要条件を扱っている。本報告の殻交換・損失線形化と同じ定理だとは認定していない。**補題 F′、E₂、T、N、Q、定理 I の文献的な新規性は未確認**。原稿へ正式採用する前に先行研究の本文まで綿密に照合すべきである。

**検証の結論**：場合 I の定理 I は、指定の前提・量化の範囲で、証明の依存関係を再構成して**独立に確認**した。Part D の76段も一穴・二穴の規則だけで独立再生できた。今回の探索で定理 I を壊す反例は見つからなかった。

**止まった場所**：場合 II・III における (R) に代わる損失関係、および複数文字内容型 `μ_m` の上界。候補 `(a|bc|cb)^n` は全 `n≥2` で既に arity 1 で壊れるため否定側に使えない。

**次に絞るべき一点**：場合 II の分岐 (S) において、同じ内容の部分語 `z` が異なる `a` 詰め物付きの一穴文脈に現れたとき、`λ(APB)=e_A+λ(P)` の二つの表現を比較して**殻の損失に非自明な関係を強制できる条件**を探すこと。まずは4乗禁止を満たす二側複数連の殻に限定し、実際の受理語を通じて共通文脈を証明できた場合だけ、損失等式を導く。現在の結果を「三文字の全内容型が解決」「境界がファンアウトで動く」などとは表現しない。

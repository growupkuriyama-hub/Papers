# MCFG fan-out 2・第十五段 独立数学探索報告

**日付：2026-11-16 JST。研究報告のみ。論文本文・GitHubは変更していない。**

## 冒頭結論

**新しく確立したこと。** TRは、文字対 `de/ed` から、任意の非空語ブロック `uv/vu` へ持ち上がる。aを含まないブロックでは室条件 `N≥4 max(δ₁,δ₂)+1` をそのまま保つ。したがって `bcc/cbc`、`bcc/ccb` は一般のパラメータで証明できる。aを含む場合にも、明示した強い室条件で成立する。内部a連の正規化と組み合わせると、完全Parikhが異なる一部の対も扱える。

**反証したこと。** 依頼書§5および第十四段O2の、一般の内部分岐対に対する**連結宿主IHは偽**。交錯・入れ子のそれぞれについて、内容型付き全arity組代入可能な有限言語と、明示的reduced good・fan-out 2・rank 2文法を構成する。具体例は `N=1027`、元文法の厚さ `θ̄_G=97`、比較する大節点の収率長 `128`、欠損 `128`。節点数最小のa冪導出木からの二重置換が実在し、目標外側a-budgetは `769≥3` だが、同内容類の二核を連結する受理語は一つも存在しない。任意の固定線形室条件 `N≥c₁ max δ+c₂` を満たす反例族もある。

**未解決。** 一般AB_pair、P_tree、非可換予想U、正式 `op:fanout-two` はOPEN。本反例は、後述の強い「小欠損窓」条件を満たさない。したがって、その条件を新たに加えたIHまで反証したとは主張しない。IHの失敗をP_treeやUの反証と取り違えてはならない。

この報告のPROVEDは、以下に記した数学的手証明の判定である。機械形式化・外部査読・文献的新規性の認定ではない。

## 1. 一次資料の実査と定義

添付 `PROMPT_ASTRA_FANOUT2_ROUND15_AB_IH_2026-11-16.md` は全文を読んだ。続いてGitHubの `growupkuriyama-hub/Papers`、`02-v4-fixed-s-mcfg/v2/` の次の現行資料を取得し、該当する定義・証明・監査結論を確認した。

1. [main.tex](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v4-fixed-s-mcfg/v2/main.tex)：特に `def:standard-mcfg`、`def:grammar-properties`、`def:tuple-substitutable`、厚さの定義、`lem:thickness-equivalence`、`op:fanout-two`。
2. [HANDOFF_CURRENT.md](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v4-fixed-s-mcfg/v2/HANDOFF_CURRENT.md)。
3. [2026-11-16最新研究索引](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v4-fixed-s-mcfg/v2/reviews/STATUS_FANOUT2_ROUNDS12_TO14_FABLE_2026-11-16.md)。
4. [第十三段独立監査](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v4-fixed-s-mcfg/v2/reviews/audit_claude_round13_noncomm_U_independent_2026-11-15.md)。
5. [第十四段独立監査](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v4-fixed-s-mcfg/v2/reviews/audit_claude_round14_noncomm_Parikh_independent_2026-11-16.md)。
6. [Fable-C独立手証明監査](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v4-fixed-s-mcfg/v2/reviews/Fable_C_complete_independent_mathematical_audit_2026-11-15.md)。
7. [第十四段原報告](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v4-fixed-s-mcfg/v2/reviews/claude_round14_noncomm_Parikh_report_2026-11-15.md)と[残存義務](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v4-fixed-s-mcfg/v2/reviews/claude_round14_noncomm_Parikh_next_obligations_2026-11-15.md)。原文の「CA PROVED」は後の独立監査に従って採用しない。
8. [第十四段完全ソース束](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v4-fixed-s-mcfg/v2/reviews/ROUND14_COMPLETE_SOURCE_AUDIT_2026-11-16.md)：必要な証明書生成器を原バイト長・SHA-256で検証して抽出した。独立した直接ファイルURLは404だったため、この保存束を使用した。

[PR #130](https://github.com/growupkuriyama-hub/Papers/pull/130) は実際に merged=true、merge commit `67a9a37925181981357737726a151e0dfe72d038` と確認した。本文全体の再査読をしたという意味ではなく、本探索で用いる定義と研究資料を照合した。

以下、`Σ={a,b,c}`、`c(w)=alph(w)`。組代入可能性は常に**各成分の実際の内容型一致**を要求する。二穴文脈 `E=(l,m,r)` は `m≠ε`、両穴は非空。goodはε-free、nondeleting、nonpermuting、nonmergingの四条件である。厚さは

\[
\bar\theta_G=\max\left(1,\max_{R\in P}\min\{|w|:w\text{ に }R\text{ を使う成功導出がある}\}\right)
\]

という**元文法の規則厚さ**を用いる。

## 2. 判定表

| ラベル | 正確な対象 | 判定 |
|---|---|---|
| H | 非消去準同型による内容型付き組代入可能性の逆像保存 | PROVED |
| BT | 加法的宿主を持つ `uv/vu` のh一致、したがってδ一致 | PROVED |
| BT-Δ | `u,v∈{b,c}⁺`、室 `N≥4maxδ+1` | PROVED |
| NF | 正欠損のRot核・加法的宿主の内部a連を長さ1に正規化 | PROVED（既知Rの明示的帰結） |
| BT-NF | 正規化後に `uv/vu` となる対。内部a個数は異なってよい | PROVED WITH CLARIFICATIONS |
| ST | 固定文字順序＋線形等式による言語の全arity内容型付き代入可能性 | PROVED |
| IH-cross | 一般の交錯木由来分岐対からの連結宿主 | REFUTED |
| IH-nest | 一般の入れ子木由来分岐対からの連結宿主 | REFUTED |
| IH-small | 明記したθ依存の小欠損窓内だけに限定した改訂IH | OPEN |
| AB_pair | 一般の同非a Parikh対、加法的宿主・適切な室の下でのδ一致 | OPEN |
| 原文X1／原文CA | 40語／67語の既知反例 | REFUTED；今回も全受理文脈を再検証 |
| 数値検査 | 有限全検査・文法DP・持上げ証明書replay | CERTIFIED FINITE |
| P_tree／U／正式LG境界 | 一般形 | OPEN |

## 3. AB側：語ブロックへの転置定理の拡張

### 3.1 使用する基本操作と、その適法な文脈

`a^N∈L` が最短の正a冪であるとする。

**U（短いa冪の剛性）。** `P a^i Q,P a^j Q∈L`、`1≤i<j≤N` は不可能。比較片 `a^i,a^j` はともに型 `{a}`、共通文脈は `P□Q`。試験文脈 `a^{N-j}□` は `a^j` を受理するため、`a^{N-j+i}∈L` を強制し最短性に反する。

**R（正のa連の再配分）。** `i,j,i',j'≥1`、`i+j=i'+j'≤N−1` なら、タプル `(a^i,a^j)` と `(a^{i'},a^{j'})` は同型。共通文脈

\[
E_0=(\varepsilon,a,a^{N-1-i-j})
\]

は両者を `a^N` に送る。従って任意の受理済み試験文脈 `E_1=(P,Q,R)`、`Q≠ε` でa配分を交換できる。a連を0にすることは、この操作からは結論しない。

**Rot。** `a^p κ a^q∈L`、`p,q≥1`、`λ=p+q∈[3,N−1]` なら `aκ≡κa`。Rで `a²κa^{λ−2}` と `aκa^{λ−1}` を得て、共通一穴文脈 `(a,a^{λ−2})` に `aκ,κa` を置く。型はともに `c(κ)∪{a}`。この一穴同値に外側文脈を付けることで、核の左右の外側aを0も含め自由に再配分できる。

**S3/S4の、今回必要な型安全版。** Rot核 `K,K'` は `c(K)=c(K')`、外側a量は `λ,λ'≥3` とする。`i,i'=i+λ'−λ≥1` なら

\[
P K a^iR\in L\iff P K'a^{i'}R\in L,
\qquad
P K Q a^iR\in L\iff P K'Q a^{i'}R\in L\quad(Q\ne\varepsilon).
\]

実際、`i₀=1+max(0,λ−λ')`、`i₀'=i₀+λ'−λ` と置く。一穴版は比較片 `K a^{i₀},K'a^{i₀'}`、共有文脈 `□a^{λ−i₀}`。二穴版は比較タプル `(K,a^{i₀}),(K',a^{i₀'})`、共有文脈

\[
E_0=(\varepsilon,a,a^{\lambda-i_0-1}).
\]

`λ−i₀−1≥0` であり、両前提語はRotによる単独受理語である。試験文脈はそれぞれ `(P,a^{i−i₀}R)`、`(P,Q,a^{i−i₀}R)`。全ての穴は非空、二穴中央はそれぞれ `a` と `Q` で非空である。

ここでは二穴版に**実際の `c(K)=c(K')`** を明記した。非a内容の一致だけから、aを含む核と含まない核の二穴交換を無条件に使わない。以下のBTでは、交換する核は `uv,vu,uvvu,uvuv` なので、この型条件が全て満たされる。

### 3.2 補題H：非消去準同型による持上げ

**命題H［PROVED］。** `μ:Γ*→Σ*` は各文字を非空語に写す準同型とする。Lが全ての `d≤f` について内容型付き組代入可能なら、`K=μ^{-1}(L)` も同じ性質を持つ。

**証明。** Γ上で成分ごとの内容が等しいタプルx,yについて、各成分の像の内容は、その成分に出現する文字の像の内容の和集合だから等しい。Kの共通受理文脈E₀をμで写すと、Lの共通受理文脈になる。μは非消去なので非空の穴・内側セパレータは非空のまま。任意のKの受理文脈E₁について、L内で

`μ(E₀)[μ(x)], μ(E₀)[μ(y)], μ(E₁)[μ(x)]∈L ⇒ μ(E₁)[μ(y)]∈L`

を適用する。逆向きも同じ。∎

μの単射性、像同士のアルファベットの互いに素性は不要。MCFLの逆像閉性は、この補題にも次の局所証明にも不要である。

### 3.3 定理BT：一般語ブロック `uv/vu`

**仮定。** `u,v∈Σ⁺`、`β=uv, γ=vu` は両端が非aのRot核とする。外側a量を `λ₁,λ₂∈[3,N−1]`、

\[
h_i=N-\lambda_i\ge1,\quad m=|uv|_a=|vu|_a,\quad\delta_i=h_i-m
\]

とする。受理済み語

\[
a^x\beta a^y\gamma a^z\in L,\qquad x+y+z=T=N-h_1-h_2\ge3
\]

が実在し、`N≥4 max(h₁,h₂)+1` とする。

**結論［PROVED］。** `h₁=h₂`、従って `δ₁=δ₂`。

これは、`μ(A)=a, μ(B)=u, μ(C)=v` に対する補題HとTRの形式的な持上げでもある。ただし以下に直接の操作も示す。

**証明。** 反転言語への移行も許して `h₁≥h₂` としてよい。反転は受理文脈の順序と二穴タプルの成分順を同時に反転するので組代入可能性を保つ。`D=h₂−h₁≤0`、`j=1−D`、`A=N−3h₁` と置く。

| 手 | 実在する受理語 | 操作 |
|---|---|---|
| 1 | `uvvu a^T` | 仮定の宿主をRotで集約 |
| 2 | `uvuv a^(N−2h₁)` | 後半 `vu→uv`、S3 |
| 2′ | `vuuv a^T` | 先頭 `uv→vu`、S4、続いて末尾 `vu→uv`、S3 |
| 3 | `uuvv a^(N−2h₁+D)` | `u[vu]v` の括弧内を `uv` へ。S4の隔ては `v≠ε` |
| 4 | `uuvvuv a^A` | `u[uv]v` を `u[uvvu]v` へ。新核の外側a量はT |
| 5 | `uvuvuv a^A` | 手2の末尾 `uv→uvuv`。新核の外側a量は `N−2h₁` |
| 6 | `uuvvvu a^A` | 下記OSの一回の二穴交換 |
| 7 | `uuvvuv a^(A+D)` | 下記CSの一回の二穴交換 |

手4の合成核 `uvvu` と手5の `uvuv` は、それぞれ手1・手2からRotの外側配分を持つ。両者とも外側a量は `[3,N−1]`。核の実際の内容は全て `alph(uv)` に等しい。

**手6の全データ：**

\[
x=(vu,uv),\ y=(uv,vu),\quad
E_0=(\varepsilon,a,a^{T-1}),\quad E_1=(u,v,a^A).
\]

E₀[x],E₀[y]は手2′と手1のRot配分、E₁[x]は手5。両成分の型は `alph(uv)`、中央セパレータはaとvで非空。従ってE₁[y]が手6を与える。

**手7の全データ：**

\[
x=(uv,vu a^j),\ y=(uv,uv a^{j+D}),\quad
E_0=(\varepsilon,a,a^{T-1-j}),\quad E_1=(u,v,a^{A-j}).
\]

E₀[x]は手1のRot配分、E₀[y]は手2のRot配分、E₁[x]は手6。型はそれぞれ `alph(uv)` と `alph(uv)∪{a}`、`j,j+D≥1`。中央セパレータは再びaとv。これで手7を得る。

**室の検算。** `N≥4h₁+1` から

\[
T\ge2h_1+1,\quad N-2h_i\ge3,\quad
A-j=N-4h_1+h_2-1\ge h_2\ge1,
\]

\[
T-1-j=N-2h_1-2\ge0,\quad
1\le A+D=N-4h_1+h_2\le A<N.
\]

したがって全ての指数・穴・セパレータの条件を満たす。D<0なら、手4と手7は**同じ接頭語** `uuvvuv` の後ろに長さAとA+Dのa冪を持つので、Uに反する。ゆえにD=0。∎

**内部aの注意。** この最後のUは末尾a冪の長さだけを比較する。u,vに多数のaが含まれると全語のa総数がNを超える場合があるが、それをL2の適用条件に誤って代入していない。

### 3.4 直ちに解決するABの切片

`u,v∈Δ⁺` なら `h_i=δ_i`。従って次は**有限実験ではなく一般定理**である。

| 核対 | ブロック分解 | 十分な室 |
|---|---|---|
| `bcc / cbc` | `u=bc, v=c` | `N≥4maxδ+1` |
| `bcc / ccb` | `u=b, v=cc` | 同左 |
| `bbc / bcb` | `u=b, v=bc` | 同左 |
| 任意の巡回共役 `uv / vu` | 任意の非空u,v | 同左 |

いずれも**単独Rot証人と加法的な連結宿主が必要**。例えば `bbcc/bcbc` は巡回共役ではなく、この定理の対象外である。

### 3.5 NF：内部a連の正規化と、異なる完全Parikhへの拡張

**命題NF［PROVED］。** Rot核κの欠損が正、すなわち単独受理語の総a数が `N−δ<N` とする。κ内の各極大a連を長さ1に縮めた核を `ν(κ)`、内部a連数を `r(κ)` と置く。すると

\[
\nu(\kappa)\text{ はRot核},\quad
\delta(\nu(\kappa))=\delta(\kappa),\quad
\lambda_{\nu}=N-\delta-r(\kappa).
\]

**証明。** 各内部a連をRの一方の穴に、正の外側a連を他方の穴に取り、前者を長さ1、後者を余りだけ長くする。間には少なくとも一つの非a文字がある。比較する二a連の合計は全a数以下で `≤N−1`。外側の両端を正に保て、外側総数は増えるだけなので `[3,N−1]` に残る。a総数は一定なので欠損は不変。∎

同様に、正欠損の二核を持つ**加法的宿主**も正規化できる。宿主の全a数は `N−δ−δ'<N`、外側に正のa連が少なくとも一つあるため、それを受け皿にRを反復すればよい。正規化後の外側budgetは

\[
N-\delta-\delta'-r(\kappa)-r(\kappa')
\]

に正確に増加する。元の加法的一致を仮定せずにこの式を使ってはならない。

**系BT-NF［PROVED WITH CLARIFICATIONS］。** 正規化後に `ν(κ)=uv`、`ν(κ')=vu` と書け、`r=r(κ)=r(κ')=|uv|_a` とする。正の欠損、元の加法的宿主、

\[
N\ge4\bigl(\max(\delta,\delta')+r\bigr)+1
\]

の下で `δ=δ'`。NFの後にBTを適用すればよい。

例えば `κ=b a^s cc`、`κ'=cb a^t c`、`s,t≥1` は、s≠tなら完全Parikhが違うが、正規化すると `bacc / cbac=(bac)c / c(bac)`。r=1なので室 `N≥4maxδ+5` で扱える。これは、単に「完全Parikh一致」だけを扱う結果ではない。

**残る境界。** 正規化はa連の長さを1にするだけで、存在するa連を消さない。非a文字の並べ替えに伴って内部a連の有無が変わる一般対や、非巡回の同Parikh対は未解決である。

## 4. IHを反証する順序不変量

### 4.1 補題ST：文字順序と線形等式は両立する

Δに固定全順序を入れ、πをa消去射影とする。`M`を整数行列、zを固定ベクトルとして

\[
L=\{w\in\Sigma^+:\pi(w)\in d_1^*\cdots d_D^*,\ M\operatorname{Parikh}(w)=z\}
\]

と定める。このLは、任意arityについて内容型付き組代入可能である（MCFL性は別途必要なら確認する）。

**証明。** 成分ごとに同内容のx,yと共通受理文脈E₀を取る。各成分の射影はE₀[x],E₀[y]の因子なので、それ自体が非減少順である。固定文脈中で複数の非減少順の断片を連結した結果が非減少になるかどうかは、各断片に現れる文字集合の最小・最大だけで決まる。x,yの成分内容は等しいので、任意のE₁で順序条件の真偽は一致する。

さらにE₀[x],E₀[y]が同じ線形等式を満たすことから

\[
\sum_i M\operatorname{Parikh}(x_i)=\sum_i M\operatorname{Parikh}(y_i).
\]

従って任意のE₁においても線形等式の真偽が一致する。E₁[x]が受理されればE₁[y]も受理される。穴・セパレータは元々適法なものだけを使い、変更していない。∎

### 4.2 反例言語

偶数 `d≥4`、整数 `q≥1`、`K=2^q`、`N=dK+3` とし、

\[
\boxed{L_{N,d}=\{w:\pi(w)\in b^*c^*,\ |w|_b=|w|_c,\ |w|_a+d|w|_b=N\}.}
\]

空語はこの条件を満たさない。有限言語であり、唯一のaのみの語は `a^N`。STにより、**d=1,2を含む任意arityで内容型付き組代入可能**である。

どの非a内容 `{b,c}` のRot核κも、その単独受理語から `π(κ)=b^m c^m`、`m≥1` を満たす。そのような二核κ,κ'を連結すると、外側a配分が何であっても

\[
\pi(a^x\kappa a^y\kappa'a^z)=b^m c^m b^{m'}c^{m'}\notin b^*c^*.
\]

**従ってこの内容類の連結二核宿主は一つも存在しない。**

障害は単純な順序量 `I(w)=|π(w)|_{cb}` である。全受理語ではI=0、二核連結ではI≥1。一方、次節の交錯・入れ子による二重置換語はI=0のままである。

## 5. 明示的reduced good文法と、木由来性

### 5.1 文法 `G_{d,q}^{cross}` と `G_{d,q}^{nest}`

開始記号S、fan-out 1の `A₁,…,A_N`、fan-out 2の `B₀,…,B_q` を取る。変数の下付き1,2は同じ子の成分番号を表す。

**A部分の規則：**

\[
A_1\to a,\qquad A_d\to bc,
\]
\[
A_n\to aA_{n-1}\ \mid\ A_{n-1}a\quad(2\le n\le N),
\qquad
A_n\to bA_{n-d}c\quad(d+1\le n\le N).
\]

**B部分の規則：**

\[
B_0\to(a^{d/2},a^{d/2})\ \mid\ (b,c).
\]

`i=1,…,q` について、子をX,Y（ともに `B_{i−1}`）とし、交錯版では

\[
B_i\to(X_1Y_1,\ X_2Y_2)(B_{i-1},B_{i-1}),
\]

入れ子版では

\[
B_i\to(X_1Y_1,\ Y_2X_2)(B_{i-1},B_{i-1}).
\]

**開始規則：**

\[
S\to A_N,\qquad S\to aX_1aX_2a(B_q).
\]

以上で規則を全て列挙した。`A₀`や空成分は導入しない。

### 5.2 言語同一性とgood/reduced

**A部分は `L_{n,d}` をちょうど生成する。** 生成される語が条件を保つことは各規則から明らか。逆に条件を満たす語の端にaがあればそれを剥がす。両端がaでなければ、非aがあるとき先頭はb、末尾はcなので一対を剥がす。空の内側に達する場合は `A_d→bc`、aのみの最終一文字は `A₁→a` で処理できる。これが語長に関する帰納証明になる。

B_iの導出組は、第一成分が `{a,b}⁺`、第二成分が `{a,c}⁺`、両者のb/c数が等しく、総a数＋d×b数が `d2^i`。この不変量は両版の規則で保存される。従って第二開始規則の語も `L_{N,d}` に入る。第一開始規則は既に全 `L_{N,d}` を生成するため、**両文法とも正確に `L_{N,d}` を生成する**。

全ての出力成分は非空。各変数はちょうど一度使われ、同じ子の成分1は成分2より先に現れる。B規則では同じ子の二成分は異なる出力成分にあり、開始規則では中央の終端aで隔てられる。従ってnonmergingを含む四good条件を満たす。全A_nはA_Nからa規則で到達でき、全B_iはB_qから到達でき、全非終端は生産的。fan-outは2、最大rankは2である。

### 5.3 元文法の厚さを正確に計算する

`ℓ(n)=2⌊n/d⌋+(n mod d)`、`ℓ(0)=0` と置く。これはA_nの最短語長である。成功文脈を `b…□…c` とaの追加で作れるので、A_nの外側に長さ `ℓ(N−n)` の成功文脈がある。

任意の非負x,yについて

\[
\ell(x)+\ell(y)\le\ell(x+y)+d-2.
\]

従ってa追加規則の最短成功語長は

\[
\ell(N-n)+1+\ell(n-1)\le1+\ell(N-1)+d-2=2K+d+1,
\]

b/c追加規則についても

\[
\ell(N-n)+2+\ell(n-d)\le2+\ell(N-d)+d-2=2K+d+1.
\]

定数規則も同じ上界に入る。B_iの非定数規則は全B₀葉を(b,c)にすれば長さ `2K+3` の成功語で使用できる。B₀の長い定数規則だけを一葉で使用し、他のK−1葉を(b,c)にすれば長さ

\[
d+2(K-1)+3=2K+d+1
\]

になる。逆に、その長い定数規則を使う成功導出はB開始規則を通るしかなく、少なくとも一葉が長さd、他のK−1葉は長さ≥2である。よってこれがその規則の厳密な厚さであり、

\[
\boxed{\bar\theta_G=2^{q+1}+d+1.}
\]

型精密化した文法の厚さも、非終端厚さによる置換も使っていない。

### 5.4 a冪の節点数最小木

A開始規則から `a^N` を得るには、b/c規則を一度も使えず、A_NからA₁までのN節点とSが必要なので `N+1` 節点。

B開始規則では、全B₀を長いa組にするしかない。B_q以下は完全二分木で `2^{q+1}−1` 節点、Sを加えて `2^{q+1}` 節点。d≥4なのでこちらが厳密に小さく、他の開始規則はない。従ってこの木は**a^Nの節点数最小導出木**である。

### 5.5 全条件を満たす具体例

`d=64,q=4,K=16,N=1027` とする。すると

\[
\bar\theta_G=97,\qquad |T|=32.
\]

B₄以下のB₁出現を、第一成分内の左から0,…,7と番号付けし、番号2と3の兄弟B₁節点を選ぶ。両節点は比較不能であり、開始規則の両端aより内側にある。純a導出組は `(a^{64},a^{64})`、収率総長128で、**128>97なので大節点**である。

各B₁の最短生産的組は `(bb,cc)`、長さ4≤97。この置換は同じ非終端の別の文法導出を使う操作である。型の違うタプルに組代入可能性を適用しているわけではない。その後の言語レベルの交換では、成分型一致を要求する。

**単独置換の実在語：**

| 配置 | B₁番号 | 語 |
|---|---:|---|
| 交錯 | 2 | `a^129 bb a^449 cc a^321` |
| 交錯 | 3 | `a^193 bb a^449 cc a^257` |
| 入れ子 | 2 | `a^129 bb a^641 cc a^129` |
| 入れ子 | 3 | `a^193 bb a^513 cc a^193` |

どれもa総数は899、欠損 `δ=1027−899=128`。Rで内部a連を1まで減らし、外側を再配分すると、全てから

\[
a\,\kappa\,a^{897}\in L,\qquad \kappa=bbacc=b^2ac^2
\]

が得られる。例えば最初の語では、穴 `(a^{129},a^{449})` の隔てをbbとして内部連を1に減らし、次いでκを隔てに外側二a連を再配分する。全穴は正、全隔ては非空、比較するa長の合計はN−1以下である。

従って核はRot核で、

\[
\lambda=898,\quad |\kappa|_a=1,\quad h=129,\quad V_\Delta(\kappa)=(2,2).
\]

**二重置換の実在語：**

\[
w_{cross}=a^{129}b^4a^{385}c^4a^{257},\qquad
w_{nest}=a^{129}b^4a^{513}c^4a^{129}.
\]

両方ともLに属し、a総数は `771=N−128−128`。成分配置はそれぞれ `B₁ C₁ B₂ C₂` と `B₁ C₁ C₂ B₂` である。入れ子の中央C₁/C₂間にも正のaセパレータがあり、同じ子の成分が隣接する禁止形は使っていない。

**IHが要求する加法的budget：**

\[
e=N-h-h=1027-129-129=769\ge3,
\qquad N\ge4\max\delta+1=513.
\]

しかし、そのbudgetと正の三つの外側a連を持つ具体的目標

\[
\boxed{a\,bbacc\,a\,bbacc\,a^{767}\notin L}
\]

はa総数771で数値的には完全に加法的であるにもかかわらず、射影が `bbccbbcc` なので不受理。さらに§4.2により、別の核J,J'を選んでも、非a内容が同じ `{b,c}` なら連結受理語は存在しない。

これで、単なる有限言語の反例ではなく、**明示的good文法・最小木・短い組・大節点・二重置換・Rot証人・正の室を全て備えた、交錯IHおよび入れ子IHの反証**となる。言語全体の組代入可能性はSTによる一般証明で保証される。

### 5.6 任意の固定線形室条件でも救えない

`q≥3,d=2^{q+2}`、比較節点をB₁とする。すると

\[
\delta=2d,\quad h=2d+1,\quad
\bar\theta_G=d+2^{q+1}+1<2d,
\]
\[
N=d2^q+3,\quad e=N-2h=d(2^q-4)+1\ge3,
\quad \frac{N}{\delta}=2^{q-1}+\frac3{2d}\longrightarrow\infty.
\]

核は常に同じ短い `bbacc`。従って任意の固定 `c₁,c₂` に対して、十分大きいqを選べば `N≥c₁maxδ+c₂` を満たす。hやθの固定倍を用いる室条件も同様に満たせる。それでも連結宿主は存在しない。

**これは数値的な最小反例を主張するものではない。** 最小の構造的障害として、二つの非a文字の順序 `b* c*` だけで十分だという主張である。

## 6. 何が反証され、何が反証されていないか

1. **一般IHの反証であり、ABの反証ではない。** ABが要求する実在する加法的連結宿主は、この言語には存在しない。宿主なしの言語をAB反例として再提出しているわけではない。
2. **P_treeはこの例でむしろ成立する。** 任意の単独受理語では `δ=d|κ|_b`。欠損は非a Parikhの線形関数である。したがって、連結宿主の生成をP_treeの必要条件と考えること自体が強過ぎる。
3. **U・LG境界の反例ではない。** この言語は内容型付けで扱っており、固定U₁型付けの対象言語だとは主張しない。また反例族では `N=d²/4+3=O(θ̄_G²)` であり、超多項式の希少型下界は得られない。
4. **小欠損窓の限定版には未到達。** 第十四段T2′には、`D=2,B=D!θ²=2θ²` として許容単位の窓

\[
\delta_J\le N_1=\frac{N-1}{4(D+1)B}=\frac{N-1}{24\theta^2}
\]

が現れる。本具体例の右辺は `1026/(24·97²)<0.005` で、δ=128は入らない。依頼書§5とO2の一般IHにはこの窓条件は書かれていないため、その一般形は反証された。しかし、この窓を**分岐対B,C自体にも明示して**主張し直す場合は別問題である。そこまでREFUTEDとはしない。
5. **以前の条件付き含意との関係。** `CA*∧IH∧AB⇒P_tree` という形式的含意そのものを反証したのではない。一般IHを常に成立する補題として埋める方針が使えなくなった。P_treeを直接証明するか、IHを適切に限定する必要がある。

## 7. 検証：有限全検査と一般証明を分ける

標準ライブラリだけの独立コード `round15_check.py` を新規記述し実行した。コード全文と実際の標準出力を付録に収める。以前の閉包チェッカーはインポートしていない。

### 7.1 二通りの厳密有限検査

実装1は、各有限言語の全受理一穴・二穴出現からタプル分布を列挙し、同型・共通文脈を持つタプルの分布集合を比較する。

実装2は、穴長・区切り長・開始位置という別の列挙から、同型タプルと受理文脈の関係を作り、三つの受理前提からの第四語が全て言語内にあることを直接検査する。有限言語では共通受理文脈を持つ全タプルはこの列挙に必ず現れるため、長さcapを設けた近似ではない。

| 対象 | 語数 | タプル数 | タプル・文脈組 | 分布比較数 | 第二実装の矩形検査数 |
|---|---:|---:|---:|---:|---:|
| 既知X1反例 | 40 | 333 | 2327 | 924 | 80660 |
| 既知CA反例 | 67 | 1566 | 12019 | 5544 | 1278526 |
| `L_{8,4}` | 17 | 226 | 1017 | 397 | 13845 |
| `L_{9,4}` | 27 | 432 | 2463 | 1108 | 80127 |
| `L_{10,4}` | 44 | 818 | 5761 | 2884 | 412526 |
| `L_{11,4}` | 72 | 1532 | 13171 | 7174 | 1903475 |

全件通過。40語例の `bc∈L, acb∉L`、67語例の `bccbaaa∈L, bccbaaaaaa∉L` も確認した。

### 7.2 文法・証人の検査

両文法で全規則のgood条件、到達性、生産性を検査。非終端の最短収率と最短成功文脈を別方向の動的計画法で求め、定義通りの規則厚さを計算した。具体例は両版とも、非終端1033個、規則3025本、記号レベルサイズ14167、厚さ97、最短a冪の最小導出節点数32。

選択したB₁節点を実際の木評価で置換し、四つの単独語と二つの二重置換語が上記の式に一致することも確認した。

小例 `d=4,q=1,N=11` では文法の**全導出語集合**を列挙し、別に生成した `L_{11,4}` の72語と一致することを両版で確認した。大例 `N=1027` の全言語列挙は行っていない。大例の全称的代入可能性と言語同一性は§§4–5の証明に基づく。

### 7.3 BTの直接証明書replay

第十四段保存束の生成器（SHA-256 `eaccd71285f51f26d702b8d76e6fe7a7a5847d08e8f6f97368b8d939729663ea`）から、抽象パラメータ `N=13,h₁=3,h₂=2` の21手証明書を一度生成した。生成結果だけを今回のコードに埋め込み、以前の検証関数は使用していない。

10種類の非空ブロック像に各証明書を写し、さらに最終の一穴交換による `a^12` の強制を追加した。計220手について、成分ごとの実際の内容型・穴非空・中央非空・三前提の既出・帰結一致を独立にreplayした。全通過。像のアルファベットが重なる例、像にaが含まれる例も含む。これはBTの一般証明の代わりではなく、直接代入操作の追加確認である。

NFの有限帰結は92例を検査して通過。閉包探索を実行していないので、seed/cap/truncatedによる未決判定はない。全実行は終了コード0。

## 8. 依存関係

| 結論 | 使用する仮定・補題 | 使用しないもの |
|---|---|---|
| BT | tuple-substitutability、a冪最短性、単独Rot証人、加法的宿主、h室、U/R/Rot/S3/S4、明示OS/CS | 原文X1、原文CA、CA*、IH、可換性 |
| NF | 正欠損、Rot証人、R | AB、CA、文字順序交換 |
| BT-NF | NF＋BT、正規化後の巡回共役性 | 一般Parikh還元 |
| ST | 成分内容一致、固定順序、線形等式 | R/Rot、MCFG、有限探索 |
| IH反例 | ST、明示文法の言語同一性・good/reduced・正確な厚さ・最小木、順序量I | 偽X1、偽CA、CA*、未証明の一般補題 |

## 9. 次に残る最小課題

### 課題1：非巡回ABの最初の切片

`κ=bbcc, κ'=bcbc`、両者のRot証人、正欠損、外側budget `N−δ−δ'≥3` の実在連結宿主、例えば `N≥Cmaxδ+C'` を仮定してδ一致を証明するか反証する。今回のBTは適用できない。枠 `b[bc]c / b[cb]c` は非空なのでFによる局所二穴交換は使えるが、TRの「単位を合成核へ膨張させる手」に対応する受理宿主を、同じa会計で構成することが残る。

想定反例は、完全Parikhでは区別できないが巡回共役類・因子順序で区別される言語。ST型の順序言語だけでは、二核連結宿主自体がないのでAB反例にはならない。

### 課題2：小欠損窓を明記したIHの再定式化

元のreduced good文法の `θ=θ̄_G` を使い、比較不能な内部大節点B,Cに `δ_B,δ_C≤(N−1)/(24θ²)` を課した場合に、同内容類の加法的連結宿主が得られるか。今回の順序障害を避けるには、まずそのような窓内分岐が `b*c*` 型不変量と両立するかを調べる必要がある。

これは新たな限定命題である。元の一般IHを表現だけ変えてPROVEDに戻してはならない。Θ(θ²)のNしか持たない今回の反例族は窓に入らない。

### 課題3：連結化を経由しないP_tree

木由来の二重置換語では、配置にかかわらず非aベクトルと欠損の総和は加法的である。その**二成分の配置を保持したまま**、同非aベクトルの整数関係から欠損関係を強制できるか。今回の反例ではP_treeが成立しIHだけが失敗するので、連結化は本来不要な強化だった可能性がある。

最小の検査対象は、成分型 `({b},{c})` のままの成分別合成 `(u₁v₁,u₂v₂)` と `(u₁v₁,v₂u₂)`。語全体の内容一致を理由に成分型を混同せず、単独受理文脈と試験文脈を二穴のまま追跡する。この課題もOPENである。

## 10. 最終到達点

一般IHは、明示的な文法と最小木を伴って反証された。一方、ABは巡回共役という非自明な一般部分クラスで進展し、内部a数が異なる一部の対にも拡張できた。一般AB、P_tree、U、`op:fanout-two` は未解決のままである。ここから先を既存原稿の定理として扱う操作は行っていない。

## 付録：再現コードと実行記録

以下は今回実行したPython 3標準ライブラリのみのコードである。`round15_check.py` として保存し、`python3 round15_check.py` で実行できる。原コード・ログは省略せず収録する。

### A. 再現コード

```python
#!/usr/bin/env python3
"""Round 15 independent checks; Python standard library only.
No previous checker imports. No closure search, caps, or random sampling.
"""
from collections import defaultdict
from itertools import combinations
from math import inf
import json

def fill(e,x):
    return ''.join(e[i]+x[i] for i in range(len(x)))+e[-1]

def exact_distributions(L):
    D=defaultdict(set)
    for w in sorted(L):
        n=len(w)
        for i,j in combinations(range(n+1),2):
            D[(w[i:j],)].add((w[:i],w[j:]))
        for i,j,k,l in combinations(range(n+1),4):
            D[(w[i:j],w[k:l])].add((w[:i],w[j:k],w[l:]))
    groups=defaultdict(list)
    for x,es in D.items():
        for e in es: groups[(tuple(frozenset(t) for t in x),e)].append(x)
    checks=0
    for xs in groups.values():
        for x in xs[1:]:
            checks+=1
            assert D[x]==D[xs[0]],('distribution',xs[0],x)
    return len(D),sum(map(len,D.values())),checks

def exact_rectangles(L):
    # Independent occurrence enumeration using component lengths, then
    # rectangularity of each same-type context/tuple incidence relation.
    C=defaultdict(set); T=defaultdict(set)
    for w in sorted(L):
        n=len(w)
        for size in range(1,n+1):
            for left in range(n-size+1):
                x=(w[left:left+size],); e=(w[:left],w[left+size:])
                typ=tuple(''.join(sorted(set(z))) for z in x)
                C[(typ,e)].add(x); T[(typ,x)].add(e)
        for size1 in range(1,n):
            for size2 in range(1,n-size1):
                for gap in range(1,n-size1-size2+1):
                    for left in range(n-size1-size2-gap+1):
                        end1=left+size1; start2=end1+gap; end2=start2+size2
                        x=(w[left:end1],w[start2:end2]); e=(w[:left],w[end1:start2],w[end2:])
                        typ=tuple(''.join(sorted(set(z))) for z in x)
                        C[(typ,e)].add(x); T[(typ,x)].add(e)
    checked=0
    for (typ,e),xs in C.items():
        if len(xs)<2: continue
        for x in xs:
            for f in T[(typ,x)]:
                for y in xs:
                    assert fill(f,y) in L,('rectangle',e,f,x,y)
                    checked+=1
    return checked

def stage_language(N,d):
    out=set()
    for m in range(N//d+1):
        na=N-d*m; n=na+2*m
        for slots in combinations(range(n),2*m):
            w=['a']*n
            for t,p in enumerate(slots): w[p]='b' if t<m else 'c'
            out.add(''.join(w))
    return out

def member(w,N,d):
    p=w.replace('a','')
    return bool(w) and set(w)<=set('abc') and 'cb' not in p and w.count('b')==w.count('c') and w.count('a')+d*w.count('b')==N

# Each variable is (child number, component number), terminals are characters.
def grammar(d,q,nested=False):
    assert d>=4 and d%2==0 and q>=1
    N=d*2**q+3; arity={'S':1}; rules=[]
    def add(A,children,outputs): rules.append((A,tuple(children),tuple(tuple(z) for z in outputs)))
    for n in range(1,N+1): arity['A'+str(n)]=1
    for i in range(q+1): arity['B'+str(i)]=2
    add('A1',[],['a']); add('A'+str(d),[],['bc'])
    for n in range(2,N+1):
        add('A'+str(n),['A'+str(n-1)],[['a',(0,0)]])
        add('A'+str(n),['A'+str(n-1)],[[ (0,0),'a']])
    for n in range(d+1,N+1): add('A'+str(n),['A'+str(n-d)],[['b',(0,0),'c']])
    add('B0',[],['a'*(d//2),'a'*(d//2)]); add('B0',[],['b','c'])
    for i in range(1,q+1):
        second=[(1,1),(0,1)] if nested else [(0,1),(1,1)]
        add('B'+str(i),['B'+str(i-1)]*2,[[(0,0),(1,0)],second])
    add('S',['A'+str(N)],[[(0,0)]])
    add('S',['B'+str(q)],[['a',(0,0),'a',(0,1),'a']])
    return N,arity,rules

def grammar_audit(d,q,nested=False):
    N,arity,rules=grammar(d,q,nested); by=defaultdict(list)
    for R in rules:
        A,ch,outs=R; by[A].append(R)
        assert len(outs)==arity[A] and all(outs) and len(ch)<=2
        flat=[v for z in outs for v in z if isinstance(v,tuple)]
        assert sorted(flat)==[(j,k) for j,B in enumerate(ch) for k in range(arity[B])]
        for j,B in enumerate(ch): assert [k for z,k in flat if z==j]==list(range(arity[B]))
        for z in outs:
            for x,y in zip(z,z[1:]):
                assert not (isinstance(x,tuple) and isinstance(y,tuple) and x[0]==y[0] and y[1]==x[1]+1)
    reached={'S'}; stack=['S']
    while stack:
        for _,ch,_ in by[stack.pop()]:
            for B in ch:
                if B not in reached: reached.add(B); stack.append(B)
    assert reached==set(arity)
    order=['A'+str(n) for n in range(1,N+1)]+['B'+str(i) for i in range(q+1)]+['S']
    lengths={}; pure_nodes={}
    def nt(R): return sum(isinstance(x,str) for z in R[2] for x in z)
    def rlen(R): return nt(R)+sum(lengths[B] for B in R[1])
    for A in order:
        lengths[A]=min(rlen(R) for R in by[A])
        pure_nodes[A]=min((1+sum(pure_nodes[B] for B in R[1]) for R in by[A]
                           if all(x=='a' for z in R[2] for x in z if isinstance(x,str))),default=inf)
    ctx={A:inf for A in arity}; ctx['S']=0
    for A in reversed(order):
        for R in by[A]:
            for B in R[1]:ctx[B]=min(ctx[B],ctx[A]+rlen(R)-lengths[B])
    th=max(ctx[A]+rlen(R) for R in rules for A in [R[0]])
    assert th==2**(q+1)+d+1
    assert pure_nodes['S']==2**(q+1)
    size=len(arity)+sum(1+len(ch)+sum(map(len,outs)) for A,ch,outs in rules)
    return {'d':d,'q':q,'nested':nested,'N':N,'nonterminals':len(arity),'rules':len(rules),'size':size,'theta':th,'min_a_tree_nodes':pure_nodes['S']}

def small_grammar_language(d,q,nested=False):
    N,arity,rules=grammar(d,q,nested); by=defaultdict(list)
    for R in rules:by[R[0]].append(R)
    order=['A'+str(n) for n in range(1,N+1)]+['B'+str(i) for i in range(q+1)]+['S']
    from itertools import product
    lang={}
    for A in order:
        result=set()
        for _,ch,outs in by[A]:
            for vals in product(*(lang[B] for B in ch)):
                result.add(tuple(''.join(x if isinstance(x,str) else vals[x[0]][x[1]] for x in z) for z in outs))
        lang[A]=result
    assert {w[0] for w in lang['S']}==stage_language(N,d)
    return len(lang['S'])

L40=set('''aaabc aabac aabca abaac abaca abcaa baaac baaca bacaa bcaaa
aaaaac aaaaca aaaacb aaacaa aaacab aaacba aacaaa aacaab aacaba aacbaa
acaaaa acaaab acaaba acabaa acbaaa caaaaa caaaab caaaba caabaa cabaaa
cbaaaa aaaaaab aaaaaba aaaabaa aaabaaa aabaaaa abaaaaa baaaaaa aaaaaaaa bc'''.split())
W48=set('''aaabbcc aaabcbc aaabccb aaacbbc aaacbcb aaaccbb
aabbcca aabcabc aabcacb aabcbca aabccba aacbabc aacbacb aacbbca aacbcba aaccbba
abbccaa abcaabc abcaacb abcabca abcacba abcbcaa abccbaa acbaabc acbaacb acbabca acbacba acbbcaa acbcbaa accbbaa
bbccaaa bcaaabc bcaaacb bcaabca bcaacba bcabcaa bcacbaa bcbcaaa bccbaaa
cbaaabc cbaaacb cbaabca cbaacba cbabcaa cbacbaa cbbcaaa cbcbaaa ccbbaaa'''.split())
L67={'a'*10}|{'a'*i+z+'a'*(8-i) for i in range(9) for z in ('bc','cb')}|W48

def evaluate_marked_tree(d,q,selected,nested=False):
    def rec(i,index):
        if i==1 and index in selected:return ('bb','cc')
        if i==0:return ('a'*(d//2),'a'*(d//2))
        x=rec(i-1,2*index);y=rec(i-1,2*index+1)
        return (x[0]+y[0],y[1]+x[1] if nested else x[1]+y[1])
    x=rec(q,0)
    return 'a'+x[0]+'a'+x[1]+'a'

def run():
    for label,L in [('X1_40',L40),('CA_67',L67)]+[(f'stage_N{N}_d4',stage_language(N,4)) for N in range(8,12)]:
        counts=exact_distributions(L); rectangles=exact_rectangles(L)
        print(label,'words',len(L),'tuples/contexts/comparisons',counts,'rectangles',rectangles,'EXACT PASS')
    assert len(L40)==40 and 'bc' in L40 and 'acb' not in L40
    assert len(L67)==67 and 'bccbaaa' in L67 and 'bccb'+'a'*6 not in L67
    for mode in [False,True]:
        print('SMALL GRAMMAR EXACT LANGUAGE',mode,small_grammar_language(4,1,mode))
        print('CONCRETE GRAMMAR',json.dumps(grammar_audit(64,4,mode),sort_keys=True))
    N=1027; d=64; delta=128; kap='bbacc'; h=129; lam=898; budget=769
    for p,g,r in [(129,449,321),(193,449,257),(129,641,129),(193,513,193)]:
        w='a'*p+'bb'+'a'*g+'cc'+'a'*r
        assert member(w,N,d) and w.count('a')==N-delta and p+r>=3
    for w in ['a'*129+'bbbb'+'a'*385+'cccc'+'a'*257,
              'a'*129+'bbbb'+'a'*513+'cccc'+'a'*129]:
        assert member(w,N,d) and w.count('a')==N-2*delta
    assert evaluate_marked_tree(d,4,set())=='a'*N
    for mode,triples in [(False,[(129,449,321),(193,449,257)]),(True,[(129,641,129),(193,513,193)])]:
        for idx,(p,g,r) in zip((2,3),triples):
            assert evaluate_marked_tree(d,4,{idx},mode)=='a'*p+'bb'+'a'*g+'cc'+'a'*r
        expected='a'*129+'bbbb'+'a'*(513 if mode else 385)+'cccc'+'a'*(129 if mode else 257)
        assert evaluate_marked_tree(d,4,{2,3},mode)==expected
    print('ACTUAL MARKED DERIVATION TREES: 4 single + 2 double substitutions PASS')
    assert member('a'+kap+'a'*(lam-1),N,d)
    target='a'+kap+'a'+kap+'a'*(budget-2)
    assert target.count('a')==N-2*delta and not member(target,N,d)
    assert N>=4*delta+1 and budget==N-2*h and 128>97
    print('IH WITNESSES PASS: delta=128 h=129 lambda=898 outer_budget=769 total_a=771')
    for q in range(3,8):
        d=2**(q+2);N=d*2**q+3;theta=d+2**(q+1)+1
        assert 2*d>theta and N-2*(2*d+1)>=3
        print('ROOM FAMILY',q,d,N,theta,'N/delta',N/(2*d))
    print('No closure search. No cap/truncation. Full finite checks above; general claims use hand proofs.')
    print('ALL CHECKS PASSED')



# Generated once from archived Round14 code, not generated by this checker.
TR_CERT = {'seed': ['aaaaaaaaaaaaa', 'abcaaaaaaaaa', 'abcacbaaaaaa', 'acbaaaaaaaaaa'], 'steps': [(('a', 'aaaaaaaaa'), ('aa', 'aaaaaaaa'), ('', 'a', 'aa'), ('', 'bc', ''), 'aabcaaaaaaaa'), (('a', 'aaaaaaaaaa'), ('aa', 'aaaaaaaaa'), ('', 'a', 'a'), ('', 'cb', ''), 'aacbaaaaaaaaa'), (('abc',), ('bca',), ('a', 'aaaaaaaa'), ('', 'acbaaaaaa'), 'bcaacbaaaaaa'), (('acb',), ('cba',), ('a', 'aaaaaaaaa'), ('bca', 'aaaaaa'), 'bcacbaaaaaaa'), (('acb',), ('cba',), ('a', 'aaaaaaaaa'), ('bc', 'aaaaaaa'), 'bccbaaaaaaaa'), (('bca',), ('abc',), ('a', 'aaaaaaaa'), ('', 'cbaaaaaaa'), 'abccbaaaaaaa'), (('a', 'aaaaaaa'), ('aa', 'aaaaaa'), ('', 'a', 'aaaa'), ('', 'bccb', ''), 'aabccbaaaaaa'), (('abc',), ('bca',), ('a', 'aaaaaaaa'), ('', 'aaaaaaaaa'), 'bcaaaaaaaaaa'), (('acb',), ('cba',), ('a', 'aaaaaaaaa'), ('', 'aaaaaaaaaa'), 'cbaaaaaaaaaaa'), (('cbaa',), ('bca',), ('', 'aaaaaaaaa'), ('bc', 'aaaaaa'), 'bcbcaaaaaaa'), (('bc', 'aaaaaaaa'), ('cb', 'aaaaaaaaa'), ('', 'a', 'a'), ('', 'cb', ''), 'cbcbaaaaaaaaa'), (('cbaa',), ('bca',), ('', 'aaaaaaaaa'), ('cb', 'aaaaaaa'), 'cbbcaaaaaaaa'), (('bca',), ('abc',), ('a', 'aaaaaaaa'), ('bc', 'aaaaaa'), 'bcabcaaaaaa'), (('bca',), ('abc',), ('a', 'aaaaaaaa'), ('', 'bcaaaaaa'), 'abcbcaaaaaa'), (('a', 'aaaaaa'), ('aa', 'aaaaa'), ('', 'a', 'aaaaa'), ('', 'bcbc', ''), 'aabcbcaaaaa'), (('cb', 'aaaaaaa'), ('bc', 'aaaaaa'), ('', 'a', 'aaa'), ('b', 'c', ''), 'bbccaaaaaa'), (('bc', 'aaaaaa'), ('bccb', 'aaaa'), ('', 'a', 'aaa'), ('b', 'c', ''), 'bbccbcaaaa'), (('bcaaaa',), ('bcbca',), ('', 'aaaaaa'), ('bc', 'aaa'), 'bcbcbcaaaa'), (('bca',), ('abc',), ('a', 'aaaaaaaa'), ('cb', 'aaaaaaa'), 'cbabcaaaaaaa'), (('cb', 'bc'), ('bc', 'cb'), ('', 'a', 'aaaaaaa'), ('b', 'c', 'aaaa'), 'bbcccbaaaa'), (('bc', 'cbaa'), ('bc', 'bca'), ('', 'a', 'aaaaa'), ('b', 'c', 'aa'), 'bbccbcaaa')], 'w4': 'bbccbcaaaa', 'w7': 'bbccbcaaa'}

def replay_lift(u,v):
    mapping={'a':'a','b':u,'c':v}
    def mu(w):return ''.join(mapping[z] for z in w)
    K={mu(w) for w in TR_CERT['seed']}
    steps=list(TR_CERT['steps'])
    # Append explicit unary contradiction, which works even when u,v contain a.
    steps.append((('aaaa',),('aaa',),('bbccbc',''),('a'*9,''),'a'*12))
    for x,y,e,f,w in steps:
        x=tuple(map(mu,x));y=tuple(map(mu,y));e=tuple(map(mu,e));f=tuple(map(mu,f));w=mu(w)
        assert len(x)==len(y) in (1,2) and all(x) and all(y)
        assert tuple(map(set,x))==tuple(map(set,y))
        assert len(e)==len(f)==len(x)+1
        if len(x)==2:assert e[1] and f[1]
        assert fill(e,x) in K and fill(e,y) in K and fill(f,x) in K
        assert fill(f,y)==w
        K.add(w)
    assert 'a'*12 in K
    return len(steps)

def check_normalization():
    cases=0
    import re
    for L,N in [(L40,8),(L67,10)]+[(stage_language(n,4),n) for n in range(8,12)]:
        for w in L:
            if not w.startswith('a') or not w.endswith('a') or set(w)=={'a'}:continue
            left=len(w)-len(w.lstrip('a'));right=len(w)-len(w.rstrip('a'))
            if not 3<=left+right<N or not 0<w.count('a')<N:continue
            k=w[left:len(w)-right];norm=re.sub('a+','a',k)
            lam=w.count('a')-norm.count('a')
            assert 'a'+norm+'a'*(lam-1) in L
            cases+=1
    print('NORMALIZATION exact finite consequences',cases,'PASS')

if __name__=='__main__':
    run()
    total=0
    pairs=[('b','cc'),('bc','c'),('bb','cc'),('b','bc'),('b','b'),
           ('bac','c'),('baaaac','c'),('b','cac'),('a','b'),('bbacc','cabb')]
    for u,v in pairs:total+=replay_lift(u,v)
    print('LIFTED PRIMITIVE CERTIFICATES',len(pairs),'steps including unary contradiction',total,'PASS')
    check_normalization()
    print('FINAL EXIT: success (0)')

```

コードSHA-256：`7dac4279d86269ad6dacd69126ad5cdb2b5076d739e59cae4af45f0399a622c8`。

### B. 実行ログ

コマンド：`python3 round15_check.py > round15_check.log`。終了コード0。

```text
X1_40 words 40 tuples/contexts/comparisons (333, 2327, 924) rectangles 80660 EXACT PASS
CA_67 words 67 tuples/contexts/comparisons (1566, 12019, 5544) rectangles 1278526 EXACT PASS
stage_N8_d4 words 17 tuples/contexts/comparisons (226, 1017, 397) rectangles 13845 EXACT PASS
stage_N9_d4 words 27 tuples/contexts/comparisons (432, 2463, 1108) rectangles 80127 EXACT PASS
stage_N10_d4 words 44 tuples/contexts/comparisons (818, 5761, 2884) rectangles 412526 EXACT PASS
stage_N11_d4 words 72 tuples/contexts/comparisons (1532, 13171, 7174) rectangles 1903475 EXACT PASS
SMALL GRAMMAR EXACT LANGUAGE False 72
CONCRETE GRAMMAR {"N": 1027, "d": 64, "min_a_tree_nodes": 32, "nested": false, "nonterminals": 1033, "q": 4, "rules": 3025, "size": 14167, "theta": 97}
SMALL GRAMMAR EXACT LANGUAGE True 72
CONCRETE GRAMMAR {"N": 1027, "d": 64, "min_a_tree_nodes": 32, "nested": true, "nonterminals": 1033, "q": 4, "rules": 3025, "size": 14167, "theta": 97}
ACTUAL MARKED DERIVATION TREES: 4 single + 2 double substitutions PASS
IH WITNESSES PASS: delta=128 h=129 lambda=898 outer_budget=769 total_a=771
ROOM FAMILY 3 32 259 49 N/delta 4.046875
ROOM FAMILY 4 64 1027 97 N/delta 8.0234375
ROOM FAMILY 5 128 4099 193 N/delta 16.01171875
ROOM FAMILY 6 256 16387 385 N/delta 32.005859375
ROOM FAMILY 7 512 65539 769 N/delta 64.0029296875
No closure search. No cap/truncation. Full finite checks above; general claims use hand proofs.
ALL CHECKS PASSED
LIFTED PRIMITIVE CERTIFICATES 10 steps including unary contradiction 220 PASS
NORMALIZATION exact finite consequences 92 PASS
FINAL EXIT: success (0)
```

### C. 一次資料の取得識別子

以下のSHAはGitHubが返したblob識別子であり、SHA-256とは区別する。

```json
{
  "repository": "growupkuriyama-hub/Papers",
  "path": "02-v4-fixed-s-mcfg/v2",
  "fetched_ref": "main",
  "date_jst": "2026-11-16",
  "pr130_merge_commit": "67a9a37925181981357737726a151e0dfe72d038",
  "sources": [
    {
      "name": "HANDOFF_CURRENT.md",
      "github_blob_sha": "305d5a460ec6a4fbe3b4a61d825ce3c7ab3f1bfd"
    },
    {
      "name": "main.tex",
      "github_blob_sha": "b299a04baefe1313eb61b010d478b28033a42fbf"
    },
    {
      "name": "reviews/STATUS_FANOUT2_ROUNDS12_TO14_FABLE_2026-11-16.md",
      "github_blob_sha": "e27e42a6b094633e5afba21c3216cde9917f8bc6"
    },
    {
      "name": "reviews/audit_claude_round14_noncomm_Parikh_independent_2026-11-16.md",
      "github_blob_sha": "17039b70c24832d8ddfd64f4bd1c575ff3ef779c"
    },
    {
      "name": "reviews/audit_claude_round13_noncomm_U_independent_2026-11-15.md",
      "github_blob_sha": "2898c2d32c0bfb6a0317b7ad2aea5db32ffe8ec3"
    },
    {
      "name": "reviews/Fable_C_complete_independent_mathematical_audit_2026-11-15.md",
      "github_blob_sha": "923d665d073367d44c95210713a9caa31dca1af7"
    },
    {
      "name": "reviews/claude_round14_noncomm_Parikh_report_2026-11-15.md",
      "github_blob_sha": "d9733f47ba5a031e42d58c258e903a470fa8a78b"
    },
    {
      "name": "reviews/claude_round14_noncomm_Parikh_next_obligations_2026-11-15.md",
      "github_blob_sha": "5cd6ada7de5499a6d23a2d698bff09f2355341e0"
    },
    {
      "name": "reviews/ROUND14_COMPLETE_SOURCE_AUDIT_2026-11-16.md",
      "github_blob_sha": "992ec07c60301768c65109043ffcb6230ed17d6e"
    }
  ]
}

```

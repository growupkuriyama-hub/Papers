# 場合 II・分岐 (B) の定量的上界、(KL) の独立監査、分岐 (S) と場合 III の残差

**研究日**：2026-11-04　**対象**：三文字内容型付け、`op:fanout-two` の三文字の核、系列第二十報  
**原稿**：`growupkuriyama-hub/Papers/02-v2-lg-fanout-boundary/main.tex`、2026-11-04 に GitHub 接続から取得、blob `b72cd2ed648f802886f0ab7c60a72f9f40c0864b`。本文は研究ノートであり、論文本文の更新ではない。

## 0. 主張ごとの判定

| 主張 | 判定 | 根拠と限界 |
|---|---|---|
| 三つの旧基礎証明書 `bcc`, `bbc`, `bcb` | **独立に確認** | §1、付録A。初期13語から各3,3,4段を再生 |
| 四文字の基礎 `xpxxq`, `pxxqx` | **独立に確認** | §1、付録A。各4段、成分内容・前提3語・二穴中央を毎段検査 |
| 非消去準同型、左側 `a^{k-6d}` の持ち上げ | **独立に確認** | §2 の一般証明と24個の具体的実行 |
| (KL) の場合分けの網羅性 | **独立に確認** | §3 の証明と長さ9まで988語の列挙（列挙は補助） |
| **(KL) 全体**：仮定下で内部の `bb`/`cc` があればどちらかの四乗を強制 | **証明済み（前二項からの帰結）** | §3。四乗文字は、内部二重文字の文字とは限らない |
| 場合 II・(B) における共通根 `u∈{bc,cb}` | **証明済み（既報の鎖・分離補題を明示的に使用）** | §4。既報の一般鎖構成を本報内で一行ずつ証明し直したわけではない |
| (B) の損失 `d_X=φ j_X`、定数項なし | **証明済み** | §5。異なる指数を交差乗算し (R) を適用 |
| **(B) の定数付き評価** `μ_a≤max{4θ+12,K^{10}R^9θ}` | **証明済み（既報の例外計数・尺度補題に依拠する合成定理）** | §6。適用条件と依存先を全て表示。全体 `op:fanout-two` は解かない |
| 一色型の扱いが場合 II にも使える | **独立に確認（既存の補題の適用）** | §6.2。二文字影の飽和／非飽和で分類し、`b⁴`,`c⁴` は不要 |
| 分岐 (S) に同じ上界が出る | **未解決** | §7。鎖の積を入れ子の片側へ移す補題がない |
| 場合 III で `cc` を持つ**あらゆる**塊から `c⁴` が出る | **確認できず** | §8。両端が `b` の塊では既存証明書は `b⁴` のみを強制し得る |
| 場合 III の端点を限定した `c⁴` 強制 | **証明済み／(KL) の特別の場合** | §8。少なくとも一端が `c` なら `cc` を含む塊は排除できる |
| 文献での新規性・全ての型付き `τ` の上界 | **未確認／未解決** | §9。既報の構成と独立の新規定理かは未調査 |

## 1. 記号、推論規則、基礎証明書の再生

`Σ={a,b,c}`, `c(w)=supp(w)`、`L∈ C_{2,c}`、`a^k∈L`、`k=μ_a(L)≥5` とする。場合 II は、**どの受理語にも** `b⁴,c⁴` が因子として出現しない場合。`F∈{b,c}^+` は両文字を含み、`d≥1`。仮定は

- `SB(F^j,jd)`（`j=1,2,3`）：`a^sF^j a^t∈L`、`s,t≥1`, `s+t=k-jd`;
- 全正配分の分離二塊：`a^pFa^qFa^r∈L`、`p,q,r≥1`, `p+q+r=k-2d`;
- `k≥6d`。

`SUB_t` は、許容文脈 `E,H`、各成分非空の組 `X,Y`、`supp(X_i)=supp(Y_i)` の下で、`E[X],E[Y],H[X]∈L` から `H[Y]∈L` を得る規則 (`t=1,2`)。**二穴の間の固定部分は `E,H` とも非空**でなければならない。`L` の (2,c)-代入可能性による分布同値の直接の帰結である。

GitHub の `reviews/check_claude_kl_internal_2026-11-04.py` の `BASE` を読み、元の検査コードとは別に付録Aの再生器を作成した。種は各型板につき13語。旧三型板も含めた実行結果は次のとおり。

| 型板 | 強制された末語 | 段数 | 四乗 |
|---|---|---:|---|
| `bcc` | `abccbcbccccbca` | 3 | `c⁴` |
| `bbc` | `abbcbbbbccbbca` | 3 | `b⁴` |
| `bcb` | `abcbcbbbbcbcba` | 4 | `b⁴` |
| `xpxxq` | `aaxpxqxpxxxxqxpxqa` | 4 | `x⁴` |
| `pxxqx` | `apxqxpxxxxqxpxqxaa` | 4 | `x⁴` |

付録Aでは各段に対し、(i) 非空穴、(ii) 成分ごとの内容一致、(iii) 二穴中央固定部非空、(iv) 前提三語が初期種または過去の帰結、(v) 帰結が未登録の語、を検証した。したがって、単なる探索時の推測でなく**再生可能な有限推論証明書**である。

## 2. 四文字からの持ち上げの健全性

`F=xPxxQ` の場合、抽象型板を `B=xpxxq`、`h(a)=a^d,h(x)=x,h(p)=P,h(q)=Q` とする。`F=PxxQx` には `B=pxxqx` を使う。`P,Q∈{b,c}^+`（具体的には文字 x と同じでもよい）とする。全証明書の各語 `w` を `a^{k-6d}h(w)` へ送る。

任意の `t` 穴文脈 `E=(e_0,…,e_t)` の像を

`E'=(a^{k-6d}h(e_0),h(e_1),…,h(e_t))`

とすると、`E'[h(X)]=a^{k-6d}h(E[X])` が文字列として成立する。`t=2` で中央 `e_1` が非空なら、非消去性から `h(e_1)` も非空。`supp(X_i)=supp(Y_i)` なら、その文字集合の像の和集合も等しいため `supp(h(X_i))=supp(h(Y_i))`。よって一段の `SUB_t` はそのまま健全な一段へ移る。**抽象字母が四文字であってもこの論証は変わらない**。四文字言語自身が三文字対象クラスに属するという主張は用いていない。

基礎種の像は、`a^6 → a^k`、`a^sB^ja^{6-j-s}→a^{k-6d+ds}F^ja^{d(6-j-s)}`、分離二塊の像は `a^{k-6d+dp}Fa^{dq}Fa^{dr}`（`p+q+r=4`）。両端・中央の a の連は全て正、a の総数も所定の `k-jd` または `k-2d`。従って**全ての像の初期種が仮定に含まれる**。末語の `x⁴` は `h(x⁴)=x⁴` として保存される。

独立コードで `xpxxq`,`pxxqx` に対して6具体塊×4組 `(k,d)=(6,1),(12,2),(21,3),(15,2)` の計24個を再生し、全件成功した。任意長への保証は直前の一般証明による。

## 3. (KL) 全体の証明

**補題 KL（完全版）。** 上記の全ての種と `k≥6d` があるとき、`F` が `bb` または `cc` を含めば、ある受理語に `b⁴` または `c⁴` が出現する。

**証明。** `xx` を F 内に一つ取り、他の文字を y とする。

1. F が `xx` で始まるなら `F=xxU` で U に y が含まれる。型板 `bbc`（x=b、U=c の像）で `x⁴`。
2. F が `xx` で終わるなら `F=Uxx`。型板 `bcc` で `x⁴`。
3. F の両端が同じ文字 z なら `F=zUz` と書け、U は反対の文字を含む。型板 `bcb` で **`z⁴`**。ここで z と選んだ二重文字 x が違う場合があることに注意する。
4. 以上でなく、両端は異なる。`xx` の文字 x はどちらかの端に一致する。F が x で始まり y で終わるなら先頭は `xx` でないから、内部の `xx` の直前に少なくとも一文字あり、その後にも末尾 y がある。したがって `F=xPxxQ`, `P,Q≠ε`。反対向きなら `F=PxxQx`, `P,Q≠ε`。§1–2 の二つの四文字型板で `x⁴`。

これらは重複を許すが漏れがない。付録Aは全長3〜9の両文字語で内部に二重文字を持つ988語について同じ分類が成功することも確認した。列挙は一般証明の代わりではない。∎

**付記（重要）**：この補題の結論は「選んだ内部 `xx` の x の四乗を必ず強制」ではない。場合3は **端点文字 z の四乗**を強制する。場合 III でこの違いが必要になる。

## 4. 場合 II の分岐 (B)：共通交代根

`G` は reduced good、fan-out≤2、rank≤r、`v=|V|`、`θ=\bar θ_G≥1`、`T` は最短 `a^k` の一様・節点数最小導出。既報 `claude_straddle` と `claude_cross_core` の記号に従い、`N=25θ³` とし、内部の両文字型ラベル X が「低い」とは `ℓ_X≤k/(2N)`、その短い代表から得る a-free 塊を `F_X`、損失を `d_X=ℓ_X-|ρ_X|_a` とする。`1≤d_X≤ℓ_X≤k/(50θ³)`、`|F_X|≤θ`。

(B) は、小さい損失を持つ二つの両文字塊を a の正の連で隔てた受理語が存在する分岐。**使う既報結果を明示**する：(i) 低い内部 X は `SB(F_X,d_X)` を持つ、(ii) (B) では任意の長さ `m≤24θ³` の低い内部ラベルの列の連結塊 `C=F_{X_1}⋯F_{X_m}` が `SB(C,Σd_{X_i})` を持つ。これらは一穴の交換補題E、a の連の自己融合 F′、初期二塊による命題4.1 の帰納法から出る。さらに `SB(C,δ)` の証拠語で左の a の連を2以上に取り、`D(a²C)=D(aCa)` を使用して `a^pCa^qCa^r` を分離して作れる。これが正配分全体へ広がるのは a の連の再配分による。必要な正の a の個数は下記予算で確保される。

- 原子 `F_X` なら `F_X,F_X²,F_X³` は1,2,3原子、いずれも `24θ³` 以下。`6d_X≤6k/(50θ³)≤k`。
- 異なるラベルの鎖 `C=F_XF_Y` なら `C,C²,C³` は2,4,6原子、`δ=d_X+d_Y≤k/(25θ³)`、ゆえに `6δ≤6k/(25θ³)≤k`。分離二塊も8原子以下の鎖ではなく、`SB(C)` から作るので同じ予算でよい。

したがってそれぞれに完全版 (KL) と、`F=zUz` を排除する旧補題を適用できる。場合 II ではどちらの四乗もないため、各低い内部 `F_X` には `bb`,`cc` がなく、同じ端点もない。よって `F_X=(bc)^{j_X}` または `(cb)^{j_X}`、`j_X≥1`。

もし二つの根が異なるなら `C=(bc)^i(cb)^j`（または逆順）は両端が同じ文字の塊となり、上の鎖の予算と `zUz` 型により矛盾する。従って低い内部ラベル全体に対し、**一つの `u∈{bc,cb}` が存在して `F_X=u^{j_X}`**。

この論証は既報の (i)(ii) を依存補題とする。既報の全ての文脈交換操作を本報内で逐次展開したとは主張しないが、今回必要な原子数、正配分、KL の予算を再点検した。

## 5. 新しい簡約：損失に定数項がない

**補題 5.1。** 場合 II・分岐(B)の全ての低い内部両文字ラベル X に対して、同じ `φ∈ℚ_{>0}` があって

`d_X=φ j_X`。

**証明。** ラベル X,Y を任意に取る。`F_X=u^{j_X}`, `F_Y=u^{j_Y}` だから、文字列として

`F_X^{j_Y}=u^{j_Xj_Y}=F_Y^{j_X}`。

前節の鎖補題はこれら両方について SB を与える。原子数は各々 `j_Y,j_X≤θ/2≤24θ³`、損失はそれぞれ `j_Yd_X, j_Xd_Y≤k/(100θ²)<k`。従って二つの受理語は共通の**完全に同一の a を除く文字列** `u^{j_Xj_Y}` を持ち、両方の a 個数が `(0,k)` に入る。既報の剛性 (R) を `σ_a`（a の連のみ縮める）について用いると、二つの a 個数は同じ：

`k-j_Yd_X=k-j_Xd_Y`、ゆえに `j_Yd_X=j_Xd_Y`。

一つの基準 X₀ を選んで `φ=d_{X₀}/j_{X₀}` と置けば全ての X で成立する。別のラベルの個数・塊の並べ方に対応する**定数項は存在しない**。空集合なら群を作らず結論は自明。∎

これは「同じ j の二ラベル」の比較を一般の異なる指数へ直接拡張するもの。交代根を共有することが不可欠である。

## 6. 定数付きの (B) 限定多項式上界

**定理 II-B（既報の一色型計数と尺度補題を組み込んだ形）。** 前節までの条件を満たし、場合 II の分岐(B)に入るとする。`r≥1`、`θ≥1` として

`E_B:=v(50θ³+θ+23)`, `K_B:=(2v+E_B)(2r+1)`, `R:=θ+2v+2`

と置く。このとき

**`μ_a(L) ≤ max{4θ+12, K_B^{10} R^9 θ}`**。

**証明。** `k<4θ+12` は自明。そうでなければ `T` の重い節点（総生成長 `>θ`）を以下に分類する。

| 区分 | 例外節点数の上界／群 |
|---|---|
| 二文字影が非飽和な一色型 | 高々 `18v`（二色の和） |
| 飽和な一色型でもラベル出現が少ないもの | 高々 `vθ` |
| 両文字型で内部でない節点 | 高々 `2v` |
| 高い両文字型 `ℓ_X>k/(2N)` | 高々 `2Nv=50θ³v` |
| 低いが内部出現1個だけのラベル | 高々 `3v` |
| 飽和な一色型で頻出のラベル | 色 x ごとに `d_X=α_x q_X`、`1≤q_X≤θ` の1次元群 |
| 低い内部両文字型 | §5 より `d_X=φ j_X`、`1≤j_X≤θ` の1次元群 |

例外の合計は `v(18+θ+2+50θ³+3)=E_B`。全分類が尽きる。両文字型では `ℓ_X=d_X+|ρ_X|_a∈[d_X,d_X+θ]`。一色型でも `ℓ_X=α_x q_X+p_X∈[α_xq_X,α_xq_X+θ]`。飽和色は b,c の**高々二つ**なので1次元群も高々二つ。両文字型の根冪群は高々一つ。従って線形パラメータ区分の次元の和は

`D ≤ 1+2=3`。

既報の尺度補題3.1 は、`D` 個の区分で生じる群値の相次ぐ尺度比を `K_B` 以下に抑える。尺度補題3.2 は `R`-疎な部分列の長さを `3D` 以下とする（部分和の単射による）。定理B型の帰結として

`k≤K_B^{3D+1}R^{3D}θ≤K_B^{10}R^9θ`。

ここで用いた尺度補題の仮定は「重い節点の例外数 ≤ E_B」「群の長さが `[D_g,D_g+θ]` に入る」「群の値が固定個数次元の整数点の線形形式で与えられる」の三点で、上の分類がそれぞれ満たす。∎

### 6.2 一色型を場合 II に流用してよい理由

第十報 `chatgpt_nested_bc_chain_2026-11-04.md` §3.1–3.2 の議論では、`L_x=L∩{a,x}^+` (`x=b,c`) が二文字内容型付けの代入可能言語であることと、`a⁴` の出現を使用する。`x⁴` が出現することは**前提ではない**。非飽和なら2つの離れた内部 x 連＋残した `aa` の矛盾から同深さの一色型重節点は高々9個、二色・深さ≤v で `18v`。飽和なら各色の頻出ラベルについて差し替え後の同一 x 個数・異なる `(0,k)` の a 個数の剛性から `d_B/q_B=α_x` を得る。両文字型節点はこれらの差し替えに使わない。このため場合 II でも同じ計数が成立する。

**本定理の射程**：これは `μ_a` の場合 II・(B) 限定上界である。分岐 (S)、場合 III、他の開始内容型および全型付き `τ` は対象外。既報の補題 E, F′、鎖、例外・尺度を依存する数学的合成結果であり、それぞれの元の査読・独立再証明まではここで完了していない。

## 7. 場合 II・分岐 (S)：確認できた必要条件

補題 T・N の設定では、関係のあるラベルは二成分に両文字を含む殻 `(A_X,B_X)` を持ち、型板 `a A a A a B a B a` と、反復入れ子 `A_X^m P B_X^m` を実現する。この補題の入れ子の予算は、各関係ラベルの `d_X≤k/(50θ³)` と、使用する殻数を限定することで確保できる。

場合 II では、各反復の語に `b⁴,c⁴` のどちらもない必要がある。したがって殻の一方が一色の冪 `x^j` なら4層を入れ子にした語は `x^{4j}` を含み矛盾する（既報 `claude_straddle` §6 の特殊結果）。さらに、片側 A の先頭と末尾がともに x で、それぞれ極大 x 連の長さを `s,t` とすれば、A² の接合の連は `x^{s+t}`、従って **`s+t≤3`** が必要。B にも同じ。これはただちに得られる必要条件であって、構造の線形化には足りない。

分岐(B)の証明は `F_XF_Y` の**任意の鎖**が存在することを本質的に使った。分岐(S)では入れ子の語 `A_X P B_X` はあっても `A_X²` 単独、`B_X²` 単独を一穴の SB 塊として得られない。従って (KL) を殻の片側へそのまま適用するのは論理的に不可。現状、殻の内部二重文字から四乗を強制する一般の二穴証明書は得ていない。**(S) の定数付き多項式上界は未解決**。

## 8. 場合 III：強制される四乗文字の区別

場合 III を `b⁴` が現れ、`c⁴` が現れない場合とする。§3 の (KL) が「何らかの四乗」と述べるだけでは矛盾にならない。

- `F=ccU` または `Ucc` で U が b を含むと、三文字型板に `x=c` を代入して **c⁴** が強制される。
- `F=cUc` で U が b を含むと、`bcb` 型板（端点文字 `x=c`）で **c⁴** が強制される。
- `F` の両端が異なり、その一方が c、内部にのみ `cc` があると、`cPccQ` または `PccQc` の四文字型板で **c⁴** が強制される。
- 一方 `F=bcccb` のように**両端が b で内部に cc がある**と、端点型 `bUb` から出るのは **b⁴** であり、場合 III では許される。現行の四文字型板でもこのケースは c を端に持たないため直接には覆えない。

従って、場合 III・(B) で同じ SB・分離の仮定を持つ低い塊 F は、「`cc` があり、少なくとも一端が c」または「両端とも c」ではあり得ない。しかし **内部 cc を両端 b が囲む場合を排除できていない**。そのため「c は必ず孤立し、b の連を縮めると交代骨格になる」とは主張できない。

## 9. 結了の三点と出典

1. **証明できたこと**：(KL) の完全独立再生と一般持ち上げ、(B) の共通根からの `d_X=φj_X`、既報の計数・尺度を用いた場合 II・(B) の `K_B^{10}R^9θ` 上界、場合 III の端点限定排除。
2. **止まった場所**：場合 II・分岐(S) の二穴の殻の内部剛性、および場合 III の `b…cc…b` の c 四乗強制。全ての型付き `τ` を抑える議論には進んでいない。
3. **次に絞る一点**：まず場合 II・(S) で、殻 `A,B` と核 `P` の `A^mPB^m` の種から、片側の内部 `xx` に対する二穴 `SUB_2` の有限証明書があるかを、`A,B` の両端型を固定して検査すること。場合 III では `F=bcccb` を最小対照として「c⁴ そのもの」が強制されるかを判別すること。

**取得した主なソース**：`main.tex` (`def:tuple-substitutable`, `lem:thickness-equivalence`, 付録二文字)、`reviews/chatgpt_key_lemma_2026-11-04.md`、`reviews/check_claude_kl_internal_2026-11-04.py`、`reviews/claude_straddle_2026-11-04.md` (§§3–4,6)、`reviews/claude_cross_core_2026-11-04.md` (命題4.1)、`reviews/chatgpt_nested_bc_chain_2026-11-04.md` (§3)、`reviews/claude_f_branching_2026-11-04.md` (§3.2–3.3)。これらはリポジトリの研究ノートで、個々の結論が刊行済み文献で先取されているかは**未確認**。

## 付録 A. Python 3 標準ライブラリの完全な独立再生器

Windows: `py -3 verify_case2_independent_20261104.py`。以下をそのまま保存して実行できる。基礎証明書は探索結果ではなく固定された推論列である。

```python
#!/usr/bin/env python3
"""Independent replay: component-support substitutability, k>=6*d. Python stdlib."""
from itertools import product

CERT = {
'xpxxq': [
(1, ('','aaa'), ('axpxxqa',), ('axpxxqxpxxq',), ('aaxpxxq','')),
(2, ('','x','a'), ('aaxp','xqxpxxqa'), ('aaxpx','qaxpxxq'), ('','xxqxpx','')),
(2, ('','x','a'), ('aaxpx','qxpxxqa'), ('aaxp','xqaxpxxq'), ('','xqxpxx','')),
(1, ('aaxp','xpxxq'), ('xxqaxpxxq',), ('xxxqxpxqa',), ('aaxpxqxpx',''))],
'pxxqx': [
(1, ('','aa'), ('aaapxxqx',), ('apxxqxapxxqx',), ('','pxxqxa')),
(2, ('','x','a'), ('aapxxqxpx','qxa'), ('apxxqxap','xqxa'), ('','xqxpxx','')),
(2, ('','x','a'), ('aapxxqxp','xqxa'), ('apxxqxpx','qxaa'), ('','xxqxpx','')),
(1, ('apxxqx','qxa'), ('apxxqxpxx',), ('apxqxpxxx',), ('','xqxpxqxaa'))]
}

BASE3 = {
'bcc': [
(2, ('','c','a'), ('aabc','bcca'), ('abccb','cbcca'), ('','cbcc','')),
(1, ('','aa'), ('aaabcc',), ('abccbccbcc',), ('','bcca')),
(1, ('abccb','cbcca'), ('cbcc',), ('ccbc',), ('abccbcbcc','a'))],
'bbc': [
(1, ('','aa'), ('aaabbc',), ('abbcbbcbbc',), ('','bbca')),
(2, ('','b','a'), ('aabbc','bca'), ('abbcb','cbbca'), ('','bbcb','')),
(1, ('abbc','bcbbca'), ('bbcb',), ('bbbc',), ('abbcb','cbbca'))],
'bcb': [
(1, ('','a'), ('aaabcba',), ('abcbaabcb',), ('a','')),
(2, ('','b','a'), ('aabcb','cba'), ('abc','aabcb'), ('','bcbb','')),
(2, ('','b','a'), ('aabc','bcba'), ('aabcb','cba'), ('','bbcb','')),
(1, ('','aabcb'), ('aabcb',), ('abcbcbb',), ('','bbcbcba'))],
}

def context_insert(c, v):
    assert len(c) == len(v)+1
    return ''.join(c[i]+v[i] for i in range(len(v)))+c[-1]

def initial(k,F,d):
    words={'a'*k}
    for n in (1,2,3):
        for left in range(1,k-n*d):
            words.add('a'*left+F*n+'a'*(k-n*d-left))
    for i in range(1,k-2*d):
        for j in range(1,k-2*d-i):
            words.add('a'*i+F+'a'*j+F+'a'*(k-2*d-i-j))
    return words

def verify(template,steps,hom,k,d,target,verbose=False):
    assert k>=6*d>=6
    mapword=lambda w:''.join(hom[ch] for ch in w)
    F=mapword(template); pad='a'*(k-6*d)
    seen=initial(k,F,d)
    if verbose: print('seedcount',len(seen),'template',template,'F',F,'k',k,'d',d)
    for i,(arity,oldc,oldx,oldy,newc) in enumerate(steps,1):
        E=(pad+mapword(oldc[0]),)+tuple(map(mapword,oldc[1:]))
        H=(pad+mapword(newc[0]),)+tuple(map(mapword,newc[1:]))
        X=tuple(map(mapword,oldx)); Y=tuple(map(mapword,oldy))
        assert arity in (1,2)
        assert len(X)==len(Y)==arity and len(E)==len(H)==arity+1
        assert all(X) and all(Y) and all(set(u)==set(v) for u,v in zip(X,Y))
        if arity==2: assert E[1]!='' and H[1]!=''
        witnesses=[context_insert(E,X),context_insert(E,Y),context_insert(H,X)]
        assert all(w in seen for w in witnesses), ('missing',template,i,[w for w in witnesses if w not in seen])
        forced=context_insert(H,Y)
        assert forced not in seen,('not new',i,forced)
        seen.add(forced)
        if verbose: print('step',i,'arity',arity,'forced',forced,'target',target in forced)
    assert target in forced,(template,forced,target)
    return len(seen),forced

def main():
    for tm,c in {**BASE3,**CERT}.items():
        last='c' if tm=='bcc' else ('b' if tm in ('bbc','bcb') else 'x')
        cnt,out=verify(tm,c,{z:z for z in 'abcpqx'},6,1,last*4,True)
        print('BASE PASS',tm,'nsteps',len(c),'terminal',out)
    examples=[('xpxxq','c','b','bc'),('xpxxq','b','cb','c'),('xpxxq','c','bbcb','cb'),
              ('pxxqx','c','bc','bb'),('pxxqx','b','cbc','cc'),('pxxqx','b','c','bcbc')]
    for tm,x,P,Q in examples:
        for k,d in ((6,1),(12,2),(21,3),(15,2)):
            h={'a':'a'*d,'x':x,'p':P,'q':Q}
            count,w=verify(tm,CERT[tm],h,k,d,x*4)
            print('LIFT PASS',tm,'F',''.join(h[c] for c in tm),'k',k,'d',d,'x',x,'output_len',len(w))
    # exhaustive word-decomposition check for all binary words through length 9:
    total=0
    for n in range(3,10):
        for v in map(''.join,product('bc',repeat=n)):
            if set(v)!={'b','c'} or ('bb' not in v and 'cc' not in v): continue
            x='b' if 'bb' in v else 'c'; xx=x+x; y=({'b','c'}-{x}).pop()
            good=(v.startswith(xx) or v.endswith(xx) or v[0]==v[-1]
              or (v.startswith(x) and v.endswith(y) and (v.find(xx)>=2) and (v.rfind(xx)+2<n))
              or (v.startswith(y) and v.endswith(x) and (v.find(xx)>=1) and (v.rfind(xx)+2<n-0)))
            # Note if chosen x occurs twice only at other edges, the first cases cover it.
            assert good,('case split',v,x)
            total+=1
    print('CASE SPLIT ENUM PASS n<=9:',total)
    print('INDEPENDENT REPLAY COMPLETE')

if __name__=='__main__':main()
```

### 実行ログ（標準出力、そのまま）

```text
seedcount 13 template bcc F bcc k 6 d 1
step 1 arity 2 forced abccbcbcccbcca target False
step 2 arity 1 forced abccbccbccbcca target False
step 3 arity 1 forced abccbcbccccbca target True
BASE PASS bcc nsteps 3 terminal abccbcbccccbca
seedcount 13 template bbc F bbc k 6 d 1
step 1 arity 1 forced abbcbbcbbcbbca target False
step 2 arity 2 forced abbcbbbcbcbbca target False
step 3 arity 1 forced abbcbbbbccbbca target True
BASE PASS bbc nsteps 3 terminal abbcbbbbccbbca
seedcount 13 template bcb F bcb k 6 d 1
step 1 arity 1 forced aabcbaabcb target False
step 2 arity 2 forced abcbcbbaabcb target False
step 3 arity 2 forced aabcbbbcbcba target False
step 4 arity 1 forced abcbcbbbbcbcba target True
BASE PASS bcb nsteps 4 terminal abcbcbbbbcbcba
seedcount 13 template xpxxq F xpxxq k 6 d 1
step 1 arity 1 forced aaxpxxqaxpxxqxpxxq target False
step 2 arity 2 forced aaxpxxxqxpxqaxpxxq target False
step 3 arity 2 forced aaxpxqxpxxxqaxpxxq target False
step 4 arity 1 forced aaxpxqxpxxxxqxpxqa target True
BASE PASS xpxxq nsteps 4 terminal aaxpxqxpxxxxqxpxqa
seedcount 13 template pxxqx F pxxqx k 6 d 1
step 1 arity 1 forced apxxqxapxxqxpxxqxa target False
step 2 arity 2 forced apxxqxapxqxpxxxqxa target False
step 3 arity 2 forced apxxqxpxxxqxpxqxaa target False
step 4 arity 1 forced apxqxpxxxxqxpxqxaa target True
BASE PASS pxxqx nsteps 4 terminal apxqxpxxxxqxpxqxaa
LIFT PASS xpxxq F cbccbc k 6 d 1 x c output_len 21
LIFT PASS xpxxq F cbccbc k 12 d 2 x c output_len 24
LIFT PASS xpxxq F cbccbc k 21 d 3 x c output_len 30
LIFT PASS xpxxq F cbccbc k 15 d 2 x c output_len 27
LIFT PASS xpxxq F bcbbbc k 6 d 1 x b output_len 21
LIFT PASS xpxxq F bcbbbc k 12 d 2 x b output_len 24
LIFT PASS xpxxq F bcbbbc k 21 d 3 x b output_len 30
LIFT PASS xpxxq F bcbbbc k 15 d 2 x b output_len 27
LIFT PASS xpxxq F cbbcbcccb k 6 d 1 x c output_len 30
LIFT PASS xpxxq F cbbcbcccb k 12 d 2 x c output_len 33
LIFT PASS xpxxq F cbbcbcccb k 21 d 3 x c output_len 39
LIFT PASS xpxxq F cbbcbcccb k 15 d 2 x c output_len 36
LIFT PASS pxxqx F bcccbbc k 6 d 1 x c output_len 24
LIFT PASS pxxqx F bcccbbc k 12 d 2 x c output_len 27
LIFT PASS pxxqx F bcccbbc k 21 d 3 x c output_len 33
LIFT PASS pxxqx F bcccbbc k 15 d 2 x c output_len 30
LIFT PASS pxxqx F cbcbbccb k 6 d 1 x b output_len 27
LIFT PASS pxxqx F cbcbbccb k 12 d 2 x b output_len 30
LIFT PASS pxxqx F cbcbbccb k 21 d 3 x b output_len 36
LIFT PASS pxxqx F cbcbbccb k 15 d 2 x b output_len 33
LIFT PASS pxxqx F cbbbcbcb k 6 d 1 x b output_len 27
LIFT PASS pxxqx F cbbbcbcb k 12 d 2 x b output_len 30
LIFT PASS pxxqx F cbbbcbcb k 21 d 3 x b output_len 36
LIFT PASS pxxqx F cbbbcbcb k 15 d 2 x b output_len 33
CASE SPLIT ENUM PASS n<=9: 988
INDEPENDENT REPLAY COMPLETE
```

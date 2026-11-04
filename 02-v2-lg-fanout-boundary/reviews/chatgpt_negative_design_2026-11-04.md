# 否定の向きの設計：文字欠損型 `ab` の指数的唯一語と二穴スロット移送

**研究日**：2026-11-04  
**論文**：栗山貴之、論文 #2、`op:fanout-two`（三文字内容型付け、系列第24報）  
**結論**：**反例は未構成。** 新たな候補族は、指数的な希少型、二次サイズ・二次規則厚さ、指数的な同一ラベル侵入反鎖を同時に実現するが、**全ての \(n\ge2\) で二穴代入可能性に違反**する。違反は一段の健全な `SUB_2` による。`n=2` の候補は一穴条件には合格し、二穴条件だけで失格となる。

## 0. 主張ごとの判定（最初に結論）

| 主張 | 判定 | 新旧・適用条件 |
|---|---|---|
| 原稿 `def:class-cmcf` の二穴中間部分は非空 | **独立に確認** | 現行 `main.tex` に明記。空成分・空中間を用いる交換は禁止 |
| `prop:rare-type` が与える希少型による特徴標本下界 | **独立に確認** | **所属 \(L\in C_{2,c}\)** を先に示す必要あり |
| 全成分が全文字型のときの線形 \(t_X,\tau_X\) | **独立に確認** | 原稿 `prop:full-content-types`（既報(134)が原稿(147)に反映） |
| 場合 II の (B) は多項式、(S) は未解決 | **独立に確認** | 既報(142) §6–7。殻の端連 \(s+t\le3\) は (S) の特殊条件 |
| 場合 I の侵入反鎖幅 \(h\) への還元 | **独立に確認** | 既報(138)(143)。\(h\) の一般多項式上界は未解決 |
| 同じ \((B,\pi)\) の全侵入節点を同じ生成組へ一様化できる | **確認できず** | (146) は**依頼・見込み**。結果の証明とは区別 |
| 相異なる核が \(\Omega(n/\log n)\) 要る | **独立に確認（射程を限定）** | (122) の \(\mu_a\ge2^{\Omega(n)}\)、\(v,\theta=n^{O(1)}\) のとき。単に \(\mu_a=n^{\omega(1)}\) というだけではこの量化にならない |
| 非負の加法重み一水準では \(\mu_a\) が多項式 | **独立に確認** | 既報(100)；代入可能性は不要 |
| 旧い倍増・Thue–Morse・符号・単一繊維の構成 | **独立に確認（既報の反証・制約）** | 本報の新族をそれらの成功例とは扱わない |
| **候補 \(G_n\) が reduced good、rank 2、fan-out 1、\(\|G_n\|=\tfrac{n(n+1)}2+9n+8\)** | **証明済み** | 本報 §2 |
| **候補の \(\bar\theta_{G_n}\le \tfrac{n(n+1)}2+3n+2\)** | **証明済み** | 本報 §2。十分な明示上界であり最適値とは主張しない |
| **\(\mu_{\{a,b\}}(L_n)=2^{n+1}\)**、その型の語は唯一 | **証明済み** | 本報 §2；まだ所属を意味しない |
| **同じ \((A_j,\pi=1)\) の無印侵入重節点が \(2^n/\operatorname{poly}(n)\) 個ある** | **証明済み** | 本報 §3。最短の `ab` 型導出に関する**文法的事実** |
| \(\{a,b\}\) 型が指数的なら \(L_n\in C_{2,c}\) | **反証** | 本報 §4。**全 \(n\ge2\) に有効な二穴証明書** |
| \(n=2\) は arity 1 を満たす | **証明済み（有限対象の全数検査）** | 本報 §5、実行済み標準ライブラリコード。無限族の arity 1 は示さない |
| 二穴スロット補完：`(ab)^N` と `abc(ab)^(N−2)` から位置 \(1,\dots,N-2\) の `c` が必要 | **証明済み／既知の `lem:power-transfer` の特別な場合** | 本報 §4。新しい一般原理とは主張しない |
| 候補を修理して \(C_{2,c}\) に属し、なお希少型が指数的となる | **未解決** | 本報 §6 |
| 上の候補スキーマ全体の禁止命題が文献上新規 | **未確認** | 論文中の power transfer に近い。先行研究の網羅検索なし |

**重要な論理的注意**：原稿 `prop:unique-two-letter-shapes` は二文字が**同一の冪等型**を持つという仮定を使う。内容型付けでは \(c(a)=\{a\}\ne\{b\}=c(b)\) なので、以下の交互語に**直接適用できない**。交互形を選ぶ動機にはなるが、定理を援用して所属を主張しない。

## 1. 資料と設計仕様

### 1.1 正本の照合

次を GitHub コネクタで**直接取得**した。

- [`main.tex`](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/main.tex)、Git blob `1bc97358a49b4e80eef96abb0eee6de4ca10eecf`。`def:standard-mcfg`, `def:grammar-properties`, `def:class-cmcf`, `lem:distinguishing`, `prop:rare-type`, `cor:distribution-representatives`, `prop:full-content-types`, `lem:power-transfer`, `op:fanout-two` を照合。
- [`README.md`](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/README.md)、Git blob `9e81af7c7eb1bcbb6fb29492c49b989ee63582f7`。Change log **(100)–(147)** を確認。なお README は長大な一行に多くの履歴が格納されている。
- [`reviews/STATUS_sl_fanout2_2026-11-01.md`](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/reviews/STATUS_sl_fanout2_2026-11-01.md)、Git blob `b3146f1b6b807b9909d2a971da06eb3f8a03be4b`。これは **11/1 時点の整理**であり、以後の変更は上記原稿・README・個別報告を優先した。
- 個別報告：[`chatgpt_weighted_codes`](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/reviews/chatgpt_weighted_codes_2026-11-02.md) (100)、[`chatgpt_nested_bc_chain`](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/reviews/chatgpt_nested_bc_chain_2026-11-04.md) (119)、[`claude_f_branching`](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/reviews/claude_f_branching_2026-11-04.md) (122)、[`claude_straddle`](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/reviews/claude_straddle_2026-11-04.md) (126)、[`chatgpt_case2_branches`](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/reviews/chatgpt_case2_branches_2026-11-04.md) (142)、[`chatgpt_typed_case1`](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/reviews/chatgpt_typed_case1_2026-11-04.md) (134)、[`chatgpt_intrusion2`](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/reviews/chatgpt_intrusion2_2026-11-04.md) (143)、[`chatgpt_skeleton_diversity`](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/reviews/chatgpt_skeleton_diversity_2026-11-02.md) (94)、[`chatgpt_parikh_closed_family`](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/reviews/chatgpt_parikh_closed_family_2026-11-01.md)、[`chatgpt_sl_fanout2`](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/reviews/chatgpt_sl_fanout2_2026-11-01.md)。

今回の主張の独立証明と、過去の報告が証明したと**記載している**事実を区別した。とくに (145)(146) は次の依頼文であって、解決済みの結果としては採用していない。

### 1.2 反例の必要条件・緊張関係

\(v=|V|\)、\(\theta=\bar\theta_G\)、\(\Sigma=\{a,b,c\}\)、fan-out \(\le2\)、rank \(\le r\)（固定 \(r\ge2\)）とする。

| 条件／路線 | 元の出典 | 地位 | 設計上の緊張 |
|---|---|---|---|
| 型 \(\Sigma\) は長くできない：全成分 \(\Sigma\) なら \(t_X\le md(2^m-1)^f(r+1)v\theta\) | 原稿 `prop:full-content-types`、(134)(147) | 証明済み | 稀な型には欠損文字が必須 |
| 可換群の剰余条件では長い「最初の違反」を隠せない | 原稿 `prop:abelian-filter-short` | 証明済み | 単なる Parikh 重みでは反例を作りにくい |
| 希少な唯一語には長い別型の随伴語も必要 | 原稿 `lem:unique-word-gap` | 証明済み | 安い規則枝と長い随伴語が、穴の共通文脈を生む |
| 純 `a` 標的・場合 I は多項式 | (126)(128) | 既報で証明／独立監査 | `a` 標的は場合 II・III へ限定 |
| 純 `a` 標的・場合 II の分岐 (B) は多項式 | (142) | 既報で証明 | 残り (S) は殻 \(A_X^m P B_X^m\)、二塊なし |
| (S) の端連 \(s+t\le3\) | (142) §7 | 特定殻への必要条件 | 殻の反復と四乗回避が衝突 |
| 核の種類 \(D\) が有界なら \(\mu_a\le K^{3D+1}R^{3D}\theta\) | (122) 定理B | 既報で証明 | 指数的 \(\mu_a\) には多くの核、しかし \(v,\theta\) は小さく |
| 両文字型の深い入れ子がないと重い節点数は多項式 | (119) 定理 (K) | 既報で証明 | 同一ラベルを大量に複製しつつ段数を確保 |
| 短い生成組に `b,c` の両方が必要な重いラベル | (110) 補題M | 既報で証明 | 短い逃げ道を多くすると比較可能な語も多くなる |
| 非負加法重みの一水準なら \(\mu_a\le(r+1)^2\theta^3\) | (100) 定理3.1 | 既報で証明 | 指数重みコードの単純設計を禁止 |
| 欠損型の最短型付き導出は侵入節点幅に帰着 | (138)(143) | 既報の還元、\(h\) は未有界 | 重い同一 \((B,\pi)\) を指数個並べる必要 |
| 各 `SUB` は**完成語の支持集合を不変**に保つ | (143) 補題2.1 | 証明済み | `abc` 側だけから `ab` 語への短縮は得られない |
| 同じ \((B,\pi)\) の侵入節点を同じ語に一様化 | (146) | 見込み・未確認 | 成立しても混合語の二穴位置交換の問題は残る |
| 括弧付き倍増、Thue–Morse、短符号、繊維型の旧失敗 | 原稿 `thm:doubling-no-lift`、(94)(100)(143) 等 | それぞれの仮定の下で反証済み | 短い代替規則が異なる内容位置へ侵入 |

**量化の区別**：`τ(G,c)` の多項式上界は特徴標本の多項式上界の**十分条件**であるが、反例の必要条件として「全ての \(\tau\) が超多項式」とは言えない。希少型 \(\mu_m\) と `prop:rare-type` を使うなら、所属した言語について**開始型一つ**を長くするだけでよい。本報はその負方向の最も直接的な路線を選ぶ。

## 2. 候補族：唯一の `ab` 型を交互語にする

**標的 (b)** を選ぶ。純 `a` 型ではなく、欠損文字 `c` を持つ開始型 \(m=\{a,b\}\) を狙う。`a` と `b` の交互列にして、単語全体の内部で `a` の連長による従来の単純な偶奇障害を避ける。

\(n\ge1\) に対して **明示的な CFG** \(G_n\) を

\[
\begin{aligned}
S&\to A_n,\\
A_0&\to ab,\\
A_1&\to A_0A_0\mid abc,\\
A_i&\to A_{i-1}A_{i-1}\mid a^icb,\qquad 2\le i\le n
\end{aligned} \tag{G}
\]

とする。記号は実際の端末語を表す（`a^icb` は長さ \(i+2\) の RHS）。通常の CFG なので fan-out は **1**、ランクは **2**、したがって fan-out \(\le2\) の許容表示である。

**命題 2.1（文法の全必要な定量条件；証明済み）**。

1. \(G_n\) は reduced good：全非終端に到達し生成可能。各規則は非削除・非置換・非併合・非空（原稿 `def:grammar-properties` の意味）。
2. \(\|G_n\|=\frac{n(n+1)}2+9n+8\)。
3. \(\bar\theta_{G_n}\le \Theta_n:=\frac{n(n+1)}2+3n+2\)。
4. `c` を含まない受理語は
   \[
      W_n=(ab)^{2^n}
   \]
   だけである。よって \(\mu_{\{a,b\}}(L_n)=|W_n|=2^{n+1}\)。
5. `b⁴` も `c⁴` も受理語の因子には現れない（場合 II）。実際、**全ての** `b`・`c` 連の長さが 1 である。

**証明**。規則が親より添字の小さい子にしか依存しないので非循環、到達可能、生産的。サイズ式は原稿の記号数による
\(\|G\|=|V|+\sum_R(1+\operatorname{rank}(R)+|\operatorname{template}(R)|)\)
であり、
\[
(n+2)+3+3+(5+4)+\sum_{i=2}^n\bigl(5+(i+3)\bigr)
=\tfrac{n(n+1)}2+9n+8.
\]

規則厚さの証人には、その規則のある \(A_i\) を導出の一本の枝に置き、上位の \(A_j\to A_{j-1}A_{j-1}\) の**他方**を最短の短い逃げ道にする。添字 \(j\ge2\) の兄弟の長さは高々 \(j+1\) （\(A_{j-1}\to a^{j-1}cb\) または \(A_1\to abc\)）。\(A_i\) の倍増規則自身も両子を短い語にして \(2(i+1)\) 文字以下、\(A_1\to A_0A_0\) は4文字。したがって全規則について成功導出の長さは
\[
2(n+1)+\sum_{j=2}^n(j+1)
\le \tfrac{n(n+1)}2+3n+2.
\]
\(A_0\) と単項 \(S\to A_n\) についても同じ上界に収まる。

`c` を含む規則は必ず完成語に `c` を残すので、`c` 無しなら全て倍増規則を使い \(A_0\to ab\) に達する。従って \(W_n\) は唯一の `ab` 型の語。逆に \(W_n\) を全倍増で導出できる。全規則の端末部分で `b,c` は単独であり、各非終端語は `a` から始まるので、連結境界にも `bb,cc` は発生しない。□

**注意**：原稿 `prop:rare-type` の前提 **\(L_n\in C_{2,c}\) はまだ示していない**。命題 2.1 のみから特徴標本の指数下界を結論してはならない。

## 3. 侵入反鎖幅まで指数的になる（所属は用いない）

既報(138)(143) の言葉に沿い、最短 `ab` 型開始導出 \(T_n\) に `a` と `b` の印を一つずつ選ぶ。これは全倍増で \(W_n\) を作る完全二分木であり、**長さが一意なので**最短導出である。

\(j_n:=\lceil\log_2\Theta_n\rceil\) とする。\(n\ge12\) なら \(2\le j_n<n\)、また
\(2^{j_n+1}>\Theta_n\ge\bar\theta_{G_n}\)。
深さ \(n-j_n\) の各 \(A_{j_n}\) 節点は `ab` 型の語を長さ \(2^{j_n+1}\) だけ導出するから重い。異なる節点同士は反鎖を成す。

配置 \(\pi=1\) の安全な `ab` 型生成の最短全長を \(\beta_{\{a,b\}}(A_j,1)\) と書く。全ての短い逃げ道には `c` が含まれ、`c` 無しの生成組は唯一 \((ab)^{2^j}\) なので、
\[
\beta_{\{a,b\}}(A_j,1)=2^{j+1}>\bar\theta_{G_n}.
\]
従って上の節点は、印を含む高々2個を除き、いずれも **\(\bar\theta\)-侵入節点**である。全て同じラベル \((A_{j_n},1)\) であり、
\[
\boxed{
h_n\ge 2^{n-j_n}-2
> \frac{2^n}{2\Theta_n}-2
=2^{n-O(\log n)}.}
\tag{3.1}
\]

これは **候補族に対する純粋な文法論的事実**で、代入可能性も `τ_X` の同質性補題も利用していない。(138)(143) が未解決として残した侵入反鎖の**幅だけ**なら容易に指数化できる。難しいのはこれを \(C_{2,c}\) **と両立させること**だと分かる。

## 4. 二穴による厳密な反証と、より一般の禁止スキーマ

### 4.1 一段の `SUB_2` 違反（全ての \(n\ge2\)）

\(N=2^n\ge4\) と置き、

\[
\begin{array}{lll}
x=((ab),\ (ab)^{N-2}),&
y=((ab)^{N-2},\ (ab)),\\
E=\Box_1\,ab\,\Box_2,&
F=\Box_1\,c\,\Box_2 .
\end{array}
\]

穴はすべて非空で、\(E,F\) の中央の固定語はそれぞれ `ab`,`c` ともに非空。各成分の内容は `ab` なので \(c^{(2)}(x)=c^{(2)}(y)\)。しかも
\[
E[x]=E[y]=(ab)^N=W_n\in L_n .
\]

一方
\[
F[x]=abc(ab)^{N-2}\in L_n
\]
である。これは \(A_n\) の完全二分木の**一番左の \(A_1\)** だけを `abc` にし、その他の \(A_1\) を `abab` にする導出である。

ところが
\[
F[y]=(ab)^{N-2}c(ab)\notin L_n.
\tag{4.1}
\]

**非所属の厳密な証明**。右辺には `c` がただ一つあり、その直前は `b` である。これが \(A_j\)（\(j\ge2\)）の逃げ道 \(a^jcb\) に由来することは不可能（その `c` の直前は必ず `a`）。ゆえに一番低い \(A_1\) の `abc` 由来でなければならない。他の全ての \(A_1\) は `abab` を導出するので、その前にある `ab` の**完全なブロック数は偶数**である。しかし
\[
F[y]=(ab)^{N-3}\,\underbrace{abc}_{A_1\text{ の逃げ道}}\,(ab)
\]
であり、左の `ab` ブロック数 \(N-3\) は奇数。矛盾。□

従って \(D^{(2)}_{L_n}(x)\) と \(D^{(2)}_{L_n}(y)\) は共通文脈 \(E\) を持ちながら、\(F\) の所属が一致しない。
\[
\boxed{L_n\notin C_{2,c}\qquad(n\ge2).}
\]

**失敗した量**：`arity 2` の分布同値。`arity 1` だけではこの反証を得られない。特に \(n=2\) では arity 1 を全数検査して成立が確認される（§5）。

### 4.2 取り出した一般的必要条件（スロット飽和）

**補題 4.2（許容二穴の位置移送；証明済み、既知の power-transfer の特例）。** \(L\in C_{2,c}\)、\(N\ge4\)、\((ab)^N\in L\)、\(abc(ab)^{N-2}\in L\) とすると、
\[
\boxed{
(ab)^k\,c\,(ab)^{N-1-k}\in L
\quad\text{for every }1\le k\le N-2.}
\tag{4.2}
\]

**証明**。上の \(E,F,x\) を固定し、任意の \(k=1,\dots,N-2\) に対して \(y_k=((ab)^k,(ab)^{N-1-k})\) を用いる。各成分の内容は `ab` であり、\(E[x]=E[y_k]=W_n\in L\)。また \(F[x]\in L\) なので `(2,c)` 代入可能性から \(F[y_k]\in L\)。□

この補題によって、長い交互語だけを残し安い `abc` 逃げ道を入れる設計には、**同じ Parikh ベクトルの少なくとも \(N-2\) 個の `c` 位置**を補完する義務があると分かる。ただし、これは指数的な文法サイズの下界ではない。多数の語を小文法で記述できる可能性は残る。

**命題 4.3（逃げ道スキーマ全体の禁止；証明済み）**。\(A_0\to ab\)、\(A_1\to A_0A_0\mid abc\)、\(A_i\to A_{i-1}A_{i-1}\mid d_i\)（\(i\ge2\)）で、各 \(d_i\) に `c` が現れ、かつ **どの `c` の直前も `a`** であるとする。この族は（その他の \(d_i\) の語形、長さ、符号の一意復号性とは無関係に）全 \(n\ge2\) で \(C_{2,c}\) に属さない。

**証明**。`c` を含まない語は依然として \(W_n\) のみである。左端 \(A_1\) を `abc` にすることで \(F[x]\) は存在する。\(F[y]\) の唯一の `c` は `b` に後続するから、いずれの高位逃げ道 \(d_i\) からも生成できない。残る可能性 \(A_1\to abc\) は §4.1 の偶奇に反する。□

これは「倍増を別符号にしただけでは修理できない」という、**具体的な構成クラスへのノーゴー命題**である。使用原理は原稿 `lem:power-transfer` の特例であり、数学史上新しい補題だとは主張しない。修理するには、少なくともこの**奇数スロットへの `c` 侵入**を生成規則で許すか、倍増木の配置構造自体を改変する必要がある。ただし、(4.2) を充足しても他の全ての一穴・二穴条件が成り立つわけではない。

## 5. 有限検査の方法・実行ログ

標準ライブラリのみの `negative_design_check.py` を実行した。`grammar_slice(n,cap)` は非循環の文法から長さ `cap` 以下を**厳密に**生成する。`occurrences(...,1)` と `occurrences(...,2)` は独立の列挙ループを持ち、後者は穴間に一文字以上の固定部分を要求する。違反候補は、**切片の分布を比較するだけでは採用しない**。必ず `exact_member(n,w)` が文法全体（切片の外も含む）の真の所属を返すことを確認する。

有限切片で `PASS` と出るのは、表示した `n=1,2,3` について `cap` がその言語の最大長以上であるため**その個別の有限言語では完全な検査**になっているからである。これを族全体の所属証明に転用していない。

**短い違反証明書（n=2、理論・プログラム両方で検証）**：
`x=(ab,abab)`, `y=(abab,ab)`, `E=□1 ab □2`, `F=□1 c □2`。  
`E[x]=E[y]=abababab∈L_2`、`F[x]=abcabab∈L_2`、`F[y]=ababcab∉L_2`。

**追加の診断**：`n=3` は一穴も失敗する。従って **「全ての \(n\) で arity 1 を満たし、arity 2 だけで失敗する」** とは主張しない。一般 \(n\ge2\) の不成立に用いるのは §4 の明示的二穴証明だけである。

### 実行コード全文

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Negative-design audit: finite slices, two arities, exact membership.
Python 3 standard library only.  Run: py -3 negative_design_check.py
"""
from collections import defaultdict
from functools import lru_cache
from itertools import combinations

def escape(i):
    return "abc" if i == 1 else "a" * i + "cb"

def grammar_slice(n, cap):
    """Exactly L(A_n) intersected with words of length <= cap."""
    assert n >= 1 and cap >= 1
    level = {"ab"} if cap >= 2 else set()
    for i in range(1, n + 1):
        nxt = {escape(i)} if len(escape(i)) <= cap else set()
        nxt |= {p + q for p in level for q in level
                if len(p) + len(q) <= cap}
        level = nxt
    return level

def exact_member(n, word):
    """Exact, unbounded membership for the acyclic CFG (not slice-based)."""
    @lru_cache(None)
    def inside(i, w):
        if i == 0:
            return w == "ab"
        if w == escape(i):
            return True
        return any(inside(i - 1, w[:k]) and inside(i - 1, w[k:])
                   for k in range(1, len(w)))
    return inside(n, word)

def occurrences(word, arity):
    """Positive holes; for arity 2 the fixed internal separator is nonempty."""
    m = len(word)
    if arity == 1:
        for i in range(m):
            for j in range(i + 1, m + 1):
                yield (word[i:j],), (word[:i], word[j:])
    else:
        assert arity == 2
        for i in range(m):
            for j in range(i + 1, m):
                for k in range(j + 1, m):
                    for l in range(k + 1, m + 1):
                        yield (word[i:j], word[k:l]), \
                              (word[:i], word[j:k], word[l:])

def content_tuple(tup):
    return tuple("".join(sorted(set(x))) for x in tup)

def fill(context, tup):
    assert len(context) == len(tup) + 1
    if len(tup) == 2:
        assert context[1]  # nonempty inter-hole separator
    return "".join(context[i] + tup[i]
                   for i in range(len(tup))) + context[-1]

def verify_certificate(n, arity, x, y, E, F):
    assert len(x) == len(y) == arity
    assert all(x) and all(y)
    assert content_tuple(x) == content_tuple(y)
    four = tuple(fill(context, tup)
                 for context, tup in ((E, x), (E, y), (F, x), (F, y)))
    status = tuple(exact_member(n, w) for w in four)
    assert status == (True, True, True, False), (four, status)
    return four

def find_arity_violation(n, cap, arity):
    """Discover with slice only; certify with exact grammar membership."""
    observed = grammar_slice(n, cap)
    dist = defaultdict(set)
    accepted_at_context = defaultdict(set)
    for w in sorted(observed, key=lambda z: (len(z), z)):
        for tup, ctx in occurrences(w, arity):
            dist[tup].add(ctx)
            accepted_at_context[(content_tuple(tup), ctx)].add(tup)
    for (_type, E), choices in sorted(
            accepted_at_context.items(),
            key=lambda kv: (sum(map(len, kv[0][1])), kv[0])):
        tuples = sorted(choices, key=lambda t: (sum(map(len, t)), t))
        for x, y in combinations(tuples, 2):
            if dist[x] == dist[y]:
                continue
            if not dist[x] - dist[y]:
                x, y = y, x
            for F in sorted(dist[x] - dist[y]):
                try:
                    four = verify_certificate(n, arity, x, y, E, F)
                except AssertionError:
                    continue  # slice edge artifact, NOT a genuine violation
                return (x, y, E, F, four)
    return None

def dyadic_certificate(n):
    assert n >= 2
    N = 2 ** n
    x = ("ab", "ab" * (N - 2))
    y = ("ab" * (N - 2), "ab")
    E = ("", "ab", "")
    F = ("", "c", "")
    four = verify_certificate(n, 2, x, y, E, F)
    return four

def main():
    for n in (1, 2, 3):
        full_cap = 2 ** (n + 1) + 10
        lang = grammar_slice(n, full_cap)
        assert all(exact_member(n, w) for w in lang)
        print("n=%d |L_n|=%d max_len=%d" %
              (n, len(lang), max(map(len, lang))))
        for d in (1, 2):
            result = find_arity_violation(n, full_cap, d)
            print("  arity=%d %s" %
                  (d, "PASS (exact finite L_n)" if result is None else "FAIL"))
            if result is not None:
                x, y, E, F, four = result
                print("   x=%s y=%s E=%s F=%s" % (x, y, E, F))
                print("   exact membership (E[x],E[y],F[x],F[y])="
                      + repr(tuple(exact_member(n, w) for w in four)))
    for n in (2, 3, 4):
        words = dyadic_certificate(n)
        print("dyadic n=%d lengths=%s statuses=%s" %
              (n, tuple(map(len, words)),
               tuple(exact_member(n, w) for w in words)))
    print("ALL REPORTED VIOLATIONS CHECKED BY EXACT GRAMMAR MEMBERSHIP")

if __name__ == "__main__":
    main()
```

### 実際の標準出力（転載、推測なし）

```text
n=1 |L_n|=2 max_len=4
  arity=1 PASS (exact finite L_n)
  arity=2 PASS (exact finite L_n)
n=2 |L_n|=5 max_len=8
  arity=1 PASS (exact finite L_n)
  arity=2 FAIL
   x=('ab', 'abab') y=('abab', 'ab') E=('', 'ab', '') F=('', 'c', '')
   exact membership (E[x],E[y],F[x],F[y])=(True, True, True, False)
n=3 |L_n|=26 max_len=16
  arity=1 FAIL
   x=('aacb',) y=('acbaacb',) E=('a', '') F=('', 'aacb')
   exact membership (E[x],E[y],F[x],F[y])=(True, True, True, False)
  arity=2 FAIL
   x=('a', 'acb') y=('a', 'cbaacb') E=('', 'a', '') F=('', 'acba', '')
   exact membership (E[x],E[y],F[x],F[y])=(True, True, True, False)
dyadic n=2 lengths=(8, 8, 7, 7) statuses=(True, True, True, False)
dyadic n=3 lengths=(16, 16, 15, 15) statuses=(True, True, True, False)
dyadic n=4 lengths=(32, 32, 31, 31) statuses=(True, True, True, False)
ALL REPORTED VIOLATIONS CHECKED BY EXACT GRAMMAR MEMBERSHIP
```

## 6. 判定・次に絞るべき一点

**証明できたこと**：三文字・内容型付け・rank 2・fan-out \(\le2\) の小文法で、欠損型 `ab` の指数的な唯一語と、同一 \((B,\pi)\) の指数的侵入反鎖幅を同時に構成できた。さらに全 \(n\ge2\) の二穴違反を**一段だけ**の証明書で示した。\(n=2\) では一穴条件を通過することも個別の厳密な全数検査で示した。従来の純 `a` に固有な殻 (S) の条件は、**別標的**の本族には適用できない。

**止まった場所**：要求された「全ての必要条件を満たし、かつ \(L_n\in C_{2,c}\)」には到達していない。従って `prop:rare-type` による特徴標本の指数下界も、`τ` によるデータ下界も**発生しない**。今回の結果は **反例の候補族を一つ一般式で排除したもの**であり、中心問題の解決ではない。

**次の一点**：純語 \(W_n=(ab)^{2^n}\) と、欠損型の多くの侵入節点を残したまま、補題 (4.2) の **\(N-2\) 個の位置移送を全て生成できる小型・低厚さの「可動欠陥」文法**を設計し、まず一穴条件（同内容の完成語が共有する文脈）を厳密に抑制する。その次に二穴を検証する。高位 `c` 逃げ道の符号を単に長くすることは、位置移送の欠陥を直さない。

**作用素と下界の射程**：もし将来この修理族について \(L_n\in C_{2,c}\)、\(\mu_{\{a,b\}}(L_n)=2^{n+1}\)、\(\|G_n\|\bar\theta_{G_n}=n^{O(1)}\) を**全て**証明できれば、固定 \(\Sigma=\{a,b,c\}\)、fan-out 2、rank cap \(r_{\max}\ge2\) について、`prop:rare-type` により \(\mathcal B^{\le r_{\max}}_{2,c}\)、\(\mathcal B_{2,c}\)、およびクラス全体に特徴標本を持つ任意の集合駆動作用素の特徴標本の**総符号長**が \(2^{n+1}+1\) 以上になる。しかし**現族にはこの条件文を適用できない**。

## 7. 文献上の位置づけ

この報告のスロット移送は、原稿 `lem:power-transfer` と通常の二穴分布の直接の特別化である。「新しい原理」として主張すべきではない。多段倍増の比較文脈の失敗は過去の (94)、(100)、(143) と同種であるが、今回の **欠損型 `ab` の交互唯一語・指数的侵入反鎖を同時に持つ明示表示**と、**すべての高位 `c` を `a` 直後に置く符号族全体の排除**はこの報告の検証可能な具体的成果として区別できる。独立した先行文献調査は未実施なので、文献上の新規性は**未確認**とする。

---

*この報告は研究用の検証ノートであり、`main.tex` や GitHub を変更していない。*

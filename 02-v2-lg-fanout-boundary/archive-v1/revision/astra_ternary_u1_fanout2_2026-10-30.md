# 三文字の U₁ 型付けと fan-out 2：証明できた部分クラスと未解決の核心

**指定ファイル名：`Ternary_U1_Fanout2_2026-10-30.md`**  
**対象：** Σ={a,b,c}、s(a)=s(b)=1、s(c)=ζ、fan-out≤2、rank≤2。  
**結論：一般の (P2) は本報告では未解決。肯定・否定のいずれも主張しない。**

本報告は先の LG の指数改善とは別の、後から指定された三文字 U₁ 問題を扱う。主な部分結果は、(i) **受理語中の c の極大連続区間が B 個以下なら、全ての reduced good 表示で特徴データ長が O((B+1)‖G‖²θ̄_G)**、(ii) 交互語と c の挿入からなる非可換な言語族の全組・全文脈に対する代入可能性、(iii) その族が下界にならない理由の全表示にわたる証明、(iv) 純部分が単一語の場合の二文字構造制限の独立再検証である。証明と計算による観測を以下で区別する。

## 1. 結論の要約表

| 主張 | 判定 | 範囲・根拠 |
|---|---|---|
| 三文字 U₁、fan-out=rank cap=2 の一般の (P2) | **未解決** | 一様な多項式も反例族も得ていない |
| 全受理語の c-run 数≤B ⇒ t_typ≤12|V|(4+5B)θ̄_G | **証明済み** | §3。文法側の命題で、代入可能性を使わない |
| 同じ仮定と (2,s)-代入可能性 ⇒ データ長 O((B+1)‖G‖²θ̄_G) | **証明済み** | §3。全ての reduced good 表示。B 固定なら要求する部分クラス |
| D-deep insertion がない ⇒ t_typ≤48D|V|θ̄_G、データ O(D‖G‖²θ̄_G) | **証明済み** | §4。既存メモ・現行原稿の結果を独立に再証明 |
| 位相を各文字が決める経路言語の型別加法量切片は、全ての arity で組代入可能 | **証明済み** | §5。内部区切り非空が不可欠 |
| P_{N,m}={(ab)^N}∪{(ab)^i c(ab)^{m−i}:0≤i≤m} は (2,s)-代入可能 | **証明済み** | §5。全 N≥1,m≥0。実験からの外挿ではない |
| P_{N,m} が小さい θ̄ に対する超多項式下界を与える | **反証済み** | §6。全表示で θ̄=t_typ=τ=μ*=max(2N,2m+1) |
| 深い挿入があれば文字ごとの Parikh 飽和になる | **反証済み** | §5。P_{N,2D} の (ab)^D c(ab)^D |
| 深い挿入の両側の純語の最小周期に一様な定数上界がある | **反証済み** | §8。Σ⁺ が反例。追加仮定なしでは成立しない |
| L の純部分が単一語 {w}、|w|≥7 ⇒ w は完全交互または内部が一定 | **証明済み** | §7。長さ7の有限部分は118件の全反例証明書を付した計算機補助証明 |
| 単純な周期倍増＋c 短絡の族が下界を与える | **反証済み** | §8。n≥2 で一穴代入可能性に反し、閉包が半分の長さの純語を強制 |
| FS 命題 C(i) の無制限な移送 | **反証済み** | §8。{aaa,abaa}、b が ζ 文字 |
| FS 命題8の有限言語の (2,s)-代入可能性 | **証明済み** | §5 の位相補題からの解析的証明と、独立な完全有限検査 |
| FS 定理Aの任意アルファベット版 | **未解決（本報告の独立認証として）** | 元メモと第二査読を確認したが、証明の前提には採用していない |
| 二文字 U₁ の多項式定理を三文字へ拡張 | **未解決** | 最新 main には二文字定理が追加されたが、ここでは前提にしない |

「証明済み」は以下に証明を掲載した主張に限定する。文献上の新規性は**未了**であり、独立に再証明したことは新規性を意味しない。

## 2. 原稿・研究メモとの照合

### 2.1 取得版

対象は Takayuki Kuriyama, *Polynomial Upper Bounds on Characteristic-Data Length for Multiple Context-Free Languages under Fixed Finite-Semigroup Typing* の [main.tex](https://github.com/growupkuriyama-hub/papers/blob/main/02_fixed-h-mcfg/main.tex)。再開後に main を再取得した。

- **最終照合版の Git blob SHA：`5f00b0d7dfdfd89d16b9f583a7b59b87514b33a5`**。
- UTF-8 の取得内容は **213794 bytes**。`SHA1(b"blob "+str(len(data)).encode()+b"\0"+data)` により上記 SHA と一致することを確認した。
- 再開前に取得した版は `10c50f014815d1bceb88e6f2278966aa89e422c4`。最終報告の基準はこの旧版ではない。
- 取得時点の最新版には `thm:binary-u1-polydata`、`lem:app-u1-shallow`、`rem:binary-u1-scope` が追加されている。`op:fanout-two` は、二文字 U₁ では肯定結果がある一方、**中立文字が二つ以上の場合を未解決**としている。依頼の「二文字の候補定理を前提にしない」という制約を維持する。
- blob SHA はファイル内容の識別子であり、commit SHA と混同しない。main は可変参照である。

### 2.2 定義の対応

| 原稿の label | 本報告での使用・確認 |
|---|---|
| `def:standard-mcfg` / `def:grammar-properties` | ‖G‖=|V|+Σ_R(1+rank(R)+テンプレートの端末・変数出現数)。good は λ-free、nondeleting、nonpermuting、nonmerging。二つの異なる子の変数を連接する通常の CFG 二分規則は good |
| `def:tuple-substitutable` | d=1,2 の双方。成分は非空。二穴文脈 E=(p,z,q) は z≠ε。型ベクトル一致と共有受理文脈から**全分布**の一致を要求 |
| `def:reconstruction` | 標本から作る作用素は B^{≤2}_{2,s}。特徴標本は、それを含む任意の有限 K′⊆L に対して復元が L となる意味 |
| `lem:thickness-equivalence` | θ_G(R) は R を一度以上使う成功導出の最短語長。θ_G=max_R θ_G(R)。各規則を同時に使う一つの導出は要求しない。各非終端の無型最短組、規則の端末長、短い導出文脈は θ̄_G 以下 |
| `lem:heavy-node-count` | typed label の経路上の無反復と、重い反鎖の個数を用いる。本報告 §3 では U₁ に必要な部分を再証明 |
| `cor:distribution-representatives` | τ_X は生成組に限らない。同じ型・全分布を持つ組の最短長。データ長≤N_typ(1+2θ̄_G+2τ)+1_{ε∈L} |
| `prop:rare-type` | μ*=max_t min{|w|:w∈L∩Σ⁺,s(w)=t}。特徴標本は各実現型を含む。μ* の超多項式下界は否定に十分だが、その上界だけでは肯定に足りない |
| `prop:three-letter-family` / `cor:typing-level-obstruction` / `rem:fanout-one-data` | 三文字倍増 K_n の一穴の下界は二穴のクラス所属を含意しない |
| `lem:power-transfer` | 非空の中央区切りを使う。同一周期語の移送は全長・Parikh ベクトルを保存し、短い代表の存在を直接は示さない |
| `thm:doubling-no-lift` | bracketed family を一般の固定有限型付けで排除する定理。今回の K₂ は別途具体的に全検査 |
| `thm:local-group-polydata` | 最新版は LG に対し二次上界。U₁ は LG でないので適用しない。実際 1U₁1=U₁ は群でない |
| `op:fanout-two` | 本問は中立文字二つの特定型付けについての残された問題 |

以下 v=|V|、θ=θ̄_G と書く。非空の対象では θ≥1。型付き非終端は高々4v個、非開始型付き規則は各元規則につき高々16個なので

\[
N_{\rm typ}\le4|V|+16|P|\le16\|G\|.
\tag{2.1}
\]

ε を分離する補助単位元は非空成分の実現型には現れない。新設される補助開始記号・そのリンクは原稿の N_typ に含めない。この点を使わない保守的な評価 81‖G‖ でも全ての多項式次数は同じである。

### 2.3 メモの取得と依存関係

依頼に挙げられたメモは、照合可能な [Research-Library](https://github.com/growupkuriyama-hub/Research-Library) の同名資料を取得して確認した。「査読で VALID」との記述を証明の代用にはしていない。

| ファイル（省略しない名前） | 取得 blob SHA | 本報告での扱い |
|---|---|---|
| ASTRA_LENGTH_SPECTRUM_2026-10-28.md | `3c5f5decb5494c769242c69d263528a9b781ddaf` | §6 で独立再証明 |
| ASTRA_LENGTH_SPECTRUM_AUDIT_2026-10-28.md | `4c8cf96409bafa0df1cbebfcfe1ef783c292925e` | 仮定・規則厚さの定義を照合 |
| ASTRA_PROBLEM_G_II_U1_Reduction_and_Singletons_2026-10-28.md | `f8e9ff1466a3ac83f989648d149cfd19c3026472` | §7 で新たに全118証明書を生成し再証明 |
| CLAUDE_FRESHSTART_I_General_MCFG_Characteristic_Data.md | `5b2b74006b94627178302254899e95713bd278bd` | 命題8と C(i) を独立検証。定理Aを仮定しない |
| CLAUDE_FRESHSTART_I_INDEPENDENT_AUDIT_2026-10-26.md | `3383295333b89dbed8d7ef1b9c5be245b468a931` | C(i) の反例を再検証 |
| CLAUDE_FRESHSTART_I_THEOREM_A_SECOND_REFEREE_2026-10-27.md | `da2fbc282b2b251265478f47347b1f3a747224ca` | 査読結果は参考情報のみ |
| CLAUDE_I_Fanout2_Characteristic_Data_Independent_Research.md | `17fdf79e6d5a5125b21a7452ef9415fdf86d492f` | shallow 論法を再証明、二文字の全体定理は不使用 |
| CLAUDE_I_INDEPENDENT_AUDIT_2026-10-26.md | `61d4c9610a71cc7457c17f9acd99c071d1ef0d85` | 適用範囲・未証明箇所の照合 |

最初の三つは同リポジトリの `notes/astra-fanout2/`、残りは `notes/claude-fanout2/`。メモ内の文字名は各主張の箇所で明示的に読み替える。arXiv:1409.6247 の未査読結果は使用していない。

## 3. c の連続区間が有界な部分クラス

c-run は語の中の極大な c の非空連続区間とする。単に c の個数を制限する仮定より弱く、例えば任意に長い c^j を一つの run と数える。

### 定理 3.1（文法側の上界）

G を上記設定の任意の reduced good MCFG とし、L(G) の全語の c-run 数が B 以下とする。B は非負整数でよい。このとき

\[
 t_{\rm typ}(G,s)\le12v(4+5B)\theta.
\tag{3.1}
\]

この主張には (2,s)-代入可能性を仮定しない。

**証明。** 各非終端 A について、無型の生成組 ω_A を総長≤θ で固定する。これは A の規則を含む長さ≤θ の成功導出の該当部分木から得られる。また各規則が直接書く端末数も≤θ。同様の成功導出から、全ての A-組を受理する導出文脈 E_A が存在する。

任意の実現型付き非終端 X=A_t に対し、総長を最小、同長なら節点数を最小にする導出木 T を取る。その根組を u とする。各節点に「元非終端と生成組の U₁ 型ベクトル」を付ける。同じラベルが一経路に二度現れれば、祖先部分木を子孫部分木で置き換えられる。U₁ の準同型性により根の型は保たれ、非削除性により長さは増えず、節点数は減る。よって各経路の節点数は≤4v。

根の純成分には先頭・末尾の一文字ずつを印し、ζ 成分には一つの c を印す。長さ一の純成分の二つの印は同じ位置でよい。印は合計≤4個。総長>θ の節点を重いと呼び、重い節点の任意の反鎖 H を取る。印を生成する部分木を含む節点は H 中に高々4個なので、これらを除いた集合を H₀ とする。

各 h∈H₀ について、その部分木だけを ω_{A(h)} に置き換えることを考える。根の印は全て残るので、元々 ζ の根成分は ζ のままである。もし元々純であった全成分も純のままなら、根型を保ったまま総長を真に減らせる。元の部分木長>θ≥|ω_{A(h)}| であり、全ての文字は根まで一度ずつ残るからである。最小性に矛盾する。したがって**各 h の置換は、元の純根成分の少なくとも一つに c を導入する**。

h の各成分は根組中の一つの連続区間として現れ、h は高々二つの区間を持つ。異なる h の区間は互いに素であり、交錯する順序でもよい。純根成分にある区間だけを見て、異なる所有者の区間が隙間ゼロで接する場合に、その所有者間に辺を張る。区間一つにつき左右高々二つの隣接区間しかないので、このグラフの最大次数は≤4。したがって、貪欲に一頂点とその近傍を除去していけば、大きさ≥|H₀|/5 の独立集合 I が取れる。

I の部分木を同時に ω へ置き換える。これは反鎖上の置換なので導出木として正当である。異なる選択所有者の純成分内区間の間には、少なくとも一つの**置換されない元の純文字**がある。理由は、元々隙間があればその文字が残り、間に非選択所有者の区間がある場合もその非空の元区間が残り、隙間ゼロで直接接する場合は独立性で排除したからである。よって各選択所有者が導入する c は、他の選択所有者が導入する c と同じ run にはならない。

さらに元の純根成分の両端は印した純文字のままである。したがって、別の根成分にある c や、E_A の固定部の c を経由してこれらの run が結合することもない。E_A に最終組を入れた成功語には少なくとも |I| 個の c-run がある。仮定より |I|≤B、従って |H₀|≤5B、|H|≤4+5B。

重い節点は祖先閉集合を作る。その葉は重い反鎖なので高々4+5B個。経路長≤4v より、重い節点の総数は≤4v(4+5B)。根が軽ければ |u|≤θ。重ければ、各端末は重い節点が書くか、重い節点の軽い子の部分木に属する。重い節点一つあたり、直接の端末≤θ、軽い子は高々二つでそれぞれ≤θ。従って |u|≤3θ·4v(4+5B)。全 X について (3.1) が従う。□

**境界・交錯の点検。** 長さ一・二の純根成分は端の印で全体が保護される。二つの置換ブロックの隣接は次数4のグラフで処理した。二成分の交錯を平面的・入れ子状と仮定していない。群の可換性等は一切使用しない。根型を保つ必要があるのは単独置換の最小性矛盾の場面である。同時置換では根型を保存すると主張せず、受理語の c-run 数の仮定に反することを用いる。

### 系 3.2（言語側の特徴データ）

さらに L∈C^{mcf}_{2,s}、G が L∩Σ⁺ の表示なら、両作用素について

\[
 \|K\|_+\le16\|G\|\bigl(1+2\theta+24v(4+5B)\theta\bigr)
 +\mathbf1_{\{\varepsilon\in L\}}.
\tag{3.2}
\]

**証明。** τ≤t_typ、(2.1)、定理3.1を `cor:distribution-representatives` に代入する。□

従って B が固定された部分クラスでは O(‖G‖²θ) が、B 自身が ‖G‖,θ の固定多項式で抑えられる場合にも多項式が得られる。**一般の L の B を多項式で抑えたわけではない。** 無限言語では B=∞ もあり、この系は一般 (P2) を解決しない。

## 4. 深い挿入のない場合の独立証明

### 定理 4.1

D≥1 とし、L(G) のどの語も、|x|=|y|=D、x,y∈{a,b}^D、c を含む z に対して xzy を因子として持たないとする。このとき

\[
 t_{\rm typ}(G,s)\le48Dv\theta.
\tag{4.1}
\]

代入可能性をさらに仮定すればデータは O(D‖G‖²θ)。

**証明。** 実現 X=A_t の導出のうち節点数最小の T を取る。同じ型付きラベルが一経路で反復すると切り詰められるので高さ≤4v。純根成分の最初と最後の min(D,成分長) 文字を印し、ζ 成分は c 一文字を印す。印は≤4D個。印を書いた節点とその祖先からなる骨格 H は≤16Dv節点。

H からぶら下がる部分木を、順に無型の ω_B（長さ≤θ）へ置き換える。全ての中間組は L_A(G) に属する。元の純成分の長さ≤2Dなら全位置が印されており、そこに置換対象区間はない。長い純成分では全置換区間が保護された先頭 D 文字と末尾 D 文字の間にある。途中で c が入ると、E_A に入れた受理語中に D-deep insertion が生じ、仮定に反する。従って純成分は純のまま。ζ 成分の印した c も残り、最終根型は t である。

各骨格節点の端末≤θ、その骨格外の子は高々二つで各≤θ だから、最終組の長さ≤3θ|H|≤48Dvθ。よって当該型にはこの長さの生成組がある。データ評価は前節と同じ原稿の系への代入による。□

これは任意の数の中立文字に通用する。最新原稿の `lem:app-u1-shallow` と一致し、先行メモの主張を無検証で借用していない。純因子長が R 以下なら D=R+1 としてこの結果が適用できる。

## 5. 非可換な候補族：トークンの境界をまたぐ穴も含む証明

「ab を一文字と見なせばよい」だけでは不十分である。穴が a と b の間で切られるからである。以下ではその切断を二状態の経路として処理する。

### 補題 5.1（文字が始点・終点を決める経路言語）

有限有向グラフの各文字は、**ちょうど一つの辺**のラベルであるとする。固定始点 p と固定終点 q を持つ経路のラベル言語を R とする。s を有限モノイドへの型付け、φ:Σ*→H を可換群への準同型、h_t∈H を型ごとに固定し、

\[
 L=\{w\in R\cap\Sigma^+:\varphi(w)=h_{s(w)}\}
\tag{5.1}
\]

と置く。この L は全ての arity d について、非空成分・非空内部区切りを使う組代入可能性を持つ。正則性・MCFL 性まではこの一般形では主張しない。

**証明。** 同じ型ベクトルの非空組 x,y が E=(v₀,…,v_d) を共有し、E[x],E[y]∈L とする。受理経路上の各非空固定文字列は、その最初の文字の辺から始点が、最後の文字の辺から終点が一意に決まる。内部 v_i は非空なので、各穴の両側の状態は固定される。両端で v₀ または v_d が空なら p または q がその状態を指定する。従って x_i と y_i は全て、同じ始点・終点を持つ有効な経路である。

各成分型が等しいので、E[x],E[y] の全体型も等しい。(5.1) より φ(E[x])=φ(E[y])。可換群で固定部を消去して

\[
 \sum_i\varphi(x_i)=\sum_i\varphi(y_i)
\tag{5.2}
\]

を得る。任意の許容 F に対し、各成分の経路の両端状態が一致することから F[x]∈R ⇔ F[y]∈R。全体型は等しく、(5.2) により全体 φ 値も等しい。よって F[x]∈L ⇔ F[y]∈L。これは全文脈での分布一致である。□

### 系 5.2（交互語への c 挿入）

N≥1、m≥0 に対し

\[
 P_{N,m}=\{(ab)^N\}\cup\{(ab)^i c(ab)^{m-i}:0\le i\le m\}
\tag{5.3}
\]

は全ての arity で組代入可能であり、特に C^{mcf}_{2,s} に属する。

**証明。** 状態0,1と辺 a:0→1、b:1→0、c:0→0 を使い、始点=終点=0 とする。R=(ab|c)*。φ(w)=(|w|_a,|w|_b,|w|_c)∈ℤ³、h₁=(N,N,0)、h_ζ=(m,m,1) と置けば (5.1) は (5.3) である。補題5.1が適用される。言語は有限なので、各語を開始記号の定数規則とする good CFG で生成できる。従って MCFL 条件も満たす。□

**深い挿入から可換性は出ない。** m=2D とすれば (ab)^D c(ab)^D が受理される。両側の純ブロック長は2Dで任意に大きい。一方、例えば m≥1 で受理語 c(ab)^m と同じ Parikh ベクトルを持つ a^m c b^m は受理されない。従って文字ごとの Parikh 飽和は成立しない。これは語の有限検査による発見に留まらず、全 D の族である。

**より広い重み族。** K,M≥1、N≥M に対して

\[
 W_{K,M,N}=\{(ab)^K\}\cup
 \{w\in(ab|c)^*:|w|_c\ge1,\ |w|_a+|w|_b+2M|w|_c=2N\}
\tag{5.4}
\]

も補題5.1で証明される。φ(a)=φ(b)=1、φ(c)=2M、h₁=2K、h_ζ=2N とすればよい。正の重みなので有限。これは複数個の c を許す非可換な候補部品であるが、**この全族で小さい θ に対する超多項式の μ* または τ を実現する文法は構成できていない**。

### FS 命題8の再証明

ここだけ FS の文字名を用い、s(a)=1、s(b)=s(c)=ζ とする。

\[
 F=\{a^8\}\cup\{a^i bc a^{6-i}:0\le i\le6\}.
\]

状態0,1、辺 a:0→0、b:0→1、c:1→0、始点=終点=0 を取れば R=(a|bc)*。φ を Parikh ベクトル、h₁=(8,0,0)、h_ζ=(6,1,1) として補題5.1を適用する。これで全ての非空組・全文脈について証明が完了し、計算ログでも d=1,2 の完全検査に通る。

## 6. 長さスペクトルと規則厚さ：候補族の下界能力の監査

### 補題 6.1（有界な長さ下降）

任意の reduced good G について μ=min{|w|:w∈L(G)} とする。長さℓ>μの任意の受理語から、長さℓ′の別の受理語を作れて

\[
 1\le\ell-\ell'\le\theta-\mu.
\tag{6.1}
\]

**証明。** 非終端 A の無型最短組長を d_A、A を根とする部分木を除去した成功導出の固定部の最短総長を o_A とする。線形・非削除性により、規則 R:A→ρ(B₁,…,B_r) を一度以上使う最短成功語の長さは正確に

\[
 \theta_G(R)=o_A+b_R,\quad
 b_R=|\rho|_{\Sigma}+\sum_j d_{B_j}.
\tag{6.2}
\]

右辺の導出を構成でき、逆にどの成功使用も外側≥o_A、各子≥d_{B_j} なので等号である。また o_A+d_A≥μ。

ℓ>μ の成功導出で、生成組長が自分の d_A より大きい節点のうち最深のものを選ぶ。根はその性質を持つので存在し、その子は全て最短長である。使用規則を R とすれば、この部分木を最短 A-組で置き換えたときの減少量は Δ=b_R−d_A>0 であり、

\[
 \Delta=(o_A+b_R)-(o_A+d_A)\le\theta_G(R)-\mu\le\theta-\mu.
\]

置換結果も成功語で、総長は正確に Δ 減る。□

### 系 6.2（スペクトル境界）

最短純受理語長 N が有限、ζ 型受理語の相異なる長さの個数が有限 q なら

\[
 N\le\mu+q(\theta-\mu).
\tag{6.3}
\]

また、受理語の長さがちょうど二種類 μ<M なら、**全ての reduced good 表示で θ=M**。

**証明。** N=μ なら自明。N>μ なら補題6.1を繰り返し、μに至る長さの真に減少する列を作る。N 未満の全項は最短純語の定義により ζ 型。これらは相異なる q 個以下の長さなので、下降回数≤q。各下降量≤θ−μ を加えれば (6.3)。二種類の場合は M からの最初の下降先が μ であり M−μ≤θ−μ、従って θ≥M。一方全成功語長≤Mだから全規則の最短成功使用も≤M。□

### 系 6.3（P_{N,m} の全表示に対する正確な値）

M=max(2N,2m+1) とする。P_{N,m} の任意の reduced good 表示 G に対して

\[
 \theta=t_{\rm typ}=\tau=\mu^*=M,
 \qquad \|K\|_+\le16\|G\|(1+4M).
\tag{6.4}
\]

**証明。** 受理長は偶数2Nと奇数2m+1の二つであるから、前系により θ=M。各型の語長は固定なので μ*=M。任意の型付き非終端の生成組は導出文脈に埋め込めて受理語になり、非削除性から組長≤M。よって t_typ≤M。μ*≤τ≤t_typ を合わせ全て等しい。データ評価は (2.1) と原稿の代表長の系による。□

この結論は、たまたま使用した文法が厚いという指摘より強い。**別の巧妙な表示に変更しても P_{N,m} の θ を M より小さくすることはできない。** 長い純語・非可換性・深い挿入・二組代入可能性を同時に満たすだけでは、下界にはならない。

## 7. 純部分が単一語の場合の構造制限

### 補題 7.1（純部分と因子への遺伝）

L が (2,s)-代入可能なら L₁=L∩{a,b}⁺ は型なしの二組代入可能言語である。また {w} が型なし二組代入可能なら、w の全ての非空因子 u について {u} もそうである。

**証明。** 前半は全成分と文脈を純文字上に制限する。型は全て1であり、L での分布一致を純文脈へ制限すると L₁ での分布一致を得る。後半は w=p u q とし、{u} の違反文脈 E,F があればその両端に p,q を付ける。共有受理語と一方の受理語は w になり、不受理側は自由モノイドの左右消去性により w と異なる。区切りの非空性は変わらない。従って {w} も違反する。□

### 定理 7.2（二文字の singleton、計算機補助の完全分類）

w∈{a,b}^n、n≥7 に対し、{w} が型なし二組代入可能であることと、次のいずれかが成り立つことは同値である。

1. w₂…w_{n−1} が同一文字の繰返しである。
2. w が完全交互である。

**十分性の証明。** d=1 では固定文脈と語から中身は一意。d=2 を考える。内部が a のみの場合、共通文脈 E で異なる切り出し u=(u₁,u₂),v=(v₁,v₂) があるなら、対称性によりある δ≥1 について u₁=v₁a^δ、v₂=a^δu₂ と書ける。切り出し位置の移動部分は必ず w の内部にあり a のみだからである。任意の F で F[u]=w なら、F の非空内部区切りも w の内部にあって a の正冪である。それを a^e と書けば

\[
 F[u]=P v_1a^{\delta}a^e u_2Q
     =P v_1a^e a^{\delta}u_2Q=F[v].
\]

逆も同様。内部が b の場合も同じ。完全交互の場合は、辺 a:0→1、b:1→0 の経路で全語長を n に固定する。始点・終点を w のものに固定すれば補題5.1（自明型、φ=長さ）の言語は {w} そのものである。

**必要性の有限部分。** n=7 の128語を全列挙し、上記二形の10語以外の118語それぞれについて E,F,x,y を出力した。各行は E[x]=E[y]=w、F[x]=w と F[y]≠w、またはその逆を満たす。全文は §12 の `SINGLETON_FAIL` 118行である。正当性は判定器の返答を信用するだけでなく `validate_certificate` による文字列連結・非空条件・型の直接照合でも確認している。10語は上記十分性の形そのものなので、これで長さ7の完全な有限証明となる。

**任意長への帰着。** 補題7.1により w の全ての長さ7因子はその10語のどれかでなければならない。w が aba または bab を含めば、それを含む長さ7窓は完全交互である。内部5文字が一定の7語形はこれらの三文字因子を含まないからである。隣接する長さ7窓は6文字重なり、その中に交互三文字因子があるので隣の窓も完全交互。左右に伝播して w 全体が完全交互になる。

そうでなければ全長さ7窓の内部5文字は一定である。隣接窓の内部は4文字重なるので、その一定文字は全窓で一致する。内部5文字区間の和集合は w₂…w_{n−1} 全体を覆う。従って w の内部は一定。□

**帰結と限界。** 純部分が単一語である否定候補は、長さ7以上ならこの二形だけ調べればよい。したがって長い非周期的・三乗回避的な純 singleton を埋め込む案は排除される。しかし純語が複数ある場合には適用できず、残る二形で μ* や τ が小さいという結論も出ない。この分類の発想は Problem G II メモに既にあり、本報告の成果は独立再証明・証明書再生成である。

## 8. 反例と失敗する候補の一般形

### 8.1 K₂ の明示的な二穴違反

K₂ の全語は

\[
\{\texttt{bbaabbaabb},\texttt{bbaabcacb},\texttt{bcacbaabb},
\texttt{bcaccacb},\texttt{cbaabc},\texttt{ccacc}\}.
\]

x=(bcac,cb)、y=(c,cc)、E=(ε,ca,ε) とすると型は両方 (ζ,ζ)、E[x]=bcaccacb∈K₂、E[y]=ccacc∈K₂。F=(b,a,acb) に対し

\[
 F[y]=\texttt{bcaccacb}\in K_2,
 \qquad F[x]=\texttt{bbcacacbacb}\notin K_2.
\]

E,F の中央は ca,a とも非空。これは全分布の不一致の完全な反例証明書である。一穴条件は六語の全分解について判定器が厳密に通過を確認した。二穴の失敗により今回のクラス所属はない。

### 8.2 無制限の純文字移送は成り立たない

この項だけ Σ={a,b}、s(a)=1、s(b)=ζ とする。L={aaa,abaa} は (2,s)-代入可能だが aaba∉L。

**代入可能性の直接証明。** 各全体型に属する語は一つだけである。同じ型ベクトルと同じ文脈で受理される二組は同じ語を作る。一穴なら中身は一意。二穴では中央固定文字列は語の厳密な内部に現れる。aaa には非空の厳密内部は中央一文字 a だけである。abaa には、内部位置で可能な中央文字列は b、a、ba で、それぞれ位置が一意である。従って外側固定部と中央の位置が決まれば二成分も一意。ゆえに共有文脈を持つ異なる同型組自体がなく、代入可能性を満たす。□

純語 a³ と a¹ba² があっても a²ba¹ は強制されない。FS C(i) で欠けた不等式は「移送する純成分の総長≤純の共有ホスト長−1」である。非空中央区切りのため、ホスト a³ から得られるのは総長≤2の組の同一視までであり、総長3の移送ではない。

### 8.3 周期倍増＋c 短絡

n≥1 に対し H_n を次の good CFG（開始 E_n）で定義する。

\[
 E_0\to ab,\qquad E_i\to E_{i-1}E_{i-1}\mid c\quad(1\le i\le n).
\tag{8.1}
\]

Σ,s,f=2,r_max=2 は族全体で固定され、実際の fan-out は1。この表示は reduced で

\[
 \|G_n\|=8n+4,\quad\theta=n+3,\quad\mu^*=2^{n+1}.
\tag{8.2}
\]

**計算式の証明。** 非終端 n+1 個、E₀ の規則サイズ3、各段の二分規則5と c 規則2で、合計8n+4。純語は一意に (ab)^{2^n}。c が受理されるので μ*=2^{n+1}。各 i≥1 の無型最短長は1。E_i（i≥1）に至る最短外側長は n−i（各上位二分の兄弟を c にする）、E₀ は n+1（最下位の兄弟 E₀ は ab で長さ2）。従って E₀ 規則と E₁ の二分規則の最短成功使用長は n+3、残る規則はそれ以下。これで θ=n+3。□

しかし n≥2 では一穴条件にさえ反する。u=(ab)^{2^{n−1}} と置くと c,uc,u²∈H_n であり、u は唯一の純語 u² と異なるので u∉H_n。

**強制補題。** 同じ設定の任意の一穴代入可能言語 L で c,uc,u²∈L、u 純なら u∈L。

**証明。** c と uc は同型で空の外側文脈を共有する。文脈 u□ で c を uc に置き換えると u²c∈L。次に純語 u と u² は文脈 □c を共有し、u² は空文脈で受理される。従って u も空文脈で受理される。□

よって (8.1) は全 n≥2 でクラスから外れる。閉包の実験でも n=2 の純長8から純長4が強制された。μ* の指数性だけを特徴データの下界と報告してはならない。

### 8.4 無条件の「深い挿入なら周期的」には反例がある

Σ⁺ は全ての組の分布が全許容文脈なので (2,s)-代入可能。任意の M に対し、純語 x=y=a^M b a^M と z=c を使った xzy を含む。この x の最小周期は M+1 である。実際 p≤M なら中央 b と p 文字前の a が衝突し、p=M+1 は周期条件を満たす。従って深い挿入だけから、両側の純語の最小周期に一様な定数上界は得られない。Σ⁺ が簡単な言語であることは、この構造命題への反例性を変えない。

## 9. 計算方法・実行結果

### 9.1 判定器が厳密である理由

有限言語 L に対し、受理語 w の全ての 0≤i<j≤|w| を一穴出現、全ての 0≤i<j<k<l≤|w| を二穴出現として列挙する。従って成分は非空、中央 w[j:k] も必ず非空。各 (E,型ベクトル) グループ内で一つの代表組を取り、他の組との**全分布**を照合する。

全分布は L の全語における指定文字列の全出現位置から再計算する。文字列長の恣意的な打切りはない。共通文脈を持つ組は必ずこの列挙に現れる。現れない組は分布が空であり、代入可能性の前件を満たさない。一つの代表との一致はグループ内の全組対の一致と同値なので、検査を省略していない。従って `check` の成功は入力した**有限言語そのもの**に対する厳密判定である。

closure は E[x],E[y],F[x] が既知で x,y の型ベクトルが等しければ F[y] を追加する。全追加に三つの前提と文脈を記録する。健全性は代入可能性の定義から直ちに従う。無限閉包の停止性は主張しない。長さ・語数・ラウンド制限に達した場合は `TRUNCATED` とし、閉包完成と表示しない。

文法計算は候補族の非循環 CFG に対して行う。各非終端の全語集合を動的計画で求め、各規則について (6.2) を計算する。外側の最短文脈を伝播させ、規則ごとの最短成功使用を**個別に**求める。τ は、代入可能性を通った候補に限り、各 A の固定した受理文脈 E_A と各実現型 t について

\[
 \tau_{A_t}=\min\{|x|:s(x)=t,\ E_A[x]\in L\}
\tag{9.1}
\]

で求める。(9.1) は代入可能性から「共有 E_A ⇒ 同一全分布」であり、逆向きも分布一致なら E_A を含むので正しい。生成語に限定しない。クラスに属さない文法では原稿の Cl(X) が保証されないため τ を `null`（適用外）とする。無理に生成組の最短長で代用していない。

### 9.2 n≤4 の正確な規則表と数値

周期挿入族の圧縮文法 Q_n は

\[
 P_0\to ab,\quad C_0\to c,\qquad
 P_i\to P_{i-1}P_{i-1},\quad
 C_i\to C_{i-1}P_{i-1}\mid P_{i-1}C_{i-1},\quad
 S\to P_n\mid C_n.
\tag{9.2}
\]

C_i は (ab)^{2^i−1} のトークン境界の任意の一箇所に c を挿入した語を生成する。帰納的に左右の二分範囲が全境界を覆うから、L(Q_n)=P_{2^n,2^n−1}。全非終端と規則が成功使用を持つので reduced。規則の変数は各子一つずつで、全て good。|V|=2n+3、規則サイズの合計=15n+11 より ‖Q_n‖=17n+14。θ,μ*,τ は系6.3より全て2^{n+1}。

| 族 | n | ‖G‖ | θ̄ | μ* | τ | 語数 | d=1,2 |
|---|---:|---:|---:|---:|---:|---:|---|
| Q_n | 1 | 31 | 4 | 4 | 4 | 3 | 両方通過 |
| Q_n | 2 | 48 | 8 | 8 | 8 | 5 | 両方通過 |
| Q_n | 3 | 65 | 16 | 16 | 16 | 9 | 両方通過 |
| Q_n | 4 | 82 | 32 | 32 | 32 | 17 | 両方通過 |
| G_n（8.1） | 1 | 12 | 4 | 4 | 4 | 2 | 両方通過 |
| G_n（8.1） | 2 | 20 | 5 | 8 | 適用外 | 5 | d=1 で失敗 |
| G_n（8.1） | 3 | 28 | 6 | 16 | 適用外 | 24 | d=1 で失敗 |
| G_n（8.1） | 4 | 36 | 7 | 32 | 適用外 | 455 | d=1 で失敗 |

これらの grammar は fan-out≤2 の範囲内だが実際は1である。**代入可能性の検査は d=2 まで実施**しており、文法の fan-out と代入条件の arity を混同していない。今回、実 fan-out=2 を必須とする新たな下界候補は構成していない。

### 9.3 系統列挙の正確な範囲

1. **二語の言語を6944個。** u は {a,b} 上の長さ3～5の全56語。v は {a,b,c} 上の長さ3～5で c がちょうど一個の全124語。各 L={u,v} を検査。通過5084、違反1860。通過例の長い方／短い方の長さ比の最大は5/3。有限の範囲内の最大にすぎない。
2. **長さ1,2の全12語から、要素数1～3の全298言語。** 一語12件全通過、二語66件中51通過、三語220件中76通過。通過例のうち Parikh 非飽和はそれぞれ6,36,56件。有限言語について、各 Parikh ベクトルの出現語数を対応する多項係数と比較して飽和を厳密に判定。
3. **二文字長さ7の全128 singleton。** 通過10、違反118。これは §7 の有限証明部分であり、全118証明書をログに収録。
4. **P_{N,m} の N,m=1,…,4 の16件。** 全て通過。
5. **重み位相族 W_{K,M,N} の K=1,…,4、M=1,…,3、N=M,…,M+3 の48件。** 全て通過。一般の代入可能性は §5 で別途証明。
6. **圧縮文法の二族それぞれ n=1,…,4。** 上表の数値を算出。Q_n は全語・全出現を検査。G_n は違反が見つかった時点で反例を返すが、その前に言語全体を正確に生成している。

ここでは言語の系統列挙を行った。全ての4～6非終端 MCFG の網羅列挙を実施したとは主張しない。それは前の LG 依頼の計算条件であり、今回の「小さな非可換言語の系統列挙」と区別する。

### 9.4 前向き強制の結果

(8.1) の n=2 の五語から開始。長さ上限10、語数上限80、最大6ラウンド。実際には第2ラウンドで長さ上限外の強制語が発生し、`TRUNCATED: length/word limit` として停止。追加16語、計21語。純語長は {8} から {4,8} となり、短い純語 abab が出現した。Parikh 飽和はしていない。全16追加の三前提証明書を §12 に収録する。

この実験は無限閉包の全体を計算したものではない。しかし各追加は無制限の代入可能な拡大言語すべてで強制されるので、**純語が短くなるという結論自体に打切りの問題はない**。さらに §8.3 の二段階の証明が全 n≥2 を扱う。

## 10. 試した方針、失敗の理由、残る補題

| 方針 | 得られたもの／失敗した具体的理由 |
|---|---|
| c への短絡規則で厚さを下げ、純語だけ倍増させる | θ=n+3、μ*=2^{n+1} は実現するが、一穴同値 c≡uc と純語の共有文脈 □c が純語 u を強制。クラス所属が失敗 |
| 非周期的な純 singleton に倍増を隠す | 純部分への遺伝と長さ7因子の全証明書で排除。長い二文字 singleton は完全交互か内部一定 |
| (ab)^N と一個の c の挿入位置を自由化する | 全 arity の代入可能性を満たす。しかし受理長二種類から全表示の θ が最大長に等しくなり、下界にならない |
| 深い挿入から文字ごとの可換性を導く | P_{N,m} が反例。得られるのは ab トークン単位の位相整合であり、a と b の自由交換ではない |
| 任意の長い純語から短周期を強制する | Σ⁺ の a^Mba^M が無条件命題を反証。純 singleton などの追加条件が必要 |
| 二文字証明の a の長い連を、長い純語に置換する | (ab)^j には長さ2の同一文字連すらない。一文字連で使えた a^i と a^{i′} の移送を、そのまま a,b の個数に適用できない |
| ab を単一の文字に符号化する | 穴は a|b を切断するので単純な符号化保存は無効。§5 の「各文字が唯一の辺」という追加構造でのみ修復した。一般の純語符号には適用できない |
| c-run 数を数えて重い反鎖を抑える | §3 で成功。ただし一般の L の c-run 数 B は無限でもよく、B の一様多項式評価は得ていない |
| length spectrum で μ* を抑える | q が小さい候補の排除には有効。しかし q が大きい場合に無力であり、そもそも μ* の上界だけでは τ を抑えない |
| FS 定理Aから部分可換類へ移す | Phase 言語での代入可能性は証明できたが、FS 定理Aの独立完全監査と、任意の元の G に対する θ 保存を伴う還元が未完成。前提にしない |
| t_typ を一律に多項式にする | 現行原稿は Σ⁺ 自体にも、c 短絡を持つ非終端を埋め込むと t_typ が指数となる例を示す。この方法は一般 U₁ では不適切。τ による緩和が必要 |

### 10.1 肯定に十分な、正確な未証明命題

次は生成組を要求せず、短い外側文脈だけで表した十分条件である。

**未証明命題 SC（短い文脈での実現）。** 固定多項式 Q が存在して、任意の L∈C^{mcf}_{2,s}、任意の reduced good fan-out≤2、rank≤2 表示 G、任意の d∈{1,2}、許容文脈 E∈𝔈_d（|E|_fix≤θ̄_G）、任意の t∈{1,ζ}^d について、

\[
 \{x\in(\Sigma^+)^d:s^{(d)}(x)=t,\ E[x]\in L\}\ne\varnothing
\]

なら、その集合に総長≤Q(‖G‖,θ̄_G) の組が存在する。

**SC が (P2) に十分な理由。** 原稿の厚さ補題で各 A の E_A を選び、各実現型 t に SC を適用する。得られた組は生成組でなくてよい。A_t の任意の生成組と E_A を共有し、同型なので、全分布が一致する。よって τ≤Q、データ≤16‖G‖(1+2θ̄+2Q)+1。SC 自体は証明していない。任意の短い文脈を量化しており、単に t_typ の別名ではない。

### 10.2 否定方向で残る条件

候補族には、(i) 純 singleton なら §7 の二形、(ii) 超多項式の長い純語を狙うなら §4 により深い挿入、(iii) 小さい θ なら §6 により十分多くの相異なる ζ 語長、(iv) §3 による制限を避けるだけの c-run 数、が必要となる。ただし (iii) は最短純語に対する必要条件であり、τ のみを大きくする別方式を排除しない。

残る最も具体的な検討対象は、複数の c と多数の受理長を許し、位相制約を保った族である。(5.4) は代入可能性を保証する部品になるが、それを小さい規則厚さで生成することと、全特徴標本に長い語を必要とさせることの両立は未解決である。

## 11. 論文に挿入する英語 LaTeX 案

以下は本報告で証明した部分結果のみを挿入する案である。三文字問題が解決したとは書かない。既存 shallow 補題・二文字定理を重複して追加しない。

```latex
\begin{theorem}[A bounded number of marker runs]
\label{thm:ternary-u1-bounded-runs}
Let $\Sigma=\{\mathtt a,\mathtt b,\mathtt c\}$ and let
$s(\mathtt a)=s(\mathtt b)=1$, $s(\mathtt c)=\zeta$ in $U_1$.
Let $G$ be reduced and good, of fan-out at most two and rank at
most two. Suppose that every word of $L(G)$ has at most $B$
maximal nonempty $\mathtt c$-runs. Then
\[
 t_{\mathrm{typ}}(G,s)
 \le 12|V|(4+5B)\bar\theta_G.
\]
If, in addition, $G$ presents $L\cap\Sigma^+$ for
$L\in\Cmcf{2}{s}$, both canonical reconstruction operators have
characteristic data of total encoded length
$O((B+1)\|G\|^2\bar\theta_G)$, with an additional datum for
$\varepsilon$ when necessary.
\end{theorem}

\begin{proof}
Put $\theta=\bar\theta_G$ and $v=|V|$. Choose, for each
nonterminal $A$, an untyped yield $\omega_A$ of total length at
most $\theta$. Such a yield exists by
Lemma~\ref{lem:thickness-equivalence}.
Fix a typed nonterminal and a derivation minimizing first yield
length and then the number of nodes. A typed label cannot repeat
on a path, so every path has at most $4v$ nodes.

Mark the first and last letters of each pure root component and
one $\mathtt c$ in each impure component. There are at most four
marks. From an antichain of nodes with yield length greater than
$\theta$, remove the at most four nodes containing a mark. For
each remaining node, replacing its subtree by $\omega_A$ must
introduce a $\mathtt c$ into an originally pure root component.
Otherwise all root types would be preserved, while the yield
length would strictly decrease.

Each remaining node owns at most two disjoint intervals in the
root tuple. Join distinct owners when their intervals in an
originally pure component touch with no letter between them.
The resulting graph has maximum degree at most four, and thus
has an independent set of size at least one fifth of its vertex
set. Replace all subtrees of these independent owners at once.
Distinct selected owners are separated, in each originally pure
component, by an unchanged pure letter. Each therefore introduces
a distinct $\mathtt c$-run. The marked pure endpoints prevent
these runs from merging through an outside derivational context.
The resulting successful word has at least as many runs as
selected owners. Hence the original heavy antichain has size
at most $4+5B$.

The heavy nodes form an ancestor-closed subtree with at most
$4+5B$ leaves and height at most $4v$. Each heavy node writes at
most $\theta$ terminals and has at most two light children, each
of yield length at most $\theta$. Thus the root yield has length
at most $3\theta\cdot4v(4+5B)$. A light root has length at most
$\theta$. This proves the first assertion without using tuple
substitutability. The data bound follows from
Corollary~\ref{cor:distribution-representatives},
$\tau\le t_{\mathrm{typ}}$, and $N_{\mathrm{typ}}=O(\|G\|)$.
\end{proof}

\begin{lemma}[Typed additive slices of a path language]
\label{lem:typed-path-slices}
Let $R$ be the language of paths between two fixed vertices of a
finite directed graph in which every alphabet symbol labels
exactly one edge. Let $s$ be a finite-monoid typing, let
$\varphi:\Sigma^*\to H$ be a morphism into an abelian group,
and fix $h_t\in H$ for each type $t$. Then
\[
 L=\{w\in R\cap\Sigma^+:\varphi(w)=h_{s(w)}\}
\]
is tuple-substitutable in every arity, when components and
internal context separators are required to be nonempty.
\end{lemma}

\begin{proof}
Suppose equal-type tuples $\tuple x,\tuple y$ share an accepting
context $E$. Each nonempty fixed separator determines its
initial and terminal vertices, since each of its letters labels
one edge. Together with the fixed endpoints of the whole path,
these separators determine both endpoints of every hole.
Consequently $x_i$ and $y_i$ are paths with identical endpoints
for every $i$. Moreover $E[\tuple x]$ and $E[\tuple y]$ have the
same total type, so cancellation of the fixed part in the abelian
group gives
$\sum_i\varphi(x_i)=\sum_i\varphi(y_i)$.
In an arbitrary context $F$, the two fillings are simultaneously
valid paths, have the same type, and have the same $\varphi$-value.
They therefore have identical membership in $L$.
\end{proof}

\begin{proposition}[Alternating pure words with one marker]
\label{prop:ternary-u1-periodic-insertion}
For $N\ge1$ and $m\ge0$, the language
\[
 P_{N,m}=\{(\mathtt{ab})^N\}\cup
 \{(\mathtt{ab})^i\mathtt c(\mathtt{ab})^{m-i}:0\le i\le m\}
\]
belongs to $\Cmcf{2}{s}$. For every reduced good presentation
$G$ of this language, putting $M=\max\{2N,2m+1\}$, one has
\[
 \bar\theta_G=t_{\mathrm{typ}}(G,s)=\tau(G,s)
 =\mu^\star(P_{N,m},s)=M.
\]
In particular, this family does not yield a superpolynomial
lower bound in grammar size and original rule thickness.
\end{proposition}

\begin{proof}
Use vertices $0,1$ and edges
$\mathtt a:0\to1$, $\mathtt b:1\to0$,
$\mathtt c:0\to0$, with both endpoints fixed at $0$.
Apply Lemma~\ref{lem:typed-path-slices} with the Parikh morphism
and targets $(N,N,0)$ and $(m,m,1)$. The language is finite and
hence has a good context-free presentation.

For completeness, consider any reduced good grammar. Let $d_A$
be the shortest yield length of $A$ and $o_A$ the shortest total
length of a derivational outside context for $A$. If a rule $R$
with left-hand side $A$ writes $c_R$ terminals and has children
$B_1,\ldots,B_r$, its shortest successful use has length
$o_A+c_R+\sum_jd_{B_j}$. Put $\mu=\min\{|w|:w\in L(G)\}$.
In a derivation of length greater than $\mu$, choose a deepest
node whose yield is not shortest for its nonterminal. Replacing
it by a shortest yield reduces the sentence length by a positive
amount at most $\bar\theta_G-\mu$, since its children already
have shortest lengths and $o_A+d_A\ge\mu$.

The language $P_{N,m}$ has exactly two lengths, $2N$ and $2m+1$.
Applying this decrease to a word of length $M$ shows
$M-\mu\le\bar\theta_G-\mu$, hence $\bar\theta_G\ge M$.
The reverse inequality holds because every successful word has
length at most $M$. Each realized yield type has a fixed length,
so $\mu^\star=M$. Every typed nonterminal yield embeds into a
successful word and therefore has total length at most $M$.
Finally $\mu^\star\le\tau\le t_{\mathrm{typ}}\le M$ proves all
remaining equalities.
\end{proof}

\begin{remark}
The preceding propositions leave the general three-letter
$U_1$ problem open. Deep insertions do not imply Parikh saturation:
$P_{N,2D}$ contains
$(\mathtt{ab})^D\mathtt c(\mathtt{ab})^D$, while it excludes
permutations with the same Parikh vector that violate the path
constraint. A polynomial bound on rare-type minima alone would
also not suffice; a bound on distribution representatives or a
different characteristic-sample construction is still needed.
\end{remark}
```

## 12. 再現用ソースコード全文と実行ログ全文

Python 標準ライブラリのみを使用。以下の Python ブロックを `verify.py` として保存し、`python3 -u verify.py` で再現できる。計測時間に依存する出力を除き、列挙・証明書の選択順は決定的である。実行環境は Python 3.12.14。終了コード0、最後の行は `ALL_ASSERTIONS_PASSED true`。

全文ログは最終ソースを実行した標準出力・標準エラーをそのまま収録する。探索用の先行試行を最終計算の結果と混在させない。§7 の118証明書も省略せず、このログに含める。

### 12.1 ソース全文

```python
#!/usr/bin/env python3
"""Standard library only; Python 3.11+. Exact finite language tests.
All comparisons use nonempty components and strictly nonempty inner gaps.
No bounded search is described as a decision procedure for infinite closure.
"""
from collections import defaultdict
from itertools import product, combinations
from functools import lru_cache
import json, hashlib, sys

def typ(x, marked='c'):
    return tuple(int(any(z in marked for z in u)) for u in x)

def occurrences(w, d):
    n = len(w)
    for i in range(n):
        for j in range(i + 1, n + 1):
            if d == 1:
                yield (w[i:j],), (w[:i], w[j:])
            else:
                for k in range(j + 1, n):
                    for l in range(k + 1, n + 1):
                        yield (w[i:j], w[k:l]), (w[:i], w[j:k], w[l:])

def fill(E, x):
    return ''.join(a + b for a, b in zip(E, x)) + E[-1]

def distribution(L, x):
    out = set()
    for w in L:
        i = w.find(x[0])
        while i >= 0:
            j = i + len(x[0])
            if len(x) == 1:
                out.add((w[:i], w[j:]))
            else:
                k = w.find(x[1], j + 1)
                while k >= 0:
                    out.add((w[:i], w[j:k], w[k + len(x[1]):]))
                    k = w.find(x[1], k + 1)
            i = w.find(x[0], i + 1)
    return frozenset(out)

def check(L, ds=(1, 2), marked='c'):
    L = frozenset(L)
    for d in ds:
        seen, cache = {}, {}
        for w in sorted(L, key=lambda w: (len(w), w)):
            for x, E in occurrences(w, d):
                key = (E, typ(x, marked))
                if key not in seen:
                    seen[key] = x
                    continue
                y = seen[key]
                if x == y:
                    continue
                for z in (x, y):
                    if z not in cache:
                        cache[z] = distribution(L, z)
                if cache[x] != cache[y]:
                    F = min(cache[x] ^ cache[y])
                    return dict(d=d, x=x, y=y, E=E, F=F,
                                Ex=fill(E, x), Ey=fill(E, y),
                                Fx=fill(F, x), Fy=fill(F, y))
    return None

def validate_certificate(L, cert, marked='c'):
    x, y, E, F = (cert[k] for k in ('x', 'y', 'E', 'F'))
    assert all(x) and all(y)
    assert len(x) == len(y) in (1, 2)
    assert len(E) == len(F) == len(x) + 1
    if len(x) == 2:
        assert E[1] and F[1]
    assert typ(x, marked) == typ(y, marked)
    assert fill(E, x) in L and fill(E, y) in L
    assert (fill(F, x) in L) != (fill(F, y) in L)

def closure(L, max_length=12, max_words=120, rounds=8, marked='c'):
    """Sound forward inference. Returns CLOSED only after a complete sweep.
    Limits stop additions, never certify a truncated fixed point as CLOSED.
    """
    L = set(L)
    trace = []
    for it in range(rounds):
        pending = {}
        for d in (1, 2):
            D, groups = defaultdict(set), defaultdict(set)
            for w in sorted(L):
                for x, E in occurrences(w, d):
                    D[x].add(E)
                    groups[E, typ(x, marked)].add(x)
            for (E, _), xs in sorted(groups.items()):
                xs = sorted(xs)
                x = xs[0]
                for y in xs[1:]:
                    for u, v in ((x, y), (y, x)):
                        for F in sorted(D[u] - D[v]):
                            z = fill(F, v)
                            if z not in L and z not in pending:
                                pending[z] = dict(round=it+1, x=u, y=v, E=E, F=F,
                                                  premises=[fill(E,u),fill(E,v),fill(F,u)],
                                                  added=z)
        if not pending:
            assert check(L, marked=marked) is None
            return L, 'CLOSED', trace
        ordered = sorted(pending, key=lambda w:(len(w),w))
        hit = False
        for z in ordered:
            if len(z) > max_length or len(L) >= max_words:
                hit = True
                continue
            item = pending[z]
            assert all(w in L for w in item['premises'])
            assert typ(item['x'],marked) == typ(item['y'],marked)
            L.add(z)
            trace.append(item)
        if hit:
            return L, 'TRUNCATED: length/word limit', trace
    return L, 'TRUNCATED: round limit', trace

def parikh_saturated(L):
    counts = defaultdict(int)
    for w in L:
        counts[tuple(w.count(a) for a in 'abc')] += 1
    import math
    for v, k in counts.items():
        m = math.factorial(sum(v))
        for q in v:
            m //= math.factorial(q)
        if m != k:
            return False
    return True

# CFG representation: integer nonterminals, string terminal blocks.
# All examples are acyclic, reduced, fan-out one, rank <= 2.
def grammar_stats(rules, start, substitutable):
    V = sorted({a for a,_ in rules})
    byhead = {a: [] for a in V}
    for a,rhs in rules:
        byhead[a].append(rhs)
    @lru_cache(None)
    def words(a):
        ans = set()
        for rhs in byhead[a]:
            factors = [words(z) if isinstance(z,int) else (z,) for z in rhs]
            ans.update(''.join(z) for z in product(*factors))
        return frozenset(ans)
    L = words(start)
    shortest = {a:min(words(a),key=lambda w:(len(w),w)) for a in V}
    outside = {start: ('','')}
    changed = True
    while changed:
        changed = False
        for a,rhs in rules:
            if a not in outside:
                continue
            p,q = outside[a]
            for i,b in enumerate(rhs):
                if not isinstance(b,int):
                    continue
                left = ''.join(shortest[z] if isinstance(z,int) else z for z in rhs[:i])
                right = ''.join(shortest[z] if isinstance(z,int) else z for z in rhs[i+1:])
                E = (p+left,right+q)
                key = lambda e:(sum(map(len,e)),e)
                if b not in outside or key(E) < key(outside[b]):
                    outside[b] = E
                    changed = True
    assert set(outside) == set(V)
    rule_minima = []
    size = len(V)
    for a,rhs in rules:
        rank = sum(isinstance(z,int) for z in rhs)
        assert rank <= 2
        term = sum(len(z) for z in rhs if isinstance(z,str))
        size += 1 + 2*rank + term
        rule_minima.append(sum(map(len,outside[a])) + term +
                           sum(len(shortest[z]) for z in rhs if isinstance(z,int)))
    mu = max(min(len(w) for w in L if typ((w,)) == (t,))
             for t in {typ((w,))[0] for w in L})
    tau = None
    if substitutable:
        vals = []
        for a in V:
            p,q = outside[a]
            for t in {typ((w,))[0] for w in words(a)}:
                eligible = []
                for w in L:
                    if len(w) <= len(p)+len(q) or not w.startswith(p) or not w.endswith(q):
                        continue
                    u = w[len(p):len(w)-len(q) if q else len(w)]
                    if typ((u,)) == (t,):
                        eligible.append(len(u))
                assert eligible
                vals.append(min(eligible))
        tau = max(vals)
    return L, dict(size=size, theta=max(rule_minima), mu_star=mu, tau=tau,
                   rule_minima=rule_minima, words=len(L), maxlen=max(map(len,L)))

def periodic_grammar(n):
    # P_i=2*i; C_i=2*i+1; S=2*n+2
    rules = [(0,('ab',)), (1,('c',))]
    for i in range(1,n+1):
        rules += [(2*i,(2*i-2,2*i-2)),
                  (2*i+1,(2*i-1,2*i-2)), (2*i+1,(2*i-2,2*i-1))]
    S = 2*n+2
    rules += [(S,(2*n,)), (S,(2*n+1,))]
    return rules,S

def shortcut_grammar(n):
    rules = [(0,('ab',))]
    for i in range(1,n+1):
        rules += [(i,(i-1,i-1)),(i,('c',))]
    return rules,n

def K(n):
    L={'a'}
    for _ in range(n):
        L = {'b'+x+y+'b' for x in L for y in L} | {'c'+x+'c' for x in L}
    return L

def out(tag, data):
    print(tag, json.dumps(data,sort_keys=True,ensure_ascii=False),flush=True)

def main():
    out('ENV',dict(python=sys.version.split()[0],alphabet='abc',f=2,rank_cap=2))
    L=K(2)
    assert check(L,(1,)) is None
    cert=check(L,(2,)); assert cert;validate_certificate(L,cert)
    out('K2',dict(language=sorted(L),d1=True,d2=False,certificate=cert))
    x,y,E=('bcac','cb'),('c','cc'),('','ca','')
    Dx,Dy=distribution(L,x),distribution(L,y)
    assert E in Dx&Dy and Dx!=Dy
    F=min(Dx^Dy)
    out('K2_USER_WITNESS',dict(x=x,y=y,E=E,F=F,Fx=fill(F,x),Fy=fill(F,y)))
    fs8={'a'*8}|{'a'*i+'bc'+'a'*(6-i) for i in range(7)}
    assert check(fs8,marked='bc') is None
    out('FS8',dict(language=sorted(fs8),marked='bc',d1_d2=True))
    C={'aaa','abaa'}
    assert check(C,marked='b') is None
    out('FS_C_COUNTEREXAMPLE',dict(language=sorted(C),marked='b',d1_d2=True))
    out('SINGLETON_LENGTH7_BEGIN',{})
    passes=[];fails=[]
    for p in product('ab',repeat=7):
        w=''.join(p);cert=check({w})
        predicted=len(set(w[1:-1]))==1 or all(w[i]!=w[i+1] for i in range(6))
        assert (cert is None)==predicted
        if cert is None:passes.append(w)
        else:
            validate_certificate({w},cert)
            fails.append((w,cert))
            out('SINGLETON_FAIL',dict(w=w,certificate=cert))
    out('SINGLETON_LENGTH7_END',dict(passed=passes,failed=len(fails)))
    for N in range(1,5):
        for m in range(1,5):
            L={'ab'*N}|{'ab'*i+'c'+'ab'*(m-i) for i in range(m+1)}
            assert check(L) is None
            out('PERIODIC_GRID',dict(N=N,m=m,words=len(L),d1_d2=True,
                                     parikh_saturated=parikh_saturated(L)))
    weighted_cases=0
    for K0 in range(1,5):
        for M in range(1,4):
            for N in range(M,M+4):
                L={'ab'*K0}
                for q in range(1,N//M+1):
                    p=N-M*q
                    for pos in combinations(range(p+q),q):
                        pos=set(pos)
                        L.add(''.join('c' if i in pos else 'ab' for i in range(p+q)))
                assert check(L) is None
                weighted_cases+=1
    out('WEIGHTED_PHASE_FAMILY',dict(cases=weighted_cases,K='1..4',M='1..3',N='M..M+3',all_pass=True))
    for n in range(1,5):
        r,S=periodic_grammar(n)
        L,stats=grammar_stats(r,S,True)
        assert check(L) is None
        assert stats['size']==17*n+14 and stats['theta']==2**(n+1)
        assert stats['tau']==stats['mu_star']==2**(n+1)
        out('PERIODIC_GRAMMAR',dict(n=n,**stats,d1_d2=True))
    for n in range(1,5):
        r,S=shortcut_grammar(n)
        L,stats=grammar_stats(r,S,False)
        cert=check(L)
        if cert:validate_certificate(L,cert)
        else:L,stats=grammar_stats(r,S,True)
        assert stats['size']==8*n+4 and stats['theta']==n+3
        assert stats['mu_star']==2**(n+1)
        out('SHORTCUT_GRAMMAR',dict(n=n,**stats,d1_d2=cert is None,certificate=cert))
    # Exhaustive pairs: pure words length 3..5, exactly-one-c words length 3..5.
    pure=[''.join(z) for n in range(3,6) for z in product('ab',repeat=n)]
    marked=[''.join(z) for n in range(3,6) for z in product('abc',repeat=n) if z.count('c')==1]
    counts=[0,0]; maxratio=(-1,None); histogram=defaultdict(int)
    for u in pure:
        for v in marked:
            cert=check({u,v})
            counts[cert is None]+=1
            if cert is None:
                histogram[len(u),len(v)]+=1
                ratio=max(len(u),len(v))/min(len(u),len(v))
                if ratio>maxratio[0]:maxratio=(ratio,(u,v))
    out('EXHAUSTIVE_PAIRS',dict(pure_count=len(pure),marked_count=len(marked),
        total=len(pure)*len(marked),fail=counts[0],pass_count=counts[1],
        max_length_ratio=maxratio,histogram={str(k):v for k,v in sorted(histogram.items())}))
    # Every subset of size <=3 of all words of length 1 or 2 over abc.
    pool=[''.join(z) for n in (1,2) for z in product('abc',repeat=n)]
    hist={}
    for k in (1,2,3):
        good=bad=noncomm=0
        for S in combinations(pool,k):
            L=set(S)
            if check(L) is None:
                good+=1
                noncomm+=not parikh_saturated(L)
            else:bad+=1
        hist[k]=dict(passed=good,failed=bad,passed_nonparikh=noncomm)
    out('EXHAUSTIVE_SMALL_SUBSETS',dict(pool=pool,by_size=hist))
    r,S=shortcut_grammar(2)
    L,_=grammar_stats(r,S,False)
    closed,status,trace=closure(L,max_length=10,max_words=80,rounds=6)
    for item in trace:out('FORCED',item)
    out('CLOSURE_RESULT',dict(seed=sorted(L),status=status,words=len(closed),steps=len(trace),
        shortest_pure=min((w for w in closed if 'c' not in w),key=lambda w:(len(w),w)),
        pure_lengths=sorted({len(w) for w in closed if 'c' not in w}),
        parikh_saturated=parikh_saturated(closed)))
    out('ALL_ASSERTIONS_PASSED',True)

if __name__=='__main__':main()
```

### 12.2 実行ログ全文

```text
ENV {"alphabet": "abc", "f": 2, "python": "3.12.14", "rank_cap": 2}
K2 {"certificate": {"E": ["", "a", "c"], "Ex": "cbaabc", "Ey": "cbaabc", "F": ["bca", "ab", ""], "Fx": "bcacbaabb", "Fy": "bcacbabab", "d": 2, "x": ["cba", "b"], "y": ["cb", "ab"]}, "d1": true, "d2": false, "language": ["bbaabbaabb", "bbaabcacb", "bcacbaabb", "bcaccacb", "cbaabc", "ccacc"]}
K2_USER_WITNESS {"E": ["", "ca", ""], "F": ["b", "a", "acb"], "Fx": "bbcacacbacb", "Fy": "bcaccacb", "x": ["bcac", "cb"], "y": ["c", "cc"]}
FS8 {"d1_d2": true, "language": ["aaaaaaaa", "aaaaaabc", "aaaaabca", "aaaabcaa", "aaabcaaa", "aabcaaaa", "abcaaaaa", "bcaaaaaa"], "marked": "bc"}
FS_C_COUNTEREXAMPLE {"d1_d2": true, "language": ["aaa", "abaa"], "marked": "b"}
SINGLETON_LENGTH7_BEGIN {}
SINGLETON_FAIL {"certificate": {"E": ["", "a", "aba"], "Ex": "aaaaaba", "Ey": "aaaaaba", "F": ["", "aaab", ""], "Fx": "aaaaaba", "Fy": "aaaabaa", "d": 2, "x": ["aa", "a"], "y": ["a", "aa"]}, "w": "aaaaaba"}
SINGLETON_FAIL {"certificate": {"E": ["", "aaa", "b"], "Ex": "aaaaabb", "Ey": "aaaaabb", "F": ["", "aaab", ""], "Fx": "aaaaabb", "Fy": "aaaabab", "d": 2, "x": ["aa", "b"], "y": ["a", "ab"]}, "w": "aaaaabb"}
SINGLETON_FAIL {"certificate": {"E": ["", "a", "baa"], "Ex": "aaaabaa", "Ey": "aaaabaa", "F": ["", "aaab", ""], "Fx": "aaaaaba", "Fy": "aaaabaa", "d": 2, "x": ["aa", "a"], "y": ["a", "aa"]}, "w": "aaaabaa"}
SINGLETON_FAIL {"certificate": {"E": ["", "a", "bab"], "Ex": "aaaabab", "Ey": "aaaabab", "F": ["", "aab", "b"], "Fx": "aaaabab", "Fy": "aaabaab", "d": 2, "x": ["aa", "a"], "y": ["a", "aa"]}, "w": "aaaabab"}
SINGLETON_FAIL {"certificate": {"E": ["", "a", "bba"], "Ex": "aaaabba", "Ey": "aaaabba", "F": ["", "aabb", ""], "Fx": "aaaabba", "Fy": "aaabbaa", "d": 2, "x": ["aa", "a"], "y": ["a", "aa"]}, "w": "aaaabba"}
SINGLETON_FAIL {"certificate": {"E": ["", "aa", "bb"], "Ex": "aaaabbb", "Ey": "aaaabbb", "F": ["", "aab", "b"], "Fx": "aaaabbb", "Fy": "aaababb", "d": 2, "x": ["aa", "b"], "y": ["a", "ab"]}, "w": "aaaabbb"}
SINGLETON_FAIL {"certificate": {"E": ["", "a", "a"], "Ex": "aaabaaa", "Ey": "aaabaaa", "F": ["", "aa", ""], "Fx": "aaabaaa", "Fy": "aaaabaa", "d": 2, "x": ["aaab", "a"], "y": ["a", "abaa"]}, "w": "aaabaaa"}
SINGLETON_FAIL {"certificate": {"E": ["", "a", "aab"], "Ex": "aaabaab", "Ey": "aaabaab", "F": ["", "aaba", ""], "Fx": "aaaabab", "Fy": "aaabaab", "d": 2, "x": ["aa", "b"], "y": ["a", "ab"]}, "w": "aaabaab"}
SINGLETON_FAIL {"certificate": {"E": ["", "a", "aba"], "Ex": "aaababa", "Ey": "aaababa", "F": ["", "aab", "a"], "Fx": "aaaabba", "Fy": "aaababa", "d": 2, "x": ["aa", "b"], "y": ["a", "ab"]}, "w": "aaababa"}
SINGLETON_FAIL {"certificate": {"E": ["", "a", "abb"], "Ex": "aaababb", "Ey": "aaababb", "F": ["", "aab", "b"], "Fx": "aaaabbb", "Fy": "aaababb", "d": 2, "x": ["aa", "b"], "y": ["a", "ab"]}, "w": "aaababb"}
SINGLETON_FAIL {"certificate": {"E": ["", "a", "baa"], "Ex": "aaabbaa", "Ey": "aaabbaa", "F": ["", "ab", "aa"], "Fx": "aaabbaa", "Fy": "aababaa", "d": 2, "x": ["aa", "b"], "y": ["a", "ab"]}, "w": "aaabbaa"}
SINGLETON_FAIL {"certificate": {"E": ["", "a", "bab"], "Ex": "aaabbab", "Ey": "aaabbab", "F": ["", "aabb", ""], "Fx": "aaaabbb", "Fy": "aaabbab", "d": 2, "x": ["aa", "b"], "y": ["a", "ab"]}, "w": "aaabbab"}
SINGLETON_FAIL {"certificate": {"E": ["", "a", "bba"], "Ex": "aaabbba", "Ey": "aaabbba", "F": ["", "ab", "ba"], "Fx": "aaabbba", "Fy": "aababba", "d": 2, "x": ["aa", "b"], "y": ["a", "ab"]}, "w": "aaabbba"}
SINGLETON_FAIL {"certificate": {"E": ["", "a", "bbb"], "Ex": "aaabbbb", "Ey": "aaabbbb", "F": ["", "ab", "bb"], "Fx": "aaabbbb", "Fy": "aababbb", "d": 2, "x": ["aa", "b"], "y": ["a", "ab"]}, "w": "aaabbbb"}
SINGLETON_FAIL {"certificate": {"E": ["", "a", "aa"], "Ex": "aabaaaa", "Ey": "aabaaaa", "F": ["", "aa", "a"], "Fx": "aabaaaa", "Fy": "aaabaaa", "d": 2, "x": ["aab", "a"], "y": ["a", "baa"]}, "w": "aabaaaa"}
SINGLETON_FAIL {"certificate": {"E": ["", "a", "ab"], "Ex": "aabaaab", "Ey": "aabaaab", "F": ["", "aa", "b"], "Fx": "aabaaab", "Fy": "aaabaab", "d": 2, "x": ["aab", "a"], "y": ["a", "baa"]}, "w": "aabaaab"}
SINGLETON_FAIL {"certificate": {"E": ["", "a", "ba"], "Ex": "aabaaba", "Ey": "aabaaba", "F": ["", "aab", ""], "Fx": "aabaaba", "Fy": "aaabbaa", "d": 2, "x": ["aab", "a"], "y": ["a", "baa"]}, "w": "aabaaba"}
SINGLETON_FAIL {"certificate": {"E": ["", "a", "b"], "Ex": "aabaabb", "Ey": "aabaabb", "F": ["", "ab", ""], "Fx": "aabaabb", "Fy": "aabbaab", "d": 2, "x": ["aaba", "b"], "y": ["a", "baab"]}, "w": "aabaabb"}
SINGLETON_FAIL {"certificate": {"E": ["", "ab", "a"], "Ex": "aababaa", "Ey": "aababaa", "F": ["", "aba", ""], "Fx": "aababaa", "Fy": "aabaaba", "d": 2, "x": ["aab", "a"], "y": ["a", "aba"]}, "w": "aababaa"}
SINGLETON_FAIL {"certificate": {"E": ["", "a", "ab"], "Ex": "aababab", "Ey": "aababab", "F": ["a", "ba", ""], "Fx": "aaabbab", "Fy": "aababab", "d": 2, "x": ["aab", "b"], "y": ["a", "bab"]}, "w": "aababab"}
SINGLETON_FAIL {"certificate": {"E": ["", "a", "ba"], "Ex": "aababba", "Ey": "aababba", "F": ["", "ab", "a"], "Fx": "aababba", "Fy": "aabbaba", "d": 2, "x": ["aab", "b"], "y": ["a", "bab"]}, "w": "aababba"}
SINGLETON_FAIL {"certificate": {"E": ["", "a", "bb"], "Ex": "aababbb", "Ey": "aababbb", "F": ["", "ab", "b"], "Fx": "aababbb", "Fy": "aabbabb", "d": 2, "x": ["aab", "b"], "y": ["a", "bab"]}, "w": "aababbb"}
SINGLETON_FAIL {"certificate": {"E": ["", "b", "aa"], "Ex": "aabbaaa", "Ey": "aabbaaa", "F": ["", "ba", "a"], "Fx": "aabbaaa", "Fy": "aababaa", "d": 2, "x": ["aab", "a"], "y": ["aa", "ba"]}, "w": "aabbaaa"}
SINGLETON_FAIL {"certificate": {"E": ["", "b", "ab"], "Ex": "aabbaab", "Ey": "aabbaab", "F": ["", "ba", "b"], "Fx": "aabbaab", "Fy": "aababab", "d": 2, "x": ["aab", "a"], "y": ["aa", "ba"]}, "w": "aabbaab"}
SINGLETON_FAIL {"certificate": {"E": ["", "b", "ba"], "Ex": "aabbaba", "Ey": "aabbaba", "F": ["", "bab", ""], "Fx": "aabbaba", "Fy": "aababba", "d": 2, "x": ["aab", "a"], "y": ["aa", "ba"]}, "w": "aabbaba"}
SINGLETON_FAIL {"certificate": {"E": ["", "a", "b"], "Ex": "aabbabb", "Ey": "aabbabb", "F": ["", "ab", ""], "Fx": "aabbabb", "Fy": "aabbbab", "d": 2, "x": ["aabb", "b"], "y": ["a", "bbab"]}, "w": "aabbabb"}
SINGLETON_FAIL {"certificate": {"E": ["", "bb", "a"], "Ex": "aabbbaa", "Ey": "aabbbaa", "F": ["", "bba", ""], "Fx": "aabbbaa", "Fy": "aabbaba", "d": 2, "x": ["aab", "a"], "y": ["aa", "ba"]}, "w": "aabbbaa"}
SINGLETON_FAIL {"certificate": {"E": ["", "b", "ab"], "Ex": "aabbbab", "Ey": "aabbbab", "F": ["", "bba", ""], "Fx": "aabbbab", "Fy": "aabbabb", "d": 2, "x": ["aab", "b"], "y": ["aa", "bb"]}, "w": "aabbbab"}
SINGLETON_FAIL {"certificate": {"E": ["a", "b", "ba"], "Ex": "aabbbba", "Ey": "aabbbba", "F": ["", "a", "bba"], "Fx": "ababbba", "Fy": "aabbbba", "d": 2, "x": ["ab", "b"], "y": ["a", "bb"]}, "w": "aabbbba"}
SINGLETON_FAIL {"certificate": {"E": ["a", "b", "bb"], "Ex": "aabbbbb", "Ey": "aabbbbb", "F": ["", "a", "bbb"], "Fx": "ababbbb", "Fy": "aabbbbb", "d": 2, "x": ["ab", "b"], "y": ["a", "bb"]}, "w": "aabbbbb"}
SINGLETON_FAIL {"certificate": {"E": ["ab", "a", "a"], "Ex": "abaaaaa", "Ey": "abaaaaa", "F": ["", "b", "aaa"], "Fx": "aabaaaa", "Fy": "abaaaaa", "d": 2, "x": ["aa", "a"], "y": ["a", "aa"]}, "w": "abaaaaa"}
SINGLETON_FAIL {"certificate": {"E": ["ab", "a", "b"], "Ex": "abaaaab", "Ey": "abaaaab", "F": ["", "b", "aab"], "Fx": "aabaaab", "Fy": "abaaaab", "d": 2, "x": ["aa", "a"], "y": ["a", "aa"]}, "w": "abaaaab"}
SINGLETON_FAIL {"certificate": {"E": ["", "a", "ba"], "Ex": "abaaaba", "Ey": "abaaaba", "F": ["", "aab", ""], "Fx": "abaaaba", "Fy": "abaabaa", "d": 2, "x": ["aba", "a"], "y": ["ab", "aa"]}, "w": "abaaaba"}
SINGLETON_FAIL {"certificate": {"E": ["", "aa", "b"], "Ex": "abaaabb", "Ey": "abaaabb", "F": ["", "aab", ""], "Fx": "abaaabb", "Fy": "abaabab", "d": 2, "x": ["aba", "b"], "y": ["ab", "ab"]}, "w": "abaaabb"}
SINGLETON_FAIL {"certificate": {"E": ["", "b", "a"], "Ex": "abaabaa", "Ey": "abaabaa", "F": ["", "ba", ""], "Fx": "abaabaa", "Fy": "abaaaba", "d": 2, "x": ["abaa", "a"], "y": ["a", "aaba"]}, "w": "abaabaa"}
SINGLETON_FAIL {"certificate": {"E": ["", "a", "ab"], "Ex": "abaabab", "Ey": "abaabab", "F": ["", "aab", ""], "Fx": "abaaabb", "Fy": "abaabab", "d": 2, "x": ["aba", "b"], "y": ["ab", "ab"]}, "w": "abaabab"}
SINGLETON_FAIL {"certificate": {"E": ["", "a", "ba"], "Ex": "abaabba", "Ey": "abaabba", "F": ["", "ab", "a"], "Fx": "abaabba", "Fy": "abababa", "d": 2, "x": ["aba", "b"], "y": ["ab", "ab"]}, "w": "abaabba"}
SINGLETON_FAIL {"certificate": {"E": ["", "a", "bb"], "Ex": "abaabbb", "Ey": "abaabbb", "F": ["", "ab", "b"], "Fx": "abaabbb", "Fy": "abababb", "d": 2, "x": ["aba", "b"], "y": ["ab", "ab"]}, "w": "abaabbb"}
SINGLETON_FAIL {"certificate": {"E": ["", "b", "aa"], "Ex": "ababaaa", "Ey": "ababaaa", "F": ["", "ba", "a"], "Fx": "ababaaa", "Fy": "abaabaa", "d": 2, "x": ["aba", "a"], "y": ["a", "aba"]}, "w": "ababaaa"}
SINGLETON_FAIL {"certificate": {"E": ["", "b", "ab"], "Ex": "ababaab", "Ey": "ababaab", "F": ["", "ba", "b"], "Fx": "ababaab", "Fy": "abaabab", "d": 2, "x": ["aba", "a"], "y": ["a", "aba"]}, "w": "ababaab"}
SINGLETON_FAIL {"certificate": {"E": ["", "ba", "b"], "Ex": "abababb", "Ey": "abababb", "F": ["", "bab", ""], "Fx": "abababb", "Fy": "ababbab", "d": 2, "x": ["aba", "b"], "y": ["a", "bab"]}, "w": "abababb"}
SINGLETON_FAIL {"certificate": {"E": ["", "b", "a"], "Ex": "ababbaa", "Ey": "ababbaa", "F": ["", "ba", ""], "Fx": "ababbaa", "Fy": "abaabba", "d": 2, "x": ["abab", "a"], "y": ["a", "abba"]}, "w": "ababbaa"}
SINGLETON_FAIL {"certificate": {"E": ["", "b", "ab"], "Ex": "ababbab", "Ey": "ababbab", "F": ["", "bba", ""], "Fx": "ababbab", "Fy": "abbaabb", "d": 2, "x": ["aba", "b"], "y": ["a", "abb"]}, "w": "ababbab"}
SINGLETON_FAIL {"certificate": {"E": ["", "b", "ba"], "Ex": "ababbba", "Ey": "ababbba", "F": ["", "bb", "a"], "Fx": "ababbba", "Fy": "abbabba", "d": 2, "x": ["aba", "b"], "y": ["a", "abb"]}, "w": "ababbba"}
SINGLETON_FAIL {"certificate": {"E": ["", "b", "bb"], "Ex": "ababbbb", "Ey": "ababbbb", "F": ["", "bb", "b"], "Fx": "ababbbb", "Fy": "abbabbb", "d": 2, "x": ["aba", "b"], "y": ["a", "abb"]}, "w": "ababbbb"}
SINGLETON_FAIL {"certificate": {"E": ["", "b", "aaa"], "Ex": "abbaaaa", "Ey": "abbaaaa", "F": ["", "ba", "aa"], "Fx": "abbaaaa", "Fy": "ababaaa", "d": 2, "x": ["ab", "a"], "y": ["a", "ba"]}, "w": "abbaaaa"}
SINGLETON_FAIL {"certificate": {"E": ["", "b", "aab"], "Ex": "abbaaab", "Ey": "abbaaab", "F": ["", "ba", "ab"], "Fx": "abbaaab", "Fy": "ababaab", "d": 2, "x": ["ab", "a"], "y": ["a", "ba"]}, "w": "abbaaab"}
SINGLETON_FAIL {"certificate": {"E": ["", "b", "aba"], "Ex": "abbaaba", "Ey": "abbaaba", "F": ["", "ba", "ba"], "Fx": "abbaaba", "Fy": "abababa", "d": 2, "x": ["ab", "a"], "y": ["a", "ba"]}, "w": "abbaaba"}
SINGLETON_FAIL {"certificate": {"E": ["", "b", "abb"], "Ex": "abbaabb", "Ey": "abbaabb", "F": ["", "ba", "bb"], "Fx": "abbaabb", "Fy": "abababb", "d": 2, "x": ["ab", "a"], "y": ["a", "ba"]}, "w": "abbaabb"}
SINGLETON_FAIL {"certificate": {"E": ["", "b", "baa"], "Ex": "abbabaa", "Ey": "abbabaa", "F": ["", "bab", "a"], "Fx": "abbabaa", "Fy": "ababbaa", "d": 2, "x": ["ab", "a"], "y": ["a", "ba"]}, "w": "abbabaa"}
SINGLETON_FAIL {"certificate": {"E": ["", "b", "bab"], "Ex": "abbabab", "Ey": "abbabab", "F": ["", "bab", "b"], "Fx": "abbabab", "Fy": "ababbab", "d": 2, "x": ["ab", "a"], "y": ["a", "ba"]}, "w": "abbabab"}
SINGLETON_FAIL {"certificate": {"E": ["", "b", "bba"], "Ex": "abbabba", "Ey": "abbabba", "F": ["", "babb", ""], "Fx": "abbabba", "Fy": "ababbba", "d": 2, "x": ["ab", "a"], "y": ["a", "ba"]}, "w": "abbabba"}
SINGLETON_FAIL {"certificate": {"E": ["", "b", "b"], "Ex": "abbabbb", "Ey": "abbabbb", "F": ["", "bb", ""], "Fx": "abbabbb", "Fy": "abbbabb", "d": 2, "x": ["abba", "b"], "y": ["a", "babb"]}, "w": "abbabbb"}
SINGLETON_FAIL {"certificate": {"E": ["", "bb", "aa"], "Ex": "abbbaaa", "Ey": "abbbaaa", "F": ["", "bba", "a"], "Fx": "abbbaaa", "Fy": "abbabaa", "d": 2, "x": ["ab", "a"], "y": ["a", "ba"]}, "w": "abbbaaa"}
SINGLETON_FAIL {"certificate": {"E": ["", "b", "aab"], "Ex": "abbbaab", "Ey": "abbbaab", "F": ["", "bbaa", ""], "Fx": "abbbaab", "Fy": "abbaabb", "d": 2, "x": ["ab", "b"], "y": ["a", "bb"]}, "w": "abbbaab"}
SINGLETON_FAIL {"certificate": {"E": ["", "b", "aba"], "Ex": "abbbaba", "Ey": "abbbaba", "F": ["", "bba", "a"], "Fx": "abbbaba", "Fy": "abbabba", "d": 2, "x": ["ab", "b"], "y": ["a", "bb"]}, "w": "abbbaba"}
SINGLETON_FAIL {"certificate": {"E": ["", "b", "abb"], "Ex": "abbbabb", "Ey": "abbbabb", "F": ["", "bba", "b"], "Fx": "abbbabb", "Fy": "abbabbb", "d": 2, "x": ["ab", "b"], "y": ["a", "bb"]}, "w": "abbbabb"}
SINGLETON_FAIL {"certificate": {"E": ["", "bbb", "a"], "Ex": "abbbbaa", "Ey": "abbbbaa", "F": ["", "bbba", ""], "Fx": "abbbbaa", "Fy": "abbbaba", "d": 2, "x": ["ab", "a"], "y": ["a", "ba"]}, "w": "abbbbaa"}
SINGLETON_FAIL {"certificate": {"E": ["", "b", "bab"], "Ex": "abbbbab", "Ey": "abbbbab", "F": ["", "bbba", ""], "Fx": "abbbbab", "Fy": "abbbabb", "d": 2, "x": ["ab", "b"], "y": ["a", "bb"]}, "w": "abbbbab"}
SINGLETON_FAIL {"certificate": {"E": ["", "a", "aba"], "Ex": "baaaaba", "Ey": "baaaaba", "F": ["", "aaab", ""], "Fx": "baaaaba", "Fy": "baaabaa", "d": 2, "x": ["ba", "a"], "y": ["b", "aa"]}, "w": "baaaaba"}
SINGLETON_FAIL {"certificate": {"E": ["", "aaa", "b"], "Ex": "baaaabb", "Ey": "baaaabb", "F": ["", "aaab", ""], "Fx": "baaaabb", "Fy": "baaabab", "d": 2, "x": ["ba", "b"], "y": ["b", "ab"]}, "w": "baaaabb"}
SINGLETON_FAIL {"certificate": {"E": ["", "a", "baa"], "Ex": "baaabaa", "Ey": "baaabaa", "F": ["", "aaab", ""], "Fx": "baaaaba", "Fy": "baaabaa", "d": 2, "x": ["ba", "a"], "y": ["b", "aa"]}, "w": "baaabaa"}
SINGLETON_FAIL {"certificate": {"E": ["", "a", "bab"], "Ex": "baaabab", "Ey": "baaabab", "F": ["", "aab", "b"], "Fx": "baaabab", "Fy": "baabaab", "d": 2, "x": ["ba", "a"], "y": ["b", "aa"]}, "w": "baaabab"}
SINGLETON_FAIL {"certificate": {"E": ["", "a", "bba"], "Ex": "baaabba", "Ey": "baaabba", "F": ["", "aabb", ""], "Fx": "baaabba", "Fy": "baabbaa", "d": 2, "x": ["ba", "a"], "y": ["b", "aa"]}, "w": "baaabba"}
SINGLETON_FAIL {"certificate": {"E": ["", "aa", "bb"], "Ex": "baaabbb", "Ey": "baaabbb", "F": ["", "aab", "b"], "Fx": "baaabbb", "Fy": "baababb", "d": 2, "x": ["ba", "b"], "y": ["b", "ab"]}, "w": "baaabbb"}
SINGLETON_FAIL {"certificate": {"E": ["", "a", "a"], "Ex": "baabaaa", "Ey": "baabaaa", "F": ["", "aa", ""], "Fx": "baabaaa", "Fy": "baaabaa", "d": 2, "x": ["baab", "a"], "y": ["b", "abaa"]}, "w": "baabaaa"}
SINGLETON_FAIL {"certificate": {"E": ["", "a", "aab"], "Ex": "baabaab", "Ey": "baabaab", "F": ["", "aaba", ""], "Fx": "baaabab", "Fy": "baabaab", "d": 2, "x": ["ba", "b"], "y": ["b", "ab"]}, "w": "baabaab"}
SINGLETON_FAIL {"certificate": {"E": ["", "a", "aba"], "Ex": "baababa", "Ey": "baababa", "F": ["", "aab", "a"], "Fx": "baaabba", "Fy": "baababa", "d": 2, "x": ["ba", "b"], "y": ["b", "ab"]}, "w": "baababa"}
SINGLETON_FAIL {"certificate": {"E": ["", "a", "abb"], "Ex": "baababb", "Ey": "baababb", "F": ["", "aab", "b"], "Fx": "baaabbb", "Fy": "baababb", "d": 2, "x": ["ba", "b"], "y": ["b", "ab"]}, "w": "baababb"}
SINGLETON_FAIL {"certificate": {"E": ["", "a", "baa"], "Ex": "baabbaa", "Ey": "baabbaa", "F": ["", "ab", "aa"], "Fx": "baabbaa", "Fy": "bababaa", "d": 2, "x": ["ba", "b"], "y": ["b", "ab"]}, "w": "baabbaa"}
SINGLETON_FAIL {"certificate": {"E": ["", "a", "bab"], "Ex": "baabbab", "Ey": "baabbab", "F": ["", "aabb", ""], "Fx": "baaabbb", "Fy": "baabbab", "d": 2, "x": ["ba", "b"], "y": ["b", "ab"]}, "w": "baabbab"}
SINGLETON_FAIL {"certificate": {"E": ["", "a", "bba"], "Ex": "baabbba", "Ey": "baabbba", "F": ["", "ab", "ba"], "Fx": "baabbba", "Fy": "bababba", "d": 2, "x": ["ba", "b"], "y": ["b", "ab"]}, "w": "baabbba"}
SINGLETON_FAIL {"certificate": {"E": ["", "a", "bbb"], "Ex": "baabbbb", "Ey": "baabbbb", "F": ["", "ab", "bb"], "Fx": "baabbbb", "Fy": "bababbb", "d": 2, "x": ["ba", "b"], "y": ["b", "ab"]}, "w": "baabbbb"}
SINGLETON_FAIL {"certificate": {"E": ["", "a", "aa"], "Ex": "babaaaa", "Ey": "babaaaa", "F": ["", "aa", "a"], "Fx": "babaaaa", "Fy": "baabaaa", "d": 2, "x": ["bab", "a"], "y": ["b", "baa"]}, "w": "babaaaa"}
SINGLETON_FAIL {"certificate": {"E": ["", "a", "ab"], "Ex": "babaaab", "Ey": "babaaab", "F": ["", "aa", "b"], "Fx": "babaaab", "Fy": "baabaab", "d": 2, "x": ["bab", "a"], "y": ["b", "baa"]}, "w": "babaaab"}
SINGLETON_FAIL {"certificate": {"E": ["", "a", "ba"], "Ex": "babaaba", "Ey": "babaaba", "F": ["", "aab", ""], "Fx": "babaaba", "Fy": "baabbaa", "d": 2, "x": ["bab", "a"], "y": ["b", "baa"]}, "w": "babaaba"}
SINGLETON_FAIL {"certificate": {"E": ["", "a", "b"], "Ex": "babaabb", "Ey": "babaabb", "F": ["", "ab", ""], "Fx": "babaabb", "Fy": "babbaab", "d": 2, "x": ["baba", "b"], "y": ["b", "baab"]}, "w": "babaabb"}
SINGLETON_FAIL {"certificate": {"E": ["", "ab", "a"], "Ex": "bababaa", "Ey": "bababaa", "F": ["", "aba", ""], "Fx": "bababaa", "Fy": "babaaba", "d": 2, "x": ["bab", "a"], "y": ["b", "aba"]}, "w": "bababaa"}
SINGLETON_FAIL {"certificate": {"E": ["", "a", "ba"], "Ex": "bababba", "Ey": "bababba", "F": ["", "ab", "a"], "Fx": "bababba", "Fy": "babbaba", "d": 2, "x": ["bab", "b"], "y": ["b", "bab"]}, "w": "bababba"}
SINGLETON_FAIL {"certificate": {"E": ["", "a", "bb"], "Ex": "bababbb", "Ey": "bababbb", "F": ["", "ab", "b"], "Fx": "bababbb", "Fy": "babbabb", "d": 2, "x": ["bab", "b"], "y": ["b", "bab"]}, "w": "bababbb"}
SINGLETON_FAIL {"certificate": {"E": ["", "b", "aa"], "Ex": "babbaaa", "Ey": "babbaaa", "F": ["", "ba", "a"], "Fx": "babbaaa", "Fy": "bababaa", "d": 2, "x": ["bab", "a"], "y": ["ba", "ba"]}, "w": "babbaaa"}
SINGLETON_FAIL {"certificate": {"E": ["", "b", "ab"], "Ex": "babbaab", "Ey": "babbaab", "F": ["", "ba", "b"], "Fx": "babbaab", "Fy": "bababab", "d": 2, "x": ["bab", "a"], "y": ["ba", "ba"]}, "w": "babbaab"}
SINGLETON_FAIL {"certificate": {"E": ["", "b", "ba"], "Ex": "babbaba", "Ey": "babbaba", "F": ["", "bab", ""], "Fx": "babbaba", "Fy": "bababba", "d": 2, "x": ["bab", "a"], "y": ["ba", "ba"]}, "w": "babbaba"}
SINGLETON_FAIL {"certificate": {"E": ["", "a", "b"], "Ex": "babbabb", "Ey": "babbabb", "F": ["", "ab", ""], "Fx": "babbabb", "Fy": "babbbab", "d": 2, "x": ["babb", "b"], "y": ["b", "bbab"]}, "w": "babbabb"}
SINGLETON_FAIL {"certificate": {"E": ["", "bb", "a"], "Ex": "babbbaa", "Ey": "babbbaa", "F": ["", "bba", ""], "Fx": "babbbaa", "Fy": "babbaba", "d": 2, "x": ["bab", "a"], "y": ["ba", "ba"]}, "w": "babbbaa"}
SINGLETON_FAIL {"certificate": {"E": ["", "b", "ab"], "Ex": "babbbab", "Ey": "babbbab", "F": ["", "bba", ""], "Fx": "babbbab", "Fy": "babbabb", "d": 2, "x": ["bab", "b"], "y": ["ba", "bb"]}, "w": "babbbab"}
SINGLETON_FAIL {"certificate": {"E": ["ba", "b", "a"], "Ex": "babbbba", "Ey": "babbbba", "F": ["", "a", "bba"], "Fx": "bbabbba", "Fy": "babbbba", "d": 2, "x": ["bb", "b"], "y": ["b", "bb"]}, "w": "babbbba"}
SINGLETON_FAIL {"certificate": {"E": ["ba", "b", "b"], "Ex": "babbbbb", "Ey": "babbbbb", "F": ["", "a", "bbb"], "Fx": "bbabbbb", "Fy": "babbbbb", "d": 2, "x": ["bb", "b"], "y": ["b", "bb"]}, "w": "babbbbb"}
SINGLETON_FAIL {"certificate": {"E": ["b", "a", "aa"], "Ex": "bbaaaaa", "Ey": "bbaaaaa", "F": ["", "b", "aaa"], "Fx": "babaaaa", "Fy": "bbaaaaa", "d": 2, "x": ["ba", "a"], "y": ["b", "aa"]}, "w": "bbaaaaa"}
SINGLETON_FAIL {"certificate": {"E": ["b", "a", "ab"], "Ex": "bbaaaab", "Ey": "bbaaaab", "F": ["", "b", "aab"], "Fx": "babaaab", "Fy": "bbaaaab", "d": 2, "x": ["ba", "a"], "y": ["b", "aa"]}, "w": "bbaaaab"}
SINGLETON_FAIL {"certificate": {"E": ["", "a", "ba"], "Ex": "bbaaaba", "Ey": "bbaaaba", "F": ["", "aab", ""], "Fx": "bbaaaba", "Fy": "bbaabaa", "d": 2, "x": ["bba", "a"], "y": ["bb", "aa"]}, "w": "bbaaaba"}
SINGLETON_FAIL {"certificate": {"E": ["", "aa", "b"], "Ex": "bbaaabb", "Ey": "bbaaabb", "F": ["", "aab", ""], "Fx": "bbaaabb", "Fy": "bbaabab", "d": 2, "x": ["bba", "b"], "y": ["bb", "ab"]}, "w": "bbaaabb"}
SINGLETON_FAIL {"certificate": {"E": ["", "b", "a"], "Ex": "bbaabaa", "Ey": "bbaabaa", "F": ["", "ba", ""], "Fx": "bbaabaa", "Fy": "bbaaaba", "d": 2, "x": ["bbaa", "a"], "y": ["b", "aaba"]}, "w": "bbaabaa"}
SINGLETON_FAIL {"certificate": {"E": ["", "a", "ab"], "Ex": "bbaabab", "Ey": "bbaabab", "F": ["", "aab", ""], "Fx": "bbaaabb", "Fy": "bbaabab", "d": 2, "x": ["bba", "b"], "y": ["bb", "ab"]}, "w": "bbaabab"}
SINGLETON_FAIL {"certificate": {"E": ["", "a", "ba"], "Ex": "bbaabba", "Ey": "bbaabba", "F": ["", "ab", "a"], "Fx": "bbaabba", "Fy": "bbababa", "d": 2, "x": ["bba", "b"], "y": ["bb", "ab"]}, "w": "bbaabba"}
SINGLETON_FAIL {"certificate": {"E": ["", "a", "bb"], "Ex": "bbaabbb", "Ey": "bbaabbb", "F": ["", "ab", "b"], "Fx": "bbaabbb", "Fy": "bbababb", "d": 2, "x": ["bba", "b"], "y": ["bb", "ab"]}, "w": "bbaabbb"}
SINGLETON_FAIL {"certificate": {"E": ["", "b", "aa"], "Ex": "bbabaaa", "Ey": "bbabaaa", "F": ["", "ba", "a"], "Fx": "bbabaaa", "Fy": "bbaabaa", "d": 2, "x": ["bba", "a"], "y": ["b", "aba"]}, "w": "bbabaaa"}
SINGLETON_FAIL {"certificate": {"E": ["", "b", "ab"], "Ex": "bbabaab", "Ey": "bbabaab", "F": ["", "ba", "b"], "Fx": "bbabaab", "Fy": "bbaabab", "d": 2, "x": ["bba", "a"], "y": ["b", "aba"]}, "w": "bbabaab"}
SINGLETON_FAIL {"certificate": {"E": ["", "b", "ba"], "Ex": "bbababa", "Ey": "bbababa", "F": ["b", "ab", ""], "Fx": "bbbaaba", "Fy": "bbababa", "d": 2, "x": ["bba", "a"], "y": ["b", "aba"]}, "w": "bbababa"}
SINGLETON_FAIL {"certificate": {"E": ["", "ba", "b"], "Ex": "bbababb", "Ey": "bbababb", "F": ["", "bab", ""], "Fx": "bbababb", "Fy": "bbabbab", "d": 2, "x": ["bba", "b"], "y": ["b", "bab"]}, "w": "bbababb"}
SINGLETON_FAIL {"certificate": {"E": ["", "b", "a"], "Ex": "bbabbaa", "Ey": "bbabbaa", "F": ["", "ba", ""], "Fx": "bbabbaa", "Fy": "bbaabba", "d": 2, "x": ["bbab", "a"], "y": ["b", "abba"]}, "w": "bbabbaa"}
SINGLETON_FAIL {"certificate": {"E": ["", "b", "ab"], "Ex": "bbabbab", "Ey": "bbabbab", "F": ["", "bba", ""], "Fx": "bbabbab", "Fy": "bbbaabb", "d": 2, "x": ["bba", "b"], "y": ["b", "abb"]}, "w": "bbabbab"}
SINGLETON_FAIL {"certificate": {"E": ["", "b", "ba"], "Ex": "bbabbba", "Ey": "bbabbba", "F": ["", "bb", "a"], "Fx": "bbabbba", "Fy": "bbbabba", "d": 2, "x": ["bba", "b"], "y": ["b", "abb"]}, "w": "bbabbba"}
SINGLETON_FAIL {"certificate": {"E": ["", "b", "bb"], "Ex": "bbabbbb", "Ey": "bbabbbb", "F": ["", "bb", "b"], "Fx": "bbabbbb", "Fy": "bbbabbb", "d": 2, "x": ["bba", "b"], "y": ["b", "abb"]}, "w": "bbabbbb"}
SINGLETON_FAIL {"certificate": {"E": ["", "b", "aaa"], "Ex": "bbbaaaa", "Ey": "bbbaaaa", "F": ["", "ba", "aa"], "Fx": "bbbaaaa", "Fy": "bbabaaa", "d": 2, "x": ["bb", "a"], "y": ["b", "ba"]}, "w": "bbbaaaa"}
SINGLETON_FAIL {"certificate": {"E": ["", "b", "aab"], "Ex": "bbbaaab", "Ey": "bbbaaab", "F": ["", "ba", "ab"], "Fx": "bbbaaab", "Fy": "bbabaab", "d": 2, "x": ["bb", "a"], "y": ["b", "ba"]}, "w": "bbbaaab"}
SINGLETON_FAIL {"certificate": {"E": ["", "b", "aba"], "Ex": "bbbaaba", "Ey": "bbbaaba", "F": ["", "ba", "ba"], "Fx": "bbbaaba", "Fy": "bbababa", "d": 2, "x": ["bb", "a"], "y": ["b", "ba"]}, "w": "bbbaaba"}
SINGLETON_FAIL {"certificate": {"E": ["", "b", "abb"], "Ex": "bbbaabb", "Ey": "bbbaabb", "F": ["", "ba", "bb"], "Fx": "bbbaabb", "Fy": "bbababb", "d": 2, "x": ["bb", "a"], "y": ["b", "ba"]}, "w": "bbbaabb"}
SINGLETON_FAIL {"certificate": {"E": ["", "b", "baa"], "Ex": "bbbabaa", "Ey": "bbbabaa", "F": ["", "bab", "a"], "Fx": "bbbabaa", "Fy": "bbabbaa", "d": 2, "x": ["bb", "a"], "y": ["b", "ba"]}, "w": "bbbabaa"}
SINGLETON_FAIL {"certificate": {"E": ["", "b", "bab"], "Ex": "bbbabab", "Ey": "bbbabab", "F": ["", "bab", "b"], "Fx": "bbbabab", "Fy": "bbabbab", "d": 2, "x": ["bb", "a"], "y": ["b", "ba"]}, "w": "bbbabab"}
SINGLETON_FAIL {"certificate": {"E": ["", "b", "bba"], "Ex": "bbbabba", "Ey": "bbbabba", "F": ["", "babb", ""], "Fx": "bbbabba", "Fy": "bbabbba", "d": 2, "x": ["bb", "a"], "y": ["b", "ba"]}, "w": "bbbabba"}
SINGLETON_FAIL {"certificate": {"E": ["", "b", "b"], "Ex": "bbbabbb", "Ey": "bbbabbb", "F": ["", "bb", ""], "Fx": "bbbabbb", "Fy": "bbbbabb", "d": 2, "x": ["bbba", "b"], "y": ["b", "babb"]}, "w": "bbbabbb"}
SINGLETON_FAIL {"certificate": {"E": ["", "bb", "aa"], "Ex": "bbbbaaa", "Ey": "bbbbaaa", "F": ["", "bba", "a"], "Fx": "bbbbaaa", "Fy": "bbbabaa", "d": 2, "x": ["bb", "a"], "y": ["b", "ba"]}, "w": "bbbbaaa"}
SINGLETON_FAIL {"certificate": {"E": ["", "b", "aab"], "Ex": "bbbbaab", "Ey": "bbbbaab", "F": ["", "bbaa", ""], "Fx": "bbbbaab", "Fy": "bbbaabb", "d": 2, "x": ["bb", "b"], "y": ["b", "bb"]}, "w": "bbbbaab"}
SINGLETON_FAIL {"certificate": {"E": ["", "b", "aba"], "Ex": "bbbbaba", "Ey": "bbbbaba", "F": ["", "bba", "a"], "Fx": "bbbbaba", "Fy": "bbbabba", "d": 2, "x": ["bb", "b"], "y": ["b", "bb"]}, "w": "bbbbaba"}
SINGLETON_FAIL {"certificate": {"E": ["", "b", "abb"], "Ex": "bbbbabb", "Ey": "bbbbabb", "F": ["", "bba", "b"], "Fx": "bbbbabb", "Fy": "bbbabbb", "d": 2, "x": ["bb", "b"], "y": ["b", "bb"]}, "w": "bbbbabb"}
SINGLETON_FAIL {"certificate": {"E": ["", "bbb", "a"], "Ex": "bbbbbaa", "Ey": "bbbbbaa", "F": ["", "bbba", ""], "Fx": "bbbbbaa", "Fy": "bbbbaba", "d": 2, "x": ["bb", "a"], "y": ["b", "ba"]}, "w": "bbbbbaa"}
SINGLETON_FAIL {"certificate": {"E": ["", "b", "bab"], "Ex": "bbbbbab", "Ey": "bbbbbab", "F": ["", "bbba", ""], "Fx": "bbbbbab", "Fy": "bbbbabb", "d": 2, "x": ["bb", "b"], "y": ["b", "bb"]}, "w": "bbbbbab"}
SINGLETON_LENGTH7_END {"failed": 118, "passed": ["aaaaaaa", "aaaaaab", "abababa", "abbbbba", "abbbbbb", "baaaaaa", "baaaaab", "bababab", "bbbbbba", "bbbbbbb"]}
PERIODIC_GRID {"N": 1, "d1_d2": true, "m": 1, "parikh_saturated": false, "words": 3}
PERIODIC_GRID {"N": 1, "d1_d2": true, "m": 2, "parikh_saturated": false, "words": 4}
PERIODIC_GRID {"N": 1, "d1_d2": true, "m": 3, "parikh_saturated": false, "words": 5}
PERIODIC_GRID {"N": 1, "d1_d2": true, "m": 4, "parikh_saturated": false, "words": 6}
PERIODIC_GRID {"N": 2, "d1_d2": true, "m": 1, "parikh_saturated": false, "words": 3}
PERIODIC_GRID {"N": 2, "d1_d2": true, "m": 2, "parikh_saturated": false, "words": 4}
PERIODIC_GRID {"N": 2, "d1_d2": true, "m": 3, "parikh_saturated": false, "words": 5}
PERIODIC_GRID {"N": 2, "d1_d2": true, "m": 4, "parikh_saturated": false, "words": 6}
PERIODIC_GRID {"N": 3, "d1_d2": true, "m": 1, "parikh_saturated": false, "words": 3}
PERIODIC_GRID {"N": 3, "d1_d2": true, "m": 2, "parikh_saturated": false, "words": 4}
PERIODIC_GRID {"N": 3, "d1_d2": true, "m": 3, "parikh_saturated": false, "words": 5}
PERIODIC_GRID {"N": 3, "d1_d2": true, "m": 4, "parikh_saturated": false, "words": 6}
PERIODIC_GRID {"N": 4, "d1_d2": true, "m": 1, "parikh_saturated": false, "words": 3}
PERIODIC_GRID {"N": 4, "d1_d2": true, "m": 2, "parikh_saturated": false, "words": 4}
PERIODIC_GRID {"N": 4, "d1_d2": true, "m": 3, "parikh_saturated": false, "words": 5}
PERIODIC_GRID {"N": 4, "d1_d2": true, "m": 4, "parikh_saturated": false, "words": 6}
WEIGHTED_PHASE_FAMILY {"K": "1..4", "M": "1..3", "N": "M..M+3", "all_pass": true, "cases": 48}
PERIODIC_GRAMMAR {"d1_d2": true, "maxlen": 4, "mu_star": 4, "n": 1, "rule_minima": [3, 3, 4, 3, 3, 4, 3], "size": 31, "tau": 4, "theta": 4, "words": 3}
PERIODIC_GRAMMAR {"d1_d2": true, "maxlen": 8, "mu_star": 8, "n": 2, "rule_minima": [7, 7, 7, 7, 7, 8, 7, 7, 8, 7], "size": 48, "tau": 8, "theta": 8, "words": 5}
PERIODIC_GRAMMAR {"d1_d2": true, "maxlen": 16, "mu_star": 16, "n": 3, "rule_minima": [15, 15, 15, 15, 15, 15, 15, 15, 16, 15, 15, 16, 15], "size": 65, "tau": 16, "theta": 16, "words": 9}
PERIODIC_GRAMMAR {"d1_d2": true, "maxlen": 32, "mu_star": 32, "n": 4, "rule_minima": [31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 32, 31, 31, 32, 31], "size": 82, "tau": 32, "theta": 32, "words": 17}
SHORTCUT_GRAMMAR {"certificate": null, "d1_d2": true, "maxlen": 4, "mu_star": 4, "n": 1, "rule_minima": [4, 4, 1], "size": 12, "tau": 4, "theta": 4, "words": 2}
SHORTCUT_GRAMMAR {"certificate": {"E": ["", ""], "Ex": "cc", "Ey": "c", "F": ["", "abab"], "Fx": "ccabab", "Fy": "cabab", "d": 1, "x": ["cc"], "y": ["c"]}, "d1_d2": false, "maxlen": 8, "mu_star": 8, "n": 2, "rule_minima": [5, 5, 2, 2, 1], "size": 20, "tau": null, "theta": 5, "words": 5}
SHORTCUT_GRAMMAR {"certificate": {"E": ["", ""], "Ex": "cc", "Ey": "c", "F": ["", "abab"], "Fx": "ccabab", "Fy": "cabab", "d": 1, "x": ["cc"], "y": ["c"]}, "d1_d2": false, "maxlen": 16, "mu_star": 16, "n": 3, "rule_minima": [6, 6, 3, 3, 2, 2, 1], "size": 28, "tau": null, "theta": 6, "words": 24}
SHORTCUT_GRAMMAR {"certificate": {"E": ["", ""], "Ex": "cc", "Ey": "c", "F": ["", "abababab"], "Fx": "ccabababab", "Fy": "cabababab", "d": 1, "x": ["cc"], "y": ["c"]}, "d1_d2": false, "maxlen": 32, "mu_star": 32, "n": 4, "rule_minima": [7, 7, 4, 4, 3, 3, 2, 2, 1], "size": 36, "tau": null, "theta": 7, "words": 455}
EXHAUSTIVE_PAIRS {"fail": 1860, "histogram": {"(3, 3)": 96, "(3, 4)": 256, "(3, 5)": 608, "(4, 3)": 192, "(4, 4)": 496, "(4, 5)": 1064, "(5, 3)": 288, "(5, 4)": 720, "(5, 5)": 1364}, "marked_count": 124, "max_length_ratio": [1.6666666666666667, ["aaa", "aaaac"]], "pass_count": 5084, "pure_count": 56, "total": 6944}
EXHAUSTIVE_SMALL_SUBSETS {"by_size": {"1": {"failed": 0, "passed": 12, "passed_nonparikh": 6}, "2": {"failed": 15, "passed": 51, "passed_nonparikh": 36}, "3": {"failed": 144, "passed": 76, "passed_nonparikh": 56}}, "pool": ["a", "b", "c", "aa", "ab", "ac", "ba", "bb", "bc", "ca", "cb", "cc"]}
FORCED {"E": ["", ""], "F": ["", "c"], "added": "ababcc", "premises": ["c", "ababc", "cc"], "round": 1, "x": ["c"], "y": ["ababc"]}
FORCED {"E": ["", ""], "F": ["c", ""], "added": "cababc", "premises": ["c", "ababc", "cc"], "round": 1, "x": ["c"], "y": ["ababc"]}
FORCED {"E": ["", ""], "F": ["abab", ""], "added": "ababababc", "premises": ["c", "ababc", "ababc"], "round": 1, "x": ["c"], "y": ["ababc"]}
FORCED {"E": ["", ""], "F": ["", "abab"], "added": "ababcabab", "premises": ["c", "ababc", "cabab"], "round": 1, "x": ["c"], "y": ["ababc"]}
FORCED {"E": ["abab", ""], "F": ["", "c"], "added": "ccc", "premises": ["ababababc", "ababcc", "ababcc"], "round": 2, "x": ["ababc"], "y": ["cc"]}
FORCED {"E": ["", "abc"], "F": ["", "ab"], "added": "abab", "premises": ["ababababc", "ababc", "abababab"], "round": 2, "x": ["ababab"], "y": ["ab"]}
FORCED {"E": ["", "a", "c"], "F": ["", "ca", ""], "added": "abcab", "premises": ["ababababc", "ababc", "ababcabab"], "round": 2, "x": ["abab", "bab"], "y": ["ab", "b"]}
FORCED {"E": ["", "abab", ""], "F": ["", "c", ""], "added": "abcabc", "premises": ["ababababc", "ababababc", "ababcc"], "round": 2, "x": ["abab", "c"], "y": ["ab", "abc"]}
FORCED {"E": ["", "c"], "F": ["c", ""], "added": "ccabab", "premises": ["ababcc", "cababc", "cababc"], "round": 2, "x": ["ababc"], "y": ["cabab"]}
FORCED {"E": ["", "a", "ab"], "F": ["", "abca", ""], "added": "abababcab", "premises": ["abababab", "abababab", "ababcabab"], "round": 2, "x": ["ab", "bab"], "y": ["abab", "b"]}
FORCED {"E": ["", "a", ""], "F": ["", "ca", ""], "added": "abcababab", "premises": ["abababab", "abababab", "ababcabab"], "round": 2, "x": ["abab", "bab"], "y": ["ab", "babab"]}
FORCED {"E": ["", "abc"], "F": ["c", "ab"], "added": "cabababab", "premises": ["ababc", "ababababc", "cabab"], "round": 2, "x": ["ab"], "y": ["ababab"]}
FORCED {"E": ["", ""], "F": ["", "c"], "added": "ababababcc", "premises": ["ababc", "ababababc", "ababcc"], "round": 2, "x": ["ababc"], "y": ["ababababc"]}
FORCED {"E": ["", "ab"], "F": ["", "abc"], "added": "ababcababc", "premises": ["cabab", "ababcabab", "cababc"], "round": 2, "x": ["cab"], "y": ["ababcab"]}
FORCED {"E": ["", "b", ""], "F": ["", "bc", ""], "added": "abcabababc", "premises": ["ababc", "ababababc", "ababcc"], "round": 2, "x": ["aba", "c"], "y": ["a", "abababc"]}
FORCED {"E": ["", ""], "F": ["c", ""], "added": "cababababc", "premises": ["ababc", "ababababc", "cababc"], "round": 2, "x": ["ababc"], "y": ["ababababc"]}
CLOSURE_RESULT {"parikh_saturated": false, "pure_lengths": [4, 8], "seed": ["abababab", "ababc", "c", "cabab", "cc"], "shortest_pure": "abab", "status": "TRUNCATED: length/word limit", "steps": 16, "words": 21}
ALL_ASSERTIONS_PASSED true
```

再現ファイルの SHA-256：

- `verify.py`: `f87f9f344cd748b4d8468e46e3eebfc53504d1ae72d1ad795d573f4021a576e9`
- `verify.log`: `53860443008ff8d793ec80830cbfe7a3397ae3802a1101173c108b9ba06ba590`

## 13. 自己点検表

| 点検項目 | 結果 |
|---|---|
| t_typ の文法側の主張と、τ・特徴標本の言語側の主張を区別したか | **はい。** 定理3.1・4.1は文法側。系3.2等でのみ代入可能性と原稿の復元定理を使う |
| (2,s)-代入可能性を d=1,2 の両方、全ての非空組について確認したか | **証明した族については、はい。** 位相補題は全 arity。有限入力の判定器は非観測組の空分布も論理的に処理。一般の L の構造を解決したという意味ではない |
| 二穴文脈の中央区切りは全て非空か | **はい。** コードでは j<k。証明では非空区切りを状態決定・移送に明示的に使用 |
| 根型の保存を全ての必要な場面で確認したか | **はい。** 純成分端と ζ 成分の c の印。短い純成分は全保護。定理3.1の同時置換は根型保存を必要とせず、run 数への矛盾を用いることを明記 |
| 隣接ブロック・二成分交錯を確認したか | **はい。** 最大次数4の所有者グラフ、非選択区間の非空性、純成分の端の印を使用。交錯順序を制限しない |
| 短縮が必要な箇所で真に長さが減るか | **はい。** heavy は長さ>θ、置換は≤θ。非削除性により根で同じだけ減る。骨格置換は短縮の大小を仮定せず最終長を直接評価 |
| 肯定方向で全ての L と全ての G に対する一般の多項式を示したか | **いいえ。一般 (P2) は未解決。** bounded-run／shallow 等の明示した部分クラスでは全表示に一様 |
| 否定方向で固定パラメータ族と全特徴標本の下界を示したか | **いいえ。否定結果は得ていない。** クラス外の倍増文法を特徴データの下界として扱っていない |
| 候補族の Σ,s,f,r_max は固定か | **はい。** Σ={a,b,c}、c だけ ζ、fan-out cap=rank cap=2。FS の再検証時の別の文字型は明示的に区別 |
| θ̄ と ‖G‖ を元の文法で計算したか | **はい。** 規則表を一般形で掲載し、規則ごとの最短成功使用を計算。全規則を一度に使う条件は不使用。不要規則による水増しなし |
| 定数は ‖G‖,θ̄ に依存しないか | **はい、各証明済み部分クラスの明示した形で。** B,D の依存を隠していない。一般 B,D が定数と主張しない |
| 添付メモの主張を使う前に検証したか | **採用した主張は再証明または完全有限検証。** 任意アルファベット版 FS 定理Aと二文字の全体定理は不採用 |
| μ* の上界と τ の上界を混同していないか | **はい。** スペクトルだけでは肯定に不足と明記。P_{N,m} の τ の等式には別の埋込み長評価を使用 |
| 有限実験を一般定理の証明と混同していないか | **はい。** 一般族には別の証明。singleton 分類は有限部分の全証明書と任意長への帰着を付した計算機補助証明として明示 |
| 閉包の打切りを閉包完成と扱っていないか | **はい。** 実際の停止は TRUNCATED。各追加の強制性のみを使用 |
| 実行ログ・コードは省略されていないか | **はい。** 最終実行の全170行、全118件の singleton 違反証明書、全16件の追加証明書、ソース全文を収録 |
| コンパニオン arXiv:1409.6247 の未査読結果を前提にしたか | **いいえ** |
| 新規性の先行文献照合を済ませたか | **未了。** 対象原稿と指定メモとの比較は実施したが、網羅的文献調査・独立査読は未実施。新規定理であるとは断定しない |

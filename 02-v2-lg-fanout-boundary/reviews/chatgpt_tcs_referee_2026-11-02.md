# TCS 査読報告：Distributional Learning of Multiple Context-Free Languages under Fixed Finite-Semigroup Typing: Local Groups and the Length of Characteristic Data

**査読日**：2026年11月2日  
**対象**：`growupkuriyama-hub/Papers/02-v2-lg-fanout-boundary/main.tex`、GitHub `main`、取得時 Git blob SHA `52d568e72624bc58195761ba45c2d14312625bef`、全 3,815 行（TeX ソース）。  
**照合**：姉妹論文 `01_fixed-h-cfg/main.tex`、blob `637ee59131f40db3f2ad0ed1bb151adaed0f26a3`；Yoshinaka (2011, TCS 412:1821–1831)、Yoshinaka (2015, MoL 2015:87–98)。  
**位置づけ**：投稿前の独立査読を模した評価。実際の TCS 編集部の判断を代弁するものではない。行番号は上記 Git blob の `main.tex` 上の番号であり、組版 PDF の行番号ではない。

## R1. 判定・総評

**推薦：major revision（大幅改訂）。** ただし、**現時点で主定理 A・B・C を否定する具体的な反例は確認していない**。これは「数学的誤りを発見したための reject」ではなく、主要な技術結果を出版可能な形で監査・独立検証できるようにするための大幅改訂要求である。完全な一行ずつの形式的検証を終えたという意味でもない。

主な貢献は次の四点である。(1) ファンアウトが二以上の場合、非可換有限群の値を、多成分に分散し相互に入り組んだ部分導出の**同時置換**によって保持する組合せ補題を与え、局所群の型付けまで特徴データ長の多項式上界を拡張する。(2) 通常の文法サイズと規則厚さによる `O(‖G‖² θ̄_G)` の上界と、十分大きいアルファベットで必要な `Ω(‖G‖ θ̄_G)` を区別する。(3) ファンアウト1で擬多様体の境界を `LG` と定める一方、既知の指数下界の構成がファンアウト2では代入可能性を失うことを示す。(4) 高ファンアウト境界を半束の内容型付けへ帰着させ、二文字ならすべての固定 `f≥2` で肯定する。

**学術的評価**：主題は TCS に適合し、技術面の核心（非可換群の owner-wise simultaneous replacement）は十分に興味深い。結論の一番大きな「`f≥2` でも境界は `LG` なのか」は未解決であるが、それ自体で不採録相当とは判断しない。むしろ A(i)、C、半束への帰着、二文字の定理を独立した完成成果として明瞭に提示できれば十分な論文価値がある。懸念は、同一稿にファンアウト1の境界、一般 MCFG の正規化、既存の質的学習理論、非可換群の長い技術補題、二文字の新定理を全て置いており、中心の定理の監査が難しい点である。

### 判定表（「確認」は査読者として追跡できた範囲を示す）

| 項目 | 今回の判定 | 根拠と留保 |
|---|---|---|
| A(i)：局所群 `O(‖G‖² θ̄_G)` | **証明構造を確認、反例未発見** | §5、Appendix A–B：同時置換→短い型付き収量→witness。非可換群の全分岐を形式検証したわけではない |
| A(ii)：`Ω(‖G‖ θ̄_G)` | **主要論証・サイズ計算を確認** | §6、Appendix G：マーカーの充足、全単語長、規則計数 |
| B：ファンアウト1の `LG` 境界 | **条件付きで妥当** | §7：上界は A(i)、下界は姉妹論文の bracketed family の代入可能性に依存 |
| C：冪の二穴移行と family の脱落 | **証明を直接追跡、反例未発見** | §8、`lem:power-transfer`：同一の受理文脈、型の周期、非空の穴間を確認 |
| 型付け単調性、半束帰着 | **証明を直接確認** | §8 `lem:typing-monotone`、`prop:sl-reduction`；量化順序も整合 |
| 二文字定理・非飽和の場合 | **主要論理を確認、反例未発見** | Appendix H：run exchange、insertion、重いノードの反鎖計数 |
| 二文字定理・飽和の場合 | **P1–P6 を順に点検、未完の独立監査** | Appendix H：行剛性、同ラベルの頻度、比率、数え上げを追跡。外部検証は別途必要 |
| 質的再構成・正規化 | **構造・引用を確認、完全検証は未実施** | §3、Appendix C–E；Yoshinaka の技術的先行性は適切に認めている |
| 全ての定理が正しい、または既知でない | **未判定** | 証明の全形式検証・完全な文献探索ではない |

## R2. 新規性、先行研究、意義

### 2.1 姉妹論文との関係と表1

序論の Table 1（`tab:companion-overlap`、概ね L251–335）の切り分けは**概ね正確**。姉妹論文の positive-semigroup typing、集合駆動再構成、Gold 学習器、typed witness、window×group の上界、固定 `U₁` による指数下界は新規成果として重複計上していない。今回取得した姉妹論文の `main.tex` も、質的学習保証は Yoshinaka (2015) の specialization により得られることを明記している。

特に本論文固有の新規性の主軸は、(a) 複数成分が**任意の順で interleave**する時の群値保存、(b) **局所群**全体への昇格、(c) ファンアウトによる下界の非移行、(d) 二文字内容型付けの全 `f≥2` に対する上界である。`thm:lg-characterization` の群・Rees 表現自体は古典であるので、「新しい代数的特徴づけ」とは主張せず、既存構造の実装と応用として示した現在の方向は適切。

ただし Table 1 には次の注意が要る。§3 の qualitative reconstruction と §4 の typed-thickness accounting は議論を成立させる基本装置であり、**質的な存在定理そのものは新規でない**。「tuple versions / not new」というセルの意味を、**本論文での再定式化・有界ランクと非有界ランクの実装／既知の原理／新しい符号長境界**に区分すると読者は誤解しにくい。

### 2.2 Yoshinaka (2011, 2015)

Yoshinaka (2011) の多次元代入可能な MCFG の正例学習と、Yoshinaka (2015) の有限ソート署名からの再構成原理を先行研究としている点は必須かつ適切。2015 論文は *General Perspective on Distributionally Learnable Classes*, MoL 2015, pp.87–98（[ACL Anthology](https://aclanthology.org/W15-2308/)）、2011 論文は *Efficient learning of multiple context-free languages with multidimensional substitutability from positive data*, *Theoretical Computer Science* 412(19), 1821–1831（[DOI](https://doi.org/10.1016/j.tcs.2010.12.058)）。

重要な区別は、**characteristic sample の単語数**と**総符号長**、**集合駆動 operator の正確再構成**と**逐次 Gold learner の構文的収束**である。序論・§3 はこれを概ね守っている。ただし「Yoshinaka (2015) が polynomial-cardinality を与える」の前提は有限署名の設定を伴い、ここでの非有界 rank 対応は別の具体化であるため、`r` 固定／`r` 可変を一段明確にしてほしい。

### 2.3 A/B/C・半束帰着・二文字定理の整合

A(i) はすべての固定 `f` の**十分条件**、B は**`f=1` に限る**擬多様体の必要十分条件、C は**特定の下界族を `f≥2` に持ち上げられない**という否定命題であり、高ファンアウトで一般的多項式上界を主張するものではない。`prop:sl-reduction` はこの未解決境界を半束へ還元するもので、二文字の `thm:two-letter-content` がそれを完結させるわけでもない。この論理は序論・結論を通じ一貫する。

未解決問題が残ることは減点要因だが、**基礎組合せ補題と `f≥2` の二文字定理が出版可能な単独の定理である**なら決定的な欠点ではない。逆に A(i) の補題が十分に監査できず、二文字定理が詳細な検査に耐えない場合は、論文の新規性の核が弱くなる。よって付録 H・Appendix A/B を投稿前にもう一段独立検証する価値が高い。

## R3. 数学的正しさの重点監査

以下では、**証明の連鎖を具体的に確認した事項**、**明示的な要修正**、**未完の監査**を区別する。

### 3.1 定理 A(i)、非可換群の同時置換：§5、Appendix A/B

**主な連鎖**：`prop:block-replacement-interface` (L1334 付近) ← `lem:block-replacement` (Appendix A, L2130 付近) ← `lem:group-block-order` / `lem:group-interval` / `lem:two-sequence` / `lem:order-homogenize`。これを `lem:marked-heavy-window-group` (L1350 以降) と、局所群の場合は `lem:lg-buffered-owners` / `lem:local-group-shortest` (L2520–2620) に適用する。最後に `lem:witness-length-template` と `thm:data-from-typed-thickness` を使う。

- 可換群では各 owner の置換前後差を `G^d` の差分ベクトルにし、非空零和部分列を選ぶ。非可換群へ単純に持ち込まず、**owner の順序を保存したまま**処理しているので、素朴な「値の差の和」問題は回避される。
- 非可換群では共通の block pattern を抽出し、同一ブロック型の位置関係を同質化して chunk 列に直し、`κ_p=P_pQ_p^{-1}` の一致を用いる。`P_p(Q_p^{-1}Q_{p'})(P_{p'}^{-1}P_n)=P_n` と `κ_p=κ_{p'}` の同値は、群が非可換でも成り立つ（乗法順序を変えていない）。減少方向の chunk では `κ_{n-j}` を用いる説明も合っている。
- §5 の window–group 短縮は、長い root component の端をマークして端情報を保ち、反鎖の節点に短い導出を挿入する。`k=ℓ=0` の場合も非空を保証する一字マークがある。局所群では `k` 文字の buffer により、長さ `k+1` の跨ぎ因子を固定し、可変部分の群値を block product に回収する。この設計は理に適っている。
- `lem:lg-rees-window-coordinate` の Rees 行列乗法 ` (i,a,λ)(j,b,μ)=(i,ap_{λj}b,μ)`、prefix/suffix による最左行・最右列、sliding-factor の群積を確認。新しい分類定理としてではなく、既知の構造の明示実装と読むべきである。

**残る検査**：`lem:group-block-order` の全順序パターンの exhaustive な分類、`lem:order-homogenize` の反復に使うパターン数、`lem:lg-buffered-owners` の境界ぴったり `2k` の場合、および短い block の消去を含む `lem:local-group-blocks` の全場合分けは、今回は全形式検証していない。見つけた不備というより、外部査読者が最も時間を使う箇所である。Appendix A に小さい `f=2` の図解と、補題間の正確な定数フローの一表を要望する。

### 3.2 定理 A(ii)、付録 G

`prop:linear-factor-all-fanout` (L1587–1624) の語族は、`t=2f` 個の異なるマーカーが固定順に並び、語 `w_i` の `d_h` の位置が `h(i+1)`、全語長が `W=2fq+2^k+2f` になる。`d≤f` 個の穴に対し、共通の固定文脈に含まれるマーカーは高々 `d−1` 個なので、少なくとも `2f−(d−1)≥d+1` 個は穴の内部にある。鳩の巣原理より、ある穴は二つのマーカーを含み、その距離が `i` を一意に決める。ここから **任意の部分言語も `(f,trivial)`-代入可能**という帰結を得る。証明の骨格は十分に追跡できる。

付録 G（L3055–3109）の文法の計数を独立に再計算した。非終端数は `2q+k+3`、規則総サイズを足すと

`(2q+k+3)+(f+1)+q(3f+2)+(q+1)(2f+4)+q(2f+3)+2+5k = (7f+11)q+6k+3f+10`

となり、表示の係数と一致する。すべての `w_i` が同じ長さ `W` なので、既約文法の rule thickness が `W` になることも明快。下界は「任意の学習器が遅い」ではなく、**対象クラス全体に特徴標本を持つ集合駆動 operator** と、指定された二種類の canonical operator に対するものである。現在の主張はこの区別を守る。

**明示的な要修正：`cor:trivial-exact`（L1640 前後）**。冒頭の「Fix `f` and `r_max`」には `r_max≥2` の条件が書かれていない。一方、鋭さを達成するため引用する `G^{(f)}_{q,k}` は**ランク2**であり、ランク1に固定するとその例は証明対象のクラスに入らない。これは上界の間違いというより**下界・鋭さの量化範囲の記載不備**である。安全な修正は「上界は `r_max≥1`、鋭さの部分は `r_max≥2`」と分けること。ランク1での鋭さを主張するなら別の構成と証明が必要である。これは具体的な原稿修正項目とする。

### 3.3 定理 B と局所群の特徴づけ

`thm:fanout-one-data`（L1710 前後）は A(i) の十分条件と `U₁` の反例を合わせる。`thm:lg-characterization`（Appendix B, L2440–2485）の `(ii)⇒(iii)` では、最小イデアル外の冪等元 `e` に対して `eye` の冪等冪 `f` を取ることで `ef=fe=f≠e`、すなわち `U₁` の二元部分半群を構成する。局所群と「十分長い積が最小イデアルへ落ちる」という古典同値も明記されている。大筋は整合する。

**独立性についての必須確認**：`prop:bracketed-family(ii)`、つまり bracketed doubling family 自身が Clark–Eyraud 代入可能であることは、**姉妹論文の Proposition 6.4(i) の証明を前提として引用**しており、この稿にはその全証明がない（§7、L1690 付近）。その引用先は少なくとも原稿として存在し、今回確認した #1 の原稿内容と整合する。しかし本稿の B の否定方向はその一事実に依存する。姉妹論文の採否や版に依存せず読める短い自己完結補題または安定した公開版への正確な参照を追加してほしい。これは「証明が偽」という指摘ではない。

### 3.4 定理 C：二穴の冪移行

`lem:power-transfer`（L1787 以降）は次を用いる。`s(u)` の eventual period を `q`、index を `i₀` とし、`a,b≥i₀`、`d∈qℤ_{>0}` なら `s(u^a)=s(u^{a+d})` と `s(u^{b+d})=s(u^b)`。二つの tuple は共通の受理文脈 `p'u □₁ u □₂ q'` に入れると**同じ語**になる。中間の `u` は非空なので、穴間非空の定義に違反しない。従って任意の別の非空中間語に挟んで二組を交換できる。

`thm:doubling-no-lift`（L1820 前後）の `n≥2|S|+3` は `i₀+q≤|S|+1`、`a=i₀,d=q,b=n-a-d-2≥i₀` を確保する十分条件であり、選んだ二箇所に `u=⌊` を挿入して初頭 `⌊` の連続長を増やすと、唯一の ceiling-free word `W_n` ではなくなる。この矛盾の位置を追跡できた。**「この指数族は `f≥2` で脱落」から「すべての指数下界は `f≥2` で消える」へ飛躍していない**のも適切。

### 3.5 `lem:typing-monotone` と `prop:sl-reduction`

`lem:typing-monotone`（L1867 以降）：`s≼t` のとき共通文脈・等 `t` 型による Link は必ず等 `s` 型の Link なので、`B_{f,t}(K)` の規則が `B_{f,s}(K)` に包含される。この向きは正しい。`L∈C_{f,s}` のとき後者は sound であり、特徴標本の引き継ぎも成立する。

`prop:sl-reduction`（L1890 以降）：`V⊄LG` ならそのある有限半群に `U₁` が部分半群として存在し、閉包性から `U₁∈V`。有限半束 `H` について `χ_z(x)=1⇔zx=z` と置けば `χ_z(xy)=χ_z(x)χ_z(y)` となり、`H` は `U₁^H` に分離的に埋め込める。よって `SL⊆V`。任意の有限半束型付け `s` は内容型付け `c_Σ` の粗い商で `s≼c_Σ` なので、内容型付けでの標本を `s` に移せる。この導出は定義どおりで、**「全部の有限半束に同一の数値定数が必要」ではなく、型付けごとの多項式を許す**点も適切。

### 3.6 付録 H：二文字内容型付け、非飽和の場合

`lem:app-two-runs(i)`（L3185 前後）の鍵は `x^4` から `(x,xx)` と `(xx,x)` が `□₁x□₂` において共通受理され、型も等しいこと。これを任意の非空区切りに用いると同じ `x`-skeleton のまま `x` の余剰数を塊間に移すことができる。(ii) は `xxyx` を `xyxx` に移し、文脈 `(Ux,xV)` が `xy` と `yx` を比較可能にする。全隣接交換で Parikh 飽和に達する。(iii)・(iv) の反証は、余剰 `x` の移動で `xxyx` または禁じられた `y⁴` が生じるという機構で、文脈の穴間非空条件を使えている。

`lem:app-two-insertion`（L3250 前後）：純な root component の左右二字、両文字型の component の各一字を保護するので、高々 `4f` 個の節点だけを反鎖から除外する。残りの所有者を、ブロックの隣接により最大次数 `2f` のグラフに入れ、`|Q₀|≥2f+2` なら独立集合は二頂点以上である。選択所有者が同じ種類の純成分を汚染すれば非中立の内部 run が二つでき、異なる種類なら各成分の `x,y,x` と `y,x,y` が生じる。この二分法が `prop:app-two-nonsaturated` へ繋がる。**単純に「二文字と同様」と省略していない点はよい**。

**確認してほしい説明上の境界点**：`lem:app-two-insertion` の「別所有者のブロックが選択後に別々の内部 run を作る」段落（およそ L3290）を、**同じ root component に属する場合／異なる root component に属する場合**に分けて図示すべきである。実際には許容文脈の内部区切りが非空であること、および `I` に含まれない owner の領域をそのまま保つことが必要になる。今回の読解では反例は見つからないが、一文だけでは各 run の distinctness の検証が難しい。

### 3.7 付録 H：Parikh 飽和の場合 P1–P6

`lem:app-two-saturated`（L3330–3452）を、次の観点で点検した。

- **union が両文字を含む場合**：内容型に対して各文字が必要な component 数 `t_a,t_b` を用い、最小化した余剰閾値 `c_a=n_a-t_a+1`、`c_b=n_b-t_b+1` により、重い部分導出がどちらかの資源を大量消費する。経路長に `v(θ+2f+1)`、各深さの反鎖に `θ+2f` の境界を出す。この点は計算とも整合。
- **P1 Row rigidity**：同一 `b`-座標に `a` の差 `δ` が `1≤δ≤K-h` で存在すれば、`a` と `a^{1+δ}` が共通文脈を持ち等分布になる。候補 `(p+K,q)` を `δ` 減らせるので最小性に矛盾。`c₀≥1` は比較対象を非空に保つ重要な条件である。
- **P2 Height**：同一非終端かつ同一 `b`-count で上下に二回短縮されると `a` が少なくとも `2(K-h+1)` 必要になる。`K>p+2h−2` に反するため、同一ラベル・同一 `b`-count の三重出現は不可。従って経路の節点数 `≤2v(q+1)`。
- **P3–P4**：重い純 `a`-節点をしきい値 `θ+f−1` として取ると、同じ非終端を持つものは互いに比較不能。`g_u=ℓ_u−x_{B_u}` と `Y(J)=∑y_B` を使う置換の比較で、同じ非終端の複数箇所の `g_u` は一致し、頻繁なラベル間で `g_B/y_B` は共通比率 `α` になる。閾値 `m_B>θ` は `y_B≤θ` を確保するためである。
- **P5**：頻繁な純節点には `ℓ_B≤(1+α)θ`、同時に重い純節点の高さは `≤v`、各層の頻繁な節点数は `(1+α)θ/α<θ+1`（`α>θ` の場合）。これと稀な節点総数 `≤vθ` の比較から `α≤(r+1)(θ+f−1)(2θ+1)v` が出る。
- **P6**：巨大な純節点には頻繁なラベルが付かないので、数は `≤vθ`。混合節点の `M≤4vθ²` と分解して `K=O_{f,r}(v²θ⁵)`。表示の粗い係数は、`r≥2, θ≥1, f≥2, v≥1` の範囲で整合する。

**重要な留保**：P3 の二つの antichain の置換後比較は、部分導出の局所収量ではなく**完成した成功導出の Parikh ベクトル**を使う。この点の説明と、P4 で選ぶ `y_C` 個の `B` 節点と `y_B` 個の `C` 節点が同一ラベル内で各々 antichain になる理由（P3）を図または独立補題に切り出すと、証明が相当に検証しやすい。今回これらを追跡して具体的な矛盾は見つからなかったが、**証明を機械的に形式検証していないため、定理全体を無条件に「完全検証済み」とは扱わない**。

### 3.8 定義・空語・operator・ランク

- 許容 `d`-文脈は `v₁,…,v_{d−1}∈Σ⁺`（L561 以降）。二穴交換の証明はすべてこの「非空の内部区切り」を用いている。
- good は `λ`-free, nondeleting, nonpermuting, nonmerging（L535 付近）、reduced は reachable+productive。この条件は短縮時の「収量が消えない」「ラベルの自己経路は identity」「子の yield が非空」に不可欠である。
- `θ̄_G=max{1,θ_G}` と「規則を使う最短**文**の長さ」を区別する定義（L994–1012）は適切。`t_G` と `t_typ` の量の方向を混同していない。
- `B^{≤r}` は composition rank を `r` で切り、`B` は標本から上界を与える unbounded-rank operator（L742 前後）。両 operator の共通特徴標本の主張は §4 の witness 構成で保証されている。
- `ε` は新しい identity で正語型から分離し、start rule だけで処理する。`ε∈L` の標本コストは `+1`。ここも一貫する。

## R4. 要旨・結論・下界の量化と未解決問題

**全体評価：大半は正確**。要旨（L66–97）・序論・結論では、`LG` の境界決定を `f=1` に限定し、`f≥2` については「半束への帰着」「二文字の場合の肯定」までとしている。C の排除は**特定の bracketed family** に対するので、`f≥2` の指数下界を一般に否定するものではないと明記されている。

要修正は次の三点。

1. 上記 `cor:trivial-exact` の鋭さの **`r_max≥2`** の追記。
2. A(ii) の下界は **`|Σ|≥4f+1`** を要する。§6 の見出し・結論ではこの条件が十分明記されているが、要旨の「the factor is unavoidable」の直後にも条件付きであることを今より視覚的に明確にしてよい。
3. 「`all but finitely many`」の C は `n≥2|S|+3` の**固定された `s` ごとの閾値**である。現在の表現は正しいが、結論で `s` への依存をもう一度明記するとよい。

`op:S1`（ファンアウト1、二文字 U₁）と `op:fanout-two`（`f=2`、半束内容型）は別問題であり、「型1の文字が一つの U₁ なら `f≥2` で任意の Σ に多項式」という未解決の強い命題が二文字の定理から出るわけではない。この区別は崩さないこと。

## R5. 構成・記号・英語

### 5.1 44ページの評価

TCS の理論論文として 44ページそのものは却下理由ではない。問題は、数学的な重みの異なる成果が散在していることである。論旨を **「A(i) の同時置換と局所群」「B/C の境界現象」「半束帰着と二文字定理」**の三本柱として見せることを提案する。

- §3 の再構成と Gold の質的結果は先行研究との差分だけを本文で、技術的な補題証明は現行 Appendix C–E でよい。
- Appendix A（群の block order）と B（局所群）の核は新規上界に直結するため**削らない**。むしろ §5 本文に正確な proof roadmap を追加する。
- §6 の線形因子例は main statement と短い理由、長い文法計数は Appendix G に維持する。
- §7 の fan-out-one `LG` 境界は主題との比較として必要だが、姉妹論文の指数族の再掲が重複する。独立性を担保する短い代入可能性補題と帰結だけに縮約してよい。
- Appendix H は二文字で**初めて全 `f≥2` に多項式**とする重要結果なので削らない。ただし P1–P6 を補題ごとに小分けする方が圧縮より有効。
- Appendix I の比較・非文脈自由例は有用だが、本文では図と一段落で十分。スペース制約があればオンライン補足へ回せる。

### 5.2 読者の混乱点

`S`（型の有限半群）・`s`（型付け）・`S`（文法の開始記号）、`G`（文法）・`𝔾`（群）、`θ_G`・`θ_typ`・`t_typ`・`τ`、`K`（標本）・`𝕂`（最小イデアル）など記号が多い。冒頭の symbol table は良いが、§4 の前で **rule thickness / typed thickness / distribution-representative length / minimal positive type length** の「定義・増減関係・何を評価するか」の表を足すと効く。また、`c_Σ` は content typing、`c_{𝔾,f}` は block-replacement constant という別概念であることを明示してほしい。

### 5.3 英文の小修正

深刻な文法破綻は見つからない。以下は style／明晰化。

- Abstract「at every fan-out every target ...」→「for every fixed fan-out, each target ...」：固定パラメータへの依存を見せる。
- §1「The factor `‖G‖ θ̄_G` is unavoidable」→「A total characteristic-data length of order `‖G‖ θ̄_G` can be necessary ...」：上界 `‖G‖² θ̄_G` のどちらの因子が最適か誤解を防ぐ。
- §5「owner-wise simultaneous selection」：最初に owner=one incomparable derivation subtree、block=one component interval と短く定義し、以降は統一。
- §8「does not lift」：本文と要旨では「this particular family fails the arity-two substitutability condition」を併記。
- §3 では capped / uncapped と bounded / unbounded rank の二組の形容詞が混ざるので、最初に対訳と対応を明示。
- Appendix B の `grp`, `row`, `col` は Rees の group coordinate / `I`-index / `Λ`-index を各一文で再確認。

## R6. 著者に求める修正（優先順位付き）

### 必須

1. **ランクの量化を修正** — `cor:trivial-exact`、§6（約 L1640）。上界は `r_max≥1` でよいが、引用している下界達成文法はランク2。鋭さの主張には `r_max≥2` を明記し、必要なら corollary を二文に分ける。
2. **姉妹論文への唯一の数学的依存を監査可能にする** — `prop:bracketed-family(ii)`、§7（約 L1690）と Table 1。対応する正確な Proposition 6.4(i) と公表版を固定し、できれば一ページの独立した証明または十分詳しい proof sketch を付す。姉妹論文が査読中であることを数学的真偽の根拠にしない。
3. **付録 A の非可換群の同時置換に「入力・出力・不変量」表を追加** — `lem:group-block-order`、`lem:group-interval`、`lem:order-homogenize`、`prop:block-replacement-interface`（L2108–2340）。同一 owner の複数 block が互いに interleave し、抽出によって順序が保たれる理由を図一枚と簡単な `f=2` の模式例で示す。特に `κ_p=P_pQ_p^{-1}` を左右からどう適用するかを式のまま記す。
4. **付録 H の挿入補題で distinct internal runs の位置を明示** — `lem:app-two-insertion`（約 L3250–3320）。`I` の同じ純成分／異なる純成分への作用を分け、「選ばなかった owner の block は元の文字のまま残る」という非空の緩衝部分を明記する。
5. **付録 H の P1–P6 の証明依存と余裕量を明示** — `lem:app-two-saturated`（約 L3330–3455）。P1 と P3 の比較対象は完成した成功導出の Parikh ベクトルであること、P4 の singleton／複数節点選択が antichain になること、P6 の残余 subtree の網羅性を補助図か独立補題で説明する。これにより過不足のない独立査読が可能になる。
6. **主要な結果の真の適用範囲を要旨・比較表でも揃える** — abstract、Theorem A、`cor:two-letter-semilattice`、`op:fanout-two`。固定 `f,r,s,Σ`、`B^{≤r}` と `B`、`|Σ|≥4f+1` の条件と、`f≥2` の未解決境界がどの段階で残るかを一表に集約する。

### 望ましい

7. 正規化（Appendix E）で fan-out、rank、size を保存するが **thickness は保存しない**ことを §3 の proposition 直後にもう一度明記する。これは結果の前提を入力文法へ無条件に移してはいけない理由に直結する。
8. 局所群を単なる window×group の言い換えと誤読されないよう、`prop:li-g-strict` の「`ab` occurrence parity」例を序論に一行増やす。
9. 既存の学習保証 vs 新しい encoded sample length を示す比較表を、Table 1 と別に §4 に配置する。
10. Appendix H の非飽和時の線形 `t_typ` 上界と、飽和時の `τ` 多項式上界を明確に別色でなく別段落で見せる。二者は証明する量自体が異なる。
11. 全 theorem/reference の label のリンクとコンパイル後の警告を CI で再確認する。今回の監査は LaTeX を実際にビルドしていないため、ページ数・図の配置・参照文字の体裁について検証済みとは主張しない。
12. 既存関連文献を網羅したという断定を避け、特に群短縮に近い Ramsey／factorization 技法との優先権について、原著掲載版を追加確認する。

## 最終勧告と採録可能性

**Major revision を推薦する**。最も重要な点は数学的意義がないことではなく、独立した誌上論文として、(i) 中核の非可換同時置換の正確な条件、(ii) 付録 H の強い全ファンアウト結論、(iii) 他稿に依存する指数族の可読性を、一人の TCS 査読者が再計算しやすく整理する必要があることだ。**今回の読みでは定理 A/B/C と二文字定理のいずれにも決定的反例を見つけていない**ので、reject は勧めない。

**数理監査の限界**：本報告は GitHub 上の実際の `main.tex` を指定範囲にわたって読み、依存関係と主要式を手計算したが、3,815 行すべてを逐語的に形式証明したものではない。全導出規則に対する機械的モデル検査、各補題の全パラメータの検証、組版 PDF のページ別校合、引用文献の網羅的先行研究調査は実施していない。指摘している修正の大部分は「偽だと証明された箇所」ではなく「正しく見える論証を他者が反復検証可能にするための要求」であり、その違いを保ったまま解釈されたい。

### 原稿と参考文献へのリンク

- 原稿正本：[GitHub `main.tex`](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/main.tex)
- 姉妹論文正本：[GitHub `01_fixed-h-cfg/main.tex`](https://github.com/growupkuriyama-hub/Papers/blob/main/01_fixed-h-cfg/main.tex)；[arXiv:1409.6247v5](https://arxiv.org/abs/1409.6247v5)
- Yoshinaka (2011): [TCS 論文 DOI](https://doi.org/10.1016/j.tcs.2010.12.058)
- Yoshinaka (2015): [ACL Anthology](https://aclanthology.org/W15-2308/)
- 背景の有限半群：Almeida–Margolis–Steinberg–Volkov (2009), *Transactions of the AMS* 361(3):1429–1461, DOI [10.1090/S0002-9947-08-04712-0](https://doi.org/10.1090/S0002-9947-08-04712-0)

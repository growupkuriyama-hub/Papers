# TCS査読報告 — 局所群とMCFGの特徴データ長（一点集中版）

**対象**：Takayuki Kuriyama, *Distributional Learning of Multiple Context-Free Languages under Fixed Finite-Semigroup Typing: Local Groups and the Length of Characteristic Data*  
**査読日**：2026年11月6日（日本時間）  
**判断**：**major revision（大幅修正）**。中心的な三定理に対する反例は今回見つからなかったが、IPTtDと呼ぶ帰結には、引用する定義と出力される仮説の表現クラスとの**形式上の不一致**がある。さらに、要旨には下界の量化範囲を過大に読ませる文がある。主要証明のうち非可換群の組合せ論と三文字族の任意の深さにわたる解析は、部分的な検証に留まる。問題は無条件の採択判断をためらわせるが、現時点で主定理A・B・Cが偽だと判定したわけではない。

---

## 0. 取得した原稿の版と査読方法

- **査読対象の唯一の本体**：[`02-v2-lg-fanout-boundary/main.tex`](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/main.tex)。GitHubのファイル取得機能を用い、2026年11月6日 **01:00–01:11 JST** に全3,554行（約187,705文字）を直接取得・通読した。冒頭と末尾、および対象定理の範囲を再取得して照合した。
- **取得したGit blob SHA**：`cb27c54a35366ff1f93a94c1d62c68464c2b9cd7`。この識別子で本報告を固定する。コミットSHAは取得・確定していない。後日に`main`が改訂されても、本報告の対象はこのblobである。
- 原稿は本文§1–9、付録A–G、参考文献から成る単一LaTeXファイルである。「41ページ」は依頼資料の版情報であり、**本査読ではTeXをコンパイルしてページ数・組版を再検証していない**。行番号は上記TeXの物理行番号であり、PDFの印刷行番号ではない。
- 外部比較に用いたものは、プロジェクト収録の姉妹論文TCS R1合成PDF、Yoshinakaの関連論文を含む参考文献集、およびEyraud–Heinz–Yoshinaka (2016) の定義2.12などである。姉妹論文のarXiv v5を今回新たに全文取得し証明し直したわけではない。先行研究評価のうち版依存の箇所はその制約を踏まえる。
- 評価対象は現行`main.tex`であり、`parked/`や2026年11月2日の旧査読報告を判断の前提にしていない。計算検証はPython 3標準ライブラリだけで実施し、コードと実測出力を§R3.10に記録した。

## R1. 総評と推奨

### 貢献の要約

1. 固定有限半群型付けを持つMCFG分布学習について、既存の定性的同定の議論から**特徴データの総符号長**の問題を切り出し、reduced goodな表示のサイズ`‖G‖`と規則厚さ`θ̄_G`に対して評価する。
2. 型付けの正の像が局所群（LG）に属すれば、固定ファンアウト・固定ランクで`O(‖G‖² θ̄_G)`の上界を与える。特に、非可換群の順序つきブロック積を同時に保つ置換がMCFG固有の技術的貢献である。
3. あらゆる型付けに対し、適切な字母数の下で`Ω(‖G‖ θ̄_G)`を要する有限言語族を構成し、自明な型付けでは上界との一致を得る。
4. ファンアウト1では、**擬多様体を量化した**一様多項式データ性の境界がちょうどLGであることを示し、従来の二元半束による指数下界を三文字の族で再構成する。
5. §8は同じ指数族がファンアウト2に移せないことを証明し、一般の`f≥2`に対する必要性を未解決と明示する。

### 推奨：**major revision**

**長所**：問題の量は明確で、三本の主定理は上界・下界・代数的境界として自然につながる。LGのスライディング因子座標と非可換群のowner-wise同時置換を結び付けた部分は、既存のCFG結果の単なる言い換えではない。§8も単なる将来課題ではなく、ファンアウト1の下界を流用できない具体的障害を証明する。

**修正が必要な理由**：第一に、§7のCorollary `cor:iptd`が引用する厳密なIPTtDの定義では、仮説は指定された**表現クラスRに属さなければならない**。原稿はRを「reduced good文法＋空語ビット」と定めながら、生成する仮説を一般のMCFGとしており、そのままでは推論が完結しない。これは定義上の実例で明示できる（§R3.8）。第二に、要旨の「every set-driven learner」という無限定な語句は、実際の定理より強い。第三に、最重要の非可換同時置換と三文字族の決定的パーサーは、正しいと考えられるが記述が圧縮されており、査読者が検査しやすい状態まで補助不変条件を明示してほしい。修復可能な問題と見るので、**rejectは推奨しない**。ただし修正を本文の語句置換だけで済ませず、仮説表現の補題・証明を追加することを要する。

## R2. 新規性と重要性

### R2.1 姉妹CFG論文との比較：表1は概ね適切

- **再構成と定性的学習**（§3–4、表1第1行）：新規性の中心と呼ばない姿勢は正しい。Yoshinaka (2011, 2015)に基づくConst/Link/CompとGold同定を本稿は具体的に再証明しているが、定性的な枠組みそのものの発明ではない。
- **窓・窓×群のデータ上界**（表1第2行）：ファンアウト1の到達点を姉妹論文側に置き、非可換順序を保ったファンアウト`≥2`の処理を本稿の新味とするのは妥当。
- **LGの扱い**（表1第3行）：重要である。ただし「LGの古典的半群特徴付け」が新規だと読まれないよう、`thm:lg-characterization`を**古典結果の自己完結な座標化**、`thm:local-group-polydata`を**新しいデータ長定理**と分けるとよい。§5.3と付録Cはすでにこの区別を概ね行っている。
- **倍増族**（表1第4行）：五文字括弧族を三文字に減らし、外部原稿を前提にしない証明を付けた点は技術的改善である。ただし「指数下界という現象そのものが今回初めて」という読みは避けるべき。
- **rare-type一般化、線形因子下界、ファンアウト2のpower transfer**（表1末尾）：区分は適切。特に線形因子は全ファンアウト・全型付けという量化が重要であり、必要字母数を表と要旨で維持すべきである。

したがって「姉妹論文の十分条件`LI∨Grp`を、ファンアウト1で**擬多様体に関する必要十分条件LGへ改善**」という位置付けは成立する。ただし、**個別の固定型付けについてLG所属が必要十分であるという定理ではない**。現稿のRemark `rem:fanout-one-data` はこの点をおおむね防いでいる。

### R2.2 Yoshinaka (2008, 2011, 2015)との関係

Yoshinaka (2008)の固定窓における長さを含む効率性、(2011)のMCFG・多次元代入可能性・厚さの議論、(2015)の有限シグネチャでの定性的同定を、§1および§3で明確に先行研究に帰している。この扱いは適切である。特に**多項式個数の例**と**その総長が多項式**であることを別命題としている点は重要で、正しい研究上の区別である。

なお§3冒頭の対応表において、2015年の有限シグネチャの一般定理と本稿の`K`に依存する無上限ランクの演算子との距離を述べているのもよい。だが「qualitative result inherited」という要旨の表現は、**既知定理から機械的に直ちに導かれる**と読める一方、実際には本稿が異なる具体的な仮説構成と無上限ランク処理を証明している。`built on / in the spirit of` などの方が正確である。

### R2.3 論文の一体性と未解決性

A→B→Cという単なる一本道ではなく、A（LG十分条件）とB（普遍的線形因子）が**既知上界の精度**をはさみ、Cがファンアウト1の代数的必要性を確定する構成になっている。§8はCを全ファンアウトへ延ばすときの誤った推論を防ぐので、論文に残す価値がある。

`f≥2`の境界が未解決であるため、「全ファンアウトでLGが必要十分」という大定理としては投稿できない。しかしこれは論文の価値を致命的に下げない。非可換同時置換の証明と全ファンアウトでの普遍下界は、それだけでも独立した結果である。むしろ**§1・要旨冒頭では「境界」を必ずファンアウト1に限定**し、§8の限界を積極的に位置付ける方が新規性が鮮明になる。

## R3. 正しさの監査

### R3.1 検証状況一覧

「**確かめた**」は本査読で定義と証明の主要論理を直接追跡し、指摘した範囲に矛盾を見つけなかったという意味であり、形式証明器による証明済みの意味ではない。「**一部確かめた**」は重要な段階を点検したが全場合の独立検証は完了していないという意味である。

| 論点（TeX位置） | 状況 | 実施した点検／残る範囲 |
|---|---|---|
| `prop:block-replacement-interface`、`lem:block-replacement`、Appendix A–B（1409–1434, 2087–2383） | **一部確かめた** | 非可換の`P_pQ_p^{-1}`の順序、反転したownerの添字、ゼロ和の可換版、`S₃`例を点検・検算。大きな`f`について順序均質化補題の全場合は形式検証していない。 |
| `lem:lg-buffered-owners`、`lem:local-group-shortest`（2562–2662） | **一部確かめた** | 距離`2k`、次数上界`4kf`、緩衝部分の長さ`≥2k+1`、型保存の伝播を追跡。全ての絡み合い配置を列挙していない。 |
| 局所群の代数的座標化 `thm:lg-characterization`（2447–2526） | **一部確かめた** | 最小イデアル・Rees座標の依存関係と`U₁`排除の論理を追跡。引用先の古典証明全体の再導出までは行っていない。 |
| 定理A `thm:local-group-polydata`（1614–1653） | **一部確かめた** | 補題を認める場合の`β=O(‖G‖ θ̄)`から`O(‖G‖² θ̄)`への計数は確認。成否は上記組合せ論補題に依存。 |
| 定理B `prop:linear-factor-all-fanout`、`cor:trivial-exact`、Appendix G（1664–1747, 3210–3331） | **確かめた** | マーカー数の鳩ノ巣、全ての部分集合の代入可能性、文法生成とサイズ`(7f+11)q+6k+3f+10`、厚さ`W`、特徴データ下界の連鎖を追跡。小例を全探索。 |
| 定理Cの三文字族 `prop:three-letter-family`、Appendix F（1770–1795, 3026–3209） | **一部確かめた** | `|W_n|=3·2^n−2`、`‖G_n‖=13n+7`、`θ̄=4n`、稀な型による下界を確認。`n=1,2,3`の代入可能性を全探索。任意の`n`のパーサー単射性は原稿の証明に依存。 |
| ファンアウト1境界 `thm:fanout-one-data`（1813–1849） | **一部確かめた** | LG十分性＋`U₁`が全ての非LG擬多様体に入ること＋三文字族の量化の連結は確認。前二者の外部半群論／上界補題の検証範囲は上記のとおり。 |
| §8 `lem:power-transfer`、`thm:doubling-no-lift`（1931–1999） | **確かめた** | 共通の2穴許容文脈`p'□₁u□₂q'`、冪の型一致、後半の非空区切り、移動後のParikh保存・非一致を直接確認。`n=6`の具体例でも検算。 |
| `prop:rare-type`、`cor:distribution-representatives`（1210–1329, 2840–2923） | **確かめた** | 型全体削除がクラス内に残ること、二標的の識別議論、分布同値代表でもwitnessが有効であることを追跡。 |
| 許容文脈、good/reduced、`θ̄_G`、`\mathcal B`対`\mathcal B^{≤r}`（444–675, 791–824, 1046–1139） | **確かめた** | 非空の内部区切りとnonmergingの対応、空語を分離するfresh identity、rank依存の箇所を追跡。`\mathcal B`は`‖K‖₊`依存の無上限演算子。 |
| `prop:good-normalization`（950–959, 2924–3025） | **一部確かめた** | 各段階の言語恒等式と`f,r`固定のサイズ計数を確認。ただし引用文献中のすべての変換を元の規定で再照合したわけではない。 |
| `cor:iptd`（1879–1923） | **問題を確認した** | 引用するIPTtDの表現クラス条件が、そのまま出力される`\mathcal B^{≤r}(K)`には満たされない例がある。§R3.8に具体例と修正法を記す。 |

### R3.2 定理A：非可換群の同時置換

主たる難所は、複数のtuple成分に散った部分木の寄与を、**ownerごとの複数ブロック**として扱い、グループの積を勝手に可換化しないことにある。付録A–Bの証明では、(i) block patternの固定、(ii) 二点順序比較の均質化、(iii) 同じ向きのchunk領域への分解、(iv) 各領域の`κ_p=P_pQ_p^{-1}`の衝突、という四段階が明示されている。この道筋は妥当である。

特に、ある領域の元の全積`P_n`に対して、区間`(p,p']`だけを置き換えた積が

`P_p (Q_p^{-1}Q_{p'}) (P_{p'}^{-1}P_n)`

になる点を確認した。従って同じ領域で積を保存する条件は`P_pQ_p^{-1}=P_{p'}Q_{p'}^{-1}`であり、**逆順の`Q_p^{-1}P_p`では一般に足りない**。原稿は正しい側を使っている。増加方向と減少方向で`κ_j`と`κ_{n-j}`を対応させ、全領域の状態を`𝔾^c`に載せる議論も整合的である。付録Aの`S₃`実例はコードで元の2行と置換後の2行がいずれも単位元になることを確認した。

非可換版の均質化定数`M_{𝔾,f}=𝒫_f max(3,|𝔾|^f)^{2^{f²}}`は極めて粗いが、`f`と`𝔾`が固定される主定理には影響しない。`lem:group-block-order`・`lem:two-sequence`・`lem:order-homogenize`の抽出段階も読んだが、任意の配列に対する完全な機械検証や別証明はない。**反例を得たのではなく検証範囲の限界**である。投稿稿には、この四段階を本文の半ページほどの図または不変量表に簡潔に残すのが望ましい。

### R3.3 LGの緩衝ownerと座標化

`lem:lg-buffered-owners`の独立集合論法（行2562–2605）は、ownerが持つ高々`f`区間ごとに左右`2k`文字未満で近接し得る別ownerを数える。次数`≤4kf`から`m/(4kf+1)`人のownerを選び、各区間を左右`k`文字で拡張するため、異なる選択ownerの拡張区間の**内部が交わらない**。拡張後は少なくとも`k`文字の固定な前後部分と非空の置換部分を保ち、長さ`≥2k+1`となる。この数え方と、rootの最初・最後`k`文字を触らない条件を確認した。

`lem:local-group-blocks`は長い置換ブロックの内部に完全に入る長さ`k+1`因子を`γ(β_j)`に、ブロック境界を跨ぐ因子を不変な`z_j`に分解する。短いブロックは窓型が一致すれば語自体が一致するため固定材に吸収する。**群が非可換でも因子の出現順を保持する**仕組みになっている。

`thm:lg-characterization`で重要なのは、最小イデアルのRees表示を使うのは十分長い語だけであり、短語を窓`ŝ_{k,k}`で厳密に記録する点である。`LG ⇔ U₁を含まない ⇔ 全冪が最小イデアルへ入る`という古典的関係を使った議論は筋が通っている。外部文献の古典補題そのものを今回独立に再証明したとは言わない。

依存する補題を認めれば、最短代表の長さが`β=O(‖G‖ θ̄_G)`、型付き規則・非終端の個数が`O(‖G‖)`なので、`thm:local-group-polydata`の`O(‖G‖² θ̄_G)`は確実に出る。定理Aの**最後の定量的な推論**には未解決の計数飛躍は見当たらない。

### R3.4 定理B：全ファンアウトの線形因子

付録Gの証明は、今回とくに確信を持てた部分である。`t=2f`個の区切り文字`d_h`がある。二つの異なる語`w_i,w_j`が許容`d`穴文脈を共有すると、左端と右端の固定部分にマーカーを置けず、中間の各固定部分も高々一つしか持てない。従って固定部分のマーカーは高々`d−1`、穴の中に少なくとも`2f−d+1≥d+1`ある。`d≤f`の穴のいずれかに二つのマーカーが含まれ、距離でパラメータ`i`を復元できる。これが**言語の任意の部分集合**の`(f,s_triv)`-代入可能性を支える。一般の型付けでもクラス包含があるため、下界が通る。

文法の生成形と各規則の長さを計算し直して、`‖G^{(f)}_{q,k}‖=(7f+11)q+6k+3f+10`、`θ̄_G=W=2fq+2^k+2f`と一致した。語が全て同じ長さであり、どの規則も成功導出に現れるので、**任意のreduced good表示でも厚さはW**である。さらに自明な型付けのcharacteristic witnessの語数上界`≤‖G‖`と、「全`q+1`語が必要」との組み合わせで、最小表示サイズが少なくとも`q+1`になる。したがって人工的に文法を水増ししただけの下界ではない。

`f=1`で五文字を二文字に同一視した場合も、二つの`d`の距離が`i`を決めるという別証明が備わっている。小例`f=1,2`、`q=2,k=1`で全ての許容文脈を列挙し、代入可能性を確認した。ただしこれはすべての`q,k,f`の計算証明ではない。

`cor:trivial-exact`の**数理内容**は上記と`thm:data-from-typed-thickness`から従う。ただし行1724–1729の英文の`and`/`or`の括弧が曖昧で、ランク2の必要性が二文字の場合にも掛かると読み取れるよう直すべきである（R6-3）。

### R3.5 定理C：三文字族と擬多様体

`G_n`には各レベルで`bE_{i−1}E_{i−1}b`と`cE_{i−1}c`の二規則があり、`c`を含まない成功導出は一つしかない。従って`W_n`は唯一の`U₁`型`1`の語で、長さは`|W_n|=2|W_{n−1}|+2=3·2^n−2`。`‖G_n‖=13n+7`、最長の規則厚さ`4n`も逐次計数と一致した。全型削除で`L_n\{W_n}`が同じクラスに残れば、どの**クラス全体を扱える**set-driven演算子も`W_n`を含むサンプルを必要とする。

問題は`L_n`自体が型付けなしでもClark–Eyraud代入可能であること。その証明は付録Fの決定的スタック機械を通す。`E_i`の各遷移で重みが厳密に下がること、同じ終了スタックへ至る二つの読みの交換から分布一致が出ることを追った。**全深さでのreachable stack上のpartial injectionの証明を独立に完全再構成したとは言えない**。そのため「一部確かめた」とした。有限集合`L_1,L_2,L_3`に含まれる全語について、1穴の全許容文脈を列挙したところ反例なしであった。付録Fの中心補題は、読者のために開く遷移と閉じる遷移の像がreachable stack上で交わらないことを、末尾frameの形で一覧化するといっそう査読可能になる。

その補題が成立する場合、`V⊄LG ⇒ U₁∈V`（擬多様体は部分半群で閉じる）から指数下界へ進む定理Cの量化は正しい。反対方向もAから直ちに従う。これが**擬多様体に関する**必要十分条件であることを強調する。

### R3.6 §8：power transferと非持ち上がり

`lem:power-transfer`は正しく定式化されている。`s(u)^{i+q}=s(u)^i`という周期性により`u^a`と`u^{a+d}`、`u^{d+b}`と`u^b`の型が一致し、元の長い冪から作る共通2穴文脈`p'□₁u□₂q'`は**穴の間に非空の`u`**を持つ。従って2-代入可能性から異なる外部許容文脈への転送ができる。

`thm:doubling-no-lift`では、最初の`u`の前と第二の`h(W_{n-1})`の最初の`u`の前の`v`冪の指数を`d`だけ左右に移す。`w_M`に最初の`u`が含まれるので非空条件を満たす。転送は`v`の個数を変えないためParikhベクトルを保ち、同じ型を保つ。`u,v,w`の字母が互いに交わらない条件が、転送後に最初の`u`の位置が変わった事実を確実に検出するために用いられている。小例`n=6`でも確認した。

従って「その族とletter-disjoint imagesは全ての固定型付けで、十分大きな`n`についてfan-out 2の標的にならない」「同じ型の語が少なくとも二つ存在する」は支持される。しかし「fan-out 2では稀な型による指数下界が存在しない」「全ての長語に短い同型代表がある」は**証明していない**。原稿の§8末尾はこれを明示しており、妥当である。

### R3.7 稀な型、分布代表、4つの定義の細部

- **稀な型**（`prop:rare-type`）：`L\s^{-1}(m)`は型の逆像という正則言語での交差によりクラス内に残る。二つの標的を同じ有限入力で同時に特徴づけることは不可能なので、その型の語を少なくとも一つ含める必要がある。`Σ_m(μ_m+1)`という下界は、異なる型の語が互いに重複しないことによって加法的に成立する。空語の1単位も別に計上している。
- **同値代表**（`cor:distribution-representatives`）：代表`ι(X)`は非終端`X`から生成される必要がないが、分布同値性により`χ(X)[ι(X)]∈L`となる。Compの子を一つずつ交換する`lem:witnessed-composition`が必要な帰結を供給している。`τ≤t_typ`は正しいが、これは`τ`を直接多項式に抑える定理ではない。
- **許容文脈の内部分離**：`v_1,…,v_{d−1}∈Σ⁺`が必須で、`lem:filling-identity`の非空性は**goodのnonmerging**と非空の子tupleに依存している。これをゼロ長区切りへ緩めると同じ証明は成立しない。
- **reduced good**：`reduced`は全非終端の到達可能性と生産性、`good`はλ-free・nondeleting・nonpermuting・nonmergingを意味する。上界はこの形の与えられたGに相対的で、正規化前の任意のGの厚さに直接移せない。原稿はここを明示している。
- **厚さ`θ̄_G`**：規則が使われる**成功導出の全文長の最小値**の規則間最大（1で下から切る）であり、単なる規則の右辺長や非終端の最短yieldではない。この定義が§4–7で一貫している。
- **`\mathcal B`と`\mathcal B^{≤r}`**：前者は入力サンプル長`‖K‖₊`をランクcapとする演算子、後者は固定rank capを持つ多項式時間構成。上界は共通のcharacteristic sampleを与える一方、固定多項式実行時間の議論は後者である。表2は概ね正しく区別している。

### R3.8 **明確な形式的不一致：Corollary `cor:iptd`**

**箇所**：§7の`cor:iptd`直前と本文、行1870–1923。原稿は、標的のrepresentation class `R`を「`L\{ε}`の**reduced good** fan-out≤f、rank≤r文法と空語ビット」とする。一方、`cor:iptd(i)`は「operator `\mathcal B^{≤r}_{f,s}` identifies … in polynomial time and thick data」と述べ、直後に「その仮説はreducedやgoodでなくてもよい」と注記する。

ここに形式上の問題がある。Eyraud–Heinz–Yoshinaka (2016), **Definition 2.12** でのIPTtDは、入力サンプルに対してアルゴリズムが**`H∈R`を返す**ことを条件にしている。ところが、例えば`f=1`、自明な型付け、`K={ε,a}`では、定義`def:reconstruction`の生の出力`\mathcal B^{≤r}(K)`はスタート規則`\widehat S→ε`を含む。その文法自体はλ-freeでなく、指定された「`L\{ε}`のgood文法＋空語ビット」という形でもない。従って**アルゴリズムとRを現行どおり固定した場合、引用した定義を満たすという証明は存在しない**。

これは中心定理A・B・Cの長さ不等式の反例ではなく、**派生する学習概念の定義への接続の不備**である。しかも簡単に直せる可能性が高い。

**具体的修復案**：アルゴリズムの仮説を`(G_K^+,[ε∈K])`とし、`G_K^+`を`\mathcal B^{≤r}(K)`から`\widehat S→ε`だけ除いた非空語用文法と定める。残りのConst, Comp, Link, Start規則はgoodであり、各非終端`[x]`はConstでproductiveである。さらに`[x]∈Obs_d(K)`は、観測語`w∈K`の1つのoccurrenceから得たものなので、内部の固定区切りが非空なテンプレート`ρ_x`により、`\widehat S→[(w)]→ρ_x([x])`という**rank 1のComp規則**でreachableになる。ゆえに`K`が正の語を含めば`G_K^+`はreduced goodである。`K⊆{ε}`に対しては空言語の専用表現をRに追加する。これらを補題として明記し、仮説表現の符号化・実行時間・一貫性を示せば、厳密なIPTtD主張を回復できるはずである。

著者がこの追加証明を行わないなら、少なくとも「IPTtD」ではなく、**標的のreduced good表示に対するデータ評価を持ち、一般MCFGを仮説にする弱いvariant**として主張を言い換える必要がある。現行の「Definition 2.12 requires …; ours are arbitrary MCFGs」という注記だけでは差異が解消されない。

### R3.9 その他の境界・未確認事項

- `thm:lg-characterization`が依拠するAlmeida–Margolis–Steinberg–Volkov (2009)の命題とRees表示の全境界事例を、個別原著の出版版に対して行単位で突合してはいない。原稿内の使用法に直ちに不整合は見当たらない。
- `prop:good-normalization`では複数の正規化の結合が前提となる。証明のサイズ係数は妥当だが、先行研究の変換の詳細を再実装していないので、元の表現とtargetとの全同値性は「一部確かめた」に留めた。
- 非可換owner lemmaの巨大な定数は十分条件を保証するためのもので、最適性は示されていない。**数値実験が小さな例で成功したことから一般の定理を証明済みと認定していない**。
- `‖G‖`と`θ̄_G`の平方因子のギャップは現稿の「既知の上界・下界間の未解決の差」であって、直ちに二次上界が最適だという主張ではない。§9の記述は適切。

### R3.10 Python 3標準ライブラリによる実験的照合

以下は**実際に実行した**スクリプトである。`substitutable`は有限言語の全ての非空tuple occurrenceと全ての**穴間が非空な**文脈を列挙し、共通の受理文脈を持つtupleの全分布が一致するかを比較する。`doubling`は`n≤3`を完全列挙、`markers`は`q=2,k=1,f=1,2`を完全列挙した。`power_transfer`は`n=6`の具体構成、`S₃`は付録Aの2行積を計算した。値が`True`でも一般の証明にはならない。

```python
from collections import defaultdict
from itertools import combinations

def doubling(n):
    langs = [{'a'}]
    for _ in range(n):
        prev = langs[-1]
        langs.append({'b' + x + y + 'b' for x in prev for y in prev}
                     | {'c' + x + 'c' for x in prev})
    return langs[-1]

def subs_check(words, f):
    dist = defaultdict(set)
    shared = defaultdict(set)
    for w in words:
        N = len(w)
        for d in range(1, f + 1):
            for cuts in combinations(range(N + 1), 2 * d):
                if any(cuts[2*j] == cuts[2*j + 1] for j in range(d)):
                    continue
                # Each internal fixed gap must be nonempty.
                if any(cuts[2*j + 1] == cuts[2*j + 2] for j in range(d - 1)):
                    continue
                tup = tuple(w[cuts[2*j]:cuts[2*j+1]] for j in range(d))
                ctx = tuple([w[:cuts[0]]] +
                            [w[cuts[2*j+1]:cuts[2*j+2]] for j in range(d-1)] +
                            [w[cuts[-1]:]])
                key = (d, tup)
                ck = (d, ctx)
                dist[key].add(ck)
                shared[ck].add(key)
    for ck, xs in shared.items():
        if len(xs) >= 2:
            first = next(iter(xs))
            for other in xs:
                if dist[first] != dist[other]:
                    return False, (ck, first, other)
    return True, (len(dist), len(shared))

def marker_words(q, k, f):
    # Represent each distinct alphabet letter as a distinct single Unicode char.
    a = [chr(0x400 + j) for j in range(2*f)]
    d = [chr(0x500 + j) for j in range(2*f)]
    z = chr(0x600)
    return {''.join(a[j]*i+d[j] for j in range(2*f)) + z*(2*f*(q-i)+2**k)
            for i in range(q+1)}

for n in (1, 2, 3):
    words = doubling(n)
    ok, info = subs_check(words, 1)
    word = 'a'
    for _ in range(n):
        word = 'b' + word + word + 'b'
    print('doubling', n, 'words', len(words), 'max_length', len(word),
          'substitutable_1', ok, 'detail', info)
for f in (1, 2):
    words = marker_words(2, 1, f)
    ok, info = subs_check(words, f)
    print('markers', 'f', f, 'q', 2, 'words', len(words),
          'length', len(next(iter(words))), 'substitutable', ok, 'detail', info)

n = 6
w5 = 'a'
for _ in range(n - 1):
    w5 = 'b' + w5 + w5 + 'b'
w6 = 'b' + w5 + w5 + 'b'
a, d, b = 1, 1, n-3
second_a = 1 + len(w5) + (n-1)
pre = w6[:1]
mid = w6[1+a:second_a-(d+b)]
suf = w6[second_a:]
assert mid and 'a' in mid
assert w6 == pre + 'b'*a + mid + 'b'*(d+b) + suf
moved = pre + 'b'*(a+d) + mid + 'b'*b + suf
assert moved != w6
assert sorted(moved) == sorted(w6)
assert ('c' in moved) == ('c' in w6)
print('power_transfer', 'n', n, 'same_Parikh', sorted(moved)==sorted(w6),
      'distinct', moved!=w6, 'length', len(w6))

# Appendix A's S3 example, with multiplication by permutation composition.
def mul(x, y):
    return tuple(x[y[i]] for i in range(3))
def prod(xs):
    z = (0, 1, 2)
    for x in xs:
        z = mul(z, x)
    return z
one = (0, 1, 2)
alpha = (1, 0, 2)
beta = (0, 2, 1)
up = [beta, one, prod([alpha,beta,alpha,beta])]
vp = [one, one, one]
wp = [one, prod([beta,alpha,beta]), alpha]
row1_before = prod([beta,beta,alpha,beta,beta,alpha,beta,beta])
row1_after = prod([up[0],beta,vp[0],alpha,up[1],beta,vp[1],alpha,up[2],beta,vp[2]])
row2_before = prod([one,beta,one,beta,one])
row2_after = prod([wp[2],beta,wp[1],beta,wp[0]])
print('S3_example', 'original', row1_before, row2_before,
      'replacement', row1_after, row2_after,
      'preserved', row1_before==row1_after and row2_before==row2_after)
```

**実測出力**（`python3 checks.py`）：

```text
doubling 1 words 2 max_length 4 substitutable_1 True detail (12, 15)
doubling 2 words 6 max_length 10 substitutable_1 True detail (93, 172)
doubling 3 words 42 max_length 22 substitutable_1 True detail (1845, 3778)
markers f 1 q 2 words 3 length 8 substitutable True detail (60, 97)
markers f 2 q 2 words 3 length 14 substitutable True detail (2208, 3306)
power_transfer n 6 same_Parikh True distinct True length 190
S3_example original (0, 1, 2) (0, 1, 2) replacement (0, 1, 2) (0, 1, 2) preserved True
```

`detail (a,b)`は分布辞書に現れたtupleと許容文脈の個数である。これはモデルの正しい量化を試験する計算であり、入力以外の未計算の出力を補っていない。

## R4. 主張の範囲と新しい文章の監査

| 箇所 | 判定 | 修正または留意点 |
|---|---|---|
| 要旨（行71–99） | **要修正** | 行80–81の`local groups are the boundary`は`at fan-out one`を同じ文に置くべき。行92–94の`for every set-driven learner`は定理より広く、`for every set-driven operator admitting characteristic samples throughout the class`などに限定する。 |
| 序論のTheorem A（157–163） | **適切** | `f, r_max, Σ, s`を固定し、`reduced good`に相対化している。`∀f`と定数依存を混同しないこと。 |
| 序論のTheorem B（164–179） | **適切** | `4f+1`字母、`f=1`では2字母、rank2、class-wide下界という条件が維持されている。 |
| 序論のTheorem C（180–197） | **概ね適切** | 必要十分は**擬多様体についての**定理であることが明記されている。個別型付けを分類していない。 |
| `The remaining question`（約198–211） | **適切** | `f≥2`のLG必要性は開いている。§8が与えるのは特定族の不適合だけ。 |
| 表1（283–343） | **概ね適切** | LGの古典的特徴付けと本稿の新しい長さ上界を明確に区別できれば、さらに誤読を防げる。 |
| 表2（345–395） | **適切** | 上界のcanonical演算子、下界のclass-wide、字母条件、`f=1`のrank条件を概ね忠実に整理。特に`B`と`B^{≤r}`を明示したのは良い。 |
| `rem:fanout-one-data`（1850–1878） | **概ね適切** | (b)の`the answer depends on which words realize...`は個別型付けでの**依存性が証明された**ように読ませる。`The individual-typing boundary is not characterized here`で止めると厳密。 |
| §8冒頭・末尾（1924–1999） | **適切** | 元族とletter-disjoint imagesについて、2穴許容性を用いた除外だけを主張している。稀な型一般の不可能性は主張していない。 |
| 結論とopen problem（2000–2069） | **適切／軽い整文** | 下界の字母条件と未解決性は維持。`Open Problems`の複数形より単数形が自然。 |
| Corollary `cor:iptd`（1879–1923） | **形式的不備** | 指定Rへ仮説を出すというIPTtD定義の条件を実装してから名付ける必要がある。 |

**要旨の具体的な反例的読み**：`for every set-driven learner`を「全てのset-driven operator」と文字どおり解すると偽である。固定した`n`に対し、任意の入力`K`へ常に`G_n`を出すset-driven operatorを考えれば、標的`L_n`の特徴サンプルは**空集合**で済む。ただしこの演算子は`Cmcf(1,s_U)`の他の標的についてcharacteristic sampleを持たない。したがって、実際の下界に必要な**クラス全体での特性**を必ず書く必要がある。これは定理Cそのものの反例ではない。

## R5. 書き方と構成

### 構成

約41ページ、付録A–Gという規模はTCSに対して長めだが、非可換群の順序抽出、LGのRees座標、三文字族のスタック解析、全ファンアウト下界の独立証明をそれぞれ省略するのは望ましくない。**今回の一点集中版へ削った方針は支持する**。削除前の59ページ版から追加の主定理を戻す根拠は見当たらない。

具体的には、付録A（群ブロック選択）とB（順序均質化）を一つの付録にまとめて「group replacement lemma → order homogenization → interval lemma」の依存関係を冒頭の図で示してもよい。付録C（LG座標とbuffer）は核なので維持する。付録D・E（定性的再構成・witness補助・正規化）は、質的な定理が既知だという本稿の位置付けに沿って、見出しを一段縮小して連結できる。付録F（倍増族のスタック証明）とG（全ファンアウト下界）は独立性が強く**残すべき**。無理に本文へ長い証明を戻す必要はない。

一方、§7のIPTtD帰結に対応する**出力形式の補題**は、本文のcorollary直前に移すか、本文で明確に参照できるようにすべきである。これは見せ方でなく定義上の欠落に対する修正である。

### 記号と定義の順序

初見の読者には`f`（fan-out）、`r`（rank）、`s`と`ŝ`（positive vs fresh-completed）、`λ`（補助モノイド型）、`t_G`・`θ_G`・`θ̄_G`・`t_typ`・`τ`（厚さ・代表長）、`\mathcal B_{f,s}`・`\mathcal B^{≤r}_{f,s}`が密集する。§2終了時に**1つの記号表**を置くと読みやすい。特に「元の文法Gのrule thickness」「型付き精密化の厚さ」「分布同値代表の最短長」を同一視しない表がほしい。

`good`のnonmergingは、穴間の非空条件を保証するための技術的要請であり、単なる正規形の趣味ではない。§2で定義した直後に`lem:filling-identity`を一文で予告するのが有益である。`reduced`がサイズ下界とθの定義に必要な点も明記するとよい。

### 英語・体裁の局所修正

- **Abstract（80–81）**：`local groups are the boundary` → `at fan-out one, local groups give the exact pseudovariety boundary; at higher fan-out they give a sufficient condition`。
- **Abstract（92–94）**：`for every set-driven learner` → `for any set-driven reconstruction operator admitting characteristic samples throughout the fixed-typing class`。
- **§7 `cor:trivial-exact`（1725–1729）**：`if r_max≥2 and (|Σ|≥4f+1 or (f=1 and |Σ|≥2))` と括る。
- **§7 `rem:fanout-one-data` (b)**：`depends on which words realize ...`は理由が予告されるだけなので、個別型付けの分類は未解決／本稿では扱わない、と断定を控える。
- **§9見出し**：`Conclusion and Open Problems` → `Conclusion and an Open Problem`（好みの範囲）。
- `positive-data identification`と`identification in polynomial time and thick data`は異なる保証である。Gold収束段階まで多項式と読ませないという既存の注記は維持する。

## R6. 著者に求める修正

### 必須の修正

1. **[R6-M1：IPTtDの厳密な表現クラス条件を解消]**  §7 `cor:iptd`（行1879–1923）と`def:reconstruction`（791–824）。引用するDefinition 2.12の`H∈R`と、現行アルゴリズムの出力の関係を形式的に証明すること。推奨は、`\mathcal B^{≤r}(K)`から空語規則を除いて`G_K^+`とし、空語ビットを添えた仮説を出すこと。全ての観測非終端がrank1のCompで到達可能でありConstで生産的であるという短い補題、`K⊆{ε}`の空正言語の特別扱い、計算時間と一貫性を明記する。これを行わないなら、CorollaryのIPTtDという名称と必要十分結論を弱い独自概念へ修正する。
2. **[R6-M2：要旨の量化・境界を限定]**  Abstract（行80–81, 89–98）。`LG is the boundary`の適用範囲を**fan-out 1の擬多様体**に限定する。下界の`every set-driven learner`を、**クラス全体にcharacteristic sampleを持つ演算子**という仮定を含む形にする。本文のTheorem CとTable 2に合わせること。`f≥2`の必要性を解決したように読ませない。
3. **[R6-M3：自明型の下界条件を括弧で固定]**  `cor:trivial-exact`（行1719–1747）の英文を、`r_max≥2`が2字母の場合にも必要であると一意に読める形にする。例えば`If r_max≥2 and (|Σ|≥4f+1, or f=1 and |Σ|≥2), ...`。rank1に下界を拡張したように読ませない。
4. **[R6-M4：三文字族のパーサー単射性を検査可能に]**  Appendix F `lem:app-tl-reachable`・`lem:app-br-branch`（行3074–3159）。reachable stackを列挙する不変条件に基づき、`a/b/c`の各遷移がreachable集合上でpartial injectionであることを、開き遷移と閉じ遷移の像が衝突しないことを含めて場合表に記す。現行証明に反例を見つけたという意味ではないが、これは定理Cの指数下界の**代入可能性**を担う核心なので、外部の計算実験に頼らず査読者が局所的に検査できる形を要求する。

### 望ましい修正

1. **[R6-S1：群の同時置換の証明地図]**  §5.1 `prop:block-replacement-interface`（行1409–1434）、Appendix A–B（2087–2383）に、patternの固定→order homogenization→chunk分解→`P_pQ_p^{-1}`状態衝突の図か短い不変量表を置く。`κ`の左右順序が本質であることを本文でも一行明示する。
2. **[R6-S2：LGの新規性の境界]**  Table 1（283–343）、§5.3（1541–1653）では、`thm:lg-characterization`の半群論的中身を既知の座標表現として、学習論への新規な適用`thm:local-group-polydata`と分けて表記する。
3. **[R6-S3：記号の一覧]**  §2末尾（約700行以降）に、`θ̄_G,t_typ,τ(G,s),μ_m,‖K‖₊`と演算子の二種類を1表で対比する。代表長の`τ`が元の文法厚さを表さないことを注記する。
4. **[R6-S4：Remarkの断定強度]**  `rem:fanout-one-data` (b)（1850–1878）を「個別型付けの必要十分条件は本稿で特徴付けていない」と表現する。個別のword realizationへの依存性を定理として主張したかのようにしない。
5. **[R6-S5：形式と文献]**  約41ページ・付録7本の現在の証明内容は残し、付録A–BやD–Eの見出し統合でナビゲーションを簡潔にする。引用文献の最新版の書誌およびTCSの最新ページ・AI申告方針は、投稿前の最終校正時に別途確認する。

---

## 査読の結語

**中心定理A・B・Cに対する具体的な数学的反例は、この査読では得られていない**。定理Bと§8の主要推論は特に強く支持される。定理Aの非可換群の選択補題と定理Cの任意の深さのパーサー補題は精査したものの完全な独立検証には至らないので、無条件に「証明済み・正しい」と断定しない。今回確認した明確な欠陥は、**IPTtDとの接続における仮説表現クラスの不整合**と、**要旨の量化・ファンアウト範囲を広く読ませる表現**である。両者は、上で提案した限定と補題の追加で修復可能と考える。

TCSへの投稿価値はあるが、提出前に少なくとも**R6-M1〜M4**を処理し、その修正版でも数理上の主張の範囲が維持されていることを再検査するのが適切である。

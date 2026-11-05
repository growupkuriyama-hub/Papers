# 有限半群・擬多様体の所蔵文献と、固定半群型付けMCFG論文を強化する研究可能性

**調査基準日：2026年11月6日（JST）**  
**対象原稿：** Takayuki Kuriyama, *Distributional Learning of Multiple Context-Free Languages under Fixed Finite-Semigroup Typing: Local Groups and the Length of Characteristic Data*  
**対象GitHubファイル：** `growupkuriyama-hub/Papers/02-v2-lg-fanout-boundary/main.tex`  
**直接取得済み版：** 2026-11-06の査読時にGitHub連携から取得した3,554行、187,705文字、**Git blob `cb27c54a35366ff1f93a94c1d62c68464c2b9cd7`**。この文書はその固定版を扱う。以後のGitHub更新は反映しない。  
**目的：** 「利用可能な原典を明示する」＋「数学的証明の成否に関係なく、原稿を強化する具体的方向と必要になる数学を多数出す」。これは査読済みの新定理集ではなく、**実行可能な研究課題の設計書**である。

## 0. 読み方と主張の強さ

この文書の各項目には次の区別を付ける。

- **[原典確認]** 原典の該当紙面を実際に取り出して確認した既知の記述。典拠として、合本番号・合本PDFページ・原著ページを付記する。
- **[原稿確認]** 2026-11-06固定版 `main.tex` にある定義・定理・式を確認したもの。「原稿にある」ことと「独立に正しいと証明した」ことは異なる。
- **[導出]** 短い説明により、定義や既知結果から従うと考えられる関係。ただし正式採用時には著者による検算が必要。
- **[着想]** 未証明の補題候補、方法、反例探索、論文の拡張方向。成否は保証しない。
- **[危険]** 短い論理では導けない命題や既知の障害。「取り入れる」前に必ず定理条件・反例を調べる。

**重要：** 合本の先頭目次／プロジェクトマスターに載るだけの文献と、本文の関連箇所を読んだ文献を混同しない。以下の「アクセス可」は**PDFの閲覧・文字抽出／ページ表示が可能**という意味であり、各巻の全数千ページを通読・全定理照合したことではない。合本ページは正式な雑誌掲載ページと異なる。2026年10月時点の索引は常に原典そのものに優先しない。作成した研究アイデアも、出典文献の著者が主張したこととして引用してはならない。

## 1. アクセス可能な情報源の厳密な範囲

### 1.1 実ファイルとしてアクセスできる12巻＋独立書籍

プロジェクトに実際に添付された次のPDFを開ける。ページ数はPDF実物から確認した。**12巻合計9,900 PDFページ／延べ原典130エントリ（重複掲載を含む）**。これとは別に**Langの単独参考書940ページ**がある。したがって研究資料PDFの合計は**10,840ページ**。合本の項目ごとの完全索引は**付録I**に載せた。

| ID | 実ファイル | PDF頁 | 収録原典 | この論文への直接性 |
|---|---|---:|---:|---|
| 01 | `01_Foundations_of_Grammatical_Inference_and_Reversibility_v8.pdf` | 907 | 13 | Gold型、characteristic sample、teaching／同定の定義 |
| 02 | `02_Substitutability_and_Positive-Data_Grammar_Learning_v6.pdf` | 186 | 11 | Yoshinaka/Clarkの置換可能性、IPTtD、有限シグネチャ |
| 03 | `03_Multiple_Context-Free_Grammars_Foundations_and_Learning_v9.pdf` | 1,213 | 34 | MCFGの正規化、ランク、LCFRS、動的計画法、2026年のsubstitution lemma |
| 04 | `04_Residual_Structure_Canonical_CFGs_and_Strong_Learning_v3.pdf` | 142 | 7 | 正準性、分布同値代表、strong learningへの分岐 |
| 05 | `05_Syntactic_Concept_Lattices_and_Finite_Algebra_v3.pdf` | 136 | 5 | syntactic semiring／concept lattice、Almeida 2009 |
| 06 | `06_Grammar_Semantics_Categories_and_Factorization_v2.pdf` | 159 | 4 | Tilsonのderived category、代数的分解 |
| 07 | `07_Algebraic_Foundations_of_Automata_Theory_Reference_v11.pdf` | 3,687 | 16 | **擬多様体・LG・Rees・半直積・factorization forest の主力** |
| 08 | `08_Tree_Automata_Techniques_and_Applications_Reference_v2.pdf` | 264 | 1 | 証明の木構造、有限木状態、ボトムアップ処理 |
| 09 | `09_Control_Sets_Pushdown_Automata_and_Typing_Bias_v5.pdf` | 278 | 15 | 制御集合／typing bias／PDA、代替学習形式 |
| 10 | `10_PACn_Higher_Arity_Learning_and_VCn_Theory_v3.pdf` | 333 | 11 | 別学習モデルとの橋渡し。ただし未決着の先行研究に注意 |
| 11 | `11_Plato_Chomsky_Stimulus_Poverty_and_Language_Learning_v1.pdf` | 1,437 | 10 | 博士論文序論への背景。TCS論文の数理証明とは分離 |
| 12 | `12_Finite_Abelian_Groups_Zero_Sum_and_Additive_Theory_v1.pdf` | 1,158 | 3 | Davenport定数、零和・短縮、可換群の厳密評価 |
| LANG | `Algebra-SergeLang-ThirdEdition.pdf` | 940 | 単独書籍1冊 | 群・群環・表現の基礎。有限半群の専門原典の代替ではない |

さらに、別添として、**姉妹論文TCS Round 1合成PDF** `TCS-D-26-00494_R1.pdf`（43頁）、**プロジェクトマスターv17** `project-master-v17-2026-11-04.md`、**2026-11-06査読報告** `chatgpt_tcs_referee_focus_2026-11-06.md`、ユーザー提供の査読依頼Markdownを読める。これらは**一次数学文献として130本に加算しない**。GitHubの当該 `main.tex` は前述のblobで全行を参照済み。プライベート `Research-Library` の**未添付・未取得の個別ファイル**まで閲覧済みと主張しない。

### 1.2 擬多様体・半群論として特に重要な実物18エントリ

| 優先 | 著者・文献 | 所蔵箇所（PDFの1始まり） | 今回の用途／確認度 |
|---|---|---|---|
| A+ | Almeida–Margolis–Steinberg–Volkov (2009), *Representation Theory of Finite Semigroups...*（正式TAMS版） | **07: 3655–3687**, 同一版 **05: 104–136** | **Prop. 2.3 を原著p.1434＝07 p.3660で本文確認**。LG↔2元半束非包含↔極小イデアルへの冪到達 |
| A+ | Almeida (1994), *Finite Semigroups and Universal Algebra* | **07: 3138–3654** | 擬多様体、擬恒等式、自由プロ有限構造、join・半直積。**画像主体の書籍で本文OCRを全章取得したわけではない** |
| A+ | Straubing (1985), *Finite Semigroup Varieties of the Form V * D* | **07: 2008–2049** | Delay、局所的構造を窓／半直積へ移す道具。本文一部確認 |
| A+ | Tilson (1987), *Categories as Algebra* | **06: 21–136** | derived category／半直積の抽象化。目次・収録を確認、全定理は未再証明 |
| A | Howie (1995), *Fundamentals of Semigroup Theory* | **07: 2050–2410** | Green関係、極小イデアル、完全単純半群、Rees行列 |
| A | Pin (1986), *Varieties of Formal Languages* | **07: 2411–2553** | Eilenberg対応、半群像、擬多様体、学習のtypingとの既知の接点 |
| A | Pin (2025), *Mathematical Foundations of Automata Theory* | **07: 2–345** | 代数的オートマトン理論と語の因子分解、最新の体系的概説 |
| A | Costa (2002), *Some Pseudovariety Joins Involving Locally Trivial Semigroups* | **07: 1950–1964** | **本文冒頭と§2.1を確認**。`LI∨V`、擬恒等式、joinの制約 |
| A | Costa (2002), *Some Pseudovariety Joins Involving Locally Trivial Semigroups and Groups* | **07: 1965–1970** | **本文冒頭を確認**。`LI∨H∨V`、`DO`など |
| A | Simon (1990), *Factorization Forests of Finite Height* | **07: 1920–1949** | 有限半群の冪と木の高さを抑える道具。主定理の代替としては未検証 |
| B | Eilenberg (1976), *Automata, Languages, and Machines*, Vol. B | **07: 2735–3137** | 有限半群とvariety、形式言語との対応 |
| B | Eilenberg (1974), Vol. A | **07: 347–815** | 基礎理論；p.346は原著ではなく編集注記 |
| B | Pin (1997), *Syntactic Semigroups* | **07: 816–892** | 認識モルフィズム・合成・型選択 |
| B | Almeida et al. (2007) 旧著者稿 | **07: 1971–2007**／**05: 12–48** | 2009刊行版との版差確認用。**正式引用は2009版を優先** |
| B | Polák (2001), *Syntactic Semiring of a Language* | **05: 2–11** | 置換の観測を通常のsyntactic monoidより多値的に整理する方向 |
| B | Clark (2013), *The Syntactic Concept Lattice...* | **05: 49–75** | tuple distributionの同値／概念束と有限型への接続 |
| B | Kuznetsov (2025), *On Syntactic Concept Lattice Models...* | **05: 76–103** | 代数的文法意味論への別方向；本稿への直接性は低い |
| B | Knuth (1968), *Semantics of Context-Free Languages* | **06: 2–20** | 半環重み／導出評価、証拠長の最適化プログラム |

**版と引用の重要な注意：** 2009年のAlmeida論文は *Transactions of the American Mathematical Society* **361(3):1429–1461**、DOI `10.1090/S0002-9947-08-04712-0`。合本07の **3655–3687** が出版社組版版、1971–2007は2007年著者稿。証明を引用するとき「合本07 p.3660」ではなく、論文の原著 **p.1434、Proposition 2.3** を記す。

### 1.3 重要な文献の『何を実際に確認したか』

1. **[原典確認] Almeida et al. (2009), Prop. 2.3**：有限半群がlocal groupであること、ある冪が単純半群／極小イデアルになること、2元半束`{0,1}`を含まないことが同値。**有限半群S自体について**の命題であり、特徴データ長に言及しない。
2. **[原典確認] Costa (2002) 2文献の冒頭**：`LI∨V`と`LI∨H∨V`、擬恒等式に基づくjoinの研究を扱う。論文の`LI∨Grp`対`LG`の比較に有用だが、`LG = LI∨Grp`とは主張していない（現原稿では真に包含）。
3. **[原稿確認] #2現行原稿**：定理A `O(‖G‖² θ̄_G)`、定理B `Ω(‖G‖ θ̄_G)`、定理C `f=1`の擬多様体境界`LG`、§8の非持ち上がり、`f≥2`の未解決性を確認した。
4. **[原稿確認] #2付録A–B**：非可換群のowner-wise同時置換には`c_{G,f}`、アーベル群にはDavenport定数`d(G^f)`を使う。下記の数表は、**原稿の式へ数値を代入した**もので、新たな上界を証明したわけではない。
5. **[目次確認] その他の文献**：各PDFの巻頭目次・プロジェクトマスター索引でアクセス可能な論文、ページ、版を確認。**未閲読の本文に特定の定理があると断定しない**。特にAlmeida(1994)の画像主体ページ、Langの個別定理、Gallotの学位論文、Kallmeyerの各補題は必要箇所をこれから個別照合する。

## 2. 数学的出発点と、改善が数値で何を意味するか

記号を固定する。`f` はファンアウト上限、`r` は規則rank上限、`N=‖G‖` は reduced good grammar のシンボルサイズ、`T=θ̄_G` は規則厚さ、`s:Σ⁺→S` は**標的によらず固定した**有限半群typing、`m=|S|`。

現行の代表的な評価は

\[
\operatorname{cs}_{f,s}(L)\ \le\ C_{f,r,s,\Sigma}\,N^2T\quad (S\in\mathbf{LG}),
\]

そして、字母数等の条件の下である有限言語族には

\[
\operatorname{cs}_{f,s}(L)\ \ge\ c_{f,s,\Sigma}\,NT.
\]

この**`N` 1因子**が残る。自明typingなら既に `Θ(NT)` が達成される（現行原稿 `cor:trivial-exact`）。したがって将来の改善候補を明確に分ける。

- **境界の完成**：`f≥2`でも、非LGの擬多様体が一様多項式特徴データ性を持たないと示す／逆に、ある非LGが持つと示す。
- **指数の鋭化**：`N²T→NT` または `N^{1+ε}T`、あるいは`N T·polylog(N)`。
- **固定定数の鋭化**：式の多項式次数は同じでも、非可換群と多成分の短縮に使う天文学的な閾値を現実的にする。
- **学習概念の正確化**：形式定義どおりのIPTtDと、現在の仮説クラスの齟齬を埋める。
- **別の情報量**：encoded word length、sample cardinality、Gold convergence stage、teaching dimension、compressed sample、PAC sample complexityは**別指標**として区別する。

### 2.1 具体的な既存の数値例

現行の三文字倍増族は `‖G_n‖=13n+7`, `θ̄_{G_n}=4n`, 強制される最長語 `|W_n|=3·2^n−2`, 正例サンプルの長さ下界 `3·2^n−1`。

| n | `‖G_n‖` | `θ̄_G` | `|W_n|` | 最小データ下界 |
|---:|---:|---:|---:|---:|
| 4 | 59 | 16 | 46 | 47 |
| 6 | 85 | 24 | 190 | 191 |
| 10 | 137 | 40 | 3,070 | 3,071 |
| 20 | 267 | 80 | 3,145,726 | 3,145,727 |

**重要な限定：** この例は`f=1`に使われる。現行§8は、**十分大きなnではこの族をf=2の下界にそのまま使えない**ことを示す。`L_n`を「fan-out 2でも指数下界の例」と扱ってはならない。

### 2.2 非可換ブロック短縮の現行閾値

原稿の定義：

\[
\mathcal P_f=f^{f+1}f!,\qquad Q_{H,f}=\max(3,|H|^f),\quad
M_{H,f}=\mathcal P_f Q_{H,f}^{2^{f^2}},\quad
c_{H,f}=M_{H,f}-1\quad(H\text{ 非可換}).
\]

`H=S₃`（位数6）を例に計算すると：

| f | `P_f` | `Q_{S3,f}` | `M_{S3,f}` | 大きさ |
|---:|---:|---:|---|---|
| 1 | 1 | 6 | `6²=36` | 36 |
| 2 | 16 | 36 | `16·36^16` | **127,338,577,759,142,414,150,270,976 ≈ 1.27×10²⁶** |
| 3 | 486 | 216 | `486·216^512` | 約 **10^1197.93** |

`f=3`の数字は**定理の真偽を疑わせる反例ではなく、証明で使うRamsey型抽出の定数が非常に粗い**という研究機会である。一方、可換 `H=C₂` なら `d(C₂^f)=f`、つまり `f=1,2,3` で `1,2,3` と桁違いに小さい。

---

## 3. A群：すぐ本文・付録を強くできる、代数的な補強（11案）

### A01. LGを単一の擬恒等式で提示する

- **[導出] 候補式**：有限半群について

  `S∈LG ⇔ (x^ω y x^ω)^ω = x^ω` （全ての`x,y`について）。
- **理由**：`e=x^ω`は冪等元。`eSe`は単位元`e`を持つ有限モノイドなので、全`z∈eSe`について`z^ω=e`であることと、各`z`が可逆であることが同値。任意の冪等元は`x=e`として得られる。
- **参照**：07-16 Almeida (1994)、07-17 Almeida et al. (2009) Prop.2.3、07-13 Pin (1986)。
- **原稿内の位置**：`thm:lg-characterization`の直後、または導入で1段落。全擬多様体読者向けに境界の*algebraic syntax*を明確化。
- **数値**：有限半群`m`個の元素の乗法表が与えられれば、各`x,y`（最大`m²`組）の冪を計算して確認できる。容易な素朴実装で`O(m⁴)`程度を上界とする検査器を設計可能（計算量は実装方式に依存）。
- **注意**：**既知の代数的特徴づけを新規定理として売らない**。導出を短い注記とする。

### A02. 「禁止される最小半群はU₁」という境界図を作る

- **[原典確認]** Almeida et al. (2009), Prop.2.3：`S∉LG`なら`U₁≤S`、擬多様体`V⊄LG`なら`U₁∈V`。
- **[着想] 図式**：`S∈LG → 短代表 → 多項式データ` 対 `V⊄LG → U₁∈V → f=1で指数データ`、真ん中に`f≥2`の未決着を置く。
- **用途**：定理Cの量化「**個別のtypingではなく擬多様体についての必要十分条件**」を一目で伝える。1ページも不要。

### A03. 局所群の遅延を`k=|S|`から最小の`d(S)`へ置き換える

- **[着想／強い補題候補]** `K`を極小イデアルとして `d(S)=min{k≥1:S^k=K}` と置く。LGならAlmeida Prop.2.3により`d(S)`は有限で、原稿の議論では`d(S)≤|S|`が利用可能。
- **仮説**：`lem:lg-rees-window-coordinate`の証明に必要なのは「長さ`k`の積がKに入ること」であり、`k=|S|`であること自体ではない。したがって`k=d(S)`にできるか検証する。
- **数値的効果**：buffer lemmaの係数`4kf+1`が`4d(S)f+1`へ。仮に`|S|=30, d(S)=3, f=2`なら`241→25`、約**9.64倍**の改善。windowの状態数はさらに指数的に下がり得る。
- **検査箇所**：sliding-factor `ν` の長さ`k+1`、Rees行列のprefix/suffix k文字、短語の判定`|w|<2k`。
- **危険**：`S^k=K`を一部の語にしか言えないなら失敗する。必ず**全ての長さkの積**で検査する。

### A04. 最小イデアル`K=M(H;I,Λ;P)`から最小群Hを抽出する

- **[着想]** Rees表現に現れる最大部分群`H`が大きくても、型付けから現れるsliding-factorラベル `ν(Σ^{k+1})` と境界の結合元が生成する小さな群`H_eff`で足りないか検討する。
- **数値**：もし`|H|=24`を`|H_eff|=4`に減らせれば、`f=2`の`Q=|H|²`が`576→16`（ただし下限3）、`Q^16`は**36^16倍**変わる。実際の生成部分群で座標計算が閉じることが必須。
- **参照**：07-12 Howie、07-17 Almeida、Lang XVIII。

### A05. `LI∨Grp ⊊ LG` の差を自動機による具体例で見せる

- **[原稿確認]** 現行`prop:li-g-strict`は文字列中の`ab`出現回数の偶奇を記録する`λ_{1,ν}`を例示する。
- **着想**：2文字アルファベット上、長さ`k+1=2`の滑動因子のみで記録できる非自明な群型を、状態図（直前文字×parity）で提示。
- **具体例**：`b^m a^N b^m`と`b^{2m}`は適切な`m,N`で全ての固定prefix/suffix窓と任意の固定**文字ごとの群準同型**値を一致させられるが、`ab`の出現偶奇はそれぞれ`1,0`。
- **作用**：「CFG姉妹論文の`LI∨Grp`から、真に広い`LG`へ」が読者に通じる。図は本文の定理数を増やさない。

### A06. 古典理論と新しい短縮を完全に切り分ける

- **既知**：LGのRees表示、`LG=Grp*D`という構造面、U₁排除（07-11 Straubing、06-02 Tilson、07-17 Almeida）。
- **新しいと主張する核**：これらを**複数成分が交錯するMCFG導出**へ適用し、群値の**順序付き**同時置換を用いて `O(N²T)` を示すこと。
- **変更案**：`thm:lg-characterization`を「classical equivalence plus explicit coordinates」、`thm:local-group-polydata`を「new quantitative statement」と別ラベルにする。先行研究誤認リスクを下げる。

### A07. 有限半群の`LG`判定・`U₁`証拠抽出を付録の実装仕様にする

- **[導出]** 冪等元集合`E(S)={e:e²=e}`を計算。各`e`について集合`eSe`を作り、単位元`e`に対してすべてが逆元を持つかチェックする。
- **決定手続き候補**：`m`×`m`の乗法表入力→局所モノイドの検査、違反なら冪等元`e`と別の冪等元`f`から`ef=fe=f`となる`U₁`を抽出する。
- **目安**：`m=2..6`の小半群列挙、`LG`と擬恒等式・Prop.2.3の三通りの判定一致をチェック。**反例探索器と同時に代数的健全性チェック**となる。
- **注意**：実際に検査した全半群数と同型削減の仕様が必要。ここでは未実施。

### A08. joinと半直積の違いを具体化する

- **現行**：`LI∨Grp`は`LI×Grp`型の有限積の部分・商として説明され、`LG`とは真に異なる。
- **[着想]** Costaの`LI∨V`とStraubingの`V*D`を並べ、`join`、`semidirect product`、`Mal'cev product`が同一演算ではないことを1表で明記。LGの上界の数学的由来が整理される。
- **危険**：`LI∨Grp=LG`、`LI∨Grp=Grp*D`などと勝手に同一視しない。

### A09. Fresh identity completionを代数的に強調する

- **[原稿確認]** `s:Σ⁺→S`のpositive imageにLG条件を課す。空語用の`s^♯`は既存の単位元とは**異なる新しい単位元**を付加する。
- **重要な反例**：`S`が単位元を持つ有限群なら、`S^♯`には元の群単位元`e`と新単位元`1_♯`があり、`e·1_♯=1_♯·e=e`。この2つは**U₁**をなすので、`S^♯∉LG`でも`S∈LG`。
- **用途**：定理Aの正の像条件が「不自然な制限」ではなく**本質的な型付け上の分離**であることを、2元の図で説明。

### A10. 原典の最小イデアル同値を定理の代数部分へ正確に引用

- **[原典確認]** Almeida et al.（2009）p.1434 Prop.2.3は`S^n`が極小イデアルであることも述べる。現行付録の「すべての冪等元がKにある」という中間条件は、証明で使う導出であってProp.2.3の箇条書きそのものではない。
- **変更案**：引用と自己証明の境界を脚注で明記し、Rees座標`i, a, λ`は著者側で展開したことを区別する。

### A11. 局所群以外にも十分条件を与える際は「型写像の実像」を使う

- **[着想]** `S`の大きなambient半群が非LGでも、`s(Σ⁺)`という**実際の正の像**がLGなら現行定理Aは適用できる。条件はcodomainのラベルではなく、surjective corestrictionで決まる。
- **提案**：実例で「ambient 8元半群に写しているが実像は4元群」といった場合に、4元側の定数を用いる小補題を明記。現在の定義との整合確認だけで済む可能性が高い。

---

## 4. B群：特徴データ長の上界を鋭くする（10案）

### B01. 最大の課題：`O(N²T)→O(NT)`

- **[着想]** 現行証明の`N`は型付きnonterminal/ruleの**証拠語数**、もう一つの`N`は短い型付き代表を得るまでの**導出路のラベル種類数**。別々に最大化するのが過大評価の候補。
- **目標命題**：固定`f,r,s∈LG`で全`G`に `cs(L)≤C_{f,r,s} NT`。
- **技術案**：各規則のwitnessに必要なrepresentative長を`b_R`とし、一様最大`max_R b_R`ではなく `Σ_R b_R` を直接評価。総量が`O(NT)`になるかを導出DAG共有、amortized chargingで検証。
- **反例候補**：規則数が`Θ(N)`、各規則が互いに異なる`Θ(NT)`の長い同値代表しか持たない言語族。**この候補の構成がなければ「二乗が必要」とは言えない**。
- **出典**：02-06、03-04、03-28〜03-32、現行`lem:witness-length-template`。

### B02. `τ(G,s)`を` t_typ(G,s)`より本質的に短くする

- **[原稿確認]** `cor:distribution-representatives`では、非終端から導出される最短型付きtupleではなく、**同じ分布同値類に属する**もっと短いtupleを使える。
- **既存例**：現行`prop:typed-thickness-exponential`では `G_n`の`N=O(n)`、`T≤2`にもかかわらず`t_typ≥2^n`。しかし言語全体が`{a,c}⁺`なので`τ=1`。
- **[着想]** LGに対し `Σ_X τ_X` を`O(NT)`に抑える「分布代表の全体量補題」を狙う。これは`t_typ`の全体量に二乗分を要しても、実際のcharacteristic dataには不要な可能性を捉える。
- **検証**：同型の複数規則をもつ文法で、`τ_X`が共通代表へ潰れる率を実測する。

### B03. 代表長を「型付き非終端ごと」に近似・計算する

- **[着想]** 固定`f,r,S`で`G×M_{k,ν}^f`の有限装飾文法を作り、各装飾非終端の**最短yield長**をmin-plus型動的計画法で求める。
- **数式**：`D[A,t]=min_R (terminals(R)+Σ_j D[B_j,t_j])`（出力型`t`を満たす子型のみ）。
- **参照**：03-30 Nederhof、03-31 Ramalingam–Reps、03-32 Huang、03-28 Riechert、06-01 Knuth。
- **成果**：現在の粗い理論定数を、**特定文法に対する実測`max D[A,t]`**で置き換えられる。ただし分布同値最短`τ_X`の計算には別の同値判定問題があり、ここでは`t_typ`しか直接計算しない。

### B04. 「到達可能な型ベクトル数」で`|V||M|^f`を置換する

- **[着想]** 現行heavy-node lemmaの路長は`|V||M|^f`で評価するが、実際に導出に現れる `(A, typevector)` の集合の大きさを `R_λ(G)` と置く。
- **期待**：`R_λ(G)≤Σ_A |Types(A)|≤|V||M|^f`、しかも特殊文法では`R_λ(G)≪|V||M|^f`。
- **例**：`|V|=100, |M|=20, f=2`の全上界は`40,000`、各非終端が平均3型しか生成しなければ`R_λ=300`（**約133倍**改善）。
- **利点**：原稿の証明をほぼ保ったままparameterized statementへ進める可能性。

### B05. 非可換群のRamsey抽出定数を削減する

- **[着想]** 現行`f=2, H=S₃`で`M≈1.27×10²⁶`。まず`f=2`専用に、4種類以下のblock-type間順序だけを分類し、完全な`2^{f²}`反復を避ける。
- **候補**：`M_{H,2}≤poly(|H|)`で**次数16未満**、さらに`O(|H|^c)`（`c≤4`など）を目指す。ただし`poly(|H|)`そのものは現行の`f`固定でも既に成立している。**真の改善は次数・定数**。
- **実験**：`H=C₂, S₃, D₈, Q₈`（群要素数2,6,8,8）で`f=2`、owner数`m≤8`、block各1〜2個の配置を列挙し、置換後積保存subsetをSAT/全探索する。
- **停止条件**：小さい`m`で反例があるなら、より強い推測を破棄。

### B06. `f=1`の非可換短縮を専用で導く

- **[導出候補]** ownerが1ブロックしか持たないとき、左から順の置換をprefix product statesで追えば、一般の順序均質化は不要になりそう。
- **現行数値**：`H=S₃, f=1`の一般定数`c=35`に対し、専用の境界状態衝突なら`|H|=6`規模が目標になる。
- **位置づけ**：本稿主眼は`f≥2`なので、独立した新定理としてページを増やすより、付録のケース分け・定数改善に使う。

### B07. 可換群でDavenport定数の厳密値を使う

- **[原稿確認]** `c_{H,f}=d(H^f)`、通常のDavenport定数は`D(H^f)=d(H^f)+1`。
- **[導出]** `H=C_p`なら`H^f=C_p^f`はp群で `d(C_p^f)=f(p−1)`。`p=2,3,5`かつ`f=2`なら`2,4,8`。
- **参照**：12-01 Gao–Geroldinger、12-02 Geroldinger–Halter-Kochの定理5.5.9、Lang I§§7–9。
- **注意**：全有限アーベル群で`d(H)=Σ(n_i−1)`が常に成り立つと**主張しない**。一般には既知の上下界を条件付きで使う。

### B08. 窓×群の上界を数値的なcoefficientまで提示する

- **[原稿公式への代入]** `f=2,r=2,k=l=1,Σ={a,b},H=C₂`。窓モノイドの上界（実際には値集合）の大きさは短語`ε,a,b`の3個＋長語のprefix/suffixの4組＝**7**。群との積は最大**14**、`h=f(k+l+1)=6`、`d(C₂²)=2`。
- **結論**：現行`lem:marked-heavy-window-group`による`β≤(r+1)T(c+h)|V||M|^f`へ代入すると `β≤3T·8·|V|·14²=4,704 |V|T`。
- **用途**：非可換定数との比較。「数学的には多項式でも係数が重い」という課題を明示できる。**この4,704は上界の代入結果で最適値ではない**。

### B09. `factorization forest`による長路の再構成

- **[着想]** Simon (07-07)の有限半群factorization forestを、MCFG導出木の`λ`評価へ移す。目的は繰返しラベルを含む路を一括短縮し、ラベル数の`N`因子を小さくすること。
- **難点**：通常の語のforestは連続部分語を扱うが、fan-out≥2の一部分木は複数の**非連続ブロック**を所有する。原稿のowner-wise同時置換との接続が核心。
- **テスト**：まずwell-nested fan-out 2に限定し、factorization forestのnodeの順序とownerを両立できるか確認。

### B10. 文法クラス別に鋭い上界を出す

- **[着想]** 全てのMCFGで`NT`を目指す前に、①acyclic、②unambiguous、③linear rank1、④well-nested fan-out2、⑤すべての非終端が一型しか生まない、の各クラスで上界を分ける。
- **例**：③では子が高々1つ、複数ownerの絡み合いが消えるため、証拠語の長さが短い経路上の型状態数で計測可能。⑤では`N_typ`が定数倍の`N`となり、型付けの負担が縮む。
- **禁止**：部分クラスでの改善を、一般fan-out2/rank2の上界だと書かない。

---

## 5. C群：ファンアウト2の未解決境界に取り組む（12案）

**大前提**：現行の`openproblem`は「`f≥2`でも擬多様体境界がLGか」。`V⊄LG`なら`U₁∈V`なので、**擬多様体レベルの否定的方向を示すにはU₁型付けを少なくとも1つ攻略すればよい**。逆方向の反例（非LGでも一様多項式）を狙うには、**その擬多様体に属する全てのtyping**への上界が必要であり、単一typingだけの例では不足する。

### C01. 稀な「型」から稀な「分布的役割」へ下界原理を拡張する

- **現行の確定原理**：`m`型の全語を消しても学習クラスに残るとき、特徴サンプルは少なくとも1つの`m`型語を含む。`μ_m(L)`が長ければ下界。
- **[着想]** `L'⊊L`を作り、`L\L'`の全語が長いが、`L'`は型を丸ごと消していない場合にも`lem:distinguishing`は適用できる。
- **候補条件**：`min{|w|:w∈L\L'}≥2^n`、`N(G),T(G)≤poly(n)`、そして**LとL'の両方が`(2,s_U)`-tuple-substitutable**。
- **意味**：§8は特定の**唯一の型の語**を禁じるだけなので、同じ型の短語が存在しても`L\L'`が長語しか含まなければ、指数下界が可能。

### C02. 2穴置換閉包を計算して候補族を設計する

- **[着想]** 有限言語`L⊆Σ^{≤n}`に対し、許容2穴文脈で同型の2tupleが共通受理文脈を持つとき、他の受理文脈でのswapを強制する閉包演算`Closure_{2,s}(L)`を反復する。
- **必要条件**：穴間separatorは**必ず非空**（現行定義）；tupleの各成分は非空。`s`は固定した`U₁`で2値。
- **実験**：`Σ={a,b,c}`, `n=5..12`、正例集合の語数`≤20`から出発。閉包で短い同型代表が生じるか、低コストな`L'`削除が可能かを観測。
- **危険**：長さ上限で閉包を切った場合、上限外に出る語を見落とす。有限実験は反例候補探索であって証明ではない。

### C03. `power-transfer`の可到達同値グラフを構成する

- **原稿の変形**：`u^{a+d}`を第1穴側へ動かし、第2穴の指数を`d`減らす。`s(u)`のeventual index/periodを`i₀,q`とすると、`a,b≥i₀`, `d∈qℕ_{>0}`。
- **[着想]** 受理語間にこの変形で辺を張る。連結成分を完全に調べて、ある長語`w`の削除が閉包に反するか調べる。
- **原稿からの数値**：一般には十分大きな`n≥2|S|+2`で非持ち上がり。`s_U(b)=1`の場合は`i₀=1,q=1`なので証明内部の条件`n≥2i₀+q+1`は**n≥4**に下げられる可能性（該当する分割が存在することを別途確認）。
- **重要な限界**：この変形は**Parikhベクトルと全長を保存する**。したがって**同じ長さの別語**は作れるが、**短い型代表**は作れない。ここを混同しない。

### C04. 2穴移行を多穴・多方向へ拡張する

- **[着想]** `f=2`の移行を`f=3`の3穴へ、または二つの異なる周期語`u,v`の交互ブロックへ拡張。
- **具体的問い**：`u^a v^b u^c`の各指数について、型を保った移動群がどの格子`q_uℤ×q_vℤ`を生成するか。
- **成果候補**：限られた種の長語下界を一括して排除する障害定理（新しい学習上界の直接証明ではない）。

### C05. 二成分にまたがる「削除に剛直な」文法を探す

- **[着想]** 長い語`w_n`を含む`L_n`で、2穴置換により強制される語を**すべて同じ長さで多量に受け入れ**つつ、`L_n\{w_n}`または`L_n\B_n`も2-代入可能になるよう設計する。
- **開始点**：元の三文字族 `E_i→b E_{i-1} E_{i-1} b | c E_{i-1} c` をそのまま使わない。2成分同期、2本のカウンタ、マーカー位置同時制約を用いる。
- **数値目標**：文法`N,T=O(n)`、最短識別語`2^{Ω(n)}`。例えば`n=12`で`≥4,096`文字が強制されるような候補を探す。

### C06. Parikh同値類全体を「消せる」か

- **[着想]** §8で単語から生成される強制語は同じParikhベクトルを持つ。そこで`L_n`を長語のParikh fiber全部と短語の集合に分割し、**長語fiberを丸ごと消した対象**が同じクラスに残るか検討。
- **具体式**：`L'_n = L_n \ {w∈L_n : Ψ(w)=v_n}`。両者が`(2,s_U)`に属し、`|v_n|=2^{Ω(n)}`なら`lem:distinguishing`により長語が必要。
- **難所**：Parikh fiber除去は正則言語との交差一般ではなく、MCFLへの閉包も自動ではない。**自明に成り立つと思わない**。

### C07. 2成分同値関係の「最小修復集合」を最適化する

- **[着想]** 有限ターゲットの2tuple distribution equivalenceに対し、語を削除したらどのswap条件が破れるかをSATで符号化する。
- **最小化**：`min Σ_w (|w|+1)x_w`（characteristic sampleの総符号長）、subject to 各subtargetを区別する正例が1つ以上含まれること。
- **期待**：唯一の稀な型ではない、**多数の部分ターゲットを同時に区別する最小証拠問題**が現れる。
- **注**：特徴サンプルの厳密な値を求めるには、指定の再構成作用素`B_{f,s}`の全上位集合条件も必要。SATはまず**下界候補発見用**。

### C08. ランク2という壁を利用する

- **[原稿確認]** 未解決問題は`r_max≥2`。一般MCFGではファンアウトとrankは別の資源で、`MCFL(2,2)=MCFL(2,3)`という言語クラス一致も参照されるが、**文法のサイズ・厚さの保存**は別問題。
- **[着想]** rank1では多項式、rank2で指数、という二分を探索。無意味な文法の増大ではなく`N,T`の両方を制御。
- **参照**：03-02、03-17、03-25。rank reductionでコストを定量追跡する。

### C09. well-nested 2-MCFGに先に限定して判定する

- **[着想]** 交錯の形を制限すれば、ownerの並びが簡単になり、C01下界またはB01上界のどちらかが得られる可能性。
- **予測すべき成果**：`well-nested`でのLG境界の必要性／不要性を個別に定める定理。
- **参照**：03-21、03-25、03-26、03-27。
- **注意**：部分クラスの結果を全2-MCFLの結論へ一般化しない。

### C10. 非LGだが簡単な個別typingの「本当に多項式か」を試す

- **[着想]** 擬多様体についてはU₁が障害だが、**個別typing**の複雑性はアルファベット上の実現方法に左右される。
- **候補例**：全字母が同じ冪等元に写るtrivial positive image、1文字アルファベットから2元半束へのsurjectionはそもそも実現しにくい、という制約の違いを整理。
- **実験**：アルファベットサイズ`|Σ|=2,3,4`、到達する有限半群の位数`≤4`でtypingを列挙し、`f=1/2`の比較表を作る。
- **危険**：1つのtypingについて多項式と分かっても、**擬多様体全体の反例ではない**。

### C11. U₁の字母実現を利用した「個別typing」の簡単な十分条件

- **[導出候補]** 異なる字母`a,b,c`が存在して、`s(a)=s(b)=e`, `s(c)=z`, `e²=e`, `z²=z`, `ez=ze=z`, `e≠z`なら、既存三文字族の`W_n`は型`e`を持ち、`c`を含む他の生成語は型`z`になる。
- **したがって**：既存の`f=1`の指数データ下界を**その個別typingにも**適用できる（原稿のClark–Eyraud substitutabilityはtypingを問わない）。
- **意味**：擬多様体についての定理Cから、字母像に対する**明示的な個別typingの指数下界条件**を切り出せる。
- **数値**：同じく`N=13n+7,T=4n`、強制語長`3·2^n−2`。
- **限界**：上記の文字像を満たさないtypingにも成立するとは言えない。ユーザー原稿の主定理Cより一般的な必要十分条件ではない。

### C12. 「非LGでもfan-out2なら短いデータ」を示す場合の十分条件を先に構想する

- **[着想]** `U₁`の全typingについて、`τ(G,s)`が`poly(N,T)`なら、`cor:distribution-representatives`によって多項式データが得られる可能性。
- **強い目標**：`τ(G,s_U) ≤ N^a T^b`（`a,b`は固定）を全ての2-代入可能targetについて示す。ただしこれは**一つのU₁ typing**に対する結果であり、擬多様体全体の反例には未到達。
- **難所**：2穴冪移行は語長を保存するため、この不等式を単独で証明しない。他の短縮操作が必要。

---

## 6. D群：計算実験・アルゴリズム・証明補助（9案）

### D01. 2穴代入可能性の完全検査器

- **入力**：有限`L⊆Σ^{≤ℓ}`、`f≤2`、有限半群の乗法表と文字像。
- **計算**：各語で最大`2f=4`切断点を列挙、`Obs_d(L)`と`D_L^{(d)}(x)`を構築。**穴の間は非空**、各穴も非空。型が等しく、分布に共通文脈があるtupleだけを比較。
- **出力**：代入可能性の真偽、偽なら反例 `(x,y,E,F)` を出す。
- **粗い計算量**：1語当たり切断列挙は`O(ℓ^{2f})`、f2なら`O(ℓ⁴)`；ただしtuple・文脈比較の管理費用が別途増える。
- **まず**：`n=1..3`の三文字族、`q=2,k=1,f=1,2`のmarker族、原稿§8の非持ち上がりを再現する。

### D02. 型付き最短導出ハイパーグラフ

- **入力**：良いMCFG、有限`λ:Σ*→M`、各非終端のcomponent type vector。
- **ノード**：`(A,t)`、最大`|V||M|^f`（実際はreachableのみ）。
- **ハイパー辺**：装飾した各規則と実現可能child型。重みは明示終端数。
- **計算**：nonnegative min-plus hyperpathで最短yield長を求める。**長さは二進整数で保持**。
- **目的**：`β`の実測、巨大な冪語を明示展開せずに`2^n`を報告する。出力語そのものを作る場合の時間は語長以上必要なので、長さ計算と語出力を区別。

### D03. 文法の同型削減・到達型数の統計

- **[着想]** ランダムまたは系統的に小文法（`|V|≤5`, `r≤2`, `f=2`）を生成し、`|Types(A)|`や`N_typ`を測る。
- **指標**：`N_typ/N`、`t_typ/T`、`Σ_X shortest(X)/(NT)`、`τ/t_typ`。
- **期待**：典型例で二乗上界が大幅に粗いことを実測し、B01–B04の攻め方を選ぶ。

### D04. 非可換owner lemmaの最小反例探索

- **モデル**：群`S₃`または`D₈`、`f=2`、owner`m=2..8`、各owner最大2ブロック、1行または2行。
- **目的**：どのowner非空subsetを選んでも元の各行積を保てない例の最大`m`を調べる。
- **数式**：全`J≠∅`について`∃row: val_row(J)≠val_row(∅)`という反例制約をSAT/SMTで表す。
- **成果**：B05の小さな多項式閾値推測、配置上の最悪形、本文に入れる図示用の小例。
- **危険**：探索範囲内で反例無しでも、普遍閾値の証明にならない。

### D05. Rees行列・LGの全小例チェック

- **テスト群**：`C₂,C₃,S₃`、行列index集合`|I|,|Λ|≤3`、全sandwich matrixの一部。
- **確認**：`s(w)`の直接積計算と、`λ_{k,ν}`によるprefix/suffix+sliding group評価が同じ語を識別するか。
- **語長**：`|w|≤2k+5`を最初に検査。短い語のboundary caseを重点確認。

### D06. 2穴冪移行の閉包／counterexample generator

- **入力**：`u,v`などの周期語、有限モノイド、最小指数`i₀`と周期`q`。
- **探索**：`w_L u^a w_M u^{d+b}w_R`を与えたとき移行先語と型、長さ、Parikhを逐一照合。
- **目標**：原稿の`n≥2|S|+2`をtyping別に鋭くする。`U₁`では`i₀=q=1`を使い、閾値候補`n≥4`を自動確認。

### D07. 「証拠を何文字に圧縮できるか」を別モデルで測る

- **[着想]** 文法サイズ`O(n)`から出る強制語`W_n`は長さ`Θ(2^n)`だが、**SLPなど圧縮表現**なら`O(n)`で表せる。これは現在の**展開した正例語の総長**とは別の指標。
- **新問い**：compressed characteristic data / compressed positive texts では、U₁指数下界が消えるか。
- **実験**：`W_0=a`, `W_i=b W_{i-1} W_{i-1} b`に対応するSLPは`O(n)`規則。一方、圧縮データ上でのsample consistencyやmembership計算は追加の計算量解析が必要。
- **注意**：圧縮版での改善を現行定理Cの反証と誤認しない。

### D08. 証拠集合の最小化をset coverとして近似する

- **[着想]** 小規模な有限言語族`𝔏`に対し、1つの語が識別する競合標的の集合を管理し、`min Σ(|w|+1)`の重み付きset coverとして候補サンプルを探索。
- **複雑性**：これは有限の競合族に対する近似であって、定義で量化する**全標的・全上位集合**を完全に扱うとは限らない。
- **比較**：current witness construction、greedy cover、最適小例の長さ比。

### D09. 4種の保証を自動チェックするビルド監査

- **[着想]** LaTeXの定理ごとに「字母数」「fan-out」「rank」「typing固定」「set-driven / sequential」「サンプル総長」「syntactic stabilization」をタグとして付ける。
- **対象**：abstract、Main Theorems A–C、Table 1–2、§7 IPTtD、§8、Conclusion。
- **目的**：例えば「every learner」という文があるのに定理は「every set-driven operator with characteristic samples」しか扱わない、という過剰主張の再発防止。

---

## 7. E群：別の理論へ橋渡しする可能性（8案）

### E01. syntactic concept latticeによる「分布同値代表」の可視化

- **材料**：05-03 Clark (2013)、05-01 Polák (2001)、04巻のresidual／strong learning。
- **[着想]** 型ベクトルごとにtuple distributionの概念束を作り、`τ_X`をクラスの最短代表コストとして扱う。
- **目的**：`t_typ`と`τ`の乖離を、非終端の導出上の制約と**言語自体の分布構造**の違いとして説明する。
- **障害**：MCFGのtuple-contextはnonempty separators付きであり、通常の二側syntactic congruenceとは別のrelation。既存のconcept latticeの定理をそのまま適用しない。

### E02. 有限半群を選ぶbiasの格子論

- **[着想]** 型付けのrefinement `s≼t`で `C_{f,s}⊆C_{f,t}`になる一方、証拠サンプルの長さは単調ではない可能性がある。`type lattice`上で`N_typ`・`τ`・学習可能クラスの包含を整理。
- **小例**：1元typing→`U₁`→`U₁×C₂`、2文字／3文字アルファベットでsame targetの最短characteristic dataを比較。
- **注意**：クラスが大きくなることと、**特定再構成operatorに対してsampleが長くなること**の関係を自明視しない。

### E03. teaching dimensionとcharacteristic sampleの関係

- **材料**：01-11 Goldman–Kearns、01-12 Goldman–Mathias、01-05 de la Higuera。
- **[着想]** 教師が特定の正例を選べるという点を整理し、語数だけのteaching dimensionと総符号長teaching costを分ける。
- **例**：三文字族では**たった1語の強制正例**でも、その語長は`3·2^n−2`。**個数が1だからデータが簡単とは言えない**。
- **注意**：Gold TxtEx／teaching／characteristic sampleは量化が異なる。

### E04. Gold収束段階・一貫性の境界を別定理に

- **[着想]** set-driven operatorに多項式長characteristic sampleがあっても、**任意のtextにおける実際の提示時点**は保証されない。保守的sequential learnerのstage complexityと区別。
- **具体例**：1語の必要なwitnessが長さ100でも、textがその語を10^9回目にしか提示しなければ、停止・収束stageは10^9より前に保証できない。
- **用途**：reviewerに対する範囲限定の正確化。

### E05. control-set／PDA側のbiasと有限半群typingを比較

- **材料**：09-03〜09-10、01巻、03巻。
- **[着想]** 偏りを「文脈の型比較への制限」と「認める導出経路への制限」に分解し、どちらが多項式characteristic dataに寄与するか比較。
- **狙い**：有限半群typingでもclassが広過ぎる際、control-setとの共通制約で稀な型／長いwitnessの障害を除けるか。
- **難所**：control-setによる言語クラス制限がMCFGの`(f,s)`-substitutabilityを保つとは限らない。

### E06. 木オートマトン・Datalog provenanceで証拠抽出を実装

- **材料**：08 TATA、03-28 Riechert、03-30 Nederhof、03-33 Datalog provenance。
- **[着想]** 装飾非終端を状態、規則をhyperedgesとし、1つのwitnessの最短導出を`min-plus`で求める。複数witnessを**共有DAG**として保存する。
- **可能な定理**：`G×S`のwitness生成器の実行時間多項式（ただし出力する非圧縮語長には当然比例）、または圧縮表現の構築時間上界。

### E07. higher-arity PAC／VC理論への研究上の接続

- **材料**：10巻。分布学習とPACは別の保証モデル。
- **[着想]** tuple context acceptanceを高階arityの関係として捉え、そのVC特性がcharacteristic dataの**語数**や**長さ**へ何を示唆するか探索。
- **重大な留保**：10巻冒頭のclaim auditでは、Chernikov–Towsner (2025)の一般PAC十分性証明には指摘がある。**争いのある命題を既知定理として引用・転用しない**。
- **TCS現行稿への扱い**：原則本文には増やさず、博士論文の将来課題または別稿。

### E08. 哲学・刺激の貧困との最小限の接続

- **材料**：11巻のGoldと異なる哲学／認知的文脈。
- **[着想]** 博士論文総論では「正例だけで同定可能か」「証拠は何語か」「何文字か」を層別して位置づける。
- **明確な区別**：Plato/Chomskyの認識論的問題はGoldのTxtEx不可能性や今回のsemigroup theoremと**同一の数学命題ではない**。現在の41ページのTCS論文に長い哲学的展開を足すべきではない。

---

## 8. F群：論文投稿の数学的正確性・見せ方を改善する（7案）

### F01. IPTtDの形式定義と仮説文法の型を一致させる【最優先】

- **査読報告の確定的指摘**：現行`cor:iptd`はrepresentation classを「reduced good＋空語bit」とするが、生の再構成grammar`B_{f,s}^{≤r}(K)`をそのまま返すと、`ε`規則やreduced性に齟齬がある。Eyraud–Heinz–Yoshinaka (2016) Definition 2.12との照合が必要。
- **[着想] 修正**：仮説を`(G_K^+, 1[ε∈K])`とし、ε規則を外した良いMCFGを出力。観測tupleは親の語からrank1構成でreachable、Constでproductiveという補題を追加する。
- **規模**：補題1個＋証明約0.5〜1.5ページが目安（編集予測であって数学的保証ではない）。
- **参照**：02-06、03-04、前回査読報告R3.8。

### F02. タイトル・要旨の「LG境界」の量化を厳格に

- **適用範囲**：LGなら上界は全`f`、**必要十分境界はf=1で擬多様体を量化したときのみ**。
- **修正案**：abstract内で「local groups are the boundary」を必ず`at fan-out one, for pseudovarieties`に修飾。`f≥2`は未解決とセットで書く。

### F03. lower boundの作用素量化を書き落とさない

- **[原稿確認]** 下界が一般化されるのは「**同一クラスの全標的にcharacteristic sampleを持つset-driven operator**」である。
- **避ける表現**：every learner / all learning algorithms / Gold learners require...。全textのpresentation scheduleへの下界でもない。

### F04. good-normalizationの「厚さ」は保存しない

- **[原稿確認]** `prop:good-normalization`は文法サイズ・fan-out・rankを制御するが、**元の任意standard grammarの`θ̄`を保存するわけではない**。
- **改稿案**：量的定理は常に「与えられた reduced good G に相対的」とAbstract末尾に補足。元のstandard Gまで広げるなら別のnormalization lemmaが必要。

### F05. 主定理3本、付録の二種類の証明の強みを維持

- **核**：(A) LG＋非可換同時置換、(B) 全f・全typingの`NT`下界、(C) f1でのpseudovariety境界。
- **避けたい肥大化**：PAC/VC、残余automata、哲学を本文に追加して「一点集中版」の利点を失うこと。

### F06. 数値を明示した表を一つ増やす

- **提案**：§5またはAppendix Aに`H=C₂`（可換）と`H=S₃`（非可換）、`f=1,2`の`c`比較表。
- **効果**：なぜgroup theory／Davenportを使い、なぜ非可換で順序均質化が難しいのかを直感化する。
- **注意**：巨大定数は**効果的だが粗い上界**、実務的サンプル量として推奨しない。

### F07. 文献を引用できる範囲は一文ずつ絞る

- Almeida 2009：LG・U₁の古典的同値。
- Straubing/Tilson：Delay／半直積の古典的背景。
- Costa：`LI∨Grp`周辺のjoin。
- Yoshinaka 2008/2011/2015：既存の分布学習・定性的同定・一部データ長。
- Gao/Geroldinger：可換群のDavenport定数。
- **新しい定理Aの導出を、いずれか1本の古典文献に直接帰属させない**。

---

## 9. 実行順序：論文が確実に強くなる順

この順位は**研究上の編集効率を考えた主観評価**であり、成功確率ではない。レベル：**短期**＝既存証明の再構成・記述改訂、**中期**＝新しい補題、**長期**＝未解決問題。記号`◎/○/△`は期待効果の相対評価で、統計的な数値ではない。

| 順位 | 作業 | 対応案 | 期限目安ではない工数階層 | 新規性の見込み | 直接効果 |
|---:|---|---|---|---|---|
| 1 | IPTtD仮説クラスを補題で修復 | F01 | 短期 | 既存結果の厳密化 | ◎形式的弱点を解消 |
| 2 | LG禁止構造・擬恒等式・fresh identityの1段落 | A01,A02,A09,A10 | 短期 | 古典整理 | ◎境界の意味が明瞭 |
| 3 | 原典版照合と引用帰属 | A06,A08,F07 | 短期 | 文献精度 | ◎査読リスク低減 |
| 4 | 例に具体数値と上界定数を加える | B07,B08,F06 | 短期 | 教示的 | ○読みやすい |
| 5 | LGのminimal delay `d(S)`への改善 | A03 | 中期 | 補題の改良 | ○係数改善 |
| 6 | reachable型数`R_λ`版の定理 | B04 | 中期 | 定量改良 | ○実務的上界 |
| 7 | `Σ τ_X`の償却解析 | B01,B02 | 長期 | **高** | ◎`N²T`を減らせる可能性 |
| 8 | fan-out2の2穴閉包探索 | C01,C02,C06,C07 | 長期 | **非常に高** | ◎open problemに接近 |
| 9 | 非可換owner閾値のf2専用改良 | B05,B06,D04 | 長期 | 高 | ○巨大定数の削減 |
| 10 | factorization forest／well-nestedの限定結果 | B09,C09 | 長期 | 高 | ○別原理の上界・下界 |

### 特に追究価値の高い3つの研究プログラム

**プログラムP1：`N²T`の余分なNを消す。** 出発点は`cor:distribution-representatives`。全nonterminalをそれぞれ最悪長で評価するのをやめ、各規則の証拠を選ぶ共同最適化へ移行する。最初の目標は`Σ_X τ_X=O(NT)`といった償却型不等式の成否判定。**反例探しも同じくらい重要**。

**プログラムP2：U₁型付け、f=2、rank2の強制長語を探す。** 元の倍増族を再投入しない。必要なのは`L_n'⊊L_n`の双方が2tuple-substitutable、差集合の最短語が`2^{Ω(n)}`、文法size/thicknessが`poly(n)`という**3条件を同時に満たす**こと。`rare type`が失敗しても`distinguishing subtargets`に活路がある。

**プログラムP3：非可換の同時置換定数を局所構造で削る。** `f=2, H=S₃`の現行`1.27×10²⁶`は組合せ的に大幅に粗い可能性がある。owner配置分類を`f=2`に固定し、2行間の順序パターンと群境界状態を同時に扱う専用証明を探す。理論的閾値`O(|H|^c)`の小さい`c`、または`c_{H,2}≤100|H|^4`など**検証可能な仮説**を立てる。ただし数値定数100や次数4に根拠はなく、明確に**挑戦的な仮説**である。

## 10. 証明責任を残す命題のチェックリスト

| 仮説・案 | すぐには主張できない理由 | 反証・検証の第一歩 |
|---|---|---|
| `LG ⇒ cs=O(NT)` | 既知の証明は`O(N²T)` | `Σ τ_X`の反例検索／償却計数 |
| `f≥2でもLGが必要十分` | 現行§8が旧下界の移植を妨害 | `U₁`に対する2tuple-substitutableな2標的族 |
| `U₁`で`τ`が常に短い | power-transferは長さ保存 | 長さを**減らす**別の置換を探す |
| `f=2`で非可換閾値`O(|H|²)` | 一般のorder configurationsを未処理 | owner数2..8でSAT反例探索 |
| arbitrary MCFGでもnormalization後`T`保存 | 現行の正規化はサイズのみ保証 | nullable／mergingの小文法で反例探索 |
| Langの群論だけでReesを証明できる | 専門の半群理論が必要 | 07-12 Howie, 07-17 Almeidaを一次資料に |
| PAC上界からGoldの特徴データ長上界 | 学習モデル・量化が異なる | 例・テキスト・確率分布の区別を定義から書く |
| 画像主体のAlmeida(1994)の章番号を引用できる | 本文検索ができず紙面要照合 | 該当ページを画像表示して章／命題／原文を確認 |

## 11. この文書自身の検証範囲と次の作業に必要な素材

- 数字のうち`12巻/9,900頁/130エントリ`、各合本頁、論文名は**実際のPDF表紙**とプロジェクトマスターv17の索引に基づく。130は**延べ件数**であり独立した130研究成果という意味ではない。Almeida旧稿・刊行版などが重複する。
- 本文で実際に確認した代表原典は**07巻 p.3660のAlmeida Prop.2.3**、同巻Costa論文の冒頭、03巻Seki等の基本、その他巻の索引。10,840ページ全ての数学的内容を精査したという主張ではない。
- 新しい研究アイデアは**私の分析・推測**であり、出典に同じ主張が明記されていることを意味しない。論文へ採用する際は先行研究を再検索し、真新しさと偽例の有無を検証する必要がある。
- 研究の現行上界・下界は2026-11-06の`main.tex`固定版に対応する。GitHubの後続revisionがある場合は同一SHAか確認してから適用する。
- 正式引用には**個々の原著の雑誌掲載頁**を使う。合本のページは内部の場所案内。書籍・スキャンは印刷頁とPDF通し頁を取り違えない。

---

## 付録I．所蔵12合本の**全130収録原典**アクセス索引

**この一覧はProjectマスターv17の§5.1–5.12と、各PDF巻頭の実物目次を照合した入口索引である。** 下記の`合本頁`はファイル内の1始まりで、引用書誌の「原著頁」ではない。`Research-Library REF`は索引上の識別子であり、同番号の独立ファイルを今回すべて開いたという意味ではない。重複版・重複原典を含む。

### 情報源1：01_Foundations_of_Grammatical_Inference_and_Reversibility_v8.pdf (907頁)

| 合本項目 | 合本頁 | 収録文献 | Research-Library REF | 元索引優先度 |
|---|---:|---|---|:---:|
| 01-01 | 2–29 | Gold (1967): Language Identification in the Limit | REF-01-01 | A |
| 01-02 | 30–46 | Angluin (1980): Finding Patterns Common to a Set of Strings | REF-01-02 | C |
| 01-03 | 47–71 | Angluin (1982): Inference of Reversible Languages | REF-01-03 | B |
| 01-04 | 72–91 | Angluin (1987): Learning Regular Sets from Queries and Counterexamples | REF-01-04 | C |
| 01-05 | 92–105 | de la Higuera (1997): Characteristic Sets for Polynomial Grammatical Inference | REF-01-05 | A |
| 01-06 | 106–115 | Angluin (1980): Inductive Inference of Formal Languages from Positive Data | REF-01-06 | A |
| 01-07 | 117–150 | Kanazawa (1993): Identification in the Limit of Categorial Grammars [CWI report] | — | C |
| 01-08 | 151–350 | Kanazawa (1998): Learnable Classes of Categorial Grammars | — | B |
| 01-09 | 351–783 | de la Higuera (2010): Grammatical Inference: Learning Automata and Grammars | — | B |
| 01-10 | 784–801 | Costa Florencio & Fernau (2012): On Families of Categorial Grammars of Bounded Value | — | C |
| 01-11 | 802–834 | Goldman & Kearns (1992): On the Complexity of Teaching [technical report] | — | C |
| 01-12 | 835–865 | Goldman & Mathias (1993): Teaching a Smarter Learner [technical report] | — | C |
| 01-13 | 866–907 | Kanazawa (1996): Identification in the Limit of Categorial Grammars [journal edition] | REF-01-16 | B |

### 情報源2：02_Substitutability_and_Positive-Data_Grammar_Learning_v6.pdf (186頁)

| 合本項目 | 合本頁 | 収録文献 | Research-Library REF | 元索引優先度 |
|---|---:|---|---|:---:|
| 02-01 | 2–22 | Clark & Eyraud (2007) - Polynomial Identification of Substitutable CFLs | REF-02-01 | A |
| 02-02 | 23–36 | Yoshinaka (2008) - Identification of (k,l)-Substitutable CFGs | REF-02-02 | A |
| 02-03 | 37–51 | Coste, Garet & Nicolas (2012) - Local Substitutability for Sequence Generalization | REF-02-03 | B |
| 02-04 | 52–63 | Yoshinaka (2015) - General Perspective on Distributionally Learnable Classes | REF-02-04 | A |
| 02-05 | 64–92 | Clark & Yoshinaka (2016) - Distributional Learning of CFGs and MCFGs | REF-02-05 | A |
| 02-06 | 93–114 | Eyraud, Heinz & Yoshinaka (2016) - Efficiency in Identification in the Limit | REF-02-06 | A |
| 02-07 | 115–128 | Coste & Nicolas (2019) - Learning Local Substitutable CFGs by Reduction | REF-02-07 | B |
| 02-08 | 129–140 | Numaya et al. (2023) - Substitutable CFGs over Infinite Alphabets | REF-02-08 | C |
| 02-09 | 141–155 | Kanazawa & Yoshinaka (2023) - Extending Distributional Learning | REF-02-09 | B |
| 02-10 | 157–170 | Kanazawa & Yoshinaka (2021) - Hierarchy of CFGs Learnable with Positive Data and MQs | — | B |
| 02-11 | 171–186 | Kanazawa (2023) - Learning CFGs from Positive Data and Membership Queries | — | B |

### 情報源3：03_Multiple_Context-Free_Grammars_Foundations_and_Learning_v9.pdf (1,213頁)

| 合本項目 | 合本頁 | 収録文献 | Research-Library REF | 元索引優先度 |
|---|---:|---|---|:---:|
| 03-01 | 2–40 | 01 Seki et al. — On Multiple Context-Free Grammars | REF-03-01 | A |
| 03-02 | 41–83 | 02 Rambow & Satta — A Two-Dimensional Hierarchy for Parallel Rewriting Systems | REF-03-02 | B |
| 03-03 | 84–99 | 03 Yoshinaka & Clark — Polynomial-Time Learning of MCFGs with MAT | REF-03-03 | B |
| 03-04 | 100–110 | 04 Yoshinaka — Efficient Learning of MCFGs with Multidimensional Substitutability | REF-03-04 | A |
| 03-05 | 111–132 | 05 Clark — An Introduction to Multiple Context-Free Grammars | REF-03-05 | B |
| 03-06 | 133–145 | 06 Clark & Yoshinaka — Beyond Semilinearity: Learning Parallel MCFGs | REF-03-06 | A |
| 03-07 | 146–157 | 07 Krishna — Multiple Context Free Grammars | REF-03-07 | C |
| 03-08 | 158–172 | 08 Clark — Strong Learning of Probabilistic MCFGs | REF-03-08 | B |
| 03-09 | 173–180 | 09 Kato, Seki & Kasami — Subclasses of TAG for RNA Secondary Structure | REF-03-09 | C |
| 03-10 | 181–233 | 10 Kato — Generative Power of Grammars for RNA Structure | REF-03-10 | C |
| 03-11 | 234–260 | 11 Uemura et al. — Tree Adjoining Grammars for RNA Structure Prediction | REF-03-11 | C |
| 03-12 | 261–465 | 12 Gallot — Safety of Transformations of Data Trees | REF-03-12 | A |
| 03-13 | 466–505 | 13 Bishop et al. — On Groups with EDT0L Word Problem | REF-03-13 | B |
| 03-14 | 506–516 | 14 Oates et al. — Inferring Mildly Context-Sensitive Grammars in Polynomial Time | REF-03-14 | C |
| 03-15 | 517–550 | 15 Rambow & Satta — Independent Parallelism in Finite Copying Rewriting Systems | REF-03-15 | B |
| 03-16 | 551–569 | 16 Kanazawa — Ogden's Lemma, MCFGs, and Control Language Hierarchy | REF-03-16 | B |
| 03-17 | 570–578 | 17 Gomez-Rodriguez et al. — Optimal Reduction of Rule Length in LCFRS | REF-03-17 | A |
| 03-18 | 579–593 | 18 Yoshinaka — Learning Mildly Context-Sensitive Languages from Positive Data | REF-03-18 | A |
| 03-19 | 594–608 | 19 Yoshinaka — Polynomial-Time MCFG Identification with Membership Queries | REF-03-19 | B |
| 03-20 | 609–880 | 20 Kallmeyer — Parsing Beyond Context-Free Grammars | — | B |
| 03-21 | 881–908 | 21 Kanazawa et al. — The Failure of the Strong Pumping Lemma for MCFGs | — | B |
| 03-22 | 909–916 | 22 Vijay-Shanker, Weir & Joshi (1987) — Structural Descriptions and LCFRS Foundations | REF-03-22 | B |
| 03-23 | 917–924 | 23 Weir (1992) — LCFRS and Deterministic Tree-Walking Transducers | REF-03-23 | B |
| 03-24 | 925–932 | 24 Gildea (2010) — Optimal Parsing Strategies for LCFRS | REF-03-24 | B |
| 03-25 | 933–941 | 25 Gomez-Rodriguez & Satta (2009) — Optimal Binarization of Fan-Out-Two LCFRS | REF-03-25 | A |
| 03-26 | 942–953 | 26 Kanazawa & Salvati (2010) — Copying Power of Well-Nested MCFGs | REF-03-26 | B |
| 03-27 | 954–1031 | 27 Engelfriet, Maletti & Maneth (2018) — Multiple Context-Free Tree Grammars: Lexicalization and Characterization | REF-03-27 | B |
| 03-28 | 1032–1081 | 28 Riechert et al. (2016) — Algebraic Dynamic Programming for MCFGs | REF-03-28 | B |
| 03-29 | 1082–1099 | 29 Gildea (2011) — Grammar Factorization by Tree Decomposition | REF-03-29 | B |
| 03-30 | 1100–1108 | 30 Nederhof (2003) — Weighted Deductive Parsing and Knuth's Algorithm | REF-03-30 | A |
| 03-31 | 1109–1143 | 31 Ramalingam & Reps (1996) — Incremental Grammar-Problem Shortest Derivations | REF-03-31 | A |
| 03-32 | 1144–1165 | 32 Liang Huang (2008) — Advanced Dynamic Programming in Semiring and Hypergraph Frameworks | REF-03-32 | B |
| 03-33 | 1166–1186 | 33 Ramusat, Maniu & Senellart (2021) — Dynamic Programming for Datalog Provenance | REF-03-33 | C |
| 03-34 | 1187–1213 | 34 Duncan, Elder, Frenkel & Lyu (2026) — A Substitution Lemma for Multiple Context-Free Languages | REF-03-34 | A |

### 情報源4：04_Residual_Structure_Canonical_CFGs_and_Strong_Learning_v3.pdf (142頁)

| 合本項目 | 合本頁 | 収録文献 | Research-Library REF | 元索引優先度 |
|---|---:|---|---|:---:|
| 04-01 | 2–33 | Denis, Lemay & Terlutte (2002) - Residual Finite State Automata | REF-04-01 | C |
| 04-02 | 34–66 | Fernau (2003) - Identification of Function-Distinguishable Languages | REF-04-02 | C |
| 04-03 | 67–80 | Clark (2010) - Distributional Learning of CFGs with MAT | REF-04-03 | B |
| 04-04 | 81–103 | Clark (2013) - Learning Trees from Strings: A Strong Learning Algorithm | REF-04-04 | B |
| 04-05 | 104–116 | Clark (2015) - Canonical CFGs and Strong Learning: Two Approaches | REF-04-05 | C |
| 04-06 | 117–128 | Kanazawa & Yoshinaka (2017) - Strong, Weak, and Very Weak Context and Kernel Properties | REF-04-06 | B |
| 04-07 | 129–142 | Kanazawa & Kappe (2019) - Decision Problems for Clark-Congruential Languages | — | B |

### 情報源5：`05_Syntactic_Concept_Lattices_and_Finite_Algebra_v3.pdf` (136頁)

| 合本項目 | 合本頁 | 収録文献 | Research-Library REF | 元索引優先度 |
|---|---:|---|---|:---:|
| 05-01 | 2–11 | Libor Polak (2001) - Syntactic Semiring of a Language | REF-05-01 | C |
| 05-02 | 12–48 | Jorge Almeida, Stuart Margolis, Benjamin Steinberg, and Mikhail Volkov (2007) - Representation Theory of Finite Semigroups, Semigroup Radicals and Formal Language Theory | REF-05-02 | A |
| 05-03 | 49–75 | Alexander Clark (2013) - The Syntactic Concept Lattice: Another Algebraic Theory of the Context-Free Languages? | REF-05-03 | B |
| 05-04 | 76–103 | Stepan L. Kuznetsov (2025) - On Syntactic Concept Lattice Models for the Lambek Calculus and Infinitary Action Logic | REF-05-04 | C |
| 05-05 | 104–136 | Almeida, Margolis, Steinberg & Volkov (2009), TAMS刊行版 — *Representation Theory of Finite Semigroups, Semigroup Radicals and Formal Language Theory*, *TAMS* 361(3):1429–1461, DOI: 10.1090/S0002-9947-08-04712-0 | —（Project合本収録・個別原典登録未確認） | A |

### 情報源6：06_Grammar_Semantics_Categories_and_Factorization_v2.pdf (159頁)

| 合本項目 | 合本頁 | 収録文献 | Research-Library REF | 元索引優先度 |
|---|---:|---|---|:---:|
| 06-01 | 2–20 | Donald E. Knuth (1968) - Semantics of Context-Free Languages | REF-06-01 | C |
| 06-02 | 21–136 | Bret Tilson (1987) - Categories as Algebra: An Essential Ingredient in the Theory of Monoids | REF-06-02 | A |
| 06-03 | 137–146 | Yo-Sub Han, Arto Salomaa, Kai Salomaa, Derick Wood, and Sheng Yu (2007) - On the Existence of Prime Decompositions | REF-06-03 | C |
| 06-04 | 147–159 | Clemente Pasti et al. (2023) - On the Intersection of Context-Free and Regular Languages | REF-06-04 | B |

### 情報源7：`07_Algebraic_Foundations_of_Automata_Theory_Reference_v11.pdf` (3,687頁)

| 合本項目 | 合本頁 | 収録文献 | Research-Library REF | 元索引優先度 |
|---|---:|---|---|:---:|
| 07-01 | 2–345 | 01 Pin (2025) — Mathematical Foundations of Automata Theory | REF-07-01 | A |
| 07-03 | 347–815 | 03 Eilenberg (1974) — Automata, Languages, and Machines, Volume A | — | A |
| 07-04 | 816–892 | 04 Pin (1997) — Syntactic Semigroups | — | B |
| 07-05 | 893–1437 | 05 Hopcroft, Motwani & Ullman (3rd ed.) — Introduction to Automata Theory, Languages, and Computation | REF-07-02 | B |
| 07-06 | 1438–1919 | 06 Sipser (3rd ed.) — Introduction to the Theory of Computation | REF-07-03 | C |
| 07-07 | 1920–1949 | 07 Simon (1990) — Factorization Forests of Finite Height | REF-05-05 | B |
| 07-08 | 1950–1964 | 08 Costa (2002) — Some Pseudovariety Joins Involving Locally Trivial Semigroups | REF-05-06 | A |
| 07-09 | 1965–1970 | 09 Costa (2002) — Some Pseudovariety Joins Involving Locally Trivial Semigroups and Groups | REF-05-07 | A |
| 07-10 | 1971–2007 | 10 Almeida et al. (2007著者稿；2009年刊行論文のプレプリント) — Representation Theory of Finite Semigroups, Semigroup Radicals and Formal Language Theory | REF-05-02（既存登録；組版版同定ではない） | A |
| 07-11 | 2008–2049 | 11 Straubing (1985) — Finite Semigroup Varieties of the Form V * D | REF-07-11 | A |
| 07-12 | 2050–2410 | 12 Howie (1995) — Fundamentals of Semigroup Theory | REF-07-12 | A |
| 07-13 | 2411–2553 | 13 Pin (1986) — Varieties of Formal Languages | REF-07-13 | A |
| 07-14 | 2554–2734 | 14 McNaughton & Papert (1971) — Counter-Free Automata | REF-07-14 | B |
| 07-15 | 2735–3137 | 15 Samuel Eilenberg (1976), *Automata, Languages, and Machines*, Volume B（Bret Tilsonの章を含む） | —（Project合本のみ・個別原典登録未確認） | A |
| 07-16 | 3138–3654 | 16 Jorge Almeida (1994), *Finite Semigroups and Universal Algebra*（World Scientific） | —（Project合本のみ・個別原典登録未確認） | A |
| 07-17 | 3655–3687 | 17 Almeida, Margolis, Steinberg & Volkov (2009), TAMS刊行版 — *Representation Theory of Finite Semigroups, Semigroup Radicals and Formal Language Theory*, *TAMS* 361(3):1429–1461, DOI: 10.1090/S0002-9947-08-04712-0 | —（Project合本収録・個別原典登録未確認） | A |

### 情報源8：08_Tree_Automata_Techniques_and_Applications_Reference_v2.pdf (264頁)

| 合本項目 | 合本頁 | 収録文献 | Research-Library REF | 元索引優先度 |
|---|---:|---|---|:---:|
| 08-01 | 2–264 | Hubert Comon et al. (2008) - Tree Automata Techniques and Applications | — | B |

### 情報源9：09_Control_Sets_Pushdown_Automata_and_Typing_Bias_v5.pdf (278頁)

| 合本項目 | 合本頁 | 収録文献 | Research-Library REF | 元索引優先度 |
|---|---:|---|---|:---:|
| 09-01 | 2–30 | Ginsburg & Greibach (1966): Deterministic Context-Free Languages | REF-09-01 | B |
| 09-02 | 31–96 | Autebert, Berstel & Boasson (1997): Context-Free Languages and Pushdown Automata | REF-09-02 | A |
| 09-03 | 97–119 | Takada (1987): A Constructive Method for Grammatical Inference of Linear Languages Based on Control Sets | REF-09-03 | B |
| 09-04 | 120–126 | Takada (1988): Inferring Parenthesis Linear Grammars Based on Control Sets | REF-09-04 | C |
| 09-05 | 127–150 | Takada (1995): Learning Formal Languages Based on Control Sets | REF-09-05 | B |
| 09-06 | 151–167 | Koshiba, Mäkinen & Takada (1997): Learning Deterministic Even Linear Languages from Positive Examples | REF-09-06 | B |
| 09-07 | 168–179 | Coste et al. (2004): Introducing Domain and Typing Bias in Automata Inference | REF-09-07 | A |
| 09-08 | 180–186 | Takada (1988): Grammatical Inference for Even Linear Languages Based on Control Sets | REF-09-08 | B |
| 09-09 | 187–211 | Ginsburg & Spanier (1966): Finite-Turn Pushdown Automata | REF-09-09 | A |
| 09-10 | 212–238 | Clark & Yoshinaka (2014): Distributional Learning of Parallel Multiple Context-Free Grammars | REF-09-10 | A |
| 09-11 | 239–248 | Wakatsuki & Tomita (1993): Inclusion for Very Simple Deterministic PDA | REF-09-11 | B |
| 09-12 | 249–252 | Wakatsuki & Tomita (1992): Shortest Distinguishing Input Bound [Japanese] | REF-09-12 | C |
| 09-13 | 253–261 | Wakatsuki & Tomita (1991): Improved Branching Equivalence Algorithm [Japanese] | REF-09-13 | C |
| 09-14 | 262–269 | Wakatsuki, Tomita & Fujihashi (1989): Direct Branching Equivalence Algorithm [Japanese] | REF-09-14 | C |
| 09-15 | 270–278 | Tajima, Tomita & Wakatsuki (2000): Polynomial-Time Learnability of Simple Deterministic Languages | REF-09-15 | C |

### 情報源10：10_PACn_Higher_Arity_Learning_and_VCn_Theory_v3.pdf (333頁)

| 合本項目 | 合本頁 | 収録文献 | Research-Library REF | 元索引優先度 |
|---|---:|---|---|:---:|
| 10-01 | 5–9 | REF-01-07 - On the PAC_n learning | — | C |
| 10-02 | 10–14 | REF-01-08 - A generalization of the PAC learning in product probability spaces | — | C |
| 10-03 | 15–36 | REF-01-09 - On n-dependence | — | C |
| 10-04 | 37–42 | REF-01-10 - On VC_2-dimension and learnability | — | C |
| 10-05 | 43–54 | REF-01-11 - Higher-arity PAC learning, VC dimension and packing lemma | — | C |
| 10-06 | 55–58 | REF-01-15 - Remarks on a recent preprint of Chernikov and Towsner | — | C |
| 10-07 | 59–71 | REF-01-12 - PAC-Learning Unambiguous NTS Languages | — | C |
| 10-08 | 72–81 | REF-03-20 - Stochastic Finite Learning of Some Mildly Context-Sensitive Languages | — | C |
| 10-09 | 82–94 | REF-03-06 - Beyond Semilinearity: Distributional Learning of Parallel Multiple Context-free Grammars | — | C |
| 10-10 | 95–182 | REF-01-13 - Hypergraph Regularity and Higher Arity VC-Dimension | — | C |
| 10-11 | 183–333 | REF-01-14 - High-arity PAC Learning via Exchangeability | — | C |

### 情報源11：11_Plato_Chomsky_Stimulus_Poverty_and_Language_Learning_v1.pdf (1,437頁)

| 合本項目 | 合本頁 | 収録文献 | Research-Library REF | 元索引優先度 |
|---|---:|---|---|:---:|
| 11-01 | 4–125 | P01  Plato - Cratylus | REF-11-01 | C |
| 11-02 | 126–370 | P02  Plato - Meno and Other Dialogues | REF-11-02 | C |
| 11-03 | 371–640 | P03  Katz - Language and Other Abstract Objects | REF-11-03 | C |
| 11-04 | 641–654 | P04  Stainton et al. - Platonism in Linguistics | REF-11-04 | C |
| 11-05 | 655–998 | P05  Chomsky - Knowledge of Language | REF-11-05 | C |
| 11-06 | 999–1258 | P06  Clark and Lappin - Linguistic Nativism | REF-11-06 | C |
| 11-07 | 1259–1300 | P07  Pullum and Scholz - Stimulus Poverty | REF-11-07 | C |
| 11-08 | 1301–1333 | P08  Perfors et al. - Learnability of Abstract Syntax | REF-11-08 | C |
| 11-09 | 1334–1403 | P09  Christiansen and Chater - Language and Brain | REF-11-09 | C |
| 11-10 | 1404–1437 | P10  Warstadt et al. - BabyLM Challenge | REF-11-10 | C |

### 情報源12：12_Finite_Abelian_Groups_Zero_Sum_and_Additive_Theory_v1.pdf (1,158頁)

| 合本項目 | 合本頁 | 収録文献 | Research-Library REF | 元索引優先度 |
|---|---:|---|---|:---:|
| 12-01 | 2–27 | 01. Gao & Geroldinger (2006): Zero-Sum Problems in Finite Abelian Groups: A Survey | REF-12-01 | A |
| 12-02 | 28–733 | 02. Geroldinger & Halter-Koch (2006): Non-Unique Factorizations: Algebraic, Combinatorial and Analytic Theory | REF-12-02 | A |
| 12-03 | 734–1158 | 03. Grynkiewicz (2013): Structural Additive Theory | REF-12-03 | B |

**上の行数：130エントリ。** うち07巻の編集注記は原典として数えず、05巻/07巻に重複したAlmeidaの刊行版等を含む。

## 付録II．Lang単独書籍と今回のファイル所在

**Lang (2002, corrected printing 2005), _Algebra_, Revised Third Edition**, GTM 211, Springer, DOI `10.1007/978-1-4613-0041-0`。PDF `Algebra-SergeLang-ThirdEdition.pdf` (940頁)。主な導線：群とモノイド（印刷p.3→PDFp.21）、有限生成アーベル群（印刷p.42→PDFp.60）、群環（印刷p.97→PDFp.115）、行列（印刷p.503→PDFp.521）、半単純性（印刷p.641→PDFp.659）、有限群表現（印刷p.663→PDFp.681）。**Rees／LG／Davenportの専門原典ではない。**

**プロジェクトの同一セッションにあるファイル：** `01_...`〜`12_...`の各PDF、Lang PDF、`TCS-D-26-00494_R1.pdf`（姉妹CFG稿の編集部合成PDF）、`project-master-v17-2026-11-04.md`（12巻の索引・投稿ルーティング）、`chatgpt_tcs_referee_focus_2026-11-06.md`（前回の査読報告）。対象のMCFG原稿は上記GitHub固定blobを基準にした。

---

**最終方針：** 現行TCS一点集中稿への即効性を優先するならF01・A01・A02・A09・A10。新規数学を狙うならB01・C01・C02・C06・B05の順で研究投資を検討する。提案を採用する前に、現行GitHub版の定理番号・条件・原著本文に照らして検証する。

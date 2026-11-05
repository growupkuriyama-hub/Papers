# 日本語版（main_JP.tex）作成報告 — 2026-11-06

依頼書：`prompt_japanese_full_translation_2026-11-06.md`（README (170)）。

## 1. 版と規模

| 項目 | 値 |
|---|---|
| 英語正本 | `02-v2-lg-fanout-boundary/main.tex`、コミット `d6753a9`（`d6753a9c9776eef160f5918c3ac70c7a7f6278e2`） |
| 取得方法 | `main` を clone（HEAD は `4107c20`、README (170) の依頼書の追加のみ）。`git diff d6753a9 HEAD -- main.tex` は空で、`main.tex` の最終変更コミットは `d6753a9`。したがって訳した版は `d6753a9` そのもの |
| 英語版の行数 | 3,758 行 |
| 英語版のページ数 | 44 ページ（`latexmk -pdf main.tex`、pdfTeX、TeX Live 2023） |
| 日本語版の行数 | 3,751 行（`japanese/main_JP.tex`） |
| 日本語版のページ数 | 49 ページ、A4（`latexmk -lualatex main_JP.tex`、LuaHBTeX 1.17.0、TeX Live 2023） |

日本語版の行数が英語版と異なるのは、日本語の改行位置が英語と一致しないためであり、内容の増減ではない（§2 の検査を参照）。

## 2. 検査スクリプトの出力

`tools/check_jp_alignment.py`（Python 3 標準ライブラリのみ）。依頼の 1〜7 に加え、表の形（6b）と、コンパイル後の `.aux` による印字番号の一致（8）も検査する。

実行：`python3 tools/check_jp_alignment.py main.tex japanese/main_JP.tex <英語版の main.aux> <日本語版の main_JP.aux>`

```
1. labels: EN=125 JP=125
[PASS] label sequence: 0 differences
2. refs: EN \ref=335 \eqref=2 \cite keys=96 | JP \ref=335 \eqref=2 \cite keys=96
[PASS] \ref multiset: 0 differences
[PASS] \eqref multiset: 0 differences
[PASS] \cite multiset: 0 differences
3. environments: EN=187 JP=187
[PASS] environment sequence: 0 differences
4. sectioning: EN={'\\section': 16, '\\paragraph': 16, '\\subsection': 14, '\\section*': 5} JP={'\\section': 16, '\\paragraph': 16, '\\subsection': 14, '\\section*': 5}
[PASS] sectioning counts: 0 differences
5. \item: EN=62 JP=62
[PASS] \item count: 0 differences
6. math fragments: EN=3113 JP=3113; \text{...} occurrences inside math: EN=16 JP=16 (compared verbatim, 0 excluded)
[PASS] math fragment sequence: 0 differences
6b. tabular/tabularx environments: EN=8 JP=8 (rows and cells per row)
[PASS] table shapes: 0 differences
7. English runs of >= 5 words in Japanese prose: 0
[PASS] English residue: 0 differences
8. printed label numbers: EN=125 JP=125
[PASS] label numbers: 0 differences
ALL CHECKS PASSED
```

補足：

- 検査 6 は `\text{…}` の中も**除外せずに**比較した（除外件数 0、`\text{…}` は英日とも 16 件）。比較は空白の連なりを一つの空白に正規化した文字列の完全一致である。
- 検査 3 は `theorem` などに限らず、本文中のすべての `\begin{…}` の列を順序ごと比較している（187 個）。
- 検査 8 により、定理・補題・節・式・表のすべての番号（125 個のラベル）が英語版の印字と一致することを確認した。
- 検査 7 の閾値を 3 語に下げても、残るのは `(i),(ii),(iv)`（英語版にある項目番号の並び）と人名 `van Emde Boas` だけであった。

### コンパイルの結果

`latexmk -lualatex main_JP.tex`：エラー 0、未定義参照 0、未定義引用 0、重複ラベル 0。警告は次がすべてである。

| 件数 | 警告 | 説明 |
|---|---|---|
| 1 | `Package luatexja Warning: LuaTeX-ja's patch against the microtype package (lltjp-microtype.sty, 2019-11-08) may not work.` | microtype を英語版のまま読み込んでいるため。出力への実害は確認されなかった |
| 15 / 15 / 15 / 10 | `Package microtype Warning: Could not parse font size '8\jsc@mpt '`（同様に `9`, `10`, `12`） | ltjsarticle の寸法単位 `\jsc@mpt` を microtype が解釈できないという警告。組版は行われている |
| 1 | `Overfull \hbox (1.63332pt too wide) detected at line 1607` | 補題 5.3（`lem:marked-heavy-window-group`）の別行立て数式。英語版から一字も変えずに写した式が、A4 の版面（英語版は letter）でわずかにはみ出す。数式を変えられないので残した |

英語版（`latexmk -pdf main.tex`）は警告 0。

## 3. 訳語表の追加分（依頼書 §4 にない語）

| 英語 | 訳語 |
|---|---|
| positive-data learning / grammatical inference | 正データ学習／正データ文法推論 |
| identification in the limit | 極限同定 |
| set-driven (reconstruction) operator | 集合駆動型（再構成）作用素（§4 のとおり） |
| sample-consistent / sample consistency | 標本無矛盾／標本無矛盾性 |
| canonical operators（表の「Canonical」） | 標準の作用素（表では「標準」） |
| class-wide | クラス全体 |
| characteristic samples throughout the class | クラス全体で特徴標本をもつ |
| witness family / witnesses（反例・例としての） | 証拠族／証拠 |
| marker / marker family | 標識／標識族 |
| target / sub-target | 標的／部分標的 |
| template | 雛形 |
| terminal derivation / successful derivation | 終端導出／成功する導出 |
| sentence（導出された文） | 文 |
| yield | 産出 |
| start link / start rule | 開始の連結／開始規則 |
| context / admissible / accept | 文脈／許容／受理する |
| cut position | 切れ目の位置 |
| hole / separator / fixed part | 穴／区切り／固定部分 |
| arity | アリティ |
| doubling family / doubling rules | 倍増族／倍増規則 |
| eventual index and period | 最終的な指数と周期 |
| Parikh vector / Parikh map | Parikh ベクトル／Parikh 写像 |
| zero-sum-free / zero-sum subsequence / Davenport constant | 零和自由／零和部分列／Davenport 定数 |
| pigeonhole | 鳩の巣論法 |
| homogenization / homogeneous | 均質化／均質な |
| chunk / class region / frame / frame product | かたまり／類の領域／フレーム／フレーム積 |
| interleaved | 交互に並ぶ |
| separated（順序の分類） | 分離される |
| block pattern / pattern（添字の） | ブロックの型／型 |
| enlarged block / thinned and padded owners | 広げたブロック／間引きと詰め物をした所有者 |
| sliding window / delay | 滑動窓／遅延 |
| sandwich matrix | サンドイッチ行列 |
| idempotent / idempotent power | べき等元／べき等な冪 |
| locally trivial | 局所自明 |
| subsemigroup / homomorphic image / divisor | 部分半群／準同型像／因子 |
| kernel refinement | 核による細分 |
| corestriction | 余制限 |
| pause symbol / content（テキストの） | 休止記号／内容 |
| conservative | 保守的（§4 のとおり） |
| stage of convergence | 収束の段階 |
| parser / stack / move / run / reachable | パーザ／スタック／遷移／実行／到達可能 |
| decoration / support pattern / composition（整数の合成） | 飾り／台の型／合成 |
| trimming | 刈り込み |
| reduced（文法） / productive / reachable | 既約／生産的／到達可能 |
| lift（導出の） | 持ち上げ |
| roadmap | 道案内 |
| thickness lemma | 厚さの補題 |
| representative | 代表 |
| guarded tuple substitution / finite-monoid observation | 保護付きタプル代入／有限モノイド観測 |
| companion paper / companion manuscript | 姉妹論文／姉妹原稿 |
| Remark | 注意（依頼書 §3 のとおり。v1 日本語版の「備考」とは異なる） |

## 4. 翻訳で判断が要った箇所

### 4.0 全体の方針（数式の出現順）

検査 6 は数式断片を**出現順の列として**比較する。日本語の語順（目的語・修飾語が前に出る）のまま訳すと数式の順序が入れ替わるので、英語の数式順を保つために次の三つの型を一貫して用いた。どれも語を足すのではなく、英語の修飾の位置を写すためのものである。

1. **括弧による後置修飾**：「the $A$-subtree of $D_R$」→「$A$-部分木（$D_R$ の）」、「a presentation $G$ of $L\cap\Sigma^+$」→「表示 $G$（$L\cap\Sigma^+$ の）」。
2. **「〜なるもの」「〜のもの」による後置**：「a typing $s$ with $s\preceq s_{k,\ell}$ for some $k,\ell$」→「型付け $s$ であって，$s\preceq s_{k,\ell}$ がある $k,\ell\ge0$ について成り立つもの」。
3. **「〜が…について成り立つ」で量化を後に置く**：「$E_A[\tuple u]\in L(G)$ for all $\tuple u\in L_A(G)$」→「$E_A[\tuple u]\in L(G)$ がすべての $\tuple u\in L_A(G)$ について成り立つ」。

この結果、量化の順序（「すべての…について，ある…が存在して」）も英語の順に読める。自然さより正確さを優先した（依頼書 §2.4）。

### 4.1 必ず載せる箇所

| 日本語版の行 | 英語原文（英語版の行） | 採った訳 | 理由 |
|---|---|---|---|
| 78–109（要旨） | "measured against the size $\|G\|$ and the rule thickness $\bar\theta_G$ of a presentation $G$ of the target"（71–） | 「それを大きさ $\|G\|$ と規則の厚さ $\bar\theta_G$ に対して測る（これらは標的の表示 $G$ のものである）」 | 「標的の表示 $G$ の大きさ $\|G\|$」と訳すと $G$ が $\|G\|$ より先に出る。括弧で「of a presentation $G$」を後置した。括弧内は「of」の言い換えで、内容の追加ではない |
| 同上 | "each target has characteristic data of length $O(\|G\|^2\bar\theta_G)$ for each of its reduced good presentations $G$ of bounded rank" | 「各標的は長さ $O(\|G\|^2\bar\theta_G)$ の特徴データを，ランク有界なその既約な良い表示 $G$ のそれぞれについてもち」 | 「各標的」「各表示」の量化の順を英語どおりに保った（データは表示ごと） |
| 同上 | "over an alphabet of at least $4f+1$ letters (two at fan-out one) and under every typing, some finite targets with near-minimal presentations need data of length $\Omega(\cdot)$" | 「$4f+1$ 文字以上（ファンアウト1では2文字）のアルファベット上で，かつすべての型付けの下で，最小に近い表示をもつある有限の標的は…を必要とし」 | 「すべての型付け」→「ある標的」の順（型付けごとに標的がある）を保った。括弧内は英語どおり「2文字」とだけ書き、「以上」は主文から読む |
| 同上 | "local groups are exactly the pseudovarieties of finite semigroups with uniformly polynomial characteristic data, and hence exactly those whose classes are identifiable …" | 「局所群は一様に多項式の特徴データをもつ有限半群の擬多様体にちょうど一致し，したがってそのクラスが多項式時間・厚データ同定可能なものにちょうど一致する」 | 英語の主語（local groups）をそのまま主語にした。数学的には「その性質をもつ擬多様体は $\mathbf{LG}$ に含まれるものにちょうど一致する」の意味だが、言い換えはしなかった |
| 同上 | "outside them, targets … need data of length exponential in $n$, for every set-driven reconstruction operator that has characteristic samples throughout the class" | 「それらの外では，…標的が，$n$ について指数的な長さのデータを必要とする．これは，クラス全体で特徴標本をもつすべての集合駆動型再構成作用素について成り立つ．」 | 「for every operator」が文末にあり、標的（作用素によらず固定）より広い作用域をもつことを、別文「これは…について成り立つ」で表した |
| 同上 | "under any fixed typing, all but finitely many of its members fail to be tuple-substitutable there, and no target there keeps their long word as the only one of its type" | 「任意の固定した型付けの下で，その成員のうち有限個を除くすべてはそこでタプル代入可能でなく，そこでのどの標的も，それらの長い語をその型の唯一の語として保たない」 | 否定（no target）を「どの標的も…保たない」と全称否定で訳した |
| 165–169（定理 A） | "every $L\in\Cmcf{f}{s}$ has characteristic data of total length $O(\|G\|^2\bar\theta_G)$ for every reduced good presentation $G$" | 「すべての $L\in\Cmcf{f}{s}$ は，総長 $O(\|G\|^2\bar\theta_G)$ の特徴データを，すべての既約な良い表示 $G$ についてもつ」 | 初稿は「すべての $G$ について，総長…のデータをもつ」と訳したが、$G$ が $O(\cdot)$ より先に出るので英語の順に直した。量化は「すべての $L$、すべての $G$」で変わらない |
| 172–186（定理 B） | (i) "for every typing $s$ there are finite targets in $\Cmcf{f}{s}$, with presentations within a constant factor of the smallest reduced good ones, whose characteristic samples all have length $\Omega(\cdot)$" | 「すべての型付け $s$ について，$\Cmcf{f}{s}$ の有限の標的であって，最小の既約な良い表示の定数倍以内の表示をもつものが存在し，その特徴標本はすべて長さ $\Omega(\cdot)$ をもつ」 | ∀$s$ ∃標的 ∀特徴標本 の順を保った。(ii) の "under the alphabet condition of (i), by the targets of (i)" は「(i) のアルファベットの条件の下で，(i) の標的によって」と語順どおり |
| 188–204（定理 C） | (i) "admits uniform polynomial characteristic-data length iff it is contained in $\mathbf{LG}$" | 「…一様多項式特徴データ長を許すのは，それが $\mathbf{LG}$ に含まれるとき，かつそのときに限る」 | iff を「…とき，かつそのときに限る」で統一（本文全体で同じ） |
| 同上 | (ii) "for a typing $s_U$ onto the two-element semilattice $U_1$" | 「型付け $s_U$（二元半束 $U_1$ の上への）について」 | $s_U$ を $U_1$ より先に出すための後置 |
| 同上 | (ii) "…whose characteristic samples all have length at least $3\cdot2^n-1$, for every set-driven operator with characteristic samples throughout the class" | 「…その特徴標本がすべて長さ $3\cdot2^n-1$ 以上をもつものが存在する．これは，クラス全体で特徴標本をもつすべての集合駆動型作用素について成り立つ」 | 要旨と同じ扱い。標的の存在が作用素に依存しないことを（英語と同様に）文末の「すべての作用素について」で表した |
| 1924–1934（定義 `def:uniform-polydata`） | "if for every nonempty finite alphabet $\Sigma$ and every surjective typing $s$ with $\mathsf S\in\mathbf V$ there is a polynomial $p=p_{f,r_{\max},s,\Sigma}$ such that for every $L\in\Cmcf{f}{s}$ and every reduced good … presentation $G$ of $L\cap\Sigma^+$, the operator … has a characteristic sample $F$ for $L$ with $\|F\|_+\le p(\|G\|,\bar\theta_G)$" | 「すべての空でない有限アルファベット $\Sigma$ と，すべての全射な型付け $s$ で $\mathsf S\in\mathbf V$ なるものについて，ある多項式 $p=p_{f,r_{\max},s,\Sigma}$ が存在して，すべての $L\in\Cmcf{f}{s}$ と，すべての既約な良い…の表示 $G$（$L\cap\Sigma^+$ の）について，作用素…が特徴標本 $F$ を $L$ に対して $\|F\|_+\le p(\cdot)$ なるものとしてもつ」 | ∀Σ ∀$s$ ∃$p$ ∀$L$ ∀$G$ ∃$F$ の順を一字も入れ替えずに保った。$p$ が $L,G$ に依存しないことはこの順序でのみ読める |
| 1936–1938（直後の段落） | "The quantifiers are ordered as written: $p$ may depend on $f$, $r_{\max}$, $\Sigma$ and the typing $s$, but not on the target $L$ or the presentation $G$." | 「量化子は書かれたとおりの順序である：$p$ は $f$，$r_{\max}$，$\Sigma$ および型付け $s$ に依存してよいが，標的 $L$ にも表示 $G$ にも依存しない．」 | "not on $L$ or $G$" を「$L$ にも $G$ にも依存しない」（両方の否定）と訳した |
| 2035–2058（系 `cor:iptd`） | 前文 "Let $\mathcal R$ consist of the pairs $(G,z)$ of a bit $z\in\{0,1\}$ and either … $G$ or a fixed grammar $G_\emptyset$ without rules" | 「$\mathcal R$ を対 $(G,z)$ からなるものとする．ここで対は，ビット $z\in\{0,1\}$ と，…MCFG $G$ または規則をもたない固定した文法 $G_\emptyset$ のいずれかとからなる」 | 数式順（$(G,z)$, $z$, $G$, $G_\emptyset$）を保つため「ここで対は…」と分けた |
| 同上 | "…represented by $(G,[\eps\in L])$ with $G$ a … presentation of $L\cap\Sigma^+$, or $G=G_\emptyset$ if $L\cap\Sigma^+=\emptyset$" | 「…$(G,[\eps\in L])$ で表される．ここで $G$ は…表示（$L\cap\Sigma^+$ の）であるか，または $G=G_\emptyset$ である，$L\cap\Sigma^+=\emptyset$ ならば．」 | 条件節「ならば」を後置して数式順を保った |
| 同上 | (i) "the algorithm returning $(G^+_K,[\eps\in K])$ …, or $(G_\emptyset,[\eps\in K])$ if $K\cap\Sigma^+=\emptyset$, identifies … in polynomial time and thick data for the class $\mathcal R$" | 「…$(G^+_K,[\eps\in K])$ を返し，または $(G_\emptyset,[\eps\in K])$ を返す（$K\cap\Sigma^+=\emptyset$ ならば）アルゴリズムは，…を，クラス $\mathcal R$ について，多項式時間・厚データ同定する」 | 同上 |
| 同上 | (ii) "no algorithm, whatever its running time, satisfies the data condition of IPTtD for …" | 「どのアルゴリズムも，その実行時間がどうであれ，IPTtD のデータ条件を…について満たさない」 | 全称否定。実行時間を問わないことを英語どおりに保った |
| 同上 | (iii) "the following are equivalent: $\mathbf V\subseteq\mathbf{LG}$; for every typing $s$ with $s(\Sigma^+)\in\mathbf V$, the class … is IPTtD" | 「次は同値である：$\mathbf V\subseteq\mathbf{LG}$；すべての型付け $s$ で $s(\Sigma^+)\in\mathbf V$ なるものについて，クラス…は IPTtD である」 | IPTtD は英字のまま（依頼書 §2.7）。「is IPTtD」を「IPTtD である」とした |
| 同上（証明 (ii)） | "Such an algorithm has a characteristic sample for every member of the class, since …" | 「そのようなアルゴリズムはクラスのすべての成員に対して特徴標本をもつ．なぜなら…」 | 英語の「Such an algorithm」は文脈上「データ条件を満たすアルゴリズム」を指すと読めるが、指示の範囲を補わずに「そのような」と写した |
| 1060–1084（命題 `prop:typed-separation`） | (ii) "$L_{\mathrm{sep}}$ is $(f,s)$-tuple-substitutable for every $f\ge1$; hence $L_{\mathrm{sep}}\in\Cmcf{f}{s}$ for every $f\ge2$" | 「$L_{\mathrm{sep}}$ は $(f,s)$-タプル代入可能である，すべての $f\ge1$ について；したがって $L_{\mathrm{sep}}\in\Cmcf{f}{s}$ がすべての $f\ge2$ について成り立つ」 | $f\ge1$ と $f\ge2$ の区別（代入可能性は全 $f$、クラス所属は $f\ge2$）を保ち、数式順も保った |
| 同上 | (iii) "is not $(f,s_{\mathrm{triv}})$-tuple-substitutable for any $f\ge1$" | 「$(f,s_{\mathrm{triv}})$-タプル代入可能でない，どの $f\ge1$ についても」 | 否定の作用域（すべての $f$ で否定）を「どの…についても…でない」で表した |
| 同上 | 定義式 "\[ L_{\mathrm{sep}}:=\{\ldots\}.\]" の直前 "and let" | 「…ものとし，次のようにおく．」 | 英語の別行立て数式の末尾の「.」は数式の内部にあるので、それを写し、日本語の述語を数式の前に置いた |
| 1491–1510（補題 `lem:heavy-node-count`(ii)） | "Suppose that for every $\lambda$-minimal $T$ and every antichain $Q$ of heavy nodes of $T$ there is $Q_0\subseteq Q$ with $|Q\setminus Q_0|\le c'$ such that, if $|Q_0|>c$, the subtrees at the nodes of some nonempty $J\subseteq Q_0$ can be replaced simultaneously by derivations, from the same nonterminals, of tuples of total length at most $\bar\theta_G$ without changing the root $\lambda$-vector." | 「次を仮定する：すべての $\lambda$-極小な $T$ と，すべての反鎖 $Q$（$T$ の重い節点の）について，ある $Q_0\subseteq Q$ で $|Q\setminus Q_0|\le c'$ なるものが存在して，$|Q_0|>c$ ならば，ある空でない $J\subseteq Q_0$ の節点における部分木を同時に，同じ非終端記号からの導出であって総長高々 $\bar\theta_G$ のタプルの導出で置き換えることが，根の $\lambda$-ベクトルを変えずにできる．」 | ∀$T$ ∀$Q$ ∃$Q_0$（$|Q_0|>c$ → ∃$J$ …）の順を保った。$Q_0$ が $|Q_0|>c$ の判定より前に選ばれ、$J$ はその後に存在するという入れ子を崩さないようにした |
| 同上 | "Then every heavy antichain of a $\lambda$-minimal derivation has at most $c+c'$ elements, and $(\mathrm R_\beta^\lambda)$ holds with $\beta=\ldots$" | 「このとき，$\lambda$-極小な導出のすべての重い反鎖は高々 $c+c'$ 個の元をもち，$(\mathrm R_\beta^\lambda)$ が $\beta=\ldots$ について成り立つ」 | at most を「高々」で統一 |
| 2183–2189（未解決問題 `op:fanout-two`） | "Is $\mathbf{LG}$ the pseudovariety boundary at fan-out $f$, that is, does every pseudovariety of finite semigroups not contained in $\mathbf{LG}$ fail to have uniform polynomial characteristic-data length at fan-out $f$ and rank $r_{\max}$" | 「$\mathbf{LG}$ はファンアウト $f$ における擬多様体の境界であるか．すなわち，$\mathbf{LG}$ に含まれない有限半群のすべての擬多様体は，ファンアウト $f$ かつランク $r_{\max}$ で一様多項式特徴データ長をもたないか」 | 「every … fail to have」を「すべての…は…をもたないか」（全称の下の否定）と訳した。「すべてが…をもつとは限らない」（部分否定）と読まれないよう、否定を述語に付けた |

### 4.2 その他の判断箇所

| 日本語版の行 | 英語原文（英語版の行） | 採った訳 | 理由 |
|---|---|---|---|
| 150–151 | "Local groups, finite semigroups $\mathsf T$ with $e\mathsf Te$ a group for every idempotent $e$"（142–143） | 「局所群，すなわち有限半群 $\mathsf T$ であって，$e\mathsf Te$ がすべてのべき等元 $e$ について群となるもの」 | 数式順（$\mathsf T$, $e\mathsf Te$, $e$）を保つ |
| 214, 1962, 1987 | "the \emph{if} direction" / "the \emph{only if} direction" | 「\emph{if} の方向」「\emph{only if} の方向」 | 定理 C(i) の iff の各方向を指す術語として英字を残した（「十分性」などと言い換えると補足になるため） |
| 2142 | "the $\delta+j\le n-1$ copies immediately before the first $u_{\mathtt a}$ of the second copy of $\varphi(W_{n-1})$, which is preceded by at least $n-1$ copies of $u_{\mathtt b}$"（2147–2149） | 「…最初の $u_{\mathtt a}$（$\varphi(W_{n-1})$ の二番目の複製の）の直前にあるものとする．そしてそれの前には少なくとも $n-1$ 個の $u_{\mathtt b}$ の複製がある．」 | 英語の "which" が「最初の $u_{\mathtt a}$」と「二番目の複製」のどちらを指すかは文法上あいまいである（どちらで読んでも主張は正しい）。あいまいさを解消せず「それ」で写した |
| 2507 | "Let $\mathcal O$ be the set of ordered pairs …, of types on a common line, If $n\ge m_{|\mathcal O|}$"（2514–2515） | 「$\mathcal O$ を…の集合とする，$n\ge m_{|\mathcal O|}$ ならば」 | **英語原文の誤植**（文末がピリオドでなくコンマ、次の "If" が大文字）。原文どおりコンマのまま写した。英語版の修正は著者の判断に委ねる |
| 1091–1093 | "$\psi$ … and let $R:=\ldots$. Then $L_{\mathrm{sep}}=R\cap\psi^{-1}(P)$ with $P:=\ldots$, and $R$ is the path language from $0$ to $3$ of the graph on $\{0,1,2,3\}$ …"（1090–1093） | 「$R$ は道の言語（$0$ から $3$ への）であって，グラフは $\{0,1,2,3\}$ 上のもので，…」 | 数式順を保つため、修飾を分けて後置した |
| 1994–1998 | 「IPTtD」の定義の段落（1999–2003） "call a class identifiable in polynomial time and thick data (IPTtD) if …" | 「クラスが多項式時間・厚データ同定可能（IPTtD）であるとは，…をいう，と定める」 | 他者の定義の引用であることを「と定める」で保った |
| 全体 | "witness"（合成証拠、証拠集合）と "witness family"（下界の例の族）、"non-context-free witnesses" | いずれも「証拠」 | 依頼書 §4 の「合成証拠／証拠集合」に合わせて全体を「証拠」で統一した。下界の族（定理 C(ii) の族）も「証拠族」とした |
| 全体 | "presentation" | 「表示」 | 依頼書 §4 のとおり。「文法表示」とは書かず「表示」で統一 |
| 全体 | "canonical"（Canonical tuple/context と、作用素についての "canonical operators"） | 前者は「標準タプル／標準文脈」、後者は「標準の作用素」 | 依頼書 §4 の「標準タプル」に合わせ、作用素も同じ語にした（英語でも同じ語） |
| 全体 | "at most / at least" | 「高々」「少なくとも」 | 一貫させた。「〜以上」は "at least … letters" など数え上げの自然な箇所でのみ用いた（例：「$4f+1$ 文字以上」） |
| 全体 | 証明の題 `\begin{proof}[Proof of Lemma~\ref{…}]` | `\begin{proof}[補題~\ref{…} の証明]` | 依頼書 §3 の \ref の前の語の対応に従った |
| 全体 | "Remark" | 「注意」 | 依頼書 §3 の表に従った（v1 の日本語版は「備考」） |
| 2235（謝辞） | "Makoto Kanazawa and Ryo Yoshinaka" | 「Makoto Kanazawa 氏と Ryo Yoshinaka 氏」 | 依頼書 §2.7 に従い人名は英字のまま。敬称「氏」だけを日本語の文の形のために付けた |
| 71（著者欄） | "Independent Researcher, Tokyo, Japan" | 「独立研究者，東京，日本」 | 著者名とメールアドレスは英字のまま |

## 5. プリアンブルで英語版から変えた点

1. `\documentclass[11pt]{article}` → `\documentclass[11pt,a4paper]{ltjsarticle}`（依頼書 §3）。
2. 定理環境の表示名だけを日本語に（定理・補題・命題・系・定義・注意・例・未解決問題、`mainthm` は「定理」）。番号付けの指定（`[section]`、共有カウンタ、`\Alph{mainthm}`）は英語版と同一。
3. `\renewcommand{\proofname}{証明}` を追加。
4. **`\appendix` の番号の修正（追加）**：ltjsarticle の `\appendix` は `\thesection` を「付録A」のように定義し直すので、そのままでは付録の定理番号や参照が「付録A.6」と印字され、英語版の「A.6」と一致しない（本文の「付録~\ref{…}」も「付録 付録A」になる）。次の 3 行を加えて `\thesection` を `\@Alph\c@section` に戻した。検査 8 で全ラベルの印字番号が英語版と一致することを確認した。
   ```latex
   \makeatletter
   \g@addto@macro\appendix{\gdef\thesection{\@Alph\c@section}}
   \makeatother
   ```
5. `\usepackage` とマクロ定義（`\Wit`, `\Cmcf`, `\D`, `\out`, `\tuple`, `\blank`, `\eps`, `\pausesym`, `\fan`, `\YSub`, `\YSL`, `\evalmap`, `\cutpos`）は**すべて英語版のまま**。`fontenc`（T1）、`lmodern`、`microtype` も残した（LuaLaTeX でエラーにならないため）。microtype については §2 の警告が出る。警告をなくすには `microtype` を外すのが最小の変更だが、依頼書の「問題になるなら最小限だけ差し替え」に当たるほどの問題ではないと判断して残した。外すかどうかは著者の判断に委ねる。

## 6. 未完了・未確認の点

- **意味の正しさは機械検査の外**：§2 の検査は構造・数式・番号・英文の残りを保証するが、日本語の文が英語の論理を正しく写しているかは保証しない。全文を作成者（Claude）が一度訳し、数式順の修正の際に該当箇所を読み直したが、**第三者による日本語の通読（英語との突き合わせ）はまだ行っていない**。特に §4.1 の箇所を優先して確認してほしい。
- 英語原文の誤植（英語版 2514 行のコンマ）は日本語版にもそのまま残っている（§4.2）。
- Overfull 1.6pt が 1 か所（数式を変えられないため、§2）。
- `README.md` の更新は行っていない（依頼書 §7、著者が行う）。
- ビルドに使った TeX 環境は TeX Live 2023（Ubuntu パッケージ、LuaTeX-ja は `texlive-lang-japanese`）。著者の環境で LuaTeX-ja の版が異なると、ページ数が 49 から多少ずれる可能性がある。
- 反映の状況（ブランチ・PR）は §7 に記す。

## 7. 反映

- ブランチ `japanese-v2-2026-11-06` に、新規 4 ファイルのみをコミット（`main.tex` を含む既存ファイルの変更なし）。
- `main` への Pull Request：#102（https://github.com/growupkuriyama-hub/Papers/pull/102）。`main` には push していない。マージは著者が行う。

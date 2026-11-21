# Fableへの研究依頼：fan-out 2におけるLG境界の中心的開問題を自由に攻めてください

**研究課題：** Grammatical inference / multiple context-free languages / positive-data learning / finite semigroup typing  
**優先事項：** 新しい数学的着想と、反例・定理・厳密な証明。既存研究の追試や論文化ではありません。  
**作業モード：** 独立した研究者として自律的に探索してください。探索方針・手法・順序はあなた自身が決めて構いません。

---

## 依頼の核心

あなたに研究してほしいのは、次の**現に未解決の問題**です。以前のClaudeが使った証明戦略、特殊クラス、計算実験に縛られず、必要なら出発点を変えて構いません。問題を肯定的に解く構成も、否定的に解く一般上界も、どちらも歓迎します。思いつく限り異なる数学的観点を試してください。

> **Open problem `op:fanout-two`.** Fix a fan-out bound \(f\ge2\) and maximal rule rank \(r_{\max}\ge2\). Is the pseudovariety \(\mathbf{LG}\) exactly the boundary for **uniform polynomial characteristic-data length** among classes of \((f,s)\)-tuple-substitutable multiple context-free languages? Equivalently, does every pseudovariety of finite semigroups \(\mathbf V\not\subseteq\mathbf{LG}\) *fail* uniform polynomial characteristic-data length at fan-out \(f\) and rank \(r_{\max}\)?

LG側の多項式上界はすでに全fan-outで証明されています。未解決なのは、**LGの外側で一様多項式上界が必ず破れるかどうか**です。

特に \(f=2\), \(r_{\max}=2\) は最重要の出発点です。ここで強い下界が得られても、それを \(f\ge3\) に移す際には別途証明が必要です。

### 一つの十分な解決経路（これに限定しない）

\(U_1=\{1,\zeta\}\), \(\zeta^2=\zeta\) を単位元1と零元\(\zeta\)を持つ2元モノイドとし、固定の全射型付け

\[
 s_U:\{a,b,c\}^+\twoheadrightarrow U_1,
 \quad s_U(a)=s_U(b)=1,\quad s_U(c)=\zeta
\]

を用いる。次のすべてを満たす \(L_n,G_n\) を構成できれば、重要な肯定的解答への道が開きます。

1. \(L_n\in\mathcal C^{\mathrm{mcf}}_{2,s_U}\)。とくに**2穴の組代入可能性**を証明する。
2. \(G_n\) は \(L_n\cap\Sigma^+\) の **reduced good** なMCFG提示で、fan-out \(\le2\)、rule rank \(\le2\)。
3. \(\|G_n\|\) と元の文法の厚さ \(\bar\theta_{G_n}\) は \(n\) の多項式以下。
4. 全ての正例の特徴標本が、\(\|G_n\|,\bar\theta_{G_n}\) に関して**超多項式**の総長を強制されることを証明する。

例えば、実現される型 \(1\) の最短語長 \(\mu_1(L_n)\) が超多項式であれば、現行論文の `prop:rare-type` により十分です。ただし**その型の語が唯一である必要はありません**。また、希少型に依存せず、\(L'_n\subsetneq L_n\)（両方とも同じ目標クラス）の区別語が全て長いことから下界を示す方法もあります。さらに別の下界証明手段を創出して構いません。

**重要：** \(U_1\) の特定の型付けで一様上界が破れることは肯定的解答のための有力な十分条件です。一方、ある一つの \(U_1\) 型付けについて多項式上界を示しただけでは、一般の開問題への否定的解答にはなりません。反対方向を主張するなら、擬多様体・型付けの全称量化を正確に扱ってください。

---

## 一次資料：GitHubを読んでから研究してください

**Repository:** https://github.com/growupkuriyama-hub/Papers  
**Paper #2 directory:** https://github.com/growupkuriyama-hub/Papers/tree/main/02-v4-fixed-s-mcfg/v2

まず以下の3件を優先して確認してください。閲覧可能ならGitHubから直接読むか、リポジトリをcloneしてください。

1. **現行の正式な問題・定義・既知結果（最優先の権威ある資料）**  
   [main.tex](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v4-fixed-s-mcfg/v2/main.tex)  
   とくに `def:grammar-properties`、`def:tuple-substitutable`、`def:uniform-polydata`、`prop:rare-type`、`lem:distinguishing`、`lem:power-transfer`、`thm:doubling-no-lift`、`op:fanout-two`。本文内の完全な仮定と証明を読んでください。  
   [正式なopen problem付近](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v4-fixed-s-mcfg/v2/main.tex#L2130-L2148) ／ [2穴定義付近](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v4-fixed-s-mcfg/v2/main.tex#L486-L529) ／ [非持ち上げ定理](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v4-fixed-s-mcfg/v2/main.tex#L2044-L2113)
2. **この研究の現在位置と既存結果の状態**  
   [HANDOFF_CURRENT.md](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v4-fixed-s-mcfg/v2/HANDOFF_CURRENT.md)  
   古い記録よりもこれを優先してください。2026-11-15時点で `op:fanout-two` はOPENです。
3. **特殊クラス \(U_2\) の研究用上界・独立監査（重要な既知の障壁だが、探索の必須路線ではない）**  
   [U₂ independent theorem note](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v4-fixed-s-mcfg/v2/reviews/theorem_U2_overlapping_projections_standalone_2026-11-15.md)  
   [U₂ scope and proof status](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v4-fixed-s-mcfg/v2/reviews/STATUS_U2_STANDALONE_FORMALIZATION_2026-11-15.md)  
   この結果は、\(\Sigma=\{a,b,c\}\)、\(A=\{a,c\}, B=\{b,c\}\)、長さ2の射影bigramデータで決まる**特殊言語クラス**の多項式代表長上界に関する手証明案（独立監査 `VALID WITH CLARIFICATIONS`）です。**一般の \(U_1\) 型付けやLG境界を証明したものではありません。** 必要であればこの上界から脱出するような構成を考えてください。

**追加のGitHub資料（必要になったら参照）**

- [第十一段：原報告・Python・監査・ログの完全ソース束](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v4-fixed-s-mcfg/v2/reviews/ROUND11_SOURCE_BUNDLE_2026-11-15.md)
- [第十一段：残余ケースを閉じるClaude原報告](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v4-fixed-s-mcfg/v2/reviews/claude_fanout2_round11_residual_report_2026-11-15.md)
- [第十一段：独立数学監査](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v4-fixed-s-mcfg/v2/reviews/audit_claude_fanout2_round11_independent_2026-11-15.md)
- [第十段：上界統合のClaude原報告](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v4-fixed-s-mcfg/v2/reviews/claude_fanout2_round10_U2_integration_report_2026-11-14.md)
- [第九段：P1/B6の原報告](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v4-fixed-s-mcfg/v2/reviews/claude_fanout2_round9_P1_B6_report_2026-11-14.md)
- [過去の研究用原稿にある「希少型で唯一の語」の剛性分類（**現行原稿ではなく履歴資料**）](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v4-fixed-s-mcfg/v2/parked/2026-11-06_focus/main_before_focus_59pp.tex) の `lem:unique-word-rigid`、`prop:unique-two-letter-shapes`、`thm:app-singleton`。これを定理として使う場合は、現行仮定との整合性を独立に確認すること。

GitHubの閲覧権限やネットワークの問題でこれらを開けない場合は、**読めたと装わず**その旨を報告し、必要なファイルの添付を要求してください。本文を読めないまま、曖昧な要約だけから定理を「証明済み」として扱わないでください。

注：直近の「第十二段」の下界候補探索は**まだGitHub未収録**です。その暫定的な知見は、新しい独立発想に先入観を与えないため、ここでは前提にしません。

---

## 自由研究への要望

ここから先の研究戦略は、あなたに任せます。既存のClaudeによる上界補題の延長や、小さい候補文法を大量生成する方式を繰り返す必要はありません。研究対象を適切に抽象化し、別分野の道具を持ち込むことも歓迎します。**中心的開問題がYESともNOとも仮定せず**、どちらが数学的に見込みがあるかを自分で評価してください。

候補の例としては、新規のMCFG族、組分布の代数、非可換な不変量、語の配置制約、有限指数の合同、符号化に頼らない下界、区別可能な部分標的、一般的な短縮定理などが考えられますが、**これは発想を制限するリストではありません**。あなたがもっとよい見方を発見した場合は、これらを無視して構いません。

単なる文献解説ではなく、**自身の定義・補題・構成・反例・計算機実験から前進すること**を目指してください。既存論文や過去のClaudeの主張が誤っていれば、遠慮なく反証してください。重要な反例一つでも価値があります。

### 数学的に譲れない要件

- **組代入可能性は全称命題。** 各 \(d=1,2\)、すべての同型タプル \(\mathbf x,\mathbf y\in(\Sigma^+)^d\) について、受理可能文脈 \(E\in\mathcal E_d\) を共有したら、その \(d\) 次分布が一致する必要があります。2穴の間の固定部分は **非空**。適切な反例は \(\mathbf x,\mathbf y,E,F\) と各充填語を明記してください。
- **文法パラメータを取り違えない。** `good` は ε-free、nondeleting、nonpermuting、nonmerging。fan-outは非終端の成分数、rankは右辺の非終端出現数です。\(\bar\theta_G\) は**元の提示文法**の厚さ。生成する長い語だけを示しても下界にはなりません。
- **既存のno-lift定理を尊重する。** 古い\(W_n\)や、そのletter-disjoint morphismの単純な持ち上げは一般に破綻します。ただし冪移動は語長とParikhベクトルを保存するので、「同じ型の語に短いものが存在する」と結論づけてはいけません。
- **十分条件と必要条件を分ける。** 「唯一の型1語」を要求する必要はありません。特別な族を一つ否定しても一般の超多項式下界不可能性は言えず、一つの特殊クラスで多項式上界を証明してもLG境界は否定されません。
- **有限実験は証明ではない。** 実験で真らしい一般命題には証明義務を付ける。反例・失敗候補には一般の\(n\)への延長と固定した型付けの条件を確かめる。証明のない補題を暗黙に引用しない。
- **量化の順番を守る。** 定義 `def:uniform-polydata` において多項式 \(p\) は \(f,r_{\max},s,\Sigma\) に依存してよいが、\(L,G\) には依存できません。固定の型付けとアルファベットのまま超多項式族を作ることが重要です。

### 成果をどう残してほしいか

途中で方針を自分で切り替えて構いません。時間や計算資源の使い方も自律的に決めてください。最終的に以下を残してください。

1. **日本語の数学研究報告 `fable_fanout2_open_problem_report.md`**。研究した主なアイデア、正確な定義、証明済み命題、条件付き命題、反例、未解決の障壁、現在の最も有望な道筋を明確に区別する。
2. **有望な数学的成果について再現可能な証明・反例証明書**。MCFG規則、長さ・厚さの計算、2穴分布の一般論証、具体的な反例四つ組など、第三者が追跡できる内容にする。
3. **必要に応じてコードと実行ログ**。有界検査を用いた場合、探索した範囲、シード、実行方法、成功・失敗例を残す。Lean等の形式化や外部研究文献の利用も自由だが、行ったことだけを正確に記録する。
4. **最後に短い結論**：`SOLVED YES`、`SOLVED NO`、`NEW THEOREM BUT OPEN`、`OBSTRUCTION/COUNTEREXAMPLE ONLY`、`INCONCLUSIVE` のいずれかを選び、解決した対象と未解決の部分を量化込みで述べる。

**研究成果はまだ論文化しないでください。GitHubへの書き込み・既存原稿の修正はしないでください。** 既存資料は読み取り専用で利用し、成果物はこのセッションで提示してください。

---

## 最初の行動

最初に `main.tex` の正式な定義・open problem・no-lift定理と `HANDOFF_CURRENT.md` を読み、上記の問題設定に誤りがないか確認してください。その後は、あなた自身が最も可能性を感じる方向に、**自律的な数学研究として**取り組んでください。

**求めているのは、以前の研究の続きの作業員ではなく、別の視点から中心的開問題に挑む研究者です。**

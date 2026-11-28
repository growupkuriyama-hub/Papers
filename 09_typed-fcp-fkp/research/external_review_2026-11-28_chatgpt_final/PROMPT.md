# 依頼：論文 09 の最終修正（2026-11-28 夜）の査読

あなたは形式言語理論と文法推論（分布学習、Kanazawa–Yoshinaka の FCP・FKP、所属質問つき学習）に詳しく、言語学にも通じた査読者です。JoLLI（Journal of Logic, Language and Information）へ投稿する直前の論文について、**最後の修正だけ**を読み、誤りが残っていないか、新しく入っていないかを確かめてください。

背景：この論文では、同じ日の編集で誤りが入ることが二日続きました（11-27 に 3 件、11-28 に 5 件。どれも文の圧縮・言い換えで、仮定や根拠が落ちる、主張の範囲が広がる、書誌を誤る、という種類）。今回の修正もその日の夜の編集です。好意的に読まず、誤りを探すつもりで読んでください。

## 対象

- リポジトリ（公開）：https://github.com/growupkuriyama-hub/Papers
- 前回の査読の対象：`5cdba4f16c1ae8ea0d29f413908d8b62cd99ed52`
- **今回の対象**：`0f10a5e4b9c9dd69259c824646a62693763c9757`
  - 原稿：https://github.com/growupkuriyama-hub/Papers/blob/0f10a5e4b9c9dd69259c824646a62693763c9757/09_typed-fcp-fkp/main.tex
  - PDF：同じフォルダの `main.pdf`（24 頁）
  - 差分：https://github.com/growupkuriyama-hub/Papers/compare/5cdba4f...0f10a5e （`09_typed-fcp-fkp/main.tex` だけ。`japanese/` と `research/` は対象外）
- 行番号は、すべて `0f10a5e` の `main.tex` の物理行番号で書いてください。
- 前回の査読の指摘（C01〜C16）は `09_typed-fcp-fkp/research/external_review_2026-11-28_chatgpt_diff/findings.csv` にあります。**これは読んでかまいません**（修正が指摘を閉じたかの確認に使う）。それ以外の `research/` 以下（とくに `REVIEW_RESPONSE_*`）は、判定を書き終えるまで開かないでください。
- §5 の確認には、添付の Kanazawa の論文（`kanazawa-invited.pdf`、WoLLIC 2023 の著者稿）を使ってください。

## 変更箇所（`0f10a5e` の行番号）

| 区切り | 行 | 内容 |
|---|---|---|
| **E1** Abstract | l.73–95 | 全面的に書き直した（JoLLI の読者向け）。問いを先に出し、$M_n$ を「abstract licensing condition」として導入、二つの尺度を「Measured by …」と「In total length …」で書き分け、括弧の記号を言葉にした。248 語 |
| **E2** 序論 | l.154–155、207–208、232–234、296–297、354–355 | 前回の C03・C04・C05・C06・C07 への修正 |
| **E3** §5 | l.1066–1071、1076–1078、1083 | 前回の C08・C10（Algorithm 3 の論法と記法）、C09（(d†′) についての結論の範囲）、C11（注意 5.6 の根拠）への修正 |
| **E4** §6 | l.1489 | 前回の C12（$x$ の範囲） |
| **E5** 参考文献 | l.1800、1886、1908 | 前回の C13（Coste–Nicolas の会議年）、C14（Ogden の誌名）、C15（Yoshinaka 2015 の出版者） |

## とくに気になっている点

1. **Abstract（E1）の各文が本文の定理を超えていないか。** 照合先は、序論の定理 A（l.185 付近、とくに (i) の生成規則の数と (ii) の積の下界）、定理 B（l.258 付近）、定理 C（l.277 付近、(iii) と (iv)）、命題 4.2(c)、定理 4.7、定理 6.8、§5 の系と命題 5.5。具体的には：
   - 「frames need only $n+1$ categories, each named by one frame of length at most $2n$, and right-hand sides of length at most $3n$ (though exponentially many productions)」は定理 A(i) と一致するか。「need only」が最小性を主張しているように読めないか。
   - 「for exemplars the product of the three quantities is at least exponential in $n$, tight up to a factor $O(n)$」の「the three quantities」は何を指すか明確か（定理 A(ii) は $\rho|N|\max(\kappa,1)$）。「tight」の主張（定理 A(iii) と注意）と合うか。
   - 「**Hence** specific learners need exponentially much data」：§5 の下界のうち、$\mathsf{Rec}_s$ と主学習器の下界は積の下界から出るが、双対学習器の下界（命題 5.5）は別の論法による。「Hence」は不正確か。代案（例：This yields exponential lower bounds on the data of specific learners）と比べて判定する。
   - 「In total length, an observer recording whether an expression is marked admits a frame presentation of size $O(n^2)$, whereas every exemplar presentation needs exponential size under any observer」：定理 C(iii) は「typed under any observer or untyped」。「under any observer」で型なしの場合が含まれると読めるか。
   - 「without an observer that distinguishes a marked leaf from an unmarked pair of leaves, frame presentations are exponential too」：定理 C(iv) の条件（観測器なし、または $\lceil a\rceil$ と $\lfloor aa\rfloor$ に同じ型を与える観測器）を正しく言い換えているか。「a marked leaf」「an unmarked pair of leaves」が $\lceil a\rceil$、$\lfloor aa\rfloor$ を指すと読み手に分かるか。
   - 「The frame upper and exemplar lower bounds extend to suitable one-word deletions」：定理 6.8 の仮定と合うか。
   - 「Refining the observer can only help frames and only hurt exemplars for some, but not all, of the finite context and kernel properties」：定理 B と合うか。
   - 「Our example is an abstract licensing condition」：言語学の査読者に過大な主張と受け取られないか。本文の類比の但し書き（l.160–175 付近、結論）と整合するか。
   - JoLLI の Abstract として：語数（上限 250）、略語と記号（$n$、$O(n)$ 以外の記号が残っていないか）、主語の明確さ、文の長さ。
2. **前回の指摘（C01〜C15）が本当に閉じたか**、修正が新しい誤りを持ち込んでいないか。とくに C06（観測器の必要性）、C08（$Q^{r,s}$ の段階の書き方が Kanazawa の Algorithm 3 の定義と一致するか、「$J$ is fixed at convergence」「once $E$ exhausts $\mathrm{Sub}(M_n)$」の正確さ）、C09（「with this word as the initial set covering the atoms」の「this word」が何を指すか曖昧でないか、結論が正しく限定されているか）、C11（「apply the proof of Lemma 5.1 relative to $L$」で論証が閉じるか）。
3. **Abstract と序論・結論の整合**：Abstract を書き直したことで、序論（l.101–360）や結論（§7）の要約と食い違う箇所（尺度の呼び方、主張の強さ、用語）が生じていないか。

## 判定の書き方

- 区切りごとに表で：`| 行 | 主張・文 | 判定 | 根拠（一、二文） | 修正案 |`。
- 判定は **OK**、**FALSE**（書いてあるとおりには偽）、**GAP**（仮定・参照の不足）、**OVERCLAIM**（本文や典拠より強い）、**UNCLEAR**（誤読されうる）、**STYLE**、**UNCHECKED**。
- 前回の指摘については `| ID | 閉じたか（closed／partly／not） | 理由 |` の表も作る。
- 修正案は差し替える英文で、元と同じくらいの長さで書く。Abstract の修正案を出す場合は、修正後の全文と語数も示す。
- 最後に総合判定を三択で：「このまま投稿してよい」「局所的な修正で投稿してよい（修正の一覧）」「投稿前に大きな見直しが要る（理由）」。

## 成果物

次のファイルを一つの zip にまとめて渡してください（私がリポジトリの `09_typed-fcp-fkp/research/external_review_2026-11-28_chatgpt_final/` に置きます）。

- `review.md`：E1〜E5 と「とくに気になっている点」の結果、前回の指摘の閉じ具合、総合判定（200 行程度まで）
- `findings.csv`：列 `id,section,severity,lines,claim,issue,suggested_fix`、`id` は `F01` から、`severity` は `false`／`gap`／`overclaim`／`unclear`／`style`
- `checks/`：語数などを計算で確かめた場合のコードと出力（任意、Python 標準ライブラリのみ）

会話の途中で止まりそうなら、E1（Abstract）の結果を先に会話に書き出してください。

# 依頼：論文 09 の 2026-11-28 の差分の独立な査読（最終の文面の確認）

あなたは形式言語理論と文法推論（分布学習、Kanazawa–Yoshinaka の FCP・FKP、所属質問つき学習）に詳しく、言語学（韻律音韻論・日本語統語論）にも通じた査読者です。JoLLI（Journal of Logic, Language and Information）に投稿する直前の論文について、**今日 1 日の修正の最終の文面だけ**を独立に読んでください。

背景：前日（11-27）には、同じ日の編集（文の圧縮・言い換え）で誤りが 3 件入りました（例：証明の中の不正確な部分集合の主張、序論の一般形の文で仮定の脱落）。今日も同じ種類の誤りが入っている可能性があります。好意的に読まず、誤りを探すつもりで読んでください。

## 対象

- リポジトリ（公開）：https://github.com/growupkuriyama-hub/Papers
- 査読前の版：`61f8a16b0658abc6fa826ea7cddc4f123e72c64b`（前回の外部査読が対象にした版）
- **今回の対象の版**：`5cdba4f16c1ae8ea0d29f413908d8b62cd99ed52`
  - 原稿：https://github.com/growupkuriyama-hub/Papers/blob/5cdba4f16c1ae8ea0d29f413908d8b62cd99ed52/09_typed-fcp-fkp/main.tex
  - PDF：同じフォルダの `main.pdf`（23 頁）
  - 差分：https://github.com/growupkuriyama-hub/Papers/compare/61f8a16...5cdba4f （`09_typed-fcp-fkp/main.tex` だけを見る。`japanese/` と `research/` は対象外）
- 行番号は、すべて `5cdba4f` の `main.tex` の物理行番号で書いてください。
- 題：Frames versus Exemplars: An Exponential Gap for Syntactic Categories

**独立性**：判定を書き終えるまで、`09_typed-fcp-fkp/research/` 以下（とくに `REVIEW_RESPONSE_*`、`external_review_*`、`KANAZAWA2023_ALG3_ON_Mn_*`、`FINAL_AUDIT_*`）は開かないでください。修正の意図を知らない読者として読むことが目的です。

## 変更箇所（`5cdba4f` の行番号）

| 区切り | 行 | 内容 |
|---|---|---|
| **D1** Abstract | l.72–95 | 二つの尺度（非終端記号の数・右辺と証人の長さの積／全長）で書き分けた。$F_n$ は生成規則が指数個であることを明記。「Both bounds extend to general one-word deletions, the lower one in terms of a prefix length」。248 語（JoLLI の上限 250 語） |
| **D2** 序論 | l.108–110、153–156、168–172、182–183、188–190、203–207、231–234、242–244、295–296、323–325、353–354 | 事例基盤のモデル（Bod、Bybee）の書き方。尺度を学習器のデータの下界が通る量と位置づけた文。厳格層仮説の帰結と典拠の頁、主格要件の例外、多重主格。定理 A(i) の生成規則の数 $2^n+2n-2$。「Exemplars can name the same categories, but only with words as long as $w^*_{n-1}$」。捕獲の説明（補題 4.4・4.5 との一致）と「Theorem A does not count productions; the gap in total length is Theorem C」。所属質問の文。双対学習器の仮定（型なしまたは $s_U$、$r\ge2$、収束時）。定理 C の後の「By (iii) and (iv), an observer yields a gap in total length and is needed for it」。イデアル制限の仮定（初期記号はどの右辺にも現れない）。先行研究の比較（Clark 2016） |
| **D3** §5 | l.1063–1076、1078–1083 | 命題 5.5 の後：Kanazawa (WoLLIC 2023) の Algorithm 3 に同じ論法が通ること、拡張正則の演算のもとでの $H_n$ の SPP、原子の長さ、$k\ge8$ での同定、性質 (d†′) についての結論。注意 5.6 の圧縮 |
| **D4** §6 | l.1483–1496 | 定理 6.11 の後：因子 $\ell+1$ は除けないこと（型なしの $H_n$ に枠を二つずつ）。補題 6.9 の証明が枠を使うのは区別する文脈だけなので、成分が $\{c\}^\lhd$（$|c|\le\ell$）のブール結合でも定理 6.11 が成り立ち、拡張正則の演算では成り立たないこと |
| **D5** §7 | l.1547–1553、1586–1591 | 未解決問題 7.3 から副問を削除。結論の二標識の例、範疇文法の書き方 |
| **D6** 参考文献 | l.1777 以降の差分 | 追加：Clark (2016, ICGI)、Kanazawa (2023, WoLLIC)。略記：ICGI の論文集名、LATA、LNCS、編者名、出版地、誌名 |

文脈を確かめるために、変更箇所が参照する定義・補題・定理（例：§4 の $G_n$、$H_n$、$w^*_i$、$u_i$、補題 4.1、命題 4.2、補題 4.4・4.5、定理 4.6、命題 5.5、命題 6.5・6.7、定理 6.8・6.11、補題 6.9）は本文で読んでかまいません。D3 は Kanazawa の論文（添付の `kanazawa-invited.pdf`、著者稿）の Algorithm 3（p.11–13）、定理 8（p.14）、(d†′)（p.15）と照らしてください。

## 確認してほしいこと

各変更箇所について、次を確かめてください。

1. **数学的な正しさ**：文が、本文の定義・補題・定理から実際に従うか。量化子、仮定（観測器、$r$、$s$、$k$、$n$ の範囲、初期記号、型付きか型なしか）が落ちたり変わったりしていないか。数値（$2^n+2n-2$、$3\cdot2^n-6$、$4(6n-4)<2^{n-2}$ が $n\ge10$ で成り立つこと、$(n+1)^2$、$3\cdot2^{n-1}-2$、248 語）は自分で計算して確かめる。
2. **本文との一致**：Abstract・序論・結論の文が、本文の命題・定理の主張を超えていないか（言い過ぎ）、弱すぎて誤解を招かないか。参照先（Theorem C(iii)・(iv)、Proposition 4.2(c)、Lemma 4.1、Section 5 など）が正しいか。
3. **他人の仕事についての主張**：D3 の Kanazawa の Algorithm 3 と (d†′) についての文、D2 の Clark (2016) についての文、D2 の言語学の典拠についての文が、その文献の内容を正確に述べているか。とくに D3 は、Kanazawa 氏がこの論文の査読者になる可能性があるので、Algorithm 3 の仮定（$\Gamma$、ガード付きの式、$Q^{r,s}$ の重複除去、原子の正規化）に照らして一語ずつ確かめる。
4. **文として**：圧縮で意味が変わった文、指示語（there、its、this）が曖昧な文、記法の衝突（同じ記号が別の意味で使われる。例：$\Gamma$ は §4 では括弧の字母、Kanazawa では演算の集合）、英語として不自然な文。
5. **参考文献**：追加・略記した項目の書誌（著者、題、会議名、叢書と巻、頁、年）が正しいか。略記の仕方が文献表の中で揃っているか。

## 判定の書き方

- 区切りごとに表で：`| 行 | 主張・文 | 判定 | 根拠（一、二文） | 修正案 |`。
- 判定は **OK**（確認できた）、**FALSE**（書いてあるとおりには偽。反例か具体的な理由）、**GAP**（結論は正しいが仮定や参照が足りない）、**OVERCLAIM**（本文や典拠より強く言っている）、**UNCLEAR**（曖昧で誤読されうる）、**STYLE**（英語・記法の問題）、**UNCHECKED**（確認できなかった）。
- 問題がない文も、なぜ OK と言えるかを一、二文で書く。
- 原稿の文を長く書き写さず、行番号で指す。修正案は差し替える英文で書く（頁数を増やさないよう、元の文と同じくらいの長さで）。
- 最後に総合判定を三択で：「このまま投稿してよい」「局所的な修正で投稿してよい（修正の一覧）」「投稿前に大きな見直しが要る（理由）」。

## 成果物

次のファイルを一つの zip にまとめて渡してください（私がリポジトリの `09_typed-fcp-fkp/research/external_review_2026-11-28_chatgpt_diff/` に置きます）。

- `review.md`：D1〜D6 の結果と総合判定（250 行程度まで）
- `findings.csv`：列 `id,section,severity,lines,claim,issue,suggested_fix`、`id` は `C01` から、`severity` は `false`／`gap`／`overclaim`／`unclear`／`style`
- `checks/`：数値を計算で確かめた場合のコードと出力（任意、Python 標準ライブラリのみ）

会話の途中で止まりそうなら、D3 と D4 の結果を先に会話に書き出してください（数学的な主張が最も多い箇所です）。

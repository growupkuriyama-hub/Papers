# 依頼：#2 論文の省略のない正確な日本語版を GitHub に作成する

あなたは形式言語理論（MCFG、分布学習、有限半群）に通じた技術翻訳者兼 LaTeX 編集者です。下の英語原稿の**完全な日本語版**を作り、GitHub に置いてください。

**目的：** 著者が日本語で内容を一行ずつ確認するための版。読みやすさのための要約・言い換え・補足は不要。**原文の論理と量化を一字一句たがえない**ことが最優先です。

## 1. 対象と出力

- リポジトリ：`growupkuriyama-hub/Papers`
- 正本（英語）：`02-v2-lg-fanout-boundary/main.tex`、**コミット `d6753a9`**（3,758 行、README の Change log (169) の版）。
  - 最初に、取得したファイルのコミット SHA と行数を報告すること。異なる版しか取れない場合は、その版の SHA を明記して作業する。
- **英語版 `main.tex` は一切変更しない。**
- 作るもの（すべて新規）：
  1. `02-v2-lg-fanout-boundary/japanese/main_JP.tex`：日本語版の本体。
  2. `02-v2-lg-fanout-boundary/japanese/main_JP.pdf`：コンパイル結果。
  3. `02-v2-lg-fanout-boundary/tools/check_jp_alignment.py`：英日の整合検査スクリプト（§5）。
  4. `02-v2-lg-fanout-boundary/reviews/jp_translation_report_2026-11-06.md`：作業報告（§6）。
- **反映の仕方：**
  - 新しいブランチ `japanese-v2-2026-11-06` にコミットし、`main` への Pull Request を作る。`main` には直接 push しない（著者がマージする）。
  - コミットメッセージと PR 本文は英語で短く書く。
  - PR が作れない環境ならブランチの push までとし、その旨を報告に書く。
  - 書き込み権限がない環境なら、上記 4 ファイルをそのまま提出する。

## 2. 「省略のない」「正確な」の定義（厳守）

1. **全文を訳す。** 対象は次のすべてで、要約・統合・削除は禁止。
   - 要旨と本文
   - 脚注、表の中身と見出し（caption）、例
   - 定理・補題・命題・系・定義・注意・未解決問題の文と証明
   - 付録すべて
   - 謝辞・利益相反・資金・データ・生成 AI の申告
2. **数式は一切変えない。**
   - インライン数式、ディスプレイ数式、`equation`/`align` などの環境、`\tag` は、英語版の文字列を**そのまま**写す。
   - 記号の改名・括弧の追加・式の並べ替え・「明らかに同じ」書き換えも禁止。
   - 数式の中の英単語（例：`\text{ has a successful derivation using }`）も写すだけにし、訳さない。
3. **構造を変えない。**
   - 節・小節・段落見出し、定理環境の種類と順序、`\label`、`\ref`、`\cite` のキーと順序を英語版と同一にする。
   - 番号（定理番号、式番号、節番号）が英語版と一致すること。
   - `\item` の数、表の行数・列数も同一にする。
4. **量化と論理の順序を保つ。**
   - 「for every … there is …」の順序、「at most / at least」、「iff」、「only」、「some」、「every」、否定のかかり方を、日本語でも同じ順で読めるように訳す。
   - 曖昧になる場合は語順を英語に寄せてよい（自然さより正確さ）。
5. **足さない。**
   - 訳注・補足説明・独自の言い換えを本文に入れない。
   - 訳語の注意が必要なら、§6 の報告に書く。
6. **参考文献は訳さない。** `thebibliography` は英語のまま写す。
7. **固有名・記号名はそのまま。** 人名、文献名、`Const`/`Link`/`Comp`/`Start` などの規則名、`IPTtD`、`TxtEx` は英字のまま。

## 3. 文書の作り方

- 文書クラスは既存の日本語版と同じにする：`\documentclass[11pt,a4paper]{ltjsarticle}`、LuaLaTeX（`latexmk -lualatex main_JP.tex`）。参考：`02-v2-lg-fanout-boundary/archive-v1/japanese/main_JP.tex`、`01_fixed-h-cfg/japanese/main_JP.tex`。
- プリアンブルは英語版の `\usepackage` とマクロ定義（`\Wit`, `\Cmcf`, `\tuple`, `\blank`, `\eps`, `\fan`, `\cutpos` など）を**すべてそのまま**写す。
  - LuaLaTeX で問題になるパッケージがあれば、報告に理由を書いたうえで最小限だけ差し替える。
- 定理環境名だけを日本語にする。番号付けの仕組みは英語版と同じにする。

  | 英語 | 日本語 |
  |---|---|
  | Theorem | 定理 |
  | Lemma | 補題 |
  | Proposition | 命題 |
  | Corollary | 系 |
  | Definition | 定義 |
  | Remark | 注意 |
  | Example | 例 |
  | Open Problem | 未解決問題 |
  | 主定理 `mainthm`（A, B, C） | 定理 |

- 英語版の `proof` 環境は「証明」と表示されるようにする（`\renewcommand{\proofname}{証明}` など）。
- 文体はである調、句読点は「，」「．」（既存の日本語版と同じ）。
- `\ref` の前の語は日本語にし、番号は `\ref` のまま残す。対応は Theorem~\ref → 定理~\ref、Lemma → 補題、Appendix → 付録、Section → 第~\ref{..}~節、Table → 表。

## 4. 訳語表（既存の日本語版に合わせる。ここにない語は一貫した訳を選び、報告に一覧を書く）

| 英語 | 訳語 |
|---|---|
| typing / positive image | 型付け／正の像 |
| fresh(-identity) completion | 新単位元による完備化 |
| window typing / window–group typing | 窓型付け／窓–群型付け |
| local group / local-group typing | 局所群／局所群型付け |
| sliding-factor morphism / labelling | 滑動因子準同型／滑動因子ラベル付け |
| local-group-determined | 局所群決定的 |
| pseudovariety / pseudo-identity | 擬多様体／擬恒等式 |
| two-element semilattice $U_1$ | 二元半束 $U_1$ |
| minimal ideal / Rees matrix semigroup | 極小イデアル／Rees 行列半群 |
| (f,s)-tuple-substitutable / substitutability | $(f,s)$-タプル代入可能／代入可能性 |
| admissible context / distribution | 許容文脈／分布 |
| tuple / component | タプル／成分 |
| fan-out / rule rank | ファンアウト／規則ランク |
| good / reduced / ε-free / nondeleting / nonpermuting / nonmerging | 良い／既約／ε-free（ε 非消去）／非削除／非置換／非併合 |
| presentation | 表示（文法表示） |
| rule thickness / nonterminal thickness | 規則の厚さ／非終端記号の厚さ |
| characteristic sample / characteristic data | 特徴標本／特徴データ |
| set-driven (reconstruction) operator | 集合駆動型（再構成）作用素 |
| conservative (sequential) learner | 保守的（逐次）学習器 |
| text / TxtEx-identification | テキスト／TxtEx 同定 |
| reconstruction / composition witness | 再構成／合成証拠 |
| yield-type refinement / trimmed | 産出型細分／刈り込んだ |
| typed nonterminal / typed rule | 型付き非終端記号／型付き規則 |
| canonical tuple / canonical context / witness set | 標準タプル／標準文脈／証拠集合 |
| representative length | 代表長 |
| rare type / realized types | 稀な型／実現型 |
| distinguishing sub-target | 判別部分標的 |
| heavy node / antichain / λ-minimal derivation | 重い節点／反鎖／λ-極小導出 |
| shortening principle | 短縮原理 |
| block-replacement family / owner / block / row (line) | ブロック置換族／所有者／ブロック／行 |
| owner-wise simultaneous replacement | 所有者ごとの同時置換 |
| pumping | ポンピング |
| power transfer | 冪の移送 |
| doubling family | 倍増族 |
| letter-disjoint | 文字が互いに素な |
| path language | 道の言語 |
| identification in polynomial time and thick data (IPTtD) | 多項式時間・厚データ同定（IPTtD） |
| uniform polynomial characteristic-data length | 一様多項式特徴データ長 |

## 5. 検査（必須。結果を報告に貼る）

`tools/check_jp_alignment.py`（Python 3、外部ライブラリなし）を書き、英語版と日本語版を比べて次を出力すること。**すべて差分 0 が合格。**

1. `\label{…}` の列（出現順）が一致する。
2. `\ref`、`\eqref`、`\cite`（オプション引数を除くキー）の多重集合が一致する。
3. 環境の列（`theorem`、`lemma`、`proposition`、`corollary`、`definition`、`remark`、`example`、`openproblem`、`mainthm`、`proof`、`enumerate`、`itemize`、`table`、`tabular*`、`equation`、`align*` など）が順序ごと一致する。
4. `\section`、`\subsection`、`\paragraph` の数が一致する。
5. `\item` の数が一致する。
6. **数式の一致：** 次の数式断片をすべて抜き出し、英日で**出現順の列として**完全一致する。
   - `$…$`、`\(…\)`、`\[…\]`、`equation`/`align` 系環境の中身
   - `\text{…}` の中は比較から除いてよいが、除いた件数を報告する。
7. 日本語版の本文（数式・コマンドを除く）に、英文の文が 1 文以上残っていない。残っていれば行番号を列挙する。対象は 5 語以上の英単語列。ただし固有名、規則名、参考文献、`\cite` は除く。

さらに：

- `latexmk -lualatex main_JP.tex` が**エラー・未定義参照・未定義引用なし**で通ること。警告はすべて報告に列挙する。
- 英語版（`latexmk -pdf main.tex`、44 ページ）と日本語版のページ数を併記する。

## 6. 報告 `reviews/jp_translation_report_2026-11-06.md` の構成

1. 取得した英語版の SHA と行数、日本語版の行数とページ数。
2. 検査スクリプトの出力（そのまま貼る）。
3. 訳語表の追加分（§4 にない語の訳を一覧）。
4. 翻訳で判断が要った箇所の一覧。行番号、英語原文、採った訳、理由を書く。特に次の箇所は必ず載せること。
   - 量化の順序が繊細な箇所：要旨、主定理 A–C、定義 `def:uniform-polydata` とその直後の段落、系 `cor:iptd`、命題 `prop:typed-separation`、補題 `lem:heavy-node-count`(ii)、未解決問題 `op:fanout-two`。
5. プリアンブルで英語版から変えた点（あれば、理由とともに）。
6. 未完了・未確認の点（あれば正直に）。

## 7. 禁止事項（再掲）

- 英語版 `main.tex` や他の既存ファイルを変更しない（新規 4 ファイルの追加のみ。`README.md` の更新も著者が行う）。
- 要約・省略・意訳・補足・訳注の挿入をしない。
- 数式・記号・ラベル・番号を変えない。
- 「おおむね同じ」で検査を通したことにしない。差分が 0 にならない項目は、その差分を報告に列挙する。

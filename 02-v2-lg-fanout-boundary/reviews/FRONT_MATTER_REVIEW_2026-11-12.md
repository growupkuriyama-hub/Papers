# 論文 #2 Title・Abstract・Introduction 査読と改訂（2026-11-12）

対象：`main` の PR #108 マージ後の版（英語43頁・日本語51頁、コミット `7aed4c8`）。
作業ブランチ：`paper02-front-matter-refinement-2026-11-12`。
査読者：Claude（AI による模擬査読。外部査読者の評価ではない）。

変更範囲は英日の要旨・キーワード・序論（`\begin{abstract}` から `\section{Preliminaries}`／`\section{準備}` の直前まで）に限る。本文・定理本体・証明・付録・退避資料は変更していない。タイトルは維持した。

---

## I. 総合査読結果

**長所。** 定理 A/B/C の量化子・前提・作用素の範囲は本文と一致している。分離例の意味（被覆の分離であり手法の必要性ではない）や、ファンアウト2の未解決性も正確に書かれている。先行研究への帰属も概ね適切だった。

**修正した問題**（重要度順）：

| # | 重要度 | 問題 | 対応 |
|---|---|---|---|
| 1 | 投稿要件 | 要旨が265語（detex）。TCS Guide for Authors の上限250語を超過 | 237語に短縮 |
| 2 | 投稿要件 | キーワードがない（TCS は1〜7語を要求） | 6語を追加 |
| 3 | 正確性（R1.7型） | 要旨の “for every set-driven **learner**” が作用素と逐次学習器を混同 | 要旨から削除。序論で作用素と Gold 学習器を一文で区別 |
| 4 | 位置づけ（R1.3, R2.1） | なぜ個数でなく長さなのかが一文（rare type）しかない | 段落「Why length」を新設：個数は $O(\|G\|)$、長さは型の代数で指数的になり得る、型細分は指数的に厚い |
| 5 | 新規性の境界（R2.1） | 自明な型付け（Yoshinaka 2011）と固定窓・ファンアウト1（Yoshinaka 2008）の**量的**結果が既知であることを序論で明示していない | 「Relation to prior work」で明示し、新規性を「これらを超える長さ解析と境界」に限定 |
| 6 | 誠実さ | 定理 A と B(i) の間に因子 $\|G\|$ の差が残ることが序論にない（結論のみ） | 定理直後に一文で明示 |
| 7 | 記法（R1.4） | $\mathbf{LI}\vee\mathbf{Grp}$、window–group typing が序論で未定義のまま使用 | 両方を一句で定義 |
| 8 | 重複（R2.4） | 「Main results」前置き・「Scope of the claims」・姉妹原稿段落が定理文・表と重複 | 削除または一文に統合 |
| 9 | 補助概念の格上げ（R2.2） | 緩衝文字補題（`lem:lg-buffered-owners`）を序論で列挙 | 削除（本文に残る） |
| 10 | 構成 | 分離例の段落が定理 A と B の間にあり流れを切る | MCFG 固有の難しさの段落へ移動 |
| 11 | 表現 | 定理 C(ii) “a typing $s_U$ of three letters”、定理環境内の解釈文、“Since fan-out one is CFG” | 修正・環境外へ移動 |
| 12 | 整合 | 定理 B(i) が $\mathcal B_{f,s}$ を挙げていない（命題 6.1(ii) は挙げる） | 命題に合わせて追加 |
| 13 | 誠実さ | 非可換群での定数が $f$ について二重指数的であることが序論にない | 一句で追加 |

**残る投稿上のリスク**（序論の書き方では解消できないもの）：ファンアウト2の境界が未解決であること、定数が巨大であること、姉妹原稿 #1 が TCS で審査中であること（表1で重複のなさを示している）。

## II. TCS 査読指摘（#1）との対応

| #1 の指摘 | #2 の該当箇所 | 問題 | 対応 |
|---|---|---|---|
| R1.7, R1.24, R1.25（作用素と学習器の混同） | 要旨・旧序論 | 要旨に “set-driven learner” | 作用素に統一。序論「Setting」で「Gold 学習器の収束時点は評価しない」と一度だけ述べる |
| R1.3（位置づけと意義） | 序論冒頭 | 長さを問う理由が弱い | 「Why length」段落 |
| R2.1（既存結果との区別） | 「Relation to prior work」 | 量的既知結果が未記載 | 自明型付け・固定窓の既知結果を明記 |
| R1.4, R1.5（未定義記号・貢献の列挙） | 「Local groups」 | LI∨Grp・window–group が未定義 | 定義を追加。補題の列挙をやめる |
| R2.2（使われない構造の強調） | 「Approach」 | 緩衝文字補題の列挙 | 削除 |
| R2.4（重複・先取り） | 「Main results」前置き・「Scope」・姉妹原稿段落 | 定理文・表と重複 | 統合・削除 |
| R2.3（扱える言語族の広がり） | 分離例 | 位置が不自然 | 難しさの段落に統合し、二つの要素（局所群・非可換性）がそれぞれ被覆を広げることとして提示 |
| R1.10, R1.13（型付けの固定） | 「Setting」 | 既に一文で十分 | 一文「標的クラス全体に一度選び、学習しない」のみ。繰り返さない |

## III. タイトル

| 候補 | 正確性 | 伝達力 | 簡潔性 |
|---|---|---|---|
| **1（推奨・維持）** *Distributional Learning of Multiple Context-Free Languages under Fixed Finite-Semigroup Typing: Local Groups and the Length of Characteristic Data* | 高い。副題が新規性（局所群・長さ）を担う | #1 と同じ主題名で連作と分かる | 21語でやや長い |
| 2 *Local Groups and the Length of Characteristic Data for Multiple Context-Free Languages under Fixed Finite-Semigroup Typing* | 高い | 新規性が先頭に来る。#1 との連続性は弱い | 17語 |
| 3 *Characteristic-Data Length in Distributional Learning of Multiple Context-Free Languages: Local Groups under Fixed Finite-Semigroup Typing* | 高い | 「長さ」が主題と分かる | 18語でやや硬い |

維持を推奨する理由：主題名＋副題の形は TCS で標準的で、主題名が質的学習（Yoshinaka の枠組み）を指していても副題が新規性を限定している。#1 と博士論文の二本柱として揃えられる。「boundary」を入れる案は、ファンアウト2が未解決なので避けた。

## IV. 要旨

語数（detex）：265 → 237。日本語要旨：654字 → 622字。

改訂点：TCS 上限への適合／“learner” の削除／分離例の説明を一文に短縮／定数の一様性を保持／最悪時下界（m9）の限定を保持。

## V. 序論の段落別監査

| 旧段落 | 判定 | 新しい扱い |
|---|---|---|
| 冒頭（背景・問題） | 短縮可能 | 維持し、IPTtD の定義を一句で補う |
| Setting | 必須 | 維持。厚さの不等式は補題参照に移し、作用素の区別とスコープ表の参照を統合 |
| 型付けでクラスが広がる／rare type | 統合可能 | 新「Why length」段落へ統合して拡充 |
| Local groups | 必須 | 維持。$\mathtt{ab}$ 偶奇の例は命題参照へ（本文 §5.3 にある） |
| Main results 前置き | 削除可能 | 削除（定理 A の文で一様性を述べる） |
| 定理 A | 必須 | 維持（$f$ の量化を明示、一様性を一句追加） |
| 分離例の段落 | 移動 | 難しさの段落へ |
| 定理 B, C | 必須 | 維持（B(i) に $\mathcal B_{f,s}$、C(ii) の表現、解釈文を環境外へ） |
| 定理後の段落 | 必須 | IPTtD・$\|G\|$ の差・擬多様体水準・姉妹原稿との関係 |
| The remaining question | 必須 | 「The fan-out-two question」として維持 |
| Approach | 必須 | 「The multiple context-free difficulty」として拡充・補題列挙を削除 |
| Relation to prior work | 必須 | 既知の量的結果を追加 |
| Relation to companion | 統合可能 | 先行研究段落の末尾一文と表1に統合 |
| 表1 | 必須 | 維持（無変更） |
| Scope of the claims | 統合可能 | Setting に統合 |
| Organization | 削除可能 | 削除（主定理が各節の定理番号を指すので道案内になる） |

語数（自作カウンタ、数式は1語、参照は1語）：

| | 旧 | 新 |
|---|---|---|
| 序論全体 | 1122 | 1203（+7%） |
| 表を除く | 1030 | 1111 |
| 表と定理を除く地の文 | 698 | 784（+12%） |
| 日本語序論（和字数） | 2735 | 2657（−3%） |

英語の地の文は短くならなかった。15〜25%の削減は、新しく加えた「長さを問う理由」「既知の量的結果」「$\|G\|$ の差」「作用素と学習器の区別」を削ることになり、査読リスクを上げるので採らなかった。

## VII. 検証

- **数学的主張の同一性**：定理 A/B/C の論理内容は不変。追加したのは本文の命題・系の範囲内の記述のみ（B(i) の $\mathcal B_{f,s}$ は命題 6.1(ii)、C(ii) の $\mathcal B_{1,s_U}$ は定理 7.3(iii)、$O(\|G\|)$ 語は定理 4.3 と $C_s(G)$、二重指数は §5.1 と結論、$\|G\|$ の差は結論「Tightness」）。
- **ラベル**：`thm:A`, `thm:B`, `thm:C`, `tab:companion-overlap`, `sec:introduction` を保持。新たに参照した既存ラベル：`thm:data-from-typed-thickness`, `def:conservative-learner`, `lem:mcfg-li-group-window`, `rem:fanout-one-data`, `sec:learner`。参照を外したもの：`sec:prelim`, `sec:char-data`, `sec:upper`, `sec:fanout-one`, `sec:fanout-two`, `lem:lg-buffered-owners`（いずれも本文に存在し、未定義参照なし）。
- **引用キー**：序論の引用キーの集合は旧版と同一。英日で一致。
- **LaTeX**：pdfLaTeX 43頁（変化なし）、LuaLaTeX 50頁（51→50）。未定義参照・重複ラベル・Overfull 0。
- **英日整合**：序論範囲の `\ref`・`\cite`・`\label` の多重集合が英日で一致。数式断片の多重集合も一致。`tools/check_jp_alignment.py` の全体の失敗数は改訂前より減った（`\cite` 多重集合は PASS に、`\ref` は 11→8）。残る失敗は本文の既存の英日差。
- **`tools/check_port.py`**：終了コード0。出力は改訂前と同一。
- **未実施**：CI（ブランチ push 後に実行される）、人間による数学査読、PDF 全頁の目視。

## VIII. 最終判断

現行版より明確に改善した（投稿要件の不適合2件、作用素/学習器の混同1件を解消し、新規性の境界と動機を補った）。Title・Abstract・Introduction について、これ以上の大きな改稿は不要と判断する。残る課題は数学側（ファンアウト2、定数の大きさ）であり、序論の書き方では解消できない。

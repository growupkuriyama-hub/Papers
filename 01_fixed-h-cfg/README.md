# #1 TCS — 現行編集版 v267（回答書／提出ZIP CI検証済み） / 凍結記録 v249

> **編集正本：main の v267（2026-10-22）。Claude最終査読の3件（§5.1定義前使用、§4.2無限標的の所属、Takada引用前の空白）を英日原稿に反映。数学的主張・番号は不変。Marked PDF 26頁、査読回答14頁、49回答項目・77参照を GitHub Actions 39751679098 で検証済み。ZIPはちょうど3ファイル。TCSへは未再投稿です。**
> 論文：**Distributional Learning of Context-Free Languages under Fixed Finite-Semigroup Typing**  
> 雑誌：*Theoretical Computer Science* / **TCS-D-26-00494** / **Round 1 major revision**

**[v267 最終提出用ZIP](TCS-D-26-00494_R1_3files.zip)**

## 提出に使用する3ファイル（v267、CI検証済み）

| TCS提出物 | ファイル | 役割 |
|---|---|---|
| **1. Clean TeX** | [TCS-D-26-00494_Manuscript_Clean.tex](TCS-D-26-00494_Manuscript_Clean.tex) | 改訂後の英文原稿（[編集正本 `main.tex`](main.tex)とバイト一致） |
| **2. Marked PDF** | [TCS-D-26-00494_Manuscript_Marked.pdf](TCS-D-26-00494_Manuscript_Marked.pdf) | 初回提出版に対して改訂箇所を表示 |
| **3. Response PDF** | [TCS-D-26-00494_Response_to_Reviewers.pdf](TCS-D-26-00494_Response_to_Reviewers.pdf) | 上記 **同一のMarked PDF** に位置参照を合わせた査読回答 |

**まとめて取得： [TCS-D-26-00494_R1_3files.zip](TCS-D-26-00494_R1_3files.zip)**（上記の3ファイルのみ）。ZIPから取り出し、Editorial Managerでそれぞれ適切な文書種別を選択してください。ここでいう「提出用」は *投稿済み* の意味ではありません。

## 閲覧・編集用（提出ZIPには入れない）

- **[英文Clean PDF](TCS-D-26-00494_Manuscript_Clean.pdf)** — 論文を読むための最新版
- **[英文編集正本 `main.tex`](main.tex)** — 数理原稿の唯一の編集正本。上記Clean TeXは同一内容の提出用コピー
- [日本語論文PDF](japanese/main_JP.pdf) / [日本語論文TeX](japanese/main_JP.tex) — 研究・著者確認用
- [査読回答の編集ソース](response/response_round1.tex) — PDFの正本（提出用PDFは自動生成）
- [最新管理情報 `PAPER.yaml`](PAPER.yaml) — **`pending_release: v261`** とv249凍結履歴を参照
- [TCSフォーム用最新版Abstract](revision/TCS_FORM_ABSTRACT_CURRENT.txt) — v246英文Abstractのプレーンテキスト

### v267 自動検証（2026-10-22）

- [Marked PDF・査読回答・3ファイルZIP（Actions 39751679098）](https://github.com/growupkuriyama-hub/Papers/actions/runs/39751679098)：成功。回答49項目・77参照を新Marked PDFに合わせ検証。ZIP3ファイル、CRC検証成功。
- [英文・日本語LaTeXビルド（Actions 39751678825）](https://github.com/growupkuriyama-hub/Papers/actions/runs/39751678825)：成功。TeX3件の軽微な表現修正を英日同期。数学の変更なし。Editorial Managerへの再投稿は未実施。

### v261自動検証（2026-10-21）

- [Marked PDF・英文回答書・3ファイルZIP（Actions 39592711566）](https://github.com/growupkuriyama-hub/Papers/actions/runs/39592711566)：成功。R1.35の形式的整数オフセットと式(★★)の記述を同期。回答書49項目／Marked PDF参照77箇所を確認。
- 回答PDF 14ページ、Marked PDF 26ページ。ZIPの3ファイル件数とCRC検査を通過。収録した各ファイルはGitHub原本とGit blob SHAが一致。
- 投稿用Clean TeXはv260から変更なし。日本語査読回答書は旧訳のまま（英文提出ZIPには含まず）。TCSの再投稿操作は未実施。

### v260の過去検証記録（2026-10-21。v261の検証を意味しない）

- [英文・日本語Clean PDF（Actions 39588432148）](https://github.com/growupkuriyama-hub/Papers/actions/runs/39588432148)：成功。英文26ページ、日本語30ページ。Overfull `\\hbox` 0件。
- [Marked PDF・英文査読回答PDF・提出用3ファイルZIP（Actions 39588432440）](https://github.com/growupkuriyama-hub/Papers/actions/runs/39588432440)：成功。Marked PDFに合わせ49項目・77箇所の位置参照を同期。ZIPは `unzip -t` と3ファイル件数検査を通過。
- 形式的整数オフセットによる (★)/(★★) の所属判定を全59,582組の短い $(u,x,v)$ で総当たり検証し不一致なし。これは一般の形式的証明の代用ではない。
- 英文 `main.tex` と投稿用Clean TeXは同一Git blob。英日で7元の型付けと非線形例の補題を同期。
- 査読回答書の日本語旧訳は未同期（英文ZIPには含まず）。TCSには未再投稿。

### v259の過去検証記録（2026-10-21。v260の検証ではない）

- [英文・日本語Clean PDF（Actions 39583718360）](https://github.com/growupkuriyama-hub/Papers/actions/runs/39583718360)：成功。英文26ページ、日本語30ページ。Overfull `\\hbox` 0件。
- [Marked PDF・英文査読回答PDF・3ファイルZIP（Actions 39583718269）](https://github.com/growupkuriyama-hub/Papers/actions/runs/39583718269)：成功。49項目／77箇所のMarked PDF参照を同期。ZIPは `unzip -t` と3ファイル件数検査を通過。
- Appendix A.1独立表示数式は英日各7→1箇所。最終定量上界のみdisplayを維持。`main.tex`と投稿用Clean TeXは同一Git blob。
- 日本語査読回答書は旧訳のままで英文ZIPには含まれない。TCSへの再投稿は未実施。

### v258の過去検証記録（2026-10-21。v259の検証ではない）

- [英文・日本語Clean PDF（Actions 39580899314）](https://github.com/growupkuriyama-hub/Papers/actions/runs/39580899314)：成功。英文26ページ、日本語31ページ。Overfull `\\hbox` 0件。
- [Marked PDF・英文査読回答PDF・3ファイルZIP（Actions 39580899262）](https://github.com/growupkuriyama-hub/Papers/actions/runs/39580899262)：成功。回答49項目／Marked PDFの77箇所を同期。ZIPは `unzip -t` と3ファイル確認を通過。
- `main.tex` と投稿用Clean TeXは同一Git blob。Appendix A.1のDepth/Width/Countingは英日同期。
- 日本語の査読回答旧訳は更新していない（英文提出ZIPには含まず）。TCSへの再投稿は未実施。

### v257の過去検証記録（2026-10-21。v258の検証ではない）

- [英文・日本語Clean PDF（Actions 39576827492）](https://github.com/growupkuriyama-hub/Papers/actions/runs/39576827492)：成功。英文26ページ、日本語30ページ、Overfull `\\hbox` 0件。
- [Marked PDF・英文査読回答PDF・提出用3ファイルZIP（Actions 39576827244）](https://github.com/growupkuriyama-hub/Papers/actions/runs/39576827244)：成功。Marked PDFに対応する回答49項目・余白行番号77箇所の参照を同期。ZIPは`unzip -t`と3ファイル件数検査を通過。
- Appendix Cの5ラベルは英日とも保持。`main.tex`と提出用Clean TeXは同一Git blob。
- 査読回答の日本語旧訳は未同期（英文提出ZIPには含まれない）。TCSには未再投稿。

### v256の過去検証記録（2026-10-21。v257の検証ではない）

- [英文・日本語Clean PDF（Actions 39574611488）](https://github.com/growupkuriyama-hub/Papers/actions/runs/39574611488)：成功。英文26ページ、日本語30ページ。英文・日本語の両ビルドを含め Overfull `\\hbox` **0件**（旧版は65ptのはみ出し）。
- [Marked PDF・英文査読回答PDF・3ファイルZIP（Actions 39574611503）](https://github.com/growupkuriyama-hub/Papers/actions/runs/39574611503)：成功。49項目・77箇所を新Marked PDFと同期。ZIPは `unzip -t` と3ファイルちょうどの検証を通過。
- `main.tex` と提出用Clean TeXはGit blob一致。§1.2と証明内の記号は英日同期。TCSへの再投稿は未実施。
- 査読回答の日本語旧訳は今回の英語改訂に未同期。英文提出ZIPには含みません。

### v255の過去検証記録（2026-10-21。v256の検証を意味しない）

- [英文・日本語Clean PDF（Actions 39570364619）](https://github.com/growupkuriyama-hub/Papers/actions/runs/39570364619)：成功。
- [Marked PDF・英文査読回答PDF・3ファイルZIP（Actions 39570364497）](https://github.com/growupkuriyama-hub/Papers/actions/runs/39570364497)：成功。回答49項目・新Marked PDFに同期した77位置参照、ZIP3ファイルのCRC検証。
- 英文編集正本 `main.tex` と提出用Clean TeXはGit blob一致。付録Cの初期スタック・受理スタックを英日同期。
- 査読回答の日本語旧訳はv255に未同期。英文提出用ZIPには含まれません。TCSには未再投稿。

### v254の過去検証記録（2026-10-21。v255の検証ではない）

- [英文・日本語Clean PDFの再生成](https://github.com/growupkuriyama-hub/Papers/actions/runs/39565101494)：成功。
- [Marked PDF・査読回答書PDF・3ファイルZIP](https://github.com/growupkuriyama-hub/Papers/actions/runs/39565101537)：成功。49査読項目・77参照を新Marked PDFと同期し、ZIPの3ファイルとCRCを検証。
- `main.tex` と提出用英文Clean TeXは同一Git blob。日本語論文本体§1.2も対応済み。TCSへの再投稿は未実施。
- 査読回答書の日本語旧訳は英文v254に未同期であり、翻訳の鮮度チェックは意図通り停止。英文提出ZIPには含まない。

### v253の検証履歴（2026-10-21。v254の検証ではない）

- Clean PDF（英・日）：[Actions 39563279785](https://github.com/growupkuriyama-hub/Papers/actions/runs/39563279785) 成功。
- Marked PDF／英語査読回答／3ファイルZIP：[Actions 39563279763](https://github.com/growupkuriyama-hub/Papers/actions/runs/39563279763) 成功。49項目・77箇所を新Marked PDFで同期し、ZIPの3ファイルとCRCを検証。
- 英文 `main.tex` とClean TeXはGit blob一致。TCSへの再投稿は未実施。
- `response/japanese/` の日本語回答訳は旧版であり、今回の英文改訂に未同期。訳の鮮度チェックは意図通り失敗しており、英文提出パッケージには含まない。

### v249の凍結済み過去検証記録（2026-10-20）

- `main.tex` と `TCS-D-26-00494_Manuscript_Clean.tex` の一致を確認。
- v249の **Clean PDF / Marked PDF / Response PDF / ZIP** はCIによる生成と公開が成功。
- v249の新Marked PDFで査読回答49項目・位置参照77か所を再同期（R2.10はMarked p.11, l.432）。ZIPは指定3ファイルのみ、GitHub ActionsでCRC検査済み。英文Clean TeXは正本とバイト一致。
- v246から引き継いだ変更：§1.2にcongruential familyの位置づけを追加、§5.1に型付き精密化の目的とRule (U)の説明を追加、Cor. 6.3の適用先を明確化、§7の半群・群の変数を統一。回答書のClean TeX提供説明を実態に合わせ、Marked版の余白行番号を再同期。利益相反申告に変更なし。
- **日本語版（2026-10-20更新）：** 英文v245を基準に、一般CFGの型付き証拠と完全性証明、BUNFの定量評価、窓・群の記号、結論、謝辞（Alexander Clarkを含む）、ChatGPT・Claudeの生成AI利用申告を同期しました。参考文献は英文v245と一致（英文v249との全文逐語同期は未実施。ただし今回のTheorem 5.2の帰納法については英文v249に同期済み）。数式・定理環境・ラベルの構造検査を実施しましたが、全文章の逐語的な翻訳校閲を完了したという主張ではありません。数学的正本は引き続き `main.tex`。`response/japanese/` は旧版v229のままで、TCS提出ZIPには含みません。

## どのファイルが正本か

| 用途 | 正本・参照先 |
|---|---|
| 数学的な本文の修正 | `main.tex` |
| 査読回答の修正 | `response/response_round1.tex` |
| バージョン確認 | `PAPER.yaml` の `current_baseline` |
| 投稿用PDF・ZIP | GitHub Actionsの成功後に更新される、上の**固定名**のファイル |

PDFを手で置き換えず、ソースを直してから `.github/workflows/publish-tcs1-clean-pdf.yml` と `publish-tcs1-revision-package.yml` による再生成・参照位置再検証を行います。**今後の数理原稿の変更では版番号も更新**してください。

### 履歴（最新版と区別）

- [初回提出版・基準アーカイブ](archive/) — Marked PDF生成に必要な旧稿、修士論文など。**削除しない**。
- [研究・査読履歴メモ](revision/) / [補足メモ](notes/) — 過去版と実験・監査の記録。提出用の正本ではありません。
- 現行版の正本は `main` 一本。過去のPR・実験系統は現行原稿として扱わない。
- 詳細な旧版変更履歴はGitのcommit履歴と `PAPER.yaml` に保存しています（旧READMEの長大な逐次履歴は掲載しません）。

---

**English:** Latest #1 TCS revision: **internal v249**, on the `main` branch. Download the **exact three-file submission ZIP** above. The Clean TeX mirrors `main.tex`; v249 marked-PDF and response anchors are VERIFIED (49 reviewer items / 77 locations); author has not yet resubmitted. The author must submit these files to Editorial Manager; GitHub publication is **not journal resubmission**.

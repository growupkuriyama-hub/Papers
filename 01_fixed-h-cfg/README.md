# #1 TCS — 最新改訂稿 / CURRENT REVISION **v238**

> **最新版は `main` の internal v238（2026-10-20）。**  
> 論文：**Distributional Learning of Context-Free Languages under Fixed Finite-Semigroup Typing**  
> 雑誌：*Theoretical Computer Science* / **TCS-D-26-00494** / **Round 1 major revision**  
> **v238：Introduction 1.1でKanazawaを明示（1996/1998の既存引用は保持）。分量は実質不変。PDF・ZIPは再生成待ち、Editorial Manager未提出。**

**最初に開くファイル： [最新版・TCS再投稿用3ファイルZIP](TCS-D-26-00494_R1_3files.zip)**

## 提出に使用する3ファイル（いずれも v238）

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
- [最新管理情報 `PAPER.yaml`](PAPER.yaml) — **`current_baseline.internal_version: v238`** と原稿SHA-256を参照
- [TCSフォーム用最新版Abstract](revision/TCS_FORM_ABSTRACT_CURRENT.txt) — v238英文Abstractのプレーンテキスト

### 検証状態（2026-10-20）

- `main.tex` と `TCS-D-26-00494_Manuscript_Clean.tex` の一致を確認。
- v238の **Clean PDF / Marked PDF / Response PDF / ZIP** は再生成・検証待ち（v237 Clean 25ページ／Marked 26ページ／査読回答14ページ）。
- v237では査読回答49項目／位置参照77か所の照合に成功。v238でも再検証する。
- v238の変更：Introduction 1.1にKanazawaを明示。v237の数学・構成・ページ圧縮は維持。
- **注意：** `response/japanese/` の日本語査読回答訳は旧稿ベースのままです。v238の対訳としては使用しないでください（TCS提出ZIPには含みません）。

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

**English:** Latest #1 TCS revision: **internal v238**, on the `main` branch. Download the **exact three-file submission ZIP** above. The Clean TeX mirrors `main.tex`; v238 marked-PDF and response anchors await fresh verification; author has not yet resubmitted. The author must submit these files to Editorial Manager; GitHub publication is **not journal resubmission**.

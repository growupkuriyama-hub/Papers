# MCFG論文・日本語版（現行正本への翻訳・査読用）

英語投稿版：[`../main.tex`](../main.tex)  
日本語全文：[`main_JP.tex`](main_JP.tex)  
対象誌：*Information and Computation*（投稿準備中）

2026-10-24に統合した内部revision 16を `main` の正規ファイル名へ反映しています。

## 実際に読み込む付録

- `appendix_group_blocks_JP.tex`：可換群・非可換群の同時ブロック置換
- `appendix_local_group_JP.tex`：有限局所群型付けと三次上界

窓型および窓＋任意有限群型の特徴正例標本総長は `O(||G||^2 θ̄_G)`、一般の局所群型では `O(||G||^3 θ̄_G)` です。

## ビルド

```sh
cd 02_fixed-h-mcfg/japanese
latexmk -lualatex -interaction=nonstopmode -halt-on-error main_JP.tex
```

英日PDFはGitHub Actionsの `publish-mcfg-bilingual-pdf.yml` で固定パスに公開します。旧v番号付き改稿記録はGit履歴から復元可能です。保留中の研究メモ・検算用スクリプトは `../revision/` に残しています。

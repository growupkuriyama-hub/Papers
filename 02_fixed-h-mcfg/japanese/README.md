# MCFG論文・日本語査読版（2026-10-24 LG二分法・代数的分離例同期）

英語投稿原稿：[`../main.tex`](../main.tex)  
日本語全文：[`main_JP.tex`](main_JP.tex)  
対象誌：*Information and Computation*（投稿準備中）

## 対応した内容

- 正例標本の**個数**ではなく、**符号化総長**を評価する動機を序論に配置。
- 型付けによる厚みの指数的増大と、有限素性付き交差依存の例を収録。
- 非可換有限群の同時ブロック短縮と、局所群の古典的Rees/sliding-factor座標への帰属を明確化。
- 元文法の `O(||G||^2 θ̄_G)` / `O(||G||^3 θ̄_G)` と任意標準入力の `O(n^3 t)` / `O(n^4 t)` を別々に表示。
- ファンアウト1におけるLG擬多様体の必要十分条件を定理化。関連CFG-R1の区別対を用い、下界は日本語付録で独立に証明。
- 重複する高アリティ下界探索の節・付録、独立Ramsey証明、未証明のsignature埋込み命題を整理。
- 局所群のみ・非可換群のみで代入可能となるファンアウト2標的を追加。高ファンアウトの必要条件と2元半束反例の可能性を区別。
- 追加の日本語証明は `additions/` に分割配置し、`main_JP.tex` から直接読み込む。

## ビルド

```sh
cd 02_fixed-h-mcfg/japanese
latexmk -lualatex -interaction=nonstopmode -halt-on-error main_JP.tex
```

PRでは `.github/workflows/verify-mcfg-bilingual-pr.yml` が英日双方を検査し、mainへのマージ後は `.github/workflows/publish-mcfg-bilingual-pdf.yml` が固定URLのPDFを再生成します。

英語版が投稿上の正本です。日本語版は数学的議論を照合するための研究翻訳であり、個々の証明の最終確認は引き続き必要です。

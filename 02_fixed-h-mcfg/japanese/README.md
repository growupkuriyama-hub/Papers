# #2 MCFG v72 — 日本語査読版

英語原稿 **v72** `02_fixed-h-mcfg/main.tex` の全文を，日本語で検討するための対照版です。
**英語版は正本**であり，日本語版は著者自身の数学的・論理的査読のために作成されています。

## ファイル

- `main_JP.tex` — 要旨，序論，準備，再構成，健全性，完全性，Gold同定，計算量，特徴データ長，すべての分離定理，結論，通常の付録，Yoshinaka (2015) に関する付録，文献一覧を含む**全文翻訳**。文献題名・著者名は原文表記のまま保持。
- `appendix_window_abelian_JP.tex` — 窓と有限アーベル群の積型付けに関する補題・定理・全証明の翻訳。本文 `main_JP.tex` から `\\input` によって組み込む。

## 対応する英語原稿

- 原稿: `02_fixed-h-mcfg/main.tex`, version **v72**
- 固定済み英語版マージコミット: `de32398d2fb9f378e33de9249b58e1a71248294f`
- 本文 Git blob: `c323536d6d329941da85ea14e61d488431d689b1`
- 群拡張付録 Git blob: `c6000d729ebd41317e2924f0c0b56779fa2c53fe`

## 同一性・注意

数式，主張の条件と量化，証明の順序，すべての `\\label`・`\\ref`・`\\cite`，および文献情報を対応させています。英語版にない定理の追加や，証明の省略は意図していません。翻訳は数学的正しさを保証しません。著者による逐語的な確認で誤訳を見つけたら英語版と照合して修正してください。

翻訳時点の機械的比較では，英語版・日本語版とも定理・補題・命題・定義・証明の個数が一致し，全 `\\label` の**集合と出現順序**も一致しています。

## PDFビルド

GitHub Actions の `Build MCFG Japanese review manuscript` ワークフローで
LuaLaTeX / TeX Live 2026 の PDF を生成します。成果物名：
`02-fixed-h-mcfg-japanese-pdf`。

ローカル環境での例：

```bash
cd 02_fixed-h-mcfg/japanese
latexmk -lualatex -interaction=nonstopmode -halt-on-error main_JP.tex
```

英語版の提出用ファイル `../main.tex` と `../appendix_window_abelian.tex`
は，日本語版の追加によって変更しません。

# #2 MCFG v73 — 日本語査読版

英語原稿 **v73** `02_fixed-h-mcfg/main.tex` の全文を，日本語で検討するための対照版です。
**英語版は正本**であり，日本語版は著者自身の数学的・論理的査読のために作成されています。
今回の日本語版v73は、v72から**数式表示（displayとinline）だけを整理した組版改訂**です。翻訳・数学的主張・証明・参照先は変更していません。

## ファイル

- `main_JP.tex` — 要旨，序論，準備，再構成，健全性，完全性，Gold同定，計算量，特徴データ長，すべての分離定理，結論，通常の付録，Yoshinaka (2015) に関する付録，文献一覧を含む**全文翻訳**。文献題名・著者名は原文表記のまま保持。
- `appendix_window_abelian_JP.tex` — 窓と有限アーベル群の積型付けに関する補題・定理・全証明の翻訳。本文 `main_JP.tex` から `\\input` によって組み込む。

## 対応する英語原稿

- 原稿: `02_fixed-h-mcfg/main.tex`, version **v73**
- 固定済み英語版マージコミット: `c9b4644c5d201395777eddc4b634210caca1a1af`
- 本文 Git blob: `48778ccbed8557a19c6f8d09c469d358987396b1`
- 群拡張付録 Git blob: `c1bbee4b26cd39dc68f4ae8e72488ec97702f117`

## 同一性・注意

数式，主張の条件と量化，証明の順序，すべての `\\label`・`\\ref`・`\\cite`，および文献情報を対応させています。英語版にない定理の追加や，証明の省略は意図していません。翻訳は数学的正しさを保証しません。著者による逐語的な確認で誤訳を見つけたら英語版と照合して修正してください。

翻訳時点の機械的比較では，英語版・日本語版とも定理・補題・命題・定義・証明の個数が一致し，全 `\\label` の**集合と出現順序**も一致しています。

今回の組版改訂では、本文の display 数式 **140 → 48**、付録 **5 → 2**（合計 **145 → 50**）です。全95か所の数式内容は、空白を正規化して照合しています。英語版v73とは言語別の行長や翻訳上の段組に応じて残す式が異なります。

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

# MCFG論文・日本語査読版（2026-10-27 英語原稿への忠実な同期）

英語投稿原稿：[`../main.tex`](../main.tex)  
日本語全文：[`main_JP.tex`](main_JP.tex)  
対象誌：*Information and Computation*（投稿準備中）

## 同期の基準

英語版 `main.tex` を唯一の投稿用正本とし、定理・補題・命題・定義・備考・例の**環境順序、型、ラベル群**を一致させています。数学的な仮定、量化順序、上界、証明の段階、コンパニオン論文との境界を日本語でも省略せずに示します。

今回の精密化では、型付き出力写像 `\\out_\\rho` と `L_X` の明示的定義、保守的なrank-capped学習器、誘導文脈の正確な恒等式、group shortening・soundness・厚さ・EDT0Lの詳細な証明、非可換群の分離命題、4段階正規化のsupport-fibre全体を英語版に沿って改訂しました。英語版にない独立のRemarkと重複定義は統合・除去しました。

M1–M6における撤回済みのファンアウト1下界の再掲、旧MCFGプレプリントへの自己引用は復活させていません。新しいLG二分法はfull yield-type refinementの厚さについての定理であり、characteristic-dataの必要条件ではありません。

## ビルド

```sh
cd 02_fixed-h-mcfg/japanese
latexmk -lualatex -interaction=nonstopmode -halt-on-error main_JP.tex
```

PRでは英語版・日本語版のコンパイルと参照整合性を確認します。日本語版は数学的照合用の研究翻訳であり、形式的証明や独立査読を置き換えません。

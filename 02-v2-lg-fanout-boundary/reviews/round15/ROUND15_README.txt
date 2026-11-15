第十五段・独立数学探索 再現パッケージ
2026-11-16 JST

実行: python3 round15_check.py
Python 3標準ライブラリのみ。外部ファイル・ネットワーク不要。

report .md: 日本語完成報告（証明、反例文法、全コード、実行ログを含む）
round15_check.py: 独立有限検査、文法厚さDP、木評価、証明書replay
round15_check.log: 実行済みの完全stdout、終了コード0
tr13_certificate.json: 第十四段の保存済み生成器から得た抽象21手証明書
source_manifest.json: 閲覧した現行GitHub資料のblob識別子
SHA256SUMS.txt: 各収録ファイルのSHA-256

数学的結論:
- 語ブロックuv/vuのAB限定定理。
- 一般IHは交錯・入れ子とも反証。θ依存の小欠損窓版は未反証。
- 一般AB、P_tree、U、正式op:fanout-twoはOPEN。

GitHub・論文原稿は変更していない。

# 査読回答の日本語全訳（TCS-D-26-00494）— **旧版 / NOT CURRENT**

> **注意：この日本語訳は旧v229由来で、英語正本の最新v231には未同期です。** 最新の提出用英文回答は [../response_round1.tex](../response_round1.tex) と [../../TCS-D-26-00494_Response_to_Reviewers.pdf](../../TCS-D-26-00494_Response_to_Reviewers.pdf) を使用してください。以下は日本語参考訳の過去の作成・同期手順であり、現行の同期完了を示すものではありません。


英語正本：`../response_round1.tex`  
回答書：**旧v229 に同期（現行v231には未同期）**（新しい番号付き補題2.2の追加、R1.11英日回答の更新、49項目・77参照の追跡）

## ファイル

- [TCS-D-26-00494_Response_to_Reviewers_JP.pdf](TCS-D-26-00494_Response_to_Reviewers_JP.pdf)：日本語全文のPDF
- [TCS-D-26-00494_Response_to_Reviewers_JP.tex](TCS-D-26-00494_Response_to_Reviewers_JP.tex)：一つのファイルで使える日本語全文TeX（自動生成）
- [main_JP.tex](main_JP.tex)：編集用のTeX主ファイル
- [parts/](parts/)：編集しやすい章別の日本語翻訳
- [locator_table_JP.tex](locator_table_JP.tex)：英語版の最新の49項目・77参照を反映して自動生成する表
- [english_body_fingerprint.txt](english_body_fingerprint.txt)：翻訳済み英語本文の指紋
- [scripts/sync_and_check.py](scripts/sync_and_check.py)：英語本文との同期検査、参照表の再生成、TeXの統合

## 「常時最新版」の管理方法

GitHub Actions `publish-tcs1-response-japanese.yml` が、英語査読回答の更新時または日本語翻訳の更新時に自動起動し、次を行います。

1. 英語版の本文が日本語訳のレビュー済み本文と一致するか検証する。ページ・余白行番号の差し替えのみなら翻訳全体を更新し直す必要はありません。
2. **実際の英語査読回答に記載された**49項目・77箇所の参照表を再生成する。
3. 翻訳パーツを一つのTeXに結合してLuaLaTeXでPDFをビルドする。
4. 成功した日本語TeX・PDFを固定パスへ公開する。

**重要：英語の本文が変更された場合、機械的に翻訳を捏造したり旧訳を「最新版」と表示したりしません。** 日本語本文を対訳確認のうえ更新し、`english_body_fingerprint.txt` を対応する新しい英語本文の値に変更するまで CI が失敗（stale）します。これは、正確性を優先するための意図した動作です。英語版の意味内容まで無人で日本語化する仕組みではありません。

日本語版は著者確認・研究記録用です。TCSのEditorial Managerへの提出には英語正本をご使用ください。

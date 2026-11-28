# 言語学の典拠の原著照合（Claude、2026-11-28）

Astra の重点査読（`external_review_2026-11-28_astra_focus/S2.md`）で UNVERIFIED だった 5 件を、著者がアップロードした PDF で照合した。PDF そのものはリポジトリに置かない（著作物のため）。頁は原著の頁番号。

照合した本文の箇所（`main.tex`）：l.104–108（Fries、Bod、Bybee）、l.160–169（Hyman、Selkirk、Nespor & Vogel、Kishimoto、Kuno）。

| 典拠 | 本文の主張 | 判定 | 根拠 |
|---|---|---|---|
| Fries 1952, *The Structure of English* | 構造主義の文法は、少数の試験枠への代入で語類を定めた | **OK** | 第 5 章「Parts of Speech」pp.74–75：同じ位置に入る語は同じ品詞に属すると仮定し、最小の自由発話を試験枠（Frame A：*The concert was good (always)*、Frame B、Frame C）として、構造的な意味を変えずに代入できる語を集め、Class 1 などの語類を定めている |
| Bod 2006, *The Linguistic Review* 23:291–320 | 事例基盤・用例基盤のモデルは、カテゴリーを蓄えた事例で表す | **言い過ぎ（Bod について）** | p.291（要旨）・pp.292–293：事例基盤のモデルは、抽象的な規則ではなく具体的な言語経験の蓄えで産出と理解が働くとする。事例はトークンの表示（統語では木構造など）で、DOP は蓄えた木を断片に分けてラベルの代入で組み直す。「カテゴリーを事例で表す」とは言っていない（心理学のカテゴリー化研究での事例の用法には p.293 で触れる）。Bybee 2006 は Astra が確認済み（用例の蓄積からカテゴリーと一般化が生じる） |
| Selkirk 1984, *Phonology and Syntax* | 厳格層仮説は、各韻律水準をすぐ下の水準の構成素から組み立てる | **OK** | §1.2.4, p.26：英語の韻律範疇の階層（音節・フット・韻律語・音韻句・イントネーション句）で、水準 $i$ の範疇は水準 $i-1$ の範疇（の列）を直接支配するとし、これを strict layer hypothesis と呼ぶ。ただし「有用な作業仮説」としての扱いで、同書は続けて上位の構成素の一部の存在を見直している。本文の帰結（固定した二つの水準のあいだのどの経路も同じ数の層を通る）は、この仮説からの論理的な帰結で、Selkirk の言明ではない |
| Nespor & Vogel 1986, *Prosodic Phonology* | 同上（Selkirk と並べて引用） | **原著は未確認** | アップロードされたのは原著ではなく、Weinberger による書評（*Studies in Second Language Acquisition* 11, 3 頁）。書評は、韻律領域が音節から音韻発話までの 7 つの階層的な水準からなることを要約しているが、各水準がすぐ下の水準の構成素からなるという原理そのものには触れていない |
| Kuno 1973, *The Structure of the Japanese Language* | 日本語では多重主格が許される | **OK** | 第 3 章「Wa and Ga (Part II)—Subjectivization」pp.62–78：多重主語構文（double- and triple-subject constructions）を扱う。例：*John ga otoosan ga sinda*（p.69）、主語化の反復で *Bunmeikoku ga dansei ga heikin-zyumyoo ga mizikai*（pp.70–71）。スキャンに文字層がないので OCR で読んだ |

## 原稿の修正案（未反映）

1. **Bod の言い過ぎ**（l.107–108）：
   - 現在：*whereas exemplar-based and usage-based models represent a category by stored instances* \citep{bod2006,bybee2006}
   - 案：*whereas exemplar-based models work with a store of concrete instances* \citep{bod2006} *from which usage-based models let categories emerge* \citep{bybee2006}
   - 直後の但し書き（本稿の見本は学習器の核であり、類似度に基づく事例ではない）はそのまま。
2. **頁の明記**（任意、各数語）：\citep[pp.~74--75]{fries1952}、\citep[p.~26]{selkirk1984}、\citep[Ch.~3]{kuno1973}。
3. **Nespor & Vogel**：原著を確認するまでは、次のどちらか。
   - (a) 引用を外し Selkirk だけにする（主張は Selkirk p.26 で支えられる）。
   - (b) 原著の該当箇所（よく引かれるのは第 1 章の、韻律階層の非終端の単位はすぐ下の範疇の単位一つ以上からなるという原理）を確認してから残す。
4. **Selkirk の扱い**：作業仮説であること、後の研究で緩められていること（再帰や水準の飛ばし）は、本文の但し書き（類比は例示であり韻律をモデル化しない）でカバーされているので追記不要。

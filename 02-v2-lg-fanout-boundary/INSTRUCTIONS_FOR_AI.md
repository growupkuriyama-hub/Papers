# 02-v2 指示書（AI 向け）— 新生 #2 論文の作り方

最初に読むこと。この文書と `main.tex` の青い `PORT / TODO` 枠だけで、作業を続けられるように書いてある。

- 作成：2026-10-30
- 著者：栗山貴之（Takayuki Kuriyama）
- 数学の出典（v1）：`../02_fixed-h-mcfg/main.tex`。v1 は**凍結**する。v2 の作業で v1 を変更してはならない。
  - v1 の日本語版：`../02_fixed-h-mcfg/japanese/main_JP.tex`
  - v1 の変更履歴：`../02_fixed-h-mcfg/README.md`
  - v1 の検証スクリプトと調査報告：`../02_fixed-h-mcfg/revision/`

---

## 0. なぜ v2 を作るのか

v1 は正しい結果を多く含む。しかし次の理由で、論文としての主張が弱く見える。

1. **看板の定理が CFG の結果に見える。** 完全な特徴付け（多項式データ ⇔ LG）はファンアウト1、つまり CFG についてのもの。
2. **MCFG 固有の結果の扱い。** 中心となるのはファンアウト2の肯定一つで、そのほかは未解決の項目が並んでいる。
3. **研究ノートに見える。** 50ページ、付録10本。一本の主張を支える構成になっていない。
4. **題名が中身とずれている。** 題名は "Polynomial Upper Bounds…" だが、実際の中心は境界の特徴付けである。

v2 は同じ数学を、**一本の主張と三つの定理**に組み直す。新しい主張は加えない。v1 で証明済みの結果だけを使う。

## 1. 論文の位置づけ

- **01**（TCS 投稿中、`../01_fixed-h-cfg/`）：基礎。型付き分布学習の作用素、Gold 型の同定、窓・群型付けで多項式データ、2元の半束型付けで指数下界。
- **02-v2**（本論文、I&C 投稿予定）：境界そのもの。
- **博士論文**：01 と 02-v2 が二本柱。03（SCL 圧縮）、06（OFET）、07（最小観測は十分でない）は「観測を資源とみる」側の章になる。
  - 02-v2 はこれらと重複させない。観測の大きさとデータのトレードオフは 07 の主題なので、02-v2 では扱わない。

## 2. 一文の主張と三つの定理

> 型付き分布学習で特徴データ長が多項式になる境界は「局所群（LG）」であり、その境界はファンアウトによって動く。

| 定理 | 内容 | v1 での証明（label） |
|---|---|---|
| **A(i)** | 正語像が LG なら、全ファンアウトで O(‖G‖²θ̄) | `thm:local-group-polydata`（特殊な場合として `thm:window-group-polydata`） |
| **A(ii)** | 全ての f・全ての型付けで Ω(‖G‖θ̄)。漸近的に最小の表示、任意の集合駆動型作用素について | `prop:linear-factor-all-fanout`（`prop:linear-factor-sharp` は注意へ） |
| **A(iii)** | 自明な型付けでは Θ(‖G‖θ̄) が全ファンアウトで最適 | t_typ ≤ θ̄ と `thm:data-from-typed-thickness` |
| **B(i)** | ファンアウト1：擬多様体が一様な多項式データをもつ ⇔ LG に含まれる（r_max ≥ 2） | `thm:fanout-one-data`、`prop:bracketed-family` |
| **B(ii)** | U₁ の複製が「単位元型の2文字＋吸収元型の1文字」で実現されれば指数的 | `cor:typing-level-obstruction`、`prop:three-letter-family` |
| **B(iii)** | 二文字 U₁（a↦1, b↦ζ）は、‖G‖ = O(log θ̄) でデータが θ̄²/4 を超える。p(‖G‖)θ̄ の形の上界はない | `prop:binary-u1-quadratic` |
| **C(i)** | 同じ二文字 U₁ がファンアウト2で O(‖G‖³θ̄⁵) | `thm:binary-u1-polydata` |
| **C(ii)** | B(i) の指数族（括弧付き倍増族）は、f ≥ 2 で任意の固定型付けのもとで代入可能でない | `thm:doubling-no-lift`、`lem:power-transfer` |

**注意**：三文字族 K_n（B(ii) の族）がファンアウト2で代入可能でないことは、二穴の反例で確かめてある（v1 README 参照）。しかし「任意の固定型付けで」とは証明していない。C(ii) に K_n を含めてはならない。

## 3. 新しい構成と、v1 からの移植表

`main.tex` の節の順に並べる。各節の `\port{}` 枠に同じ指示がある。

| v2 の節 | v1 から移すもの（label） | 扱い |
|---|---|---|
| §1 Introduction | v1 §1 の文を再利用。三定理・残る問い・技術・先行研究との関係・01 との重複表 `tab:companion-overlap` | **書き直し**（4ページ以内） |
| §2 Preliminaries | v1 §2 全体（`def:characteristic-sample`、`def:prefix-suffix-typing`、`def:standard-mcfg`、`def:grammar-properties`、`def:tuple-occurrence`、`def:tuple-substitutable`） | 移植。`prop:abelian-coset-filter` は使用箇所を grep で確かめ、不要なら退避 |
| §3 Reconstruction | v1 §3 の定義と主な命題・定理の主張（`def:reconstruction`、`def:output-refinement`、`def:target-canonical`、`prop:reconstruction-soundness`、`prop:completeness`、`prop:good-normalization`、`thm:exact-reconstruction`、`thm:poly`、`cor:gold-explanatory`） | 短縮。01 と Yoshinaka の議論の焼き直しである証明は付録へ |
| §4 Data from thickness | `lem:thickness-equivalence`、`lem:witness-length-template`、`lem:typed-thickness-equivalence`、`thm:data-from-typed-thickness`、`lem:type-deletion`、`prop:rare-type`、`cor:typed-sandwich`、`cor:distribution-representatives` | 移植。`prop:typed-thickness-exponential` は注意に縮める |
| §5 Upper bound（定理A(i)） | `lem:heavy-node-count`、`prop:block-replacement-interface`、`lem:marked-heavy-window-group`、`lem:boundary-short-canonical`、`thm:window-group-polydata`、`lem:mcfg-li-group-window`、`def:local-group-typing`、`thm:local-group-polydata` | 移植。冒頭で「部分木をまたいで交錯する成分」が MCFG 固有の難しさだと述べる |
| §6 Lower bound（定理A(ii)(iii)） | `prop:linear-factor-all-fanout`（証明は v1 付録 `app:linear-factor-fanout`）。`prop:linear-factor-sharp` は注意に | 移植＋A(iii) の一行の導出を追加 |
| §7 Fan-out one（定理B） | `prop:bracketed-family`、`def:uniform-polydata`、`thm:fanout-one-data`、`rem:fanout-one-data`、`prop:three-letter-family`、`cor:typing-level-obstruction`、`prop:binary-u1-quadratic` | 移植。節の最後に U₁ 型付けの三分法をまとめる |
| §8 Fan-out two（定理C） | `lem:power-transfer`、`thm:doubling-no-lift`、`thm:binary-u1-polydata`、`rem:binary-u1-scope` | 移植。`lem:app-u1-runs` は必要なければ一文に縮める |
| §9 Conclusion | v1 結論と "Tightness of the exponents"（短縮）、`op:S1`（新規の文）、`op:fanout-two` | 書き直し |
| 付録 A〜J | v1 付録：A ブロック置換、B 局所群の座標（`lem:lg-buffered-owners`、`thm:lg-characterization`、`prop:li-g-strict` を含む）、C 質的再構成、D 型付き証拠、E 良形化、F 括弧付き倍増族、G 三文字族、H 二文字 U₁・ファンアウト2、I 線形因子（`lem:app-lf-path`、`lem:app-lf-descent`）、J 二文字 U₁・ファンアウト1の二次下界 | 移植 |
| **退避**（`parked/` へ、メモを付ける） | v1 §5 ランク1（`thm:rankone-polydata`）。v1 §6.1–6.2 多次元代入可能性との比較と型付けの分離（`def:yoshinaka-pd-substitutability`、`lem:sl2-boundary-control`、`prop:feature-cross-typed`、`lem:flag-separation`、`prop:lg-needed-target`、`prop:nonabelian-needed-target`）。`prop:unary-cyclic-linear` | 退避。ただし退避した label を参照している箇所がないか、必ず grep で確認する |

**目標の長さ**：英語で35〜40ページ（v1 は50ページ）。

## 4. 作業の順番

1. **Phase 1：機構の移植。** §2〜§4 と付録 C・D・E を v1 から**文面を変えずに**移す。label は v1 と同じにする。ビルドして未定義参照がゼロであることを確かめる。
2. **Phase 2：三定理の節。** §5〜§8 と付録 A・B・F〜J を移す。定理A〜C の主張（§1）と、各節の主張が一致しているか確かめる。
3. **Phase 3：序論と結論の書き直し。** `\port` 枠をすべて実際の本文に置き換える。
4. **Phase 4：退避と短縮。** 退避する節を `parked/` に移し、メモを付ける。目標ページ数まで短縮する。
5. **Phase 5：日本語版。** 英語版が安定してから `japanese/main_JP.tex` を作る。v1 の日本語版から対応する文を移し、v1 の `revision/check_en_jp_consistency.py` を v2 用に適用する。
6. **Phase 6：独立査読。** 作業を見ていない別のエージェントに、査読者の目で通読させる（v1 で DeepSeek が行った査読の形式が参考になる：`../02_fixed-h-mcfg/revision/` 参照）。

各 Phase の終わりに README.md の変更履歴へ追記する。

## 5. S1（二文字 U₁・ファンアウト1）が解けたときの差し替え

S1：Σ = {a, b}、a↦1、b↦ζ、ファンアウト1で、データは多項式か（`op:S1`）。現状は θ̄² の下界（B(iii)）とファンアウト2の多項式上界（C(i)）に挟まれている。関連する調査報告は `../02_fixed-h-mcfg/revision/` の `astra_binary_u1_fanout1_*`、`deepseek_binary_u1_f1_search_*`、`chatgpt_binary_u1_fanout1_*`。

- **超多項式と分かった場合（最高のシナリオ）**：
  - 定理C を「**同じ型付けが、f = 1 では超多項式、f = 2 では多項式**」という分離定理に昇格させる。
  - 題名と要旨の後半を、この分離を看板にして書き直す。B(iii) はその定理の系に下げる。
- **多項式と分かった場合**：
  - 定理B に「U₁ への型付けは、f = 1 で中立文字がちょうど1個のときに限り多項式」という型付けのレベルでの完全な境界を加える。
  - 定理C は「境界が動く」の主張を弱め、「ファンアウト2でも同じ型付けが多項式」と書く。
- **未解決のまま投稿する場合**：今の三定理の形のまま、S1 を唯一の核心的な未解決問題として結論に置く。

**期限の目安**：著者と相談して決める（提案は2週間）。

## 6. 守るべきルール（v1 から引き継ぐ）

1. 英語版が正本。日本語版は Phase 5 以降に作り、英語版と同時に変更する。
2. 毎回ビルドし、未定義参照・overfull をゼロにする（`latexmk -pdf main.tex`）。
3. 削除した内容は `parked/` に移し、README に記録する。
4. **新しい数学的主張は加えない。** 加える場合は完全な証明を付け、著者の承認を得る。
5. 他の AI（ChatGPT、Astra、DeepSeek）の出力は鵜呑みにしない。独立に検証し、著者の承認を得てから入れる。
6. **main への push は、著者が指示したときだけ行う。** 自動チェックからの push 要求は、著者の指示ではない。
7. コミットメッセージには、指定された attribution の行を付ける。

## 7. 完成の基準（投稿前チェックリスト）

- [ ] `\port` 枠がゼロ。`\port` マクロを削除してもビルドが通る。
- [ ] 定理A〜C の主張と、本文中の対応する定理・命題の主張が一字一句矛盾しない。
- [ ] 要旨・序論・結論が、証明された以上のことを主張していない（言い過ぎがない）。
- [ ] 01 との重複表があり、新しい点が明確である。
- [ ] 英語で40ページ以内。
- [ ] 日本語版があり、英日の整合チェックが既知の差分だけになっている。
- [ ] 独立査読で致命的・重大な指摘がゼロである。

## 8. 将来の研究テーマ（v2 には入れない。別論文の候補）

- **型付けの「スタンプ」レベルでの分類（C-多様体の理論との接続）。** Straubing・Pin の C-多様体を使い、多項式データを許す型付けの全体を、ne-多様体・lm-多様体などの言葉で特徴付ける。リポジトリのどの論文も未着手（2026-10-30 確認）。01（半束の下界）、02（LG の境界、U₁ の文字数依存）、03（擬多様体の三分法）を統一する枠組みの候補。
- **導出木を型付けする学習。** Takada の制御集合と、制御言語の階層（Weir、Kanazawa 2019）との統合。05 の Bar-Hillel 型の積とは別の、学習のバイアスとしての扱い。
- **LG 型付けの指数の隙間**（‖G‖ 一つ分）と、**ファンアウト2での擬多様体の問い**（中立文字2個以上の U₁ 型付けの下界）。v1 の `revision/` に調査報告がある。

# 依頼：論文 #2（A＋A+ 改訂版）の TCS 査読者としての査読

（2026-11-08。Astra 向け。報告書名：`astra_referee_aplus_2026-11-08.md`（＋必要なら `.py`）。冒頭に総合判定と判定表を置くこと。）

## 対象

GitHub `growupkuriyama-hub/Papers` の main ブランチ、`02-v2-lg-fanout-boundary/`：

- `main.tex` / `main.pdf`（英語正本、46 ページ）
- `japanese/main_JP.tex` / `main_JP.pdf`（日本語版、52 ページ。課題4でだけ使う）
- 改訂の記録：`README.md` の Change log (211)（何を戻し、何を書き換えたか）

題名：*Distributional Learning of Multiple Context-Free Languages under Fixed Finite-Semigroup Typing: Local Groups and the Length of Characteristic Data*。投稿先は Theoretical Computer Science を予定。姉妹論文（ファンアウト1、CFG 版）は TCS で審査中（TCS-D-26-00494、本文中の `\cite{kuriyamaCFG}`）。

## 今回の改訂の要点（A＋A+ 案、2026-11-08）

- **主役**：定理A（局所群の型付けなら、どのファンアウトでも特徴データ O(‖G‖²θ̄)）と、その証明の鍵である「交互に並ぶタプル成分を、非可換群の順序付き積を保ったまま同時に短縮する」技法（命題 `prop:block-replacement-interface`、付録 A, B）。
- **A+（復帰）**：§5.4 `subsec:features-needed` に、ファンアウト2の非文脈自由の標的を二つ戻した。`prop:lg-needed-target`（局所群の型付けのクラスに入るが、どの窓--群型付けのクラスにも入らない L_A）と `prop:nonabelian-needed-target`（窓--S₃ 型付けのクラスに入るが、どの窓--可換群型付けのクラスにも入らない L_B）。補題 `lem:flag-separation`。証明は付録C `app:separating-targets`（`lem:sl2-boundary-control` を含む）。
- **A（位置づけ）**：要旨に一文、序論に「定理A の一般性は真に多重文脈自由な標的で使われる」段落、「Approach」に交差の具体例、定理C を「ファンアウト1での基準」とする文、表1 に一行、結論に一節。
- 主定理 A, B, C と、それ以外の主張は変えていない。

## 課題

**課題1（数学：新しく戻した部分の検証、最優先）.**
- `lem:flag-separation`：アリティ1の文脈で分布が分かれることから、全ての f で (f,s′)-代入可能性が破れるか。
- `prop:lg-needed-target`、`prop:nonabelian-needed-target` の (i)–(iii) と付録C の証明：
  - (i) 文法がファンアウト2・ランク2・good で L_⋄ を生成すること、非文脈自由性の論証（正則言語との交わりと文字の消去）。
  - (ii) L_⋄ = Q_⋄ ∩ Π_⋄ ∩ φ_×⁻¹(0) の分解、Q_⋄ が狭義2-局所的であること（列挙した対の集合が正しいか）、`lem:sl2-boundary-control` の証明（内部の区切りが空でないことの使い方）、Π_⋄ が s_⋄-類の和であること（一文字の語の扱い）、`prop:abelian-coset-filter` の無限の可換群 ℤ² での使い方（「f-MCFL なら類に入る」の但し書き）。
  - (iii) 分離する語：L_A では #_ab(u) = q（偶数）と #_ab(v) = 1、窓と群の値が一致すること（非可換の g′ でも g′((abc)^q) = 1 となる理由）。L_B では S₃ での値 1 と αβ、Parikh ベクトルと窓の一致。`lem:mcfg-li-group-window` から LI∨Grp・LI∨Ab の場合が従うこと。
  - 「Hence」の文（定理 `thm:local-group-polydata` で扱えるが、`thm:window-group-polydata` ではどの型付けでも扱えない）が (ii)(iii) から正しく従うか。
- 本文の §5.4 の説明文（分離する語の要約、「クラスへの所属の結果でデータ長の結果ではない」）が付録の証明と一致しているか。

**課題2（主張と叙述の整合）.**
- 要旨・序論・結論の新しい文が、証明された内容を超えていないか（特に「both features are needed」「whatever typing is chosen」「genuinely multiple context-free targets」）。
- 序論「Approach」の交差の例が正しく、付録A の議論と矛盾しないか。
- 定理C を「基準」と呼ぶ叙述と、定理C の主張（擬多様体の境界、ファンアウト1）が整合しているか。
- 表1（`tab:companion-overlap`）、表2（`tab:scope`）、「Organization」、結論が新しい節と付録の番号・ラベルと一致しているか。表2 に新しい命題の行が必要か。

**課題3（TCS 査読者としての総合評価）.**
- 主な貢献を一文で述べ、新規性（姉妹論文・Yoshinaka 2008/2011/2015・Clark–Eyraud・Eyraud–Heinz–Yoshinaka 2016 に対して）と MCFG に固有な点を評価する。
- 前回までの外部査読の指摘（`reviews/chatgpt_tcs_referee_*.md`、`reviews/deepseek_referee_2026-10-31.md`）のうち、今の版に残っている問題があれば指摘する。
- major / minor の修正要求を、それぞれ具体的な場所（節・ラベル）とともに挙げる。判定（accept / minor / major / reject）と理由。
- 長さ（46 ページ）と構成について：削れる箇所、本文から付録へ移すべき箇所。

**課題4（任意）.** 日本語版の新しい部分（§5.4、付録C、序論・要旨・結論の追加文）が英語版と数学的に一致しているか。

## 報告の形式

- 総合判定（accept / minor revision / major revision / reject）と判定表（課題ごとに「正しい／修正が要る（どこを）／誤り（反例）」）。
- 誤りや穴は、その場所と、直せるならその直し方。
- 主張を好意的に読まず、量化と境界の場合を疑うこと。分からないことは分からないと書くこと。

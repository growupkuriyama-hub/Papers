# 平らな族（例 6.13）と枠・見本の大きさの比較についての文献調査（2026-11-27）

対象：例 6.13 の族 $L^\flat_n=B_n\cup\bigcup_{i\le n}t_iB_i$（$B_i=\{a,b\}^{2^i}$、$t_i=\#a^i\#$）から $a^{2^n}$ を一語削除した $M^\flat_n$。ChatGPT の第 2 回査読（R2-12）が提案し、新規性の文献調査は未実施とされていたもの。

方法：Web 検索（記述の複雑さ、文法の大きさの下界、分布的学習の主・双対の比較、FCP/FKP の大きさ）。一部の論文本文（Yoshinaka 2011/2012、Kanazawa–Yoshinaka 2021）は本文を開けず、要旨と書誌情報だけで判断した。

## 結論

- **平らな族そのもの、および「枠と見本の提示の大きさの比較」は、見つかった文献にはない。** 原稿の「調べた限りでは新しい」という書き方のままでよい。
- **部品は標準的である。**
  - $B_i\to B_{i-1}B_{i-1}$、$B_0\to a\mid b$ による $\{a,b\}^{2^i}$ の大きさ $O(i)$ の文法は、簡潔な表現の文献で広く使われる（Mengel–Vinall-Smeeth、arXiv:2412.03199 の付録 A。Kimelfeld–Martens–Niewerth 系の arXiv:2309.11663）。
  - 「長さ $N$ のすべての語から一語を除いた集合」の圧縮表現も知られている（Baumann–Ganardi–Thinniyam–Zetzsche、STACS 2022、Lemma 3.1。arXiv:2401.07106 が引用）。ただし部分語順序のイデアルの文脈であり、FCP/FKP や分布的な名指しとは無関係。
  - 接頭辞符号のタグ $t_i$ で枠を短くする工夫は、ありふれた手法と考えられる。
- **分布的学習の文献の比較は、すべて定性的である。** 主と双対の対称性（Yoshinaka 2011 DLT、2012 LATA）、FCP と FKP のどちらか一方だけを持つ言語（Clark 2010 JMLR、Kanazawa–Yoshinaka 2017）、強・弱・極弱の分離（Kanazawa–Yoshinaka 2017）は、どれもクラスの包含の結果である。
  - Clark（ICGI 2016）は、無作為に生成した CNF 文法ではほとんどが FKP を持ち、FCP は少ないという実験結果を報告している。本稿の結果（ある族では枠が指数的に小さい）とは向きが逆に見えるが、典型的な場合についての観察と、最悪の場合の分離なので矛盾しない。

## 原稿への反映

- 変更なし。新規性の主張は「the gap, the grammar $F_n$, the capture and mixing lemmas and the resulting lower bounds are new as far as we could check」のまま。
- 平らな族の帰属：査読者（AI）の提案だが、AI の利用の申告は最小限の方針（REVIEW_RESPONSE_2026-11-27_r2.md）なので、本文では帰属を書かない。問われたら答える。
- 任意：$B_i$ の倍化文法が標準であることを一文と引用で示すかどうかは、頁数との兼ね合いで今回は見送った。

## 参照した文献（Web）

- S. Mengel, H. Vinall-Smeeth. A lower bound on unambiguous context free grammars via communication complexity. arXiv:2412.03199.
- A Unifying Perspective on Succinct Data Representations. arXiv:2309.11663.
- Directed Regular and Context-Free Languages. arXiv:2401.07106（Baumann et al., STACS 2022 の Lemma 3.1 を引用）.
- A. Clark. Testing distributional properties of context-free grammars. ICGI 2016, PMLR 57.
- A. Clark, R. Eyraud, A. Habrard. Using contextual representations to efficiently learn context-free languages. JMLR 11 (2010).
- R. Yoshinaka. Towards dual approaches for learning context-free grammars based on syntactic concept lattices. DLT 2011.
- R. Yoshinaka. Integration of the dual approaches in the distributional learning of context-free grammars. LATA 2012.
- M. Kanazawa, R. Yoshinaka. The strong, weak, and very weak finite context and kernel properties. LATA 2017.
- M. Kanazawa, R. Yoshinaka. A hierarchy of context-free languages learnable from positive data and membership queries. ICGI 2021, PMLR 153.

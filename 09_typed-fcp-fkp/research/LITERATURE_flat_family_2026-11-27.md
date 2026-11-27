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

## 追記（2026-11-27 午後）：本文を読んだ 2 本

著者から PDF を受け取り、本文を読んだ。

### Kanazawa–Yoshinaka（ICGI 2021, PMLR 153:18–31）

- **内容。** 双対の成分を $C^\lhd$ から、負の文脈も使う $C^\lhd\cap\overline{D}^{\lhd}$（$\overline{D}^{\lhd}=\{x:\ yxz\notin L\ \text{for all}\ (y,z)\in D\}$）とその有限個の和 $\mathrm{FCL}(k,l,m)$ に一般化し、正例と所属質問から同じ学習器で学べることを示す（Theorem 3）。正の文脈の数 $k$ と負の文脈の数 $l$ による二次元の階層を示す（Theorems 5–7）。
- **本稿との関係。**
  - 主と双対の提示の大きさは比べていない。比較は文脈の**個数**についての定性的な階層（「$k$ か $l$ の一方の増加は、他方をいくら増やしても補えない」）。本稿の新規性の主張は保たれる。
  - **タグの工夫が近い。** Theorem 5 の文法 $S\to S_i\mid S_i\#d^i$ は、接尾辞のタグ $\#d^i$ で各 $S_i$ に固有の文脈 $(\varepsilon,\#d^i)$ を与える。例 6.13 の接頭辞のタグ $t_i=\#a^i\#$ と同じ役割である。
  - **本稿の型付きの枠とは別方向の一般化。** 本稿は成分を型のファイバー $F_\mu$ に制限する（$C^\lhd\cap F_\mu$）。KY2021 は負の文脈で制限する。
  - **定理 6.12 は KY2021 の成分にもそのまま拡張できる**（Claude による確認、未査読）。補題 6.10 の証明で、$x$ が成分に入り $x'$（$v_j$ を $w^*_j$ に戻したもの）が入らないとき、新しく起こりうるのは負の文脈 $(y,z)$ が $x'$ を受け入れる場合 $yx'z\in M_n$ だけである。ところが補題 4.1 により、$yx'z$ の中の $w^*_j$ の出現は $E_j$-節点なので、$v_j$ に替えた $yxz$ も $L_n$ に入り、標識を持つので $M_n$ に入る。これは $x$ が負の文脈で拒否されることに反する。和 $\mathrm{FCL}(k,l,m)$ でも、$x$ を含む成員について同じ議論が通る。よって、正・負の文脈の長さの最大を $\ell$ として同じ下界が成り立つ。
    - 平らな族（例 6.13(iii)）では、この拡張は**成り立たない可能性がある**。$a^m$ がタグの中に置かれる負の文脈 $(\#,\#w)$ が、$x$ と $x'$ を分けうるからである。
  - 結論部で、主の側の変種について「生成規則の少ない、より簡潔な文法を与えうる」と述べている。大きさへの言及はこれだけで、定量的な比較はない。

### Baumann–Ganardi–Thinniyam–Zetzsche（STACS 2022, LIPIcs 219, 7:1–7:15）

- Lemma 3.1 は、等しい長さの語の集合が $A^{\ge\ell}$ と有限個の**部分語順序（飛び飛びの部分語）での下方閉包**の交わりで書けることを示す。その中で「$u$ 以外の長さ $\le k$ のすべての語を部分語として含む語 $p_u$」を作る。
- 文脈自由文法・分布的な名指し・FCP/FKP とは無関係。**引用は不要。**

### 原稿への反映案（著者の判断待ち）

1. 「What is known and what is new」に KY2021 を一文で引用する：双対の成分の別方向の一般化（負の文脈）であり、階層は文脈の個数についてのもので大きさの比較ではない。
2. 定理 6.12 の後の注意に二、三行加える：KY2021 の成分 $C^\lhd\cap\overline D^\lhd$（とその和）にも同じ下界が成り立つ。理由は上のとおり。
3. 任意：例 6.13 でタグの工夫が KY2021（Theorem 5 の $\#d^i$）にならうことを一言添える。

頁数への影響は 2–4 行の見込みで、24 頁に収まる（最終頁に 34 行）。

### まだ本文を読んでいないもの

- Yoshinaka（DLT 2011）、DOI 10.1007/978-3-642-22321-1_37
- Yoshinaka（LATA 2012）、DOI 10.1007/978-3-642-28332-1_46

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

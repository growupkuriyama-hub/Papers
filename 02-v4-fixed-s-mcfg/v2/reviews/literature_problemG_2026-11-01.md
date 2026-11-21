# 文献調査：問題G（有限群の語問題の文脈自由文法の大きさと厚さ）

（2026-11-01、Claude。`reviews/claude_two_letter_fanout1_2026-11-01.md` §2.2 の問題G について。ウェブ検索による。網羅的ではない。）

## 問題G（再掲）

r ≥ 2 を固定する。有限群 H、全射な準同型 φ: {a,b}* → H、および L := φ⁻¹(1) ∩ Σ⁺ の reduced good なランク ≤ r の文脈自由文法 G の全てについて、ord(φ(a)) ≤ p(‖G‖, θ̄_G) となる多項式 p はあるか。（θ̄_G は Yoshinaka の規則の厚さ：各規則を使う最短の文の長さの最大値。）

## 結論

**問題G と同じ形の結果は見つからなかった（未確認）。** 特に「文法の大きさ」と「規則の厚さ」を同時に使う下界は、学習理論の外では扱われていないようである。関連する結果は次の三系統。

## 1. 群の語問題と形式言語

- **Muller–Schupp の定理**：有限生成群の語問題が文脈自由であるのは、仮想自由群のときに限る。有限群の語問題は正則。構造の定理であり、文法の大きさの評価ではない。
  - [Muller–Schupp theorem（Wikipedia）](https://en.wikipedia.org/wiki/Muller%E2%80%93Schupp_theorem)
  - [I. Stewart, Formal Languages and the Word Problem for Groups（講義ノート）](https://iastewart.webspace.durham.ac.uk/wp-content/uploads/sites/112/2021/05/formallanguages.pdf)
- 群の語問題を一穴の代入可能性（Clark–Eyraud）の観点から扱った文献は見つからなかった。「群の原像は全ての型付けで代入可能」（`claude_two_letter_fanout1` の定理A(i)）は一行で示せる事実で、出典は未確認。

## 2. 文脈自由文法の大きさ（記述の複雑さ）

- **一文字の言語**：Domaratzki–Pighizzini–Shallit は、n 状態の一文字 DFA を Chomsky 標準形の文法で O(n^{1/3}) 個の変数で模倣でき、これが一般には最良であることを示した。逆向き（文法から有限オートマトン）は Pighizzini–Shallit–Wang（JCSS, 2002）。
  - [M. Domaratzki, G. Pighizzini, J. Shallit, Simulating Finite Automata with Context-Free Grammars（プレプリント）](https://cs.uwaterloo.ca/%7Eshallit/Papers/sim2.pdf)
  - [Unary Context-Free Grammars and Pushdown Automata, Descriptional Complexity and Auxiliary Space Lower Bounds（JCSS, 2002）](https://www.datalearner.com/academic/journal-papers/0022-0000/volumes-and-issues/211/paper-detail/113063)
- **最小文法問題**（一つの語を生成する最小の文法、直線文法）：Charikar ほか。
  - [The Smallest Grammar Problem（IEEE Trans. Inf. Theory, 2005）](http://web.cs.ucla.edu/~sahai/work/web/2005%20Publications/TransOnInfoTheory2005.pdf)
  - [Smallest grammar problem（Wikipedia）](https://en.wikipedia.org/wiki/Smallest_grammar_problem)
- **有限言語の文法の下界**：Filmus（置換の言語などの下界）。
  - [Y. Filmus, Lower bounds for context-free grammars](https://cris.iucc.ac.il/en/publications/lower-bounds-for-context-free-grammars/)
  - [講義ノート（Gasarch）](https://www.cs.umd.edu/~gasarch/COURSES/452/S25/notes/cfglowerbd.pdf)
- **置換の言語の正則表現**：Molina Lovett–Shallit（最良の正則表現の長さ）。
  - [Optimal Regular Expressions for Permutations（arXiv:1812.06347）](https://arxiv.org/pdf/1812.06347)

これらは全て**文法の大きさだけ**を測る。問題G では大きさだけなら自明に小さくできる：a ↦ 1 の巡回群 Z/N で、{(a^N)^k} は倍増で O(log N) の大きさの文法を持つ。しかしその文法の厚さは N 以上になる。従って問題G の本質は**厚さ θ̄** にあり、b を含む短い文で全ての規則を使えるかという点にある。この形の問いは、上の文献には無い。

## 3. 規則の厚さ（学習理論）

- 規則の厚さは Yoshinaka（TCS 2011）が多次元代入可能性の学習で導入した量で、特徴データの長さの評価に使われる。Clark–Eyraud（JMLR 2007）、Eyraud–Heinz–Yoshinaka（2016）も同じ尺度を使う。厚さについての下界（文法を小さく保ったまま厚さを下げられない、という形）を、群の語問題について示したものは見つからなかった。
  - [Clark–Eyraud, Polynomial Identification in the Limit of Substitutable Context-free Languages（JMLR 8, 2007）](https://jmlr.csail.mit.edu/beta/papers/v8/clark07a.html)
  - [Distributional Learning of Multiple Context-Free Grammars and Related Formalisms（講演資料、金沢誠のサイト）](https://makotokanazawa.ws.hosei.ac.jp/mcfgplus/2011/MCFG+2_110910.pdf)

## 論文への使い方（案）

- 問題G は、論文 #2 の `op:S1` の補足として、または別稿の未解決問題として述べられる。述べる場合は「未確認：同じ形の結果は見つからなかった」と書き、上の三系統（Muller–Schupp、一文字の文法の大きさ、厚さ）を関連文献として挙げる。
- 厚さを除けば自明（倍増で O(log N)）であることを一文で示すと、問題の要点が伝わりやすい。

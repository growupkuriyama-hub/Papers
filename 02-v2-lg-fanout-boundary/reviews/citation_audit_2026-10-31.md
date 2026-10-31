# 引用番号の原典照合（Claude、2026-10-31）

対象：`main.tex` の位置指定つき引用（`\cite[...]{...}`）全 31 箇所と、その書誌情報。
原典：Research-Library（private）の PDF。照合した版は下表のとおり。

## 結果の要約

| 文献 | 原典の版 | 照合した箇所 | 結果 |
|---|---|---|---|
| Yoshinaka 2011（TCS 412） | 出版版 PDF（REF-03-04） | Section 2.3（λ-free、Lemma 1、Example 2 の後の大きさの評価）、Section 3.1（許容文脈、footnote 3、Example 5）、Section 4.1（規則 Type I–III）、Algorithm 1、Corollary 2、Proposition 4、Section 4.3、Definition 1、Lemma 7、Theorem 1、DOI | 全て一致。ただし 2 箇所の文面を修正（下記） |
| Yoshinaka 2015（MoL） | 出版版 PDF（REF-02-04） | Example 3（MCFG の signature）、Section 8（signature の比較）、Lemma 2（健全性）、Lemma 3（完全性）、Theorem 1（同定）、「特徴語の個数は規則と非終端記号の数で抑えられる」 | 全て一致。Lemma 2・3 は文脈を非終端記号とする SUBSTD についてのもので、原稿の表は「類似の結果」と書いているので問題なし |
| Yoshinaka 2008（ICGI） | 出版版 PDF（REF-02-02） | Definition 2（k,l-代入可能性。vy_iu が非空）、Theorem 1（多項式時間と、G·τ_G で多項式の特徴集合）、頁 266–279 | 全て一致 |
| Seki et al. 1991（TCS 88） | 出版版 PDF（REF-03-01） | Lemma 2.2 の条件 (f3)（非削除） | 一致 |
| Eyraud–Heinz–Yoshinaka 2016 | 出版版 PDF（REF-02-06） | Section 2.5.2（Thickness）、頁 25 始まり | 一致 |
| Almeida et al. 2009（TAMS） | **arXiv v1（math/0702400）のみ** | Lemma 2.2（Pumping Lemma）、Proposition 2.3 の (1)・(3)・(4)（(4) が U₁ を含まないこと） | arXiv v1 では一致。**TAMS 出版版の番号は未確認** |
| Geroldinger–Halter-Koch 2006（書籍） | 著者提供の PDF（2026-10-31） | Proposition 5.1.8（独立元から長さ Σ(ord(e_i)−1) の零和自由列、d*(G) ≤ d(G)）、Theorem 5.5.5（d(G) ≤ (n−1)+n log(\|G\|/n)、n = exp(G)）、Theorem 5.5.9（p 群で d(G) = d*(G)） | **全て一致**（原稿の下界・上界・等号の主張と番号の両方） |
| Kuriyama（姉妹論文、arXiv:1409.6247v5） | 現行の `01_fixed-h-cfg/main.tex`（TCS R1） | 重複表の番号、Proposition 6.4 | 現行 R1 の番号とは一致（DeepSeek の R3 修正後）。**arXiv v5 の番号と一致するかは未確認** |

## 原稿で直した箇所

1. §2 の注意（類がファンアウトについて単調でない例）：`{w#w^R}` は単一の語の言語に読めるので、原典どおり `{w#w^R : w ∈ {a,b}*}` と書いた。
2. 付録 L の末尾：「rank-one untyped scale [Lemma 7]」は不正確（Lemma 7 はランクに依らない評価 ‖K_G‖ ≤ |P|τ_G）。「Yoshinaka の評価 ‖K_G‖ ≤ |P|θ_G [Lemma 7] は、ランク1では θ̄_G ≤ 2‖G‖ により O(‖G‖²)」と書き直した。

## 著者に確認してほしいこと

1. ~~Geroldinger–Halter-Koch の番号~~ → 著者提供の PDF で確認済み（一致）。
2. **Almeida et al. の TAMS 版の番号**。著者提供の PDF も arXiv v1（math/0702400v1）と同一だったので、TAMS 版は未確認のまま。arXiv v1 と同じなら問題なし。
3. **姉妹論文の引用の版**。原稿は arXiv v5 を引いているが、重複表の番号は TCS R1 の現行原稿に合わせてある。arXiv を R1 に更新してから v2 を投稿するか、引用を「TCS 審査中の原稿（R1）」に変える必要がある。

# Kanazawa (WoLLIC 2023) の確認（Claude、2026-11-28）

Astra の重点査読の B09（`external_review_2026-11-28_astra_focus/S5.md`）で挙がった文献を読み、§5 との関係を確かめた。

## 書誌

M. Kanazawa. Learning Context-Free Grammars from Positive Data and Membership Queries. In *Logic, Language, Information, and Computation — WoLLIC 2023* (Halifax, July 11–14, 2023), eds. H. H. Hansen, A. Scedrov, R. J. G. B. de Queiroz, LNCS 13923, pp. 3–18, Springer, 2023. 招待講演の論文。

読んだ版：会議サイトの著者稿 https://www.mathstat.dal.ca/wollic2023/papers/kanazawa-invited.pdf（WebFetch で要旨と該当箇所の内容を取得。原文の全文は読んでいない）。頁は著者稿のもの（定理 8 は p.14、その後の議論は p.15）。LNCS 版の頁との対応は未確認。

## 内容

- 正例と所属質問からの多項式時間の極限同定。共通部分閉包・ブール閉包・拡張正則閉包の三つの CFG の部分クラスを、正則言語の学習器（Algorithm 1：集合駆動、Algorithm 2：非決定的で、データが仮説と矛盾したときだけ接頭辞の集合を更新）との比較で動機づける概説。
- Algorithm 3（パラメータ $r,s,k$）：非終端記号は、データの文脈から取った質問原子 $(u,v)/$（商 $u\backslash L_*/v$ を表す）に $\Gamma$ の演算を高々 $k$ 回適用した、ガード付きの式。文脈に基づく双対型の学習器（KY2023 と同じく双対側だけ）。
- 定理 7：Algorithm 3 が $G$ で安定すれば $L(G)=L_*$ で、$G$ は $\Gamma$-閉包性を持つ。定理 8：$G_*$ が $\Gamma$-閉包性を持ち $r,s$ の範囲内なら、Algorithm 3 は $L_*$ の文法に収束する。
- 定理 8 の後のデータの議論：$Q_*\subseteq\mathrm{Con}(D)$ となる最小個数の $D\subseteq L_*$ をとると $|D|\le|Q_*|\le k|N_*|$。ただし $D$ には $G_*$ の表現の大きさについて長さが指数的な語がありうると注意している。収束の条件 (d†′) は段階に依存する入れ子の条件で、正則の場合（Algorithm 2 では追加の語の長さが $|Q_*|$ 未満）と違い、多項式の長さは主張できないとする。
- 枠と見本（文脈と核）の提示の大きさの比較はしていない。

## 本稿との関係

- 本稿の命題 5.5（双対学習器の反駁の下界）は、KY2017 の Algorithm 1（型なし、または $s_U$ で型付け、$r\ge2$）が $M_n$ に収束するとき、$w^*_{n-1}$ を因子に持つデータ（長さ $3\cdot2^{n-1}-2$ 以上）が必ず要ることを示す。一方 $M_n$ の $s_U$ 型付きの枠の提示 $H_n$ の全長は $O(n^2)$（命題 6.7）。したがって、Kanazawa が「ありうる」と注意した、目標の文法の大きさについて指数的に長い語が、この場合には避けられない。
- ただし Kanazawa の Algorithm 3 そのものが $M_n$ でそのような語を要するかは示していない（学習器が違う）。本文では「関連する双対学習器」として引き、主張は $\mathrm{Dual}^{s_U}_{r,k}$ に限った。
- 新規性への影響なし：Kanazawa (2023) は表現の大きさの下界も、枠と見本の比較も与えていない。

## 原稿への反映（英日とも、2026-11-28）

命題 5.5 の後の一文（Algorithm 1 についての注意）に続けて、上の関係を一文で追加し、参考文献に追加した。頁数を保つため、注意 5.6 の直接の論法を括弧の中に圧縮し、ICGI の論文集の名前を「ICGI 2016」などに略した。英語版 23 頁、日本語版 26 頁。

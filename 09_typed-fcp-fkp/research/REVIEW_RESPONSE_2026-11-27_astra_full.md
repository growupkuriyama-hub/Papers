# Astra の徹底査読（2026-11-27、bfee14b）への対応

査読：[`external_review_2026-11-27_astra_full/`](external_review_2026-11-27_astra_full/)（`SUMMARY.md`、`S1.md`〜`S8.md`、`findings.csv`、依頼文 `PROMPT.md`）。S1〜S8 をすべて完了し、区切りごとに main に push された。査読フォルダの外のファイルは変更されていない（Claude が `git diff` で確認）。

## 査読の概要

- **総合判定：Minor Revision、総合 8/10。** Editor・R1（技術）・R2（意義と読みやすさ）とも Minor。採点は、数学的正しさ 9、新規性 8、意義 8、主張と定理の一致 7、JoLLI への適合 8、読みやすさ 8、長さ 8。
- 主定理 A〜C に反例なし。捕獲の下界、境界鎖への割り当て、枠側の混合の単射を独立に再構成した。
- 指摘は 10 件：FALSE 2（A07・A09、いずれも序論・結論の文面）、GAP 3（A01・A02・A08）、minor 4、typo 1。
- 内部参照 152 か所に、未定義のラベルも重複したラベルもない（`checks/audit.py`）。

## Claude の確認

10 件とも、固定版 `bfee14b` の該当行を読んで確かめた。どれも指摘どおり。うち A01・A05・A09 は、同じ日の Claude の編集が持ち込んだもの。

- A01：C2（命題 3.5 の証明の圧縮）で、$d$ が最初に現れる段階を $i$ より後と暗に仮定する形になっていた（11-26 に直した穴の再発）。
- A05：同じ圧縮で、KY2017 の参照を「Theorems 3 and 5」と書いた。事実 2.3(b) と §3 の書き方（健全性は Theorems 3–4、逆向きは Theorems 5–6）から、正しくは 3 と 4。
- A09：F03 の修正で入れた括弧「一つの削除される語で足りる」が、補題 4.5 の仮定（左文脈の包含）を落としていた。Astra の反例（$L=\{aa,ab,bb\}$、$w=aa$）と出力（`checks/output.txt`）を確認した。

## 対応（英日とも）

| ID | 判定 | 対応 |
|---|---|---|
| A09 | FALSE | 結論：「補題 4.5 は、削除される語 $RT^\circ$ について、ある $RT\in L$（$T\ne T^\circ$）がすべての $y$ で $yT\in L\Rightarrow yT^\circ\in L$ を満たすときに捕獲の条件を与える」に |
| A07 | FALSE | 序論：双対学習器のデータの長さに「at least」 |
| A01 | GAP | 命題 3.5 の証明：「$d\in D_j$ なる段階 $j>i$ をとる。$D_j\not\subseteq L(G)=L(G_{j-1})$ なので $j$ はリセット」 |
| A02 | GAP | 表 1：学習器の行に「at convergence」、双対学習器の行に「$r\ge2$; untyped or $s_U$」 |
| A08 | GAP | 序論の一般形の文を、補題 4.5 の仮定どおり「$w=RT^\circ$、$RT\in L$、$yT\in L\Rightarrow yT^\circ\in L$ なら $\rho|N|\max(\kappa,1)\ge|R|$」と書き直した |
| A03 | minor | 序論で $L_n$ の提示の大きさを、非終端記号 $O(n)$ 個、右辺の長さ 4 以下、証人の長さ $O(n)$ と尺度ごとに。「What is known」の「linear size」も同様に |
| A04 | minor | 注意 6.6：命題 4.2(b) は「無用な非終端記号を除けば」命題 6.5 の場合 |
| A05 | typo | 命題 3.5 の証明の参照を KY2017 Theorems 3 and 4 に |
| A06 | minor | 命題 6.3 の後：「kernel failures are observer-invariant」を「persist under every observer」に |
| A10 | minor | 結論：範疇文法は弱生成力では文脈自由だがカテゴリーを型で名指すので扱わない、と別の文に |

定理・証明の内容の変更はない。英語版 23 頁（最終頁は参考文献 4 行）、日本語版 25 頁。英日でラベルが一致し、未定義の参照はない。

## 残ること

- 今日 Claude が編集で持ち込んだ誤りが 3 件見つかった。投稿版を確定する前に、今回の修正箇所（上の 10 件）だけをもう一度独立に読ませるとよい。
- 人間による監査、#1 の arXiv 番号の照合（`PAPER.yaml` の pending）。

# ChatGPT による最終修正（2026-11-28 夜）の査読への対応

査読：[`external_review_2026-11-28_chatgpt_final/`](external_review_2026-11-28_chatgpt_final/)（依頼文 `PROMPT.md`、`review.md`、`findings.csv`、`checks/`）。対象は `5cdba4f..0f10a5e` の英語版の差分（C01〜C15 への修正と書き直した Abstract）。

## 査読の概要

- **総合判定：局所的な修正で投稿してよい。** 主要定理への新しい反例・数値の矛盾はなし。
- 前回の指摘：C02・C04〜C09・C11〜C15 は closed、C01・C03・C10・C16 は partly（F03・F06・F08 で補う。C16 は様式の変換時に統一）。
- 新しい指摘 F01〜F12 は FALSE・OVERCLAIM なし。GAP 1（F04、Abstract の「Hence」が双対学習器の独立の論証まで含めてしまう）、UNCLEAR 7、STYLE 4。
- Abstract の「abstract licensing condition」は過大ではない（本文の但し書きと整合）と判定された。
- ChatGPT は Abstract の全面的な差し替え案も示したが、正確さと引き換えに読みにくくなっているので採らず、Claude の構成を保ったまま指摘だけを取り込んだ。

## 対応（英日とも）

| ID | 対応 |
|---|---|
| F01 | Abstract：KY2017 は「very weak」な性質が所属質問つきの学習器の成功を特徴づけることを示した、と明記（序論 l.123–126 と一致） |
| F02 | Abstract：「structures over one leaf symbol …, with $n$ constructors on every branch」（削除する語の一意性に効く条件を明示） |
| F03 | Abstract：「maximal lengths」と「a bound attained up to a factor $O(n)$」（下界はすべての提示に、達成は存在の主張）。$\max(\kappa,1)$ は本文に任せた（$M_n$ では健全性から $\kappa\ge1$） |
| F04 | Abstract：「Hence specific learners need …」を独立の文「Specific learners also need data of exponential total length」に（双対学習器の下界は積からではない） |
| F05 | Abstract：見本の全長の下界は「typed or untyped」、観測器の条件は「separating the marked leaf from the combination of two leaves」。「two-valued」は語数のため省いた |
| F06 | 序論 l.154：$\ell$ は主学習器のデータの下界に入らないので、「(with $\kappa$ these bound the data of the primal learners …)」に |
| F07 | §5：段階 $i$ での安定、$J$ の文脈の商の代表、$N_j=N_i$ から $e$ が $G_i$ の非終端記号であること、生成規則が $E_i$ の検査で落ちるので $w^*_{n-1}\in E_i$、を明示 |
| F08 | §5：$\Gamma$ が本稿の字母であることを明記（Kanazawa では演算の集合） |
| F09 | §5：「for the initial data $D=\{d\}$ with $d$ such a word」（語と集合の区別） |
| F10 | 注意 5.6：「rank at most 2」。空言語の場合は正の提示では無意味なので書き足さない |
| F11 | 結論：積を $\rho\lvert N\rvert\max(\kappa,1)$ と書き、見本の全長の下界は「typed under every observer or untyped」 |
| F12 | Abstract：246 語（空白区切り）、ハイフンで区切る数え方でも 249 語で、上限 250 に収まる |

英語版 24 頁、日本語版 26 頁。定理・証明の変更なし。

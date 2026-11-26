# 2 回目の外部査読（Astra、2026-11-25）への対応

査読：[`external_review_2026-11-25_astra/review_09_typed-fcp-fkp_astra_20261125.md`](external_review_2026-11-25_astra/review_09_typed-fcp-fkp_astra_20261125.md)（ChatGPT Business 上の Astra、記憶をリセットした別会話。対象はコミット 673064f）。
総合判定は Major revision 相当、主定理の撤回は不要。

## 重大な指摘（高）

| 指摘 | 判断 | 対応 |
|---|---|---|
| 3.1 比較表の「核側（どの型付けでも）$L_n$ は $O(n)$」は誤り。$s_U$ では初期記号の核が $\{w^*_n\}$ に限られ、$\kappa\ge3\cdot2^n-2$ | **正しい**（Claude が証明を確認） | 新しい命題 4.7（`prop:Ln-sU`）として証明を追加。比較表を「型なし／$s_0$」と「$s_U$」の行に分けた。Abstract・Theorem A の後の文・定理 4.5(iii)・考察に「観測なしなら」「型なしの」を明記 |
| 3.2 同じ $L^+$ で $s_0$ 型付き weak 2-FCP も構成でき、未解決問題 8.1 に否定解がある | **正しい**（Claude が証明を確認し、独立のコードで確認） | 命題 6.6(a) に $s_0$ 版を追加し、「$k\ge2$ で $\mathrm{FCP}^k_{\rm w}[s_0]\not\subseteq\mathrm{FCP}^k_{\rm w}[h]$」を結論に加えた。題を「the weak FCP is not monotone」に変更。未解決問題 8.1 は $k=1$ の場合に縮めた。Theorem B・Abstract・考察・結論の文言を合わせた |
| 3.3 KY2017 Lemma 12 で証明なしに述べられた「旧非終端記号は同じ文脈で特徴づけられたまま」の検算 | 正しい | $S_2,S_3$ の閉包を本文で直接示した（上の主張を使う）。強く特徴づけられる非終端記号は、文脈の形から $L$ または $L'$ 相対の等式がそのまま移ることを示した。KY2017 から使うのは証明に書かれた等式と Lemma 13 の証明だけになった |

## 中・低の指摘

| 指摘 | 対応 |
|---|---|
| Clark–Eyraud との同一視（$s_0$ 版は空語を除いた変種） | 文言を「nonempty fragments の変種、#1 で使うもの」に修正 |
| `check_deletion_family.py` の型の判定（閉じ括弧だけの因子） | 修正して再実行。(U) の比較数は 15→20、1732→1967、全通過 |
| Abstract・結論の weak FCP の文言、strong FKP | Abstract は「trivial typing から 2 元の指示型付けへの細分化でも失敗し得る」に。Theorem B と結論に strong FCP の包含と「strong FKP は対象外」を明記 |
| 認可条件・「negative test」の表現 | 序論と考察を書き直し、「negative test」を削除 |
| 学習器のパラメータ | 序論の箇条書きに「$r,k$ 固定」「$r\ge2,k\ge1$」を明記。KY2017 の Algorithms 1, 2 そのものについての主張であること、Clark の元の判定法の修正は Leiß (2014) を、§5 冒頭に記した |
| 補題 5.1 の空言語、標本ノルムの未定義 | 「nonempty」と $\|K\|$ の定義を補題に入れた |
| 定理 4.5(ii) の有限核 | 明記 |
| 文脈長・$\kappa$ の定義 | 序論で定義 |
| $k$ を省いたクラスの意味 | 定義の直後に明記 |
| 注意 5.8 の共通文脈の説明（$\ell+i,\ell+j\in[\ell,2\ell]$） | 追記 |
| 命題 6.4 の手法の出典 | KY2017 Prop 2(ii) の相殺の論法であると明記 |
| 未解決問題 8.2 の「証人が壊れる」 | 「Lemma 13 の証明が使えない。型付き weak FCP を持つかは不明」に限定。語の形も原文どおり $c^id^ie^i$ に |
| Clark–Yoshinaka (2016) の節番号 MISMATCH | Sec. 6.5.3 に修正 |
| 書誌 | KY2017 に LNCS 10168, pp. 77–88 と DOI、KY2023 に pp. 8–22、Clark–Yoshinaka に DOI。Coste–Nicolas (2019)、Leiß (2014) を追加（Web で書誌を確認） |
| 関連研究（Clark–Eyraud Example 2、Coste–Nicolas） | 序論の「What is known and what is new」に追加（Example 2 の内容は JMLR 版 p. 1729 で確認）。$L_n$・文法・$u_i$ が #1 §6 のものであることも明記 |
| Data availability | 「No data were used」を、スクリプトの所在を示す文に変更 |
| 生成AIの申告 | ChatGPT による査読を 2 回とし、命題 6.6 の型付き版と命題 4.7 につながったことを明記 |

## 反映していない指摘

- 命題 3.5 の reset の場合分け、系 5.7 の空言語の提示規約、§1 の「概念を外延と同一視する」約束、$D_i,E_i,J_i,H_i$ の初出定義：いずれも低。証明の正しさに影響しないため今回は見送り。
- `check_deletion_family.py` の (E) の長さの打ち切り：査読の指摘どおり、(U) の分布一致と到達文脈を別に示せば懸念は消える。本文の証明（補題 5.1）はこの打ち切りに依存しない。
- Funding の記載：事実の確認が必要なため著者に確認する。→ 2026-11-26、著者の確認により「No funding was received for conducting this study.」を英日に追加。
- Data availability の URL：投稿時にコミットを固定したリンクに差し替える。

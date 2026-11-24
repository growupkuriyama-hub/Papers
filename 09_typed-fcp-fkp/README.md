# 09_typed-fcp-fkp — 有限観測と有限文脈・有限核性質

*Finite Observation Helps Contexts but Not Kernels in Distributional Learning of Context-Free Languages*（仮題）

- 英語正本：[`main.tex`](main.tex)（[PDF](main.pdf)、研究草稿 revision 2、15 頁、2026-11-24）
- 研究報告（日本語、依頼の成果物 1–6）：[`research/REPORT_2026-11-24.md`](research/REPORT_2026-11-24.md)
- 研究台帳（状態の分類・否定された案）：[`research/LEDGER.md`](research/LEDGER.md)
- 外部査読（ChatGPT、2026-11-24、major revision・反例なし）と対応：[`research/REVIEW_RESPONSE_2026-11-24.md`](research/REVIEW_RESPONSE_2026-11-24.md)、原本は [`research/external_review_2026-11-24/`](research/external_review_2026-11-24/)
- 有限計算：`python3 -I tools/check_deletion_family.py 4`、`python3 -I tools/check_reduction_identity.py 4000`

## 何の論文か

金澤・吉仲（LATA 2017）の strong／weak／very weak の有限文脈性（FCP）・有限核性（FKP）に、#1 の固定有限半群型付け $s:\Sigma^+\to\mathsf S$ を組み合わせる。学習モデルは**正例＋所属質問**（#1 の正例のみとは別）。

- **Theorem A（双対性）**：型付けを細かくすると、文脈で定まるクラスは広がり、核で定まるクラスは狭まる。型付きの核は、型で均質な通常の核にすぎない（核の縮約補題）。どちらも 2 元半束 $U_1$ で、どの $k\ge1$ でも厳密。型付き VW-FKP = W-FKP。型なし weak FCP は観測を足すと保存されない（KY2017 Lemmas 8, 12 を前提）。
- **Theorem B（一語削除の代償、主結果）**：$M_n=L_n\setminus\{w^*_n\}$ は、VW-FKP を持つどの文法でも（どの型付けでも）$\rho\,|N|\max(\kappa,1)\ge3\cdot2^{n-1}-1$。$U_1$ 型付きの文脈表示は $O(n)$。primal 学習器は収束までに $2^{\Omega(n)}$ のデータ、dual 学習器も長さ $3\cdot2^{n-1}-2$ 以上のデータを要する。
- **系（既知の帰結）**：どの $s$ でも $\mathcal C^{\rm cf}_s$ は型なし weak 1-FKP（階数 2）で、型なし primal 学習器一つが $\bigcup_s\mathcal C^{\rm cf}_s$ を同定する。#1 Prop 9.7 から直ちに従う。

## 既知との境界

- 型付き学習器と型付き very weak 性質の対応は Yoshinaka (2015) の sorted 枠組みの特殊例（新規性なし）。
- 型付き文脈集合は Kanazawa–Yoshinaka (2023) の拡張正則閉包に入る。新しさは観測器どうしの比較と核（primal）の側。

## 状態

証明はすべて Claude（2026-11-24）。外部査読（ChatGPT）で反例なし・major revision、指摘は rev2 で反映済み。人間による監査は未。未解決：型付き weak FCP の単調性、任意の型付けでの VW/W-FCP の分離、$M_n$ の型なし文脈下界。

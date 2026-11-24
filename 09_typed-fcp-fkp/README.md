# 09_typed-fcp-fkp — 有限観測と有限文脈・有限核性質

*Frames versus Exemplars: An Exponential Gap for Syntactic Categories under Finite Observation*（仮題）

- 英語正本：[`main.tex`](main.tex)（[PDF](main.pdf)、研究草稿 revision 3（JoLLI 向けに再構成）、18 頁、2026-11-25）
- 研究報告（日本語、現行）：[`research/REPORT_2026-11-25.md`](research/REPORT_2026-11-25.md)。12 頁初稿時点の報告 [`research/REPORT_2026-11-24.md`](research/REPORT_2026-11-24.md) は履歴として残す
- 研究台帳（状態の分類・否定された案）：[`research/LEDGER.md`](research/LEDGER.md)
- 外部査読（ChatGPT、2026-11-24、major revision・反例なし）と対応：[`research/REVIEW_RESPONSE_2026-11-24.md`](research/REVIEW_RESPONSE_2026-11-24.md)、原本は [`research/external_review_2026-11-24/`](research/external_review_2026-11-24/)
- 有限計算：`python3 -I tools/check_deletion_family.py 4`、`python3 -I tools/check_reduction_identity.py 4000`、`python3 -I tools/check_toy_example.py`

## 何の論文か

#1 の固定有限半群型付け $s:\Sigma^+\to\mathsf S$（有限観測）のもとで、二つの量を調べる。

- **表現の複雑さ**：文脈自由言語を、金澤・吉仲（LATA 2017）の健全な前不動点（SPP）で、有限個の核（語）や文脈によって表すときの大きさ（非終端記号の数、右辺の長さ、核や文脈の長さ）。
- **データの複雑さ**：#1 と同じ正例のみの再構成 $\mathsf{Rec}_s$ の特性データの大きさ。

金澤・吉仲の所属質問付きの dual／primal 学習器への帰結は、応用として扱う。

- **Theorem A（核と文脈の指数的な隔たり、主結果）**：構造を二項の結合 $\lfloor xy\rfloor$ と一項の標識 $\lceil x\rceil$ で $n$ 段に組み、「少なくとも一つの標識を含む」という大域的な認可条件を課した言語 $M_n$（＝ $L_n$ から標識のない一語 $w^*_n$ を除いたもの）を考える。標識の有無を見る 2 元の観測のもとでは、文脈による表示は $2n$ 個のカテゴリーと長さ $2n$ 以下の文脈で済む。一方、核（例）による表示は、どの観測のもとでも $\rho\,|N|\max(\kappa,1)\ge3\cdot2^{n-1}-1$。認可条件がなければ（$L_n$）どちらも $O(n)$。
- **応用（§5）**：この下界は文法についての主張で、学習モデルによらない。帰結として、#1 の正例のみの再構成 $\mathsf{Rec}_s$ は $M_n$ に $\|K\|^3\ge3\cdot2^{n-1}-1$ の特性データを要する（#1 に無い下界）。所属質問付きの primal 学習器は収束までに $2^{\Omega(n)}$、dual 学習器も長さ $3\cdot2^{n-1}-2$ 以上のデータを要する。
- **Theorem B（観測の細分化、§6）**：型付けを細かくすると、strong と very weak の FCP で定まるクラスは広がり、very weak（＝weak）FKP で定まるクラスは狭まる（型付きの核は型で均質な通常の核にすぎない）。weak FCP はこの型に従わない。どちらも 2 元半束 $U_1$ で、どの $k\ge1$ でも厳密。型付き VW-FKP = W-FKP。型なし weak FCP は観測を足すと保存されない（KY2017 Lemmas 8, 12, 13 を引用、原文と照合済み）。
- **系（既知の帰結、§5.3）**：どの $s$ でも $\mathcal C^{\rm cf}_s$ は型なし weak 1-FKP（階数 2）で、型なし primal 学習器一つが $\bigcup_s\mathcal C^{\rm cf}_s$ を同定する。#1 Prop 9.7 から直ちに従う。

序論は数理言語学寄りで、FCP/FKP を「カテゴリーを有限個の文脈で名指すか、有限個の例で名指すか」として、数の一致を持つ小さな英語断片（例 1.1、`tools/check_toy_example.py` で確認）で説明している。言語学的な例は数学的な概念の説明であり、自然言語についての実証的な主張はしない。

## 既知との境界

- 型付き学習器と型付き very weak 性質の対応は Yoshinaka (2015) の sorted 枠組みの特殊例（新規性なし）。
- 型付き文脈集合は Kanazawa–Yoshinaka (2023) の拡張正則閉包に入る。新しさは観測器どうしの比較と核（primal）の側。

## 状態

証明はすべて Claude（2026-11-24）。外部査読（ChatGPT）で反例なし・major revision、指摘は rev2 で反映済み。人間による監査は未。未解決：型付き weak FCP の単調性、任意の型付けでの VW/W-FCP の分離、$M_n$ の型なし文脈下界。

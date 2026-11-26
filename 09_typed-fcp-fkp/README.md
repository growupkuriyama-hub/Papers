# 09_typed-fcp-fkp — 有限観測と有限文脈・有限核性質

*Frames versus Exemplars: An Exponential Gap for Syntactic Categories*（仮題）

- 英語正本：[`main.tex`](main.tex)（[PDF](main.pdf)、研究草稿 revision 4（JoLLI 向け、3 回目の査読を反映）、23 頁、2026-11-26）
- 日本語版（査読用の全訳、英語版と同じ版、28 頁）：[`japanese/main_JP.tex`](japanese/main_JP.tex)（[PDF](japanese/main_JP.pdf)）。定理番号・ラベル・数式は英語版と一対一
- 研究報告（日本語、現行）：[`research/REPORT_2026-11-25.md`](research/REPORT_2026-11-25.md)。12 頁初稿時点の報告 [`research/REPORT_2026-11-24.md`](research/REPORT_2026-11-24.md) は履歴として残す
- 研究台帳（状態の分類・否定された案）：[`research/LEDGER.md`](research/LEDGER.md)
- 外部査読（ChatGPT、2026-11-24、major revision・反例なし）と対応：[`research/REVIEW_RESPONSE_2026-11-24.md`](research/REVIEW_RESPONSE_2026-11-24.md)、原本は [`research/external_review_2026-11-24/`](research/external_review_2026-11-24/)
- 2 回目の外部査読（ChatGPT／Astra、2026-11-25、major revision 相当・主定理の撤回なし）と対応：[`research/REVIEW_RESPONSE_2026-11-25.md`](research/REVIEW_RESPONSE_2026-11-25.md)、原本は [`research/external_review_2026-11-25_astra/`](research/external_review_2026-11-25_astra/)
- 3 回目の査読（Claude、#1 の Reviewer 1・2 の観点、2026-11-26、major revision・反例なし）と対応：[`research/REVIEW_RESPONSE_2026-11-26.md`](research/REVIEW_RESPONSE_2026-11-26.md)、原本は [`research/external_review_2026-11-26_tcs1_lens/`](research/external_review_2026-11-26_tcs1_lens/)
- 有限計算：`python3 -I tools/check_deletion_family.py 4`、`python3 -I tools/check_reduction_identity.py 4000`、`python3 -I tools/check_toy_example.py`、`python3 -I tools/check_exemplar_upper.py 4`、`python3 -I tools/check_rec_samples.py`、`python3 -I tools/check_untyped_frames.py 5`、`python3 -I tools/check_parity_typing.py 4`、`python3 -I tools/check_general_capture.py 4`、`python3 -I tools/check_ideal_restriction.py`、`python3 -I tools/check_frame_total_length.py 7`

**2026-11-26 追記：** Python のジェネレータ関数の例を序論「答え：指数的な隔たり」の冒頭に移して定理 A の動機づけにし、考察では文字どおりの移植についての留保だけを残した。中国語の疑問詞原位置の類例は削除。定理・証明に変更なし。

**2026-11-26 追記（2）：** 序論に段落「Positive data and membership queries」を追加した。#1 の学習モデルが正例のみであること、所属質問は文法性判断の要求にあたり、子どもの言語獲得では明示的な否定証拠が乏しいとされること（Marcus 1993、動機づけのみで獲得についての主張はしない）、観測器は正例だけの設定で働き、所属質問があれば $\mathcal C^{\rm cf}_s$ について不要になること（Gold 1967、注意 5.7）を一か所にまとめた。「固定型付けの理論との関係」の重複する一文は削除。参考文献に Gold (1967)、Marcus (1993) を追加。英語版 23 頁、日本語版 25 頁。定理・証明に変更なし。

**2026-11-26 追記（3）：** §2.1 のクラスの記法を定義と同じ順（強・弱・極弱）に並べ直し、$\mathrm{FCP}^k_{\rm st}\subseteq\mathrm{FCP}^k_{\rm w}\subseteq\mathrm{FCP}^k_{\rm vw}$（FKP も同様、核では後ろが等号、文脈では $k\ge2$ で真）とその理由を一文で添えた。英日とも。

**2026-11-26 追記（4）：** 2 回目の独立査読（Claude、#1 の Reviewer 1・2 の観点、第 2 版）を反映。注意 5.3 の問い（特性標本は因子 $w^*_{n-1}$ を含むか）は $n=3$ で否（11 語の反例、`tools/check_rec_samples.py`）と書き換え、問いを「長さ $2^{\Omega(n)}$ の語が要るか」に。定理 4.4 の後に、自明な列挙の提示も積は $O(n)$ 倍以内であること（尺度は規則数を数えない）と、下界の内容（$\rho|N|$ が多項式なら $\kappa$ は指数的）を追加。注意 5.7 を補題 5.1 と #1 の特性標本から導く形に。小節を番号なしに（補題・系・命題の番号との衝突解消）。付録の集合 $B$ を $\mathcal B$ に。系 6.2 の量化を明確化。Clark (FG 2009) を引用。英語版 23 頁、日本語版 26 頁。

**2026-11-27 追記：** 謝辞（金澤誠氏・吉仲亮氏）を英日とも削除した（著者の判断）。

**2026-11-27 追記（2）：構成の変更。** 題を「Frames versus Exemplars: An Exponential Gap for Syntactic Categories」に変更。定理 A を観測器なしの形に：型なしの枠の文法 $F_n$（新しい命題 4.3、非終端記号 $n+1$、$\rho=3n$、文脈長 $\le2n$、強 1-FCP、規則 $2^n+2n-2$）と見本の下界（どの観測器でも）と $H_n$ の見本の上界。観測器の結果は新しい定理 C（定理 6.6：標識の観測器は枠の文法の規則数を $6n-4$ に減らし、見本は助けない）と定理 B にまとめ、第 6 節の題を「The role of the observer」に。未解決問題 8.3 を「型なしの枠は指数個の規則を要するか」に書き換え。序論・Abstract・考察・結論を対応して改稿。検証：`python3 -I tools/check_untyped_frames.py 5`。英語版 24 頁、日本語版 27 頁。

**2026-11-27 追記（3）：全長の比較。** 定義 3.4 に提示の全長（生成規則と証人の長さの総和）を追加。定理 6.6(d)（序論の定理 C(iii)）：$s_U$ のもとで枠の提示の全長は $O(n^2)$、$M_n$ のどの見本の提示も（どの型付けでも型なしでも）全長 $(3\cdot2^{n-1}-1)^{1/3}$ 以上。観測器なしでは $F_n$ の全長 $\Theta(n2^n)$ と $H_n$ の見本の提示の $\Theta(2^n)$ は同程度であり、定理 A はパラメータの隔たり、定理 C(iii) は全長の隔たりと明記。未解決問題 8.3 を「型なしの枠の提示は全長 $2^{\Omega(n)}$ を要するか」に。`tools/check_untyped_frames.py` に全長の計算を追加。

**2026-11-27 追記（4）：** ChatGPT の独立査読（`research/external_review_2026-11-27_chatgpt/`、Major、主定理は正しい）に対応。表の注記の偽の一般化を修正し、長さの偶奇の例を注意 4.7 に追加。定理 6.6(d) の全長の下界を $2\sqrt{3\cdot2^{n-1}-1}$ に強化。全長での比較の過剰な推論、未解決問題 8.3 の解釈、「各パラメータが別々に指数的か」の誤記を修正。検証コードの型判定・全長の集計・終了コードを修正し、`tools/check_parity_typing.py` を追加。対応の記録は `research/REVIEW_RESPONSE_2026-11-27.md`。英語版 25 頁、日本語版 28 頁。

**2026-11-27 追記（5）：短縮。** 序論を約 5 頁から 3 頁に（三つの主定理の文はそのまま、周りの説明の重複を整理し、「固定型付けの理論との関係」を「既知のことと新しいこと」に統合）。§2・§3 の既知の補題の証明と例、使わない逆向きの段落、注意 3.6 を圧縮。§5 の導入と注意、考察、未解決問題の説明、結論、AI 利用の申告を圧縮。定理・証明の内容は変更なし。英語版 22 頁、日本語版 25 頁。

**2026-11-27 追記（6）：一般形。** 捕獲補題を一般形に（補題 4.4、条件 (4.1)）し、一語削除の補題 4.5、一般の核の下界（定理 4.6）を追加。$M_n$ では入れ替える接尾辞を最後の $E_1$-節点に選び直し、下界を $3\cdot2^n-n-5$ に改良（定理 4.7、旧 $3\cdot2^{n-1}-1$）、全長の下界も $2\sqrt{3\cdot2^n-n-5}$。§6 にイデアルによる制限（命題 6.6）とその二つの例（注意 6.7：$H_n$、標識が二つ以上）、一般の隔たり（定理 6.9）を追加。探索の記録は Project の `claude/claude_typed_fcp_fkp_explore_AB_2026-11-27.md`。検証：`check_general_capture.py 4`、`check_ideal_restriction.py`。英語版 24 頁、日本語版 27 頁。

**2026-11-27 追記（7）：観測器なしの枠の全長（旧未解決問題 8.3 の解決）。** 観測器なし、または $\lceil a\rceil$ と $\lfloor aa\rfloor$ に同じ型を与える観測器のもとでは、$M_n$ のどの枠の提示も $(\ell+1)\sum|\alpha|\ge2^{n-2}$ を満たし、全長 $2^{n/2}$ 以上（定理 6.12）。一般の $j$ では $(3\cdot2^{j-1}-1)(\ell+1)\sum|\alpha|\ge2^{n-j}$（長さの偶奇の観測器でも $2^{n/2}/\sqrt5$ 以上）。旧命題 8.4 を型付きに拡張して補題 6.10 に移し、混合の補題 6.11 を追加。定理 C に (iv)、定理 6.8 に (e) を追加し、全長での比較は「観測器がなければ枠も見本も指数、標識の観測器で枠だけ $O(n^2)$」に。未解決問題 8.3 は指数の値と一般形を問うものに置き換え。探索の記録は Project の `claude/claude_typed_fcp_fkp_explore_C_2026-11-27.md`。検証：`check_frame_total_length.py 7`。英語版 25 頁、日本語版 28 頁。

**2026-11-27 追記（8）：AI 利用の申告を最小限に。** TCS #1（TCS-D-26-00494 R1）と同じ文面（言語の編集・原稿の構成・数学的議論の検討の補助として ChatGPT と Claude を使用、著者が検討・編集し結果と証明に全責任を負う）に置き換え。詳細は査読で問われたときに答える方針。

## 何の論文か

#1 の固定有限半群型付け $s:\Sigma^+\to\mathsf S$（有限観測）のもとで、二つの量を調べる。

- **表現の複雑さ**：文脈自由言語を、金澤・吉仲（LATA 2017）の健全な前不動点（SPP）で、有限個の核（語）や文脈によって表すときの大きさ（非終端記号の数、右辺の長さ、核や文脈の長さ）。
- **データの複雑さ**：#1 と同じ正例のみの再構成 $\mathsf{Rec}_s$ の特性データの大きさ。

金澤・吉仲の所属質問付きの dual／primal 学習器への帰結は、応用として扱う。

- **Theorem A（核と文脈の指数的な隔たり、主結果）**：構造を二項の結合 $\lfloor xy\rfloor$ と一項の標識 $\lceil x\rceil$ で $n$ 段に組み、「少なくとも一つの標識を含む」という大域的な認可条件を課した言語 $M_n$（＝ $L_n$ から標識のない一語 $w^*_n$ を除いたもの）を考える。標識の有無を見る 2 元の観測のもとでは、文脈による表示は $2n$ 個のカテゴリーと長さ $2n$ 以下の文脈で済む。同じ文法は長さ $\max(3\cdot2^{n-1}-2,2n+1)$ 以下の核（例）でも表示できる（命題 4.2(c)、2026-11-26 追加）。一方、核による表示は、どの観測のもとでも $\rho\,|N|\max(\kappa,1)\ge3\cdot2^{n-1}-1$ で、上界と $O(n)$ 倍の範囲で一致する。隔たりは証人の長さにある。認可条件がなければ（$L_n$）どちらも $O(n)$。
- **応用（§5）**：この下界は文法についての主張で、学習モデルによらない。帰結として、#1 の正例のみの再構成 $\mathsf{Rec}_s$ は $M_n$ に $\|K\|^3\ge3\cdot2^{n-1}-1$ の特性データを要する（#1 に無い下界）。所属質問付きの primal 学習器は収束までに $2^{\Omega(n)}$、dual 学習器も長さ $3\cdot2^{n-1}-2$ 以上のデータを要する。
- **Theorem B（観測の細分化、§6）**：型付けを細かくすると、strong と very weak の FCP で定まるクラスは広がり、very weak（＝weak）FKP で定まるクラスは狭まる（型付きの核は型で均質な通常の核にすぎない）。weak FCP はこの型に従わず、細分化で単調でない（$s_0$ から 2 元の指示型付けへ）。どちらも 2 元半束 $U_1$ で、どの $k\ge1$ でも厳密。型付き VW-FKP = W-FKP。型なし weak FCP は観測を足すと保存されない（KY2017 Lemmas 8, 12, 13 を引用、原文と照合済み）。
- **系（既知の帰結、§5.3）**：どの $s$ でも $\mathcal C^{\rm cf}_s$ は型なし weak 1-FKP（階数 2）で、型なし primal 学習器一つが $\bigcup_s\mathcal C^{\rm cf}_s$ を同定する。#1 Prop 9.7 から直ちに従う。

序論は数理言語学寄りで、FCP/FKP を「カテゴリーを有限個の文脈で名指すか、有限個の例で名指すか」として、数の一致を持つ小さな英語断片（例 1.1、`tools/check_toy_example.py` で確認）で説明している。言語学的な例は数学的な概念の説明であり、自然言語についての実証的な主張はしない。

## 既知との境界

- 型付き学習器と型付き very weak 性質の対応は Yoshinaka (2015) の sorted 枠組みの特殊例（新規性なし）。
- 型付き文脈集合は Kanazawa–Yoshinaka (2023) の拡張正則閉包に入る。新しさは観測器どうしの比較と核（primal）の側。

## 状態

証明はすべて Claude（2026-11-24）。外部査読（ChatGPT、2 回）で主定理への反例なし。2 回目の査読で、$s_U$ のもとでの $L_n$ の核の下界（命題 4.7）と、weak FCP の非単調性（命題 6.5）が加わった。人間による監査は未。未解決：weak 1-FCP の単調性、任意の型付けでの VW/W-FCP の分離、$M_n$ の型なし文脈下界。

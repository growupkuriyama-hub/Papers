# 09_typed-fcp-fkp — 有限観測と有限文脈・有限核性質

*Frames versus Exemplars: An Exponential Gap for Syntactic Categories*（仮題）

- 英語正本：[`main.tex`](main.tex)（[PDF](main.pdf)、JoLLI 向け、2026-11-28 の差分の ChatGPT 査読の修正まで反映、24 頁、2026-11-28）
- 日本語版（査読用の全訳、英語版と同じ版、26 頁）：[`japanese/main_JP.tex`](japanese/main_JP.tex)（[PDF](japanese/main_JP.pdf)）。定理番号・ラベル・数式は英語版と一対一
- 研究報告（日本語、現行）：[`research/REPORT_2026-11-25.md`](research/REPORT_2026-11-25.md)。12 頁初稿時点の報告 [`research/REPORT_2026-11-24.md`](research/REPORT_2026-11-24.md) は履歴として残す
- 研究台帳（状態の分類・否定された案）：[`research/LEDGER.md`](research/LEDGER.md)
- 外部査読（ChatGPT、2026-11-24、major revision・反例なし）と対応：[`research/REVIEW_RESPONSE_2026-11-24.md`](research/REVIEW_RESPONSE_2026-11-24.md)、原本は [`research/external_review_2026-11-24/`](research/external_review_2026-11-24/)
- 2 回目の外部査読（ChatGPT／Astra、2026-11-25、major revision 相当・主定理の撤回なし）と対応：[`research/REVIEW_RESPONSE_2026-11-25.md`](research/REVIEW_RESPONSE_2026-11-25.md)、原本は [`research/external_review_2026-11-25_astra/`](research/external_review_2026-11-25_astra/)
- 3 回目の査読（Claude、#1 の Reviewer 1・2 の観点、2026-11-26、major revision・反例なし）と対応：[`research/REVIEW_RESPONSE_2026-11-26.md`](research/REVIEW_RESPONSE_2026-11-26.md)、原本は [`research/external_review_2026-11-26_tcs1_lens/`](research/external_review_2026-11-26_tcs1_lens/)
- 2026-11-27 の査読：ChatGPT の独立査読 2 回（`research/external_review_2026-11-27_chatgpt/`、`research/external_review_2026-11-27_chatgpt_r2/`）と対応 [`research/REVIEW_RESPONSE_2026-11-27.md`](research/REVIEW_RESPONSE_2026-11-27.md)、[`research/REVIEW_RESPONSE_2026-11-27_r2.md`](research/REVIEW_RESPONSE_2026-11-27_r2.md)
- 凍結版（`2cd1ece`）の独立検証査読（ChatGPT、2026-11-27、**局所修正のみで投稿可**・反例なし）と対応：[`research/REVIEW_RESPONSE_2026-11-28_frozen.md`](research/REVIEW_RESPONSE_2026-11-28_frozen.md)、原本と依頼文は [`research/external_review_2026-11-28_chatgpt_frozen/`](research/external_review_2026-11-28_chatgpt_frozen/)
- Astra の重点査読（2026-11-28、`61f8a16`、Minor Revision・主定理への反例なし、#1 の番号照合は一致）と対応：[`research/REVIEW_RESPONSE_2026-11-28_astra_focus.md`](research/REVIEW_RESPONSE_2026-11-28_astra_focus.md)、原本と依頼文は [`research/external_review_2026-11-28_astra_focus/`](research/external_review_2026-11-28_astra_focus/)
- 有限計算：`python3 -I tools/check_deletion_family.py 4`、`python3 -I tools/check_reduction_identity.py 4000`、`python3 -I tools/check_toy_example.py`、`python3 -I tools/check_exemplar_upper.py 4`、`python3 -I tools/check_rec_samples.py`、`python3 -I tools/check_untyped_frames.py 5`、`python3 -I tools/check_parity_typing.py 4`、`python3 -I tools/check_general_capture.py 4`、`python3 -I tools/check_ideal_restriction.py`、`python3 -I tools/check_frame_total_length.py 7`、`python3 -I tools/check_flat_example.py 3`、`python3 -I tools/check_untyped_two_frames.py 4`

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

**2026-11-27 追記（8）：AI 利用の申告を最小限に。** TCS #1（TCS-D-26-00494 R1）と同じ文面（言語の編集・原稿の構成・数学的議論の検討の補助として ChatGPT と Claude を使用、著者が検討・編集し結果と証明に全責任を負う）に置き換え。詳細は査読で問われたときに答える方針。 Data availability も TCS #1 と同じ一文（No empirical data were used…）にし、本文の `tools/check_rec_samples.py` の名指しを「計算機で発見した」に。`tools/` は引き続きこのリポジトリにあり、求められたら示す。

**2026-11-27 追記（9）：ChatGPT の独立査読・第2回への対応。** 査読は `research/external_review_2026-11-27_chatgpt_r2/`（Editor Major / R1 Minor / R2 Major、総合 8.0）、対応は `research/REVIEW_RESPONSE_2026-11-27_r2.md`。命題 6.6 の誤り（イデアル外の旧初期記号のコピーが残る）を修正し、定理 4.6・6.9 の空の場合、注意 6.7、定理 6.12 の細部を補った。Abstract を 243 語に短縮し、一般性・単調性・最適性の主張を限定。木構造を持たない平らな族を例 6.13 として追加。検証：`check_flat_example.py 3`（新規）、`check_ideal_restriction.py`（回帰検査を追加）、`check_exemplar_upper.py`・`check_toy_example.py` を修正。英語版 26 頁、日本語版 28 頁。

**2026-11-27 追記（10）：24 頁に短縮、平らな族の文献調査。** 重複を削った（序論の「正例と所属質問」と「学習への応用」を統合、「構成」の段落を削除、定理 A・C の後の比較、§6 の比較の段落、§7 の考察、結論、注意 3.6・5.3・5.6・5.7・5.8・6.7、系 6.2 の後の一文、Python の例のコード片など）。証明は削っていない。付録の表を一段小さい字に。英語版 24 頁、日本語版 27 頁。平らな族とその大きさの比較は、見つかった文献にはなかった（部品の倍化文法は標準）：`research/LITERATURE_flat_family_2026-11-27.md`。

**2026-11-27 追記（11）：先行研究 4 本を本文で確認、引用を追加。** Kanazawa–Yoshinaka 2021、Yoshinaka 2011・2012、Baumann ほか 2022 を読んだ（記録は `research/LITERATURE_flat_family_2026-11-27.md`）。どれも枠と見本の提示の大きさを比べておらず、新規性は保たれる。「What is known」に比較は定性的であるという一文、定理 6.12 の後に KY2021 の負の文脈の成分への拡張、例 6.13 にタグが KY2021 の $\#d^i$ にならうことを追加し、ky2021・yoshinaka2012lata を引用。頁数を保つため参考文献の DOI の URL を外し、付録 A の表をフロート（表 1）にした。英語版 24 頁、日本語版 27 頁。

**2026-11-27 追記（12）：凍結版の独立検証査読への対応。** `2cd1ece` を凍結し、ChatGPT に新しい会話で今日追加した部分（命題 4.3〜定理 4.8、命題 6.6〜例 6.13、Abstract・結論）を、過去の査読を見ずに検証させた。判定は「局所修正のみで投稿可」。主定理 A・C と新しい補題・定理に反例も閉じていない証明の穴もなく、R2-01〜R2-18 は見送り分を除き修正済みと確認された。指摘 F01〜F05（文面または局所的な理由づけ）を英日とも修正した：定理 6.9 から直接出る部分の限定（F01）、尺度と観測器の条件の明記（F02、Abstract の「標識を見る観測器」を「$\lceil a\rceil$ と $\lfloor aa\rfloor$ を分ける観測器」に）、Limits の仮定を捕獲の条件 (4.1) に（F03）、結論で双対学習器の下界を別の論法と明記（F04）、注意 5.7 の「閉包は変わらない」を「文脈集合は変わらない」に（F05）。頁数を保つため、定理 6.8 の後の全長の比較の繰り返しを削った。定理・証明・数値の変更なし。英語版 24 頁、日本語版 27 頁。記録：`research/REVIEW_RESPONSE_2026-11-28_frozen.md`。

**2026-11-27 追記（13）：冗長な箇所の洗い出し。** `3a0a893` の英語版を通読し、重複（A1〜A10）、本筋から外れる部分（B1〜B10）、圧縮できる証明・既知の部分（C1〜C5）、構成の選択（D1〜D3）を一覧にした：`research/REDUNDANCY_AUDIT_2026-11-27.md`。原稿は未変更。§4 冒頭に F03 と同じずれが残っていることも見つけた（A10）。

**2026-11-27 追記（14）：重複の削除と圧縮（A1〜A10、C1〜C3）。** 洗い出しの A と C を英日とも反映した。定理 A の再掲だった定理 4.8 を削除し、定理 6.8 を全長の命題 6.8 に縮め、比較の文と注意 5.6 の表を序論の表 1 一つに集約、型付きの但し書きを補題 3.7 の後の一文に、§7 の重複した二段落を削除、学習器の説明と命題 3.5・6.3 の証明を圧縮。§4 冒頭の F03 の直し残しも修正。定理・証明の内容の変更なし。英語版 24 頁（最終頁は 4 行）、日本語版 26 頁。§4 以降の番号が一つずつずれた（例：注意 4.9 → 4.8）。記録：`research/REDUNDANCY_AUDIT_2026-11-27.md` の「反映の記録」。

**2026-11-27 追記（15）：本筋から外れる部分の削除（B1〜B9）。** Python の例（序論・$s_U$ の説明・§7、参考文献）、注意 3.6（EXREG）、注意 5.8 を削除し、注意 5.7 を 6 行に、注意 4.8 の偶奇の例と系 6.2 をそれぞれ一文に、定理 6.12 の後の KY2021 への拡張と注意 5.3 の計算機の発見を削除、未解決問題 8.4 を強 FKP の一問に絞った。B10（§2 の SPP の例）は残した。§7 は「Limits」に。定理・証明の変更なし。英語版 23 頁、日本語版 25 頁。§3・§5・§6 の番号がずれた。記録：`research/REDUNDANCY_AUDIT_2026-11-27.md` の「B の反映の記録」。

**2026-11-27 追記（16）：構成の選択（D）。** D3 だけ採り、「Limits」の節を結論の第二段落に移した（§7 未解決問題、§8 結論）。D1（命題 6.4 の証明を概略にして付録を削る）と D2（型付き学習器を落とす）は、新しい結果の検証可能性と、観測器と学習の話のつながりを失うので採らない。理由は `research/REDUNDANCY_AUDIT_2026-11-27.md` の「D の判断」。英語版 23 頁、日本語版 25 頁。

**2026-11-27 追記（17）：Astra の徹底査読への対応。** `bfee14b` を Astra が S1〜S8 の区切りで通読し、区切りごとに push した（`research/external_review_2026-11-27_astra_full/`）。判定は Minor Revision、総合 8/10（Editor・R1・R2 とも Minor）。主定理 A〜C に反例なし。指摘 10 件（FALSE 2：序論の「at least」の欠落と結論の一語削除の条件、GAP 3：命題 3.5 の証明、表 1 の学習器の仮定、序論の左文脈の向き、ほか minor・typo）を英日とも修正した。うち 3 件（A01・A05・A09）は同日の Claude の圧縮・修正が持ち込んだもの。定理・証明の内容の変更なし。英語版 23 頁、日本語版 25 頁。記録：`research/REVIEW_RESPONSE_2026-11-27_astra_full.md`。

**2026-11-27 追記（18）：言語学的な意義付け。** 「$M_n$ が人工的に見える」という弱点に対し、序論に二つの段落を加えた。(1) 枠と見本を、構造主義の試験枠（Fries 1952）と事例基盤・用例基盤モデル（Bod 2006、Bybee 2006）の二つの伝統に対応させた。(2) $M_n$ を「少なくとも一つ」の条件として位置づけた：音韻論の義務性（Hyman 2006）と厳格層仮説（Selkirk 1984、Nespor & Vogel 1986）、標準日本語の主格要件（Kishimoto 2010、多重主格は Kuno 1973）。葉の記号が一種類で深さが一様なら標識のない構造はちょうど一つなので、一語の削除は認可条件そのものである。結論に、類比は例示であること、頂点性と組にした「ちょうど一つ」は扱わないことを加えた。定理・証明の変更なし。英語版 23 頁、日本語版 25 頁。記録：`research/LINGUISTIC_MOTIVATION_2026-11-27.md`。

**2026-11-28 追記：Astra の重点査読への対応。** Claude が依頼文を書き、Astra が `61f8a16` の気になる箇所（前回の指摘への修正、言語学の段落と典拠、Abstract・序論・結論の主張、§6 後半の証明、新規性、#1 の番号照合、模擬査読）を S0〜S8 で確認した（`research/external_review_2026-11-28_astra_focus/`）。判定は Minor Revision、主定理への反例なし、#1 の番号は arXiv v5 と 13 か所すべて一致。指摘 12 件を英日とも反映した：定理 6.11 の因子 $\ell+1$ は除けないこと（型なしの $H_n$ に枠を二つずつ与えると $\sum|\alpha|=O(n)$）を定理の後に示して未解決問題 7.3 の副問を削除（B10、`tools/check_untyped_two_frames.py 4`）、序論の「Exemplars cannot」の誤り（B05）、イデアル制限と捕獲の説明の仮定（B01・B06）、Clark (ICGI 2016) の引用（B08）、ほか minor。B09 は著者稿を読んでから反映し、命題 5.5 の後に Kanazawa (WoLLIC 2023) との関係を一文で追加した（`research/LITERATURE_kanazawa2023_wollic_2026-11-28.md`）。定理・証明の変更なし。英語版 23 頁、日本語版 26 頁。記録：`research/REVIEW_RESPONSE_2026-11-28_astra_focus.md`。

**2026-11-28 追記（2）：Kanazawa (WoLLIC 2023) の Algorithm 3。** 著者稿の全文を読み、命題 5.5 の論法が Algorithm 3 にそのまま通ること（$M_n$ に収束するまでに $w^*_{n-1}$ を含むデータが必ず要る）、拡張正則の演算のもとでは $M_n$ が短い原子だけの小さな文法を持つことを確かめた（`research/KANAZAWA2023_ALG3_ON_Mn_2026-11-28.md`）。ChatGPT の独立検証（`research/external_review_2026-11-28_chatgpt_alg3/`）は「局所的な修正で正しい」：原子の正規化（K01）、長い例の場所（K04）、尺度（K05）を直して、命題 5.5 の直後の文を書き換えた（英日とも）。結論：Kanazawa の性質 (d†′) は追加の例の個数を抑えるが、その長さまで目標の文法の大きさの多項式で抑えることはできない。英語版 23 頁、日本語版 26 頁。

**2026-11-28 追記（3）：ブール演算の場合。** ChatGPT が検証の中で示した「成分が商のブール結合の SPP でも $2(\ell+1)\sum|\alpha|\ge2^{n-1}$」を Claude が確認した。定理 6.11 の証明で枠を使うのは補題 6.9 の一か所だけで、区別する文脈が区別する原子に置き換わるだけで通る（向きは補題 4.1 で一つに決まる）。拡張正則の演算では通らない。短い原子と小さな文法を両立させるのは正則演算で、Algorithm 3 のデータの長さの下界は演算の選び方によらない。記録は `research/KANAZAWA2023_ALG3_ON_Mn_2026-11-28.md`。定理 6.11 の後の「因子 $\ell+1$ は除けない」段落の末尾に一文として反映した（英日とも。23 頁を保つため参考文献を 4 件略記）。

**2026-11-28 追記（4）：尺度の整理。** 仕上げ前の洗い出し（`research/FINAL_AUDIT_2026-11-28.md`）の A4・B1・B3 を英日とも反映した。Abstract と序論で、定理 A は非終端記号の数・右辺と証人の長さの積の隔たり（$F_n$ の生成規則は指数個と明記）、尺度によらない全長での隔たりは標識の観測器のもとの定理 C、と書き分けた。Algorithm 3 の文に $k\ge8$ を追加。英語版 23 頁、日本語版 26 頁。

**2026-11-28 追記（5）：言語学の典拠の原著照合。** Fries (pp.74–75)、Selkirk (p.26)、Nespor & Vogel (p.7、第 2 版)、Kuno (第 3 章) は本文の主張どおり。Bod は「カテゴリーを事例で表す」とは言っていないので、「事例基盤のモデルは蓄えた事例で働き (Bod)、用例基盤のモデルはそこからカテゴリーが生じるとする (Bybee)」に直し、頁を明記した（英日とも）。記録：`research/LINGUISTIC_SOURCES_CHECK_2026-11-28.md`。英語版 23 頁、日本語版 26 頁。

**2026-11-28 追記（6）：今日の差分の独立な査読。** ChatGPT に `61f8a16..5cdba4f` の英語版の差分だけを読ませた（`research/external_review_2026-11-28_chatgpt_diff/`）。判定は「局所的な修正で投稿してよい」。指摘 16 件のうち、C04（定理 A は生成規則を数えないという文と定理 A(i) の矛盾）、C06（観測器の必要性の言い過ぎ）、C09（(d†′) についての結論の範囲）、C11（注意 5.6 の圧縮で落とした根拠）、C13（ICGI 2018 を 2019 と誤記）は今日の編集で入った誤り。C16 以外を英日とも反映した。記録：`research/REVIEW_RESPONSE_2026-11-28_chatgpt_diff.md`。英語版 24 頁、日本語版 26 頁、Abstract 246 語。

**2026-11-28 追記（7）：Abstract を JoLLI の読者向けに推敲。** 問い（一つの言語の二種類の提示の大きさ）を先に出し、$M_n$ を「抽象的な認可の条件」として一文で導入、二つの尺度（非終端記号の数・右辺と証人の長さ／全長）を「Measured by …」「In total length …」で書き分け、記号 $\lceil a\rceil$・$\lfloor aa\rfloor$ を「標識を持つ葉と標識のない葉の対」と言葉に置き換えた。主張の範囲は ChatGPT の C01・C02 の修正どおり（下界は $O(n)$ 倍で最良、一般化は適当な一語の削除）。248 語（数式を除くと 245）。英日とも。

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

証明はすべて Claude（2026-11-24〜27）。模擬査読は 9 回（ChatGPT 4 回、Astra 3 回、Claude 2 回）で、主定理への反例なし。最後の Astra の重点査読（2026-11-28、`61f8a16`）の判定は Minor Revision で、その修正は反映済み。#1 の arXiv 版の番号照合は済み。人間による監査は未。未解決：weak 1-FCP の単調性、任意の型付けでの VW/W-FCP の分離、観測器なしの枠の全長の指数（未解決問題 7.3）。

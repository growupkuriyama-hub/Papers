# ファンアウト2境界問題：局所鳩の巣法・反例・型付き修復の研究記録（2026-11-13）

> **研究アーカイブ / 未投稿 / 未査読**。現行論文の正式な主結果は \`../main.tex\` の Theorems A/B/C と \`op:fanout-two\` であり、本記録の新定理案を採択・証明済みとみなさない。新しい Claude Fable による追加探索を行うための出発点。本文・日本語原稿・PDFは変更していない。

## 1. 現行問題

固定 fan-out \(f\ge2\)、rank 上限 \(r_{\max}\ge2\) で、局所群 \(\mathbf{LG}\) は一様多項式特徴データ長の正確な擬多様体境界か。現行 \`op:fanout-two\` は **未解決**。

- YES：\(\mathbf{LG}\) が境界であり続ける（\(\mathbf{SL}\) は一様多項式データ長を持たない）。
- NO：境界が広がる（\(\mathbf{SL}\) が一様多項式データ長を持つ）。
- \`parked/plan1_boundary_extensions_2026-11-11.tex\` の \`prop:sl-reduction\` による \(\mathbf{SL}\) 帰着を参照。全アルファベットへの上界が必要。一つの \(U_1\) 型付けの上界では不十分。
- Main Theorem A（LG上界 \(O(\|G\|^2\bar\theta_G)\)、固定 fan-out 全体）と Theorem C（LG必要十分は fan-out 1, rank≥2）は区別。

## 2. 今回保存した一次資料

| ファイル | 起源・役割 | 信頼度 |
|---|---|---|
| [claude_fanout2_local_pigeonhole_2026-11-13.md](claude_fanout2_local_pigeonhole_2026-11-13.md) | Claude Fable 5.2 による \(\mathcal N_{\mathrm{st}}\) 上界の当初の報告、補題1〜3・定理1・候補D1 | 補題2(a)に反例あり。**元の証明は不成立** |
| [check_local_pigeonhole_2026-11-13.py](check_local_pigeonhole_2026-11-13.py) | Claude 添付。T1: 特定の有限箱で局所移動を検査。T2: 成分ごとの連結型の8例 | 有界検査のみ。無限言語の証明ではない |
| [independent_review_local_pigeonhole_2026-11-13.md](independent_review_local_pigeonhole_2026-11-13.md) | ChatGPT による旧補題2(a)への明示的な反例 | 手計算＋検査スクリプトあり |
| [check_free_node_counterexample_2026-11-13.py](check_free_node_counterexample_2026-11-13.py) | 反例の型・生成組・自由節点を再現 | 2026-11-13 ChatGPT で再実行成功 |
| [local_pigeonhole_repair_2026-11-13.md](local_pigeonhole_repair_2026-11-13.md) | 型付き状態の節点最小導出を用いた修復証明案 | **未査読の新しい証明案** |
| [PROMPT_FABLE_FANOUT2_ROUND2_2026-11-13.md](PROMPT_FABLE_FANOUT2_ROUND2_2026-11-13.md) | 新しい Fable セッション向け第二段プロンプト | 今回の証明修復監査と新規探索を指定 |

## 3. クラス \(\mathcal N_{\mathrm{st}}\) と主張

\(\mathrm{st}:\Sigma\to\{1,\ldots,t\}\)、\(\mathrm{ND}\) を段番号が非減少な語の集合、\(\Psi\) を Parikh 写像とする。**段付きParikhクラス**：

\[
\mathcal N_{\mathrm{st}}=\{L\mid L\cap\Sigma^+=\mathrm{ND}\cap\Sigma^+\cap\Psi^{-1}(Q),\quad Q\subseteq\mathbb N^\Sigma\}.
\]

\(Q\) は任意。ただし学習対象言語は別途 \(L\in\mathcal C^{\mathrm{mcf}}_{f,c_\Sigma}\) と仮定する。\(t=1\) は Parikh 飽和言語。以前の Fable クラス \(\mathcal K\) はこの部分クラス。

Claude当初の上界主張は \(\tau(G,c_\Sigma)=O_{k,f,r}(v^{k+2}\bar\theta_G^{k+1})\)。この**結論そのものへの反例は見つかっていない**が、当初の証明は誤り。

### 3.1 旧証明への反例（再現済み）

アルファベット \(\Sigma=\{p,x,b,y\}\)、arity \(A=B=2\) の reduced good MCFG：

\`\`\`text
A -> (x,y)
A -> (p, ξ1^1 b ξ1^2)(A)
B -> (p ξ1^1 p, xby ξ1^2 xby)(A)
S -> (a ξ1^1)(S)       (a∈Σ ごと)
S -> (a)                (a∈Σ ごと)
S -> (ξ1^1 b ξ1^2)(B)
\`\`\`

\(L(G)=\Sigma^+\)（1段の Parikh 飽和で全 arity 代入可能）。型 \((\{p\},\{x,b,y\})\) を持つ \(B\) の最小導出は \(B(1)=(ppp,xbyxbyxby)\)。その導出の道に、基底ラベル \(A\) が2回、かつ**双方自由節点**として現れる。祖先 \(A\) を子孫 \(A\) で短絡すると成分への文字配置が変わり、型が保存されない。

したがって「自由な道の基底非終端ラベルは相異なる」という旧補題2(a)は偽。元の骨格・接頭反鎖評価 \(O(v)\) はその論法からは従わない。**反例は上界定理自体の否定ではない。**

### 3.2 ChatGPT の修復証明案

各節点に**基底非終端と成分ごとの内容型** \((A,T_1,\ldots,T_d)\) を付け、\(X=A_{\mathbf T}\) の導出木を節点数で最小に取る。

型付きラベルが一本の道で重複すると、祖先の部分木を子孫の同型付き部分木に置き換えても根の型付き導出は適法であり、節点数最小性と矛盾する。したがって高さは

\[
H:=v(2^k-1)^f
\]

以下（固定 \(k,f\) では \(O(v)\)）。この正しい高さ評価から、原案の骨格節点数を \(2kfH\)、DFS 接頭反鎖サイズを \(rH\)、色数を \(C=(1+rH\Theta)^k\) と置き換える。原報告の局所移動補題と反鎖の貪欲削除を利用すると、修復ノートでは

\[
\tau(G,c_\Sigma)\le
2kfH\Theta\left(1+rH(1+rH\Theta)^k\right),
\qquad \Theta=\bar\theta_G
\]

が導かれると主張する。固定 \(k,f,r\) なら同じ多項式次数 \(O_{k,f,r}(v^{k+2}\Theta^{k+1})\)。

**重要な地位：これは証明案であり、独立査読済みの定理ではない。** 特に（a）局所移動補題で同一段の複数穴の許容性、（b）異なる自由部分木の削除順による予備文字の保全、（c）DFS切り口での挿入文字数評価と文脈、（d）型付き節点の置換の詳細、を独立に点検する必要がある。

## 4. 実施した検査・未実施の検査

2026-11-13にChatGPTが次を再実行：
- \`python check_free_node_counterexample_2026-11-13.py\`：すべてのassert成功。
- Claudeの\`check_local_pigeonhole_2026-11-13.py\`の\`t2()\`：8つの例でassert成功。

**今回はT1の全箱網羅検査を再実行していない**。T1の数値はClaudeの報告によるもの。T2ではある言語の判定関数が語を段順にソートするため、非ND語の排除に関する検証としては使えない。またT2は一般のgood MCFGの成分移動規則を網羅していない。

無限族の定理に有限の計算結果を代用してはいけない。

## 5. これまでの地図と次の焦点

- \`reviews/STATUS_sl_fanout2_2026-11-01.md\`：SLへの帰着、二文字上界、三文字で残った問題。
- \`parked/plan1_boundary_extensions_2026-11-11.tex\`：退避されたSL帰着・二文字定理等。
- \`reviews/astra_fanout2_map_2026-11-10.md\`：有限群認識や順序付き文字群での多項式代表長。
- \`reviews/fable_three_stages_2026-11-11.md\`：\(\mathcal K\) の \(t\le2f\) など。もし修復定理が成立すれば \(\mathcal K\) の段数制限が消える。
- \`reviews/claude_fanout2_U1_lower_2026-11-09.md\`、\`reviews/claude_fanout2_transfer_round4_2026-11-09.md\`、\`reviews/claude_fanout2_rigid_round5_2026-11-09.md\`：候補倍増族への二穴分布の障壁。
- 元の \`op:fanout-two\` は未解決。次は \(\mathcal N\) の**外**、すなわち語順・経路・非可換な局所制約を扱うこと。ただし修復定理の独立検証が先。

## 6. 投稿原稿との関係

このアーカイブは研究段階。Theorems A/B/C、Abstract、Conclusion、日本語版、PDF、正式な未解決問題の記述には一切手を加えない。新定理を論文に移すには、独立した厳密監査と著者判断を要する。

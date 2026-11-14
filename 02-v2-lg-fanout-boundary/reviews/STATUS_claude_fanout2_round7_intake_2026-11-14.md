# 第七段：重なる射影の hostability 第1・最終報告と初期点検

**日付：2026-11-14。区分：研究アーカイブ／未投稿・未査読。** 原資料はユーザー提出ZIP `新しいフォルダー(20261114-101144).zip`。報告の「PROVED」はClaude側の証明主張として記録し、ChatGPTが全ての一般論証を独立に認証したという意味にはしない。

## 提出資料

- `claude_fanout2_round7_checkpoint1_2026-11-14.md`（中間報告）
- `claude_fanout2_round7_hostability_report_2026-11-14.md`（最終研究報告）
- `check_round7_hostability_2026-11-14.py`（最上位ランナー）
- `round7_hostability_code_2026-11-14.tar.gz` 内の補助ソース：`hc_core.py`、`hc_construct.py`、`hc_search_case2.py`、`hc_check_case2.py`、`hc_search_case13.py`、最上位ランナーの同一コピー
- `out_check_round7_hostability_2026-11-14.txt`（Claudeが提出した全実行ログ。全体459秒と記載）

検査実行には最上位ランナーに加え **5個の補助Pythonソースが必須**。GitHubでは最上位ランナーと5補助スクリプトを同じ `reviews/round7_hc/` に保存する。

## 研究報告の到達点（主張の強さを分ける）

1. **場合I：単独削除**。$Z_{\kappa,A}=p\,aa,\ Z_{\kappa,B}=p'\,bb$（$p,p'>0$）、他の成分の削除差が0なら、2穴 `$h_1=a,h_2=b$`（適切な方向）を選ぶ構成を報告。印付き `aa` / `bb` の存在とY側の両持ち区間を用いる。**報告では PROVED、今回の独立評価は詳細補題の完全再証明までは行っていない**。
2. **場合II：削除のある別のη成分が別の根成分**。`HC_II` を報告。`FO`（印付き初出は自由部分木の前）、`P`（頻出窓の持続）、`FL`（硬直配置の排除）、`AB`（{a,b}の共通穴）、`OT`（他の削除型の共通穴）により、各根成分に閉じたデータ保存再配置を行い、**2穴 `e'=2`** でY/F両側に置く。報告では **PROVED（引用補題を前提）**。本ターンの再現試験は同構成を支持するが、完全な独立形式検証ではない。
3. **場合III：削除のある二つのη成分が同一根成分**。削除を「OT型の穴＋1文字穴」に再分割するアイデアはあるが、F側で他のψ成分に触れず両穴を置く局所化、Y/Fの方向と非空区切りの同時維持は**OPEN**。存在を示す有限テストで反例なし、は証明ではない。
4. **結論**：重なる射影の全面的な予想U、提案された一様多項式代表上界 `U_2`（$\tau(G,c_\Sigma)=O_r(v^{18}\bar\theta_G^{17})$）、一般の `op:fanout-two` はいずれも **未確立／OPEN**。S/P/L/互いに素なブロック版 $L^{\otimes\prime}$ と混同しない。

## ChatGPT側の独立した再実行（部分）

提出済みのコードをZIPから展開して個別に再実行した。以下はすべて exit status 0 で、報告にある `ok` または成功件数を出力した。

```text
python -I hc_check_case2.py 3 3 5     -> Case II 5 configs, ok=504
python -I hc_search_case13.py 3 7 10  -> Case I:ok=180; Case III:ok=20
python -I hc_check_case2.py 3 5 20    -> Case II 20 configs, ok=4680
python -I hc_check_case2.py 5 12 12   -> Case II 12 configs, ok=2772
python -I hc_search_case2.py random 3 21 24 -> tested=47
python -I hc_search_case13.py 4 9 25  -> Case I:ok=480; Case III:ok=20
```

- 合計 Case II 構成検査は37設定で7956組の `(状態、穴構成)` を確認。
- 上記 **6つの部分実行のみ**がChatGPT側で再実行済み。提出された459秒の全ランナー実行は、この監査では再実行していない。
- 最上位ソース `check_round7_hostability_2026-11-14.py` はtar内の同名コピーと**バイト単位一致**。
- 提出ログのSHA256: `3f697f7ccd327c57a16729376595ca5cd2401d3c4625524ce7268ba2e516a806`。実行ログが真正に生成されたことの保証ではなく、提供された原本を識別するためのチェックサム。
- 大規模ログの最終行は `ALL CHECKS PASSED  (459 s)`。これを**Claude提出ログの主張**として区別する。

## 論証・検証上の留保

- `HC_II` の証明は既存 `P1^⊗` のspan版、W2、型付き高さ、印を触らない先行削除などの**引用補題に依存**する。今回の検査は一般のgood MCFG導出から無限族の全量化を確認するものではない。
- `hc_check_case2.py` は成立する自由因子の抽象配置を乱数生成し、各設定の状態を最大24/12の部分標本に制限する。報告はこの間引きを明記している。
- `hc_search_case13.py` の場合IIIは、長さ≤3の穴候補で共通穴があるかを検査する**探索**。構成的な一般補題・文法反例の存在や不在は証明していない。
- 今回は新しい具体的な反例（定理主張への反例）は提出されていない。

## 今後

**最優先は場合IIIのF側局所化を証明するか、すべての型・印・極大自由部分木の仮定を満たす明示反例を構成すること。** その後に重なり版P0/P1/DFS/W2を含む一般の上界を別途監査する。研究原稿 `main.tex`、`japanese/main_JP.tex`、PDF、Theorems A/B/C、`op:fanout-two` は変更しない。

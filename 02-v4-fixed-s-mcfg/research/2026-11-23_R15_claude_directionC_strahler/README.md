# R15 — 方向C：Strahler 数（次元）で切った部分クラスでの型付けの境界（2026-11-23）

- 担当：Claude Opus 5.5（別スレッド）。依頼は `PROMPT_CLAUDE_R15_DIRECTIONC_STRAHLER_2026-11-23.md`（研究者の指示による方向C。並行して Astra が R14＝方向A を担当）。
- **名前の注意**：再開後の通し番号の R15 である。停止前（2026-11-16）の Astra の「R15」（言語 $L_{N,d}$、`rr:RV1-crossing`(ii) などで「R15 の $L_{N,d}$」と呼ばれているもの）とは別物。
- `deliverable/`：成果物 `R15_claude_directionC_strahler_2026-11-23.zip`（sha256 `cc388e71…9ebb4`）を展開したもの。原報告は無改変。`code/run_all_rerun_by_checker.log` は記録時の再実行ログ（PYTHONHASHSEED=1。添付ログとバイト単位で一致）。
- `claude_check_R15_2026-11-23.md`：記録時のメモ。**報告を書いたのと同じセッションによる機械的な確認だけ**で、数学的な確認としての価値はない。独立監査は別系列（Astra か DeepSeek）に回すこと。

## 主な結果（自己判定）

1. **上界（C2）〔VALID〕**：どの有限半群型付け・どの fan-out でも、次元（全導出木の Strahler 数の上限）$\le b$ の reduced good な提示では $t_{\rm typ}\le2r^b\bar\theta_G(|V||\mathsf S|^f)^{b+1}$、特徴データは $O(\|G\|^{b+2}\bar\theta_G)$。RV1 (ii) の論法をラベル（非終端、型ベクトル）に読み替えて `thm:data-from-typed-thickness` に代入したもの。$b=0$ が `thm:rankone-polydata`。
2. **fan-out 1 の下界（C3）〔VALID〕**：02-v3 の倍増族を $b$ 段・各段 $n$ 歩に打ち切った有限言語 $L_{n,b}$（$\dim=b$、$\|G\|=(13b+11)n+3$、$\bar\theta=(4b+2)n+2$）は Clark–Eyraud 代入可能で、$s_{U,3}$ のもとで長さ $(n+1)^b(2n+3)-2$ の語をすべての特徴標本に強いる。次数 $\delta_s(b)$ は LG で $\le2$（一様）、$s_{U,3}$ で $[(b+1)/2,\,b+2]$。fan-out 1 で「LG の境界は次元が有界でなくなる極限で現れる」という二分法が閉じた。型付けの水準では $s_{U,2}$ が LG の外でも次数一様。
3. **fan-out 2**：$L_{n,b}$ は冪移送で倒れる（具体的な二穴 Rect）〔VALID〕。次数が $b$ とともに増える族は **OPEN**（内容型付け $|\Sigma|\ge3$ に帰着）。C2 から、`op:fanout-two` を肯定する族は次元非有界が必要、`conj:rare-types` は全有界次元部分クラスで成立。

## 監査の最優先

報告 §5.3（$L_{n,b}$ の代入可能性。02-v3 付録 B のパーサ証明の移植、特に到達可能なスタック上の単射性の場合分け）。fan-out 1 の下界はこれだけに依存する。

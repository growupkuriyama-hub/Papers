# 研究台帳 — 02-v5-mcfg-regular-skeletons（#2骨格MCFG、方向A）

方向A：標的を「正則な骨格 $R$ ＋ 加法的な計数条件」として見て、骨格の統語半群によって、全 fan-out で分布代表長 $\tau(G,s)$ が多項式になる範囲を決める。

出発点は `02-v4-fixed-s-mcfg/` の第四段報告（定理L、2026-11-14、`02-v4-fixed-s-mcfg/v2/reviews/claude_fanout2_round4_report.md`）と、その監査 `audit_theorem_L_independent_2026-11-14.md`（GPT-6、FIXABLE）。

## ラウンド

| ラウンド | 日付 | 担当 | 主題 | 結果（判定は担当の自己判定） | 確認 |
|---|---|---|---|---|---|
| R14 | 2026-11-23 | Astra | 定理Lの確定、置換群の剰余類補題、偶数 run 言語 | T1 修正版 VALID（E1・E2 を修正、印についての無限定な文は REFUTED）。T2 補題 G と定理 $L^{\mathsf G}$ VALID（次数 $fk^\ell$）。T3 (A)：$E_{\rm ev}$（統語半群 $I_2\notin\mathbf{LG}$）は全 fan-out で多項式 | Claude が再実行（SHA・ログ一致）、$I_2$ と LG 型での一穴の反例を手で確認 |
| R15 | 2026-11-23 | 別スレッドの Claude | 方向C（Strahler 数で切った部分クラス） | 依頼文のみ（`PROMPT_CLAUDE_R15_DIRECTION_C_STRAHLER_2026-11-23.md`）。報告未着 | — |
| R16 | 2026-11-23 | Astra | 統一定理：装飾の移送定理と骨格のクラス | DT VALID。全入口で統語値を復元できる LG 下層を持つ骨格 ⟺ $S_R\in\mathbf{SL}*\mathbf{LG}=\mathbf{LTT}*\mathbf{LG}$。境界：局所冪等元が非可換な最小例 3 つ、ループ交換による障害 | Claude が再実行（ログ一致）。下の確認メモ |
| check | 2026-11-23 | Claude | R16 の監査と仕上げ | $\mathbf{SL}*\mathbf{LG}=\mathbf L\,\mathbf{ECom}$ を導出（文献の組み合わせ、要原典照合）。§5.2・DT 五段に誤りなし（補う論拠 3 点）。指数を $f|Q|k^m$ に下げる補題 L′（概略） | `2026-11-23_claude_check_R16/` |

## 規約

- 各ラウンドのフォルダに、依頼文、成果物（`deliverable/`）、再実行ログを置く。
- 第三者の著作物（Thérien–Weiss 1985 の PDF など）は、公開リポジトリには置かない。
- 有限検査は全称証明ではない。原稿に入れる主張は、本文の証明と、別系列による監査の両方を経てから確定とする。

## 未了の義務

1. $\mathbf{ECom}$ の局所性（$\mathbf{ECom}*\mathbf D=\mathbf L\,\mathbf{ECom}$）の既出文献を探す。なければ確認メモ §1(d) の論証を本文に入れる。
2. 補題 L′（現れうる窓だけを数える）を、定理Lの証明で確かめる。
3. 別系列（DeepSeek など）による、R16 §5.2 と DT の独立監査。

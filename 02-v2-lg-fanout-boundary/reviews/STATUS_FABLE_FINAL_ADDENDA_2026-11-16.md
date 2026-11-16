# Fable第3回・最終追補：AB絶対定数15、RRの導出、内部a排出

**2026-11-16 JST｜研究専用の最新索引**。本資料は[前段の第3回統合索引](STATUS_FABLE_ROUND3_AB_AND_MIXED_2026-11-16.md)の**後から届いた追補**であり、従来の原報告・監査・有限検査結果を上書きしない。以下は独立した数学的手証明監査による評価であり、形式証明・専門家査読・新規性の認定ではない。正本の定義は現行 [`main.tex`](../main.tex)。

## 新たに確認した結果

| 名称 | 監査後の数学的状態 | 正確な範囲 |
|---|---|---|
| **L（連補題）** | **VALID** | 枠付きオフセット交換F、実際の連 `x^R y` または `y x^R`、R≥4、2回分の正a室。合法2穴スライドとの比較で交換コスト0。 |
| **定理5（AB絶対定数）** | **VALID WITH STATED HYPOTHESES** | `κ=pbcq`, `κ′=pcbq`, `p,q∈{b,c}⁺`, 両Rot証人、実在加法的連結宿主、`N≥15M`（`M=max(δ,δ′)`）から `δ=δ′`。**枠長に依存しない十分定数15**（最適性は未主張）。 |
| **系6（block内部a）** | **VALID AT LANGUAGE LEVEL** | 非消去逆像によりu/vの内部a可。ただし枠はu,vの積、実在宿主とRot証人、`N≥15max(h,h′)`、`h=δ+|κ|_a`が必要。MCFGの新文法や厚さ上界は得ていない。 |
| **命題7（障壁のある枠）** | **VALID WITH STATED HYPOTHESES** | κκ′内に、b,cの両方があり一方を4個以上含む**連続{b,c}因子**があれば成立。**孤立枢軸**は対象外。 |
| **RC／CH（再切断・c連汲み上げ）** | **VALID WITH CONTEXT CLARIFICATION** | 同じ受理語の二通りの二穴切断と、`P(b^t c^q)^n b^t cQ`（t≥1,q≥2,n≥3）を用いて長いc連を作る。各比較成分型・中央非空を確認。 |
| **無RRの混合支持MX** | **VALID WITH ROOM/MS HYPOTHESES** | a-free成分 `(b^p c^q,b^r c^s)`、χ≥2、適法Single／**交錯または入れ子**の実在加法的Seed、`6d_*≤N−4`、任意Jの`d_*+d_J≤N−4`、比較対象各`d_m≤N−4`。RRは6重語からの**帰結**で、独立仮定ではない。 |
| **ON-loc／RED／SEED（内部a）** | **VALID WITH CLARIFICATIONS** | aを消すと各成分が`b^pc^q`、両端非a、Singleの外側a室`N−h_J≥4`、Seedの実際のa-budget、全局所非aブロックの1穴合同を保持。**δは保存、hは外側a室用**。 |
| **一般AB_pair／一般P_tree／非可換U／正式`op:fanout-two`** | **OPEN** | 一般IHは以前に反証済みで、今回の限定定理は元木の量化・全擬多様体境界の証明にはならない。 |

補足：前段索引の「枠長から独立した定数はOPEN」「入れ子だけの混合支持最小切片はOPEN」は、**ここに明記した新しい十分条件の下では解消**した。無条件の一般AB・一般P_treeを解いたことにはならない。3cの同名ファイル2個はバイト完全同一のため1本だけ保存。

## 一次資料と検証記録

- [AB絶対定数とblock版・元報告](fable_round3_framed_AB_addendum_absolute_constant_2026-11-16.md)
- [RR導出RC/CH・元報告](fable_round3b_RR_derivation_general_units_report_2026-11-16.md)
- [内部a排出RED/SEED・元報告](fable_round3c_internal_a_reduction_report_2026-11-16.md)
- [上記3報告の独立数学監査](audit_fable_final_addenda_independent_2026-11-16.md)
- [独立ローカル検証Python](audit_fable_final_2026-11-16_checker.py)
- [独立検証ログ](audit_fable_final_2026-11-16_checker.log)
- [最新ハンドオフ](../HANDOFF_CURRENT.md)

独立検査では、枠長1～4の全900組×欠損6組で**5,400**パラメータ、RC/CHの**80系列・600件の合法二穴交換**、ON-loc/REDの**32成分・136回のブロック交換**を検査し、すべてPASS。**有限の文字列検査は手証明とは別**であり、全言語の形式検証を意味しない。

## 次に残る核心

1. `π(u)=bcb`等の一般混合順序・χ=1と内部aの一般化。
2. 枠がa・他文字で隔離された**孤立枢軸**（命題7の外）。
3. 一般の同Parikh核について、中間Rot/全辺宿主の存在なしで欠損一致を示すAB_pair。
4. 木の大きい種B,Cから任意の小窓単位Jへの実移送・元文法厚さ・最小木の量化を持つ一般P_tree。
5. 非可換U・正式LG境界 `op:fanout-two` は依然**OPEN**。

**禁止された結論：** 今回の15という定数から無条件の特性標本上界やLG必要性を導いてはいけない。論文・PDF・`PAPER.yaml`・既存定理は変更しない。

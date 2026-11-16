# 研究停止時の数学的判定台帳 — 2026-11-16

**用途**：途中の「OPEN」「PROVED」表記の時間差を解決する索引。詳細証明の代わりではない。**主問題 `op:fanout-two` は OPEN**。原稿正本の定義は [`main.tex`](../main.tex)。数値実験は全称証明ではない。

## 判定レベル

- **MANUSCRIPT THEOREM**：現行`main.tex`の証明済み主張。査読済みの意味ではない。
- **HAND-AUDITED VALID [WITH HYPOTHESES]**：AI原報告の手証明を別の監査で再構成し、明示条件の下に正しいと判定。形式証明／専門家査読ではない。
- **CONDITIONAL**：依存補題・種・室条件が別途必要、または構成が未証明。
- **REFUTED**：原文の普遍命題に反例あり。修正命題が別にある場合は区別。
- **OPEN**：証明・完全な反例なし。探索が失敗しただけでもOPEN。
- **CERTIFIED FINITE**：指定した有限例・証明書の範囲のみ。

## 正式な主張と補助定理

| ID | 停止時の状態 | 正確な射程・必須前提 | 一次情報 |
|---|---|---|---|
| LG-SUFF | **MANUSCRIPT THEOREM** | 任意固定fan-out、rank固定、`S∈LG`：`O(||G||² θ̄_G)`型の特性標本長。 `thm:local-group-polydata`。 | [main.tex](../main.tex) |
| LG-BOUNDARY-F1 | **MANUSCRIPT THEOREM** | `f=1,r_max≥2` の必要十分境界／非LG側の指数下界。fan-out 2へは移せない。 | [main.tex](../main.tex) |
| LG-BOUNDARY-F2 | **OPEN** | `f≥2,r_max≥2` で `LG` が必要か。下界族未構成。 | [main.tex](../main.tex)の`op:fanout-two` |
| FABLE-C | **HAND-AUDITED WITH CLARIFICATIONS** | 可換・半束型付き・特定言語クラスの単項語長上界。一般非可換や任意`U₁`ではない。 | [Fable-C完全監査](Fable_C_complete_independent_mathematical_audit_2026-11-15.md) |
| T1 | **HAND-AUDITED** | R13の限定骨格型上界`N< θ̄_G [2(r+1)]^{2M+1}`。そのまま一様多項式の証明ではない。 | [R13統合](ROUND13_COMPLETE_SOURCE_AUDIT_2026-11-16.md) |
| TR／BT | **HAND-AUDITED WITH HYPOTHESES** | 局所`de/ed`転置、巡回`uv/vu`。単独Rot・実在加法的連結宿主・`h`等の室。 | [R14](ROUND14_COMPLETE_SOURCE_AUDIT_2026-11-16.md)／[R15](STATUS_ASTRA_FANOUT2_ROUND15_2026-11-16.md) |
| AB16／AB16-block | **HAND-AUDITED WITH HYPOTHESES** | `bbcc/bcbc`なら`N≥6M+1`、block版は`h`。後の改善・一般化を確認。 | [Astra R16](STATUS_ASTRA_FANOUT2_ROUND16_2026-11-16.md) |
| F/S/X | **HAND-AUDITED** | 枠補題Fは`(bc,a^i)↔(cb,a^{i+s})`、Sは同一受理語の合法二切断、Xは室付き二核順序交換。 | [Fable R3監査](audit_fable_round3_framed_AB_independent_2026-11-16.md) |
| AB-SPECIAL | **HAND-AUDITED** | `bbccc/bcbcc`：`N≥2M+1`、`bbbcc/bbcbc`と`bbcc/bcbc`：`N≥2M+2`（各Rotと宿主）。 | [Fable R3](STATUS_FABLE_ROUND3_AB_AND_MIXED_2026-11-16.md) |
| AB-FRAMED-15 | **HAND-AUDITED WITH STATED HYPOTHESES** | `κ=pbcq, κ′=pcbq`、`p,q∈{b,c}⁺`、単独Rot・**実在加法的連結宿主**、`N≥15M`で`δ=δ′`。15は枠長に依存しない。 | [最終追補](STATUS_FABLE_FINAL_ADDENDA_2026-11-16.md)／[監査](audit_fable_final_addenda_independent_2026-11-16.md) |
| AB-BLOCK-15 | **HAND-AUDITED AT LANGUAGE LEVEL** | 非消去逆像で`u,v`に内部aを許す。枠は`{u,v}⁺`、外側室には`h=δ+|κ|_a`、`N≥15max h`。新文法の厚さ不主張。 | [最終追補](STATUS_FABLE_FINAL_ADDENDA_2026-11-16.md) |
| AB-BARRIER | **HAND-AUDITED WITH HYPOTHESES** | `κκ′`にb,c両方と一方≥4個を含む連続`{b,c}`因子が実在する範囲。孤立枢軸除外。 | [最終追補](STATUS_FABLE_FINAL_ADDENDA_2026-11-16.md) |
| MS/P2 | **HAND-AUDITED WITH CLARIFICATIONS** | a-free混合支持のSingle、実在加法的交錯または入れ子Seed、正の室：二成分順序を保持し多重集合合成。種と許容小窓単位を混同しない。 | [Fable R2](STATUS_FABLE_ROUND2_MIXED_SUPPORT_2026-11-16.md)／[Astra R16](STATUS_ASTRA_FANOUT2_ROUND16_2026-11-16.md) |
| RR→MX | **HAND-AUDITED WITH ROOM/MS** | `(b^pc^q,b^rc^s)`、`χ≥2`、`6d_*≤N−4`、`d_*+d_J≤N−4`、比較両多重集合は`d_m≤N−4`。RC/CHからRRを生成、総非a Parikh一致⇒欠損和一致。交錯・入れ子両可。 | [RR原報告](fable_round3b_RR_derivation_general_units_report_2026-11-16.md)／[監査](audit_fable_final_addenda_independent_2026-11-16.md) |
| RED/SEED | **HAND-AUDITED WITH CLARIFICATIONS** | 成分のa消去後が`b^pc^q`、両端非a、Singleの元の外側a室`N−h≥4`、Seed再配置可能。欠損`δ`を保存し外側室だけ`h`で管理。 | [内部a原報告](fable_round3c_internal_a_reduction_report_2026-11-16.md)／[監査](audit_fable_final_addenda_independent_2026-11-16.md) |
| J/K-MIN | **HAND-AUDITED WITH HYPOTHESES** | `J=(bc,bc),K=(bbcc,bbcc)`。交錯Seedと`2max(δ,D)≤N−4`で`D=2δ`、入れ子は後のRR→MXにより指定室で到達。 | [R3統合](STATUS_FABLE_ROUND3_AB_AND_MIXED_2026-11-16.md)／[最終追補](STATUS_FABLE_FINAL_ADDENDA_2026-11-16.md) |
| U₂-OVERLAP | **HAND-AUDITED WITH CLARIFICATIONS** | overlapping projections `{a,c}`,`{b,c}`、bigramデータで言語所属決定、内容型、f/r≤2：`O(||G||^19 θ̄_G^17)`の限定上界。**U₁型付けの一般境界と別物**。 | [U₂ standalone](STATUS_U2_STANDALONE_FORMALIZATION_2026-11-15.md) |
| P_TREE-GENERAL | **OPEN** | 元の節点数最小木、任意単位、支持型混在、外側a会計、`∃B,C`→`∀J`。 | [R16残義務](astra_fanout2_round16_next_obligations_2026-11-16.md) |
| AB_PAIR-GENERAL | **OPEN** | 隣接交換に限らない同Parikh核で中間Rot・各連結宿主を一般に持たない場合。 | [最終追補](STATUS_FABLE_FINAL_ADDENDA_2026-11-16.md) |
| IH-GENERAL | **REFUTED** | 交錯・入れ子で連結宿主の一般存在は偽。実際のreduced good fan-out2/rank2文法族反例。**P_treeを反証したのではない**。 | [Astra R15](STATUS_ASTRA_FANOUT2_ROUND15_2026-11-16.md) |
| SMALL-WINDOW-IH | **OPEN** | `δ_J≤(N−1)/(24θ²)`に入る単位に限定したIHの一般成否（種B,Cは窓外でもよい）。 | [R15](STATUS_ASTRA_FANOUT2_ROUND15_2026-11-16.md) |
| U-NONCOMM | **OPEN** | 非可換の一般Parikh/欠損剛性に関する補助予想。全称形は現時点では証明なし。 | [R13/14](STATUS_FANOUT2_ROUNDS12_TO14_FABLE_2026-11-16.md) |
| LONG-U1-LOWER | **OPEN** | fan-out2/rank2でgood/reduced/全1・2穴代入可能、元厚さが小さい超多項式希少型語族。 | [R12](ROUND12_COMPLETE_SOURCE_AUDIT_2026-11-16.md) |

## やってはいけない推論

- `AB-FRAMED-15`の「15」は**連結宿主を構成しない**。`AB_PAIR-GENERAL`も解けない。
- `RR→MX`は任意の成分内容型に渡らない。a-free `b^pc^q`・`χ≥2`・指定室を保持。
- `J/K-MIN`は全木・全単位の量化を満たさない。
- `U₂`は`U₁`ではない。有限半群型付けと「二つの射影を使う特別な言語クラス」を混同しない。
- 反証済みX1/CA/IHを補題として使わない。元の半窓 `(N−1)/(24θ²)` の`θ`は**元文法の厚さ**であり、細分後の厚さではない。
- 古い研究索引の`OPEN`は作成当時の履歴。新追補が解決した**限定切片**だけが状態更新される。無条件の一般問題は今もOPEN。

## 原文にある別の定量的未解決点

現行`main.tex`のConclusionは、LG上界の`||G||` 1因子の隙間と、非可換群での定数`c_{G,f}`の絶対多項式依存も未解決としている。今回のfan-out2研究では手を付けていない。主開問題と混同しない。

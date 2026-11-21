# Fable 第2回：混合支持P2+の語列加法性MS・RR付きParikh剛性MX

**2026-11-16 JST。独立数学監査後の研究専用アーカイブ。** 現行論文 [`main.tex`](../main.tex) の定義が優先。これは研究報告および独立した手証明の監査であり、形式証明・専門家査読・文献的新規性の認定ではない。正式な`op:fanout-two`は**OPEN**。

## 主張と監査状態

| 対象 | 判定 | 厳密な射程 |
|---|---|---|
| **Comm** | **VALID** | 単位の二成分`u_J,v_J`がa-free、正の単独受理語`a^l u_J a^g v_J a^r`、外側a総数`N-d_J≥4`で、各**ブロック全体**について`a u_J ≡ u_J a`、`a v_J ≡ v_J a`。内部のa挿入を主張しない。 |
| **MS**（mixed-support sequence additivity） | **VALID WITH CLARIFICATIONS** | `u_J=b^{p_J}c^{q_J},v_J=b^{r_J}c^{s_J}`、p,q,r,s≥1、正欠損、実際のSingleおよび交錯・入れ子の**実在加法的Seed**、種a-room≥2、許容半窓、合成欠損≤N−4。連結核宿主を使わず、交錯で`u_1...u_n v_1...v_n a^{N-d_m}`、入れ子で`u_1...u_n v_n...v_1 a^{N-d_m}`を構成。 |
| **Rc**（c-run redistribution） | **VALID** | 長さmのc連を含む**実在受理語**が必要。非空比較片と非空中央の正c連の和≤m−1。 |
| **CC**（`cb^t≡b^tc`） | **VALID WITH LOCAL HOST** | 実在する`Pc^α b^t c^βQ∈L`の両側c連（各正）とRcのroom。両c連1のとき別のc連から合法に1文字借りる宿主が必要。 |
| **MX**（under RR） | **VALID WITH EXPLICIT HYPOTHESES** | 許容単位のc指数最大値`χ≥2`、実在受理語のc連`m≥2χ+1`、上記MS条件。すると二多重集合の**非a総Parikh**一致から欠損和一致。 |
| **RR無しの一般P_tree／一般AB／小窓IH／非可換U／正式LG境界** | **OPEN** | 新しい一般反例・一般多項式上界は未発見。旧一般IHと原文X1/CAは引き続き**REFUTED**。 |

**重要な修正・限定**（独立監査が優先）：
1. MSの「成分が同型なら任意の語にも成立」は、今回の手証明では**a-free成分に限定**。内部aを許す場合、外側のa会計に`h=δ+内部a数`を導入して別途再証明する必要がある。
2. 入れ子の場合、二穴中央を非空にするためaを1文字移す。`d_B+d_C≤N−2`から小さい種欠損を保持し、**内側・外側の交換順を場合分け**してa室≥2を確保。種B,C自身に小窓は課さない。
3. RR無しで「共通受理文脈が存在しない」という普遍的な非存在は**証明されていない**。現在の証明の方法では作れていない、という意味でのみ正しい。
4. `χ=2`のRRは`m≥5`。Fable原報告§6の「m≥4」は誤記で、RRを満たさない最大連長2の切片の地位は変わらない。
5. Fable自身は**Pythonを実行していない**。独立監査では新しい標準ライブラリのチェッカーを実行し、交錯・入れ子のTransport 40,840事例、CC一穴宿主3,190事例、a会計の注意例を確認。有限テンプレート検査と一般の手証明を区別。

## 具体的な未解決ミニマル問題

`J=(bc,bc)`、`K=(bbcc,bbcc)`、欠損`δ=d_J`, `D=d_K`に関して、**RR無し**の適法なSingle/交錯Seedと正のa室から`D=2δ`を強制できるか。MSから得る`(bc)^4 a^{N−2δ}`と`(bbcc)^2 a^{N−D}`は同Parikhだが**同じ語ではない**ため、現状でU_shiftに直接適用できない。RR無しの証明・木由来反例とも未発見。単なる有限言語の反例と、元文法厚さおよび節点数最小木まで満たす木版反例を区別すること。

## 一次資料

- [Fable第2回・原報告（元バイト）](fable_round2_mixed_support_P2plus_report_2026-11-16.md)
- [ChatGPT独立数学監査](audit_fable_round2_mixed_support_P2plus_independent_2026-11-16.md)
- [独立の局所検査コード](audit_fable_round2_local_checks.py) — `python3 -I reviews/audit_fable_round2_local_checks.py`
- [Fable第3回・省枠集中探索プロンプト](PROMPT_FABLE_ROUND3_MINIMAL_MIXED_SUPPORT_2026-11-16.md)
- [直前のAstra第16段・研究索引](STATUS_ASTRA_FANOUT2_ROUND16_2026-11-16.md)
- [最新の引き継ぎ](../HANDOFF_CURRENT.md)

**保存対象のSHA-256**：
- 原報告 `798962fe0b872b7ec7dd4c312ad29604311d8d9b26d3abfe87e6c348037ce6ad`
- 独立監査 `cb11e045c2476107335557b3554534963bf8d0c61df557169445818f621cd21a`
- チェッカー `b75a64062c87233364c4b34023dfaf4f044c0a51aef54413c58639dec5c94614`
- 第3回プロンプト `fb0c0494eb0cdbc2a3e68716cc4683b48e2de06c8b000854d2c15708625cb277`

**厳格な保存境界**：英日`main.tex`、PDF、`PAPER.yaml`、Theorems A/B/Cは変更せず、新しい独立論文も起案しない。

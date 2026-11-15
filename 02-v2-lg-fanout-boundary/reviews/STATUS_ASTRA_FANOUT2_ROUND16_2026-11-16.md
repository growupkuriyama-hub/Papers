# Astra第十六段：AB16／P2／P2+ — 独立数学監査済み研究アーカイブ

**2026-11-16 JST。研究専用。** 正本は[`main.tex`](../main.tex)。現行`op:fanout-two`は**OPEN**。この資料は[第十五段](STATUS_ASTRA_FANOUT2_ROUND15_2026-11-16.md)を更新する研究状況であり、専門家査読や形式証明済みという意味ではない。

## 数学的判定（独立手証明監査）

| 対象 | 判定 | 正確な射程 |
|---|---|---|
| **AB16** `bbcc/bcbc` | **VALID WITH STATED HYPOTHESES** | 内容型付き1/2穴代入可能L、最短a冪`a^N`、両単独Rot証人、**実在加法的連結宿主**、正欠損、`N≥6max(δ₁,δ₂)+1`なら`δ₁=δ₂`。C=6は十分定数で最適とは不明。 |
| **AB16-block** `uuvv/uvuv` | **VALID WITH STATED HYPOTHESES** | 非消去準同型の逆像による移送。`u,v`内部にaがある場合`h=δ+内部a数`とし`N≥6max(h₁,h₂)+1`。 |
| **P2** | **VALID WITH CLARIFICATIONS** | 二成分の非a支持が単色`({b},{c})`、実在する交錯または入れ子の加法的種と正のa室の下、**連結核宿主を使わず**同Parikh多重集合の欠損和一致。 |
| **ON/P2+** | **VALID WITH CLARIFICATIONS** | b相／c相の各成分にaの混入は許すが、極大a連の数と余剰a条件を保持。**混合支持`({b,c},{b,c})`には未拡張**。 |
| **有限計算** | **CERTIFIED FINITE** | 11証明書・21,249原始1/2穴交換の独立検査、AB1,810事例ほか。数値検査は一般証明の代わりではない。 |
| **原文X1・原文CA・一般IH** | **REFUTED（既存の反例）** | 40語X1・67語CA・第十五段交錯／入れ子IH反例は有効のまま。 |
| **一般AB・一般P_tree・小欠損窓IH・U・正式LG境界** | **OPEN** | 部分クラス定理は一般形を解決しない。 |

AB16では枠内`bc/cb`のオフセット付き局所転置と受理語`bbbbcccc a^E`の二通りのb冪二分割を使い、同一接頭語`bbcbbccc`と異なる末尾a指数に関する`U_shift`の矛盾を導く。P2の二穴Transportには`E₀=(a^{e−1},a,ε)`、`E₁=(ε,b^r,c^s)`を使い、中央・各成分の非空性と実型一致を監査。**種B,Cを小欠損窓へ押し込まず、任意の小窓単位Jへの移送**という量化を保つ。

## 正本資料（原バイト同一で保存）

- [第十六段Astra完成数学報告](astra_fanout2_round16_report_2026-11-16.md)
- [独立数学監査報告](audit_astra_fanout2_round16_independent_2026-11-16.md)
- [次に残る三つの数学的義務](astra_fanout2_round16_next_obligations_2026-11-16.md)
- [第十六段Astraへの探索依頼](PROMPT_ASTRA_FANOUT2_ROUND16_NONCYCLIC_AB_DIRECT_PTREE_2026-11-16.md)
- [元Astra再現ZIP（全証明書・ソース・ログ）](round16/astra_fanout2_round16_reproducibility_2026-11-16.zip)
- [独立監査補完ZIP（再実行可能）](round16/astra_fanout2_round16_reproducibility_audit_fixed_2026-11-16.zip)
- [軽量PythonソースZIP](round16/round16_portable_source_2026-11-16.zip)
- [ZIPの封入漏れ・SHA-256・再現性](round16/REPRODUCIBILITY_PROVENANCE_2026-11-16.md)
- [全体ハンドオフ](../HANDOFF_CURRENT.md)

## 正本ZIPの再現性に関する注意

元の再現ZIPの59ファイルのSHA-256照合は全件一致。しかし本来必要な`sources/reviews/round15/SHA256SUMS.txt`が**1ファイル欠落**するため、**元ZIPのままの`code/run_all.py`は途中で停止**。監査用の派生ZIPには固定GitHub原本を補い、全6ジョブ終了コード0、元ログと一致、21,249手の独立replay完了。原ZIPを完全版と呼び直さない。完全ZIPと監査補完ZIPは、このGitHubアーカイブに**原バイト同一で保存した**。Git blob SHAはそれぞれ`f9a56d18d09580a95c7b20e90e4a7bb21465a4b5`と`7e41fa36f9b42a76e2f24a491e5f55146f13781a`で原本と一致する。元ZIPの封入漏れは修復されないので、再実行には補完ZIPを使うこと。

## 次の研究義務

1. `({b,c},{b,c})`等の**混合支持の直接二成分Transport**（連結宿主を仮定しない）。
2. 一般の枠付き隣接転置`pbcq/pcbq`のコスト消去、室と型の完全な追跡。
3. 支持クラスが異なる単位間の橋渡し。木の分岐種B,Cと任意の小欠損単位Jの**量化順序を維持**する。

**保護対象：** 英語・日本語論文、PDF、`PAPER.yaml`、既存Theorems A/B/Cは変更しない。以上は新しい独立論文の起案でもない。

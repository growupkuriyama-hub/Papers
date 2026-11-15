# Astra 第十五段 — fan-out 2 AB/IH 探索・独立監査・再現資料

**基準日：2026-11-16 JST。研究アーカイブのみ。** 論文の正本は [`main.tex`](../main.tex)、最新ハンドオフは [`HANDOFF_CURRENT.md`](../HANDOFF_CURRENT.md)。正式な `op:fanout-two` は引き続き **OPEN**。

## 最新判定（独立した手証明監査であり、専門家査読・形式証明ではない）

| 対象 | 判定 | 厳密な射程・注意 |
|---|---|---|
| **BT**（任意非空ブロック `uv/vu`） | **VALID WITH HYPOTHESES** | 単独Rot証人、実在する**加法的な連結宿主**、`N≥4 max(h₁,h₂)+1`。内部aがない場合のみ `h_i=δ_i`。旧TRの非消去逆像による持ち上げ。 |
| **NF / BT-NF** | **VALID WITH HYPOTHESES** | 正欠損・非空a室を保持する内部a連正規化。正規化後に巡回共役となる限定対。 |
| **ST** | **VALID** | 整列した非a射影とParikh線形等式による**全arity内容型付き組代入可能性**。MCFL性は別途確保。 |
| **一般IH（交錯／入れ子）** | **REFUTED** | 有限言語 `L_{N,d}`、reduced good fan-out 2/rank 2 文法、節点最小の `a^N` 導出木、内部比較不能大節点、二重置換、正の加法的室を満たすが**連結宿主なし**。 |
| **小欠損窓IH** | **OPEN** | 第十四段T2′に現れる `δ_J≤(N−1)/(24θ²)`。今回の大節点はこの窓外。分岐種B,Cと許容単位Jを混同しない。 |
| **一般AB_pair／P_tree／非可換U／正式LG境界** | **OPEN** | BTは一般ABの証明ではなく、IH反例はP_treeの反例でもない。 |

### 具体的なIH反例

`π` をa消去射影として、`L_{N,d}={w : π(w)∈b*c*, |w|_b=|w|_c, |w|_a+d|w|_b=N}`（`N=d2^q+3`）。同じ非a内容 `{b,c}` の二核を連結すると射影に `cb` が現れ、`b*c*` に反する。具体例 `d=64,q=4` では `N=1027`、元文法厚さ `θ̄_G=97`、比較節点収率長128、欠損128、目標外側a-budget769であっても連結宿主がない。任意固定線形室条件で同じ障壁が残る。一方、この言語で `δ=d|κ|_b` なので **P_treeは保持される**。

**以前の反証は有効のまま：** 第十三段の原文X1（40語反例）と第十四段の原文CA（67語反例）は偽。X1⁺／CA*の型一致・加法的初期budget・正の室を省略しない。

## 保存資料

- [Astraへの第十五段探索プロンプト](PROMPT_ASTRA_FANOUT2_ROUND15_AB_IH_2026-11-16.md)
- [Astra原報告全文（証明・反例・コード・ログを含む）](astra_fanout2_round15_report_2026-11-16.md)
- [ChatGPT独立数学監査](audit_astra_fanout2_round15_independent_2026-11-16.md)
- [検証プログラム](round15/round15_check.py) ／ [完全実行ログ](round15/round15_check.log)
- [TR 21手証明書](round15/tr13_certificate.json) ／ [調査したGitHubソースのblob識別子](round15/source_manifest.json)
- [オリジナルパッケージREADME](round15/ROUND15_README.txt) ／ [SHA-256一覧](round15/SHA256SUMS.txt)

ユーザー添付の再現用ZIPに含まれた**7つのテキストエントリを個別ファイルとして保存**する（ZIPバイナリ自体はこの記録では保存しない）。`SHA256SUMS.txt` の参照ファイル名について、原報告はこの `reviews/` ディレクトリ、その他は `reviews/round15/` を指す。文献的な新規性や正式証明の認定は行っていない。

## 次の探索義務

1. **非巡回AB**：`bbcc/bcbc` のRot証人と実在の加法的連結宿主、十分な室の下で欠損一致を証明するか反例を出す。現在のBTは適用不能。
2. **連結化を経由しないP_tree**：交錯・入れ子の二成分配置を保ったまま欠損の線形関係を導く。
3. **小窓IHの量化**：最初の大きい分岐種B,Cと、後から交換する小欠損単位Jの役割を分離して再定式化する。

**保存の範囲：** 本研究資料と引き継ぎ索引のみ。英語・日本語 `main.tex`、PDF、`PAPER.yaml`、Theorems A/B/C、`op:fanout-two` は変更しない。

# fan-out2／LG境界研究の時系列（停止時点 2026-11-16）

この年表は**研究中に実際に蓄積したアーカイブ**の流れを示す。古い報告の判定をそのまま最新とはしない。最新は [停止時台帳](PAUSE_PROOF_STATUS_LEDGER_2026-11-16.md)。対象は `02-v2-lg-fanout-boundary` の研究専用資料であり、論文の投稿状態や博士論文全体ではない。

| 日付・段階 | 当時の研究・結果 | 現在から見た位置づけ |
|---|---|---|
| 2026-11-01〜11-13 | 基礎的なfan-out2／有限半群境界の調査、論文主定理A/B/C・open problemを分離。 | 正式原稿と独立研究を混在させない。[長期HANDOFF](../HANDOFF_CURRENT.md)と原稿本文を参照。 |
| 11-13〜14 | Opus系、局所鳩ノ巣、ordered joining S/P、block L^⊗；旧4穴法の破綻とbundle修復。 | 限定上界ルートの歴史。[L^⊗監査](audit_Ltensor_prime_independent_2026-11-14.md)を優先。 |
| 11-14〜15 | Claude R6–11：重複射影の共通穴・hostability・P1/B6/DFSを修正。 | [U₂の限定多項式上界](STATUS_U2_STANDALONE_FORMALIZATION_2026-11-15.md)を手監査。全`U₁`型付けへの拡張は未証明。 |
| 11-15 R12 | 3,093の下界候補を探索。違法な1/2穴代入可能性を排除したが、超多項式族未発見。 | [R12](ROUND12_COMPLETE_SOURCE_AUDIT_2026-11-16.md)。失敗は一般不可能性ではない。 |
| 11-15 Fable初回 | 可換／半束型付けのFable-Cなど。 | [完全監査](Fable_C_complete_independent_mathematical_audit_2026-11-15.md)；非可換の一般Uには届かない。 |
| 11-15 R13 | Rot・骨格型T1・U探索。原文X1を40語反例で反証。 | [R13](ROUND13_COMPLETE_SOURCE_AUDIT_2026-11-16.md)。X1⁺での型・paddingが必要。 |
| 11-15〜16 R14 | 型安全X1⁺、TR（`de/ed`）、CA原文を67語反例で反証。 | [R14](ROUND14_COMPLETE_SOURCE_AUDIT_2026-11-16.md)。CA*は実在加法的Seedが必要。 |
| 11-16 Astra R15 | block BT/NF、一般IHの**交錯・入れ子反例**。 | [R15](STATUS_ASTRA_FANOUT2_ROUND15_2026-11-16.md)、[PR #131](https://github.com/growupkuriyama-hub/Papers/pull/131)。P_treeは反証されていない。 |
| 11-16 Astra R16 | AB16（`bbcc/bcbc`）、二成分単色P2/P2+、再現ZIPと独立監査。 | [R16](STATUS_ASTRA_FANOUT2_ROUND16_2026-11-16.md)、[PR #132](https://github.com/growupkuriyama-hub/Papers/pull/132)。元ZIPはSHA一覧が1件欠落。 |
| 11-16 Fable R2 | mixed-support MSと、実在長c連RRを仮定するMX。 | [R2](STATUS_FABLE_ROUND2_MIXED_SUPPORT_2026-11-16.md)、[PR #133](https://github.com/growupkuriyama-hub/Papers/pull/133)。RRは後の追補で一定条件下に**導出**。 |
| 11-16 Fable R3（並行2本） | 枠付きABの長さ5切片・長さ依存定数、交錯`J=(bc,bc),K=(bbcc,bbcc)`の`D=2δ`。 | [R3](STATUS_FABLE_ROUND3_AB_AND_MIXED_2026-11-16.md)、[PR #134](https://github.com/growupkuriyama-hub/Papers/pull/134)。後の追補が絶対定数と入れ子に拡張。 |
| 11-16 Fable最終追補 | AB絶対定数15／block版／障壁版、RC/CHからRRを導出、ON-loc/REDで内部a排出。 | **[最新数学索引](STATUS_FABLE_FINAL_ADDENDA_2026-11-16.md)**、[PR #135](https://github.com/growupkuriyama-hub/Papers/pull/135)。一般AB_pair・P_tree・正式LG境界はOPEN。 |
| 11-16 著者による研究一時終了 | この停止時点を、状態台帳・依存マップ・反証・再現・未解決・再開プロンプトの複数索引に整理。 | **[研究停止の入口](../RESEARCH_PAUSED_2026-11-16.md)**。新しい研究を自動開始しない。 |

## 原稿とアーカイブの分離

原稿の現行 `main.tex` にあるTheorems A/B/Cと`op:fanout-two`は、この停止作業でも変更しない。研究記録は`reviews/`下に残し、個別AIの「PROVED」と独立監査の「VALID WITH HYPOTHESES」を区別。GitHub保存の日付は証明の学術的正当性・新規性を意味しない。

**時系列の補正規則**：後から追加された報告は、以前のOPENの**限定切片だけ**を解決する場合がある。例：Fable R3一般枠の`O(n²)`が後の`15`へ改善、R2の追加仮定RRはR3b条件下に導出。個々の元ファイルは原記録のまま改変しない。

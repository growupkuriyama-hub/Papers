# Astra第十六段：再現資料の由来・検証結果・保管境界

**2026-11-16 JST。** 本資料はGitHubに**実際にバイナリ保存したZIP**のチェックサム、封入漏れと独立再実行の範囲を記録する。

| 元ファイル | SHA-256 | 状態 |
|---|---|---|
| `astra_fanout2_round16_reproducibility_2026-11-16.zip` | `0948b04df8cee3a6350e648b041e292a35851e227d0055d27c21457fd37874e2` | 60項目、元の`SHA256SUMS.txt`が記載する59個はいずれも一致。ただし前段のSHA一覧1件欠落。 |
| `astra_fanout2_round16_reproducibility_audit_fixed_2026-11-16.zip` | `26889debd64b12b5e888a87bc002e204c37af692aea58b9915febfbb3cb5f3ae` | 64項目。元ファイルを変更せず、1件の不足原本・追加独立replay・数学監査・修復説明を加えた派生ZIP。 |
| `astra_fanout2_round16_report_2026-11-16.md` | `56dfa39a51cee7fa3d5d29e9d328a491b0bd2b49c1cf7622cc5f487e18825571` | GitHub内の原報告ファイルへ原バイトそのまま保存。 |
| `astra_fanout2_round16_next_obligations_2026-11-16.md` | `e636a637df6f00e8dc5ddae36976c351ba50f110367446796c01507c3f3a9f15` | GitHub内の原義務ファイルへ原バイトそのまま保存。 |
| `audit_astra_fanout2_round16_independent_2026-11-16.md` | `ff17ef1a695fb54d11921577b69d68cc1e294c5f837abb32545b98828953c545` | GitHub内の独立監査ファイルへ原バイトそのまま保存。 |
| `PROMPT_ASTRA_FANOUT2_ROUND16_NONCYCLIC_AB_DIRECT_PTREE_2026-11-16.md` | `b19afcf33cfe8194525cbfac6a64d4646b0ffe298389234d2630dd013ba424c3` | GitHub内の探索依頼原本へ原バイトそのまま保存。 |

**封入漏れ**：元ZIPの`code/source_audit.py`が参照する`sources/reviews/round15/SHA256SUMS.txt`が元ZIPにない。固定commit `d1718eff64830be0ae6e2483fbeda8a6fe04843d` の[GitHub原本](../round15/SHA256SUMS.txt)（Git blob `72d0d77ba705a270395c087188f7c17e25a4ff3a`）を監査用派生ZIPにだけ補完。**元ZIPの`python3 code/run_all.py`はsource_auditでFileNotFoundError。**

**修復後の結果**：Python 3.13.5で`python3 -I code/run_all.py`を実行し、全6ジョブ終了0。元ログのstdout・stderr・終了コード一致、元の記録との差はPython版記録（3.12.14 vs 3.13.5）のみ。生成した11証明書は保存済み証明書と一致。さらにAstra元実装をimportせず21,249原始交換を独自検証し、3種の意図的改竄を拒否。有限全件チェックは一般命題の形式証明を意味しない。

**ZIP全体をGitHubに原バイト同一で保存済み**：Git blob SHAはローカルで計算したZIPそのもののSHAと一致する。

- [元のAstra完全ZIP](astra_fanout2_round16_reproducibility_2026-11-16.zip)：556,306バイト、Git blob `f9a56d18d09580a95c7b20e90e4a7bb21465a4b5`。元ZIPは`source_audit`で停止する。
- [独立監査補完ZIP](astra_fanout2_round16_reproducibility_audit_fixed_2026-11-16.zip)：619,412バイト、Git blob `7e41fa36f9b42a76e2f24a491e5f55146f13781a`。不足した前段SHA一覧と監査資料を追加し、全6ジョブ再生済み。
- [軽量ソースZIP](round16_portable_source_2026-11-16.zip)：16,472バイト、Git blob `00184a1a29b6b0126f8abf659400bc1e40b9e851`。Pythonソースを含むが、巨大な証明書と固定原文スナップショットは省略。READMEに再生成手順を記載。

元ZIPと補完ZIPは11個の証明書JSON、コード、ログ、取得した原文スナップショットを保持する。約48MBは解凍後総容量であり圧縮ZIPのサイズと区別する。

# Astra第十六段：再現資料の由来・検証結果・保管境界

**2026-11-16 JST。** 本資料はZIPバイナリをGitHubに保存したという主張ではなく、完全ZIPを識別するチェックサム、封入漏れ、独立再実行の範囲を記録するものである。

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

**ZIP全体はこのGitHubコミットに格納しない**：完全ZIPは圧縮約556/619KBだが11個のJSON証明書、固定ソーススナップショット等を展開すると約48MBになる。これらのバイト列はチャットのアップロード資料として残り、GitHubのこの報告・監査・SHAで識別できる。再現コード・ログ・巨大な証明書全体をGitHubにあると誤読しないこと。

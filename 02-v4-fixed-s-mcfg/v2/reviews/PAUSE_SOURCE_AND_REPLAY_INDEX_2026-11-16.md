# 研究停止時・原資料／監査／再現可能性の索引

**2026-11-16 JST。** 既存資料をリンクで結ぶ索引。元ファイルは移動・改名・上書きしない。以下の`reviews/`内リンクは同ディレクトリを基準とする。非ASCII ZIP等はバイナリをGitHubで直接開けない場合がある。正本索引は [停止入口](../RESEARCH_PAUSED_2026-11-16.md)。

## 1. 系統別に読む順序

| 系統／時期 | 正確な現行研究状況 | 原報告 | 独立監査／検査 |
|---|---|---|---|
| R12 失敗した下界候補 | [R12完全記録](ROUND12_COMPLETE_SOURCE_AUDIT_2026-11-16.md) | [R12 report](claude_fanout2_round12_lower_bound_report_2026-11-15.md) | [R12 audit](audit_claude_fanout2_round12_independent_2026-11-15.md) |
| 初回Fable A/B/C | [完全記録](FABLE_20261115_COMPLETE_SOURCE_AUDIT_2026-11-16.md) | [初回 report](fable_fanout2_open_problem_report.md) | [Fable-C 全文監査](Fable_C_complete_independent_mathematical_audit_2026-11-15.md) |
| R13 Rot/T1とX1反例 | [R13完全記録](ROUND13_COMPLETE_SOURCE_AUDIT_2026-11-16.md) | [R13 report](claude_round13_noncomm_U_final_report_2026-11-15.md) | [独立監査](audit_claude_round13_noncomm_U_independent_2026-11-15.md) |
| R14 TR、CA反例 | [R14完全記録](ROUND14_COMPLETE_SOURCE_AUDIT_2026-11-16.md) | [R14 report](claude_round14_noncomm_Parikh_report_2026-11-15.md) | [独立監査](audit_claude_round14_noncomm_Parikh_independent_2026-11-16.md) |
| Astra R15 BT/NF、IH反例 | [R15状態](STATUS_ASTRA_FANOUT2_ROUND15_2026-11-16.md) | [R15原報告](astra_fanout2_round15_report_2026-11-16.md) | [R15監査](audit_astra_fanout2_round15_independent_2026-11-16.md)、[コード](round15/round15_check.py)、[ログ](round15/round15_check.log) |
| Astra R16 AB16/P2/P2+ | [R16状態](STATUS_ASTRA_FANOUT2_ROUND16_2026-11-16.md) | [R16原報告](astra_fanout2_round16_report_2026-11-16.md) | [監査](audit_astra_fanout2_round16_independent_2026-11-16.md)、[ZIPの由来](round16/REPRODUCIBILITY_PROVENANCE_2026-11-16.md) |
| Fable R2 MS/MX（RR付き） | [R2状態](STATUS_FABLE_ROUND2_MIXED_SUPPORT_2026-11-16.md) | [R2原報告](fable_round2_mixed_support_P2plus_report_2026-11-16.md) | [R2監査](audit_fable_round2_mixed_support_P2plus_independent_2026-11-16.md)、[局所検査](audit_fable_round2_local_checks.py) |
| Fable R3 2本の独立ルート | [R3状態](STATUS_FABLE_ROUND3_AB_AND_MIXED_2026-11-16.md) | [枠付きAB](fable_round3_framed_AB_report_2026-11-16.md)、[J/K最小障害](fable_round3_mixed_support_minimal_obstruction_report_2026-11-16.md) | [AB監査](audit_fable_round3_framed_AB_independent_2026-11-16.md)、[J/K監査](audit_fable_round3_mixed_support_independent_2026-11-16.md) |
| **Fable R3最終追補（停止時最新）** | **[最終状態](STATUS_FABLE_FINAL_ADDENDA_2026-11-16.md)** | [絶対定数15](fable_round3_framed_AB_addendum_absolute_constant_2026-11-16.md)、[RR導出](fable_round3b_RR_derivation_general_units_report_2026-11-16.md)、[内部a還元](fable_round3c_internal_a_reduction_report_2026-11-16.md) | [最終監査](audit_fable_final_addenda_independent_2026-11-16.md)、[検査コード](audit_fable_final_2026-11-16_checker.py)、[ログ](audit_fable_final_2026-11-16_checker.log) |
| L^⊗／ブロック系 | [旧方法4穴の修復監査](audit_Ltensor_prime_independent_2026-11-14.md) | [R5状態](STATUS_fable_fanout2_round5_2026-11-14.md) | [de Bruijn検査](audit_fable_round5_debruijn_ell2_ell3_2026-11-14.py) |
| 重複射影`U₂`上界 | [U₂状態](STATUS_U2_STANDALONE_FORMALIZATION_2026-11-15.md) | [U₂単独定理・証明](theorem_U2_overlapping_projections_standalone_2026-11-15.md) | [R11 source bundle](ROUND11_SOURCE_BUNDLE_2026-11-15.md) |

**古い資料中の未解決ラベルは、より新しい限定結果が判明した時点では更新されていない場合がある。** 原文は不変、現在の判定は最新追補＋本停止台帳で確認する。

## 2. そのまま実行できる局所チェックの入口

レポジトリをclone済みで、`02-v4-fixed-s-mcfg/v2`をカレントディレクトリにしてから、Python 3（標準ライブラリ）で：

```bash
python3 -I reviews/audit_fable_round2_local_checks.py
python3 -I reviews/audit_fable_round3_local_replay.py
python3 -I reviews/audit_fable_round3_mixed_support_replay.py
python3 -I reviews/audit_fable_final_2026-11-16_checker.py
python3 -I reviews/round15/round15_check.py
```

**目的**：既存の局所Rect式、実型、文字列、a予算、または指定有限反例の再生。**形式証明でも、すべてのMCFLの会員判定でもない**。Python版によって出力時刻などは異なり得る。提出済みログと一致する場合も「一般証明」の新根拠にはならない。

Astra R16： [補完ZIP](round16/astra_fanout2_round16_reproducibility_audit_fixed_2026-11-16.zip) を解凍したディレクトリで `python3 -I code/run_all.py`。**元ZIPは必要な`sources/reviews/round15/SHA256SUMS.txt`の1ファイルが欠落し同コマンドは失敗する**。正確な検査件数、ZIPのSHA-256、Git blob SHA、修復方法は[由来／再現性](round16/REPRODUCIBILITY_PROVENANCE_2026-11-16.md)に固定済み。元バイナリは変更しない。

その他の長い元報告／チェックコードは各`COMPLETE_SOURCE_AUDIT`／`SOURCE_BUNDLE`に抽出手順がある。全件再実行は再開時の目的が明確な場合に限る。

## 3. 識別子・基準

- **停止直前のGit main**：`7f1e609bd02ef7108554a1ab7a84b9a729606814`。次の停止整理PRのmergeでmain SHAが変わることは正常。基準本体の`main.tex`は`b299a04baefe1313eb61b010d478b28033a42fbf`。
- **2026-11-16先行研究マージPR**： [#131](https://github.com/growupkuriyama-hub/Papers/pull/131)（Astra R15）、[#132](https://github.com/growupkuriyama-hub/Papers/pull/132)（Astra R16）、[#133](https://github.com/growupkuriyama-hub/Papers/pull/133)（Fable R2）、[#134](https://github.com/growupkuriyama-hub/Papers/pull/134)（Fable R3 2系統）、[#135](https://github.com/growupkuriyama-hub/Papers/pull/135)（Fable最終追補）。
- **見分けるべき異なる意味のU**：`U₁`（二元半束の型付け／正式境界問題）、`U₂`（射影重複を持つ限定クラスの研究上界）、`U`（非可換欠損剛性に関する補助予想）。同一の対象ではない。
- **`δ`と`h`**：内部a付きの核について `h=δ+|κ|_a`、`δ`は総a数の欠損。外側a室は`N−h`。
- **全性質の基準**：good = ε-free / nondeleting / nonpermuting / nonmerging、reduced = reachable + productive、型は内容型`alph`または該当する有限半群への実際の写像。最短木の量化を変えない。

## 4. 保全ルール

研究の中断時点での追加監査・元ファイルは`reviews/`以下のまま残す。原稿の`main.tex`、日本語原稿、PDF、PAPER.yamlは実際の投稿を準備する別タスクでのみ変更する。元報告に誤記がある場合でも原ファイルは書き換えず、最新索引に訂正を記す。再開時に古い追補プロンプトをそのまま送って重複探索しない。

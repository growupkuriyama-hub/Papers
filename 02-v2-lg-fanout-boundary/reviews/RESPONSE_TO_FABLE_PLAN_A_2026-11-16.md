# Response to Fable referee review — Paper #2 Plan A (2026-11-16)

**Review source:** `paper02_planA_claude_referee_2026-11-16.zip`, `REFEREE_REPORT.md`, Claude/Fable 5.2, dated 2026-11-16. 
**Frozen reviewed commit:** `608d9279390f59d94059684bd55a557a9aa7c3f4`.
**Response branch:** `paper2/fable-referee-revisions-2026-11-16`.
**Change request:** [PR #138](https://github.com/growupkuriyama-hub/Papers/pull/138), against `main`.
**Status:** Draft revision; not author-approved, not submitted or independently proof-verified. The code changes were made after the report. This response log records what was changed rather than treating any AI review as mathematical certification.

## Major points

| Referee point | Response | Files |
| --- | --- | --- |
| MAJOR 1, companion CFG overlap | Explain companion's fan-out-one `LI ∨ Grp` sufficient condition, distinguish different grammar/thickness regime, identify new all-fixed-fan-out full-`LG` scope; cite `kuriyamaCFG` and Costa–Nogueira–Teixeira 2021. | EN and JP introductory paragraphs |
| MAJOR 2, prior MCFG preprint | Cite arXiv:2605.11644v3 with bibliographic key `KuriyamaMCFGpreprint`, acknowledge existing reconstruction and *conditional* polynomial data-length statements (exposure/single-spine), do **not** assert all polynomial bounds absent there. | EN and JP introduction and bibliography |
| MAJOR 3, motivating example/figure | Add good fan-out-two grammar for the non-CFL `1^m 2^n 3^m 4^n`, with first/last-letter locally trivial typing and class-membership argument; add schematic two-row reversed interleaving-block TikZ figure. This demonstrates non-CFL coverage, **not** a strict `LG` versus `LI ∨ Grp` separation. | EN and JP introduction |

## Minor points

| Referee point | Response |
| --- | --- |
| m1 | Remove `τ`, `μ_m` from preliminary definitions and unsupported exponential-`t_typ` sentence; soften the conclusion's unsupported necessity language |
| m2 | State reduced/good/fan-out/rank assumptions at the beginning of the shortening section |
| m3 | Explain why `D_L` equals `D_{L∩Σ+}` for admissible contexts filled with nonempty tuples |
| m4 | Define pair representation size `‖G‖+1`, `t_G`-thickness and empty-grammar convention; clarify the syntactic representation class `R` versus target class |
| m5 | Replace 'by ideality' for `K⊆S^k` with the argument `K=K^k⊆S^k` for completely simple `K` |
| m6 | Introduce `lem:lg-unconditional-shortening` (prior to the local-group type-shortest lemma), migrate the shortening construction into its proof, and rederive both shorter-representative results from it rather than a proof fragment |
| m7 | Credit Yoshinaka 2011 §2.3 for the linear-size normalization claim; retain the derivation of the bound |
| m8 | Remove thirteen unreferenced bibliographic entries; preserve the verified companion arXiv v5 reference, and add the two directly relevant cited works |
| Further clarity | Replace undefined `|Σ|^{<2k}` by an explicit finite sum; put all new figures, lemmas and text in both languages |

## Mathematical integrity & verification

- The theorem/lemma **statements** for `thm:A`, `thm:local-group-polydata`, `lem:lg-buffered-owners`, `lem:block-replacement`, `cor:lg-type-level-shortest` and `cor:iptd` were checked against the frozen source and are unchanged.
- The **proof organization**, literature positioning, example and one standalone lemma *were changed*. The extracted lemma merits independent rereading and cannot be certified solely by compilation.
- Static source scan reports no missing internal references, no missing cited bibliography keys, no duplicate labels, balanced checked LaTeX theorem/proof/figure environments; EN labels are all present in JP. One historical JP-only label is retained.
- Historical `tools/check_port.py` recognizes new label `lem:lg-unconditional-shortening` and figure `fig:interleaved-blocks` under its `NEW` registry, without altering the frozen v1/Plan-A archives.
- Rebuild EN `pdfLaTeX`, JP `LuaLaTeX` from the PR branch and visually inspect the resulting PDF before merging. CI status should be recorded from the successful workflow rather than assumed.

## Publication boundaries

This revision **does not** restore Theorems B/C, converse or pseudovariety boundary claims, fan-out-two nonlifting or lower bounds. All removed full sources remain preserved in `parked/planA_2026-11-16/`. The fan-out-two necessity question is still open and paused. Do not infer that a Major-Revision recommendation guarantees acceptance, and do not submit a stale fixed-path PDF.

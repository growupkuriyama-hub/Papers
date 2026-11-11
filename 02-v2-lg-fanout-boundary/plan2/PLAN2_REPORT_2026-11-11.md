# #2 MCFG — Plan 2 editorial compression report

**Date:** 2026-11-11 JST  
**Source:** Plan 1 English 45-page core on `paper02-plan1-core-split-2026-11-11`; Plan 1 Japanese 52-page historical baseline.  
**Working branch:** `paper02-plan2-editorial-2026-11-11`, stacked draft PR #104 against Plan1 PR #103.  
**Target:** English 40–42 pages without discarding proofs of Theorems A/B/C.  
**Actual English result:** **42 pages**, pdfLaTeX 2026 CI verified.  
**Actual Japanese result:** **49 pages**, LuaLaTeX 2026 CI verified (the separate display alignment adjustment has been committed; final verification run must be checked).

## Editorial changes

English `main.tex`: shortened from **212,402 characters / 3,890 lines** (Plan1) to **199,549 characters / 3,720 lines** (Plan2).

- Introduction: condensed setting, background, relation to prior work, approach and organization; compressed the ten-row companion comparison to five rows while keeping the novelty/credit distinctions and no-dependency statement.
- Preliminaries: reduced a redundant symbols table to a notation paragraph (symbols still defined where used).
- Reconstruction: replaced a duplicate four-row prior-results comparison with a precise acknowledgement and direct appendix references.
- Characteristic data: consolidated an explanatory three-step roadmap into one paragraph, while retaining the formal proof-bearing material.
- Appendix A: condensed its roadmap table to a paragraph citing the same chain of technical lemmas. **The block-family definition remains untouched**.
- Introduction and conclusion: removed repeated summaries of A/B/C, typed-class separation and fan-out-two boundary; scope table retains all parameter/rank/alphabet restrictions, with its duplicate open-problem row removed.
- None of the steps hides an original proof or changes the value of a theorem.

Japanese `japanese/main_JP.tex`: shortened from **162,018 characters / 3,948 lines** to **155,579 characters / 3,815 lines**. The corresponding narrative sections and introductory tables were revised in Japanese. A single displayed inequality in `lem:marked-heavy-window-group` was reflowed as a two-line `aligned` display; the mathematical formula remains the same. Compared to English, the Japanese Plan1 baseline retains three pre-existing explanatory statement labels not in the English Plan1 branch; a strict bijective EN/JP statement-by-statement review is still recommended.

## Integrity checks (against Plan1 source)

| Check | English | Japanese |
|---|---|---|
| Main theorems A/B/C | exact same environments | exact same environments |
| Complete proof environments | all identical | all identical |
| Other theorem/lemma/proposition/corollary/definition/open-problem environments | all identical | identical except one *display layout* (aligned inequality in a lemma) |
| Missing LaTeX \ref / \eqref / \pageref / \autoref targets | 0 | 0 |
| Missing bibliography keys referenced by \cite | 0 | 0 |
| New/deleted mathematical proof blocks | 0 | 0 |

In the English version we compared the exact strings of **3 mainthm, 7 theorem, 31 lemma, 16 proposition, 4 corollary, 16 definition, 1 openproblem and 58 proof environments** against Plan1: all exact matches. This is stronger than checking only theorem labels.

The v1-to-v2 `tools/check_port.py` previously failed on Plan1 because `cor:typing-level-obstruction` and `prop:binary-u1-quadratic` were transferred from `main.tex` into a new parked file not enumerated by the checker. Plan2 updates `PKS` to include `parked/plan1_small_alphabet_2026-11-11.tex` and adds the two labels to PARKED. The GitHub CI now runs `python3 tools/check_port.py`; successful result (v1 140 labels, v2 128 labels, 29 parked labels from v1).

## CI runs and PDFs

- **English build:** [GitHub Actions run 43017965112](https://github.com/growupkuriyama-hub/Papers/actions/runs/43017965112), final pdfLaTeX: `Output written on main.pdf (42 pages, 852016 bytes)`; final pass had no undefined-reference, Overfull or Underfull warnings.
- **Japanese build (before display-reflow adjustment):** [run 43018494983](https://github.com/growupkuriyama-hub/Papers/actions/runs/43018494983), `Output written on main_JP.pdf (49 pages, 1142200 bytes)`. The one reported overfull display was 1.66905 pt; a subsequent commit changed only the display layout and triggered [run 43019020259](https://github.com/growupkuriyama-hub/Papers/actions/runs/43019020259).
- The tracked `main.pdf` and `japanese/main_JP.pdf` on the branch were inherited from the older source and **are not the verified Plan2 outputs**. Obtain up-to-date PDFs via the Actions artifacts (until expiration), not those tracked PDF paths.

## What is and is not validated

**Validated:** page count (42 EN / 49 JP before final alignment), CI builds, all exact proof blocks retained, all English formal statement blocks retained, no dangling cross-references or bibliography citations, v1 source coverage via updated port checker.

**Not certified:** independent proof-check of the mathematics, a full printed-page visual layout review, final bibliography priority check, or submission readiness. These require a separate referee-level check. Appendix H/J and other independent small-alphabet results remain intact in Plan1 parked sources; no source has been deleted.

**Merge policy:** stay a DRAFT stacked PR until the author reviews the distinction between Plan1 (selection of mathematical content) and Plan2 (proof-preserving editorial compression). Do not merge straight to `main`; merge Plan1 first if both are approved.

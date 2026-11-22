# #2研究MCFG — 02-v4-fixed-s-mcfg

**Research compendium of the fixed-s MCFG line (paper #2): multiple context-free languages under a fixed finite-semigroup typing.**
Created 2026-11-21 by merging the former folders `02-v2-lg-fanout-boundary/` and `02_fixed-h-mcfg/`.

| Path | Content |
|---|---|
| [`main.tex`](main.tex) / [`main.pdf`](main.pdf) | **Compendium (English, pdfLaTeX, 146 pp.)**: every result of v1 and v2 in one document, regardless of length |
| [`research/`](research/) | **live research ledger since the resumption of 2026-11-21**: one folder per round (prompt, original report, replay code and log, check note) |
| [`v2/`](v2/) | former `02-v2-lg-fanout-boundary/` (frozen): Plan A paper (EN 30 / JA 33 pp.), all parked sources, `reviews/` research archive, fan-out-two research stop-state |
| [`v1/`](v1/) | former `02_fixed-h-mcfg/` (frozen v1, arXiv:2605.11644; moved first to `02-v2-lg-fanout-boundary/archive-v1/` on 2026-10-31) |

The submission-oriented paper #2 is now [`../02-v3-cfg-typing-classification/`](../02-v3-cfg-typing-classification/) (fan-out one). Open Problem `op:fanout-two` (is **LG** the boundary at fan-out ≥ 2?) remains **OPEN**. Its research was paused on 2026-11-16 ([stop-state](v2/RESEARCH_PAUSED_2026-11-16.md)) and **resumed on 2026-11-21** ([ledger](research/README.md)); Rounds R1–R2 (Astra) proved no-go theorems for doubling-type families with one or several, stationary or level-dependent escapes, strictly containing the R12 search space, and refuted strict shortening; R3 isolated Conjecture IC on internal classes, which by `cor:distribution-representatives` would give a negative answer at fan-out two, and proved it under componentwise conservation laws (all read-through checked by Claude, not independently reconstructed). R4 (a separate Claude Opus 5.5 session) reduced IC to rare types over an enlarged alphabet, so that a negative answer at fan-out two is equivalent to the rare-type conjecture for all content typings (Result `rr:R4-equivalence`; depends on `prop:pattern-thickness-transfer`; independent audit pending). R5 generalized the intrusion reduction to all alphabets and root types and proved rigidity theorems in periodic frames (`sec:p4-resume-R5`). R6 removed the periodicity hypothesis (frame lemma; `sec:p4-resume-R6`); R7 showed that distinct Parikh differences do not protect a code (`sec:p4-resume-R7`); R8 excluded the periodic spine with level-uniform escapes for every code by a grammar-size lower bound (`sec:p4-resume-R8`); R9 lifted the bound to node-dependent escapes and, for the root type {a} with fan-out-one heavy nodes, to a quasi-polynomial bound for general grammars (`sec:p4-resume-R9`); R10 made the bound for {a} polynomial when forced heavy nodes are effectively of fan-out one, including context-free presentations (`sec:p4-resume-R10`); R11 removed crossings and exact fills for single-letter classes (`sec:p4-resume-R11`); R12 (classes with two or more letters besides a) is requested.

## Structure of `main.tex`

| Part | Content | Status |
|---|---|---|
| I. Main paper | fullest version of the v2 paper: Theorem A (LG upper bound `O(‖G‖²θ̄_G)` at every fan-out), Theorem B (linear factor), Theorem C (fan-out-one LG boundary), the U₁ classification and isolated letters at fan-out one, two-letter/semilattice results and the SL reduction at fan-out two, non-lifting, non-CFL separations, all appendices | complete proofs, not peer reviewed |
| II. Further results of v2 | everything parked on 2026-10-31, 11-06, 11-09: sandwich bound, undecidability of membership, unique words, full-content types, the S1 programme (S1 later solved), three-letter linear factor, constant weight, rank one, binary U₁ at fan-out two, unary cyclic typing, single words with two holes, comparison with multidimensional substitutability, bracketed-family substitutability, earlier proofs | complete proofs |
| III. Results of v1 | ic-slim parked results (2026-10-29), structural separations, the rare-type conjecture (M3), and the results of the pre-trim v82 (2026-10-18) that are in no later version (semilattice-indexed cosets, Yoshinaka 2015 embedding, early window-abelian / window-group / local-group appendices) | complete proofs (v1 notation) |
| IV. Fan-out-two research record | v1-era U₁ results, semilattices at fan-out two (2026-11-01–11), special-class upper bounds (Theorems S, P, L, L⊗′, U₂, Fable-C), the P_tree programme, the rounds after the 2026-11-21 resumption (`sec:p4-resume-*`), refuted claims, open questions, source index | **research results with verification status; not manuscript theorems** |

Precedence when a statement exists in several versions: Plan A `v2/main.tex` (2026-11-17) > 43-page v2 (2026-11-13) > 64-page v2 (2026-11-11) > parked v2 blocks > v1. Sections of Parts II–III begin with a provenance note; their text is verbatim except for section levels, label suffixes (`-foc`, `-cmp`, `-u1`, `-f2`, `-br5`, `-v1s`, `-v1r`, `-v82`) and notes marked *Compendium note*.

Coverage check (2026-11-21): every `\label` of the 22 source files listed below occurs in `main.tex` (possibly with a suffix); the compendium has 364 labels, builds with no errors, no undefined references or citations and no duplicate labels.

## Sources used

| Source | Git blob / ref |
|---|---|
| `v2/main.tex` (Plan A, 2026-11-17) | in this folder |
| `v2/parked/planA_2026-11-16/original_en_43pp.tex` (2026-11-13) | in this folder |
| v2 `main.tex`, 64 pages (2026-11-11) | blob `d7bb4f7d3c51d1a050d9f082e03726f342543621` |
| `v2/parked/2026-11-06_focus/removed_blocks.tex`, `2026-11-09_compress/removed_blocks.tex`, `parked_u1_typing_level.tex`, `parked_fanout2_and_comparison.tex`, `parked_from_v1.tex` | in this folder |
| `v1/parked/2026-10-29_ic-slim/parked_EN.tex`, `v1/revision/parked_structural_results_EN.tex`, `v1/revision/M3_rare_type_lower_bound_patch_2026-10-28.tex` | in this folder |
| v1 `main.tex` before ic-slim (commit `66897a1`, branch `archive/mcfg-pre-slim-full-20261029`) | blob `0d85734e83f723025cc2c9144262ad1741052c55` (bibliography entries and one remark) |
| v1 `main.tex` v82 and `appendix_window_abelian.tex`, `appendix_window_group.tex`, `appendix_local_group.tex` (branch `archive/mcfg-v82-pretrim-full-20261018`) | blobs `39576a71…`, `1d54516d…`, `ca7608a7…`, `3584b1fb…` |
| Part IV | `v2/reviews/` (ledgers, status files, audits), `v1/README.md`, `v1/revision/` |

v1 states older than v82 (2026-09-28 – 10-18, and the arXiv versions) were not mined separately: v82 was the cumulative full version at that time.

## Working rules

- `main.tex` is now the master and is edited directly (it is no longer generated).
- English only for now; there is no Japanese compendium yet. `v2/` and `v1/` keep their bilingual sources.
- `v1/` and `v2/` are frozen archives; do not delete parked material. New research goes to `research/` and is summarized in Part IV of `main.tex`.
- Research results enter Parts I–III only after an independent proof check and the author's decision.
- The PDF at the fixed URL is rebuilt by `.github/workflows/publish-02-v4-pdfs.yml` after a push to `main`.

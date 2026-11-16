# Paper #2: Plan A pruning archive (2026-11-16)

The initial Plan A editing branch keeps only the local-group upper bound as the principal research result. The source files in this directory are **byte-for-byte copies** of the English and Japanese source files on the main branch at the start of the work, prior to any removal. They are intentionally not compiled as part of the active paper.

- English original: 43 pages, source Git blob `b299a04baefe1313eb61b010d478b28033a42fbf`.
- Japanese original: 50 pages, source Git blob `8dfffaa23fd63a9ff0a6656df45b20bdb4c9fbc1`.
- Canonical starting points: `02-v2-lg-fanout-boundary/main.tex`, `japanese/main_JP.tex` as of November 13, 2026.
- Results to park, with proofs: Theorem B (all-fan-out linear lower bound), Theorem C (fan-out-one exact LG boundary, three-letter doubling family), non-context-free typing-regime separation propositions, and fan-out-two non-lifting theorem. Ancillary lemmas and appendices are preserved here as part of the complete original source. Existing `archive-v1/` and `parked/` are not overwritten.
- This is a submission **draft branch**, not a publication/retraction or a claim that the parked mathematics is incorrect.
- All-fan-out Theorem A and its needed mathematical support remain the focus of the active manuscript.

Reconstruction instructions: compare active `main.tex` with `original_en_43pp.tex` or use git history. Restore parked independent results selectively in later papers; do not silently combine the old fan-out-one lower bound with the fan-out-two positive result.

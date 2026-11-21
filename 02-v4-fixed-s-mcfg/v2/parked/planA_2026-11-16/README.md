# Paper #2: Plan A pruning archive (2026-11-16)

The initial Plan A editing branch keeps only the local-group upper bound as the principal research result. The source files in this directory are **byte-for-byte copies** of the English and Japanese source files on the main branch at the start of the work, prior to any removal. They are intentionally not compiled as part of the active paper.

- English original: 43 pages, source Git blob `b299a04baefe1313eb61b010d478b28033a42fbf`.
- Japanese original: 50 pages, source Git blob `8dfffaa23fd63a9ff0a6656df45b20bdb4c9fbc1`.
- Canonical starting points: `02-v4-fixed-s-mcfg/v2/main.tex`, `japanese/main_JP.tex` as of November 13, 2026.
- Results to park, with proofs: Theorem B (all-fan-out linear lower bound), Theorem C (fan-out-one exact LG boundary, three-letter doubling family), non-context-free typing-regime separation propositions, and fan-out-two non-lifting theorem. Ancillary lemmas and appendices are preserved here as part of the complete original source. Existing `../v1/` and `parked/` are not overwritten.
- This is a submission **draft branch**, not a publication/retraction or a claim that the parked mathematics is incorrect.
- All-fan-out Theorem A and its needed mathematical support remain the focus of the active manuscript.

Reconstruction instructions: compare active `main.tex` with `original_en_43pp.tex` or use git history. Restore parked independent results selectively in later papers; do not silently combine the old fan-out-one lower bound with the fan-out-two positive result.

## Earlier reviews of the parked Theorems B and C (all made on pre-Plan-A sources)

None of these reports audited the Plan A manuscript; each refers to the version named in its own header. The archived `original_en_43pp.tex` is the 2026-11-13 state, i.e. *after* the 2026-11-12 revisions listed below.

| Report | Version reviewed | Verdict on B / C (summary; read the report itself) | Author response |
| --- | --- | --- | --- |
| [Claude independent referee, 2026-11-12](../../reviews/claude_independent_referee_2026-11-12.md) | `main` 28b6abde, 42 EN / 49 JP pp (Plan2 core) | Simulated **Minor Revision**; no Critical/Major error; A, B, C, `thm:doubling-no-lift` and the non-CFL propositions judged to hold under the stated proofs | [RESPONSE_TO_CLAUDE_REFEREE_2026-11-12.md](../../reviews/RESPONSE_TO_CLAUDE_REFEREE_2026-11-12.md) (PR #106) |
| Post-structural independent review, 2026-11-12 (text supplied separately) | 96c32d9b, 43 EN / 50 JP pp | Simulated **Minor Revision** (0 Critical, 0 Major, 5 Minor, 6 Editorial) | [RESPONSE_TO_POST_STRUCTURAL_REFEREE_2026-11-12.md](../../reviews/RESPONSE_TO_POST_STRUCTURAL_REFEREE_2026-11-12.md) (PR #108) |
| Structural audit, 2026-11-12 (text supplied separately) | 39e5a46b, 43 EN / 50 JP pp | Redundancy and proof-check decisions | [STRUCTURAL_AUDIT_RESPONSE_2026-11-12.md](../../reviews/STRUCTURAL_AUDIT_RESPONSE_2026-11-12.md) (PR #107) |
| [Front-matter review, 2026-11-12](../../reviews/FRONT_MATTER_REVIEW_2026-11-12.md) | 7aed4c8, 43 EN / 51 JP pp | Wording and scope of the Theorem C statement (pseudovariety dichotomy, not a classification of individual typings) | same file (PR #109) |
| [ChatGPT full TCS referee, 2026-11-09](../../reviews/chatgpt_referee_full_2026-11-09.md) | 7ae4d819, 64-page expansion | **Major Revision** overall; Theorem C checked against the TeX proof and small exhaustive enumeration; scope issue on Theorem B's alphabet condition (later addressed) | — |
| [Astra A+A+ referee, 2026-11-08](../../reviews/astra_referee_aplus_2026-11-08.md) | 46-page A+A+ version | **Minor revision**; Theorem C as the fan-out-one benchmark judged consistent | — |

**Do not confuse** the paper's `thm:C` (fan-out-one LG boundary) with the research-only "Fable-C" theorem audited in [Fable_C_complete_independent_mathematical_audit_2026-11-15.md](../../reviews/Fable_C_complete_independent_mathematical_audit_2026-11-15.md); the latter belongs to the paused fan-out-two investigation.

Before restoring Theorem C (or B) to a submission, obtain a **new** independent audit of the restored text against the current Plan A manuscript, and decide how its fan-out-one content relates to the companion CFG paper under review at TCS.


# Paper #2 — CURRENT HANDOFF (as of 2026-11-12 JST)

> **Authoritative status for this repository.** This file supersedes the *current-state* portions of `HANDOFF_2026-11-01.md`, `HANDOFF_2026-11-02.md`, `HANDOFF_2026-11-04.md`, and older status notes in `INSTRUCTIONS_FOR_AI.md`. Those remain historical records, not the manuscript currently on `main`.

## Current manuscript

**Title:** *Distributional Learning of Multiple Context-Free Languages under Fixed Finite-Semigroup Typing: Local Groups and the Length of Characteristic Data*.  
**Target journal:** *Theoretical Computer Science* (not yet submitted; target timing noted in `PAPER.yaml`).  
**Canonical branch:** `main`. **English source:** [main.tex](main.tex) — **43 pages**. **Japanese source:** [japanese/main_JP.tex](japanese/main_JP.tex) — **51 pages**.  
**PDFs:** [English fixed URL](main.pdf) and [Japanese fixed URL](japanese/main_JP.pdf). The post-review sources passed [English CI](https://github.com/growupkuriyama-hub/Papers/actions/runs/43214327984) (43 pages) and [Japanese CI / port audit](https://github.com/growupkuriyama-hub/Papers/actions/runs/43214328041) (51 pages). The [fixed-URL publisher](https://github.com/growupkuriyama-hub/Papers/actions/runs/43214766355) successfully committed the PDFs (English 871,232 bytes; Japanese 1,155,729 bytes).

**2026-11-12 front-matter refinement (branch `paper02-front-matter-refinement-2026-11-12`, not yet merged):** Title kept. English/Japanese abstract, new keywords line and introduction rewritten for TCS submission (abstract 265→237 words, within the TCS 250-word limit; 6 keywords as TCS requires). The introduction now states why length rather than count, the known quantitative cases (Yoshinaka 2011 trivial typing; Yoshinaka 2008 windows at fan-out one), the one-factor gap between Theorems A and B, and the operator/Gold-learner distinction once. Theorem A/B/C content unchanged (B(i) and C(ii) now list exactly the operators of Proposition 6.1 and Theorem 7.3). English 43 pp, Japanese 50 pp locally; `tools/check_port.py` passes. Audit: [reviews/FRONT_MATTER_REVIEW_2026-11-12.md](reviews/FRONT_MATTER_REVIEW_2026-11-12.md). AI review, not an external opinion.

**2026-11-12 independent post-structural review ([PR #108](https://github.com/growupkuriyama-hub/Papers/pull/108) merged):** A fresh AI reviewer reported simulated Minor Revision (Critical 0, Major 0, Minor 5, Editorial 6). The [point-by-point response](reviews/RESPONSE_TO_POST_STRUCTURAL_REFEREE_2026-11-12.md) fixes parameter-scope wording, gives the complete short-type corollary shortening/epsilon-free/typed-thickness explanation in both languages, adds the pseudovariety qualifier, and corrects a notation typo. It keeps the stronger lambda-preserving lemma, all theorem labels, the scope table, and the parked research unchanged. This review is not an external journal opinion or human proof certification.

**2026-11-12 structural refinement:** [PR #107](https://github.com/growupkuriyama-hub/Papers/pull/107) merged. A1/A3(d)/A4/A7/A8/A10/A13/A14 remove strictly duplicated exposition in both languages; the scope table and mathematical remarks were retained. A new independent [s-type shortening corollary](main.tex) strengthens Theorem A to a coefficient depending only on f, r_max and |s(Sigma+)|, not alphabet cardinality. The original lambda-preserving lemma remains unchanged. [Structural audit response and deferred candidates](reviews/STRUCTURAL_AUDIT_RESPONSE_2026-11-12.md) records U1, G1-b and corrected G2-a separately; NONE of those candidates were inserted as established theorems. Fan-out-two learning boundary remains open.

**2026-11-12 referee revision:** [PR #106](https://github.com/growupkuriyama-hub/Papers/pull/106) incorporates the clarified \(t=u\) hypothesis, rank and worst-case qualifications, an explicit upper bound for the theorem-A proof constant, a direct LG-equivalence proof, and the corrected fan-out-uniform degree question. The Japanese Theorem C now matches the English quantitative exponential statement. The model referee report is archived [here](reviews/claude_independent_referee_2026-11-12.md), with the complete [response log](reviews/RESPONSE_TO_CLAUDE_REFEREE_2026-11-12.md). No parked results are reinserted; fan-out-two remains open. The referee's Minor Revision opinion is not an external journal decision.\n\nThe current manuscript is the result of **Plan1 (PR [#103](https://github.com/growupkuriyama-hub/Papers/pull/103)) + Plan2 (PR [#104](https://github.com/growupkuriyama-hub/Papers/pull/104))**, both merged into `main` on 2026-11-11. Main theorem statements and complete proofs were preserved in Plan2, which compressed supporting discussion and duplicated tables. [Plan1 report](plan1/PLAN1_REPORT_2026-11-11.md), [Plan2 report](plan2/PLAN2_REPORT_2026-11-11.md). The earlier Plan2-source CI checks were [English pdfLaTeX](https://github.com/growupkuriyama-hub/Papers/actions/runs/43019927350) and [Japanese LuaLaTeX / port-check](https://github.com/growupkuriyama-hub/Papers/actions/runs/43019927151). The earlier fixed-URL PDF publication completed in [workflow run 43021169918](https://github.com/growupkuriyama-hub/Papers/actions/runs/43021169918); it predates the referee revisions.

### Scope of *current* mathematical claims

- **Theorem A:** local-group typings give characteristic sample length `O(||G||^2 θ̄_G)` for every fixed fan-out, rank and typing; proof uses owner-wise simultaneous block shortening.
- **Theorem B:** a linear-factor lower bound `Ω(||G|| θ̄_G)` at every fan-out **under the alphabet side conditions stated in the theorem**, plus the exact trivial-typing benchmark.
- **Theorem C:** at **fan-out one**, and rank bound `r_max ≥ 2`, the pseudovariety boundary is precisely `LG`, with an exponential obstruction outside `LG`.
- Non-CFL fan-out-two examples distinguish local-group from window--group, and window--group from window--abelian, **for class coverage**, not the optimality of a particular proof technique.
- The three-letter exponential family does not lift to fan-out two under a fixed typing (`thm:doubling-no-lift`).
- **`op:fanout-two` remains open** for fan-out `f ≥ 2`. Do not claim that `LG` is a proven boundary at every fan-out.

These are summaries only: consult the actual current theorem statements in `main.tex` for all quantifiers, alphabet/rank restrictions and operator variants.

### Parked mathematical results (preserved; NOT part of this 43-page manuscript)

- [Small-alphabet results, English](parked/plan1_small_alphabet_2026-11-11.tex): isolated letters at fan-out one, individual `U_1` typings, two-letter content/semilattice typings, including the former Appendices H/I/J with their proof sources.
- [Small-alphabet results, Japanese](parked/plan1_small_alphabet_JP_2026-11-11.tex): Japanese source counterparts of the removed sections and former H/I/J.
- [Boundary extensions](parked/plan1_boundary_extensions_2026-11-11.tex): semilattice reductions / additional boundary investigations, including `prop:zeta-capacity`.
- Older `parked/` files and `archive-v1/` remain intact. The excerpts above are *source archives*, **not standalone compilable submissions**; do not put them back in `main.tex` without an explicit new editorial decision.

The Nov 9 historical assertions that `thm:two-letter-content` and `prop:zeta-capacity` are in the body of `main.tex` are **no longer current**. Their files are archived, not discarded.

### Research exploration versus submitted-paper content

Active work on `op:fanout-two` is kept under [reviews/](reviews/) and [the exploration status log](reviews/STATUS_sl_fanout2_2026-11-01.md). It contains findings and candidate arguments beyond the present paper. Its latest dated entries must be checked independently; **a research report being present does not mean its theorem has been inserted into the 43-page manuscript or independently verified.** Do not silently equate the research frontier with paper status.

### Validation and remaining tasks

- **Verified:** CI builds for English 43-page and Japanese 50-page manuscripts; published PDF bytes match the final 43-/51-page source build artifacts; Plan2 preserved full English formal theorem/lemma/proposition/definition/proof blocks verbatim relative to Plan1 (the subsequent referee fixes explicitly clarified some English/JP statements and added the self-contained LG characterization proof) (and Japanese proofs, apart from purely typographic math spacing), with no missing internal references or citation keys; `python3 tools/check_port.py` accounts for parked labels.
- **Not yet certified:** a human mathematical referee audit of the final *combined* manuscript, full PDF visual proofreading, complete English/Japanese claim-by-claim alignment, or journal submission acceptance. An additional AI-only independent review (simulated Minor Revision) and response are documented below; neither is a proof certificate. The historical Plan1/Plan2 reports capture narrower checks.
- **Next editorial priority:** human mathematical reading and author PDF inspection, not further indiscriminate compression; preserve all proofs and the separately archived mathematics.
- **AI assistants:** always fetch `main.tex` (and `japanese/main_JP.tex` if needed), this CURRENT handoff, `PAPER.yaml`, and then consult [README.md](README.md) for *historical* dated changelog entries. **Do not start from the 2026-11-06 41-page focus or the 2026-11-09 64-page expansion when asked for the latest.**

- **2026-11-12 post-structural independent-review corrections:** [PR #108](https://github.com/growupkuriyama-hub/Papers/pull/108) merged; **43 English / 51 Japanese pages**. Kept the fuller proof rather than trimming mathematical arguments to force pagination. [PDF publisher 43214766355](https://github.com/growupkuriyama-hub/Papers/actions/runs/43214766355) succeeded.

## Provenance

- 2026-11-08 A+A+ core: 46 pp (historical).
- 2026-11-09 expanded small-alphabet exploration: 64 pp (historical).
- 2026-11-11 Plan1 separation: 45 pp English; archived independent results.
- 2026-11-11 Plan2 exposition consolidation: **42 pp English / 49 pp Japanese**, merged and published.
- 2026-11-12: status/metadata synchronization only; mathematical `main.tex`, `japanese/main_JP.tex` and the parked proof fragments are not rewritten.

- **2026-11-12 (referee revisions):** Claude's Nov 12 independent report was checked against the live source, and issues m1--m9 and the newly discovered uniform-degree ambiguity m11 were addressed in both languages (see PR #106 and the response log). English PR CI 43 pages; Japanese PR CI 50 pages; historical Plan2 baseline stays 42/49 pages.

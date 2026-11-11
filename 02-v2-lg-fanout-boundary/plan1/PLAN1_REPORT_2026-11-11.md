# #2 MCFG — Plan 1: 46-page core restoration / independent-results split

**Date:** 2026-11-11 (JST)  
**Working branch:** `paper02-plan1-core-split-2026-11-11` (never edit `main` as part of Plan 1).  
**Baseline:** commit `22e101c4e3d848c660afe55fba980c12b82427ce`, 46-page English version after 2026-11-08 README (215), original Git blob `629939945aa9fa641eb1a7e4b2ca77d1031acc3d`.  
**Current 64-page source before split:** Git blob `d7bb4f7d3c51d1a050d9f082e03726f342543621` (2026-11-09 main.tex, with subsequent research-only commits).  
**Status:** Plan 1 *working candidate*: static checks completed, independent LaTeX/PDF build and mathematical re-audit still required. NOT submission-ready. Plan 2 NOT started.

## Decision and mathematical boundary

Retained in working `main.tex`:
- Theorem A (`thm:A`, `thm:local-group-polydata`): LG upper bound, all fixed fan-outs/ranks, and the simultaneous-shortening proof (including group/local-group appendices).
- Both non-CFL fan-out-two typing-regime separations (`prop:lg-needed-target`, `prop:nonabelian-needed-target`) and full proof appendix.
- Theorem B (`thm:B`, `prop:linear-factor-all-fanout`, `cor:trivial-exact`) and the full linear-factor appendix.
- Theorem C (`thm:C`, `thm:fanout-one-data`) and the three-letter doubling family with full parser proof.
- `thm:doubling-no-lift`, fan-out-two obstruction and `op:fanout-two`.
- Qualitative reconstruction, thickness and normalization apparatus as needed for A/B/C. These can be shortened in Plan 2 but their necessary proofs are not dropped.

Separated, **not discarded**, into `parked/plan1_small_alphabet_2026-11-11.tex`:
- Isolated-letter polynomial theorem and corollary (`thm:two-letter-fanout-one`, `cor:two-letter-fanout-one`), with former Appendix H.
- Individual `U_1` typing results (`cor:typing-level-obstruction`, `prop:binary-u1-quadratic`, `cor:u1-classification`), with former Appendix I.
- Binary content-typing polynomial theorem (`thm:two-letter-content`, `cor:two-letter-semilattice`), with former Appendix J.
- The semilattice reduction (`lem:typing-monotone`, `prop:sl-reduction`) is also preserved as a separate candidate; it does not depend on H/J but is not required by the 46-page core.

Additional 64-page conclusion material including `prop:zeta-capacity` is preserved in `parked/plan1_boundary_extensions_2026-11-11.tex`. The core proposal deliberately does not claim that the binary case or all individual `U_1` typings have been settled. The open problem remains genuinely open.

## Method of reconstruction

Compared full `main.tex` at both refs with paragraph-level LCS: 24 changed regions. Started from the original 46-page version, applied **selected** later edits that preserve A/B/C and their scope, while not reintroducing the independent small-alphabet results. This avoids blindly restoring stale surrounding discussion. In particular:
- Retained recent clarifications in Theorem C and the fan-out-one boundary theorem.
- Retained shortened explanations in the non-CFL separation and linear-factor discussion.
- Retained edits to the IPTtD corollary.
- Removed superseded standalone remarks/corollaries and redundant appendix tables without deleting proofs required by A/B/C.
- Kept the 46-page introduction, scope table and conclusion as the **consistent** baseline until Plan 2; no claims about H/J remain in this core candidate.

## Static verification (on the assembled candidate)

- Old English source: 4006 lines, 217251 characters, 131 labels.
- 64-page English source: 5478 lines, 303010 characters, 162 labels.
- Plan 1 draft: 3890 lines, 212402 characters, 128 labels.
- Duplicate label count: 0.
- Undefined \ref/\eqref/\pageref/\autoref targets: 0.
- Formula environments were checked for begin/end count; a real TeX build is still mandatory.
- The separate small-alphabet source fragment has 33 labels and 1437 lines (not standalone/compilable).
- No proof has been replaced with “omitted”; moved H/I/J proof source is preserved exactly as a nonincluded fragment.

## Risks / safeguards

1. **Build not yet run.** GitHub-source/static validation does not establish a PDF, page count, sound typesetting, bibliographic consistency or mathematical correctness. Run `latexmk -pdf main.tex`; inspect PDF and log. The branch's committed `main.pdf` still belongs to the 64-page version, hence it must not be treated as the Plan 1 PDF.
2. **Japanese source not yet synchronized.** `japanese/main_JP.tex` on this branch remains at the previous 73-page state; do not distribute as a bilingual matching release until translated and built.
3. **Proof check required:** independently read the retained 2026-11-08 corrected claims (including rank/representation scope), the 2026-11-09 clarifications, and new refactoring-induced transitions. Passing LaTeX does not certify a theorem.
4. A separate small-alphabet article is only a **candidate**, not an automatically viable submission: its \Sigma, typing, theorem statements, dependencies on the core paper, and complete original proofs need an independent introduction and bibliography.
5. If the semilattice reduction is to remain in the main paper, add its proof explicitly in a later revision (estimated ~1 page), and rework the open-problem paragraph. Do not cite a result placed only in a parked file as though proved in the core.

## Plan 2 entry criteria

After English TeX build + reference review + Japanese version synchronization (and independent math review), shorten the core by common-counting lemmas, eliminating duplicate qualitative learning explanations, and consolidating introduction/scope/conclusion. Target 40–42 typeset pages **without removing any proofs of A/B/C**.

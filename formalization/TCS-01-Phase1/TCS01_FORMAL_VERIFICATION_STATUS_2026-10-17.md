# TCS paper 01: Lean formalization status and resumption handoff (2026-10-17)

## 0. Scope and source-of-truth

Paper: *Distributional Learning of Context-Free Languages under Fixed Finite-Monoid Typing*, TCS-D-26-00494.

Public repository: https://github.com/growupkuriyama-hub/Papers

Canonical paper source: 01_fixed-h-cfg/main.tex; PAPER.yaml on main currently reports internal v227 (main SHA observed on 2026-10-17: 083f2ff84198f905aa599c54ff9cc62b3aa1b93e). Later source edits must be checked before asserting an exact manuscript-to-proof match.

Most complete proof branch: formalization/tcs-phase5b-canonical-witnesses-20261017; **known complete Lean-code-and-documentation baseline before this handoff**: bdba053849ee7f5c6ab721cfb4e4b5e225497b0d.

**Evidence**: GitHub Actions https://github.com/growupkuriyama-hub/Papers/actions/runs/39036182063, job 117406294087, conclusion SUCCESS at that exact baseline SHA: Lean 4.24.0 / Mathlib v4.24.0, Lake 7,448 jobs, 49 modules directly checked, end-of-job message "Phase 1-5B modules compiled and audited." Printed axioms for the key proofs are standard Lean principles only ([propext, Classical.choice, Quot.sound], with subsets as applicable); no sorryAx. The results below are derived from the GitHub theorem files, their proof reports, and the final successful CI log, *not* a claim that the entire paper is kernel-verified.

**Protect** paper source, Japanese manuscript, response-to-reviewers, PDFs, PAPER.yaml, prior Phase 1-5B theorem sources, and main. This status report is not a paper revision, submission, or arXiv upload. Do not merge or submit without author approval.

## 1. Kernel-verified theorem clusters

| Phase | Proof content | Precise scope / caveat |
|---|---|---|
| 1 | Abstract set-driven characteristic-sample lower bound and distinguishing-pair principle | General operator result requires characteristic-sample hypotheses for both targets; not an assumption-free existence theorem for arbitrary operators. |
| 2 | Concrete bracketed language L_n: derivation/enumeration correspondence; witness w_n*, length 3*2^n-2; unique h_U-type-one witness; punctured language L_n^-; quantitative abstract lower-bound bridge | Specialized grammar and U1 type; old conditional Clark-Eyraud bridge subsequently discharged in Phase 3C. |
| 3, 3B, 3C | Appendix C stack parser, reversibility and recognition; subtree exchange, branch synchronization, path congruence, unconditional Clark–Eyraud substitutability of L_n; typed substitutability of L_n^- | Key theorems include TCSPhase3.language_clark_eyraud and TCSPhase3.languageMinus_typed. Formal CFL-class membership predicate itself not uniformly encoded. |
| 4 | General finite SSBNF model for the five-symbol bracket alphabet; real typed derivations, trimming, finite typed-rule refinement and operational reachability equivalence; shortest typed yield and arbitrary-presentation typed-thickness exponential lower bound | TCSPhase4.intrinsic_typed_thickness_lower_bound_all holds for ALL finite SSBNF presentations generating L_n, with no size/reducedness bound; fixed h_U, not an arbitrary typing theorem. |
| 5A | General sample-based reconstruction with **actual finite** B/U/L/S rule sets, observed contiguous factors, independent derivations, soundness invariant, sample consistency, sample monotonicity, and concrete witness exclusion for Rec_{h_U} on L_n | TCSPhase5.rec_soundness, rec_sample_consistency, rec_monotone, rec_witness_exclusion. Generic logical proofs quantify over arbitrary alphabet and monoid homomorphism; finite-rule construction assumes finite alphabet. |
| 5B | General finite SSBNF (arbitrary alphabet and finite monoid); independent typed lifting, successful-tree trimming, finite typed productions and derivation equivalence; least-length yield and least-total-length reaching context; four-family literal Finset positive witnesses; U/B/L simulation; completeness, exact reconstruction, and characteristic-sample existence for the **actual Phase 5A Rec_h** | TCSPhase5B.rec_complete_from_positive_witnesses, rec_exact_reconstruction, canonical_witnesses_characteristic, rec_characteristic_sample_exists, finite_typed_grammar_language_eq, finite_rec_complete_from_positive_witnesses. The selected witnesses have minimum lengths but **NOT manuscript shortlex tie-breaking** among equal-length candidates. This distinction is the only stated difference from the literal canonical choices in equation eq:W, not a gap in the characteristic-sample existence result. |

Relevant Phase-5B files: TCSPhase5BGeneralSSBNF.lean, TCSPhase5BTypedRefinement.lean, TCSPhase5BRetained.lean, TCSPhase5BChoices.lean, TCSPhase5BFiniteTyped.lean, TCSPhase5BFiniteDerivation.lean, TCSPhase5BWitnesses.lean, TCSPhase5BRuleSimulation.lean, TCSPhase5BCompleteness.lean, TCSPhase5BCharacteristic.lean, TCSPhase5BMain.lean.

Detailed primary audit: PHASE5B_README.md and PHASE5B_VERIFICATION_REPORT.md in this directory, and analogous reports for prior phases.

## 2. Manuscript-to-Lean coverage: what is and is not complete

**Verified mathematical reconstruction core:**
- lem:sample-consistency and thm:soundness;
- prop:typed-core's typed lifting / retained typed symbol language (with actual finite grammar correspondence);
- thm:complete and thm:reconstruction-fixed-h for an explicitly constructed shortest-length-choice witness Finset;
- *existence* of a finite characteristic sample via the original Phase 1 Characteristic predicate, for target languages presented by general finite SSBNF grammars and satisfying fixed-h substitutability;
- Appendix C / L_n CE proof, Proposition 6.3(iii)'s actual Rec_h witness exclusion, conditional operator-distinguishing argument of Proposition 6.3(iv), and Corollary 6.4's representation-independent typed-thickness lower bound.

**Not yet independently established in Lean, or only partly covered:**
- exact shortlex tie-break defining the literal manuscript omega(X), chi(X) and eq:W (the current generic witness theorem is nevertheless sufficient for existence);
- lemma lem:typed-thickness-bound: quantitative bound on terminal reaching context lengths, on each witness word, and on the ENCODED SIZE of the witness Finset;
- cor:typed-thickness-data and quantitative clauses of thm:main(iv)-(v);
- cor:ilt: the conservative sequential Gold learner's convergence and at-most-one-change-after-characteristic-data guarantee;
- thm:poly-build: explicit O(n_K^4) finite grammar construction (mathematical finiteness is proved, algorithmic time complexity is not);
- prop:thick-ssbnf-normal (arbitrary CFG to SSBNF normalization algorithm and quantitative guarantees), lem:window-typed-yield, thm:window-thick, locally-trivial/group algebra, lem:li-group-factor, cor:li-thickness;
- prop:linear-normal, lem:linear-short, thm:linear-poly, and linear normal-form cost guarantees;
- Proposition 6.3(ii)'s particular small F_n and its exact encoded size 3n^2+4n+2, including concrete small-sample characteristic proof. Abstract h_0 characteristic existence is covered by Phase 5B only once a suitable SSBNF presentation is provided; the *specific* polynomial estimate is not proved by that fact alone;
- other separated language examples (e.g. CTR, Dyck, nonlinear example), regular/finite-window classification, and general CFG/CFL-class presentation abstractions.
- The entire TCS manuscript is NOT machine checked. Successful CI verifies the declarations that have been encoded, not unencoded mathematical assertions.

**Main theorem thm:main (v227):**
(i) consistency YES, polynomial construction NO;
(ii) characteristic-sample existence YES for the SSBNF presentation setting, arbitrary-CFG normalization bridge not Lean-verified;
(iii) Gold convergence and per-update polynomial bound NO;
(iv) locally-trivial/group quantitative polynomial data NO;
(v) linear subclass polynomial data NO.

No mathematical counterexample was found by this audit; that does not establish correctness of all unformalized claims.

## 3. Best next target: quantitative characteristic-data bound

Prioritize the exact non-algorithmic counting lemma lem:typed-thickness-bound, **using the existing Phase 5B PositiveWitnesses**, not reconstructing the entire grammar or its soundness/completeness.

Notation: N = number of original non-start NTs, Nt = cardinality of retained typed symbols, m = |M|, Pter/Pbin = terminal/binary rule counts, tau = max({shortest yield length of each retained typed symbol} union {1}), encodedSize W = sum over DISTINCT sample words (length+1).

The manuscript requires:
  contextLength(X) <= (Nt - 1) * tau
  each witness length <= (Nt + 1) * tau
  encodedSize(PositiveWitnesses) <=
    (N*m + |Pter| + |Pbin|*m*m + 1) * ((N*m + 1)*tau + 1).

The bounds apply to the Phase 5B *minimum-length choices* even with unspecified shortlex tie-break. Prove graph path shortening or an equivalent successful-context compression: any retained X admits a cycle-free path from a typed start child, with <= Nt-1 edges; sibling canonical yields along this path each have length <= tau. Since chosenContext has globally MINIMAL total length, its length is <= that constructed context. Then bound four witness families individually; use Finset cardinal/image/union bounds rather than pretending images are disjoint. Handle empty language, epsilon-only target, Nt=0, saturated Nat subtraction, and zero-size edge cases carefully. Prove actual cardinality inequalities: Nt <= N*m, terminal rules <= |Pter|, typed binary rules <= |Pbin|*m*m, epsilon family <= 1. Derive the exact bound above, then combine with the EXISTING Phase 5B characteristic predicate to certify cor:typed-thickness-data's quantitative core.

A full executable algorithm, CFG normalization, and Gold convergence belong to separate phases. Do not promise them from a counting lemma.

**Suggested next branch**: formalization/tcs-phase6-typed-witness-bounds-20261017, BASED ON the latest audited Phase 5B branch commit (including this handoff). New Lean modules should extend/import the existing Phase5BMain and leave all earlier statements/files unchanged. Milestone order: type/symbol/cardinality definitions; existence of loop-free context path; length bounds; finite witness cardinalities; encoded size inequality; characteristic-data corollary; CI audit.

## 4. Operational discipline for continuation

1. Read PAPER.yaml and the latest main.tex at their CURRENT HEAD. Use theorem labels, not outdated line numbers; v227 is the status at this report's creation, not a permanent assumption.
2. Read this report, PHASE5B_README.md, PHASE5B_VERIFICATION_REPORT.md and TCSPhase5BMain.lean/Choices/Retained/FiniteTyped/Witnesses/Characteristic. Check the exact Lean signatures before implementing anything.
3. Confirm the known full-green Phase5B run at https://github.com/growupkuriyama-hub/Papers/actions/runs/39036182063 and code state; do not redo old proofs.
4. Work in a SEPARATE formalization branch. Do not touch the submission branches or main. Commit only Lean module additions, dedicated CI and progress/audit docs.
5. Use Lean 4.24.0 / Mathlib v4.24.0; run lake build and directly compile all Lean modules; inspect #print axioms (permitted built-in logical axioms only) and run source / sorryAx checks. No custom axiom, opaque theorem, sorry, admit or weakened theorem.
6. Save complete mathematical interface and honest status to GitHub at milestones, including full successful CI run URL and matching commit SHA. Recheck the exact final documentation HEAD, not only a prior proof-code HEAD.
7. If implementation takes too long, commit all completed pieces, report precisely which theorems are kernel-verified and which goals remain. Do not spend an entire session repeatedly polling CI with no progress.
8. Do not edit TCS editorial-manager responses, PDFs, Japanese translation, journal submission, or arXiv.

## 5. Scientific evaluation

The *qualitative learning-theory core* (soundness, finite positive witness construction, completeness, exact reconstruction, characteristic sample existence) and the substantial exponential lower-bound/Appendix C results are kernel-checked. That is a major success, but it is NOT a numerical percentage of the manuscript. Quantitative bounds, Gold convergence, computational complexity, normalizations and much of the algebra/examples remain open as FORMALIZATION TASKS, not established counterexamples.

Phase 5B scientific verdict remains **B for literal manuscript canonicality**: genuine finite witness existence and completeness are verified, but the exact shortlex-determined representative words are not. This does not diminish the already-proved existential result.

# Formalization roadmap

Status meanings: ARCHIVED = historical upstream verification record; BOOTSTRAP = source written, build and statement audit pending; TODO = not formalized here; OPEN = unresolved mathematical question, not a proof task.

| Track | Target | Status |
|---|---|---|
| 01 | v88 CFG proof library, reconstruction, CYK, Gold convergence, bounds | ARCHIVED; imported, integration build pending |
| 01 | current manuscript, semigroup/fresh identity, BUNF and exact statement correspondence | TODO |
| Shared | polar operators and typed Galois connection (09 lem:typed-galois, partial) | BOOTSTRAP |
| Shared | semigroup evaluation, fresh empty value and observation refinement | BOOTSTRAP; extension monoid and multiplication proof TODO |
| 02 CFG | observation-relative substitutability | BOOTSTRAP |
| 02 CFG | LG upper bound and pseudovariety boundary; U1 typing classification; linear and quadratic lower bounds | TODO |
| 02 MCFG | arity-indexed syntax, named contexts, legacy working derivation semantics | BOOTSTRAP; copied historical foundation |
| 02 MCFG | all-fan-out LG results, thickness, characteristic data, regular-skeleton theorem and approved compendium results | TODO |
| 02 MCFG | op:fanout-two, research-only conjectures and partial bounds | OPEN / research ledger only; audit individually |
| 09 | individual typed frame/kernel generation | BOOTSTRAP |
| 09 | typed CFG refinement, closure-product identity, SPP and kernel reduction | TODO |
| 09 | strong/weak/very weak FCP/FKP, refinement inclusions and strictness, weak FCP counterexample | TODO |
| 09 | marked doubling family, one-word deletion, exponential kernel lower bound, Rec_s/MQ applications | TODO |

## First milestones

1. Make the full integration build green and commit lake-manifest.json; check declaration dependencies.
2. Define the exact fresh-identity semigroup extension and prove its relation to the historical 01 monoid observation. Align current 01 manuscript definitions and statements.
3. Share CFG derivation, normal forms, grammar size/thickness and characteristic-sample semantics between 01 and 02 CFG. Prove the fan-out-one correspondence to the MCFG layer rather than assuming it.
4. Port 09 typed Galois/closure-product/kernel-reduction lemmas and SPP semantics. Reuse 01's verified level-coded grammar family for the deletion construction after checking exact family equality.
5. Formalize 02 CFG LG and U1 results; then 02 MCFG core results and regular-skeleton classification with exact source labels.
6. Add executable examples and finite counterexample search, documented inputs, regression tests and a declaration index for future AI-assisted research.

For every port record: exact manuscript commit, label, declaration name, hypotheses, dependency list, proof/build status. Distinguish mathematical open questions from missing formalization.

## 09 phase 1 (2026-11-29)

Manuscript: Papers main commit fd3fe3ec18dfddd3478d13ea50b00caaee70fb07,
09 TeX blob c6ef28a9a53a3459e14da2648ae860383e4936bf (24 pages).
Baseline bootstrap CI run 46157134952 succeeded; new code needs its own build.

| Label | Shared declaration / remaining bridge |
|---|---|
| lem:clark | closure_product_subset, rhsSet_closure_subset (arbitrary mixed RHS) |
| lem:typed-galois | typed_polar_galois, typedClosure_extensive/mono/idempotent, typed_closed_iff_frames, typed_subset_closure_iff |
| lem:star | rhs_frames_insensitive |
| def:typed | freshMul, eval_append, rhsType, semigroup_ruleFiberConsistent |
| def:typed-props | individual category generation only; grammar-level hierarchy pending |
| lem:reduction | typed_kernel_reduction_semigroup (least-closed semantics); exact derivation bridge still to audit |
| lem:one-word | one_word_deletion_capture (general statement); concrete five-letter family pending |
| lem:capture | kernel_capture (local algebra); reaching-context/parse-tree occurrence bridge pending |
| thm:general-lower, thm:deletion, thm:frame-total | NOT formalized; need actual trees, minimality, splicing, coverage, counting |
| prop:duality and strictness, prop:learners, prop:ideal, cor:rec-data, cor:primal-data, prop:dual-refutation, total-length results | NOT formalized |

Important: the upstream v83 LevelTree family uses six letters and a different
shortcut constructor; it is not definitionally the five-letter family of 09.
Do not identify them. The common RHS and closure calculus is directly reusable.
No manuscript edits in this PR.

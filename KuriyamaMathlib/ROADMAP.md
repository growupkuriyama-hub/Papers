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

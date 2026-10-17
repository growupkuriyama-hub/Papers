# Phase 5B — Finite positive witness reconstruction

**Research paper:** *Distributional Learning of Context-Free Languages under Fixed Finite-Monoid Typing* (TCS-D-26-00494). Source of truth: `01_fixed-h-cfg/main.tex`, main HEAD `b7abdcf95d537a4f7ef364e387ec01ebd87d3e32`, PAPER.yaml **v225**, manuscript blob `7a3ed5ca1aaaf376a1e5104d12e08f59f424ab0d`, inspected on 2026-10-17.

**Work branch:** `formalization/tcs-phase5b-canonical-witnesses-20261017` from the immutable, CI-successful Phase 5A HEAD `013400b7e53f55209c1c7555ecbdd0c5e3c66ada`.

## Exact user-facing mathematical scope

The original `prop:typed-core` concerns *all* finite typed monoid morphisms, whereas Phase 4 used the particular five-terminal alphabet and `hU`. The new general modules parameterize arbitrary `Alphabet`, finite nonstart symbol type `NT`, finite monoid `M`, and a real homomorphism `h : List Alphabet →* M`. The start is external to `NT`.

`TCSPhase5BGeneralSSBNF.lean`: finite `startRules`, `startEmpty`, `terminalRules`, `binaryRules`; independent `DerivesFrom` and `StartDerives`.

`TCSPhase5BTypedRefinement.lean`: independent typed derivations with `A_{h(a)}→a` and `A_{μν}→B_μC_ν`, proving `typed_lifting` (actual tree induction).

`TCSPhase5BRetained.lean`: independent finite-tree reaching contexts `TypedContext` using productive siblings, semantic `RetainedTypedSymbol`, actual `TrimmedTypedDerives`, generic `trimmed_lifting`, `context_plug` and `retained_binary_children`.

`TCSPhase5BChoices.lean`: choose an **actual shortest-length** typed terminal yield and an **actual minimum-total-length** terminal reaching context using `Nat.find`, both with construction proofs. Start children have the empty context **by theorem**, not by assumption.

**Important canonicality distinction:** The selected minimum-length yield and minimum-length context here do **not yet implement the manuscript's shortlex tie-breaking**. They are *minimum representatives* and yield a potentially different finite witness `Finset` when ties occur. A characteristic-sample theorem for this witness set would be a stronger general-choice construction theorem, but is not a literal proof about the exact shortlex-determined `eq:W` set. This gap must not be suppressed in any final status report.

`TCSPhase5BFiniteTyped.lean`: real finite typed `Finset`s of symbols, start/terminal/binary rules. `TCSPhase5BFiniteDerivation.lean`: independent derivations from those finite collections; proof of correspondence to the semantic successful-tree trimming and start-language preservation.

`TCSPhase5BWitnesses.lean`: literal four-family finite witness set `PositiveWitnesses` from typed symbols, terminal rules, binary rules, and epsilon, and `positive_witnesses_subset_language`.

`TCSPhase5BRuleSimulation.lean`: direct sample-context `witness_unary` (actual U rule), terminal and binary rule simulations, and `canonical_symbol_reconstructs` by typed derivation induction. This is not defined by the sought completeness conclusion.

`TCSPhase5BCompleteness.lean`: generic `rec_complete_from_positive_witnesses`, with **only** `PositiveWitnesses G h ⊆ K` as sample premise. In particular the proof does not assume `K⊆L(G)` or target substitutability.

`TCSPhase5BCharacteristic.lean`: uses the fully verified **original Phase 5A `TCSPhase5.rec_soundness`** to derive `rec_exact_reconstruction` and the *actual Phase 1* `Characteristic` predicate. No extra soundness axiom is introduced.

`TCSPhase5BMain.lean` has direct `#print axioms` for all central theorem names.

## Submission-independent verification

The CI `.github/workflows/tcs-phase5b-lean.yml` installs Lean 4.24.0, resolves Mathlib tag v4.24.0, runs `lake build`, then `lake env lean` for **all 38 inherited sources and all new Phase 5B sources**. It scans source for forbidden proof tokens and checks no `sorryAx` occurs. Its complete results and code-SHA matching are recorded in [PHASE5B_VERIFICATION_REPORT.md](PHASE5B_VERIFICATION_REPORT.md). **Source files are not counted as proven until the actual CI succeeds.**

No existing Phase 1–5A proofs, the manuscript, PAPER.yaml, reviewer responses, PDFs, main, arXiv, or Editorial Manager have been edited.

## Not yet covered

Exact shortlex tie-breaking, an executable polynomial learner, Gold identification, arbitrary-CFG-to-SSBNF normalization, polynomial witness-size upper bounds, and full TCS manuscript verification are logically separate from the present witness-existence and completeness claims.

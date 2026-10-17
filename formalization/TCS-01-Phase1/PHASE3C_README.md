# Appendix C, Phase 3C — complete Lean 4 verification of the language-theoretic core

Research paper: Takayuki Kuriyama, *Distributional Learning of Context-Free Languages under Fixed Finite-Monoid Typing*, TCS-D-26-00494.

**Result:** The bounded bracketed grammar's `Language n` is Clark–Eyraud substitutable for every natural number `n`, and its genuine singleton-punctured `LanguageMinus n` is `hU`-typed substitutable. Branch synchronization and path congruence are proven as the crucial independent intermediate steps, not taken as mathematical assumptions.

## Provenance

- Authoritative paper source: `01_fixed-h-cfg/main.tex`, GitHub main HEAD inspected `97d5e57b24f13901c0164e9ce248f2eca8dc40a0`, file blob SHA `64c6db794e6438a71a706569621ae35038329541`, `PAPER.yaml` internal version **v217**.
- Base: complete Phase 3B branch commit `c94039d7482b8930b16515e77409fb7214b00737`.
- New branch: `formalization/tcs-phase3c-ce-proof-20261017`.
- Lean 4.24.0, Lake 5.0.0, Mathlib tag v4.24.0. `lake update` resolves Mathlib as in earlier phases; the repository does not track the generated manifest.
- Manuscript's parser rules, fixed finite-monoid target definitions, and selected Appendix C claims were verified against v217. No paper manuscript files or any earlier Lean theorem declarations were modified.

## Modules

- [TCSPhase3CAux.lean](TCSPhase3CAux.lean): two distinct initial one-letter moves, positive and additive stack weights, strict weight separation of remaining-prefix versus consumed-prefix, right cancellation of a shared stack suffix and classification of first-visit outcomes.
- [TCSPhase3CSynchronization.lean](TCSPhase3CSynchronization.lean): `opposite_branches_both_visit`, `oriented_branch_synchronization`, and final unconditional `branch_synchronization`, for words with different initial letters.
- [TCSPhase3CPathCongruence.lean](TCSPhase3CPathCongruence.lean): `language_word_nonempty` and `path_congruence` for *arbitrary* parser stack start and end points by strong induction on the **sum of input lengths**, with all decreases kernel checked.
- [TCSPhase3CClarkEyraud.lean](TCSPhase3CClarkEyraud.lean): `language_clark_eyraud` and unconditional `languageMinus_typed`. Also proves `punctured_language_finite` via `language_finite` from Phase 2. No residual CE premise.
- [TCSPhase3CMain.lean](TCSPhase3CMain.lean): aggregates the verified imports and prints the logical axiom dependencies of the central statements.
- [PHASE3C_VERIFICATION_REPORT.md](PHASE3C_VERIFICATION_REPORT.md): mathematical correspondence, CI evidence, source integrity and precise remaining proof boundaries.
- [GitHub Actions](../../.github/workflows/tcs-phase3c-lean.yml) (located at repository root): direct compilation of every source module and source/axiom scan.

## Exact main theorems

```lean
TCSPhase3.branch_synchronization
TCSPhase3.path_congruence (n : Nat)
TCSPhase3.language_clark_eyraud (n : Nat) :
    ClarkEyraud (TCSPhase2.Language n)
TCSPhase3.languageMinus_typed (n : Nat) :
    TypedSubstitutable hU (LanguageMinus n)
```

The synchronization lemma is stated for concrete starting words `c :: x`, `d :: y`, with `c ≠ d`, explicitly requiring both corresponding `Run bound` proofs. It constructs a single level `1 ≤ i ≤ bound`, a shared remainder stack `ψ`, complete `Language i` words `w,w'`, and suffix words with both remainder runs from `ψ` to the original endpoint. This is exactly the manuscript's different-first-letter hypothesis in a form convenient for pattern-matching.

`ClarkEyraud` is the **existing** Phase 2 definition that quantifies over two **nonempty words** and requires a shared accepting two-sided context, not a newly weakened definition. `LanguageMinus n` is the exact Phase 2 punctured target; `hU` is the existing finite monoid morphism.

**Complete final CI:** [GitHub Actions #39015571444](https://github.com/growupkuriyama-hub/Papers/actions/runs/39015571444) (job `117346885435`), proof commit **`8148fc2abc401e22f7525a70157baf21ab125fcd`**. All **7,388 jobs** passed; 19 Lean source files were directly compiled and audited, with no proof holes or user-defined mathematical postulates. Documentation-only commits follow that validated code SHA.

## Reproduction

```bash
cd formalization/TCS-01-Phase1
lake update
lake exe cache get
lean --version
lake --version
lake build
for f in TCSPhase1 TCSPhase2 TCSPhase2Bridge TCSPhase3Parser \
  TCSPhase3Recognition TCSPhase3Congruence TCSPhase3Prefix TCSPhase3Main \
  TCSPhase3Suffix TCSPhase3RecognitionConverse TCSPhase3Marker \
  TCSPhase3RecognitionFull TCSPhase3Subtree TCSPhase3BMain \
  TCSPhase3CAux TCSPhase3CSynchronization TCSPhase3CPathCongruence \
  TCSPhase3CClarkEyraud TCSPhase3CMain; do
  lake env lean "$f.lean"
done
```

CI also scans all Lean sources for disallowed proof-stub declarations and the `#print axioms` logs for `sorryAx`. Standard Lean logical principles (`propext`, `Classical.choice`, `Quot.sound`) are permitted.

## Formalization boundary

**Proved here:** finite language `Language n`; finite punctured language `LanguageMinus n`; `ClarkEyraud (Language n)`; `TypedSubstitutable hU (LanguageMinus n)`; the original grammar derivation relation and its reversible parser characterization; the two key appendix lemmas.

**Not claimed here:** full learning-class membership (`Ccf h0 ∩ Ccf hU`) under an independently formalized class definition, `Rec_h` grammar reconstruction, arbitrary SSBNF/presentation-independent lower bounds, numerical thickness or characteristic-sample existence for specific learning operators, or the entire TCS revision beyond the formally modeled definitions. Finiteness implies context-freeness mathematically, but that fact and the exact class predicates have not been encoded.

Main was not merged; Editorial Manager, arXiv, PDFs, source manuscripts and reviewer responses were not touched.

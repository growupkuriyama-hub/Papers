# TCS #1 Phase 8 — Executable reconstruction and cost verification

**Project:** *Distributional Learning of Context-Free Languages under Fixed Finite-Monoid Typing* (TCS-D-26-00494), theorem `thm:poly-build`.
**Toolchain:** Lean 4.24.0; Mathlib v4.24.0.
**Work branch:** `formalization/tcs-phase8-rec-poly-build-20261018` (NO merge to main).
**Paper provenance:** `main/01_fixed-h-cfg/PAPER.yaml` identifies **v227**. The Phase 8 work branch still contains the historical **v209** paper snapshot inherited from Phase 7. Neither was edited during this formalization.
**Phase 7 baseline:** `295d0f7d2142e60c832c6a10cb457eabebcf6d76`, CI [39080411807](https://github.com/growupkuriyama-hub/Papers/actions/runs/39080411807) success.

## Confirmed machine-checked milestone (candidate-count integration)

The dedicated Phase 8 CI succeeded at commit `ca2dfb80f7f90fcfe3c7167b5f2cd7a4ba8c83d7`, [run 39083766666](https://github.com/growupkuriyama-hub/Papers/actions/runs/39083766666), job `117545942780`. `lake build`, inherited regressions, direct module compilation, and axiom audits passed.

- `TCSPhase8Occurrences.lean`: exact nonempty occurrence enumeration and equality with `ObservedFactors`.
- `TCSPhase8Typing.lean`: recursive letter-table evaluation agrees with abstract `MonoidHom` when the table agrees on letters.
- `TCSPhase8BinaryEnumeration.lean`, `TCSPhase8UnaryEnumeration.lean`, `TCSPhase8StartLexical.lean`: exact (B)(U)(L)(S) rule equalities, including epsilon.
- `TCSPhase8ExecutableGrammar.lean`: `buildRecGrammar_eq_makeRecGrammar` proves six-field grammar equality without changing the Phase 5 mathematical specification.
- `TCSPhase8CandidateBounds.lean`: `enumerateOccurrences_card_le_square` proves `|O_K| <= n_K^2`.
- `TCSPhase8RuleCandidateBounds.lean`: `unary_candidate_pairs_card_le_cube` proves `|O_K × K| <= n_K^3`; `binary_rules_card_le_cubic` proves `|P_B| <= n_K^2(n_K+1)`.
- `TCSPhase8Main.lean`: `reconstruction_correct_and_candidate_bounds` integrates the above equalities and inequalities.

All certified theorems in this milestone depend only on ordinary logical axioms (`propext`, `Classical.choice`, `Quot.sound`); no `sorryAx`.

## Further work after this stable success

`TCSPhase8TypingCache.lean`, `TCSPhase8TypingCacheCorrectness.lean`, `TCSPhase8SampleTypeCache.lean`, `TCSPhase8Trie.lean`, and `TCSPhase8TrieCost.lean` provide new concrete List-based multiplication counting and bit-trie insertion accounting. **Kernel verified** at commit `b32a73f46a9979459d72d481df62d61366694ddd`, [Actions 39084750762](https://github.com/growupkuriyama-hub/Papers/actions/runs/39084750762), job `117548864944`: all five modules directly compiled, baseline `lake build` 7448 jobs and all inherited regression checks passed, and `#print axioms` found only standard logical axioms with no `sorryAx`.

The new type cache counts actual monoid-multiplication calls per extension and scans all suffixes. `cacheSampleTypes_finset_count_le_square` **proves** the exact finite-sample bound `n_K^2`; `cachedScan_sound_h` establishes typing soundness against the original homomorphism. The bit trie measures visits per inserted bit-string and offers a conditional `n^4` insertion theorem under cubic candidate count and linear encoded-key lengths.

**Unproved end-to-end O(n_K^4) assertion:** A cost-preserving bridge is still required from the actual (B)(U)(L)(S) rule-list enumerator to an injective bit encoding, the tested trie insertion sequence, the exact duplicate-free `RecGrammar`, and explicit costs for substring slicing, equality, encoding, output, and fixed-monoid table lookup. Neither `Finset` cardinality nor the conditional trie theorem alone establishes runtime. Do not claim the manuscript's full polynomial-time theorem is machine-verified.

No Phase 1–7 sources, Phase 5 specifications, English or Japanese manuscript, review response, `PAPER.yaml`, PDF, arXiv or Editorial Manager were changed.

## Phase 8 continuation: nine operational modules certified, List-object bridge

On 2026-10-18, the resumed session began at `7695e4e4c5a8299a85dd7b92dd43eb954b7f256f`. The original CI [39088202965](https://github.com/growupkuriyama-hub/Papers/actions/runs/39088202965) failed in the unary List membership proof and bit-trie empty-child cases.

**The nine new operational modules are now kernel-certified** at `a7d954f491d5c3ad72aaa61ee0360bf0f181ddee`: [successful dedicated CI 39099534325](https://github.com/growupkuriyama-hub/Papers/actions/runs/39099534325), job `117592776195`. The run completed `lake build`, inherited Phase 1–7 regression, every Phase 8 direct compilation, standard-logic-only `#print axioms`, and the forbidden-token audit without `sorryAx`. The new certified modules are `TCSPhase8CacheIndexing`, `TCSPhase8OccurrenceLists`, `TCSPhase8OccurrenceListCounts`, `TCSPhase8BinaryRuleLists`, `TCSPhase8UnaryRuleLists`, `TCSPhase8StartLexicalLists`, `TCSPhase8RuleListCounts`, `TCSPhase8TrieSemantics`, and `TCSPhase8RuleEncoding`.

The changes explicitly fix unary `Finset.mem_filter`/product witness nesting, Boolean-reflected membership conditions, empty-trie search contradictions, the unary-code successor recursion, and Nat bounds for raw candidate lists. The executable emitter now accepts an explicit List input, not non-executable `Finset.toList`.

**Further separate kernel-compiled proof at `b3456d4a5d30bf20301add5b1aa48946c1d67486`**: `TCSPhase8OperationalGrammar.lean` compiled directly in [run 39099850932](https://github.com/growupkuriyama-hub/Papers/actions/runs/39099850932); `buildListedRecGrammar_spec` and `buildListedRecGrammar_correct` establish six-field mathematical grammar equality for the set-valued projection of a concrete List emitter. Their reported dependencies are standard `propext`, `Classical.choice`, `Quot.sound`. `TCSPhase8TrieRuleBridge.lean` proves `contains_encoded_list_iff` for an *arbitrary injective* provided encoder, but its cost equation needed a minor function-composition simplification; repaired at `1189d70df661de6ba50ebb0e63243d3291e4ee3a`. A final-head success run for this extension must still be confirmed before marking its whole CI successful.

**Not yet proved:** an injective bit encoding of *all* tagged B/U/L/S/epsilon rules (the current encoder covers only Nat token lists), operational trie deduplication and final emission connected to `makeRecGrammar`, and explicit time charges for copies, equality, monoid tables, bit generation, trie enumeration, and output. The manuscript's total `O(n_K^4)` reconstruction cost is **NOT** kernel-verified. List-to-Finset projection is specification-level and is not treated as free runtime duplicate elimination.

No Phase 1–7 source, mathematical reconstruction definitions, TCS manuscript, Japanese version, referee response, PDF, or `PAPER.yaml` was edited. No main merge, arXiv, or submission action.


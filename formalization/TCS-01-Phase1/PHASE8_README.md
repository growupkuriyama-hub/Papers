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

## Operational List/trie extension (2026-10-18 continuation)

- Session starting commit: `834f041c85e35395724fc820c0f9a8020b79460e`, [final baseline success run 39085542717](https://github.com/growupkuriyama-hub/Papers/actions/runs/39085542717), job `117551182391`.
- New work (Phase 8 modules only): `TCSPhase8TrieSemantics.lean`, `TCSPhase8CacheIndexing.lean`, `TCSPhase8OccurrenceLists.lean`, `TCSPhase8OccurrenceListCounts.lean`, `TCSPhase8BinaryRuleLists.lean`, `TCSPhase8UnaryRuleLists.lean`, `TCSPhase8StartLexicalLists.lean`, `TCSPhase8RuleListCounts.lean`, `TCSPhase8RuleEncoding.lean`.
- Critical architecture correction: `Finset.toList` has no executable implementation in this project. The new operational enumerator therefore takes an explicit `List (List Alphabet)` sample; `List.toFinset` occurs in *specification theorems*, not in the runtime scanner. No noncomputable global CandidateWords scan is introduced.
- The new theorem statements address exact cache-index lookup, list-versus-Finset candidate equality, duplicate-tolerant *raw* candidate counts, bit-trie set invariants, and injective self-delimiting **numeric token-list** encoding. The generic token encoder is **not yet** an injective encoding of all (B)(U)(L)(S) production objects.
- **Gate:** new modules were committed as proof work-in-progress; do **not** label them machine-verified until a corresponding final-HEAD success run. Consolidated failure-collecting CI (still fails if any module fails) was pushed at `96d145597db4fb5ecc23bf6f1846708659e88057`, [run 39087920741](https://github.com/growupkuriyama-hub/Papers/actions/runs/39087920741); results require separate confirmation.
- **Unfinished:** complete rule-tag+word-boundary encoder with linear bit size, trie-to-rule decoding, operational grammar object equality, constant-time finite tables, substring and output charges, and an end-to-end Nat cost bound. `T_{Rec_h}(K)=O(n_K^4)` remains **unverified**.
- Only new Phase 8 Lean files, its Actions YAML, and these two report files were edited; protected proofs and manuscripts remain untouched.

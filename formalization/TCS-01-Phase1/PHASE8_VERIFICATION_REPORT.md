# Phase 8 verification and audit report

Date: 2026-10-18 (JST). Paper: `01_fixed-h-cfg/main.tex`, theorem `thm:poly-build`. Canonical main-branch `PAPER.yaml`: **v227**; Phase 8 branch contains historical v209 snapshot. No manuscript edits. Toolchain: Lean 4.24.0 / Mathlib v4.24.0.

## GitHub status

- Branch: `formalization/tcs-phase8-rec-poly-build-20261018`.
- Start HEAD for this resumed session: `35ea32406b6bae35f3451a64061d496a5a42ce87`.
- Candidate repair: `8ff487d07172caee9ce8c28495026c4ce20f51de`. Fixes `Finset.card_product` by explicit `×ˢ` coercion and correctly parentheses the constant term of a Finset sum.
- Integration: `TCSPhase8Main.lean` and workflow at `ca2dfb80f7f90fcfe3c7167b5f2cd7a4ba8c83d7`.
- **Success** [run 39083733863](https://github.com/growupkuriyama-hub/Papers/actions/runs/39083733863), job `117545845552`, repair proof.
- **Success** [run 39083766666](https://github.com/growupkuriyama-hub/Papers/actions/runs/39083766666), job `117545942780`, full Phase 8 integration.
- **Success** [run 39084750762](https://github.com/growupkuriyama-hub/Papers/actions/runs/39084750762), job `117548864944`, commit `b32a73f46a9979459d72d481df62d61366694ddd`: concrete cached typing and instrumented bit-trie; all direct modules, `lake build` (7448 jobs), inherited regression, standard axiom audit and no `sorryAx`.

## Kernel-checked theorems at the successful integration and cache/trie SHAs

- Occurrences: `mem_enumerateOccurrences_iff`, `efficient_observed_factors_eq`.
- Typing: `codeWord_eq_h`.
- Rules: `efficient_binary_rules_eq`, `efficient_unary_rules_eq`, `efficient_lexical_rules_eq`, `efficient_start_rules_eq`, `efficient_start_empty_eq`.
- Six-field object equality: `buildRecGrammar_eq_makeRecGrammar`.
- Explicit cardinality: `enumerateOccurrences_card_le_square` (`|O_K| ≤ n_K²`), `unary_candidate_pairs_card_le_cube` (`|O_K × K| ≤ n_K³`), `binary_rules_card_le_cubic` (`|P_B(K)| ≤ n_K²(n_K+1)`).
- Integrated: `reconstruction_correct_and_candidate_bounds`.
- Concrete type cache: `cachedScan_count`, `cachedScan_eq_scanl`, `cachedScan_sound_h`, `cacheAllStarts_count_le_square`, `cacheSampleTypes_count_le_square`, `cacheSampleTypes_finset_count_le_square`.
- Concrete trie cost: `BitTrie.insertCount_steps`, `BitTrie.insertCount_contains`, `BitTrie.insertManyCount_steps`, `BitTrie.insertManyCount_cost_le_fourth` (conditional on size of supplied bit encodings).
- `#print axioms`: only `propext`, `Classical.choice`, and `Quot.sound`. No `sorryAx` in success job logs. Baseline `lake build` 7448 jobs succeeded; inherited Phase 1–7 regression passed.

## Precise cost status (important)

1. Substring occurrence equality: **proved**, nonempty factor positions only.
2. Grammar field equality, including direct unary overlap: **proved**.
3. Occurrences ≤ `n_K²`: **proved**.
4. Unary candidate pair count ≤ `n_K³`: **proved**.
5. Binary rule-set cardinality ≤ `n_K²(n_K+1)`: **proved**; an explicitly instrumented *raw* binary iteration counter is still distinct.
6. Incremental typing cache multiplication count ≤ `n_K²`: **kernel-proved** as `cacheSampleTypes_finset_count_le_square`. The soundness theorem `cachedScan_sound_h` also compiled. A concrete constant-time finite-monoid multiplication/letter-lookup representation remains to be connected.
7. Duplicate elimination: `BitTrie.insertCount_steps`, `insertCount_contains`, `insertManyCount_steps` and the **conditional** `insertManyCount_cost_le_fourth` are kernel-verified. The key missing step is a rule-encoding/output equality bridge; no total grammar-construction bound follows.
8. All operations, including substring comparisons, encoding, duplicate removal, rule output: **NOT mechanized end-to-end**.
9. Manuscript `T_{Rec_h}(K)=O(n_K^4)`: **NOT verified**. Never interpret polynomial Finset cardinality as runtime.

## Remaining obligations

- Complete final-HEAD CI on the updated audit files without modifying old proof modules.
- Prove completeness and exact index-to-factor correspondence for the incremental typing cache, not merely that stored values match some prefix.
- Establish injective rule bit encodings of O(n_K) size for all six fields.
- Define an explicit List/Array-based emission of all grammar rule candidates; bridge this collection to the already-verified `buildRecGrammar`.
- Bridge emitted code list to the instrumented bit trie, preserve membership and no extraneous keys, account for output and final decoding.
- Cost string slicing, equality, typing-table lookup, and all scans; conclude an explicit total-cost Nat inequality, then the desired O(n_K^4).
- Verify unchanged Phase 1–7, manuscript, and protected files via SHA-based compare audit; avoid main merge.

## Judgment

**B confirmed at `b32a73f46a9979459d72d481df62d61366694ddd`**: grammar equality, candidate bounds, cached type-multiplication bounds, and conditional bit-trie insertion bounds are machine-verified; no end-to-end fourth-degree reconstruction runtime theorem. The post-report final HEAD must also pass its own CI.

## Phase 8 continuation: nine operational modules certified, List-object bridge

On 2026-10-18, the resumed session began at `7695e4e4c5a8299a85dd7b92dd43eb954b7f256f`. The original CI [39088202965](https://github.com/growupkuriyama-hub/Papers/actions/runs/39088202965) failed in the unary List membership proof and bit-trie empty-child cases.

**The nine new operational modules are now kernel-certified** at `a7d954f491d5c3ad72aaa61ee0360bf0f181ddee`: [successful dedicated CI 39099534325](https://github.com/growupkuriyama-hub/Papers/actions/runs/39099534325), job `117592776195`. The run completed `lake build`, inherited Phase 1–7 regression, every Phase 8 direct compilation, standard-logic-only `#print axioms`, and the forbidden-token audit without `sorryAx`. The new certified modules are `TCSPhase8CacheIndexing`, `TCSPhase8OccurrenceLists`, `TCSPhase8OccurrenceListCounts`, `TCSPhase8BinaryRuleLists`, `TCSPhase8UnaryRuleLists`, `TCSPhase8StartLexicalLists`, `TCSPhase8RuleListCounts`, `TCSPhase8TrieSemantics`, and `TCSPhase8RuleEncoding`.

The changes explicitly fix unary `Finset.mem_filter`/product witness nesting, Boolean-reflected membership conditions, empty-trie search contradictions, the unary-code successor recursion, and Nat bounds for raw candidate lists. The executable emitter now accepts an explicit List input, not non-executable `Finset.toList`.

**Further separate kernel-compiled proof at `b3456d4a5d30bf20301add5b1aa48946c1d67486`**: `TCSPhase8OperationalGrammar.lean` compiled directly in [run 39099850932](https://github.com/growupkuriyama-hub/Papers/actions/runs/39099850932); `buildListedRecGrammar_spec` and `buildListedRecGrammar_correct` establish six-field mathematical grammar equality for the set-valued projection of a concrete List emitter. Their reported dependencies are standard `propext`, `Classical.choice`, `Quot.sound`. `TCSPhase8TrieRuleBridge.lean` proves `contains_encoded_list_iff` for an *arbitrary injective* provided encoder, but its cost equation needed a minor function-composition simplification; repaired at `1189d70df661de6ba50ebb0e63243d3291e4ee3a`. A final-head success run for this extension must still be confirmed before marking its whole CI successful.

**Not yet proved:** an injective bit encoding of *all* tagged B/U/L/S/epsilon rules (the current encoder covers only Nat token lists), operational trie deduplication and final emission connected to `makeRecGrammar`, and explicit time charges for copies, equality, monoid tables, bit generation, trie enumeration, and output. The manuscript's total `O(n_K^4)` reconstruction cost is **NOT** kernel-verified. List-to-Finset projection is specification-level and is not treated as free runtime duplicate elimination.

No Phase 1–7 source, mathematical reconstruction definitions, TCS manuscript, Japanese version, referee response, PDF, or `PAPER.yaml` was edited. No main merge, arXiv, or submission action.



## Verified checkpoint — 2026-10-18, Actions 39112579231

This section **supersedes older 'Not yet proved' / 'Remaining obligations' statements above where they conflict**, without rewriting the historical audit. It records only results independently cross-checked against the successful GitHub Actions job and source code. The full end-to-end time theorem is still unverified.

### Source and CI provenance

- Branch: `formalization/tcs-phase8-rec-poly-build-20261018` (not main); verified source HEAD: `aad9fd6703a15da77d864cbbdfa3361fbcb4643e`.
- [GitHub Actions run 39112579231](https://github.com/growupkuriyama-hub/Papers/actions/runs/39112579231): **success**, job `117631639058`, on the precise SHA above.
- Environment: Lean 4.24.0 and Mathlib v4.24.0. Log reports `Build completed successfully (7448 jobs)` and `All inherited and new Phase 8 modules compiled, axioms audited`.
- Direct compilation includes `TCSPhase8ActualItemLength.lean`, `TCSPhase8TrieUniqueness.lean` and `TCSPhase8TrieExtractionUnique.lean`. The previous failure at SHA `72bd205b99b1a87b9340b7bc1a3be5557a9c5e7f` was repaired; the earlier failure is not the current status.
- In this success log, `#print axioms` for the principal theorems listed below reports only standard Lean logical axioms (`propext`, `Classical.choice`, `Quot.sound` as applicable), no `sorryAx`. The workflow's forbidden-token and inherited-phase checks passed. Compilation warnings about simplifier arguments remain nonfatal.
- Canonical paper source is **main** `01_fixed-h-cfg/main.tex`, with `PAPER.yaml` internal **v227** at time of check. The formalization branch has an older manuscript snapshot: do not use it to overwrite main.

### Kernel-verified results now available

1. **Concrete emitted grammar and exact specification:** `TCSPhase8.reconstructOperational_correct` relates the executable trie-deduplicated List output's six-field set projection to `TCSPhase5.makeRecGrammar h sample.toFinset`, assuming agreement between letter table and `h`. The earlier `buildListedRecGrammar_correct` supplies the List-to-mathematical-specification bridge.
2. **All six tagged item kinds and injective serialization:** `TCSPhase8.decodeRecItem_encodeRecItem`, `TCSPhase8.encodeRecItem_injective`; actual item count `TCSPhase8.emitAllRecItems_length_le` bounds raw candidates by `3 * (encodedListSample sample + 1)^3`.
3. **Source-derived length bound:** `TCSPhase8.observed_factor_length_le_encodedListSample` and `TCSPhase8.emitAllRecItems_letterCount_le` establish that each *actual emitted item* has at most `2 * (encodedListSample sample + 1)` source letters. This closes the previously conditional item-size premise.
4. **Unconditional quartic trie insertion-step bound for the actual stream:** `TCSPhase8.buildItemTrie_insertion_steps_fourth` proves
   
   `(buildItemTrie c t sample).2 <= (18 * tokenBound c + 3) * (encodedListSample sample + 1)^4`.
   
   **Scope:** counted trie **insertion** visits for the emitted keys; it is **not** a bound on the total runtime of `reconstructOperational`.
5. **No duplicates in actual emitted decoded items:** `TCSPhase8.BitTrie.dedupTrieKeys_nodup`, `TCSPhase8.dedupRecItems_encoded_keys`, and `TCSPhase8.dedupRecItems_nodup`. These prove List-level uniqueness, not just set equality.
6. Earlier successful phases: characteristic samples/completeness, Gold convergence, grammar reconstruction equality, nonempty factor enumeration, typing cache multiplication-count bounds, and raw candidate bounds are retained. This checkpoint does not claim to formalize every statement in the manuscript.

### Still NOT proved: whole-program O(n^4) reconstruction time

- The proof of `TCSPhase8.buildItemTrie_insertion_steps_fourth` does **not** count the `contains` lookups executed by `BitTrie.collectUniqueKeys`, nor the code construction/encoding/decoding/output stages.
- Missing end-to-end charges: substring extraction and copying, equality checks, cache build plus lookups, letter-numbering/finite-monoid table access, raw candidate generation, serialization, trie search, reverse/filterMap/decoder and six-field output. The actual List/data-structure representation must be linked to any cost model.
- An executable instrumented operational builder, a cost-preserving correspondence with `reconstructOperational`, and a proven explicit total-cost bound `C * (n+1)^4` remain outstanding. Avoid confusing the number of candidates, trie insertion visits, and full RAM-machine time.
- The existing source-level correctness, decoder round-trip, and insertion-step results are genuine kernel-checked milestones; do not discard or re-prove them unnecessarily.

### Resume point and safety boundary

The next isolated task is instrumenting `BitTrie.collectUniqueKeys` for **both lookup and insertion**, proving its result equals `dedupTrieKeys`, and bounding both costs using the verified encoded-key length theorem; after that, account for candidate construction, encoding, decoding, and output. Work only on the Phase 8 branch. **No main merge, manuscript/PAPER.yaml/reviewer-response modification, arXiv update, or submission action.**

### Status classification

**Phase 8: substantial partial success — mathematical output correctness, injective serialization, duplicate-free emitted items, and actual-stream trie insertion visit bound are verified. Entire `thm:poly-build` O(n^4) execution-time theorem: NOT verified.**

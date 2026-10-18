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


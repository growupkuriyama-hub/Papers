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

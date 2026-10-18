# Phase 8 verification and audit report

Date: 2026-10-18 (JST). Paper: `01_fixed-h-cfg/main.tex`, theorem `thm:poly-build`. Canonical main-branch `PAPER.yaml`: **v227**; Phase 8 branch contains historical v209 snapshot. No manuscript edits. Toolchain: Lean 4.24.0 / Mathlib v4.24.0.

## GitHub status

- Branch: `formalization/tcs-phase8-rec-poly-build-20261018`.
- Start HEAD for this resumed session: `35ea32406b6bae35f3451a64061d496a5a42ce87`.
- Candidate repair: `8ff487d07172caee9ce8c28495026c4ce20f51de`. Fixes `Finset.card_product` by explicit `×ˢ` coercion and correctly parentheses the constant term of a Finset sum.
- Integration: `TCSPhase8Main.lean` and workflow at `ca2dfb80f7f90fcfe3c7167b5f2cd7a4ba8c83d7`.
- **Success** [run 39083733863](https://github.com/growupkuriyama-hub/Papers/actions/runs/39083733863), job `117545845552`, repair proof.
- **Success** [run 39083766666](https://github.com/growupkuriyama-hub/Papers/actions/runs/39083766666), job `117545942780`, full Phase 8 integration.
- Later type-cache/trie implementation and cost lemmas: **verification ongoing**; consult the newest run's SHA, do not transfer success from older HEADs.

## Kernel-checked theorems at the successful integration SHA

- Occurrences: `mem_enumerateOccurrences_iff`, `efficient_observed_factors_eq`.
- Typing: `codeWord_eq_h`.
- Rules: `efficient_binary_rules_eq`, `efficient_unary_rules_eq`, `efficient_lexical_rules_eq`, `efficient_start_rules_eq`, `efficient_start_empty_eq`.
- Six-field object equality: `buildRecGrammar_eq_makeRecGrammar`.
- Explicit cardinality: `enumerateOccurrences_card_le_square` (`|O_K| ≤ n_K²`), `unary_candidate_pairs_card_le_cube` (`|O_K × K| ≤ n_K³`), `binary_rules_card_le_cubic` (`|P_B(K)| ≤ n_K²(n_K+1)`).
- Integrated: `reconstruction_correct_and_candidate_bounds`.
- `#print axioms`: only `propext`, `Classical.choice`, and `Quot.sound`. No `sorryAx` in success job logs. Baseline `lake build` 7448 jobs succeeded; inherited Phase 1–7 regression passed.

## Precise cost status (important)

1. Substring occurrence equality: **proved**, nonempty factor positions only.
2. Grammar field equality, including direct unary overlap: **proved**.
3. Occurrences ≤ `n_K²`: **proved**.
4. Unary candidate pair count ≤ `n_K³`: **proved**.
5. Binary rule-set cardinality ≤ `n_K²(n_K+1)`: **proved**; an explicitly instrumented *raw* binary iteration counter is still distinct.
6. Incremental typing cache multiplication count ≤ `n_K²`: code and theorem drafted in newly added modules; check subsequent CI and kernel axioms before upgrading status. Explicit constant-time finite monoid operation/table lookup remains to be connected.
7. Duplicate elimination: bit-trie insertion has an instrumented node-visit cost and a conditional fourth-power statement in new modules; compilation and the relationship to concrete grammar encodings remain outstanding.
8. All operations, including substring comparisons, encoding, duplicate removal, rule output: **NOT mechanized end-to-end**.
9. Manuscript `T_{Rec_h}(K)=O(n_K^4)`: **NOT verified**. Never interpret polynomial Finset cardinality as runtime.

## Remaining obligations

- Obtain green direct compile and axiom audits for each new typing-cache and trie module, plus final SHA.
- Prove completeness and exact index-to-factor correspondence for the incremental typing cache, not merely that stored values match some prefix.
- Establish injective rule bit encodings of O(n_K) size for all six fields.
- Define an explicit List/Array-based emission of all grammar rule candidates; bridge this collection to the already-verified `buildRecGrammar`.
- Bridge emitted code list to the instrumented bit trie, preserve membership and no extraneous keys, account for output and final decoding.
- Cost string slicing, equality, typing-table lookup, and all scans; conclude an explicit total-cost Nat inequality, then the desired O(n_K^4).
- Verify unchanged Phase 1–7, manuscript, and protected files via SHA-based compare audit; avoid main merge.

## Judgment

**B at the stable success SHA `ca2dfb80`**: complete finite-grammar equality and candidate cardinality bounds, but not end-to-end runtime. Latest HEAD retains an independent CI gate; do not assign it the successful baseline result before that run finishes.

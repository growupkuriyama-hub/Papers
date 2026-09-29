# v65 → v66 pre-submission review revision

## Purpose

v66 incorporates the concrete fixes arising from the Information and Computation pre-submission review and the independent Claude cross-check. The pass keeps the mathematical architecture unchanged while making the novelty boundary, notation, class membership, and terminology harder to misread.

## Changes

- Rewrote the abstract to foreground typed completeness and the rank-dependent characteristic-data results, while shortening the separation-example detail.
- Recast Contribution (1) around finite positive completeness under the type guard, rather than presenting the guard itself as the main novelty.
- Recast Contribution (3) around the higher-rank thickness theorem and moved the intrinsic-rank witness to a supporting role.
- Clarified the relation to Yoshinaka (2011): the observed-tuple architecture is prior work; the present technical contribution is completeness under finite typing and the resulting quantitative frontier.
- Prepared the companion fixed-h CFG citation for the corrected October arXiv release, arXiv:1409.6247v5.
- Defined “boundary typing” and “boundary-typed” explicitly, with the target-level term introduced only after the target class itself is defined.
- Removed or flattened one-off terminology such as “information-lossless”, “structural good form”, “rectangular-window condition”, “substitution rectangle”, “certified witnesses”, and “full-image property”.
- Renamed the manuscript’s nonterminal-thickness parameter from \(\tau_G\) to \(t_G\), matching Yoshinaka’s notation, while retaining Yoshinaka’s \(\tau_G\) for rule thickness in quoted comparisons.
- Replaced “Since \(h\) is given explicitly” by a reference to the finite-typing representation definition.
- Added the missing justification that the exponential singleton example lies in the typed target class, so the rank-two lower-bound paragraph is internally complete.
- Rephrased “primal objects” as “basic sample-derived objects”.

## Safety

- No main theorem, proposition, corollary, learning construction, or proof architecture was strengthened or weakened.
- Exact reconstruction, conservative TxtEx identification, polynomial bounded-rank updates, rank-one polynomial characteristic data, the boundary-typing theorem, and the separation theorems retain their previous statements.
- The singleton paragraph gains an explicit class-membership justification that was previously implicit.
- The arXiv v5 citation is intentional and refers to the corrected fixed-h CFG version planned for the October 2026 arXiv update.

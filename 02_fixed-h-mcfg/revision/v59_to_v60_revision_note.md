# v59 → v60 revision note

Date: 2026-09-29

## Purpose

Safe pre-submission compression pass.  The goal is to reduce reading load without reopening the mathematical core after the v58--v59 correctness and source audits.

## Changes

1. **Introduction compressed.**  The fixed-typing motivation, adjacent learning literature, prior-work positioning, and roadmap were shortened while retaining the four-item contribution list and the explicit Yoshinaka/companion-paper scope distinctions.
2. **Preliminaries lightly compressed.**  Explanatory prose around finite-state typings was shortened; formal definitions and notation were left intact.
3. **Higher-rank scope prose compressed.**  The boundary theorem and its proof are unchanged; repeated discussion after the proof was consolidated.
4. **Comparison section compressed.**  The introductory comparison with Yoshinaka, the same-typing-filter proof, the discussion after the fan-out-sensitive example, and the arbitrary-filter positioning were shortened.
5. **Secondary example removed.**  The unreferenced renamed-copy extension `L_phi={w phi(w)}` was removed.  The formal COPY proposition and its proof remain.
6. **J_s presentation shortened.**  The explicit grammar, typed-membership argument, and prefix--suffix separation rectangle remain; only the standard non-CFL closure argument and positioning prose were compressed.
7. **H_m and L_star protected.**  The strict fan-out hierarchy theorem, its Seki-based lower bound, its substitution rectangle, and the arbitrary-filter theorem/proof were not altered.
8. **Intrinsic-rank witness protected.**  The v59 Gallot/Bishop source bridge and the explicit modular-construction caveat remain unchanged.
9. **Conclusion compressed.**  Repeated result summaries were consolidated; the open problem remains unchanged.
10. **Appendix locator synchronized.**  The remaining Yoshinaka size locator now reads Section 2.3, after Example 2, matching the v59 source audit.

## Structural check

- Source lines: **3755 → 3613** (142 lines removed; about 3.8%).
- Theorem environments: **7 → 7**.
- Proposition environments: **16 → 16**.
- Lemma environments: **13 → 13**.
- Proof environments: **39 → 39**.
- No duplicate labels, unresolved internal references, or citation keys were detected by the static consistency check.
- The H_m Seki Lemma 3.3 step, Gallot Theorem 28 bridge, and modular intrinsic-witness qualification are all retained.

This pass intentionally does not compress the exact-reconstruction core, the characteristic-data theorem proofs, the H_m proof, the L_intr proof, or the L_star proof.

## Baseline hashes

- v59 `main.tex` SHA-256: `1fee043a6c0e748c917e7cc1811ffeb656ae7f74097a95fbbc5dc49510bc3a79`
- v60 `main.tex` SHA-256: `dcb6f34aaf5984dabc8426ba7dba22504b72f2ad394d5922eed29aeccaba9d31`

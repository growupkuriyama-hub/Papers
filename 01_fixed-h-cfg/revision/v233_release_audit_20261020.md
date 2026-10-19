# TCS-D-26-00494 — v233 approved revision (2026-10-20)

## Accepted changes
1. In English Appendix A.1 of `main.tex` and the exact submission Clean TeX, change `d:=|P|` to `d:=|\\mathrm{Prot}|`. The protected-position set is named `\\mathrm{Prot}`, whereas `P` denotes the grammar's productions. This is a notation repair only. The Japanese reference uses a separately declared local `P` and does not require a change.
2. Update README and `PAPER.yaml` release pointers to v233; English SHA-256: `fd385a01fde590703be46ff88b2799cdc8f129c07ea2c77abf38369871fd2c90`. No mathematical theorem, bound, proof, abstract, or reviewer-response claim is altered.

## Focused review carried forward
Reviewed Appendix A.1's window/group combinatorial shortening and Appendix C's reversible parser; no decisive counterexample identified (not a formal proof certificate). Compared Yoshinaka (2015, Theorem 1 and Lemma 3) with the manuscript and reviewer reply. Qualitative positive-only learning, polynomial update and witness *cardinality* are treated as prior work; new contribution centers on *encoded length* upper and lower bounds and algebraic scope.

## Publication boundary
v232 PDF/ZIP artifacts are not v233: build v233 Clean PDF, Marked PDF, response PDF, and exact three-file ZIP. Verify 49 reviewer items and 77 marked-PDF anchors before release. No TCS Editorial Manager or arXiv submission is performed. Work exclusively from `main` as the single canonical source.

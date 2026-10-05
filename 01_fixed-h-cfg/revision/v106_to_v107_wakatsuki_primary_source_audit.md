# v106 to v107: Wakatsuki--Tomita primary-source source audit (2026-10-05)

## Verified primary sources and exact locators

1. Wakatsuki & Tomita, 1992, Japanese *IEICE* J75-D-I(10):950–953, p. 951: defines the shortest accepting input for a stack string in the simple-DPDA equivalence procedure, calls its length **thickness**, and takes a maximum over stack symbols.
2. Wakatsuki & Tomita, 1993, *IEICE Transactions on Information and Systems* E76-D(10):1224–1233, **Definition 3.1 (p. 1226)**: `tau(alpha)=min{|w|: w in L(alpha)}` for reduced very simple DPDA configurations and `k_i=max{tau(A): A in Gamma_i}`; these are used in inclusion checking and complexity analysis. The 1993 paper was received from coauthor Mitsuo Wakatsuki on 2026-10-05.
3. Tajima, Tomita & Wakatsuki, 2000, E83-D(4):757–765, p. 757 (summary): learning from a representative sample *with membership and equivalence queries*. It is not evidence for an unconditional positive-text characteristic sample.

Original PDFs are kept privately in Research-Library as REF-09-12, REF-09-11, REF-09-15 respectively. We do not assert that Wakatsuki--Tomita originated the word *thickness*, since the absolute historical first use was not established in this source audit.

## Exact manuscript changes

- EN and JP: historic DPDA measure carefully distinguished from CFG nonterminal thickness in the Preliminaries.
- EN and JP: MAT/representative-sample model contrast added at the learning-definition boundary.
- EN and JP: three primary-source bibliography entries added, one translated Japanese title explicitly marked translated in English.
- **Unchanged:** `tau_G`, `tau_h^{typ}(G)`, all theorems, proofs, algorithm constructions, witness bounds and class-separation claims.

## Submission and version guard

- Baseline: v106; current source v107.
- Immutable pre-update EN, JP and PAPER metadata are archived at `archive/pre-wakatsuki-v106/`.
- `response/response_round1.tex` is deliberately unchanged. Its page/line locators may not match the v107 PDF; re-audit before journal submission. No v107 submission/approval is asserted here.
- Lean v88 theorem-facing baseline remains the same; this editorial change is not a new theorem/proof formalization.

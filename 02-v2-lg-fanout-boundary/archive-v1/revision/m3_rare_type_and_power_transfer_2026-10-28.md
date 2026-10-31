# M3 — rare-type lower bounds and the fan-out-two obstruction (2026-10-28)

## Editorial choice
The **English manuscript remains the submission master**, with `japanese/main_JP.tex` kept structurally synchronized. The M3 patch has been adopted selectively, with the two directions of the existing higher-fan-out open problem preserved.

## New statements
1. **Type deletion (`lem:type-deletion`):** deleting an entire positive typing fibre preserves `C^{mcf}_{f,s}`; removing epsilon also preserves it.
2. **Rare-type samples (`prop:rare-type`):** for each realised type `m`, every characteristic sample must contain a positive word of that type. The stronger lower bound is the **sum** of `mu_m(L)+1` over realised types, plus an epsilon term when the operator must distinguish `L` from `L\{epsilon}`. The epsilon term is asserted for the paper's canonical operators and class-wide set-driven operators, not for arbitrary partial-domain operators.
3. **Sandwich (`cor:typed-sandwich`):** for each reduced good presentation, the sum of minimal type-wise costs is bounded above by the existing typed-shortest-yield sample construction.
4. **Fan-out one (`rem:fanout-one-data`):** with rank two permitted, the precise *pseudovariety-level* necessary-and-sufficient condition for class-uniform polynomial sample length is `V ⊆ LG`. The exponential lower-bound family is **attributed to the companion CFG paper, Proposition 6.4**, which is publicly available in arXiv:1409.6247v5 (2026-10-22). The statement does **not** claim the negative conclusion for every particular non-LG typing on its original alphabet.
5. **Fan-out two (`lem:power-transfer`, `thm:doubling-no-lift`):** a two-hole common-context argument transfers periodic powers between nonempty components, proving that the companion bracketed-doubling family fails tuple substitutability for every fixed finite typing once n is sufficiently large. This is a non-membership result, not a sample-length lower bound.

## Retained boundaries
- The refinement-thickness dichotomy remains exact for LG at all fan-outs.
- The main independent noncommutative window–group and local-group upper-bound theorems remain intact.
- Both existing higher-fan-out directions remain open: a positive example of polynomial data outside LG, and an exponential/superpolynomial lower-bound example in the U1 class.
- Whether all realised types have polynomial-length shortest words at fan-out two is posed as a **question**, not established or claimed as a theorem.
- This patch does not reproduce or claim originality for the companion's exponential CFG family or the Clark–Eyraud substitutability proof.

## Checks
- Local English pdflatex: three successful passes, **44 pages**, no missing references or overfull boxes, inspected page 16 containing the sandwich formula.
- Exact revised English source blob SHA: `9051e138f9811b7ce5871459139e2f3487ba95e9`.
- English/Japanese label sequences: **129/129 identical**, theorem-like environment sequences **88/88 identical**, bibliography keys **39/39 identical**.
- Both source files await GitHub Actions' English/Japanese compilation for cross-platform confirmation.

These tests are mathematical spot audits and TeX checks, not formal machine verification of the pre-existing group-shortening lemmas.
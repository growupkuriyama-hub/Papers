# M5: fixed-typing motivation and group-valued agreement (2026-10-28)

This revision strengthens the mathematical motivation for the noncommutative window–group and local-group bounds in `main.tex`.

## Additions
- Proposition `prop:group-agreement` defines a single fixed window–`A × A` typing for all feature relations `R ⊆ A × A`, supplies fan-out-two/rank-two grammars, and proves that the agreement target is excluded from every window–abelian typing when `[A,A]` is not central. The proof uses equal Parikh vectors, a common accepting two-hole context, and a separating two-hole context.
- For `A = S_3` the group component is **`S_3 × S_3`**, not `S_3` alone. The separation is for the diagonal agreement target, **not for every member** of the feature-relation family.
- The existing strict inclusion `LI ∨ Grp ⊊ LG` is strengthened with a binary-alphabet example. The parity of the factor `ab` is not determined by a fixed prefix–suffix window and an arbitrary finite-group morphism; witness words are `b^K a^N b^K` and `b^{2K}` with suitable `K,N`.
- Introductory motivation and scope remark distinguish a **separation of fixed biases** from a **lower bound on characteristic-data length**, and distinguish arity-one counterexamples from the new arity-two witness.
- Independent window–group and local-group theorems, as well as the characteristic-data reduction through `t_typ`, remain unchanged.

## Validation
- The complete revised English `main.tex` was compiled three consecutive times using pdfLaTeX with `-halt-on-error -file-line-error`.
- Final output: 42 pages; no unresolved citations/references, duplicate labels, or overfull boxes. A few underfull-line warnings remain.
- The group-product identity for the `S_3` witness was separately checked by explicit permutation multiplication.
- Compilation and finite-example checks **do not** constitute formal verification of every lemma in the article.

The Japanese manuscript and published PDF assets are not edited here; their regular publishing workflow may update the generated artifacts.

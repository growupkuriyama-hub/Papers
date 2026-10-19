# Finite-semigroup foundation v3 — experimental reconstruction
Date: 2026-10-19
Status: DRAFT, mathematical proof audit pending; no submission, no merge.

## Baselines and isolation
- Base: Hybrid v2 experiment PR #60, commit 8019ae32c5a8f7d33854f3ad647b266cb7e9a903.
- Official TCS v230 remains on main and is not edited.
- Earlier full fresh-identity experiment PR #59 remains closed.

## Mathematical pivot
The primitive finite typing is a semigroup morphism
  s: Sigma+ -> S
onto a finite semigroup S (codomain restriction to the positive image is WLOG).
The fixed-s substitutability condition compares only positive factors x,y with s(x)=s(y) and common contexts. For targets requiring lambda, the unique monoid extension of s is
  s-hat: Sigma* -> S-sharp = S sqcup {e}
where e is a genuinely fresh identity, distinct from any identity S may have.
It sends lambda to e and nonempty w to s(w). Then
  ker(s-hat) = {(lambda,lambda)} union ker(s)
and S-sharp is isomorphic to Sigma* / ker(s-hat).
The empty alphabet case is handled separately: only empty and singleton-lambda languages are possible.

Every finite-monoid typing h:Sigma*->M restricts to a finite-semigroup typing s=h|Sigma+ into h(Sigma+); the learning family and reconstruction remain the same. Conversely s has the unique fresh-identity extension s-hat. This is not a monoid-subobject embedding that preserves preexisting identities.

## Algorithm and completeness
The reconstruction grammar keeps precisely the v230 positive-factor nonterminals, binary/typed-unary/lexical/start rules, and direct start epsilon rule. No epsilon-factor hypothesis nonterminal is introduced.
The target is refined over S-sharp in reduced BUNF, including nullable and unit productions.
The Hybrid v2 witnessed-U completeness induction is retained:
for positive-typed X and rule rho:X->alpha, the RHS canonical yield t_rho is nonempty and has the same positive semigroup type as omega(X). Rule U moves [omega(X)] to [t_rho]; nullable children disappear, while two positive children use the original B rule. The original start epsilon rule handles lambda.

## Structural conversions
- Recognizable regular languages over Sigma* are recognized by s-hat, *not* by the partial-domain map s alone.
- Refinement and products reduce to kernels of the fresh-identity completions. Product completions use the positive image of the product, which need not be the full target product.
- Erasing inverse morphisms phi are handled by the positive restriction of s-hat o phi; this absorbs the old erasure flag while respecting the positive-domain typing convention.
- Locally trivial / LI-join conditions concern the *positive semigroup* S, NEVER S-sharp: adding a global fresh identity generally destroys local triviality.
- A fixed-window monoid morphism h_{k,l}, the semilattice h_U, and group-valued g are permitted auxiliary full-word morphisms. When a named h_* indexes substitutability, learning, or typed thickness, its restriction to Sigma+ is meant. Auxiliary monoid values of lambda remain available in finite-state proofs.
- The LI-window proof evaluates possibly empty interior r using s-hat(r), with b s-hat(r) c in S. The LI-group factorization proof distinguishes the semigroup typing s from its auxiliary local-trivial morphism sigma.
- The semilattice's original identity 1_U stays distinct from the added fresh identity e. The typed fiber of h_U is the completion of its positive restriction.

## Review checklist
1. Independently reprove the semigroup-to-monoid extension and comparison of the language classes and reconstruction.
2. Audit the regular-recognition theorem's epsilon behavior, erasing inverse-image typing, and reduced-image product kernel argument.
3. Verify the LI-window shortening proof for r=lambda and LI-group divisor argument after renaming.
4. Verify all BUNF typed lifting and positive-only witness-U completeness steps, and SSBNF quantitative results for the newly renamed type.
5. Compare all named concrete monoid witnesses against the positive-restriction convention, especially h_{0,0} and h_U.
6. Check English/Japanese alignment, compilation, and PDF layout.
7. If adopted for TCS, regenerate the Marked PDF, 49-item referee responses and exact margin-line locators, abstract, submission PDFs/ZIP. The files still checked in for these are v230 artifacts and are NOT valid v3 outputs.

No mathematical verification certification is claimed from GitHub Actions or this research note.

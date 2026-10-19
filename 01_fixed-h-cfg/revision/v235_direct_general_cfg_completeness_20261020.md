# TCS-D-26-00494 — v235 direct general-CFG qualitative proof

Date: 2026-10-20. Canonical editing branch: `main`.

## Mathematical structure
For arbitrary reduced CFG `G=(V, Sigma, P, S0)`, every production is expressible as `rho: A -> u0 B1 u1 ... Br ur` with `u_i` terminal words and `B_i` nonterminals, including r=0, empty rules, unit rules and mixed terminal/nonterminal right-hand sides.
For every tuple of child types `mu_i` in the **fresh-identity completion** `S^sharp`, include a typed version with the parent index equal to the ordered product of terminal-block images and child types. Add a fresh start with one rule for each typed copy of `S0`, then trim. This refinement is finite even if it is not polynomial in the input grammar size.

Fix canonical terminal yield `omega(X)` and a terminal reaching context `(u_X,v_X)` for each retained typed non-start `X`. For each retained typed rule `rho:X->u0 Y1 u1 ... Yr ur`, define `t_rho=u0 omega(Y1) u1 ... omega(Yr) ur`. The finite witness set consists exactly of `u_X omega(X) v_X` for each typed non-start symbol and `u_X t_rho v_X` for each typed production (empty-type witnesses duplicate the canonical ones).

## Completeness proof (no normal form)
For a positive-type `X`, the two witnesses place `omega(X)` and `t_rho` in the same sample context, so unary Rule U derives `[[omega(X)]] -> [[t_rho]]`. Split the nonempty components of `t_rho` in their left-to-right order with repeated Rule B; every piece and intermediate concatenation is a nonempty observed factor of `u_X t_rho v_X`. Emit terminal blocks by B/L and replace positive child components via inductive derivations. Fresh-identity children generate only lambda and disappear. Terminal-only, mixed, unit, any number of nullable children and all r>=0 are covered; a positive parent cannot have `t_rho=lambda`. Initial typed start copies cover all nonempty yields and lambda is witnessed directly. This proves qualitative completeness for any reduced CFG, hence exact reconstruction and Gold convergence without BUNF assumptions.

## Quantitative-only BUNF assumptions
BUNF definition is recorded in Section 5 as a signpost for the later technical bounds, but **no Section 5 theorem assumes BUNF**. Section 6 bounds typed grammar/witness cardinalities using |S^sharp|^2 for binary rules and two children per rule; nullable-type rule witness duplicates the ordinary canonical yield witness. Lemma 7.1 and Appendix A use binary derivation-tree branching. Linear-spine normalization uses terminal-wrapper BUNF. For arbitrary initial CFGs, use the existing polynomial-size BUNF normalizations only in quantitative statements.

## Scope and checks
- Same learning algorithm `Rec_s` and `Learn_s`, same theorem labels and claimed scope, no incremental polynomial-data claim.
- Same 58 labels and 39 proof environments; all internal local references resolved.
- Reviewer response overview, R1.2, R1.11, R2.8 updated to state the new direct general-CFG proof and BUNF's exclusively quantitative role.
- English `main.tex` and `TCS-D-26-00494_Manuscript_Clean.tex` mirror.
- Updated English source SHA-256: `364a4ec03f178dbefcac0fd420b037ff88a398f894741966edb0b33c00dbf08d`.
- PDF build and 49-item marked-PDF anchor check required before journal submission. Japanese manuscript and Japanese reviewer response are NOT synchronized. No Editorial Manager or arXiv submission performed.

## Review caveat
The new direct general-CFG argument has undergone internal symbolic verification of all terminal/mixed/nullable cases; it is an author-approved revision but is not certified by formal proof software. Independent adversarial review remains useful, particularly for sample-factor splitting and proof-local indexing.

# MCFG v88 — independent four-lemma audit and integration checks

Date: 2026-10-23. Baseline: v87 on main. Proposal: Claude's v86 Sections 4–6 and A–C refactor, integrated with the *v87* qualitative front. Working PR: #70.

**Status:** detailed independent mathematical proof-path inspection and bilingual TeX/label validation. Not a Lean/Coq formal proof and not an independent full-paper signoff; journal submission is blocked pending the remaining citation/full-visual audit and author approval.

## Confirmed fixes

- **R1 mathematical correction**: `prop:effective-char-data` must NOT transfer existential total-length estimates of non-derivational relaxed witnesses `K^\dagger` to the computed derivational minimum-weight witnesses. English and Japanese statement/proof scopes corrected. The `(A_n)_1` example has shortest derivable tuple length `2^n` even though its ambient distribution class has a short representative.
- **v87 bridge**: removed stale `lem:exposed-rule-enumerated` reference from the new `prop:mcfg-relaxed-witnesses` proof. Explicitly invoke generalized v87 `prop:completeness` with `\iota(X)=\omega^\dagger(X)`, admissible `\chi(X)=E_A`, representative and rule evidence in positive sample, componentwise type equality, capped and uncapped construction, and separate `prop:reconstruction-soundness`.
- **GitHub Actions**: new `appendix_group_blocks.tex` now appears in the bilingual verification workflow path triggers, publishing workflow path triggers, and publishing stale-source `git diff` guard.
- All English main+2 included appendices and all Japanese main+3 included appendices were independently checked for duplicate `\label`s and unresolved `\ref`s; each set has **zero** unresolved and duplicate labels. The older unreferenced English group appendices remain in GitHub for archival comparison.

## Core 1 — Window skeleton (new `lem:boundary-short-canonical`)

**Reasoning**: choose a typed derivation minimal by node count. If a typed symbol recurs strictly along a root-to-leaf path, replacing the ancestor subtree with the descendant subtree (same rank/sort) yields a smaller derivation, a contradiction. Thus a path contains at most `n_typ` grammar nodes. For each root component mark its required prefix/suffix endpoints (and one symbol in the `k=ell=0` case). Every omitted child component is a contiguous, unmarked interval in one root component by linear nondeleting nonpermuting MCFG syntax. Short components are fully marked; long components keep the same marked boundaries after replacements, with nonempty good children. For an arbitrary finite monoid morphism `kappa`, per-block `kappa` equality preserves ordered products by homomorphism, **without commutativity**. Since `h\preceq(h_window,kappa)`, type-preserving replacement lifts the untyped yield to the same trimmed typed nonterminal. Terminal bookkeeping yields `f(k+ell+1)*n_typ*(theta_bar+r*beta)`.

**Audit status:** no gap located under the explicit hypotheses; crucial constraints: componentwise nonempty yields, all omitted child tuples realizable and replaceable with the same componentwise `kappa` value, and finite typed rank. Not a statement about arbitrary deleting/permuting grammars.

## Core 2 — Heavy node count (`lem:heavy-node-count`)

**Reasoning**: minimize first total root length, then derivation node count, at fixed root `lambda` vector. A repeated pair (nonterminal, full componentwise `lambda`-vector) on an ancestor chain can be spliced out, contradicting lexicographic minimality. Thus path length is at most `|V||N|^f`. Heavy nodes (subtree total length > b) are ancestor-closed by nondeletion. Their maximal heavy nodes (leaves of the heavy subtree) form an antichain of size `<=c`. Hence at most `c|V||N|^f` heavy nodes; root terminal contributions come from either a heavy rule's explicit terminals (<=theta_bar<=b) or a light child below a heavy rule (length <=b, at most r children). The claimed `(r+1)b max{1,c|V||N|^f}` bound follows.

**Audit status:** proof valid subject to the stated **uniform antichain bound for every minimal tree**, which is proved separately from Core 3; there is no hidden conclusion from pigeonhole alone.

## Core 3 — Finite-group block replacement (`lem:block-replacement`)

**Commutative:** with additive notation, one owner's difference across the d lines gives a vector in `A^d`. If `m>d(A^f)>=d(A^d)`, a nonempty zero-sum subsequence produces the simultaneous replacement. This does not assert a noncommutative zero-sum theorem.

**Noncommutative:** if a selected owner has no blocks, replacing it alone trivially preserves values; this case was added explicitly before unary-pattern counting. Otherwise record for each owner its `1..f` owned blocks, line assignments and within-line order (<=U_f patterns). Uniformize `N^{2^{f^2}}` indices of one pattern, apply order homogenization over at most `f^2` comparisons to obtain N selected indices. The homogeneous line-order lemma splits these into at most f consecutive class regions with index-monotone chunks. For each region set `P_j,Q_j` to original/replacement prefix products and `K_j=P_jQ_j^{-1}`; equality `K_a=K_b` implies replacing exactly the intervening chunks preserves the region's **ordered** product via `P_a Q_a^{-1}Q_b P_b^{-1}P_n=P_n`. Use one state per class in `A^q` and `N+1>|A|^q` to find two matching states simultaneously. Reversing chunk indices for decreasing classes preserves the common owner interval. All untouched constants remain in order.

**Audit status:** explicit proof path is coherent; the uniformization and homogeneous-order lemmas are preserved rather than replaced by an informal Ramsey invocation. The bound `M_{A,f}` is conservative. General block-family definitions may permit unused owners, handled separately. The old `lem:group-heavy-antichain` label was *not* attached to this pure group lemma, since that would silently change the semantics of the named result.

## Core 4 — Local-group shortening (`lem:local-group-shortest`)

**Reasoning**: fix root `lambda_{k,g}` values and minimize length/node count. Let `b_w=f(2k+1)n_w(r+1)theta_bar`; each heavy child has a retained window-refinement sort, since its derivation can be inserted in a successful untyped context. Core 1 for trivial `kappa` supplies a shorter tuple preserving all component windows. Every root window is unchanged, including short root components (short replacement components are *literally* unchanged by window equality). The local-group factorization lemma expresses each long root component's `gamma` as an ordered word in the chosen long block values, with constants depending only on unchanged window boundaries/fixed segments. Heavy owners contribute at most f blocks. This is exactly Core 3's abstract block family, and replacing a nonempty owner set preserves all root `gamma` values, hence root `lambda`, contradicting minimality. Core 2 yields `beta_lambda=(r+1)b_w max{1,(M_{A,f}-1)n_lambda}`; for abelian A substitute `d(A^f)`.

**Audit status:** no failed assumption found. Crucial distinction: `gamma_{k,g}` itself is not treated as a global monoid morphism; **the combined** `lambda_{k,g}` is the finite-monoid typing, and `gamma` is handled by the separate ordered block product argument. Japanese local-group proof has been expanded to spell out the pattern-counting/order-homogenization/interval-selection bridge rather than saying `verbatim`.

## Bilingual status and remaining gates

- English: full Claude structural refactoring of Sections 4–6 plus appendix A, new group appendix B, revised local-group appendix C; mathematically uses the preserved v87 qualitative front.
- Japanese: **R1 corrected**; translated new English v88 lemmas for witness-length template, typed replacement, generic auxiliary-monoid window skeleton and uniform heavy-node count, including full proofs. The LG proof now invokes the heavy-node lemma and spells out group-block ordering rather than relying on a verbatim argument. Original separate abelian and arbitrary-group appendices are retained. This is mathematical-content synchronization, not identical layout.
- English 38-page and Japanese 55-page PDF builds passed in GitHub Actions; complete source checks are required before the merge. This is a **light independent proof-path check**, not a complete mathematical audit. Full-page PDF visual review remains a pre-submission gate.

## Lightweight independent recheck before author-authorized main merge

The following four proof steps were inspected directly in v88 source.

1. **Window skeleton:** typed-symbol repeats along a derivation path can be spliced; the empty-window case marks one terminal in each nonempty root component; disjoint omitted child intervals keep their ordered finite-monoid values. The Japanese generic lemma now explicitly cites typed replacement.
2. **Heavy nodes:** lexicographic minimality (root length, then node count), componentwise typing preservation, ancestor-closed heavy subtrees, and the bound on the leaf antichain give the announced node and output-length estimates.
3. **Finite-group blocks:** the identity involving prefix products P_a Q_a^{-1} = P_b Q_b^{-1} preserves an ordered (not commuted) group product. Empty-owner indices are handled. Davenport zero-sum shortening is confined to abelian groups.
4. **Local groups:** short components are unchanged, longer components preserve windows, and all variable gamma contributions factor into ordered blocks with constants independent of selected owners. The group block lemma and heavy-node lemma then give the unchanged bound.

No counterexample was found under the stated assumptions. This is not a full independent mathematical proof certification, and the Japanese appendices retain the older separate group proofs despite mathematical synchronization of the shared bounds.

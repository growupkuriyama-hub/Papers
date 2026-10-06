# v115 → v116 audit: collapse of occurrence-indexed hypothesis states

Date: 2026-10-07

## Question

The v115 batch constructor used one hypothesis nonterminal
`[x:u,v]` for every observed factor/context triple `uxv in K`.
Rule (R2) connected all observed context copies of the same factor `x`.
This raises the question whether the context index carries any language-
generating information.

## Exact quotient theorem

For every finite sample `K` and fixed typing `h`, the v115 constructor
and the v116 substring-indexed constructor generate exactly the same language.

The v116 states are one symbol `[x]` for each distinct nonempty factor of
`K`, with rules

- (B) `[xy] -> [x][y]` when `xy` is observed;
- (U) `[x] -> [y]` when `h(x)=h(y)` and `x,y` share an observed context;
- (L) `[a] -> a`;
- (S) start entry to each observed sample word, plus the direct empty-word
  start rule when needed.

### v115 → v116

Map every old state `[x:u,v]` to `[x]`.

- (R1) maps to (B).
- (R2) maps to zero steps, because its source and target both map to `[x]`.
- (R3) maps to (U): the two displayed old states certify a shared sample
  context and the rule already requires equal `h`-type.
- (R4) maps to (L).
- (R5) maps to (S).

Therefore every old derivation maps to a v116 derivation.

### v116 → v115

Prove a stronger simulation statement: a v116 derivation rooted at `[x]`
can be simulated from **any** old representative `[x:u,v]`.

- For (U), choose the observed context `(p,q)` witnessing the unary rule.
  Old (R2) first transports `[x:u,v]` to `[x:p,q]`, and old (R3) changes
  it to `[y:p,q]`. Apply the induction hypothesis from that representative.
- For (B), choose an observed occurrence `pxyq in K`. Old (R2) transports
  the current `[xy:u,v]` to `[xy:p,q]`; old (R1) then produces
  `[x:p,yq][y:px,q]`. Apply the induction hypothesis to both children.
- (L) is old (R4).
- (S) is old (R5), followed by the same induction.

Hence every v116 derivation is simulated by v115. This proves exact language
equivalence for every finite sample, not only eventual equivalence on
characteristic samples.

## Direct soundness proof for v116

The quotient form admits the simpler invariant

`[x] =>* w  implies  x ==_L w and h(w)=h(x)`.

The unary case follows from one shared sample context plus fixed-`h`
substitutability. The branching case follows because syntactic congruence is
a monoid congruence. A start state `[x]` has `x in K subset L`, so equality
of distributions implies that its derived terminal word is also in `L`.

This proof no longer needs a context-transport case.

## Completeness and witnesses

The existing canonical witness set is retained unchanged.

- For a typed terminal rule `X -> a`, the first witness for `omega(X)`
  and the terminal-rule witness for `a` share the canonical context and
  have equal `h`-type, licensing (U), followed by (L).
- For a typed binary rule `X -> Y Z`, the first witness for `omega(X)`
  and the binary-rule witness for `omega(Y)omega(Z)` share the canonical
  context. The typed-yield invariant gives equal `h`-type, licensing (U),
  after which (B) exposes the two child states.
- At the root, the canonical context is the empty context, so (S) starts the
  same induction.

Thus the exact-reconstruction theorem, characteristic-sample theorem, Gold
convergence argument, typed-thickness bounds, fixed-window transfer, and
linear-target bound do not change.

## Complexity

With `n_K = ||K||`:

- factor occurrences / distinct factor states: `O(n_K^2)`;
- branching candidates: `O(n_K^3)`;
- unary candidates: bucket observed factor occurrences by
  `(left context, right context, h-type)`. There are `O(n_K^2)` total
  bucket entries and each bucket has size at most `|K| <= n_K`, so
  `sum_B |B|^2 = O(n_K^3)`;
- if factor strings are copied literally into productions, each production
  has encoding length `O(n_K)`.

Therefore an explicit conservative bound is `O(n_K^4)`, improving the v115
`O(n_K^5)` bound.

## Relation to prior work

Clark (2013), Algorithm 1, uses one nonterminal per observed substring,
branching rules `[[uv]] -> [[u]][[v]]`, lexical rules, and unary rules
between substrings sharing an observed context. The v116 constructor is this
standard substring-indexed architecture with its unary relation filtered by
the fixed finite-monoid type `h` (plus an explicit single start symbol and
the manuscript's separate empty-word convention).

Accordingly, the paper no longer treats the reconstruction architecture
itself as the main novelty. The contribution is the fixed-`h` language
class and its finite-witness, typed-thickness, algebraic, linear, and boundary
analysis.

## Other v116 corrections

- The parity toy example now says only that yield-type splitting is required
  by the **present completeness argument**, not by every possible learner.
- The exponential source-to-typed thickness gap is promoted from a remark to
  a proposition; its algorithm-independent-lower-bound caveat remains.
- Formula-adjacent footnote markers that could look like exponents were moved
  into prose.
- Major metavariable collisions were reduced.
- Singleton subsections in Sections 6 and 8 were removed.
- The nonregular linear separator now explains why identifying `c` and `d`
  under one `h`-value is deliberate rather than merely encoding center
  symbols by type.

## Verification status

The mathematical equivalence above is an exact proof. In addition, source-level
preflight checks confirm balanced LaTeX environments/braces, no duplicate
labels, no unresolved internal references, and synchronization of theorem
labels between the English and Japanese sources.

GitHub Actions successfully compiles the v116 English manuscript, Japanese
reference translation, Round-1 response, and marked-up revision. Basic PDF
preflight reports all four generated PDFs as openable, unencrypted,
text-based documents with no XFA. The archived Lean v88 artifact remains the
theorem-facing formalization baseline; v116 has not been minted as a separate
Lean archive.

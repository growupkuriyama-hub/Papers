# Proof audit — Observation Is Not Enough v2

Date: 2026-09-30

## Verdict

No fatal mathematical gap was found in the v1 theorem package. The main new
result that required the most adversarial checking — the all-arity Clark--Wurm
compression theorem for X_{k,r} — survives the audit.

The audit did identify several presentation/interface issues that are repaired
in v2:

1. Safe_f and cmp_f were occasionally used without fixing the tuple interface.
2. The X_{k,r} all-arity proof was correct in substance but compressed two
   positional arguments that a reviewer could reasonably challenge. The proof
   is now rewritten around unique skeleton intervals and invariant tuple
   support.
3. The positive-interface proof now treats the d=1 and vacuous large-arity
   cases explicitly.
4. The MCFG encoded-data scale in OFET is sum max(1,|w|), while the current #2
   manuscript defines positive sample size as sum (|w|+1). The v2 bridge paper
   now states explicitly that its mcd formulas use the OFET convention; exact
   sample-cardinality statements do not depend on that bookkeeping choice.
5. The fixed-compression theorem now quantifies both minima explicitly.
6. The Pareto theorem is now parametrized by a fixed safety interface.

These are repairs to rigor and notation, not changes to the headline theorems.

## Theorem-by-theorem status

### Interface monotonicity — PROVED

The positive sentence-context interface tests a subset of the Clark--Wurm
comparisons, so every Clark--Wurm-safe observer is positive-interface safe.
The convention min(empty set)=infinity is now stated.

### Fixed-length unary bridge — PROVED

For L subseteq Sigma^n, an empty and a nonempty unary fragment cannot share an
accepting context because the two resulting words would have different
lengths. Hence the unary empty-fragment convention does not change safety.

### Observer refinement / reconstruction monotonicity — PROVED

This is proved for the two fixed reconstruction architectures used in OFET.
If h=pi o g, every semantic substitution rule admitted by the finer observer g
is also admitted by h; all other rules are observer-independent. Therefore the
g hypothesis is a subgrammar of the h hypothesis. Soundness under h then
implies nesting of locking-sample families.

### R_{m,q} observation--reconstruction separation — PROVED from OFET inputs

The current OFET source was rechecked for:

- exact minimum observation size qm;
- minimum-observation forcing kappa >= m;
- the q(m+1) gap when kappa < m;
- exact characteristic-data formula 4(qm+m^2+kappa(q-1)).

The bridge to Clark--Wurm unary compression follows from fixed target length
three. The optimizer separation, exact gap 4(m-1)(q-1), and the q=m^2
factor-two asymptotic follow algebraically.

### Exact Clark--Wurm compression of X_{k,r} — PROVED after adversarial audit

The upper bound uses the two-element idempotent monoid that records only
emptiness. The key invariant is the unique skeleton

A_1 ... A_r B_1 ... B_r,

whose symbols occur once each. For any nonempty tuple component, its skeleton
substring therefore has a unique interval. Empty-separated blocks may move
internal hole boundaries, but their concatenated skeleton interval is
invariant. The revised proof tracks the union U of tuple-supported skeleton
positions and checks the paired index constraint slot by slot.

The arity-two lower bound against the trivial observer remains valid, giving
the exact sequence 1,2,2,...

### Positive-interface collapse on X_{k,r} — PROVED

With nonempty components and nonempty internal separators, the shared context
anchors each component interval. The trivial observer is therefore safe. The
revised proof explicitly handles unary root contexts and arities too large to
admit nonempty tuples.

### Equality of learner rules and compression--reconstruction coincidence — PROVED

This is for the OFET occurrence learner. On observed nonempty tuple components
the emptiness observer is constant. Shared admissible context already forces
equal slot type, so the trivial, emptiness, and slot observers generate the
same semantic unary rules; all other rules are observer-independent. Hence the
hypotheses agree sample-by-sample.

### Fixed compression, unbounded reconstruction — PROVED

For L_r=X_{2,r}, Clark--Wurm compression through arity two is constantly two,
while the global minimum characteristic-sample cardinality is r+1. Under the
OFET encoded-data convention, the minimum is 2r(r+1). Therefore no function
of the compression number alone can upper-bound that reconstruction cost on a
class containing all X_{2,r}.

Scope caution: alphabet size, word length, and witnessed rank grow with r. The
theorem does not exclude bounds using those additional parameters.

### Relational-morphism reconstruction separation — PROVED from #3 inputs

The current #3 source was rechecked. A minimum-codomain separating relational
morphism has codomain size equal to the compression number. Every free-monoid
selector is safe and has image size at most that codomain; strict inequality
would contradict minimality, so every selector is compression-optimal. The
R_{m,q} separation theorem then makes every such selector
reconstruction-suboptimal.

### Observer-resource Pareto principle — PROVED

After fixing one safety interface, the set of realized finite natural-valued
resource vectors lies in N^d; Dickson's lemma gives finitely many minimal
vectors. The minimum first coordinate equals the corresponding compression
number. Refinement-monotone coordinates force distinct Pareto points to be
represented only by incomparable observers.

### Weighted phase transition — PROVED

It is an exact comparison of the two OFET Pareto points. The sign calculation
was independently rechecked.

## Computational sanity check for X_{k,r}

The ancillary script xkr_cw_small_audit.py exhaustively enumerates accepted
context/tuple factorizations for:

- (k,r)=(2,2),
- (k,r)=(2,3),
- (k,r)=(3,2).

It checks multiple arities, including arities beyond the target length where
empty Clark--Wurm components are possible. In every tested case:

- the emptiness observer is Clark--Wurm safe;
- the trivial observer is positive-interface safe;
- the trivial observer fails Clark--Wurm safety at arity two.

All checks pass. This is supplementary evidence only; it is not used as a
proof.

## Remaining open audit item

The mathematical proof audit is now internally closed. The remaining
substantive pre-submission task is a dedicated literature-priority search. An
independent human proof read would still be desirable before submission, but
there is no currently identified mathematical gap blocking use of the theorem
package in the dissertation.

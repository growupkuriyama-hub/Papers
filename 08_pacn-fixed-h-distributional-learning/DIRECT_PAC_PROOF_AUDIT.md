# Direct fixed-h PAC proof audit

Date: 2026-10-05  
Scope: `direct-improper-learner.tex`, `direct-semantic-proper-learner.tex`,
`direct-finite-grammar-proper-learner.tex`.

This is an internal manual proof audit, not a formal verification.

## 1. Dependency boundary

The direct fixed-`h` PAC results do **not** use Chernikov–Towsner
Theorem 6.5.  The only ingredients are:

1. finite componentwise typing;
2. typed tuple substitutability;
3. the product structure of the sampling measure;
4. full or support-sensitive coordinate-slice observations;
5. elementary missing-mass estimates;
6. positive Horn closure for semantic properness.

Consequently the Malliaris objection to the proposed proof of CT25 v2 does
not affect these direct results.

## 2. Typed rectangle lemma

For one fixed tuple type `tau`, two nonempty tuple-columns are either
identical or disjoint.  This follows immediately from the substitutability
axiom: an intersection forces equality.  Grouping equal columns therefore
gives a disjoint union of complete rectangles

[
R|_	au=dotigcup_j C_{	au,j}	imes B_{	au,j}.
]

Across different tuple types the `B_{	au,j}` are also disjoint because
the type fibers themselves are disjoint.  Context sides need only be
disjoint *within* a fixed type.

Audit result: **sound**.

## 3. What one captured block requires

A block is recovered once:

- some sampled context lies in its context side; and
- for at least one factor coordinate `i`, some sampled `i`-th factor
  value lies in the projection of the tuple side.

The context slice reveals the complete tuple side for the relevant type.
After selecting a tuple in that side matching the sampled factor value, the
corresponding factor-coordinate slice reveals the complete context side.

This works for every factor coordinate, not only coordinate 1.  Using all
`d` factor-coordinate streams improves the one-batch estimate.

Audit result: **sound**.

## 4. Sharpened one-batch bound

Write

[
a_{	au,j}=mu_0(C_{	au,j}),qquad
b_{	au,j}=(mu_1otimescdotsotimesmu_d)(B_{	au,j}),
]

and

[
c_{i,	au,j}=mu_i(pi_i(B_{	au,j})).
]

Then `c_{i,tau,j} >= b_{tau,j}` for every `i`.  With `n` anchors,

[
P[	ext{miss block}]
 le e^{-na_{	au,j}}+e^{-nsum_i c_{i,	au,j}}
 le e^{-na_{	au,j}}+e^{-ndb_{	au,j}}.
]

Globally,

[
sum_{	au,j} b_{	au,j}le1,
qquad
sum_{	au,j} a_{	au,j}le Q,
qquad
Q=prod_i |g_i(X_i)|.
]

Using `u exp(-lambda u) <= 1/(e lambda)`,

[
E[	ext{one-sided error}]
 le {1+Q/dover en}.
]

Thus a batch of size

[
nge
leftlceil {2over eepsilon}left(1+{Qover d}ight)ightceil
]

fails with probability at most `1/2` by Markov.  Independent batching and
the monotonicity of one-sided union/closure give

[
N_{epsilon,delta}le
leftlceil {2over eepsilon}left(1+{Qover d}ight)ightceil
leftlceillog_2{1overdelta}ightceil.
]

For fixed-`h`, `Q=q^d` with `q=|h(Sigma^+)|`.

Audit result: **sound; improves the previous `4Q/(e epsilon)` bound**.

## 5. Support-sensitive observations

On a finite/countable product, the atomic support product has full measure.
For arity at least two coordinates (here `d+1 >= 2`), the domain of one
nonempty support-sensitive coordinate-cross reveals each coordinate support
by projection.  The direct learner therefore does not need the numerical
probabilities or the unknown measure.

Audit result: **sound under the support-sensitive observation definition
used in this manuscript**.

## 6. Positive Horn closure

The semantic class of all `(f,h)`-tuple-substitutable languages is closed
under arbitrary intersections.  Equivalently, the least semantic target
containing a positive seed is obtained by the positive rules

[
E[ec x],E[ec y],F[ec y]Rightarrow F[ec x]
]

for equal componentwise `h`-types, with the reverse direction supplied by
swapping `x` and `y`.

Because the true target is one model of these rules containing the observed
positive words, the closure is always a sublanguage of the target.  Every
captured rectangle is contained in the closure by one application of the
arity-`d` Horn rule.  Hence semantic properness preserves the same PAC
bound.

Audit result: **sound**.

## 7. Finite-target grammar properness

If the true target is finite, the Horn closure is a finite sublanguage of
the target, hence regular, context-free, and fan-out-one MCFG.  Saturation
from an explicitly supplied finite positive list terminates because every
generated word remains in the finite target.

Important representation caveat: this does **not** say that an algorithm
given an infinite slice oracle can detect in finite time that it has already
seen the complete finite set of positive labels.  The manuscript states this
caveat explicitly.

Audit result: **sound with the stated explicit-positive-list convention**.

## 8. Claims that remain open

The following are not established by the direct argument:

- a general finite-`VC_k` => proper `PAC_k` theorem;
- Takeuchi 2020 Problem 11 in full generality;
- effective proper CFG/MCFG-valued learning for arbitrary infinite
  fixed-`h` targets;
- effective finite encoding of arbitrary infinite labelled slices;
- a tight lower bound matching the current `q^d`-scale direct upper bound.

## 9. Current status

The direct fixed-`h` semantic PAC theorem is suitable to use as the
project's **independent sufficiency route**, provided the distinction between

- semantic properness,
- grammar-presentation properness, and
- effective finite-input learning

is kept explicit.

# Direct fixed-h PAC proof audit

Date: 2026-10-05  
Scope: \`direct-improper-learner.tex\`, \`direct-semantic-proper-learner.tex\`,
\`direct-finite-grammar-proper-learner.tex\`.

This is an internal manual proof audit, not a formal verification.

## 1. Dependency boundary

The direct fixed-\`h\` PAC results do **not** use Chernikov–Towsner
Theorem 6.5. The only ingredients are:

1. finite componentwise typing;
2. typed tuple substitutability;
3. the product structure of the sampling measure;
4. full or support-sensitive coordinate-slice observations;
5. elementary missing-mass estimates;
6. positive Horn closure for semantic properness.

Consequently the Malliaris objection to the proposed proof of CT25 v2 does
not affect these direct results.

## 2. Typed rectangle lemma

For one fixed tuple type \(\tau\), two nonempty tuple-columns are either
identical or disjoint. This follows immediately from the substitutability
axiom: an intersection forces equality. Grouping equal columns therefore
gives a disjoint union of complete rectangles
\[
R|_\tau=\mathop{\dot\bigcup}_j C_{\tau,j}\times B_{\tau,j}.
\]

Across different tuple types the \(B_{\tau,j}\) are also disjoint because
the type fibers themselves are disjoint. Context sides need only be
disjoint *within* a fixed type.

Audit result: **sound**.

## 3. What one captured block requires

A block is recovered once:

- some sampled context lies in its context side; and
- for at least one factor coordinate \(i\), some sampled \(i\)-th factor
  value lies in the projection of the tuple side.

The context slice reveals the complete tuple side for the relevant type.
After selecting a tuple in that side matching the sampled factor value, the
corresponding factor-coordinate slice reveals the complete context side.

This works for every factor coordinate, not only coordinate 1.

Audit result: **sound**.

## 4. Projection-volume bound

Write
\[
a_{\tau,j}=\mu_0(C_{\tau,j}),\qquad
b_{\tau,j}=(\mu_1\otimes\cdots\otimes\mu_d)(B_{\tau,j}),
\]
and
\[
c_{i,\tau,j}=\mu_i(\pi_i(B_{\tau,j})).
\]

Because
\[
B_{\tau,j}\subseteq\prod_{i=1}^d\pi_i(B_{\tau,j}),
\]
product measure gives
\[
b_{\tau,j}\le\prod_{i=1}^d c_{i,\tau,j}.
\]
AM–GM therefore yields
\[
\sum_{i=1}^d c_{i,\tau,j}
\ge d\,b_{\tau,j}^{1/d}.
\]

With \(n\) anchors,
\[
\Pr[\text{miss block}]
\le
e^{-na_{\tau,j}}
+
e^{-nd b_{\tau,j}^{1/d}}.
\]

Globally,
\[
\sum_{\tau,j}b_{\tau,j}\le1,\qquad
\sum_{\tau,j}a_{\tau,j}\le Q,\qquad
Q=\prod_i |g_i(X_i)|.
\]

The two elementary maxima are
\[
\sup_{u\ge0}u e^{-nu}=\frac1{en},
\qquad
\sup_{0\le b\le1} b e^{-ndb^{1/d}}
=\frac{e^{-d}}{n^d}.
\]
Hence
\[
\mathbb E[\text{one-sided error}]
\le
\frac1{en}+\frac{Q}{e^d n^d}.
\]

A sufficient one-batch size is
\[
n_{Q,d,\epsilon}
=
\left\lceil
\max\left\{
\frac4{e\epsilon},
\frac{(4Q/\epsilon)^{1/d}}e
\right\}
\right\rceil,
\]
which makes the expectation at most \(\epsilon/2\), hence the batch failure
probability at most \(1/2\) by Markov.

Independent batching and monotonicity of one-sided union/closure give
\[
N_{\epsilon,\delta}
\le
n_{Q,d,\epsilon}
\left\lceil\log_2\frac1\delta\right\rceil.
\]

For fixed \(h\), \(Q=q^d\) with \(q=|h(\Sigma^+)|\), so
\[
N_{\epsilon,\delta}
\le
\left\lceil
\max\left\{
\frac4{e\epsilon},
\frac{4^{1/d}q}{e\epsilon^{1/d}}
\right\}
\right\rceil
\left\lceil\log_2\frac1\delta\right\rceil.
\]

Thus the dependence on observer type count is **linear in \(q\)** rather
than \(q^d\).

Audit result: **sound; this supersedes the earlier
\(2(1+Q/d)/(e\epsilon)\) bound.**

## 5. Support-sensitive observations

On a finite/countable product, the atomic support product has full measure.
For arity at least two coordinates (here \(d+1\ge2\)), the domain of one
nonempty support-sensitive coordinate cross reveals each coordinate support
by projection. The direct learner therefore does not need the numerical
probabilities or the unknown measure.

Audit result: **sound under the support-sensitive observation definition
used in this manuscript**.

## 6. Positive Horn closure

The semantic class of all \((f,h)\)-tuple-substitutable languages is closed
under arbitrary intersections. Equivalently, the least semantic target
containing a positive seed is obtained by the positive rules
\[
E[\vec x],E[\vec y],F[\vec y]\Rightarrow F[\vec x]
\]
for equal componentwise \(h\)-types, with the reverse direction supplied by
swapping \(\vec x,\vec y\).

Because the true target is one model of these rules containing the observed
positive words, the closure is always a sublanguage of the target. Every
captured rectangle is contained in the closure by one application of the
arity-\(d\) Horn rule. Hence semantic properness preserves the same PAC
bound.

Audit result: **sound**.

## 7. Finite-target grammar properness

If the true target is finite, the Horn closure is a finite sublanguage of
the target, hence regular, context-free, and fan-out-one MCFG. Saturation
from an explicitly supplied finite positive list terminates because every
generated word remains in the finite target.

Important representation caveat: this does **not** say that an algorithm
given an infinite slice oracle can detect in finite time that it has already
seen the complete finite set of positive labels. The manuscript states this
caveat explicitly.

Audit result: **sound with the stated explicit-positive-list convention**.

## 8. Claims that remain open

The following are not established by the direct argument:

- a general finite-\(VC_k\) \(\Rightarrow\) proper \(PAC_k\) theorem;
- Takeuchi 2020 Problem 11 in full generality;
- effective proper CFG/MCFG-valued learning for arbitrary infinite
  fixed-\(h\) targets;
- effective finite encoding of arbitrary infinite labelled slices;
- a tight higher-arity lower bound matching the current linear-\(q\)
  direct upper bound for every fixed observer.

## 9. Current status

The direct fixed-\(h\) semantic PAC theorem is suitable to use as the
project's **independent sufficiency route**, provided the distinction between

- semantic properness,
- grammar-presentation properness, and
- effective finite-input learning

is kept explicit.

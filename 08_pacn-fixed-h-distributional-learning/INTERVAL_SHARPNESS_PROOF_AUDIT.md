# Cyclic-interval sharpness proof audit

Date: 2026-10-05  
Scope: \`main.tex\`, especially \`lem:interval-rigid-decoding\`,
\`thm:interval-realization\`, \`prop:universal-interval-frame\`,
\`cor:all-q-sharp\`, and \`thm:observer-budget-law\`.

This is an internal manual proof audit plus exhaustive finite
counterexample search. It is not formal verification or external review.

## 1. Why this audit was needed

The sharpness family contains an **arbitrary** sublanguage
\[
L_S=\{w_{\mathbf i}:\mathbf i\in S\}
\]
of a rigid finite codebook. It is not enough to prove substitutability only
for the full codebook: an arbitrary choice of \(S\) could in principle keep
a common accepting context while deleting one side of another substitution.

The revised proof isolates exactly this issue in the rigid-decoding lemma.

## 2. Rigid-decoding lemma

For any \(1\le e\le d\), let two \(e\)-tuples of factors have equal
componentwise observer type and share a sentence context in the full rigid
codebook.

The proof establishes the dichotomy:

1. the factor tuples are literally equal; or
2. \(e=1\) and both factors have the same singleton distribution in the
   full codebook.

The argument uses only the grammar's contiguous-hole geometry and cyclic
interval injectivity.

### Case A — a context-specific marker lies outside the holes

The common context fixes \(i_0\). Every hole with at most \(d-1\) variable
roles has a contiguous variable-role interval, so its type uniquely recovers
all variable indices.

The only possible loss of injectivity is a one-hole factor containing all
\(d\) variable roles. Such a factor contains every internal separator
marker and therefore fixes the complete index tuple literally. Its boundary
pattern is fixed, so its full-codebook distribution is a singleton.

For \(e\ge2\), a hole cannot contain all \(d\) variable roles: a contiguous
factor containing \(X_1,\ldots,X_d\) also contains all internal separator
positions, leaving only the adjacent end positions outside, with no room for
the required nonempty gap to a second hole.

### Case B — no context-specific marker lies outside the holes

For \(e=1\), the factor contains both end markers and hence the entire
codeword. Its distribution is the singleton empty context.

For \(e\ge2\), each nonempty literal gap must contain a variable-role symbol.
Thus at least one variable role lies outside the holes. The two end holes
contain the two copies of role \(B_0\); at least one end hole has at most
\(d-2\) variable roles. Its nonzero role contributions therefore form a
cyclic interval of at most \(d-1\) roles. Interval injectivity recovers
\(i_0\). Once \(i_0\) is known, every remaining hole has at most \(d-1\)
variable roles and is decoded in the same way.

Audit result: **the dichotomy is sound under the manuscript's
nonempty-inner-gap definition of sentence contexts.**

## 3. Why the dichotomy survives arbitrary S

Suppose the same-type tuples share an accepting context in \(L_S\).

- If the tuples are equal, their distributions in \(L_S\) are equal
  trivially.
- If they are distinct, the rigid-decoding lemma says both full-codebook
  distributions are exactly the same singleton \(\{E\}\). Since both
  \(E[\mathbf x]\) and \(E[\mathbf y]\) are already assumed in \(L_S\),
  restriction to an arbitrary \(S\) leaves both distributions equal to
  \(\{E\}\).

Thus the arbitrary-sublanguage quantifier is handled explicitly.

Audit result: **sound**.

## 4. Universal interval frame over Z/qZ

Put \(m=d-1\) and use role vectors
\[
e_1,\ldots,e_m,\quad a=(1,\ldots,1),\quad b,
\]
where \(b\) alternates between \(0\) and \(1\) and has final coordinate \(1\).

There are \(m+2\) cyclic windows of length \(m\). Their determinants are,
up to sign,
\[
1,\quad a_1=1,\quad
a_r b_{r+1}-a_{r+1}b_r=b_{r+1}-b_r\in\{\pm1\},
\quad b_m=1.
\]

Hence every length-\(m\) cyclic window is a basis over
\(\mathbb Z/q\mathbb Z\) for **every integer \(q\)**, because \(\pm1\) is a
unit modulo every \(q\). Every shorter cyclic interval is a subset of one of
these bases and is therefore injective.

Audit result: **sound for arbitrary composite \(q\); no field assumption is
used.**

## 5. Exact observer-budget law

The general upper bound gives
\[
VC_{d+1}\le\lfloor t_h^{1/(d-1)}\rfloor
\qquad(d\ge2).
\]

For
\[
q=\lfloor T^{1/(d-1)}\rfloor
\]
the universal interval frame supplies a sharp observer with
\[
t_h=q^{d-1}\le T,\qquad VC_{d+1}=q.
\]

Therefore the worst-case budget law
\[
\mathfrak V_d(T)=\lfloor T^{1/(d-1)}\rfloor
\]
follows without a prime-power restriction. The separate padding
construction changes \(t_h\) from \(q^{d-1}\) to exactly \(T\) while the
target family ignores the fresh types.

Audit result: **sound conditional only on the already-audited typed-box/root
upper bound and the interval realization proved above.**

## 6. Exhaustive finite counterexample search

Reproducible script:
\`tools/interval_sharpness_audit.py\`

Recorded output:
\`computations/interval_sharpness_audit.txt\`

Audited cases include:

- \(d=2,\ q=2,3\);
- \(d=3,\ q=2,3,4\);
- \(d=4,\ q=2,3\);
- \(d=5,\ q=2,3\);
- \(d=6,\ q=2\).

For every \(1\le e\le d\), every legal hole pattern and every same-type
tuple pair sharing a full-codebook context was checked. No arbitrary-\(S\)
counterexample was found.

A notable structural pattern is that in all tested cases, same-type distinct
tuple collisions with a common context disappear completely for \(e\ge2\).
The remaining \(e=1\) collisions all satisfy the exact universal-\(S\)
condition; representative collisions have singleton distributions, matching
the proof.

## 7. Status after audit

The following are reasonably marked **manually proof-audited in draft**:

- cyclic interval realization;
- universal \((\mathbb Z/q\mathbb Z)^{d-1}\) interval frame;
- sharpness for every integer side \(q\);
- same-cardinality observer VC separation based on this sharpness;
- exact worst-case observer-budget law.

This audit does not certify unrelated claims in #8 and does not replace
peer review.

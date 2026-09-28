# MCFG v57 -> v58 revision note

## Purpose

v58 strengthens the intrinsic-rule-rank witness so that the witness is
genuinely multiple-context-free at the language level.

The v57 target
\[
L_{\mathrm{intr}}=P_{\mathrm{intr}}\mathtt{\#}\mathrm{MIX}_2^+
\]
was context-free.  It correctly had intrinsic minimum rule rank two even when
arbitrary finite fan-out was allowed, but it did not itself witness minimum
fan-out greater than one.  v58 replaces it by a non-context-free target with
minimum fan-out two while retaining the all-finite-fan-out rule-rank lower
bound.

This revision was prompted by a reviewer-style audit of the v57 positioning.
The exact auxiliary proposal
\(P_{\mathrm{intr}}\#\mathrm{MIX}_2^+\$ \{c^nd^ne^n:n\ge1\}\)
was not adopted: reusing \(c,d\) from the marker prefix makes the proposed
regular wrapper fail to be strictly 2-local and prevents the advertised single
abelian-kernel factorization.  v58 uses fresh suffix terminals
\(\mathtt u,\mathtt v,\mathtt w\), which removes both problems.

## New witness

Let
\[
P_{\mathrm{intr}}
=\{\mathtt{lpc},\mathtt{lpd},\mathtt{lqc},
  \mathtt{rpc},\mathtt{rpd}\},
\]
\[
\mathrm{MIX}_2^+
=\{x\in\{\mathtt a,\mathtt b\}^+:
  |x|_{\mathtt a}=|x|_{\mathtt b}\},
\]
and
\[
T_3^+=\{\mathtt u^n\mathtt v^n\mathtt w^n:n\ge1\}.
\]
The v58 target is
\[
L_{\mathrm{intr}}
=
P_{\mathrm{intr}}\mathtt{\#}
\mathrm{MIX}_2^+\mathtt{\$}T_3^+.
\]

The theorem now proves:

- \(L_{\mathrm{intr}}\in\mathsf{MCFL}(2,2)\);
- \(L_{\mathrm{intr}}\notin\mathrm{CFL}\), so its minimum fan-out is two;
- for every \(f\ge2\),
  \(L_{\mathrm{intr}}\in
  \mathcal C^{\mathrm{mcf}}_{f,h_{\Sigma_{\mathrm{intr}}}^{1,1}}\);
- for every \(f\ge1\),
  \(L_{\mathrm{intr}}\notin\mathsf{YSub}(f)\);
- for every finite \(f'\ge1\),
  \(L_{\mathrm{intr}}\notin\mathsf{MCFL}(f',1)\).

Hence the same language has minimum fan-out exactly two and minimum rule rank
exactly two, where the rule-rank minimum ranges over all finite-fan-out MCFG
presentations.

## Reviewer-style proof audit

### Explicit grammar

The old balanced-count nonterminal \(B\) is retained.  A fan-out-two
nonterminal \(A\) is added:
\[
A\to(\mathtt u,\mathtt w)
\mid
(\mathtt u\xi_1^1\mathtt v,\mathtt w\xi_1^2)(A).
\]
It derives exactly
\[
(\mathtt u^n\mathtt v^{n-1},\mathtt w^n),\qquad n\ge1.
\]
A start rule
\[
S\to
\alpha\mathtt{\#}\xi_1^1\mathtt{\$}
\xi_2^1\mathtt v\xi_2^2(B,A)
\qquad(\alpha\in P_{\mathrm{intr}})
\]
therefore generates exactly the new target.

The presentation has fan-out two and maximum rule rank two.  It is reduced,
nondeleting, nonpermuting, \(\lambda\)-free, and nonmerging; in particular,
the two components of \(A\) are separated by the literal terminal
\(\mathtt v\) in the start rule.

### Minimum fan-out

Intersecting with
\[
\mathtt{lpc\#ab\$}\mathtt u^+\mathtt v^+\mathtt w^+
\]
isolates
\[
\{\mathtt{lpc\#ab\$}\mathtt u^n\mathtt v^n\mathtt w^n:n\ge1\}.
\]
Erasing the fixed prefix gives
\(\{\mathtt u^n\mathtt v^n\mathtt w^n:n\ge1\}\), so the target is not
context-free.  Since fan-out-one MCFGs are CFGs in the present syntax and the
displayed grammar has fan-out two, the minimum fan-out is exactly two.

### Boundary-typed membership

Put
\[
Q_{\mathrm{intr}}
=
P_{\mathrm{intr}}\mathtt{\#}\{\mathtt a,\mathtt b\}^+
\mathtt{\$}\mathtt u^+\mathtt v^+\mathtt w^+.
\]
With the fresh suffix alphabet this language is strictly 2-local.

Define
\[
\Phi_{\mathrm{intr}}:\Sigma_{\mathrm{intr}}^*\to\mathbb Z^3
\]
by
\[
\Phi_{\mathrm{intr}}(\mathtt a)=(1,0,0),\qquad
\Phi_{\mathrm{intr}}(\mathtt b)=(-1,0,0),
\]
\[
\Phi_{\mathrm{intr}}(\mathtt u)=(0,1,0),\qquad
\Phi_{\mathrm{intr}}(\mathtt v)=(0,-1,1),\qquad
\Phi_{\mathrm{intr}}(\mathtt w)=(0,0,-1),
\]
with all other terminals mapped to zero.  Then
\[
L_{\mathrm{intr}}
=
Q_{\mathrm{intr}}\cap\Phi_{\mathrm{intr}}^{-1}(0).
\]
The three coordinates impose the balanced \(a/b\) condition and the two
equalities needed for \(u^nv^nw^n\).  The existing strictly-2-local boundary
lemma and abelian-filter proposition therefore give
\((f,h^{1,1})\)-tuple substitutability for every \(f\), and the explicit
fan-out-two grammar gives typed-class membership for every \(f\ge2\).

The allowed-bigram description was checked mechanically against the regular
expression for \(Q_{\mathrm{intr}}\) on all accepted paths up to length 18;
no spurious word was found.  The balanced grammar for \(B\) was also checked
exhaustively through length 10 against the predicate
\(|x|_{\mathtt a}=|x|_{\mathtt b}\).

### Yoshinaka separation

The v57 one-hole rectangle survives after appending the new suffix:
\[
x=\mathtt p,\qquad y=\mathtt q,
\]
\[
E=\mathtt l\Box\mathtt{c\#ab\$uvw},\qquad
F=\mathtt r\Box\mathtt{d\#ab\$uvw}.
\]
The first three corners are in the target and \(F[y]\) is not.  Thus the
arity-one substitution implication fails, and therefore the target is outside
\(\mathsf{YSub}(f)\) for every \(f\ge1\).

### Intrinsic rule rank

The homomorphism fixing \(\mathtt a,\mathtt b\) and erasing all other
terminals maps the new target exactly onto \(\mathrm{MIX}_2^+\).  Hence a
rank-one presentation at any finite fan-out would yield one for
\(\mathrm{MIX}_2^+\), and adding epsilon at a fresh start symbol would yield
one for \(\mathrm{MIX}_2\).

The primary Gallot source was rechecked.  Definition 38 defines non-branching
MCFGs by one-child positive-rank rules.  Proposition 5 converts any such
grammar for \(\mathrm{MIX}_2\) into a uniform \(k\)-derivation bound, while
Proposition 6 gives, for every \(k\), a counterexample word.  Theorem 29
identifies non-branching MCFLs with finite-index EDT0L, and Theorem 31 records
the resulting finite-index lower bound.  The manuscript now cites this chain
explicitly rather than making Theorem 31 alone carry the MCFG implication.

Bishop--Elder--Evetts--Gallot--Levine (2026) is retained as a peer-reviewed
expanded treatment proving the stronger non-EDT0L statement, but the v58 proof
states explicitly that Theorem C is not needed for the MCFG lower-bound step.

## Separation-role clarification

The strengthened intrinsic-rank witness is not used to separate arbitrary
target-dependent regular filtering.  In fact,
\[
L_{\mathrm{intr}}
=
\Phi_{\mathrm{intr}}^{-1}(0)\cap Q_{\mathrm{intr}},
\]
with the abelian kernel in Yoshinaka's trivial-typing class and
\(Q_{\mathrm{intr}}\) regular.  Thus
\(L_{\mathrm{intr}}\in\mathcal F_f^{\mathrm{arb}}\) for every \(f\ge2\).

The division of labor is now explicit:

- \(L_{\mathrm{intr}}\): minimum fan-out two + intrinsic minimum rule rank two
  + boundary typing + separation from the trivial-typing class;
- \(L_\star\): separation from arbitrary target-dependent regular filtering.

## Positioning changes

The Abstract, Contribution (3), the scope paragraph after the higher-rank
theorem, the comparison-section overview, the discussion after
\(L_\star\), and the Conclusion now describe the witness as non-context-free
with minimum fan-out two and intrinsic minimum rule rank two.

References to "outside Yoshinaka's class" for this witness were tightened to
"outside Yoshinaka's trivial-typing class."

## Static checks

After the v58 edit:

- no duplicate labels;
- no duplicate bibliography keys;
- no unresolved \`ref\` / \`eqref\` targets;
- no unresolved citation keys;
- all \`begin\` / \`end\` environment counts match;
- unescaped brace balance is zero.

The only bibliography item currently unused in the manuscript remains
\`Clark2010Congruential\`, a pre-existing v57 issue unrelated to this revision.
A full TeX-engine build was not run through the GitHub connector; the new
dollar-terminal notation was separately syntax-checked with pdfLaTeX.

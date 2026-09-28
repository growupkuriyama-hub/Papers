# MCFG v56 -> v57 revision note

## Purpose

v57 adds a corrected and strictly stronger language-level witness for the
higher-rank characteristic-data theorem.

The v56 manuscript deliberately withdrew the earlier \(L_{\mathrm{r2}}\)
example after an explicit fan-out-two rule-rank-one grammar invalidated its
lower bound.  The replacement witness in v57 uses the known non-branching MCFG
lower bound for the balanced-count language \(\mathrm{MIX}_2\), and then wraps
that language in a strictly local marker skeleton so that the resulting target
is \((1,1)\)-boundary typed but lies outside Yoshinaka's trivial-typing class.

## New witness

Let

\[
P_{\mathrm{intr}}
 =\{\mathtt{lpc},\mathtt{lpd},\mathtt{lqc},
     \mathtt{rpc},\mathtt{rpd}\},
\]

\[
\mathrm{MIX}_2^+
 =\{w\in\{\mathtt a,\mathtt b\}^+:
     |w|_{\mathtt a}=|w|_{\mathtt b}\},
\]

and

\[
L_{\mathrm{intr}}
 =P_{\mathrm{intr}}\mathtt{\#}\mathrm{MIX}_2^+.
\]

The new theorem proves:

- \(L_{\mathrm{intr}}\) has a reduced good fan-out-one MCFG of rule rank two;
- \(L_{\mathrm{intr}}\in
  \mathcal C^{\mathrm{mcf}}_{1,h^{1,1}}\);
- \(L_{\mathrm{intr}}\notin\mathsf{YSub}(1)\);
- for every finite \(f'\ge1\),
  \(L_{\mathrm{intr}}\notin\mathsf{MCFL}(f',1)\).

Hence the minimum rule rank of the language is exactly two even when competing
MCFG presentations may use arbitrary finite fan-out.

This is stronger than the withdrawn v55 claim, which only attempted to rule
out fan-out-two rank-one presentations.

## Membership and separation checks

The target is written as

\[
L_{\mathrm{intr}}
 =Q_{\mathrm{intr}}\cap\varphi^{-1}(0),
\]

where
\(Q_{\mathrm{intr}}=P_{\mathrm{intr}}\mathtt{\#}\{\mathtt a,\mathtt b\}^+\)
is strictly 2-local and
\(\varphi(\mathtt a)=1,\ \varphi(\mathtt b)=-1\), with all marker letters
mapped to \(0\).  The existing strict-2-local boundary lemma and abelian-filter
proposition therefore give typed membership.

The explicit Yoshinaka substitution rectangle uses

- \(x=\mathtt p\),
- \(y=\mathtt q\),
- \(E=\mathtt l\,\square\,\mathtt{c\#ab}\),
- \(F=\mathtt r\,\square\,\mathtt{d\#ab}\).

The first three corners are in \(L_{\mathrm{intr}}\), while
\(F[y]\) is not.  The \((1,1)\) typing distinguishes the one-letter factors
\(\mathtt p\) and \(\mathtt q\).

## Intrinsic rank lower bound

The terminal homomorphism erasing all marker symbols and fixing
\(\mathtt a,\mathtt b\) maps \(L_{\mathrm{intr}}\) exactly onto
\(\mathrm{MIX}_2^+\).

Paul Gallot's 2021 thesis defines a non-branching MCFG as an MCFG whose
positive-rank rules have a single child nonterminal (Definition 38).  Under the
rule-rank convention of the present paper this is exactly rule rank at most
one, with arbitrary finite nonterminal arities.  Because every finite grammar
has a finite maximum arity, Gallot's non-branching MCFL class is

\[
\bigcup_{f'<\infty}\mathsf{MCFL}(f',1).
\]

Gallot's proof of Theorem 31 (via Propositions 5 and 6) shows that

\[
\mathrm{MIX}_2
 =\{w:|w|_{\mathtt a}=|w|_{\mathtt b}\}
\]

is not in this class.  Bishop--Elder--Evetts--Gallot--Levine (2026) give a
peer-reviewed expanded proof for the same language, viewed as the word problem
of the infinite cyclic group, and prove that it is not EDT0L.

If \(L_{\mathrm{intr}}\) had a rank-one presentation at any finite fan-out,
terminal homomorphism would give a rank-one presentation of
\(\mathrm{MIX}_2^+\); adding a fresh start symbol with a unary link and a
rank-zero epsilon rule would then give a rank-one presentation of
\(\mathrm{MIX}_2\), contradiction.

## Positioning changes

The abstract, Contribution (3), the discussion after the boundary theorem,
the comparison-section overview, and the Conclusion now state the intrinsic
rank-two result.

The v56 open problem asking whether any typed language has intrinsically
higher rule rank has been removed because v57 answers it positively.  The
remaining original-thickness open problem is unchanged.

The manuscript explicitly distinguishes the prior lower-bound ingredient from
the new contribution: the strictly local boundary-typed wrapper, its
Yoshinaka separation, and its connection to the quantitative learning theorem.

## Sources added

- P. D. Gallot, *Safety of transformations of data trees: Tree transducer
  theory applied to a verification problem on shell scripts*, PhD thesis,
  Université de Lille, 2021.  Relevant locations: Definition 38,
  Propositions 5--6, Theorem 31.
- A. Bishop, M. Elder, A. Evetts, P. Gallot, A. Levine,
  *On groups with EDT0L word problem*, International Journal of Algebra and
  Computation 36(4):425--486, 2026, DOI 10.1142/S0218196726500165.
  Relevant locations: Definition 7.1 and Theorem C.

## Static checks

- no unresolved \`ref\` / \`eqref\` targets;
- no unresolved citation keys;
- no duplicate labels;
- no duplicate bibliography keys;
- all \`begin\` / \`end\` environment counts match;
- unescaped brace balance is zero.

A full TeX-engine build was not run in this connector-only pass.

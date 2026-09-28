
# MCFG v47 -> v48 revision note

## Purpose

v48 adds a concrete language-level witness showing that the higher-rank
prefix--suffix theorem is genuinely needed beyond the rank-one regime.

The new target is fan-out two, has minimum rule rank exactly two, belongs to
the fixed `(1,1)` boundary-typed class, and lies outside Yoshinaka's
trivial-typing baseline.  This removes the principal scope limitation left
explicit in v47.

## Main change: a genuinely rank-two typed target

A new subsection, `A Genuine Minimum-Rank-Two Boundary-Typed Target`, defines

`L_r2 = #0 a1^n1 b1^n1 c1^n1 #1 a2^n2 b2^n2 #2 a3^n3 b3^n3 #3 a4^n4 b4^n4 #4`

with all exponents positive and the five separator symbols distinct.

The new Theorem `thm:genuine-ranktwo-witness` proves simultaneously that

- `L_r2` is in `MCFL(2,2)`;
- `L_r2` is in the `(2, h^{1,1})` finite-typed class;
- `L_r2` is not in `MCFL(2,1)`;
- `L_r2` is not in Yoshinaka's `YSub_2`.

Hence its minimum rule rank among fan-out-two MCFG presentations is exactly
two, and the higher-rank characteristic-data theorem applies to a language
that the rank-one theorem cannot cover.

## Proof ingredients

1. **Explicit rank-two MCFG.**
   A self-contained fan-out-two rank-two grammar is given.  The first tuple
   component generates the triple-equality block
   `a1^n b1^n c1^n`; the other tuple nonterminals generate the three
   double-equality blocks, and rank-two `B_i` rules concatenate the four blocks.

2. **Membership in the `(1,1)`-typed class.**
   The regular skeleton with five distinct separators is strictly 2-local.
   Intersecting it with the kernel of the abelian counting homomorphism to
   `Z^5` enforces the five required count equalities.  The existing strictly
   2-local lemma plus the abelian-filter proposition therefore place the target
   in `C^{mcf}_{2,h^{1,1}}`.

3. **Minimum rank two.**
   A terminal homomorphism erases `c1` and identifies the five separators.
   The image is the standard four-block language recorded by Kato, Seki, and
   Kasami as belonging to `CFL \ SL-TAL`.  Kato's 2005 thesis proves
   `SL-TAL = (2,1)-MCFL` (Theorem 18).  Since applying a terminal homomorphism
   to MCFG rule templates preserves fan-out and rule rank, a rank-one
   presentation of `L_r2` would yield a rank-one presentation of that known
   separator language, contradiction.

4. **Outside Yoshinaka's baseline.**
   An explicit arity-one substitution rectangle is given:
   `x=b1`, `y=a1 b1^2 c1`, with two displayed one-hole contexts.
   Three corners are in the language and the fourth is not.  The `(1,1)`
   typing distinguishes `x` and `y`, explaining directly why the typed
   condition blocks the overgeneralization.

## Prior-work verification

The external ingredients were checked against:

- Y. Kato, H. Seki, and T. Kasami, *Subclasses of Tree Adjoining Grammar for
  RNA Secondary Structure*, TAG+ 2004, pp. 48--55.  The paper records the
  four-block separator language as a member of `CFL \ SL-TAL`.
- Y. Kato, *Studies on the Generative Power of Grammars for Describing RNA
  Secondary Structure*, master's thesis, NAIST, 2005.  Theorem 18 proves
  `SL-TAL = (2,1)-MCFL`.

Both references are now included in the bibliography.

## Positioning changes

- The abstract no longer says that genuinely higher-rank language territory is
  open; it now cites the minimum-rank-two witness.
- Contribution (2) is retitled to emphasize genuine higher rank.
- The discussion immediately after the boundary theorem now points forward to
  the new witness.
- The comparison-section overview and conclusion now state explicitly that the
  higher-rank theorem reaches language-level territory outside the rank-one
  theorem.
- The old paragraph saying that no minimum-rank-greater-than-one witness was
  known has been removed.

## Checks

- Static label scan: no duplicate labels.
- Static reference scan: no unresolved `ref` / `eqref` targets.
- Static bibliography scan: no unresolved citation keys.
- All `begin` / `end` environment counts match.
- Unescaped brace balance is zero.
- A full TeX-engine build was not run in this connector-only pass.

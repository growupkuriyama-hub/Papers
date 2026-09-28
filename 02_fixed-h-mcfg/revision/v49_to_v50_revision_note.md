# MCFG v49 -> v50 revision note

## Purpose

v50 implements the second medium pre-submission review item: make the
notation bridge in the minimum-rank-two lower-bound argument explicit.

## Change

Immediately after citing Kato (2005), Theorem 18, the manuscript now states
that Kato's MCFG **dimension** is the maximum nonterminal tuple dimension and
Kato's **rank** is the maximum number of arguments of a rule function.  These
are exactly the parameters called **fan-out** and **rule rank** in the present
paper.

Consequently, the text now says explicitly that Kato's `(2,1)-MCFL` is
precisely `MCFL(2,1)` in the notation of this paper.

The convention is cited to Kato, Seki & Kasami (2004), Section 2.2.

## Scope

No theorem statement, language definition, grammar, homomorphism, or lower
bound changed.  This is a notation/citation clarification only.

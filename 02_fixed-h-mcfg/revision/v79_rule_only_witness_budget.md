# MCFG #2 v79 — rule-only characteristic witness certificate

Working date: 2026-10-18. Independent from Claude's higher-fan-out lower-bound exploration.

## Statement

For a trimmed good yield-typed presentation, select for each non-start
typed nonterminal X a minimum-weight terminal derivation, comparing
(terminal length, number of derivation nodes) lexicographically.
Select all canonical tuples omega(X) using the resulting acyclic
minimizing-rule DAG.

If the chosen minimizing rule at X is R_X: X -> rho_X(Y_1,...,Y_q),
then, including rank zero,
  omega(X) = rho_X(omega(Y_1),...,omega(Y_q)).
Thus the nonterminal witness chi(X)[omega(X)] is already exactly the
rule witness for R_X.  The old witness set from Definition
def:witness-set therefore equals the set of rule witnesses alone.

The refined cardinality certificate is |Wit| <= |R_typed|,
rather than |N_typed| + |R_typed|.

The computable total-length certificate is
  B_rule(G,h) =
    sum_{R in R_typed}
      (1 + mu(lhs(R)) + c_R + sum_child lambda(Y)).
The exact same characteristic set obeys ||Wit||_+ <= B_rule(G,h).
The bound is polynomial-time computable in the grammar size, in binary,
when f, rank, typing and alphabet are fixed.

## Why this is valid

- Additive minimum-weight deductions have the optimal-substructure
  property. Each chosen root minimizing rule uses shortest child
  derivations.
- Breaking equal-length ties by minimum derivation node count
  prevents cyclic choices when rules can write zero terminals.
- Every productive non-start typed nonterminal X has an outgoing
  non-start typed rule to choose.
- Canonical contexts remain arbitrary admissible ones, e.g. minimum
  outside length contexts. The same chi(X) is used for the canonical
  and rule witness.
- Set equality is literal equality of terminal words, so the
  established completeness and soundness results are preserved
  without a new learner argument.

## Quantitative scope

This reduces the number of selected sample words and the explicit
presentation-sensitive budget, but does NOT lower the worst-case
polynomial exponents 2 (window only) and 3 (local groups). It also
does not establish any fan-out-two sample-length lower bound.

## Tiny strict-improvement example

For trivial typing and S -> A, A -> a, with A the only non-start
nonterminal, the old counting scheme includes twice the same word
"a": once for A and once for A -> a. Rule-only selection includes
one occurrence. Old indexed budget is 2*(1+1)=4 while the new
rule-only budget is 1+1=2; both refer to the same characteristic
sample {"a"} with encoded size 2.

## Verification priorities

Check the canonical tuple identity simultaneously for all typed
symbols, including rank-zero rules and tie cases. Check the
target's positivity, start-link and epsilon conventions. Check
bilingual label and citation equality; compile both PDFs.
Full independent mathematical review and author signoff remain
separate publication requirements.

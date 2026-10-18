# #2 fixed-h MCFG — v77 candidate: computable data budgets

Date: 2026-10-18.
Branch: `mcfg2-v77-computable-data-budget`.
Status: **draft, not merged, not independently human-reviewed**. V76 remains the pre-submission main baseline.

## What is proposed

Proposition `prop:computed-witness-budget` defines, for a fixed typed reduced good presentation,
a computable *presentation-sensitive* witness-budget
```
B(G,h) = sum_X (1 + outside_min(X) + inside_min(X))
       + sum_R (1 + outside_min(lhs(R)) + explicit_terminals(R)
                    + sum_child inside_min(child)).
```
The witness set from `def:witness-set` using shortest typed tuples and
derivational contexts has encoded total positive length at most `B(G,h)`.
The number is computed in binary polynomial time with fan-out, rank, and
typing fixed. Optional empty-word evidence adds one to the encoded total.

This does not change worst-case exponents (2 for window, 3 for group/LG).
It is an instance-sensitive *upper certificate*, and does not optimize
among all characteristic samples.

## Proof cross-check

- The chosen context is valid for **every** tuple of its typed
  nonterminal by Lemma `lem:identity-canonical-contexts`.
- Every selected nonterminal word has exact length `mu(X)+lambda(X)`.
- Every selected rule word has exact length `mu(X)+c_R+sum lambda(Y_i)`,
  including rank zero.
- The indexed multiset can include duplicate words. Passing to the
  witness *set* can only decrease the encoded total.
- Proposition `prop:effective-char-data` supplies the inside/outside
  values and polynomial-time computation; nonnegative weights with
  tie-breaking prevent cyclic derivation pointers.

## Next deeper questions (not claims)

1. Can a better *amortized* upper bound be obtained by sharing expensive
   typed representatives among many rule witnesses **as plain strings**
   rather than just as DAGs? Ordinary positive-data size counts repeated
   terminal occurrences, so DAG sharing by itself does **not** reduce the
   data total.
2. Does some family force characteristic-data length
   `Omega(||G||^2 theta)` in the window case, or
   `Omega(||G||^3 theta)` in the local-group case?
   A lower bound for this specific witness construction is not sufficient
   to claim an operator-independent lower bound.
3. Is a fan-out-two semilattice lower-bound family possible while
   retaining full `(2,h)` substitutability? The existing doubling
   family fails this condition; naive embedding is invalid.

## Review gates

Check the new proposition's counting against all rank-zero cases, optional
epsilon, and the precise reconstruction operator. Dedicated bilingual
compilation and references. Do not alter main journal submission before
reviewing this separately.

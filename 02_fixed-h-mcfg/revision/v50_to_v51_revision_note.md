# MCFG v50 -> v51 revision note

## Purpose

v51 implements the third medium pre-submission review item: qualify the
higher-rank characteristic-data claim in the abstract so that it matches the
precise hypothesis of the theorem in the body.

## Change

The abstract previously said that, at arbitrary fixed rank, prefix--suffix
typings admit a polynomial bound in grammar size and rule thickness.

It now states explicitly that this characteristic-data bound is for
**reduced good presentations**, matching Theorem
`thm:boundary-polydata`.

The theorem's separate transfer clause for reduced lambda-free input
presentations remains unchanged in the body.

## Scope

No theorem, proof, asymptotic bound, or learning claim changed.  This is a
scope-precision edit to prevent the abstract from being read as a statement
about arbitrary original presentations with empty tuple components.

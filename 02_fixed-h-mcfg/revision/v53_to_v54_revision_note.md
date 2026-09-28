# MCFG v53 -> v54 revision note

## Purpose

v54 implements the remaining minor review suggestion concerning the empty
word in the rank-one characteristic-data theorem.

## Change

The statement of Theorem `thm:rankone-polydata` now says explicitly that if
the target contains the empty word, the characteristic sample includes the
single direct-start datum `epsilon`, following the global reconstruction
convention.  Because this datum has length zero, it does not alter the stated
total-positive-length bound.

## Scope

No proof, asymptotic estimate, learner, or target class changed.  The edit only
makes the existing empty-word convention explicit at the theorem where a
reader is most likely to check the quantitative claim.

# v84 → v85 citation-source audit

Date: 2026-10-02

This revision changes literature attribution only. No theorem, definition, proof,
algorithm, complexity bound, or scope claim is changed.

## Changes

1. **Kanazawa**
   - Current manuscript: cite Kanazawa (1996), *Identification in the Limit of Categorial Grammars*, for positive-data learnability of fixed-`k` / `k`-valued classical categorial grammars.
   - Removed the direct dependence on the later 1998 monograph from the current manuscript.
   - The historical first-submission snapshot remains untouched.
   - DOI added: `10.1007/BF00173697`.

2. **Finite-monoid characterization**
   - Replaced the direct citation to Eilenberg (1974) in Proposition 3.1 with the directly checked modern account:
     Jean-Éric Pin, *Mathematical Foundations of Automata Theory*, version of March 24, 2025.
   - The proof itself remains explicit and unchanged apart from the citation.

3. **Thickness attribution**
   - The manuscript now cites Yoshinaka (2008) for the thickness discussion and states that Yoshinaka attributes the parameter to Wakatsuki and Tomita.
   - The direct citation to Wakatsuki–Tomita (1993) has been removed from the current manuscript because that original has not been independently checked in the project.
   - No quantitative theorem changes.

## Response to reviewers

The Round-1 response letter now records this bibliographic audit in the overview.
The response to Reviewer 2, comment R2.5, identifies Pin as the cited modern source
for the standard finite-monoid characterization.

## Current status

- English manuscript: internal v85.
- Japanese reference manuscript: same citation-source audit synchronized.
- Round-1 response letter: citation-audit paragraph synchronized.
- LaTeX CI: current TeX state compiles successfully for the English manuscript,
  response letter, and Japanese reference manuscript.

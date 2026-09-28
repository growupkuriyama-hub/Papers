# v58 → v59 revision note

Date: 2026-09-29

## Purpose

This is a pre-submission citation-and-positioning hardening pass after independent review of the v58 manuscript.  The mathematical architecture, theorem statements, reconstruction algorithm, and quantitative bounds are unchanged.

## Changes

1. **COPY attribution corrected.**  The manuscript no longer attributes the separator-free language `COPY={ww}` to Yoshinaka's Example 5, which treats the related separator-marked copy language.  The finite-typing obstruction remains proved directly in the manuscript.
2. **Gallot lower-bound bridge made source-explicit.**  The intrinsic-rank proof now cites Gallot's Theorem 28 for the non-erasing/non-permuting normalization used by the non-branching lower-bound argument, in addition to Theorem 29, Propositions 5--6, and Theorem 31.
3. **Bishop et al. locator strengthened.**  The peer-reviewed comparison now points to the non-branching/R-MCFG material in Definition 6.1, Lemma 6.8, and Section 7, while retaining Theorem C only as the stronger non-EDT0L statement.
4. **Intrinsic-witness positioning clarified.**  The text now states explicitly that the construction is modular: the `MIX2^+` factor carries the rule-rank-one obstruction, while the `T3^+` factor forces the target outside CFL and hence to minimum fan-out two.  The theorem establishes coexistence of these two lower bounds in one finitely typed target and does not claim an irreducible interaction between them.
5. **Yoshinaka normalization locator tightened.**  The size statement is located in Section 2.3 after Example 2 rather than described as occurring immediately after Lemma 1.
6. **Unused bibliography removed.**  The uncited `Clark2010Congruential` entry was deleted.

## Deliberate non-change

The proof that
`H_m={a_1^n ... a_{2m}^n:n>=1}`
has minimum fan-out `m` is retained.  Original-source verification confirms that Seki et al.'s Lemma 3.3, with parameter `m-1`, gives the `2m-1`-block lower-bound language used in the current homomorphic argument.

## Baseline hashes

- v58 `main.tex` SHA-256: `48bf5d5805d1d18b2e2804d1f35bb4263968cd3ca0df0638fca2d0d3166b4b33`
- v59 `main.tex` SHA-256: `1fee043a6c0e748c917e7cc1811ffeb656ae7f74097a95fbbc5dc49510bc3a79`

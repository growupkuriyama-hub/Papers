# v60 → v61 submission-hardening revision

## Purpose

v61 incorporates the final pre-submission audit of the fixed-h MCFG manuscript.  It does not change the learner architecture or any theorem statement.  The revision tightens citation scope, prior-work positioning, and the interpretation of the intrinsic-rank witness.

## Changes

1. **Uniform recognition attribution.**  The bounded-rank learner now cites Yoshinaka (2011), Proposition 4, for the polynomial membership bound jointly in grammar encoding size and input length when fan-out and rule rank are fixed.  Seki et al. and Kallmeyer are retained as classical recognition/parsing background rather than as the sole support for this uniform complexity claim.
2. **Seki normalization scope.**  The good-normalization discussion now states explicitly that it uses only the nondeleting/information-lossless step (f3) from the proof of Seki et al.'s Lemma 2.2, together with Kanazawa's rank-preserving formulation, rather than attributing rank preservation to the whole of Lemma 2.2.
3. **Yoshinaka locator synchronization.**  The remaining locator is corrected from “immediately after Lemma 1” to “after Example 2”.
4. **Intrinsic-rank witness positioning.**  The manuscript now records explicitly that MIX2+ already belongs to Yoshinaka's trivial-typing class (and is context-free), so the intrinsic rule-rank-two obstruction itself is not created by finite typing.  The role of L_intr is stated as combining that known obstruction with non-context-freeness, minimum fan-out two, and separation from the trivial-typing baseline in one boundary-typed target.
5. **Gallot/Bishop bridge.**  Gallot remains the direct non-branching MCFG lower-bound route.  Bishop et al. are strengthened as an independent peer-reviewed corroborating route via Definition 6.1, Lemma 6.8, and Section 7, with Theorem C identified as the stronger non-EDT0L conclusion.
6. **Defensive prose reduction.**  Several repeated “not claimed / no assertion” formulations are rewritten affirmatively while preserving theorem scope.

## Preserved architecture

The batch reconstruction, conservative TxtEx learner, characteristic-sample construction, rank-one theorem, boundary/thickness theorem, L_cd, H_m, J_s, L_star, and the statement of the L_intr theorem are unchanged.

## Validation

The update script required every intended source block to occur exactly once before replacement.  A static LaTeX sanity check preserved begin/end-environment counts and verified balanced unescaped braces.  Repository CI job `pdfLaTeX — 02 fixed-h MCFG` completed successfully for commit `cf763448303cab7e327403d86753b650c86f338c`, providing the full manuscript build check.

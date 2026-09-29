# v63 → v64 citation-hardening pass

## Purpose

v64 is a deliberately small pre-submission hardening pass following the independent audit of v63. It does not change any theorem, proposition, lemma, corollary, definition, example, open problem, construction, or proof dependency.

## Main edit

- Strengthened the Bishop et al. corroboration paragraph in the intrinsic-rank-two witness.
- Made the source chain explicit through Proposition A, Proposition 6.2, Remark 6.3, Definition 6.1, Lemma 6.8, Definition 7.1, Section 7, and Theorem C.
- Preserved Gallot (2021) as the direct source for the non-branching MCFG lower bound actually used by the proof.
- Clarified that Bishop et al. provide an independent corroborating route rather than the primary implication.

## Safety constraints

- No mathematical statement is changed.
- No theorem scope is enlarged.
- No new novelty claim is introduced.
- The exact reconstruction, TxtEx learner, quantitative bounds, and all separation witnesses are untouched.
- The manuscript remains source-compatible with the v63 38-page baseline apart from the local citation/prose expansion.

## Audit rationale

The v63 argument was mathematically sound, but the Bishop paragraph compressed several formal correspondences into a short citation chain. The v64 wording makes those intermediate source points visible so that a reviewer cannot reasonably read Theorem C alone as the direct MCFG rank-one obstruction. The proof itself continues to rely on Gallot's direct non-branching MCFG lower bound.

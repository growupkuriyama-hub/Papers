# MCFG #2 v68 → v69: I&C referee-audit corrections

Date: 2026-10-17 (JST)
Branch: `revision/02-v69-ic-referee-corrections`
Source of truth: `02_fixed-h-mcfg/main.tex`
Status: **v69 revision candidate; current CI and merge state are tracked by [PR #31](https://github.com/growupkuriyama-hub/Papers/pull/31).**

## Source and audit basis

- Uploaded external review: `MCFG02_IC_Comprehensive_Referee_Audit_and_v69_Revision_Plan_20261017.md`.
- Companion TCS #1: `01_fixed-h-cfg/main.tex` (at pinned revision `7f4c680e3a896b41b748970d75d5084fa6e08e6d`).
- Paul Gallot (2021), *Safety of transformations of data trees*, thesis, Definition 38 and Theorems 28–29, 31: source read and theorem numbering directly checked against https://pepite-depot.univ-lille.fr/LIBRE/EDMADIS/2021/2021LILUB030.pdf
- Yoshinaka (2015) MoL framework, Section 7, and Yoshinaka (2011) grammar normalizations.

## Mathematically substantive changes

1. **P0 corrected.** The original conclusion claimed that the arbitrary-typing original-thickness polynomial bound was open even for fan-out 1/rank 2. This is false by the bracketed-doubling distinguishing-pair example in the companion CFG paper. New `prop:fanout-one-lower-bound` proves the operator-independent exponential positive-data lower bound for the fixed `h_U` typed `(1,2)` class. The lower bound is explicitly attributed to #1 and does *not* pretend to be an independent new MCFG construction.
2. **Open problem properly narrowed.** New `op:fanout-two` asks for a higher-fan-out analogue, without asserting that the #1 family fails $(f,h)$-substitutability for every `n` or that the answer for `f>=2` is known.
3. **Signature/primal correspondence promoted to a lemma.** `lem:substp` explicitly compares per-sample generated languages, including the start sort, promotion and epsilon. An accompanying prose paragraph relates the witness families. No syntax-level identity is claimed.
4. **Gallot source scope checked and clarified.** Definition 38 permits erased child variables; Theorem 28 normalizes non-branching grammars; Theorem 29 equates this class with finite-index EDT0L; Theorem 31 rules out MIX2. No unverified converse is needed.

## Editorial / positioning changes

5. Abstract and contribution list now center the multiple-component `thm:boundary-polydata` theorem and the upper/lower length boundary, with rank-one a supporting elementary case.
6. Repeated priority accounts reduced in the Introduction. Exact signature correspondence moved out of Preliminaries to its own section **after** the reconstruction definitions and results, reducing forward-definition usage.
7. The characteristic-data comparison table now includes the actual fan-out-one lower bound rather than only full-refinement thickness blow-up.
8. Companion preprint citation corrected from unpublished arXiv v5 to public v4; proof in the *revised*, not public, version is linked to a pinned GitHub revision for referees.
9. No unreviewed finite-abelian-group extension has been inserted. The proposed proof in the Claude audit remains independently unverified, as does the nonabelian case.

## Verification and deferred work

- [x] Distinct labels and resolved `\\ref` and `\\cite` in source (static scans during edits).
- [x] Standard theorem/proof/list environment counts balanced during edits.
- [x] CI pdfLaTeX full build for first v69 source: run 39015572350, 42 pages, successful; final bibliography link display shortened afterward, so check PR #31 for the latest source build.
- [ ] Full manual rendered-PDF inspection (not asserted from CI alone).
- [ ] Independent mathematical referee review of the inserted lemma/lower-bound proof (source-priority checked but not externally refereed).
- [ ] Full 30–35 page structural compression while preserving detailed proofs.
- [ ] Review whether current journal guidelines require a generative-AI usage declaration, and obtain author confirmation of its exact wording before adding any declaration on the author's behalf.
- [ ] Elsevier-specific submission template and journal formatting check.
- [ ] Optional window–finite-abelian-group extension, but **only after independent proof verification**.

No changes to #1 or other paper projects. No I&C portal submission and no arXiv upload. Main-branch merge state is the live state of PR #31, not a claim made by this static note.

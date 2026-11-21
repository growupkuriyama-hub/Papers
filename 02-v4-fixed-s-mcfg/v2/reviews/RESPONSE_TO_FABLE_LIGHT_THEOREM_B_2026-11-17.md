# Response to Fable differential referee review — light Theorem B (2026-11-17)

**Scope and base:** Fable report `paper02_lightThmC_diff_referee_2026-11-17.md`, based on Git commit `97d87d727202fd8f1491afa898810ac7253add97`; proposed changes in branch `paper2/fable-light-thmB-precision-2026-11-17`. This response is an editorial revision record, not a journal referee decision. The source label `thm:C` prints as **Theorem B**. Theorem A and its proof chain were not modified or independently re-audited in this response.

## Disposition of Fable findings

| Item | Response in EN/JA source |
| --- | --- |
| P1 | Main Theorem B and Theorem 6.*(iii) now explicitly quantify the two reconstruction operators and, separately, any set-driven operator with characteristic samples for both the target and its one-word deletion. |
| P2 | Replaced claims that the *polynomial bound* is "sharp" with exactness of the **local-group hypothesis at the pseudovariety level**. Explicitly do not claim optimality of the polynomial exponent. |
| P3 | Added rank cap at least two to abstract, introductory bridge, Section 6 lead, conclusion and scope remark; rank-one boundary is not claimed. |
| P4 | Restricted the comparison with the companion to **reduced good bounded-rank presentations and rule thickness** under the current definition; no thickness-preserving good normalization for arbitrary CFG presentations is claimed. |
| P5 | Kept the lower-bound family's source and proof in the companion's Proposition 6.4 and Appendix C. Explicitly identified arXiv:1409.6247v5 citation locators in Section 6; did not copy the parser proof, overstate journal status, or treat a hypothetical editorial decision as fact. |
| P6 | Clarified that excluding the two-element semilattice is a purely algebraic equivalence from the local-group criterion, applicable to abstract finite semigroups. |
| P7 | Replaced "verbatim"/"word for word" by equality of definitions **up to notation**; distinguished the notion of characteristic sample from the implementation of the respective reconstruction operators. |
| P8 | Added the stronger uniform-coefficient consequence, independent of alphabet and the specific typing at fixed positive-image size. |
| P9 | Used reconstruction soundness for the two named operators, then the distinguishing-pair argument for general set-driven operators with characteristic samples for both languages. |
| T1 | Defined `U_1={1,zeta}` as a two-element semilattice in the introductory main theorem and Section 6. |
| T2 | Renamed the typed-rule-thickness **remark** label from `lem:typed-thickness-equivalence` to `rem:typed-thickness-equivalence` and updated the source-port checker NEW registry. The internal `thm:C` label is intentionally retained, but public-facing text calls it Theorem B. |
| T3 | Made the contradiction explicit; proof now separates the soundness case from the general distinguishing-pair case. |
| J1/J2 | Aligned Japanese wording on Yoshinaka's thickness comparison and normalization-stage attribution with English. |
| J3/J4 | Handled by T3 and T1. J5/J6 were optional and not changed. |

## #1 acceptance premise and citation integrity

The author instructed us to **proceed with research and revisions on the premise that TCS #1 is accepted**. This is a conditional planning assumption, **not verification of an actual acceptance decision**. Accordingly the draft's bibliographic status remains "Manuscript under review" pending acceptance evidence. All proof citations to `kuriyamaCFG` still target Proposition 6.4 and Appendix C of arXiv:1409.6247v5. If TCS publishes a renumbered final version, update precise locators in both languages.

The lower-bound construction is not re-proved from scratch; accepting the companion's published/refereed proof as background is part of the author's plan. Its mathematical dependence is openly disclosed.

## Verification status at the time of PR preparation

- Source-level check: EN and JA each contain **89 labels**, with identical label sets; no duplicate labels, missing `\ref` labels, missing `\cite` bibliography entries, or imbalanced checked LaTeX environments.
- Theorem A's English statement block is unchanged relative to the base commit. No theorem-A proof claim was added.
- The source-port checker has been updated for the corrected remark label. Its actual execution and compilation tests are **not** asserted here without a successful CI run.
- **Pending:** EN pdfLaTeX and JA LuaLaTeX builds, PDF visual inspection, further independent proof audit of Theorem A, and author approval. The published fixed-URL PDFs remain baseline until a verified post-merge regeneration.
- No submission, journal acceptance, or final manuscript approval is represented by this branch or PR.

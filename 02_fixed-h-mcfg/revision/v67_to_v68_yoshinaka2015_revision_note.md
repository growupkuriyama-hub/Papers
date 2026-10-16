# MCFG #2 v68 — Yoshinaka (2015) independent-referee revision

Date: 2026-10-17
Branch: `revision/02-yoshinaka2015-v68`
Source: `02_fixed-h-mcfg/main.tex`
Base: `revision/02-yoshinaka2015-v67` (v67)
Main-TeX update commit: `9bf5b0087de749104ba5a6b525b5e3f5bd5d91d2`
Status: **revision candidate, not merged to main; whole-article build pending**.

## Reason for revision

The independent report `MCFG_v67_Yoshinaka2015_review.md` evaluated the embedding as MINOR REVISION but the novelty account as MAJOR REVISION. Original sources: Yoshinaka, MoL 2015, Theorem 1, Assumptions 1–3, Examples 3–4, Sections 6–8 and Lemmas 2–3; Yoshinaka, TCS 2011.

## Implemented

1. The bounded-rank class is characterized by the **equality**
   `Subst(S_{f,r,h}) = C_mcf(f,h) ∩ MCFL(f,r)`,
   not merely a one-way inclusion. The construction uses good templates, finitely many tagged monoid-valued tuple sorts, promotion, and separate epsilon.
2. An independent `lem:signature-contexts` shows **both** directions of the correspondence of signature context functions with positive tuple sentence contexts with nonempty separators, using nonpermuting, nonmerging, and nonempty sibling components.
3. The verification of Assumptions 1–3 now enumerates SUB, CON, FUN using bounded interval decompositions and defines the latter as **function names**.
4. The learner statement distinguishes Yoshinaka's context-indexed SUBST_D (proved correct in 2015) from the substructure-indexed SUBST_P; `rem:substp` gives a language-level per-sample correspondence to the guarded constructor, not a claim of syntactic grammar identity.
5. Canonical witness sets are related to D* with explicit qualifications about promotions, start symbols, and epsilon, rather than attributing characteristic-data cardinality or existence to this paper.
6. Abstract, Introduction, Contributions, and Related Work now foreground **total positive sample length in the original grammar parameters**, rule rank/thickness, and typing/fan-out separation.
7. Fixed the abstract typo `emph{length}` -> `\\emph{length}`; changed the two erroneous `\\tau_{E_n}\\le2` occurrences to `t_{E_n}\\le2` (nonterminal thickness).

## Scope preserved

No changes to the core #2 learner definitions or earlier theorems, apart from the priority bridge and two notation fixes. The group-kernel/center-index arity result remains deferred by agreement; there is no modification to #3/#7.

## Validation

- [x] Main TeX saved and read back from the revision branch
- [x] Distinct and defined LaTeX labels, bibliography keys and references (static check)
- [x] Matched standard theorem/proof/equation/list environments (static check)
- [x] New 2015 embedding section taken from referee-provided replacement, with precise start/epsilon witness qualification
- [x] **New-section standalone LaTeX smoke test**: two pdflatex passes, return code 0, no overfull box. Undefined cross-references are expected because the rest of the original paper was deliberately omitted from the three-page test harness.
- [ ] **Complete article** two-pass compilation and PDF visual inspection; full GitHub source could not be transferred to the isolated local TeX runtime in this session.
- [ ] External follow-up review of the `SUBST_P` per-sample language equivalence and normalization scope
- [ ] Merge revision branch into main after full build and review

## Prior-art framing

Do not claim the 2015 general learning theorem yields a characteristic-data *total length* polynomial in original grammar size/thickness. In bounded rank the prior framework already covers qualitative identification, polynomial update time (as a function of data size), and a characteristic set with cardinality bounded by `|N|+|P|` for the signature grammar. Rank-unbounded learnability is closely related to Yoshinaka (2011), and should not be advertised as a fundamentally new learning paradigm.

Links:
- https://aclanthology.org/W15-2308/
- https://github.com/growupkuriyama-hub/Papers/tree/revision/02-yoshinaka2015-v68/02_fixed-h-mcfg

# I&C lean-core editorial experiment for MCFG #2 (2026-10-22)

Status: **experimental, separate branch, not a vetted or submitted revision**.

Branch: \`mcfg2-v82-lean-ic-experiment\`
Base (unchanged during Claude's review): \`mcfg2-v82-semigroup-migration-stage1\`

## The editorial hypothesis

I&C readers should encounter one research spine:

1. Fixed positive-semigroup tuple substitutability and exact reconstruction;
2. Characteristic positive-data **total length**, not just cardinality;
3. Rank-one polynomial bound, quadratic prefix/suffix-window bound;
4. Window+arbitrary finite group and local-group cubic extensions;
5. An intrinsic rank-two typed MCFG witness proving the higher-rank regime is nonvacuous;
6. Explicitly scoped high-fan-out lower-bound open problem.

This is a targeted focus test, **not** a claim that the removed results are incorrect.

## Concrete diff

- Parked three complete peripheral comparative subsections from the main PDF,
  with the exact original text preserved under:
  - \`revision/parked_structural_results_EN.tex\` (21,317 characters, ~531 lines);
  - \`revision/parked_structural_results_JP.tex\` (15,510 characters, ~650 lines).
- These parked sections include \`prop:strong-fanout-separation\`,
  \`thm:arbitrary-filter-separation\`, the fixed-window doubling obstruction,
  rare-type deletion/lower bound, Ramsey mobility and the stronger
  arbitrary-finite-typing doubling nonmembership theorem.
- Kept in the paper the intrinsic-rank-two boundary-typed witness
  \`thm:intrinsic-ranktwo-witness\`, as it ties directly to quantitative rank.
- Moved the self-contained strictly-2-local lemma
  \`lem:sl2-boundary-control\` into the retained comparison section,
  because the intrinsic-rank proof invokes it. Added a concise definition.
- Adjusted EN/JP Abstract, introduction contribution paragraph and Conclusion
  so the lean article claims **only results still proved inside the PDF**.
- Removed the extra EN introductory paragraph about AI-assisted methods;
  the formal manuscript disclosure remains intact.
- Bilingual reference scans: no duplicate labels or unresolved internal
  labels, counting all three still-included mathematical appendices.
  Also checked equality of EN/JP theorem environment sequence.

## Important: reduction vs hiding the proof

This experiment truly deletes the three sections from the **compiled article**
(and archives them in separate tracked TeX files), rather than merely moving
those sections to a compiled appendix: the total page count should decrease.
The removed results are no longer advertised as claims of the lean paper.
Their proofs remain recoverable and may become a dedicated short paper,
a referee-requested appendix or optional supplementary material later.
Do **not** claim they are all included in the shorter PDF.

No semigroup definitions or core quantitative proofs have been rewritten in
this experiment. It builds on v82 Stage 2 and is logically independent of
the parallel Claude mathematical audit; reconcile the audit's findings before
accepting any editorial removals.

## Further cutting candidates (not yet edited)

1. Relocate the ~240-line intrinsic-rank witness to a compiled appendix
   while leaving its accurate theorem statement in the main text. This
   shortens the **main body**, not total PDF length.
2. Reduce introduction repetition of Yoshinaka 2011/2015 qualitative learning
   scope across the early baseline and the later "Relation to prior work".
   Keep explicit novelty boundaries and correct attribution.
3. Review whether "Distributional Representatives and Abelian-Filtered
   Targets" (~240 lines) should be split into a sequel. It supplies a real
   quantitative theorem not implied by the local-group condition; do not
   silently delete it without a replacement positioning plan.
4. The later detailed signature/2015 comparison is ~220 lines in a compiled
   appendix. Preserve its proof until Claude has confirmed assumptions.
5. Noncommutative group and LG appendices are part of the central claim:
   cutting them without a fully valid proof elsewhere would be unacceptable.

## Proposed editorial acceptance criteria

- No mathematical statements retained without a proof or valid citation.
- Compilation of English and Japanese sources, with no undefined references.
- Compare complete rendered PDFs and establish true page difference.
- Inspect the final PDF for margins, text density, proof flow and typos.
- Apply only after the semigroup audit and author signoff.

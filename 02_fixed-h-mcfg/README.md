# #2 — fixed-h MCFG

**Title:** Positive-Data Learning of Multiple Context-Free Languages under Fixed Finite-Monoid Typing  
**Author:** Takayuki Kuriyama  
**Target journal:** Information and Computation  
**Public preprint:** arXiv:2605.11644

## Current working baseline

- `main.tex` — English working manuscript, internal v63; this is the current source of truth.
- `revision/v62_to_v63_revision_note.md` — final planned page-reduction pass: compresses characteristic-data exposition and normalization appendix bookkeeping without removing named results.
- `revision/v62_to_v63.diff` — unified manuscript diff for the v62 → v63 compression.
- `revision/v61_to_v62_revision_note.md` — safe page-reduction pass confined to the comparison section; compresses proof narration while preserving named result statements and the intrinsic-rank-two audit core.
- `revision/v61_to_v62.diff` — unified manuscript diff for the v61 → v62 comparison-section compression.
- `revision/v60_to_v61_revision_note.md` — final submission-hardening pass after two independent audits: fixes recognition/normalization citation scope, sharpens intrinsic-witness novelty positioning, strengthens the Gallot/Bishop bridge, and reduces defensive prose without changing theorem statements.
- `revision/v60_to_v61.diff` — unified manuscript diff for the v60 → v61 revision.
- `revision/v59_to_v60_revision_note.md` — safe pre-submission compression pass: trims repeated exposition and one unused secondary example while preserving theorem/proposition/lemma counts and the mathematical core.
- `revision/v59_to_v60.diff` — sequential unified patches for the v59 → v60 compression revision.
- `revision/v58_to_v59_revision_note.md` — pre-submission citation and positioning hardening after independent review; corrects the COPY attribution, strengthens the Gallot/Bishop source bridge, clarifies the modular intrinsic witness, and removes an unused bibliography entry.
- `revision/v58_to_v59.diff` — unified diff for the v58 → v59 revision.
- `revision/v57_to_v58_revision_note.md` — strengthens the intrinsic-rank-two witness to a non-context-free minimum-fan-out-two target while retaining the all-finite-fan-out rank lower bound.
- `revision/v57_to_v58.diff` — unified diff for the v57 → v58 revision.
- `revision/v56_to_v57_revision_note.md` — adds a corrected intrinsic-rank-two boundary-typed witness based on the non-branching lower bound for MIX2.
- `revision/v56_to_v57.diff` — unified diff for the v56 → v57 revision.
- `revision/v55_to_v56_revision_note.md` — withdraws the invalid minimum-rank-two witness, reframes the higher-rank theorem as presentation-sensitive, and records intrinsic rule rank as an open problem.
- `revision/v55_to_v56.diff` — unified diff for the v55 → v56 correction.
- `revision/v54_to_v55_revision_note.md` — stable ACL Anthology locator for Kato--Seki--Kasami (2004).
- `revision/v54_to_v55.diff` — unified diff for the v54 → v55 revision.
- `revision/v53_to_v54_revision_note.md` — explicit empty-word clause in the rank-one characteristic-data theorem.
- `revision/v53_to_v54.diff` — unified diff for the v53 → v54 revision.
- `revision/v52_to_v53_revision_note.md` — primary-PDF citation audit and locator tightening for Yoshinaka/Seki sources.
- `revision/v52_to_v53.diff` — unified diff for the v52 → v53 citation-audit revision.
- `revision/v51_to_v52_revision_note.md` — targeted prose-compression pass in the quantitative characteristic-data section.
- `revision/v51_to_v52.diff` — compact diff summary for the v51 → v52 revision.
- `revision/v50_to_v51_revision_note.md` — abstract scope precision for the higher-rank characteristic-data theorem.
- `revision/v50_to_v51.diff` — unified diff for the v50 → v51 revision.
- `revision/v49_to_v50_revision_note.md` — explicit Kato dimension/rank ↔ fan-out/rule-rank notation bridge.
- `revision/v49_to_v50.diff` — unified diff for the v49 → v50 revision.
- `revision/v48_to_v49_revision_note.md` — citation-provenance precision pass for the minimum-rank-two lower-bound chain.
- `revision/v48_to_v49.diff` — unified diff for the v48 → v49 revision.
- `revision/v47_to_v48_revision_note.md` — summary of the v47 → v48 genuine-rank-two witness revision.
- `revision/v47_to_v48.diff` — unified diff for the v47 → v48 revision.
- `revision/v46_to_v47_revision_note.md` / `revision/v46_to_v47.diff` — retained history for the preceding revision.
- `revision/v45_to_v46_revision_note.md` / `revision/v45_to_v46.diff` — retained history for the preceding revision.
- `revision/v44_to_v45_revision_note.md` / `revision/v44_to_v45.diff` — earlier retained history.

The public arXiv record currently corresponds to an earlier manuscript baseline; the working source in this directory has advanced substantially beyond that version.

## Scope

The manuscript studies positive-data learning of bounded-fan-out multiple context-free languages under fixed finite-monoid typing, including exact finite-sample reconstruction, conservative TxtEx learning, quantitative characteristic-data bounds, and expressiveness/separation results.

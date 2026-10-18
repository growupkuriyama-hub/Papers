# v85 — stronger-theorem absorption and reversible archive

Status: I&C review draft, not merged or submitted. Date: 2026-10-19.
Immediate full restoration: branch `archive/mcfg-v84-preabsorption-full-20261018`, commit `ed945ec8792f3840cdb108b09c49780f8fa4d404`.

## Main-paper theorem hierarchy
- `thm:local-group-polydata` is the typing-side cubic main theorem; windows with any finite (possibly nonabelian) group belong to its scope. Separate window-group cubic theorem and its shortening chain are removed from the compiled appendix.
- `cor:mcfg-li-group-polydata` remains as a **sharper quadratic bound** for locally trivial positive image, with `lem:mcfg-li-group-window`.
- `thm:mcfg-semilattice-twisted-polydata` is the target-side polynomial main theorem. Its D and one-marker consequences (`thm:mcfg-abelian-filter-data`, `cor:mcfg-one-marker-split-polydata`) remain as short corollaries, with labels intact.
- `prop:mcfg-relaxed-witnesses` and `lem:mcfg-coset-representative-transfer` retain their distinct roles as general distributional and coset-specific transfers. Computable rule-only witnesses remain separate.
- Group order-homogenization/interval/antichain lemmas remain in the compiled group appendix because LG shortening invokes them.

## Archived exact original sources
- `archive/trim-v85/{en,jp}/appendix_window_abelian*.tex`: full abelian zero-sum and Davenport sharpening appendix.
- `archive/trim-v85/{en,jp}/appendix_window_group*.tex`: entire v84 arbitrary-group appendix.
- `archive/trim-v85/{en,jp}/appendix_local_group*.tex`: entire v84 LG appendix.
- `archive/trim-v85/{en,jp}/old_li_group_block.tex`: previous group-refinement lemma and two-case corollary.
- `archive/trim-v85/{en,jp}/omitted_window_group_theorems.tex`: now-subsummed arbitrary-group constructive theorem and window/group characteristic data proof.
- `archive/trim-v85/{en,jp}/omitted_pseudovariety_lower_side.tex`: old type-filter lemma and full fan-out-one pseudovariety corollary proof.

The archived full appendix sources are verbatim v84 snapshots. The omitted TeX segments preserve statements/proofs but require the enclosing manuscript preamble to compile. Nothing is destroyed.

## Restoration
To recover v84 exactly, checkout its fixed commit. To reintroduce only one result, copy the relevant stored TeX back into the intended appendix/main source, restore appropriate `\input` and `\ref`, check duplicate labels and rebuild **both** languages. The first-stage archive `archive/trim-v83` is unaffected.

## Pending checks
- [x] EN/JP compiled-source label/static environment audit: zero missing/duplicate labels.
- [ ] Bilingual CI PDF compile, citations, overfull box check, page counts.
- [ ] Human PDF whole-page visual inspection.
- [ ] Independent mathematical audit of preserved LG and semilattice proofs.
- [ ] I&C author signoff.

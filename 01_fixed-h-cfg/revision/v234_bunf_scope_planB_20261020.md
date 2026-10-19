# TCS v234 — General CFG statements with BUNF as proof technique (2026-10-20)

**Author direction:** keep the BUNF definition; assume BUNF only for arguments actually requiring it; state other results for arbitrary CFGs. Single canonical branch: `main`. No draft PR.

## Statement changes
- Intro §1.2: describe the unrestricted fixed-slice CFG target classes explicitly. The normalized typed-thickness upper bound is attached to the BUNF normal form, not falsely to arbitrary CFG size alone. State the positive-image `LI vee Grp` ordinary-thickness regime and arbitrary linear CFG regime explicitly. Restrict the presentation-independent exponential typed-thickness referent to `L_n`, not both distinguishing targets.
- §5 exact reconstruction (existing theorem label `thm:reconstruction-fixed-s`): allow an arbitrary reduced CFG `G_*`, normalize it to reduced BUNF `G`, take the canonical witness `Wit(tilde G)`, and apply existing BUNF completeness plus soundness. No stronger uniform incremental learning claim.
- §5 Gold corollary (existing label `cor:ilt`): allow arbitrary reduced CFG `G_*`, normalizing solely to certify a finite witness. The conservative learner remains unchanged.
- §6 typed-thickness corollary (existing label `cor:typed-thickness-data`): state arbitrary reduced CFG `G_*` as input and a polynomial-size reduced BUNF normalization `G` (identity when `G_*` is already BUNF). Data length polynomial in `|G_*|` and **`tau_s^typ(G)` of that normalization**; NO asserted polynomial bound in `|G_*|,tau_(G_*)` for arbitrary s.

## Technical BUNF assumptions deliberately retained
- BUNF definition and typed refinement grammar; `thm:complete` uses the four explicit witness families and Rule U/B/L/S.
- Typed-thickness witness lemma `lem:typed-thickness-bound` uses binary branching in canonical context and number-of-rules bounds.
- BUNF-dependent intrinsic typed-thickness corollary `cor:typed-gap-intrinsic` (lower bound remains valid as stated; no new general CFG parameter silently introduced).
- Window/group typed-yield Lemma 7.1 and Appendix A.1's essential-node counting, polynomial-thickness-preserving BUNF normalization, and linear-spine BUNF technical normalization.

## Mathematical justification
Given any reduced CFG `G_*` generating nonempty fixed-s substitutable `L`, terminal isolation and binarization yield equivalent reduced BUNF `G` with `|G|=poly(|G_*|)`. The existing typed refinement `tilde G` has a finite witness set. By Theorem 5 completeness applied to `G` and soundness of `Rec_s`, that witness is characteristic for `L`, proving arbitrary CFG reconstruction. The Gold-learner proof needs only the existence of a finite witness. Lemma 6.1 bounds the encoded witness size by a polynomial in `|G|,tau_s^typ(G)`; composition yields a polynomial in `|G_*|,tau_s^typ(G)`. No result is asserted concerning a typed thickness parameter attached directly to unnormalized general CFGs.

## Validation and release
No changes to algorithms, witness sets, normal-form construction, numbered environments, lemma labels, abstract, or proof details inside Appendices A--C. Changes checked for unchanged label sequence, theorem/proof counts and resolved local references. Regenerate Clean/Marked/Response PDFs and exact three-file ZIP and verify all 49 reviewer items and marked-PDF locators; check final page numbering. Japanese manuscript is an earlier reference translation and is not synchronized to v234. Not submitted to Editorial Manager, arXiv or I&C.

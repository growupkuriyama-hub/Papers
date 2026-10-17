# MCFG #2 v74 → v75: final adversarial referee hardening

Date: 2026-10-18 (JST)
Target: Information and Computation
Status: pre-submission; GitHub working revision. Not submitted to the journal or arXiv.
Sources: `main.tex`, `appendix_window_group.tex`, Japanese counterparts. Existing abelian mathematical theorem left intact.

## Source and audit

- Input: `MCFG_v74_FINAL_ADVERSARIAL_REFEREE_REPORT_20261018.md` (external Claude adversarial audit); independent follow-up evaluation.
- Verdict at intake: CONDITIONAL PASS, 0 critical, 0 major, 2 moderate (D-1 and D-2), 8 minor.
- GitHub version of #1 CFG companion paper used: [fixed commit 834e99a1](https://github.com/growupkuriyama-hub/Papers/blob/834e99a1f35b4a5fb949acc55a080658388d4480/01_fixed-h-cfg/TCS-D-26-00494_Manuscript_Clean.pdf), [TeX source](https://github.com/growupkuriyama-hub/Papers/blob/834e99a1f35b4a5fb949acc55a080658388d4480/01_fixed-h-cfg/TCS-D-26-00494_Manuscript_Clean.tex). In that snapshot, the exponential semilattice characteristic-data lower-bound statement and its distinguishing-pair proof are present. Do NOT imply this statement appears in public arXiv v4. Once arXiv v5 exists, cite both.

## Resolved findings

1. **D-1: abstract exponent mismatch.** Explicit window-only data bound `O(||G||^2 theta_bar)` versus window-plus-group `O(||G||^3 theta_bar)` in both languages.
2. **D-2: companion paper discoverability.** Replace reliance on unpublished arXiv v5 with a version-locked, public GitHub reference, identifying the revised manuscript and earlier arXiv v4 honestly. No claim of released arXiv v5.
3. **D-3: Gallot citations.** Primary PDF at https://pepite-depot.univ-lille.fr/LIBRE/EDMADIS/2021/2021LILUB030.pdf (section 8.1/8.2) explicitly contains Definition 38, Theorem 29, Theorem 31, Propositions 5–6, matching the manuscript's uses. Bishop et al. 2026 has DOI 10.1142/S0218196726500165 and IJAC 36(4):425–486.
4. **D-4/D-5: Japanese references and hypothesis.** Removed redundant prefix `付録~\\ref` and added `r_max>=1` to the Japanese D.4 statement.
5. **D-6: block-order proof.** Spell out opposite-direction cycles and both interleaving transitivity orders; no theorem scope change.
6. **D-7: Ramsey greedy extraction.** Add the exact retained-set inequality and clarify that the last selected vertex completes the monochromatic clique.
7. **D-8: formerly indirect dependency.** Add dedicated `lem:window-group-short` for nonabelian groups; Theorem D.5 invokes it directly instead of citing the proof of an abelian-only statement.
8. **D-9: explicit open questions.** Record optimality of exponent 2/3 and refinement of Ramsey constant as open.
9. **D-10: disclose the #1/#2 relation in the submission cover letter.** Remains a submission-time administrative action; manuscript's Introduction and reference now explain the relation.
10. **Independent related-work cross-check.** Yoshinaka (2008) publisher/bibliographic record and secondary definition corroboration; Yoshinaka (2011) publisher abstract and bibliographic metadata; Yoshinaka (2015) full open-access source https://aclanthology.org/W15-2308.pdf. In 2015, the general signature framework is already a qualitative learner and bounded witness-cardinality result, not a theorem about original-grammar total characteristic length. The full Yoshinaka (2008) and Yoshinaka (2011) original papers were additionally inspected from the project reference anthologies. Yoshinaka (2008), Theorem 1, explicitly provides a characteristic set with polynomial cardinality in CFG size and polynomial total length in CFG size times rule thickness for fixed (k,l); Yoshinaka (2011), Lemma 7 and Theorem 1, explicitly provide |K_G|<=|P| and ||K_G||<=|P| tau_G for the **untyped** multidimensional substitutability learner. Thus neither paper should be described as lacking total-length results in general: the present distinctive claim is the transfer of original-grammar thickness bounds to **fixed finite-monoid typed MCFGs** at higher fan-out via simultaneous boundary/group-preserving shortening. Yoshinaka (2015) provides the general signature learning framework and characteristic-cardinality bound, while original-thickness transfer for these typed higher-fan-out settings is not established there. This is direct source comparison, not a guarantee that no further prior art exists. Duncan et al. (2026), DOI 10.1142/S0218196726500463, offers a *different*, nonmembership-oriented substitution lemma for MCFL and does not supply these characteristic-data bounds; a concise distinction and citation have been added.

## Mathematical scope preserved

- No extension to arbitrary finite **monoid** typing is claimed.
- Fan-out, rule-rank cap, group, terminal alphabet, window and typing are fixed parameters in the polynomial statements.
- No proof of optimal exponent 2 or 3 is claimed.
- The arbitrary finite group proof is noncommutative, and the abelian zero-sum proof and sharper constant remain available.
- The qualitative learnability mechanism remains attributed to Yoshinaka.

## Release checklist

- [x] English and Japanese TeX source corrections committed on feature branch.
- [x] GitHub companion citation pinned to a concrete, public manuscript.
- [x] Primary-source Gallot and related-work bibliography review.
- [x] PR #40 English pdfLaTeX and Japanese LuaLaTeX builds passed; the dedicated reference/citation/duplicate-label checks passed.
- [x] English/Japanese theorem-label sets (83 each) and their order, bibliography keys and source SHA-256 values independently matched.
- [ ] Full-page *visual* inspection of both final PDFs remains a human review gate; automated compilation and published PDF availability alone do not establish it.
- [ ] Author review of editorial/AI-use wording and I&C submission metadata.
- [ ] Add #1 arXiv v5 beside GitHub citation **after actual public release**.
- [ ] Disclose companion TCS manuscript overlap in I&C cover letter.

This version remains a working submission candidate, not a peer-reviewed or proof-assistant-certified mathematical result.

## GitHub release confirmation

- PR [#40](https://github.com/growupkuriyama-hub/Papers/pull/40) merged as `356c178ae2f9b525b79ecd1a50481a0e2a972a8a`.
- CI `Verify MCFG` run 39055371346, manuscript job 117462146785: successful English and Japanese builds, with successful automated check for unresolved references/citations and duplicate labels.
- Publisher commit `91194b733bc8509a2883496f3fab89ae4d7f34ce` wrote updated stable-path English and Japanese PDFs to main; their Git blob SHA values differ from the previous v74 releases.
- Full-page PDF visual inspection is still outstanding; this is not represented as completed.

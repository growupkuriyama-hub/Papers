# TCS v243 — new identity symbol and final editorial reconciliation

Date: 2026-10-20; canonical branch main. Single pass of precision fixes motivated by the Claude report, without altering any numerical results, theorem numbering, proof cases or algorithms.

- Replace every appearance of fresh identity \\mathbf e (EN 18; JP 23) with \\mathbf{1}_{\\sharp}; leave idempotent e and terminal e untouched.
- Explain BUNF and the locally trivial/group join LI v Grp on first use; introduce s' in the kernel-comparison display; label group-valued g as a monoid morphism; apply trimmed general-CFG refinement in Prop 9.7 instead of BUNF; state x,y share empty context in Thm 9.2.
- Response R1.2: delete internal CI/workflow comment; R1.32: attribute standard binarization references to Appendix A.2 and single-spine construction to Appendix B, with correct locator. Shorten locator guide introduction. Keep 49 responses and linked marker structure.
- Japanese reference manuscript: update all fresh-identity notation and corresponding short local corrections; it still predates the fully general CFG Section 5, updated Conclusion, AI Declaration and Alexander Clark acknowledgment and is not EN v243-equivalent.
- Separate Declaration of Competing Interests already corrected by author, NOT modified. For reviewers to read an unmarked PDF in Editorial Manager, upload separate Clean PDF manually if desired (the official ZIP contains only Clean TeX, Marked PDF, Response PDF).
- Clean TeX mirrors English main.tex, SHA256 f6dc247a65025298e1d9ae1b5ced3967ff5f6145b43ca8326158de94718f3f6a. Japanese source SHA256 47634aceb0a49cf6bff5731c45221c8fb4d2bcacb6fde0092fa24e89128016a9. Post-commit Actions must rebuild PDFs and check all 49/77 locations before release is marked verified. No action in journal portal.

## Verified v243 English/Japanese build — 2026-10-20
- English Clean PDF 26 pages, GitHub Actions run 39372842023 success (Japanese PDF rebuild succeeded too).
- English Marked PDF 26 pages and reviewer response 14 pages, GitHub Actions run 39372842012 success.
- All 49 reviewer-item page and margin-line anchors verified against actual Marked PDF, response source has 77 marked-PDF references.
- Exact three-file ZIP GitHub Actions artifact 12241774044 downloaded as TCS-D-26-00494-v243-R1-three-files.zip; archive has only Clean TeX, Marked PDF, reviewer response PDF; CRC pass.
- Clean TeX SHA256 f6dc247a65025298e1d9ae1b5ced3967ff5f6145b43ca8326158de94718f3f6a equals official English main.tex SHA256; all 18 new 1-sharp markers present, no old bold-e in Clean TeX.
- Independently compiled stand-alone English Clean PDF from ZIP TeX using two pdflatex passes, 26 pages and A4, non-encrypted. Examined rendered page 4: 1-sharp properly typeset in Lemma 2.2. Marked and response PDF are also A4/unencrypted.
- Japanese main_JP.tex has all 23 notation replacements and matching local errata, Japanese PDF builds; entire Japanese manuscript and Japanese reviewer response remain unsynchronized with current English mathematics (v235+).
- Clean PDF is a separate optional Editorial Manager display attachment; adding it inside EM is a manual user action. No change to already corrected external Declaration of Competing Interests; no EM submission by assistant.

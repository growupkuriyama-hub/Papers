# TCS v241 — minimal disclosure of generative AI assistance

Date: 2026-10-20. Source of truth: `main.tex` on `main`; submit only after English bundle verification.

Added exactly one unnumbered section after Acknowledgments and before Appendices, titled `Declaration of generative AI and AI-assisted technologies in the manuscript preparation process`. The statement follows the previously accepted neutral Candidate A verbatim (aside from TeX source line wrapping), disclosing ChatGPT and Claude for language editing, manuscript organization and the examination of mathematical arguments; acknowledges author review, editing, and responsibility. Does not assert independent verification of all proofs.

No change elsewhere in manuscript, including theorem/proof statements, algorithms, references, reviewers' response and acknowledgments. No new LaTeX labels or theorem numbers. Same git blob must be used for main.tex and TCS-D-26-00494_Manuscript_Clean.tex. English source SHA-256 `4a2ec3de4cca362666ac8a5a35973b59cf93d9eb62ccb4f498fe022c5eb4e62b`.

Release gate: build Clean/Marked PDFs; update reviewer-response PDF locations against marked manuscript (49 reviewer items, 77 location references), validate exact three-file ZIP. Japanese version not synchronized. Editorial Manager and arXiv untouched.

## Verified release results (2026-10-20)

- English Clean PDF produced by GitHub Actions run 39351699686: **26 pages** (previous v240 Clean PDF was 25 pages).
- Marked PDF and response/ZIP workflow run 39351699718: SUCCEEDED; Marked PDF 26 pages; Response PDF 14 pages; 49 reviewer-item locators and 77 marked-PDF references verified against actual PDF margin lines.
- GitHub Actions artifact 12233194309 downloaded and locally checked as `TCS-D-26-00494-v241-R1-three-files.zip`: exact 3 files (Clean TeX, Marked PDF, Response PDF), ZIP CRC passed; Clean TeX 110020 bytes with SHA256 `4a2ec3de4cca362666ac8a5a35973b59cf93d9eb62ccb4f498fe022c5eb4e62b`, matching canonical `main.tex`.
- PDF preflight passed (both A4, nonencrypted); Declaration on Marked PDF page 21 rendered and visually checked for visible text, clipping, overlap and glyph errors.
- Japanese translation is not synchronized; Editorial Manager resubmission has NOT been performed.

# TCS v237: concise general-CFG witness presentation and locator CI fix (2026-10-20)

Canonical authoring on `main` only; this is an editorial tightening of the v236 proof.

## Changes
- In Section 5 replace three non-essential displayed mathematical equations (general production `rho`, parent semigroup type `mu`, canonical rule yield `t_rho`) with inline definitions. Preserve a displayed typed production and the formally labelled canonical witness set `eq:W`, and the fiber identity of Proposition 5.1.
- Replace the expanded explanatory paragraphs from the v235 general-CFG rewrite with concise wording, retaining all induction ingredients: the two same-context witnesses for unary Rule U, finite-factor decomposition via repeated binary Rule B, nullable children producing lambda, lexical terminal blocks, and start / lambda cases.
- Section 6 removes repeated explanations of why BUNF is used and retains its substantive quantitative counting argument.
- Static source delta -2444 characters, three fewer displayed unnumbered equations, 55 fewer source lines in Section 5. Same 58 LaTeX labels and theorem/proof counts, and all local references resolved. Direct quantitative results and parameter scopes unchanged.
- **CI repair:** `response/synchronize_marked_locators.py` had a hardcoded ordered-position anchor `Proposition 6.3`, outdated since v236 moved the BUNF definition and renumbered the lower-bound proposition to 6.4. Update to 6.4, plus Gold Corollary 5.4 and completeness Theorem 5.2 in special heading fallback logic. The prior v236 marked PDF successfully compiled (26 pages) but the 49-item locator synchronization failed solely on the stale ordered anchor. CI must pass freshly against v237.

## Release gate
- English Clean PDF and Marked PDF page counts before/after and layout review; synchronized English reviewer-response PDF; exactly three submission files in ZIP and verified 49 reviewer items/77 locator citations.
- No Japanese translation update and no Editorial Manager submission.
- English TeX SHA256: `a14e1c244f420c53a33c16e93147c176336cd7a4c293bf081c72442c88166732`.

## Final English package checks (2026-10-20)
- Clean PDF: 25 A4 pages, successful Publish TCS run 39291148695 (previous v236: 26 pages).
- Marked PDF: 26 A4 pages, response PDF 14 pages, successful run 39291148674, all 49 reviewer items PDF-page-and-margin-line validated; 77 embedded marked-PDF locator references in response source.
- Downloaded and tested artifact 12205343929, exact three-file ZIP: Clean TeX 109795 bytes, Marked PDF 614204 bytes, Response PDF 323698 bytes. ZIP passed unzip -t. Clean TeX SHA256 a14e1c244f420c53a33c16e93147c176336cd7a4c293bf081c72442c88166732 matches v237 source.
- PDF preflight: openable, searchable, nonencrypted, A4; manuscript pages 9-10 rendered and visually checked. No Editorial Manager resubmission, no Japanese manuscript synchronization.

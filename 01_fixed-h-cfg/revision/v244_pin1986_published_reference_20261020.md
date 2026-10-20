# TCS v244 — replace Pin's 2025 lecture notes with published 1986 monograph

Date: 2026-10-20. Canonical main branch, no journal submission.

Actual source verified from user's uploaded published scan: J.-E. Pin, *Varieties of Formal Languages*, translated by A. Howie, Plenum Press, New York, 1986, ISBN 0-306-42294-8. Printed p. 11 Chapter 1 Proposition 1.12 (for n>|S|, S^n=S E(S)S), printed p. 37 Chapter 2 Proposition 3.5 (locally trivial iff e s f = ef for all idempotent e,f), printed p. 38 Chapter 2 Theorem 3.6 (prefix/suffix recognizable languages). The arbitrary-typing kernel criterion in the TCS paper is NOT asserted as a verbatim statement of Pin 1986; it is stated and proved in Proposition 3.5.

- EN main.tex / Clean TeX: replace reference pin2025 and legacy numbers XI.4.17, XIV.1.20, II.6.35; reword classical-source boundary; leave Pin (1997) original Handbook reference intact.
- JP main_JP.tex: same local citation/bibliographic updates, but other parts are still a historical partial translation and NOT full v244 parity.
- Response: revise statement attributing whole positive-image/kernel proposition to Pin, accurately identifying classical identities and language characterization as antecedent and acknowledging our explicit kernel formulation proof.
- No changes to the mathematical proof steps or theorem labels. Conflict-of-interest form already fixed externally by author and not touched here.
- Exact SHA-256 EN 87c68654f02de2675deaeab6081ae8db3315cad251f65ab99f5714799342021a; JP 6a9f2fcb7a884f4f50502f8c8ad3643044944f518681d507e4b15722cf448e28. Automated clean, marked, reviewer response, all 49 reviewer items/77 page-line links, exact 3-file ZIP must be verified before calling this release verified.

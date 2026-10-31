# MCFG typed-thickness restructuring — 2026-10-28

## Scope
This revision responds selectively to the proposed M1 restructuring. It introduces the typed shortest-yield scale
\(t_{\mathrm{typ}}(G,s)\), its comparison with full refinement rule thickness, and a general characteristic-data length reduction. The pre-existing window–group and local-group theorems are **retained as independent main results**, because their simultaneous noncommutative block replacement and sliding-factor shortening carry the novel proof content.

## New intermediate claims
For reduced good G and its trimmed yield-type refinement, the new comparison lemma proves
\(t_{\mathrm{typ}}\le\theta_{\mathrm{typ}}\le2\bar\theta_G+r_{\max}t_{\mathrm{typ}}\).
The new reduction theorem proves
\(\|W\|_+\le N_{\mathrm{typ}}(1+2\bar\theta_G+r_{\max}t_{\mathrm{typ}})\)
with \(N_{\mathrm{typ}}=O(\|G\|)\) for fixed parameters. An optional epsilon witness adds at most one to the *full* sample's encoded length.

The existing exponential non-local-group refinement example is strengthened to show exponential **typed shortest-yield length**, not merely exponential refined rule thickness. Both directions of the refinement-thickness dichotomy therefore also apply to \(t_{\mathrm{typ}}\). These are not lower bounds on characteristic-data length or Gold-learner convergence.

## Deliberately retained proofs
- Window and finite-group results, including noncommutative interleaved block replacement.
- Local-group theorem and its sliding-factor/owner-wise shortening proof.
- The separate rank-one argument \(\bar\theta_G\le2\|G\|\), essential to retain the cubic grammar-size bound; the generic thickness lemma alone gives a weaker route.
- Abelian-filtered distributional witnesses, which are not claimed to factor through \(t_{\mathrm{typ}}\).

## Local verification
- Checked against the current `02_fixed-h-mcfg/main.tex` on `main` as of 2026-10-28.
- LuaLaTeX: 3 successive successful runs with `-halt-on-error -file-line-error`.
- 40-page PDF; no unresolved cross-references, multiply defined labels, or overfull boxes in final log.
- Structural argument check performed; this is not a machine-checked proof of the noncommutative group or local-group lemmas.

## Bibliography
Updated the public companion-preprint reference from arXiv v4 to v5 while retaining the separate citation of TCS-R1 for the revision-specific Proposition 6.4.

Only the English primary manuscript has been edited in this change. Japanese translations and release PDF automation, if any, should be synchronized through their own established workflow.

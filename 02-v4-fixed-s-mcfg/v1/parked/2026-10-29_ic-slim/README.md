# Parked material — "ic-slim" restructuring of paper #2 (2026-10-29)

This folder holds results and text that were **removed from the submission
manuscript** of paper #2 (`02_fixed-h-mcfg/main.tex`, `japanese/main_JP.tex`) to make
it shorter and more focused for *Information and Computation*. Nothing here was
found to be wrong; it was moved out because the main line of the paper does not use
it.

- English pages: 48 → 37. Japanese pages: 51 → 39.
- Work branch: `mcfg-ic-slim-20261029`.
- Full pre-cut manuscript (EN + JP, every label intact): branch
  **`archive/mcfg-pre-slim-full-20261029`** (= `main` at commit `66897a1`).
- Verbatim extracts: `parked_EN.tex` and `parked_JP.tex`. Each block is tagged
  `[P1]`, `[P2]`, … with the same tag in both languages. Line numbers in
  `parked_EN.tex` refer to `main.tex` at `66897a1`.
- **Do not `\input` these files** into the article: their labels would collide and
  some blocks cite results that remain in the article.

## The main line that was kept

1. Window–group bound $O(\|G\|^2\bar\theta_G)$, including noncommutative groups and
   interleaved tuple components (owner-wise simultaneous block replacement, App. A).
2. Local-group bound $O(\|G\|^3\bar\theta_G)$ (App. B).
3. Rare-type lower bound and the fan-out-one pseudovariety characterization
   (`thm:fanout-one-data`, bracketed doubling family, App. G).
4. Power transfer: the lower-bound family does not lift to fan-out ≥ 2.
5. Rank one, typing separations ($L_A$, $L_B$), feature-licensing example.

## What was parked

| Tag | Labels (removed from the article) | Content | Why parked |
|---|---|---|---|
| P1 | `app:supplementary`, `subsec:effective-char-data`, `prop:effective-char-data`, `subsec:short-distributional-representatives`, `prop:mcfg-relaxed-witnesses`, `thm:mcfg-abelian-filter-data`, `app:feature-budget`, `prop:feature-family-witness-budget`, `app:group-agreement`, `prop:group-agreement`, `subsec:intrinsic-ranktwo`, `lem:rank-one-edt0l`, `thm:intrinsic-ranktwo-witness` | Former Appendix H: polynomial-time computation of short witness sets and rule-only budget; distributional representatives $\kappa_G$ and polynomial data $O((\|G\|\bar\theta_G)^{3|\Sigma|+2})$ for abelian-filtered targets (Papadimitriou bound); explicit data budget for the feature family; group-valued agreement ($S_3$ separates window–abelian from window–group at arity two); EDT0L lemma and a target needing both fan-out 2 and rank 2 | Not used by the main line; each is a side result |
| P2 | `subsec:unrestricted-source`, `def:component-pattern-thickness`, `prop:pattern-thickness-transfer`, `cor:unrestricted-standard-mcfg-data` | Bounds for arbitrary standard input MCFGs via component-pattern thickness ($O(n_H^3t)$, $O(n_H^4t)$) | Generality not needed for the main claims; costs 2+ pages with App. C |
| P3 | `app:pattern-thickness`, `prop:structural-good-thickness` | Former Appendix C (proof of the pattern-thickness transfer) | Only supports P2 |
| P4 | `prop:empty-component-blowup` | Empty-component elimination can blow up thickness | Only supports P2 |
| P5 | `cor:refinement-dichotomy`, `rem:refinement-vs-data` | LG dichotomy for polynomial **full-refinement** thickness at every fan-out | Concerns the witness construction, not the data; required repeated caveats |
| P6 | `thm:boundary-polydata` | Window-only bound | Now the trivial-group case of `thm:window-group-polydata` (same constant: $c_{\{1\},f}=0$) |
| P7 | `thm:window-abelian-polydata` | Abelian constant | Now `rem:window-abelian` (Remark, same content) |
| P8 | `cor:mcfg-li-group-polydata` | $\mathbf{LI}\vee\mathbf{Grp}$ ⇒ polynomial data | Now one sentence after `lem:mcfg-li-group-window` |
| P9 | — (label kept) | General part (a) of `prop:typed-thickness-exponential` (any $e\ne z$ with $ez=ze=z$) | Only the two-letter instance is used now; (a) was needed only by P5 |
| P10 | `tab:thickness-scales` | Table of six thickness scales | Four of the scales left with P1–P4 |
| P11 | `cor:feature-relation-family` | Feature family as a separate corollary | Merged into `prop:feature-cross-typed` (statement now covers every $R$) |
| P12 | `rem:necessity-scope` | Remark linking the separations to the abelian-filter theorem | Referred to P1 |
| P13 | — | One sentence in §3 pointing to P1 (EN only) | Referred to P1 |
| P14 | — | Old Conclusion (incl. the "more focused question" on $\mu^\star$ at fan-out 2) | Rewritten and shortened |

Also rewritten (old text in the archive branch only): Abstract (one sentence on
arbitrary input MCFGs removed), Introduction (results table without the
"any standard input" column; companion table reduced to 3 columns / 8 rows),
§4 opening, §6 opening, symbol table ($n_H$, $H$, $\mathsf A$, $\mathsf H$ removed;
$G_{\mathrm{in}}$ added).

Bibliography entries removed because nothing cites them any more (copy them back
from the archive branch when restoring): `Gallot2021`, `BishopEtAl2026EDT0L`
(P1, H.5), `RamalingamReps1996`, `Nederhof2003` (P1, H.1), `Papadimitriou1981`,
`Parikh1966` (P1, H.2).

## Status of the parked results

- P1/H.2 (abelian filter): exponent $3|\Sigma|+2$ and the ILP/Papadimitriou step were
  rechecked in the 2026-10-29 referee checks; Parikh citation added the same day.
- P1/H.5 (EDT0L lemma): both directions written out on 2026-10-29. Gallot (2021)
  numbering was checked by the author (README entry T7); Bishop et al. content
  (word problem of ℤ is not EDT0L) confirmed on arXiv:2505.20057, journal data
  (IJAC 36(4):425–486, 2026) **not** confirmed.
- P2–P4: proofs as in the archive branch; not re-audited after 2026-10-29.
- P5: correct as stated, but it is **not** a characteristic-data lower bound.

## Possible future homes

- An "extended version" on arXiv that keeps P1–P5 (the I&C submission can cite it).
- P1/H.2 and P1/H.3 fit a short note on abelian-filtered targets and data budgets.
- P2–P4 fit any later paper that needs arbitrary input presentations.

## How to restore a block

1. Copy the block from `parked_EN.tex` / `parked_JP.tex` (or take the whole file
   from the archive branch).
2. Restore the bibliography items listed above if the block cites them.
3. Rebuild both languages and check that `grep -o '\\label{[^}]*}'` gives the same
   set in EN and JP and that there are no undefined references.

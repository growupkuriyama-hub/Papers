# v83 I&C trim archive

Original full v82 snapshot: `bcc0caf0eade66f552127171c0de24d2b92950b0` on branch `archive/mcfg-v82-pretrim-full-20261018`.

All files in `en/` and `jp/` preserve the v82 mathematical statements, proof text and labels verbatim except the leading archival comment header. Restore by copying an archived block (without header) to its former location and rebuilding both languages.

| Mathematical material | EN | JP |
|---|---|---|
| Intrinsic rank-two, typed and regular-filter separation theorems | `en/typed_separations.tex` | `jp/typed_separations.tex` |
| Fan-out doubling obstruction, rare-type lower bounds and mobility lemmas | `en/fanout_doubling_and_mobility.tex` | `jp/fanout_doubling_and_mobility.tex` |
| Full Yoshinaka 2015 signature correspondence and SUBST_P proof | `en/yoshinaka_signature_framework.tex` | `jp/yoshinaka_signature_framework.tex` |

The *original complete* `main.tex` and `japanese/main_JP.tex` remain retrievable from the full v82 snapshot. Current focused versions are on `mcfg-v83-ic-focused-trim`.

**Kept in the I&C manuscript:** learning and reconstruction; rank-one; window, finite-group and local-group bounds; semilattice-indexed abelian-coset theorem with D and one-marker specializations; relaxed and effective witnesses; normalization appendix and disclosures.

**Kept for dependency safety:** the three original algebraic appendices including the Davenport refinement. Further shortening of these appendices requires an independent dependency audit.

The archived files are not input into the compiled paper and are not individual standalone TeX manuscripts. The archived results are not retracted. Restore a single result by reinserting it at its corresponding subsection, restoring intro/conclusion references, checking uniqueness of labels, recompiling both manuscripts, and updating `PAPER.yaml`.

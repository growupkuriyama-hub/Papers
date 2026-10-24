# #2 — Characteristic-Data Bounds for Multiple Context-Free Languages under Fixed Finite-Semigroup Typing

**Author:** Takayuki Kuriyama  
**Target journal:** Information and Computation (pre-submission)  
**Preprint:** [arXiv:2605.11644](https://arxiv.org/abs/2605.11644)

## Canonical manuscripts on `main`

| Language | Main LaTeX file | Appendix arrangement | PDF |
| --- | --- | --- | --- |
| English (submission master) | `main.tex` | Finite-group and local-group appendices inlined into `main.tex` | `main.pdf` |
| Japanese (review translation) | `japanese/main_JP.tex` | Finite-group and local-group appendices inlined into `main_JP.tex` | `japanese/main_JP.pdf` |

These paths contain the bilingual integrated manuscript compiled on 2026-10-24 (latest research integration: internal revision 18). As requested, the two English appendices (finite-group block replacement and local-group typings) were embedded directly into `main.tex`; the standalone English files were deleted. The two Japanese appendices are likewise inlined into `japanese/main_JP.tex`, and the standalone appendix files have been removed from the current tree. Earlier separate window-abelian/window-group appendices are also obsolete.

### Quantitative results

For reduced good MCFG presentations, with fixed fan-out, rule-rank bound and typing:

- Prefix–suffix window typing and window + any finite group (including noncommutative groups): total positive-data length `O(||G||^2 · θ̄_G)`.
- Positive-image local-group typings: `O(||G||^3 · θ̄_G)`.

The 2026-10-24 research integration additionally proves short Parikh-difference certificates
and a uniform hitting set for abelian-coset competitors. For finite targets it
establishes a tuple-nesting obstruction, a linear shortest-type-fibre bound
when every marker is unique and strictly internal, and a finite-MCFG
length-spectrum upper bound. These are **partial obstructions**, not a proof
of the general fan-out-two characteristic-data lower bound. Proofs and
EN/JP references were independently checked; literature priority and formal
verification remain outstanding. Local builds: English 46 pages; Japanese 59 pages.

The general local-group bound does not supersede the sharper quadratic bounds for its window/group subclasses. These are mathematical claims of the manuscript, not guarantees of acceptance or independent formal verification.

## Local builds

From `02_fixed-h-mcfg/`:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
cd japanese
latexmk -lualatex -interaction=nonstopmode -halt-on-error main_JP.tex
```

On pushes to `main`, `.github/workflows/publish-mcfg-bilingual-pdf.yml` rebuilds the English and Japanese PDFs at the stable paths above; verify the corresponding GitHub Actions run before relying on the updated published PDFs.

## Version cleanup

Only canonical working manuscripts are kept in the current tree. Earlier version-numbered revision notes and unused standalone appendices were removed from the **working tree**, not from Git history; use `git log -- 02_fixed-h-mcfg/` or an older commit to recover them. The `revision/` directory retains reproducibility scripts and parked research results rather than superseded draft versions.

Before submission, verify bibliographic/preprint versions, the author-facing AI disclosure, and the rendered journal package.

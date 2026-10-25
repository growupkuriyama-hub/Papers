# #2 — Polynomial Upper Bounds on Characteristic-Data Length for Multiple Context-Free Languages under Fixed Finite-Semigroup Typing

**Author:** Takayuki Kuriyama  
**Target journal:** Information and Computation (pre-submission)  
**Preprint:** [arXiv:2605.11644](https://arxiv.org/abs/2605.11644) (the public version may be older)

## Canonical bilingual sources

| Language | Source of truth | Stable PDF |
| --- | --- | --- |
| English, submission master | [main.tex](main.tex) | [main.pdf](main.pdf) |
| Japanese, research translation | [japanese/main_JP.tex](japanese/main_JP.tex) | [japanese/main_JP.pdf](japanese/main_JP.pdf) |

**2026-10-24 LG dichotomy and bilingual revision:** The English and Japanese masters now include a pseudovariety-level characterization at fan-out one, with an operator-independent distinguishing-pair proof; non-context-free examples separating local groups from window–group typings and nonabelian from window–abelian typings; corrected higher-fan-out open questions; related-publication disclosure; and an explicit separation of the TCS submitted R1 from the public arXiv v4. The Japanese additions are source-level translations in `japanese/additions/`. Both texts retain their existing core MCFG shortening proofs.

**2026-10-24 editorial integration (M1–M9):** The English source is the 45-page upper-bound-centered I&C manuscript. The Japanese source has been updated to reflect the same principal claims, the finite-feature crossing example, local-group Rees/sliding-factor proof, streamlined qualitative attribution, and the single higher-arity open problem. Detailed historical versions remain in Git history.

## Proven upper bounds (fixed alphabet, fan-out, rank and typing)

For a reduced good MCFG $G$ with rule thickness $\bar\theta_G$:

- Fixed prefix–suffix windows, with or without finite-group values (including noncommutative groups): $O(\|G\|^2\bar\theta_G)$ total encoded characteristic-data length.
- Positive-image local-group typings: $O(\|G\|^3\bar\theta_G)$.
- For any standard input grammar $H$ with $n=\max\{1,\|H\|\}$ and component-pattern thickness $t$, the corresponding bounds are $O(n^3t)$ and $O(n^4t)$.
- Rank-one input MCFGs: $O(n^3)$ under any fixed typing.

Qualitative learning and characteristic-set cardinality are attributed to Yoshinaka's prior work; the quantitative owner-wise shortening and presentation-sensitive encoded-length results are the paper's focus. This manuscript does not claim a fan-out-two characteristic-data lower bound. The companion CFG paper and the present MCFG paper employ different reconstruction operators.

## Build and publication

```sh
cd 02_fixed-h-mcfg
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
cd japanese
latexmk -lualatex -interaction=nonstopmode -halt-on-error main_JP.tex
```

Pull requests modifying either source trigger `.github/workflows/verify-mcfg-bilingual-pr.yml` to compile both manuscripts and check citations/references. After merging to `main`, `.github/workflows/publish-mcfg-bilingual-pdf.yml` rebuilds and commits the two stable PDFs. Verify Actions success before treating the published PDFs as current.

The Japanese version is for internal reading and review; English is the submission master. Both mathematical proof streams still require author sign-off and independent scholarly review.

**2026-10-25 Round 4 source merge:** English and Japanese sources now include the standalone rank-one/EDT0L lemma, a full higher-arity obstruction proof, the self-contained bracketed-doubling substitutability proof, consistent shortest-length notation and the fixed-feature-family corollary. Stable PDFs are rebuilt by the main-branch publication workflow.

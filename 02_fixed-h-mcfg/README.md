# #2 — Polynomial Upper Bounds on Characteristic-Data Length for Multiple Context-Free Languages under Fixed Finite-Semigroup Typing

**Author:** Takayuki Kuriyama  
**Target journal:** Information and Computation (pre-submission)  
**Preprint:** [arXiv:2605.11644](https://arxiv.org/abs/2605.11644) (the public version may be older)

**2026-10-28 M3 exponent tightness (referee pre-review):** A new paragraph *Tightness of the exponents* at the end of the Conclusion identifies the source of each factor in the upper bounds (witness count, label-bounded path length, and the two-stage window exchange in the local-group case), records that $\bar\theta_G$ is unavoidable via the $\{\mathtt c^{2^n}\}$ example, and poses whether some fixed typing forces $\Omega(\|G\|\bar\theta_G)$, explaining why the rare-type argument cannot. The Scope paragraph points to it. No new theorem; English and Japanese synchronized.

**2026-10-28 M2 scope consolidation (referee pre-review):** The negative caveats scattered through the Introduction (operator-specific bounds, refinement obstructions not being data lower bounds, separations of fixed biases, abelian-filter scope, pseudovariety-level characterization, open necessity at fan-out ≥2) are consolidated into a single *Scope of the claims* paragraph; the related-work text after the table is halved, and generic caveats after individual statements (Section 4, Theorem `thm:mcfg-abelian-filter-data`, Remark `rem:necessity-scope`) are removed while statement-specific ones are kept. The Introduction is about 13% shorter. Also fixes the 𝖳♯→𝖲♯ typo. English and Japanese synchronized.

**2026-10-28 M1 self-containment (referee pre-review):** The fan-out-one pseudovariety boundary no longer relies on an unrefereed result of the companion CFG manuscript. The bracketed doubling family is stated as Proposition `prop:bracketed-family` (size and thickness $O(n)$, unique ceiling-free word $W_n$, exponential sample lower bound via the rare-type proposition), and its Clark–Eyraud substitutability is proved in a new final appendix (`app:bracketed-family`) by an adapted deterministic-parser argument. The abstract, introduction, related-work paragraph, Remark `rem:fanout-one-data`, Theorem `thm:doubling-no-lift`, conclusion and Open Problem now cite the companion for attribution only. English and Japanese masters are synchronized.

**2026-10-27 M5–M6 bilingual master:** The English source is the 51-page I&C pre-submission draft. The Japanese `japanese/main_JP.tex` is synchronized for its principal results: class-level typing bias, characteristic-data witness budgets, two thickness scales, noncommutative shortening, and the new refinement-thickness LG dichotomy. The prior CFG companion's fan-out-one characteristic-data boundary and lower-bound appendix have been removed from both sources. The refinement-thickness dichotomy does **not** imply a characteristic-data lower bound.


**2026-10-27 Japanese single-file consolidation:** `japanese/main_JP.tex` contains all Japanese text, theorem proofs, appendices and references in one UTF-8 LuaLaTeX source. Its technical appendix order now follows the English master; no `\\input` or `\\include` statements remain. Legacy supplement files are recoverable in Git history. English theorem and lemma labels and cross-references were checked against the Japanese version.

## Canonical bilingual sources

| Language | Source of truth | Stable PDF |
| --- | --- | --- |
| English, submission master | [main.tex](main.tex) | [main.pdf](main.pdf) |
| Japanese, research translation | [japanese/main_JP.tex](japanese/main_JP.tex) | [japanese/main_JP.pdf](japanese/main_JP.pdf) |

**2026-10-24 LG dichotomy and bilingual revision:** The English and Japanese masters now include a pseudovariety-level characterization at fan-out one, with an operator-independent distinguishing-pair proof; non-context-free examples separating local groups from window–group typings and nonabelian from window–abelian typings; corrected higher-fan-out open questions; related-publication disclosure; and an explicit separation of the TCS submitted R1 from the public arXiv v4. The Japanese additions are source-level translations in `japanese/additions/`. Both texts retain their existing core MCFG shortening proofs.

**2026-10-24 editorial integration (M1–M9):** The English source is the 45-page upper-bound-centered I&C manuscript. The Japanese source has been updated to reflect the same principal claims, the finite-feature crossing example, local-group Rees/sliding-factor proof, streamlined qualitative attribution, and the single higher-arity open problem. Detailed historical versions remain in Git history.

## Separate private higher-arity lower-bound research track (2026-10-25)

The manuscript does **not** prove a fan-out-two characteristic-data encoded-length lower bound. A private **exploratory working dossier** of Astra I–XII rigidity/finite-difference/recursive-template investigations is available to the project owner and authorized assistants in [Research-Library: notes/MCFG_FANOUT2_CHARACTERISTIC_DATA_EXPLORATION_2026-10-25.md](https://github.com/growupkuriyama-hub/Research-Library/blob/main/notes/MCFG_FANOUT2_CHARACTERISTIC_DATA_EXPLORATION_2026-10-25.md). It contains proof-status and cross-thread handoff instructions; it is *not manuscript text*, and mathematical priority and full proofs require independent validation. **The research problem remains open.** This differs from the intrinsic rule-rank lower bound already in this manuscript.

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

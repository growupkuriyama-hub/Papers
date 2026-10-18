# MCFG #2 v75 → v76 candidate: three strengthening drafts

Date: 2026-10-18 (JST)
Status: **draft on branch `mcfg2-v76-strengthening-drafts`; adoption is the author's decision.** Not submitted.
Sources: new reference bundle (Geroldinger–Halter-Koch 2006; Gao–Geroldinger survey; Knuth 1977; Nederhof 2003; Simon 1990; Costa 2001).

No main theorem statement changes. All polynomial exponents ($\|G\|^2\bar\theta_G$, $\|G\|^3\bar\theta_G$) unchanged. Only constants and an effectiveness result are added.

## 1. Abelian constant: Davenport constant replaces $|A|^f-1$

- `appendix_window_abelian.tex`, Lemma `lem:group-typed-shortest`: the antichain step already shows that replacing any subset $J$ changes the root vector by $\sum_{i\in J}\delta_i$. Hence the obstacle is a nonempty zero-sum **subsequence**, and the bound becomes $\mathsf d(A^f)=\mathsf D(A^f)-1$ instead of the consecutive-prefix-sum bound $|A|^f-1$.
- New Remark `rem:davenport-size`:
  - $f\sum(n_i-1)\le\mathsf d(A^f)\le(n-1)+n\log(|A|^f/n)$, with $n=\exp(A)$ (GHK Prop. 5.1.8, Thm. 5.5.5).
  - Equality on the left for $p$-groups (Olson; GHK Thm. 5.5.9).
  - So the constant is linear in $f$ (for $C_2$: $2^f-1\to f$).
  - This is the limit of the antichain argument; we do not claim extremal grammars exist.
- Check: brute-force small groups ($C_2^k$ for $k\le4$, $C_3^2$, $C_3^3$, $C_6$, $C_2\oplus C_4$) confirm $\mathsf d=\mathsf d^*$ and the upper bound.

## 2. Nonabelian constant: order homogenization replaces multicolor Ramsey

- `appendix_window_group.tex`: new Lemma `lem:order-homogenize`.
  - Step 1: Erdős–Szekeres makes each block type monotone.
  - Step 2: for two monotone types the comparison matrix $[p_t(i)<p_u(j)]$ is a monotone staircase. Either a chain gives an all-true set, or an interval gives an all-false set, from $(m-1)^2+1$ indices.
  - Iterating over at most $f^2$ ordered type pairs needs $N^{2^{f^2}}$ indices.
- Constant: $M_{A,f}=U_f\max\{3,|A|^f\}^{2^{f^2}}$, **polynomial in $|A|$ for fixed $f$**. v75's $U_f c_f^{c_f(N-1)+1}$ was exponential in $|A|^f$.

  | $f$, $\lvert A\rvert$ | $\log_2 M$ (v75) | $\log_2 M$ (v76) |
  |---|---|---|
  | 2, 2 | 200 | 36 |
  | 2, 6 | 2248 | 87 |
  | 3, 2 | 32274 | 1545 |

- The dependence on $f$ remains doubly exponential.
- Wording updated: abstract, overview paragraph, conclusion open problem, abelian remark, and appendix remark.
- Check: exhaustive test of the two-sequence step for all interleavings with $N=3$, plus 20,000 random cases for $N\le8$. Random full extractions also pass.

## 3. Effective computation of short characteristic data

- `main.tex`: new Subsection `subsec:effective-char-data`, Proposition `prop:effective-char-data`.
- For fixed $f,r_{\max},h$, the following are computable in time polynomial in $\|G\|$ (lengths in binary):
  - $\theta_G(R)$, $\theta_G$ and $t_G$;
  - minimum-length canonical tuples and minimum-length derivational contexts;
  - polynomial-size derivation DAGs for every witness word.
- Method: Knuth's superior-function Dijkstra on the typed refinement (Nederhof's deductive form), then an outside Dijkstra pass.
- All bounds of Sec. 5 and Apps. C/D hold for the computed sample, because each proof bounds context, template and child tuples separately by exhibiting some admissible object.
- The $\{c^{2^n}\}$ example shows that explicit words can be exponential while the DAGs stay polynomial.
- Check: Knuth inside lengths match brute force on a toy fan-out-2 MCFG with typing into $\mathbb Z_2\times\mathbb Z_3$. All 48 typed nonterminals agree; one witness found shorter than a truncated brute search, and its type and length were verified.

## Bilingual alignment and build

- Japanese `main_JP.tex` and both Japanese appendices carry translations of all three items.
- Label sets (87 each) and bibliography keys match.
- Local builds: pdfLaTeX (EN, 41 pp) and LuaLaTeX (JP, 45 pp). No undefined references or citations, no duplicate labels.
- New bibliography: GeroldingerHalterKoch2006, Knuth1977, Nederhof2003.

## Open gates

- [ ] Author review of whether to adopt items 1–3 (independently or together).
- [ ] Independent mathematical check of `lem:order-homogenize`, in particular the two column-direction cases.
- [ ] Full visual PDF review.
- [ ] Not included: research directions in `v76_research_memo_dichotomy_and_lower_bounds.md`.

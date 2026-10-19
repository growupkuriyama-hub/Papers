# PR #62 — Round-2 editorial revision and mathematical audit
Date: 2026-10-19. Source commit: `cc57b4b50b96ddaf98b2d4ba5278e069d0258167`. Scope: English main/Clean and Japanese main. Research Draft PR only; no submission or merge.

## Editorial changes
- Condensed the Introduction's historical background and “Relation to earlier work and general signature learning” to a short, explicit positioning paragraph: earlier Kuriyama preprint, Yoshinaka's general qualitative learnability, and the distinct quantitative/algebraic contribution. Originality of locally trivial window criterion is not claimed.
- Removed repeated Yoshinaka positioning from “Contributions and main results”; kept exactly two high-level contribution groups.
- Removed the “Organization of the paper” subsection; compressed the typing-bias explanation and Conclusion.
- Deleted the extended illustrative argument for order-dependent final Gold hypotheses, retaining a short acknowledgment and citation; dropped a redundant post-proof reminder and repeated BUNF normalization prose.
- Converted four short displayed proof equations in each language to inline formulas (LI cancellation, deleted-word type-fiber filter, protected-mark triple, nonabelian cancellation identity). Converted the explicit `s_U` letter-value display to a sentence. Kept central definitions, theorem bounds, case splits, and interval product equations in display.
- Checked changes jointly in EN/JP; all 58 labels, 39 explicit proof environments, references and theorem-order labels remain intact.

## Mathematical audit (performed after editorial changes)
The mathematical claims were **not changed**. These are independent manual proof checks, not a formal proof certificate.

| Topic | What was checked | Finding |
| --- | --- | --- |
| Positive semigroup and fresh identity | `Sigma+` typing, epsilon separation, recognition, and distinction between `U1` identity and fresh `e` | Coherent |
| Window quotient and LI criterion | Short/long congruence, idempotents, positive image, `S^n=SE(S)S` and `etf=ef`; compared with Pin's LI characterization | Coherent, conditional on cited classical identities |
| LI × finite-group factor lemma | Letter lifts to divisor subsemigroup, projections, group restriction and quotient map | Coherent |
| Reconstruction soundness | Nonempty-factor U/B/L rules, syntactic congruence and direct epsilon start rule | Coherent |
| Finite witness completeness | Typed target split, U/B simulation, nullable/unit children, lambda start witness | Coherent; start copies retained |
| Gold learner | Sample consistency, conservative rebuild, one possible rebuild after finite witness inclusion | Coherent; no incremental polynomial-data conclusion |
| Encoded characteristic data | Retained typed nonterminals, canonical reaching contexts, witness counts and encoded lengths | Coherent with presentation-dependent thickness |
| Semilattice lower bound | Singleton type-1 fiber; distinguishing pair `L_n,L_n^-`; ordinary thickness vs typed thickness | Coherent |
| BUNF window × group proof | Shortest nonempty fiber word, protected anchor, fewest-node tie-break, essential-node count, ordered nonabelian cancellation | No counterexample or incorrect cancellation found |
| Linear-spine BUNF | Fresh wrappers, spine reachability, unary/nullable rules and typed-state repetition | Coherent |
| Expressiveness | Finite-semigroup obstruction, Dyck and quotient arguments; reversible bracket parser path exchange | No counterexample found in manual proof review |

## Independent finite sanity checks actually executed
1. Alphabet `{a,b}`, all nine `(k,l)` with `0<=k,l<=2`: 345,744 positive-word/context congruence comparisons with words up to length 8 and contexts up to length 2; zero failures.
2. Enumerated bracketed doubling languages `L_1,L_2,L_3` with 2, 6 and 42 words. Exhaustively compared observed-factor distributions for trivial substitutability of `L_n` and `s_U`-substitutability of `L_n^- = L_n\{w_n^*\}`. No counterexamples.
3. Ordered-product cancellation was checked in the nonabelian symmetric group `S_3` over 840,000 index comparisons, including 139,919 repeated invariant values; no failed equality.
4. GitHub Actions built English pdfLaTeX and Japanese LuaLaTeX; English local double-run pdfLaTeX had 0 overfull hboxes. PDFs are 25 English and 30 Japanese A4 pages.

## Residual risk and possible further compression (not applied)
- The appendix's full reversible stack parser and nonlinear `Delta^*` entry-height proof remain deep proof obligations. A future independent line-by-line adversarial review or small formal verification effort would be stronger than these bounded tests.
- The window × group derivation-tree lemma is an original combinatorial argument. Its precise constants and handling of zero-yield sibling subtrees are natural targets for a dedicated adversarial audit, even though no flaw was found here.
- The capped regular-counter family is a pedagogical comparison; if R1 insists on more shortening, consider moving it to an appendix, **not** removing the theorem without refreshing cross-references and reviewer reply landmarks.
- A stronger presentation compression could combine the prose around the window-group lemma/theorem/corollary, while preserving all numbered statements in the R1 revision.
- Existing R1 marked version, 49 reviewer responses/77 locators and Editorial Manager abstract are **not** synchronized with the experimental paper.

Outcome: no decisive counterexample to the audited central claims, and no detected new proof dependency from editorial shortening. “Coherent” is not “formally proved.”

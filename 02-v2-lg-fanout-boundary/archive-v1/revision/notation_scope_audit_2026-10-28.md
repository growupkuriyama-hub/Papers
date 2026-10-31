# #2 MCFG referee-style editorial audit: first use, symbol scopes, and collisions
Date: 2026-10-28 JST. Status: **implemented as source edits in English and Japanese on the paired PR**, with source-level structural validation. This is an editorial mathematical-notation review; it is **not** a formal proof verification or a scholarly priority audit.

## Trigger and scope

The TCS revision-review experience motivated an independent inspection of the current I&C-target #2 MCFG masters for (1) terminology or assumptions appearing before definitions, (2) symbol names with multiple meanings, (3) ambiguously suppressed grammar arguments, and (4) quantifier/scope mismatches between text and mathematics. Review was carried out against the **live GitHub source**, not an earlier PDF or arXiv version.

The check covered section and theorem inventories, definitions, major proof interfaces and appendices throughout the **4,000+ line English** and **2,000+ line Japanese** files, with deliberate closer inspection of:
- Introduction, notation table, positive-data/semigroup/MCFG/tuple definitions;
- operator Const/Link/Comp, canonical distributional classes and witnesses;
- thickness, typed-thickness, rare-type and polynomial upper-bound statements;
- finite-group block selection, local-group/LI criteria, window/abelian cases;
- untyped standard-grammar normalization and pattern-thickness appendix;
- constructive rule budgets, relaxed semantic representatives, abelian Parikh proof;
- lower-bound/nonlift, intrinsic rule-rank/EDT0L, concluding open-problem quantifiers.

No new lower-bound theorem was introduced; no upper-bound exponents or assumptions were relaxed.

## Verified ambiguities and source fixes (EN + JP)

| Category | Before | Fix | Why |
|---|---|---|---|
| **Notation collision: semantic vs syntactic brackets** | \`[X]\` denoted the \`≡_{L,s}\`-class of a typed nonterminal, while \`[tuple x]\` already denoted a syntactic nonterminal of the learner | Use \`Cl_{L,s}(X)\` (typeset \`\operatorname{Cl}_{L,s}(X)\`) for the semantic class, explaining the distinction explicitly; keep \`[tuple x]\` for the reconstruction grammar | Prevents conflating language equivalence classes and grammar objects |
| **Same literal symbol, incompatible mathematical sorts** | \`c_R\` = scalar number of terminals in the computed-rule budget; later \`c_R∈N^Σ\` = terminal Parikh vector | Use \`\mathbf c_R\` for the vector, preserve scalar \`c_R\`, explain distinction | Otherwise a formula silently changes the sort of the same notation |
| **Global constant vs local grammar nonterminal** | \`C\` used both as theorem's universal multiplicative constant and nonterminal \`C∈V\` in its proof | Rename bound constant \`C_{\mathrm{ab}}\` | Clears a genuine same-proof variable clash |
| **Undeclared free semigroup symbol** | \`eSe={e}\` in LI class definition without locally binding \`S\`, also grammar start symbol elsewhere | Quantify finite semigroup \`T\`, use \`eTe={e}\` and \`T×A\` | Explicitly binds variable and separates grammar start symbol |
| **Use before definition** | \`U_f\` appears inside introductory \`M_{A,f}\` formula; defined much later | State \`U_f=f^{f+1}f!\` at first use | No reader must search ahead to decode displayed quantity |
| **Use before definition: algebra** | \`local group\`, \`pseudovariety\` in Introduction | Add concise descriptions at their first discussion; maintain precise definitions in the technical section | Removes essential algebraic terminology as implicit prerequisites |
| **Use before definition: parameters** | \`H_{\mathrm{red}}\` in introductory bounds, \`Obs(K)\` with an unnamed fixed \`f\` | Explain trimming and explicitly bind \`f≥1\` when defining observations | Local scope is visible |
| **Undefined conventional notations** | \`[m]\`, group exponent \`\exp(A)\`, \`\mathfrak S_d\`, Parikh map \`\psi\` and finite-index EDT0L used with implicit conventions | Give concise definitions at first pertinent use | Avoids disputes over conventions / index meaning |
| **Zero-sum terminology** | \`zero-sum-free\` invoked to define \`d(H)\` without its operational meaning | State “no nonempty subsequence summing to the identity” | Makes group constant definition self-contained |
| **Unbound grammar in proof** | \`I∈Pat(A)\` in pattern-transfer proof, while defined \`Pat_H(A)\` and grammar \`H_red\` | Write \`I∈Pat_{H_red}(A)\` and \`L_A(H_red)=⋃_I F_{A,I}\` | Prevents collision with the normalization lemma’s later, separately defined local \`Pat(A)\` |
| **Same row-value symbol with inconsistent TeX forms** | \`\operatorname{val}_c\` in body, \`\mathrm{val}_c\` in appendix | Uniform \`\operatorname{val}_c\` across both | Consistent notation across theorem and proof |

All changes are mathematical notation, grammar-independent definitions or brief expository clarifications. The original family of operators, all quantifiers, witness data, theorem labels, proofs’ inference steps, and stated asymptotic rates were intentionally preserved.

## Structural audit (run on patched EN and JP)

- **135 labels per language**, identical label order, no duplicates.
- **93** theorem-like environments (definition/lemma/proposition/theorem/corollary/remark/open problem/example), identical order and types.
- **39** bibliography entries per language, identical keys and order.
- **350** internal \`ref\`/\`eqref\` etc. commands per language, with **zero unresolved target labels**.
- **Zero unresolved citation keys** in both sources.
- Braces are balanced in a source-level scan that ignores escaped braces and unescaped TeX comments.
- Semantic \`[X]\` in mathematical notation is eliminated; the remaining literal \`F[X]\` is a **context filled by X**, not a semantic-class bracket.
- Row value notation is unified; semantic class labels and ordinary learner nonterminal brackets are separated.
- No results from research-only Astra/Claude Problem G files were added to \`main.tex\`.

These checks validate syntax-level consistency and cross-language parity; they cannot certify mathematical correctness, TeX line breaking, complete natural-language translation accuracy, or external priority.

## Intentionally retained scoped overloads / risks (not silently rewritten)

- \`G,H,S\` for grammar presentations/start versus \`\mathsf S\` for the typing image; distinct glyph/case conventions are fixed in the notation table.
- \`R\` for a locally bound grammar rule and \`r/r_max\` for rank; declared within each proof.
- \`T\` for a derivation tree and the locally defined lattice shift-length budget \`T\` in the abelian proof; locally introduced, but could be changed to \`T_{\mathrm{lat}}\` if a human referee insists. Extensive subscript edits would add risk without changing semantics.
- \`\mathsf{Pat}(A)\` in the **normalization lemma itself** is intentionally defined locally and differs from \`\mathsf{Pat}_H(A)\` for arbitrary input grammars.
- Group noncommutativity case divisions, the full good-normalization construction, and the integer-programming small-solution lemma are nontrivial mathematical proof obligations; this editorial pass does **not** independently reprove them.
- The characterization of **refinement thickness** at all fan-outs remains distinct from a **characteristic-data lower bound** at fan-out two. The latter is still open.

## Publication guardrails

Run the bilingual PR verification (English pdfLaTeX and Japanese LuaLaTeX), inspect logs for undefined references, errors and overfull lines before merging. Source-level edits should not be mistaken for review of the PDF appearance. Maintain the present M1–M3 data lower-bound scope and do not import speculative research-only results.

If a later human or AI reviewer alleges “undefined variable”, request a specific location, exact free symbol and quantified scope; a generic request for a matching exponential lower bound is **not** a notation defect.

# MCFG #2 v81 — pre-submission manuscript preflight

Date: 2026-10-18. Target: Information and Computation.
Base: GitHub main v80, commit cc2503a2abb2d0ad8f0e30c11fb903387697ed52.
Purpose: independent mathematical/editorial source review and safe preparation;
not a statement that the paper has been independently peer-reviewed.

## Findings and repairs

1. **Long abstract:** prior English abstract was about 330 words and
   did not prioritize the v80 work efficiently. Both abstracts were rewritten
   to foreground the actual O(||G||^2 theta_bar) window theorem,
   O(||G||^3 theta_bar) group/LG results, rank-one result, abelian-filter
   theorem, characteristic-witness improvements, and the all-typing
   fan-out-two obstruction. The new English abstract is about 210–220 words.
   Journal-specific final limits must still be checked at submission.
2. **Stale conclusion:** v80 conclusions omitted its key new results.
   Both now distinguish:
   - algebraic sufficient condition (LG positive-image semigroup);
   - language-based sufficient condition (abelian-filtered targets);
   - algorithmically computable grammar-derived rule-only witnesses;
   - existential distributional witnesses, which need not be grammar-derived.
   The higher-fan-out superpolynomial sample lower bound remains OPEN.
3. **Data availability:** changed from a generic "No data" to specify
   that there were no *empirical datasets*, and to point to public
   reproducibility scripts. Finite checks are not presented as proofs.
4. **Elsevier AI disclosure:** explicit existing declaration identifies
   ChatGPT and Claude, mathematical exploration, drafting/critique,
   literature checking and author accountability. Final human approval
   remains needed under Elsevier's 2026 generative-AI policy.
5. **Bibliography:** checked Papadimitriou 1981, "On the Complexity
   of Integer Programming", Journal of the ACM 28(4):765--768,
   DOI 10.1145/322276.322287, which justifies the small-solution
   ingredient of the abelian-filter argument.

## Mathematical source audit (not formal proof certification)

- The type-deletion and rare-type arguments have the required
  regular intersection / characteristic-set quantifiers.
- The power-transfer argument has a shared accepting context with a
  nonempty separator; the universal-finite-typing obstruction
  changes the first opening-bracket run of the unique ceiling-free word.
- The Ramsey shift factorization equates componentwise monoid values
  using the chosen five cuts and a nonempty letter separator.
- Relaxed distributional representatives require BOTH symbol and
  rule witnesses; v79 rule-only elimination does NOT apply to them.
- The abelian-filter proof explicitly fixes alphabet and finite typing
  and reduces to a nonnegative integer system with a fixed number
  of equations and polynomially bounded variables/coefficients.
  The auxiliary abelian group is unrestricted, but a bounded-rank
  reduced good MCFG presentation of the target is assumed.
- The manuscript does NOT establish Conjecture E or the universal
  fan-out-two original-thickness polynomial bound.
- Dedicated v80 computational sanity-check script
  (v79_check_all_typing_obstruction.py) was rerun on 3,000 random
  transformation typings with three offsets each: PASS. This
  is supplementary empirical cross-checking only.

## CI layout correction

- Dedicated v81 EN/JP builds passed. The Japanese LuaLaTeX log initially
  reported one `Overfull \\hbox` of 37.2546 pt near the long relaxed-witness
  formula (JP source lines 2859--2875), despite zero unresolved citations
  in the final compilation pass. Reformatted that formula as displayed
  mathematics without changing its value. The subsequent Japanese
  LuaLaTeX review run succeeded with **zero overfull and zero underfull
  boxes**. The combined MCFG workflow generated an English 52-page PDF
  and a Japanese 57-page PDF. The English log retained only two minor
  underfull warnings; no final-pass undefined-reference error remained.

## Remaining gates before pressing Submit

- Dedicated EN/JP LaTeX build and reference checks on the final commit.
- Full-page visual examination of the FINAL compiled PDFs, including
  theorem environments, long displayed equations, and bibliography.
  Build success alone is insufficient for that visual gate.
- Author-led spot-check of the local-group Rees-coordinate reduction,
  arbitrary finite-group order homogenization and nonmerging
  witness-composition proof. Full independent expert refereeing is
  precisely what the I&C submission will seek; it is not presented as
  a prerequisite to making that submission. AI scrutiny alone is
  not formal proof certification.
- Author confirmation of all abstract novelty statements, affiliation,
  AI declaration, submission metadata, and relationship to TCS #1.
- Confirm I&C's current guide-for-authors details, cover letter and
  disclosure fields at the time of submission.

The manuscript was *not submitted* by this preflight.

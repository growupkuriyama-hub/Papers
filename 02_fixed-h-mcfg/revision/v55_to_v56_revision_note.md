# MCFG v55 -> v56 revision note

## Purpose

v56 corrects the pre-submission manuscript after an independent review found
that the minimum-rank-two witness introduced in v48 is false.

The previous manuscript claimed that the language \(L_{\mathrm{r2}}\) was not
in \(\mathsf{MCFL}(2,1)\).  This is incorrect: the language admits a
fan-out-two, rule-rank-one MCFG presentation.  The claimed lower bound therefore
cannot support a language-level separation between the rank-one and higher-rank
characteristic-data theorems.

## Main correction

The subsection **A Genuine Minimum-Rank-Two Boundary-Typed Target** and
Theorem \`thm:genuine-ranktwo-witness\` have been removed in full.

The earlier lower-bound argument passed through a four-paired-block language
recorded outside SL-TAL and then used a claimed identification of SL-TAL with
unrestricted fan-out-two rank-one MCFLs.  The explicit rank-one counter-
presentation shows that this chain cannot be used for the standard
\(\mathsf{MCFL}(2,1)\) class employed in the present manuscript.  The Kato,
Kato--Seki--Kasami, and Uemura references that were used only for this withdrawn
argument have therefore been removed from the manuscript bibliography.

This revision does **not** affect the verified positive facts about the old
example (its displayed rank-two grammar, boundary-typed membership, or its
separation from Yoshinaka's untyped class); they are simply no longer needed
for the paper once the rank lower bound is withdrawn.

## Repositioning of the higher-rank theorem

The prefix--suffix higher-rank theorem is now stated and discussed as a
**presentation-sensitive quantitative result**:

- rule rank one: characteristic data polynomial in grammar size alone;
- arbitrary fixed rank under boundary-determined typing: characteristic data
  polynomial in the size and rule thickness of a reduced good presentation;
- no claim is made that the second theorem reaches a strictly larger language
  class when fan-out is allowed to vary.

The paragraph immediately following Theorem \`thm:boundary-polydata\`, the
abstract, the Contributions paragraph, the comparison section, and the
Conclusion have all been revised consistently with this scope.

## New open problem

The Conclusion now asks explicitly whether there exists a finitely typed
substitutable MCFG language that has **no** rule-rank-one MCFG presentation at
any finite fan-out.  The broader tradeoff among fan-out, rule rank, and typed
presentation size is also recorded as open.

No replacement witness is asserted in v56.

## Additional cleanup

- The normalization attribution to Seki et al. is narrowed to the
  nondeleting/information-lossless step underlying the proof of Lemma 2.2,
  with the rank-preserving formulation attributed to Kanazawa.
- Repeated companion-paper disclaimers were compressed to a single
  relation-to-prior-work discussion.
- The exact Yoshinaka rule correspondence is stated compactly in the
  Introduction and still proved in Proposition \`prop:yoshinaka-type-guard\`.
- The existing \(\theta_G/\tau_G\) notation table is retained; no risky
  notation-wide renaming was made.

## Static checks

After the edit:

- no occurrence of \`genuine-ranktwo\`, \(L_{\mathrm{r2}}\), or the withdrawn
  minimum-rank-two claim remains;
- no unresolved \`ref\` / \`eqref\` targets were found;
- no unresolved citation keys were found;
- no duplicate labels or bibliography keys were found;
- all \`begin\` / \`end\` environment counts match;
- unescaped brace balance is zero.

A full TeX-engine build was not run in this connector-only pass.

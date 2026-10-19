# Hybrid v2: canonical Q_h typed BUNF, unchanged v230 learner
Date: 2026-10-19
Base: main @ f0f895ecc1de82c099992a12234fa9638bde1282 (TCS #1 v230)
Status: EXPERIMENT ONLY; no TCS submission, no arXiv update, no merge authorized.

## Mathematical construction
Let S_h = h(Sigma^+) be the positive-image semigroup. Let Q_h=S_h\sqcup{e} be its freshly adjoined identity completion, where e is not an element of S_h even when S_h already has an identity. Define q_h(lambda)=e and q_h(w)=h(w) for positive w. Thus ker q_h is exactly the positive-word h-kernel together with (lambda,lambda), and Q_h is a canonical image of the older M^sharp completion. Its cardinality is |S_h|+1 <= |M|+1.

**Learner stays literally v230.** Section 4 (Rec_h with Rules B/U/L/S and *only positive-word factor nonterminals*, and the conservative sequential learner) and the polynomial build complexity section have been verified textually byte-identical to v230. No epsilon factor symbol is ever introduced into the hypothesis.

The target is any reduced BUNF grammar (binary/unit/terminal/nullable). Split *every* target nonterminal, including the original start symbol, by q_h-yield type in Q_h. A typed e-symbol can derive only lambda. Retain the four witness families from the prior full-unification experiment: symbol/terminal/unit/binary; lambda belongs automatically to the first family through the typed start copy of e-type when lambda is in L.

## Key hybrid completeness lemma
Simulate only retained typed X with positive q_h type:
  [omega(X)] =>* w for every X =>* w.
For a terminal rule: use U then L.
For a unit rule: use U to the positive typed child.
For a binary rule where both children are positive: use U then B and both induction hypotheses.
For a binary rule with exactly one nullable child: its entire yield is lambda, so the binary witness reduces to the canonical yield of the sole positive child; use a *direct U rule*, no epsilon factor nonterminal, then induction.
Two nullable children imply nullable parent and do not enter positive simulation.
For positive start yields use the v230 S -> [w] rule; for lambda use the v230 S -> lambda rule, justified by the first witness family for the e-typed start copy.

Hence the original v230 Rec_h reconstructs all of L given the Q_h/BUNF witnesses (whether or not L is substitutable or K is positive-only relative to L). Soundness itself is *identical to v230*, and exact characteristic sets follow under the original fixed-h substitutability assumption.

## Quantitative compatibility
On an SSBNF source grammar, productive typed copies of original non-starts all have positive type and coincide with the old split after trimming; the new typed copies of S0 contribute only already-present canonical start yields or lambda witnesses. Consequently the *set* of witnesses and typed thickness coincide with v230. General BUNF witness upper bounds now count |V||Q_h| symbols, |P_unit||Q_h| unit rules and |P_bin||Q_h|^2 binary rules. SSBNF normalization continues to be used in polynomial window/group and linear-spine theorems.

## Claude deep-review findings for prior PR #59: addressed by design
- Prior false Takada control-set fiber statement: fixed with q_h, Q_h and initial accumulator (e,e). Original h-based control set is distinguished explicitly.
- Prior ambiguous/inactive empty-factor elimination lemma: no longer needed; no extra empty-factor grammar exists, so no lemma or extra maintenance burden.
- Prior unresolved empty-yield-type scope: new Lemma 2.2 defines q_h on *all* words, including lambda.
- Prior English/Japanese BUNF mismatch and obsolete JP empty-target C_L: corrected.
- Prior identity confusion: distinguish 1 in U_1 from fresh e of Q_h.
- Prior two-target-form restriction: qualitative exact reconstruction generalized to arbitrary reduced BUNF; quantitative results continue to invoke SSBNF.
- Prior incorrect reviewer-response/marked PDF coordinates: this branch does not claim its v230 response and PDF artifacts represent the experimental TeX.

## Explicit gates before any journal use
1. Full independent adversarial mathematics audit of positive-only simulation, especially nullable/unit cycles and preservation of SSBNF witness sets.
2. Check quantitative proofs throughout Appendix A and linear section with Q_h typed start copies, and check Clark CONG definition permits the required grammar.
3. Regenerate English/Japanese PDFs from this branch and inspect typesetting.
4. If and only if adopted, update the English and Japanese responses and regenerate marked manuscript, all 49 comment anchors and all 77+ page/margin-line references, submission PDF/ZIP and abstract. v230 response artifacts are *not* current with hybrid v2.
5. Keep main's v230 untouched; do not merge while experimental.

This file is a research note, not a reviewer response or proof certification.

## 2026-10-19 — focused Q_h unification audit after completeness compression

### Core proof condensation
The English completeness theorem/proof was compressed from 72 source lines and 2,874 characters to 47 source lines and 1,978 characters. The preceding v230 version uses 43 lines/2,117 characters. The Japanese counterpart was shortened from 70 to 48 lines. No hypotheses or witness families changed in this shortening.

The proof uses a single witnessed-unary simulation principle. For any productive typed X of positive q_h-type and a successful first production rho:X->alpha, define t_rho by replacing every nonterminal Y in alpha by omega(Y). Typed lifting gives q_h(t_rho)=q_h(omega(X)) != e. The first-symbol witness and the rule witness yield a shared sample context, so the original v230 Rule (U) supplies [omega(X)]->[t_rho]. The remaining derivation uses Rule (L) for a terminal, induction for a unit production, Rule (B)+induction for a binary production with two positive-type children, or direct induction when one child has empty type. No [lambda] is ever introduced. For the start copies, positive witness -> original (S), and empty witness -> original (S)->lambda.

### Positive changes supported by Q_h (implemented)
1. **Canonical quotient:** Q_h is the image monoid of q_h and is isomorphic to Sigma*/ker q_h. The fresh identity distinguishes lambda from all positive words, even when the original S_h has an internal identity. A special empty-alphabet case Q_h={e} is spelled out.
2. **Refinement order and products:** ker(q_h') subset ker(q_h) iff ker(h'|Sigma+) subset ker(h|Sigma+); ker(q_{h x g})=ker(q_h) intersection ker(q_g). Moreover Q_{h x g} is the image (not necessarily all) of q_h x q_g inside Q_h x Q_g.
3. **Erasing inverse homomorphism:** For phi:Gamma*->Sigma*, instead of the older erasure-flag product (h o phi) x e_phi, one can use t=q_h o phi:Gamma*->Q_h, and obtain phi^-1(L) in RS_t (and in the CFL slice for context-free L). This is a genuinely useful proof simplification and absorbs the erasure flag. A quick independent proof: equal t-types imply both images are lambda or both positive with equal h-type; shared inverse-image contexts then transfer substitutability. The old erasure-flag kernel and the new t-kernel agree on all Gamma*.
4. **Typing adequacy:** the all-fragment congruence ker q_h (instead of the positive restriction of ker h) expresses the exact separation requirement for common-context unequal distributions; stronger ker q_h subset syntactic congruence forces regularity.
5. **Gold corollary:** the finite-witness convergence condition now quantifies over arbitrary reduced BUNF targets, because the unchanged v230 learner was proved complete for those witnesses.
6. **Finite-state control:** the control construction is stated once for any finite-monoid typing t, then specialized to t=h and t=q_h, including the empty type e. This prevents the older Takada-control identity mismatch.
7. **Clark congruential grammar:** the q_h-typed BUNF copies cover nullable symbols without introducing an extra artificial epsilon-only initial symbol.
8. **Quantitative constants:** the general bound uses |Q_h|=|h(Sigma+)|+1 rather than |M|+1; it can avoid unused elements of M. For SSBNF the witness set and thickness stay exactly those of v230.

### Not unified on purpose (mathematical guardrails)
- **Algebraic locally-trivial/group conditions:** they apply to the *positive image semigroup* S_h, NOT Q_h. The new global unit e of Q_h witnesses failure of local triviality for any nonempty S_h, since e t e=t != e for t in S_h. Replacing S_h with Q_h in Proposition li-window or the LI-join statements would be false.
- **Reconstruction grammar:** only observed nonempty factors and the original direct start-epsilon rule; rewriting the hypothesis to Q_h-typed/empty-factor rules is redundant and would defeat the goal of Hybrid v2.
- **Positive-image/window-kernel proofs:** keep restricted-positive forms when quoting existing semigroup literature or doing explicit window counts; the ker-q reformulation is available but not automatically shorter.
- **Semilattice lower bounds:** keep the original U_1 identity 1 distinct from the new e of Q_{h_U}; in particular q_{h_U}^{-1}({1}) contains nonempty words only.
- **Clark--Eyraud untyped all-fragment definition:** cannot simply be identified with q_h-typed all-fragment substitution; the latter deliberately separates lambda and positive words.

### Review and submission limitations
These are author-side mathematical edits, NOT an independent referee certification. The previous Claude findings against the older all-factor experimental PR #59 are addressed as described above, but new v2 arguments (especially erasing inverse images and the generic witnessed-U completeness induction) need fresh adversarial review.
The v230 reviewer responses, locator table, prebuilt PDF binaries and submission ZIP remain unchanged on this branch. A successful CI-generated PDF is only an experimental build, not a TCS-submission package.

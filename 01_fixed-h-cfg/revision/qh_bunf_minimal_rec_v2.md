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

# MCFG #2 v92 — R1/R2-oriented editorial tightening (EN/JP)

Date: 2026-10-23.

**Status:** Editorial revision only; no mathematical assertion, definition,
lemma, theorem, proof, assumption, asymptotic bound, or citation identifier
is changed. Prior mathematical v91 (sliding separators / no lift of the
doubling family, and local-group cubic data theorem in the main text)
remains intact.

## Six requested edits

1. **Abstract.** Replace the earlier long, list-like abstract by a concise
   problem/method/bounds/scope abstract. Retain the window quadratic and
   window–finite-group/local-group cubic bounds; correctly attribute the
   qualitative learning mechanism to Yoshinaka; mention the rank-one,
   abelian-filtered, effective witness, intrinsic-rank-two, and new
   fan-out-two non-transfer results in compact form.
2. **Public preprint.** Condense the preprint relationship to two short
   clauses, making arXiv:2605.11644 historical rather than equating it
   with the current working source.
3. **Prior art and scope.** Reduce duplication; explicitly distinguish the
   proved SUBST_D case of Yoshinaka 2015 from the present substructure
   correspondence, identify inherited CFG and rank-one results, and
   foreground ordered simultaneous noncommutative shortening as an MCFG
   quantitative contribution.
4. **Front AI paragraph.** Delete the redundant Japanese-only
   "Proof method and AI-assisted research" front-matter paragraph. Retain
   the formal disclosure.
5. **Conclusion (§7).** Replace lengthy recapitulation with the
   characteristic-data bound hierarchy, scope of examples, non-transfer
   obstruction, and the one outstanding higher-fan-out question.
6. **AI disclosure.** Move the existing full text of the separate
   ChatGPT/Claude declaration from before the technical appendices to
   **immediately before** \`thebibliography\`, after the final active
   appendix in **both** editions. Position reflects Elsevier journal
   GenAI policy:
   https://www.elsevier.com/en-gb/about/policies-and-standards/generative-ai-policies-for-journals

## Source edit boundary

- \`main.tex\`
- \`japanese/main_JP.tex\`
- \`PAPER.yaml\`
- This revision note

No source appendices or other mathematics are modified.

## Acceptance tests

- English pdfLaTeX / Japanese LuaLaTeX;
- No unresolved references/citations/duplicate labels;
- EN/JP narrative and labeled mathematics correspond;
- Exactly one separate disclosure in each edition, located after the last
  appended proof and immediately before the bibliography;
- All v91 mathematical labels and theorem statements untouched;
- Proofread first, conclusion and bibliography transition pages.

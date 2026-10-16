# #2 MCFG v67a–v67b: Yoshinaka (2015) priority clarification

Date: 2026-10-16
Branch: `revision/02-yoshinaka2015-v67`
Base: main, internal v66
Status: **draft for independent mathematical review; not merged into main**

## Purpose

Clarify the qualitative learning boundary with R. Yoshinaka, *General Perspective on Distributionally Learnable Classes*, MoL 2015, pp. 87–98, DOI 10.3115/v1/W15-2308.

The author's general Theorem 1 identifies substitutable languages over suitable grammar signatures from positive data. Assumptions 1–3 require effective membership/context operations, uniformly bounded operation arity, and polynomially enumerable observed structures, contexts, and operations. Example 3 specifically treats MCFG-style tuple signatures at bounded fan-out and operation arity.

## Scope of the proposed embedding

For **fixed alphabet, fan-out f, finite monoid observer h, and rank cap r**, a signature with tagged nonempty tuple sorts `T_{d,mu}`, good rank-bounded templates, unary start promotion, and separate epsilon start generation is proposed.

Proposition `prop:yoshinaka2015-embedding` records and proves the inclusion

`C_mcf(f,h) ∩ MCFL(f,r) ⊆ substitutable languages over S_{f,r,h}`.

The tuple-context comparison hinges on good nonmerging rules: along an open derivation context, components of the distinguished child remain separated by nonempty terminal yield. Thus signature contexts are admissible in #2's positive sentence-context interface. This is a **one-way inclusion**; equality of the two substitutability notions is not asserted.

Under the fixed bounds, operation templates have bounded numbers of variable occurrences and admissible decomposition witnesses are polynomially enumerable in input-word length. This supplies the requisite **signature-level** effective conditions. The direct, explicit #2 constructor remains independently valuable and can work without a uniform rule-rank cap.

## Files and changes

- `02_fixed-h-mcfg/main.tex`: Abstract, early Introduction paragraph, first contribution, prior-work section, new embedding proposition after target-class definition, Yoshinaka 2015 bibliography.
- No changes to core learner, old theorems, separation witnesses, or #3/#7.
- No group-kernel observer theorem imported in this step (deferred as agreed).

## Integrity / outstanding gates

- [x] New citation key `Yoshinaka2015General` supplied
- [x] Required TeX environment names balanced
- [x] Source and line-count comparison done in GitHub edit step
- [ ] Independent proof review of the context-interface bridge, especially all allowable signature operations
- [ ] Independent check of Assumptions 1–3 under the chosen tagged-sort signature, including `FUN(d)`
- [ ] Two-pass LaTeX build and visual PDF check **not yet performed**
- [ ] Update `PAPER.yaml` after the draft is accepted and its source hash/build are verified
- [ ] Merge into `main` only after technical checks

## Priority warning

Do not claim that Yoshinaka 2015 supplies polynomial *positive data lengths* in the original untyped MCFG size/thickness parameters; its Theorem 1 is a qualitative positive-identification theorem and the finite witness size is expressed through a chosen signature grammar. Do not claim that the 2015 theorem directly handles arbitrarily large finite rule rank with a single fixed signature satisfying Assumption 2.

Reference: https://aclanthology.org/W15-2308/

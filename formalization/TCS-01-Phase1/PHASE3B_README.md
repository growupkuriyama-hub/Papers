# TCS Lean Phase 3B — first-visit suffix factorization and complete Recognition Lemma C.1

Paper: Takayuki Kuriyama, *Distributional Learning of Context-Free Languages under Fixed Finite-Monoid Typing*, manuscript TCS-D-26-00494.

**Status: Milestones A–E fully verified, including BOTH assertions of Appendix C Recognition Lemma C.1. Optional complete-subtree exchange also verified.** This is **not** a proof of all Appendix C: branch synchronization, path congruence, unconditional Clark–Eyraud substitutability and unconditional typed substitutability remain open.

## Source / version / provenance

- Source of truth: `01_fixed-h-cfg/main.tex`; inspected main HEAD `9a094b68ed683c85e2eab8f33cd978f45af0a19f`, file blob SHA `bc638f6032cb04414cb36a88ad6953188097add1`, `PAPER.yaml` internal **v215**. The user anticipated v213; v215 is newer. The five parser transitions and relevant CFG derivations are unchanged relative to Phase 3's v212 source. Changes in the intervening paper versions are unrelated notation and proof-presentation refinements. The protected paper files were not modified here.
- Branch: `formalization/tcs-phase3b-suffix-recognition-20261017`; based on Phase 3 completed commit `1e400c20d05d49648095bc8324303c0b5e67cf77`. Phase 1–3 Lean source declarations were not altered.
- Lean 4.24.0, Lake 5.0.0, Mathlib tag v4.24.0 (historical resolved SHA `f897ebcf72cd16f89ab4577d0c826cd14afaafc7`). Existing `lean-toolchain` is unchanged. A manifest is not tracked, and CI runs `lake update`.

The terminals retain their Phase 1/2 constructor names: `Terminal.a`=a, `Terminal.left/right`=floor delimiters, `Terminal.squareLeft/squareRight`=ceiling delimiters. The parser is the exact five-rule bounded `Step bound`, with separate `Run bound` and an independent grammar `Derives i w` inherited from earlier phases.

## New sources

- [TCSPhase3Suffix.lean](TCSPhase3Suffix.lean): empty-stack inertness, inverse one-step suffix split, **complete first-visit run factorization**, and `Run (α++ψ) w ψ ↔ Run α w []` for nonempty α.
- [TCSPhase3Marker.lean](TCSPhase3Marker.lean): single closing-marker behavior, last-marker preservation until the stack is emptied, and impossibility of two different closing markers at the bottom of equal stacks.
- [TCSPhase3RecognitionConverse.lean](TCSPhase3RecognitionConverse.lean): height-inductive parser-to-`Derives` implication, exact closing marker consumption, **recognition converse** and **recognition_iff**.
- [TCSPhase3RecognitionFull.lean](TCSPhase3RecognitionFull.lean): opening-prefix invariant implies initial nonterminal height, yielding the **second assertion of Recognition Lemma C.1** for arbitrary starting stacks.
- [TCSPhase3Subtree.lean](TCSPhase3Subtree.lean): optional **complete-subtree exchange** as unconditional equality of actual `Distributions (Language n)`.
- [TCSPhase3BMain.lean](TCSPhase3BMain.lean): explicit dependency and printed-axiom audit for the main Phase 3B theorems.
- [PHASE3B_VERIFICATION_REPORT.md](PHASE3B_VERIFICATION_REPORT.md): audit, statement-by-statement correspondence, execution and remaining work.
- [Phase 3B GitHub Actions workflow](../../.github/workflows/tcs-phase3b-lean.yml): automatic rebuild of all phases.

## Reproduce

```sh
cd formalization/TCS-01-Phase1
lake update
lake exe cache get
lean --version
lake --version
lake build
for source in TCSPhase1.lean TCSPhase2.lean TCSPhase2Bridge.lean \
  TCSPhase3Parser.lean TCSPhase3Recognition.lean TCSPhase3Congruence.lean \
  TCSPhase3Prefix.lean TCSPhase3Main.lean TCSPhase3Suffix.lean \
  TCSPhase3RecognitionConverse.lean TCSPhase3Marker.lean \
  TCSPhase3RecognitionFull.lean TCSPhase3Subtree.lean TCSPhase3BMain.lean; do
  lake env lean "$source"
done
grep -nE '(^|[^[:alnum:]_])(sorry|admit|axiom|opaque)([^[:alnum:]_]|$)' TCSPhase*.lean
```

The final grep must find no forbidden proof terms or assertions. Each new module has `#print axioms` directives. The complete successful run was **[GitHub Actions #39010703450](https://github.com/growupkuriyama-hub/Papers/actions/runs/39010703450)**, job `117332450214`, exact verified code commit **`4319a5c5a9671da10121764232df1e7bf5e96f4e`**. Its log reads `Build completed successfully (7378 jobs).` and `All Phase 1-3B modules compiled without proof holes`. Only standard Lean logical axioms occur, no `sorryAx`.

## Formalization scope and next proof frontier

First-visit decomposition distinguishes the remaining-active-prefix case from the **first** moment when the active prefix becomes empty; thereafter the parser may consume the exposed suffix. In particular it is stronger than Phase 3's forward-only `run_suffix` lemma.

Both parts of Appendix C Recognition Lemma C.1 are now proved for all heights `i ≤ bound`:
`Run bound (E_i :: ψ) w ψ ↔ w ∈ Language i`, and
`Run bound σ w θ → w ∈ Language i → ∃ψ, σ=E_i::ψ ∧ θ=ψ`.
The `Language i` in these statements is Phase 2's independently verified actual CFG language.

Subtree exchange can now be proved using the recognition equivalence and the arbitrary-state assertion. The only remaining major Appendix C chain is **branch synchronization → path congruence → unconditional ClarkEyraud (Language n) → unconditional TypedSubstitutable hU (LanguageMinus n)**. No substitute assumption has been introduced for those unresolved propositions.

No manuscript, translation, reviewer response, clean/marked PDF, arXiv source or Editorial Manager submission was touched, and the branch was not merged.

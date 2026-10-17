# TCS Appendix C — Lean 4 Phase 3 (partial, proof-checked)

Paper: Takayuki Kuriyama, *Distributional Learning of Context-Free Languages under Fixed Finite-Monoid Typing*, TCS-D-26-00494.

**Result: foundational partial success, NOT Appendix C completion.** The unconditional theorems `language_clark_eyraud` and `languageMinus_typed` are **not** defined or proved in this phase. See [PHASE3_VERIFICATION_REPORT.md](PHASE3_VERIFICATION_REPORT.md).

## Canonical source and provenance

- Latest source checked: `01_fixed-h-cfg/main.tex`, internal version **v212**, main commit `4193be1fb437a67479ca75ace368571c7d38d389`, manuscript blob SHA `b64aea13d875e7ebd8aa8c5a57ec46dd9def3006`. Main Appendix C lines 2197–2358 and bracketed grammar lines 1108–1131.
- Work branch: `formalization/tcs-phase3-appendix-c-20261016`, based on proven Phase 2 commit `adf208645921f54b9ce4d9a1f05ee08396dca50e`.
- The earlier phases' modules `TCSPhase1.lean`, `TCSPhase2.lean`, and `TCSPhase2Bridge.lean` are unchanged.
- Lean 4.24.0, Mathlib git tag v4.24.0. The repository does not track a `lake-manifest.json`; `lake update` resolves the pinned Mathlib tag during a build.
- The v212 notation-only manuscript revision does not change the Appendix C transition rules. Existing Lean constructors `a`, `left`, `right`, `squareLeft`, `squareRight` represent respectively the literal terminals `a`, floor-left, floor-right, ceiling-left, ceiling-right.

## New Lean modules

- [TCSPhase3Parser.lean](TCSPhase3Parser.lean): five bounded one-letter transition constructors, inductive word runs, empty run, concatenation/decomposition, determinism, per-letter and whole-word reverse injectivity, untouched stack suffix extension, strictly decreasing weight and no nonempty cycles.
- [TCSPhase3Recognition.lean](TCSPhase3Recognition.lean): **forward** Lemma C.1 direction; actual `Derives i w` from Phase 2 yields a run `E_i ψ --w→ ψ` with any stack suffix ψ and bound ≥ i. The converse and the lemma's last assertion remain unverified.
- [TCSPhase3Congruence.lean](TCSPhase3Congruence.lean): equality of context distributions is compatible with concatenation on either side.
- [TCSPhase3Prefix.lean](TCSPhase3Prefix.lean): a structural induction shows every generated `L_i` word starts with exactly i opening terminals followed by `a`.
- [TCSPhase3Main.lean](TCSPhase3Main.lean): import-only proof audit aggregator; intentionally does not claim the missing final theorem.

## Reproduce

From this directory:

```sh
lake update
lake exe cache get
lean --version
lake --version
lake build
for f in TCSPhase1.lean TCSPhase2.lean TCSPhase2Bridge.lean TCSPhase3Parser.lean TCSPhase3Recognition.lean TCSPhase3Congruence.lean TCSPhase3Prefix.lean TCSPhase3Main.lean; do
  lake env lean "$f"
done
grep -nE '(^|[^[:alnum:]_])(sorry|admit|axiom|opaque)([^[:alnum:]_]|$)' TCSPhase*.lean
```

The scan's last command should return no matches. Each module contains explicit `#print axioms` checks. CI: [successful proof-build for Parser, Recognition, Congruence, Prefix, and previous phases #39004601678](https://github.com/growupkuriyama-hub/Papers/actions/runs/39004601678). The Main aggregator is separately compiled in the later branch CI.

**Not yet proved**: first-visit suffix factorization, final closing-marker invariant, recognition converse and arbitrary-state final assertion, subtree exchange, branch synchronization, path congruence, `ClarkEyraud (Language n)`, and unconditional typed substitutability of `LanguageMinus n`. No part of the TCS manuscript or PDF was modified.

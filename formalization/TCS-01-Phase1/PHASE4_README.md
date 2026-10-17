# Phase 4 — Presentation-independent typed thickness, Lean 4

**Status:** The mathematical core is kernel-checked; the final integrated audit is executed by [tcs-phase4-lean.yml](../../.github/workflows/tcs-phase4-lean.yml). See [PHASE4_VERIFICATION_REPORT.md](PHASE4_VERIFICATION_REPORT.md) for the precise successful run ID, axiom report, boundaries, and original manuscript provenance.

## Source and branch

- Research target: Corollary 6.4, *presentation-independent typed-thickness gap*, of Takayuki Kuriyama, *Distributional Learning of Context-Free Languages under Fixed Finite-Monoid Typing*, TCS-D-26-00494.
- Official research source: `01_fixed-h-cfg/main.tex`, as of **2026-10-17**, main branch HEAD `7eecac48a1fc2391a0300ffcd7746609eaa62997`, **v222** in `PAPER.yaml`, main.tex blob SHA `3963c9f93c08d00cb47e0421ad5e16932d651051`.
- The complete Corollary 6.4 statement **and proof** are byte-for-byte identical to the earlier Phase 4 starting manuscript **v218** at main `8d4fcb749c58ffa513725eb459dcadc3964247ac`. Changes to other manuscript sections have not been imported into the Lean code.
- Existing Phase 4 branch: `formalization/tcs-phase4-intrinsic-thickness-20261017`, originally based on immutable Phase 3C HEAD `673939835e5fade5812b5808f5fb41fb57662c6c`. No other working branch; no merge to main.
- Lean 4.24.0, Lake 5.0.0, Mathlib tag v4.24.0. CI runs `lake update` and `lake exe cache get` before compiling.

## Fully independently defined mathematical objects

**Finite generic SSBNF grammar:** `SSBNFGrammar NT` has a finite non-start-symbol type `NT`, four independent fields `startRules : Finset NT`, `startEmpty : Bool`, `terminalRules : Finset (NT × Terminal)`, and `binaryRules : Finset (NT × NT × NT)`. The distinguished start is external to `NT`, so cannot appear on a RHS. Original derivation `DerivesFrom` and start derivation `StartDerives` are separate inductive relations. All rule sets are finite; **there is no fixed bound on their cardinalities**.

**Typed refinement:** `TypedDerives G A μ w` is an independent inductively generated relation with a terminal constructor indexed by `hU [c]` and a binary constructor indexed by the monoid product `μ * ν`. The exact `typed_lifting` equivalence to `DerivesFrom G A w ∧ hU w = μ` is proved, not stipulated.

**Successful-tree trimming:** `TypedOccurrence` models actual occurrences, including successful sibling derivations. `RetainedTypedSymbol` means a symbol occurs on such a path from an original start rule. `TrimmedTypedDerives` is a separate inductive relation allowing terminal and binary productions only on retained parents, with typed children also generated in the retained relation. Subtree grafting proves `trimmed_lifting` and `trimmed_grammar_language_eq`.

**Explicit finite typed production set:** `FiniteTrimmedRefinement G : SSBNFGrammar (NT × U1)` contains filtered `Finset`s for every typed start, terminal, binary rule, as well as the epsilon-start bit. The proofs `finite_trimmed_{start,terminal,binary}_iff` characterize each real retained production. `finite_trimmed_sound` and `finite_trimmed_complete` prove *equality of derivations*, while `finite_trimmed_grammar_language_eq` proves preservation of the entire start language. No grammar is represented merely as a set of words.

**Independent operational retention:** `OperationalReachable` is another inductive relation: successful typed start, then traversal of a binary production whose **both** child symbols are productive in the independently defined typed CFG. `operational_retained_iff` proves equality with successful-tree occurrence. Consequently `finite_operational_terminal_iff` and `finite_operational_binary_iff` characterize the explicit pruned `Finset`s by the operational relation. These are mathematical least-reachability proofs, **not executable fixed-point-trimming algorithms**, and do not claim termination or polynomial runtime for such algorithms.

**Typed thickness:** `shortestTypedLength G A μ` is the least length of a terminal word derivable from a retained typed symbol in the trimmed CFG, defined using `Nat.find`. `shortestTypedLength_spec` proves attainment; `shortestTypedLength_le` proves minimality; `shortest_length_characterization` proves any shortest/shortlex-selected yield has that same length. `retainedTypedPairs` is the exact finite set of retained typed non-start symbols, and
```lean
typedThickness G =
  max ( { shortestTypedLength G A μ | (A, μ) is retained } ∪ {1} )
```
is the actual paper parameter, **not the maximum length in the entire target language**. No new surrogate thickness parameter was introduced.

The actual finite trimmed CFG has exactly the retained productive `(A,μ)` symbols (`finite_trimmed_productive_iff_retained`) and exactly the same yield lengths (`finite_trimmed_shortest_length`), so the elements over which `typedThickness G` takes the maximum are precisely the elements and lengths of the concrete finite trimmed grammar. There is no need to redefine the paper's parameter or to assume this relationship.

## Main unconditional lower bound (for arbitrary finite presentations)

```lean
theorem intrinsic_typed_thickness_lower_bound_all (n : Nat)
    {NT : Type} [Fintype NT] [DecidableEq NT]
    (G : SSBNFGrammar NT)
    (hLang : GrammarLanguage G = TCSPhase2.Language n) :
    3 * 2 ^ n - 2 ≤ typedThickness G
```

The source also provides the manuscript's (n≥1) variant `intrinsic_typed_thickness_lower_bound`; both hold **without a reducedness hypothesis**, and neither imposes restrictions on rule or nonterminal count. The witness `witness n` belongs to the actual language, the nonempty start derivation passes through a start child `A`, its type is `U1.one`, hence `(A,U1.one)` is retained. The original Phase 2 theorem `unique_type_one` implies that this typed child has **only** `witness n` as a yield. The shortest-yield length is `3*2^n-2`; the finite retained-symbol maximum is at least that large.

The original Phase 1–3C proof files and theorem statements are unchanged. The pre-existing characteristic-data bound `grammar_characteristic_exponential_lower_bound` is a separate, conditional, set-driven characteristic-sample statement and should **not** be interpreted as a Gold convergence-time or mind-change bound. The intrinsic typed-thickness statement does **not** assume any characteristic-sample existence.

## Files and their scope

| File | Formalized contents |
| --- | --- |
| [TCSPhase4SSBNF.lean](TCSPhase4SSBNF.lean) | Arbitrary finite SSBNF productions and derivation trees |
| [TCSPhase4TypedLifting.lean](TCSPhase4TypedLifting.lean) | Independent typed inductive derivations and lifting |
| [TCSPhase4Trimming.lean](TCSPhase4Trimming.lean) | Tree occurrence, retained nodes, semantic trimmed derivations |
| [TCSPhase4TrimmingLanguage.lean](TCSPhase4TrimmingLanguage.lean) | Preservation of the start language |
| [TCSPhase4Thickness.lean](TCSPhase4Thickness.lean) | Shortest terminal yields, minimality, finite max |
| [TCSPhase4IntrinsicGap.lean](TCSPhase4IntrinsicGap.lean) | Corollary 6.4 for every finite SSBNF presentation |
| [TCSPhase4FiniteRefinement.lean](TCSPhase4FiniteRefinement.lean) | Explicit finite typed rules, derivational correspondence |
| [TCSPhase4OperationalTrim.lean](TCSPhase4OperationalTrim.lean) | Independent productive reachability and equivalence |
| [TCSPhase4Main.lean](TCSPhase4Main.lean) | One aggregate import and direct axiom audit |

## Local reproduction

```bash
cd formalization/TCS-01-Phase1
lake update
lake exe cache get
lean --version
lake --version
lake build
for m in TCSPhase1 TCSPhase2 TCSPhase2Bridge \
  TCSPhase3Parser TCSPhase3Recognition TCSPhase3Congruence \
  TCSPhase3Prefix TCSPhase3Main TCSPhase3Suffix \
  TCSPhase3RecognitionConverse TCSPhase3Marker \
  TCSPhase3RecognitionFull TCSPhase3Subtree TCSPhase3BMain \
  TCSPhase3CAux TCSPhase3CSynchronization \
  TCSPhase3CPathCongruence TCSPhase3CClarkEyraud \
  TCSPhase3CMain TCSPhase4SSBNF TCSPhase4TypedLifting \
  TCSPhase4Trimming TCSPhase4Thickness TCSPhase4IntrinsicGap \
  TCSPhase4TrimmingLanguage TCSPhase4Main \
  TCSPhase4FiniteRefinement TCSPhase4OperationalTrim; do
  lake env lean "$m.lean"
done
```

The GitHub Actions workflow does exactly this 28-module build/direct compile and checks forbidden proof tokens in every `TCSPhase*.lean`, plus `sorryAx` in the `#print axioms` output. No forbidden-token test was disabled.

## Deliberate formalization boundaries

No proof of general CFG-to-SSBNF normalization, an executable trimming algorithm's termination/runtime, generic learning reconstruction `Rec_h`, positive-data identification itself, any Gold learner's exact convergence stage, or the **entire** TCS manuscript is claimed. All statements above are proved only for finite SSBNF presentations over the literal five bracketed terminals and the paper's fixed two-element monoid `U1`. This covers Corollary 6.4's original universal quantification over its fixed alphabet and `hU`.

No revisions to manuscripts, `PAPER.yaml`, Japanese version, response letters, PDFs, arXiv, submission sites or the main branch were made.

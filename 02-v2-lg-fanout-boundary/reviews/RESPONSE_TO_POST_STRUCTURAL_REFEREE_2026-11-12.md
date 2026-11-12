# Paper #2 — Response to 2026-11-12 independent mathematical review (post-PR #107)

**Manuscript base:** commit `96c32d9b388e3d33bfc664d5bf3d7c44cfac1ca1` (43 EN / 50 JP pages); review dated 2026-11-12.
**Review verdict:** simulated **Minor Revision**, 0 Critical, 0 Major, 5 Minor, 6 Editorial.
**Status of verification:** An AI referee's mathematical assessment, **not a journal decision, peer-review certificate, or independent human proof validation**. Source-literature cross-checking and full visual PDF proofreading remain outside the review's verified scope.

## Author-side editorial decisions

| Referee item | Action in this revision | Reason |
| --- | --- | --- |
| m1: inconsistent parameter dependence after Theorem A strengthening | **Corrected**, EN/JP introduction, separated-language remark, fan-out-one theorem (ii), and scope table | The *learning class* still specifies `Sigma` and `s`, while the **coefficient** is uniform across those data for fixed `f, r_max, |S|`. The formal definition of uniform polynomial data is unchanged. |
| m2: no explanation of `n_{hat{s}}(G) <= |V||S|^f` | **Corrected**, EN/JP new short-type corollary | Every component of every nonterminal yield is nonempty in a good epsilon-free grammar; its type belongs to the positive image `S`, not merely `S^sharp`. |
| m3: vague transition from short derivations to typed thickness | **Corrected**, EN/JP new short-type corollary | Explicitly cite `prop:output-invariants` and `lem:witness-length-template(i)` with `lambda=hat{s}` to obtain representatives of all typed nonterminals. |
| m4: proposed extraction of an independent heavy-antichain replacement lemma | **Resolved by explicit self-contained statement in the corollary's proof**, but **not** extracted as an additional numbered lemma | The existing `lem:local-group-shortest` already proves the construction. The updated proof restates the unconditional shortening claim with threshold, universal quantifiers, exact bound, preservation and strict-shortening conclusion, then cites its ingredients; this avoids duplicating an extended argument and changing the lemma dependency graph. |
| m5: pseudovariety-level scope of "no intermediate growth" | **Corrected** in English introduction; already explicit in Japanese | Does not claim classification of every individual typing or fan-out-two boundary. |
| e1: `m_0` vs `h_0` typo in order homogenization | **Corrected** in EN (`h_0`), already correct in JP | Pure notation. |
| e2: notation `hat{s} preceq lambda` | **Clarified** in EN/JP | Gives the full-monoid kernel meaning when lambda separates epsilon. |
| e3: pointer to group-constant bound | **Corrected** in EN/JP | Points to the following explicit formula, rather than an earlier unrelated paragraph. |
| e4: optionally replace `|S^sharp|` by `|S|` in the canonical-grammar count | **Deferred** | Not required for correctness; would change several other constants and deserves a separate audit. |
| e5: JP-only labels with legacy `lem:` prefix on remarks | **Kept** | Renaming risks needless historical-reference / label-port churn. |
| e6: stale `42-/50-page` text in handoff | **Corrected** | The latest published baseline is 43 EN / 50 JP pages. |

## Mathematical invariants protected

- Statements of Theorems A, B and C unchanged. In particular Theorem A still has an `O_{f,r_max,|S|}(||G||^2 theta_bar)` coefficient.
- Original stronger fine-type shortening lemma `lem:local-group-shortest` **not edited**.
- New type-level shortening corollary `cor:lg-type-level-shortest` still uses an `hat{s}`-minimal derivation for the path count and finer `lambda_{k,nu}`-preserving replacements for antichain shortening.
- All theorem/lemma/proposition/definition labels retained; none added or removed. Existing parked research and unresolved fan-out-two boundary untouched.
- English/Japanese source kept synchronized around every modification.

## Checks and limitations

Pre-PR mechanical audit: zero missing bibliography keys, zero missing internal references, zero duplicate labels, and no added or removed labels in either language. Proof environment counts preserved (EN 59, JP 60). Independently verify CI page counts, both TeX compilers, and the strict historical-label port check before merge. Compilation establishes source integrity, not mathematical soundness.

This response covers editorial refinements arising from the *post-structural independent mathematical review*; it is distinct from the earlier referee report and reply stored in `reviews/claude_independent_referee_2026-11-12.md` and `reviews/RESPONSE_TO_CLAUDE_REFEREE_2026-11-12.md`.

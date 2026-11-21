# Response to Fable Round 2 — 2026-11-17

**Source**: user-supplied `paper02_planA_fable_round2_independent_referee_2026-11-16.zip` (reviewer report, issues register, proposed patches and checks).
**Reviewed revision**: `592b72cee9cb2cc5d5e7c7c57d6a3a562af8acdb`, PR #138.
**Referee result**: Minor Revision (0 CRITICAL, 0 MAJOR, 9 MINOR, 5 EDITORIAL).
**Revision location**: the working branch for PR #138; this log is not a substitute for validating the current GitHub Actions build.

## Individual dispositions

| Finding | Disposition |
| --- | --- |
| P2-01, LG beyond LI ∨ Grp | Added explicit ten-element sliding-factor positive typing on {a,b}; proved LG by the sliding-factor characterization and failure of the identity `x^ω y^ω x^ω=x^ω` using idempotents represented by aa, bb and aabbaa. No claim of target-language class strictness. |
| P2-02, strict-inclusion citation | Kept Costa–Nogueira–Teixeira (2021) as contextual support and supplied a short self-contained identity argument and concrete counterexample. The article's discussion of LG versus the join of LI and finite groups is available in published/scanned text. |
| P2-03, fan-out-one comparison | Distinguished arbitrary reduced CFG presentations and the companion thickness-controlled normal form from this paper's reduced good presentations; expressly avoids implication across presentations. |
| P2-04, balance argument | Cited the author's earlier arXiv:2605.11644v3 Proposition 3.1 as a comparable balance argument; added an arity-one witness that L_x is outside trivial-typing substitutability. |
| P2-05, Yoshinaka 2011 pinpoints | Removed the unverified sharp Lemma 7/Theorem 1 numerical claim and uncertain §4.3 / after-Example-2 page locators rather than claiming to have independently verified those exact locators. General attribution retained. |
| P2-06, Yoshinaka 2015 | Updated discussion from "does not itself provide" to the more precise bibliographic statement "does not state"; Theorem 1 and Lemmas 2–3 in MoL 2015 explicitly give qualitative reconstruction and a cardinality bound on D*. |
| P2-07, Japanese exponential t_typ claim | Deleted the unsupported sentence; both texts now give only the untyped baseline and cite Yoshinaka generally. |
| P2-08, English/Japanese equivalence | **Preserved** the mathematically useful JA-only typed-rule-thickness remark and normalization copies table by adding corresponding English versions. Now all labels occur in both texts. |
| P2-09, undefined B | Replaced by "the root nonterminal of T" in English and Japanese. |
| P2-10, undefined S and asymptotic subscript | Explicitly defined s:Σ+→S and S=s(Σ+) within the theorem; added f,r_max,|S| dependence to cardinality big-O. |
| P2-11, stale Appendix A dependency | Updated pointer to `lem:lg-unconditional-shortening` in English and Japanese. |
| P2-12, companion bibliographic verification | Retained arXiv:1409.6247v5; independent public metadata gives 2026-10-22 v5 and exact "Fixed Finite-Semigroup Typing" title. |
| P2-13, large constant | Disclosed the doubly-exponential fan-out dependence of the explicit upper-bound coefficient in both abstracts (while retaining fixed-fan-out polynomial data guarantee). |
| P2-14, L_x proof readability | Expanded the common-context boundary/adjacent-pair and additive-balance argument in both languages. |

## Mathematical and editorial boundaries

- Main Theorem A, its `O(‖G‖² θ̄_G)` length bound, the noncommutative block interface and the new unconditional shortening lemma remain the mathematical core. No parked Theorem B/C or lower bound was restored.
- The newly added ten-element typing distinguishes **semigroup typing regimes**, not automatically the classes of target languages covered by every possible competing typing.
- The independent finite checks reported by the referee are corroborating examples, not proofs of the full theorem.
- Unlike unverified locators in the prior manuscript, the revised source does not present uncertain pinpoint claims as facts.
- Both EN/JA source references and bibliography keys were checked for consistency; all theorem labels now match. Rebuild and revalidate the PR's final head before merging.
- **No journal submission is authorized by a merge.** Publication is a separate decision.

## Confirmed public sources

- Yoshinaka (2015), MoL 2015: https://aclanthology.org/W15-2308/ , see Theorem 1, Lemmas 2–3 and the bound |D*| ≤ |P*|+|N*|.
- Yoshinaka (2011), TCS 412(19):1821–1831: https://doi.org/10.1016/j.tcs.2010.12.058 . The exact old page/lemma locators were dropped unless confirmed.
- Costa, Nogueira and Teixeira (2021), Semigroup Forum 103:439–468: https://doi.org/10.1007/s00233-021-10207-9 . The article notes that LG is not the join of LI and finite groups.
- Kuriyama companion v5: https://arxiv.org/abs/1409.6247v5 (updated 2026-10-22).

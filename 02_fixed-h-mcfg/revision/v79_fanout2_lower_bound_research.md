# #2 MCFG v79 research memo: fan-out-two characteristic-data lower bounds

Date: 2026-10-18 (JST). Branch: `mcfg2-v79-fanout2-lower-bound-search`.
Base audited: `PAPER.yaml` internal version **v78** at repository HEAD
`2f2754deedc17e539e8ecbec9f923f40fae3fbea` (2026-10-18 02:30 UTC, "Publish
latest MCFG #2 English and Japanese PDFs"); `PAPER.yaml` still records v78,
so no newer manuscript version exists. The user-cited v78 commit
`1525e0ca…` is an ancestor that is not present in the shallow clone; the
audited `main.tex` is the HEAD copy.

**Status of this memo.** Nothing here is merged into `main.tex` or
`main_JP.tex`. `revision/v79_fanout2_results.tex` (+PDF) contains the
proofs written for independent audit. **Open Problem `op:fanout-two`
remains open.**

| Item | Content | Status |
|---|---|---|
| A | Type deletion stays in the class; rare types force long data (all f, also operator-independent form) | proved (short; uses v78 soundness + intersection) |
| B | Power-transfer lemma at fan-out two | proved |
| B′ | Local shift pairs in every word of length ≥ R_c(5) | proved (Ramsey) |
| C | Bracketed doubling family ∉ C(2,h) for **every** finite typing h, n ≥ 2\|M\|+3 | proved; strengthens v78 Prop. `prop:fixed-window-doubling-fanout-two` |
| R | Relaxed witnesses: data length of B^{≤r} is poly(‖G‖, θ_G, κ_G), κ_G = shortest members of typed distribution classes | proved (re-uses v78 completeness verbatim) |
| D | Abelian-filtered targets h⁻¹(Acc)∩φ⁻¹(γ+H) have polynomial characteristic data for **every** h, f, r | proved (Parikh + Papadimitriou small IP solutions) |
| E | Conjecture: κ_G ≤ poly(‖G‖θ_G) at fan-out two for all h (would give a *negative* answer to op:fanout-two) | open; supported by all experiments |
| Experiments | 6 hand-designed families + 28,642 enumerated doubling schemas | all fail (2,h)-substitutability; logs in `revision/` |

---

## 1. Phase 1 audit

### 1.1 Sources actually opened
- `02_fixed-h-mcfg/PAPER.yaml`, `main.tex` (Preliminaries, Sections 3–4,
  comparison section, Conclusion incl. `op:fanout-two` and
  `prop:fixed-window-doubling-fanout-two`), `appendix_local_group.tex`
  (statements, `lem:local-group-shortest`), `revision/v76_stage1_lg_dichotomy.md`,
  `revision/v78_fanout2_window1_negative_finding.md`,
  `revision/check_fixed_window_general_obstruction.py`.
- `01_fixed-h-cfg/main.tex`: Proposition `prop:typed-thickness-gap`
  (statement and proof of (i)–(iv), the construction of L_n and L_n^-) and
  Corollary `cor:typed-gap-intrinsic`.
- Papadimitriou (1981) small-solution bound: confirmed through its
  restatement in Fomin–Panolan–Ramanujan–Saurabh, *On the optimality of
  pseudo-polynomial algorithms for integer programming* (arXiv:1607.05342,
  Sec. 1). The original J. ACM paper was **not** opened.

### 1.2 Not opened (do not treat as checked)
- `japanese/main_JP.tex` was not re-read line by line (only its sha in
  `PAPER.yaml`); nothing in it is changed.
- The ChatGPT-side source volumes 02/03/07 are not in this Claude project
  (the project holds Core B/F/L/N excerpts). Yoshinaka (2011, 2015),
  Clark–Yoshinaka, Seki et al. (1991) and Almeida et al. (2009) were used
  **only through the statements quoted in main.tex**; I did not open the
  originals. The facts used from them are standard (closure of MCFLs under
  intersection with regular sets; good-form conventions).
- TCS #1 Appendix proof of bracketed substitutability was not re-audited
  (it is not needed: every result here concerns arity two).

### 1.3 Exact reformulation
Fix f≥2, r≥2, finite h:Σ*→M. Wanted: reduced good G_n (fan-out ≤ f,
rank ≤ r) with L(G_n) ∈ C^mcf_{f,h}, ‖G_n‖·max{1,θ_{G_n}} = poly(n), and
every characteristic sample of B^{≤r}_{f,h} superpolynomial. Derived
requirements (this memo):
1. **Sufficient**: a *rare type* m_n with μ_{m_n}(L(G_n)) superpolynomial
   (Prop. A). Then the bound also holds for every set-driven operator
   having characteristic samples for L and L∖h⁻¹(m).
2. **Necessary**: a typed distribution class [X] of G_n all of whose
   members are superpolynomially long, κ_{G_n} = n^{ω(1)} (Cor. R).
3. **Forbidden shapes**: (i) any long power u^K in any word forces
   quantum transfers between u-blocks (Lemma B); (ii) every word longer
   than R_c(5) carries a bounded interchangeable shift pair (Lemma B′);
   (iii) abelian-filtered targets are impossible (Thm D).

---

## 2. Proved results (proofs in `v79_fanout2_results.tex`)

### A. Type deletion and distinguishing pairs (any f)
For L ∈ C(f,h) and m ∈ h(L): L∖h⁻¹(m) ∈ C(f,h). Hence if K ⊆ L omits
type m then L(B^{≤r}_{f,h}(K)) ⊆ L∖h⁻¹(m) ⊊ L (same for uncapped B),
so every characteristic sample has ‖F‖₊ ≥ μ_m(L)+1; and every set-driven
operator with a characteristic sample for L∖h⁻¹(m) needs a type-m word in
every characteristic sample of L. This is the exact fan-out-f form of
TCS #1 Prop. `prop:typed-thickness-gap`(iii)–(iv); it shows that the TCS
mechanism transfers to every f **as soon as a member of C(f,h) with a
superpolynomially rare type exists**. The open problem is therefore purely
a question about class membership.

### B. Power transfer (fan-out two)
L ∈ C(2,h), u ∈ Σ⁺, h(u)^i = h(u)^{i+π} for i ≥ i₀ ≥ 1, s,r ≥ i₀,
π | d > 0. If some word of L contains u^{s+d+r+2} then for all X,Z and
Y ≠ ε:  X u^s Y u^{d+r} Z ∈ L ⇔ X u^{s+d} Y u^r Z ∈ L.
Witness: x=(u^s,u^{d+r}), y=(u^{s+d},u^r), E=(Pu)□u□Q.

### B′. Local shift pairs (fan-out two)
With c = |M|²|Σ| and R = R_c(5): every w with |w| ≥ R factors as
P x₁ p q p y₂ Q (|p|=1) with h(x₁)=h(x₁pq), h(qpy₂)=h(y₂). If w ∈ L ∈ C(2,h)
then (x₁,qpy₂) ≡ (x₁pq,y₂): the block pq may be moved between any
occurrence of x₁ and any later occurrence of y₂ across arbitrary nonempty
material, in every word of L. Fan-out one has no analogue.

### C. No finite typing rescues the doubling family
For every finite h:Γ*→M and n ≥ 2i₀+π+2 (i₀,π the index/period of h(⌊)),
in particular n ≥ 2|M|+3: L_n ∉ C(2,h). Proof: apply B with u=⌊ inside
the leading run ⌊ⁿ of W_n; move ⌊^π from the run that opens the second
copy of W_{n−1} to the leading run. The result is ceiling-free and ≠ W_n.
This subsumes v78's window and window×h_U cases (with a cruder threshold).
Formula check: `revision/v79_check_all_typing_obstruction.py`
(3000 random DFA typings, ≤5 states, 3 offsets each: PASS).

### R. Relaxed witnesses
In v78's witness set, the canonical tuple ω(X) ∈ L_X may be replaced by
**any** ω′(X) ≡_{L,h} L_X, and χ(X) by any derivational context of the
*untyped* A. The completeness proof uses nothing else. Hence
‖K*‖₊ ≤ (|V||M|^f+|P||M|^{fr})(1+θ_G+‖G‖+(r+1)κ_G), where
κ_G = max_X min{‖v‖ : v ∈ [X]}.
Consequences:
- a positive answer to op:fanout-two **requires** superpolynomial κ;
- v78's exponential full-refinement thickness (`prop:typed-thickness-exponential`,
  L={a,c}⁺) is an artefact of insisting on ω(X) ∈ L_X: there [X] contains
  the one-letter tuple `a`.

### D. Abelian-filtered targets have polynomial data (every h, f, r)
For L = h⁻¹(Acc) ∩ φ⁻¹(γ+H), φ into **any** abelian group, with reduced
good presentation G (fan-out ≤ f, rank ≤ r):
|K*| ≤ |V||M|^f+|P||M|^{fr} and ‖K*‖₊ ≤ C(‖G‖·max{1,θ_G})^e with C,e
depending only on Σ,h,f,r (e = O(|Σ|)). Proof idea: nonterminal Parikh
values are constant modulo Λ = φ̄⁻¹(H) (nondeletion); shortest yields and
rule defects generate a lattice Λ_T by vectors of ℓ₁-norm
T=(r+1)t_G+‖G‖; every yield is congruent to the shortest one modulo Λ_T;
Parikh's theorem for h⁻¹(t_i) and Papadimitriou's bound give a tuple of
the prescribed type and congruence class of size poly(T); type + value
mod Λ determine the distribution class; apply R.
This holds also for typings outside **LG** (e.g. h_U) and at fan-out one;
it explains why every member of C(f,h) built by abelian filtering
(MIX₂⁺, L_intr, …) is useless for op:fanout-two.

---

## 3. Candidate constructions and their failures (Phase 2–3)

All checks are **exact for the finite languages tested** (`v79_lib.py`
enumerates every arity-1/2 occurrence, every context, compares
distributions; violations are re-verified independently). A pass at small
n is never treated as a theorem.

| # | Construction principle | Rare (U-type-free) word | First failure (h_U / win(1,1)×h_U) | Root cause |
|---|---|---|---|---|
| P1 | rigid bracket doubling (TCS #1) | W_n, 3·2ⁿ−2 | n=2 arity 2 / n=3 arity 2 | power ⌊ⁿ → Thm C |
| P2 | unary rare word aⁿ + level counter `c dⁱ` | a^{2ⁿ} | n=2 arity 1 / n=3 arity 1 | shortcut ambiguity; d-runs (Lemma B) |
| P3 | free rare part {a,b}^{2ⁿ} + ceiling shortcuts | all of {a,b}^{2ⁿ} | n=2 arity 1 / n=3 arity 1 | dyadic alignment vs. transfer |
| P4 | fan-out-2 split: (leaf letters, single a-run) | c^{2ⁿ} m a^{2ⁿ} | n=2 arity 1 / n=2 arity 1 | λ-freeness forces a second long run (leaf letters) |
| P5 | synchronised fan-out-2 brackets, two bracket alphabets | 2^{n+2}−1 | n=2 arity 2 / n=3 arity 2 | cross-component shift pairs (B′) |
| P6 | Thue–Morse rare word (overlap-free, no high powers) | Tₙ#T̄ₙ | n=2 arity 2 / n=3 arity 1 | shift pair (b,ac)~(ba,c); wrap ambiguity |
| S1 | enumerated fan-out-1 doubling schemas (322) | Θ(2ⁿ) | all fail by n≤3 | — |
| S2 | enumerated fan-out-2 doubling schemas (28,320) | Θ(2ⁿ) | all fail by n≤3 under both typings | — |

Explicit minimal violations are in `revision/v79_candidate_families_output.txt`.
Example (P5, n=2, h_U): x=(`[`,`]`), y=(`([a`,`b])`) share
`□(aa#bb)□`, but `□[a#b□]` accepts x only.
Example (P6, n=2, h_U): x=(`b`,`ac`), y=(`ba`,`c`) share
`abcb#□a□`, but `ca□#b□` accepts x only — exactly a B′ shift pair
(x₁=b, p=a, q=ε).

Schema space (`v79_schema_search.py`): X₀ constant over {a,b}; X_i →
τ(X_{i−1},X_{i−1}) with every good rank-2 template of fan-out d∈{1,2}
plus ≤1 inserted letter from {a,b}; X_i → σ(X_{i−1}) or constant with ≤2
inserted letters including the marker c; d=2 root S→(x¹ t x²), t∈{a,b}.
Every grammar is reduced, good, |G|=O(n), θ=O(n), and its unique c-free
word has length Θ(2ⁿ). **No schema survives to n=3** under h_U or under
win(1,1)×h_U. This is a finite search; it rules out only this schema
space.

### Why the three "escape routes" close
1. *Rigid (tree-like) rare words* contain either long powers (Lemma B) or,
   when overlap-free, constant-size shift pairs (B′) that transport blocks
   between unrelated occurrences; rigidity is then violated (P1, P5, P6).
2. *Commutative rare words* (unary or free) need the transported quanta to
   be harmless, i.e. membership must depend only on counts. Exponential
   compression then needs short "shortcut" encodings whose values are
   consistent with all 1- and 2-dimensional substitutions; for exact
   abelian filters Theorem D shows this is impossible, and in the
   non-abelian prototypes P2–P3 the value encoding breaks
   substitutability already at arity one.
3. *Single-run designs* (all long material in one block, so transfers are
   trivial) collide with λ-freeness of good grammars: every leaf of the
   pure derivation contributes a letter to **each** component, so a second
   long region appears (P4).

---

## 4. New insights (Phase 5 D)
- **Local mobility** is the fan-out-two phenomenon: by B′ every word
  longer than a constant depending only on (Σ,h) contains an
  interchangeable pair of bounded size, and the pair's components can be
  re-placed anywhere in the language. Fan-out-one substitutability has no
  such consequence, which is why the TCS #1 rigid family works there.
- The real quantity behind the data length of B^{≤r} is **κ_G**, the
  shortest member of the typed distribution classes (R), not the typed
  thickness of the full refinement. Lower bounds need long classes; rare
  types are long classes at start-linked typed symbols.
- Abelian invariants cannot create long classes (D), independently of the
  typing's position relative to **LG**. Hence the semilattice obstruction
  of v76 is necessary but far from sufficient at fan-out ≥2.
- Conjectural picture (E): local mobility + finite typing force class
  membership to be determined by type and an "additive" invariant at large
  scale, which would make κ_G polynomial; this would make the answer to
  `op:fanout-two` **negative** for B^{≤r}_{2,h}.

## 5. Precisely formulated next steps (Phase 5 F)
1. **Conjecture E (κ-boundedness).** For fixed Σ,h,r there is a polynomial
   p with κ_G ≤ p(‖G‖·max{1,θ_G}) for every reduced good G of fan-out ≤ 2,
   rank ≤ r and L(G) ∈ C(2,h). (Implies a negative answer; false at f=1.)
2. **Lemma F1 (branched abelian targets).** Extend Theorem D to finite
   unions L = ⋃_j h⁻¹(Acc_j) ∩ φ_j⁻¹(γ_j+H_j) with pairwise disjoint Acc_j
   (covers v78's L_⋆). Expected proof: Steps 1–5 per branch, with the
   branch of a context-filled tuple determined by component types.
3. **Lemma F2 (schemas).** For every fixed good doubling schema
   (β, τ, σ) of fan-out ≤ 2 and every finite h, L_n ∉ C(2,h) for all large
   n. Route: show that the pure yield contains u^{K(h)} for some u (then
   Lemma B), or, for Thue–Morse-type schemas, exhibit a B′ pair whose
   transport across a shortcut leaves L_n.
4. **Lemma F3 (power normal form).** If L ∈ C(2,h) and some word contains
   u^{2|M|+3}, then for every word of L the vector of lengths of its
   maximal u-blocks of length ≥ i₀ matters only through its sum modulo the
   transfers of Lemma B; derive that the classes [X] containing long
   u-blocks contain representatives whose u-blocks are all < i₀+π except
   one.
5. **Question G (positive direction).** Find L ∈ C(2,h) with a single
   typed class whose members are all superpolynomially long, ignoring
   grammar size. If even this is impossible for fixed h, Conjecture E is
   true in a strong, presentation-free form.

## 6. Reproducibility
```
python3 revision/v79_check_all_typing_obstruction.py       # Thm C formula check
python3 revision/v79_candidate_families.py 3                # P1–P6 (output: v79_candidate_families_output.txt)
python3 revision/v79_schema_search.py --d 1 [--window]      # S1
python3 revision/v79_schema_search.py --d 2 [--window]      # S2 (~10 min, 2 cores)
pdflatex revision/v79_fanout2_results.tex                   # proofs A,B,B′,C,R,D
```
Library: `revision/v79_lib.py` (finite MCFG evaluation, goodness and
thickness checks, exact (2,h)-substitutability test).

## 7. Impact on the canonical manuscript (not applied)
- Theorem C could replace or follow `prop:fixed-window-doubling-fanout-two`
  (universal over typings; v78's sharper threshold remains valid for
  windows).
- Lemma R + Theorem D would be a new subsection of Section 5; it also
  reinterprets `prop:typed-thickness-exponential` (full-refinement blow-up
  is not a data lower bound).
- `op:fanout-two` text could add the necessary condition κ_{G_n}=n^{ω(1)}.
All of this needs independent audit before adoption; English/Japanese
synchronisation would be required.

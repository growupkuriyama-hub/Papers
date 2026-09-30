# Literature Priority Audit v3

Date: 2026-09-30  
Scope: `07_Minimal_Observation_Is_Not_Enough/`  
Status: internal literature-priority audit completed; external expert priority check still recommended.

## 1. Question audited

The audit asks whether prior work already contains the specific theorem-level connection claimed in this manuscript:

1. optimize **finite-monoid observer image size** over the same class of safe observers used for substitution;
2. optimize, over those observers, a **learner-relative positive characteristic/locking-sample cost**;
3. prove that the two optima can have different optimizers, or that a fixed compression number can coexist with unbounded optimal reconstruction cost; and
4. connect minimum-codomain separating **relational morphisms** to reconstruction suboptimality of their functional selectors.

The audit is deliberately narrower than the broad slogan “model size and sample complexity are different.”

## 2. Search strategy

Project literature was searched first, especially the SCL/finite-algebra, substitutability/positive-data, and typing-bias anthologies. External searches then covered combinations of:

- characteristic sample / characteristic set / teaching dimension;
- representation size / state complexity / sample complexity;
- grammatical inference / positive-data learning;
- typing bias / domain bias / background knowledge;
- active automata learning / alphabet abstraction / abstraction refinement;
- symbolic automata / passive learning;
- incompletely specified FSM minimization / compatibility classes / closed covers;
- finite monoid / relational morphism / grammatical inference;
- Pareto / multiobjective / automata learning.

Particular attention was paid to work that could invalidate the manuscript's strongest scoped novelty statements, not merely to papers sharing vocabulary.

## 3. Closest prior lines of work

### 3.1 Characteristic samples and teaching complexity

Colin de la Higuera's 1997 paper, *Characteristic Sets for Polynomial Grammatical Inference*, Machine Learning 27(2):125--138, DOI 10.1023/A:1007353007695, is an important novelty boundary. It formalizes polynomial characteristic data for grammatical inference and emphasizes that learnability/data requirements depend on the chosen representation. In particular, the surrounding literature notes that DFA and NFA can behave differently under polynomial-time-and-data criteria despite recognizing the same regular language class.

Goldman and Kearns, *On the Complexity of Teaching*, JCSS 50(1):20--31 (1995), DOI 10.1006/jcss.1995.1003, introduced teaching dimension as a minimum-example complexity. Goldman and Mathias, *Teaching a Smarter Learner*, JCSS 52(2):255--267 (1996), DOI 10.1006/jcss.1996.0020, further developed learner-relative teaching.

**Overlap:** minimum examples are a distinct learning resource; representation/learner choice can materially change data complexity.

**Not found there:** optimization over a common feasible set of safe finite-monoid observers, exact observer-image/locking-data optimizer separation, or an SCL/relational-morphism formulation.

**Priority consequence:** the bridge paper must not claim to be the first work showing that compact representations and small teaching/characteristic samples are different notions.

### 3.2 Typing and background knowledge in automata inference

Coste, Fredouille, Kermorvant, and de la Higuera, *Introducing Domain and Typing Bias in Automata Inference*, ICGI 2004, LNCS 3264:115--126, DOI 10.1007/978-3-540-30195-0_11, gives a generic framework for domain and typing background knowledge in state-merging inference.

**Overlap:** finite typing/background information changes which merges are admissible and can change inference behavior.

**Not found there:** a minimum typing/observer-size invariant, a comparison with minimum positive characteristic-data cost, or exact Pareto/separation theorems of the present kind.

**Priority consequence:** “typing affects inference” is prior art and is not a novelty claim here.

### 3.3 Abstraction refinement in active automata learning

Howar, Steffen, and Merten, *Automata Learning with Automated Alphabet Abstraction Refinement*, VMCAI 2011, LNCS 6538:263--277, DOI 10.1007/978-3-642-18275-4_19, and Aarts et al., *Automata Learning through Counterexample Guided Abstraction Refinement*, FM 2012, LNCS 7436:10--27, DOI 10.1007/978-3-642-32759-9_4, refine abstractions during active automata learning.

A particularly close recent conceptual neighbor is Yoel Kim and Yunja Choi, *Active Learning of Symbolic Automata for Reactive Programs via Dynamic Symbolic Mapper*, Proc. ACM Softw. Eng. 3 (FSE 2026), DOI 10.1145/3808154. Their mapper is explicitly granularity-aware: it uses coarse predicates for teaching/exploration and refines them as needed for learning.

**Overlap:** abstraction/observation granularity is itself a learning resource, and different granularities can be useful at different stages.

**Not found there:** passive positive-only grammar reconstruction, finite-monoid factor/tuple observers, SCL safety compression, characteristic locking samples on a fixed positive-data reconstruction architecture, or the exact optimizer-separation theorem proved here.

**Priority consequence:** broad language such as “more information does not always make learning easier” is too general to claim as new. The new statement must stay tied to the fixed reconstruction architecture and its exact monotonicity/separation theorems.

### 3.4 Passive symbolic-automata learning

Habermehl and Loulergue, *Passive Learning of Symbolic Automata over Monotonic Algebras*, DLT 2026, LNCS 16578:238--251, DOI 10.1007/978-3-032-28404-4_18 (also arXiv:2606.06050), proves passive identification with polynomial-size characteristic samples for symbolic automata over monotonic algebras.

**Overlap:** passive learning, symbolic/finite observation structure, characteristic samples.

**Not found there:** joint optimization of abstraction size and characteristic-data cost over safe observers, or the SCL/relational-morphism connection.

### 3.5 Incompletely specified FSM minimization

Paull and Unger, *Minimizing the Number of States in Incompletely Specified Sequential Switching Functions*, IRE Trans. Electronic Computers EC-8(3):356--367 (1959), DOI 10.1109/TEC.1959.5222697, and Grasselli and Luccio, *A Method for Minimizing the Number of Internal States in Incompletely Specified Sequential Networks*, IEEE Trans. Electronic Computers EC-14(3):350--359 (1965), DOI 10.1109/PGEC.1965.264140, use compatibility classes and cover/closure constraints for state minimization.

**Overlap:** compatibility-based compression and nontrivial global constraints on valid mergers/covers.

**Not found there:** positive characteristic-data cost, learner-relative reconstruction, observer refinement monotonicity of locking samples, or relational-morphism selector separation.

### 3.6 SCL, substitutability, and multidimensional distributional learning

Clark's syntactic concept lattice and Clark--Eyraud/Yoshinaka/Clark--Yoshinaka distributional learning provide the semantic and learning foundations used by the project. They establish concept/residual structure, tuple-context substitution, and positive-data reconstruction under substitutability assumptions.

**Overlap:** this is foundational dependence, not merely related work.

**Not found in the audited sources:** the cross-optimization of minimum finite-monoid observation and minimum reconstruction evidence developed in the bridge manuscript.

## 4. Collision matrix

| Candidate claim | Closest prior line | Priority risk | Audit judgment |
| --- | --- | --- | --- |
| Characteristic/teaching data is a resource distinct from representation size | de la Higuera; Goldman--Kearns/Mathias | **High** | **Not novel in this broad form** |
| Typing/background information changes inference | Coste et al. 2004 | **High** | **Not novel in this broad form** |
| Coarse/fine abstraction can matter differently during learning | Howar et al.; Aarts et al.; Kim--Choi 2026 | **High** | **Not novel in this broad form** |
| Compatibility-based finite-state compression is nontrivial | Paull--Unger; Grasselli--Luccio | **High** | **Not novel in this broad form** |
| Exact optimization of observer image vs positive locking data on the same safe finite-monoid observer space | no direct predecessor found | **Low/medium** | **Scoped novelty appears defensible** |
| Exact disjoint optimizer theorem for (R_{m,q}) | no direct predecessor found | **Low** | **No direct precedence found in searched scope** |
| Fixed (operatorname{cmp}^{CW}_2=2) with unbounded optimal OFET reconstruction on (X_{2,r}) | teaching/sample-complexity literature is conceptually adjacent | **Low/medium** | **Explicit finite-monoid/SCL statement appears new** |
| Minimum-codomain separating relational morphism whose every selector is reconstruction-suboptimal | finite-semigroup relational-morphism theory + learning literature | **Low** | **No direct predecessor found** |
| Finite Pareto frontier by Dickson's lemma | generic wqo/Pareto fact | **High if sold alone** | **Routine general device; novelty is the instantiated exact geometry, not finiteness itself** |
| Weighted two-point phase transition on (R_{m,q}) | generic weighted multiobjective optimization | **Medium** | **Exact formula is a corollary of the new explicit frontier; do not oversell the generic method** |

## 5. Direct-precedence search result

Within the project corpus and the external literature searched on 2026-09-30, **no direct prior theorem was found** that does all of the following in one framework:

- fixes the same family of safe finite-monoid factor/tuple observers;
- minimizes observer image cardinality;
- independently minimizes learner-relative positive characteristic/locking data;
- proves exact optimizer separation or fixed-compression/unbounded-reconstruction; and
- relates the compression optimum via separating relational morphisms to reconstruction behavior of functional selectors.

This is a negative search result, not a proof of absolute priority. It should be stated as “to the best of our knowledge” and backed by the novelty boundary above.

## 6. Recommended novelty wording

Safe wording:

> Prior work separately studies characteristic/teaching data, typing and abstraction biases, compatibility-based state minimization, and distributional grammar learning. To the best of our knowledge, the exact optimization problem considered here---comparing minimum safe finite-monoid observation with minimum positive reconstruction cost over the same observer space---has not previously been isolated. Our contribution is the theorem-level connection: an exact optimizer separation on (R_{m,q}), fixed Clark--Wurm compression with unbounded optimal reconstruction on (X_{2,r}), and a relational-morphism selector consequence.

Avoid:

- “We are the first to show that more information can hurt learning.”
- “We are the first to separate model size from sample complexity.”
- “We introduce the first Pareto analysis in automata learning.”
- “Minimum representation and minimum data were previously assumed to coincide.”
- Any learner-independent interpretation of the characteristic-data results.

## 7. Strongest conceptual neighbor

The closest current conceptual neighbor found is Kim--Choi (FSE 2026), because it explicitly makes abstraction granularity stage-dependent and distinguishes coarse teaching abstraction from finer learning abstraction. It does **not** preempt the present results, but it should be cited because a reviewer searching for “granularity vs learning resources” is likely to notice it.

The strongest classical novelty boundary is de la Higuera (1997): it already makes representation dependence of characteristic-data efficiency explicit. This prevents broad priority claims but does not contain the observer-optimization problem of the present manuscript.

## 8. Priority status after audit

- Direct theorem-level precedence found: **no, in the searched scope**.
- Broad conceptual precedence found: **yes, substantial**.
- Scoped novelty claim for the (R_{m,q}), (X_{k,r}), and relational-selector results: **defensible**.
- Generic Pareto-finiteness claim as independent novelty: **not recommended**.
- External expert/human priority check before submission: **recommended**.
- Submission-ready solely on the basis of this internal audit: **no**.

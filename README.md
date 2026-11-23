# Papers

Public source repository for Takayuki Kuriyama's research papers.

## Latest TCS #1 revision — **v231 (2026-10-19)**

**[TCS-D-26-00494: current submission files and exact three-file ZIP](01_fixed-h-cfg/README.md)** — revised manuscript, marked PDF, and synchronized response. **Submitted to Editorial Manager on 2026-10-22; under review (sent to reviewers, 2026-10-25).** Historical experiments and older versions are not current.


## #2研究MCFG — `02-v4-fixed-s-mcfg/` (2026-11-21)

**[`02-v4-fixed-s-mcfg/`](02-v4-fixed-s-mcfg/README.md)** merges the former `02-v2-lg-fanout-boundary/` (now [`v2/`](02-v4-fixed-s-mcfg/v2/)) and `02_fixed-h-mcfg/` (v1, arXiv:2605.11644; now [`v1/`](02-v4-fixed-s-mcfg/v1/)). Its [`main.tex`](02-v4-fixed-s-mcfg/main.tex) is the **research compendium** that contains every result of the fixed-s MCFG line regardless of length ([PDF](02-v4-fixed-s-mcfg/main.pdf), English, 135 pp.). The fan-out-two boundary `op:fanout-two` remains **OPEN**; its research is paused ([stop-state](02-v4-fixed-s-mcfg/v2/RESEARCH_PAUSED_2026-11-16.md)). The submission-oriented paper #2 is now [`02-v3-cfg-typing-classification/`](02-v3-cfg-typing-classification/).

## Contents

- **[`01_fixed-h-cfg/`](01_fixed-h-cfg/)** — *Distributional Learning of Context-Free Languages under Fixed Finite-Semigroup Typing* (**TCS-D-26-00494, current R1 v231**; [submission ZIP](01_fixed-h-cfg/TCS-D-26-00494_R1_3files.zip))
- **[`02-v4-fixed-s-mcfg/`](02-v4-fixed-s-mcfg/)** — **#2研究MCFG** (research compendium, 2026-11-21): *Multiple Context-Free Languages under Fixed Finite-Semigroup Typing — all results of the v1 and v2 research lines*. [Compendium source](02-v4-fixed-s-mcfg/main.tex) · [PDF](02-v4-fixed-s-mcfg/main.pdf). Contains the frozen v2 (Plan A paper, [`v2/`](02-v4-fixed-s-mcfg/v2/), EN 30 / JA 33 pp.) and v1 ([`v1/`](02-v4-fixed-s-mcfg/v1/), arXiv:2605.11644).
- **[`02-v3-cfg-typing-classification/`](02-v3-cfg-typing-classification/)** — *Which Fixed Typings Give Polynomial Characteristic Data? A Classification for Substitutable Context-Free Languages* (**new paper #2, started 2026-11-20; skeleton**). Fan-out one only: pseudovariety boundary LG, typing-level classification onto U₁, shape of the bound. Derived from the frozen `02-v4-fixed-s-mcfg/v2/`; see its [OUTLINE.md](02-v3-cfg-typing-classification/OUTLINE.md).
- **[`02-v5-mcfg-regular-skeletons/`](02-v5-mcfg-regular-skeletons/)** — **#2骨格MCFG** (direction A, started 2026-11-23; first draft): *Which Regular Skeletons Give Polynomial Characteristic Data for Multiple Context-Free Languages?*. Target-side boundary at every fan-out: skeletons whose syntactic semigroup is in **L ECom** (= SL∗LG). [Source](02-v5-mcfg-regular-skeletons/main.tex) · [PDF](02-v5-mcfg-regular-skeletons/main.pdf) · [research ledger](02-v5-mcfg-regular-skeletons/research/README.md)
- `03_scl-compression/` — *Finite-Monoid Compression in Syntactic Concept Lattices: Arity Hierarchies and a Pseudovariety Trichotomy* (arXiv:2608.29639)
- `04_relative-factorization/` — *Relative Prime Factorization and Finite-State Presentations under Fixed Finite-Monoid Observation*
- `05_jalc-occurrence-descriptors/` — *Finite Occurrence Descriptors for Context-Free Grammar Presentations under Monoid Typing* (JALC manuscript)
- `06_ofet/` — *Observer--Fragmentation--Exposure Tradeoffs: From rectangular CFG exposure to ordered MCFG scheduling*
- `07_Minimal_Observation_Is_Not_Enough/` — *Minimal Observation Is Not Enough: Reconstruction Tradeoffs in Identification in the Limit* (focused journal-candidate; intended third paper after #1/#2)
- `08_pacn-fixed-h-distributional-learning/` — *PAC_n and Higher-Arity VC Geometry under Fixed Finite-Monoid Distributional Typing* (exploratory research note; typed-box VC theory plus PAC-model audit for the fixed-observer CFG/MCFG program)
- **[`09_typed-fcp-fkp/`](09_typed-fcp-fkp/)** — *Finite Observation Helps Contexts but Not Kernels in Distributional Learning of Context-Free Languages* (research draft, started 2026-11-23; 12 pp.). Typed finite context/kernel properties (Kanazawa–Yoshinaka 2017) under fixed finite-semigroup typing, positive data + membership queries: context–kernel duality under refinement, one primal learner for all fixed-typing substitutable CFLs, and a one-word-deletion kernel lower bound. [Source](09_typed-fcp-fkp/main.tex) · [PDF](09_typed-fcp-fkp/main.pdf) · [report (JA)](09_typed-fcp-fkp/research/REPORT_2026-11-24.md) · [ledger](09_typed-fcp-fkp/research/LEDGER.md)
- `doctoral-thesis/` — larger five-component dissertation plan for *Observation Is Not Enough — Finite Observation and Resource Tradeoffs in Identification in the Limit*; preserved as the maximal integration track
- `doctoral-thesis-minimal/` — **current minimal high-impact dissertation track** for *Identification in the Limit beyond Fixed Observation*; core = #1 + #2 + #7 MOINE; no thesis TeX yet

## Other papers

- `misc/primitive-dyck/` — *Additive Bases from Primitive Dyck Words: Regular Underapproximations, Motzkin Coding, and Digit Lifting* (IJFCS manuscript; under review; outside the doctoral-dissertation project)

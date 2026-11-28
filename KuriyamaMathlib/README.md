# KuriyamaMathlib

A research library for formal language theory and grammatical inference, independent of manuscript layout.
Scope: **01, 02 CFG, 02 MCFG, 09**. Bootstrap (2026-11-28); not a completed formalization.

## Build

```sh
cd KuriyamaMathlib
lake update
lake exe cache get
lake build
```

```lean
import KuriyamaMathlib
```

Lean and Mathlib release are aligned with the historical TCS1 artifact (v4.31.0-rc1).
TCS1 is a Git dependency pinned to a commit. Commit the resolved Lake manifest after the first successful build.
New code is provisional until the CI build and theorem-statement audit pass.

## Architecture

| Layer | Purpose |
|---|---|
| Core/Observation | words, contexts, observation fibres |
| Algebra/SemigroupTyping | finite semigroup observer with fresh empty-word value; extension multiplication pending |
| Distribution/Closure | polar operators, Galois connection, typed closure |
| Paper01 | pinned historical TCS1 import (237 direct imports in upstream facade) |
| MCFG/Basic | unmodified legacy MCFG foundation |
| Paper02CFG | observation-relative substitutability and refinement |
| Paper02MCFG | arity-indexed tuple observation and refinement |
| Paper09 | typed finite frame/kernel generation, not yet grammar-wide FCP/FKP |

Reusable results belong in shared modules. Paper modules are adapters, not duplicate definitions.

## Source and verification policy

- 01: [current manuscript](../01_fixed-h-cfg/); historical Lean dependency [ecc6209](https://github.com/growupkuriyama-hub/tcs1-lean-formalization/tree/ecc6209fa38ade5f987cab31ca2f3b8250a34a94), exact theorem-facing baseline v88 ([DOI](https://doi.org/10.5281/zenodo.23120560)). Do not infer verification of submitted v231.
- 02 CFG: [typing classification](../02-v3-cfg-typing-classification/).
- 02 MCFG: [compendium](../02-v4-fixed-s-mcfg/) and [regular skeletons](../02-v5-mcfg-regular-skeletons/). The legacy Basic file is copied verbatim from [e38a9b0](https://github.com/growupkuriyama-hub/lean_cfg_project/blob/e38a9b09fbba7933777d7a00d7de4a7d77c4a916/LeanCfgProject/MCFG/Basic.lean), retaining its original copyright header; it is not a proof of the compendium.
- 09: [typed FCP/FKP](../09_typed-fcp-fkp/).
- Manuscript snapshot for this initial scope: Papers commit fd3fe3ec18dfddd3478d13ea50b00caaee70fb07.

No sorry/admit or new axioms in library declarations. Audit axiom dependencies (including native decision procedures) and statement fidelity, not just successful compilation. Never encode open problems as axioms or mark finite experiments as proofs. Preserve all existing manuscripts and archived formalizations.

See [ROADMAP.md](ROADMAP.md) for the initial work ledger.

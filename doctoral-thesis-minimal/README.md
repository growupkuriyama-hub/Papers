# Minimal Doctoral Thesis Plan

## Fixed title

**Identification in the Limit beyond Fixed Observation**

## Purpose

This directory is the **minimal-dissertation track**.

The goal is to obtain the strongest coherent doctoral thesis with the least thesis-specific additional work.  The core is deliberately restricted to:

1. `01_fixed-h-cfg/`
2. `02_fixed-h-mcfg/`
3. one short dissertation-level synthesis on moving **beyond one fixed observer**.

The larger dissertation plan in `../doctoral-thesis/` remains preserved separately.  This minimal track does **not** require #3 SCL-Compression, OFET, or Observation Is Not Enough.

## Current policy

**No dissertation TeX tree yet.**

The source-of-truth for #1 and #2 remains each paper directory.  This directory stores only the minimal dissertation architecture, status, and the short additional theorem package.

A thesis `tex/` directory should be created only when:

- #1 has a stable post-review baseline;
- #2 has a stable submission baseline;
- the short "beyond fixed observation" synthesis has passed a proof/scope audit.

Until then, use:

- `THESIS_MASTER.md` — architecture and mathematical spine;
- `STATUS.yaml` — current maturity and TeX gate.

## Minimal mathematical spine

[
	ext{fixed finite observation for CFG}
;longrightarrow;
	ext{fixed finite observation for MCFG}
;longrightarrow;
	ext{bounded unknown observation}
;longrightarrow;
	ext{unbounded-observation impossibility}.
]

The intended final message is:

> A single observer need not be fixed in advance: a bounded finite observation budget can be compiled into one universal product observer.  But removing the observation bound altogether crosses a Gold-style nonlearnability boundary.

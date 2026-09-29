# Doctoral Thesis

## Fixed title

**Observation Is Not Enough — Finite Observation and Resource Tradeoffs in Identification in the Limit**

## Current phase

This directory is the planning and integration layer for the doctoral dissertation.

The dissertation is **not yet maintained as a monolithic TeX source**. The five core research components are still evolving independently, so the thesis is currently managed master-first:

1. `01_fixed-h-cfg/`
2. `02_fixed-h-mcfg/`
3. `03_scl-compression/`
4. `06_ofet/`
5. `07_observation-is-not-enough/`

The source-of-truth for each research component remains its own paper directory. This directory records only the dissertation-level architecture, dependencies, terminology, status, and integration decisions.

## TeX policy

Do **not** create a dissertation `main.tex` yet.

A TeX thesis tree should be created only after the component papers have reached a sufficiently stable theorem/proof baseline. Until then:

- paper manuscripts stay authoritative;
- dissertation-level wording is recorded in `THESIS_MASTER.md`;
- current maturity is tracked in `STATUS.yaml`;
- no paper text is copied into a thesis chapter merely for convenience.

When the TeX phase begins, the intended layout is approximately:

```
doctoral-thesis/
  README.md
  THESIS_MASTER.md
  STATUS.yaml
  tex/
    main.tex
    frontmatter/
    chapters/
      01_introduction/
      02_common_foundations/
      03_fixed_h_cfg/
      04_fixed_h_mcfg/
      05_scl_compression/
      06_ofet/
      07_observation_is_not_enough/
      08_conclusion/
    appendices/
    bibliography/
```

The `tex/` tree is intentionally absent for now.

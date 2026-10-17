# MCFG #2 v72 to v73: inline/display mathematical typesetting

Date: 2026-10-18
Scope: presentation-only revision of the English canonical manuscript and its included English appendix.

- Convert **66** of **112** unnumbered display equations in `main.tex` to inline math.
- Convert **2** of **4** displays in `appendix_window_abelian.tex`.
- Retain **46+2=48** displays for long definitions, multi-line arrays, significant grammar rules, and central derivations; previous total was 116.
- The mathematical content of every affected equation was checked for equality after whitespace normalization. No propositions, definitions, labels, cross-references, bibliography, or stated bounds are intentionally changed.
- LaTeX math delimiter changes are localized: `\\[ ... \\]` becomes `\\( ... \\)` with line whitespace normalized inside the math body.
- Japanese review translation is unchanged; align bilingual typography separately if desired.
- Building PDF and checking overfull warnings are required after this commit.

Original English baseline SHA256: `1ab76531c2320ac553fc0814bdee4fca90d76c2d3b9cdebbeaaf57d45b96f151`
New English manuscript SHA256: `19b8b697a0a4fdb703d99226f707804a10b377207876a91d120b1304e5cb6c87`
Original appendix SHA256: `a4a05cbc0c3d0b1076e2fbf59bf3d28c7d32f9000d7cbbe23f00ff039a7921b4`
New appendix SHA256: `4c30cb9316770b9ab9fa3e9cf099d09a9c7a50740e3e94097759dff245b3a312`

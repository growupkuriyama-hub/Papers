# TCS v239 — remove unnecessary reduced assumptions in qualitative Section 5

Date: 2026-10-20. Single canonical edit branch: `main`.

- Replace exactly five occurrences of 'reduced CFG' on the **original input CFG** in Section 5: the refinement setup, typed-lifting Proposition 5.1, witness completeness Theorem 5.2, exact reconstruction Theorem 5.3, and Gold identification Corollary 5.4.
- The critical `trim to the reduced grammar \\widetilde G` operation remains unchanged. It ensures all retained typed symbols are productive and reachable and therefore have canonical yields `omega(X)` and terminal reaching contexts `(u_X,v_X)`.
- The typed-fiber equality for a retained symbol also holds if the source CFG has unreachable or unproductive symbols: annotate any productive original derivation and graft it into a retained reachable typed occurrence; trimming removes only unsuccessful derivations.
- Replace 'It exists by reduction' with 'It exists because \\widetilde G was trimmed' to identify the exact grammar to which reduction applies.
- Section 6 and all later quantitative reduced BUNF assumptions remain unchanged; no altered theorem numbers, witnesses, algorithms, term interpretations or proof cases.
- Source `main.tex` and Clean TeX identical; SHA256 `5d6e66fa19180b1fd4d3f268101302b56c1a45f34394cead98eee221c59d238a`. Rebuild all English submission outputs, check 49 reviewer items and 77 marked PDF locations, and only then mark v239 verified. Editorial Manager not yet submitted; Japanese reference translation not synchronized.

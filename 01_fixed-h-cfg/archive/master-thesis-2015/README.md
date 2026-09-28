# 2015 Master's thesis — historical archive

This directory preserves the master's thesis that preceded the line of work now developed in `01_fixed-h-cfg`.

## Files

- `master-thesis-2015.pdf` — the authoritative historical thesis PDF, dated **2015-02-21** (25 pages).
- `master-thesis-source-later-edited.tex` — the TeX file supplied together with the PDF, preserved byte-for-byte as received in 2026.

## Important provenance note: the TeX is not the exact source revision of the PDF

The title, author, and much of the mathematical core correspond, but the two files are **not the same revision**.

Observed differences include:

- the PDF has no abstract, while the TeX contains a later abstract discussing capped-counter languages (CCLs), the one-bracket Dyck language, and a current open problem;
- the PDF contains 9 chapters, while the active TeX contains 10 chapters and a differently developed/ordered middle part;
- the TeX also contains a disabled (`\\if0 ... \\fi`) chapter on multiple context-free languages;
- the TeX has no fixed thesis date, so compiling it now prints the current date rather than 2015-02-21;
- the TeX references an external `refs.bib` file that was not supplied here.

Accordingly, the PDF should be treated as the authoritative 2015 thesis artifact; the TeX is retained as a historically related, later-edited source file rather than claimed as its exact build source.

## SHA-256 of the uploaded originals

- PDF: `9471c78cd445b8d213188ee25fd815a065177eeb1a637de36e60c9cded234166`
- TeX: `c6dfecc57d53a783e363f817ccf7f85bb8ba5b7f48f2342482d9d79a5ffcc8d7`

No normalization or rewriting was applied to either archived file.

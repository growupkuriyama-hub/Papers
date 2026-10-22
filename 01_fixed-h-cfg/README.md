# Paper 01 — TCS fixed-semigroup CFG

**Current English editing source:** `main.tex`
**Current Japanese editing source:** `japanese/main_JP.tex`
**Current English reading PDF:** `main.pdf`

## TCS submission history

- Initial TCS submission: `archive/tcs-round1-arxiv-v4/`
  - Original submission PDF: `TCS-D-26-00494_Initial_Submission.pdf`
  - Initial submission / arXiv v4 source: `main.tex`
- Round 1 revision, 2026-10-22: `archive/tcs-r1-2026-10-22/`
  - Clean TeX and Clean PDF
  - Additions-marked PDF
  - Response to Reviewers PDF
  - Exact three-file submission ZIP
  - Editorial Manager composite PDF (43 pages)
  - `SUBMISSION_RECORD.md`

The author reported R1 resubmission on 2026-10-22. The Editorial Manager composite is not independently a final submission receipt. The R1 archive is immutable.

## Editing and builds

- English manuscript: `main.tex`
- Japanese manuscript: `japanese/main_JP.tex`
- Reviewer response source: `response/response_round1.tex`
- Version and submission metadata: `PAPER.yaml`
- Historical reviews and working notes: `revision/` and `notes/`

The root-level R1 submission copies were removed after hash verification against the frozen R1 archive. Do not regenerate them in the root directory.

`publish-tcs1-clean-pdf.yml` maintains the live `main.pdf` and Japanese PDF. `publish-tcs1-revision-package.yml` is manual-only and uploads a build artifact without rewriting the repository. `refresh-stable-paper-pdfs.yml` is also manual-only.

For future R2 submissions, create a new frozen archive directory rather than overwriting the R1 records.

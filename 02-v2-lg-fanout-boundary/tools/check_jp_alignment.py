#!/usr/bin/env python3
"""Check structural and mathematical alignment between main.tex and japanese/main_JP.tex.

Usage (from 02-v2-lg-fanout-boundary/):
    python3 tools/check_jp_alignment.py [main.tex] [japanese/main_JP.tex] [main.aux main_JP.aux]

The optional .aux files (from compiled builds) enable check 8.

Python 3 standard library only.  Every check prints PASS (0 differences) or
FAIL with the differences.  The exit status is 0 iff every check passes.

Checks
  1. sequence of \\label{...} keys (in order)
  2. multisets of \\ref, \\eqref and \\cite keys (optional arguments ignored)
  3. sequence of environment names (every \\begin{...}, in order)
  4. counts of \\section, \\section*, \\subsection, \\subsection*, \\paragraph
  5. count of \\item
  6. sequence of math fragments: $...$, \\(...\\), \\[...\\] and the bodies of
     equation/align/gather/multline/eqnarray environments (starred or not),
     compared verbatim (whitespace runs normalised to one space).  Contents of
     \\text{...} are compared too; the script reports how many \\text{...}
     occurrences there are and that none was excluded.
  6b. shape of every tabular/tabularx: number of rows and cells per row.
  7. English residue in the Japanese prose: runs of >= 5 consecutive English
     words outside math, command names, command arguments that are keys or
     URLs (\\label, \\ref, \\eqref, \\cite, \\url, \\texttt, \\href) and the
     bibliography.  Reported with line numbers.
  8. (optional, needs the two .aux files) the printed number of every \\label
     (theorem, section, equation and table numbers) is identical.
"""
import re
import sys
from collections import Counter

DISPLAY_ENVS = ["equation", "align", "gather", "multline", "eqnarray",
                "flalign", "alignat"]


def strip_comments(text):
    """Remove TeX comments, keeping line structure (so line numbers survive)."""
    out = []
    for line in text.split("\n"):
        i = 0
        cut = None
        while i < len(line):
            c = line[i]
            if c == "\\":
                i += 2
                continue
            if c == "%":
                cut = i
                break
            i += 1
        out.append(line if cut is None else line[:cut])
    return "\n".join(out)


def body(text):
    """Text between \\begin{document} and \\end{document}."""
    a = text.find("\\begin{document}")
    b = text.rfind("\\end{document}")
    return text[a:b] if a >= 0 and b >= 0 else text


def labels(t):
    return re.findall(r"\\label\{([^}]*)\}", t)


def ref_multisets(t):
    refs = Counter(re.findall(r"\\ref\{([^}]*)\}", t))
    eqrefs = Counter(re.findall(r"\\eqref\{([^}]*)\}", t))
    cites = Counter()
    for m in re.finditer(r"\\cite(?:\[[^\]]*\])*\{([^}]*)\}", t):
        for k in m.group(1).split(","):
            cites[k.strip()] += 1
    return refs, eqrefs, cites


def env_sequence(t):
    return re.findall(r"\\begin\{([^}]*)\}", t)


def sectioning(t):
    c = Counter()
    for m in re.finditer(r"\\(section|subsection|subsubsection|paragraph)(\*?)\{", t):
        c["\\" + m.group(1) + m.group(2)] += 1
    return c


def items(t):
    return len(re.findall(r"\\item\b", t))


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


def math_fragments(t):
    """Return list of (line, fragment) in order of appearance; also the
    character spans covered, so that prose can be separated from math."""
    frags = []
    spans = []
    env_re = re.compile(r"\\begin\{(" + "|".join(DISPLAY_ENVS) + r")(\*?)\}")
    i = 0
    n = len(t)
    while i < n:
        c = t[i]
        if c == "\\":
            m = env_re.match(t, i)
            if m:
                name = m.group(1) + m.group(2)
                end = "\\end{" + name + "}"
                j = t.find(end, m.end())
                if j < 0:
                    j = n
                frags.append((t.count("\n", 0, i) + 1,
                              "[" + name + "]" + norm(t[m.end():j])))
                spans.append((i, j + len(end)))
                i = j + len(end)
                continue
            if t.startswith("\\(", i) or t.startswith("\\[", i):
                close = "\\)" if t[i + 1] == "(" else "\\]"
                j = t.find(close, i + 2)
                if j < 0:
                    j = n
                frags.append((t.count("\n", 0, i) + 1,
                              t[i:i + 2] + norm(t[i + 2:j])))
                spans.append((i, j + 2))
                i = j + 2
                continue
            i += 2
            continue
        if c == "$":
            j = i + 1
            while j < n:
                if t[j] == "\\":
                    j += 2
                    continue
                if t[j] == "$":
                    break
                j += 1
            frags.append((t.count("\n", 0, i) + 1, "$" + norm(t[i + 1:j])))
            spans.append((i, j + 1))
            i = j + 1
            continue
        i += 1
    return frags, spans


def table_shapes(t):
    """For every tabular/tabularx environment: the number of rows and the
    number of cells in each row (cells = unescaped '&' outside math + 1)."""
    shapes = []
    for m in re.finditer(r"\\begin\{(tabular\*?|tabularx)\}", t):
        name = m.group(1)
        end = t.find("\\end{" + name + "}", m.end())
        content = t[m.end():end]
        # skip the column specification arguments
        content = re.sub(r"^\s*(\{[^{}]*\}\s*)?\{(?:[^{}]|\{(?:[^{}]|\{[^{}]*\})*\})*\}", "", content, count=1)
        _, spans = math_fragments(content)
        chars = list(content)
        for a, b in spans:
            for k in range(a, min(b, len(chars))):
                chars[k] = " "
        body_ = "".join(chars).replace("\\hline", "")
        rows = [r for r in re.split(r"\\\\", body_) if r.strip()]
        cells = [len(re.findall(r"(?<!\\)&", r)) + 1 for r in rows]
        shapes.append(f"{name}: {len(rows)} rows, cells per row {cells}")
    return shapes


def text_count(frags):
    return sum(len(re.findall(r"\\text\{", f)) for _, f in frags)


KEY_ARG_CMDS = r"label|ref|eqref|cite|url|href|texttt|begin|end|includegraphics|bibitem|newblock|tikz"


def english_residue(t, spans, min_words=5):
    # blank out math, keeping newlines
    chars = list(t)
    for a, b in spans:
        for k in range(a, min(b, len(chars))):
            if chars[k] != "\n":
                chars[k] = " "
    s = "".join(chars)
    # drop the bibliography
    a = s.find("\\begin{thebibliography}")
    if a >= 0:
        b = s.find("\\end{thebibliography}", a)
        s = s[:a] + re.sub(r"[^\n]", " ", s[a:b]) + s[b:]
    # drop arguments of key-like commands (with optional args)
    def blank(m):
        return re.sub(r"[^\n]", " ", m.group(0))
    s = re.sub(r"\\(?:" + KEY_ARG_CMDS + r")\*?(?:\[[^\]]*\])*(?:\{[^}]*\})?", blank, s)
    # drop remaining command names
    s = re.sub(r"\\[A-Za-z@]+\*?", lambda m: " " * len(m.group(0)), s)
    hits = []
    word = r"[A-Za-z][A-Za-z'\-]*"
    pat = re.compile(word + r"(?:[ \t,;:.()~]+" + word + r"){%d,}" % (min_words - 1))
    for lineno, line in enumerate(s.split("\n"), 1):
        for m in pat.finditer(line):
            hits.append((lineno, m.group(0).strip()))
    return hits


def main():
    en_path = sys.argv[1] if len(sys.argv) > 1 else "main.tex"
    jp_path = sys.argv[2] if len(sys.argv) > 2 else "japanese/main_JP.tex"
    en_raw = open(en_path, encoding="utf-8").read()
    jp_raw = open(jp_path, encoding="utf-8").read()
    en = strip_comments(en_raw)
    jp = strip_comments(jp_raw)
    # keep line numbers relative to the whole file: blank out the preamble
    def body_keep_lines(t):
        a = t.find("\\begin{document}")
        return re.sub(r"[^\n]", " ", t[:a]) + t[a:]
    enb = body_keep_lines(en)
    jpb = body_keep_lines(jp)
    ok = True

    def report(name, diffs):
        nonlocal ok
        if diffs:
            ok = False
            print(f"[FAIL] {name}: {len(diffs)} difference(s)")
            for d in diffs[:60]:
                print("   ", d)
            if len(diffs) > 60:
                print(f"    ... ({len(diffs) - 60} more)")
        else:
            print(f"[PASS] {name}: 0 differences")

    def seq_diff(a, b):
        diffs = []
        for k in range(max(len(a), len(b))):
            x = a[k] if k < len(a) else "<missing>"
            y = b[k] if k < len(b) else "<missing>"
            if x != y:
                diffs.append(f"#{k + 1}: EN={x!r}  JP={y!r}")
        return diffs

    def ms_diff(a, b):
        diffs = []
        for k in sorted(set(a) | set(b)):
            if a[k] != b[k]:
                diffs.append(f"{k}: EN={a[k]} JP={b[k]}")
        return diffs

    la, lb = labels(enb), labels(jpb)
    print(f"1. labels: EN={len(la)} JP={len(lb)}")
    report("label sequence", seq_diff(la, lb))

    (ra, ea, ca), (rb, eb, cb) = ref_multisets(enb), ref_multisets(jpb)
    print(f"2. refs: EN \\ref={sum(ra.values())} \\eqref={sum(ea.values())} \\cite keys={sum(ca.values())}"
          f" | JP \\ref={sum(rb.values())} \\eqref={sum(eb.values())} \\cite keys={sum(cb.values())}")
    report("\\ref multiset", ms_diff(ra, rb))
    report("\\eqref multiset", ms_diff(ea, eb))
    report("\\cite multiset", ms_diff(ca, cb))

    va, vb = env_sequence(enb), env_sequence(jpb)
    print(f"3. environments: EN={len(va)} JP={len(vb)}")
    report("environment sequence", seq_diff(va, vb))

    sa, sb = sectioning(enb), sectioning(jpb)
    print("4. sectioning: EN=" + str(dict(sa)) + " JP=" + str(dict(sb)))
    report("sectioning counts", ms_diff(sa, sb))

    ia, ib = items(enb), items(jpb)
    print(f"5. \\item: EN={ia} JP={ib}")
    report("\\item count", [] if ia == ib else [f"EN={ia} JP={ib}"])

    fa, spa = math_fragments(enb)
    fb, spb = math_fragments(jpb)
    print(f"6. math fragments: EN={len(fa)} JP={len(fb)}; \\text{{...}} occurrences inside math:"
          f" EN={text_count(fa)} JP={text_count(fb)} (compared verbatim, 0 excluded)")
    diffs = []
    for k in range(max(len(fa), len(fb))):
        x = fa[k] if k < len(fa) else (None, "<missing>")
        y = fb[k] if k < len(fb) else (None, "<missing>")
        if x[1] != y[1]:
            diffs.append(f"#{k + 1}: EN line {x[0]}: {x[1]!r}\n        JP line {y[0]}: {y[1]!r}")
    report("math fragment sequence", diffs)

    ta, tb = table_shapes(enb), table_shapes(jpb)
    print(f"6b. tabular/tabularx environments: EN={len(ta)} JP={len(tb)} (rows and cells per row)")
    report("table shapes", seq_diff(ta, tb))

    hits = english_residue(jpb, spb)
    print(f"7. English runs of >= 5 words in Japanese prose: {len(hits)}")
    report("English residue", [f"line {ln}: {w}" for ln, w in hits])

    if len(sys.argv) > 4:
        def aux_numbers(path):
            txt = open(path, encoding="utf-8", errors="replace").read()
            return {m.group(1): m.group(2) for m in
                    re.finditer(r"\\newlabel\{([^}]*)\}\{\{([^}]*)\}", txt)}
        na, nb = aux_numbers(sys.argv[3]), aux_numbers(sys.argv[4])
        print(f"8. printed label numbers: EN={len(na)} JP={len(nb)}")
        report("label numbers", [f"{k}: EN={na.get(k)!r} JP={nb.get(k)!r}"
                                 for k in sorted(set(na) | set(nb)) if na.get(k) != nb.get(k)])
    else:
        print("8. printed label numbers: skipped (pass main.aux and main_JP.aux to enable)")

    print("ALL CHECKS PASSED" if ok else "SOME CHECKS FAILED")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())

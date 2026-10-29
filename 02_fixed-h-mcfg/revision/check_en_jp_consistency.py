# EN/JP consistency check for paper #2 (2026-10-29). Splits main.tex and japanese/main_JP.tex into
# units (sections, paragraphs, theorem-like environments), aligns them, and reports per unit
# differences in \ref/\cite and in math content (symbol-level). Usage: python3 revision/check_en_jp_consistency.py
# Expected residual noise: JP repeats symbols in prose, writes small numbers outside math, etc.
import re, sys, collections
EN = open(__import__('os').path.join(__import__('os').path.dirname(__file__),'..','main.tex')).read()
JP = open(__import__('os').path.join(__import__('os').path.dirname(__file__),'..','japanese','main_JP.tex')).read()

def body(s):
    i = s.index(r'\begin{document}'); j = s.index(r'\end{document}')
    return s[i:j]
EN, JP = body(EN), body(JP)

ENVS = 'theorem|lemma|proposition|corollary|definition|remark|example|openproblem|proof|table|abstract'
HEAD = re.compile(r'(\\section\*?\{[^}]*\}|\\subsection\*?\{[^}]*\}|\\paragraph\{[^}]*\}|\\begin\{(?:' + ENVS + r')\}(?:\[[^\]]*\])?|\\appendix\b|\\begin\{thebibliography\})')

def units(s):
    pos = [m.start() for m in HEAD.finditer(s)] + [len(s)]
    out = []
    for a, b in zip(pos, pos[1:]):
        out.append(s[a:b])
    return out

def kind(u):
    m = re.match(r'\\(section\*?|subsection\*?|paragraph|appendix|begin)\{?([^}\]]*)', u)
    k = m.group(1) if m.group(1) != 'begin' else m.group(2)
    return k

def labels(u): return re.findall(r'\\label\{([^}]*)\}', u)
def refs(u):
    r = []
    for m in re.finditer(r'\\(?:eq)?ref\{([^}]*)\}', u): r.append(m.group(1))
    return collections.Counter(r)
def cites(u):
    c = []
    for m in re.finditer(r'\\cite(\[[^\]]*\])?\{([^}]*)\}', u):
        opt = (m.group(1) or '').replace('~', ' ')
        for k in m.group(2).split(','): c.append((k.strip(), opt))
    return collections.Counter(c)

def maths(u):
    u = re.sub(r'(?<!\\)%.*', '', u)
    toks = []
    for m in re.finditer(r'\\\[(.*?)\\\]|\$\$(.*?)\$\$|\\begin\{(equation\*?|align\*?|gather\*?|aligned)\}(.*?)\\end\{\3\}|\$((?:\\\$|[^$])+?)\$|\\\((.*?)\\\)', u, flags=re.S):
        t = next(g for g in m.groups() if g is not None and g not in ('equation','equation*','align','align*','gather','gather*','aligned'))
        t = re.sub(r'\\text\{[^}]*\}', '', t)           # drop text inside math (language-specific)
        t = re.sub(r'\\(?:mathrm|textup)\{[^}]*?[^\x00-\x7f][^}]*\}', '', t)
        t = re.sub(r'\\label\{[^}]*\}', '', t)
        t = re.sub(r'\\(?:,|;|!|quad|qquad| )', '', t)
        t = re.sub(r'\s+', ' ', t).strip()
        t = t.replace('\\{', '{').replace('\\}', '}')
        if t: toks.append(t)
    return collections.Counter(toks)

E, J = units(EN), units(JP)
print('units EN', len(E), 'JP', len(J))
ke = [kind(u) for u in E]; kj = [kind(u) for u in J]
import difflib
sm = difflib.SequenceMatcher(a=[k + '|' + ','.join(labels(u)) for k, u in zip(ke, E)],
                             b=[k + '|' + ','.join(labels(u)) for k, u in zip(kj, J)], autojunk=False)
pairs = []
for tag, a1, a2, b1, b2 in sm.get_opcodes():
    if tag == 'equal':
        pairs += list(zip(range(a1, a2), range(b1, b2)))
    else:
        print('STRUCT', tag, [(ke[i], labels(E[i]), E[i][:60].replace('\n',' ')) for i in range(a1, a2)],
              '<->', [(kj[i], labels(J[i]), J[i][:60].replace('\n',' ')) for i in range(b1, b2)])
        if a2 - a1 == b2 - b1:
            pairs += list(zip(range(a1, a2), range(b1, b2)))
mode = sys.argv[1] if len(sys.argv) > 1 else 'all'
nd = 0
for i, j in pairs:
    e, jj = E[i], J[j]
    head = f'[EN unit {i} {ke[i]} {labels(e)} | {e[:70]!r}]'
    msgs = []
    if refs(e) != refs(jj):
        msgs.append(f'  REF  EN-only {dict(refs(e)-refs(jj))}  JP-only {dict(refs(jj)-refs(e))}')
    if cites(e) != cites(jj):
        msgs.append(f'  CITE EN-only {dict(cites(e)-cites(jj))}  JP-only {dict(cites(jj)-cites(e))}')
    me, mj = maths(e), maths(jj)
    def lex(c):
        s=' '.join(c.elements())
        s=re.sub(r'[,.;:]','',s)
        return collections.Counter(re.findall(r'\\[A-Za-z]+|\\.|[^\s{}]', s))
    if me != mj and lex(me) != lex(mj):
        le,lj=lex(me),lex(mj)
        msgs.append(f'  MATHLEX EN-only {dict(le-lj)}  JP-only {dict(lj-le)}')
        msgs.append(f'  MATH EN-only {list((me-mj).elements())}\n       JP-only {list((mj-me).elements())}')
    if msgs:
        nd += 1
        print(head); print('\n'.join(msgs))
print('units with differences:', nd, 'of', len(pairs))

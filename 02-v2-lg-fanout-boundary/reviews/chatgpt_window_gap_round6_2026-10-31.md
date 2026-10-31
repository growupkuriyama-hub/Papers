# 両側1文字窓における背骨の乗り換えと特徴標本長 — 第6次調査

**対象**：$F_n=L(E_n)$、$\Sigma=\{a,l,c,r\}$、$s_{1,1}$、ファンアウト1の $\mathcal B_{1,s_{1,1}}^{\le2}$（したがって無制限版も）。  
**調査日**：2026年10月31日。**原稿**：[`main.tex`](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/main.tex)、確認した Git blob `d03710d94d0274df05b7b49e53e85b218e65d599`。以下の「証明済み」は本報告内の数学的証明を指す。有限プログラムの計算結果は独立した「観察」として扱う。

## 結論の要約表

| 主張 | 判定 | 根拠の節 |
|---|---|---|
| 任意の端末ギャップを許す rank-2 Comp は「単項の両側端末ギャップ」と「2子のギャップなし連結」だけで言語として正確に再現できる | **証明済み** | §2 |
| 指定した標準橋 $c^{n-i}l\,H_i^q\,r^{n-i}$ を各段で別々に観測する乗換方式は、全段に橋を課すなら総長 $\Omega(n^3)$ を要する | **証明済み（その方式に限定）** | §3 |
| この観察から元の $\mathcal B_{1,s_{1,1}}$ 自体に $\Omega(n^3)$ 下界が従う | **未解決** | §3–§4 |
| $F_n$ に対する両側窓の $O(n^2)$ 特徴標本が構成できる | **未解決** | §3–§4 |
| $n=1,2$ の最短値はそれぞれ $8,44$ | **観察（全標本の厳密有限検査）** | §5–§6 |
| $n=3$ では単独で必須の語は0語。末尾 $a$ の標本は2語以上、末尾 $r$ の標本は3語以上必要 | **観察（明示的な有限全検査）** | §5–§6 |
| $n=3$ で $56\le\operatorname{cs}(F_3)\le144$。下界56は従来の稀な型の34より強い | **観察（検査器の正確性を§2で証明）** | §5–§6 |
| $n=3$ の144の標本には末尾 $a$ の長い背骨が2本あり、左右の子の先頭列は `cca` と `lca` | **観察** | §5–§6 |
| $n=3$ の厳密値、$n=4$ の既報上界336の改善、最短長の漸近次数の決定 | **未解決** | §4–§7 |

## 1. 定義、既知結果、および検証範囲

\[
E_0\to a,\qquad E_i\to lE_{i-1}E_{i-1}\mid cE_{i-1}r\quad(1\le i\le n),
\qquad F_n=L(E_n).
\]
長さ2以上の語は $s_{1,1}(x)=(x_1,x_{|x|})$、長さ1は独立した一文字型とする。標本 $K\subseteq F_n$ の非空因子全体を $\mathrm{Obs}(K)$ とし、原稿 `def:reconstruction` の Start / Const / Comp / Link を使用する。Link は同じ型かつ標本内に**まったく同一の左右文脈**を持つ2因子の間に張る。原稿 `prop:reconstruction-soundness` と既証明の $F_n$ の Clark–Eyraud 代入可能性により、$K$ が特徴標本であることと $F_n\subseteq L(\mathcal B(K))$ は同値である（単調性を併用）。

既知の $\|G_n\|=12n+3$ と $\bar\theta_{G_n}=4n-1$ は開始記号を別に数えない表示に従う。従来の別表示 $S\to E_n$ を入れる数値 $12n+7$ とは同じ文法の符号化差であり、本報告の議論には影響しない。第2次報告の二分化により無制限版とランク2版はファンアウト1で同じ言語である。既報の理論上の一般区間は、$n\ge2$ で
\[
n^2+7n+4\le\operatorname{cs}_{\mathcal B,s_{1,1}}(F_n)\le O(n^3).
\]

引用元は [第2次報告](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/reviews/chatgpt_window_gap_round2_2026-10-31.md)、[第3次報告](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/reviews/astra_window_gap_round3_2026-10-31.md)、[第5次報告](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/reviews/astra_window_gap_round5_2026-10-31.md)、[DeepSeek計算](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/reviews/deepseek_window_gap_search_2026-10-31.md) である。これらの歴史的数値と本報告の再計算を混同しない。

## 2. 正確な閉包判定に使える Comp 正規化

**補題2.1（端末ギャップ付き Comp の分解）。** $f=1$ とし、有限標本 $K$、型付け $s$ は任意でよい。原稿の $\mathcal B_{1,s}^{\le2}(K)$ における Comp の全規則のうち、次の二種類だけを残しても、その生成言語は変わらない。

- 単項：$[z]\to\alpha[u]\beta$、$z=\alpha u\beta$、$u\ne\varepsilon$、$\alpha,\beta\in\Sigma^*$。
- 二項：$[z]\to[u][v]$、$z=uv$、$u,v\ne\varepsilon$。

**証明。** 新しい2種はいずれも元の rank-2 以下の Comp 規則そのものであるから、一方の言語包含は即座に成立する。逆に、元の二項規則を
\[
[z]\to\alpha_0[u]\alpha_1[v]\alpha_2,
\qquad z=\alpha_0u\alpha_1v\alpha_2
\]
と書く。$p=\alpha_0u\alpha_1$、$q=v\alpha_2$ と置くと $p,q\ne\varepsilon$ で、双方とも観測済み $z$ の連続因子だから $[p],[q]$ が存在する。したがって
\[
[z]\Rightarrow[p][q]\Rightarrow
(\alpha_0[u]\alpha_1)([v]\alpha_2)
\]
と模倣できる。右辺の3規則は、順に許可された二項・単項・単項 Comp であり、元の規則と同じ非終端列を得る。元の単項 Comp はすでに許可された形である。Const、Link、Start は変更していないので、任意の導出木で二項規則を置換する帰納法により言語が一致する。$\square$

**補題2.2（区間動的計画法の完全性）。** 観測因子を Link の無向連結成分に潰し、元の各非終端 $[x]$ を所属成分で表す。補題2.1の単項・二項規則をこの成分上に射影して区間DPを行うと、任意の目標語 $w$ について $w\in L(\mathcal B_{1,s}^{\le2}(K))$ を正確に判定する。

**証明。** Link は型一致かつ同じ左右文脈をもつ因子から対称の規則を与えるため、無向辺の連結成分内では任意の2非終端間を Link 導出で相互に行き来でき、成分を同一視してよい。逆に成分の同一視による推移的移動は、有限個の Link 規則の連鎖として実現できる。単項規則に $\alpha=\beta=\varepsilon$ の場合は元の $u=z$ で同一成分への自己ループだけとなるから、削除してよい。それ以外の単項規則は生成語長を子の語長より厳密に増やし、二項規則も2子がいずれも非空なので親より短い。従って目標語の区間長の昇順に全規則を評価すれば必ず有限で停止し、規則を使う導出の高さに関する帰納法およびDPで採用した規則への逆向き帰納法により、可導出性とDPの状態が一致する。$\square$

これが§6の完全なPython実装の根拠である。Linkのキーは `(左文脈, 右文脈, ('pair',先頭,末尾))`、一文字には `('single',文字)` を用い、異なる長さの型を混同しない。すべての単項端末ギャップを許すので、`maxgap=0` の近似版では**ない**。

## 3. S1：乗り換えの標準橋が三次費用を持つこと

$U_0=a$、$U_i=lC_{i-1}U_{i-1}$、$C_i=c^iar^i$ とする。第5次報告の $H_i^q$（$i\ge2$, $q\in\{c,l\}$）を
\[
H_i^q=\{\partial w:w\in L_i,\ \mathrm{last}(w)=a,\ \mathrm{first}(\partial w)=q\}
\]
と書けば、既証明の最短長は
\[
\min|H_i^c|=i^2+i,\qquad \min|H_i^l|=i^2+3i-4.
\tag{3.1}
\]
ここで $\min|H|$ は $\min\{|h|:h\in H\}$ の略記である。

**命題3.1（提案された標準橋方式の三次コスト）。** $i=2,\ldots,n$ の各段で、$h_i\in H_i^{q_i}$ を少なくとも1個、次の**正確に指定した文脈**で観測する方式を考える：
\[
  b_i=c^{n-i}l\,h_i\,r^{n-i}\in F_n.
\tag{3.2}
\]
ここで $q_i\in\{c,l\}$ は任意でよい。この方式の観測標本には、重複を除いても総符号長 $\Omega(n^3)$ が必要である。各段で異なる2つの $h_i$ を同じ文脈で直接 Link する方式でも同じ下界である。

**証明。** (3.2)が $F_n$ の語なのは、$lh_i\in L_i$ であり、それを外側で $n-i$ 回 $c(\cdot)r$ に入れているためである。異なる $i$ の語 $b_i$ は、先頭で $l$ が初めて現れる位置が $n-i+1$ なので同一になれない。各語の符号長について、(3.1)より
\[
|b_i|+1\ge 2(n-i)+1+(i^2+i)+1
 =i^2-i+2n+2.
\]
従って
\[
 \|K\|_+\ge\sum_{i=2}^n(i^2-i+2n+2)
 =\Theta(n^3).
\]
直接 Link のため同じ段に異なる断片を2個置くなら、必要な標本語は少なくとも2個となるので下界は弱くならない。$\square$

**量化の注意。** 命題は「各段について *(3.2) の正確な周辺文脈* で橋を別々に置く」という設計の下界である。原稿の $B$ は任意の観測因子・別の周辺文脈・二項分割・Link 鎖を使える。したがってこの命題から、$\operatorname{cs}(F_n)=\Omega(n^3)$ を推論してはいけない。逆に、4本の背骨で隣接した段の `cc,cl,lc,ll` を全て表現しても、同じ型の断片間に共通文脈が存在する保証はない。これも二次上界の証明にはならない。

## 4. S1 の停止点と次の検査可能な中間命題

**未解決 A**：第5次報告の $O(n^2)$ 内部証拠に、総長 $O(n^2)$ の追加語を入れて末尾 $a$ の語を全て導く構成。必要な条件は、異なる長い背骨の断片が Link で合流できる文脈の**全段共有**、または Link に頼らず同じ役割を果たす分割の明示である。命題3.1から、段別の `c^{n-i}l □ r^{n-i}` の橋をそのまま使う設計は解決法ではない。

**未解決 B**：全ての導出に、段 $i$ に対応する長さ $\Omega(i^2)$ の節点が強制され、しかもそれらの費用を別々に課金できること。第2次報告が示した構文境界を跨ぐ Link の反例があるため、「元の $E_i$ 構文木と同じ節点が標本に必要」というだけでは証明にならない。スタック変換による合同類の分類は、型付き合同を確認する道具だが、それ自体はBの導出節点の出現を強制しない。

**有限検査用の具体的命題**：$n=3$ で「末尾 $r$ の全語を標本に与えても、末尾 $a$ の標本1語では $a$-終端の全12語を導けない」。また「末尾 $a$ の全12語を与えても、型 $(c,r)$ と $(l,r)$ の2語だけでは $r$-終端の全30語を導けない」。§5–§6でそれぞれ12件と144件を正確に検査し、どちらも真だった。これらは $n=3$ の事実であり、各 $n$ に同じ個数の背骨が必要という一般定理ではない。

## 5. S2：有限計算から確定する区間と構造

§6の実装は、有限 $K$ について原稿の型と観測文脈をすべて列挙し、補題2.1・2.2により $\mathcal B^{\le2}_{1,s_{1,1}}$ の**完全な**生成判定を行う。$n=1,2$ では全 $2^{|F_n|}$ 標本を列挙する。$n=3$ では全42語の部分集合は列挙しないため、厳密値は主張しない。

### 5.1 新たな有限下界56

$F_3$ の末尾 $a$ の語を $A$、末尾 $r$ の語を $R$ とする。$|A|=12$、$|R|=30$。$R$ のうち先頭 $c$ は6語、先頭 $l$ は24語である。

1. $R$ の30語を**すべて**補助に置き、$A$ から1語だけ選ぶ12通りを検査しても、$A$ の全12語を生成する候補は0。$A$ から2語選ぶ66通りでは52通り成功。
2. $A$ の12語を**すべて**補助に置き、$R$ から型 $(c,r)$ と $(l,r)$ の語をそれぞれ1個選ぶ $6\times24=144$ 通りを検査しても、$R$ の全30語を生成する候補は0。

この有限検査と単調性から、どの特徴標本も少なくとも **2個の $a$-終端語**と **3個の $r$-終端語**を含む。$a$-終端の最小符号長は14、$(c,r)$ の最小符号長は8、$(l,r)$ の最小符号長は12である。3個の $r$ 語には両型が少なくとも1個ずつ必要なので最も安い場合でも $8+8+12=28$。従って有限検査を正確とした場合の厳密な下界は
\[
\boxed{\operatorname{cs}_{\mathcal B,s_{1,1}}(F_3)\ge2\cdot14+(8+8+12)=56.}
\tag{5.1}
\]
これは稀な型だけからの34を厳密に強めるが、**理論上の一般 $n$ の下界を強めない**。

全42語から任意の1語を除去しても導出可能であり、**単独で必須の語は0**。したがって「必須語の固定＋分枝限定」という従来の工夫だけでは $n=3$ の探索を劇的に小さくできない。

### 5.2 上界144を独立に再検証

§6の標本12語は、Full Comp（全端末ギャップあり）で42語をすべて生成するため、$\operatorname{cs}\le144$ である。うち末尾 $a$ の語は

- `lccarrlcarlaa`（14点）。右背骨の各 $l$ 段で左子が始まる文字の列は `cca`。
- `llcarlaalcarlaa`（16点）。同じ列は `lca`。

ここで列は上段から順に、左の子の先頭文字を記したもの。最下段 $E_1$ の左子は $a$ 固定である。2本以外の標本10語は $r$ 終端である。4本の全パターンをそのまま置いているわけではない点は、今後の乗り換え構成の手がかりとなる。ただしこれだけで一様な二次上界は導けない。

### 5.3 $n=4$ の扱い

前回の [DeepSeek計算報告](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/reviews/deepseek_window_gap_search_2026-10-31.md) が報告した $\operatorname{cs}(F_4)\le336$（`maxgap=0` の部分作用素で確認）は既知の上界として維持する。本報告の付録コードは $n=4$ の1806語に対する全判定・改善探索を実行していない。従って **新たな改善値を証明・観測したとは主張しない**。

## 6. 実装・再現性（標準ライブラリのみ）

以下が実行したスクリプト**全文**。`script.py` としてUTF-8で保存し、Windows PowerShellで `py -3 script.py` を実行できる。Linuxで実行した今回のコマンドは `python /mnt/data/window_round6.py`。Python 3.13.5、標準ライブラリのみ。ソースは同一で、経過時間のみCPU等に依存する。

```python
"""Exact rank-two fan-out-one substring reconstruction (standard library only)."""
import sys, time, itertools
from collections import defaultdict
from functools import lru_cache


def language(n):
    words = ('a',)
    for _ in range(n):
        words = tuple(sorted({'c'+u+'r' for u in words} |
                             {'l'+u+v for u in words for v in words}))
    return words


def typ(x):
    return ('single', x) if len(x) == 1 else ('pair', x[0], x[-1])


def cost(F):
    return sum(len(w)+1 for w in F)


class Grammar:
    def __init__(self, sample):
        self.sample = tuple(sorted(sample))
        factors = {w[i:j] for w in self.sample
                   for i in range(len(w)) for j in range(i+1,len(w)+1)}
        self.fac = tuple(sorted(factors, key=lambda x:(len(x),x)))
        ids = {s:i for i,s in enumerate(self.fac)}
        par = list(range(len(ids)))
        def root(x):
            while par[x] != x:
                par[x] = par[par[x]]
                x = par[x]
            return x
        def union(x,y):
            a,b=root(x),root(y)
            if a!=b: par[b]=a
        ctx = defaultdict(list)
        for w in self.sample:
            for i in range(len(w)):
                for j in range(i+1,len(w)+1):
                    x=w[i:j]
                    ctx[(w[:i],w[j:],typ(x))].append(ids[x])
        for bucket in ctx.values():
            if len(bucket)>1:
                x=bucket[0]
                for y in bucket[1:]: union(x,y)
        self.state={x:root(ids[x]) for x in self.fac}
        self.start=set(self.state[w] for w in self.sample)
        self.start_bits=sum(1<<s for s in self.start)
        unary=defaultdict(set)
        binary=defaultdict(set)
        for z in self.fac:
            sz=self.state[z]
            L=len(z)
            for i in range(L):
                for j in range(i+1,L+1):
                    if i==0 and j==L: continue
                    u=z[i:j]
                    unary[(z[:i],z[j:],self.state[u])].add(sz)
            for i in range(1,L):
                binary[(self.state[z[:i]],self.state[z[i:]])].add(sz)
        U=defaultdict(dict)
        for (a,b,st),vals in unary.items():
            U[(a,b)][st]=sum(1<<v for v in vals)
        self.unary=dict(U)
        self.binary={key:sum(1<<v for v in vals) for key,vals in binary.items()}
        self.inits=self.state

    def derives(self,w):
        N=len(w)
        chart=[[0]*(N+1) for _ in range(N)]
        pairs=self.binary
        urules=self.unary
        inits=self.inits
        for d in range(1,N+1):
            for i in range(N-d+1):
                j=i+d
                x=w[i:j]
                init=inits.get(x)
                states=(1<<init) if init is not None else 0
                for k in range(i+1,j):
                    left,right=chart[i][k],chart[k][j]
                    while left:
                        lb=left&-left
                        sl=lb.bit_length()-1
                        left-=lb
                        rr=right
                        while rr:
                            rb=rr&-rr
                            sr=rb.bit_length()-1
                            rr-=rb
                            states |= pairs.get((sl,sr),0)
                for na in range(d):
                    a=x[:na]
                    for nb in range(d-na):
                        if na==0 and nb==0: continue
                        b=x[d-nb:] if nb else ''
                        rule=urules.get((a,b))
                        if not rule: continue
                        child=chart[i+na][j-nb]
                        while child:
                            bit=child&-child
                            st=bit.bit_length()-1
                            child-=bit
                            states |= rule.get(st,0)
                chart[i][j]=states
        return bool(chart[0][N]&self.start_bits)


def covered(F,targets,stop_early=True):
    g=Grammar(F)
    if stop_early:
        for w in targets:
            if not g.derives(w): return False
        return True
    return [w for w in targets if not g.derives(w)]


def essentials(words):
    essential=[]
    for w in words:
        if not Grammar(set(words)-{w}).derives(w): essential.append(w)
    return tuple(essential)


def rare_bound(words):
    return sum(min(len(w)+1 for w in words if typ(w)==t)
               for t in {typ(w) for w in words})


def greedy(words,seed):
    F=set(seed)
    assert covered(F,words), 'seed does not reconstruct!'
    for w in sorted(F,key=lambda x:(-(len(x)+1),x)):
        if covered(F-{w},words): F.remove(w)
    return tuple(sorted(F))


def spine(w,n):
    """Follow the right child of every l-node until c/a; output left-child initials."""
    if n==0: return ''
    choices=[]
    while n:
        if w[0]=='c': break
        assert w[0]=='l'
        # derive the unique left E_(n-1) prefix using a deterministic parser
        p=end_of(w,1,n-1)
        choices.append(w[1])
        w=w[p:]
        n-=1
    return ''.join(choices)


def end_of(w,start,k):
    if k==0:
        assert w[start]=='a'
        return start+1
    if w[start]=='c':
        p=end_of(w,start+1,k-1)
        assert w[p]=='r'
        return p+1
    assert w[start]=='l'
    p=end_of(w,start+1,k-1)
    return end_of(w,p,k-1)


def check_n(n,seed=None):
    words=language(n)
    t=time.perf_counter()
    print('n=%d |L|=%d total=%d rare=%d' % (
        n,len(words),cost(words),rare_bound(words)),flush=True)
    e=essentials(words)
    print('individually essential=%d cost=%d' % (len(e),cost(e)),flush=True)
    if n<=2:
        best=10**9
        winners=[]
        for bits in range(1<<len(words)):
            F=tuple(w for i,w in enumerate(words) if bits>>i&1)
            c=cost(F)
            if c<=best and covered(F,words):
                if c<best:
                    best=c
                    winners=[]
                winners.append(F)
        print('exact=%d minimizers=%d' %(best,len(winners)),flush=True)
    elif n==3:
        A=[w for w in words if w.endswith('a')]
        R=[w for w in words if w.endswith('r')]
        C=[w for w in R if w.startswith('c')]
        Q=[w for w in R if w.startswith('l')]
        assert (len(A),len(R),len(C),len(Q))==(12,30,6,24)
        a_one=sum(all(Grammar(R+[a]).derives(w) for w in A) for a in A)
        a_two=0
        spinepairs={}
        for x,y in itertools.combinations(A,2):
            g=Grammar(R+[x,y])
            if all(g.derives(w) for w in A):
                a_two+=1
                key=tuple(sorted((spine(x,3),spine(y,3))))
                spinepairs[key]=spinepairs.get(key,0)+1
        r_two=0
        for x in C:
            for y in Q:
                g=Grammar(A+[x,y])
                if all(g.derives(w) for w in R):
                    r_two+=1
        print('n3 a-with-all-r one successes=%d / 12' % a_one,flush=True)
        print('n3 a-with-all-r two successes=%d / 66' % a_two,flush=True)
        print('n3 successful spine pairs='+repr(sorted(spinepairs.items())),flush=True)
        print('n3 r-with-all-a cross-type two successes=%d / 144' % r_two,flush=True)
        assert a_one==r_two==0
        bound=(14+14)+(8+8+12)
        print('n3 certified lower=%d' % bound,flush=True)
        F=greedy(words,seed)
        print('n3 certified upper=%d sample size=%d' %(cost(F),len(F)),flush=True)
        print('n3 sample='+repr(F),flush=True)
        print('n3 a-spines='+repr([(w,spine(w,3)) for w in F if w.endswith('a')]),flush=True)
    print('n%d elapsed=%.3fs' %(n,time.perf_counter()-t),flush=True)


if __name__=='__main__':
    t=time.perf_counter()
    check_n(1)
    check_n(2)
    seed3=('cclaarr','clcarlaar','lccarrlcarcar','lccarrlcarlaa',
           'llcarlaaccarr','llcarlaalcarlaa','lccarrclaar',
           'lccarrllaacar','llcarcarclaar','cllaalaar',
           'clcarcarr','cccarrr')
    check_n(3,seed3)
    print('total elapsed=%.3fs' %(time.perf_counter()-t),flush=True)
```

### 実行ログ（標準出力全文）

実行環境：Linuxコンテナ、Python 3.13.5。総実行時間は `25.351s`（プログラムの `time.perf_counter` 計測値）。特に $n=3$ 部分は `25.308s`。実行時のCPU負荷により再実行値は変わる。

```text
n=1 |L|=2 total=8 rare=8
individually essential=2 cost=8
exact=8 minimizers=1
n1 elapsed=0.000s
n=2 |L|=6 total=44 rare=22
individually essential=6 cost=44
exact=44 minimizers=1
n2 elapsed=0.038s
n=3 |L|=42 total=584 rare=34
individually essential=0 cost=0
n3 a-with-all-r one successes=0 / 12
n3 a-with-all-r two successes=52 / 66
n3 successful spine pairs=[(('cca', 'cla'), 4), (('cca', 'lca'), 4), (('cca', 'lla'), 8), (('cla', 'lca'), 8), (('cla', 'lla'), 4), (('lca', 'lca'), 4), (('lca', 'lla'), 16), (('lla', 'lla'), 4)]
n3 r-with-all-a cross-type two successes=0 / 144
n3 certified lower=56
n3 certified upper=144 sample size=12
n3 sample=('cccarrr', 'cclaarr', 'clcarcarr', 'clcarlaar', 'cllaalaar', 'lccarrclaar', 'lccarrlcarcar', 'lccarrlcarlaa', 'lccarrllaacar', 'llcarcarclaar', 'llcarlaaccarr', 'llcarlaalcarlaa')
n3 a-spines=[('lccarrlcarlaa', 'cca'), ('llcarlaalcarlaa', 'lca')]
n3 elapsed=25.308s
total elapsed=25.351s
```

## 7. まとめと原稿への採用判断

本報告の新しい理論的成果は、**全ギャップ付きランク2 Comp の正確な2形式への分解**（補題2.1・2.2）と、**指定された標準橋を各段別に置くと三次費用が避けられない**という限定命題（命題3.1）である。有限計算では、$n=3$ の厳密値は求まらなかったものの、$56\le\mathrm{cs}\le144$ まで狭め、単独必須語が存在しないことと、2本の $a$ 終端背骨で被覆できることを確認した。

従って、現時点で **$s_{1,1}$ の $\Theta(n^2)$ あるいは $\Omega(n^3)$ を原稿の定理として追加することはできない**。命題3.1はB全体の下界に読み替えず、補題2.1・2.2についても掲載前に独立検証することを推奨する。小さい $n$ の比だけから漸近次数を推定しない。

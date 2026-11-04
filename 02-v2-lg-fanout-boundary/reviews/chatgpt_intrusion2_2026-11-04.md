# 場合 I の型付き τ：侵入反鎖への還元の再点検と、c-融合・背景 b の限界

**研究日**：2026-11-04　**対象**：三文字内容型付け、`op:fanout-two` の場合 I、系列第二十一報  
**原稿**：`growupkuriyama-hub/Papers/02-v2-lg-fanout-boundary/main.tex`（2026-11-04 に GitHub 接続から取得、blob `b72cd2ed648f802886f0ab7c60a72f9f40c0864b`）。本報は研究ノートであり、原稿の改稿を行っていない。

## 0. 主張ごとの判定

| 主張 | 判定 | 根拠・限界 |
|---|---|---|
| 配置つき安全代表 `β_X(B,π)` と侵入の定義 | **独立に確認** | §1。fan-out 2 ではラベル B だけでなく配置 π が必要 |
| 無印重節点 ⇒ θ-侵入 | **独立に確認／既報補題** | §1。安全短縮が型付き最小性に反する |
| `τ_X≤49(r+1)vθ(3d+q_X)` と、`q_X≤4vh` | **独立に確認／既報の還元で目的には不足** | §1。h の上界は出さない |
| J1：`c⁴` から c 連の再配分・自己融合 | **証明済み／既報 F′ の文字置換** | §2。根語にすでに c が存在する場合の操作 |
| J1：融合だけで、c が侵入した語を c-free の型 `{a,b}` へ戻せる | **反証（この推論の形は不可能）** | §2。各 `SUB_t` は完成語の内容集合を保存。別の c-free 証拠との橋渡しはなお可能 |
| J2：背景 b があっても、(R) の**全ての前提を満たせば** a 個数は等しい | **独立に確認／既存の (R)** | §3。σ の一致と b,c 個数一致が必要 |
| J2：b,c 個数一致だけで (R) を適用 | **反証** | §3。`L′_5={a^5,b^4,c^4,abc,acab}` は (2,c) 代入可能 |
| 反鎖同ラベルの個数 `h≤poly(v,θ)`、全ての型付き τ の多項式上界 | **未解決** | §5。fan-out1 の `{a,b}` についても一般上界なし |
| `θ_{ab}≤poly(v,θ)` の条件下の `μ_ab` 上界 | **証明済み／既存二文字定理への帰着** | §4。条件付きであり核心には不足 |
| `L_N` の支援集合別 Parikh 繊維の例 | **証明済み／既報原理の特例** | §4・付録A。全 arity で代入可能、数値検査は arity1,2 |
| `L_N` が小 θ の超多項式反例である | **主張しない** | §4。低厚さの表示を与えていない |
| 抽象文字の強制閉包が一般 h を抑える | **未解決** | §5。汎用的な小型種の完全証明書を得ていない |
| 文献上の新規性 | **未確認** | §6。支持集合の不変性は初等的 |

## 1. 配置と反鎖の還元を再点検

`Σ={a,b,c}`、`L∈C_{2,c}`、`G` を reduced good、fan-out≤2、rank≤r、`v=|V|`, `θ=\bar θ_G≥1` とする。場合 I は、ある受理語の因子として `a⁴,b⁴,c⁴` の全てが現れること。型付きラベル `X=A_{(t_1,…,t_d)}` (`d≤2`) の最短導出組のうち節点数が最小の導出 T を取る。`t_X` は型付き導出組の最小全長、`τ_X` は同一分布類の最短全長。原稿 `lem:typed-homogeneity` により `τ_X≤t_X`。

根の成分 i ごとに内容 `t_i` の各文字の出現を一つずつ印付ける。全印数 `M_X≤3d`。節点 u の無型ラベルを B、B の成分 j が根の成分 `π_u(j)` へ写るとする。good の非削除・線形・非併合性によりこの配置は定まり、π は `≤d^{fan(B)}≤4` 通り。

`β_X(B,π)=min{||z||_1 : z∈L_B(G), supp(z_j)⊆t_{π(j)} for every j}`

（該当する z がなければ無限大）。**安全な短い代表**は `β_X(B,π)≤θ`。T にある u は元の u の部分木が候補になるので β は有限である。

**重節点に関する判定**。`ℓ_u>θ`、しかも u の部分木に印がない場合、もし `β_X(B,π_u)≤θ` なら安全な z に置換すると、全ての根成分で印が残る一方、禁じた文字は新たに入らない。成分内容は元の `t_i` のままで、根の全長だけ短くなる。これは型付き最短性に矛盾する。よってこの u は θ-侵入節点。

一経路上の型付きラベルは反復しない（反復すれば部分木を刈り込み、最短性または節点数最小性に矛盾）。型付きラベルは高々 `49v` 個。θ-重い反鎖から印を持つ高々 `M_X` 個を除くと、残りは侵入節点の反鎖である。最大侵入反鎖幅を q_X とすると、重節点数は `≤49v(M_X+q_X)`。重節点の直接書込みは θ 以下、軽い子は各節点高々 r 個で各総長 θ 以下、従って

`τ_X≤t_X≤49(r+1)vθ(M_X+q_X)≤49(r+1)vθ(3d+q_X)`。

同じ `(B,π)` の侵入節点の反鎖幅が h 以下なら、種類は最大 `4v` なので `q_X≤4vh`、結果

`τ_X≤49(r+1)vθ(3d+4vh)`。

ここまでを前報 `chatgpt_intrusion_2026-11-04.md` と照合した。**h の上界そのものは導いていない**。新規の多項式上界ではなく、未解決量の明確な定式化である。

## 2. J1：c 連の融合はできるが、c の消去ではない

### 2.1 成立する操作

`c⁴` が受理語に因子として現れるとする。二穴組 `(c,cc)` と `(cc,c)` はともに内容ベクトル `({c},{c})` を持ち、許容文脈 `(ε,c,ε)` に入れると双方とも `c⁴` となる。従って

`D_L^{(2)}(c,cc)=D_L^{(2)}(cc,c)`。

任意の許容二穴文脈でこの組を交換できるので、**既に二つの c 連がある受理語**では、その間の固定部分を保ったまま一文字の c を左右に移せる。さらに、一穴の `D(c²U)=D(cUc)` が一つの受理語を共有する場合には、既報 F′ の証明中の `a→c` の文字交換により、c の連を自己融合できる。c の連の数と個数に必要な余裕は F′ と同じで、単に `c⁴` が存在するだけで無条件にすべての c を動かせるという主張ではない。

### 2.2 根の内容型を回復するためには足りない：支持集合不変性

**補題 2.1（全体支持集合の不変性）。** 一段の `SUB_t` で `E[X],E[Y],H[X]∈L` から `H[Y]∈L` を導くとき

`supp(H[Y])=supp(H[X])`。

**証明。** `supp(X_i)=supp(Y_i)` が全成分で成り立ち、穴以外の文字は文脈 H で一致する。全体の支持集合は各固定部と穴の支持集合の和集合であるから、両者で等しい。∎

従って、c を含む受理語の中でどれほど c 連を再配分・融合しても、その操作から直接 c-free な `{a,b}` の語は生じない。例えば二つの θ-侵入節点をそれぞれ c を含む短い代表へ替えた後、二つの c 連を一つへ融合しても、残った c を**完全に**消去することはできない。

ただしこの観察は、**c を含む共通文脈で確立した分布同値を、別の c-free な受理語に適用すること**まで禁止するものではない。そのような短縮を実現するには、c-free な共通の穴組と、その c-free な別文脈で受理される語を用意する必要がある。これが J1 を定理 I から一般の τ へ移す際の欠けている段である。

### 2.3 融合できるというだけでは反鎖幅は減らない

多数の侵入節点を c-containing 代表で縮めて得られるのは、根の型 ab ではなく abc の語である。反鎖幅 h を抑えるには、同じラベルの多数の候補から生じたこの abc の語を、**既存の ab 受理語を受理する許容文脈と結び付けて** c-free な短い組へ移す必要がある。現行の F′・E・N は、純粋 a の根語で使っていた a-free 塊への移行を自動で提供しない。

## 3. J2：背景に b があっても (R) は成立する。ただし骨格一致が必要

場合 I の既報の剛性 (R) は、`σ_{b,c}(w)` を a,b,c 全ての極大連を一文字に縮めた骨格として、二つの受理語 w,w' が

`σ_{b,c}(w)=σ_{b,c}(w')`, `|w|_b=|w'|_b`, `|w|_c=|w'|_c`, `0<|w|_a,|w'|_a<k`

を満たせば `|w|_a=|w'|_a` というもの。これは背景が純粋 a に限られる主張では**ない**。同じ骨格上で b,c の連の長さを合わせてから、a の骨格と最小純粋 a 語の長さ k を使う元の証明がそのまま適用できる。

しかし、**骨格の一致を示さない限り (R) は適用できない**。背景 b と c の侵入が入り交じると、c 連の融合や c の追加によって b 連の隣接関係・全体の極大連骨格が変わるため、定理 I と同じ骨格を自動生成することはできない。

この前提を落とせないことは、**場合 I 自体**の有限言語

`L′_k={a^k, bbbb, cccc, abc, acab}`（少なくとも `k=5,6,7`）

で分かる。`a⁴,b⁴,c⁴` の全てが受理語に出現し、付録Aで `k=5,6,7` の (1,c),(2,c) 代入可能性を**全許容文脈の有限全数検査**で確認した。既報の `L_k={a^k,abc,acab}` の議論に b⁴,c⁴ を付加した模型である。`abc`,`acab` は b,c 個数がともに1なのに a 個数は1と2で違い、骨格も一致しない。したがって「b,c の個数だけ合わせれば a の損失が一致する」という推論は偽である。**(R) の前提を満たす比較自体は依然として健全**である。

## 4. ファンアウト1型 ab、開始型 ab に関して確認できる限定結果

### 4.1 二文字影への帰着（既報の条件付き結果）

`Γ={a,b}`、`L_Γ=L∩Γ^+` とする。非削除性により G の c を直接書く規則を落として成功導出を刈り込んだ H は L_Γ を生成し、`L_Γ∈C_{2,c_Γ}`。H の非終端数は ≤v、fan-out≤2、rank≤r。ただし `θ_Γ=\bar θ_H` を元の θ で抑えることはできない。

原稿 `thm:two-letter-content` の定数 `C_{2,r}=(r+1)(28r+117)+3` を用いると、開始型 ab が実現するとき

`μ_ab(L)≤C_{2,r}v² θ_Γ⁴ H_{θ_Γ}`、`H_m=Σ_{j=1}^m 1/j`。

また、Γ-only 成功導出に現れる型付き X については、同じ影の短い分布代表を元の L にも移せる。したがって `θ_Γ≤poly(v,θ)` **という追加仮定の下では** μ_ab と該当する τ_X に多項式上界が出る。これは既存の二文字定理の応用であって、一般の h を抑えるものではない。影に X が実際に現れない場合の τ_X には適用できない。

### 4.2 支持集合ごとに一つの Parikh 繊維を持つ対照模型

任意の `N≥4` について Parikh ベクトルの集合

`P_N={(4,0,0),(0,4,0),(0,0,4),(N,1,0),(N,1,1)}`

を取り、`L_N={w∈{a,b,c}^+ : Ψ(w)∈P_N}` とする。各ベクトルは全て**異なる支持集合** `{a},{b},{c},{a,b},{a,b,c}` を持つ。ある許容文脈が同じ成分内容の二組をともに受理すれば、完成語の支持集合が等しいため、受理語の Parikh ベクトルも一致し、固定文脈の寄与を引けば穴の Parikh 総数が一致する。したがって他のいかなる許容文脈でも両組の所属は一致する。よって

**`L_N` は全ての有限 arity に対して内容型付けによる代入可能言語**である。

特に `a⁴,b⁴,c⁴∈L_N`、`μ_ab(L_N)=N+1`、`a^Nb∈L_N`、`a^{N-1}b∉L_N`。同時に内容 abc の語も存在する。この模型は、c⁴ と多量の abc 語があるだけで ab 型の短い語が自動強制されるわけではないことを示す。ただし L_N の**小さい θ を持つ reduced good 表示は与えていない**。従って `μ_ab≤poly(v,θ)` の反例ではなく、h の超多項式下界でもない。

付録Aのプログラムは `N=4,5,6` について、有限言語の**全ての非空穴・許容一穴／二穴文脈**を列挙し、共通文脈で受理される同内容の穴組の分布集合を比較した。全件 PASS。全 N の証明は直前の Parikh 繊維の論証による。

## 5. J3 と、h が止まった場所

今回、抽象文字による新しい短い **c-free 短縮の証明書**は得られなかった。§2.2 の補題により、abc 支持の種しかない探索で ab 支持の結論が出ることはないため、J3 の種は最低限**既存の ab 型の受理語**と、それを変形する共通穴の文脈を明示しなければならない。この要件は探索の枝刈りには使えるが、h の上界そのものを証明しない。

まず fan-out1 の同一ラベル B で、最短の ab 型根導出の反鎖にある侵入節点を二つ選ぶことを考える。各々の短い代表は少なくとも一つ c を持ち得る。二節点を短縮すると生じる abc 語に c を再配分しても、元の ab の長さを短縮したとはいえない。一方、原稿の代入可能性がその別の c-free 文脈への短縮を与えないという**反例も構成できていない**。よって

`h≤poly_r(v,θ)` は **fan-out1 の ab 型、開始記号の μ_ab、二成分の一方だけが ab の型の全てについて未解決**。

`L_N` はこの未解決を否定する例ではなく、二穴での代入可能性を備えた低厚さ指数族も得ていない。既報の倍増文法（`S→A_n b|a⁴|b⁴|c⁴`, `A_i→A_{i-1}A_{i-1}|c`）は `cb,ccb∈L` が `(ε,b)` を共有し、`c⁴∈L`, `c⁵∉L` によって arity 1 ですでに破れる。これを本件の反例として再利用するのは不正確である。

## 6. 結論・次に絞るべき一点

1. **証明できたこと**：配置つき侵入反鎖の定式化と上界を再点検し、J1 の c-連移送・融合が成り立つ範囲、`SUB_t` の全体支持集合不変性、J2 の (R) に必要な骨格一致を確定した。既報の二文字影条件付き定理と支持集合別の対照模型も検査した。
2. **止まった場所**：複数の c-intruding 短縮から生じる abc 語を、**c-free の根型と同じ許容文脈**へ戻す操作。一般の `h≤poly(v,θ)` も全 τ の上界も得ていない。
3. **次に絞るべき一点**：fan-out1、開始型 `{a,b}`、同一 B の侵入節点二つに限定し、各 B の短い c-containing 代表で得る abc 語と既存の ab 語の間に、**どの c-free 穴組・許容二穴文脈が共有可能か**を分類する。もしこれが不可能なら、`θ=poly(v)` と真の (1,c)/(2,c)-代入可能性を満たす反例族を探す。

**先行研究との関係**：マーク保存法、型付き分布クラス、二文字上界は `main.tex` と `chatgpt_typed_case1_2026-11-04.md`、侵入の還元は `chatgpt_intrusion_2026-11-04.md`、F′ と (R) は `claude_straddle_2026-11-04.md` / `claude_f_branching_2026-11-04.md`。全体支持集合不変性は集合の和の初等的性質で、新規発見とはしない。一般の先行刊行文献との一致は未確認。

## 付録 A. Python 3 標準ライブラリ、有限言語の分布全数検査

Windows: `py -3 verify_intrusion_independent_20261104.py`。有限の PASS はあくまで表示した有限言語についてのもの。全 N に対する言語所属は §4.2 の数学的証明による。

```python
#!/usr/bin/env python3
"""Finite countercheck for support-fibre isolation; Python standard library."""
from collections import defaultdict

def make_L(n):
    # One Parikh vector for each of the distinct supports a, b, c, ab, abc.
    out={'a'*4, 'b'*4, 'c'*4}
    for pos in range(n+1):
        v=['a']*(n+1); v[pos]='b'; out.add(''.join(v))
    for bp in range(n+2):
        for cp in range(n+2):
            if bp==cp: continue
            v=['a']*(n+2); v[bp]='b'; v[cp]='c'; out.add(''.join(v))
    return out

def decompose(w,arity):
    N=len(w)
    if arity==1:
        for i in range(N):
            for j in range(i+1,N+1):
                yield (w[i:j],),(w[:i],w[j:])
    else:
        for i in range(N):
            for j in range(i+1,N):
                for p in range(j+1,N): # middle fixed nonempty
                    for q in range(p+1,N+1):
                        yield (w[i:j],w[p:q]),(w[:i],w[j:p],w[q:])

def check(L):
    for arity in (1,2):
        dist=defaultdict(set); shared=defaultdict(set)
        for w in L:
            for u,E in decompose(w,arity):
                ty=tuple(frozenset(t) for t in u)
                dist[u].add(E)
                shared[(ty,E)].add(u)
        for (_,E),u_set in shared.items():
            if len(u_set)>1:
                pivot=next(iter(u_set))
                for other in u_set:
                    if dist[pivot]!=dist[other]:
                        return False,(arity,pivot,other,E)
    return True,None

def support_fixed_by_substitution():
    # For each coordinate support A_i = B_i, a fixed surrounding context
    # yields identical total support, by union of sets.
    abc='abc'
    for arity in (1,2):
        for m in range(1<<3):
            for e in range(1<<3):
                # formal arbitrary supports of fixed context and tuple components
                before={abc[i] for i in range(3) if m&(1<<i)}
                comp={abc[i] for i in range(3) if e&(1<<i)}
                assert before|comp==comp|before
    return True

def main():
    assert support_fixed_by_substitution()
    print('SUPPORT INVARIANCE: PASS (set-union identity)')
    for n in (4,5,6):
        L=make_L(n)
        ok,fail=check(L)
        assert ok,fail
        ab=min(len(w) for w in L if set(w)=={'a','b'})
        assert ab==n+1
        assert 'a'*n+'b' in L and 'a'*(n-1)+'b' not in L
        assert any('c' in w and set(w)=={'a','b','c'} for w in L)
        print('N=%d |L|=%d exact arity1/2=PASS mu_ab=%d all fourth powers=YES'% (n,len(L),ab))
    for k in (5,6,7):
        small={'a'*k,'bbbb','cccc','abc','acab'}
        ok,fail=check(small)
        assert ok,fail
        assert sum(c=='a' for c in 'abc')==1 and sum(c=='a' for c in 'acab')==2
        print('Lprime_k k=%d case I exact arity1/2=PASS same b,c counts but unequal a counts'%k)
    print('END')
if __name__=='__main__':main()
```

### 実行ログ（標準出力、そのまま）

```text
SUPPORT INVARIANCE: PASS (set-union identity)
N=4 |L|=38 exact arity1/2=PASS mu_ab=5 all fourth powers=YES
N=5 |L|=51 exact arity1/2=PASS mu_ab=6 all fourth powers=YES
N=6 |L|=66 exact arity1/2=PASS mu_ab=7 all fourth powers=YES
Lprime_k k=5 case I exact arity1/2=PASS same b,c counts but unequal a counts
Lprime_k k=6 case I exact arity1/2=PASS same b,c counts but unequal a counts
Lprime_k k=7 case I exact arity1/2=PASS same b,c counts but unequal a counts
END
```

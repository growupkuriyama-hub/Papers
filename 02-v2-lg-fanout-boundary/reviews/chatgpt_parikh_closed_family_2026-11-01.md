# Parikh 閉包を用いた fan-out 2 半束反例設計：差分保存則、混合文脈による障害、有限候補の検査

**研究日：2026年11月1日**  
**対象正本：** `growupkuriyama-hub/Papers/02-v2-lg-fanout-boundary/main.tex`（取得した Git blob `802b181f4f7e5423496c1f10cf81d317137d4f85`）。併読：`reviews/chatgpt_sl_fanout2_2026-11-01.md`、`archive-v1/revision/deepseek_s2_typewise_search_2026-10-31.md`、`archive-v1/revision/astra_s2_pureword_2026-10-31.md`。  
**規約：** 「証明済み」は以下に数学的証明があるという意味で、外部査読・文献上の新規性の認定ではない。有限検査は証明に用いない。

## 結論の判定表

| 主張 | 判定 | 根拠 |
|---|---|---|
| 観察A「任意の代入可能性が強制する交換は Parikh ベクトルを保存する」 | **反証** | §1、例1.2。共通文脈は交換組の Parikh 一致を意味しない |
| 任意の型付け、任意の arity において、交換前後の Parikh **差分**は交換組の差分に等しい | **証明済み** | §1、命題1.1 |
| 内容型付けでは、交換によって完成語の**内容型**が変化しない | **証明済み** | §1、命題1.1 |
| 固定 Parikh ベクトルの**全順列集合**は、任意の fan-out・任意の型付けで組代入可能 | **証明済み** | §2、命題2.1 |
| 固定 Parikh の稀な内容繊維は、**その中で完結する交換**に対して安全 | **証明済み（条件付き）** | §2、系2.2。混合繊維で観測された交換には別の障害がある |
| 純繊維が厳密に一つの Parikh ベクトルに限られると、異 Parikh の同内容交換が混合側で観測され、純側に適用可能な場合は代入可能性に反する | **証明済み** | §3、定理3.1（混合→純文脈の衝突） |
| 混合側が `c a` と `c aa` を含み、純側に `a` を含む語があれば、純側の `a` 挿入が強制される | **証明済み** | §3、系3.2。有限の固定 Parikh 純繊維とは共存できない |
| **すべて**の `c` 含有語を混合側に採用すると、非空の純繊維は内容型ごとに全語へ飽和する | **証明済み** | §3、定理3.3。`c` を含まない文字集合上で述べる |
| 候補 `R_n ∪ {ca,caa}` は `n=2,3` で `(2,c_Σ)`-代入可能 | **反証（各 n に理論的反例）** | §4、§5。arity 1 が失敗し、arity 2 単独検査は通る |
| 上記候補の arity 2 条件だけは `n=2,3` で成立 | **観察** | §5 の有限全数検査 |
| `R_n` を全順列として保持しつつ、短い混合枝を加える `O(n)` サイズ・多項式厚さの reduced good 2-MCFG で所望の全条件を達成 | **未解決** | §4、§6。文法の構成と全混合文脈の制御が残る |
| 「全順列に閉じた稀な繊維は必ず混合側の加法量が一定になる」 | **未解決（本報告では主張しない）** | §6。今回の障害からは導けない |
| fan-out 2 の反例だけで**すべての** `f≥2` の境界が LG と決まる | **反証（推論として不成立）** | §6。`C_{f,s}` は `f` とともに条件が強くなる |

## 1. T0：Parikh 保存ではなく、Parikh 差分則

有限アルファベット `Σ` の Parikh 写像を `π:Σ*→ℕ^Σ`、内容を `c(w)=supp π(w)` とする。arity `d` の組 `x=(x_1,…,x_d)` に対し `Π(x)=Σ_i π(x_i)` と記す。受理文脈 `E=v_0 □_1 v_1 ⋯ □_d v_d` の固定部分の Parikh 和を `π_fix(E)=Σ_i π(v_i)` とする。内部区切り `v_1,…,v_{d-1}` は非空とする（原稿 `def:class-cmcf`）。

**命題1.1（交換の正確な保存則；任意の有限半群型付け・任意の arity）。** `s^{(d)}(x)=s^{(d)}(y)` と `D_L^{(d)}(x)∩D_L^{(d)}(y)≠∅` とする。任意の許容文脈 `F` について

`π(F[y])−π(F[x]) = Δ(x,y) := Π(y)−Π(x)`。

加えて `s(F[y])=s(F[x])` が両方非空の完成語に対して成立する。特に `s=c_Σ` なら **内容型は一致する**。ただし一般に `Δ(x,y)≠0` である。`L∈C_{f,s}` かつ `d≤f` なら、`F[x]∈L ⇔ F[y]∈L`。

*証明。* Parikh 写像の連接に関する加法性から `π(F[z])=π_fix(F)+Π(z)`。差を取れば第一式。`s` の準同型性と各成分の `s` 値の一致から、固定部分を含む積の型も一致する。内容型付けのときはこれを文字の集合の一致とも読める。最後の同値は `(f,s)`-代入可能性の定義そのものである。□

**例1.2（観察Aへの最小反例）。** `Σ={a,b}`, `L=Σ+`、内容型付け `c_Σ`。この言語は**すべての** fan-out `f` で `(f,c_Σ)`-代入可能である（許容文脈へ非空の成分を入れた結果は常に `Σ+`）。`d=1`、`x=a`、`y=aa`、`E=□_1` とすると `E[a]=a∈L` と `E[aa]=aa∈L` だが `π(a)≠π(aa)`。したがって「共通文脈 ⇒ Parikh 一致」は成り立たない。より一般に、型一致と共通文脈は**同じ Parikh ベクトルであることを要求しない**。

この反例は重要である。Parikh 閉包で救えるのは `Δ=0` の交換だけであり、内容型だけが同じ `Δ≠0` の交換は、稀な繊維の長さを変え得る。

## 2. T1(a)：全順列の稀な繊維は内部交換には強い

**命題2.1（固定 Parikh 層の普遍的代入可能性）。** `v∈ℕ^Σ` とし `R_v={w∈Σ+: π(w)=v}` と置く。任意の有限半群型付け `s` と任意の `f≥1` に対して、`R_v` は `(f,s)`-組代入可能である。`R_v` は有限言語なので、各固定 `v` ごとに fan-out 1 の CFG で生成できる（その文法サイズが `v` の二進表現長について多項式であるという主張では**ない**）。

*証明。* `E[x],E[y]∈R_v` なら両方の Parikh が `v` であるから命題1.1により `Δ(x,y)=0`。ゆえにすべての `F` に対し `π(F[x])=π(F[y])`、すなわち `F[x]∈R_v ⇔ F[y]∈R_v`。型一致さえ不要な強い性質である。□

**系2.2（単一 Parikh 純繊維での局所安全性）。** `A⊆Σ` を非空とし、`L∩c^{-1}(A)=R_v`（`supp(v)=A`）と仮定する。`x,y` が成分ごとに同内容で `Δ(x,y)=0` なら、`c(F[x])=A` となるどの文脈 `F` についても `F[x]∈L ⇔ F[y]∈L`。*証明。* 内容型は同じで、全 Parikh も同じ。よって両方とも `R_v` に入るか、両方とも入らない。□

**候補：** `Σ={a,b,c}`、`N=2^{n-1}` とし

`R_n={w∈{a,b}^{2N}: |w|_a=|w|_b=N}`。

この純繊維は内容 `{a,b}` で、最短長 `μ_{ {a,b} }(R_n)=2N=2^n`、全順列に閉じており、`R_n` 自体は任意の arity で代入可能。しかし `R_n` のみを生成する reduced good 文法では、全成功文の長さが `2^n` なので、少なくとも一つの規則があり、その規則厚さも `2^n` である。**小さい規則厚さには純繊維以外の短い成功文が本質的に必要**である。

## 3. T2：異 Parikh 交換の「混合→純」衝突

次の主張は、前回の二穴再分割補題とは違い **arity 1 だけ**で起こる。構造を細かく選べば、避けるべき混合枝を構成前に排除できる。

**定理3.1（混合文脈からの Parikh 差分漏洩）。** `L` が `(1,c_Σ)`-代入可能、`A⊆Σ` が非空で、`L∩c^{-1}(A)⊆R_v` とする。`x,y∈Σ+` が `c(x)=c(y)`、`Δ=π(y)−π(x)≠0` を満たし、ある許容文脈 `E` で `E[x],E[y]∈L` だとする。このとき、**どんな許容文脈 `F` についても** `c(F[x])=A` なら `F[x]∉L` かつ `F[y]∉L` である。

*証明。* `c(x)=c(y)` から `c(F[x])=c(F[y])=A`。もし `F[x]∈L` なら代入可能性により `F[y]∈L`。純繊維の仮定から両完成語の Parikh はともに `v` だが、命題1.1より差は `Δ≠0`。矛盾。`x,y` を入れ替えて同様に `F[y]∉L`。□

**系3.2（`ca/caa` の禁止）。** `Σ={a,b,c}`、`A={a,b}`、`L∩c^{-1}(A)=R_n` とする。もし `ca,caa∈L` なら `L` は `(1,c_Σ)`-代入可能でない。したがって `(2,c_Σ)`-代入可能でもない。

*証明。* `x=a`、`y=aa` とすると同内容 `{a}`、共通文脈 `E=c□` で `E[x],E[y]∈L`。`w∈R_n` は `a` を含むので `w=F[a]` と書ける。定理3.1から矛盾。直接には `F[aa]∈L` が強制されるが、それは内容 `{a,b}`、Parikh `(N+1,N,0)` であり `R_n` にない。□

**定理3.3（混合側が飽和すると純側も飽和する）。** `Σ=A∪{c}`、`c∉A`、`A` は非空、`L` は `(1,c_Σ)`-代入可能とし、`{w∈Σ+:c∈c_Σ(w)}⊆L` と仮定する。このとき各非空 `B⊆A` について、`L∩c_Σ^{-1}(B)` は **空集合または `c_Σ^{-1}(B)` 全体**である。特に純な内容 `{a,b}` が実現されれば、その最短語長は 2 である。

*証明。* `u,v∈B+` の内容がともに `B` なら `E=c□` により `E[u],E[v]∈L`。従って `D_L^{(1)}(u)=D_L^{(1)}(v)`。もし `u∈L` なら、文脈 `F=□` を適用して `v∈L` を得る。`B` の列挙ではなく、全ての内容等値な語に適用できる。□

**解釈。** 単に混合側の Parikh 値を「多数に散らす」と、それだけで安全になるわけではない。むしろ混合側に**同内容で異 Parikh の組**が同じ文脈で見えるほど、純側の異 Parikh 交換を誘発しやすい。調べるべき量は混合語全体の Parikh 値の種類数ではなく、**純側で実現可能な因子組に作用する混合文脈由来の Parikh 差分の集合**である。

なお、定理3.1は「混合の加法量がすべて一つの値になる」という主張を証明しない。差分が純側に適用できない構造なら、混合側の値がばらついていても矛盾はしない。

## 4. T1(b)–(d)：試作族の成否と、正しい設計仕様

最小試作は

`L_n^trial = R_n ∪ {ca,caa}`、`Σ={a,b,c}`、`n≥1`。

- 純繊維：`L_n^trial∩c^{-1}({a,b})=R_n`、`μ_{ {a,b} }=2^n`。
- 混合繊維：`ca,caa` は長さが異なるので、混合側に少なくとも二種類の Parikh 値がある。
- **不合格：** 系3.2よりすべての `n` で arity 1 の条件を破る。文法サイズ・規則厚さを論じる以前の障害である。
- `R_n` を `O(n)` のランク2・fan-out2 文法で**全順列として**出力し、各規則を長さ `poly(n)` の混合文で使う一般構成は本調査で確立できなかった。形態素の倍増から直ちに全順列の生成可能性を結論しない。

**新しい候補設計原理（未証明の研究方針）。** 混合側 `M_n` について「Parikh 値を複数にする」よりも、混合側が作る *共通受理文脈グラフ* を制御する。頂点は各 arity `d≤2` の成分ごとの内容型を持つ組、辺 `x↔y` はある一つの受理文脈 `E` が `E[x],E[y]∈L` を満たすこと。辺には差分 `Δ(x,y)` を付す。純繊維で実現する組の頂点に到達する `Δ≠0` の辺を禁止する必要がある。厳密には、到達可能性のみではなく、**同じ純文脈 `F` が片側を受理するか**を検査する（定理3.1）。

これを実装可能にする一案は、短い枝に階層別の固有な局所標識を付け、純語内に現れる因子と同内容の短い混合枝が**共通受理文脈を持たない**ようにすること。しかし内容型付けは順序を記録しない上、固定アルファベットのため階層ごとの新文字追加は禁止される。必要な証明は (i) 短い枝の利用可能性、(ii) 純因子と混合因子の同内容共通文脈の不在または `Δ=0`、(iii) 二穴の再分割に対する同じ条件、の三点である。

**補助的な一般定理（Parikh 合同類の安全域）。** `H≤ℤ^Σ` が部分群、`v∈ℤ^Σ` とし、`L=(v+H)∩ℕ^Σ` の Parikh 逆像（空語の扱いは原稿通り別扱い）とする。この言語は任意の `f,s` で組代入可能である。なぜなら共通の受理文脈があれば `Δ(x,y)∈H`、従って任意の文脈で合同類への所属が保存されるからである。これは混合側の Parikh が多数に散る構成を実際に与えるが、**短い枝と指数的な稀な純繊維とを多項式厚さで両立することは示さない**。また、この言語自体が 2-MCFL になるかどうかは個別の `H` ごとに検証を要する。一般に `H` は有限生成だが、Parikh 逆像が常に 2-MCFL とはこの議論から言えない。

## 5. T3：`n=2,3` の有限全数検査

**検査対象** `L_n^trial=R_n∪{ca,caa}`。各 arity `d=1,2` について、全ての受理語の長さ正の非重複 `d` 区間と非空内部ギャップから分布集合を構築し、同型で一つの受理文脈を共有する組の分布を直接比較する。候補となる `x,y` がいずれも受理語に現れない場合は分布が空なので、探索対象から省ける。`F[x]` が受理され `F[y]` が不受理となる文脈が見つかれば反例を出す。有限言語についてはこれで全許容文脈の違いを判定できる（非空分布は必ず受理語内に現れる）。

**実行結果（Python 3、標準ライブラリのみ）：**

```text
n= 2 size= 8 pure shortest= 4
 arity 1 FAIL: ('a',) -> ('aa',) shared ('c', '') witness aabb forced aaabb
 arity 2 PASS (finite exhaustive check)
n= 3 size= 72 pure shortest= 8
 arity 1 FAIL: ('a',) -> ('aa',) shared ('c', '') witness aaaabbbb forced aaaaabbbb
 arity 2 PASS (finite exhaustive check)
```

**位置づけ：** arity 1 の不合格はすでに系3.2で**全 `n` に証明済み**。arity 2 の通過は `n=2,3` に限る**観察**である。「arity 2 だけが通る」ことは `(2,c_Σ)`-代入可能を意味しない。

以下が実行可能な**スクリプト全文**。保存名は `parikh_check.py` とし Windows では `py -3 parikh_check.py`。

```python
from itertools import combinations
from collections import defaultdict


def content(w):
    return frozenset(w)


def observations(L, arity):
    # Maps each observed tuple to all its accepting contexts.
    seen = defaultdict(set)
    for w in sorted(L):
        n = len(w)
        for cuts in combinations(range(n + 1), 2 * arity):
            intervals = [(cuts[2*j], cuts[2*j+1]) for j in range(arity)]
            if any(a == b for a, b in intervals):
                continue
            if any(intervals[j][0] == intervals[j-1][1] for j in range(1,arity)):
                continue
            pieces = tuple(w[a:b] for a,b in intervals)
            gaps = tuple([w[:intervals[0][0]]] +
                         [w[intervals[j][1]:intervals[j+1][0]] for j in range(arity-1)] +
                         [w[intervals[-1][1]:]])
            seen[pieces].add(gaps)
    return seen


def fill(gaps, parts):
    return ''.join(gaps[j] + parts[j] for j in range(len(parts))) + gaps[-1]


def counterexample(L, arity):
    distrib = observations(L, arity)
    grouping = defaultdict(list)
    for parts, contexts in distrib.items():
        typ = tuple(map(content, parts))
        for E in contexts:
            grouping[(typ, E)].append(parts)
    for (_typ, shared), members in grouping.items():
        leader = members[0]
        for other in members[1:]:
            if distrib[leader] != distrib[other]:
                for x,y in ((leader,other),(other,leader)):
                    for F in sorted(distrib[x] - distrib[y]):
                        return x,y,shared,F,fill(F,x),fill(F,y)
    return None


def balanced(k):
    out = set()
    for apos in combinations(range(2*k), k):
        p = set(apos)
        out.add(''.join('a' if i in p else 'b' for i in range(2*k)))
    return out


if __name__ == '__main__':
    for n in (2,3):
        pure = balanced(2**(n-1))
        L = pure | {'ca','caa'}
        print('n=',n,'size=',len(L),'pure shortest=',2**n)
        for d in (1,2):
            z = counterexample(L,d)
            if z is None:
                print(' arity',d,'PASS (finite exhaustive check)')
            else:
                x,y,E,F,word,forced = z
                print(' arity',d,'FAIL:',x,'->',y,'shared',E,
                      'witness',word,'forced',forced)
```

**実装範囲：** `combinations(range(n+1),2d)` が `d` 組の開始・終了カットを厳密に昇順列挙し、非空の穴と穴間の非空固定ギャップを満たす。先頭・末尾の固定部分は空を許容する。`L` は有限で、`observations` に現れない組の分布は空であるため、共通受理文脈を持てない。したがって検査が `PASS` なら、その与えられた有限 `L` の当該 arity 条件は網羅している。ただし無限族への一般化は不可。

## 6. 結論・論文への採用判断・次の問題

1. **直ちに利用可能な数学的成果：** 命題1.1、命題2.1、定理3.1、系3.2、定理3.3 は原稿の定義だけから独立に証明した。特に定理3.1の「同内容・異 Parikh の混合交換は、それが純受理文脈に挿入可能なら衝突する」は、**稀な型の全順列閉包が十分でない理由**を一般化する。これらの原稿への追加は、現在の `op:fanout-two` を解決したという位置づけではなく、障害分析として適切である。
2. **必要な設計変更：** 混合側の Parikh 多様性は条件ではない。混合側の**共通文脈で観測される差分**が純側の許容文脈へ漏れないようにする。これを固定アルファベットで実現しながら、全規則に短い成功文を与えるところが未解決。
3. **特徴データ下界の条件：** もし固定 `Σ`、内容型付け `c_Σ`、fan-out `f`、ランク上限 `r_max≥2` で `L_n∈C_{f,c_Σ}` と、reduced good・fan-out `≤f`・ランク `≤r_max` の `G_n` が構成され、`μ_A(L_n)=2^{Ω(n)}`、`‖G_n‖,θ̄_{G_n}=n^{O(1)}` が証明できれば、原稿 `prop:rare-type` より、`B^{≤r_max}_{f,c_Σ}` と `B_{f,c_Σ}`、さらに**クラス全体に特徴標本を持つ任意の集合駆動作用素**の各特徴標本は、内容型 `A` の少なくとも一語を含み、その総符号長は `μ_A(L_n)+1` 以上となる。この帰結は **必要な族が構成された場合に限る**。本報告の `L_n^trial` にこの下界を適用することはできない。
4. **fan-out に関する論理的注意：** `C_{2,s}` 所属は `C_{f,s}`（`f≥3`）所属を意味しない。したがって fan-out 2 で反例を得れば、`prop:sl-reduction` により**fan-out 2 における** LG 境界は確定するが、それだけで全高ファンアウトへの一般化はできない。一般の各 `f` には所属と下界を別に証明する必要がある。
5. **未解決点：** 提案された `R_n` の多項式サイズ good MCFG 全順列生成、短い混合証人、両 arity の代入可能性を同時に満たす族は見つかっていない。`SL` の多項式データ性も否定・肯定のいずれも未証明である。

### 文献上の位置づけ

- Clark and Eyraud, *Polynomial Identification in the Limit of Substitutable Context-free Languages*, JMLR **8** (2007), 1725–1745: 代入可能性の原型と有限言語 `{a,aa}` の障害を扱う。https://www.jmlr.org/papers/volume8/clark07a/clark07a.pdf
- Seki, Matsumura, Fujii and Kasami, *On Multiple Context-Free Grammars*, Theoretical Computer Science **88** (1991), 191–229: MCFG の形式的基礎（プロジェクト情報源03収録）。
- Kuriyama, 現行 `main.tex`：`def:class-cmcf`、`prop:rare-type`、`lem:typing-monotone`、`prop:sl-reduction`、`op:fanout-two`、先行する二穴移送結果が今回の比較基準。
- 本報告の命題1.1・命題2.1・定理3.1・定理3.3の**文献上の独立した新規性は未確認**。命題1.1は直接の加法性、命題2.1は同じ Parikh の受理条件に由来する初等的事実であり、新しい主定理としての優先権は主張しない。

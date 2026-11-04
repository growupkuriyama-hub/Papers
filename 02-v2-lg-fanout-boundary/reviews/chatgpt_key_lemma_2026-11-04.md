# 場合 II の鍵補題 KL：境界二重文字・同一端点の一般排除と、残る内部二重文字

**研究日**：2026-11-04／三文字の核・系列第十八報  
**対象**：栗山貴之論文 #2、`op:fanout-two`、**場合 II のみ**  
**正本**：`growupkuriyama-hub/Papers/02-v2-lg-fanout-boundary/main.tex`（確認 Git blob `b72cd2ed648f802886f0ab7c60a72f9f40c0864b`）。既報 `chatgpt_alternating_2026-11-04.md`、`claude_straddle_2026-11-04.md`、`claude_cross_core_2026-11-04.md`、`check_claude_case2_blocks_2026-11-04.py`、`check_claude_mixed_roots_2026-11-04.py` を照合した。以下の新結果は独立査読前の研究ノートである。

## 0. 主張別判定

| 主張 | 判定 | 根拠・限界 |
|---|---|---|
| **端点型 KL**：`k≥6d`、SB(F,d)、SB(F²,2d)、SB(F³,3d)、分離二塊の全正配分の下で、`F=Uxx`、`xxU`、`xUx`（それぞれ U が反対の文字を含む）なら受理語に `x⁴` が強制される | **証明済み** | §2–3。13語の基礎証明書を任意の非消去準同型に移送。F および k,d は任意の大きさ |
| **同一端点排除**：場合 II の上記 SB 条件の下で、F の先頭と末尾が同じ文字であることは不可能 | **証明済み** | §3。`F=xUx` への特殊化。`xx` を含まない奇数交代語も排除する |
| 異なる交代根 `(bc)^i(cb)^j` または `(cb)^i(bc)^j` が、上記条件のある一塊 C として現れること | **反証（そのような場合 II の L はない）** | §3。C の両端が一致。条件が C に実際に適用できるときのみ |
| 分岐 (B) の低いラベルについて、異なる交代根の鎖に上の結論を適用すること | **条件付き** | §4。既報の鎖・分離補題とその予算の点検。鎖補題の全依存関係を今回改めて独立証明したわけではない |
| **KL 全体**：F が任意の位置に `bb` または `cc` を含む場合 | **未解決** | §5。内部だけに二重文字を持ち、異なる端点を持つ F は今回の一般型板では覆えない |
| `k=9,d=2` の既報証明書が KL の数値仮定を満たすという解釈 | **反証** | §1。`3d=6>9/2`。今回 `k=6,d=1` と `k=12,d=2` で改めて検査した |
| 内部二重文字 F=`bccbc`、`k=6,d=1` で四乗が強制されること | **有限証明書** | §5。健全な一段推論3段。一般 F への移植ではない |
| 場合 II の分岐 (B) の μ_a の定数付き多項式上界、分岐 (S)、場合 III | **未解決** | §5–6。新しい定量的上界は主張しない |
| 本報の一般型板の刊行文献での新規性 | **未確認** | §6。基礎となる分布代入の考え方は既知 |

## 1. 定義と、従来の実験の数値上の注意

`Σ={a,b,c}`、`c(w)=supp(w)`、`L∈C_{2,c}` とし、`a^k∈L`、`k=μ_a(L)≥5`。場合 II では `b⁴` と `c⁴` のいずれも L の受理語の因子に現れない。F は a を含まず b,c をともに含む語、`d≥1` は損失とする。

`SB(F,d)` は `a^s F a^t∈L` が全ての正整数 `s+t=k−d` で成立すること。今回の前提は `SB(F^j,jd)`（j=1,2,3）と、全ての正整数 `p+q+r=k−2d` に対する `a^p F a^q F a^r∈L` である。`3d≤k/2` は整数に関して **`k≥6d`** と同値。

原稿 `def:tuple-substitutable` の許容文脈を `E=(e₀,…,e_t)`（t=1,2）と書く。t=2 なら **e₁≠ε** である。成分ごとの内容が同じ非空組 X,Y について

`E[X], E[Y], H[X]∈L  ⇒  H[Y]∈L`　（`SUB_t`）

が成立する。両文脈 E,H が許容であることを要する。これは分布等式の直接の帰結であり、この規則だけを使用する。

**数値監査。** 第十六報の `k=9,d=2` は `6d=12>9` なので、そこにある証明書は有効な有限強制の証明書ではあるものの、KL の仮定を満たす例ではない。`a→a^m` の移送でも両辺の比 `6d/k=12/9` は変化しない。そこで今回は **KL を満たす最小の `k=6,d=1`** の新しい証明書を作り、さらに `k=12,d=2` 等へ無限に持ち上げる。

## 2. 基礎証明書：三つの有限型板

### 補題 2.1（長さ6の三基礎証明書）

任意の `L∈C_{2,c}` が、`k=6,d=1` に対する上記の全ての種を含むなら、F に関して次が成り立つ。

* `F=bcc` のとき **`c⁴` を含む語**が強制される（3段）。
* `F=bbc` のとき **`b⁴` を含む語**が強制される（3段）。
* `F=bcb` のとき **`b⁴` を含む語**が強制される（4段）。

**証明。** 各 F の種はちょうど13語：`a⁶`、`a^sF^ja^t`（j=1,2,3、s,t≥1、s+t=6−j）、`a^pFa^qFa^r`（p,q,r≥1、p+q+r=4）。§7 の Python に、3種類すべての一段 `SUB_t` を**探索結果ではなく固定された証明書**として記した。各段で、前提三語が初期13語または先に強制した語であり、二組が同じ内容を持ち、二穴の中央が非空であり、帰結が実際に `H[Y]` であることを独立に `assert` する。

基礎証明書の最終語はそれぞれ

* `bcc`: `abccbcbccccbca` （`cccc` を含む）
* `bbc`: `abbcbbbbccbbca` （`bbbb` を含む）
* `bcb`: `abcbcbbbbcbcba` （`bbbb` を含む）。

従っていずれも指定する四乗を論理的に強制する。これは有限言語についての推測ではなく、**13語を含む任意の `(2,c)`-代入可能 L への有限の含意**である。∎

### 補題 2.2（非消去準同型と左側定数の移送）

`h:{a,b,c}^*→{a,b,c}^*` を非消去準同型で `h(a)=a^d`、`h(b),h(c)∈{b,c}⁺` とし、`q≥0` を整数とする。有限の `SUB_1`,`SUB_2` 証明書中の**全ての語**を

`w ↦ a^q h(w)`

で移すと、これも健全な証明書である。

**証明。** `E=(e₀,…,e_t)` に対して `E'=(a^q h(e₀),h(e₁),…,h(e_t))` とする。`E'[h(X)]=a^q h(E[X])`。t=2 の中央 `h(e₁)` は、非消去性から非空のまま。`c^{(t)}(X)=c^{(t)}(Y)` なら、各成分の文字集合に `h` の文字集合の和集合を作用させるので `c^{(t)}(h(X))=c^{(t)}(h(Y))`。したがって各一段は移送後も前提三語と帰結の関係を正確に保つ。∎

## 3. 主定理：KL の三つの無限部分クラス

### 定理 3.1（端点二重文字と同一端点）

`L∈C_{2,c}` が上述の `SB(F,d),SB(F²,2d),SB(F³,3d)`、全ての分離二塊、および **`k≥6d`** を満たすとする。`x∈{b,c}`、`y` を他方の文字とする。このとき、次のどれかが成立すれば、**L の受理語に x⁴ が因子として現れる**。

1. `F=Uxx` で、`U∈{b,c}⁺` が y を含む。
2. `F=xxU` で、`U∈{b,c}⁺` が y を含む。
3. `F=xUx` で、`U∈{b,c}⁺` が y を含む。

**証明。** `q=k−6d≥0` とおく。場合1では補題2.1の `bcc` の13語証明書に `h(a)=a^d`、`h(b)=U`、`h(c)=x` を作用させる。場合2は `bbc` に `h(b)=x`、`h(c)=U`、場合3は `bcb` に `h(b)=x`、`h(c)=U` を作用させる。全て非消去で、画像は目的の F。基礎の単一塊 j 個の種は `a^(q+ds) F^j a^(dt)`（`s+t=6−j`）となり、a の数が `q+d(6−j)=k−jd`、両端は正である。同様に分離二塊の画像は `a^(q+dp)F a^(dq)F a^(dr)`（元の p,q,r の和は4）で、合計 a の数は `k−2d`、全連正。基礎 `a⁶` は `a^k` に移る。従って**画像の全初期種は今回の仮定に含まれる**。補題2.2で全証明書を移送し、場合1は `h(c⁴)=x⁴`、場合2と3は `h(b⁴)=x⁴` を因子に持つ受理語を得る。∎

**系 3.2（同一端点の禁止）。** 場合 II で同じ仮定を置くと、F は先頭と末尾に同じ文字を持てない。なぜなら両端が x なら `F=xUx` であり、F が両文字を含むので U に他方の文字 y が入るからである。

**系 3.3（根不一致の鎖）。** `i,j≥1` として C=`(bc)^i(cb)^j` または `(cb)^i(bc)^j` が上記 SB・分離条件を持ち、`k≥6δ`（C の損失を δ とする）なら、場合 II の L にそのような C は存在しない。前者は b で始まり b で終わり、後者は c で始まり c で終わるので系3.2による。**この結論は内部の `cc` や `bb` を使わず、同一端点だけで得られる。**

定理3.1は F の長さにも U の内容や複雑さにも依存しない、**一様3～4段の有限型板**である。これは既報 `k=9,d=2` の具体例を言い換えただけではない。

## 4. 分岐 (B) の鎖に戻したときの正確な予算

既報 `claude_straddle` §4.1–4.2 の低い関係ラベルでは `N=25θ³`、`d_X≤ℓ_X≤k/(2N)=k/(50θ³)` である。二つの低いラベル X,Y の鎖 `C=F_XF_Y` の損失は既報の鎖補題に従えば `δ=d_X+d_Y≤k/(25θ³)`。よって

`6δ ≤ 6k/(25θ³) ≤ k`（`θ≥1`）。

C, C², C³ は原子ラベルの長さがそれぞれ2,4,6個であり、`6≤24θ³`。合計損失も `3δ≤3k/(25θ³)<k/2`。従って**既報の分岐 (B) の鎖・分離補題がこれらの鎖に適用できるという前提の下では**、系3.3は異根鎖を完全に排除する。また `F_XF_X` にも同じ予算があり、奇数交代語の同一端点も排除される。

必要な論理を分解しておく。(a) 低い塊と任意の鎖が SB を持つこと、(b) 同じ鎖を a で隔てて二つ置いた全正配分語を得られること、(c) `C³` までの損失が許容範囲であること。**(c) は上の不等式で確認した**。(a),(b) は既報の補題 E・F′、分岐 (B) と命題4.1 の組合せであるが、全補題の独立再証明を本報に含めていない。したがってここで**分岐 (B) の全体解決や全ブロックへの無条件な根統一を宣言しない**。一方、§3 の条件付き含意は既報を使わない完結した定理である。

注意：`δ≤k/6` をある塊 F に適用した後、その **F² に再度 KL を適用するには** `6·(2δ)≤k`、すなわち `δ≤k/12` が必要である。元の `δ≤k/6` をそのまま倍の鎖に流用するのは不正確。今回の低いラベルの具体的な `k/(50θ³)` に戻せばこの不足は生じない。

## 5. 残る内部二重文字と計算の限界

一般の `F=PxxQ` で P,Q の両方が非空、かつ F の**先頭と末尾が異なり**、xx が内部にしかない場合は定理3.1の画像として記述できない。例は `F=bccbc`：先頭 b、末尾 c、内部 cc。`k=6,d=1` の種13語からも有限の健全な一段推論3段によって `aabccbbccccbbccbca` が得られ、`c⁴` が強制された（元の種と各推論の独立検査を実施した）。この3段の証明書（各行は `SUB_t` の `(t,E,X,Y,H)`）は次の通りで、§7 のコード `verify_internal` で各前提を初期種から順次再生する。

```text
1: t=2, E=('aaabccb','c',''), X=('cbc','bca'), Y=('cb','cbca'), H=('aabc','bcc','a')
   -> aabccbbcccbcaa
2: t=2, E=('','c','aa'), X=('aabccbcb','cbc'), Y=('aaabc','bc'), H=('','ccb','cbca')
   -> aaabcccbbccbca
3: t=1, E=('','bcaa'), X=('aaabcc',), Y=('aabccbbccc',), H=('','cbbccbca')
   -> aabccbbccccbbccbca
```

ただし**この現象は任意の内部二重文字への型板を与えていない**。単語の巡回回転で `PxxQ` を `QPxx` にする前に、その回転後の語が同じ損失の SB を持つことを証明しなければならない。単なる文字列の巡回回転は、言語の閉包性ではない。

**KL 全体は未解決**。したがって (ALT) 全体、分岐 (B) の `μ_a` の定数付き多項式上界、分岐 (S)、場合 III を解決したとは言えない。超多項式下界を示す対象族も構成しておらず、どの学習作用素についても下界を主張しない。新しい結果の既刊文献での先取は**未確認**。

**次に絞る一点**：`PxxQ` の両端が異なる場合、`SB(F),SB(F²),SB(F³)` と分離二塊から、`xx` を末尾に持つ適切な共役 `QPxx` の SB（損失 d のまま）を導けるか。導ければ本報の定理3.1の `Uxx` 型に帰着する。導けないなら、この「共役移送」が成立しない最小の具体的な代入可能言語を探す。

## 6. 結了の三点

1. **証明できたこと**：KL の `Uxx`、`xxU`、`xUx` に対する長さ独立の一般証明。特に同一端点、奇数交代塊、異なる交代根の鎖（SB 前提付き）の排除。
2. **止まった場所**：F の内部にしか xx がない異端点型。一般の巡回共役が同じ損失で SB を持つことが示せない。
3. **次の一点**：`F=PxxQ` に対する共役移送補題の証明、またはその代入可能な反例。

## 7. Python 3 標準ライブラリ：証明書全文と実行ログ

次のプログラムは **基礎証明書を固定データとして内蔵**しており、探索を行わない。各前提と型、許容性、帰結を独立再生する。任意長の F・k・d に対する数学的根拠は §2.2 の準同型持上げの証明であって、下の8実例の有限計算ではない。

Windows: `py -3 key_lemma_certificate.py`。すべて Python 3 の標準ライブラリのみ。

```python
#!/usr/bin/env python3
"""Sound finite (1,c)/(2,c) witnesses, lifted by nonerasing morphisms.
Run on Windows: py -3 key_lemma_certificate.py. Standard library only.
"""

BASE = {
    'bcc': [
        (2, ('','c','a'), ('aabc','bcca'), ('abccb','cbcca'), ('','cbcc','')),
        (1, ('','aa'), ('aaabcc',), ('abccbccbcc',), ('','bcca')),
        (1, ('abccb','cbcca'), ('cbcc',), ('ccbc',), ('abccbcbcc','a')),
    ],
    'bbc': [
        (1, ('','aa'), ('aaabbc',), ('abbcbbcbbc',), ('','bbca')),
        (2, ('','b','a'), ('aabbc','bca'), ('abbcb','cbbca'), ('','bbcb','')),
        (1, ('abbc','bcbbca'), ('bbcb',), ('bbbc',), ('abbcb','cbbca')),
    ],
    'bcb': [
        (1, ('','a'), ('aaabcba',), ('abcbaabcb',), ('a','')),
        (2, ('','b','a'), ('aabcb','cba'), ('abc','aabcb'), ('','bcbb','')),
        (2, ('','b','a'), ('aabc','bcba'), ('aabcb','cba'), ('','bbcb','')),
        (1, ('','aabcb'), ('aabcb',), ('abcbcbb',), ('','bbcbcba')),
    ],
}


def fill(context, words):
    assert len(context) == len(words) + 1
    return ''.join(p + w for p, w in zip(context, words)) + context[-1]


def ctype(words):
    return tuple(frozenset(w) for w in words)


def seed_words(k, F, loss):
    assert 6 * loss <= k and loss >= 1 and set(F) == {'b','c'}
    out = {'a' * k}
    for j in (1,2,3):
        out.update('a' * s + F * j + 'a' * (k - j * loss - s)
                   for s in range(1, k-j*loss))
    out.update('a'*p + F + 'a'*q + F + 'a'*(k-2*loss-p-q)
               for p in range(1,k-2*loss)
               for q in range(1,k-2*loss-p))
    return out


def apply_h(s, table):
    return ''.join(table[ch] for ch in s)


def validate(root, table, k, loss, expected_x):
    assert 6*loss <= k
    F=apply_h(root,table)
    assert 'a' not in F and set(F)=={'b','c'}
    pad='a'*(k-6*loss)
    tr=lambda s: pad+apply_h(s,table)
    map_h=lambda s: apply_h(s,table)
    known=seed_words(k,F,loss)
    assert tr('a'*6) in known
    target=None
    for i,(d,E,X,Y,C) in enumerate(BASE[root],1):
        e=(pad+map_h(E[0]),)+tuple(map_h(s) for s in E[1:])
        z=(pad+map_h(C[0]),)+tuple(map_h(s) for s in C[1:])
        x=tuple(map_h(s) for s in X)
        y=tuple(map_h(s) for s in Y)
        assert d in (1,2) and len(e)==len(z)==d+1
        assert all(x) and all(y)
        assert ctype(x)==ctype(y)
        if d==2: assert e[1] and z[1]
        premises=(fill(e,x),fill(e,y),fill(z,x))
        assert set(premises)<=known,(root,i,premises-set(known))
        goal=fill(z,y)
        assert goal not in known,(root,i,goal)
        known.add(goal)
        target=goal
    assert expected_x*4 in target,(root,target,expected_x)
    print('case=%-11s k=%2d d=%d forced=%s steps=%d' %
          (F,k,loss,expected_x,len(BASE[root])))


INTERNAL = [
    (2, ('aaabccb','c',''), ('cbc','bca'), ('cb','cbca'), ('aabc','bcc','a')),
    (2, ('','c','aa'), ('aabccbcb','cbc'), ('aaabc','bc'), ('','ccb','cbca')),
    (1, ('','bcaa'), ('aaabcc',), ('aabccbbccc',), ('','cbbccbca')),
]


def verify_internal():
    known=seed_words(6,'bccbc',1)
    for i,(d,E,x,y,F) in enumerate(INTERNAL,1):
        assert len(E)==len(F)==d+1
        assert ctype(x)==ctype(y)
        if d==2: assert E[1] and F[1]
        assert {fill(E,x),fill(E,y),fill(F,x)}<=known
        w=fill(F,y)
        assert w not in known
        known.add(w)
        print('internal bccbc step=%d word=%s' % (i,w))
    assert 'cccc' in w
    print('INTERNAL FINITE CERTIFICATE VERIFIED')


def main():
    tests=[('bcc',{'a':'a','b':'b','c':'c'},6,1,'c'),
           ('bbc',{'a':'a','b':'b','c':'c'},6,1,'b'),
           ('bcb',{'a':'a','b':'b','c':'c'},6,1,'b'),
           ('bcc',{'a':'aa','b':'bcb','c':'c'},12,2,'c'),
           ('bbc',{'a':'aa','b':'b','c':'cbbc'},13,2,'b'),
           ('bcb',{'a':'aaa','b':'b','c':'ccbcbcc'},20,3,'b'),
           ('bcb',{'a':'aa','b':'b','c':'cc'},12,2,'b'),
           ('bcc',{'a':'aa','b':'cb','c':'b'},12,2,'b')]
    for test in tests: validate(*test)
    print('ALL CERTIFICATES VERIFIED')
    verify_internal()

if __name__=='__main__': main()

```

**実測した標準出力（そのまま）**

```text
case=bcc         k= 6 d=1 forced=c steps=3
case=bbc         k= 6 d=1 forced=b steps=3
case=bcb         k= 6 d=1 forced=b steps=4
case=bcbcc       k=12 d=2 forced=c steps=3
case=bbcbbc      k=13 d=2 forced=b steps=3
case=bccbcbccb   k=20 d=3 forced=b steps=4
case=bccb        k=12 d=2 forced=b steps=4
case=cbbb        k=12 d=2 forced=b steps=3
ALL CERTIFICATES VERIFIED
internal bccbc step=1 word=aabccbbcccbcaa
internal bccbc step=2 word=aaabcccbbccbca
internal bccbc step=3 word=aabccbbccccbbccbca
INTERNAL FINITE CERTIFICATE VERIFIED
```

**参照**：原稿 `def:tuple-substitutable`, `app:singleton`; 既報 `reviews/chatgpt_alternating_2026-11-04.md`、`reviews/claude_straddle_2026-11-04.md`、`reviews/claude_cross_core_2026-11-04.md`。公開論文の標準的な背景として Yoshinaka (2011, *Theoretical Computer Science* 412:1821–1831) ほかを参照。刊行文献との定理単位の先取関係は未確認。

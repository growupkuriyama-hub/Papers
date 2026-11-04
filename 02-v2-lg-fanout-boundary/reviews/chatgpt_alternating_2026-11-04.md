# 場合 II：交代塊予想 (ALT) の部分定理と、非交代塊に対する再生可能な強制証明書

**研究日** 2026-11-04／系列第十六報  
**範囲** 三文字 `Σ={a,b,c}`、内容型付け、`L∈C_{2,c}`、`a^k∈L` で k≥5、かつ **b⁴・c⁴ を含む受理語が存在しない場合 II** のみ。  
**正本** GitHub `growupkuriyama-hub/Papers/02-v2-lg-fanout-boundary/main.tex`、blob `b72cd2ed648f802886f0ab7c60a72f9f40c0864b`。先行ノート `claude_straddle_2026-11-04.md`、`claude_cross_core_2026-11-04.md`、`chatgpt_case2_2026-11-04.md`、原実験 `check_claude_case2_blocks_2026-11-04.py` を照合した。**以下の証明はこの報告内の証明であって査読済みではない。**

## 0. 判定表

| 主張 | 判定 | 根拠・限界 |
|---|---|---|
| 場合 II の非交代塊を一般に排除する (ALT) 第一節 | **未解決** | §4。一般の F に対する x⁴ 強制の帰納補題は得られなかった |
| 全ての関係する塊の根が bc または cb の**一方に統一**される (ALT) 第二節 | **未解決** | §4。`bc·cb=bccb` 自体に4連はなく、根の不一致だけでは矛盾しない |
| **Parikh 飽和の場合 II** に限り、F³ があるなら `F∈{bc,cb}` | **証明済み／容易な追加仮定の特別な場合** | §2。一般の (ALT) より強い結論だが、飽和の仮定を外せない |
| `F=bcc,bbc,bcb` の損失2・k=9 の明示的な全配分種は場合 II の言語に同時に入らない | **証明済み／有限証明書** | §3、§5。各例について arity 1,2 の健全な一段推論だけを順に再生し b⁴/c⁴ を得た |
| 同じ証明書を `a→a^m` で写した種（k=9m、損失2m、m≥1）も場合 II には同時に入らない | **証明済み／証明書の単純な持ち上げ** | §3。新しい一般的 ALT の証明ではない |
| `F=bc,bcbc` の有限の長さ制限付き閉包がそれぞれ55語、165語で停止した | **観察** | §5。無限言語の (2,c) 代入可能性も (ALT) も証明しない |
| (ALT) を仮定した場合 II・分岐 (B) の `μ_a` の定数付き多項式上界 | **未証明** | §4。損失の線形化は見通しにとどまり、例外計数を再証明していない |
| 場合 II の分岐 (S)、場合 III への拡張 | **対象外／未解決** | §4。場合 III に結果を広げない |
| 文献上の新規性 | **未確認** | §6。証明書は既存の実験と同じ現象の独立再実装 |

## 1. 準備と健全な一段規則

原稿 `def:tuple-substitutable` では arity 1,2 の非空成分について、二穴の場合には中央に少なくとも一文字の固定区間がある文脈だけを認める。文脈を `E=(e_0,...,e_d)` と書き、`E[x]` をその組への穴埋めとする。`c^{(d)}(x)=c^{(d)}(y)` かつ

`E[x], E[y], F[x] ∈ L`

なら、両組が E を共有するので分布等式により

`F[y] ∈ L`。

この単一の推論規則 **(SUB_d)** のみを使う。d=1,2 の場合は E,F のどちらも許容文脈でなくてはならない。**固定の上限長以下で新しい語を発見しないこと**は否定結果を与えない。一方、得られた b⁴/c⁴ を含む語は、有限個の前提から全ての `(2,c)`-代入可能な上位言語に強制される。

今回の部分結果では原稿の定理 I や、先行報告の補題 F′・E₂・T・N・P*・Q を黒箱として使わない。したがって、それらの証明を本報で再検証したという主張もしない。既存の報告にある (R) などを援用して多項式上界を無証明に宣言することは避ける。

## 2. Parikh 飽和した場合 II の塊は単位交代語に限る

**補題 2.1。** L が Parikh-saturated で、b⁴ も c⁴ も受理語の因子に現れないとする。このとき任意の w∈L について `|w|_b≤3` および `|w|_c≤3` が成立する。

**証明。** もし `|w|_b≥4` なら w と同じ Parikh ベクトルの語のうち全ての b を連続して先頭に置いたものも L に属する。その語は b⁴ を含み矛盾する。c も同様。∎

**系 2.2。** 補題 2.1 の仮定下で、b と c の両方を含む a-free 語 F について、ある受理語の中に因子 F³ があれば `F∈{bc,cb}` である。

**証明。** `3|F|_b≤3`、`3|F|_c≤3` なので両出現回数は1。従って F は bc または cb。∎

これは **追加の Parikh 飽和という強い仮定**を使っている。一般の場合 II の定理にはならない。更に、bc と cb の混在自体を禁じるものでもない。両方とも F³ を満たす場合の根統一はここからは出ていない。

## 3. 三種の非交代塊に対する有限の強制排除

k=9、損失 `λ=2` とし、a を含まない塊 u に対して前提集合 `S(u)` を以下のように取る：

- `a^9`。
- `j=1,2,3`、`1≤s≤9−2j−1` に対する `a^s u^j a^(9−2j−s)`。
- `p,q≥1, p+q≤9−4−1` に対する `a^p u a^q u a^(9−4−p−q)`。

全ての a の連は正、各 u で前提は19語である。原実験と同じ形の種だが、以下は **共有文脈からの直接の一段規則を記録する独立実装**である。推移的な分布の同値類にまとめた推論を省略していない。導出した語には、その時点までに存在した三つの根拠語 `E[x],E[y],F[x]` が必ず付属する。

実行結果は、u=bcc では9段、u=bbc では6段、u=bcb では4段の証明書を抽出し、それぞれ受理語に c⁴ または b⁴ が出現した。具体的な語と各推論文脈は §5 の標準出力の `CERT` 行に表示した。コードは証明書を**種から再帰的に組み立て、先行する根拠語が既に存在することを assert で検査**する。よってこれは探索の成否についての観察だけでなく、提示された有限の前提に対する具体的な論理的排除である。

**系 3.1（a 連の一様拡大）。** 任意の m≥1 について、`a→a^m, b→b, c→c` という非消去モノイド準同型写像を上の証明書の全ての文脈・組・受理語に適用しても、共通文脈と成分内容の一致、中央固定部分の非空性が保存される。従って `a^(9m)` と、損失 `2m` における上の種の写像を全て含む場合 II の L は存在しない。一般の k,λ には拡張していない。

## 4. 全体の (ALT) と μ_a 上界に至らない理由

(1) 上の証明書は `bcc`,`bbc`,`bcb` の指定 k,λ と全配分の種に対して有効である。しかし `F` の任意長・任意周期、任意の k と λ、あるいは (ALT) に記された最小限の F³ と二塊の存在だけから同様の強制が得られるとは証明できていない。証明書は F の中の連をずらす二穴現象の実例だが、一般の F を短い禁止パターンに還元するための補題がない。

(2) 仮に全ての関係塊が `(bc)^j` または `(cb)^j` と分かっても、それらの根が全て同じであることは別途必要となる。`(bc)(cb)=bccb`、`(cb)(bc)=cbbc` は4連を持たないので、「異根の境界では直ちに b⁴/c⁴」という論証は誤り。塊が持つ **別の共有文脈**を構成しなければならない。

(3) 一根だけになることを仮定すれば、同根の結合 `u^i u^j=u^(i+j)` により、骨格に対応する指数の加法性を期待できる。ただし、それと先行報告の (R)・定理 C から直ちに **定数付きの全分岐多項式上界**が出るとは今回検証していない。低いラベルの例外、鎖の独立性、rank r と θ の明示依存を点検する作業が残る。

(4) 分岐 (S) と場合 III は今回証明していない。場合 III に結果を拡張したとは書かない。反例族 `G_n` も構成しておらず、特徴標本の新しい下界を述べない。

**次に絞る一点**：`F` が内部に `bb` または `cc` を持つか、長さが奇数の交代語（例 `bcb`）である場合に、任意の正の a 配分による三連 `F³` と二分離 `F a^q F` から、**長さに依らない有限個の (SUB_2) 型板**で x⁴ を導く局所禁止補題を証明すること。まず周期ずらしが作る二穴組の型の一致と中央文脈の非空性を変数つきで定式化する。

## 5. Python 3 標準ライブラリによる再実験と証明書

次を `py -3 check_alt.py` で実行した。プログラムの `maxlen=13` は **新たに導く語にだけ適用**し、前提語は全て含める。探索の各一段に対し、二穴なら E,F 両方の中央固定部分が非空であること、共通成分内容の一致、前提三語が存在することを assert で検査する。終了後、実際に見つかった各禁止語から必要な導出だけを再帰的に抜き出して検査し直す。`FIXPOINT` はあくまで有限上限内・指定反復回数内の観察である。


```python
#!/usr/bin/env python3
"""Sound direct (1,c)/(2,c) closure; Python 3 standard library only."""
from collections import defaultdict


def occ(w, d):
    n = len(w)
    if d == 1:
        for i in range(n):
            for j in range(i + 1, n + 1):
                yield (w[i:j],), (w[:i], w[j:])
    else:
        for i in range(n):
            for j in range(i + 1, n):
                for p in range(j + 1, n):
                    for q in range(p + 1, n + 1):
                        yield (w[i:j], w[p:q]), (w[:i], w[j:p], w[q:])


def fill(E, xs):
    return ''.join(u + x for u, x in zip(E, xs)) + E[-1]


def ty(xs):
    return tuple(''.join(sorted(set(x))) for x in xs)


def seeds(k, u, loss):
    words = {'a' * k}
    for j in (1, 2, 3):
        words.update('a' * s + u * j + 'a' * (k - j * loss - s)
                     for s in range(1, k - j * loss))
    words.update('a' * p + u + 'a' * q + u +
                 'a' * (k - 2 * loss - p - q)
                 for p in range(1, k - 2 * loss)
                 for q in range(1, k - 2 * loss - p))
    return words


def closure(seed, maxlen=13, rounds=4):
    known = set(seed)
    provenance = {}
    for rnd in range(1, rounds + 1):
        added = {}
        for d in (1, 2):
            D = defaultdict(set)
            by_context = defaultdict(set)
            for w in sorted(known):
                for xs, E in occ(w, d):
                    D[xs].add(E)
                    by_context[(ty(xs), E)].add(xs)
            for (_, E), xs_set in sorted(by_context.items()):
                xs_list = sorted(xs_set)
                for x in xs_list:
                    for y in xs_list:
                        if x == y:
                            continue
                        for F in sorted(D[x] - D[y]):
                            w = fill(F, y)
                            if len(w) > maxlen or w in known or w in added:
                                continue
                            assert ty(x) == ty(y)
                            assert fill(E, x) in known
                            assert fill(E, y) in known
                            assert fill(F, x) in known
                            assert len(E) == d + 1 and len(F) == d + 1
                            if d == 2:
                                assert E[1] and F[1]
                            added[w] = (d, E, x, y, F)
                            if 'bbbb' in w or 'cccc' in w:
                                provenance.update(added)
                                known.update(added)
                                print('block: forced at round', rnd,
                                      'seeds', len(seed), 'word', w)
                                return known, provenance, w
        if not added:
            print('block: fixpoint', len(known), 'words')
            return known, provenance, None
        known.update(added)
        provenance.update(added)
        print('block: round', rnd, 'added', len(added), 'total', len(known))
    print('block: round limit', len(known))
    return known, provenance, None


def verify_certificate(goal, seed, provenance):
    ordered, used = [], set()

    def visit(w):
        if w in seed:
            return
        if w in used:
            return
        d, E, x, y, F = provenance[w]
        for v in (fill(E, x), fill(E, y), fill(F, x)):
            visit(v)
        used.add(w)
        ordered.append((w, d, E, x, y, F))

    visit(goal)
    certified = set(seed)
    for i, (w, d, E, x, y, F) in enumerate(ordered, 1):
        assert ty(x) == ty(y)
        assert len(E) == len(F) == d + 1
        assert d == 1 or (E[1] and F[1])
        assert all(fill(C, t) in certified
                   for C, t in ((E, x), (E, y), (F, x)))
        assert fill(F, y) == w
        certified.add(w)
        print('CERT', i, 'd=', d, 'E=', E, 'x=', x,
              'y=', y, 'F=', F, '=>', w)
    print('certificate steps:', len(ordered))


def main():
    for u in ('bcc', 'bbc', 'bcb', 'bc', 'bcbc'):
        print('\nROOT', u)
        seed = seeds(9, u, 2)
        words, provenance, forced = closure(seed)
        assert not any(set(w) == {'a'} and len(w) < 9 for w in words)
        if u in ('bcc', 'bbc', 'bcb'):
            assert forced is not None
            verify_certificate(forced, seed, provenance)
        else:
            assert forced is None


if __name__ == '__main__':
    main()
```

**実際の標準出力（改変なし）**

```text

ROOT bcc
block: round 1 added 28 total 47
block: round 2 added 142 total 189
block: forced at round 3 seeds 19 word abcbccccbcbcc
CERT 1 d= 1 E= ('', 'aaa') x= ('aaaabcc',) y= ('abccbcca',) F= ('', 'bcca') => abccbccabcca
CERT 2 d= 2 E= ('', 'c', 'a') x= ('aaabc', 'bcca') y= ('abccb', 'cbcca') F= ('', 'ca', '') => abccbcacbcca
CERT 3 d= 1 E= ('', 'a') x= ('aaaaabcca',) y= ('aabccaabcc',) F= ('a', '') => aaabccaabcc
CERT 4 d= 2 E= ('abcc', 'a', 'a') x= ('bcc', 'bcc') y= ('bc', 'cbcc') F= ('aaa', 'aa', '') => aaabcaacbcc
CERT 5 d= 1 E= ('a', 'aa') x= ('aaabcca',) y= ('bccaabcc',) F= ('abcc', '') => abccbccaabcc
CERT 6 d= 2 E= ('abcc', 'a', 'a') x= ('bcc', 'bcc') y= ('bc', 'cbcc') F= ('a', 'bccaa', '') => abcbccaacbcc
CERT 7 d= 1 E= ('', 'a') x= ('aaaaabcca',) y= ('aabccbccbcc',) F= ('a', '') => aaabccbccbcc
CERT 8 d= 2 E= ('abcc', 'a', 'a') x= ('bc', 'cbcc') y= ('bcc', 'bcc') F= ('aaa', 'cbc', '') => aaabcccbcbcc
CERT 9 d= 1 E= ('', 'aacbcc') x= ('aaabc',) y= ('abcbcc',) F= ('', 'ccbcbcc') => abcbccccbcbcc
certificate steps: 9

ROOT bbc
block: round 1 added 28 total 47
block: round 2 added 142 total 189
block: forced at round 3 seeds 19 word abbcbcbbbbcbc
CERT 1 d= 2 E= ('', 'b', 'a') x= ('aaabbc', 'bca') y= ('abbcb', 'cbbca') F= ('', 'ab', '') => abbcbabcbbca
CERT 2 d= 1 E= ('', 'aaa') x= ('aaaabbc',) y= ('abbcabbc',) F= ('', 'bbca') => abbcabbcbbca
CERT 3 d= 2 E= ('', 'a', 'cbbca') x= ('abbcb', 'b') y= ('abbc', 'bb') F= ('', 'bc', 'bcaa') => abbcbcbbbcaa
CERT 4 d= 1 E= ('', 'a') x= ('aaaaabbca',) y= ('aabbcbbcbbc',) F= ('a', '') => aaabbcbbcbbc
CERT 5 d= 2 E= ('', 'a', 'cbbca') x= ('abbc', 'bb') y= ('abbcb', 'b') F= ('aa', 'bbc', 'c') => aaabbcbbbcbc
CERT 6 d= 1 E= ('', 'bbcaa') x= ('aaabbc',) y= ('abbcbcb',) F= ('', 'bbbcbc') => abbcbcbbbbcbc
certificate steps: 6

ROOT bcb
block: round 1 added 73 total 92
block: forced at round 2 seeds 19 word aabcbbbbccba
CERT 1 d= 2 E= ('', 'b', 'aa') x= ('aabcb', 'cba') y= ('aabc', 'abcb') F= ('', 'bcbb', '') => aabcbcbbabcb
CERT 2 d= 1 E= ('a', 'aaa') x= ('aabcba',) y= ('bcbabcb',) F= ('aabcb', '') => aabcbbcbabcb
CERT 3 d= 2 E= ('', 'b', 'aa') x= ('aabc', 'bcba') y= ('aabcb', 'cba') F= ('', 'bbcb', '') => aabcbbbcbcba
CERT 4 d= 1 E= ('aabc', 'babcb') x= ('bcb',) y= ('bbc',) F= ('aabcbb', 'cba') => aabcbbbbccba
certificate steps: 4

ROOT bc
block: round 1 added 27 total 46
block: round 2 added 9 total 55
block: fixpoint 55 words

ROOT bcbc
block: round 1 added 57 total 76
block: round 2 added 89 total 165
block: fixpoint 165 words
```

## 6. 文献・結論

原稿 `app:singleton` は二文字の単語言語について arity 2 の構造的制約と禁止語の証明書を与えている。ただし **その singleton 分類を一般の三文字場合 II に無条件で適用してはいない**。`lem:app-two-runs` は四乗が現れるときの連交換を使うが、今回 b⁴,c⁴ は禁止されているため、そのまま b/c に適用できない。今回の直接証明書は、原実験 `reviews/check_claude_case2_blocks_2026-11-04.py` の観察の独立な再生に相当する。新規性は**未確認**。

**証明できたこと**：Parikh 飽和に限れば F³ の塊は bc または cb の一回ずつしか許されない。一般の `(2,c)` 代入可能性の下でも、明記した19語の全配分種を含む言語について `bcc`・`bbc`・`bcb` の三塊を排除する有限の証明書を得た。

**止まった場所**：任意の F・任意の予算への一般化と、両根の混在を排除する二穴交換の構成。故に (ALT) と場合 II の μ_a 多項式上界は未解決。

**次の一点**：三連 F³ の周期内部の二穴ずらしを、F の連の局所構造にしか依存しないテンプレートへ変換すること。**場合 II の普遍定理・反例族・新しい特徴標本下界は今回得ていない。**

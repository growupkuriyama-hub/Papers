# 単語言語の二穴代入可能性の完全な二文字分類と高ファンアウト・多文字への帰結

**研究日:** 2026-11-02　**対象:** 栗山貴之 #2 論文 `02-v2-lg-fanout-boundary/main.tex`　**基準ソース:** Git blob `f238b751ea60bfa48a09cef5dd25b8b5327944c0`　**検証:** Python 3 標準ライブラリの完全列挙＋手書きの任意長証明。

「証明済み」は本文の論証と完全列挙証明書を意味し、外部査読・文献的新規性を意味しない。実験と一般証明を分離する。

## 0. 判定一覧

| ID | 主張 | 判定 | 根拠 |
|---|---|---|---|
| S1 | 二文字・同じ冪等型の単語言語 `{W}` は、`|W|≥7` なら **5形**（文字交換・反転込み）と同値 | **証明済み** | §2–§4：48の有限証明書、長さ7の10状態遷移、任意 arity の十分性 |
| S1s | `|W|≤6` の全ての該当語の列挙 | **証明済み（有限検査）** | §3、§8：長さ別 `2,4,8,16,24,16`、違反は長さ5の2軌道・6の14軌道 |
| S2 | 二文字の単語言語について、`(2,trivial)`-substitutability なら **すべての arity** で成立 | **証明済み** | §4：5形の直接証明、短語の arity≥3 の完全検査 |
| S3a | 3文字以上でも、**異なる文字を各1回含む周期**を繰り返す語は全 arity で成立 | **証明済み（十分条件）** | §5.1；例 `(abc)^k` |
| S3b | 両端に別の文字を置いた `p x^n q` は全 arity で成立（`p,q≠x`） | **証明済み（十分条件）** | §5.2 |
| S3c | `k≥3` における一般の全語の構造分類 | **未解決** | §5.3；3文字の有限分布は観察のみ |
| S3d | `s(a)=s(b)=g`, `g²=e≠g` とすると、`W=aaabbaba` は長さ8・型 `e` で5形ではないが `{W}` は全 arity で代入可能 | **証明済み（有限完全列挙）** | §6、§8 |
| S4 | 型 `e` の唯一語 `W∈{a,b}⁺`（`s(a)=s(b)=e=e²`）には S1 が適用される。さらに単語 `{W}` は全 arity で代入可能 | **証明済み** | §7.1、前回報告補題2.1 |
| S4b | 5形の希少語だけから `op:fanout-two` の肯定・否定、あるいは `|W|≤poly(‖G‖,θ̄)` | **未解決** | §7.2–7.4 |
| P | 本分類の文献上の初出性 | **未確認** | §9 |

**重要な結論:** この二文字の単語言語問題では、**fan-out 2 以上に上げても条件は変わらない**。ただし「単語言語」あるいは「指定型に語がただ一つ」という条件を外した一般の `(f,s)`-言語には、この結論をそのまま使えない。

## 1. 定義・参照・二つの遺伝補題

原稿 §2–§4 の定義に従う。許容 `d`-文脈とは

\[
 E=v_0\Box_1v_1\cdots v_{d-1}\Box_dv_d,
 \qquad v_0,v_d\in\Sigma^*,\quad v_i\in\Sigma^+\ (1\le i<d).
\]

穴に入れる各語も **非空**。`E[\mathbf x]` は置換結果、`D_L^{(d)}(\mathbf x)` はその言語に属する置換結果を与える許容文脈の集合。`(f,s)`-代入可能性は **全 `1≤d≤f`** と、**成分ごとの型一致**についての条件である。

以下、二文字アルファベット `{a,b}` 上で `s(a)=s(b)=e=e²` とすれば、全ての非空語の型は `e`。したがって `{W}` に対する `(f,s)`-条件は、**自明な型付け**での条件と一致する。

### 補題1.1（単語言語は1穴で常に代入可能）【証明済み】

`{W}` の場合、`E[x]=E[y]=W` を満たす1穴の `E=p\Box q` と非空 `x,y` は自由モノイドの左右消去により `x=y` を満たす。よって型付けに関係なく arity 1 は成立する。

### 補題1.2（唯一型剛性と因子遺伝）【前回の結果を確認】

`L∈C_{f,s}`、`L∩s^{-1}(m)={W}` とする。`E[\mathbf x]=E[\mathbf y]=F[\mathbf x]=W`、`s^{(d)}(\mathbf x)=s^{(d)}(\mathbf y)`、`E,F` 許容なら、代入可能性により `F[\mathbf y]∈L`。半群準同型性と成分型一致から `s(F[\mathbf y])=s(W)=m` なので、`F[\mathbf y]=W`。これにより `{W}` も全 arity で代入可能である。

さらに、長さ `k` の因子 `v` に四つ組の証明書 `E,\mathbf x,\mathbf y,F` があり、`E[\mathbf x]=E[\mathbf y]=F[\mathbf x]=v`、`F[\mathbf y]≠v` なら、任意の `W=pvq` において `pEq,pFq` を使えば同じ違反になる。**中間区切りの非空性は保たれる**。したがって、単語言語が合格なら全ての因子も合格する。

逆にこれらの証明書だけで、`{W}` が不合格であることを形式的に確認できる。以下、`E=u;t;v` は `u\Box_1t\Box_2v`（**`t≠ε`**）、`\mathbf x=x_1;x_2` を表す。

## 2. 主定理：全長の二文字分類（S1）

### 定理2.1【証明済み】

`W∈{a,b}⁺`, `n=|W|≥7` とする。次の三条件は同値。

1. `{W}` が自明型付けで `(2,s)`-tuple-substitutable。
2. `{W}` が自明型付けで **すべての arity `d≥1`** について tuple-substitutable。
3. 異なる文字 `x,y∈{a,b}` について、反転・文字交換を含め、次のいずれか：
   \[
   \boxed{x^n,\quad x^{n-1}y,\quad yx^{n-2}y,\quad (xy)^k\ (n=2k),\quad (xy)^kx\ (n=2k+1).}
   \]

`x^{n-1}y` の **反転 `yx^{n-1}` も含む**。`yx^{n-2}y` は両端が同じ例外文字。交互形は長さに応じて書き分けているので、固定 `n` の同型類の数は実質4（交互形は偶奇で別表記）だが、依頼文の**5表示**を保持する。

**必要性の証明。** §3で長さ7の `{a,b}^7` **全128語**に対し、48個の軌道代表証明書のうち長さ7用32個から全118不合格を排除し、合格10語が次と一致することを完全検査する：

```
aaaaaaa  aaaaaab  abababa  abbbbba  abbbbbb
bbbbbbb  bbbbbba  bababab              baaaaab  baaaaaa
```

すなわち `a` で始まる代表が

```
aaaaaaa, aaaaaab, abababa, abbbbba, abbbbbb
```

で、残りは文字交換。長さ7の全ての因子も合格でなければならない（補題1.2）。そこで、長さ7の窓 `v` の右に文字 `z` を付けて次の窓 `v[1:]z` も合格するかを調べる。全10状態・全20候補の遷移は次の通り（`-` は合法な後続なし）：

| 長さ7窓 | 追加できる次の文字 |
|---|---|
| `aaaaaaa` | `a`,`b` |
| `aaaaaab` | - |
| `abababa` | `b` |
| `abbbbba` | - |
| `abbbbbb` | `a`,`b` |
| `baaaaaa` | `a`,`b` |
| `baaaaab` | - |
| `bababab` | `a` |
| `bbbbbba` | - |
| `bbbbbbb` | `a`,`b` |

これはすべての候補を尽くす。周期2の2状態は交互に遷移する。`a^7→a^7` で何度か進んでから `a^6b` に入れば `a^{n-1}b` で終わる。`ba^6` から `a^7` に入れば `ba^{n-1}` で終わり、最後に `a^6b` に入れば `ba^{n-2}b` で終わる。両者の文字交換も同様。その他の状態は終端である。これで任意の長さにおいて5表示以外は不可能と示された。

**長さ8の独立チェック。** 8文字語256個中、両方の7文字窓が上表の10語に含まれるものはちょうど10語。完全な8文字の二穴判定でも合格は同じ10語である。よって8文字から新しい例外はなく、8文字の不合格246語すべては7文字の不合格因子の証明書を左右に埋め込むことで処理される。有限チェックは§8のプログラムで実行し、無限長の部分は上の**窓遷移の帰納法**で示した。

**十分性**は§4にて、`d` を任意にして直接証明する。□

## 3. 短語 `|W|≤6` の完全分類と反例証明書

二文字の各語とその文字交換をまとめるため、以下では **`a` から始まる合格語をすべて**掲げる。`b` から始まる合格語は、一律に `a↔b` を施して得る。

| `|W|` | `a` 始まりの全合格語 | 全合格数 |
|---:|---|---:|
| 1 | `a` | 2 |
| 2 | `aa`, `ab` | 4 |
| 3 | `aaa`, `aab`, `aba`, `abb` | 8 |
| 4 | `aaaa`, `aaab`, `aaba`, `aabb`, `abaa`, `abab`, `abba`, `abbb` | 16 |
| 5 | `aaaaa`, `aaaab`, `aaaba`, `aabaa`, `aabab`, `abaaa`, `abaab`, `ababa`, `ababb`, `abbab`, `abbba`, `abbbb` | 24 |
| 6 | `aaaaaa`, `aaaaab`, `aabaab`, `abaaba`, `ababab`, `abbabb`, `abbbba`, `abbbbb` | 16 |

`d=1` は補題1.1、長さ6以下で `d≥4` では非空の穴とその間の非空区切りに **少なくとも `2d−1≥7` 文字**必要で受理文脈が存在しない。`d=3` が可能な長さ5・6についても、合格したすべての語を全出現列挙し、**追加の違反はゼロ**だった。よって長さ6以下でも「2穴合格 ⇒ 全 arity 合格」が成立する。

### 表3.1：長さ5・6・7の全不合格を証明する48軌道の `(E,x,y,F)`

各行は **`E[x]=E[y]=F[x]=W` かつ `F[y]≠W`** を満たし、`E,F` の中間区切りは非空、穴成分はすべて非空。文字交換・反転の4要素からなる群で軌道を取る。1軌道の要素数は2または4で、全行の軌道和は **長さ5で8語、6で48語、7で118語**。合格数と足すとそれぞれ `2^5,2^6,2^7` になる。

| 長さ | W（軌道代表） | E (`左;中;右`) | x (`1;2`) | y (`1;2`) | F (`左;中;右`) |
|---:|---|---|---|---|---|
| 5 | `aaabb` | `;a;b` | `aa;b` | `a;ab` | `;ab;` |
| 5 | `aabba` | `a;b;` | `a;ba` | `ab;a` | `;ab;` |
| 6 | `aaaaba` | `;a;ba` | `aa;a` | `a;aa` | `;aab;` |
| 6 | `aaaabb` | `;a;b` | `aaa;b` | `a;aab` | `;ab;` |
| 6 | `aaabaa` | `a;a;` | `a;baa` | `aab;a` | `;aa;` |
| 6 | `aaabab` | `;a;ab` | `a;ab` | `aa;b` | `;aab;` |
| 6 | `aaabba` | `;a;ba` | `aa;b` | `a;ab` | `;ab;a` |
| 6 | `aaabbb` | `;a;b` | `aa;bb` | `a;abb` | `;ab;` |
| 6 | `aababa` | `;ab;` | `a;aba` | `aab;a` | `a;b;` |
| 6 | `aababb` | `;a;b` | `aab;b` | `a;bab` | `;ab;` |
| 6 | `aabbaa` | `;b;a` | `aab;a` | `aa;ba` | `;ba;` |
| 6 | `aabbab` | `a;b;` | `a;bab` | `ab;ab` | `;ab;` |
| 6 | `aabbba` | `a;b;` | `a;bba` | `ab;ba` | `;ab;` |
| 6 | `abaaab` | `ab;a;` | `a;ab` | `aa;b` | `;baa;` |
| 6 | `ababba` | `ab;b;` | `ab;a` | `a;ba` | `;abb;` |
| 6 | `abbaab` | `;b;ab` | `ab;a` | `a;ba` | `;ba;b` |
| 7 | `aaaaaba` | `;a;aba` | `aa;a` | `a;aa` | `;aaab;` |
| 7 | `aaaaabb` | `;a;b` | `aaaa;b` | `a;aaab` | `;ab;` |
| 7 | `aaaabaa` | `;a;baa` | `a;aa` | `aa;a` | `;aaab;` |
| 7 | `aaaabab` | `;a;ab` | `aa;ab` | `a;aab` | `;aab;` |
| 7 | `aaaabba` | `;a;ba` | `aaa;b` | `a;aab` | `;ab;a` |
| 7 | `aaaabbb` | `;a;b` | `aaa;bb` | `a;aabb` | `;ab;` |
| 7 | `aaabaaa` | `;a;a` | `aaab;a` | `a;abaa` | `;aa;` |
| 7 | `aaabaab` | `;a;aab` | `a;ab` | `aa;b` | `;aaba;` |
| 7 | `aaababa` | `;a;aba` | `a;ab` | `aa;b` | `;aab;a` |
| 7 | `aaababb` | `;a;abb` | `a;ab` | `aa;b` | `;aab;b` |
| 7 | `aaabbaa` | `;a;baa` | `aa;b` | `a;ab` | `;ab;aa` |
| 7 | `aaabbab` | `;a;bab` | `a;ab` | `aa;b` | `;aabb;` |
| 7 | `aaabbba` | `;a;ba` | `aa;bb` | `a;abb` | `;ab;a` |
| 7 | `aabaaab` | `;a;ab` | `aab;a` | `a;baa` | `;aa;b` |
| 7 | `aabaaba` | `;a;ba` | `aab;a` | `a;baa` | `;aab;` |
| 7 | `aabaabb` | `;a;b` | `aaba;b` | `a;baab` | `;ab;` |
| 7 | `aababaa` | `;ab;` | `a;abaa` | `aab;aa` | `a;b;` |
| 7 | `aababab` | `;a;ab` | `a;bab` | `aab;b` | `a;ba;` |
| 7 | `aababba` | `;a;ba` | `aab;b` | `a;bab` | `;ab;a` |
| 7 | `aabbaab` | `;b;ab` | `aab;a` | `aa;ba` | `;ba;b` |
| 7 | `aabbaba` | `;ab;` | `a;baba` | `aabb;a` | `a;b;` |
| 7 | `aabbbaa` | `;b;a` | `aabb;a` | `aa;bba` | `;ba;` |
| 7 | `aabbbab` | `;b;ab` | `aab;b` | `aa;bb` | `;bba;` |
| 7 | `aabbbba` | `a;b;` | `a;bbba` | `ab;bba` | `;ab;` |
| 7 | `abaaaab` | `ab;a;` | `a;aab` | `aa;ab` | `;baa;` |
| 7 | `abaaaba` | `;a;ba` | `aba;a` | `ab;aa` | `;aab;` |
| 7 | `abaabab` | `;a;ab` | `ab;ab` | `aba;b` | `;aab;` |
| 7 | `abaabba` | `;a;ba` | `aba;b` | `ab;ab` | `;ab;a` |
| 7 | `ababaab` | `;b;ab` | `aba;a` | `a;aba` | `;ba;b` |
| 7 | `ababbba` | `;b;ba` | `aba;b` | `a;abb` | `;bb;a` |
| 7 | `abbaaab` | `;b;aab` | `ab;a` | `a;ba` | `;ba;ab` |
| 7 | `abbabba` | `;b;bba` | `ab;a` | `a;ba` | `;babb;` |

表の網羅性は「全候補 `2^n` を列挙→不合格の `W` の正確な E,x,y,F を算出→表の全軌道の和が不合格集合に一致」という集合の完全等号で監査。適法性、全等式、差の存在、対称性での保存を§8で assert する。**小さい長さの実験から任意長を類推したのではない**（一般長は§2の窓帰納法による）。

## 4. 5表示がすべての arity で成立する直接証明（S2）

`d≥2` を任意に固定し、同じ許容文脈 `E` で `E[\mathbf u]=E[\mathbf v]=W` とする。どの許容 `F` についても `F[\mathbf u]=W` なら `F[\mathbf v]=W` を示す。`E` 共有から **`Σ_i|u_i|=Σ_i|v_i|`** が成立することに注意。

### (A) `W=x^n`

受理される全タプル成分、全固定部は `x` の冪。全長保存より `F[\mathbf v]` は `x^n`。任意の `d` について成立する。

### (B) `W=x^{n-1}y` とその反転

`y` は末尾に一回だけある。`E` の右端固定部 `E_d` が非空なら、そこに唯一の `y` があり、すべての成分は `x` の冪。`E_d=ε` なら最終穴 `u_d,v_d` はともに末尾に `y` を持ち、それ以外の穴成分は純粋な `x` の冪。どの `F` においても `F[\mathbf u]=W` を満たすなら、末尾の `y` が最終穴内か右固定部内かは**最終穴 `u_d` が `y` を含むか**だけで決まる。`v_d` も同じ有無なので、置換後も唯一の `y` が末尾にあり、残りは `x`、全長は `n`。よって `F[\mathbf v]=W`。反転 `yx^{n-1}` は対称。

### (C) `W=yx^{n-2}y`

`n≥3`。2つの `y` はそれぞれ先頭・末尾にのみ現れ、内部はすべて `x`。`d≥2` の中間区切りが非空なので、一つの穴が両端の `y` をまたぐことはない。共通の `E` に関して、初めの穴の語は `E_0=ε` なら先頭 `y`、そうでなければ純粋な `x` の冪であり、`\mathbf u` と `\mathbf v` で一致する。同じく末尾穴は `E_d=ε` の場合に限り末尾 `y` を持ち、他の成分は `x` だけである。任意の `F[\mathbf u]=W` においても、`\mathbf u` の先頭・末尾穴が `y` を含むかどうかで左右端の `y` の置き場所が決まるため、`\mathbf v` へ置換しても左右端の `y` は維持され、内部は `x` のみ、総長 `n`。よって一致する。`d=1` は補題1.1。

### (D) 交互語 `W=(xy)^k` または `(xy)^kx`

`W` の文字は絶対位置の偶奇で決まり、**同じ文字が現れればその位置の偶奇も同じ**。`E` の各中間固定区切り `E_j` は非空なので、その先頭の同じ文字が `E[\mathbf u]` と `E[\mathbf v]` に現れる位置の差は偶数。固定部長は同じであるから、

\[
 \sum_{i=1}^j(|v_i|-|u_i|)\equiv0\pmod2\qquad(1\le j<d).
\]

総長も同じなので `j=d` の差はゼロ。差分を取れば、**すべての `i` で `|u_i|≡|v_i| (mod 2)`**。また、それぞれの穴の開始位置の偶奇は二つの埋込みで一致するので、`u_i` と `v_i` は **同じ始端文字・同じ終端文字**を持つ（内部も交互）。

`F[\mathbf u]=W` で各 `u_i` を `v_i` に差し替えると、変わる部分は内部では交互、両境界の文字が同一だから外側との隣接も交互のまま。全長も `n` のままで、全語の最初の文字も不変（固定部が先頭にあればそこ、不在なら第1穴の最初の文字）。ゆえに結果は**唯一の長さnの同じ始端文字を持つ交互語** `W` である。

以上で全 arity で成立。必要性§2と短語§3を合わせ、**二文字の単語言語は、全 `f≥2` で2穴の場合と完全に同じ分類**。□

## 5. 文字が3種類以上・同じ冪等型の場合（S3の部分結果）

### 命題5.1（全字相異なる周期語は全 arity で代入可能）【証明済み】

互いに相異なる文字 `z_0,…,z_{p-1}`（`p≥1`）を並べた語 `u=z_0…z_{p-1}` を取る。`u^ω` の**任意の有限連続因子** `W` の単語言語 `{W}` は、自明型付けで任意の arity `d≥1` について代入可能。

**証明。** `d=1` は自明。`d≥2` で共通文脈 `E` により `E[\mathbf x]=E[\mathbf y]=W` とする。周期中の各文字がちょうど一箇所に現れるので、各中間固定区切りの先頭文字が同じことから、対応する埋込み位置の差は `p` の倍数。よって各穴長差は `p` の倍数、各 `x_i,y_i` は周期語の同じ開始位相を持ち、同じ終端文字を持つ。任意の `F[\mathbf x]=W` でも置換で各境界の文字・周期的隣接規則を維持し、全長・先頭文字を変えないため、`F[\mathbf y]=W`。□

特に、`u=abc` として任意の `N≥1` の `(abc)^N` は **全 arity で合格**。これは「長語は一文字の冪か二文字周期に限る」という素朴な予想に対する明示的反例。ただし **3文字の周期語なので、任意に複雑な非周期語の存在を示したわけではない**。

### 命題5.2（2個の端末マーカーを持つ長い単色内部）【証明済み】

`x` と異なる文字 `p,q`（`p=q` も許す）、`N≥1` に対し `{p x^N q}` はすべての arity に対して自明型で代入可能である。理由は §4(C) の2つの端末記号の議論と同じで、端点の特殊文字は先頭・末尾以外にないため、共有する `E` の穴が特殊文字を持つか否かは両タプルで一致し、別の `F` でもその両端配置は保存される。`p≠q` ならなお容易。よって `b a^N c` は `N` に関して任意に長い3文字の合格語になる。

### 部分的必要条件と未解決部分

`Σ_e={z∈Σ:s(z)=e}` が `k≥3` 文字から成るとし、`W∈Σ_e⁺` が唯一の型 `e` の語なら、`W` の **任意の二文字集合 `{x,y}` 上の連続因子**で長さ7以上のものは§2の5形でなければならない。これは因子遺伝と S1 の直接の系（そのような因子内では全成分の型が `e`）。一方、3文字を頻繁に交ぜる `(abc)^N` には長さ7の二文字だけからなる因子がなく、制約は空になる。

**`k≥3` の完全な構造分類は未解決。** 3文字での全数検査（自明型、長さ `1～11`）の合格数を§8に載せる。列挙は長さ固定の観察であり、**これを無限長の定理とは呼ばない**。文字数が変わると現れる繰り返し周期の候補も変わり、二文字の7状態帰納法だけでは解けない。

## 6. 異なる型の文字を含む場合（S3・非冪等型）

### 命題6.1（冪等中立語の分類は非中立文字に拡張できない）【有限計算による厳密な反例】

群 `C₂={e,g}`（`g²=e`, `g≠e`）へ `s(a)=s(b)=g` とする。この正の像は `C₂` であり、`s(W)=e` となる長さ8の語

\[
 W=\mathtt{aaabbaba}
\]

を考える。`W` は§2の5形に属さない。自明型での具体的違反は `E=(ε,a,baba)`, `x=(aa,b)`, `y=(a,ab)`, `F=(ε,abba,a)` で、`E[x]=E[y]=F[x]=aaabbaba`, `F[y]=aabbaaba≠W`。ただし `s(aa)=e≠g=s(a)` なので、この組は偶奇型の条件を満たさない。ところが `{W}` は **すべての arity** について `(f,s)`-tuple-substitutable。実際、同じ型のタプル成分は**長さの偶奇が同じ**ことに等しい。§8の正確な列挙は `d=1,2,3,4` のすべてで違反がないことを検査する。`d≥5` は最低 `2d−1≥9` 文字が必要であり、長さ8の `W` を受理する許容文脈が存在しない。したがって任意の `f` で成立する。比較として自明型では、例えば検査プログラムが具体的な2穴違反を返す。

これは「最終語の型が `e` だから、その中のすべての穴も型 `e`」とはならないことを示す。逆に、**同一の冪等元へ写る文字だけを使う**という S1/S4 の仮定が本質である。

任意の有限半群の冪等元 `e` に対し、記号列の部分語型が `e` にならない場合、単純な二文字分類の移植は一般にできない。`g²=e` の例で、すでに長さ8から分類が変わる。**一般の有限半群の型別完全分類は本報告で証明していない。**

## 7. 論文へ移せる命題と未解決問題への影響（S4）

### 命題7.1（idempotent-two-letter singleton obstruction）【証明済み】

`f≥2`、`s:Σ⁺→S` は固定有限半群型付け、`a,b∈Σ` は異なる文字で `s(a)=s(b)=e=e²`、`L∈C_{f,s}` とする。ある型 `e` の語が一意に `W` で、しかも `W∈{a,b}⁺` なら、`|W|≥7` では

\[
 W\in\{x^n, x^{n-1}y, yx^{n-1}, yx^{n-2}y,
   (xy)^k,(xy)^kx\}
\]

（`x,y` は異なる `a,b`、`n=|W|`、交互語の `k` は総長に合わせる）。`|W|≤6` なら §3 の表どおり。さらに `{W}` は**すべての arity**で自明型付け代入可能である。

**証明。** 先行報告の唯一型剛性（§1）により `{W}` は `d≤f` で `(f,s)`-tuple-substitutable、特に `d=2`。`W` とその任意の非空因子は、冪等性から型 `e`。したがって `{W}` の arity2 条件は自明型付けのそれと同じであり、定理2.1で分類される。定理2.1の十分性により同じ `{W}` が全 arity で成立。□

**コード語版（追加系）:** 2つの非空コード語 `u,v∈Σ⁺` が `s(u)=s(v)=e=e²` を満たし、`h(a)=u,h(b)=v` による写像 `h:{a,b}*→Σ*` が**単射**だとする。唯一型語 `W=h(T)` なら、`T` は定理2.1の5形（短い場合は§3の分類）に入る。`T` の反例の各 `E,x,y,F` を非消去準同型 `h` で写せば、中間区切りは非空のまま、型一致も保たれ、`F[y]≠T` は単射性から `h(F[y])≠h(T)=W`。唯一型剛性に反する。したがってこの系は `cor:typing-level-obstruction` が用いる letter-disjoint code とも整合する。ただし非単射コードでは結論を主張しない。

### §7.2 他定理との正確な関係

| 原稿の結果 | 本分類から言えること | **言えないこと** |
|---|---|---|
| `thm:doubling-no-lift`（定理C） | 長い倍増語の一意中立型の失敗を、**二文字内部構造**の観点から別証明可能な場合がある。5形以外の `W` は長さ7の短い局所証明書ですでに失敗 | 任意型付けの `W_n` への定理Cの**全ての内容**を置き換えられない。型付けの文字像が冪等で同一とは限らない |
| `cor:typing-level-obstruction` | fan-out1 の指数下界が依存する同じ冪等型文字 `a,b` による語を fan-out≥2 へ移す際の形の障害を精密に与える | fan-out≥2 の指数下界や5形候補の実現性は導かない |
| `op:S1` | 一中立文字の binary `s(a)=1,s(b)=ζ` は本命題の「**2文字とも `e`**」条件を満たさない。既存の `thm:two-letter-content` は fan-out≥2 に多項式上界を与える | fan-out1 の open problem を解かない |
| `op:fanout-two` / `prop:sl-reduction` | U₁で二つの中立文字だけからなる唯一希少語を探索する場合、5形への絞り込みが可能 | 内容型の3文字以上での一般多項式上界、または新しい下界族は得られていない |
| `prop:rare-type` | もし5形を唯一型語に実現する**小さい reduced good・小さい厚さの有限言語族**が得られれば、その語の長さは両正準作用素とクラス全体の集合駆動作用素の下界を与える | 語の形式と単語言語の代入可能性 **だけでは** その有限族の存在・文法表示・厚さは保証されない |

### §7.3 長語 `x^N` と交互語に下界の余地があるか

**単語言語 `{W}` 単独では、目標の下界反例にならない。** どの reduced good 表示 `G` についても各規則は成功導出で使われ、すべての成功導出語の長さが `|W|`。したがって原稿の規則厚さは **`θ̄_G=max(1,|W|)=|W|`**（`W` 非空）。また `{W}` の自明型への特性標本として `{W}` 自体を取れるため、符号長は `|W|+1=O(θ̄_G)`。`x^{2^n}` の短い SLP は文法サイズ `O(n)` でも厚さ `2^n` なので、`poly(‖G‖,θ̄_G)` に矛盾しない。

しかし、天井文字 `c` を含む**別の型の短語**も生成する有限言語 `L` に `W` を唯一中立型として加え、かつ `L∈C_{2,s}`、`‖G‖,θ̄_G=poly(n)` を両立できるかは、この分類のみでは決定できない。特に `W=x^N` や交互語の単語言語が高 arity でも代入可能だということは**必要条件**に過ぎず、短い別型語との二穴干渉を排除していない。

### §7.4 `thm:two-letter-content` による多項式化の適用範囲

原稿 `thm:two-letter-content` は `Σ={a,b}` の**内容型付け**で、`f≥2`、固定ランク `r_max≥2`、すべての reduced good 表示について両正準作用素の特徴標本の総符号長を明示的多項式に抑える。二文字セミラティス型付けへも `lem:typing-monotone` で移る。したがって**アルファベット全体が2文字のときの**希少な `a^N`（例 `a↦1,b↦ζ`）は、既存定理の枠内で超多項式データ下界に使えない。

一方、`Σ={a,b,c}` として `a,b↦1`, `c↦ζ` の**三文字**天井型付けでは、短い `c` 語との干渉を含む問題であるから、二文字定理を無条件で使えない。`L∩{a,b}⁺` への切片は単語であっても、その切片用の**文法の普通の厚さ**が元の `G` から多項式に制御されるとは示されていない。この差を消さない限り `op:fanout-two` は未解決。

**要するに**「ファンアウト≥2では二文字の障害が一文字（または交互）へ帰着する」と言えるのは、**二文字が同じ冪等型に属し、当該型の受理語がただ一つで、その語がその二文字のみからなる場合**だけ。`x^{n-1}y` と `yx^{n-2}y` も残るため、さらに「一文字または交互」だけへは**帰着できない**。

## 8. 再現コードと実行結果（標準ライブラリのみ）

下のコードは `singleton_classification_verify_2026-11-02.py` として保存し、Windows PowerShell で `py -3 singleton_classification_verify_2026-11-02.py`。入力 n の最大値を任意に増やす必要はない。**無限長の保証は§2・§4の数学的証明に依存する**。

検査の論理：長さ `n` について切断位置 `0≤i_1<j_1<⋯<i_d<j_d≤n` の全ての `2d` 個の切断を `itertools.combinations(range(n+1),2*d)` で列挙する。これは非空穴・穴間非空区切りを**正確に**全列挙する。各許容文脈 `E` に対して受理する同型タプルを群にし、その各タプルの受理文脈集合を比較する。`D(x)≠D(y)` なら対称差の `F` は必ず一方で受理され、もう一方で不受理である。したがって有限単語言語に関する **PASS は完全検査、FAIL は具体的証明書**。

```python
#!/usr/bin/env python3
"""Singleton tuple-substitutability exhaustive audit, standard library only.
Run: py -3 singleton_classification_verify_2026-11-02.py
All 2d cuts are strictly increasing; thus gaps between holes are nonempty.
"""
from itertools import product, combinations
from collections import defaultdict

# Populated below from independently recomputed orbit-representative certificates.
CERTIFICATES = r'''
5|aaabb|;a;b|aa;b|a;ab|;ab;
5|aabba|a;b;|a;ba|ab;a|;ab;
6|aaaaba|;a;ba|aa;a|a;aa|;aab;
6|aaaabb|;a;b|aaa;b|a;aab|;ab;
6|aaabaa|a;a;|a;baa|aab;a|;aa;
6|aaabab|;a;ab|a;ab|aa;b|;aab;
6|aaabba|;a;ba|aa;b|a;ab|;ab;a
6|aaabbb|;a;b|aa;bb|a;abb|;ab;
6|aababa|;ab;|a;aba|aab;a|a;b;
6|aababb|;a;b|aab;b|a;bab|;ab;
6|aabbaa|;b;a|aab;a|aa;ba|;ba;
6|aabbab|a;b;|a;bab|ab;ab|;ab;
6|aabbba|a;b;|a;bba|ab;ba|;ab;
6|abaaab|ab;a;|a;ab|aa;b|;baa;
6|ababba|ab;b;|ab;a|a;ba|;abb;
6|abbaab|;b;ab|ab;a|a;ba|;ba;b
7|aaaaaba|;a;aba|aa;a|a;aa|;aaab;
7|aaaaabb|;a;b|aaaa;b|a;aaab|;ab;
7|aaaabaa|;a;baa|a;aa|aa;a|;aaab;
7|aaaabab|;a;ab|aa;ab|a;aab|;aab;
7|aaaabba|;a;ba|aaa;b|a;aab|;ab;a
7|aaaabbb|;a;b|aaa;bb|a;aabb|;ab;
7|aaabaaa|;a;a|aaab;a|a;abaa|;aa;
7|aaabaab|;a;aab|a;ab|aa;b|;aaba;
7|aaababa|;a;aba|a;ab|aa;b|;aab;a
7|aaababb|;a;abb|a;ab|aa;b|;aab;b
7|aaabbaa|;a;baa|aa;b|a;ab|;ab;aa
7|aaabbab|;a;bab|a;ab|aa;b|;aabb;
7|aaabbba|;a;ba|aa;bb|a;abb|;ab;a
7|aabaaab|;a;ab|aab;a|a;baa|;aa;b
7|aabaaba|;a;ba|aab;a|a;baa|;aab;
7|aabaabb|;a;b|aaba;b|a;baab|;ab;
7|aababaa|;ab;|a;abaa|aab;aa|a;b;
7|aababab|;a;ab|a;bab|aab;b|a;ba;
7|aababba|;a;ba|aab;b|a;bab|;ab;a
7|aabbaab|;b;ab|aab;a|aa;ba|;ba;b
7|aabbaba|;ab;|a;baba|aabb;a|a;b;
7|aabbbaa|;b;a|aabb;a|aa;bba|;ba;
7|aabbbab|;b;ab|aab;b|aa;bb|;bba;
7|aabbbba|a;b;|a;bbba|ab;bba|;ab;
7|abaaaab|ab;a;|a;aab|aa;ab|;baa;
7|abaaaba|;a;ba|aba;a|ab;aa|;aab;
7|abaabab|;a;ab|ab;ab|aba;b|;aab;
7|abaabba|;a;ba|aba;b|ab;ab|;ab;a
7|ababaab|;b;ab|aba;a|a;aba|;ba;b
7|ababbba|;b;ba|aba;b|a;abb|;bb;a
7|abbaaab|;b;aab|ab;a|a;ba|;ba;ab
7|abbabba|;b;bba|ab;a|a;ba|;babb;
'''

def plug(E, x):
    assert len(E) == len(x) + 1
    return ''.join(E[i] + x[i] for i in range(len(x))) + E[-1]

def occurrences(w, d):
    for cuts in combinations(range(len(w) + 1), 2*d):
        E = (w[:cuts[0]],) + tuple(w[cuts[2*i+1]:cuts[2*i+2]] for i in range(d-1)) + (w[cuts[-1]:],)
        x = tuple(w[cuts[2*i]:cuts[2*i+1]] for i in range(d))
        assert all(x) and all(E[1:-1]) and plug(E,x) == w
        yield E, x

def tau(x, mode='trivial'):
    if mode == 'trivial': return tuple(0 for _ in x)
    if mode == 'parity': return tuple(len(u) % 2 for u in x)
    if mode == 'content': return tuple(frozenset(u) for u in x)
    if mode == 'u1': return tuple('c' in u for u in x)
    raise ValueError(mode)

def certificate(w, d=2, mode='trivial'):
    """Exact witness (E,x,y,F); None iff arity-d substitutability."""
    contexts = defaultdict(lambda: defaultdict(set))
    distributions = defaultdict(set)
    for E, x in occurrences(w, d):
        contexts[E][tau(x,mode)].add(x)
        distributions[x].add(E)
    for E in sorted(contexts):
        for kind in sorted(contexts[E], key=str):
            members = sorted(contexts[E][kind])
            if len(members) < 2: continue
            baseline = members[0]
            for other in members[1:]:
                different = distributions[baseline] ^ distributions[other]
                if different:
                    F = min(different)
                    x, y = (baseline, other) if F in distributions[baseline] else (other,baseline)
                    assert plug(E,x) == plug(E,y) == plug(F,x) == w
                    assert plug(F,y) != w and tau(x,mode) == tau(y,mode)
                    return E,x,y,F
    return None

def orb(w):
    comp = str.maketrans('ab','ba')
    return {w,w[::-1],w.translate(comp),w.translate(comp)[::-1]}

def binary_words(n):
    return {''.join(v) for v in product('ab',repeat=n)}

def five_shapes(n):
    result = set()
    for a,b in [('a','b'),('b','a')]:
        result |= {a*n, a*(n-1)+b, b+a*(n-1)}
        if n>=2: result.add(b+a*(n-2)+b)
        result.add(''.join((a if i%2==0 else b) for i in range(n)))
    return result

def check_cert_rows():
    covered = {5:set(),6:set(),7:set()}
    for line in CERTIFICATES.strip().splitlines():
        n, w, E, x, y, F = line.split('|')
        n=int(n)
        E=tuple(E.split(';')); F=tuple(F.split(';'))
        x=tuple(x.split(';')); y=tuple(y.split(';'))
        assert len(E)==len(F)==3 and len(x)==len(y)==2
        assert all(x) and all(y) and E[1] and F[1]
        assert tau(x)==tau(y)
        assert plug(E,x)==plug(E,y)==plug(F,x)==w
        assert plug(F,y)!=w
        covered[n].update(orb(w))
    for n in (5,6,7):
        bad={w for w in binary_words(n) if certificate(w) is not None}
        assert covered[n]==bad,(n,len(covered[n]),len(bad))
        print('certification',n,'bad',len(bad),'orbits',sum(1 for l in CERTIFICATES.strip().splitlines() if l.startswith(str(n)+'|')))

def check_binary():
    good_at={}
    for n in range(1,9):
        good={w for w in binary_words(n) if certificate(w) is None}
        good_at[n]=good
        assert len(good)=={1:2,2:4,3:8,4:16,5:24,6:16,7:10,8:10}[n]
        assert all(certificate(w,d) is None for w in good for d in range(3,(n+1)//2+1))
        print('binary',n,'good',len(good),'a-start',','.join(sorted(w for w in good if w[0]=='a')))
    assert good_at[7]==five_shapes(7)
    # Complete 8-word audit: every 8-word with both windows 7-good is 8-good.
    local={w for w in binary_words(8) if w[:7] in good_at[7] and w[1:] in good_at[7]}
    assert local==good_at[8]==five_shapes(8)
    for n in range(7,17):
        assert all(certificate(w,d) is None for w in five_shapes(n) for d in range(2,min((n+1)//2,5)+1))
    print('binary 7-window transition graph:')
    for w in sorted(good_at[7]):
        print(' ',w,':',','.join(c for c in 'ab' if (w+c)[-7:] in good_at[7]) or '-')

def check_other():
    # Three-letter examples; these are experiments only, not a classification.
    for n in range(1,12):
        words=[''.join(v) for v in product('abc',repeat=n)] if n<=5 else None
        if n==1: current={'a','b','c'}
        elif n>1:current={u+c for u in current for c in 'abc' if certificate(u+c) is None}
        if n<=5:
            assert current=={u for u in words if certificate(u) is None}
        print('ternary',n,'good',len(current))
    for n in (9,12,18):
        w=('abc'*(n//3+1))[:n]
        for d in range(2,min((n+1)//2,5)+1):assert certificate(w,d) is None
    W='aaabbaba'
    assert certificate(W,2,'trivial') is not None
    assert all(certificate(W,d,'parity') is None for d in range(1,5))
    print('group Z2 counterexample',W,'trivial FAIL; parity all d<=4 PASS')

def main():
    check_cert_rows()
    check_binary()
    check_other()
    print('ALL ASSERTIONS PASSED; infinite-length classification relies on the written proofs.')

if __name__=='__main__':main()
```

### 実行ログ

```text
certification 5 bad 8 orbits 2
certification 6 bad 48 orbits 14
certification 7 bad 118 orbits 32
binary 1 good 2 a-start a
binary 2 good 4 a-start aa,ab
binary 3 good 8 a-start aaa,aab,aba,abb
binary 4 good 16 a-start aaaa,aaab,aaba,aabb,abaa,abab,abba,abbb
binary 5 good 24 a-start aaaaa,aaaab,aaaba,aabaa,aabab,abaaa,abaab,ababa,ababb,abbab,abbba,abbbb
binary 6 good 16 a-start aaaaaa,aaaaab,aabaab,abaaba,ababab,abbabb,abbbba,abbbbb
binary 7 good 10 a-start aaaaaaa,aaaaaab,abababa,abbbbba,abbbbbb
binary 8 good 10 a-start aaaaaaaa,aaaaaaab,abababab,abbbbbba,abbbbbbb
binary 7-window transition graph:
  aaaaaaa : a,b
  aaaaaab : -
  abababa : b
  abbbbba : -
  abbbbbb : a,b
  baaaaaa : a,b
  baaaaab : -
  bababab : a
  bbbbbba : -
  bbbbbbb : a,b
ternary 1 good 3
ternary 2 good 9
ternary 3 good 27
ternary 4 good 81
ternary 5 good 207
ternary 6 good 381
ternary 7 good 489
ternary 8 good 333
ternary 9 good 183
ternary 10 good 189
ternary 11 good 195
group Z2 counterexample aaabbaba trivial FAIL; parity all d<=4 PASS
ALL ASSERTIONS PASSED; infinite-length classification relies on the written proofs.
```

**独立実装との照合**：前回の `nolift_exhaustive_2026-11-02.py` の別実装と、本プログラムの `certificate(w,2)` の合否を長さ1～8の二元語 **全510語** に対して照合し、すべて一致した。これは実験的なコード監査であって、一般長の数学的証明の代替ではない。

## 9. 文献位置づけ・残課題

- 栗山貴之の原稿の定義と前提： [`main.tex`](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/main.tex)（2026-11-02取得の上記 Git blob）。`def:tuple-substitutable`, `prop:rare-type`, `lem:no-insertion`, `thm:doubling-no-lift`, `thm:two-letter-content` 等。
- Yoshinaka, *Efficient Learning of MCFGs with Multidimensional Substitutability*（研究情報源 `03_Multiple_Context-Free_Grammars_Foundations_and_Learning_v9.pdf` 所収）。非空セパレータと複数穴の文脈・代入可能性の先行枠組みであり、本分類自体とは区別。
- Holub–Raška–Starosta (2021), *Combinatorics on Words Basics*, Archive of Formal Proofs, <https://isa-afp.org/entries/Combinatorics_Words.html>。語の等式、共役、周期、Fine–Wilf などの標準理論を形式化。本研究の「窓遷移による分類」に関連する基本背景。
- 語の共役方程式 `XZ=ZY` については、例えば <https://www.numdam.org/item/ITA_2009__43_1_23_0/> の関連文献を参照。**ただし語方程式の既知性は「本稿の5形分類が既知」を意味しない**。
- 本報告の正確な singleton 2-hole 分類が既知か、また同型の二穴分解の一意性・bounded-delay code との同一視が可能かは**未確認**。文献上の優先権や新規性を断言しない。

**残課題**：多文字 `k≥3` の全構造分類、異型文字を許す一般有限半群の分類、5形の唯一希少型語を小さい通常厚さの reduced good な有限 `C_{2,s}` 言語として実現可能か、あるいはその不可能性の多項式短縮定理。これらは `op:fanout-two` に直結するが、今回の証明の範囲外。

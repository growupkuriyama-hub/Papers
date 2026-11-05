# 一本化・一般化・圧縮の独立検算（README (161), (162)）

**検算日：2026-11-06**  
**範囲：指定された C1–C6 の改訂箇所のみ。** 本報告は原稿全体の正当性の保証ではない。

## 1. 取得した版（SHA・行数）

- リポジトリ：`growupkuriyama-hub/Papers`
- ファイル：[`02-v2-lg-fanout-boundary/main.tex`](https://github.com/growupkuriyama-hub/Papers/blob/2234ded/02-v2-lg-fanout-boundary/main.tex)
- **検算対象コミット：`2234ded`**（指定と一致）。Git blob SHA：**`23a35246a37c9fbb1bd355faa411661f3e2f6499`**。**3,640行**（取得テキストは末尾改行なし）。
- 比較コミット `9b49d07`：blob `0e3853dbfac16a7467ab79abd729b47019a1c810`、3,629行。
- 比較コミット `7150f5e`：blob `c28dca26dfbe46abe03ba6feef725c3911c13134`、3,623行。
- 指定版 `README.md`：blob `f40cfa9b899aaed3e6a87591198666961ae2afbb`、195行。Change log (161), (162) を照合。

GitHubコミット比較 API では、`7150f5e..2234ded` は **3コミット先**であり、対象 `main.tex` の差分は **185行追加・168行削除（計353変更行）**、README は5行追加・2行削除と確認できた。

行番号は**対象 `2234ded/main.tex`** のもの。比較は各コミットのファイルを直接取得して行った。特に二つの定理本体の LaTeX テキストは `7150f5e`、`9b49d07`、`2234ded` の三版で**完全一致**した（ただし参照する `c_{\mathbb G,f}` の定義は改訂されている：C1・C3参照）。

## 2. 総合判定（一行）

**C1・C2・C3・C4・C6 は指定改訂の論理を確認、C5 の `prop:output-invariants`(iv) は「すべての導出」のままでは反例があるため「終端導出」への限定修正が必要；主要な短縮・標本上界の証明はこの修正で保たれる。**

## 3. C1–C6 の判定と数学的根拠

### C1. 短縮の原理：**正しい**（定数の数値変化について注記）

対象：`lem:heavy-node-count`（1357–1401行）、`lem:marked-heavy-window-group`（1469–1506行）、`lem:local-group-shortest`（2677–2727行）。

**(i) 実現ラベルで経路長を数えること：正しい。** ラベルを
\[
 (C,\lambda^{(\operatorname{fan}(C))}(\mathbf u))
\]
とする。同じラベルが一つの根から葉への経路上で祖先と真の子孫に現れれば、祖先の部分導出をその子孫の部分導出で置き換えられる。非削除性によって子孫の全 yield は祖先 yield に各文字を一度だけ寄与するため、根全体の長さは増えない。同じ非終端・同じ \(\lambda\)-ベクトルを持つので、各テンプレートの準同型評価を帰納的に適用して根の \(\lambda\)-ベクトルは変わらない。置換で真にノード数が減るので、「総長最小、次にノード数最小」という `\lambda`-minimal 性に反する。したがって経路には高々 \(n_\lambda(G)\) 個のノードしかない（1381–1388行）。上界 \(n_\lambda(G)\le |V||\mathsf N|^f\) も正しい。

**(ii) 反鎖から短縮原理と \(\beta\)：正しい。** 最小導出の重い反鎖 \(Q\) に \(|Q|>c+h\) があれば \(|Q_0|\ge |Q|-h>c\)、仮定により非空 \(J\subseteq Q_0\) を同時に置換できる。各 \(v\in J\) の元の yield 長は \(>\bar\theta_G\)、代替 yield 長は \(\le\bar\theta_G\)。線形かつ非削除のテンプレートなので、互いに比較不能な各ノードが寄与する根の文字位置は重ならず、各成分は根に**ちょうど一回**現れる。したがって
\[
 |\mathbf u_{\rm new}|_1-|\mathbf u_{\rm old}|_1
 =\sum_{v\in J}\bigl(|\mathbf u_v'|_1-|\mathbf u_v|_1\bigr)<0.
\]
根の \(\lambda\)-ベクトルは変わらないため、総長最小性と矛盾する。ゆえに全ての重い反鎖の幅は \(c+h\) 以下。

重いノードは祖先閉な部分木を作り、その葉は重い反鎖である。各経路のノード数が高々 \(n_\lambda(G)\) なので重いノード数は高々 \((c+h)n_\lambda(G)\)。根が軽ければ全長 \(\le b\)。重ければ、根の文字は、重いノードが明示的に書く文字（各ノード高々 \(\bar\theta_G\le b\)）または重いノードの軽い子に属する文字（各ノード高々 \(r_{\max}\) 個、各 \(\le b\)）に分配される。よって
\[
 \|\mathbf u\|_1\le (r_{\max}+1)b\max\{1,(c+h)n_\lambda(G)\},
\]
特に \(b=\bar\theta_G\) で本文の \(\beta\) を得る（1388–1401行）。

**二つの適用：正しい。**

- `lem:marked-heavy-window-group`：各根成分の先頭 \(k\)、末尾 \(\ell\)（\(k=\ell=0\) なら一文字）を記し、短い成分では全てを記す。印は合計高々 \(h=f(k+\ell+1)\) で、互いに素な反鎖部分木のうち印に触るものは高々 \(h\) 個。残余 \(Q_0\) の各ノードを短い yield へ替えるとき、\(g\) の各根成分値は \(d\le f\) 行・各 owner 高々 \(f\) ブロックの群一斉置換で表せる。`prop:block-replacement-interface` が \(|Q_0|>c_{\mathbb G,f}\) で非空 \(J\) を与える。印を残したことで窓型は保存される（1481–1505行）。よって \((c,h)=(c_{\mathbb G,f},f(k+\ell+1))\)。
- `lem:local-group-shortest`：根境界に高々 \(h=2kf\) 個の印を付ける。印に触れない \(Q_0\) から `lem:lg-buffered-owners` により \(|I|\ge |Q_0|/(4kf+1)\) を抽出する。\(|Q_0|>(4kf+1)c_{\mathbb G,f}\) なら \(|I|>c_{\mathbb G,f}\)。拡大ブロックの先頭・末尾 \(k\) 文字が保存され、長さも \(\ge2k+1\) なので、`lem:local-group-blocks` の固定境界係数と群一斉置換が適用できる。得た \(\varnothing\ne J\subseteq I\subseteq Q_0\) で窓型と順序付き sliding-factor 積を同時に保存できる（2633–2675、2693–2726行）。よって \((c,h)=((4kf+1)c_{\mathbb G,f},2kf)\)。

**上界の比較。** `thm:window-group-polydata`（1527–1543行）および `thm:local-group-polydata`（1612–1624行）の**定理文・表示式そのものは**旧二版と一致する。`lem:local-group-shortest` の \(\beta_\lambda=(r_{\max}+1)\bar\theta_G C^{\rm buf}_{k,\mathbb G,f}|V||M_{k,\nu}|^f\) も、旧版の記号 `n_λ` が現行の `\bar n_λ` になった点を除き数式は同じ。ただし**定義の代入後の係数値は必ずしも同じではない**。非可換 \(f=1\) で \(c_{\mathbb G,1}\) は旧 \(M_{\mathbb G,1}-1\) から新 \(|\mathbb G|-1\) へ改善された。\(\mathbb G=S_3\) では \(35\to5\)。したがって「式は不変」は正しいが、「全ての数値定数が不変」は**誤り**。これは改訂による改善であり、定理修正を要しない。

### C2. Pumping と三か所の使用：**正しい**

対象：付録B（2426–2454行）、`lem:lg-rees-window-coordinate`（2503–2541行）、`thm:lg-characterization`（2543–2573行）、`lem:mcfg-li-group-window`（2575–2598行）。

**Pumping：正しい。** \(n=|T|\) 個の因子 \(a_1\cdots a_n\) の正の prefix products を \(t_i=a_1\cdots a_i\) とする。異なる \(i<j\) に \(t_i=t_j=t_i x\)（\(x=a_{i+1}\cdots a_j\)）があれば \(t_i=t_i x^\omega\) なので積全体を \(t_i x^\omega\) と残りの suffix の積に書き直せる。\(x^\omega\in E(T)\)。一方 \(t_1,\ldots,t_n\) が相異なれば、これらは \(T\) の全要素であり、有限半群に存在する冪等元のどれかが prefix として出現する。いずれも全積は \(T^1E(T)T^1\) に入る。因子数がさらに多い場合は先頭 \(n\) 個へ適用して右側に残りを掛ければよい。原稿2447–2452行の証明で十分。

**Rees 窓座標：正しい。** \(S^k\subseteq K\) なら長さ \(k\) の任意の \(h\)-像が \(K\) に入る。Rees 積 \((i,a,\lambda)(j,b,\mu)=(i,ap_{\lambda j}b,\mu)\) により、右乗法は \(I\)-座標を保存し、左乗法は \(\Lambda\)-座標を保存する。よって prefix の \(\Lambda\)-座標は末尾 \(k\) 文字の像から計算できる。\(\nu(F)=\operatorname{act}(\operatorname{col}(h(F[1..k])),h(F[k+1]))\) によって群座標の順序付き積が得られる（2522–2540行）。独立の旧ステップ(1)は pumping に置換可能であり、現行の (1)「Coordinates」と (2)「Group coordinate」、(2) 内の「(1)」参照は正しい。

**同値定理：正しい。** Almeida–Margolis–Steinberg–Volkov (2009), *Transactions of the AMS* 361, Proposition 2.3 の (1),(3),(4) はそれぞれ LG、ある \(m\) で \(S^m=K\)、\(U_1\) を部分半群に含まないことの同値を述べる。原著の掲載頁は **1434**（提供された第05巻合本のPDF 109頁）で確認した。本文の (iii)「全冪等元が \(K\) にある」からは pumping により \(S^{|S|}\subseteq S^1E(S)S^1\subseteq K\)。\(S^{|S|}\) は非空 ideal なので最小 ideal \(K\) を含み、等号となる。逆に \(S^m=K\) なら \(e=e^m\in K\)。よって (i)–(iii) は完結する。残りの (iii)⇒(iv) は Rees 窓座標、(iv)⇒(i) は長い窓型の fiber 上の積 \(\alpha\star\beta=\alpha J\beta\) が群であり、\(eTe\) がその有限非空部分半群となることから成立（2558–2572行）。(iv) で \(S^k=K\) となる**任意の \(k\ge1\)**を選べる。

**LI×群への使用：正しい。** \(S_0=\tau(\Sigma^+)\in\mathbf{LI}\)、\(k=|S_0|\) とすると長さ \(k\) の prefix/suffix はそれぞれ \(aeb,cfd\)（\(a,b,c,d\in S_0^1\)、\(e,f\in E(S_0)\)）に分解できる。これは上記 pumping の直接適用。局所自明性から任意の \(u\in S_0^1\) に対し \(euf=ef\)：実際 \(fef=f\)、\(e(uf)e=e\) より \(euf=eu(fef)=(eufe)f=ef\)。したがって \(\tau(pxz)=a e(b\tau(x)c) f d=aefd\) で、中央 \(x\) に依存せず \(p,z\) の像だけで定まる。\(x=\varepsilon\) も \(S_0^1\) の単位元で扱える（2583–2597行）。

### C3. ファンアウト1の群定数：**正しい**

対象：`lem:block-replacement`(c)（2185–2194、2394–2401行）、`lem:group-interval`（2289–2321行）、`prop:block-replacement-interface`（1442–1460行）。

\(f=1\) なら行は一つ、各 owner は高々一ブロックを持つ。ブロックのない owner があれば単独で選べる。そうでなければ**ブロックの出現位置順**に owner 番号を振り直してよい。定数も含めたチャンクの元値 \(u_1,\ldots,u_m\)、代替値 \(v_1,\ldots,v_m\) とし、\(P_p=u_1\cdots u_p\)、\(Q_p=v_1\cdots v_p\)、\(\kappa_p=P_pQ_p^{-1}\)（\(P_0=Q_0=1\)）を置く。連続 owner 区間 \((a,b]\) のみの置換後は
\[
 P_a(Q_a^{-1}Q_b)(P_b^{-1}P_m).
\]
これが元値 \(P_m\) に等しいことと \(\kappa_a=\kappa_b\) は同値。\(m\ge|\mathbb G|\) なら \(m+1>|\mathbb G|\) 状態で鳩の巣を適用でき、必ず \(0\le a<b\le m\) を取れる。非可換でも因子の順序を交換していない。

- 可換の場合：\(m>\mathsf d(\mathbb G^f)\) は非空ゼロ和部分列を保証する。
- 非可換 \(f=1\)：\(m>|\mathbb G|-1\iff m\ge|\mathbb G|\)。
- その他：\(m>M_{\mathbb G,f}-1\iff m\ge M_{\mathbb G,f}\)。

以上より、区分的定義と `prop:block-replacement-interface` の厳密不等号が整合する。小群での独立テストは§6。

### C4. 特性標本の統合：**正しい**

対象：`lem:witness-length-template`(ii),(iv)（1111–1143、2899–2932行）、`prop:completeness`（926–944、2766–2781行）、`thm:data-from-typed-thickness`（1172–1188、2942–2946行）、`cor:distribution-representatives`（1314–1326、2972–2980行）。

\(\iota(X)\in\operatorname{Cl}_{L,s}(X)\) は \(L_X\) の語と同じ型・同じ分布同値類に属する。\(\chi(X)\) は \(L_X\) の任意の yield を受理するので、\(\chi(X)[\iota(X)]\in L\)。型付き規則 \(X\to\rho(Y_1,\ldots,Y_q)\) に対し実際の \(\mathbf u_j\in L_{Y_j}\) を選ぶと、`lem:witnessed-composition` によって
\[
 \rho(\iota(Y_1),\ldots,\iota(Y_q))
 \equiv_{L,s}
 \rho(\mathbf u_1,\ldots,\mathbf u_q)\in L_X.
\]
したがって全 rule witness も \(L\) に属し、\(\Wit_\iota\subseteq L\)。各 \(\iota(X)\) の型は \(\widehat s\)-型としても \(X\) に一致する。さらに \(\chi(S_{(t)})=E_S=\square_1\)、型付き規則の rank は元の規則の rank 以下で \(r_G\le r_{\max}\)。よって `prop:completeness` の前提を満たす。

同命題の Link は同じ \(\chi(X)\) に観測された \(\iota(X)\) と規則右辺を結び、Const/Comp はその規則をシミュレートする。Comp の rank は \(\le r_{\max}\) で、無制限版では \(r\le\|K\|_+\)（`eq:sample-rank`）。Start は \(\chi=\square_1\) の根 witness により得られる。soundness と合わせて、どちらの演算子にも同じ特性標本となる。\(\varepsilon\) 受理は \(\varepsilon\in K\) に一致する。

長さはコンテキストに高々 \(\bar\theta_G\)、規則の明示終端に高々 \(\bar\theta_G\)、子が高々 \(r_{\max}\) 個、各 \(\iota\) 長が高々 \(b\) なので、一語 \(\le2\bar\theta_G+r_{\max}b\)。本文の \(1+\) は \(\|K\|_+\) の符号化分である。

`thm:data-from-typed-thickness` は \(\iota=\omega\) を各型付き非終端の最短**生成** yield として \(b=t_{\rm typ}\) とすれば得られる。`cor:distribution-representatives` は同値類内の最短（生成される必要はない）を選び \(b=\tau(G,s)\)。\(L_X\subseteq\operatorname{Cl}_{L,s}(X)\) より \(\tau\le t_{\rm typ}\)。各実現正型 \(m\in M_L\) に根の型付き非終端 \(S_{(m)}\) があり、\(\chi(S_{(m)})=\square_1\) なのでその同値類の全要素は正例 \(L\) の \(m\)-型を持ち、\(\tau_{S_{(m)}}\ge\mu_m(L)\)。従って \(\mu^\star(L,s)\le\tau(G,s)\)。短縮で結論が失われていない。

### C5. 挿入の事実：**誤り（字面の反例）／限定修正が必要**

対象：`prop:output-invariants`(iv)（854–867、2810–2822行）および `lem:witness-length-template`(i)（1116–1120、2899–2906行）。

**反例。** \(\Sigma=\{\mathtt a,\mathtt b\}\)、型半群 \(S=\{0,1\}\)（\(0\) は零元、\(1\) は単位元）、\(s(\mathtt a)=0\)、\(s(\mathtt b)=1\) とする。次の fan-out-one・非削除・非空・良形・reduced な文法を取る：

```text
S -> A
A -> a | a B
B -> b
```

\(A_{(0)}\) は \(A\Rightarrow\mathtt a\) により productive かつ成功導出内に現れるため、\(\widetilde G_0\) の型付き非終端である。しかし **full** refinement \(G^{\widehat s}\) は規則
\[
 A_{(0)}\longrightarrow \mathtt a\,B_{(0)}
\]
も含む（\(0\cdot0=0\)）。\(B_{(0)}\) は終端導出を持たない（\(B\Rightarrow\mathtt b\) は型 \(1\) のみ）ため、この規則はどの成功導出にも現れず \(\widetilde G_0\) から刈り込まれる。それでも
\(A_{(0)}\Rightarrow_{G^{\widehat s}}\mathtt a B_{(0)}\)
という**部分導出**は存在する。よって「すべての \(G^{\widehat s}\)-derivation from \(X\) が \(\widetilde G_0\) の規則だけを使う」は字面どおりには偽。

**正しい限定。** 「\(X\) から**終端 tuple までの導出**はすべて \(\widetilde G_0\) の規則だけを使う」は正しい。\(X\) は trimmed なので成功導出内に出現する。\(X\Rightarrow^*_{G^{\widehat s}}\mathbf u\) を**終端導出**とすれば、それを成功導出の \(X\)-部分木へ挿入できる。型付き規則が保存され、全体も成功導出となるので、置換後に使われる全規則は「何らかの成功導出に現れる規則」として trimming が保持する。このことから
\(L_X=\{\mathbf u:X\Rightarrow^*_{G^{\widehat s}}\mathbf u,\ \mathbf u\text{ terminal}\}\)
は正しい。`lem:witness-length-template`(i) で挿入するのは \(G\) の**終端** yield の unique lift なので、そこの議論はこの修正でそのまま成立する。

### C6. 小さな変更：**すべて正しい**

1. `prop:li-g-strict`(i)（2613–2618行）：\(\mathbf{LG}\) は部分半群、有限積、準同型像に閉じる擬多様体であり、局所自明半群の \(eSe=\{e\}\) と群自身を共に含む。したがって \(\mathbf{LI}\vee\mathbf{Grp}\subseteq\mathbf{LG}\)。**正しい**。
2. 付録B冒頭（2429–2436行）：有限モノイド \(eSe\) が群であることと、その唯一の冪等元が \(e\) であることは同値。任意の冪等元はある \(x^\omega\) なので、\((x^\omega yx^\omega)^\omega=x^\omega\) がちょうど全局所モノイドが群であることを述べる。**正しい**。
3. typing の直後（498–500行）：有限非空半群 \(S\) の最小 ideal は冪等元 \(f\) を含む。fresh identity \(\mathbf1_\sharp\notin S\) と \(f\) は相異なる冪等元で、\(\mathbf1_\sharp f=f\mathbf1_\sharp=f\)、\(f^2=f\)。ゆえに \(\{\mathbf1_\sharp,f\}\cong U_1\)。したがって \(S^\sharp\notin\mathbf{LG}\)。**正しい**。

## 4. 必要な修正の一覧

**必須：1件。** `prop:output-invariants`(iv) の量化を終端導出に限定し、その証明でも「終端」と明記する（上の C5 反例）。LaTeX の差し替え案：

```latex
\item For every typed nonterminal $X$ of $\widetilde G_0$, every
\emph{terminal} $G^{\widehat s}$-derivation
$X\Rightarrow^*_{G^{\widehat s}}\tuple u$ uses only rules of
$\widetilde G_0$; hence
$L_X=\{\tuple u:X\Rightarrow^*_{G^{\widehat s}}\tuple u\}$.
```

2818–2821行の証明の (iv) 部分は次に置き換えると誤読の余地がない：

```latex
For (iv), let $X\Rightarrow^*_{G^{\widehat s}}\tuple u$ be a
terminal derivation, and insert it at an occurrence of $X$ in a
successful derivation of $\widetilde G_0$.  Since typed rules depend
only on typed symbols, the result is a successful derivation of
$G^{\widehat s}$.  By the definition of trimming, every rule used
in the inserted terminal derivation belongs to $\widetilde G_0$.
```

**数値についての注記（原稿修正不要）。** 「定理の表示式は不変」と「展開された係数は不変」を区別する。\(f=1\)・非可換群の係数改善は意図した正しい改訂である。

## 5. 範囲外の指摘

なし。C5 の反例は指定範囲内の指摘である。

## 6. 実行したスクリプトと出力

検証Aは位数1–3の**ラベル付き全結合的半群**を全列挙し、長さ \(|T|\) の全積が \(T^1E(T)T^1\) に入ることを調べた。検証Bは \(S_3\)・位数8の二面体群 \(D_4\) で、各 owner に一つのブロックがあり定数を挟む一般の行を10,000例ずつ生成し、\(\kappa_p\) の重複から得た**連続 owner 区間**を直接代入して前後の行積一致を調べた。Bは**乱択検査であり全探索ではない**。

実行した Python 3 スクリプト（要点を省かず再実行できる形）：

```python
from itertools import product, permutations
import random

def small_semigroups(n):
    count = checks = 0
    for table in product(range(n), repeat=n*n):
        op = lambda a,b: table[n*a+b]
        if any(op(op(a,b),c) != op(a,op(b,c))
               for a in range(n) for b in range(n) for c in range(n)):
            continue
        count += 1
        E = {a for a in range(n) if op(a,a)==a}
        I = set(E)
        I |= {op(a,e) for a in range(n) for e in E}
        I |= {op(e,b) for e in E for b in range(n)}
        I |= {op(op(a,e),b) for a in range(n) for e in E
                                  for b in range(n)}
        for z in product(range(n),repeat=n):
            x=z[0]
            for y in z[1:]: x=op(x,y)
            assert x in I
            checks += 1
    print(f'n={n}: associative tables={count}, length-n products tested={checks}, failures=0')

for n in (1,2,3): small_semigroups(n)

P=list(permutations((0,1,2)))
ix={v:i for i,v in enumerate(P)}
S3=[[ix[tuple(a[b[i]] for i in range(3))] for b in P] for a in P]
S3e=ix[(0,1,2)]
D=list(product(range(4),range(2)))
dx={v:i for i,v in enumerate(D)}
D4=[[dx[((a[0]+(-b[0] if a[1] else b[0]))%4,
          (a[1]+b[1])%2)] for b in D] for a in D]
D4e=dx[(0,0)]

def trial(label, mult, identity, seed):
    rng=random.Random(seed)
    n=len(mult)
    inv=[next(j for j in range(n)
              if mult[i][j]==identity and mult[j][i]==identity)
         for i in range(n)]
    for _ in range(10000):
        orig=[rng.randrange(n) for _ in range(n)]
        repl=[rng.randrange(n) for _ in range(n)]
        fixed=[rng.randrange(n) for _ in range(n+1)]
        P=[identity]; Q=[identity]
        for i in range(n):
            P.append(mult[mult[P[-1]][fixed[i]]][orig[i]])
            Q.append(mult[mult[Q[-1]][fixed[i]]][repl[i]])
        k=[mult[P[i]][inv[Q[i]]] for i in range(n+1)]
        a,b=next((a,b) for a in range(n+1)
                            for b in range(a+1,n+1) if k[a]==k[b])
        val=identity
        for i in range(n):
            val=mult[mult[val][fixed[i]]][repl[i] if a<=i<b else orig[i]]
        assert mult[val][fixed[n]]==mult[P[n]][fixed[n]]
    print(f'{label}: 10000 random width-1 families with m={n} owners; '
          'all had preserving interval (0 failures)')

trial('S3',S3,S3e,20261106)
trial('D4',D4,D4e,20261107)
```

出力：

```text
n=1: associative tables=1, length-n products tested=1, failures=0
n=2: associative tables=8, length-n products tested=32, failures=0
n=3: associative tables=113, length-n products tested=3051, failures=0
S3: 10000 random width-1 families with m=6 owners; all had preserving interval (0 failures)
D4: 10000 random width-1 families with m=8 owners; all had preserving interval (0 failures)
```

**検証限界：** 乱択テストは任意サイズの群に対する定理の証明ではなく、本文で示した \(\kappa_p\) による鳩の巣が証明である。全半群検査も位数3以下に限る。また、C1–C6 を超える全文査読・LaTeXビルド・全補題の形式検証は実施していない。

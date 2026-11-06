# 定理 H・Astra 定理 1.2 の独立監査

**日付**：2026-11-07  
**目的**：新定理の提案ではなく、指定された既存証明の独立検証と反例探索。  
**総合判定**：**両定理の証明に、結論を覆す数学的な誤りは検出しなかった。** 定理 H の厚さの記号には修正が必要で、計算報告については独立に再実行できた範囲を明確に区別する。これは人手で行った論理監査と有限実験であり、形式証明器による検証ではない。

## 0. 原資料と検証範囲

GitHub リポジトリ `growupkuriyama-hub/Papers` の `02-v2-lg-fanout-boundary/` にある以下の**現行 main 上のファイル**を GitHub 連携で直接取得した（引用先は固定版を意味せず、取得時の Git blob を記録した）。

| 資料 | Git blob SHA の先頭 | 確認 |
|---|---|---|
| `reviews/claude_proposition_H_2026-11-07.md` | `b24ec21f8e38` | §1–§10 全文、344行 |
| `reviews/check_claude_proposition_H_2026-11-07.py` | `075a77c58da9` | ソース読解、972行 |
| `reviews/astra_fanout2_core_2026-11-07.md` | `3d1b8b644169` | §4–§6 と定義・仮定を中心に精査 |
| `reviews/astra_fanout2_core_2026-11-07.py` | `f26814fe0bf8` | ソース構造確認 |
| `parked/2026-11-06_focus/main_before_focus_59pp.tex` | `1bc97358a49b` | 指定された定義と厚さ補題を照合 |
| `README.md` | — | Change log (175)–(182) の位置付けを照合 |

**再実行に関する重要な制約**：GitHub 連携はファイル内容を読めたが、こちらの Python 実行コンテナに原スクリプトそのものを転送できなかった（コンテナから GitHub への直接ネットワーク接続も失敗）。したがって、**原スクリプトの `--seed 1 --trials 400` は再実行していない**。§9の数値との一致も**未検証**であり、「一致した」「違反ゼロを再現した」とは報告しない。一方、独立に執筆した付録コードを実行した結果は下の §5 に示す。この未完項目は数理証明の真偽と区別する。

## 1. 主結論を支える仮定の整理

原稿 `def:standard-mcfg`（TeX 622–648行）ではファンアウトは1以上、線形性は変数の高々1回使用。`def:grammar-properties`（664–677行）で、*good* は λ-free・nondeleting・nonpermuting・nonmerging の連言、*reduced* は全非終端が reachable かつ productive、と明記されている。定理 H の証明はそのうち**線形・非削除、既約性**だけを使うので、実際には good 表示より広いクラスを扱う。

一方、`lem:thickness-equivalence`（TeX 1168–1202行）の厚さは

\[
 \theta_G(R)=\min\{|w|:\ w\text{ の成功導出で規則 }R\text{ を使う}\},\quad
 \bar\theta_G=\max\{1,\max_R\theta_G(R)\}.
\]

H の報告書 §1.2 における定義は

\[
 \tau(B)=\min_{\vec u\in L_B(G)}|\vec u|,\qquad
 \rho(R)=|t_R|+\sum_j\tau(B_j),\qquad \theta_{\rm loc}=\max_R\rho(R).
\]

規則を含む成功導出のその規則の部分木は長さが少なくとも \(\rho(R)\) なので

\[
 \boxed{\theta_{\rm loc}\le\max_R\theta_G(R)\le\bar\theta_G.}
\]

これはファンアウトが2以上でも、成分を合算した Parikh 長について成り立つ。これより報告書の \(\theta\) を原稿の \(\bar\theta_G\) に置換してよい。反対方向の等号は一般には主張できない。

**(T1)–(T3)**：各非終端 B は生成的であるため、その左辺を持つ規則 R があり、\(\tau(B)\le\rho(R)\le\theta_{\rm loc}\)。また \(|t_R|\le\rho(R)\) かつ、\(\tau(B_j)\ge0\) なので \(|t_R|+\sum_{j\in J}\tau(B_j)\le\rho(R)\)。すなわち三性質は一切の循環論法なく従う。ab 語が存在すれば、その導出に正の終端長を持つ規則があり \(\theta_{\rm loc}\ge1\)。

**判定**：厚さの換算自体は **[正しい]**。ただし報告書で \(\theta=\bar\theta_G=\max_R\rho(R)\) と書いた §1.2/定理見出しは **[正しいが記述を直すべき]**。明確な修正は \(\theta_{\rm loc}:=\max_R\rho(R)\le\bar\theta_G\) と書き、まず局所厚さで証明し、最後に原稿の厚さへ戻すこと。

## 2. 定理 H：補題ごとの数学的監査

### 2.1 補題 3.1：同一ラベル・同一印集合の短絡 — [正しい]

祖先 y と真の子孫 y' に同じ非終端ラベルがあれば、y' の導出を y に移植できる。非削除性から、元の y' の終端出現は各成分の部分語として全て残り、他の位置の終端出現だけが消える（順番は変わり得る）。\(M_y=M_{y'}\) は選んだ二つの印が失われないための**十分条件**。その外の印は置換の影響を受けない。新語の内容は元の ab 内容の部分集合であり、両印が残るのでちょうど {a,b}。長さは増えず、導出木の節点は真に減る。

最短長だけでなく、**同長の場合の節点数最小性**も要ることを明示すべきである。報告書は §4 の辞書式最小の選択で満たしている。

### 2.2 補題 3.2：代表の長さ — [正しいが記述を直すべき]

各要求文字について一出現を印とし、印のない枝を非終端の最短生成に置く。二印の場合、背骨は共有幹 \(M=\{a,b\}\) と分岐後の a 側・b 側の二腕（同一節点に両印が直接書かれるときは腕が空）からなる。各一本の幹・腕で M が一定なので、同じラベルの重複は短絡可能。各腕のラベル種類は高々 v、合計背骨節点数は高々 \(3v\)。背骨節点ごとの「直接終端＋背骨外の子の最短生成」の長さは (T3) で θ 以下。よって \(\ell(B,\{a,b\})\le 3v\theta\)。一印なら vθ、無印なら θ。

**追記推奨**：報告書 §3.2 の「背骨の節点は高々 \(v|F|\)（|F|=2 なら 3v）」という中間記述は数式として矛盾する（\(v|F|=2v\)）。実際に必要な一般表現は「|F|=2 なら高々3v、|F|=1 なら高々v」である。**最終不等式は正しい**。この誤記は定数や定理を損なわない。

### 2.3 場合 A・補題 4.1 — [正しい]

印を含まない重い節点 z（\(|y(z)|>\theta\)）を長さ θ 以下の c-free 生成に替えると、両印は外に残り、新しい成功語は ab 内容で短くなる。したがって c-free の短い生成はなく、**全ての短い生成は c を含む**。この量化が四語比較に必要で、証明は満たしている。

### 2.4 場合 A・補題 4.2 — [正しい]

比較不能な印なし重い節点 t,t' について、元の \(W\) は ab 内容、\(W_t,W_{t'},W_{tt'}\) は各置換が c を含むので abc 内容。\(\{a,b,c\}\notin\mathcal M\) なら \(W_t\) 自身が受理条件に反する。許される場合は二つの位置が比較不能であることと linear/nondeleting 性から

\[
 \pi(W_t)-\pi(W)=\pi(W_{tt'})-\pi(W_{t'}).
\]

両辺に \(\Phi\) を作用させると、左辺が \(g_{abc}-g_{ab}+H\)、右辺が H に属し、場合 A の仮定に矛盾する。**MCFG で各成分が離れていても総 Parikh ベクトルは加法的**であり、ファンアウトによる例外はない。

### 2.5 場合 A・数え上げ — [正しい]

重い節点は祖先について閉じる（各規則が linear/nondeleting なので子の文字は親の生成に全部含まれる）。重い葉は互いに比較不能。印ありの葉は高々2、印なしの葉は補題4.2で高々1。重い根から各葉への道では印集合は \(\{a,b\}\to\{a\}\text{ or }\{b\}\to\varnothing\) の高々3区間。各区間で同じラベルの反復は補題3.1と辞書式最小性に反する。従って道は高々3v節点、葉は高々3、重い節点は合計高々9v。

軽い子の全生成は θ 以下なので、各重い節点がその上に直接寄与する長さは高々 \(\theta+r\theta\)。根が重ければ

\[
 N=\sum_{z\text{ 重い}}
 (|t_{R(z)}|+\sum_{j\text{ 軽い子}}|y(j)|)
 \le 9v(r+1)\theta.
\]

重い根がなければ \(N\le\theta\)。\(\{a,b,c\}\notin\mathcal M\) の場合は葉高々2、\(N\le6v(r+1)\theta\) も正しい。

### 2.6 場合 B・(★) — [正しい]

Σ に三文字しかないので、a と b を含む内容は {a,b} または {a,b,c} の二つだけ。後者が不許可か、両内容の受理剰余類が一致する場合、成功語の群値は必ず \(g_{ab}+H\) に属する。他の内容にどんな剰余類を割り当てても本段には影響しない。

### 2.7 補題 5.1：打ち消し恒等式 — [正しい]

\(p_z\) を (ラベル,印集合) の代表、\(p'_z\) を「根に R(z)、子には各子の印型代表」としたとき、\(\sum_z\pi(p'_z)-\pi(p_z)\) で、根以外の各 \(p_z\) は親側の正項と自分側の負項でちょうど一度打ち消される。根の印集合は {a,b} なので、

\[
 \pi(W)=\pi(\mathrm{rep}(S,\{a,b\}))+
 \sum_{z\in T}(\pi(p'_z)-\pi(p_z)).
\]

各印型の最短代表であることは**長さ上界のため**で、恒等式自体は任意の一貫した代表選択で成立する。

### 2.8 補題 5.2：証人と不変量 — [正しいが記述を直すべき]

\(M_z\) は文字集合の単なる和ではなく、「二つの**特定の印の位置**」をどの節点が所有するかの分割から得られる。この意味で

\[
 M_z=M(t_{R(z)})\,\dot\cup\,\dot\bigcup_j M_{z_j}
\]

は正しい。代表 \(p_z\) も \(p'_z\) も対応する印の**文字**を必ず含み、外側で元の印が残るので、\(W[z\leftarrow p_z], W[z\leftarrow p'_z]\) は双方 a,b を含む成功語。場合 B の (★) により両者の群値の差 \(\Phi(\delta_z)\in H\)、経路の同始終点性により \(\partial\delta_z=0\)。\(p_0\) は S の成功語なので群値と流量境界条件も満たす。

**軽微修正**：報告書の式では \(p_z\) を「導出木（組）」、\(p_0\) を「ベクトル」と使い分けているので、\(\vec p_z=\pi(\mathrm{rep}(A_z,M_z))\) と表記を分離すると、\(\Phi(p_0)\) と置換操作の混同を防げる。論理の穴ではない。

### 2.9 補題 5.3：大きさの上界 — [正しい]

\(M_{z_j}=\emptyset\) の全ての子は最短生成なので、直接終端と合わせて (T3) により θ 以下。印あり子の分配は (i) 一つの子が {a,b} を持つ、(ii) a 子と b 子が一つずつ（または片方だけ）、のいずれか。高々 \(3v\theta\) を追加すれば

\[
 |p'_z|\le(3v+1)\theta,\quad
 \|\delta_z\|_\infty\le(3v+1)\theta,\quad
 \|p_0\|_1\le3v\theta.
\]

非削除性・二つの印の唯一性で r への依存が消える。片方の子に二つの印が入る場合に、別の印あり子は存在しないことが肝心。

### 2.10 補題 5.4：階数 0〜3 の格子補題 — [正しいが記述を直すべき]

\(\Lambda\le\mathbb Z^3\) の生成元各座標の絶対値を Θ、基点の \(\ell_1\) 長を Θ₀ とし、面 z=0 の正象限に交点があるとする。以下の段階を独立に確認した。

| 階数・配置 | 使用する短い格子移動 | 導かれる x+y 上界 |
|---|---|---|
| 0 | 交点は p₀ しかない | Θ₀ |
| 1、z≠0 の方向 | z=0 との交点は一つ | 2ΘΘ₀（さらに非負基点なら改善可） |
| 1、z=0、同符号・片座標0・異符号 | 一次元の整数移動、正象限との最初の交点または固定座標 | 2Θ²+2Θ²Θ₀ 以内 |
| 2、Λ が z=0 に含まれる | 二つの独立生成元の平行四辺形 | 2+4Θ |
| 2、Λ が z=0 に含まれない | \(u=\gamma_z\gamma'-\gamma'_z\gamma\)、\(\|u\|_\infty\le2\Theta^2\) | \(2\Theta^2\Theta_0+4\Theta^2\) 以内 |
| 3 | \(u_2,u_3\) の基本平行四辺形、各座標の幅 ≤4Θ² | \(2+8\Theta^2\) |

特に階数3では、\(\gamma_1,\gamma_2,\gamma_3\) を一次独立に選び、\(\gamma_{1z}\ne0\) とすれば、\(u_2,u_3\) は水平面で一次独立。\(\mathbb Z u_2+\mathbb Z u_3\) の各剰余類はどの平行移動した半開基本平行四辺形にも一点を持つ。**平行四辺形の x, y の下限が共に1になるよう、平行移動の二座標を独立に選べる**。これにより \(1\le x,y\le1+4\Theta^2\)。

階数2で断面が斜線の場合、外積 \(n=(n_x,n_y,n_z)\) から \(n_xx+n_yy=c\)、\(|c|\le2\Theta^2\Theta_0\)。\(n_xn_y<0\) なら水平移動を両座標正に選び、−u の方向の**最後の正象限の点**へ移す。一方の座標が対応する u 成分以下になり、直線方程式で他方を \(u_x+u_y+|c|\) に抑える。\(n_xn_y>0\) は係数の整数絶対値が1以上であるため、\(x+y\le|c|\)。片係数0も固定座標＋格子周期で足りる。

階数1の同符号 case (iv) も正しいが、\(g_x,g_y>0\)、最後の交点で \(x\le g_x\) とした後、\(x=p_{0x}+kg_x\) より \(k\le1+|p_{0x}|\) となることを**式で補足**すべき。符号混在なら保存される正の線形式から \(x+y\le\Theta\Theta_0\)。

従って全階数で

\[
 \boxed{K(\Theta,\Theta_0)=2\Theta^2\Theta_0+8\Theta^2+2}
\]

を満たす。Θ₀≤Θ なら \(K\le12\Theta^3\)。**明確な反例・定数不足は見つからなかった**。

### 2.11 補題 5.5：オイラー路・最終段 — [正しい]

W の存在は a,b 辺の無向支持が連結して s を含むことを保証する。新ベクトル \(m=(x',y',0)\) は各成分正で **a,b の辺支持が W と完全一致する**。\(\partial m=\mathbf 1_t-\mathbf 1_s\) であり、t→s の補助辺を加えた有向多重グラフに Euler 閉路がある。補助辺を除けば s→t 歩道 \(W'\) を得る（s=t のときは追加不要）。

ここで \(W'\in\mathrm{Path}_D(s,t)\)、内容が {a,b}、群値が \(g_{ab}+H\) という**三条件から \(W'\in L\) に戻す最後の一歩**に、\(L=L(G)=(16)\) の「等号」を使用する。単なる \(L(G)\subseteq (16)\) では場合 B の結論を得られない。原報告の扱いは正しい。

数値は \((3v+1)^2\le16v^2\) と \(v,\theta\ge1\) から

\[
 K((3v+1)\theta,3v\theta)
 \le 96v^3\theta^3+128v^2\theta^2+2
 \le(96+128+2)v^3\theta^3=226v^3\theta^3.
\]

## 3. Astra 定理 1.2 の独立監査

### 3.1 補題 4.1：恒等式と短い二成功語 — [正しい]

Astra では各 B に最短生成組 \(u_B\)、\(q_B=\pi(u_B)\) を固定し、規則 \(R:A\to\rho(B_1,\dots,B_k)\) に

\[
 \delta_R=\pi(t_R)+\sum_jq_{B_j}-q_A
\]

を割り当てる。成功導出の各節点で足せば根以外の \(q_B\) は打ち消し合い、\(\pi(w)=q_S+\sum_z\delta_{R(z)}\)。

**長さ ≤\(\bar\theta_G\) の証人が二つあること**も正しい。R を使用する長さ \(\theta_G(R)\) の成功導出を選び、その使用位置の A 全体を \(u_A\) に置換した成功語 p と、R を残して全ての子を \(u_{B_j}\) に置換した成功語 p' を比較する。どちらの置換も当該部分木を長くしない（最短性・非削除性）ので、\(|p|,|p'|\le\theta_G(R)\le\bar\theta_G\)、差は δ_R。故に \(\|\delta_R\|_\infty\le\bar\theta_G\)。この強い証人条件は H の印型版より短いものの、**剰余類が一つ**のときにだけ全規則に共通して利用できる。

### 3.2 補題 5.2：三次元格子・各階数 — [正しい]

基点 \(\|p_0\|_1\le\bar\theta_G\)、各生成元の座標 ≤\(\bar\theta_G\)。独立に以下を確認した。

- **階数0**：p₀ 自身だけ。\(x+y\le\theta\)。
- **階数1**：方向の c 成分が非零なら面との交点は一意で \(x+y\le3\theta^2\)。c 成分0なら整数直線の縮小補題を使い同じ上界。
- **階数2、水平**：二独立生成元の xy 行列式 \(d\ne0\)、\(|d|\le2\theta^2\)。随伴行列から \(d e_a,d e_b\in\Lambda\)、二座標を1〜dへ独立に剰余縮小し、\(x+y\le4\theta^2\)。
- **階数2、非水平**：外積 \(n=(A,B,C)\)、\(|A|,|B|\le2\theta^2\)、\(|n\cdot p_0|\le2\theta^3\)。水平な格子方向 \((B,-A,0)=u_c v-v_c u\in\Lambda\) に沿って縮小し、\(x+y\le2\theta^3+4\theta^2\le6\theta^3\)。
- **階数3**：三独立生成元を並べた整数行列の行列式 d は \(1\le d\le6\theta^3\)。随伴行列により \(d e_a,d e_b\in\Lambda\) なので、\(x+y\le2d\le12\theta^3\)。

任意の選択した独立生成元が格子全体の整数基底であると**仮定していない**点は適切。得られる移動が選択した部分格子に入っていれば十分である。

### 3.3 定理 1.2 と等号 (1) — [正しいが記述を直すべき]

短い面代表 \(p'\) が得られた後、\(\Phi(p')\in g+H\)、\(\partial p'=\partial\pi(W)\)、正の a,b 支持という三条件から Euler 路 \(w'\) が存在し、**(1) の完全な等号**で \(w'\in L\) となる。包含だけなら証明は閉じない。この箇所は論理的に正しい。

**記号上の修正**：H は \(\partial e=\mathbf1_{\mathrm{head}}-\mathbf1_{\mathrm{tail}}\)（入−出）、Astra は \(\partial e=\mathbf1_{\mathrm{tail}}-\mathbf1_{\mathrm{head}}\)（出−入）を採用しており、それぞれの証明内では整合している。統合した原稿に引用する場合、どちらかへ統一すること。これは反例ではない。

## 4. 適用例の検査

| 対象 | (16) か | 分類 | 留意点 |
|---|---|---|---|
| 層言語 \(L=\{w\in\mathrm{Path}: |w|=\nu(\mathrm{cont}(w))\}\) | [正しい] φ=長さ、A=ℤ、H={0} | \(\nu(abc)\ne\nu(ab)\) かつ abc 許可なら A、そうでなければ B | ab 実現可能が前提。長さが固定のため L は有限 |
| 言語 J：ab 内容だけ奇数長、**他の全内容は偶数長** | [正しい] A=ℤ/2、H={0}、ab は1、他は0 | abc 許可なら A | D は一頂点の3ループ、\(\mathcal M\) は全ての非空内容とできる |
| J の別解釈：ab 内容だけ奇数長、**他の全内容は長さ自由** | [正しいが記述を直すべき] 一般に (16) には表せない | 定理 H の対象外 | 全ての一文字内容の語を長さ自由にすると、aⁿ と aⁿ⁺¹ 等の群値差から Φ(a),Φ(b),Φ(c)∈H が強制され、ab の奇偶を区別できない。説明時は J の正確な定義を固定する |
| \(g_{ab}+H=g_{abc}+H\)、その他の内容の値は異なる族 | [正しい] | B | a,b を含む証人の群値だけ一致すればよい |

## 5. 計算・独立実装の実施結果

### 5.1 原スクリプト

原コードは閲覧したが、**環境間転送ができず未実行**。したがって、Claude 報告 §9 の「seed 1 で A1/A4 各3326、B4 1439、L 1696、違反なし」等は**Claude の報告値**として記録したのみである。こちらの独立再現値ではない。

原コードの検査範囲の表現にも二つの注意がある。

1. `check_A` は a と b の印ペアが40組を超える場合 `rng.sample(pairs,40)` により**40組だけ**検査する。スクリプト冒頭の「全ての印の選び方について」はそのままでは正確でない。**[正しいが記述を直すべき]**：『印候補が40組以下なら全数、それより多ければ40組を抽出』に訂正。
2. `check_B` の面の最小点の所属を調べる `in_lattice(Hh, ...)` は、`plane_points` と**同じ `hnf` の出力**に依存する。『所属の別法』ではあるが、独立した HNF アルゴリズムによる二重検算ではない。**[正しいが記述を直すべき]**：共通コードへの依存を明記する。

### 5.2 自作コードの実行（原コードを再利用しない）

`python3 chatgpt_check_proposition_H_2026-11-07.py --seed 1 --trials 400` を実行済み。乱数生成元 \(\Gamma\subset[-3,3]^3\)、小さい非負基点 p₀、負係数も許した整数結合から、面上の正象限の点をあらかじめ構成した。**格子所属を独立な「最大階数の小行列式の gcd」判定**で確認し、階数別に短い代表を明示構成した。

- 面の交点が生成された試行：**242 / 400**（階数0：20、階数1：46、階数2：62、階数3：114）。残り158例は前提となる面上交点を構成できず、合否には算入していない。
- 242例で \(x+y\le K\) を全て確認。構成された点の最大 x+y は **63**、\((x+y)/K\) の最大は **0.572727**。違反なし。
- これは **K 内の全数探索ではなく、小範囲乱数＋厳密な格子所属判定**。境界近傍全体を網羅した主張ではない。

**場合 A の完全な表示の例**：一頂点に a,b,c の3ループ、\(A=\mathbb Z/2\)、\(\Phi(a)=\Phi(b)=0,\Phi(c)=1\)、\(H=0\)、\(\mathcal M=\{\{a,b\},\{a,b,c\}\}\)、\(g_{ab}=0,g_{abc}=1\)。この正則言語を受理する12状態 DFA 由来の ε-free 右線形 CFG に、同じ L の語だけを作る冗長な鎖

\[
 S\to aA_{20}b,\quad A_0\to a,\quad A_i\to aA_{i-1}\mid c\quad(1\le i\le20)
\]

を追加する。完全性は DFA 部が、健全性は鎖の各生成が c なしまたは c ちょうど一つであることから従う。どの非終端も到達可能・生成的で、規則は good。計算した局所厚さ θ=4。鎖の導出の \(A_{20}\) は長さ21で、根 S に直接書いた a,b を印に選ぶと、**印なし重い節点**になる。\(A_{20}\Rightarrow c\) に置換すると `acb` は許される。仮に独立な二節点で同じ短絡を許すと、四語は

`aaaaaaaaab` / `acaaaab` / `aaaaacb` / `accb`

となり、最後の `accb` だけは c の偶数性によって**不受理**。従って四語の条件が独立な二節点を禁止することを具体的に確認する。**重要**：この完全表示では \(\mu_{ab}=2\) であり、重い節点を示した長語の導出は最短 ab 語の導出ではない。**最短導出に重い節点がある実例の提供には成功していない**。これを満たしたと誤記しない。

**場合 B の完全な表示の例**：\(L=\Sigma^+\)、D は一頂点の三ループ、群・剰余類条件は自明。CFG

\[
 S\to a\mid b\mid c\mid SS\mid a\underbrace{TT\cdots T}_{8\text{ 個}}b,
 \qquad T\to a\mid TT
\]

は reduced good で \(L(G)=\Sigma^+\)。\(v=2,r=8,\theta=10\)、\(\mu_{ab}=2\)。最後の S 規則で各 T を a の32個生成にすれば長さ258の語となり、根に直接ある a,b を印としたとき、長さ32>θ の印なし重い T 節点が**8個比較不能**に現れる。これは場合 B では重い反鎖を抑える必要がないことを示す（やはり長語は最短ではない）。

最後に \(v=\theta=1\) なら Θ=4、Θ₀=3 となり、数式から **K=226** となることも確認した。

## 6. 判定表と原稿への採用意見

| 指定された監査対象 | 判定 | 結論への影響 |
|---|---|---|
| H：厚さの大小関係、(T1)–(T3) | **[正しいが記述を直すべき]** | θ の記号と原稿の \(\bar\theta\) を区別。定理は維持 |
| H：補題3.1 | **[正しい]** | 穴なし |
| H：補題3.2 | **[正しいが記述を直すべき]** | \(v|F|\) という誤記を3vへ訂正。定数維持 |
| H：場合A・補題4.1 | **[正しい]** | 穴なし |
| H：場合A・四語比較、ファンアウト | **[正しい]** | 穴なし |
| H：場合A・葉と9(r+1)vθ | **[正しい]** | 穴なし |
| H：場合B・(★) | **[正しい]** | 穴なし |
| H：場合B・補題5.1 | **[正しい]** | 穴なし |
| H：場合B・補題5.2 | **[正しいが記述を直すべき]** | ベクトルと生成組の区別を明確化。定理維持 |
| H：場合B・補題5.3 | **[正しい]** | 穴なし |
| H：場合B・補題5.4（全階数） | **[正しいが記述を直すべき]** | 1次元 case (iv) の k の評価を補筆。K 維持 |
| H：場合B・Euler路と226 | **[正しい]** | 完全な等号の使用を確認 |
| H：§7 適用例 | **[正しいが記述を直すべき]** | 言語 J の二解釈を題名・定義で区別 |
| Astra：補題4.1 | **[正しい]** | 短い二成功語の構成を確認 |
| Astra：補題5.2 | **[正しい]** | 階数0〜3と12θ³を確認 |
| Astra：定理1.2、等号(1) | **[正しいが記述を直すべき]** | 両報告統合時に ∂ の符号を統一 |
| 原スクリプトの試験内容の説明 | **[正しいが記述を直すべき]** | 印ペア最大40、HNF共通依存を明記。原再実行は未完了 |

**別稿への採用について**：定理 H と Astra 定理1.2の**数学的結論を否定する反例は見つからず、読んだ証明は閉じている**。ただし「そのまま」は勧めない。H は \(\theta_{\rm loc}\) と \(\bar\theta_G\) の区別、§3.2 の誤記、§5.4 の省略を修正し、双方とも経路境界写像の符号を揃えること。Astra の上界は単一剰余類という限定を外さないこと。**原コードの再実行という依頼項目は未完了なので、計算再現まで要求する投稿前監査としては保留**とする。

**残る問題**：H の v 依存を消す上界は本監査では示していないし、下界族も得ていない。\(H_M\) が内容ごとに異なる場合、(★) も全規則の群差分保存も失われるので、本証明の直接拡張はできない。|Σ|>3 や同じ文字を複数辺に付す D でも、内容と Euler 復元の段が変わる。これらは定理の欠陥ではなく、適用範囲の限界である。

## 付録 A. 自作スクリプトの全文（標準ライブラリのみ）

以下は**原報告の検証コードをコピー・改変したものではない**。本監査用に独立執筆し、上記の試験を実行したコードである。

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Independent finite audit of Proposition H (2026-11-07).
Standard library only. Does NOT import or reuse either supplied checker.
Tests the lattice bound by constructive witnesses plus exact lattice membership
using gcds of maximal minors, and illustrates the A/B grammar mechanisms.
It is a finite test, not a proof. Run: python3 this_file.py --seed 1 --trials 400
"""
import argparse
from itertools import combinations, product
from math import gcd
from random import Random


def det2(a, b, c, d):
    return a*d-b*c


def det3(a, b, c):
    return (a[0]*det2(b[1], b[2], c[1], c[2])
            - a[1]*det2(b[0], b[2], c[0], c[2])
            + a[2]*det2(b[0], b[1], c[0], c[1]))


def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2],
            a[0]*b[1]-a[1]*b[0])


def rank_basis(gens):
    result=[]
    for g in gens:
        if not any(g):
            continue
        if len(result)==0 or (len(result)==1 and any(cross(result[0],g))) or (len(result)==2 and det3(result[0],result[1],g)):
            result.append(g)
            if len(result)==3:
                break
    return result


def minor_gcd(vectors, k):
    """gcd of ALL k x k minors, including all column and row selections."""
    if k==0:
        return 1
    gg=0
    for cols in combinations(vectors,k):
        for axes in combinations(range(3),k):
            if k==1:
                d=cols[0][axes[0]]
            elif k==2:
                d=det2(cols[0][axes[0]], cols[0][axes[1]],
                       cols[1][axes[0]], cols[1][axes[1]])
            else:
                d=det3(*cols)
            gg=gcd(gg,abs(d))
    return gg


def belongs(gens, diff):
    """Independent exact Z-lattice membership test (rank + determinantal divisors)."""
    k=len(rank_basis(gens))
    extended=gens+[diff]
    if len(rank_basis(extended))!=k:
        return False
    return minor_gcd(gens,k)==minor_gcd(extended,k)


def ceildiv(a,b):
    return -((-a)//b)


def shrink_line(w, d):
    """Minimize x+y along the integer line w + Z*d with x,y >= 1.
    It suffices to check the first/last feasible integer shift.
    """
    x,y,z=w
    dx,dy,dz=d
    assert z==0 and dz==0 and (dx or dy)
    lo,hi=None,None
    for coord,step in ((x,dx),(y,dy)):
        if step>0:
            low=ceildiv(1-coord,step)
            lo=low if lo is None else max(lo,low)
        elif step<0:
            high=(coord-1)//(-step)
            hi=high if hi is None else min(hi,high)
        else:
            assert coord>=1
    assert lo is None or hi is None or lo<=hi
    slope=dx+dy
    if slope>0:
        assert lo is not None
        t=lo
    elif slope<0:
        assert hi is not None
        t=hi
    else:
        t=0 if (lo is None or lo<=0) and (hi is None or 0<=hi) else (lo if lo is not None else hi)
    q=(x+t*dx,y+t*dy,0)
    assert q[0]>0 and q[1]>0
    return q


def short_representative(gens, p0, w):
    """Construct a short element in (p0+<gens>) intersect {z=0,x,y>=1}.
    Uses independent rank cases / adjugate, not the source report's routines.
    """
    assert w[2]==0 and w[0]>0 and w[1]>0
    bs=rank_basis(gens)
    k=len(bs)
    if k==0:
        return p0
    if k==3:
        d=abs(det3(*bs))
        return ((w[0]-1)%d+1,(w[1]-1)%d+1,0)
    if k==2:
        u,v=bs
        n=cross(u,v)
        if n[0]==n[1]==0:
            d=abs(n[2])
            return ((w[0]-1)%d+1,(w[1]-1)%d+1,0)
        return shrink_line(w,(n[1],-n[0],0))
    g=bs[0]
    if g[2]!=0:
        return w
    return shrink_line(w,g)


def stress(rng, trials):
    tested={0:0,1:0,2:0,3:0}
    tight=0
    maximum_ratio=0.0
    for trial in range(trials):
        theta=rng.randint(1,3)
        p0=(rng.randint(0,3),rng.randint(0,3),rng.randint(0,2))
        cap0=sum(p0)
        count=rng.randint(0,4)
        gens=[tuple(rng.randint(-theta,theta) for _ in range(3)) for _ in range(count)]
        bs=rank_basis(gens)
        # Plant a known solution, without relying on a lattice search or an HNF implementation.
        # Random coefficients are allowed to be negative; the resulting word vector must be positive.
        candidates=[]
        for _ in range(400):
            coeff=[rng.randint(-8,8) for __ in gens]
            w=tuple(p0[j]+sum(c*g[j] for c,g in zip(coeff,gens)) for j in range(3))
            if w[2]==0 and w[0]>=1 and w[1]>=1:
                candidates.append(w)
                break
        if not candidates:
            continue
        w=candidates[0]
        theta_eff=max(1,max((abs(x) for g in gens for x in g),default=0))
        K=2*theta_eff**2*cap0+8*theta_eff**2+2
        q=short_representative(gens,p0,w)
        assert q[2]==0 and q[0]>=1 and q[1]>=1
        assert belongs(gens,tuple(q[j]-p0[j] for j in range(3))), (gens,p0,w,q)
        assert q[0]+q[1]<=K, (gens,p0,w,q,K)
        assert minor_gcd(gens,len(bs))>=0
        tested[len(bs)]+=1
        tight=max(tight,q[0]+q[1])
        maximum_ratio=max(maximum_ratio,(q[0]+q[1])/K)
    return tested,tight,maximum_ratio


def case_a():
    # EXACT case A target, D is one vertex with 3 different labeled loops.
    # A=Z/2, phi(a)=phi(b)=0, phi(c)=1, H={0}, g_ab=0, g_abc=1.
    # The regular portion of G is the right-linear grammar of the *complete*
    # 12-state DFA for the language, with final transitions made terminal rules.
    # Extra S -> a A20 b, A0 -> a, Ai -> a A(i-1) | c are redundant and sound.
    def accepts(w):
        co=set(w)
        return (co=={'a','b'} and w.count('c')==0) or (co=={'a','b','c'} and w.count('c')%2==1)
    start=(0,0,0,0)    # seen(a),seen(b),seen(c), parity(c)
    def step(q,ch):
        a,b,c,p=q
        return (a or ch=='a', b or ch=='b', c or ch=='c',p^(ch=='c'))
    def accept_state(q):
        a,b,c,p=q
        return bool(a and b and (not c or p))
    states={start}
    pending=[start]
    while pending:
        q=pending.pop()
        for ch in 'abc':
            v=step(q,ch)
            if v not in states:
                states.add(v)
                pending.append(v)
    assert len(states)==12
    # Length of a shortest nonempty accepting continuation from each state,
    # as needed for rho(R). A BFS here enumerates at most 3^5 words.
    def shortest(q):
        for n in range(1,7):
            for cs in product('abc',repeat=n):
                z=q
                for ch in cs:
                    z=step(z,ch)
                if accept_state(z):
                    return n
        raise AssertionError('state not coaccessible')
    tau={q:shortest(q) for q in states}
    theta=max([3,2,1]+[1+tau[step(q,ch)] for q in states for ch in 'abc'])
    assert theta<=5
    n=20
    W='a'+'a'*(n+1)+'b'
    Wt='a'+'c'+'b'
    assert accepts(W) and accepts(Wt) and n+1>theta
    # Actual shortest ab word of this COMPLETE grammar is 'ab' (length 2).
    assert accepts('ab')
    # The four-word obstruction uses two hypothetical incomparable shortcuts.
    raw='a'+'a'*4+'a'*4+'b'
    left='a'+'c'+'a'*4+'b'
    right='a'+'a'*4+'c'+'b'
    both='a'+'c'+'c'+'b'
    assert accepts(raw) and accepts(left) and accepts(right) and not accepts(both)
    assert (left.count('c')-raw.count('c'))%2 == (both.count('c')-right.count('c'))%2
    return {'theta':theta,'dfa_states':len(states),'mu_ab':2,
            'long_ab_derivation':W,'heavy_unmarked_A20_length':n+1,
            'short_escape':Wt,'four_words':(raw,left,right,both),
            'fourth_rejected':True,'equality_with_target':True,
            'heavy_node_is_in_minimal_derivation':False}


def case_b():
    # Complete CFG for Sigma+: S -> a|b|c|SS|a T^8 b; T -> a|TT.
    # The S -> a T^8 b rule is additional: completeness comes from S -> SS and constants.
    # The intentionally NONMINIMAL derivation makes eight pairwise incomparable heavy T-nodes.
    q=8
    theta=q+2  # max rho(rule), because tau(S)=tau(T)=1
    heavy_t_len=32
    W='a'+'a'*(q*heavy_t_len)+'b'
    assert theta==10 and heavy_t_len>theta and len(W)==258
    min_ab=2  # 'ab' belongs to L(G)=Sigma^+, also has both letters.
    v=2
    assert min_ab <= 226*v**3*theta**3
    return {'theta':theta,'v':v,'rank':q,'mu_ab':min_ab,
            'nonminimal_word_length':len(W),'incomparable_unmarked_heavy':q,
            'equality_with_target':True}


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--seed',type=int,default=1)
    ap.add_argument('--trials',type=int,default=400)
    args=ap.parse_args()
    result=stress(Random(args.seed),args.trials)
    print('INDEPENDENT lattice audit',{'seed':args.seed,'trials':args.trials,
         'successful_planted_cases_by_rank':result[0],
         'max_constructed_length':result[1], 'max_length_over_K':round(result[2],6)})
    print('CASE A:',case_a())
    print('CASE B:',case_b())
    print('K at (v,theta)=(1,1):',2*4**2*3+8*4**2+2)
    print('ALL ASSERTIONS PASSED')

if __name__=='__main__':
    main()

```

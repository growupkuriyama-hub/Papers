# Fable independent exploration — Theorems A/B/C, certificate, reproducible sources and audits

**Research archive — original unmodified inputs**, not changes to `main.tex`.

Each file body is UTF-8 text preserved byte-for-byte. Extract by reading the `bytes` value and slicing that many bytes after the header newline. SHA-256 verifies integrity.

The boundaries use bytes, so an original file without a final newline is preserved.

```python
from pathlib import Path
import re, hashlib
b=Path(__file__).read_bytes()
pat=re.compile(rb"^===== BEGIN FILE (.*?) bytes=(\d+) sha256=([a-f0-9]{64}) =====\n",re.M)
for m in pat.finditer(b):
    name=m.group(1).decode("utf-8")
    size=int(m.group(2)); data=b[m.end():m.end()+size]
    assert hashlib.sha256(data).hexdigest()==m.group(3).decode()
    p=Path("extracted")/name; p.parent.mkdir(parents=True,exist_ok=True); p.write_bytes(data)
```

## Manifest

| Path | Size (bytes) | SHA-256 |
|---|---:|---|
| `Fable_C_complete_independent_mathematical_audit_2026-11-15.md` | 17724 | `63be1443497ba90d945c04e1ed7895fa220fc9f464e4d9b0416b5a5a416e72d2` |
| `Fable_original_open_problem_report_2026-11-15.md` | 27376 | `c0369cdc571944bfe702e52a3571939bc5981c332637bf8c49765ebc3e3ca223` |
| `L2.txt` | 53 | `286d7916fd30d54f799aa7597cd6b6d9164edf88c504c5baee01a62682714a1c` |
| `L3.txt` | 737 | `a3c44ea863d82881abee40a9368ddd629a9f2edec29b8920aca7d03ddbdedca3` |
| `PROMPT_FABLE_FANOUT_TWO_OPEN_PROBLEM_FREEDOM_2026-11-15.md` | 13168 | `6efd5907537c20688ebbf6f88324ca8306d6a6d5671b0ad294886d271d3c692b` |
| `V3.txt` | 736 | `d47d8cbdf1b596e60257afef69d72012bd9d04f732deea367fc98163bdad988a` |
| `audit_fable_fanout2_independent_2026-11-15.md` | 9775 | `19c88f1a1f65ae2faa3214f8aab622339a12475a99395d1dd55dd3789fa09352` |
| `build_cert.py` | 3568 | `791271975ba1ba70ccbc5b9e9edbbcfdef9535bd4f131d3d181ea644d0eaca4f` |
| `cert_L3_to_baab_pruned.json` | 4905 | `7188c424fce6f372468cf46b274a9e680927d2355266e25b9d2163f3a07df7c0` |
| `cfree_search.cpp` | 2983 | `322957ea7109df3f8ce5f004fdb9fe5a509913418217ee4e22fa3050f875ea21` |
| `check_fable_C_independent.py` | 7662 | `fa4af3cbc8ce1af719fa99e96d3d96486b7f413232bb8b93643e55b59060f2f5` |
| `clos.cpp` | 5732 | `187a0f2ad1a2d8d32cce975eb74c7abed94f70da182d672e8ea893d7196da089` |
| `closure.py` | 2563 | `58c5fff3e3337ea8b3cebfe9579802b6b77ef7ab949ae00c1d07b20f077bf676` |
| `experiments_log.txt` | 2849 | `05bd9e22dfbb4ebcce6ffdb8d5baf8664575f0a2ed7aac269f1e70fab95083ac` |
| `fable_fanout2_open_problem_report.md` | 27376 | `c0369cdc571944bfe702e52a3571939bc5981c332637bf8c49765ebc3e3ca223` |
| `independent_cert_audit.py` | 2778 | `bd575fec785315e048d549e5ff380f913a28f6c74689e43275838a52808ea125` |
| `independent_cert_log.txt` | 412 | `58398972f9419afdf5f2ef9a3c11a29131f097df3068ede6837886125070a4cf` |
| `independent_check_log.txt` | 241 | `540bd1e59acb4e30457c04b78b4b7cc2fed9b0f108d5ba22a5a75ce8269f4fe2` |
| `verify_cert.py` | 2748 | `03f04263b5dbd0e96664f8ad606ee3e868f7f035068452de899fcbb6fc29db9e` |
| `verify_log.txt` | 1170 | `64b957d464aefa1c62b89ec98c6dd60126cb1929e95bd9c8db27fccc6ea60c13` |

## Original source bodies


===== BEGIN FILE Fable_C_complete_independent_mathematical_audit_2026-11-15.md bytes=17724 sha256=63be1443497ba90d945c04e1ed7895fa220fc9f464e4d9b0416b5a5a416e72d2 =====
# Fable-C：可換・半束型付き組代入可能言語の単項語長上界 — 独立完全数学監査

**監査日**：2026-11-15（JST）  
**対象**：ユーザー提供 `新しいフォルダー(20261115-114855).zip` 中の `fable_fanout2_open_problem_report.md` §5（補題5.1・定理C）、既存の初回監査 `audit_fable_fanout2_independent_2026-11-15.md`、および現行 #2 MCFG `main.tex` の `def:grammar-properties`, `def:tuple-substitutable`, `lem:thickness-equivalence`。  
**方法**：原報告を独立に読み、§5(0)–(7) をそのまま引用せず各論証を再構成。明示的な受理文脈、整数係数、木の包含関係、窓幅と次数を検算。独立コードで境界事例の有限ストレス検査を実施。Fableのチェックコードは流用していない。  
**総合判定**：**VALID AS A MATHEMATICAL HAND-PROOF, WITH EXPLICIT CLARIFICATIONS**。以下の補足を入れると、定理Cの手証明は論理的に閉じると評価する。これは形式証明・専門家による査読・研究的新規性の認定を意味しない。**`op:fanout-two` は OPEN**。

---

## 1. 対象定理の正確な量化

有限アルファベット \(\Sigma=\{a\}\sqcup\Delta\)、\(D=|\Delta|\ge1\)、有限**半束**への型付け \(s:\Sigma^+\to\mathsf S\)、\(f\ge1\) とする。\(L\subseteq\Sigma^*\) は **可換**（全ての語の置換で所属が不変、すなわち Parikh ベクトルだけで所属が決まる）かつ \(L\in\mathcal C^{\mathrm{mcf}}_{f,s}\)。\(G\) は \(L\cap\Sigma^+\) の **reduced good** MCFG で、fan-out は任意、rule rank \(\le r\)（\(r\ge1\)）、\(v=|V(G)|\)、\(\theta=\bar\theta_G\ge1\)。\(N=\min\{n\ge1:a^n\in L\}\) が定義されるとする。

\[
 B=D!\theta^D,\quad \rho=2DB,\quad
 K_0=2(r+1)\theta\,[4(r+1)\rho]^{D2^D}.
\]

Fable-Cの結論は

\[
 \boxed{N\le\max\{(D+1)BK_0+1,\ 2^{D+1}v(r+1)K_0\}}
 \quad\Longrightarrow\quad
 N=O_{D,r}\bigl(v\theta^{1+D+D^22^D}\bigr).
\]

- **固定するもの**：\(D\)、\(r\)（指数と暗黙定数はこれらに依存）。アルファベットサイズが成長する場合の一様多項式定理ではない。
- **使う代入可能性**：\(d=1\) のみ。二穴やfan-out 2固有の主張ではない。
- **測る厚さ**：型付き精密化後ではなく元の \(G\) の \(\bar\theta_G\)。
- **対象**：\(a^N\) の最短長のみ。任意の型の代表長や一般の特徴標本長ではない。

## 2. 準備：短縮不能性と Parikh 交換

### 2.1 一意性 (U) — 有効

もし \(P a^iQ,\ Pa^{i'}Q\in L\)、\(1\le i<i'\le N\) なら、半束型付けで \(s(a^i)=s(a^{i'})\)。共通の受理文脈 \(P\square Q\in\mathcal E_1\) によって \(a^i\equiv_{L,s}a^{i'}\)。文脈 \(a^{N-i'}\square\) に代入すれば \(a^{N-i'+i}\in L\) となり、\(0<N-i'+i<N\) は \(N\) の最小性に矛盾する。\(i'=N\) でも文脈 \(\square\) は適法。

このため、非 \(a\) 文字の Parikh ベクトル \(V\in\mathbb N^\Delta\setminus\{0\}\) が一定で、\(1\le e<N\) の語が存在するとき、受理される \(a\) の個数 \(e\) は高々一つ。実際、可換性から両候補を \(a^e w_V,a^{e'}w_V\) と並べれば、共通文脈 \(\square w_V\) が (U) に反する。以後

\[
 \mathcal V=\{V\ne0:\ (e,V)\in\operatorname{Parikh}(L)
 \text{ for some }1\le e<N\},\qquad
 \delta(V):=N-e
\]

は一価に定義され、\(1\le\delta(V)\le N-1\)。

### 2.2 Fable §5(2) の交換補題 — 明示的な受理文脈を補完

\(V,V'\in\mathcal V\) が同じ非 \(a\) 文字の台 \(T\) を持つとする。\(d=\delta(V)\), \(d'=\delta(V')\) とし、\((e,Q+V)\in\operatorname{Parikh}(L)\)、\(e'=e+d-d'\ge1\) とする。次を置く：

\[
 i=1+\max(0,d'-d),\qquad i'=1+\max(0,d-d').
\]

すると \(i'-i=d-d'\), \(i\le e\), \(i\le N-d\), \(i'\le N-d'\)。非 \(a\) 語 \(w_V,w_{V'},w_Q\) をそれぞれの Parikh ベクトルどおり選び、

\[
 x=a^i w_V,\qquad y=a^{i'}w_{V'},\qquad
 E_0=a^{N-d-i}\square,\qquad
 E_1=a^{e-i}\square w_Q
\]

とする。\(E_0[x],E_0[y]\) はそれぞれ Parikh \((N-d,V),(N-d',V')\) を持ち**両方受理**される。\(s(x)=s(y)\) は台 \(\{a\}\cup T\) の一致による。従って \(x\equiv_{L,s}y\)。\(E_1[x]\in L\) だから \(E_1[y]\in L\) であり、Parikh は \((e',Q+V')\)。これで \(§5(2)\) は証明された。

**5.1(E) の補完**：\(aVa^e,aV'a^{e'}\in L\), \(1\le e,e'\le N-2\) なら、5.1(R) を使って \(a^eVa,a^{e'}V'a\in L\) と再配分できる。内容が等しいので、共通の恒等文脈 \(\square\) により \(a^eVa\equiv_{L,s}a^{e'}V'a\)。Fableの差 \(i'-i=e'-e\) は \(i=e,i'=e'\) で成立。これは定理Cの主証明では直接引用しないが、補題5.1の量化も確認した。

## 3. §5(0) 最小導出木、短い収率、欠損 — 有効

\(a^N\) の導出木 \(\mathcal T\) を**節点数最小**に固定する。good の非削除性から、各節点の収率タプルの文字は全て \(a\) であり、その合計長を \(k_X\) とする。

**同一非終端の出現は根葉道上に二度ない**：もし出現 \(X,Y\) が同じ非終端 \(A\) で異なる収率長を持てば、長い方の \(A\)-部分木を短い方の導出木で置換し、\(a^N\) より短い正の \(a\) 冪を生成する。これは \(N\) の最小性に矛盾する。長さが同じで一方が他方の祖先なら、祖先の導出木を子孫の導出木に置換して同じ語 \(a^N\) をより少ない節点で生成でき、節点数最小性に矛盾する。従って高さは \(\le v\)。**分岐部分で同じ非終端が反復することは禁止しない**。

既存 thickness lemma から、各 \(A\) に \(\|u_A\|_1\le\theta\) の短い導出タプルがある。\(\operatorname{Parikh}(u_A)=(\alpha_A,V_A)\) とする。大節点を \(k_A>\theta\) と呼ぶ。\(V_A=0\) なら大節点の置換によって \(a^{N-k_A+\alpha_A}\in L\) を作る。長さは \(N\) 未満（かつ、もし0なら \(\eps\) と矛盾しないが、**good の非空成分により置換後の語は正長**）。従って \(V_A\ne0\) が必須。

\[
 \delta_A=k_A-\alpha_A>0,
 \qquad k_A-\theta\le\delta_A\le k_A,
 \qquad |V_A|_1\le\theta.
\]

大節点で \(\delta_A\le N-1\) なら、単一節点置換から \((N-\delta_A,V_A)\in\operatorname{Parikh}(L)\) が得られ \(V_A\in\mathcal V\), \(\delta(V_A)=\delta_A\)。Fableの §5(1) は \(k_A<N\) を十分条件としているが、その後の §5(3),(4) で使う \(\delta_A\le(N-1)/2\) でも当然満たされる。

**注意（0収率回避）**：\(k_A=N\), \(\alpha_A=0\) で置換した語には \(V_A\ne0\) があるため正長であり、\(a\) の数は0でもよい。ただしこの場合 \(\delta_A=N\) なので集合 \(\mathcal V\) に使用しない。\(V_A=0\) の場合、短いgoodタプルは正長なので \(\alpha_A\ge1\)、したがって本当に短い正の \(a\) 冪が得られて矛盾する。

## 4. §5(3) 分岐類の完全加法性 — 有効

台 \(T\subseteq\Delta\), \(T\ne\emptyset\) を固定。元の木に互いに祖先子孫でない二つの大節点 \(B,C\) があり \(\operatorname{supp}V_B=\operatorname{supp}V_C=T\)、\(\delta_B+\delta_C\le N-1\) のとき「分岐類」と呼ぶ。

両節点を同時に短い収率へ置換すれば、非削除性と元が \(a^N\) であることから
\[
 (N-\delta_B-\delta_C,V_B+V_C)\in\operatorname{Parikh}(L).
\]
\(\delta_B\le\delta_C\) として \(\delta_B\le(N-1)/2\)。

台 \(T\) の大非終端 \(J\) で \(\delta_J\le(N-1)/2\) のものを「許容単位」とする。任意の二単位 \(J,J'\) について、種 \(V_B+V_C\) の \(C\) を \(J\) に交換：中間欠損 \(\delta_B+\delta_J\le N-1\)。次に \(B\) を \(J'\) に交換：最終欠損 \(\delta_J+\delta_{J'}\le N-1\)。§2.2 によって両交換は合法。従って二単位の和が実現する。

**任意多重集合への帰納**：一単位は上記単一節点置換で実現する。二単位は直前の議論。\(|m|\ge3\)、総欠損 \(\delta_m\le N-1\) の多重集合から単位 \(J'\) を一つ取り除いた \(M\) は帰納的に実現し、\(\operatorname{supp}V_M=T\)、\(\delta(V_M)=\delta_M\)。\(M\) 中の単位 \(J\) を一つ選ぶ。既知の二単位の和 \(V_J+V_{J'}\)（欠損 \(\delta_J+\delta_{J'}\)）に対し \(V_J\to V_M\) を交換すれば、目標の \(V_M+V_{J'}\)（欠損 \(\delta_M+\delta_{J'}=\delta_m\le N-1\)）を得る。種 \(V_M\) は単一の台 \(T\) を持つから §2.2 の前提を満たす。これで全長の帰納法は閉じる。

**重要な補完**：整数関係の正負側が単位一つだけとなる場合がある。だから帰納法のベース \(|m|=1\) を明記する必要がある。Fableは「\(m\ne0\)」と正しく主張しているが、印刷上は \(|m|=2\) から証明を始めているので補う。

## 5. §5(4) 整数関係と疎な欠損列の排除 — 有効

台 \(T\) のサイズを \(t\le D\) とする。各許容 \(V_J\) は非零、成分が \([0,\theta]\) の整数ベクトル。\(t+1\) 本の列には非自明な整数関係 \(\sum_i\lambda_iV_{J_i}=0\) があり、\(0<\max_i|\lambda_i|\le t!\theta^t\le B\) となる。証明：行列階数 \(h\le t\) の \(h+1\) 本に、階数 \(h\) の非零小行列の符号付き \(h\times h\) 小行列式を係数として使う。各小行列式は Leibniz 展開で \(\le h!\theta^h\) に抑えられる。他の列の係数は0とする。全ての列が非零かつ成分非負なので、非自明な関係には正負両符号が必ず現れる。

分岐類の許容欠損に \(t+1\) 個 \(\delta_0<\cdots<\delta_t\le N_1\) があって \(\delta_{i+1}>\rho\delta_i\) と仮定する。ただし
\[
 N_1=(N-1)/((D+1)B),\qquad \rho=2DB.
\]
有界関係の正負側 \(m^+,m^-\) はそれぞれ総欠損 \(\le t B N_1\le N-1\) なので §4 の加法性が使える。二つは同じ非 \(a\) ベクトルを実現するため、一意性 (U) より \(\sum_i\lambda_i\delta_i=0\)。係数が非零の最大添字を \(j\ge1\) とすれば
\[
 |\lambda_j|\delta_j\ge\delta_j
 >2DB\delta_{j-1}\ge 2tB\delta_{j-1}
 \ge 2\Bigl|\sum_{i<j}\lambda_i\delta_i\Bigr|,
\]
矛盾。この疎列排除から、該当する欠損集合は**高々 \(t\) 個**の区間 \([x,\rho x]\) で覆える（左端の最小値から貪欲に覆い、次は覆い外の最小値を取る）。台の種類は \(2^D-1\) 以下なので全区間数
\[
 M_b\le\sum_{\emptyset\ne T\subseteq\Delta}|T|
 =D2^{D-1}<D2^D
\]
である。Fableの粗い上界は安全。

## 6. §5(5) 非分岐類の二本根道被覆 — 有効

非分岐台 \(T\) の大節点の集合 \(\mathcal N_T\) を考える。

- 互いに比較不能な二節点が一つもなければ、全て祖先子孫関係にあり、最深の節点への一本の根道上に載る。
- 比較不能な \(B,C\in\mathcal N_T\) があるなら、非分岐性から \(\delta_B+\delta_C\ge N\)。しかし独立した部分木なので \(\delta_B+\delta_C\le k_B+k_C\le N\)。ゆえに **\(\delta_B+\delta_C=k_B+k_C=N\)**、従って \(\alpha_B=\alpha_C=0\) である。
- \(B\) の真下の二つの \(T\)-節点 \(X,Y\) が比較不能だと、\(\delta_X+\delta_Y\le k_X+k_Y\le k_B\le N-k_C\le N-1\) で分岐類になり矛盾。よって \(B\) 以下の \(T\)-節点は一本の鎖、\(C\) 以下も同様。
- 他の \(T\)-節点 \(X\) が \(B,C\) の双方と比較不能なら、三つの部分木が互いに素であり \(k_B+k_C+k_X>N\) になって矛盾。したがって \(X\) は \(B\) か \(C\) の祖先または子孫で、上記二本の根道のどちらかに含まれる。

また \(k=N\) の節点はすべて一列の祖先鎖である。非分岐台ごとの高々二本と、この一本の**根からの道**の和を \(U\) と定める。\(U\) は祖先に関し閉じ、\(a^N\) の節点数最小性からどの根道も高々 \(v\) 節点なので
\[
 |U|\le [2(2^D-1)+1]v\le2^{D+1}v.
\]
\(X\notin U\) なら、その全子孫も \(U\) の外にあり、その大節点は全て**分岐台**に属する。これが §7 への正確な橋渡し。

## 7. §5(6) 最重子の窓被覆 — 有効、量化を明示

\(\sigma:=2(r+1)\)。\(X\notin U\)、\(k_X>\theta\) とする。最も長い子を繰り返し選ぶ経路の収率長を \(k_0=k_X\ge k_1\ge\cdots\) とする。各規則は端末を \(\le\theta\) 個書き、子は高々 \(r\) なので、\(k_i>\theta\) で子を持つとき
\[
 k_{i+1}\ge(k_i-\theta)/r.
\tag{H}
\]
（子がないなら \(k_i\le\theta\) である。）

任意の実数 \(y\in[\sigma\theta,k_X]\) をとり、**最初に** \(k_j\le y\) になる節点を選ぶ。最後の葉は \(k\le\theta\) なので必ず存在。

- \(j=0\) なら \(y=k_X\) であり \(\delta_j\ge y-\theta>y/\sigma\), \(\delta_j\le y\)。
- \(j>0\) なら \(k_{j-1}>y\ge\sigma\theta\) なので (H) と \(\delta_j\ge k_j-\theta\) から
\[
 \delta_j>\frac{y-\theta}{r}-\theta
 =\frac{y-(r+1)\theta}{r}
 \ge\frac{y}{2r}\ge\frac{y}{\sigma}.
\]
  一方 \(\delta_j\le k_j\le y\)。

両場合に \(\delta_j\in[y/\sigma,y]\)、しかも \(\delta_j>\theta\) だから \(j\) は大節点であり、\(j\notin U\) なので分岐類に属する。これで **全ての \(y\)** に対する窓被覆を証明した。これは単なる標本点の検査ではない。

\(\min(k_X,N_1)\ge K_0\) と仮定する。\(y_j:=\sigma\theta(2\sigma\rho)^j\)（\(0\le j\le M_b\)）の全てが \(\le\min(k_X,N_1)\) なので、\(M_b+1\) 個の窓 \(I_j=[y_j/\sigma,y_j]\) がそれぞれ分岐欠損を含む。他方、§5 の被覆区間 \(J=[x,\rho x]\) は異なる二つの窓を同時には交わらない。実際 \(I_j\) 内の点は \(\le y_j\)、\(I_{j+1}\) 内の点は \(\ge y_{j+1}/\sigma=2\rho y_j\) で、同じ \([x,\rho x]\) には入らない。よって \(M_b\) 個以下の被覆区間で \(M_b+1\) 個の窓を覆うのは不可能。従って
\[
 \min(k_X,N_1)<K_0,
 \quad K_0=\sigma\theta(2\sigma\rho)^{D2^D}
 =2(r+1)\theta[4(r+1)\rho]^{D2^D}.
\]

## 8. §5(7) 最終集計・指数 — 有効

- \(N_1<K_0\) なら、\(N-1<(D+1)BK_0\) なので \(N<(D+1)BK_0+1\)。
- \(N_1\ge K_0\) なら、直前の不等式から \(U\) の外側の大節点は全て \(k_X<K_0\)、小節点は \(k_X\le\theta<K_0\)。よって \(U\) の外に出る辺の各子部分木は長さ \(<K_0\)。\(U\) の各節点は高々 \(\theta\) 個の終端を明示し、子は高々 \(r\) 個。従って全語長 \(N\le |U|(\theta+rK_0)\le |U|(r+1)K_0\le2^{D+1}v(r+1)K_0\)。

最後に \(B=D!\theta^D\)、\(\rho=2DB=O_D(\theta^D)\) より
\[
 K_0=O_{D,r}\bigl(\theta^{1+D^22^D}\bigr),\qquad
 (D+1)BK_0=O_{D,r}\bigl(\theta^{1+D+D^22^D}\bigr).
\]
\(v\ge1\) なので両分岐を合わせて \(N=O_{D,r}(v\theta^{1+D+D^22^D})\)。Fableの指数 **\(1+D+D^22^D\)** は正しい。

## 9. Fableコード非依存の独立検査

ファイル `check_fable_C_independent.py` を新規作成。出力は `independent_check_log.txt`。次の数学的必要条件を、ランダムまたは有限全列挙でストレス検査した：

| 検証 | 件数 | 結果 |
|---|---:|---|
| §5(2) 交換の共通受理文脈、i/i′ の非負性 | 36,820 | PASS |
| §5(3) 二単位の初期置換と多重集合帰納の数値条件 | 550 | PASS |
| §5(5) 非分岐台が高々二根道に載る | 3,500ランダム木 | PASS |
| §5(6) 最重子経路の全整数窓 | 153,625件 | PASS |
| §5(4) 有界整数関係の符号付き小行列式の係数境界 | 24,446件 | PASS |

**独立性**：Fableのプログラム・証明書をインポートしていない。**限界**：この有限検査は実際のMCFG組代入可能言語の普遍的な列挙ではない。定理の認証理由は §§2–8 の独立に再構成した一般手証明であり、コードは補助的な境界チェックである。

## 10. 監査上の修正事項と判定

1. **§5(0) の「根道の非終端重複なし」**：短い \(a\)-冪の矛盾と節点数最小性を明示する（§3）。
2. **§5(2) の交換**：実際の共通受理文脈 \(E_0\) と試験文脈 \(E_1\)、\(i,i'\) の非負性を明示する（§2.2）。
3. **§5(3) の多重集合**：\(|m|=1\) のベースと、\(J+J'\) から \(M+J'\) への帰納法を明示する（§4）。
4. **§5(4) の整数関係**：非零・非負列による正負両符号、および係数上界を明示する（§5）。
5. **§5(5) の「高々二根道」**：悪い対が \(k_B+k_C=N\) を強制することと、子孫内の分岐を排除することを明示する（§6）。
6. **§5(6) の窓**：全ての実数 \(y\) と端点の扱いを厳密化し、\(M_b+1\) 個の離れた窓に被覆区間を重複使用できないことを証明する（§7）。
7. **独立性・新規性**：本監査は証明の内的妥当性の評価であり、新しい定理であることの文献的証明ではない。Claude既存の定理 L 等との一致・包含関係は未調査。
8. **中心開問題への含意**：可換・単項希少型という限定領域に限った障壁。非可換な言語、2文字以上の希少型、一般の区別部分言語を排除しない。`op:fanout-two` は **OPEN**。

**最終判定：Fable-C は、上記の補足付きで VALID AS A HAND-PROOF。** 少なくとも提供された原報告の §5 の証明に関しては、定理の成立を妨げる論理ギャップを独立追跡で確認しなかった。正式な研究定理として引用する際は別の専門家による独立査読または機械形式化を推奨する。GitHub/論文の変更は行っていない。

===== END FILE =====

===== BEGIN FILE Fable_original_open_problem_report_2026-11-15.md bytes=27376 sha256=c0369cdc571944bfe702e52a3571939bc5981c332637bf8c49765ebc3e3ca223 =====
# `op:fanout-two` 独立研究報告（Fable, 2026-11-15）

**結論ラベル：`NEW THEOREM BUT OPEN`**
`op:fanout-two` 自体は解けていない。得られたのは (i) 倍化族に対する no-lift 定理の決定的な強化（機械検証済み証明書つき）、(ii) 薄い文法に対するアーベル型下界の一般的不可能性、(iii) 可換言語における単項希少型の多項式上界（新しい証明法）、(iv) 開問題の単一言明への還元、である。私の現時点の評価は「答えは NO（LG は fan-out 2 では境界でない）の方が見込みが高い」だが、これは**予想**であり証明ではない。

各主張の状態は次の記号で区別する：**[証明]** 本報告内に完全な証明がある／**[検証]** 明示的証明書を独立チェッカで検査済み／**[計算]** ハッシュベースの探索結果で証明書は未抽出／**[予想]**。

---

## 0. 読んだ資料と読んでいない資料

- GitHub を clone して読んだもの：`main.tex` の定義（`def:grammar-properties`, `def:tuple-substitutable`, `def:uniform-polydata`）、`lem:thickness-*`, `lem:distinguishing`, `prop:rare-type`, `prop:three-letter-family`, `thm:fanout-one-data`, `lem:power-transfer`, `thm:doubling-no-lift`, `op:fanout-two`；`HANDOFF_CURRENT.md`；U₂ ノートの定義と主張部分。
- **読んでいないもの**：`reviews/` の各ラウンド報告の本文（定理 L, P, S, L^⊗′ の証明、第九〜十一段の詳細）。したがって §5 の可換定理が既存の定理 L（ℓ=1）と結論の上で重なる可能性は排除していない。証明法は独立に構成した。
- 依頼書の問題設定に誤りは見つからなかった。一点だけ補足がある（§1）。

## 1. 開問題の単一言明への還元 [証明]

**命題 1.** \(f\ge2,\ r_{\max}\ge2\) を固定する。次は同値。
1. `op:fanout-two` の答えが YES。
2. 有限半束の擬多様体 \(\mathbf{SL}\) が fan-out \(f\)・rank \(r_{\max}\) で一様多項式特徴データ長を持たない。
3. ある有限アルファベット \(\Sigma\) とある半束型付け \(s:\Sigma^+\twoheadrightarrow\mathsf S\) について `def:uniform-polydata` の多項式が存在しない。

*証明.* \(\mathbf V\not\subseteq\mathbf{LG}\) なら \(U_1\in\mathbf V\)（`thm:lg-characterization`）で、擬多様体は有限直積・部分・商で閉じるから \(\mathbf{SL}=\langle U_1\rangle\subseteq\mathbf V\)。一様多項式性の失敗は \(\mathbf V\) について単調なので 2⇒1。逆に \(\mathbf{SL}\) 自身が \(\mathbf{LG}\) に含まれないので 1⇒2。2⇔3 は定義。∎

**補足 1′（上界側は内容型付けだけ見ればよい）.** 任意の半束型付け \(s\) は内容型付け \(c_\Sigma\) を経由するので \(\mathcal C^{\mathrm{mcf}}_{f,s}\subseteq\mathcal C^{\mathrm{mcf}}_{f,c_\Sigma}\)。さらに \(L\in\mathcal C^{\mathrm{mcf}}_{f,s}\) に対し \(\tau(G,s)\le\tau(G,c_\Sigma)\)：\(s\)-型付き非終端 \(B_{\mathbf t}\) の収率を含む内容型付き非終端 \(B_{\mathbf T}\) の類代表は、同じ分布を持ち \(s\)-型も \(\mathbf t\) だから \(\operatorname{Cl}_{L,s}(B_{\mathbf t})\) に入る。よって「全ての \(\Sigma\) で \(\tau(G,c_\Sigma)\) が多項式」が示されれば答えは NO。

つまり問題は U₁ の特定の3文字型付けではなく、**任意アルファベット上の内容型付け**の問題そのものである。下界側は大きなアルファベットを自由に使ってよく、上界側は内容型付けだけ処理すればよい。

## 2. 道具

以下 \(c(w)=\operatorname{alph}(w)\)、\(L\in\mathcal C^{\mathrm{mcf}}_{f,s}\)、\(f\ge2\)。

**補題 2.1（滑り補題／共役移送）[証明].** \(l,r\in\Sigma^*\)、\(x_1,y_2,z,z',m\in\Sigma^+\) が \(zm=mz'\)、\(s(x_1z)=s(x_1)\)、\(s(z'y_2)=s(y_2)\)、\(l\,x_1\,z\,m\,y_2\,r\in L\) を満たすなら
\[(x_1z,\;y_2)\ \equiv_{L,s}\ (x_1,\;z'y_2).\]
*証明.* 文脈 \(E=l\,\square_1\,m\,\square_2\,r\)（\(m\neq\varepsilon\)）は両方の組を同じ語 \(l x_1 z m y_2 r=l x_1 m z' y_2 r\) に埋めるので共通の受理文脈であり、成分型は仮定より等しい。∎

`lem:power-transfer` は \(z=z'=u^\delta\), \(m=u\) の特別な場合。内容型付けでは条件は \(c(z)\subseteq c(x_1)\cap c(y_2)\) だけになる。特に：

**系 2.2（単位の移送）.** 内容型付けで、\(L\) のある語が因子 \(x_1\cdot d\kappa\cdot d\cdot y_2\)（\(d\in\Sigma\), \(\kappa\in\Sigma^*\), \(c(d\kappa)\subseteq c(x_1)\cap c(y_2)\)）を持てば、全ての \(l,r\in\Sigma^*\), \(m'\in\Sigma^+\) で
\[l\,x_1\,d\kappa\;m'\;y_2\,r\in L\iff l\,x_1\;m'\;\kappa d\,y_2\,r\in L .\]
同じ文字 \(d\) の連続する二つの出現に挟まれた単位 \(d\kappa\) は、後方の \(y_2\) の出現の直前へ（\(\kappa d\) として）語長と Parikh ベクトルを保ったまま移動できる。長い語では文字が必ず再出現するので、この移動は**避けられない**。

**定義 2.3（導出閉包）.** \(K\subseteq\Sigma^*\) に対し \(\operatorname{Cl}(K)\) を、\(K\) を含み次の規則で閉じた最小集合とする：\(d\in\{1,2\}\)、\(\mathbf x,\mathbf y\in(\Sigma^+)^d\) が成分ごとに同じ内容を持ち、\(E_0,E_1\in\mathcal E_d\) について \(E_0[\mathbf x],E_0[\mathbf y],E_1[\mathbf x]\) が既に入っていれば \(E_1[\mathbf y]\) を入れる。

**補題 2.4（健全性）[証明].** 半束型付け \(s\) と \(f\ge2\) について、\(K\subseteq L\in\mathcal C^{\mathrm{mcf}}_{f,s}\) なら \(\operatorname{Cl}(K)\subseteq L\)。（\(L\in\mathcal C^{\mathrm{mcf}}_{f,c_\Sigma}\) なので各規則適用は定義そのもの。）

**補題 2.5（射による輸送）[証明].** \(\varphi:\Sigma^*\to\Sigma'^*\) を非消去射、\(P,Q\in\Sigma'^*\) とすると \(P\,\varphi(\operatorname{Cl}(K))\,Q\subseteq\operatorname{Cl}(P\varphi(K)Q)\)。
*証明.* 導出の長さの帰納法。\(c(\varphi(u))=\bigcup_{e\in c(u)}c(\varphi(e))\) は \(c(u)\) のみで決まるので、内容が等しい成分は像でも内容が等しい。成分と穴の間の部分は非消去性により非空のまま。文脈 \(E=(l,m,r)\) は \((P\varphi(l),\varphi(m),\varphi(r)Q)\) に移る。∎

内容型付けの本質的な点は、**任意の**非消去射で導出が輸送されることである（文字互いに素である必要はない）。

## 3. 定理 A：倍化族は fan-out 2 で完全に崩壊する

\(L_n,W_n\) は `prop:three-letter-family` のもの（\(W_1=\mathtt{baab}\), \(|W_n|=3\cdot2^n-2\)）。

**定理 A [証明＋検証].** \(\Sigma\supseteq\{a,b,c\}\)、\(s\) を \(\Sigma^+\) 上の任意の半束型付け（\(s_U\)、\(c_\Sigma\) を含む）、\(f\ge2\)、\(n\ge3\) とする。\(L_n\subseteq L\) なる全ての \(L\in\mathcal C^{\mathrm{mcf}}_{f,s}\) は \(W_1,W_2,\dots,W_n\) を全て含む。特に \(\mathtt{baab}\in L\) であり、\(W_n\) の型の最短語長は \(n\) によらず \(4\) 以下。
より一般に、非消去射 \(\psi\) について \(\psi(L_n)\subseteq L\) なら \(\psi(\mathtt{baab})\in L\)。

これは `thm:doubling-no-lift`（「同じ型・同じ Parikh の別の語がある」）を、半束型付けについて「定数長の語がある」まで強める。語を追加して族を修復する余地は一切ない。

*証明.*
(1) **証明書** [検証]：\(W_2=\mathtt{bbaabbaabb}\in\operatorname{Cl}(L_3)\) かつ \(\mathtt{baab}\in\operatorname{Cl}(L_3)\)。添付 `cert_L3_to_baab_pruned.json` は定義 2.3 の規則 33 回（\(d=1\) が 9 回、\(d=2\) が 24 回）の明示的列で、`verify_cert.py` が各ステップの前提（成分・中間部の非空性、内容の一致、\(E_0[\mathbf x],E_0[\mathbf y],E_1[\mathbf x]\) の所属）を独立に検査する。
(2) \(k\ge0\)、\(\varphi_k:a\mapsto W_k,\ b\mapsto b,\ c\mapsto c\) とすると \(\varphi_k(L_3)\subseteq L^{(k+3)}\)（\(E_{k+3}\) の収率集合）。\(k+3\le n\) なら \(E_{k+3}\) は \(L_n\) の中で文脈 \((P_k,Q_k)\)（例えば \(P_k=b^{\,n-k-3}\)）を持ち、\(P_k\varphi_k(L_3)Q_k\subseteq L_n\subseteq L\)。補題 2.5, 2.4 より \(P_kW_{k+2}Q_k,\ P_kW_{k+1}Q_k\in L\)。
(3) \(W_{k+3},W_{k+2},W_{k+1}\) は内容 \(\{a,b\}\) が等しく文脈 \((P_k,Q_k)\) を共有するので互いに \(\equiv_L\)（分布が一致）。
(4) \(W_n\in L\)。\(j\ge3\) で \(W_j\in L\) なら、\(k=j-3\) の同値 \(W_j\equiv W_{j-1}\) を文脈 \((\varepsilon,\varepsilon)\) に適用して \(W_{j-1}\in L\)。\(W_3\in L\) からは \(k=0\) の \(W_3\equiv W_1\) で \(W_1\in L\)。射版は \(\psi\circ\varphi_k\) で同じ。∎

**崩壊の機構.** 核は系 2.2 の「文字の飛び越し」である。探索で最初に見つかった例では、\(L_3\) の二つの語 \(b\,W_2\,[c\,W_1\,c]\,b\) と \(b\,W_2\,[b\,W_1\,c\,a\,c\,b]\,b\) から、\(b\) が \(c\) を右へ、\(c\) が \(\mathtt{bbaab}\) を左へ飛び越して、**同じ枠** \(b\,W_2\,c\,\square\,c\,bb\) に長さの違う \(c\) なし語 \(\mathtt{baa}\) と \(\mathtt{bbaaba}\) が入る。添付の証明書が実際に使うのは同種の二つの枠で、枠 \((\mathtt{bbcacbaabbc},\mathtt{acbb})\) に \(\mathtt{bbbaa}\) と \(\mathtt{ba}\) が、枠 \((\mathtt{bcbaabcb},\mathtt{cbacbb})\) に \(\mathtt{baabba}\) と \(\mathtt{baa}\) が入る。これと \(b\) の冪移送 \((b,bb)\equiv(bb,b)\) を合わせて \(W_3\) が \((a,2b)\) ずつ縮む（22→19→16→13→10→7→4）。省略記号 \(c\) が可動なので「省略の深さ」を位置で符号化できない、というのが本質である。

**検証の範囲.** `verify_log.txt`：\(L_3\) 上の証明書（刈込み 33 手・完全版 2945 手）に加え、輸送補題に頼らず \(L_4\)（\(k=1\) および \(k=0\) で枠 \((b,W_3b)\)）、\(L_5\)（\(k=2\)、および \(k=0\) で枠 \((bc,\,c^5ac^4b)\)）、\(L_6\)（\(k=1\)）、\(L_7\)（\(k=4\)）の中で同じ 33 手を直接検査し全て通過。所属判定は \(L_n\) の再帰的認識器による（列挙やハッシュに依存しない）。

**命題 A′（括弧を別文字にした変種）[計算].** \(E_i\to b\,E_{i-1}E_{i-1}\,d\mid c\,E_{i-1}\,e\)、\(E_0\to a\)（5文字、内容型付け）の族 \(V_n\) についても、\(\operatorname{Cl}(V_3)\) は \(W_1'=\mathtt{baad}\) と \(W_2'=\mathtt{bbaadbaadd}\) を含む（長さ 22 → 19 → 16 → 13 → 10 → 7 → 4）。これが正しければ定理 A の証明 (2)–(4) がそのまま通り \(V_n\) も定数長に崩壊する。ただしこれは 64 bit ハッシュを用いた打切り閉包＋最良優先探索の結果で、**明示的証明書は抽出していない**。

**観察 [計算].** \(s_U\) 型付けでは \(L_2\) の（長さ 10 打切り）閉包が既に語 \(\mathtt a\) を含む。内容型付けでは \(L_2\) は閉じており、崩壊は \(n=3\) から始まる。

## 4. 定理 B：薄い文法はアーベル不変量を隠せない

**定理 B [証明].** \(G\) を reduced good MCFG（fan-out 任意、rank \(\le r\)）、\(\theta=\bar\theta_G\)、\(g:\Sigma^*\to\mathsf A\) をアーベル群へのモノイド射、\(\mathsf H\le\mathsf A\)、\(\gamma\in\mathsf A\) とする。長さ \(\le(r+2)\theta\) の全ての \(w\in L(G)\) が \(g(w)\in\gamma+\mathsf H\) を満たせば \(L(G)\subseteq g^{-1}(\gamma+\mathsf H)\)。

*証明.* 各非終端 \(A\) に `lem:thickness-equivalence`(ii),(iv) の短い収率 \(\mathbf u_A\)（\(\|\mathbf u_A\|_1\le\theta\)）と文脈 \(E_A\)（固定部 \(\le\theta\)）を取り、\(c_A:=\sum_i g(u_{A,i})\) とおく。主張：全ての \(\mathbf u\in L_A\) で \(\sum_ig(u_i)\equiv c_A\pmod{\mathsf H}\)。導出の高さの帰納法：\(\mathbf u=\rho(\mathbf u^1,\dots,\mathbf u^q)\) なら非削除性と可換性から \(g(\mathbf u)=g(\text{$\rho$ の終端})+\sum_jg(\mathbf u^j)\equiv g(\rho(\mathbf u_{B_1},\dots,\mathbf u_{B_q}))\)。語 \(E_A[\rho(\mathbf u_{B_1},\dots)]\) と \(E_A[\mathbf u_A]\) は共に \(L(G)\) に属し長さ \(\le(q+2)\theta\) なので仮定より \(g\) 値が同じ剰余類にあり、\(g(\rho(\mathbf u_{B_j}))\equiv c_A\)。\(A=S\) では \(c_S=g(u_S)\in\gamma+\mathsf H\)。∎

**帰結.**
- `lem:distinguishing` を \(L'=L\cap g^{-1}(\gamma+\mathsf H)\)（`prop:abelian-coset-filter` の型の部分標的）に適用しても、区別語の長さは高々 \((r_{\max}+2)\bar\theta_G\)。**アーベル剰余類フィルタによる部分標的では超多項式下界は出ない。**
- 例：\(\{w:|w|_a\equiv|w|_c \pmod{2^n}\}\) は全ての型付けで組代入可能だが、多項式サイズ・多項式厚さの reduced good 提示を持たない（持てば上の議論で \(|w|_a=|w|_c\) が \(\mathbb Z\) 上で成立してしまう）。指数的な法や重みを持つ計数は厚さに必ず現れる。

## 5. 単項型の構造と定理 C

以下 \(a\in\Sigma\)、\(s\) は半束型付け、\(a^N\in L\) で \(N=\min\{i\ge1:a^i\in L\}\)。

**補題 5.1 [証明]（非可換・一般の \(L\in\mathcal C^{\mathrm{mcf}}_{2,s}\) で成立）.**
- **(R) 連の再配分.** \(p\,a^i\,q\,a^j\,r\in L\)、\(q\in\Sigma^+\)、\(i,j,i',j'\ge1\)、\(i'+j'=i+j\le N-1\) なら \(p\,a^{i'}q\,a^{j'}r\in L\)。（\(a^N=a^i\cdot a\cdot a^j\cdot a^{N-1-i-j}\) が共通文脈。）
- **(U) 一意性.** \(P a^iQ,\ Pa^{i'}Q\in L\)、\(1\le i<i'\le N\) は起こらない。（起これば \(a^i\equiv a^{i'}\) で \(a^{N-i'+i}\in L\)、最小性に反する。）
- **(E) 交換.** \(V,V'\notin a^*\) が \(aVa^{e},\,aV'a^{e'}\in L\)（\(1\le e,e'\le N-2\)）を満たし \(c(V)\cup\{a\}=c(V')\cup\{a\}\) なら、\(i'-i=e'-e\) なる適当な \(i,i'\ge1\) について \(a^iVa\equiv a^{i'}V'a\)。

(R),(U) から、\(a\) の総数が \(N\) 未満の語では「\(a\) の個数は、\(a\) の連を1文字に潰した骨格の関数」である。すなわち単項希少語 \(a^N\) があると、\(L\) の他の語は**骨格 → 欠損 \(\delta=N-|w|_a\)** という関数のグラフになり、(E) により欠損は同じ内容類の部品の入替えについて加法的に振る舞う。

**定理 C（可換言語では単項型は希少になれない）[証明；独立監査は未実施].** \(\Sigma=\{a\}\sqcup\Delta\)、\(D=|\Delta|\ge1\)。\(L\) を可換（所属が Parikh ベクトルのみで決まる）とし、ある半束型付け \(s\) と \(f\ge1\) で \(L\in\mathcal C^{\mathrm{mcf}}_{f,s}\)、\(G\) を \(L\cap\Sigma^+\) の reduced good 提示（fan-out 任意、rank \(\le r\)、\(v=|V|\)、\(\theta=\bar\theta_G\)）とする。\(a^N\in L\) で \(N\) が最小なら
\[N\ \le\ \max\bigl\{(D+1)BK_0+1,\ \ 2^{D+1}\,v\,(r+1)K_0\bigr\},\quad B=D!\,\theta^{D},\ \rho=2DB,\ K_0=2(r+1)\theta\,\bigl(4(r+1)\rho\bigr)^{D2^{D}} .\]
特に \(N=O_{D,r}\bigl(v\,\theta^{\,1+D+D^22^D}\bigr)\)：固定アルファベットでは多項式。

*証明.* \(P\subseteq\mathbb N\times\mathbb N^\Delta\) を \(L\) の Parikh 像とし、点を \((e,V)\) と書く。
**(0) 木.** \(a^N\) の \(G\) における導出木を節点数最小に取る。同じ非終端の二節点は収率の総長 \(k\) が等しく（違えば短い \(a\) 冪が出る）、入れ子にならない（節点数最小性）。よって深さ \(\le v\)。短い収率 \(\mathbf u_A\) の Parikh を \((\alpha_A,V_A)\) とする。\(k_A>\theta\) の節点を「大」と呼ぶと \(V_A\neq0\)（さもなくば \(a^{N-k_A+\alpha_A}\in L\) が最小性に反する）。欠損 \(\delta_A:=k_A-\alpha_A\in[k_A-\theta,k_A]\)、類 \(T_A:=\operatorname{supp}V_A\)。\(k_A=N\) の節点は根からの単項鎖をなす。
**(1) 実現集合.** \(\mathcal V:=\{V\ne0:\exists e\in[1,N-1],(e,V)\in P\}\)。(U) より \(e\) は一意で \(\delta(V):=N-e\) が定まる。\(k<N\) の大節点を省略すれば \(V_A\in\mathcal V\), \(\delta(V_A)=\delta_A\)。
**(2) 交換.** \(V,V'\in\mathcal V\)、\(\operatorname{supp}V=\operatorname{supp}V'\)、\((e,Q+V)\in P\)、\(e\ge1\)、\(e':=e+\delta(V)-\delta(V')\ge1\) なら \((e',Q+V')\in P\)。（\(i=1+\max(0,\delta(V')-\delta(V))\), \(i'=1+\max(0,\delta(V)-\delta(V'))\) とし、Parikh \((i,V)\) と \((i',V')\) の語は内容が等しく文脈 \((N-\delta(V)-i,0)\) を共有するので同値。\(e\ge i\) は \(e'\ge1\) と同値。）
**(3) 分岐類での完全加法性.** 類 \(T\) が**分岐的**とは、互いに素な大節点 \(B,C\)（\(k<N\)）で \(T_B=T_C=T\)、\(N-\delta_B-\delta_C\ge1\) なるものがあること。このとき、類 \(T\) の大非終端 \(J_1,\dots,J_t\)（各 \(\delta_{J}\le(N-1)/2\)）と \(\sum m_j\delta_{J_j}\le N-1\) なる多重集合 \(m\ne0\) について \(\sum m_jV_{J_j}\in\mathcal V\) で欠損は \(\sum m_j\delta_{J_j}\)。
　\(|m|=2\)：種 \(V_B+V_C\)（欠損 \(\delta_B+\delta_C\)）で \(\delta_B\le\delta_C\) としてよく、(2) で \(V_C\to V_J\)、次に \(V_B\to V_{J'}\) と入れ替える（途中の \(a\) 個数は \(N-\delta_B-\delta_J\ge1\)、\(N-\delta_J-\delta_{J'}\ge1\)）。\(|m|\to|m|+1\)：\(M=\sum m_jV_{J_j}\)（台 \(T\)）、\(m_J\ge1\) とし、\(V_J+V_{J'}\) に (2) を \(V=V_J\), \(V'=M\), \(Q=V_{J'}\) で適用する。
**(4) 分岐類には疎な鎖がない.** 分岐類 \(T\)（\(t=|T|\)）の大非終端 \(J_0,\dots,J_t\) で \(\delta_{J_{i+1}}>\rho\,\delta_{J_i}\)、\(\delta_{J_t}\le N_1:=(N-1)/((D+1)B)\) なるものは存在しない。
　実際 \(t+1\) 個のベクトル \(V_{J_i}\in[0,\theta]^T\) には Cramer の公式から \(|\lambda_i|\le t!\theta^t\le B\) の非自明な整数関係 \(\sum\lambda_iV_{J_i}=0\) があり、\(V_{J_i}\ge0\), \(\neq0\) なので両符号が現れる。\(m^\pm=\lambda^\pm\) は (3) の条件を満たし同じベクトルを実現するから、(U) より \(\sum\lambda_i\delta_{J_i}=0\)。しかし最大の添字 \(i^*\) で \(|\lambda_{i^*}|\delta_{J_{i^*}}\ge\delta_{J_{i^*}}>2Bt\,\delta_{J_{i^*-1}}\ge2\bigl|\sum_{i<i^*}\lambda_i\delta_{J_i}\bigr|\)。矛盾。
　したがって分岐類の欠損のうち \(N_1\) 以下のものは高々 \(D\) 個の区間 \([x,\rho x]\) で覆われる（貪欲法）。全分岐類で区間は \(M_b<D2^D\) 個。
**(5) 非分岐類は高々二本の根道に載る.** 類 \(T\) に互いに素な対がなければ全節点が比較可能で一本の根道上。互いに素な対 \(B,C\) が全て「悪い」（\(k_B+k_C=N\)）なら、\(B\) の下の類 \(T\) 節点は互いに比較可能（互いに素な \(X,Y\subseteq B\) は \(N-\delta_X-\delta_Y\ge k_C\ge1\) で良い対になる）、\(C\) の下も同様、その他は \(B\) か \(C\) と比較可能。\(U\) を、非分岐類の節点が載る根道と \(k=N\) の鎖の和集合とすると \(U\) は上方閉で \(|U|\le2^{D+1}v\)。
**(6) 窓の議論.** \(X\notin U\) を大節点とする。その子孫の大節点は全て分岐類。最重の子を辿る列 \(k_0=k_X\ge k_1\ge\cdots\) は \(k_i>(r+1)\theta\) の間 \(k_{i+1}\ge(k_i-\theta)/r\ge k_i/(r+1)\) を満たす。よって \(\sigma:=2(r+1)\) として、\(y\in[\sigma\theta,k_X]\) なる各窓 \([y/\sigma,y]\) は分岐類の大節点の欠損を含む。\(y_j:=\sigma\theta(2\sigma\rho)^j\)（\(j=0,\dots,M_b\)）の窓は、一つの区間 \([x,\rho x]\) が二つと交わることがないほど離れている。したがって \(\min(k_X,N_1)<K_0=\sigma\theta(2\sigma\rho)^{M_b}\)（\(M_b\le D2^D\)）。
**(7) 集計.** \(N_1<K_0\) なら \(N<(D+1)BK_0+1\)。\(N_1\ge K_0\) なら \(U\) の外の大節点は全て \(k<K_0\) で、\(U\) の各節点は終端 \(\le\theta\) 個と高々 \(r\) 個の子を持つから \(N\le|U|(r+1)K_0\)。∎

**注意.** (a) 証明は \(d=1\) の代入可能性しか使っていない。可換言語では fan-out に関係なく単項型が希少になれない、という主張である。(b) 対照的に非可換・fan-out 1 では `thm:fanout-one-data` の指数的下界がある。fan-out 2 が何を変えるかは次節。(c) `prop:rare-type` 経由の下界のうち「可換言語の単項型」を使うものはこれで閉じられるが、**開問題そのものには届かない**。

## 6. 非可換の場合：見取り図・予想・障壁

**直観.** fan-out 1 の下界は「非可換な剛構造（木）」が希少型の語を長く保つことで成立する。fan-out 2 の代入可能性は系 2.2 により全ての長い語を「単位の移送」で攪拌し、言語を局所データ＋計数データで決まるものへ近づける（先行ラウンドの Euler 付け替えと同じ現象を別方向から見ている）。一方、計数データで決まる部分では定理 B, C の論法（薄さ ⟹ 短い整数関係 ⟹ 疎な重み列が存在しない）が多項式上界を与える。移送に免疫を持つのは文字の順序が剛な有界言語型（例：\(\{a^nb^n\}\) は内容型付けでは 2 次元代入可能）だが、そこではブロック数が固定で次元が有界である。

**予想 U [予想].** 半束型付け \(s\)、\(f\ge2\)、\(L\in\mathcal C^{\mathrm{mcf}}_{f,s}\)、reduced good 提示 \(G\) について、\(L\) の最短の \(a\) 冪の長さは \(\|G\|,\bar\theta_G\) の多項式（次数は \(|\Sigma|\) に依存）で抑えられる。

**証明計画と欠けている部分.** 補題 5.1 は非可換でそのまま成立する。定理 C の (3)–(7) を非可換で再現するには、(U) を適用するために**骨格が語として一致する二語**が必要で、ここが唯一の本質的な穴である：
1. 系 2.2 から「交叉」が出る：部品 \(\alpha d\beta\) と \(\alpha'd\beta'\) が、後方に \(\alpha'd\beta'\) の複製を持つ適当な語の中に現れれば、\(\alpha d\beta'\) と \(\alpha'd\beta\) を部品とする語も \(L\) に入り \(a\) の個数は変わらない [証明：系 2.2 の直接の適用]。
2. 交叉は部品の bigram 多重集合（\(a\) との境界 bigram を含む）を保つ。**未証明**：同じ bigram 多重集合を持つ二つの部品多重集合が、常に宿主条件（系 2.2 の因子 \(x_1d\kappa dy_2\) の存在）を満たしたまま交叉と部品の並べ替えで結べること。これは有向多重グラフの Euler 分解の連結性＋「宿主可能性」で、先行ラウンドが HC と呼んだ困難と同種と思われる。部品の複製を自由に増やせる（補題 5.1(E) と定理 C(3) の論法）ので宿主の用意は U₂ より容易だと期待するが、確認していない。
3. これが通れば欠損は bigram 計数ベクトル（次元 \(\le(D+1)^2\)）の加法的関数になり、定理 C の (4)–(7) が次元だけ替えて通る。
4. fan-out 2 の非終端では部品が2成分になり、交換に \(d=2\) の同値が必要。帳簿は増えるが新しい困難は見えていない（未確認）。

**一般の希少型（2文字以上）について.** \(c\) なしの語が \(\{a,b\}\) 上にある場合、(U) の類似は「骨格ごとに \((|w|_a,|w|_b)\) の可能な値が格子の剰余類に入る」になるはずで、可換版ですら未着手である。定理 A の崩壊はこの場合の最初の実例にあたる。

**下界側の候補が残る場所.** 私が排除できていないのは次だけである：(i) 希少型を使わず、非アーベルかつ組代入可能な部分標的 \(L'\subsetneq L\) で区別する経路（定理 B はアーベルな \(L'\) しか殺さない）；(ii) 移送に免疫のある剛構造を、固定アルファベットのまま非有界な深さで実現する未知の符号化。(ii) について、単一ブロックに非線形な重み \(\sigma(j)\) を持たせる有界形 \(\{a^ic^jb^k:i+k=\sigma(j)\}\) を調べたが、\(a^uc^{j_1}\) と \(a^{u'}c^{j_1'}\) の比較から \(\sigma\) は \(j\ge1\) でアフィンに強制され、非線形性は \(j=0\)（別の型）にしか置けず、その場合は薄い提示が作れなかった（議論は概略のみで、定理としては主張しない）。

## 7. 計算の記録

詳細は `experiments_log.txt`。全て決定的で乱数は不使用。閉包は全て長さ打切りなので真の閉包の下からの近似であり、報告した語が閉包に属することだけを主張する。

| 対象 | 型付け | 打切り | 結果 | 状態 |
|---|---|---|---|---|
| \(L_2\)（6語） | \(s_U\) | 10 | 3306語で閉、\(\mathtt a\) を含む | [計算] |
| \(L_2\) | 内容 | 10 | 既に閉（6語） | [計算] |
| \(L_3\)（42語） | 内容 | 22 | 第2巡 \(d=1\) で 644 万語、\(c\) なし長さ16 | [計算] |
| \(L_3\vdash W_2,\ \mathtt{baab}\) | 内容 | — | 33 手の証明書、\(L_4\)–\(L_7\) 内でも直接検査 | [検証] |
| \(V_3\)（42語、5文字） | 内容 | 22、組長/枠長 \(\le7\) | 174 万語、その後 \(\mathtt{baad}\), \(W_2'\) に到達 | [計算] |

失敗・未完：\(L_3,V_3\) の無制限閉包は第2巡以降メモリと時間で完走せず。Python の \(c\) なし語 BFS は 25 分で出力なしのため打ち切り、証明書構成に置き換えた。

## 8. 最も有望な次の一手

1. **予想 U の穴（§6 の 2.）を埋める**か、反例を作る。部品複製が自由な設定での Euler 連結性は、U₂ の宿主問題より扱いやすい特殊化であり、通れば「単項型による下界は fan-out 2 で不可能」という型付け・言語クラスによらない最初の一般上界になる。
2. 定理 C を 2 文字の希少型へ拡張する（可換の場合）。(U) を格子版に置き換える。
3. 定理 A′ の証明書抽出（`build_cert.py` を \(V_3\) 用に書き換えるだけだが計算量が大きい）。
4. 下界を狙うなら §6 の (i) のみが未踏。ただし非アーベルで組代入可能な部分標的の例を私は一つも構成できていない。

## 9. 結論

**`NEW THEOREM BUT OPEN`.**

- **解決したこと（量化込み）.**
  - 全ての \(f\ge2\)、\(n\ge3\)、\(\Sigma\supseteq\{a,b,c\}\)、全ての半束型付け \(s\)、\(L_n\) を含む全ての \(L\in\mathcal C^{\mathrm{mcf}}_{f,s}\) について \(\mathtt{baab}\in L\)（定理 A、証明書は機械検査済み）。任意の非消去射像でも同様。
  - 全ての reduced good MCFG \(G\)（rank \(\le r\)）と全てのアーベル剰余類条件について、長さ \((r+2)\bar\theta_G\) 以下の語で成り立てば \(L(G)\) 全体で成り立つ（定理 B）。
  - 全ての可換な \(L\in\mathcal C^{\mathrm{mcf}}_{f,s}\)（\(s\) 半束、\(f\ge1\)）と全ての reduced good 提示について、最短の \(a\) 冪は \(O_{|\Sigma|,r}(|V|\,\bar\theta_G^{\,1+D+D^22^D})\)（定理 C、手証明・未監査）。
  - `op:fanout-two` は「\(\mathbf{SL}\) が fan-out \(f\) で一様多項式データ長を持たないか」と同値（命題 1）。
- **未解決のまま.** ある \(\Sigma\) とある半束型付けについて超多項式族が存在するか（YES）、全ての \(\Sigma\) で \(\tau(G,c_\Sigma)\) が多項式か（NO）。非可換言語では単項希少型すら未決（予想 U）。\(f\ge3\) への移行も未検討。

===== END FILE =====

===== BEGIN FILE L2.txt bytes=53 sha256=286d7916fd30d54f799aa7597cd6b6d9164edf88c504c5baee01a62682714a1c =====
bbaabbaabb
bbaabcacb
bcacbaabb
bcaccacb
cbaabc
ccacc

===== END FILE =====

===== BEGIN FILE L3.txt bytes=737 sha256=a3c44ea863d82881abee40a9368ddd629a9f2edec29b8920aca7d03ddbdedca3 =====
bbbaabbaabbbbaabbaabbb
bbbaabbaabbbbaabcacbb
bbbaabbaabbbcacbaabbb
bbbaabbaabbbcaccacbb
bbbaabbaabbcbaabcb
bbbaabbaabbccaccb
bbbaabcacbbbaabbaabbb
bbbaabcacbbbaabcacbb
bbbaabcacbbcacbaabbb
bbbaabcacbbcaccacbb
bbbaabcacbcbaabcb
bbbaabcacbccaccb
bbcacbaabbbbaabbaabbb
bbcacbaabbbbaabcacbb
bbcacbaabbbcacbaabbb
bbcacbaabbbcaccacbb
bbcacbaabbcbaabcb
bbcacbaabbccaccb
bbcaccacbbbaabbaabbb
bbcaccacbbbaabcacbb
bbcaccacbbcacbaabbb
bbcaccacbbcaccacbb
bbcaccacbcbaabcb
bbcaccacbccaccb
bcbaabcbbaabbaabbb
bcbaabcbbaabcacbb
bcbaabcbcacbaabbb
bcbaabcbcaccacbb
bcbaabccbaabcb
bcbaabcccaccb
bccaccbbaabbaabbb
bccaccbbaabcacbb
bccaccbcacbaabbb
bccaccbcaccacbb
bccacccbaabcb
bccaccccaccb
cbbaabbaabbc
cbbaabcacbc
cbcacbaabbc
cbcaccacbc
ccbaabcc
cccaccc

===== END FILE =====

===== BEGIN FILE PROMPT_FABLE_FANOUT_TWO_OPEN_PROBLEM_FREEDOM_2026-11-15.md bytes=13168 sha256=6efd5907537c20688ebbf6f88324ca8306d6a6d5671b0ad294886d271d3c692b =====
# Fableへの研究依頼：fan-out 2におけるLG境界の中心的開問題を自由に攻めてください

**研究課題：** Grammatical inference / multiple context-free languages / positive-data learning / finite semigroup typing  
**優先事項：** 新しい数学的着想と、反例・定理・厳密な証明。既存研究の追試や論文化ではありません。  
**作業モード：** 独立した研究者として自律的に探索してください。探索方針・手法・順序はあなた自身が決めて構いません。

---

## 依頼の核心

あなたに研究してほしいのは、次の**現に未解決の問題**です。以前のClaudeが使った証明戦略、特殊クラス、計算実験に縛られず、必要なら出発点を変えて構いません。問題を肯定的に解く構成も、否定的に解く一般上界も、どちらも歓迎します。思いつく限り異なる数学的観点を試してください。

> **Open problem `op:fanout-two`.** Fix a fan-out bound \(f\ge2\) and maximal rule rank \(r_{\max}\ge2\). Is the pseudovariety \(\mathbf{LG}\) exactly the boundary for **uniform polynomial characteristic-data length** among classes of \((f,s)\)-tuple-substitutable multiple context-free languages? Equivalently, does every pseudovariety of finite semigroups \(\mathbf V\not\subseteq\mathbf{LG}\) *fail* uniform polynomial characteristic-data length at fan-out \(f\) and rank \(r_{\max}\)?

LG側の多項式上界はすでに全fan-outで証明されています。未解決なのは、**LGの外側で一様多項式上界が必ず破れるかどうか**です。

特に \(f=2\), \(r_{\max}=2\) は最重要の出発点です。ここで強い下界が得られても、それを \(f\ge3\) に移す際には別途証明が必要です。

### 一つの十分な解決経路（これに限定しない）

\(U_1=\{1,\zeta\}\), \(\zeta^2=\zeta\) を単位元1と零元\(\zeta\)を持つ2元モノイドとし、固定の全射型付け

\[
 s_U:\{a,b,c\}^+\twoheadrightarrow U_1,
 \quad s_U(a)=s_U(b)=1,\quad s_U(c)=\zeta
\]

を用いる。次のすべてを満たす \(L_n,G_n\) を構成できれば、重要な肯定的解答への道が開きます。

1. \(L_n\in\mathcal C^{\mathrm{mcf}}_{2,s_U}\)。とくに**2穴の組代入可能性**を証明する。
2. \(G_n\) は \(L_n\cap\Sigma^+\) の **reduced good** なMCFG提示で、fan-out \(\le2\)、rule rank \(\le2\)。
3. \(\|G_n\|\) と元の文法の厚さ \(\bar\theta_{G_n}\) は \(n\) の多項式以下。
4. 全ての正例の特徴標本が、\(\|G_n\|,\bar\theta_{G_n}\) に関して**超多項式**の総長を強制されることを証明する。

例えば、実現される型 \(1\) の最短語長 \(\mu_1(L_n)\) が超多項式であれば、現行論文の `prop:rare-type` により十分です。ただし**その型の語が唯一である必要はありません**。また、希少型に依存せず、\(L'_n\subsetneq L_n\)（両方とも同じ目標クラス）の区別語が全て長いことから下界を示す方法もあります。さらに別の下界証明手段を創出して構いません。

**重要：** \(U_1\) の特定の型付けで一様上界が破れることは肯定的解答のための有力な十分条件です。一方、ある一つの \(U_1\) 型付けについて多項式上界を示しただけでは、一般の開問題への否定的解答にはなりません。反対方向を主張するなら、擬多様体・型付けの全称量化を正確に扱ってください。

---

## 一次資料：GitHubを読んでから研究してください

**Repository:** https://github.com/growupkuriyama-hub/Papers  
**Paper #2 directory:** https://github.com/growupkuriyama-hub/Papers/tree/main/02-v2-lg-fanout-boundary

まず以下の3件を優先して確認してください。閲覧可能ならGitHubから直接読むか、リポジトリをcloneしてください。

1. **現行の正式な問題・定義・既知結果（最優先の権威ある資料）**  
   [main.tex](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/main.tex)  
   とくに `def:grammar-properties`、`def:tuple-substitutable`、`def:uniform-polydata`、`prop:rare-type`、`lem:distinguishing`、`lem:power-transfer`、`thm:doubling-no-lift`、`op:fanout-two`。本文内の完全な仮定と証明を読んでください。  
   [正式なopen problem付近](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/main.tex#L2130-L2148) ／ [2穴定義付近](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/main.tex#L486-L529) ／ [非持ち上げ定理](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/main.tex#L2044-L2113)
2. **この研究の現在位置と既存結果の状態**  
   [HANDOFF_CURRENT.md](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/HANDOFF_CURRENT.md)  
   古い記録よりもこれを優先してください。2026-11-15時点で `op:fanout-two` はOPENです。
3. **特殊クラス \(U_2\) の研究用上界・独立監査（重要な既知の障壁だが、探索の必須路線ではない）**  
   [U₂ independent theorem note](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/reviews/theorem_U2_overlapping_projections_standalone_2026-11-15.md)  
   [U₂ scope and proof status](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/reviews/STATUS_U2_STANDALONE_FORMALIZATION_2026-11-15.md)  
   この結果は、\(\Sigma=\{a,b,c\}\)、\(A=\{a,c\}, B=\{b,c\}\)、長さ2の射影bigramデータで決まる**特殊言語クラス**の多項式代表長上界に関する手証明案（独立監査 `VALID WITH CLARIFICATIONS`）です。**一般の \(U_1\) 型付けやLG境界を証明したものではありません。** 必要であればこの上界から脱出するような構成を考えてください。

**追加のGitHub資料（必要になったら参照）**

- [第十一段：原報告・Python・監査・ログの完全ソース束](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/reviews/ROUND11_SOURCE_BUNDLE_2026-11-15.md)
- [第十一段：残余ケースを閉じるClaude原報告](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/reviews/claude_fanout2_round11_residual_report_2026-11-15.md)
- [第十一段：独立数学監査](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/reviews/audit_claude_fanout2_round11_independent_2026-11-15.md)
- [第十段：上界統合のClaude原報告](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/reviews/claude_fanout2_round10_U2_integration_report_2026-11-14.md)
- [第九段：P1/B6の原報告](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/reviews/claude_fanout2_round9_P1_B6_report_2026-11-14.md)
- [過去の研究用原稿にある「希少型で唯一の語」の剛性分類（**現行原稿ではなく履歴資料**）](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/parked/2026-11-06_focus/main_before_focus_59pp.tex) の `lem:unique-word-rigid`、`prop:unique-two-letter-shapes`、`thm:app-singleton`。これを定理として使う場合は、現行仮定との整合性を独立に確認すること。

GitHubの閲覧権限やネットワークの問題でこれらを開けない場合は、**読めたと装わず**その旨を報告し、必要なファイルの添付を要求してください。本文を読めないまま、曖昧な要約だけから定理を「証明済み」として扱わないでください。

注：直近の「第十二段」の下界候補探索は**まだGitHub未収録**です。その暫定的な知見は、新しい独立発想に先入観を与えないため、ここでは前提にしません。

---

## 自由研究への要望

ここから先の研究戦略は、あなたに任せます。既存のClaudeによる上界補題の延長や、小さい候補文法を大量生成する方式を繰り返す必要はありません。研究対象を適切に抽象化し、別分野の道具を持ち込むことも歓迎します。**中心的開問題がYESともNOとも仮定せず**、どちらが数学的に見込みがあるかを自分で評価してください。

候補の例としては、新規のMCFG族、組分布の代数、非可換な不変量、語の配置制約、有限指数の合同、符号化に頼らない下界、区別可能な部分標的、一般的な短縮定理などが考えられますが、**これは発想を制限するリストではありません**。あなたがもっとよい見方を発見した場合は、これらを無視して構いません。

単なる文献解説ではなく、**自身の定義・補題・構成・反例・計算機実験から前進すること**を目指してください。既存論文や過去のClaudeの主張が誤っていれば、遠慮なく反証してください。重要な反例一つでも価値があります。

### 数学的に譲れない要件

- **組代入可能性は全称命題。** 各 \(d=1,2\)、すべての同型タプル \(\mathbf x,\mathbf y\in(\Sigma^+)^d\) について、受理可能文脈 \(E\in\mathcal E_d\) を共有したら、その \(d\) 次分布が一致する必要があります。2穴の間の固定部分は **非空**。適切な反例は \(\mathbf x,\mathbf y,E,F\) と各充填語を明記してください。
- **文法パラメータを取り違えない。** `good` は ε-free、nondeleting、nonpermuting、nonmerging。fan-outは非終端の成分数、rankは右辺の非終端出現数です。\(\bar\theta_G\) は**元の提示文法**の厚さ。生成する長い語だけを示しても下界にはなりません。
- **既存のno-lift定理を尊重する。** 古い\(W_n\)や、そのletter-disjoint morphismの単純な持ち上げは一般に破綻します。ただし冪移動は語長とParikhベクトルを保存するので、「同じ型の語に短いものが存在する」と結論づけてはいけません。
- **十分条件と必要条件を分ける。** 「唯一の型1語」を要求する必要はありません。特別な族を一つ否定しても一般の超多項式下界不可能性は言えず、一つの特殊クラスで多項式上界を証明してもLG境界は否定されません。
- **有限実験は証明ではない。** 実験で真らしい一般命題には証明義務を付ける。反例・失敗候補には一般の\(n\)への延長と固定した型付けの条件を確かめる。証明のない補題を暗黙に引用しない。
- **量化の順番を守る。** 定義 `def:uniform-polydata` において多項式 \(p\) は \(f,r_{\max},s,\Sigma\) に依存してよいが、\(L,G\) には依存できません。固定の型付けとアルファベットのまま超多項式族を作ることが重要です。

### 成果をどう残してほしいか

途中で方針を自分で切り替えて構いません。時間や計算資源の使い方も自律的に決めてください。最終的に以下を残してください。

1. **日本語の数学研究報告 `fable_fanout2_open_problem_report.md`**。研究した主なアイデア、正確な定義、証明済み命題、条件付き命題、反例、未解決の障壁、現在の最も有望な道筋を明確に区別する。
2. **有望な数学的成果について再現可能な証明・反例証明書**。MCFG規則、長さ・厚さの計算、2穴分布の一般論証、具体的な反例四つ組など、第三者が追跡できる内容にする。
3. **必要に応じてコードと実行ログ**。有界検査を用いた場合、探索した範囲、シード、実行方法、成功・失敗例を残す。Lean等の形式化や外部研究文献の利用も自由だが、行ったことだけを正確に記録する。
4. **最後に短い結論**：`SOLVED YES`、`SOLVED NO`、`NEW THEOREM BUT OPEN`、`OBSTRUCTION/COUNTEREXAMPLE ONLY`、`INCONCLUSIVE` のいずれかを選び、解決した対象と未解決の部分を量化込みで述べる。

**研究成果はまだ論文化しないでください。GitHubへの書き込み・既存原稿の修正はしないでください。** 既存資料は読み取り専用で利用し、成果物はこのセッションで提示してください。

---

## 最初の行動

最初に `main.tex` の正式な定義・open problem・no-lift定理と `HANDOFF_CURRENT.md` を読み、上記の問題設定に誤りがないか確認してください。その後は、あなた自身が最も可能性を感じる方向に、**自律的な数学研究として**取り組んでください。

**求めているのは、以前の研究の続きの作業員ではなく、別の視点から中心的開問題に挑む研究者です。**

===== END FILE =====

===== BEGIN FILE V3.txt bytes=736 sha256=d47d8cbdf1b596e60257afef69d72012bd9d04f732deea367fc98163bdad988a =====
bbbaadbaaddbbaadbaaddd
bbbaadbaaddbbaadcaedd
bbbaadbaaddbcaebaaddd
bbbaadbaaddbcaecaedd
bbbaadbaaddcbaaded
bbbaadbaaddccaeed
bbbaadcaedbbaadbaaddd
bbbaadcaedbbaadcaedd
bbbaadcaedbcaebaaddd
bbbaadcaedbcaecaedd
bbbaadcaedcbaaded
bbbaadcaedccaeed
bbcaebaaddbbaadbaaddd
bbcaebaaddbbaadcaedd
bbcaebaaddbcaebaaddd
bbcaebaaddbcaecaedd
bbcaebaaddcbaaded
bbcaebaaddccaeed
bbcaecaedbbaadbaaddd
bbcaecaedbbaadcaedd
bbcaecaedbcaebaaddd
bbcaecaedbcaecaedd
bbcaecaedcbaaded
bbcaecaedccaeed
bcbaadebbaadbaaddd
bcbaadebbaadcaedd
bcbaadebcaebaaddd
bcbaadebcaecaedd
bcbaadecbaaded
bcbaadeccaeed
bccaeebbaadbaaddd
bccaeebbaadcaedd
bccaeebcaebaaddd
bccaeebcaecaedd
bccaeecbaaded
bccaeeccaeed
cbbaadbaadde
cbbaadcaede
cbcaebaadde
cbcaecaede
ccbaadee
cccaeee
===== END FILE =====

===== BEGIN FILE audit_fable_fanout2_independent_2026-11-15.md bytes=9775 sha256=19c88f1a1f65ae2faa3214f8aab622339a12475a99395d1dd55dd3789fa09352 =====
# Fable の `op:fanout-two` 独立探索：数学監査（2026-11-15）

**入力:** `新しいフォルダー(20261115-114855).zip`、`fable_fanout2_open_problem_report.md`、`cert_L3_to_baab_pruned.json`、`verify_cert.py`、実験ログ、および入れ子の `fable_fanout2_package_2026-11-15.zip`。

**判定:** **NEW STRUCTURAL RESULTS; CENTRAL OPEN PROBLEM STILL OPEN.** 以下の Fable-A の証明書は、Fableの検証器の再実行に加え、**別実装の直接列挙によって33ステップすべてを検証**した。Fable-B の証明は現行原稿の thickness lemma を用いる論理として妥当と評価する。Fable-C は実質的に興味深いが、長い組合せ論的手証明について**完全な独立逐行認証は未実施**であり、研究用の `CLAIMED PROOF / NEEDS ADVERSARIAL LINE-BY-LINE REVIEW` とする。新規性の文献調査は未実施。

**重要:** Fable-A/B/C はこの報告書内の仮称。論文 #2 の既存 Theorems A/B/C と混同しない。

## 1. 中心問題に対する結論

現行論文 `op:fanout-two`（`main.tex`）の問い、すなわち任意の擬多様体 \(\mathbf V\not\subseteq\mathbf{LG}\) が fan-out \(f\ge2\)、rank \(r_{\max}\ge2\) で一様多項式特徴データ長に失敗するかは、**依然 OPEN**。Fable は YES 方向の超多項式下界構成も、NO 方向の一般多項式上界も証明していない。Fable の「NO が見込み高い」は根拠ある研究上の**予想**であって定理・確率ではない。

## 2. Fable-A：倍増族の定数長への崩壊

### 2.1 定理の正確な射程

\(L_n\) は現行 `prop:three-letter-family` の言語、\(W_0=a\)、\(W_{n+1}=bW_nW_nb\)。\(n\ge3\) で **言語全体** \(L_n\subseteq L\) かつ \(L\in\mathcal C^{\mathrm{mcf}}_{f,s}\)、\(f\ge2\)、\(s\) が半束型付けなら \(baab=W_1\in L\)。したがって実現型 \(s(W_n)=s(W_1)\) は長さ \(\le4\) の受理語を持つ。非消去射 \(\psi\) による \(\psi(L_n)\subseteq L\) でも \(\psi(baab)\in L\)。

**既存の `thm:doubling-no-lift` と論理的に別の射程:** 既存定理は任意の有限半群型付けで *単一の* \(W_n\) の受理だけから同型・同Parikhの別の語の存在を結論する。Fable-A は **半束型付けと \(L_n\) 全体の受理**という強い仮定の下、**定数長**というより強い結論を出す。既存定理の全面的な論理的強化、あるいは \(W_n\in L\Rightarrow baab\in L\) ではない。

### 2.2 独立再実行

- Fable 提供の `verify_cert.py` を原の `cert_L3_to_baab_pruned.json` に対し再実行：**PASS**。`L_3` と \(a\mapsto W_k\) の \(k=1,2,4\) による輸送を再実行：**PASS**。
- **Fableコードから独立**の `independent_cert_audit.py` を新規作成：`L_3` を再帰生成（42語）、二穴文脈の中間固定部分の非空性、成分の非空性、成分内容型一致、既知の受理語3つ、追加語の連結を33手すべて各々検証：**PASS**。
- 33手の内訳：2穴24手、1穴9手。最終語 \(baab\)、途中で \(W_2=bbaabbaabb\) も導出。追加された異なる語は22語。
- 別実装の再帰認識器で \(\varphi_k(L_3)\subseteq L_{k+3}\) を \(k=0,1,2\) について42語ずつ検証：**PASS**。無限の \(k\) については添付の文法代入・非消去射輸送の一般論証による。

### 2.3 有限証明書から全 \(n\) への論理鎖

(1) 33手の証明書により \(W_1,W_2\in\mathrm{Cl}(L_3)\)。\(W_3\) は元の \(L_3\) にある。(2) \(a\mapsto W_k\), \(b\mapsto b\), \(c\mapsto c\) は非消去射 \(\varphi_k\)。導出文法の \(E_{k+3}\) から \(\varphi_k(L_3)\subseteq L^{(k+3)}\) が成立。(3) \(k+3\le n\) のとき、\(L^{(k+3)}\) は \(L_n\) のある二側文脈 \(P_k\square Q_k\) 内に出現する。(4) 射輸送とコンテキスト付加により \(P_kW_{k+1}Q_k,P_kW_{k+2}Q_k,P_kW_{k+3}Q_k\in L\)。(5) 半束型では3語の型が一致し、\(d=1\) の代入可能性により三語の受理分布が一致。(6) \(W_n\in L\) から \(j=n,\dots,3\) に帰納して \(W_{j-1}\in L\)、最後に \(W_1\in L\) を得る。

上記は全称の論証で、単に \(n\le7\) の実験結果を一般化しているわけではない。**判定: VALID FOR THE STATED SCOPE (explicit certificate + independent replay + transparent transport).**

## 3. Fable-B：アーベル剰余類の短い区別証人

\(G\) を reduced good MCFG、rule rank \(\le r\)、\(\theta=\bar\theta_G\)、\(g:\Sigma^*\to\mathsf A\) をアーベル群への準同型、\(\gamma+H\) を剰余類とする。\(L(G)\) の長さ \(\le(r+2)\theta\) の全語の \(g\)-値が当該剰余類に入れば、\(L(G)\) の全語が同じ剰余類に入る。対偶により逸脱する語が存在するなら長さ \(\le(r+2)\theta\) の逸脱語も存在する。

**監査:** `lem:thickness-equivalence` (i),(ii),(iv) から、各非終端の短い代替収率は長さ \(\le\theta\)、文脈固定部は長さ \(\le\theta\)、規則の明示端末は高々 \(\theta\)。任意の rank \(q\le r\) 規則で \(E_A[\rho(\mathbf u_{B_1},\ldots,\mathbf u_{B_q})]\) の長さは \(\le(q+2)\theta\) となり、\(E_A[\mathbf u_A]\) とともに同じ剰余類に入る。可換群で固定文脈の寄与を相殺できるから、規則を通じて各非終端の Parikh 型が剰余類 \(g(\mathbf u_A)+H\) に固定される。導出帰納法で根へ持ち上がる。**主張の論証は整合的**。この命題にはそもそも組代入可能性を要しない。

**注意:** `lem:distinguishing` を応用するなら \(L'=L\cap g^{-1}(\gamma+H)\) が真の部分言語である場合に限る。アーベル剰余類で切る手法ではこの形の超多項式区別長下界は生じないが、非アーベル・言語固有の部分標的一般を排除しない。**判定: VALID WITH STATED ASSUMPTIONS.**

## 4. Fable-C：可換言語の単項型の上界

報告は、\(L\) が語順に対して可換、固定 \(\Sigma=\{a\}\sqcup\Delta\)（\(D=|\Delta|\)）、半束型付けで組代入可能、\(a^N\) が最短の受理 \(a\)-冪であれば \(N=O_{D,r}(v\theta^{1+D+D^22^D})\) と主張する。対象は**単項**、**可換な言語**であり、一般の中心問題を解かない。

**数学的監査メモ:** 1穴代入可能性の下で \(a^i\equiv a^{i'}\) が最短 \(a\)-冪を短縮すること（補題U）、可換性を使った \(\Delta\)-Parikh 部品の交換、短い導出収率の Parikh ベクトル間の有界整数関係、分岐クラスと非分岐クラスの分離、重い子の窓被覆、の骨格は整合的に見える。特に Fable 報告 §5(2) の交換は、\((N-\delta(V),V),(N-\delta(V'),V')\in P\) から同じ \(a\)-文脈で内容型が等しい二語を作れば導ける。§5(3) の二つの部品への置換順は、欠損の小さい元の方を残してから交換する必要がある。

**未完の独立検証:** §5(3) の任意多重集合への加法性、§5(5) の非分岐支持類が高々二本の根道に載る主張、§5(6) の厚さを伴う窓被覆・指数定数の全量化を、別実装や独立した逐行完全証明としてはまだ検証していない。独立監査において致命的な反例を確認したわけではないが、Fable自己申告の `[証明]` を外部認定したものでもない。**判定: PROMISING HAND-PROOF; FULL INDEPENDENT CERTIFICATION PENDING.**

## 5. その他の主張の扱い

- **命題1（SL還元）:** \(U_1\) が有限半束擬多様体 \(\mathbf{SL}\) を生成すること、\(\mathbf V\not\subseteq\mathbf{LG}\Rightarrow U_1\in\mathbf V\) と定義の全称／存在量化から導ける。上界側で内容型付けに還元する際は、任意の半束型付けが内容型付けを通じて因子化すること、および \(\mathcal C_{f,s}\subseteq\mathcal C_{f,c_\Sigma}\) に注意。**論理的な整理として妥当**。
- **補題2.1/系2.2（滑り・共役移送）:** 二穴の共通受理文脈は \(zm=mz'\) により文字どおり同じ語に埋まるので妥当。任意の \(m'\ne\varepsilon\) の転送は定義どおり。
- **補題2.4/2.5（閉包・非消去射）:** 内容型を使う限り妥当。穴間の \(\Sigma\) 上の非空区切りは非消去射で維持される。
- **別括弧の A′:** C++ ハッシュ探索による到達報告のみ。**数学的定理としては未監査／明示証明書なし**。元の `cert_L3_to_baab_pruned.json` はこの族の証明書ではない。
- **実験での L2 の分類:** 有限長打切りの観察。L2 の全無制限閉包の一般定理ではない。
- **「Fable-B/Cは新規」という評価:** 文献調査および先行ラウンドの既存補題との重複チェックは未実施。

## 6. 次の数学的優先順位

1. **Fable-C の逐行 adversarial 監査**（特に §5(3), (5), (6) と命題 E の補完）。正しければ「可換で単項型」の下界方向は閉じる。
2. **非可換の単項予想 U** を進める：Euler 的な再結合が常に共通受理ホストを持つか、明示的な反例を構成する。これは中心問題の YES/NO を決める補題ではまだない。
3. **非アーベルな区別部分標的**の探索、または `SL` 全体の uniform-polydata を決める別の原理を探す。下界仮説一本に固執しない。
4. 別括弧変種 A′ に対しハッシュ非依存の有限証明書を抽出する。ただし中心問題への直接寄与は限定的。

**GitHub/論文:** 今回はユーザーから更新依頼がないため変更していない。論文本文に Fable-A/B/C を新定理として自動挿入していない。

===== END FILE =====

===== BEGIN FILE build_cert.py bytes=3568 sha256=791271975ba1ba70ccbc5b9e9edbbcfdef9535bd4f131d3d181ea644d0eaca4f =====
# Builds an explicit substitution certificate: L_3  |-  baab  (content typing, fan-out 2)
import json
from collections import defaultdict, deque
from closure import occs, Ln, tC
def fill(E,x): return E[0]+x[0]+E[1] if len(x)==1 else E[0]+x[0]+E[1]+x[1]+E[2]
def graph(S,d,cfree_only=False):
    ctx2t=defaultdict(set); t2c=defaultdict(set)
    for w in S:
        for x,E in occs(w,d):
            if cfree_only and any('c' in c for c in x): continue
            ctx2t[E].add(x); t2c[x].add(E)
    adj=defaultdict(list)
    for E,ts in ctx2t.items():
        bt=defaultdict(list)
        for x in ts: bt[tuple(tC(c) for c in x)].append(x)
        for lst in bt.values():
            for x in lst[1:]:
                adj[lst[0]].append((x,E)); adj[x].append((lst[0],E))
    return t2c,adj
def path(adj,x,y):
    prev={x:None}; dq=deque([x])
    while dq:
        u=dq.popleft()
        if u==y: break
        for v,E in adj[u]:
            if v not in prev: prev[v]=(u,E); dq.append(v)
    assert y in prev, (x,y)
    p=[]; u=y
    while prev[u] is not None:
        q,E=prev[u]; p.append((q,u,E)); u=q
    return p[::-1]   # list of (from,to,E0)
L0=Ln(3); S=set(L0); steps=[]
def apply(E1,pth):
    # pth: links (u,v,E0); E1[u0] in S
    for u,v,E0 in pth:
        assert fill(E1,u) in S and fill(E0,u) in S and fill(E0,v) in S
        w=fill(E1,v)
        steps.append({"d":len(u),"E0":list(E0),"x":list(u),"y":list(v),"E1":list(E1),"new":w})
        S.add(w)
# Phase A: one class pass (d=2) over L0, with explicit paths
t2c,adj=graph(L0,2)
comp={}
for x in list(t2c):
    if x in comp or not adj[x]: continue
    members=[x]; comp[x]=x; dq=deque([x])
    while dq:
        u=dq.popleft()
        for v,E in adj[u]:
            if v not in comp: comp[v]=x; members.append(v); dq.append(v)
    ctxs={}
    for m in members:
        for E in t2c[m]: ctxs.setdefault(E,m)
    for y in members:
        for E,xp in ctxs.items():
            if E in t2c[y]: continue
            w=fill(E,y)
            if len(w)<=22 and w not in S: apply(E,path(adj,xp,y))
print("after phase A |S|=",len(S),"steps",len(steps))
# Phase B: c-free d=1 equivalences over S, plus the b-slide (b,bb)~(bb,b) from L0
t1,adj1=graph(S,1,cfree_only=True)
def rep1(w,i,j,y):   # replace factor w[i:j] by y
    x=(w[i:j],); assert w in S
    apply((w[:i],w[j:]),path(adj1,x,(y,)))
    return w[:i]+y+w[j:]
def slide(w,i,j,k,l,y):  # replace tuple (w[i:j],w[k:l]) by y using d=2 graph on L0
    x=(w[i:j],w[k:l]); assert w in S
    apply((w[:i],w[j:k],w[l:]),path(adj,x,y))
    return w[:i]+y[0]+w[j:k]+y[1]+w[l:]
w="bbbaabbaabbbbaabbaabbb"; assert w in L0
def R1(w):
    i=w.index("bbbaa"); return rep1(w,i,i+5,"ba")
def R2(w):
    i=w.index("babbaa"); return rep1(w,i,i+6,"baa")
def mv(w,src):  # move one b from run starting at index src (take 'bb' there -> 'b') to the first b-run
    # first component: last b of the leading run; second: 'bb' at src
    i=0
    while w[i+1]=='b': i+=1
    assert w[src:src+2]=="bb"
    return slide(w,i,i+1,src,src+2,("bb","b"))
log=[w]
w=R1(w); log.append(w); w=R2(w); log.append(w)          # baa bbbb aa bb aa bbb
w=mv(w,w.index("bbbb")); log.append(w); w=mv(w,w.index("aabbb")+2); log.append(w)
w=R1(w); log.append(w); w=R2(w); log.append(w)          # baa bb aa bbb
w=mv(w,len(w)-3); log.append(w); w=mv(w,len(w)-2); log.append(w)
w=R1(w); log.append(w); w=R2(w); log.append(w)
print("\n".join(log)); assert w=="baab"
json.dump({"start":"L_3","typing":"content","steps":steps,"goal":"baab"},open("cert_L3_to_baab.json","w"))
print("total steps",len(steps))

===== END FILE =====

===== BEGIN FILE cert_L3_to_baab_pruned.json bytes=4905 sha256=7188c424fce6f372468cf46b274a9e680927d2355266e25b9d2163f3a07df7c0 =====
{
"start": "L_3",
"typing": "content",
"goal": "baab",
"steps": [
{
"d": 2,
"E0": [
"",
"b",
"cacbbbaabbaabbb"
],
"x": [
"b",
"baab"
],
"y": [
"bb",
"aab"
],
"E1": [
"bcbaa",
"cb",
"cacbb"
],
"new": "bcbaabbcbaabcacbb"
},
{
"d": 2,
"E0": [
"",
"aabcbc",
"b"
],
"x": [
"bcb",
"accacb"
],
"y": [
"bcb",
"acbaabb"
],
"E1": [
"",
"aabcbc",
"b"
],
"new": "bcbaabcbcacbaabbb"
},
{
"d": 2,
"E0": [
"",
"ab",
"accacbb"
],
"x": [
"bbcacba",
"bbc"
],
"y": [
"bcba",
"cbc"
],
"E1": [
"",
"a",
"baabcb"
],
"new": "bcbaacbcbaabcb"
},
{
"d": 2,
"E0": [
"",
"ab",
"accacbb"
],
"x": [
"bcba",
"cbc"
],
"y": [
"bbcacba",
"bbc"
],
"E1": [
"",
"ab",
"accacbb"
],
"new": "bbcacbaabbbcaccacbb"
},
{
"d": 2,
"E0": [
"",
"ab",
"accacbb"
],
"x": [
"bcba",
"cbc"
],
"y": [
"bbcacba",
"bbc"
],
"E1": [
"",
"ab",
"acbaabbb"
],
"new": "bbcacbaabbbcacbaabbb"
},
{
"d": 2,
"E0": [
"",
"c",
"b"
],
"x": [
"bcbaab",
"cbaabc"
],
"y": [
"bcbaabcbbaab",
"acb"
],
"E1": [
"",
"b",
"acbb"
],
"new": "bcbaabcbbaabbacbacbb"
},
{
"d": 2,
"E0": [
"",
"bc",
"b"
],
"x": [
"bcbaa",
"cbaabc"
],
"y": [
"bcbaabcbbaa",
"acb"
],
"E1": [
"",
"cb",
"b"
],
"new": "bcbaabcbbaacbacbb"
},
{
"d": 2,
"E0": [
"",
"bc",
"b"
],
"x": [
"bcbaa",
"cbaabc"
],
"y": [
"bcbaa",
"bbaabcacb"
],
"E1": [
"",
"cb",
"b"
],
"new": "bcbaacbbbaabcacbb"
},
{
"d": 2,
"E0": [
"",
"bc",
"b"
],
"x": [
"bcbaa",
"bcaccacb"
],
"y": [
"bcbaa",
"cbaabc"
],
"E1": [
"",
"bc",
"b"
],
"new": "bcbaabccbaabcb"
},
{
"d": 2,
"E0": [
"",
"bc",
"b"
],
"x": [
"bcbaa",
"cbaabc"
],
"y": [
"bbcaccac",
"baabc"
],
"E1": [
"",
"bc",
"b"
],
"new": "bbcaccacbcbaabcb"
},
{
"d": 2,
"E0": [
"",
"cbaab",
""
],
"x": [
"bcbaabc",
"cb"
],
"y": [
"bbcacbaabb",
"cb"
],
"E1": [
"",
"bbaabca",
"b"
],
"new": "bbcacbaabbbbaabcacbb"
},
{
"d": 2,
"E0": [
"",
"b",
"aabbaabbb"
],
"x": [
"bcbaabc",
"b"
],
"y": [
"bbcacbaabb",
"b"
],
"E1": [
"",
"cbaa",
"cb"
],
"new": "bbcacbaabbcbaabcb"
},
{
"d": 2,
"E0": [
"",
"b",
"aabbaabbb"
],
"x": [
"bcbaabc",
"b"
],
"y": [
"bbcacbaabb",
"b"
],
"E1": [
"",
"bbaabbaabb",
""
],
"new": "bbcacbaabbbbaabbaabbb"
},
{
"d": 2,
"E0": [
"b",
"c",
"b"
],
"x": [
"bcaccacb",
"baabc"
],
"y": [
"cbaabcb",
"accacb"
],
"E1": [
"b",
"c",
"b"
],
"new": "bcbaabcbcaccacbb"
},
{
"d": 2,
"E0": [
"b",
"c",
"b"
],
"x": [
"cbaabcb",
"accacb"
],
"y": [
"cbaab",
"bbaabcacb"
],
"E1": [
"b",
"c",
"b"
],
"new": "bcbaabcbbaabcacbb"
},
{
"d": 2,
"E0": [
"bcbaabcbca",
"b",
""
],
"x": [
"cbaab",
"b"
],
"y": [
"cbaa",
"bb"
],
"E1": [
"bbcacbaabb",
"c",
""
],
"new": "bbcacbaabbcbaacbb"
},
{
"d": 2,
"E0": [
"b",
"bc",
"aabbb"
],
"x": [
"cbaa",
"bcacb"
],
"y": [
"bcacbaabb",
"acb"
],
"E1": [
"b",
"cbbbaa",
"b"
],
"new": "bbcacbaabbcbbbaaacbb"
},
{
"d": 2,
"E0": [
"b",
"c",
"cacbb"
],
"x": [
"bca",
"baabbbbaab"
],
"y": [
"cbaab",
"bbaab"
],
"E1": [
"b",
"c",
"baabbb"
],
"new": "bcbaabcbbaabbaabbb"
},
{
"d": 2,
"E0": [
"",
"a",
"bbbaabbaabbb"
],
"x": [
"bbba",
"bbaab"
],
"y": [
"bbbaabb",
"ab"
],
"E1": [
"",
"abbaabb",
"baabbb"
],
"new": "bbbaabbabbaabbabbaabbb"
},
{
"d": 2,
"E0": [
"bcbaabc",
"a",
"bb"
],
"x": [
"bba",
"bbaab"
],
"y": [
"bbaabb",
"ab"
],
"E1": [
"bbbaa",
"abb",
"baabbb"
],
"new": "bbbaabbaabbabbabbaabbb"
},
{
"d": 1,
"E0": [
"bbcacbaabbc",
"acbb"
],
"x": [
"bbbaa"
],
"y": [
"ba"
],
"E1": [
"",
"bbaabbbbaabbaabbb"
],
"new": "babbaabbbbaabbaabbb"
},
{
"d": 1,
"E0": [
"bbbaab",
"bbabbaabbb"
],
"x": [
"babbaa"
],
"y": [
"baabba"
],
"E1": [
"",
"bbbbaabbaabbb"
],
"new": "baabbabbbbaabbaabbb"
},
{
"d": 1,
"E0": [
"bcbaabcb",
"cbacbb"
],
"x": [
"baabba"
],
"y": [
"baa"
],
"E1": [
"",
"bbbbaabbaabbb"
],
"new": "baabbbbaabbaabbb"
},
{
"d": 2,
"E0": [
"bbcacbaa",
"b",
"aabbaabbb"
],
"x": [
"b",
"bb"
],
"y": [
"bb",
"b"
],
"E1": [
"",
"aa",
"bbaabbaabbb"
],
"new": "bbaabbbaabbaabbb"
},
{
"d": 2,
"E0": [
"bbcacbaa",
"b",
"aabbaabbb"
],
"x": [
"b",
"bb"
],
"y": [
"bb",
"b"
],
"E1": [
"b",
"aa",
"baabbaabbb"
],
"new": "bbbaabbaabbaabbb"
},
{
"d": 1,
"E0": [
"bbcacbaabbc",
"acbb"
],
"x": [
"bbbaa"
],
"y": [
"ba"
],
"E1": [
"",
"bbaabbaabbb"
],
"new": "babbaabbaabbb"
},
{
"d": 1,
"E0": [
"bbbaab",
"bbabbaabbb"
],
"x": [
"babbaa"
],
"y": [
"baabba"
],
"E1": [
"",
"bbaabbb"
],
"new": "baabbabbaabbb"
},
{
"d": 1,
"E0": [
"bcbaabcb",
"cbacbb"
],
"x": [
"baabba"
],
"y": [
"baa"
],
"E1": [
"",
"bbaabbb"
],
"new": "baabbaabbb"
},
{
"d": 2,
"E0": [
"bbcacbaa",
"b",
"aabbaabbb"
],
"x": [
"b",
"bb"
],
"y": [
"bb",
"b"
],
"E1": [
"",
"aabbaa",
"b"
],
"new": "bbaabbaabb"
},
{
"d": 2,
"E0": [
"bbcacbaa",
"b",
"aabbaabbb"
],
"x": [
"b",
"bb"
],
"y": [
"bb",
"b"
],
"E1": [
"b",
"aabbaa",
""
],
"new": "bbbaabbaab"
},
{
"d": 1,
"E0": [
"bbcacbaabbc",
"acbb"
],
"x": [
"bbbaa"
],
"y": [
"ba"
],
"E1": [
"",
"bbaab"
],
"new": "babbaab"
},
{
"d": 1,
"E0": [
"bbbaab",
"bbabbaabbb"
],
"x": [
"babbaa"
],
"y": [
"baabba"
],
"E1": [
"",
"b"
],
"new": "baabbab"
},
{
"d": 1,
"E0": [
"bcbaabcb",
"cbacbb"
],
"x": [
"baabba"
],
"y": [
"baa"
],
"E1": [
"",
"b"
],
"new": "baab"
}
]
}
===== END FILE =====

===== BEGIN FILE cfree_search.cpp bytes=2983 sha256=322957ea7109df3f8ce5f004fdb9fe5a509913418217ee4e22fa3050f875ea21 =====
// reads a word set; computes d=1 equivalence classes among c-free factors (no 'c','e') sharing a context with equal content;
// then BFS-rewrites c-free words by class replacement (length cap) and reports the shortest c-free word reached.
#include <bits/stdc++.h>
using namespace std;
typedef unsigned long long u64;
static inline u64 mix(u64 h,u64 v){h^=v+0x9e3779b97f4a7c15ULL+(h<<6)+(h>>2);h*=0xff51afd7ed558ccdULL;h^=h>>33;return h;}
static u64 hs(const char*s,int n,u64 seed){u64 h=seed;for(int i=0;i<n;i++)h=mix(h,(unsigned char)s[i]);return mix(h,n);}
int main(int argc,char**argv){
  int cap=atoi(argv[1]);int maxf=atoi(argv[2]);
  vector<string> L;string w;while(cin>>w)L.push_back(w);
  unordered_map<string,int> id;vector<string> fs;vector<int> par;
  function<int(int)> find=[&](int a){while(par[a]!=a){par[a]=par[par[a]];a=par[a];}return a;};
  unordered_map<u64,int> ctxrep; ctxrep.reserve(1<<26);
  for(auto&w:L){int n=w.size();
    for(int i=0;i<n;i++){int m=0;for(int j=i+1;j<=n&&j-i<=maxf;j++){char ch=w[j-1];if(ch=='c'||ch=='e')break;m|=1<<(ch-'a');
      string f=w.substr(i,j-i);auto it=id.find(f);int k;if(it==id.end()){k=fs.size();id[f]=k;fs.push_back(f);par.push_back(k);}else k=it->second;
      u64 c=mix(mix(hs(w.data(),i,1),hs(w.data()+j,n-j,2)),m);
      auto r=ctxrep.find(c);if(r==ctxrep.end())ctxrep[c]=k;else{int a=find(k),b=find(r->second);if(a!=b)par[a]=b;}
    }}}
  unordered_map<int,vector<int>> cl;for(size_t k=0;k<fs.size();k++)cl[find(k)].push_back(k);
  int shown=0;
  for(auto&kv:cl){set<int> lens;for(int k:kv.second)lens.insert(fs[k].size());
    if(lens.size()>1&&shown<12){shown++;string a=fs[kv.second[0]],b=a;for(int k:kv.second){if(fs[k].size()<a.size())a=fs[k];if(fs[k].size()>b.size())b=fs[k];}
      fprintf(stderr,"class size %zu lens %d..%d  e.g. %s ~ %s\n",kv.second.size(),*lens.begin(),*lens.rbegin(),a.c_str(),b.c_str());}}
  unordered_set<string> seen;auto cmp=[](const string&a,const string&b){return a.size()>b.size();};priority_queue<string,vector<string>,decltype(cmp)> q(cmp);
  for(auto&w:L)if(w.find('c')==string::npos&&w.find('e')==string::npos){if(seen.insert(w).second)q.push(w);}
  string best=*min_element(seen.begin(),seen.end(),[](const string&a,const string&b){return a.size()<b.size();});
  while(!q.empty()&&seen.size()<3000000){string w=q.top();q.pop();int n=w.size();
    for(int i=0;i<n;i++)for(int j=i+1;j<=n&&j-i<=maxf;j++){auto it=id.find(w.substr(i,j-i));if(it==id.end())continue;
      auto&ms=cl[find(it->second)];if(ms.size()<2)continue;
      for(int k:ms){string v=w.substr(0,i)+fs[k]+w.substr(j);if((int)v.size()>cap)continue;
        if(seen.insert(v).second){q.push(v);if(v.size()<best.size()){best=v;fprintf(stderr,"new best %zu %s\n",best.size(),best.c_str());}}}}}
  for(const char*t:{"baad","bbaadbaadd","adba","abad","baaadbbadd"})printf("target %s reached: %d\n",t,(int)seen.count(t));printf("shortest c-free reached: %zu %s (explored %zu)\n",best.size(),best.c_str(),seen.size());
}

===== END FILE =====

===== BEGIN FILE check_fable_C_independent.py bytes=7662 sha256=fa4af3cbc8ce1af719fa99e96d3d96486b7f413232bb8b93643e55b59060f2f5 =====
#!/usr/bin/env python3
"""Independent finite stress tests of purely combinatorial Fable-C sublemmas.
No Fable sources imported. Not a substitute for the universal proofs.
"""
import random, itertools

rng=random.Random(20261115)

# Exchange-lemma certificate: common word-context E0, accepted target-context E1.
exchange=0
for _ in range(40000):
    N=rng.randint(3,150)
    d1=rng.randrange(1,N); d2=rng.randrange(1,N)
    V1=rng.randint(1,8);V2=rng.randint(1,8);Q=rng.randint(0,8)
    e=rng.randint(1,160)
    ep=e+d1-d2
    if ep<1: continue
    i=1+max(0,d2-d1);ip=1+max(0,d1-d2)
    assert i<=N-d1 and ip<=N-d2 and i<=e
    # E0 = a^(N-d1-i) [] produces (N-d1,V1), (N-d2,V2)
    assert (N-d1-i)+i==N-d1
    assert (N-d1-i)+ip==N-d2
    # E1 = a^(e-i) [] b^Q produces (e,Q+V1),(ep,Q+V2)
    assert e-i+i==e and e-i+ip==ep
    exchange+=1

# Branch seed -> all pairs -> induction for all multisets of eligible delta.
branch=0
for _ in range(550):
    N=rng.randint(5,24)
    k=rng.randint(2,5)
    deficits=[rng.randint(1,(N-1)//2) for _ in range(k)]
    seed_pair=None
    for i in range(k):
      for j in range(i,k):
        if deficits[i]+deficits[j]<=N-1:seed_pair=(i,j);break
      if seed_pair:break
    if seed_pair is None:continue
    # This checks the numerical admissibility of the actual two-step argument.
    db,dc=sorted((deficits[seed_pair[0]],deficits[seed_pair[1]]))
    for i in range(k):
      for j in range(k):
        if deficits[i]+deficits[j]>N-1:continue
        # replace the larger seed atom first, then smaller seed atom
        assert db+deficits[i]<=N-1
        assert deficits[i]+deficits[j]<=N-1
    for m in itertools.product(range(5),repeat=k):
        total=sum(n*d for n,d in zip(m,deficits))
        if not (2<=sum(m)<=5 and total<=N-1):continue
        ind=next((i for i in range(k) if m[i]>0),None)
        # Induction: a pair (J,J') is already producible; replace J by M.
        assert ind is not None
        prev=list(m); prev[ind]-=1
        prevd=total-deficits[ind]
        if sum(prev)<2:continue
        j=next(j for j in range(k) if prev[j]>0)
        assert deficits[j]+deficits[ind]<=total<=N-1
        # previous group of all but one has delta <= total, so new fill is legal
        assert prevd+deficits[ind]==total
    branch+=1

class Node:
    def __init__(self,parent,term):
        self.parent=parent;self.term=term;self.children=[];self.k=0
        self.alpha=0;self.support=None;self.delta=0

def is_ancestor(nodes,i,j):
    while j is not None:
        if i==j:return True
        j=nodes[j].parent
    return False

def tree_test():
    # positive-size leaves; each internal node 1..r children, writing <=theta terminals.
    theta=rng.randint(3,8);r=rng.randint(1,3);D=rng.randint(1,3)
    nodes=[Node(None,0)];frontier=[0]
    for _ in range(rng.randint(12,62)):
        candidates=[i for i in frontier if len(nodes[i].children)<r]
        if not candidates:break
        p=rng.choice(candidates)
        j=len(nodes);nodes.append(Node(p,0));nodes[p].children.append(j)
        frontier.append(j)
        if len(nodes[p].children)>=r:frontier.remove(p)
    for node in nodes:
        node.term=rng.randint(0,theta) if node.children else rng.randint(1,theta)
    for i in reversed(range(len(nodes))):
        nodes[i].k=nodes[i].term+sum(nodes[j].k for j in nodes[i].children)
    N=nodes[0].k
    if N<=3*theta:return 0,0
    bytype={}
    for i,node in enumerate(nodes):
        if node.k<=theta:continue
        node.support=rng.randint(1,(1<<D)-1)
        # ensure short witness with this support (one copy of each type letter)
        vsize=node.support.bit_count()
        if vsize>theta:continue
        node.alpha=rng.randint(0,theta-vsize)
        node.delta=node.k-node.alpha
        bytype.setdefault(node.support,[]).append(i)
    branch_types=set();nonbranch_types=set()
    for typ,inds in bytype.items():
        good=any(not is_ancestor(nodes,i,j) and not is_ancestor(nodes,j,i)
                 and nodes[i].delta+nodes[j].delta<=N-1
                 for i,j in itertools.combinations(inds,2))
        (branch_types if good else nonbranch_types).add(typ)
    # Cover all nodes with nonbranch support using at most two root-to-leaf paths per support.
    leaves=[i for i,n in enumerate(nodes) if not n.children]
    U=set()
    for typ in nonbranch_types:
        inds=bytype[typ]
        possible=[]
        for leaf in leaves:
            possible.append({i for i in inds if is_ancestor(nodes,i,leaf)})
        assert any((inds_set:=set(inds))<=p or inds_set<=(p|q)
                   for p in possible for q in possible),('two-path counterexample',N,typ,inds)
        for p in possible:
            for q in possible:
                if set(inds) <= (p|q):
                    chosen=(p,q);break
            else: continue
            break
        for p in chosen:
            for i in p:
                while i is not None:U.add(i);i=nodes[i].parent
    for i,node in enumerate(nodes):
        if node.k==N:
            while i is not None:U.add(i);i=nodes[i].parent
    # If X not in upward-closed U, heavy chain must pass through branch-class large nodes.
    assert all(nodes[i].parent in U for i in U if nodes[i].parent is not None)
    win=0
    sigma=2*(r+1)
    for X,node in enumerate(nodes):
        if X in U or node.k<=theta:continue
        chain=[];v=X
        while True:
            nn=nodes[v];chain.append(v)
            if not nn.children:break
            v=max(nn.children,key=lambda j:nodes[j].k)
        for y in range(sigma*theta,node.k+1):
            matches=[i for i in chain if nodes[i].k>theta and i not in U
                     and y/sigma <= nodes[i].delta <=y]
            assert matches,('window counterexample',theta,r,D,N,X,y,
                            [(i,nodes[i].k,nodes[i].delta) for i in chain])
            win+=1
    return 1,win

runs=0;windows=0
for i in range(3500):
    good,nw=tree_test();runs+=good;windows+=nw
print('EXCHANGE_CONTEXT_CERTIFICATES',exchange)
print('BRANCH_INDUCTION_NUMERIC_CASES',branch)
print('NONBRANCH_TWO_PATH_RANDOM_TREES',runs)
print('HEAVY_PATH_WINDOW_INSTANCES',windows)
print('ALL INDEPENDENT LOCAL CHECKS PASSED')

# Exhaustively verify the t! theta^t coefficient bound in small dimensions
# by signed-minor construction (no symbolic nullspace package used).
def det(m):
    n=len(m)
    if n==0:return 1
    if n==1:return m[0][0]
    return sum(((-1)**j)*m[0][j]*det([row[:j]+row[j+1:] for row in m[1:]]) for j in range(n))

def relation(cols,dim):
    # Choose a minimal dependent subset of h+1 columns of rank h;
    # select independent rows with nonzero maximal minor.
    import itertools
    for h in range(1,dim+1):
      for ids in itertools.combinations(range(len(cols)),h+1):
        for rows in itertools.combinations(range(dim),h):
          sub=[[cols[i][j] for i in ids] for j in rows]
          coeff=[((-1)**k)*det([row[:k]+row[k+1:] for row in sub]) for k in range(h+1)]
          if not any(coeff):continue
          if all(sum(cols[i][j]*c for i,c in zip(ids,coeff))==0 for j in range(dim)):
            return ids,coeff
    raise AssertionError('No bounded integer relation found')

import math
Cramer=0
for dim, theta in [(1,5),(2,3),(3,2)]:
    vec=[x for x in itertools.product(range(theta+1),repeat=dim) if any(x)]
    B=math.factorial(dim)*theta**dim
    for cols in itertools.combinations_with_replacement(vec,dim+1):
        ids,coeff=relation(cols,dim)
        assert all(abs(c)<=B for c in coeff)
        assert any(c>0 for c in coeff) and any(c<0 for c in coeff)
        Cramer+=1
print('INTEGER_DEPENDENCE_MINOR_CASES',Cramer)
print('ALL CRAMER BOUNDS PASSED')

===== END FILE =====

===== BEGIN FILE clos.cpp bytes=5732 sha256=187a0f2ad1a2d8d32cce975eb74c7abed94f70da182d672e8ea893d7196da089 =====
// 2-substitutable closure (content typing or U1 typing) of a finite language, with length cap.
// usage: clos <typing: content|U1> <maxlen> <maxwords> <maxtuple(total tuple length bound, 0=none)> < words
#include <bits/stdc++.h>
using namespace std;
typedef unsigned long long u64;
static inline u64 mix(u64 h,u64 v){h^=v+0x9e3779b97f4a7c15ULL+(h<<6)+(h>>2);h*=0xff51afd7ed558ccdULL;h^=h>>33;return h;}
static u64 hs(const char*s,int n,u64 seed){u64 h=seed;for(int i=0;i<n;i++)h=mix(h,(unsigned char)s[i]);return mix(h,n);}
bool U1=false;
static inline int typ(const char*s,int n){int m=0;for(int i=0;i<n;i++)m|=1<<(s[i]-'a');if(U1)return (m>>2)&1;return m;}
struct Rec{u64 ctx;u64 tup;};
int main(int argc,char**argv){
  U1=string(argv[1])=="U1";int maxlen=atoi(argv[2]);size_t maxwords=atoll(argv[3]);int maxtup=atoi(argv[4]);
  unordered_set<string> L;string w;while(cin>>w)L.insert(w);
  int round=0;
  while(true){
    round++;
    size_t added=0;
    for(int d=1;d<=2;d++){
      vector<Rec> recs;
      unordered_map<u64,string> tupstr; // tuple hash -> "x1|x2"
      for(const string&w:L){
        int n=w.size();const char*s=w.data();
        if(d==1){
          for(int i=0;i<n;i++)for(int j=i+1;j<=n;j++){
            if(maxtup&&j-i>maxtup&&n-(j-i)>maxtup)continue;
            u64 c=hs(s,i,1);c=mix(c,hs(s+j,n-j,2));c=mix(c,typ(s+i,j-i));
            u64 t=hs(s+i,j-i,7);
            recs.push_back({c,t});
            if(!tupstr.count(t))tupstr[t]=w.substr(i,j-i);
          }
        }else{
          for(int i=0;i<n;i++)for(int j=i+1;j<n;j++)for(int k=j+1;k<n;k++)for(int l=k+1;l<=n;l++){
            int tl=(j-i)+(l-k);
            if(maxtup&&tl>maxtup&&n-tl>maxtup)continue;
            u64 c=hs(s,i,1);c=mix(c,hs(s+j,k-j,3));c=mix(c,hs(s+l,n-l,2));
            c=mix(c,typ(s+i,j-i)*64+typ(s+k,l-k));
            u64 t=mix(hs(s+i,j-i,7),hs(s+k,l-k,9));
            recs.push_back({c,t});
            if(!tupstr.count(t))tupstr[t]=w.substr(i,j-i)+"|"+w.substr(k,l-k);
          }
        }
      }
      sort(recs.begin(),recs.end(),[](const Rec&a,const Rec&b){return a.ctx<b.ctx||(a.ctx==b.ctx&&a.tup<b.tup);});
      unordered_map<u64,u64> par;
      function<u64(u64)> find=[&](u64 a){u64 r=a;while(true){auto it=par.find(r);if(it==par.end()||it->second==r)break;r=it->second;}
        while(a!=r){u64 nx=par[a];par[a]=r;a=nx;}return r;};
      for(size_t i=1;i<recs.size();i++)if(recs[i].ctx==recs[i-1].ctx&&recs[i].tup!=recs[i-1].tup){
        u64 a=find(recs[i].tup),b=find(recs[i-1].tup);if(a!=b)par[a]=b;}
      // classes with >1 member
      unordered_map<u64,vector<u64>> members;
      for(auto&kv:par){members[find(kv.first)].push_back(kv.first);}
      for(auto&kv:members){auto&v=kv.second;if(find(kv.first)==kv.first&&!par.count(kv.first)){} }
      // ensure root included
      for(auto&kv:members){bool has=false;for(u64 x:kv.second)if(x==kv.first)has=true;if(!has)kv.second.push_back(kv.first);}
      if(members.empty())continue;
      // collect contexts per class: need context strings -> second pass over words
      unordered_map<u64,vector<array<string,3>>> ctxs; // class root -> contexts (dedupe by hash)
      unordered_map<u64,unordered_set<u64>> seen;
      for(const string&w:L){
        int n=w.size();const char*s=w.data();
        if(d==1){
          for(int i=0;i<n;i++)for(int j=i+1;j<=n;j++){
            if(maxtup&&j-i>maxtup&&n-(j-i)>maxtup)continue;
            u64 t=hs(s+i,j-i,7);if(!par.count(t))continue;u64 r=find(t);
            u64 c=mix(hs(s,i,1),hs(s+j,n-j,2));
            if(seen[r].insert(c).second)ctxs[r].push_back({w.substr(0,i),"",w.substr(j)});
          }
        }else{
          for(int i=0;i<n;i++)for(int j=i+1;j<n;j++)for(int k=j+1;k<n;k++)for(int l=k+1;l<=n;l++){
            int tl=(j-i)+(l-k);
            if(maxtup&&tl>maxtup&&n-tl>maxtup)continue;
            u64 t=mix(hs(s+i,j-i,7),hs(s+k,l-k,9));if(!par.count(t))continue;u64 r=find(t);
            u64 c=mix(mix(hs(s,i,1),hs(s+j,k-j,3)),hs(s+l,n-l,2));
            if(seen[r].insert(c).second)ctxs[r].push_back({w.substr(0,i),w.substr(j,k-j),w.substr(l)});
          }
        }
      }
      vector<string> nw;
      for(auto&kv:members){
        auto&cs=ctxs[kv.first];
        for(u64 t:kv.second){
          const string&ts=tupstr[t];string x1=ts,x2;
          if(d==2){size_t p=ts.find('|');x1=ts.substr(0,p);x2=ts.substr(p+1);}
          for(auto&c:cs){
            size_t len=c[0].size()+c[1].size()+c[2].size()+x1.size()+x2.size();
            if((int)len>maxlen)continue;
            string nwd=c[0]+x1+c[1]+x2+c[2];
            if(!L.count(nwd))nw.push_back(nwd);
          }
        }
      }
      for(auto&x:nw)if(L.insert(x).second)added++;
      {size_t best=1e9;string bw;for(auto&x:L)if(x.find('c')==string::npos){if(x.size()<best||(x.size()==best&&x<bw)){best=x.size();bw=x;}}
      fprintf(stderr,"round %d d=%d recs=%zu merged-classes=%zu |L|=%zu mincfree=%zu %s\n",round,d,recs.size(),members.size(),L.size(),best,bw.c_str());
      if(L.size()>maxwords){printf("ABORT |L|=%zu mincfree=%zu %s\n",L.size(),best,bw.c_str());if(argc>5){ofstream f(argv[5]);for(auto&x:L)f<<x<<"\n";}return 0;}}
    }
    // report shortest c-free
    size_t best=1e9;string bw;size_t ncf=0;
    for(auto&x:L)if(x.find('c')==string::npos){ncf++;if(x.size()<best||(x.size()==best&&x<bw)){best=x.size();bw=x;}}
    fprintf(stderr,"== round %d |L|=%zu added=%zu c-free=%zu min c-free=%zu (%s)\n",round,L.size(),added,ncf,best,bw.c_str());
    if(!added){printf("CLOSED |L|=%zu mincfree=%zu %s\n",L.size(),best,bw.c_str());break;}
    if(L.size()>maxwords){printf("ABORT |L|=%zu mincfree=%zu %s\n",L.size(),best,bw.c_str());break;}
  }
  if(argc>5){ofstream f(argv[5]);for(auto&x:L)f<<x<<"\n";}
}

===== END FILE =====

===== BEGIN FILE closure.py bytes=2563 sha256=58c5fff3e3337ea8b3cebfe9579802b6b77ef7ab949ae00c1d07b20f077bf676 =====
import sys, itertools
from collections import defaultdict
def occs(w, d):
    n=len(w)
    if d==1:
        for i in range(n):
            for j in range(i+1,n+1):
                yield (w[i:j],), (w[:i], w[j:])
    else:
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    for l in range(k+1,n+1):
                        yield (w[i:j], w[k:l]), (w[:i], w[j:k], w[l:])
def closure(L, typ, maxlen=None, maxsize=200000, verbose=False, dims=(1,2)):
    L=set(L)
    while True:
        new=set()
        for d in dims:
            ctx2t=defaultdict(set); t2ctx=defaultdict(set)
            for w in L:
                for x,E in occs(w,d):
                    ctx2t[E].add(x); t2ctx[x].add(E)
            parent={}
            def find(a):
                while parent.get(a,a)!=a:
                    parent[a]=parent.get(parent[a],parent[a]); a=parent[a]
                return a
            for E,ts in ctx2t.items():
                bytype=defaultdict(list)
                for x in ts: bytype[tuple(typ(c) for c in x)].append(x)
                for lst in bytype.values():
                    r=find(lst[0])
                    for x in lst[1:]:
                        q=find(x)
                        if q!=r: parent[q]=r
            classes=defaultdict(list)
            for x in t2ctx: classes[find(x)].append(x)
            for cl in classes.values():
                if len(cl)==1: continue
                ctxs=set()
                for x in cl: ctxs|=t2ctx[x]
                for x in cl:
                    for E in ctxs-t2ctx[x]:
                        if d==1: w=E[0]+x[0]+E[1]
                        else: w=E[0]+x[0]+E[1]+x[1]+E[2]
                        if maxlen is None or len(w)<=maxlen:
                            if w not in L: new.add(w)
        if verbose: print("size",len(L),"new",len(new),file=sys.stderr)
        if not new: return L, True
        L|=new
        if len(L)>maxsize: return L, False
def Ln(n):
    cur={'a'}
    for i in range(n):
        cur={'b'+x+y+'b' for x in cur for y in cur}|{'c'+x+'c' for x in cur}
    return cur
tU=lambda x: 'c' in x
tC=lambda x: frozenset(x)
if __name__=="__main__":
    n=int(sys.argv[1]); 
    for name,t in (("U1",tU),("content",tC)):
        C,done=closure(Ln(n),t,verbose=True)
        cf=sorted([w for w in C if 'c' not in w],key=lambda w:(len(w),w))
        print(name,"n",n,"closed",done,"size",len(C),"c-free count",len(cf),"min c-free len",len(cf[0]),"lens",sorted(set(map(len,C))))
        print(cf[:10])

===== END FILE =====

===== BEGIN FILE experiments_log.txt bytes=2849 sha256=05bd9e22dfbb4ebcce6ffdb8d5baf8664575f0a2ed7aac269f1e70fab95083ac =====
# Fable fan-out-2 experiments, 2026-11-15 (all runs deterministic; no random seeds are used)
# Tools: clos.cpp (2-substitutable closure, 64-bit hashing of contexts/tuples), cfree_search.cpp (c-free d=1 classes + best-first rewriting),
#        closure.py / build_cert.py (Python reference + certificate builder), verify_cert.py (independent certificate checker).
# All closures are LENGTH-CAPPED, hence under-approximations of the true closure: every word reported IS in the closure
# (up to hash collisions for the C++ tools; the L_3 result is additionally certified by an explicit, hash-free certificate).

g++ -O2 -o clos clos.cpp ; g++ -O2 -o cfree_search cfree_search.cpp
# usage: clos <content|U1> <maxlen> <maxwords> <maxtuple (0 = unrestricted)> [outfile] < words

## (1) L_2 (6 words), cap 10
./clos U1 10 100000 0 < L2.txt        -> CLOSED |L|=3306 mincfree=1 a          (s_U typing: closure contains the word "a")
./clos content 10 100000 0 < L2.txt   -> CLOSED |L|=6    mincfree=10 bbaabbaabb (L_2 itself is closed for content typing)
   (python reference closure.py gives the same two results)

## (2) L_3 (42 words), content typing, cap 22
./clos content 22 3000000 0 < L3.txt
round 1 d=1 recs=6378 merged-classes=309 |L|=42 mincfree=22
round 1 d=2 recs=147626 merged-classes=7852 |L|=1639 mincfree=22
round 2 d=1 recs=302951 merged-classes=356 |L|=6445587 mincfree=16 abaaabbbbbbaabbb
ABORT (size limit)                                            => a c-free word of length 16 < 22 = |W_3|
python3 build_cert.py     -> explicit certificate L_3 |- baab (2945 steps; pruned to 33 steps), intermediate c-free words:
   22,22,19,19,16,16,16,13,13,10 (baabbaabbb),10 (bbaabbaabb = W_2),10,7,7,4 (baab = W_1)
python3 verify_cert.py ...  -> see verify_log.txt (independent check; also direct checks inside L_4,...,L_7)

## (3) distinct-bracket variant V_3:  E_i -> b E E d | c E e, E_0 -> a   (42 words, alphabet {a,b,c,d,e}), content typing, cap 22
./clos content 22 1500000 7 V3bclos.txt < V3.txt      (tuple occurrences restricted: tuple length <= 7 or frame length <= 7)
round 1 d=2 ... |L|=76 mincfree=22
round 2 d=1 ... |L|=1416 mincfree=22
round 2 d=2 recs=4684517 merged-classes=52251 |L|=1737946 mincfree=19 aaaddbbaadbbbbaaddd
ABORT (size limit)
./cfree_search 22 12 < V3bclos.txt
new best 16 dbbaaadbbabaaddd / 13 adbabbabaaddd / 10 baaadbbadd / 7 dbbaaad / 4 adba
target baad reached: 1 ; target bbaadbaadd reached: 1 ; shortest c-free reached: 4 adba
   => W_1 = baad and W_2 = bbaadbaadd lie in the closure of V_3 (hash-based search; no explicit certificate extracted)

## failed / inconclusive runs
- unrestricted closure of L_3 and V_3 beyond round 2: memory/time blow-up (millions of words); not completed.
- a Python BFS over c-free words (cfree_bfs.py) was killed after 25 min without output; superseded by build_cert.py.

===== END FILE =====

===== BEGIN FILE fable_fanout2_open_problem_report.md bytes=27376 sha256=c0369cdc571944bfe702e52a3571939bc5981c332637bf8c49765ebc3e3ca223 =====
# `op:fanout-two` 独立研究報告（Fable, 2026-11-15）

**結論ラベル：`NEW THEOREM BUT OPEN`**
`op:fanout-two` 自体は解けていない。得られたのは (i) 倍化族に対する no-lift 定理の決定的な強化（機械検証済み証明書つき）、(ii) 薄い文法に対するアーベル型下界の一般的不可能性、(iii) 可換言語における単項希少型の多項式上界（新しい証明法）、(iv) 開問題の単一言明への還元、である。私の現時点の評価は「答えは NO（LG は fan-out 2 では境界でない）の方が見込みが高い」だが、これは**予想**であり証明ではない。

各主張の状態は次の記号で区別する：**[証明]** 本報告内に完全な証明がある／**[検証]** 明示的証明書を独立チェッカで検査済み／**[計算]** ハッシュベースの探索結果で証明書は未抽出／**[予想]**。

---

## 0. 読んだ資料と読んでいない資料

- GitHub を clone して読んだもの：`main.tex` の定義（`def:grammar-properties`, `def:tuple-substitutable`, `def:uniform-polydata`）、`lem:thickness-*`, `lem:distinguishing`, `prop:rare-type`, `prop:three-letter-family`, `thm:fanout-one-data`, `lem:power-transfer`, `thm:doubling-no-lift`, `op:fanout-two`；`HANDOFF_CURRENT.md`；U₂ ノートの定義と主張部分。
- **読んでいないもの**：`reviews/` の各ラウンド報告の本文（定理 L, P, S, L^⊗′ の証明、第九〜十一段の詳細）。したがって §5 の可換定理が既存の定理 L（ℓ=1）と結論の上で重なる可能性は排除していない。証明法は独立に構成した。
- 依頼書の問題設定に誤りは見つからなかった。一点だけ補足がある（§1）。

## 1. 開問題の単一言明への還元 [証明]

**命題 1.** \(f\ge2,\ r_{\max}\ge2\) を固定する。次は同値。
1. `op:fanout-two` の答えが YES。
2. 有限半束の擬多様体 \(\mathbf{SL}\) が fan-out \(f\)・rank \(r_{\max}\) で一様多項式特徴データ長を持たない。
3. ある有限アルファベット \(\Sigma\) とある半束型付け \(s:\Sigma^+\twoheadrightarrow\mathsf S\) について `def:uniform-polydata` の多項式が存在しない。

*証明.* \(\mathbf V\not\subseteq\mathbf{LG}\) なら \(U_1\in\mathbf V\)（`thm:lg-characterization`）で、擬多様体は有限直積・部分・商で閉じるから \(\mathbf{SL}=\langle U_1\rangle\subseteq\mathbf V\)。一様多項式性の失敗は \(\mathbf V\) について単調なので 2⇒1。逆に \(\mathbf{SL}\) 自身が \(\mathbf{LG}\) に含まれないので 1⇒2。2⇔3 は定義。∎

**補足 1′（上界側は内容型付けだけ見ればよい）.** 任意の半束型付け \(s\) は内容型付け \(c_\Sigma\) を経由するので \(\mathcal C^{\mathrm{mcf}}_{f,s}\subseteq\mathcal C^{\mathrm{mcf}}_{f,c_\Sigma}\)。さらに \(L\in\mathcal C^{\mathrm{mcf}}_{f,s}\) に対し \(\tau(G,s)\le\tau(G,c_\Sigma)\)：\(s\)-型付き非終端 \(B_{\mathbf t}\) の収率を含む内容型付き非終端 \(B_{\mathbf T}\) の類代表は、同じ分布を持ち \(s\)-型も \(\mathbf t\) だから \(\operatorname{Cl}_{L,s}(B_{\mathbf t})\) に入る。よって「全ての \(\Sigma\) で \(\tau(G,c_\Sigma)\) が多項式」が示されれば答えは NO。

つまり問題は U₁ の特定の3文字型付けではなく、**任意アルファベット上の内容型付け**の問題そのものである。下界側は大きなアルファベットを自由に使ってよく、上界側は内容型付けだけ処理すればよい。

## 2. 道具

以下 \(c(w)=\operatorname{alph}(w)\)、\(L\in\mathcal C^{\mathrm{mcf}}_{f,s}\)、\(f\ge2\)。

**補題 2.1（滑り補題／共役移送）[証明].** \(l,r\in\Sigma^*\)、\(x_1,y_2,z,z',m\in\Sigma^+\) が \(zm=mz'\)、\(s(x_1z)=s(x_1)\)、\(s(z'y_2)=s(y_2)\)、\(l\,x_1\,z\,m\,y_2\,r\in L\) を満たすなら
\[(x_1z,\;y_2)\ \equiv_{L,s}\ (x_1,\;z'y_2).\]
*証明.* 文脈 \(E=l\,\square_1\,m\,\square_2\,r\)（\(m\neq\varepsilon\)）は両方の組を同じ語 \(l x_1 z m y_2 r=l x_1 m z' y_2 r\) に埋めるので共通の受理文脈であり、成分型は仮定より等しい。∎

`lem:power-transfer` は \(z=z'=u^\delta\), \(m=u\) の特別な場合。内容型付けでは条件は \(c(z)\subseteq c(x_1)\cap c(y_2)\) だけになる。特に：

**系 2.2（単位の移送）.** 内容型付けで、\(L\) のある語が因子 \(x_1\cdot d\kappa\cdot d\cdot y_2\)（\(d\in\Sigma\), \(\kappa\in\Sigma^*\), \(c(d\kappa)\subseteq c(x_1)\cap c(y_2)\)）を持てば、全ての \(l,r\in\Sigma^*\), \(m'\in\Sigma^+\) で
\[l\,x_1\,d\kappa\;m'\;y_2\,r\in L\iff l\,x_1\;m'\;\kappa d\,y_2\,r\in L .\]
同じ文字 \(d\) の連続する二つの出現に挟まれた単位 \(d\kappa\) は、後方の \(y_2\) の出現の直前へ（\(\kappa d\) として）語長と Parikh ベクトルを保ったまま移動できる。長い語では文字が必ず再出現するので、この移動は**避けられない**。

**定義 2.3（導出閉包）.** \(K\subseteq\Sigma^*\) に対し \(\operatorname{Cl}(K)\) を、\(K\) を含み次の規則で閉じた最小集合とする：\(d\in\{1,2\}\)、\(\mathbf x,\mathbf y\in(\Sigma^+)^d\) が成分ごとに同じ内容を持ち、\(E_0,E_1\in\mathcal E_d\) について \(E_0[\mathbf x],E_0[\mathbf y],E_1[\mathbf x]\) が既に入っていれば \(E_1[\mathbf y]\) を入れる。

**補題 2.4（健全性）[証明].** 半束型付け \(s\) と \(f\ge2\) について、\(K\subseteq L\in\mathcal C^{\mathrm{mcf}}_{f,s}\) なら \(\operatorname{Cl}(K)\subseteq L\)。（\(L\in\mathcal C^{\mathrm{mcf}}_{f,c_\Sigma}\) なので各規則適用は定義そのもの。）

**補題 2.5（射による輸送）[証明].** \(\varphi:\Sigma^*\to\Sigma'^*\) を非消去射、\(P,Q\in\Sigma'^*\) とすると \(P\,\varphi(\operatorname{Cl}(K))\,Q\subseteq\operatorname{Cl}(P\varphi(K)Q)\)。
*証明.* 導出の長さの帰納法。\(c(\varphi(u))=\bigcup_{e\in c(u)}c(\varphi(e))\) は \(c(u)\) のみで決まるので、内容が等しい成分は像でも内容が等しい。成分と穴の間の部分は非消去性により非空のまま。文脈 \(E=(l,m,r)\) は \((P\varphi(l),\varphi(m),\varphi(r)Q)\) に移る。∎

内容型付けの本質的な点は、**任意の**非消去射で導出が輸送されることである（文字互いに素である必要はない）。

## 3. 定理 A：倍化族は fan-out 2 で完全に崩壊する

\(L_n,W_n\) は `prop:three-letter-family` のもの（\(W_1=\mathtt{baab}\), \(|W_n|=3\cdot2^n-2\)）。

**定理 A [証明＋検証].** \(\Sigma\supseteq\{a,b,c\}\)、\(s\) を \(\Sigma^+\) 上の任意の半束型付け（\(s_U\)、\(c_\Sigma\) を含む）、\(f\ge2\)、\(n\ge3\) とする。\(L_n\subseteq L\) なる全ての \(L\in\mathcal C^{\mathrm{mcf}}_{f,s}\) は \(W_1,W_2,\dots,W_n\) を全て含む。特に \(\mathtt{baab}\in L\) であり、\(W_n\) の型の最短語長は \(n\) によらず \(4\) 以下。
より一般に、非消去射 \(\psi\) について \(\psi(L_n)\subseteq L\) なら \(\psi(\mathtt{baab})\in L\)。

これは `thm:doubling-no-lift`（「同じ型・同じ Parikh の別の語がある」）を、半束型付けについて「定数長の語がある」まで強める。語を追加して族を修復する余地は一切ない。

*証明.*
(1) **証明書** [検証]：\(W_2=\mathtt{bbaabbaabb}\in\operatorname{Cl}(L_3)\) かつ \(\mathtt{baab}\in\operatorname{Cl}(L_3)\)。添付 `cert_L3_to_baab_pruned.json` は定義 2.3 の規則 33 回（\(d=1\) が 9 回、\(d=2\) が 24 回）の明示的列で、`verify_cert.py` が各ステップの前提（成分・中間部の非空性、内容の一致、\(E_0[\mathbf x],E_0[\mathbf y],E_1[\mathbf x]\) の所属）を独立に検査する。
(2) \(k\ge0\)、\(\varphi_k:a\mapsto W_k,\ b\mapsto b,\ c\mapsto c\) とすると \(\varphi_k(L_3)\subseteq L^{(k+3)}\)（\(E_{k+3}\) の収率集合）。\(k+3\le n\) なら \(E_{k+3}\) は \(L_n\) の中で文脈 \((P_k,Q_k)\)（例えば \(P_k=b^{\,n-k-3}\)）を持ち、\(P_k\varphi_k(L_3)Q_k\subseteq L_n\subseteq L\)。補題 2.5, 2.4 より \(P_kW_{k+2}Q_k,\ P_kW_{k+1}Q_k\in L\)。
(3) \(W_{k+3},W_{k+2},W_{k+1}\) は内容 \(\{a,b\}\) が等しく文脈 \((P_k,Q_k)\) を共有するので互いに \(\equiv_L\)（分布が一致）。
(4) \(W_n\in L\)。\(j\ge3\) で \(W_j\in L\) なら、\(k=j-3\) の同値 \(W_j\equiv W_{j-1}\) を文脈 \((\varepsilon,\varepsilon)\) に適用して \(W_{j-1}\in L\)。\(W_3\in L\) からは \(k=0\) の \(W_3\equiv W_1\) で \(W_1\in L\)。射版は \(\psi\circ\varphi_k\) で同じ。∎

**崩壊の機構.** 核は系 2.2 の「文字の飛び越し」である。探索で最初に見つかった例では、\(L_3\) の二つの語 \(b\,W_2\,[c\,W_1\,c]\,b\) と \(b\,W_2\,[b\,W_1\,c\,a\,c\,b]\,b\) から、\(b\) が \(c\) を右へ、\(c\) が \(\mathtt{bbaab}\) を左へ飛び越して、**同じ枠** \(b\,W_2\,c\,\square\,c\,bb\) に長さの違う \(c\) なし語 \(\mathtt{baa}\) と \(\mathtt{bbaaba}\) が入る。添付の証明書が実際に使うのは同種の二つの枠で、枠 \((\mathtt{bbcacbaabbc},\mathtt{acbb})\) に \(\mathtt{bbbaa}\) と \(\mathtt{ba}\) が、枠 \((\mathtt{bcbaabcb},\mathtt{cbacbb})\) に \(\mathtt{baabba}\) と \(\mathtt{baa}\) が入る。これと \(b\) の冪移送 \((b,bb)\equiv(bb,b)\) を合わせて \(W_3\) が \((a,2b)\) ずつ縮む（22→19→16→13→10→7→4）。省略記号 \(c\) が可動なので「省略の深さ」を位置で符号化できない、というのが本質である。

**検証の範囲.** `verify_log.txt`：\(L_3\) 上の証明書（刈込み 33 手・完全版 2945 手）に加え、輸送補題に頼らず \(L_4\)（\(k=1\) および \(k=0\) で枠 \((b,W_3b)\)）、\(L_5\)（\(k=2\)、および \(k=0\) で枠 \((bc,\,c^5ac^4b)\)）、\(L_6\)（\(k=1\)）、\(L_7\)（\(k=4\)）の中で同じ 33 手を直接検査し全て通過。所属判定は \(L_n\) の再帰的認識器による（列挙やハッシュに依存しない）。

**命題 A′（括弧を別文字にした変種）[計算].** \(E_i\to b\,E_{i-1}E_{i-1}\,d\mid c\,E_{i-1}\,e\)、\(E_0\to a\)（5文字、内容型付け）の族 \(V_n\) についても、\(\operatorname{Cl}(V_3)\) は \(W_1'=\mathtt{baad}\) と \(W_2'=\mathtt{bbaadbaadd}\) を含む（長さ 22 → 19 → 16 → 13 → 10 → 7 → 4）。これが正しければ定理 A の証明 (2)–(4) がそのまま通り \(V_n\) も定数長に崩壊する。ただしこれは 64 bit ハッシュを用いた打切り閉包＋最良優先探索の結果で、**明示的証明書は抽出していない**。

**観察 [計算].** \(s_U\) 型付けでは \(L_2\) の（長さ 10 打切り）閉包が既に語 \(\mathtt a\) を含む。内容型付けでは \(L_2\) は閉じており、崩壊は \(n=3\) から始まる。

## 4. 定理 B：薄い文法はアーベル不変量を隠せない

**定理 B [証明].** \(G\) を reduced good MCFG（fan-out 任意、rank \(\le r\)）、\(\theta=\bar\theta_G\)、\(g:\Sigma^*\to\mathsf A\) をアーベル群へのモノイド射、\(\mathsf H\le\mathsf A\)、\(\gamma\in\mathsf A\) とする。長さ \(\le(r+2)\theta\) の全ての \(w\in L(G)\) が \(g(w)\in\gamma+\mathsf H\) を満たせば \(L(G)\subseteq g^{-1}(\gamma+\mathsf H)\)。

*証明.* 各非終端 \(A\) に `lem:thickness-equivalence`(ii),(iv) の短い収率 \(\mathbf u_A\)（\(\|\mathbf u_A\|_1\le\theta\)）と文脈 \(E_A\)（固定部 \(\le\theta\)）を取り、\(c_A:=\sum_i g(u_{A,i})\) とおく。主張：全ての \(\mathbf u\in L_A\) で \(\sum_ig(u_i)\equiv c_A\pmod{\mathsf H}\)。導出の高さの帰納法：\(\mathbf u=\rho(\mathbf u^1,\dots,\mathbf u^q)\) なら非削除性と可換性から \(g(\mathbf u)=g(\text{$\rho$ の終端})+\sum_jg(\mathbf u^j)\equiv g(\rho(\mathbf u_{B_1},\dots,\mathbf u_{B_q}))\)。語 \(E_A[\rho(\mathbf u_{B_1},\dots)]\) と \(E_A[\mathbf u_A]\) は共に \(L(G)\) に属し長さ \(\le(q+2)\theta\) なので仮定より \(g\) 値が同じ剰余類にあり、\(g(\rho(\mathbf u_{B_j}))\equiv c_A\)。\(A=S\) では \(c_S=g(u_S)\in\gamma+\mathsf H\)。∎

**帰結.**
- `lem:distinguishing` を \(L'=L\cap g^{-1}(\gamma+\mathsf H)\)（`prop:abelian-coset-filter` の型の部分標的）に適用しても、区別語の長さは高々 \((r_{\max}+2)\bar\theta_G\)。**アーベル剰余類フィルタによる部分標的では超多項式下界は出ない。**
- 例：\(\{w:|w|_a\equiv|w|_c \pmod{2^n}\}\) は全ての型付けで組代入可能だが、多項式サイズ・多項式厚さの reduced good 提示を持たない（持てば上の議論で \(|w|_a=|w|_c\) が \(\mathbb Z\) 上で成立してしまう）。指数的な法や重みを持つ計数は厚さに必ず現れる。

## 5. 単項型の構造と定理 C

以下 \(a\in\Sigma\)、\(s\) は半束型付け、\(a^N\in L\) で \(N=\min\{i\ge1:a^i\in L\}\)。

**補題 5.1 [証明]（非可換・一般の \(L\in\mathcal C^{\mathrm{mcf}}_{2,s}\) で成立）.**
- **(R) 連の再配分.** \(p\,a^i\,q\,a^j\,r\in L\)、\(q\in\Sigma^+\)、\(i,j,i',j'\ge1\)、\(i'+j'=i+j\le N-1\) なら \(p\,a^{i'}q\,a^{j'}r\in L\)。（\(a^N=a^i\cdot a\cdot a^j\cdot a^{N-1-i-j}\) が共通文脈。）
- **(U) 一意性.** \(P a^iQ,\ Pa^{i'}Q\in L\)、\(1\le i<i'\le N\) は起こらない。（起これば \(a^i\equiv a^{i'}\) で \(a^{N-i'+i}\in L\)、最小性に反する。）
- **(E) 交換.** \(V,V'\notin a^*\) が \(aVa^{e},\,aV'a^{e'}\in L\)（\(1\le e,e'\le N-2\)）を満たし \(c(V)\cup\{a\}=c(V')\cup\{a\}\) なら、\(i'-i=e'-e\) なる適当な \(i,i'\ge1\) について \(a^iVa\equiv a^{i'}V'a\)。

(R),(U) から、\(a\) の総数が \(N\) 未満の語では「\(a\) の個数は、\(a\) の連を1文字に潰した骨格の関数」である。すなわち単項希少語 \(a^N\) があると、\(L\) の他の語は**骨格 → 欠損 \(\delta=N-|w|_a\)** という関数のグラフになり、(E) により欠損は同じ内容類の部品の入替えについて加法的に振る舞う。

**定理 C（可換言語では単項型は希少になれない）[証明；独立監査は未実施].** \(\Sigma=\{a\}\sqcup\Delta\)、\(D=|\Delta|\ge1\)。\(L\) を可換（所属が Parikh ベクトルのみで決まる）とし、ある半束型付け \(s\) と \(f\ge1\) で \(L\in\mathcal C^{\mathrm{mcf}}_{f,s}\)、\(G\) を \(L\cap\Sigma^+\) の reduced good 提示（fan-out 任意、rank \(\le r\)、\(v=|V|\)、\(\theta=\bar\theta_G\)）とする。\(a^N\in L\) で \(N\) が最小なら
\[N\ \le\ \max\bigl\{(D+1)BK_0+1,\ \ 2^{D+1}\,v\,(r+1)K_0\bigr\},\quad B=D!\,\theta^{D},\ \rho=2DB,\ K_0=2(r+1)\theta\,\bigl(4(r+1)\rho\bigr)^{D2^{D}} .\]
特に \(N=O_{D,r}\bigl(v\,\theta^{\,1+D+D^22^D}\bigr)\)：固定アルファベットでは多項式。

*証明.* \(P\subseteq\mathbb N\times\mathbb N^\Delta\) を \(L\) の Parikh 像とし、点を \((e,V)\) と書く。
**(0) 木.** \(a^N\) の \(G\) における導出木を節点数最小に取る。同じ非終端の二節点は収率の総長 \(k\) が等しく（違えば短い \(a\) 冪が出る）、入れ子にならない（節点数最小性）。よって深さ \(\le v\)。短い収率 \(\mathbf u_A\) の Parikh を \((\alpha_A,V_A)\) とする。\(k_A>\theta\) の節点を「大」と呼ぶと \(V_A\neq0\)（さもなくば \(a^{N-k_A+\alpha_A}\in L\) が最小性に反する）。欠損 \(\delta_A:=k_A-\alpha_A\in[k_A-\theta,k_A]\)、類 \(T_A:=\operatorname{supp}V_A\)。\(k_A=N\) の節点は根からの単項鎖をなす。
**(1) 実現集合.** \(\mathcal V:=\{V\ne0:\exists e\in[1,N-1],(e,V)\in P\}\)。(U) より \(e\) は一意で \(\delta(V):=N-e\) が定まる。\(k<N\) の大節点を省略すれば \(V_A\in\mathcal V\), \(\delta(V_A)=\delta_A\)。
**(2) 交換.** \(V,V'\in\mathcal V\)、\(\operatorname{supp}V=\operatorname{supp}V'\)、\((e,Q+V)\in P\)、\(e\ge1\)、\(e':=e+\delta(V)-\delta(V')\ge1\) なら \((e',Q+V')\in P\)。（\(i=1+\max(0,\delta(V')-\delta(V))\), \(i'=1+\max(0,\delta(V)-\delta(V'))\) とし、Parikh \((i,V)\) と \((i',V')\) の語は内容が等しく文脈 \((N-\delta(V)-i,0)\) を共有するので同値。\(e\ge i\) は \(e'\ge1\) と同値。）
**(3) 分岐類での完全加法性.** 類 \(T\) が**分岐的**とは、互いに素な大節点 \(B,C\)（\(k<N\)）で \(T_B=T_C=T\)、\(N-\delta_B-\delta_C\ge1\) なるものがあること。このとき、類 \(T\) の大非終端 \(J_1,\dots,J_t\)（各 \(\delta_{J}\le(N-1)/2\)）と \(\sum m_j\delta_{J_j}\le N-1\) なる多重集合 \(m\ne0\) について \(\sum m_jV_{J_j}\in\mathcal V\) で欠損は \(\sum m_j\delta_{J_j}\)。
　\(|m|=2\)：種 \(V_B+V_C\)（欠損 \(\delta_B+\delta_C\)）で \(\delta_B\le\delta_C\) としてよく、(2) で \(V_C\to V_J\)、次に \(V_B\to V_{J'}\) と入れ替える（途中の \(a\) 個数は \(N-\delta_B-\delta_J\ge1\)、\(N-\delta_J-\delta_{J'}\ge1\)）。\(|m|\to|m|+1\)：\(M=\sum m_jV_{J_j}\)（台 \(T\)）、\(m_J\ge1\) とし、\(V_J+V_{J'}\) に (2) を \(V=V_J\), \(V'=M\), \(Q=V_{J'}\) で適用する。
**(4) 分岐類には疎な鎖がない.** 分岐類 \(T\)（\(t=|T|\)）の大非終端 \(J_0,\dots,J_t\) で \(\delta_{J_{i+1}}>\rho\,\delta_{J_i}\)、\(\delta_{J_t}\le N_1:=(N-1)/((D+1)B)\) なるものは存在しない。
　実際 \(t+1\) 個のベクトル \(V_{J_i}\in[0,\theta]^T\) には Cramer の公式から \(|\lambda_i|\le t!\theta^t\le B\) の非自明な整数関係 \(\sum\lambda_iV_{J_i}=0\) があり、\(V_{J_i}\ge0\), \(\neq0\) なので両符号が現れる。\(m^\pm=\lambda^\pm\) は (3) の条件を満たし同じベクトルを実現するから、(U) より \(\sum\lambda_i\delta_{J_i}=0\)。しかし最大の添字 \(i^*\) で \(|\lambda_{i^*}|\delta_{J_{i^*}}\ge\delta_{J_{i^*}}>2Bt\,\delta_{J_{i^*-1}}\ge2\bigl|\sum_{i<i^*}\lambda_i\delta_{J_i}\bigr|\)。矛盾。
　したがって分岐類の欠損のうち \(N_1\) 以下のものは高々 \(D\) 個の区間 \([x,\rho x]\) で覆われる（貪欲法）。全分岐類で区間は \(M_b<D2^D\) 個。
**(5) 非分岐類は高々二本の根道に載る.** 類 \(T\) に互いに素な対がなければ全節点が比較可能で一本の根道上。互いに素な対 \(B,C\) が全て「悪い」（\(k_B+k_C=N\)）なら、\(B\) の下の類 \(T\) 節点は互いに比較可能（互いに素な \(X,Y\subseteq B\) は \(N-\delta_X-\delta_Y\ge k_C\ge1\) で良い対になる）、\(C\) の下も同様、その他は \(B\) か \(C\) と比較可能。\(U\) を、非分岐類の節点が載る根道と \(k=N\) の鎖の和集合とすると \(U\) は上方閉で \(|U|\le2^{D+1}v\)。
**(6) 窓の議論.** \(X\notin U\) を大節点とする。その子孫の大節点は全て分岐類。最重の子を辿る列 \(k_0=k_X\ge k_1\ge\cdots\) は \(k_i>(r+1)\theta\) の間 \(k_{i+1}\ge(k_i-\theta)/r\ge k_i/(r+1)\) を満たす。よって \(\sigma:=2(r+1)\) として、\(y\in[\sigma\theta,k_X]\) なる各窓 \([y/\sigma,y]\) は分岐類の大節点の欠損を含む。\(y_j:=\sigma\theta(2\sigma\rho)^j\)（\(j=0,\dots,M_b\)）の窓は、一つの区間 \([x,\rho x]\) が二つと交わることがないほど離れている。したがって \(\min(k_X,N_1)<K_0=\sigma\theta(2\sigma\rho)^{M_b}\)（\(M_b\le D2^D\)）。
**(7) 集計.** \(N_1<K_0\) なら \(N<(D+1)BK_0+1\)。\(N_1\ge K_0\) なら \(U\) の外の大節点は全て \(k<K_0\) で、\(U\) の各節点は終端 \(\le\theta\) 個と高々 \(r\) 個の子を持つから \(N\le|U|(r+1)K_0\)。∎

**注意.** (a) 証明は \(d=1\) の代入可能性しか使っていない。可換言語では fan-out に関係なく単項型が希少になれない、という主張である。(b) 対照的に非可換・fan-out 1 では `thm:fanout-one-data` の指数的下界がある。fan-out 2 が何を変えるかは次節。(c) `prop:rare-type` 経由の下界のうち「可換言語の単項型」を使うものはこれで閉じられるが、**開問題そのものには届かない**。

## 6. 非可換の場合：見取り図・予想・障壁

**直観.** fan-out 1 の下界は「非可換な剛構造（木）」が希少型の語を長く保つことで成立する。fan-out 2 の代入可能性は系 2.2 により全ての長い語を「単位の移送」で攪拌し、言語を局所データ＋計数データで決まるものへ近づける（先行ラウンドの Euler 付け替えと同じ現象を別方向から見ている）。一方、計数データで決まる部分では定理 B, C の論法（薄さ ⟹ 短い整数関係 ⟹ 疎な重み列が存在しない）が多項式上界を与える。移送に免疫を持つのは文字の順序が剛な有界言語型（例：\(\{a^nb^n\}\) は内容型付けでは 2 次元代入可能）だが、そこではブロック数が固定で次元が有界である。

**予想 U [予想].** 半束型付け \(s\)、\(f\ge2\)、\(L\in\mathcal C^{\mathrm{mcf}}_{f,s}\)、reduced good 提示 \(G\) について、\(L\) の最短の \(a\) 冪の長さは \(\|G\|,\bar\theta_G\) の多項式（次数は \(|\Sigma|\) に依存）で抑えられる。

**証明計画と欠けている部分.** 補題 5.1 は非可換でそのまま成立する。定理 C の (3)–(7) を非可換で再現するには、(U) を適用するために**骨格が語として一致する二語**が必要で、ここが唯一の本質的な穴である：
1. 系 2.2 から「交叉」が出る：部品 \(\alpha d\beta\) と \(\alpha'd\beta'\) が、後方に \(\alpha'd\beta'\) の複製を持つ適当な語の中に現れれば、\(\alpha d\beta'\) と \(\alpha'd\beta\) を部品とする語も \(L\) に入り \(a\) の個数は変わらない [証明：系 2.2 の直接の適用]。
2. 交叉は部品の bigram 多重集合（\(a\) との境界 bigram を含む）を保つ。**未証明**：同じ bigram 多重集合を持つ二つの部品多重集合が、常に宿主条件（系 2.2 の因子 \(x_1d\kappa dy_2\) の存在）を満たしたまま交叉と部品の並べ替えで結べること。これは有向多重グラフの Euler 分解の連結性＋「宿主可能性」で、先行ラウンドが HC と呼んだ困難と同種と思われる。部品の複製を自由に増やせる（補題 5.1(E) と定理 C(3) の論法）ので宿主の用意は U₂ より容易だと期待するが、確認していない。
3. これが通れば欠損は bigram 計数ベクトル（次元 \(\le(D+1)^2\)）の加法的関数になり、定理 C の (4)–(7) が次元だけ替えて通る。
4. fan-out 2 の非終端では部品が2成分になり、交換に \(d=2\) の同値が必要。帳簿は増えるが新しい困難は見えていない（未確認）。

**一般の希少型（2文字以上）について.** \(c\) なしの語が \(\{a,b\}\) 上にある場合、(U) の類似は「骨格ごとに \((|w|_a,|w|_b)\) の可能な値が格子の剰余類に入る」になるはずで、可換版ですら未着手である。定理 A の崩壊はこの場合の最初の実例にあたる。

**下界側の候補が残る場所.** 私が排除できていないのは次だけである：(i) 希少型を使わず、非アーベルかつ組代入可能な部分標的 \(L'\subsetneq L\) で区別する経路（定理 B はアーベルな \(L'\) しか殺さない）；(ii) 移送に免疫のある剛構造を、固定アルファベットのまま非有界な深さで実現する未知の符号化。(ii) について、単一ブロックに非線形な重み \(\sigma(j)\) を持たせる有界形 \(\{a^ic^jb^k:i+k=\sigma(j)\}\) を調べたが、\(a^uc^{j_1}\) と \(a^{u'}c^{j_1'}\) の比較から \(\sigma\) は \(j\ge1\) でアフィンに強制され、非線形性は \(j=0\)（別の型）にしか置けず、その場合は薄い提示が作れなかった（議論は概略のみで、定理としては主張しない）。

## 7. 計算の記録

詳細は `experiments_log.txt`。全て決定的で乱数は不使用。閉包は全て長さ打切りなので真の閉包の下からの近似であり、報告した語が閉包に属することだけを主張する。

| 対象 | 型付け | 打切り | 結果 | 状態 |
|---|---|---|---|---|
| \(L_2\)（6語） | \(s_U\) | 10 | 3306語で閉、\(\mathtt a\) を含む | [計算] |
| \(L_2\) | 内容 | 10 | 既に閉（6語） | [計算] |
| \(L_3\)（42語） | 内容 | 22 | 第2巡 \(d=1\) で 644 万語、\(c\) なし長さ16 | [計算] |
| \(L_3\vdash W_2,\ \mathtt{baab}\) | 内容 | — | 33 手の証明書、\(L_4\)–\(L_7\) 内でも直接検査 | [検証] |
| \(V_3\)（42語、5文字） | 内容 | 22、組長/枠長 \(\le7\) | 174 万語、その後 \(\mathtt{baad}\), \(W_2'\) に到達 | [計算] |

失敗・未完：\(L_3,V_3\) の無制限閉包は第2巡以降メモリと時間で完走せず。Python の \(c\) なし語 BFS は 25 分で出力なしのため打ち切り、証明書構成に置き換えた。

## 8. 最も有望な次の一手

1. **予想 U の穴（§6 の 2.）を埋める**か、反例を作る。部品複製が自由な設定での Euler 連結性は、U₂ の宿主問題より扱いやすい特殊化であり、通れば「単項型による下界は fan-out 2 で不可能」という型付け・言語クラスによらない最初の一般上界になる。
2. 定理 C を 2 文字の希少型へ拡張する（可換の場合）。(U) を格子版に置き換える。
3. 定理 A′ の証明書抽出（`build_cert.py` を \(V_3\) 用に書き換えるだけだが計算量が大きい）。
4. 下界を狙うなら §6 の (i) のみが未踏。ただし非アーベルで組代入可能な部分標的の例を私は一つも構成できていない。

## 9. 結論

**`NEW THEOREM BUT OPEN`.**

- **解決したこと（量化込み）.**
  - 全ての \(f\ge2\)、\(n\ge3\)、\(\Sigma\supseteq\{a,b,c\}\)、全ての半束型付け \(s\)、\(L_n\) を含む全ての \(L\in\mathcal C^{\mathrm{mcf}}_{f,s}\) について \(\mathtt{baab}\in L\)（定理 A、証明書は機械検査済み）。任意の非消去射像でも同様。
  - 全ての reduced good MCFG \(G\)（rank \(\le r\)）と全てのアーベル剰余類条件について、長さ \((r+2)\bar\theta_G\) 以下の語で成り立てば \(L(G)\) 全体で成り立つ（定理 B）。
  - 全ての可換な \(L\in\mathcal C^{\mathrm{mcf}}_{f,s}\)（\(s\) 半束、\(f\ge1\)）と全ての reduced good 提示について、最短の \(a\) 冪は \(O_{|\Sigma|,r}(|V|\,\bar\theta_G^{\,1+D+D^22^D})\)（定理 C、手証明・未監査）。
  - `op:fanout-two` は「\(\mathbf{SL}\) が fan-out \(f\) で一様多項式データ長を持たないか」と同値（命題 1）。
- **未解決のまま.** ある \(\Sigma\) とある半束型付けについて超多項式族が存在するか（YES）、全ての \(\Sigma\) で \(\tau(G,c_\Sigma)\) が多項式か（NO）。非可換言語では単項希少型すら未決（予想 U）。\(f\ge3\) への移行も未検討。

===== END FILE =====

===== BEGIN FILE independent_cert_audit.py bytes=2778 sha256=bd575fec785315e048d549e5ff380f913a28f6c74689e43275838a52808ea125 =====
#!/usr/bin/env python3
"""Independent, hash-free checker of Fable's 33-step L3 => baab proof.
Does NOT import Fable's verify_cert.py or closure.py.
"""
import sys, json, collections, functools, hashlib, os
BASE=os.path.dirname(os.path.abspath(__file__))
@functools.lru_cache(None)
def words(n):
    if n==0:return frozenset({'a'})
    S=words(n-1)
    return frozenset({'b'+p+q+'b' for p in S for q in S} | {'c'+p+'c' for p in S})

def plug(v,parts):
    assert len(parts)==len(v)-1
    return ''.join(v[i]+parts[i] for i in range(len(parts)))+v[-1]

def admissible(t): return len(t) in (2,3) and all(bool(x) for x in t[1:-1])

@functools.lru_cache(None)
def accepts(n,w):
    if n==0:return w=='a'
    if len(w)<3:return False
    if w[0]=='c' and w[-1]=='c' and accepts(n-1,w[1:-1]):return True
    if w[0]=='b' and w[-1]=='b':
       core=w[1:-1]
       for m in range(1,len(core)):
           if accepts(n-1,core[:m]) and accepts(n-1,core[m:]): return True
    return False

c=json.load(open(os.path.join(BASE,'cert_L3_to_baab_pruned.json')))
assert c['typing']=='content' and c['start']=='L_3' and c['goal']=='baab'
S=set(words(3));assert len(S)==42
initial=set(S)
trace=[]
for idx,z in enumerate(c['steps'],1):
    d=z['d'];x=z['x'];y=z['y'];E0=z['E0'];E1=z['E1']
    assert d in (1,2) and len(x)==d==len(y),(idx,'arity')
    assert admissible(E0) and admissible(E1) and len(E0)==d+1==len(E1),(idx,'admissibility')
    assert all(len(w)>0 for w in x+y),(idx,'empty tuple')
    assert all(set(u)==set(v) for u,v in zip(x,y)),(idx,'types')
    targets=[plug(E0,x),plug(E0,y),plug(E1,x)]
    assert all(t in S for t in targets),(idx,'missing premise', [t for t in targets if t not in S])
    u=plug(E1,y)
    assert u==z['new'],(idx,'target word')
    S.add(u)
    trace.append((idx,d,len(u),u,targets))
assert 'baab' in S and 'baab' not in initial
assert 'bbaabbaabb' in S and 'bbaabbaabb' not in initial
print('INDEPENDENT_CERTIFICATE: PASS')
print('base words:',len(initial),'proof steps:',len(trace),'arity counts:',dict(collections.Counter(r[1] for r in trace)))
print('final:',trace[-1][3], 'intermediate W2:',trace[28][3])
print('unique derived:',len(S-initial))
print('min c-free:',min(((len(w),w) for w in S if 'c' not in w)))
@functools.lru_cache(None)
def W(k):return 'a' if k==0 else 'b'+W(k-1)+W(k-1)+'b'
for k in (0,1,2):
    atom=W(k)
    def phi(w):return ''.join(atom if a=='a' else a for a in w)
    allmembers=all(accepts(k+3,phi(w)) for w in initial)
    assert allmembers
    print('EMBEDDED_L3: PASS',f'k={k}', f'level={k+3}',f'words={len(initial)}',f'|W(k+3)|={len(W(k+3))}')
for k in range(0,8):
    assert W(k) == 'a' if k==0 else W(k)=='b'+W(k-1)*2+'b'
print('THEOREM_A_TRANSPORT_HYPOTHESES: PASS (finite bases + universal homomorphism reasoning)')

===== END FILE =====

===== BEGIN FILE independent_cert_log.txt bytes=412 sha256=58398972f9419afdf5f2ef9a3c11a29131f097df3068ede6837886125070a4cf =====
INDEPENDENT_CERTIFICATE: PASS
base words: 42 proof steps: 33 arity counts: {2: 24, 1: 9}
final: baab intermediate W2: bbaabbaabb
unique derived: 22
min c-free: (4, 'baab')
EMBEDDED_L3: PASS k=0 level=3 words=42 |W(k+3)|=22
EMBEDDED_L3: PASS k=1 level=4 words=42 |W(k+3)|=46
EMBEDDED_L3: PASS k=2 level=5 words=42 |W(k+3)|=94
THEOREM_A_TRANSPORT_HYPOTHESES: PASS (finite bases + universal homomorphism reasoning)

===== END FILE =====

===== BEGIN FILE independent_check_log.txt bytes=241 sha256=540bd1e59acb4e30457c04b78b4b7cc2fed9b0f108d5ba22a5a75ce8269f4fe2 =====
EXCHANGE_CONTEXT_CERTIFICATES 36820
BRANCH_INDUCTION_NUMERIC_CASES 550
NONBRANCH_TWO_PATH_RANDOM_TREES 3500
HEAVY_PATH_WINDOW_INSTANCES 153625
ALL INDEPENDENT LOCAL CHECKS PASSED
INTEGER_DEPENDENCE_MINOR_CASES 24446
ALL CRAMER BOUNDS PASSED

===== END FILE =====

===== BEGIN FILE verify_cert.py bytes=2748 sha256=03f04263b5dbd0e96664f8ad606ee3e868f7f035068452de899fcbb6fc29db9e =====
#!/usr/bin/env python3
"""Independent checker for the substitution certificate  L_3 |- baab  and its transports.
A step (d,E0,x,y,E1) is valid w.r.t. a set S of words known to lie in every (2,content)-substitutable
language containing the base language if
  * x,y are d-tuples (d in {1,2}) of NONEMPTY words with equal componentwise content,
  * E0,E1 are admissible contexts (for d=2 the middle part is NONEMPTY),
  * E0[x], E0[y], E1[x] are in S.
Then E1[y] must be in every such language, and is added to S.
Usage: verify_cert.py cert.json            (base L_3, identity transport)
       verify_cert.py cert.json n k P Q    (base L_n, morphism a->W_k, frame (P,Q))
"""
import json, sys
from functools import lru_cache
sys.setrecursionlimit(10000)
@lru_cache(maxsize=None)
def inL(i,w):
    if i==0: return w=='a'
    if len(w)<3: return False
    if w[0]=='c' and w[-1]=='c' and inL(i-1,w[1:-1]): return True
    if w[0]=='b' and w[-1]=='b':
        u=w[1:-1]
        return any(inL(i-1,u[:j]) and inL(i-1,u[j:]) for j in range(1,len(u)))
    return False
def W(k): return 'a' if k==0 else 'b'+W(k-1)*2+'b'
def main():
    cert=json.load(open(sys.argv[1]))
    if len(sys.argv)>2:
        n,k=int(sys.argv[2]),int(sys.argv[3]); P=sys.argv[4].replace('_',''); Q=sys.argv[5].replace('_','')
    else: n,k,P,Q=3,0,'',''
    atom=W(k)
    phi=lambda u: u.replace('a',atom)
    # sanity: (P,Q) is a context of the level-(k+3) nonterminal inside L_n: check on the two extreme yields
    assert inL(n,P+W(k+3)+Q) and inL(n,P+'c'*(k+3)+'a'+'c'*(k+3)+Q)
    derived=set()
    member=lambda w: w in derived or inL(n,w)
    def fill(E,x):
        return E[0]+x[0]+E[1] if len(x)==1 else E[0]+x[0]+E[1]+x[1]+E[2]
    nsteps=0
    for st in cert["steps"]:
        d=st["d"]; x=[phi(u) for u in st["x"]]; y=[phi(u) for u in st["y"]]
        E0=[phi(u) for u in st["E0"]]; E1=[phi(u) for u in st["E1"]]
        E0=[P+E0[0]]+E0[1:-1]+[E0[-1]+Q]; E1=[P+E1[0]]+E1[1:-1]+[E1[-1]+Q]
        assert d in (1,2) and len(x)==d==len(y) and len(E0)==d+1==len(E1)
        assert all(len(u)>0 for u in x+y)
        if d==2: assert len(E0[1])>0 and len(E1[1])>0
        assert [frozenset(u) for u in x]==[frozenset(u) for u in y], "content types differ"
        assert member(fill(E0,x)) and member(fill(E0,y)), "no shared context"
        assert member(fill(E1,x)), "E1[x] not known"
        new=fill(E1,y); assert new==P+phi(st["new"])+Q
        derived.add(new); nsteps+=1
    goal=P+phi(cert["goal"])+Q
    assert goal in derived
    cf=[w for w in derived if 'c' not in w]
    print(f"OK: base L_{n}, atom W_{k} (|atom|={len(atom)}), frame P={P!r} Q={Q!r}: {nsteps} steps verified; "
          f"derived {goal!r} (length {len(goal)}); |W_{k+3}|={len(W(k+3))}")
main()

===== END FILE =====

===== BEGIN FILE verify_log.txt bytes=1170 sha256=64b957d464aefa1c62b89ec98c6dd60126cb1929e95bd9c8db27fccc6ea60c13 =====
# verification log (verify_cert.py), 2026-11-15
OK: base L_3, atom W_0 (|atom|=1), frame P='' Q='': 33 steps verified; derived 'baab' (length 4); |W_3|=22
OK: base L_4, atom W_1 (|atom|=4), frame P='' Q='': 33 steps verified; derived 'bbaabbaabb' (length 10); |W_4|=46
OK: base L_4, atom W_0 (|atom|=1), frame P='b' Q='bbbaabbaabbbbaabbaabbbb': 33 steps verified; derived 'bbaabbbbaabbaabbbbaabbaabbbb' (length 28); |W_3|=22
OK: base L_5, atom W_2 (|atom|=10), frame P='' Q='': 33 steps verified; derived 'bbbaabbaabbbbaabbaabbb' (length 22); |W_5|=94
OK: base L_5, atom W_0 (|atom|=1), frame P='bc' Q='cccccaccccb': 33 steps verified; derived 'bcbaabcccccaccccb' (length 17); |W_3|=22
OK: base L_6, atom W_1 (|atom|=4), frame P='bc' Q='ccccccacccccb': 33 steps verified; derived 'bcbbaabbaabbccccccacccccb' (length 25); |W_4|=46
OK: base L_7, atom W_4 (|atom|=46), frame P='' Q='': 33 steps verified; derived 'bbbbbaabbaabbbbaabbaabbbbbbaabbaabbbbaabbaabbbbbbbbaabbaabbbbaabbaabbbbbbaabbaabbbbaabbaabbbbb' (length 94); |W_7|=382
# full (unpruned) certificate:
OK: base L_3, atom W_0 (|atom|=1), frame P='' Q='': 2945 steps verified; derived 'baab' (length 4); |W_3|=22

===== END FILE =====
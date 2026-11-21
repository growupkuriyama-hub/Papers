# Round Eleven U₂ — Complete Source, Checker, and Independent Audit Bundle

**Research-only archival.** Each source below is reproduced byte-for-byte as UTF-8 in a delimited raw section. Extract with the lines strictly between `BEGIN SOURCE <filename>` and `END SOURCE <filename>`; restore a trailing newline if the original indicates it. Compare SHA256 hashes below. The large code and logs are not mathematical proofs. The center open problem `op:fanout-two` remains OPEN.

## Manifest

| File | UTF-8 bytes | SHA256 |
|---|---:|---|
| `claude_fanout2_round11_residual_report_2026-11-15.md` | 31115 | `0fc54cd73e7d7388ecf537d5ef486b835f7f566575afd645d9fabdebe1141b2c` |
| `claude_fanout2_round11_checkpoint1_2026-11-15.md` | 14190 | `48f54e96aa61308c4ef6babd4edcf4dbd21c070d95795a1c0515bbb5191c626b` |
| `claude_fanout2_round11_next_obligations_2026-11-15.md` | 3563 | `e15b1ccd2b37d808563f5761eb78cdd9d121c522187808fd111ac988132d2f34` |
| `check_round11_residual_2026-11-15.py` | 56462 | `dfbae608d273bb31e901c198b9ac17ba06d811f572a991a37f1afe1d165518aa` |
| `out_check_round11_residual_2026-11-15.txt` | 14310 | `78a6bd8392151c485cafc5ae8cdede2abba06fd41a01162e3e3b9ca707d9f07d` |
| `README_RUN.txt` | 758 | `3a1e8155129e0a889accd746e7ea595221bbdb642f24cd6e5097b21623762067` |
| `MANIFEST_SHA256.txt` | 1313 | `0d2bdf13b3a52d0519c8757b53af636f05aad9bb9e8d664c9033b02d13b46f0a` |
| `audit_claude_fanout2_round11_independent_2026-11-15.md` | 10823 | `574384ed8838c656ea84e5181b61e577e0d1dd9b5758afbf25ea8d62fe8456f8` |
| `round11_full_independent_rerun.txt` | 14303 | `1d6bf0befe4b98dba0697678cbaca84add4eb64450ca5ccacdbd3e522a8d3d34` |
| `independent_round11_local_audit_2026-11-15.py` | 2877 | `873830e47e3b181d46b2d284ba1c5ca67c8758fc88b1a678837749db5b2bf87e` |
| `out_independent_round11_local_audit_2026-11-15.txt` | 50 | `6798edd432d96733c2cf6fe54070edf40fe9b5851795d3b784b798ca49abb201` |
| `check_round10_HC_exhaustiveness_2026-11-14.py` | 47748 | `aa316db69814583cf02dc5338057f360916c6c6aa1be7f6e5e5c1224d6b0a2e2` |
| `check_round10_U2_integration_2026-11-14.py` | 13878 | `d0b5cc90fd050068aa0a4ed23d891ac1b4a1fb61a8b5f8c23498d21769e3689d` |
| `check_round9_overlap_P1_B6_2026-11-14.py` | 47322 | `c468f6ad5eb972b64803ca90de69a3b8c85beeedd21e9762363e89b83c78bde3` |

## Raw sources

### Claude final report — `claude_fanout2_round11_residual_report_2026-11-15.md`

BEGIN SOURCE claude_fanout2_round11_residual_report_2026-11-15.md
# 第十一段 最終数学報告：残余 𝓡_open の閉鎖と、豊かでない全段の独立証明（U₂）

**日付**：2026-11-15 JST　／　**作成**：Claude（Opus 5.5、新規セッション）
**状態**：研究アーカイブ。**全て自己報告の手証明**で、第三者の独立監査と形式検証はまだない。
**原稿・GitHub**：変更なし。`growupkuriyama-hub/papers` を読み取り専用で浅く clone した（HEAD `bbfb4630`、2026-11-14 21:43 JST。第十段と同じ版）。commit・push・PR はしていない。
**前段**：`claude_fanout2_round11_checkpoint1_2026-11-15.md`（定理 R の初版）

> **正式問題との区別.** 本報告が扱うのは特殊クラス U₂ だけである。設定は Σ={a,b,c}、A={a,c}、B={b,c}、ℓ=2、f=r=2、s=c_Σ で、所属は dat_ov の述語で決まる。結果は多項式代表長の**上界**である。**`op:fanout-two` は OPEN のまま**で、本報告はその肯定も否定も与えない（§10）。

## 判定表

| 項目 | 判定 | 数学的根拠 | 依存 | 検査の限界 |
|---|---|---|---|---|
| **A1**（同根 ac/b と鏡像） | **PROVED** | 補題 V により ν_B=0 が強制される。その上で補題 E を使う（§3） | 補題 M・W1・LG・B6(3)(5)・補題G・定理1 | 193,945 例で 0 失敗（§6）。8 例は全て補題 E の枝 |
| **A2**（同根 ac/bc） | **PROVED（空虚）** | 補題 V から、豊かでない成分では起こらない（§2.5）。型を使わない独立証明もある（§4） | 補題 V | 生成モデルで出現 0。c\*=0 の対照では V が破れる |
| **A3**（半遷移 abcA/abcB、単独・組） | **PROVED（空虚）** | 補題 V（§2.5）。独立証明は §4 の I/II/III | 同上 | 同上 |
| ztype の網羅 | **PROVED** | (p+r, p′+r′, m) の正負と、abc の 4 分割（§4.0） | — | — |
| T1〜T4（第十段） | **PROVED（定理 N で独立に置き換え）** | 本段の定理 N が全ての非豊かな段を覆う。旧証明に依存しない（§5） | 定理 N | 旧証明の逐行監査は不要になった |
| T5（豊かな成分） | **PROVED（再監査）** | F6・Y6・旗の継承を逐条で再証明し、量化も確認（§5） | B6(5)、c\*≥3 | — |
| 非豊かな HC_I/II/III | **PROVED（定理 N。引用は解消）** | §4 の 0d・0e（ab 型の κ を含む全場合） | 定理 N | 第十段で「CITED」と分類される 15,740 例（モデル）と 90 段（実導出）で 0 失敗 |
| 真正最短導出＋残余 | **OPEN（構成していない）** | 探索不足であり、不可能性は示していない。A2/A3 だけは補題 V で全ての導出について不可能 | — | 実導出 475 段は全て通過したが、残余は 0 |
| **J の全称** | **PROVED（自己報告）** | 豊かな成分があれば T5、なければ定理 N | 定理1 の前提一式 | 有界検査は補助にすぎない |
| 長さ上界 | **PROVED（自己報告、修正込み）** | 第十段 §5 の「訪れる添字の色が全て異なる」は偽なので、「跳ばない一歩の色が相異なる」に差し替えた。四分類の被覆も監査した（§7） | J の全称 | — |
| **U₂ 全定理** | **PROVED-U2（自己報告。第三者監査・形式証明なし）** | τ(G,c_Σ)=O(v^{18}θ̄_G^{17})、‖K‖₊≤4096‖G‖(1+2θ̄_G+2τ)+1_{ε∈L}（§7） | 上の全て | — |
| 正式 `op:fanout-two` | **OPEN** | U₂ は特殊クラスの上界にすぎない（§10） | — | — |

## 0. 結論

1. **補題 V（空虚性）[PROVED].**
   - 主張：根成分 x で ν_l(x)=0（l∈{a,b}）なら、l を含む η 成分 φ⊆x は c を含まない。
   - 理由：l は端の区間にしかない。そこから c まで伸びる φ は、唯一の lc 窓（または cl 窓）の両端を含むが、その窓は印付きである。
   - 帰結：豊かでない成分では κ の型は {a, b, c, ab, ac, bc} に限られる。`abcA`・`abcB`・`abc+` は起こらず、同根 {ac,bc} も起こらない。
   - したがって 𝓡_open は実質的に「同根 {ac,b}（その成分で ν_B=0）とその鏡像」だけになる。
2. **定理 R [PROVED].** 𝓡_open の全段で J が成り立つ。補題 E が閉じる。補題 V を使わない (r,r′) 分けの独立証明もある（checkpoint1 §4）。
3. **定理 N [PROVED].** **豊かな根成分のない全ての段**で J が成り立つ（e≤2）。
   - 第十段の T1〜T4 にも、引用していた HC_I/II/III（非豊か部分）にも依存しない。
   - T5 と合わせると、**型付き根最短木の全ての段で J が成り立つ**。
4. **U₂ 定理（自己報告）.** 第十段 §5 の計数（誤りを一つ修正）と合わせると、次が無条件で成り立つ。
   $$\tau(G,c_\Sigma)\le52+192(2\bar\theta_G+4)(H{+}1)+768\,C\,H\bar\theta_G(H{+}1),\quad H\le49v,\ C\le7^4(1+2H(\bar\theta_G+2))^{16}$$
   よって $\tau=O(v^{18}\bar\theta_G^{17})$。さらに
   $$\|K\|_+\le4096\|G\|(1+2\bar\theta_G+2\tau)+\mathbf 1_{\varepsilon\in L}$$
5. **有界検査.**
   - 第十一段の検査器は**証明の場合分けをそのままたどる構成器**で、探索をしない。
   - モデル上の全段と実導出 475 段で、PROOF_FAIL=0、VERIFY_FAIL=0。
   - 第十段の 8 例は完全トレースを取り、全て補題 E の枝に入った。
   - 失敗するべき対照は全て失敗した（§6）。

## 1. 資料・再実行

- 依頼書 3,524 行を全て読んだ。付録の 11 資料を抽出し、**SHA256 は全て一致**した（`extract.py`）。
- 第十段の HC 検査器を再実行した：`PYTHONHASHSEED=0 … --rand 400`、137 秒、exit 0。**time 行を除き、提出ログと一致**した。
- 第十段の実導出検査器を再実行した：exit 0。**提出ログとバイト一致**（SHA256 `66355f70…`）。
- **相違**：付録 C の監査メモが記したこのログの SHA256 は `66355f70…cec6933cd8…` で **63 桁**しかない。付録 H のヘッダと実ファイルは `66355f70…cec693f3cd8…`（64 桁）で、監査メモは `f` を 1 文字落としている。転記誤りと判断した。実ファイルは付録 H のヘッダと一致する。
- 読み取り専用 clone の `main.tex` で次を確認した。
  - `def:grammar-properties`（good＝ε-free・非削除・非置換・非併合）
  - $\mathcal E_d$（$v_1,\dots,v_{d-1}\in\Sigma^+$）
  - `def:tuple-substitutable`
  - `lem:thickness-equivalence`(i)(ii)(iv)
  - τ の定義（$\tau_X=\min\{\|\tuple v\|_1:\tuple v\in\mathrm{Cl}_{L,s}(X)\}$）
  - `cor:distribution-representatives`（L1240）
  - `thm:data-from-typed-thickness`（L1118）
  - $N_{\rm typ}\le C_s(G)\le|\mathsf S^\sharp|^{fr_{\max}}\|G\|$（L1114, L1461）
  - `op:fanout-two`（L2131）

## 2. 道具

記法：$x=u_0c_1u_1\cdots c_nu_n$。区間 s が **A 占有**とは $a\in u_s$ のこと。π_A の窓は区間と次のように対応する。
- ca 窓：A 占有の s≥1
- ac 窓：A 占有の s<n
- cc 窓：A 非占有の内側区間
- aa 窓：区間内の a の隣接

各型の窓は左から数え、最初の c\* 個の両端点に印を付ける。B も同様。c\*=3 とし、各補題で必要な下限も記す。

### 2.1 補題 M（印の位置）[PROVED、c\*≥2]

- **M1.** 最小の A 占有 $s_0\ge1$ について、$c_{s_0}$ と $u_{s_0}$ の最初の a に印が付く。最初の ca 窓だからである。
- **M2.** A 占有の s<n のうち小さい方から 2 つについて、$u_s$ の最後の a と $c_{s+1}$ に印が付く。$s_0<n$ なら、$a''$（$u_{s_0}$ の最後の a）と $c_{s_0+1}$ に印が付く。
- **M3.** ν_B=0 のとき：$b_0$ なら $u_0$ の最後の b と $c_1$ に、$b_n$ なら $c_n$ と $u_n$ の最初の b に印が付く。どちらも唯一の bc 窓・cb 窓である（c\*≥1 で足りる）。
- **M4.** $|\pi_Ax|\ge2$ なら、x の最初の a に印が付く。
  - 区間 0 にあれば、そこから出る窓（aa か ac）が、その型の最初の窓である。
  - 区間 s≥1 にあれば、そこに入る ca 窓が最初の ca 窓である。
- **M5.** N(aa)≥1 なら、最初の aa 窓の両端 $a_1<a_2$ に印が付く。これは π_A で連続する 2 つの a で、同じ区間にある。
- **M6.** n≥2 なら $c_1$ に印が付く。$c_1$ から出る π_A の窓は ca か cc で、どちらもその型の最初の窓である。
- **M7.** x の最初の a が区間 0 にあり n≥2 なら、$c_2$ に印が付く。区間 1 にあり n≥3 なら、$c_3$ に印が付く。
  - 前者：$c_2$ に入る窓は、ac の 2 番目か cc の 1 番目である。
  - 後者：$c_3$ に入る窓は、ac の 2 番目か cc の 1 番目である。区間 1 が A 占有なので、区間 2 が最初の A 非占有の内側区間になり得る。

### 2.2 W1 の精密形 [PROVED]

W_{j'} はその段の η の成分 φ_κ だけを非空語 ψ_κ に置き換えた語で、他の η は置き換えない（B6 §4.1(4)、F 側は原木から作る）。

- φ に入らない x の文字（印付きの文字は全てこれに当たる）は、同順で文字どおり残る。
- x で隣接していれば W でも隣接する。間に φ が入る余地がないからである。
- 隣接していなければ W でも隣接しない。ψ は非空だからである。

### 2.3 補題 LG（文字配置 ⇒ hosting）[PROVED]

補題G により、Γ が同じなら区間内の並べ方は自由である。

- **LG1.** $c^\circ<a^\circ<b^\circ$ かつ $b^\circ\ge a^\circ+2$ ⇒ Γ(w) は (ca, b) を hosting する。
  - $a^\circ$ を区間の先頭に置く。
  - $b^\circ$ が後の区間なら、間に区切りの c がある。
  - 同じ区間なら、間の非 c 文字を一つ挟む。
- **LG3.** $a^\circ<b^\circ$ で、$c'$ を $a^\circ$ の後の最初の c とし、$c'<b^\circ$ かつ $b^\circ\ge c'+2$ ⇒ (ac, b)。
  - $a^\circ$ を区間の末尾に置く。
  - $b^\circ$ が次の区間にあれば、その区間の他の文字を先に置く。
  - 2 つ以上後の区間なら、間に区間と区切りがある。
- **LG5.** $c^\circ<a^\circ<b^\circ<c^\bullet$ かつ $b^\circ\ge a^\circ+2$ ⇒ (ca, bc)。$a^\circ$ を先頭に、$b^\circ$ を末尾に置く。
- 反転と a↔b の入れ替えで、(b,ac)、(cb,a)、(a,bc)、(b,ca)、(bc,a)、(a,cb)、(cb,ac) が得られる。一穴の ca、ac、cb、bc と、同じ区間の ab も同様。
- 検査器 [1] は、この並べ替えを**オラクルなしで実際に構成**して照合する。

### 2.4 Y 側（B6(3)(5)＋補題G）[PROVED]

T(i) について、次は $x_i$ と一致する。
- $a_0,a_n,b_0,b_n$（ŝ₂ による）
- $[\nu_A\ge1]$、$[\nu_B\ge1]$
- 内容

また $n_T\ge\min(n_x,c^*)$、$N_T(e)\ge\min(N_0(e),c^*)$ である。補題G により、内側の占有区間の位置は個数の範囲で自由に選べ、余った文字は占有区間に集められる。例えば $N_T(aa)\ge1$ なら、指定した A 占有区間に a を 2 個置ける。

### 2.5 補題 V（空虚性）[PROVED、c\*≥1]

**主張.** $\nu_l(x)=0$ かつ x が c を含むなら、l を含む η 成分 φ⊆x は c を含まない。

*証明.*
- φ が $u_0$ の l と c を含むとする。φ は連続なので、$u_0$ の最後の l から $c_1$ までを含む。この窓（π_X で連続）は l で始まり c で終わる唯一の窓で、印付きである。φ は印を含まないので矛盾する。
- $u_n$ の場合も同様（cl 窓）。∎

**帰結**（豊かでない成分、c\*≥3）：
- $r_\kappa>0$ ⇒ ν_A≥c\*、n≥c\*+1≥3。豊かでないので ν_B=0。
  - `abcA`（p′>0）なら φ は b と c を含むので矛盾。よって **abcA は起こらない**。鏡像の abcB も起こらない。
- `abc+` は φ が a,b,c を含む。
  - n≥3 なら ν_A=0 か ν_B=0 なので矛盾。
  - n≤2 なら m>0 が不可能（cc 削除には n≥c\*+2、ac 削除には n≥c\*+1 が要る）。
- ac 型の κ はその成分で ν_A≥1 を強制する。r=0 でも、φ が a と c を含むからである。m>0 から n≥c\*+2 なので、豊かでなければ ν_B=0。bc 型はその逆である。
  - よって **同根の {ac,bc} は豊かな成分でしか起こらない**。
- 生成モデルの全段で V を assert した（違反 0）。c\*=0（印なし）の対照では V が破れる（§6）。

## 3. 定理 R：残余の閉鎖

$\mathcal R_{\rm open}$ は、豊かな成分がなく、aa+bb を同時に削る κ もない段である。そこでの型の組は、補題 V によって同根の {ac,b} か {bc,a} に限られる。半遷移型と {ac,bc} は空虚である。

{ac,b} 同根（成分 i）の場合：
- ac 型なので ν_A(x_i)≥1、ν_B(x_i)=0。
- b 型なので b∈x_i。
- $r'=0$ だから、次の分割はどちらも非零・保存的である。
  - $D_{ac}=(p\,aa+q\,cc+r(ac{+}ca),\ m\,cc)$
  - $D_b=(0,p'bb)$

### 補題 E [PROVED]

**仮定.** ν_A(x_i)≥1、ν_B(x_i)=0、b∈x_i、$D=D_{ac}+D_b$。

**結論.** 成分 i に置く二穴で J が成り立つ。

*証明.* $s_0$ を最小の A 占有 s≥1 とする（$\le n-1$）。

- **$b_n$ の場合：(ca, b).**
  - F：$c_{s_0}<a''<c_{s_0+1}\le c_n<b^*$（M1, M2, M3）。W1 と LG1 による。
  - Y：内側の A 占有を区間 1 に取り、その先頭に a、b を区間 $n_T\ge2$ に置く。
- **$b_0$ の場合：(b, ac).**
  - F：$b^*<c_1\le c_{s_0}<a''<c_{s_0+1}$。LG2（LG1 の反転）による。
  - Y：b を区間 0 に、区間 1 の末尾に a を置く。
- 長射影：成分 i は a,b,c を含む。∎

鏡像の {bc,a} も同様である。∎

**8 例との対応.** 第十段の 8 例（ac/b 5、a/bc 3）は、検査器 [3] で全て `I:LemmaE-b0` と `II[I:LemmaE-bn]`（鏡像）に入った（§6.2）。

## 4. 定理 N：豊かでない全ての段

### 4.0 場合の立て方

- 総差分 $D=(p,q,r,p',q',r')$ について、$(r>0?,\ r'>0?)$ で大きく分ける。
- r=r′=0 なら q=q′ で、さらに $(p>0?,\ p'>0?,\ q>0?)$ で分ける。
- κ の位置は次の 3 つの集合で表す。
  - CA：$p_\kappa>0$ の κ の成分
  - CB：$p'_\kappa>0$ の κ の成分
  - CC：$q_\kappa>0$ の κ の成分
- 2.5 節の下界を使う：$p_\kappa>0$ ⇒ $N^A(aa)\ge c^*+1$、$q_\kappa>0$ ⇒ n≥c\*+2。
- 全ての $D_i$ が保存的・非零で $R(D_i)\subseteq\mathrm{alph}(h_i)$ を満たすことは、検査器が全ての段で assert している。

### 4.1 III：r,r′>0

r>0 の κ は ν_A≥c\* の成分 $i_A$ にあり、そこは ν_B=0 である。r′>0 の κ は成分 $i_B$ にあり、ν_A=0 である。豊かでないので $i_A\ne i_B$ となる。

- r′>0 の κ は $r_\kappa=0$ なので $q_\kappa\ge r'_\kappa$。よって $q\ge r'$。
- 次のように分ける。
  - $D_1=(p\,aa+(q-r')cc+r(ac{+}ca),\ q'cc)$
  - $D_2=(r'cc,\ p'bb+r'(bc{+}cb))$
- 穴の置き方：
  - $i_A<i_B$ なら (ca, bc)。F は LG5 で、$c_{s_0},a''\in x_{i_A}$、$b'''$ は $x_{i_B}$ の最小の B 占有区間 <n の最後の b（M2 の鏡像）、その後に印付きの c。
  - $i_B<i_A$ なら (cb, ac)。
- Y：成分ごとに独立に置く。長射影は、$i_A$ の π_B と $i_B$ の π_A がともに $c^{n_T}$（$n_T\ge3$）であることによる。∎

### 4.2 I：r>0=r′（II はその鏡像）

成分 i（$r_\kappa>0$ の κ の成分）は ν_A≥c\*、ν_B=0 を満たす。

- **p′=0：** 一穴の ca。
  - F：$c_{s_0}<a''$。
  - Y：ν_A^T≥1。π_B は $n_T\ge3$ 個の c を含むので長い。
- **p′>0 かつ b∈x_i：** 補題 E。
- **p′>0 かつ b∉x_i：補題 X.** bb を削る κ は他方の成分 i′ にある。
  - ca（または ac）を成分 i に、b を成分 i′ に置く。b は M4 の最初の b。
  - F：i<i′ なら LG1 で (ca,b)、i′<i なら LG2 で (b,ac)。
  - Y は成分ごとに独立。∎

### 4.3 0：r=r′=0

$D_a=(p\,aa,0)$、$D_b=(0,p'bb)$、$D_c=(q\,cc,q\,cc)$ とする。

- **0a（正のものが一つ）.** 一文字の穴を、該当する κ の成分に置く。F は M4 または M6。Y の長射影は $N_T(aa)\ge1$、または $n_T\ge3$ による。
- **0b（p,q>0、p′=0）.**
  - **別の成分：** 印付きの a と c を成分の順に、文字どおり使う。間には $v_1\ne\varepsilon$ がある。
  - **同じ成分 i（n≥c\*+2）.** $a^\circ$ を最初の a、その区間を s とする。
    - s=0：(a, c₂)。F は M7、Y は a を区間 0 に置く。
    - s=1：(a, c₃)。F は M7、Y は ν_A≥1 から a を区間 1 に置く。
    - s≥2：(c₁, a)。F は M6・M4。Y は、a が内側なら区間 2、$a_n$ なら区間 $n_T\ge3$ に置く。

    いずれも隙間に c が入る。
- **0c.** 0b の鏡像。
- **0d（p,p′>0、q=0）.**
  - **別の成分：** 文字どおり使う。
  - **同じ成分：補題 L-ab** [PROVED]。
    - M5 の $a_1<a_2$、$b_1<b_2$ は相異なる 4 位置である。4 組 $(a_k,b_l)$ が全て隣接すると $b_1=b_2=a_1+1$ になって矛盾するので、距離≥2 の組 $(a_k,b_l)$ がある。F はそれを、その順に文字どおり使う。
    - Y は順序 (a,b) について次のように置く（(b,a) も同様）。
      - **x で同じ区間の場合：** 区間 0 なら $a_0b_0$、区間 n なら $a_nb_n$、内側なら $\nu_A,\nu_B\ge1$ の旗で、T にも共通区間が取れる。$N_T(aa)\ge1$ なので a を 2 個置き、「a a b」とする。
      - **別の区間（$s<t$）の場合：** T に共通区間が取れれば同上。取れなければ x でも a と b は互いに素な区間にある。
        - s=0 なら $b_0=0$ で、T の b は区間 ≥1 にある。
        - s が内側なら ν_B=0 なので t=n。T では a を区間 1、b を区間 $n_T\ge2$ に置く。∎
- **0e（p,p′,q>0）.**
  - **e1（CA∩CB∩CC∋i）.** $x_i$ は a,b,c を含み、n≥c\*+2、$N(aa),N(bb)\ge c^*+1$ で、豊かでないので ν_A=0 か ν_B=0。
    - ν_B=0<ν_A なら補題 E（$D_{ac}=(p\,aa+q\,cc,\ q\,cc)$）。
    - 逆なら鏡像。
    - ν_A=ν_B=0 なら**補題 EO**（checkpoint1 §3.3）。
      - E1：$a_0\wedge b_n$ なら (a, cb)。
      - E2：$b_0\wedge a_n$ なら (b, ca)。
      - E3：全てが $u_0$ にある場合。最後の文字が b なら (a, bc) を文字どおり、a なら鏡像。
      - E4：全てが $u_n$ にある場合。反転する。
  - **e2（CA∩CB∋i₀、CC∌i₀）.** CC の κ は別の成分 $i_c$ にある。η の成分は ≤2 なので、$x_{i_0}$ にある η の成分は、p,p′>0 をもつ**一つの φ だけ**である。
    - $a\in x_{i_c}$ なら**補題 X′**。$h_{ac}$ を $i_c$ に置く：最初の a が区間 ≥1 なら ca（M1）、区間 0 なら ac（M6）。b を $i_0$ に置く。F は LG1〜LG4、Y は旗による。
    - $b\in x_{i_c}$ なら鏡像。
    - $x_{i_c}\in c^+$ の場合：$a^\circ,b^\circ$（$x_{i_0}$ の最初の a と b）は印付きで、φ より前にある。φ は a と b を含み、最初のものは印付きだからである。したがって $\max(a^\circ,b^\circ)$ までの接頭辞は W に文字どおり残る。
      - (i) 同じ x 区間：('ab','c') または ('c','ab')。
        - F：同じ W 区間にあるので、ab に並べ替えられる。c は $x_{i_c}=c^k$ の印付き $c_2$（$i_0<i_c$）か $c_1$（$i_c<i_0$）で、隙間に c が入る。
        - Y：共通区間の旗による。
      - (ii) 別の区間（$a^\circ<b^\circ$、鏡像も同様）。s,t をそれぞれの区間とする。
        - $t\ge s+2$、または区間 t の $b^\circ$ の前に a がある場合：文字どおりの (ac, b)。
        - そうでない場合：文字どおりの acb（e=1）。
        - Y は旗による。豊かな配置（内側と内側）は仮定から除かれる。
  - **e3（CA∩CC∋i、CB∌i）.** 補題 X′ と同じ構成。
  - **e4.** 鏡像。
  - **三つの集合が互いに素な場合.** d≤2 では起こらない。∎

## 5. T1〜T5 の再監査

- **T5.** F6 分類を逐条で再証明した。
  - $a_0b_0$ ⇒ abc、$a_nb_n$ ⇒ cab。
  - $\nu_A,\nu_B\ge1$ ⇒ 内側の共通区間で abc。
  - ν_A≥1=…、ν_B=0 ⇒ bca か acb。
  - 両方 0 ⇒ 両端に分かれ、n=1 なら acb、n≥2 なら硬直形。

  Y6 は区間 1・2（$n_T\ge3$）による。量化については、Q と W の外側文脈は F 側で W の文字としてしか使わないので、任意でよい。Γ(W\*) と Γ(T) は別物として扱っている。$c^*\ge3$ ⇒ $n_T\ge\min(n_x,3)=3$ も成り立つ。**誤りは見つからなかった。**
- **T1〜T4.** 定理 N が T5 以外の全ての段を独立に覆うので、**最終定理はもう T1〜T4 に依存しない**。
  - T2 の同根の順序継承は L-ab と 0b:same で独立に再証明した。
  - T4 は I（補題 X）、III、0e3 が置き換える。
  - 旧文の誤りは指摘していない。逐行の監査はしていない。
- **HC_I/II/III（非豊か部分）.** 補題 V により、豊かでない成分の aa+bb 型は c なしの ab 型に限られる（abc+ は空虚）。それを含む全ての段は 0d/0e が覆う。**引用は解消した。**

## 6. 有界検査（`check_round11_residual_2026-11-15.py`）

実行：`PYTHONHASHSEED=0 python3 -I check_round11_residual_2026-11-15.py --src <付録抽出ディレクトリ>`。標準ライブラリのみ、固定 seed。結果は `out_check_round11_residual_2026-11-15.txt` にある。

### 6.1 結果（全量実行）

実行時間 860.5 秒、exit 0、最終行 `ALL CHECKS PASSED`。

| 節 | 内容 | 結果 |
|---|---|---|
| [0] | 独立実装の dat/Γ（長さ≤8 の全 1,558 類）。**総当たり参照オラクル**と第十段オラクルを照合（一穴 14,297、順序対 60,552、2 成分タプル 4,000） | 全て一致 |
| [1a]〜[1h] | **証明追従構成器**（探索なし）。対象は網羅 d=1（93）、乱数、疎・非豊か、残余の意図的生成（25,503。第十段の OPEN 類は 838）、d=2 の跨り（47,368）、枝を狙った形（81,673）、端だけの成分（25,554）、決定的構成（695） | **193,945 例、PROOF_FAIL=0、VERIFY_FAIL=0**。F は LG 構築で 181,873、オラクルで 12,072（T5 の枝） |
| 枝ごとの件数 | T5 12,072、III 50、I:single-ca 10,720、I:LemmaE-bn 596、I:LemmaE-b0 313、I:LemmaX 520、0a 136,185、0b:diff 4,443、0b:same 6,803、0d:diff 2,571、0d:L-ab 16,263、0e1:LemmaE-bn 948、0e1:LemmaE-b0 233、EO1 883、EO3 152、EO4 132、0e2:a-in-c 74、0e2:i-ab 514、0e2:ii-ac,b 44、0e2:ii-acb 396、0e3 33（鏡像は別に数えた） | **全ての枝に事例がある**（coverage missing なし） |
| 第十段の分類との対応 | 「CITED-HC_I/II/III」は 15,740 例、「OPEN」は 838 例で、全て定理 N/R で検証。OPEN は全て補題 E の枝（`I:LemmaE-*`、`II[…]`、`0e1*:LemmaE-*`）に入った | — |
| [2] | 補題 V を全段で検査 | 86,267 段で違反 0。豊かでない成分の ztype は a, b, c, ab, ac, bc だけ。**abcA/abcB/abc+/abc2 は 0（coverage missing。補題 V により空虚）** |
| [2′] 対照 | c\*=0（印なし） | V は 778 配置中 321 で破れる（**破れるべき対照が破れた**） |
| [3] | 第十段ドライバの再実行 | `ALL CHECKS PASSED` を再現し、OPEN 8 例を捕捉して完全トレース。8/8 で検証 |
| [4] 対照 | 失敗するべきもの | e≤1 だけ：193,852 中 4,031 で失敗。補題 E を逆の型で使う：2,090 中 902 で失敗。補題 X の二穴を一成分に置く：520 中 514 で失敗。長射影の条件を外す：ŝ₂ が `('w','b')`→`('ps','b','b')` と壊れる（検出）。「印付き窓が W に文字どおり残る」：1,837 中 60 で偽（証明は印付き**文字**しか使わない） |
| [5] | 実導出（第九段の文法、第十段の統合ドライバで再生） | **非零 475 段、全て検証、FAIL 0**。枝：T5 214、III 171、0e1/EO3 系 84、L-ab 6。第十段の「CITED」90 段も全て定理 N の枝で検証した |

### 6.2 第十段の 8 例

第十段のドライバを同じ seed で再実行し（[3]）、OPEN に分類された構成を捕まえた。構成は 6 個、T の状態を含めて 8 例である。

| # | 第十段の tag・類 | 根 x（成分） | 旗 | 第十一段の枝 | 穴・分割 D_i | F の構築 |
|---|---|---|---|---|---|---|
| 1–3 | NR377 `OPEN:ac/b:same` | `abbbbbbbbcaaaacccaccaaccac` | n=9、ν_A=4、ν_B=0、b₀ | `I:LemmaE-b0` | (b, ac)：$(0,p'bb)$＋$(r(ac{+}ca),\,r\,cc)$（p′=1,2,2） | LG2（b\*<c₁≤c_{s₀}<a″<c_{s₀+1}） |
| 4–5 | NR548 `OPEN:ac/b:same` | (`bbbbbbbcacacaaccacacaac`, `bbb`) | 成分 0：n=8、ν_A=6、ν_B=0、b₀ | `I:LemmaE-b0` | (b, ac) を成分 0 に | LG2 |
| 6–8 | NR695 `OPEN:a/bc:same` | `aaaaaacbbcbcbcbcbcbbccbcaaaaaaaabb` | n=9、ν_A=0、ν_B=7、a_n | `II[I:LemmaE-bn]`（鏡像） | (cb, a)：$(q\,cc,\,r'(bc{+}cb))$＋$(p\,aa,0)$（p=4,3,1） | 鏡像の LG1 |

8 例とも、Γ(W_{j′})、κ ごとの Z、原の計数 N₀、T と Γ(T)、F 証人の語と穴の位置、F[t]、e=1 の可否をログ [3] に全て記録した。e=1 も可能だった（第十段も e=1 で通過している）。本段は補題 E の二穴を使う。

### 6.3 独立性と限界

- **独立性.**
  - 第十段から借りたのは、段モデルの生成器と、Γ レベルの hosting オラクル（`hosts`/`host_comp`/`build_comp`）と `expand` だけである。
  - オラクルは [0] で、**別実装の総当たり**（dat 類の全ての語の文字どおりの探索）と 74,849 件で照合した。
  - F 側は、証明が指定した LG の並べ替えを**オラクルなしで構築**する。
  - 構成器は**探索しない**。
- **限界.**
  - 有限検査である。生成モデルは第十段の敵対的モデルの範囲にある。
  - 実導出（[5]）では W の位置が公開されていないので、F は**オラクル**で確かめている。

## 7. 一体の代表長評価（修正込み）

第十段 §5.1〜5.3（型付き高さ H≤49v、骨格 $N_{\rm sk}\le32c^*(H{+}1)$、η の数 $\le rN_{\rm sk}$、$|I_j|\le rH$、$|U_{k+1}\setminus U_k|\le H\theta$、色数 C）を逐条で読み、正しいことを確認した。

最終状態で残る原窓 w=(p,q)（射影 X、成分 i）は、次の四類に**漏れなく**入る（重複は上界を緩めるだけである）。

1. 印付き窓：成分・射影ごとに $\le4c^*$。
2. 端点が骨格節点の書く文字：印付き文字はここに入る。射影ごとに $\le2\theta N_{\rm sk}$。
3. 両端が別の η 成分にある：骨格でない節点は、自分を含む極大自由部分木 η に入る。φ は連続なので、窓の左端は φ の最後の X 文字である。成分ごとに 1 個。
4. 両端が同じ成分の内部にあり、削られなかった：$k(w):=\min\{k:\mathrm{span}(w)\cap U_k\ne\emptyset\}$ とする。
   - 貪欲列は (0,m] を区間に分ける。跳ぶ区間 (k,j′] では、k<k(w)≤j′ の w が**全て**削られる（P1-b の 𝒟）。
   - よって残るのは、跳ばない一歩 k→k+1 で k(w)=k+1 となる w だけである。

**§5.4 の修正.**
- 第十段の「貪欲法が訪れる添字の色は全て異なる」は偽である（例：色 A,A）。
- 正しくは次のとおり。跳ばない一歩を踏む添字 k では、それより後に col(k) が現れない（現れれば最後の出現まで跳ぶ）。よって跳ばない一歩の色は相異なり、その数は ≤C である。
- 一歩で新しく加わる位置は ≤Hθ で、各位置は一つの射影で高々 2 つの窓の span に入る。よって η ごとに射影あたり ≤2CHθ。

以上から、第十段 §5.4 の式がそのまま成り立つ（$d=r=2$、$c^*=3$）。

$$\tau_X\le2\bigl[4c^*d+(2\theta+2r)N_{\rm sk}+2rCH\theta N_{\rm sk}\bigr]+2d\le52+192(2\theta+4)(H{+}1)+768\,CH\theta(H{+}1).$$

$c^*$ を変えるときは、定数を次のように取り直す。
- $52=8c^*d+2d$
- $192=2\cdot32c^*$
- $768=2\cdot2r\cdot32c^*$

**定理 U₂（自己報告）.** $L\cap\Sigma^+=\operatorname{dat}_{\rm ov}^{-1}(\mathcal Q)$、$L\in\mathcal C^{\rm mcf}_{2,c_\Sigma}$ とし、G を reduced good、fan-out≤2、rank≤2、$L(G)=L\cap\Sigma^+$ とする。このとき上の上界が成り立ち、$\tau(G,c_\Sigma)=O(v^{18}\bar\theta_G^{17})$ である。

`cor:distribution-representatives`（L1240、仮定は `thm:data-from-typed-thickness` と同じで、U₂ はそれを満たす）と $N_{\rm typ}\le8^4\|G\|$ から、
$$\|K\|_+\le4096\|G\|(1+2\bar\theta_G+2\tau)+\mathbf 1_{\varepsilon\in L}=O(\|G\|^{19}\bar\theta_G^{17}).$$
θ̄ は**元の G の値**だけを使う。

## 8. 真正最短導出（優先 D）

- **構成していない。** 分類は「(1) 探索不足」である。
- 補題 V により、A2・A3 は**全ての導出で**（最短性を使わずに）不可能である。
- A1 は段モデルでは起こる（[1d] に多数）が、型付き最短の実導出では作っていない。
- 実導出 475 段（[5]）は全て prove_J を通過し、残余は 0 だった。
- 定理 N は一般の証明なので、真正の例の有無は U₂ の結論に影響しない。

## 9. 依存表

| 主張 | 状態 |
|---|---|
| 補題 M、W1、LG、補題 V、補題 E/X/X′/EO/L-ab、定理 R、定理 N | 本報告で手証明（自己報告）。有界検査は補助 |
| T5・F6・Y6 | 第十段の証明を逐条で再証明（自己報告） |
| 定理1（J⇒短縮）、P0、H\*\* | 第十段の証明。ChatGPT 監査は「中核は整合的」と判断。本段では再監査していない |
| P1、B6 計数形 | 第九段の証明で、独立監査済み（VALID WITH EXPLICIT SCOPE） |
| 型付き高さ、骨格、色数 | 第十段の証明を確認 |
| 長さの四分類 | 本報告で修正して監査 |
| T1〜T4、HC_I/II/III | **もう使わない**（定理 N が置き換えた） |

## 10. 正式問題との区別

`op:fanout-two` は「LG の外の任意の擬多様体で、一様な多項式データ長が**失敗する**か」を問う。

- 原稿（L2143 以降）は、肯定の十分条件として「ある $U_1$-型付けで、ある実現型の最短代表が超多項式になる標的族」を挙げている。
- 本報告が示すのは、**この特定の族**（Σ={a,b,c}、重なる二射影、c_Σ）**の代表長は多項式**だということである。この族はそうした証人にならない。
- 他の族について、また `op:fanout-two` そのものについては何も言わない。

**`op:fanout-two` は OPEN。原稿を変更する根拠はない。**
END SOURCE claude_fanout2_round11_residual_report_2026-11-15.md

### Claude checkpoint — `claude_fanout2_round11_checkpoint1_2026-11-15.md`

BEGIN SOURCE claude_fanout2_round11_checkpoint1_2026-11-15.md
# 第十一段 チェックポイント1：残余 𝓡_open の手証明（最初の数学的結果）

**日付**：2026-11-15 JST　／　**作成**：Claude（Opus 5.5、新規セッション）　／　**状態**：研究メモ・未査読・形式検証なし・**独立監査未実施**
**原稿・GitHub**：変更なし（閲覧もしていない。付録の原資料だけを使用）

## 0. 量化と資料

- 依頼書全 3,524 行を読んだ。付録の 11 資料は `BEGIN SOURCE` から抽出し、**全て SHA256 一致**。
- 設定は依頼書 §1 のまま：Σ={a,b,c}、A={a,c}、B={b,c}、f=r=2、ℓ=2、s=c_Σ、c\*≥3（具体値 3）。
- 対象は、G の型付き根最短木から作られる全ての貪欲 DFS 段。J は第十段 §2.4 の定義のままで、強化していない。F 側は Γ(W_{j'}) のデータ類、Y 側は B6 状態 T のタプル。
- 使う前段の結果：定理1（J⇒短縮）、P1-b/d、B6(3)(5)、補題G（dat_ov↔Γ と区間内の自由配置）、W1（φ の外の文字は W_{j'} に文字どおり同順で残る）。どれも本段で新たに仮定を足していない。

## 1. 結論（チェックポイント時点）

**定理 R [PROVED（自己報告の手証明）].** 𝓡_open の全ての段で J が成り立つ（e≤2）。

- A1（同根 {ac,b}・鏡像）、A2（同根 {ac,bc}）、A3（`abcA`/`abcB` 単独、または任意の第二の型との組、同根・別根とも）を全て覆う。
- 証明は κ の型ではなく、**総差分 D の (r, r′) の正負**で場合を分ける。
  - **I**：r′=0<r。
  - **II**：鏡像。
  - **III**：r,r′>0。
  - **0**：r=r′=0。

  この分け方なら半遷移型も自然に入る。
- 有限検査や「現れなかったこと」は除外の理由に使っていない。
- **副産物（§5）**：同じ道具で、豊かでない段の**全て**（HC_I/II/III の引用部分を含む）に J の独立証明が付く見込みである。最終報告で検証する。

## 2. 道具

### 2.0 記法

- 根成分 $x=u_0cu_1\cdots cu_n$ について、$c_k$ は第 k 番の c（$u_{k-1}$ と $u_k$ の間）。
- 区間 s が **A 占有** とは $u_s\ni a$ のこと。
- $\pi_Ax$ の窓は次のように区間と対応する。
  - `ca` 窓：A 占有の s≥1 と一対一。
  - `ac` 窓：A 占有の s<n と一対一。
  - `cc` 窓：A 非占有の内側区間と一対一。
  - `aa` 窓：区間内の a の隣接。
- 各型の窓は左から順に数え、最初の c\* 個の**両端点**に印が付く。B も同様。

### 2.1 補題 M（印の位置）[PROVED]

c\*≥2 とする。
- (M1) 最小の A 占有 $s_0\ge1$ について、$c_{s_0}$ と $u_{s_0}$ の最初の a に印が付く（最初の ca 窓）。
- (M2) A 占有の s<n のうち小さい方から 2 つについて、$u_s$ の最後の a と $c_{s+1}$ に印が付く（ac 窓の 1・2 番目）。とくに $s_0<n$ なら、$u_{s_0}$ の最後の a（$a''$ とする）と $c_{s_0+1}$ に印が付く。$s_0$ より前の ac 窓は高々 s=0 の 1 つだからである。
- (M3) ν_B=0 のとき：
  - $b_0$ なら、$u_0$ の最後の b と $c_1$ に印が付く。bc 窓は s=0 の一つだけである。
  - $b_n$ なら、$c_n$ と $u_n$ の最初の b に印が付く。cb 窓は s=n の一つだけである。
- (M4) $|\pi_Ax|\ge2$ なら、x の最初の a に印が付く。その a から出る窓（aa か ac）か、入る窓（ca）が、その型の最初の窓だからである。
- (M5) $N(aa)\ge1$ なら、最初の aa 窓の両端 $a_1<a_2$ に印が付く。

### 2.2 W1 の精密形 [PROVED]

その段の η の成分 φ_κ に**入らない** x の文字（印付きの文字を全て含む）は、W_{j'} に同順で文字どおり現れる。
- x で隣接していれば W でも隣接する。
- 隣接していなければ W でも隣接しない。置換片は非空だからである。

### 2.3 文字配置 ⇒ hosting の補題 LG [PROVED]

語 w が次の位置を持てば、Γ(w) は対応する穴列を、その順・間隔≥1で hosting する（補題G の区間内並べ替えによる）。

- (LG1) $c^\circ<a^\circ<b^\circ$ かつ $b^\circ\ge a^\circ+2$ ⇒ (ca, b)。
  - $a^\circ$ をその区間の先頭に置く。
  - $b^\circ$ が後の区間なら、間に区切りの c がある。
  - 同じ区間なら、間の非 c 文字を一つ挟む。
- (LG2) $b^\circ<a^\circ<c^\circ$ かつ $a^\circ\ge b^\circ+2$ ⇒ (b, ac)。$a^\circ$ を区間の末尾に置く。
- (LG3) $a^\circ<b^\circ$ で、$c'$ を $a^\circ$ の後の最初の c とし、$c'<b^\circ$ かつ $b^\circ\ge c'+2$ ⇒ (ac, b)。
  - $a^\circ$ を区間の末尾に置く。
  - $b^\circ$ が次の区間にあれば、その前の非 c 文字を先に置く。
- (LG4) 鏡像（反転）：$b^\circ<c''<a^\circ$ で、$c''$ を $a^\circ$ の前の最後の c とし、$b^\circ\le c''-2$ ⇒ (b, ca)。
- a↔b の入れ替えで (cb, a)、(a, bc)、(bc, a)、(a, cb) も同様。一穴の ca（c が a の前）、ac も同様。
- 文字どおりの出現は自明に hosting される。

### 2.4 Y 側の旗 [B6(3)(5)＋補題G]

状態 T(i) について、次は $x_i$ と一致する。
- $a_0,a_n,b_0,b_n$
- $[\nu_A\ge1]$、$[\nu_B\ge1]$
- 内容

さらに $n_T\ge\min(n_x,c^*)$、$N_T(e)\ge\min(N_0(e),c^*)$ である。

補題G により、占有集合は次の条件の範囲で自由に選べる。
- 端は旗で決まる。
- 内側は個数だけが決まり、位置は任意。
- 余った文字は占有区間のどこに集めてもよい。

### 2.5 κ の型から根成分への帰結（c\*≥2。窓 e を削るなら $N_0(e)\ge c^*+1$）

- $r_\kappa>0$ ⇒ その成分で $N(ac)\ge c^*+1$ なので、$\nu_A\ge c^*$、$n\ge c^*+1\ge3$。
  - 豊かでないなら **ν_B=0**。
  - さらに $N^B(bc)\le1$ なので、その成分の κ は $r'=0$。
- $q'_\kappa>0$（B 側の cc 削除）⇒ B 非占有の内側区間が $\ge c^*+1$ 個あるので、$n\ge c^*+2$。
- $p_\kappa>0$ ⇒ $N^A(aa)\ge c^*+1$。

## 3. 三つの鍵補題

### 3.1 補題 E（端の b）[PROVED]

**仮定.** 根成分 i が $\nu_A(x_i)\ge1$、$\nu_B(x_i)=0$、$b\in x_i$ を満たす。D が非零・保存的な二つの和 $D=D_{ac}+D_b$ に分かれ、$R(D_{ac})\subseteq\{a,c\}$、$D_b=(0,p'bb)$、$p'>0$ とする。

**結論.** $e=2$ で J が成り立つ。

*証明.* 両方の穴を成分 i に置く。i は a,b,c を含むので、両射影が長い。ν_B=0 なので、b は $u_0$ か $u_n$ にある。$s_0$ を最小の A 占有 $s\ge1$ とする。ν_A≥1 なので $s_0\le n-1$ である。

- **$b_n$ の場合：穴 (ca, b).**
  - F：$c_{s_0}<a''<c_{s_0+1}\le c_n<b^*$ で、4 文字とも印付き（M1, M2, M3）。W1 から W でも同順。$c_{s_0+1}$ が間にあるので、$b^*$ は後の W 区間にある。LG1 により hosting される。
  - Y：$n_T\ge2$、$\nu_A^T\ge1$。内側の A 占有を区間 1 に取り、その先頭に a、b を区間 $n_T\ge2$ に置く。間には $c_2$ がある。
- **$b_0$ の場合：穴 (b, ac).**
  - F：$b^*<c_1\le c_{s_0}<a''<c_{s_0+1}$（M3, M1, M2）。LG2 による。
  - Y：b を区間 0 に、区間 1 の末尾に a を置き、その後に $c_2$ が来る。
- 長射影：$\operatorname{req}(D_{ac})\subseteq\{A,B\}$、$\operatorname{req}(D_b)=\{B\}$。どちらも成分 i で長い。∎

### 3.2 補題 X（別根成分へ分ける）[PROVED]

**仮定.** d=2 とする。成分 i が $\nu_A\ge1$ を満たし、もう一方の成分 i′ が $N^B(bb)\ge1$ を満たす。さらに $D=D_{ac}+D_b$ で、$\pi_B(T_i)$ が長い（$n_T\ge2$）。

**結論.** $h_1\in\{ca,ac\}$ を成分 i に、$h_2=b$ を成分 i′ に置いて J が成り立つ。

*証明.*
- Y：成分ごとに独立に置ける。$\nu_A^T\ge1$ なので ca も ac も置ける。成分 i′ は b を含み、π_B が長い。
- F：W の順序は成分の順序である。
  - i<i′ なら (ca, b)：$c_{s_0}<a''<c_{s_0+1}<b^*$ で、$b^*$ は $x_{i'}$ の印付き b（M5）。LG1 による。
  - i′<i なら (b, ac)：$b^*<c_{s_0}<a''<c_{s_0+1}$。LG2 による。∎

### 3.3 補題 EO（端だけの成分）[PROVED]

**仮定.** 根成分 i が a,b,c を含み、$\nu_A=\nu_B=0$、$n\ge2$、$N^A(aa),N^B(bb)\ge c^*+1$ を満たす。D は $r=r'=0$ で、$D=(p\,aa+q\,cc,\ p'bb+q\,cc)$、$p,p',q>0$ とする。

**結論.** 成分 i に置く二穴で J が成り立つ。

ここで $x_i=u_0c^nu_n$ であり、$u_0,u_n\in\{a,b\}^*$ である。旗は次の四通りに尽きる。$a_0\wedge b_n$ でも $b_0\wedge a_n$ でもなければ、全文字が $u_0$ に入るか、全文字が $u_n$ に入る。

- **(E1) $a_0\wedge b_n$：穴 (a, cb)、分割 $(p\,aa,0)+(q\,cc,\ p'bb+q\,cc)$.**
  - F：$a^*<c_1<c_n<b^*$。$a^*$ は $u_0$ の最後の a で、ac 窓は唯一。$c_n,b^*$ は唯一の cb 窓。$c_1\ne c_n$ なので、$b^*$ の区間は $a^*$ の区間の 2 つ以上後になる。
  - Y：a を区間 0 に、b を区間 n の先頭に置く。
- **(E2) $b_0\wedge a_n$：鏡像で (b, ca).**
- **(E3) 全てが $u_0$ にある場合.** $|u_0|_a,|u_0|_b\ge c^*+2$。
  - $u_0$ が b で終わるなら、穴 (a, bc)。
    - F：$a_1$（M5）、$u_0$ の最後の b、$c_1$ が x で「a_1 …(a_2 を含む非空)… b c_1」と並ぶ。W でも**文字どおり**この形で現れる（W1）。
    - Y：区間 0 を「a a … b」とし、その後に $c_1$ が来る。
  - $u_0$ が a で終わるなら、鏡像で (b, ac)。
- **(E4) 全てが $u_n$ にある場合.** 反転して (ca, b) または (cb, a) を使う。
  - $c_n$ は唯一の ca 窓（または cb 窓）の端点である。
  - $u_n$ の 2 番目の b（または a）は最初の bb 窓の端点で、先頭から 2 以上離れている。

長射影は成分 i が a,b,c を含むことから成り立つ。∎

## 4. 定理 R の証明（残余の全場合）

$\mathcal R_{\rm open}$ の段では、全ての根成分が豊かでない。各 κ の型は $\{a,b,c,ac,bc,abcA,abcB\}$ のいずれかである（ab・abc+ は除外条件 (ii)、abc2 は豊かさを導く）。さらに $R(D)=\{a,b,c\}$ である（残余の全ての型の組がそうなる）。

### I. r′=0<r

κ_r（$r_\kappa>0$）の成分を i とすると、§2.5 から ν_A≥c\*、ν_B=0 である。
$D=D_{ac}+D_b$ と分ける。
- $D_{ac}=(p\,aa+q\,cc+r(ac{+}ca),\ m\,cc)$
- $D_b=(0,p'bb)$
- $r'=0$ なので $q'=m$、両者とも保存的
- $b\in R(D)$ と $r'=0$ から $p'>0$

場合分け：
- $b\in x_i$ なら補題 E。
- そうでなければ、bb を削る κ は他方の成分 i′ にあり、補題 X を使う。$\pi_B(T_i)=c^{n_T}$ で、$n_T\ge3$。

**これで A3（`abcA`：$r>0=r'$、$p=0<p'$）の単独と、r′=0 の型との組が全て片付く。** 同時に、A1 の r>0 の場合と、A2 の「$r_1>0=r'_2$」の場合も片付く。

### II. 鏡像

`abcB`、A1 の鏡像 {bc,a}、A2 の「$r'_2>0=r_1$」がここに入る。

### III. r,r′>0

- r>0 の κ は ν_A≥c\* の成分 $i_A$ にあり、その成分は ν_B=0 である。r′>0 の κ は成分 $i_B$ にあり、ν_A=0 である。豊かでないことから $i_A\ne i_B$、d=2 となる。
- r′>0 の各 κ は $r_\kappa=0$ なので、$q_\kappa=q'_\kappa+r'_\kappa\ge r'_\kappa$。和を取って $q\ge r'$。
- そこで次のように分ける。
  - $D_1=(p\,aa+(q-r')cc+r(ac{+}ca),\ q'cc)$
  - $D_2=(r'cc,\ p'bb+r'(bc{+}cb))$

  どちらも保存的で非零、$R(D_1)\subseteq\{a,c\}$、$R(D_2)\subseteq\{b,c\}$ である。
- $i_A<i_B$ の場合、穴は (ca, bc)。
  - F：$c_{s_0}<a''<c_{s_0+1}$（$x_{i_A}$）$<b'''<c_{t_0+1}$（$x_{i_B}$）。ここで $t_0$ は最小の B 占有 s<n で、$b'''$ はその区間の最後の b（M2 の鏡像）。
  - 補題G で、$a''$ を区間の先頭に、$b'''$ を区間の末尾に置く。
- $i_B<i_A$ の場合は (cb, ac)。
- Y：成分ごとに独立に置ける。長射影は、$i_A$ の π_B と $i_B$ の π_A がともに $c^{n}$（$n\ge3$）であることから成り立つ。

**A3 の「`abcA`＋`abcB`」「`abcA`＋bc（r′>0）」（別根）はここで片付く。**

### 0. r=r′=0

$D=(p\,aa+q\,cc,\ p'bb+q\,cc)$、$p,p',q>0$ である。この場合の残余の構成は、同根の次の三つだけである。
- {ac(r=0), b}
- {bc(r′=0), a}
- {ac(r=0), bc(r′=0)}

その成分 i は a,b,c を含み、$n\ge c^*+2$、$N^A(aa),N^B(bb)\ge c^*+1$ を満たす。豊かでないので ν_A=0 か ν_B=0 である。

- ν_A≥1、ν_B=0 なら補題 E（$D_{ac}=(p\,aa+q\,cc,\ q\,cc)$）。
- ν_B≥1、ν_A=0 なら鏡像（$D_a+D_{bc}$）。
- ν_A=ν_B=0 なら補題 EO。

**A1・A2 の r=0 の端場合はここで片付く。** ∎

### A4（ztype の網羅）

R(D) は次の三つで決まり、全 8 通りが `ztype` の a, b, c, ab, ac, bc, abc に対応する。
- $[p{+}r>0]$
- $[p'{+}r'>0]$
- $[m>0]$

abc はさらに次のように分かれ、互いに排反で全てを尽くす。
- abc+：$pp'>0$
- abc2：$rr'>0$、$pp'=0$
- abcA：$r>0=r'$、したがって $p'>0$、$p=0$
- abcB：鏡像

端の場合：
- $m=0$ ⇒ $r=r'=q=q'=0$（型 a, b, ab）。
- ac 型で $r=0$ ⇒ $p,q>0$。
- 片射影 0 は参加型（P1-d）で aa か bb だけになる。

**定理 R は型を使わず (r,r′) で分けるので、これらの端の場合も全て含む。**

## 5. 次の義務（この時点）

1. 有界検査：証明が指定する穴をそのまま構成して検証する「証明追従構成器」。`abcA/B` の意図的な生成、8 例の完全トレース、別実装の参照オラクル、失敗するべき対照。
2. 定理 R と同じ道具で、**豊かでない全ての段**（HC_I/II/III の引用部分）に J を独立に証明する（定理 N）。成功すれば HC の引用が不要になる。
3. §5.4 の長さの数え上げの修正（跳ばない一歩の色が相異なること）と、四分類の監査。
4. **`op:fanout-two` は OPEN のまま。** 原稿を変更する根拠にはならない。
END SOURCE claude_fanout2_round11_checkpoint1_2026-11-15.md

### Claude next obligations — `claude_fanout2_round11_next_obligations_2026-11-15.md`

BEGIN SOURCE claude_fanout2_round11_next_obligations_2026-11-15.md
# 第十一段 → 次段：残る義務（量化つき）

**日付**：2026-11-15 JST　／　**作成**：Claude（Opus 5.5）　／　**状態**：研究メモ・未査読
**正式問題**：`op:fanout-two` は OPEN。以下は全て特殊クラス U₂ の上界についての義務である。

本段の判定は **PROVED-U2（自己報告）** である。数学の残余はないが、**第三者監査と形式化**がまだない。そのため義務の中心は「監査」になる。

## 1. 第三者による独立監査（最優先）

量化はいずれも、G の型付き根最短木から作られる**全ての**貪欲 DFS 段（c\*=3、または固定の c\*≥3）である。

1. **補題 V（空虚性）.** ν_l=0 の成分で、l を含む η 成分は c を含まない（唯一の lc/cl 窓が印付きであることによる）。帰結として、豊かでない成分の κ の型は {a,b,c,ab,ac,bc} に限られる。
   - 特に点検すること：「`abc+` は豊かでない成分で m>0 になり得ない」という n≤2 の場合の議論。
2. **補題 M の M1〜M7.** 何番目の窓かの数え方。特に M7（$c_2,c_3$ に印が付くこと）。
3. **補題 LG の並べ替え.** 同じ区間か次の区間かの分岐と、隙間が非空であること。
4. **定理 N の場合分けが漏れないこと.**
   - (r,r′) と (p,p′,q) の全符号。
   - CA/CB/CC の交わり方。d≤2 なので互いに素にはならない。
   - 0e2 の「$x_{i_0}$ にある η 成分は一つだけ」という論拠：η の成分は ≤2 で、CC の κ は別の成分にある。
   - 0e2(ii) の Y 側：豊かな配置は仮定で除かれること。
5. **補題 L-ab（4 位置の議論）と補題 EO の E1〜E4.** 旗が四通りに尽きること。
6. **定理1・P0・H\*\*.** 第十段の証明。ChatGPT 監査は「中核は整合的」としたが、逐行の第三者監査はまだない。特に次の二点。
   - Y 側の穴を、削除が起きた成分と**別の**成分に置く使い方（P0 の総和形）。
   - 長射影の条件。
7. **長さの四分類と、修正した「跳ばない一歩 ≤C」.** 型付き高さ H≤49v、骨格、色数の評価。
8. 定数の取り直し（c\*≠3 のとき：52=8c\*d+2d、192=64c\*、768=256c\*）。

## 2. 形式化（推奨）

- 補題 V、M、LG、定理 N の場合分けは有限的で局所的なので、Lean 化に向いている。Γ の組合せ論と hosting の定義だけで閉じる。
- P1・B6・定理1 は導出木の操作を含むので、文法の形式化が先に要る。

## 3. 任意（数学的には不要になったもの）

- 型付き最短な実導出で、残余（同根 {ac,b}、ν_B=0）を実際に作る。補助文字なしで、Σ={a,b,c} を守ること。定理 N は一般の証明なので、作れなくても結論には影響しない。
- 第八段 `hc3_construct.py` を実導出の段に走らせる。NOT RUN のままで、本段の結論には不要である。

## 4. 原稿の扱い

- U₂ は特殊クラスの上界にすぎない。`op:fanout-two`（LG の外の失敗）の肯定も否定も与えない。
- 原稿 L2143 以降の「超多項式代表をもつ $U_1$-型付けの標的族」という道筋について、本族（重なる二射影、c_Σ）は**証人にならない**ことが分かった。他の族については何も言わない。
- **原稿・PDF・定理 A/B/C・`op:fanout-two` の変更は、監査が済むまで行わない。**
END SOURCE claude_fanout2_round11_next_obligations_2026-11-15.md

### Claude checker — `check_round11_residual_2026-11-15.py`

BEGIN SOURCE check_round11_residual_2026-11-15.py
#!/usr/bin/env python3
"""Round 11 (fan-out 2, rank 2, A={a,c}, B={b,c}, ell=2, s=c_Sigma): residual closure checker.
Python 3 standard library only.  Fixed seeds.

Needs, in the directory given by --src (default ../r10src):
  check_round10_HC_exhaustiveness_2026-11-14.py  (SHA256 aa316db6...; used for: the stage-model
      GENERATORS, the Gamma-level hosting oracle `hosts`/`host_comp`/`build_comp`, `expand`)
  check_round10_U2_integration_2026-11-14.py     (SHA256 d0b5cc90...; real round-9 derivations)
  check_round9_overlap_P1_B6_2026-11-14.py       (SHA256 c468f6ad...; imported by the above)
Run:  python3 -I check_round11_residual_2026-11-15.py [--src DIR] [--quick]
Final line ALL CHECKS PASSED (exit 0) iff every assertion holds.

What is NEW here (independent of round 10):
  [0] independent dat_ov / Gamma / marks; reference hosting oracle by BRUTE FORCE over all words
      of a dat class (len<=8), compared with the round-10 oracle on single holes, ordered pairs and
      2-component tuples.
  [1] the PROOF-FOLLOWING constructor prove_J: it does NOT search.  It follows the case split of the
      round-11 report (T5 for a rich component; otherwise Theorem N: cases III, I, II, 0a-0e, with
      Lemmas E, X, EO, L-ab, LG) and returns the holes, the split D=D_1+D_2, the component of each
      hole, the marked letters it relies on, and the LG pattern.  The checker then verifies:
        - every letter the proof calls "marked" is marked and lies outside every phi (Lemma M, W1);
        - the F-side word W* is BUILT from W by the LG rearrangement named in the proof (no oracle),
          dat_ov(W*) = dat_ov(W), holes literal, gaps >= 1;
        - the Y side: Gamma(T_i) hosts exactly the holes the proof assigns to component i, in order,
          with long projections for req(D_j);
        - Theorem 1 transfer: F[t] has dat = dat(W)+D, y^pi keeps per-component shat_2/content and
          total N2 = T + D.
  [2] Lemma V (vacuity): in a component with nu_l = 0, an eta component containing l contains no c.
      Consequently abcA/abcB/abc+ never occur in a non-rich component and same-root {ac,bc} is never
      non-rich.  Checked on every generated stage; control with c*=0 (no marks) must VIOLATE it.
  [3] the 8 round-10 R_open configurations, re-generated by re-running the round-10 driver with the
      same seed (stdout captured), with complete traces.
  [4] controls that MUST fail: e<=1 only; Lemma E with the wrong pattern; Lemma X with both holes in
      one component; long-projection condition dropped (H** shat_2 breaks); literal persistence of
      marked windows; c*=0 for Lemma V.
  [5] real derivations (round-9 grammars via the round-10 integration driver): prove_J on every
      nonzero actual stage, F via oracle (W positions not exposed there), Y and transfer verified.
"""
import sys, os, io, random, itertools, hashlib, importlib.util, contextlib, time
from collections import Counter

T0 = time.time()
ARGS = sys.argv[1:]
SRC = ARGS[ARGS.index('--src') + 1] if '--src' in ARGS else os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'r10src')
QUICK = '--quick' in ARGS
SHAS = {'check_round10_HC_exhaustiveness_2026-11-14.py': 'aa316db69814583cf02dc5338057f360916c6c6aa1be7f6e5e5c1224d6b0a2e2',
        'check_round10_U2_integration_2026-11-14.py': 'd0b5cc90fd050068aa0a4ed23d891ac1b4a1fb61a8b5f8c23498d21769e3689d',
        'check_round9_overlap_P1_B6_2026-11-14.py': 'c468f6ad5eb972b64803ca90de69a3b8c85beeedd21e9762363e89b83c78bde3'}
LOG = []
def log(*a):
    s = ' '.join(str(x) for x in a); LOG.append(s); print(s, flush=True)

for fn, sh in SHAS.items():
    assert hashlib.sha256(open(os.path.join(SRC, fn), 'rb').read()).hexdigest() == sh, fn
def load(name, fn):
    spec = importlib.util.spec_from_file_location(name, os.path.join(SRC, fn))
    m = importlib.util.module_from_spec(spec); sys.modules[name] = m; spec.loader.exec_module(m); return m
hc = load('hc10', 'check_round10_HC_exhaustiveness_2026-11-14.py')

# ============================================================ [0] independent primitives
A = frozenset('ac'); B = frozenset('bc'); PJ = (('A', A), ('B', B))
def proj(w, X): return ''.join(ch for ch in w if ch in X)
def shat(u): return ('w', u) if len(u) < 2 else ('ps', u[0], u[-1])
def N2(u):
    C = Counter()
    for i in range(len(u) - 1): C[u[i:i + 2]] += 1
    return C
def dat(w): return tuple((shat(proj(w, X)), tuple(sorted(N2(proj(w, X)).items()))) for _, X in PJ)
def gam(w):
    """(n, |a|, a0, an, nuA, |b|, b0, bn, nuB) -- written independently of round 10."""
    sg = w.split('c'); n = len(sg) - 1; out = [n]
    for L in 'ab':
        occ = [L in s for s in sg]; tot = w.count(L)
        if n == 0: out += [tot, tot > 0, tot > 0, 0]
        else: out += [tot, occ[0], occ[-1], sum(occ[1:-1])]
    return tuple(out)
def marks(x, cs):
    """positions of x that are endpoints of the first cs windows of each type, per projection."""
    M = set()
    for _, X in PJ:
        idx = [i for i, ch in enumerate(x) if ch in X]; seen = Counter()
        for p, q in zip(idx, idx[1:]):
            e = x[p] + x[q]; seen[e] += 1
            if seen[e] <= cs: M |= {p, q}
    return M
def nu(x, L):
    sg = x.split('c'); return sum(1 for s in sg[1:-1] if L in s) if len(sg) > 2 else 0
def rich(x): return x.count('c') >= 3 and nu(x, 'a') >= 1 and nu(x, 'b') >= 1
def cpos(x):
    return [i for i, ch in enumerate(x) if ch == 'c']   # c_k = cpos[k-1]
def segspan(x, s):
    cp = cpos(x); lo = 0 if s == 0 else cp[s - 1] + 1; hi = len(x) if s == len(cp) else cp[s]
    return lo, hi
def Rof(D):
    p, q, r, p2, q2, r2 = D; s = set()
    if p or r: s.add('a')
    if p2 or r2: s.add('b')
    if q + r: s.add('c')
    return frozenset(s)
def reqX(D):
    p, q, r, p2, q2, r2 = D
    return frozenset(x for x, nz in (('A', p or q or r), ('B', p2 or q2 or r2)) if nz)
def cons(D): return min(D) >= 0 and D[1] + D[2] == D[4] + D[5]
def longp(G): return frozenset(x for x, ok in (('A', G[0] + G[1] >= 2), ('B', G[0] + G[5] >= 2)) if ok)
SW = str.maketrans('ab', 'ba')
def swapD(D): return (D[3], D[4], D[5], D[0], D[1], D[2])
def swapG(G): return (G[0],) + tuple(G[5:9]) + tuple(G[1:5])

def sec0():
    byd = {}
    for n in range(1, 9):
        for p in itertools.product('abc', repeat=n):
            w = ''.join(p); byd.setdefault(dat(w), []).append(w)
    for d0, ws in byd.items():
        gs = {gam(w) for w in ws}; assert len(gs) == 1
        assert hc.gamma(ws[0]) == next(iter(gs))
    def lit(w, hs):
        def rec(j, st):
            if j == len(hs): return True
            p = w.find(hs[j], st)
            while p != -1:
                if rec(j + 1, p + len(hs[j]) + 1): return True
                p = w.find(hs[j], p + 1)
            return False
        return rec(0, 0)
    H1 = ['a', 'b', 'c', 'ab', 'ba', 'ac', 'ca', 'bc', 'cb', 'abc', 'bac', 'cab', 'cba', 'acb', 'bca', 'acc', 'cac']
    H2 = [(u, v) for u in ('a', 'b', 'c', 'ac', 'ca', 'bc', 'cb', 'ab', 'ba') for v in ('a', 'b', 'c', 'ac', 'ca', 'bc', 'cb', 'ab')]
    n1 = n2 = pos = 0
    small = [ws for ws in byd.values() if len(ws[0]) <= 7]
    for ws in small:
        G = gam(ws[0])
        for h in H1:
            br = any(lit(w, (h,)) for w in ws); assert br == hc.hosts((G,), (h,)), (ws[0], h); n1 += 1; pos += br
        for hp in H2:
            br = any(lit(w, hp) for w in ws); assert br == hc.hosts((G,), hp), (ws[0], hp); n2 += 1; pos += br
    # 2-component tuples: holes split across components (no gap needed across), random sample
    rng = random.Random(7); n3 = 0
    keys = [ws for ws in byd.values() if len(ws[0]) <= 5]
    for _ in range(4000):
        w1s, w2s = rng.choice(keys), rng.choice(keys)
        G = (gam(w1s[0]), gam(w2s[0])); hp = rng.choice(H2)
        br = False
        for k in range(3):   # k holes in comp 1, rest in comp 2
            left, right = hp[:k], hp[k:]
            if any(lit(u, left) for u in w1s) and any(lit(v, right) for v in w2s): br = True; break
        assert br == hc.hosts(G, hp), (w1s[0], w2s[0], hp); n3 += 1
    log('[0] independent dat/Gamma on all %d dat classes (len<=8) agree with round 10; reference BRUTE-FORCE hosting '
        '== round-10 oracle: %d single-hole + %d ordered-pair checks on %d classes (len<=7), %d positive; %d random '
        '2-component tuple checks' % (len(byd), n1, n2, len(small), pos, n3))

# ============================================================ LG constructive rearrangements (no oracle)
def segb(w, p):
    lo = w.rfind('c', 0, p) + 1; hi = w.find('c', p); hi = len(w) if hi == -1 else hi
    return lo, hi
def _remove(s, idxs):
    return ''.join(ch for k, ch in enumerate(s) if k not in idxs)
def LG1(w, c0, a0, b0):
    """(ca, b): c0<a0<b0, b0>=a0+2."""
    assert w[c0] == 'c' and w[a0] == 'a' and w[b0] == 'b' and c0 < a0 < b0 and b0 >= a0 + 2
    s, e = segb(w, a0)
    if b0 >= e:
        ns = 'a' + _remove(w[s:e], {a0 - s}); w2 = w[:s] + ns + w[e:]
        return w2, [('ca', s - 1), ('b', b0)]
    rest = _remove(w[s:e], {a0 - s, b0 - s}); assert rest
    ns = 'a' + rest[0] + 'b' + rest[1:]; return w[:s] + ns + w[e:], [('ca', s - 1), ('b', s + 2)]
def LG3(w, a0, b0):
    """(ac, b): c' = first c after a0, c' < b0, b0 >= c'+2."""
    assert w[a0] == 'a' and w[b0] == 'b'
    cp = w.index('c', a0); assert cp < b0 and b0 >= cp + 2
    s, e = segb(w, a0); assert e == cp
    w2 = w[:s] + _remove(w[s:e], {a0 - s}) + 'a' + w[e:]
    s2, e2 = segb(w2, b0)
    if s2 == cp + 1:
        rest = _remove(w2[s2:e2], {b0 - s2}); assert rest
        w2 = w2[:s2] + rest[0] + 'b' + rest[1:] + w2[e2:]; return w2, [('ac', cp - 1), ('b', s2 + 1)]
    return w2, [('ac', cp - 1), ('b', b0)]
def LG5(w, c0, a0, b0, c1):
    """(ca, bc): c0<a0<b0<c1, b0>=a0+2."""
    assert w[c0] == 'c' and w[a0] == 'a' and w[b0] == 'b' and w[c1] == 'c' and c0 < a0 < b0 < c1 and b0 >= a0 + 2
    s, e = segb(w, a0); s2, e2 = segb(w, b0)
    if s != s2:
        w2 = w[:s] + 'a' + _remove(w[s:e], {a0 - s}) + w[e:s2] + _remove(w[s2:e2], {b0 - s2}) + 'b' + w[e2:]
        return w2, [('ca', s - 1), ('bc', e2 - 1)]
    rest = _remove(w[s:e], {a0 - s, b0 - s}); assert rest
    return w[:s] + 'a' + rest + 'b' + w[e:], [('ca', s - 1), ('bc', e - 1)]
def LGca(w, c0, a0):
    assert w[c0] == 'c' and w[a0] == 'a' and c0 < a0
    s, e = segb(w, a0); return w[:s] + 'a' + _remove(w[s:e], {a0 - s}) + w[e:], [('ca', s - 1)]
def LGab(w, a0, b0):
    s, e = segb(w, a0); assert segb(w, b0) == (s, e)
    return w[:s] + 'ab' + _remove(w[s:e], {a0 - s, b0 - s}) + w[e:], [('ab', s)]
def LIT(w, *hs):
    return w, list(hs)
def transformed(fn, w, pos, rev=False, swap=False, extra=()):
    """apply fn on swapped and/or reversed coordinates, map the witness back."""
    L = len(w); w1 = w.translate(SW) if swap else w
    if rev: w1 = w1[::-1]; pos = [L - 1 - p for p in pos][::-1]
    w2, hs = fn(w1, *pos, *extra)
    if rev:
        w2 = w2[::-1]; hs = [(h[::-1], L - (st + len(h))) for h, st in hs][::-1]
    if swap: w2 = w2.translate(SW); hs = [(h.translate(SW), st) for h, st in hs]
    return w2, hs
PATTERN = {   # name -> (base function, rev, swap)
    '(ca,b)': (LG1, False, False), '(b,ac)': (LG1, True, False), '(cb,a)': (LG1, False, True), '(a,bc)': (LG1, True, True),
    '(ac,b)': (LG3, False, False), '(b,ca)': (LG3, True, False), '(bc,a)': (LG3, False, True), '(a,cb)': (LG3, True, True),
    '(ca,bc)': (LG5, False, False), '(cb,ac)': (LG5, False, True),
    '(ca)': (LGca, False, False), '(ac)': (LGca, True, False), '(cb)': (LGca, False, True), '(bc)': (LGca, True, True),
    '(ab)': (LGab, False, False),
}
def check_Fwit(W, w2, hs, holes):
    assert dat(w2) == dat(W), 'LG changed dat'
    assert [h for h, _ in hs] == list(holes), (hs, holes)
    for h, st in hs: assert w2[st:st + len(h)] == h, (w2, h, st)
    for (h1, s1), (h2, s2) in zip(hs, hs[1:]): assert s1 + len(h1) < s2, 'gap'

# ============================================================ the proof-following constructor
class Fail(Exception): pass
class Stage:
    def __init__(s, xs, layout, Zs, cs, GF, GY, W=None, pmap=None):
        s.xs = list(xs); s.layout = list(layout); s.Zs = list(Zs); s.cs = cs; s.GF = GF; s.GY = tuple(GY)
        s.W = W; s.pmap = pmap; s.M = [marks(x, cs) for x in s.xs]
        s.phi = [[(a, b) for (i, a, b) in s.layout if i == k] for k in range(len(s.xs))]
    def swapped(s):
        t = Stage([x.translate(SW) for x in s.xs], s.layout, [swapD(Z) for Z in s.Zs], s.cs, swapG(s.GF),
                  tuple(swapG(g) for g in s.GY), s.W.translate(SW) if s.W else None, s.pmap)
        return t
    def mk(s, i, p, letter):
        """the proof uses x_i[p] as a MARKED letter: assert marked, outside phi; return W position."""
        assert s.xs[i][p] == letter, (s.xs[i], p, letter)
        assert p in s.M[i], ('not marked', s.xs[i], p)
        assert not any(a <= p < b for a, b in s.phi[i]), 'marked letter inside phi'
        return s.pmap(i, p) if s.pmap else None
    def outside(s, i, p):
        assert not any(a <= p < b for a, b in s.phi[i]); return s.pmap(i, p) if s.pmap else None
    def comps_with(s, k):
        return [iv[0] for Z, iv in zip(s.Zs, s.layout) if Z[k] > 0]

def s0_of(x):   # least A-occupied segment s >= 1 (inner by nu_A>=1)
    sg = x.split('c'); return min(k for k in range(1, len(sg)) if 'a' in sg[k])
def first(x, L): return x.index(L)

def prove_J(st):
    """Return dict(label, holes, Ds, comp, pattern, pos) following the report's proof; raise Fail otherwise."""
    xs = st.xs; D = tuple(map(sum, zip(*st.Zs)))
    R = [k for k, x in enumerate(xs) if rich(x)]
    if R:                                   # ---- T5
        i = R[0]
        Fh = [h for h in ('abc', 'bac', 'cab', 'cba', 'acb', 'bca') if hc.hosts((st.GF,), (h,))]
        if not Fh: raise Fail('T5: F6 violated')
        return dict(label='T5', holes=(Fh[0],), Ds=(D,), comp=(i,), pattern=None, pos=None)
    p, q, r, p2, q2, r2 = D
    if r > 0 and r2 > 0:                    # ---- case III
        iA = st.comps_with(2)[0]; iB = st.comps_with(5)[0]
        if iA == iB: raise Fail('III: same component (would be rich)')
        assert q >= r2, 'q >= r\' (proof)'
        D1 = (p, q - r2, r, 0, q2, 0); D2 = (0, r2, 0, p2, 0, r2)
        xa, xb = xs[iA], xs[iB]; s0 = s0_of(xa); cpa = cpos(xa)
        c0 = st.mk(iA, cpa[s0 - 1], 'c'); lo, hi = segspan(xa, s0); a2 = st.mk(iA, max(k for k in range(lo, hi) if xa[k] == 'a'), 'a')
        sgb = xb.split('c'); t0 = min(k for k in range(len(sgb) - 1) if 'b' in sgb[k]); lo2, hi2 = segspan(xb, t0)
        b3 = st.mk(iB, max(k for k in range(lo2, hi2) if xb[k] == 'b'), 'b'); c1 = st.mk(iB, cpos(xb)[t0], 'c')
        if iA < iB:
            return dict(label='III', holes=('ca', 'bc'), Ds=(D1, D2), comp=(iA, iB), pattern='(ca,bc)', pos=(c0, a2, b3, c1))
        # (cb, ac): mirror with letters swapped -> positions c(of xb), b, a, c(of xa)
        sgb_ = xb.split('c'); s0b = min(k for k in range(1, len(sgb_)) if 'b' in sgb_[k]); lob, hib = segspan(xb, s0b)
        cb0 = st.mk(iB, cpos(xb)[s0b - 1], 'c'); bb = st.mk(iB, max(k for k in range(lob, hib) if xb[k] == 'b'), 'b')
        sga = xa.split('c'); ta = min(k for k in range(len(sga) - 1) if 'a' in sga[k]); loa, hia = segspan(xa, ta)
        aa_ = st.mk(iA, max(k for k in range(loa, hia) if xa[k] == 'a'), 'a'); ca1 = st.mk(iA, cpos(xa)[ta], 'c')
        return dict(label='III', holes=('cb', 'ac'), Ds=(D2, D1), comp=(iB, iA), pattern='(cb,ac)', pos=(cb0, bb, aa_, ca1))
    if r2 > 0 and r == 0:                   # ---- case II = mirror of I
        out = prove_J(st.swapped()); return unswap(out, 'II')
    if r > 0:                               # ---- case I
        i = st.comps_with(2)[0]; x = xs[i]
        if nu(x, 'b') != 0: raise Fail('I: nu_B != 0 (would be rich)')
        Dac = (p, q, r, 0, q2, 0); Db = (0, 0, 0, p2, 0, 0)
        s0 = s0_of(x); cp = cpos(x); lo, hi = segspan(x, s0)
        c0 = st.mk(i, cp[s0 - 1], 'c'); a2 = st.mk(i, max(k for k in range(lo, hi) if x[k] == 'a'), 'a')
        st.mk(i, cp[s0], 'c')
        if p2 == 0:
            return dict(label='I:single-ca', holes=('ca',), Ds=(D,), comp=(i,), pattern='(ca)', pos=(c0, a2))
        sg = x.split('c')
        if 'b' in sg[-1]:
            b = st.mk(i, cp[-1] + 1 + sg[-1].index('b'), 'b')
            return dict(label='I:LemmaE-bn', holes=('ca', 'b'), Ds=(Dac, Db), comp=(i, i), pattern='(ca,b)', pos=(c0, a2, b))
        if 'b' in sg[0]:
            b = st.mk(i, sg[0].rindex('b'), 'b'); c3 = st.pmap(i, cp[s0]) if st.pmap else None
            return dict(label='I:LemmaE-b0', holes=('b', 'ac'), Ds=(Db, Dac), comp=(i, i), pattern='(b,ac)', pos=(b, a2, c3))
        j = [k for k in st.comps_with(3) if k != i]
        if not j: raise Fail('I: no b anywhere')
        j = j[0]; bj = st.mk(j, first(xs[j], 'b'), 'b')
        if i < j:
            return dict(label='I:LemmaX', holes=('ca', 'b'), Ds=(Dac, Db), comp=(i, j), pattern='(ca,b)', pos=(c0, a2, bj))
        c3 = st.pmap(i, cp[s0]) if st.pmap else None
        return dict(label='I:LemmaX', holes=('b', 'ac'), Ds=(Db, Dac), comp=(j, i), pattern='(b,ac)', pos=(bj, a2, c3))
    # ---- case 0: r = r' = 0, so q = q2
    assert q == q2
    P, Pp, Q = p > 0, p2 > 0, q > 0
    Da = (p, 0, 0, 0, 0, 0); Db = (0, 0, 0, p2, 0, 0); Dc = (0, q, 0, 0, q, 0)
    if [P, Pp, Q].count(True) == 1:
        if P:
            i = st.comps_with(0)[0]; a = st.mk(i, first(xs[i], 'a'), 'a')
            return dict(label='0a:single', holes=('a',), Ds=(D,), comp=(i,), pattern='lit', pos=(('a', a),))
        if Pp:
            i = st.comps_with(3)[0]; b = st.mk(i, first(xs[i], 'b'), 'b')
            return dict(label='0a:single', holes=('b',), Ds=(D,), comp=(i,), pattern='lit', pos=(('b', b),))
        i = st.comps_with(1)[0]; c = st.mk(i, cpos(xs[i])[0], 'c')
        return dict(label='0a:single', holes=('c',), Ds=(D,), comp=(i,), pattern='lit', pos=(('c', c),))
    if P and Q and not Pp:
        ia = st.comps_with(0)[0]; ics = st.comps_with(1); ic = ia if ia in ics else ics[0]
        if ia != ic:
            a = st.mk(ia, first(xs[ia], 'a'), 'a'); c = st.mk(ic, cpos(xs[ic])[0], 'c')
            if ia < ic: return dict(label='0b:diff', holes=('a', 'c'), Ds=(Da, Dc), comp=(ia, ic), pattern='lit', pos=(('a', a), ('c', c)))
            return dict(label='0b:diff', holes=('c', 'a'), Ds=(Dc, Da), comp=(ic, ia), pattern='lit', pos=(('c', c), ('a', a)))
        x = xs[ia]; cp = cpos(x); fa = first(x, 'a'); s = x[:fa].count('c'); a = st.mk(ia, fa, 'a')
        if s == 0:
            c = st.mk(ia, cp[1], 'c'); return dict(label='0b:same', holes=('a', 'c'), Ds=(Da, Dc), comp=(ia, ia), pattern='lit', pos=(('a', a), ('c', c)))
        if s == 1:
            c = st.mk(ia, cp[2], 'c'); return dict(label='0b:same', holes=('a', 'c'), Ds=(Da, Dc), comp=(ia, ia), pattern='lit', pos=(('a', a), ('c', c)))
        c = st.mk(ia, cp[0], 'c'); return dict(label='0b:same', holes=('c', 'a'), Ds=(Dc, Da), comp=(ia, ia), pattern='lit', pos=(('c', c), ('a', a)))
    if Pp and Q and not P:
        return unswap(prove_J(st.swapped()), '0c')
    if P and Pp and not Q:
        ia = st.comps_with(0)[0]; ibs = st.comps_with(3); ib = ia if ia in ibs else ibs[0]
        if ia != ib:
            a = st.mk(ia, first(xs[ia], 'a'), 'a'); b = st.mk(ib, first(xs[ib], 'b'), 'b')
            if ia < ib: return dict(label='0d:diff', holes=('a', 'b'), Ds=(Da, Db), comp=(ia, ib), pattern='lit', pos=(('a', a), ('b', b)))
            return dict(label='0d:diff', holes=('b', 'a'), Ds=(Db, Da), comp=(ib, ia), pattern='lit', pos=(('b', b), ('a', a)))
        return L_ab(st, ia, Da, Db)
    # P, Pp, Q all positive
    CA, CB, CC = set(st.comps_with(0)), set(st.comps_with(3)), set(st.comps_with(1))
    if CA & CB & CC: return E_family(st, min(CA & CB & CC), D)
    if CA & CB: return case_e2(st, min(CA & CB), min(CC), D)
    if CA & CC: return case_e3(st, min(CA & CC), min(CB), D)
    if CB & CC: return unswap(prove_J(st.swapped()), '0e4')
    raise Fail('0e: pairwise disjoint component sets (impossible for d<=2)')

def unswap(out, tag):
    o = dict(out); o['label'] = tag + '[' + out['label'] + ']'
    o['holes'] = tuple(h.translate(SW) for h in out['holes']); o['Ds'] = tuple(swapD(Dx) for Dx in out['Ds'])
    o['swapped'] = not out.get('swapped', False); return o

def L_ab(st, i, Da, Db):
    x = st.xs[i]; ia = [k for k, ch in enumerate(x) if ch == 'a']; ib = [k for k, ch in enumerate(x) if ch == 'b']
    # first aa window of pi_A: consecutive a's with no c between
    pa = next((u, v) for u, v in zip(ia, ia[1:]) if 'c' not in x[u:v]); pb = next((u, v) for u, v in zip(ib, ib[1:]) if 'c' not in x[u:v])
    for u in pa:
        for v in pb:
            if abs(u - v) >= 2:
                st.mk(i, u, 'a'); st.mk(i, v, 'b')
                if u < v: return dict(label='0d:L-ab', holes=('a', 'b'), Ds=(Da, Db), comp=(i, i), pattern='lit', pos=(('a', st.outside(i, u)), ('b', st.outside(i, v))))
                return dict(label='0d:L-ab', holes=('b', 'a'), Ds=(Db, Da), comp=(i, i), pattern='lit', pos=(('b', st.outside(i, v)), ('a', st.outside(i, u))))
    raise Fail('L-ab: all four pairs adjacent (impossible)')

def E_family(st, i, D):
    """single component with a,b,c, n>=c*+2, N(aa),N(bb)>=c*+1, non-rich (case 0e1)."""
    p, q, r, p2, q2, r2 = D; x = st.xs[i]
    Dac = (p, q, 0, 0, q, 0); Db = (0, 0, 0, p2, 0, 0); Da = (p, 0, 0, 0, 0, 0); Dbc = (0, q, 0, p2, q, 0)
    na, nb = nu(x, 'a'), nu(x, 'b'); sg = x.split('c'); cp = cpos(x)
    if na >= 1 and nb >= 1: raise Fail('0e1: rich')
    if na >= 1:                      # Lemma E
        s0 = s0_of(x); lo, hi = segspan(x, s0)
        c0 = st.mk(i, cp[s0 - 1], 'c'); a2 = st.mk(i, max(k for k in range(lo, hi) if x[k] == 'a'), 'a'); c3 = st.mk(i, cp[s0], 'c')
        if 'b' in sg[-1]:
            b = st.mk(i, cp[-1] + 1 + sg[-1].index('b'), 'b')
            return dict(label='0e1:LemmaE-bn', holes=('ca', 'b'), Ds=(Dac, Db), comp=(i, i), pattern='(ca,b)', pos=(c0, a2, b))
        b = st.mk(i, sg[0].rindex('b'), 'b')
        return dict(label='0e1:LemmaE-b0', holes=('b', 'ac'), Ds=(Db, Dac), comp=(i, i), pattern='(b,ac)', pos=(b, a2, c3))
    if nb >= 1:
        return unswap(E_family(st.swapped(), i, swapD(D)), '0e1m')
    # Lemma EO: x = u0 c^n un
    a0, an, b0, bn = 'a' in sg[0], 'a' in sg[-1], 'b' in sg[0], 'b' in sg[-1]
    if a0 and bn:
        a = st.mk(i, sg[0].rindex('a'), 'a'); st.mk(i, cp[0], 'c'); cn = st.mk(i, cp[-1], 'c'); b = st.mk(i, cp[-1] + 1 + sg[-1].index('b'), 'b')
        return dict(label='0e1:EO1', holes=('a', 'cb'), Ds=(Da, Dbc), comp=(i, i), pattern='(a,cb)', pos=(a, b))
    if b0 and an:
        return unswap(E_family(st.swapped(), i, swapD(D)), '0e1m')
    if a0:                           # everything in u0
        u = sg[0]; c1 = st.mk(i, cp[0], 'c')
        if u[-1] == 'b':
            a = st.mk(i, u.index('a'), 'a'); b = st.mk(i, len(u) - 1, 'b'); assert b is None or b + 1 == c1
            return dict(label='0e1:EO3', holes=('a', 'bc'), Ds=(Da, Dbc), comp=(i, i), pattern='lit', pos=(('a', a), ('bc', b)))
        return unswap(E_family(st.swapped(), i, swapD(D)), '0e1m')
    u = sg[-1]; cn = st.mk(i, cp[-1], 'c')           # everything in un
    if u[0] == 'a':
        bs = [k for k, ch in enumerate(u) if ch == 'b']; b = st.mk(i, cp[-1] + 1 + bs[1], 'b')
        return dict(label='0e1:EO4', holes=('ca', 'b'), Ds=(Dac, Db), comp=(i, i), pattern='lit', pos=(('ca', cn), ('b', b)))
    return unswap(E_family(st.swapped(), i, swapD(D)), '0e1m')

def case_e2(st, i0, ic, D):
    p, q, r, p2, q2, r2 = D
    Dac = (p, q, 0, 0, q, 0); Db = (0, 0, 0, p2, 0, 0); Dab = (p, 0, 0, p2, 0, 0); Dc = (0, q, 0, 0, q, 0)
    xc = st.xs[ic]
    if 'a' in xc: return cross_ac(st, ic, i0, Dac, Db, '0e2:a-in-c-comp')
    if 'b' in xc: return unswap(prove_J(st.swapped()), '0e2m')
    x = st.xs[i0]; fa, fb = first(x, 'a'), first(x, 'b'); st.mk(i0, fa, 'a'); st.mk(i0, fb, 'b')
    if 'c' not in x[min(fa, fb):max(fa, fb)]:                    # (i) same segment
        cps = cpos(xc)
        if i0 < ic:
            c = st.mk(ic, cps[1], 'c')
            return dict(label='0e2:i-ab', holes=('ab', 'c'), Ds=(Dab, Dc), comp=(i0, ic), pattern='(ab)+c', pos=(st.outside(i0, fa), st.outside(i0, fb), c))
        c = st.mk(ic, cps[0], 'c')
        return dict(label='0e2:i-ab', holes=('c', 'ab'), Ds=(Dc, Dab), comp=(ic, i0), pattern='c+(ab)', pos=(c, st.outside(i0, fa), st.outside(i0, fb)))
    if fb < fa: return unswap(prove_J(st.swapped()), '0e2m')
    s = x[:fa].count('c'); t = x[:fb].count('c'); cp = cpos(x)            # (ii) a first
    aL = segspan(x, s)[1] - 1; assert x[aL] == 'a'
    for k in range(fb + 1): st.outside(i0, k)
    if t >= s + 2 or fb > cp[s] + 1:
        return dict(label='0e2:ii-ac,b', holes=('ac', 'b'), Ds=(Dac, Db), comp=(i0, i0), pattern='lit', pos=(('ac', st.outside(i0, aL)), ('b', st.outside(i0, fb))))
    return dict(label='0e2:ii-acb', holes=('acb',), Ds=(D,), comp=(i0,), pattern='lit', pos=(('acb', st.outside(i0, aL)),))

def cross_ac(st, ic, ib, Dac, Db, label):
    """h_ac in component ic (contains a and c, pi_B long), 'b' in component ib != ic."""
    x = st.xs[ic]; fa = first(x, 'a'); s = x[:fa].count('c'); cp = cpos(x)
    a = st.mk(ic, fa, 'a'); b = st.mk(ib, first(st.xs[ib], 'b'), 'b')
    if s >= 1:
        c = st.mk(ic, cp[s - 1], 'c')
        if ic < ib: return dict(label=label, holes=('ca', 'b'), Ds=(Dac, Db), comp=(ic, ib), pattern='(ca,b)', pos=(c, a, b))
        return dict(label=label, holes=('b', 'ca'), Ds=(Db, Dac), comp=(ib, ic), pattern='(b,ca)', pos=(b, a))
    c = st.mk(ic, cp[0], 'c')
    if ic < ib: return dict(label=label, holes=('ac', 'b'), Ds=(Dac, Db), comp=(ic, ib), pattern='(ac,b)', pos=(a, b))
    return dict(label=label, holes=('b', 'ac'), Ds=(Db, Dac), comp=(ib, ic), pattern='(b,ac)', pos=(b, a, c))

def case_e3(st, ia, ib, D):
    p, q, r, p2, q2, r2 = D
    return cross_ac(st, ia, ib, (p, q, 0, 0, q, 0), (0, 0, 0, p2, 0, 0), '0e3:cross')

# ------------------------------------------------------------ verification of a proof output
def build_F(st, out):
    W = st.W; pat = out['pattern']; pos = out['pos']
    if out.get('swapped'):
        pass
    if pat is None: return None
    if pat == 'lit':
        hs = [(h, p0) for h, p0 in pos]; return W, hs
    if pat == '(ab)+c':
        w2, hs = LGab(W, pos[0], pos[1]) if W[pos[0]] == 'a' else LGab(W, pos[1], pos[0]); return w2, hs + [('c', pos[2])]
    if pat == 'c+(ab)':
        w2, hs = LGab(W, pos[1], pos[2]) if W[pos[1]] == 'a' else LGab(W, pos[2], pos[1]); return w2, [('c', pos[0])] + hs
    fn, rv, sw = PATTERN[pat]
    return transformed(fn, W, list(pos), rev=rv, swap=sw)

def verify(st, out, D, stats, need_F_construct=True):
    holes, Ds, comp = out['holes'], out['Ds'], out['comp']
    assert 1 <= len(holes) <= 2 and len(holes) == len(Ds) == len(comp)
    tot = (0,) * 6
    for h, Dx in zip(holes, Ds):
        assert cons(Dx) and any(Dx) and Rof(Dx) <= set(h), (h, Dx); tot = tuple(u + v for u, v in zip(tot, Dx))
    assert tot == D, (tot, D)
    assert list(comp) == sorted(comp), 'hole order must follow component order'
    # F side
    if st.W is not None and need_F_construct and out['pattern'] is not None:
        Wst = st.W
        w2, hs = build_F(st, out) if not out.get('swapped') else build_F_sw(st, out)
        check_Fwit(st.W, w2, hs, holes); stats['F_constructed_LG'] += 1
        Fw, Fsp = w2, [(st0, st0 + len(h)) for h, st0 in hs]
    else:
        wf = hc.hosts((st.GF,), holes, want=True); assert wf, ('F oracle', out)
        Fw = wf[0][0]; Fsp = [(s0, s1) for _, s0, s1 in wf[1]]
        if st.W is not None: assert dat(Fw) == dat(st.W)
        stats['F_oracle'] += 1
    assert hc.hosts((st.GF,), holes), 'oracle disagrees with construction'
    # Y side: holes of component i in that component, in order, long projections
    ys = []; ysp = {}
    for i, G in enumerate(st.GY):
        hi = [j for j in range(len(holes)) if comp[j] == i]
        for j in hi: assert reqX(Ds[j]) <= longp(G), ('Y long', out['label'], holes[j], G)
        res = hc.host_comp(G, tuple(holes[j] for j in hi))
        assert res is not None, ('Y hosting', out['label'], G, holes, comp)
        al, be, sts = res; w, sp = hc.build_comp(al, be, [holes[j] for j in hi], sts)
        assert gam(w) == G
        for j, (a0, a1) in zip(hi, sp): assert w[a0:a1] == holes[j]; ysp[j] = (i, a0, a1)
        if len(hi) == 2: assert sp[0][1] < sp[1][0], 'Y gap'
        ys.append(w)
    # Theorem 1 transfer on the constructed words
    Ft = Fw
    for (s0, s1), h, Dx in sorted(zip(Fsp, holes, Ds), key=lambda z: -z[0][0]):
        Ft = Ft[:s0] + hc.expand(h, Dx) + Ft[s1:]
    for (Xn, X), k in zip(PJ, (0, 3)):
        d1 = N2(proj(Ft, X)); d1.subtract(N2(proj(Fw, X)))
        want = Counter({e: v for e, v in zip(('aa', 'cc', 'ac', 'ca') if Xn == 'A' else ('bb', 'cc', 'bc', 'cb'),
                                              (D[k], D[k + 1], D[k + 2], D[k + 2])) if v})
        assert +d1 == want and not -d1
        assert shat(proj(Ft, X)) == shat(proj(Fw, X))
    ypi = list(ys)
    for j in sorted(ysp, key=lambda j: (ysp[j][0], -ysp[j][1])):
        i, a0, a1 = ysp[j]; ypi[i] = ypi[i][:a0] + hc.expand(holes[j], Ds[j]) + ypi[i][a1:]
    for i in range(len(ys)):
        assert set(ypi[i]) == set(ys[i])
        for _, X in PJ: assert shat(proj(ypi[i], X)) == shat(proj(ys[i], X)), 'Y shat'
    for (Xn, X), k in zip(PJ, (0, 3)):
        t1 = Counter(); t0 = Counter()
        for i in range(len(ys)): t1 += N2(proj(ypi[i], X)); t0 += N2(proj(ys[i], X))
        t1.subtract(t0); assert sum(t1.values()) == D[k] + D[k + 1] + 2 * D[k + 2] and not -t1
    stats['verified'] += 1

def build_F_sw(st, out):
    """F construction for outputs produced on the swapped stage: rebuild in swapped coordinates."""
    o = dict(out); o['holes'] = tuple(h.translate(SW) for h in out['holes'])
    sst = Stage.__new__(Stage); sst.W = st.W.translate(SW)
    w2, hs = build_F(sst, o)
    return w2.translate(SW), [(h.translate(SW), s0) for h, s0 in hs]

# ============================================================ stage model driver
def lemmaV(st):
    """Lemma V: comp with nu_l = 0 => every phi containing l is c-free."""
    for (i, s, e) in st.layout:
        ph = st.xs[i][s:e]
        for L in 'ab':
            if nu(st.xs[i], L) == 0 and st.xs[i].count('c') >= 1 and L in ph and 'c' in ph: return False
    return True

def ztype(Z): return hc.ztype(Z)

def run_stage(xs, ctx, cs, layout, Zs, psis, Ts, stats, tag, traces=None, controls=True):
    d = len(xs); xp = []; offs = []
    for i, x in enumerate(xs):
        segs = []; pos = 0
        for kk, (ci, s, e) in sorted([(k, iv) for k, iv in enumerate(layout) if iv[0] == i], key=lambda t: t[1][1]):
            segs.append(x[pos:s]); segs.append(psis[kk]); pos = e
        segs.append(x[pos:]); xp.append(''.join(segs))
    W = ctx[0] + xp[0] + ctx[1] + (xp[1] + ctx[2] if d == 2 else '')
    base = [len(ctx[0]), len(ctx[0]) + len(xp[0]) + len(ctx[1])]
    def pmap(i, p):
        sh = 0
        for kk, (ci, s, e) in enumerate(layout):
            if ci == i and e <= p: sh += len(psis[kk]) - (e - s)
            assert not (ci == i and s <= p < e)
        q = base[i] + p + sh; assert W[q] == xs[i][p]; return q
    D = tuple(map(sum, zip(*Zs)))
    if not any(D): return
    if len(hc._HC) > 150000: hc._HC.clear()          # bound memory (cache only)
    if len(hc._SEQ) > 50000: hc._SEQ.clear()
    GF = gam(W); assert GF == hc.gamma(W)
    stV = Stage(xs, layout, Zs, cs, GF, ())
    stats['lemmaV_checked'] += 1
    if not lemmaV(stV): stats['lemmaV_VIOLATED'] += 1
    nonrich = not any(rich(x) for x in xs)
    for Z, (i, s, e) in zip(Zs, layout):
        if any(Z) and not rich(xs[i]):
            stats['nonrich_ztype:' + ztype(Z)] += 1
    cls = hc.classify(Zs, layout, xs)
    for T, GT in Ts:
        st = Stage(xs, layout, Zs, cs, GF, GT, W, pmap)
        stats['cases'] += 1; stats['cls:' + cls] += 1
        try:
            out = prove_J(st)
        except (Fail, AssertionError) as ex:
            stats['PROOF_FAIL'] += 1; log('  [PROOF FAIL]', tag, ex, xs, layout, Zs, psis, W, GT); continue
        stats['lab:' + out['label']] += 1
        stats['base:' + out['label'].split('[')[-1].rstrip(']')] += 1
        if cls.startswith('OPEN'): stats['open_lab:' + out['label']] += 1
        try:
            verify(st, out, D, stats)
        except AssertionError as ex:
            stats['VERIFY_FAIL'] += 1; log('  [VERIFY FAIL]', tag, repr(ex), out, xs, layout, Zs, psis, W, GT); continue
        if traces is not None and cls.startswith('OPEN'):
            traces.append((tag, xs, ctx, cs, layout, Zs, psis, W, GF, GT, T, out, cls))
        if controls:
            stats['ctl_e1_total'] += 1
            if hc.joint(GF, GT, D, emax=1) is None: stats['ctl_e1_FAILS'] += 1
            lab = out['label']
            if 'LemmaE-bn' in lab or 'LemmaE-b0' in lab:
                wrong = ('b', 'ac') if out['holes'] == ('ca', 'b') else ('ca', 'b')
                if out.get('swapped'): wrong = tuple(h.translate(SW) for h in wrong)
                i = out['comp'][0]; stats['ctl_wrongE_total'] += 1
                if not (hc.hosts((GF,), wrong) and hc.host_comp(GT[i], wrong) is not None): stats['ctl_wrongE_FAILS'] += 1
            if 'LemmaX' in lab:
                stats['ctl_X_onecomp_total'] += 1
                ok = all(hc.host_comp(GT[k], out['holes']) is not None and all(reqX(Dx) <= longp(GT[k]) for Dx in out['Ds']) for k in (out['comp'][0],))
                ok2 = all(hc.host_comp(GT[k], out['holes']) is not None and all(reqX(Dx) <= longp(GT[k]) for Dx in out['Ds']) for k in (out['comp'][1],))
                if not ok and not ok2: stats['ctl_X_onecomp_FAILS'] += 1

def gen_residual(rng):
    """root x with nu_B = 0, inner a-segments, b only at an end; phi1 deletes ac/ca or aa+cc, phi2 deletes bb."""
    while True:
        k = rng.randint(4, 9); inner = []
        for s in range(k):
            inner.append(rng.choice(['a', 'aa', 'a' * rng.randint(1, 5), '', '']))
        mid = 'c' + 'c'.join(inner) + 'c'
        end = rng.choice(['0', 'n', 'both'])
        u0 = ('a' * rng.randint(0, 2) + 'b' * rng.randint(5, 12)) if end in ('0', 'both') else 'a' * rng.randint(0, 3)
        un = ('b' * rng.randint(5, 12) + 'a' * rng.randint(0, 2)) if end in ('n', 'both') else 'a' * rng.randint(0, 3)
        if rng.random() < 0.3: u0 = ''.join(rng.sample(u0, len(u0)))
        x = u0 + mid + un
        if rng.random() < 0.5: x = x.translate(SW)
        if not rich(x): return x

def residual_stages(rng, x, cs, tries=40):
    """choose two unmarked factors: one with an A-transitional/aa+cc window, one with bb (or mirror)."""
    M = marks(x, cs)
    free = []
    s = 0
    while s < len(x):
        if s in M: s += 1; continue
        e = s
        while e < len(x) and e not in M: e += 1
        free.append((s, e)); s = e
    out = []
    for _ in range(tries):
        if len(free) < 1: break
        lay = []
        for _ in range(2):
            fs, fe = rng.choice(free); a = rng.randint(fs, fe - 1); b = rng.randint(a + 1, fe); lay.append((0, a, b))
        u, v = sorted(lay, key=lambda t: t[1])
        if not u[2] < v[1]: continue
        out.append((u, v))
    return out

def shape(rng, kind):
    """targeted root shapes for the branches of Theorem N."""
    mix = lambda k: ''.join(rng.choice('ab') for _ in range(k))
    if kind == 'Arich':     # nu_A >= 3, no b
        return rng.choice(['', 'a' * rng.randint(1, 3)]) + 'c' + 'c'.join(rng.choice(['a', 'aa', 'a', '', 'aaa']) for _ in range(rng.randint(7, 11))) + 'c' + rng.choice(['', 'a'])
    if kind == 'Arich_b':   # nu_A >= 3, b only at an end
        x = shape(rng, 'Arich'); return ('b' * rng.randint(5, 9) + x) if rng.random() < 0.5 else (x + 'b' * rng.randint(5, 9))
    if kind == 'abend':     # mixed a/b end segment, inner c-runs and optional inner a-segments
        inner = 'c'.join(rng.choice(['', '', 'a', 'aa'] if rng.random() < 0.6 else ['']) for _ in range(rng.randint(6, 10)))
        x = mix(rng.randint(14, 22)) + 'c' + inner + 'c' + rng.choice(['', 'b' * rng.randint(1, 5), 'a' * rng.randint(1, 5), mix(4)])
        return x if rng.random() < 0.5 else x[::-1]
    if kind == 'cc': return 'c' * rng.randint(7, 12)
    if kind == 'abmix': return mix(rng.randint(12, 20))
    if kind == 'bword': return rng.choice(['b' * rng.randint(6, 10), mix(rng.randint(10, 16)), 'b' * 5 + 'c' + 'b' * 5])
    if kind == 'Acc':       # a's in some inner segments plus long A-empty runs (types a, c, ac with r = 0)
        return 'a' * rng.randint(0, 6) + 'c' + 'c'.join(rng.choice(['', '', '', 'aaaaa', 'aaaaaa']) for _ in range(rng.randint(8, 12))) + 'c'
    raise ValueError(kind)
SHAPES1 = ['abend', 'Arich_b', 'Acc']
SHAPES2 = [('Arich', 'bword'), ('Arich', 'Arich'), ('abend', 'cc'), ('abmix', 'cc'), ('Acc', 'bword'), ('Acc', 'abmix'),
           ('abend', 'Acc'), ('abmix', 'Acc'), ('abend', 'bword'), ('Arich_b', 'cc')]

def main():
    log('== Round 11 residual-closure checker; seeds 20261115 (model), 20261114 (round-10 replay) ==')
    log('sources verified:', {k[:24]: v[:12] for k, v in SHAS.items()})
    sec0()
    rng = random.Random(20261115); stats = Counter(); traces = []
    # [1a] exhaustive d=1 roots |x|<=7 (round-10 generator, c*=3)
    for n in range(4, 8 if not QUICK else 6):
        for pp in itertools.product('abc', repeat=n):
            x = ''.join(pp)
            for layout, Zs, psis, Ts in hc.stage_iter([x], ('', ''), 3, rng, 6, 2, 1):
                run_stage([x], ('', ''), 3, layout, Zs, psis, Ts, stats, 'EXH', controls=False)
    log('[1a] exhaustive d=1 |x|<=7: cases=%d proof_fail=%d verify_fail=%d' % (stats['cases'], stats['PROOF_FAIL'], stats['VERIFY_FAIL']))
    K = 120 if QUICK else 400
    for it in range(K):        # [1b] random d in {1,2}
        d = rng.choice((1, 2)); cs = rng.choice((3, 3, 4))
        xs = [hc.gen_word(rng, rng.randint(14, 30 if d == 1 else 22)) for _ in range(d)]
        ctx = [''.join(rng.choice('abc') for _ in range(rng.randint(0, 2))) for _ in range(d + 1)]
        if d == 2 and not ctx[1]: ctx[1] = rng.choice('abc')
        for layout, Zs, psis, Ts in hc.stage_sample(xs, ctx, cs, rng, 10, 6, 2):
            run_stage(xs, ctx, cs, layout, Zs, psis, Ts, stats, 'RND%d' % it)
    for it in range(K * 3):    # [1c] sparse / non-rich (round-10 generators)
        d = rng.choice((1, 1, 2)); cs = rng.choice((3, 3, 4))
        xs = [hc.gen_sparse(rng) if rng.random() < 0.5 else hc.gen_nonrich(rng) for _ in range(d)]
        ctx = [''] * (d + 1) if rng.random() < 0.4 else [''.join(rng.choice('abc') for _ in range(rng.randint(0, 2))) for _ in range(d + 1)]
        if d == 2 and not ctx[1]: ctx[1] = rng.choice('abc')
        for layout, Zs, psis, Ts in hc.stage_sample(xs, ctx, cs, rng, 10, 6, 3):
            run_stage(xs, ctx, cs, layout, Zs, psis, Ts, stats, 'SPNR%d' % it)
    # [1d] TARGETED residual: same root, ac/b and mirror, many roots
    before = Counter(stats)
    for it in range(K * 4):
        x = gen_residual(rng); cs = 3
        for lay in residual_stages(rng, x, cs, 12):
            phis = [x[s:e] for _, s, e in lay]
            opts = [hc.z_options(ph, rng, 6) for ph in phis]
            for Zs in itertools.product(*opts):
                if not any(map(any, Zs)): continue
                ps = []
                for Z in Zs:
                    while True:
                        w = ''.join(rng.choice('abc') for _ in range(rng.randint(1, 4)))
                        if (Z[0] or Z[1] or Z[2]) and len(proj(w, A)) < 2: continue
                        if (Z[3] or Z[4] or Z[5]) and len(proj(w, B)) < 2: continue
                        break
                    ps.append(w)
                Zi = tuple(map(sum, zip(*Zs)))
                Ts = [(None, (g,)) for _, g in hc.T_options(x, Zi, cs, rng, 2)]
                ctx = ('', '') if rng.random() < 0.5 else (rng.choice('abc'), rng.choice(['', 'a', 'bc']))
                run_stage([x], ctx, cs, lay, Zs, ps, Ts, stats, 'RES%d' % it, traces)
    dd = stats - before
    log('[1d] targeted residual roots (nu_B=0 or mirror, inner a-runs, b-runs at an end): cases=%d, round-10 OPEN-class cases=%d'
        % (dd['cases'], sum(v for k, v in dd.items() if k.startswith('cls:OPEN'))))
    # [1e] TARGETED d=2 cross configurations (cases I-X, III, 0e2, 0e3)
    before = Counter(stats)
    for it in range(K * 4):
        cs = 3
        xs = [gen_residual(rng) if rng.random() < 0.6 else hc.gen_sparse(rng) for _ in range(2)]
        if rng.random() < 0.25: xs[rng.randrange(2)] = 'c' * rng.randint(7, 11)
        if rng.random() < 0.25: xs[rng.randrange(2)] = ''.join(rng.choice('ab') for _ in range(rng.randint(8, 14)))
        ctx = ['', rng.choice('abc'), '']
        for layout, Zs, psis, Ts in hc.stage_sample(xs, ctx, cs, rng, 12, 6, 2):
            run_stage(xs, ctx, cs, layout, Zs, psis, Ts, stats, 'X2_%d' % it)
    dd = stats - before
    log('[1e] targeted d=2 cross configurations: cases=%d' % dd['cases'])
    before = Counter(stats)
    for it in range(K * 5):           # [1f] branch-targeted shapes
        cs = 3
        if rng.random() < 0.35: xs = [shape(rng, rng.choice(SHAPES1))]
        else:
            k1, k2 = rng.choice(SHAPES2)
            if k1 == 'Arich' and k2 == 'Arich': xs = [shape(rng, 'Arich'), shape(rng, 'Arich').translate(SW)]
            else: xs = [shape(rng, k1), shape(rng, k2)]
            if rng.random() < 0.5: xs = [x.translate(SW) for x in xs]
            if rng.random() < 0.5: xs = xs[::-1]
        d = len(xs); ctx = [''] * (d + 1)
        if d == 2: ctx[1] = rng.choice('abc')
        for layout, Zs, psis, Ts in hc.stage_sample(xs, ctx, cs, rng, 14, 8, 2):
            run_stage(xs, ctx, cs, layout, Zs, psis, Ts, stats, 'SH%d' % it)
    dd = stats - before
    log('[1f] branch-targeted shapes: cases=%d' % dd['cases'])
    before = Counter(stats)
    for it in range(K * 2):           # [1g] end-only / E-family roots with eta placed in maximal free intervals        cs = 3; mix = lambda k: ''.join(rng.choice('ab') for _ in range(k))
        inner = 'c'.join(rng.choice(['', '', 'a', 'aa']) if rng.random() < 0.3 else '' for _ in range(rng.randint(7, 11)))
        x = mix(rng.randint(16, 24)) + 'c' + inner + 'c' + rng.choice(['', 'b' * rng.randint(2, 6), 'a' * rng.randint(2, 6), mix(rng.randint(3, 8))])
        if rng.random() < 0.5: x = x[::-1]
        if rng.random() < 0.5: x = x.translate(SW)
        if rich(x): continue
        M = marks(x, cs); free = []; q0 = 0
        while q0 < len(x):
            if q0 in M: q0 += 1; continue
            e0 = q0
            while e0 < len(x) and e0 not in M: e0 += 1
            free.append((0, q0, e0)); q0 = e0
        lays = [(u, v) for u, v in itertools.combinations(free, 2) if u[2] < v[1]]
        rng.shuffle(lays)
        for lay in lays[:6]:
            phis = [x[a:b] for _, a, b in lay]; opts = [hc.z_options(ph, rng, 8) for ph in phis]
            combos = [c for c in itertools.product(*opts) if any(map(any, c))]
            for Zs in rng.sample(combos, min(6, len(combos))):
                ps = []
                for Z in Zs:
                    while True:
                        w = ''.join(rng.choice('abc') for _ in range(rng.randint(1, 4)))
                        if (Z[0] or Z[1] or Z[2]) and len(proj(w, A)) < 2: continue
                        if (Z[3] or Z[4] or Z[5]) and len(proj(w, B)) < 2: continue
                        break
                    ps.append(w)
                Zi = tuple(map(sum, zip(*Zs)))
                Ts = [(None, (g,)) for _, g in hc.T_options(x, Zi, cs, rng, 2)]
                run_stage([x], ('', ''), cs, lay, Zs, ps, Ts, stats, 'EO%d' % it)
    dd = stats - before
    log('[1g] end-only / E-family roots, eta = maximal free intervals: cases=%d' % dd['cases'])
    before = Counter(stats)
    # [1h] deterministic stages for the rarest branch 0e2:ii-acb (and its mirror): x0 = a c b ..., x1 = c^9
    for x0 in ('acb' + 'aaaa' + 'bbbb' + 'aabbaabbaabb', 'acb' + 'aaaa' + 'bbbb' + 'abababababab'):
        for sw in (False, True):
            for order in (0, 1):
                xs = [x0, 'c' * 9]
                if sw: xs = [x.translate(SW) for x in xs]
                M0 = marks(xs[0], 3); f0 = max(M0) + 1
                lay = [(0, f0, len(xs[0])), (1, 4, 9)]
                if order: xs = xs[::-1]; lay = [(1, f0, len(xs[1])), (0, 4, 9)][::-1]; lay = [(0, 4, 9), (1, f0, len(xs[1]))]
                phis = [xs[i][a:b] for i, a, b in lay]
                opts = [[Z for Z in hc.z_options(ph) if any(Z)] for ph in phis]
                for Zs in itertools.islice(itertools.product(*opts), 0, 40, 3):
                    ps = ['aacbb' if any(Z[:3]) and any(Z[3:]) else ('aca' if any(Z[:3]) else 'bcb') for Z in Zs]
                    Ts_per = []
                    for i, x in enumerate(xs):
                        Zi = tuple(map(sum, zip(*[Z for Z, iv in zip(Zs, lay) if iv[0] == i]))) if any(iv[0] == i for iv in lay) else (0,) * 6
                        Ts_per.append(hc.T_options(x, Zi, 3, rng, 1))
                    Ts = [(tuple(t for t, _ in c), tuple(g for _, g in c)) for c in itertools.product(*Ts_per)]
                    run_stage(xs, ['', 'a', ''], 3, lay, Zs, ps, Ts, stats, 'DET')
    dd = stats - before
    log('[1h] deterministic stages for branch 0e2:ii-acb (both orders, a<->b mirror): cases=%d' % dd['cases'])
    log('[1] proof-following constructor on the stage model: cases=%d  PROOF_FAIL=%d  VERIFY_FAIL=%d  verified=%d '
        '(F built by the named LG rearrangement: %d; F by oracle: %d)'
        % (stats['cases'], stats['PROOF_FAIL'], stats['VERIFY_FAIL'], stats['verified'], stats['F_constructed_LG'], stats['F_oracle']))
    log('[1] cases per proof label (coverage; 0 = coverage missing):')
    LABELS = ['T5', 'III', 'I:single-ca', 'I:LemmaE-bn', 'I:LemmaE-b0', 'I:LemmaX', 'II[', '0a:single', '0b:diff', '0b:same',
              '0c[', '0d:diff', '0d:L-ab', '0e1:LemmaE-bn', '0e1:LemmaE-b0', '0e1m[', '0e1:EO1', '0e1:EO3', '0e1:EO4',
              '0e2:a-in-c-comp', '0e2m[', '0e2:i-ab', '0e2:ii-ac,b', '0e2:ii-acb', '0e3:cross', '0e4[']
    BASE = ['T5', 'III', 'I:single-ca', 'I:LemmaE-bn', 'I:LemmaE-b0', 'I:LemmaX', '0a:single', '0b:diff', '0b:same', '0d:diff',
            '0d:L-ab', '0e1:LemmaE-bn', '0e1:LemmaE-b0', '0e1:EO1', '0e1:EO3', '0e1:EO4', '0e2:a-in-c-comp', '0e2:i-ab',
            '0e2:ii-ac,b', '0e2:ii-acb', '0e3:cross']
    log('      (innermost proof branch, mirrors merged : cases ; outer wrappers II/0c/0e1m/0e2m/0e4 = a<->b mirror)')
    for L in BASE:
        v = stats['base:' + L]; log('      %-22s %7d%s' % (L, v, '' if v else '   <-- coverage missing'))
    log('      wrappers:', {k[4:]: v for k, v in sorted(stats.items()) if k.startswith('lab:') and '[' in k})
    log('[1] round-10 classes -> cases:', {k[4:]: v for k, v in sorted(stats.items()) if k.startswith('cls:')})
    log('[1] round-10 OPEN-class cases -> round-11 proof label:', {k[9:]: v for k, v in sorted(stats.items()) if k.startswith('open_lab:')})
    log('[2] Lemma V on every generated stage: checked=%d violated=%d' % (stats['lemmaV_checked'], stats['lemmaV_VIOLATED']))
    nr = {k[14:]: v for k, v in sorted(stats.items()) if k.startswith('nonrich_ztype:')}
    log('[2] ztype of nonzero kappa in NON-rich components:', nr)
    for t in ('abcA', 'abcB', 'abc+', 'abc2'):
        log('      %s in a non-rich component: %d  (%s)' % (t, nr.get(t, 0), 'coverage missing -- vacuous by Lemma V' if t != 'abc2' else 'vacuous: abc2 forces richness'))
    assert stats['lemmaV_VIOLATED'] == 0 and all(nr.get(t, 0) == 0 for t in ('abcA', 'abcB', 'abc+', 'abc2'))
    # [2'] control: c* = 0 (no marks) must violate Lemma V
    sV = Counter()
    for it in range(300):
        x = gen_residual(rng)
        for lay in residual_stages(rng, x, 0, 6):
            st = Stage([x], lay, [(0,) * 6, (0,) * 6], 0, gam(x), ())
            sV['n'] += 1; sV['viol'] += (not lemmaV(st))
    log("[2'] control c*=0 (no marks): Lemma V violated on %d of %d layouts (MUST be > 0: marks are what make abcA etc. vacuous)" % (sV['viol'], sV['n']))
    assert sV['viol'] > 0
    # [3] replay round 10 and capture the R_open configurations
    cap = []
    orig_run = hc.run_config
    def spy(xs, ctx, cstar, layout, Zs, psis, Ts, st_, fails, tag, controls=True):
        if hc.classify(Zs, layout, xs).startswith('OPEN'): cap.append((xs, ctx, cstar, layout, Zs, psis, Ts, tag))
        return orig_run(xs, ctx, cstar, layout, Zs, psis, Ts, st_, fails, tag, controls)
    hc.run_config = spy; old = sys.argv; sys.argv = ['x', '--rand', '400']
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf): hc.main()
    sys.argv = old; hc.run_config = orig_run
    r10out = buf.getvalue()
    assert 'ALL CHECKS PASSED' in r10out and 'cls:OPEN:ac/b:same\': 5' in r10out and 'cls:OPEN:a/bc:same\': 3' in r10out
    ncfg = sum(len(c[6]) for c in cap)
    log('[3] round-10 driver replayed (seed 20261114, --rand 400): ALL CHECKS PASSED reproduced; captured %d OPEN configurations (%d with their T states)'
        % (len(cap), ncfg))
    s3 = Counter(); k = 0
    for xs, ctx, cs, layout, Zs, psis, Ts, tag in cap:
        d = len(xs); D = tuple(map(sum, zip(*Zs)))
        for T, GT in Ts:
            k += 1
            xp = []
            for i, x in enumerate(xs):
                segs = []; pos = 0
                for kk, (ci, s, e) in sorted([(kk, iv) for kk, iv in enumerate(layout) if iv[0] == i], key=lambda t: t[1][1]):
                    segs.append(x[pos:s]); segs.append(psis[kk]); pos = e
                segs.append(x[pos:]); xp.append(''.join(segs))
            W = ctx[0] + xp[0] + ctx[1] + (xp[1] + ctx[2] if d == 2 else '')
            base = [len(ctx[0]), len(ctx[0]) + len(xp[0]) + len(ctx[1])]
            def pmap(i, p, layout=layout, psis=psis, base=base, W=W, xs=xs):
                sh = sum(len(psis[kk]) - (e - s) for kk, (ci, s, e) in enumerate(layout) if ci == i and e <= p); return base[i] + p + sh
            st = Stage(xs, layout, Zs, cs, gam(W), GT, W, pmap)
            out = prove_J(st); verify(st, out, D, s3)
            Sst = []
            for i, x in enumerate(xs):
                N0 = {Xn: N2(proj(x, X)) for Xn, X in PJ}
                Sst.append({Xn: dict(N0[Xn]) for Xn in N0})
            w2, hs = (build_F(st, out) if not out.get('swapped') else build_F_sw(st, out))
            log('  --- R_open #%d (%s, class %s) ---' % (k, tag, hc.classify(Zs, layout, xs)))
            log('     x=%s ctx=%s c*=%d  Gamma(x)=%s  nu_A=%s nu_B=%s rich=%s' % (xs, ctx, cs, [gam(x) for x in xs], [nu(x, 'a') for x in xs], [nu(x, 'b') for x in xs], [rich(x) for x in xs]))
            log('     phi=%s  Z_kappa=%s  ztypes=%s  psi^(j\')=%s' % ([xs[i][s:e] for i, s, e in layout], Zs, [ztype(Z) if any(Z) else '0' for Z in Zs], psis))
            log('     original counts N0 = N2(pi_X x_i) (the model takes S between N0 and T): %s' % Sst)
            log('     state T (after) = %s ; Gamma(T)=%s' % ([{Xn: (T[i][Xn][0], dict(T[i][Xn][1])) for Xn in ('A', 'B')} for i in range(d)], GT))
            log('     W_j\'=%s  Gamma(W_j\')=%s' % (W, gam(W)))
            log('     round-11 proof: label=%s holes=%s split=%s components=%s pattern=%s' % (out['label'], out['holes'], out['Ds'], out['comp'], out['pattern']))
            log('     F witness (built by %s): %s  hole spans=%s' % (out['pattern'], w2, hs))
            Ft = w2
            for (h, s0), Dx in sorted(zip(hs, out['Ds']), key=lambda z: -z[0][1]): Ft = Ft[:s0] + hc.expand(h, Dx) + Ft[s0 + len(h):]
            log('     F[t]=%s  dat(F[t])-dat(F[h]) = D: verified; e=1 possible (round-10 search): %s' % (Ft, hc.joint(gam(W), GT, D, emax=1) is not None))
    log('[3] all %d R_open configurations: proof label/holes reproduced and fully verified (%d)' % (k, s3['verified']))
    assert k == 8 and s3['verified'] == 8
    # [4] controls summary
    log('[4] controls (MUST fail somewhere):')
    log('      e<=1 only                                : fails on %d of %d cases' % (stats['ctl_e1_FAILS'], stats['ctl_e1_total']))
    log('      Lemma E with the other pattern            : fails on %d of %d cases' % (stats['ctl_wrongE_FAILS'], stats['ctl_wrongE_total']))
    log('      Lemma X with both holes in one component  : fails on %d of %d cases' % (stats['ctl_X_onecomp_FAILS'], stats['ctl_X_onecomp_total']))
    assert stats['ctl_e1_FAILS'] > 0 and stats['ctl_wrongE_FAILS'] > 0 and stats['ctl_X_onecomp_FAILS'] > 0
    # long-projection condition dropped: H** in a component whose pi_B has length 1
    y = 'ab'; t = hc.expand('b', (0, 0, 0, 1, 0, 0))
    broke = shat(proj(y.replace('b', t), B)) != shat(proj(y, B))
    log('      long projection dropped (y_i=ab, hole b, D_B=bb): shat_2(pi_B) %s -> %s : %s' % (shat(proj(y, B)), shat(proj(y.replace('b', t), B)), 'BROKEN (detected)' if broke else 'not broken'))
    assert broke
    # literal persistence of marked windows: count marked windows of x not literally windows of W
    lost = 0; tot = 0; rr = random.Random(5)
    for it in range(400):
        x = hc.gen_word(rr, rr.randint(14, 26)); M = marks(x, 3)
        for lay, Zs, psis, Ts in hc.stage_sample([x], ('', ''), 3, rr, 4, 2, 1):
            W = ''; pos = 0; mp = {}
            for (ci, s, e), ps in sorted(zip(lay, psis), key=lambda t: t[0][1]):
                for k2 in range(pos, s): mp[k2] = len(W) + k2 - pos
                W += x[pos:s] + ps; pos = e
            for k2 in range(pos, len(x)): mp[k2] = len(W) + k2 - pos
            W += x[pos:]
            for _, X in PJ:
                idx = [i for i, ch in enumerate(x) if ch in X]; seen = Counter()
                for p0, q0 in zip(idx, idx[1:]):
                    e = x[p0] + x[q0]; seen[e] += 1
                    if seen[e] <= 3:
                        tot += 1
                        if proj(W[mp[p0]:mp[q0] + 1], X) != x[p0] + x[q0]: lost += 1
            break
    log('      "marked windows persist literally in W"   : false for %d of %d marked windows (only marked LETTERS are used)' % (lost, tot))
    assert lost > 0
    # [5] real derivations
    s5 = Counter()
    if not QUICK:
        ri = load('r10int', 'check_round10_U2_integration_2026-11-14.py')
        r9 = sys.modules['r9'] if 'r9' in sys.modules else ri.r9
        cur = {}
        orig_ri = ri.run_instance
        def run_inst(inst, fam, typed_min, Lmem, rng_, show):
            cur['cs'] = inst.cstar; cur['fam'] = fam; return orig_ri(inst, fam, typed_min, Lmem, rng_, show)
        orig_cls = ri.hc.classify
        def cls_spy(Zs, layout, xs=None):
            if xs is not None: cur['xs'] = list(xs); cur['layout'] = list(layout); cur['Zs'] = list(Zs)
            return orig_cls(Zs, layout, xs)
        orig_joint = ri.hc.joint
        def joint_spy(GF, GY, D, emax=2, merge=True, perkappa=None):
            res = orig_joint(GF, GY, D, emax, merge, perkappa)
            if emax == 2 and merge and 'xs' in cur:
                st = Stage(cur['xs'], cur['layout'], cur['Zs'], cur['cs'], GF, GY)
                try:
                    out = prove_J(st); verify(st, out, D, s5, need_F_construct=False); s5['lab:' + out['label']] += 1
                except (Fail, AssertionError) as ex:
                    s5['FAIL'] += 1; log('  [REAL FAIL]', cur['fam'], repr(ex))
                s5['cls:' + orig_cls(cur['Zs'], cur['layout'], cur['xs'])] += 1
                del cur['xs']
            return res
        ri.run_instance = run_inst; ri.hc.classify = cls_spy; ri.hc.joint = joint_spy
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf): ri.main()
        assert 'ALL CHECKS PASSED' in buf.getvalue()
        log('[5] real round-9 derivations (round-10 integration driver replayed, its own checks PASSED): nonzero stages run through prove_J=%d, verified=%d, FAIL=%d'
            % (s5['verified'] + s5['FAIL'], s5['verified'], s5['FAIL']))
        log('      labels:', {k[4:]: v for k, v in sorted(s5.items()) if k.startswith('lab:')})
        log('      round-10 classes:', {k[4:]: v for k, v in sorted(s5.items()) if k.startswith('cls:')})
        assert s5['FAIL'] == 0 and s5['verified'] == 475
    ok = stats['PROOF_FAIL'] == 0 and stats['VERIFY_FAIL'] == 0
    log('time %.1fs' % (time.time() - T0))
    log('ALL CHECKS PASSED' if ok else 'FAILURES (see above)')
    if not ok: sys.exit(1)

if __name__ == '__main__':
    main()
END SOURCE check_round11_residual_2026-11-15.py

### Claude submitted log — `out_check_round11_residual_2026-11-15.txt`

BEGIN SOURCE out_check_round11_residual_2026-11-15.txt
== Round 11 residual-closure checker; seeds 20261115 (model), 20261114 (round-10 replay) ==
sources verified: {'check_round10_HC_exhaust': 'aa316db69814', 'check_round10_U2_integra': 'd0b5cc90fd05', 'check_round9_overlap_P1_': 'c468f6ad5eb9'}
[0] independent dat/Gamma on all 1558 dat classes (len<=8) agree with round 10; reference BRUTE-FORCE hosting == round-10 oracle: 14297 single-hole + 60552 ordered-pair checks on 841 classes (len<=7), 21558 positive; 4000 random 2-component tuple checks
[1a] exhaustive d=1 |x|<=7: cases=93 proof_fail=0 verify_fail=0
[1d] targeted residual roots (nu_B=0 or mirror, inner a-runs, b-runs at an end): cases=25503, round-10 OPEN-class cases=553
[1e] targeted d=2 cross configurations: cases=47368
[1f] branch-targeted shapes: cases=81673
[1g] end-only / E-family roots, eta = maximal free intervals: cases=25554
[1h] deterministic stages for branch 0e2:ii-acb (both orders, a<->b mirror): cases=695
[1] proof-following constructor on the stage model: cases=193945  PROOF_FAIL=0  VERIFY_FAIL=0  verified=193945 (F built by the named LG rearrangement: 181873; F by oracle: 12072)
[1] cases per proof label (coverage; 0 = coverage missing):
      (innermost proof branch, mirrors merged : cases ; outer wrappers II/0c/0e1m/0e2m/0e4 = a<->b mirror)
      T5                       12072
      III                         50
      I:single-ca              10720
      I:LemmaE-bn                596
      I:LemmaE-b0                313
      I:LemmaX                   520
      0a:single               136185
      0b:diff                   4443
      0b:same                   6803
      0d:diff                   2571
      0d:L-ab                  16263
      0e1:LemmaE-bn              948
      0e1:LemmaE-b0              233
      0e1:EO1                    883
      0e1:EO3                    152
      0e1:EO4                    132
      0e2:a-in-c-comp             74
      0e2:i-ab                   514
      0e2:ii-ac,b                 44
      0e2:ii-acb                 396
      0e3:cross                   33
      wrappers: {'0c[0b:diff]': 2424, '0c[0b:same]': 3198, '0e1m[0e1:EO1]': 280, '0e1m[0e1:EO3]': 77, '0e1m[0e1:EO4]': 94, '0e1m[0e1:LemmaE-b0]': 90, '0e1m[0e1:LemmaE-bn]': 461, '0e2m[0e2:a-in-c-comp]': 16, '0e2m[0e2:ii-ac,b]': 7, '0e2m[0e2:ii-acb]': 223, '0e4[0e3:cross]': 12, 'II[I:LemmaE-b0]': 139, 'II[I:LemmaE-bn]': 284, 'II[I:LemmaX]': 237, 'II[I:single-ca]': 4950}
[1] round-10 classes -> cases: {'CITED-HC_I/II/III': 15740, 'OPEN:a/bc:same': 385, 'OPEN:ac/b:same': 453, 'PROVED:T1-single-a': 52042, 'PROVED:T1-single-ac': 6317, 'PROVED:T1-single-b': 49760, 'PROVED:T1-single-bc': 5151, 'PROVED:T1-single-c': 24762, 'PROVED:T2-letter-pair': 15710, 'PROVED:T3-merge': 10915, 'PROVED:T4-transitional-diff-root': 638, 'PROVED:T5-rich-component': 12072}
[1] round-10 OPEN-class cases -> round-11 proof label: {'0e1:LemmaE-b0': 4, '0e1m[0e1:LemmaE-b0]': 14, '0e1m[0e1:LemmaE-bn]': 10, 'I:LemmaE-b0': 171, 'I:LemmaE-bn': 278, 'II[I:LemmaE-b0]': 107, 'II[I:LemmaE-bn]': 254}
[2] Lemma V on every generated stage: checked=86267 violated=0
[2] ztype of nonzero kappa in NON-rich components: {'a': 36595, 'ab': 7872, 'ac': 4422, 'b': 33793, 'bc': 2889, 'c': 14375}
      abcA in a non-rich component: 0  (coverage missing -- vacuous by Lemma V)
      abcB in a non-rich component: 0  (coverage missing -- vacuous by Lemma V)
      abc+ in a non-rich component: 0  (coverage missing -- vacuous by Lemma V)
      abc2 in a non-rich component: 0  (vacuous: abc2 forces richness)
[2'] control c*=0 (no marks): Lemma V violated on 321 of 778 layouts (MUST be > 0: marks are what make abcA etc. vacuous)
[3] round-10 driver replayed (seed 20261114, --rand 400): ALL CHECKS PASSED reproduced; captured 6 OPEN configurations (8 with their T states)
  --- R_open #1 (NR377, class OPEN:ac/b:same) ---
     x=['abbbbbbbbcaaaacccaccaaccac'] ctx=['', ''] c*=3  Gamma(x)=[(9, 9, True, False, 4, 8, True, False, 0)]  nu_A=[4] nu_B=[0] rich=[False]
     phi=['bbb', 'cac']  Z_kappa=((0, 0, 0, 1, 0, 0), (0, 0, 1, 0, 1, 0))  ztypes=['b', 'ac']  psi^(j')=['ccaa', 'bbcc']
     original counts N0 = N2(pi_X x_i) (the model takes S between N0 and T): [{'A': {'ac': 5, 'ca': 4, 'aa': 4, 'cc': 4}, 'B': {'bb': 7, 'bc': 1, 'cc': 8}}]
     state T (after) = [{'A': (('ps', 'a', 'c'), {'aa': 4, 'ac': 4, 'ca': 3, 'cc': 4}), 'B': (('ps', 'b', 'c'), {'bb': 6, 'bc': 1, 'cc': 7})}] ; Gamma(T)=((8, 8, True, False, 3, 7, True, False, 0),)
     W_j'=abbbbccaabcaaaacccaccaacbbcc  Gamma(W_j')=(11, 10, True, False, 4, 7, True, False, 2)
     round-11 proof: label=I:LemmaE-b0 holes=('b', 'ac') split=((0, 0, 0, 1, 0, 0), (0, 0, 1, 0, 1, 0)) components=(0, 0) pattern=(b,ac)
     F witness (built by (b,ac)): abbbbccaabcaaaacccaccaacbbcc  hole spans=[('b', 9), ('ac', 14)]
     F[t]=abbbbccaabbcaaaacacccaccaacbbcc  dat(F[t])-dat(F[h]) = D: verified; e=1 possible (round-10 search): True
  --- R_open #2 (NR377, class OPEN:ac/b:same) ---
     x=['abbbbbbbbcaaaacccaccaaccac'] ctx=['', ''] c*=3  Gamma(x)=[(9, 9, True, False, 4, 8, True, False, 0)]  nu_A=[4] nu_B=[0] rich=[False]
     phi=['bbb', 'cac']  Z_kappa=((0, 0, 0, 2, 0, 0), (0, 0, 1, 0, 1, 0))  ztypes=['b', 'ac']  psi^(j')=['cacb', 'bbac']
     original counts N0 = N2(pi_X x_i) (the model takes S between N0 and T): [{'A': {'ac': 5, 'ca': 4, 'aa': 4, 'cc': 4}, 'B': {'bb': 7, 'bc': 1, 'cc': 8}}]
     state T (after) = [{'A': (('ps', 'a', 'c'), {'aa': 4, 'ac': 4, 'ca': 3, 'cc': 4}), 'B': (('ps', 'b', 'c'), {'bb': 5, 'bc': 1, 'cc': 7})}] ; Gamma(T)=((8, 8, True, False, 3, 6, True, False, 0),)
     W_j'=abbbbcacbbcaaaacccaccaacbbac  Gamma(W_j')=(10, 10, True, False, 5, 8, True, False, 2)
     round-11 proof: label=I:LemmaE-b0 holes=('b', 'ac') split=((0, 0, 0, 2, 0, 0), (0, 0, 1, 0, 1, 0)) components=(0, 0) pattern=(b,ac)
     F witness (built by (b,ac)): abbbbcacbbcaaaacccaccaacbbac  hole spans=[('b', 9), ('ac', 14)]
     F[t]=abbbbcacbbbbcaaaacacccaccaacbbac  dat(F[t])-dat(F[h]) = D: verified; e=1 possible (round-10 search): True
  --- R_open #3 (NR377, class OPEN:ac/b:same) ---
     x=['abbbbbbbbcaaaacccaccaaccac'] ctx=['', ''] c*=3  Gamma(x)=[(9, 9, True, False, 4, 8, True, False, 0)]  nu_A=[4] nu_B=[0] rich=[False]
     phi=['bbb', 'cac']  Z_kappa=((0, 0, 0, 2, 0, 0), (0, 0, 1, 0, 1, 0))  ztypes=['b', 'ac']  psi^(j')=['cacb', 'bbac']
     original counts N0 = N2(pi_X x_i) (the model takes S between N0 and T): [{'A': {'ac': 5, 'ca': 4, 'aa': 4, 'cc': 4}, 'B': {'bb': 7, 'bc': 1, 'cc': 8}}]
     state T (after) = [{'A': (('ps', 'a', 'c'), {'aa': 4, 'ac': 4, 'ca': 3, 'cc': 3}), 'B': (('ps', 'b', 'c'), {'bb': 5, 'bc': 1, 'cc': 6})}] ; Gamma(T)=((7, 8, True, False, 3, 6, True, False, 0),)
     W_j'=abbbbcacbbcaaaacccaccaacbbac  Gamma(W_j')=(10, 10, True, False, 5, 8, True, False, 2)
     round-11 proof: label=I:LemmaE-b0 holes=('b', 'ac') split=((0, 0, 0, 2, 0, 0), (0, 0, 1, 0, 1, 0)) components=(0, 0) pattern=(b,ac)
     F witness (built by (b,ac)): abbbbcacbbcaaaacccaccaacbbac  hole spans=[('b', 9), ('ac', 14)]
     F[t]=abbbbcacbbbbcaaaacacccaccaacbbac  dat(F[t])-dat(F[h]) = D: verified; e=1 possible (round-10 search): True
  --- R_open #4 (NR548, class OPEN:ac/b:same) ---
     x=['bbbbbbbcacacaaccacacaac', 'bbb'] ctx=['c', 'ca', 'a'] c*=3  Gamma(x)=[(8, 8, False, False, 6, 7, True, False, 0), (0, 0, False, False, 0, 3, True, True, 0)]  nu_A=[6, 0] nu_B=[0, 0] rich=[False, False]
     phi=['bb', 'cac']  Z_kappa=((0, 0, 0, 1, 0, 0), (0, 0, 1, 0, 1, 0))  ztypes=['b', 'ac']  psi^(j')=['bbb', 'cba']
     original counts N0 = N2(pi_X x_i) (the model takes S between N0 and T): [{'A': {'ca': 6, 'ac': 6, 'aa': 2, 'cc': 1}, 'B': {'bb': 6, 'bc': 1, 'cc': 7}}, {'A': {}, 'B': {'bb': 2}}]
     state T (after) = [{'A': (('ps', 'c', 'c'), {'aa': 2, 'ac': 5, 'ca': 5, 'cc': 1}), 'B': (('ps', 'b', 'c'), {'bb': 5, 'bc': 1, 'cc': 6})}, {'A': (('w', ''), {}), 'B': (('ps', 'b', 'b'), {'bb': 2})}] ; Gamma(T)=((7, 7, False, False, 5, 6, True, False, 0), (0, 0, False, False, 0, 3, True, True, 0))
     W_j'=cbbbbbbbbcacacaaccacbaaaccabbba  Gamma(W_j')=(9, 10, False, True, 5, 12, False, True, 2)
     round-11 proof: label=I:LemmaE-b0 holes=('b', 'ac') split=((0, 0, 0, 1, 0, 0), (0, 0, 1, 0, 1, 0)) components=(0, 0) pattern=(b,ac)
     F witness (built by (b,ac)): cbbbbbbbbcacacaaccacbaaaccabbba  hole spans=[('b', 8), ('ac', 10)]
     F[t]=cbbbbbbbbbcacacacaaccacbaaaccabbba  dat(F[t])-dat(F[h]) = D: verified; e=1 possible (round-10 search): True
  --- R_open #5 (NR548, class OPEN:ac/b:same) ---
     x=['bbbbbbbcacacaaccacacaac', 'bbb'] ctx=['c', 'ca', 'a'] c*=3  Gamma(x)=[(8, 8, False, False, 6, 7, True, False, 0), (0, 0, False, False, 0, 3, True, True, 0)]  nu_A=[6, 0] nu_B=[0, 0] rich=[False, False]
     phi=['bb', 'cac']  Z_kappa=((0, 0, 0, 1, 0, 0), (0, 0, 1, 0, 1, 0))  ztypes=['b', 'ac']  psi^(j')=['bbb', 'cba']
     original counts N0 = N2(pi_X x_i) (the model takes S between N0 and T): [{'A': {'ca': 6, 'ac': 6, 'aa': 2, 'cc': 1}, 'B': {'bb': 6, 'bc': 1, 'cc': 7}}, {'A': {}, 'B': {'bb': 2}}]
     state T (after) = [{'A': (('ps', 'c', 'c'), {'aa': 2, 'ac': 3, 'ca': 3, 'cc': 1}), 'B': (('ps', 'b', 'c'), {'bb': 3, 'bc': 1, 'cc': 4})}, {'A': (('w', ''), {}), 'B': (('ps', 'b', 'b'), {'bb': 2})}] ; Gamma(T)=((5, 5, False, False, 3, 4, True, False, 0), (0, 0, False, False, 0, 3, True, True, 0))
     W_j'=cbbbbbbbbcacacaaccacbaaaccabbba  Gamma(W_j')=(9, 10, False, True, 5, 12, False, True, 2)
     round-11 proof: label=I:LemmaE-b0 holes=('b', 'ac') split=((0, 0, 0, 1, 0, 0), (0, 0, 1, 0, 1, 0)) components=(0, 0) pattern=(b,ac)
     F witness (built by (b,ac)): cbbbbbbbbcacacaaccacbaaaccabbba  hole spans=[('b', 8), ('ac', 10)]
     F[t]=cbbbbbbbbbcacacacaaccacbaaaccabbba  dat(F[t])-dat(F[h]) = D: verified; e=1 possible (round-10 search): True
  --- R_open #6 (NR695, class OPEN:a/bc:same) ---
     x=['aaaaaacbbcbcbcbcbcbbccbcaaaaaaaabb'] ctx=['', ''] c*=3  Gamma(x)=[(9, 14, True, True, 0, 11, False, True, 7)]  nu_A=[0] nu_B=[7] rich=[False]
     phi=['cbc', 'aaaaa']  Z_kappa=((0, 1, 0, 0, 0, 1), (4, 0, 0, 0, 0, 0))  ztypes=['bc', 'a']  psi^(j')=['cabc', 'bcc']
     original counts N0 = N2(pi_X x_i) (the model takes S between N0 and T): [{'A': {'aa': 12, 'ac': 1, 'cc': 8, 'ca': 1}, 'B': {'cb': 8, 'bb': 3, 'bc': 7, 'cc': 1}}]
     state T (after) = [{'A': (('ps', 'a', 'a'), {'aa': 8, 'ac': 1, 'ca': 1, 'cc': 7}), 'B': (('ps', 'c', 'b'), {'bb': 3, 'bc': 6, 'cb': 7, 'cc': 1})}] ; Gamma(T)=((8, 10, True, True, 0, 10, False, True, 6),)
     W_j'=aaaaaacbbcbcbcbcabcbbccbcaabccabb  Gamma(W_j')=(11, 10, True, True, 2, 12, False, True, 8)
     round-11 proof: label=II[I:LemmaE-bn] holes=('cb', 'a') split=((0, 1, 0, 0, 0, 1), (4, 0, 0, 0, 0, 0)) components=(0, 0) pattern=(ca,b)
     F witness (built by (ca,b)): aaaaaacbbcbcbcbcabcbbccbcaabccabb  hole spans=[('cb', 6), ('a', 25)]
     F[t]=aaaaaacbcbbcbcbcbcabcbbccbcaaaaaabccabb  dat(F[t])-dat(F[h]) = D: verified; e=1 possible (round-10 search): True
  --- R_open #7 (NR695, class OPEN:a/bc:same) ---
     x=['aaaaaacbbcbcbcbcbcbbccbcaaaaaaaabb'] ctx=['', ''] c*=3  Gamma(x)=[(9, 14, True, True, 0, 11, False, True, 7)]  nu_A=[0] nu_B=[7] rich=[False]
     phi=['cbc', 'aaaaa']  Z_kappa=((0, 1, 0, 0, 0, 1), (3, 0, 0, 0, 0, 0))  ztypes=['bc', 'a']  psi^(j')=['cc', 'aba']
     original counts N0 = N2(pi_X x_i) (the model takes S between N0 and T): [{'A': {'aa': 12, 'ac': 1, 'cc': 8, 'ca': 1}, 'B': {'cb': 8, 'bb': 3, 'bc': 7, 'cc': 1}}]
     state T (after) = [{'A': (('ps', 'a', 'a'), {'aa': 9, 'ac': 1, 'ca': 1, 'cc': 7}), 'B': (('ps', 'c', 'b'), {'bb': 3, 'bc': 6, 'cb': 7, 'cc': 1})}] ; Gamma(T)=((8, 11, True, True, 0, 10, False, True, 6),)
     W_j'=aaaaaacbbcbcbcbccbbccbcaaabaabb  Gamma(W_j')=(9, 11, True, True, 0, 11, False, True, 6)
     round-11 proof: label=II[I:LemmaE-bn] holes=('cb', 'a') split=((0, 1, 0, 0, 0, 1), (3, 0, 0, 0, 0, 0)) components=(0, 0) pattern=(ca,b)
     F witness (built by (ca,b)): aaaaaacbbcbcbcbccbbccbcaaabaabb  hole spans=[('cb', 6), ('a', 23)]
     F[t]=aaaaaacbcbbcbcbcbccbbccbcaaaaaabaabb  dat(F[t])-dat(F[h]) = D: verified; e=1 possible (round-10 search): True
  --- R_open #8 (NR695, class OPEN:a/bc:same) ---
     x=['aaaaaacbbcbcbcbcbcbbccbcaaaaaaaabb'] ctx=['', ''] c*=3  Gamma(x)=[(9, 14, True, True, 0, 11, False, True, 7)]  nu_A=[0] nu_B=[7] rich=[False]
     phi=['cbc', 'aaaaa']  Z_kappa=((0, 1, 0, 0, 0, 1), (1, 0, 0, 0, 0, 0))  ztypes=['bc', 'a']  psi^(j')=['cccb', 'aa']
     original counts N0 = N2(pi_X x_i) (the model takes S between N0 and T): [{'A': {'aa': 12, 'ac': 1, 'cc': 8, 'ca': 1}, 'B': {'cb': 8, 'bb': 3, 'bc': 7, 'cc': 1}}]
     state T (after) = [{'A': (('ps', 'a', 'a'), {'aa': 11, 'ac': 1, 'ca': 1, 'cc': 7}), 'B': (('ps', 'c', 'b'), {'bb': 3, 'bc': 6, 'cb': 7, 'cc': 1})}] ; Gamma(T)=((8, 13, True, True, 0, 10, False, True, 6),)
     W_j'=aaaaaacbbcbcbcbcccbbbccbcaaaaabb  Gamma(W_j')=(10, 11, True, True, 0, 11, False, True, 6)
     round-11 proof: label=II[I:LemmaE-bn] holes=('cb', 'a') split=((0, 1, 0, 0, 0, 1), (1, 0, 0, 0, 0, 0)) components=(0, 0) pattern=(ca,b)
     F witness (built by (ca,b)): aaaaaacbbcbcbcbcccbbbccbcaaaaabb  hole spans=[('cb', 6), ('a', 25)]
     F[t]=aaaaaacbcbbcbcbcbcccbbbccbcaaaaaabb  dat(F[t])-dat(F[h]) = D: verified; e=1 possible (round-10 search): True
[3] all 8 R_open configurations: proof label/holes reproduced and fully verified (8)
[4] controls (MUST fail somewhere):
      e<=1 only                                : fails on 4031 of 193852 cases
      Lemma E with the other pattern            : fails on 902 of 2090 cases
      Lemma X with both holes in one component  : fails on 514 of 520 cases
      long projection dropped (y_i=ab, hole b, D_B=bb): shat_2(pi_B) ('w', 'b') -> ('ps', 'b', 'b') : BROKEN (detected)
      "marked windows persist literally in W"   : false for 60 of 1837 marked windows (only marked LETTERS are used)
[5] real round-9 derivations (round-10 integration driver replayed, its own checks PASSED): nonzero stages run through prove_J=475, verified=475, FAIL=0
      labels: {'0d:L-ab': 6, '0e1:EO3': 7, '0e1:LemmaE-b0': 21, '0e1m[0e1:EO3]': 48, '0e1m[0e1:LemmaE-b0]': 8, 'III': 171, 'T5': 214}
      round-10 classes: {'CITED-HC_I/II/III': 90, 'PROVED:T4-transitional-diff-root': 171, 'PROVED:T5-rich-component': 214}
time 860.5s
ALL CHECKS PASSED
exit 0
END SOURCE out_check_round11_residual_2026-11-15.txt

### Claude readme — `README_RUN.txt`

BEGIN SOURCE README_RUN.txt
Round 11 (fan-out 2, U2) -- how to reproduce
  python3 -I check_round11_residual_2026-11-15.py --src deps     # ~15 min, final line ALL CHECKS PASSED
  python3 -I check_round11_residual_2026-11-15.py --src deps --quick   # ~5 min smoke test
deps/ = round-9/10 sources extracted byte-for-byte from the round-11 brief (SHA256 checked at start-up).
extract.py = the extraction script used:  python3 -I extract.py <brief.md> <outdir>
rerun_round10_*.txt = fresh re-runs of the round-10 checkers (HC: identical to the submitted log except the time line;
                      integration: byte-identical, SHA256 66355f70..., after dropping the trailing "exit 0" line our wrapper appended).
Logs are from runs actually executed in this session (PYTHONHASHSEED=0).
END SOURCE README_RUN.txt

### Claude manifest — `MANIFEST_SHA256.txt`

BEGIN SOURCE MANIFEST_SHA256.txt
3a1e8155129e0a889accd746e7ea595221bbdb642f24cd6e5097b21623762067  ./README_RUN.txt
dfbae608d273bb31e901c198b9ac17ba06d811f572a991a37f1afe1d165518aa  ./check_round11_residual_2026-11-15.py
48f54e96aa61308c4ef6babd4edcf4dbd21c070d95795a1c0515bbb5191c626b  ./claude_fanout2_round11_checkpoint1_2026-11-15.md
e15b1ccd2b37d808563f5761eb78cdd9d121c522187808fd111ac988132d2f34  ./claude_fanout2_round11_next_obligations_2026-11-15.md
0fc54cd73e7d7388ecf537d5ef486b835f7f566575afd645d9fabdebe1141b2c  ./claude_fanout2_round11_residual_report_2026-11-15.md
aa316db69814583cf02dc5338057f360916c6c6aa1be7f6e5e5c1224d6b0a2e2  ./deps/check_round10_HC_exhaustiveness_2026-11-14.py
d0b5cc90fd050068aa0a4ed23d891ac1b4a1fb61a8b5f8c23498d21769e3689d  ./deps/check_round10_U2_integration_2026-11-14.py
c468f6ad5eb972b64803ca90de69a3b8c85beeedd21e9762363e89b83c78bde3  ./deps/check_round9_overlap_P1_B6_2026-11-14.py
88c78f73289db74ea342bc9a510e75df47f3d60b9517632d98363149f62cbabd  ./extract.py
78a6bd8392151c485cafc5ae8cdede2abba06fd41a01162e3e3b9ca707d9f07d  ./out_check_round11_residual_2026-11-15.txt
217c1b9470127074f051b72ec5ff0f7268bffd61270840bb1a338a53669b2b62  ./rerun_round10_HC_exhaustiveness_2026-11-15.txt
7c9fe96f4055f011ef142f4b7b166aed043a566302698e9692103c8199ddc84f  ./rerun_round10_U2_integration_2026-11-15.txt
END SOURCE MANIFEST_SHA256.txt

### Independent audit report — `audit_claude_fanout2_round11_independent_2026-11-15.md`

BEGIN SOURCE audit_claude_fanout2_round11_independent_2026-11-15.md
# 第十一段 U₂ 残余閉鎖：独立数学監査

**日付**：2026-11-15 JST  
**対象**：ユーザー提供 `claude_fanout2_round11_2026-11-15.zip`（Claude第十一段最終報告、チェックポイント、証明追従プログラム、提出ログ、依存コード）  
**主張の厳格な範囲**：`Σ={a,b,c}`, `A={a,c}`, `B={b,c}`, bigram 長 `ℓ=2`, `f=r_max=2`, 内容型 `c_Σ`, `L∩Σ⁺=dat_ov^{-1}(Q)`、`L∈C^{mcf}_{2,c_Σ}`, reduced good MCFG `G`。一般 `op:fanout-two` とは別問題である。  
**監査区分**：数学の手証明の独立再構成＋証明追従プログラムの再実行＋Claudeコードとは独立した局所補題全列挙。専門家の査読・形式化証明ではない。

## 1. 結論

**第十一段の新しい「補題 V → 残余の補題 E → 非豊か全場合の定理 N」には、手証明を追跡した範囲で致命的な欠陥を認めない。第十段の残余 `R_open` は、証明案の論理上は解消されたと評価する。** 第十段の T1〜T4 と従来の HC_I/II/III を直接引用せずに非豊かな場合を網羅する構造は妥当である。豊かな場合には T5 を適用する。したがって先行の P1/B6/P0/H**/J⇒短縮と骨格計数を前提とする **特殊クラス U₂ の完全な手証明案**が揃ったと認める。

ただし、この判定は形式証明や専門家査読による完全な保証を意味しない。また、論文本文の正式開問題 `op:fanout-two` は OPEN であり、その結論を更新するものではない。

## 2. ZIP・ソース整合性と計算検証

- ZIP 内ファイル一覧、Claude最終報告、checkpoint、manifest、依存 Python 3 本を確認。`MANIFEST_SHA256.txt` に記載された主要ファイルのハッシュは実ファイルと一致した。
- Claude提供の第十一段検証器は第九・十段の3ソースをインポートするため「全体として完全独立の別実装」ではない。もっとも、その F 側の証明追従構成では大半の枝について hosting オラクルを使わず具体語を構成する。T5 および一部実導出は引き続きオラクルに依存する。これは有限検査の独立性の限界であり、手証明の妥当性とは分けて扱う。
- **独立の追加検査**：本監査で新作した `independent_round11_local_audit_2026-11-15.py` は、Claudeのコードをインポートせず、`|w|≤10` の **88,572 非空語**について、各射影の最初の `c*=3` 窓から端点マークを作り、補題 M1〜M7 と補題 V（連続自由因子）を総当たり確認。**ALL INDEPENDENT LOCAL CHECKS PASSED**。
- **第十一段の全量再実行**：提出ZIPに含まれるソースで `PYTHONHASHSEED=0 python3 -I check_round11_residual_2026-11-15.py --src deps` を新規実行し、**exit 0、`ALL CHECKS PASSED`、193,945設定、PROOF_FAIL=0・VERIFY_FAIL=0、残余旧分類838設定、実導出475非零段（全て検証）**を再現。実行時間は提出860.5秒に対して本環境570.1秒。**提出ログと異なるのは `time` の１行と提出時に追記された `exit 0` の１行だけ**で、計算結果・枝別内訳・反例トレース・負の対照は全て一致。ログを `round11_full_independent_rerun.txt` に保存した。

## 3. 数学的監査

### 3.1 補題 V：半遷移型の空虚性

`ν_b(x)=0` なら `b` は `c` で区切った先頭・末尾の区間にしか存在しない。ある自由 η 成分 `φ⊆x` が `b` と `c` の双方を含めば、`u_0` 側ではその中に `u_0` の最後の `b` と最初の `c` が、`u_n` 側では最後の `c` と `u_n` の最初の `b` がともに含まれる。これは唯一の `bc` または `cb` の射影窓の両端であり、先頭 `c*` 個として印が付く。自由 η は印を含まないので矛盾。`a` も鏡像で同様。

これを P1 の「非零の `r` ⇒ `N_0(ac)≥c*+1` ⇒ `ν_A≥c*`」等と併用すると、非豊かな成分では `abcA/abcB`, `abc+`, `abc2` は起こらず、`ac` と `bc` が同一根成分にあれば豊かさが強制される。この帰結は単なる有限探索での未発見ではなく、上記の印の位置からの数学的帰結である。

### 3.2 残余の補題 E

非豊かな同一根成分で `ac` 遷移と `bb` ループが別の η 成分から削除される場合、`ν_A≥1,ν_B=0` により `b` は先頭 `u_0` または末尾 `u_n` にある。`ac` に由来する最小の内側 A 占有区間 `u_{s0}` を用いる。

- 末尾 `b_n`：原位置に `c_{s0}<a''<c_{s0+1}≤c_n<b*` の印付き文字がある。F 側に順序 `(ca,b)` を置け、Y 側では内側区間1に `a`、末尾区間に `b` を置く。
- 先頭 `b_0`：逆向きに `b*<c_1≤c_{s0}<a''<c_{s0+1}` があり、F/Y とも `(b,ac)` を置ける。

各穴の射影に必要な長さは、`a,b,c` を持つ根成分と `n_T≥3` で保証される。共通の η 成分に穴を固定する必要がないことは、先行定理 J の「総和型 P0」に基づく。原 `R_open` の8設定が E の枝に落ちるという対応も整合的である。

### 3.3 定理 N の大場合分け

`D` の遷移係数を `r,r'` として、(III)双方正、(I)Aのみ正、(II)Bのみ正、(0)双方ゼロに分けることで網羅している。

- **III**：非豊かでは A 遷移と B 遷移は同じ根成分に起こせず、二根成分に分離する。各 κ の c 共有保存から `q≥r'` を導き、`D_1=(p aa+(q-r')cc+r(ac+ca),q'cc)` と `D_2=(r'cc,p'bb+r'(bc+cb))` に分割する。F の `(ca,bc)` または `(cb,ac)`、Y の成分別長射影を確認した。
- **I/II**：一方に遷移があり他方にない場合、他方のループを同じ根成分に置ければ補題 E、別根成分なら補題 X を使う。分割した `D_i` が保存的で合計 `D` になることを確認した。
- **0**：`r=r'=0` なら `D_a=p aa,D_b=p'bb,D_c=q cc` の三要素の正負で完全に分けられる。単独、2種の和、3種の和を含め、同根／別根の分類がある。先頭の印付き `aa/bb` 2端点から距離2以上の組を選ぶ L-ab の議論は正しい。`q>0` なら `n≥c*+2` が必要で、これを用いる M7/EO の枝も整合する。

**精密化を勧める点**：`0e2(ii)`（他方の根成分が `c^+`、先頭の a,b が別区間）では、F 側の「`acb` は文字どおり」または「`(ac,b)` に非空隙間がある」の分岐を、**「最初の b より前には b がないため、先の a 区間の最後の文字は a」**と明記すると読み手が検証しやすい。また、Y 側の対応は、非豊か条件により異なる内側区間の同時占有が排除されることを逐語で示すとよい。この点は現時点では補足推奨であり、判定を覆す反例ではない。

### 3.4 T5 と一般移送 J

ある根成分が `ν_A,ν_B≥1` かつ `#c≥3` なら、B6 の計数下限と旗の持続から、Y は6種の3文字順列をすべて hosting できる。F は印付き `ac` と `ca` に対応する元文字の順序を保つため、硬直形 `a^+c^n b^+` または逆順を除外でき、少なくとも1種を hosting できる。共通穴 `h` を一つ選び、任意の保存的総差分 `D` を H** によって膨張する T5 を支持する。

定理 J では、F 側の `F[h],F[t]∈L` を `dat_ov` の同値と組代入可能性から使い、Y 側で `h→t` を行った `y^π` と現在語の内容・成分ごとの `ŝ₂`・**射影ごとの総 N₂** を P0 で一致させる。非零差分では `|D_A|+|D_B|-m>0` となる。先行監査で確認した長射影条件も J に明記されている。

### 3.5 多項式代表長と修正された貪欲DFS計数

`H≤49v`、印付き文字数・骨格・η数、`C≤7^4(1+2H(θ̄_G+2))^{16}` の組合せ計数を確認。第十段の誤記「訪問添字すべての色が異なる」は使わず、**跳ばない一歩の出発点の色だけが相異なる**ため高々 `C` 回とする修正は正しい。

元窓を (1)印付き、(2)骨格文字端点、(3)異なる自由成分にまたがる、(4)同じ自由成分の内部、に分ける被覆と `|U_{k+1}\setminus U_k|≤Hθ̄_G` を使うと、`c*=3,d=r=2` で以下を得る。

\[
\tau(G,c_\Sigma)\le52+192(2\bar\theta_G+4)(H+1)+768\,C H\bar\theta_G(H+1)
=O(v^{18}\bar\theta_G^{17}).
\]

`cor:distribution-representatives` から `||K||_+≤4096||G||(1+2θ̄_G+2τ)+1_{ε∈L}`。**ここで原 G の厚さを使うこと**は重要であり、型付け後文法の厚さにすり替えてはいない。

## 4. なお残る検証の限界

1. **真正な型付き根最短導出で `R_open` を具体例として実現する検査はなし**。証明は任意の段を扱うので論理的な必要条件ではないが、ストレステストの穴として記録する。
2. **F 構成のコード化には一部オラクルを使用**。全ケースの有限検証は証明の形式化ではない。
3. **専門家査読・Lean/Coq等の機械形式証明は未実施**。現時点の評価は独立した数学的手監査であって、証明の正しさを絶対的に保証するものではない。
4. 本定理は特殊な `dat_ov` 言語族上の上界であり、一般 `op:fanout-two` の LG 必要性とは論理的に別。論文 #2 の `main.tex`、日本語版、PDF、定理 A/B/C、正式 open problem は変更しない。

## 5. 検証コード再実行の抜粋

- 同色・段モデル：193,945設定、`PROOF_FAIL=0`, `VERIFY_FAIL=0`。
- 第十段の分類で `CITED-HC_I/II/III` だった15,740設定も定理N系の枝で全て通過。
- 第十段の `OPEN` 分類だった838設定も補題E系の枝に落ち、全て通過。
- 補題V：86,267段について違反0。故意に印を外した負の対照 `c*=0` は778配置中321配置で失敗し、印の必要性を再確認。
- 実導出：475非零段、失敗0。従来の条件付きHCと分類された90段も新しい枝で検証。
- 故意の不足条件：`e≤1` のみでは193,852設定中4,031失敗、Eの逆向き穴配置では2,090中902失敗、Xを一成分に押し込めると520中514失敗。長射影を外すと `ŝ₂` が壊れる。
- Claudeコードから独立したM/V全列挙：88,572語で全通過。

## 6. 今後の推奨

第十一段の原資料と本監査を研究アーカイブに保存し、次は **(i) U₂ のコンパクトな独立論文草稿＋専門家レベルの逐行査読、(ii) 一般 `op:fanout-two` に戻って U₁ 型付けの超多項式下界を探す探索**を明確に分ける。いきなり現行論文 #2 に新定理として差し込まない。
END SOURCE audit_claude_fanout2_round11_independent_2026-11-15.md

### Independent rerun log — `round11_full_independent_rerun.txt`

BEGIN SOURCE round11_full_independent_rerun.txt
== Round 11 residual-closure checker; seeds 20261115 (model), 20261114 (round-10 replay) ==
sources verified: {'check_round10_HC_exhaust': 'aa316db69814', 'check_round10_U2_integra': 'd0b5cc90fd05', 'check_round9_overlap_P1_': 'c468f6ad5eb9'}
[0] independent dat/Gamma on all 1558 dat classes (len<=8) agree with round 10; reference BRUTE-FORCE hosting == round-10 oracle: 14297 single-hole + 60552 ordered-pair checks on 841 classes (len<=7), 21558 positive; 4000 random 2-component tuple checks
[1a] exhaustive d=1 |x|<=7: cases=93 proof_fail=0 verify_fail=0
[1d] targeted residual roots (nu_B=0 or mirror, inner a-runs, b-runs at an end): cases=25503, round-10 OPEN-class cases=553
[1e] targeted d=2 cross configurations: cases=47368
[1f] branch-targeted shapes: cases=81673
[1g] end-only / E-family roots, eta = maximal free intervals: cases=25554
[1h] deterministic stages for branch 0e2:ii-acb (both orders, a<->b mirror): cases=695
[1] proof-following constructor on the stage model: cases=193945  PROOF_FAIL=0  VERIFY_FAIL=0  verified=193945 (F built by the named LG rearrangement: 181873; F by oracle: 12072)
[1] cases per proof label (coverage; 0 = coverage missing):
      (innermost proof branch, mirrors merged : cases ; outer wrappers II/0c/0e1m/0e2m/0e4 = a<->b mirror)
      T5                       12072
      III                         50
      I:single-ca              10720
      I:LemmaE-bn                596
      I:LemmaE-b0                313
      I:LemmaX                   520
      0a:single               136185
      0b:diff                   4443
      0b:same                   6803
      0d:diff                   2571
      0d:L-ab                  16263
      0e1:LemmaE-bn              948
      0e1:LemmaE-b0              233
      0e1:EO1                    883
      0e1:EO3                    152
      0e1:EO4                    132
      0e2:a-in-c-comp             74
      0e2:i-ab                   514
      0e2:ii-ac,b                 44
      0e2:ii-acb                 396
      0e3:cross                   33
      wrappers: {'0c[0b:diff]': 2424, '0c[0b:same]': 3198, '0e1m[0e1:EO1]': 280, '0e1m[0e1:EO3]': 77, '0e1m[0e1:EO4]': 94, '0e1m[0e1:LemmaE-b0]': 90, '0e1m[0e1:LemmaE-bn]': 461, '0e2m[0e2:a-in-c-comp]': 16, '0e2m[0e2:ii-ac,b]': 7, '0e2m[0e2:ii-acb]': 223, '0e4[0e3:cross]': 12, 'II[I:LemmaE-b0]': 139, 'II[I:LemmaE-bn]': 284, 'II[I:LemmaX]': 237, 'II[I:single-ca]': 4950}
[1] round-10 classes -> cases: {'CITED-HC_I/II/III': 15740, 'OPEN:a/bc:same': 385, 'OPEN:ac/b:same': 453, 'PROVED:T1-single-a': 52042, 'PROVED:T1-single-ac': 6317, 'PROVED:T1-single-b': 49760, 'PROVED:T1-single-bc': 5151, 'PROVED:T1-single-c': 24762, 'PROVED:T2-letter-pair': 15710, 'PROVED:T3-merge': 10915, 'PROVED:T4-transitional-diff-root': 638, 'PROVED:T5-rich-component': 12072}
[1] round-10 OPEN-class cases -> round-11 proof label: {'0e1:LemmaE-b0': 4, '0e1m[0e1:LemmaE-b0]': 14, '0e1m[0e1:LemmaE-bn]': 10, 'I:LemmaE-b0': 171, 'I:LemmaE-bn': 278, 'II[I:LemmaE-b0]': 107, 'II[I:LemmaE-bn]': 254}
[2] Lemma V on every generated stage: checked=86267 violated=0
[2] ztype of nonzero kappa in NON-rich components: {'a': 36595, 'ab': 7872, 'ac': 4422, 'b': 33793, 'bc': 2889, 'c': 14375}
      abcA in a non-rich component: 0  (coverage missing -- vacuous by Lemma V)
      abcB in a non-rich component: 0  (coverage missing -- vacuous by Lemma V)
      abc+ in a non-rich component: 0  (coverage missing -- vacuous by Lemma V)
      abc2 in a non-rich component: 0  (vacuous: abc2 forces richness)
[2'] control c*=0 (no marks): Lemma V violated on 321 of 778 layouts (MUST be > 0: marks are what make abcA etc. vacuous)
[3] round-10 driver replayed (seed 20261114, --rand 400): ALL CHECKS PASSED reproduced; captured 6 OPEN configurations (8 with their T states)
  --- R_open #1 (NR377, class OPEN:ac/b:same) ---
     x=['abbbbbbbbcaaaacccaccaaccac'] ctx=['', ''] c*=3  Gamma(x)=[(9, 9, True, False, 4, 8, True, False, 0)]  nu_A=[4] nu_B=[0] rich=[False]
     phi=['bbb', 'cac']  Z_kappa=((0, 0, 0, 1, 0, 0), (0, 0, 1, 0, 1, 0))  ztypes=['b', 'ac']  psi^(j')=['ccaa', 'bbcc']
     original counts N0 = N2(pi_X x_i) (the model takes S between N0 and T): [{'A': {'ac': 5, 'ca': 4, 'aa': 4, 'cc': 4}, 'B': {'bb': 7, 'bc': 1, 'cc': 8}}]
     state T (after) = [{'A': (('ps', 'a', 'c'), {'aa': 4, 'ac': 4, 'ca': 3, 'cc': 4}), 'B': (('ps', 'b', 'c'), {'bb': 6, 'bc': 1, 'cc': 7})}] ; Gamma(T)=((8, 8, True, False, 3, 7, True, False, 0),)
     W_j'=abbbbccaabcaaaacccaccaacbbcc  Gamma(W_j')=(11, 10, True, False, 4, 7, True, False, 2)
     round-11 proof: label=I:LemmaE-b0 holes=('b', 'ac') split=((0, 0, 0, 1, 0, 0), (0, 0, 1, 0, 1, 0)) components=(0, 0) pattern=(b,ac)
     F witness (built by (b,ac)): abbbbccaabcaaaacccaccaacbbcc  hole spans=[('b', 9), ('ac', 14)]
     F[t]=abbbbccaabbcaaaacacccaccaacbbcc  dat(F[t])-dat(F[h]) = D: verified; e=1 possible (round-10 search): True
  --- R_open #2 (NR377, class OPEN:ac/b:same) ---
     x=['abbbbbbbbcaaaacccaccaaccac'] ctx=['', ''] c*=3  Gamma(x)=[(9, 9, True, False, 4, 8, True, False, 0)]  nu_A=[4] nu_B=[0] rich=[False]
     phi=['bbb', 'cac']  Z_kappa=((0, 0, 0, 2, 0, 0), (0, 0, 1, 0, 1, 0))  ztypes=['b', 'ac']  psi^(j')=['cacb', 'bbac']
     original counts N0 = N2(pi_X x_i) (the model takes S between N0 and T): [{'A': {'ac': 5, 'ca': 4, 'aa': 4, 'cc': 4}, 'B': {'bb': 7, 'bc': 1, 'cc': 8}}]
     state T (after) = [{'A': (('ps', 'a', 'c'), {'aa': 4, 'ac': 4, 'ca': 3, 'cc': 4}), 'B': (('ps', 'b', 'c'), {'bb': 5, 'bc': 1, 'cc': 7})}] ; Gamma(T)=((8, 8, True, False, 3, 6, True, False, 0),)
     W_j'=abbbbcacbbcaaaacccaccaacbbac  Gamma(W_j')=(10, 10, True, False, 5, 8, True, False, 2)
     round-11 proof: label=I:LemmaE-b0 holes=('b', 'ac') split=((0, 0, 0, 2, 0, 0), (0, 0, 1, 0, 1, 0)) components=(0, 0) pattern=(b,ac)
     F witness (built by (b,ac)): abbbbcacbbcaaaacccaccaacbbac  hole spans=[('b', 9), ('ac', 14)]
     F[t]=abbbbcacbbbbcaaaacacccaccaacbbac  dat(F[t])-dat(F[h]) = D: verified; e=1 possible (round-10 search): True
  --- R_open #3 (NR377, class OPEN:ac/b:same) ---
     x=['abbbbbbbbcaaaacccaccaaccac'] ctx=['', ''] c*=3  Gamma(x)=[(9, 9, True, False, 4, 8, True, False, 0)]  nu_A=[4] nu_B=[0] rich=[False]
     phi=['bbb', 'cac']  Z_kappa=((0, 0, 0, 2, 0, 0), (0, 0, 1, 0, 1, 0))  ztypes=['b', 'ac']  psi^(j')=['cacb', 'bbac']
     original counts N0 = N2(pi_X x_i) (the model takes S between N0 and T): [{'A': {'ac': 5, 'ca': 4, 'aa': 4, 'cc': 4}, 'B': {'bb': 7, 'bc': 1, 'cc': 8}}]
     state T (after) = [{'A': (('ps', 'a', 'c'), {'aa': 4, 'ac': 4, 'ca': 3, 'cc': 3}), 'B': (('ps', 'b', 'c'), {'bb': 5, 'bc': 1, 'cc': 6})}] ; Gamma(T)=((7, 8, True, False, 3, 6, True, False, 0),)
     W_j'=abbbbcacbbcaaaacccaccaacbbac  Gamma(W_j')=(10, 10, True, False, 5, 8, True, False, 2)
     round-11 proof: label=I:LemmaE-b0 holes=('b', 'ac') split=((0, 0, 0, 2, 0, 0), (0, 0, 1, 0, 1, 0)) components=(0, 0) pattern=(b,ac)
     F witness (built by (b,ac)): abbbbcacbbcaaaacccaccaacbbac  hole spans=[('b', 9), ('ac', 14)]
     F[t]=abbbbcacbbbbcaaaacacccaccaacbbac  dat(F[t])-dat(F[h]) = D: verified; e=1 possible (round-10 search): True
  --- R_open #4 (NR548, class OPEN:ac/b:same) ---
     x=['bbbbbbbcacacaaccacacaac', 'bbb'] ctx=['c', 'ca', 'a'] c*=3  Gamma(x)=[(8, 8, False, False, 6, 7, True, False, 0), (0, 0, False, False, 0, 3, True, True, 0)]  nu_A=[6, 0] nu_B=[0, 0] rich=[False, False]
     phi=['bb', 'cac']  Z_kappa=((0, 0, 0, 1, 0, 0), (0, 0, 1, 0, 1, 0))  ztypes=['b', 'ac']  psi^(j')=['bbb', 'cba']
     original counts N0 = N2(pi_X x_i) (the model takes S between N0 and T): [{'A': {'ca': 6, 'ac': 6, 'aa': 2, 'cc': 1}, 'B': {'bb': 6, 'bc': 1, 'cc': 7}}, {'A': {}, 'B': {'bb': 2}}]
     state T (after) = [{'A': (('ps', 'c', 'c'), {'aa': 2, 'ac': 5, 'ca': 5, 'cc': 1}), 'B': (('ps', 'b', 'c'), {'bb': 5, 'bc': 1, 'cc': 6})}, {'A': (('w', ''), {}), 'B': (('ps', 'b', 'b'), {'bb': 2})}] ; Gamma(T)=((7, 7, False, False, 5, 6, True, False, 0), (0, 0, False, False, 0, 3, True, True, 0))
     W_j'=cbbbbbbbbcacacaaccacbaaaccabbba  Gamma(W_j')=(9, 10, False, True, 5, 12, False, True, 2)
     round-11 proof: label=I:LemmaE-b0 holes=('b', 'ac') split=((0, 0, 0, 1, 0, 0), (0, 0, 1, 0, 1, 0)) components=(0, 0) pattern=(b,ac)
     F witness (built by (b,ac)): cbbbbbbbbcacacaaccacbaaaccabbba  hole spans=[('b', 8), ('ac', 10)]
     F[t]=cbbbbbbbbbcacacacaaccacbaaaccabbba  dat(F[t])-dat(F[h]) = D: verified; e=1 possible (round-10 search): True
  --- R_open #5 (NR548, class OPEN:ac/b:same) ---
     x=['bbbbbbbcacacaaccacacaac', 'bbb'] ctx=['c', 'ca', 'a'] c*=3  Gamma(x)=[(8, 8, False, False, 6, 7, True, False, 0), (0, 0, False, False, 0, 3, True, True, 0)]  nu_A=[6, 0] nu_B=[0, 0] rich=[False, False]
     phi=['bb', 'cac']  Z_kappa=((0, 0, 0, 1, 0, 0), (0, 0, 1, 0, 1, 0))  ztypes=['b', 'ac']  psi^(j')=['bbb', 'cba']
     original counts N0 = N2(pi_X x_i) (the model takes S between N0 and T): [{'A': {'ca': 6, 'ac': 6, 'aa': 2, 'cc': 1}, 'B': {'bb': 6, 'bc': 1, 'cc': 7}}, {'A': {}, 'B': {'bb': 2}}]
     state T (after) = [{'A': (('ps', 'c', 'c'), {'aa': 2, 'ac': 3, 'ca': 3, 'cc': 1}), 'B': (('ps', 'b', 'c'), {'bb': 3, 'bc': 1, 'cc': 4})}, {'A': (('w', ''), {}), 'B': (('ps', 'b', 'b'), {'bb': 2})}] ; Gamma(T)=((5, 5, False, False, 3, 4, True, False, 0), (0, 0, False, False, 0, 3, True, True, 0))
     W_j'=cbbbbbbbbcacacaaccacbaaaccabbba  Gamma(W_j')=(9, 10, False, True, 5, 12, False, True, 2)
     round-11 proof: label=I:LemmaE-b0 holes=('b', 'ac') split=((0, 0, 0, 1, 0, 0), (0, 0, 1, 0, 1, 0)) components=(0, 0) pattern=(b,ac)
     F witness (built by (b,ac)): cbbbbbbbbcacacaaccacbaaaccabbba  hole spans=[('b', 8), ('ac', 10)]
     F[t]=cbbbbbbbbbcacacacaaccacbaaaccabbba  dat(F[t])-dat(F[h]) = D: verified; e=1 possible (round-10 search): True
  --- R_open #6 (NR695, class OPEN:a/bc:same) ---
     x=['aaaaaacbbcbcbcbcbcbbccbcaaaaaaaabb'] ctx=['', ''] c*=3  Gamma(x)=[(9, 14, True, True, 0, 11, False, True, 7)]  nu_A=[0] nu_B=[7] rich=[False]
     phi=['cbc', 'aaaaa']  Z_kappa=((0, 1, 0, 0, 0, 1), (4, 0, 0, 0, 0, 0))  ztypes=['bc', 'a']  psi^(j')=['cabc', 'bcc']
     original counts N0 = N2(pi_X x_i) (the model takes S between N0 and T): [{'A': {'aa': 12, 'ac': 1, 'cc': 8, 'ca': 1}, 'B': {'cb': 8, 'bb': 3, 'bc': 7, 'cc': 1}}]
     state T (after) = [{'A': (('ps', 'a', 'a'), {'aa': 8, 'ac': 1, 'ca': 1, 'cc': 7}), 'B': (('ps', 'c', 'b'), {'bb': 3, 'bc': 6, 'cb': 7, 'cc': 1})}] ; Gamma(T)=((8, 10, True, True, 0, 10, False, True, 6),)
     W_j'=aaaaaacbbcbcbcbcabcbbccbcaabccabb  Gamma(W_j')=(11, 10, True, True, 2, 12, False, True, 8)
     round-11 proof: label=II[I:LemmaE-bn] holes=('cb', 'a') split=((0, 1, 0, 0, 0, 1), (4, 0, 0, 0, 0, 0)) components=(0, 0) pattern=(ca,b)
     F witness (built by (ca,b)): aaaaaacbbcbcbcbcabcbbccbcaabccabb  hole spans=[('cb', 6), ('a', 25)]
     F[t]=aaaaaacbcbbcbcbcbcabcbbccbcaaaaaabccabb  dat(F[t])-dat(F[h]) = D: verified; e=1 possible (round-10 search): True
  --- R_open #7 (NR695, class OPEN:a/bc:same) ---
     x=['aaaaaacbbcbcbcbcbcbbccbcaaaaaaaabb'] ctx=['', ''] c*=3  Gamma(x)=[(9, 14, True, True, 0, 11, False, True, 7)]  nu_A=[0] nu_B=[7] rich=[False]
     phi=['cbc', 'aaaaa']  Z_kappa=((0, 1, 0, 0, 0, 1), (3, 0, 0, 0, 0, 0))  ztypes=['bc', 'a']  psi^(j')=['cc', 'aba']
     original counts N0 = N2(pi_X x_i) (the model takes S between N0 and T): [{'A': {'aa': 12, 'ac': 1, 'cc': 8, 'ca': 1}, 'B': {'cb': 8, 'bb': 3, 'bc': 7, 'cc': 1}}]
     state T (after) = [{'A': (('ps', 'a', 'a'), {'aa': 9, 'ac': 1, 'ca': 1, 'cc': 7}), 'B': (('ps', 'c', 'b'), {'bb': 3, 'bc': 6, 'cb': 7, 'cc': 1})}] ; Gamma(T)=((8, 11, True, True, 0, 10, False, True, 6),)
     W_j'=aaaaaacbbcbcbcbccbbccbcaaabaabb  Gamma(W_j')=(9, 11, True, True, 0, 11, False, True, 6)
     round-11 proof: label=II[I:LemmaE-bn] holes=('cb', 'a') split=((0, 1, 0, 0, 0, 1), (3, 0, 0, 0, 0, 0)) components=(0, 0) pattern=(ca,b)
     F witness (built by (ca,b)): aaaaaacbbcbcbcbccbbccbcaaabaabb  hole spans=[('cb', 6), ('a', 23)]
     F[t]=aaaaaacbcbbcbcbcbccbbccbcaaaaaabaabb  dat(F[t])-dat(F[h]) = D: verified; e=1 possible (round-10 search): True
  --- R_open #8 (NR695, class OPEN:a/bc:same) ---
     x=['aaaaaacbbcbcbcbcbcbbccbcaaaaaaaabb'] ctx=['', ''] c*=3  Gamma(x)=[(9, 14, True, True, 0, 11, False, True, 7)]  nu_A=[0] nu_B=[7] rich=[False]
     phi=['cbc', 'aaaaa']  Z_kappa=((0, 1, 0, 0, 0, 1), (1, 0, 0, 0, 0, 0))  ztypes=['bc', 'a']  psi^(j')=['cccb', 'aa']
     original counts N0 = N2(pi_X x_i) (the model takes S between N0 and T): [{'A': {'aa': 12, 'ac': 1, 'cc': 8, 'ca': 1}, 'B': {'cb': 8, 'bb': 3, 'bc': 7, 'cc': 1}}]
     state T (after) = [{'A': (('ps', 'a', 'a'), {'aa': 11, 'ac': 1, 'ca': 1, 'cc': 7}), 'B': (('ps', 'c', 'b'), {'bb': 3, 'bc': 6, 'cb': 7, 'cc': 1})}] ; Gamma(T)=((8, 13, True, True, 0, 10, False, True, 6),)
     W_j'=aaaaaacbbcbcbcbcccbbbccbcaaaaabb  Gamma(W_j')=(10, 11, True, True, 0, 11, False, True, 6)
     round-11 proof: label=II[I:LemmaE-bn] holes=('cb', 'a') split=((0, 1, 0, 0, 0, 1), (1, 0, 0, 0, 0, 0)) components=(0, 0) pattern=(ca,b)
     F witness (built by (ca,b)): aaaaaacbbcbcbcbcccbbbccbcaaaaabb  hole spans=[('cb', 6), ('a', 25)]
     F[t]=aaaaaacbcbbcbcbcbcccbbbccbcaaaaaabb  dat(F[t])-dat(F[h]) = D: verified; e=1 possible (round-10 search): True
[3] all 8 R_open configurations: proof label/holes reproduced and fully verified (8)
[4] controls (MUST fail somewhere):
      e<=1 only                                : fails on 4031 of 193852 cases
      Lemma E with the other pattern            : fails on 902 of 2090 cases
      Lemma X with both holes in one component  : fails on 514 of 520 cases
      long projection dropped (y_i=ab, hole b, D_B=bb): shat_2(pi_B) ('w', 'b') -> ('ps', 'b', 'b') : BROKEN (detected)
      "marked windows persist literally in W"   : false for 60 of 1837 marked windows (only marked LETTERS are used)
[5] real round-9 derivations (round-10 integration driver replayed, its own checks PASSED): nonzero stages run through prove_J=475, verified=475, FAIL=0
      labels: {'0d:L-ab': 6, '0e1:EO3': 7, '0e1:LemmaE-b0': 21, '0e1m[0e1:EO3]': 48, '0e1m[0e1:LemmaE-b0]': 8, 'III': 171, 'T5': 214}
      round-10 classes: {'CITED-HC_I/II/III': 90, 'PROVED:T4-transitional-diff-root': 171, 'PROVED:T5-rich-component': 214}
time 570.1s
ALL CHECKS PASSED
END SOURCE round11_full_independent_rerun.txt

### Independent local auditor — `independent_round11_local_audit_2026-11-15.py`

BEGIN SOURCE independent_round11_local_audit_2026-11-15.py
#!/usr/bin/env python3
"""Independent exhaustive check of Round Eleven origin-marker lemmas V/M.
No imports from Claude's round 9/10/11 modules.
"""
from itertools import product
from collections import Counter
A=set('ac'); B=set('bc'); CS=3

def windows(w, alph):
    pos=[i for i,c in enumerate(w) if c in alph]
    return [(pos[k],pos[k+1],w[pos[k]]+w[pos[k+1]]) for k in range(len(pos)-1)]

def marks(w):
    mark=set(); count=Counter()
    for alph in (A,B):
        for i,j,e in windows(w,alph):
            count[(frozenset(alph),e)]+=1
            if count[(frozenset(alph),e)]<=CS: mark.update((i,j))
    return mark

def nu(w,letter):return sum(letter in block for block in w.split('c')[1:-1])

def check(w):
    mark=marks(w); cp=[i for i,c in enumerate(w) if c=='c']; n=len(cp)
    blocks=w.split('c')
    # M1--M7 provenance positions
    for l in 'ab':
        occupied=[s for s in range(1,n) if l in blocks[s]]
        if occupied:
            s0=occupied[0]
            start=cp[s0-1]+1
            fst=start+blocks[s0].index(l)
            assert {cp[s0-1],fst} <=mark,('M1',w,l,s0,mark)
        occ_ac=[s for s in range(n) if l in blocks[s]]
        for s in occ_ac[:min(2,len(occ_ac))]:
            last=(0 if s==0 else cp[s-1]+1)+blocks[s].rindex(l)
            assert {last,cp[s]}<=mark,('M2',w,l,s,mark)
        if n and nu(w,l)==0:
            if l in blocks[0]:
                last=blocks[0].rindex(l)
                assert {last,cp[0]}<=mark,('M3',w,l,mark)
            if l in blocks[-1]:
                fst=cp[-1]+1+blocks[-1].index(l)
                assert {cp[-1],fst}<=mark,('M3tail',w,l,mark)
        if l in w and len(''.join(c for c in w if c in (set(l)|{'c'})))>=2:
            assert w.index(l) in mark,('M4',w,l,mark)
    for l in 'ab':
        for i,j,e in windows(w,set(l+'c')):
            if e==l+l:
                assert {i,j}<=mark,('M5',w,l,mark)
                break
    if n>=2: assert cp[0] in mark,('M6',w,mark)
    for l in 'ab':
        if n>=2 and w.index(l)<cp[0] if l in w else False:
            assert cp[1] in mark,('M7-left',w,l,mark)
        if n>=3 and l in blocks[1]:
            assert cp[2] in mark,('M7-inner',w,l,mark)
    # V: every unmarked contiguous original interval in non-rich block
    if n:
        for l in 'ab':
            if nu(w,l)==0:
                for i in range(len(w)):
                    if i in mark:continue
                    for j in range(i+1,len(w)+1):
                        if j-1 in mark: break
                        s=w[i:j]
                        assert not(l in s and 'c' in s),('V',w,l,i,j,s,mark)
    return len(mark)

N=0
for n in range(1,11):
    for seq in product('abc',repeat=n):
        w=''.join(seq)
        try:check(w)
        except AssertionError as e:
            print('FAIL',e);raise
        N+=1
print('ALL INDEPENDENT LOCAL CHECKS PASSED, words=',N)
END SOURCE independent_round11_local_audit_2026-11-15.py

### Independent local log — `out_independent_round11_local_audit_2026-11-15.txt`

BEGIN SOURCE out_independent_round11_local_audit_2026-11-15.txt
ALL INDEPENDENT LOCAL CHECKS PASSED, words= 88572
END SOURCE out_independent_round11_local_audit_2026-11-15.txt

### Round ten HC checker dependency — `check_round10_HC_exhaustiveness_2026-11-14.py`

BEGIN SOURCE check_round10_HC_exhaustiveness_2026-11-14.py
#!/usr/bin/env python3
"""Round 10 (fan-out 2, rank 2, overlapping projections A={a,c}, B={b,c}, ell=2):
HC exhaustiveness checker.  Python 3 standard library only.  Independent of the
round-7/8 modules (hc_core, hc3_construct) and of the round-9 Instance class.

Run:   python3 check_round10_HC_exhaustiveness_2026-11-14.py [--seed N] [--rand K]
Exit 0 and final line ALL CHECKS PASSED on success (failures of the joint-hosting
property J are REPORTED, not asserted, because J is the object under test).

Sections
  [0] dat_ov <-> Gamma bijection on all words of length <= 8 (independent code).  [1] hosting oracle (Gamma-level, free arrangement inside c-segments) == brute
      force over every member of each dat_ov class, words <= 7, holes: all single
      words <= 3 and all ordered pairs of words <= 2 (gap >= 1).
  [2] Lemma H** (general expansion): for every conservative D with coefficients
      <= 2 and every h (|h|<=3) with R(D) <= alph(h): t=expand(h,D) has
      alph(t)=alph(h) and N2(pi_X(u t v)) - N2(pi_X(u h v)) = D_X for ALL contexts
      u,v of length <= 2 and 300 random longer ones.
  [3] Lemma P0 (total-N2 form): 2-tuples bucketed by (per-component shat_2 and
      content, total N2 per projection); every bucket pair gives equal dat_ov in
      every tested admissible context, incl. pairs whose PER-COMPONENT N2 differ.
  [4] Adversarial model of one shortening stage (superset of real stages), all
      Z-type combinations; search for joint hosting J with e<=2 holes |h|<=3.
      [4a] exhaustive (d=1, |x|<=7); [4b] random; [4d] planted eta shapes behind mark absorbers;
      [4e] sparse / rigid-like roots; [4g] non-rich roots carrying transitional deletions.
      [4f] every case is classified by which hand proof of the report covers it (T1..T5, CITED
      HC_I/II/III, or OPEN) and J failures are counted per class.
  [5] Negative controls: e=1 only; one hole per kappa without merging; c*=1.
  Model = superset of real stages: psi^(j') arbitrary nonempty words with |pi_X psi|>=2 when
  Z_{kappa,X}!=0; Z_kappa any conservative sub-multiset of the unmarked internal windows of
  phi_kappa; T any state with min(N0,c*) <= T <= N0 - Z (B6 range) that is realisable.
"""
import sys, random, itertools, time
from collections import Counter

A = frozenset('ac'); B = frozenset('bc'); PROJ = (('A', A), ('B', B))
LOG = []
STATSH = Counter()
def log(*a):
    s = ' '.join(str(x) for x in a); LOG.append(s); print(s, flush=True)

# ------------------------------------------------------------------ data (independent)
def proj(w, X): return ''.join(ch for ch in w if ch in X)
def shat(u): return ('w', u) if len(u) < 2 else ('ps', u[0], u[-1])
def N2(u):
    C = Counter()
    for i in range(len(u) - 1): C[u[i:i + 2]] += 1
    return C
def side(w, X): u = proj(w, X); return (shat(u), N2(u))
def dat(w): return tuple((s, tuple(sorted(n.items()))) for s, n in (side(w, A), side(w, B)))

def gamma(w):
    segs = w.split('c'); n = len(segs) - 1
    out = [n]
    for L in 'ab':
        al = [s.count(L) for s in segs]; tot = sum(al)
        if n == 0: out += [tot, tot > 0, tot > 0, 0]
        else: out += [tot, al[0] > 0, al[-1] > 0, sum(1 for v in al[1:-1] if v)]
    return tuple(out)

def gamma_side(sh, N, L):
    """(n, tot, first, last, nu) of the projection onto {L,c} from (shat, N2); None if inconsistent."""
    if sh[0] == 'w':
        u = sh[1]
        if sum(N.values()) != 0: return None
        segs = u.split('c'); n = len(segs) - 1; al = [s.count(L) for s in segs]
        if n == 0: return (0, al[0], al[0] > 0, al[0] > 0, 0)
        return (n, sum(al), al[0] > 0, al[-1] > 0, sum(1 for v in al[1:-1] if v))
    f, l = sh[1], sh[2]
    cc, Lc, cL, LL = N.get('cc', 0), N.get(L + 'c', 0), N.get('c' + L, 0), N.get(L + L, 0)
    n = cc + Lc + (f == 'c')
    if n != cc + cL + (l == 'c'): return None
    tot = LL + cL + (f == L); blocks = cL + (f == L)
    if n == 0:
        if f != L or l != L or tot < 2: return None
        return (0, tot, True, True, 0)
    a0 = f == L; an = l == L; nu = blocks - a0 - an
    if nu < 0 or nu > n - 1 or tot < blocks or Lc != blocks - an or cc != (n - 1) - nu: return None
    return (n, tot, a0, an, nu)

def gamma_from_state(st):
    """st = {'A':(shat,Counter),'B':(shat,Counter)} -> Gamma or None."""
    ga = gamma_side(st['A'][0], st['A'][1], 'a'); gb = gamma_side(st['B'][0], st['B'][1], 'b')
    if ga is None or gb is None or ga[0] != gb[0]: return None
    if ga[1] == 0 and gb[1] == 0 and ga[0] == 0: return None
    return (ga[0],) + ga[1:] + gb[1:]

# ------------------------------------------------------------------ Gamma -> segment sequences
_SEQ = {}
def seqs(n, tot, f, l, nu):
    key = (n, tot, f, l, nu)
    if key in _SEQ: return _SEQ[key]
    out = []
    if n == 0:
        out = [(tot,)] if (tot > 0) == f else []
    else:
        for inner in itertools.combinations(range(1, n), nu):
            S = ([0] if f else []) + list(inner) + ([n] if l else [])
            k = len(S)
            if k == 0:
                if tot == 0: out.append(tuple([0] * (n + 1)))
                continue
            if tot < k: continue
            for cuts in itertools.combinations(range(1, tot), k - 1):
                parts = [b - a for a, b in zip((0,) + cuts, cuts + (tot,))]
                v = [0] * (n + 1)
                for s, p in zip(S, parts): v[s] = p
                out.append(tuple(v))
    _SEQ[key] = out
    return out

def arrangements(G):
    n = G[0]
    for al in seqs(n, *G[1:5]):
        for be in seqs(n, *G[5:9]):
            if n == 0 and al[0] + be[0] == 0: continue
            yield al, be

# ------------------------------------------------------------------ hosting
def pieces(h):
    ps = h.split('c'); k = len(ps) - 1
    return ps, k

def hole_touches(h, i):
    ps, k = pieces(h)
    if k == 0: return [(i, 'in', ps[0])]
    return [(i, 'suf', ps[0])] + [(i + m, 'full', ps[m]) for m in range(1, k)] + [(i + k, 'pre', ps[k])]

def seg_ok(al, be, ds):
    if any(k == 'full' for k, _ in ds):
        if len(ds) != 1: return False
        p = ds[0][1]; return al == p.count('a') and be == p.count('b')
    if sum(1 for k, _ in ds if k == 'pre') > 1 or sum(1 for k, _ in ds if k == 'suf') > 1: return False
    na = sum(p.count('a') for _, p in ds); nb = sum(p.count('b') for _, p in ds)
    return na <= al and nb <= be and al + be >= na + nb + (len(ds) - 1)

def place_comp(al, be, holes):
    """Return list of start segments for the holes (in order) or None."""
    n = len(al) - 1
    def rec(j, last_seg, last_kind, dem, starts):
        if j == len(holes):
            for s, ds in dem.items():
                if not seg_ok(al[s], be[s], ds): return None
            return list(starts)
        h = holes[j]; k = pieces(h)[1]
        lo = 0 if last_seg is None else last_seg
        for i in range(lo, n - k + 1):
            tch = hole_touches(h, i)
            if last_seg is not None and i == last_seg:
                if last_kind not in ('pre', 'in') or tch[0][1] not in ('suf', 'in'): continue
            d2 = {s: list(v) for s, v in dem.items()}
            bad = False
            for s, kind, p in tch:
                d2.setdefault(s, []).append((kind, p))
                if kind == 'full' and len(d2[s]) > 1: bad = True
            if bad: continue
            # quick count prune
            if any(not seg_ok_partial(al[s], be[s], d2[s]) for s, _, _ in tch): continue
            r = rec(j + 1, tch[-1][0], tch[-1][1], d2, starts + [i])
            if r is not None: return r
        return None
    return rec(0, None, None, {}, [])

def seg_ok_partial(al, be, ds):
    if any(k == 'full' for k, _ in ds) and len(ds) > 1: return False
    na = sum(p.count('a') for _, p in ds); nb = sum(p.count('b') for _, p in ds)
    return na <= al and nb <= be

def build_comp(al, be, holes, starts):
    """Construct the word and literal hole spans for an accepted placement."""
    n = len(al) - 1
    dem = {}
    for j, (h, i) in enumerate(zip(holes, starts)):
        for s, kind, p in hole_touches(h, i): dem.setdefault(s, []).append((j, kind, p))
    segtxt = []; marks = []   # per segment: list of (text, hole_id or None, part)
    for s in range(n + 1):
        ds = dem.get(s, [])
        ra = al[s] - sum(p.count('a') for _, _, p in ds); rb = be[s] - sum(p.count('b') for _, _, p in ds)
        rest = ['a'] * ra + ['b'] * rb
        full = [d for d in ds if d[1] == 'full']
        if full:
            segtxt.append([(full[0][2], full[0][0])]); continue
        pre = [d for d in ds if d[1] == 'pre']; ins = [d for d in ds if d[1] == 'in']; suf = [d for d in ds if d[1] == 'suf']
        order = pre + ins + suf
        parts = []
        for idx, d in enumerate(order):
            if idx > 0:
                parts.append((rest.pop(), None))
            parts.append((d[2], d[0]))
        if not order:
            parts = [(''.join(rest), None)]; rest = []
        else:
            # leftover letters: put between first hole piece and second if that is not 'pre'-anchored,
            # else right after the 'pre' piece (never before a pre or after a suf)
            if rest:
                pos = 1 if order[0][1] == 'pre' else 0
                parts.insert(pos, (''.join(rest), None)); rest = []
        segtxt.append(parts)
    # assemble with c's; holes may span c's
    word = []; spans = {}
    for s, parts in enumerate(segtxt):
        for txt, hid in parts:
            if hid is not None:
                st = len(word)
                if hid not in spans: spans[hid] = [st, st]
            word.extend(txt)
            if hid is not None: spans[hid][1] = len(word)
        if s < n:
            # the c belongs to a hole if some hole touches s with suf/full and s+1 with full/pre
            for j, (h, i) in enumerate(zip(holes, starts)):
                ks = pieces(h)[1]
                if i <= s < i + ks:
                    if j not in spans: spans[j] = [len(word), len(word)]
            word.append('c')
            for j, (h, i) in enumerate(zip(holes, starts)):
                ks = pieces(h)[1]
                if i <= s < i + ks: spans[j][1] = len(word)
    w = ''.join(word)
    sp = [tuple(spans[j]) for j in range(len(holes))]
    # hole spans: start must be the start of its first piece; recompute by literal search consistent with order
    return w, sp


def feasible_seq(n, tot, f, l, nu, dem):
    """A segment-count sequence for one letter with Gamma data (n,tot,f,l,nu) meeting per-segment
    demands dem: s -> ('exact', v) | ('lb', v); None if impossible.  Exact (proof in report §3.2)."""
    if n == 0:
        d = dem.get(0)
        if (tot > 0) != f: return None
        if d is None or (d[0] == 'exact' and d[1] == tot) or (d[0] == 'lb' and tot >= d[1]): return (tot,)
        return None
    forced = {s for s, (k, v) in dem.items() if v >= 1}
    forbid = {s for s, (k, v) in dem.items() if k == 'exact' and v == 0}
    for s, flag in ((0, f), (n, l)):
        if flag and s in forbid: return None
        if not flag and s in forced: return None
    fi = [s for s in forced if 0 < s < n]; fb = [s for s in forbid if 0 < s < n]
    if len(fi) > nu or nu > (n - 1) - len(fb): return None
    free = [s for s in range(1, n) if s not in forced and s not in forbid]
    S = set(fi) | set(free[:nu - len(fi)]) | ({0} if f else set()) | ({n} if l else set())
    vals = {}; slack = None
    for s in sorted(S):
        d = dem.get(s)
        if d and d[0] == 'exact': vals[s] = d[1]
        else: vals[s] = max(1, d[1] if d else 0); slack = s
    tt = sum(vals.values())
    if tt > tot: return None
    if tt < tot:
        if slack is None: return None
        vals[slack] += tot - tt
    return tuple(vals.get(s, 0) for s in range(n + 1))

def host_comp(G, holes):
    """(alpha, beta, starts) placing the holes in order (gap>=1) in some realisation of G, or None."""
    n = G[0]
    if not holes:
        al = feasible_seq(n, *G[1:5], {}); be = feasible_seq(n, *G[5:9], {})
        return (al, be, []) if al is not None and be is not None else None
    def leaf(dem):
        segs = sorted(dem)
        base = {}
        for sg in segs:
            ds = dem[sg]
            if any(k == 'full' for k, _ in ds):
                if len(ds) != 1: return None
                base[sg] = ('exact', ds[0][1].count('a'), ds[0][1].count('b'), 0)
            else:
                if sum(1 for k, _ in ds if k == 'pre') > 1 or sum(1 for k, _ in ds if k == 'suf') > 1: return None
                base[sg] = ('lb', sum(p.count('a') for _, p in ds), sum(p.count('b') for _, p in ds), len(ds) - 1)
        gs = [sg for sg in segs if base[sg][3] > 0]
        for split in itertools.product(*[range(base[sg][3] + 1) for sg in gs]):
            ga = dict(zip(gs, split))
            dA = {}; dB = {}
            for sg in segs:
                k, na, nb, g = base[sg]
                if k == 'exact': dA[sg] = ('exact', na); dB[sg] = ('exact', nb)
                else:
                    x = ga.get(sg, 0); dA[sg] = ('lb', na + x); dB[sg] = ('lb', nb + g - x)
            al = feasible_seq(n, *G[1:5], dA)
            if al is None: continue
            be = feasible_seq(n, *G[5:9], dB)
            if be is None: continue
            if n == 0 and al[0] + be[0] == 0: continue
            return al, be
        return None
    def rec(j, last_seg, last_kind, dem, starts):
        if j == len(holes):
            r = leaf(dem)
            return None if r is None else (r[0], r[1], list(starts))
        h = holes[j]; k = pieces(h)[1]
        lo = 0 if last_seg is None else last_seg
        for i in range(lo, n - k + 1):
            tch = hole_touches(h, i)
            if last_seg is not None and i == last_seg:
                if last_kind not in ('pre', 'in') or tch[0][1] not in ('suf', 'in'): continue
            d2 = {sg: list(v) for sg, v in dem.items()}
            bad = False
            for sg, kind, pc in tch:
                d2.setdefault(sg, []).append((kind, pc))
                if any(kk == 'full' for kk, _ in d2[sg]) and len(d2[sg]) > 1: bad = True
            if bad: continue
            r = rec(j + 1, tch[-1][0], tch[-1][1], d2, starts + [i])
            if r is not None: return r
        return None
    return rec(0, None, None, {}, [])

def hosts_enum(G, holes):
    """reference implementation by full enumeration of segment sequences (small G only)."""
    for al, be in arrangements(G):
        if place_comp(al, be, holes) is not None: return True
    return False

_HC = {}
def longp(G):
    return frozenset(x for x, ok in (('A', G[0] + G[1] >= 2), ('B', G[0] + G[5] >= 2)) if ok)

def hosts(Gs, holes, want=False, req=None):
    """Gs: tuple of component Gammas (in order).  holes: tuple of words (in order).
    Holes in the same component need a nonempty gap; different components are separated by
    the (admissible) context.  Returns bool, or (words, [(comp, start, end)]) if want."""
    key = (Gs, holes, req)
    if not want and key in _HC: return _HC[key]
    d = len(Gs); res = False
    for assign in itertools.combinations_with_replacement(range(d), len(holes)):
        if req is not None and any(not (req[j] <= longp(Gs[assign[j]])) for j in range(len(holes))): continue
        groups = [[j for j in range(len(holes)) if assign[j] == i] for i in range(d)]
        sol = []
        ok = True
        for i in range(d):
            hs = tuple(holes[j] for j in groups[i])
            found = host_comp(Gs[i], hs)
            if found is None: ok = False; break
            sol.append(found)
        if ok:
            res = True
            if want:
                words = []; spans = []
                for i in range(d):
                    al, be, st = sol[i]; hs = [holes[j] for j in groups[i]]
                    w, sp = build_comp(al, be, hs, st)
                    words.append(w)
                    for j, (s0, s1) in zip(groups[i], sp): spans.append((j, i, s0, s1))
                spans.sort()
                return words, [(i, s0, s1) for _, i, s0, s1 in spans]
            break
    _HC[key] = res
    if want: return None
    return res

def literal_hosts(w, holes):
    """brute: holes occur in w in order, nonoverlapping, gap >= 1."""
    def rec(j, start):
        if j == len(holes): return True
        h = holes[j]; p = w.find(h, start)
        while p != -1:
            if rec(j + 1, p + len(h) + 1): return True
            p = w.find(h, p + 1)
        return False
    return rec(0, 0)

# ------------------------------------------------------------------ conservative differences
def Dvec(DA, DB):
    """(p,q,r,p2,q2,r2) from Counters; asserts circulation form."""
    assert DA.get('ac', 0) == DA.get('ca', 0) and DB.get('bc', 0) == DB.get('cb', 0)
    return (DA.get('aa', 0), DA.get('cc', 0), DA.get('ac', 0), DB.get('bb', 0), DB.get('cc', 0), DB.get('bc', 0))
def conservative(D): return D[1] + D[2] == D[4] + D[5] and min(D) >= 0
def Dzero(D): return not any(D)
def Dadd(D, E): return tuple(x + y for x, y in zip(D, E))
def Dsub(D, E): return tuple(x - y for x, y in zip(D, E))
def R_of(D):
    p, q, r, p2, q2, r2 = D; s = set()
    if p or r: s.add('a')
    if p2 or r2: s.add('b')
    if q + r: s.add('c')
    return frozenset(s)
def Dcounters(D):
    p, q, r, p2, q2, r2 = D
    return (Counter({k: v for k, v in (('aa', p), ('cc', q), ('ac', r), ('ca', r)) if v}),
            Counter({k: v for k, v in (('bb', p2), ('cc', q2), ('bc', r2), ('cb', r2)) if v}))

def expand(h, D):
    """Lemma H**: t with alph(t)=alph(h) and context-free bigram difference D."""
    p, q, r, p2, q2, r2 = D; m = q + r
    assert conservative(D) and m == q2 + r2
    R = R_of(D); assert R <= set(h), (h, D)
    out = []; done_c = done_a = done_b = False
    for ch in h:
        if ch == 'c' and m > 0 and not done_c:
            al = ['a' * (1 + (p if (k == 0 and r > 0) else 0)) if k < r else '' for k in range(m)]
            be = ['b' * (1 + (p2 if (k == 0 and r2 > 0) else 0)) if k < r2 else '' for k in range(m)]
            out.append('c' + ''.join(x + y + 'c' for x, y in zip(al, be))); done_c = True
        elif ch == 'a' and p > 0 and r == 0 and not done_a:
            out.append('a' * (1 + p)); done_a = True
        elif ch == 'b' and p2 > 0 and r2 == 0 and not done_b:
            out.append('b' * (1 + p2)); done_b = True
        else:
            out.append(ch)
    return ''.join(out)

def splits(D):
    """All ordered conservative splits D=D1+D2 with D1,D2 nonzero (deduplicated by (R1,R2))."""
    seen = {}
    for D1 in itertools.product(*[range(v + 1) for v in D]):
        D2 = Dsub(D, D1)
        if Dzero(D1) or Dzero(D2) or not conservative(D1) or not conservative(D2): continue
        key = (R_of(D1), R_of(D2))
        if key not in seen: seen[key] = (D1, D2)
    return list(seen.values())

ALLW = [''.join(p) for n in (1, 2, 3) for p in itertools.product('abc', repeat=n)]
def cands(R): return [h for h in ALLW if R <= set(h)]

def reqX(D):
    p, q, r, p2, q2, r2 = D
    return frozenset(x for x, nz in (('A', p or q or r), ('B', p2 or q2 or r2)) if nz)

def joint(GF, GY, D, emax=2, merge=True, perkappa=None):
    """Search J.  GF: Gamma of W_{j'} (1 component); GY: tuple of Gammas of T.
    Y-side holes must sit in a component whose pi_X is long for every X with D_X != 0.
    Returns (e, holes, Ds) or None."""
    R = R_of(D)
    hF = {h for h in ALLW if hosts((GF,), (h,))}
    hY = {h for h in ALLW if hosts(GY, (h,))}
    if merge:
        for h in cands(R):
            if h in hF and h in hY and hosts(GY, (h,), req=(reqX(D),)): return (1, (h,), (D,))
    if emax < 2: return None
    sp = splits(D) if merge else ([perkappa] if perkappa else [])
    for D1, D2 in sp:
        c1 = [h for h in cands(R_of(D1)) if h in hF and h in hY]
        c2 = [h for h in cands(R_of(D2)) if h in hF and h in hY]
        for h1 in c1:
            for h2 in c2:
                if hosts((GF,), (h1, h2)) and hosts(GY, (h1, h2), req=(reqX(D1), reqX(D2))):
                    return (2, (h1, h2), (D1, D2))
    return None

# ------------------------------------------------------------------ the stage model
def windows_of(w, X):
    idx = [i for i, ch in enumerate(w) if ch in X]
    return list(zip(idx, idx[1:]))

def marks_of(x, cstar):
    M = set()
    for X in (A, B):
        seen = Counter()
        for p, q in windows_of(x, X):
            e = x[p] + x[q]; seen[e] += 1
            if seen[e] <= cstar: M |= {p, q}
    return M

def internal_counts(phi):
    return {Xn: N2(proj(phi, X)) for Xn, X in PROJ}

def z_options(phi, rng=None, cap=None):
    """All conservative Z (as 6-vectors) bounded by the internal windows of phi."""
    C = internal_counts(phi); a = C['A']; b = C['B']
    rA = min(a['ac'], a['ca']); rB = min(b['bc'], b['cb'])
    out = []
    for p in range(a['aa'] + 1):
        for q in range(a['cc'] + 1):
            for r in range(rA + 1):
                for p2 in range(b['bb'] + 1):
                    for r2 in range(rB + 1):
                        q2 = q + r - r2
                        if 0 <= q2 <= b['cc']: out.append((p, q, r, p2, q2, r2))
    if cap and len(out) > cap and rng: out = [out[0]] + rng.sample(out[1:], cap - 1)
    return out

def state_of(x):
    return {Xn: (shat(proj(x, X)), N2(proj(x, X))) for Xn, X in PROJ}

def T_options(x, Zi, cstar, rng, k):
    st = state_of(x); res = []
    keys = [(Xn, e) for Xn in ('A', 'B') for e in sorted(st[Xn][1])]
    zc = dict(zip(('A', 'B'), Dcounters(Zi)))
    ranges = []
    for Xn, e in keys:
        N0 = st[Xn][1][e]; lo = min(N0, cstar); hi = N0 - zc[Xn].get(e, 0)
        assert lo <= hi, ('unmarked bound', x, Xn, e)
        ranges.append((lo, hi))
    choices = [tuple(lo for lo, _ in ranges), tuple(hi for _, hi in ranges)]
    for _ in range(k): choices.append(tuple(rng.randint(lo, hi) for lo, hi in ranges))
    seen = set()
    for ch in choices:
        if ch in seen: continue
        seen.add(ch)
        T = {Xn: (st[Xn][0], Counter()) for Xn in ('A', 'B')}
        for (Xn, e), v in zip(keys, ch):
            if v: T[Xn][1][e] = v
        G = gamma_from_state(T)
        if G is not None: res.append((T, G))
    return res

def realizable_gamma_contents(G, x):
    """content of any realisation equals content of x."""
    cont = set()
    if G[0] > 0: cont.add('c')
    if G[1] > 0: cont.add('a')
    if G[5] > 0: cont.add('b')
    return cont == set(x)

def phi_choices(xs, M, cstar):
    """All eta component layouts: 1 or 2 nonempty unmarked factors; same comp => gap >= 1."""
    ivs = []
    for i, x in enumerate(xs):
        for s in range(len(x)):
            for e in range(s + 1, len(x) + 1):
                if all(p not in M[i] for p in range(s, e)): ivs.append((i, s, e))
    out = [(iv,) for iv in ivs]
    for u, v in itertools.combinations(ivs, 2):
        if u[0] == v[0]:
            if not (u[2] < v[1] or v[2] < u[1]): continue   # overlap or adjacent
            if v[1] < u[1]: u, v = v, u
        out.append((u, v))
    return out

def ztype(Z):
    p, q, r, p2, q2, r2 = Z
    R = ''.join(sorted(R_of(Z)))
    if R != 'abc': return R
    if p and p2: return 'abc+'          # some kappa deletes aa AND bb (HC_I/II/III territory)
    if r and r2: return 'abc2'          # doubly transitional
    return 'abcA' if r else 'abcB'      # semi-transitional (r>0,r'=0,p'>0,p=0) / mirror

PROVED_SINGLE = {'a', 'b', 'c', 'ac', 'bc', 'abc2'}
def rich(x):
    """Lemma T5 hypothesis: nu_A>=1, nu_B>=1 and at least 3 c's."""
    g = gamma(x); return g[0] >= 3 and g[4] >= 1 and g[8] >= 1

def classify(Zs, layout, xs=None):
    """Which hand proof of the round-10 report covers this stage (section 3 of the report)."""
    nz = [(Z, iv) for Z, iv in zip(Zs, layout) if not Dzero(Z)]
    if xs is not None and any(rich(x) for x in xs): return 'PROVED:T5-rich-component'
    if any(Z[0] > 0 and Z[3] > 0 for Z, _ in nz): return 'CITED-HC_I/II/III'
    ts = [ztype(Z) for Z, _ in nz]
    if len(nz) == 1:
        return 'PROVED:T1-single-' + ts[0] if ts[0] in PROVED_SINGLE else 'OPEN:semi-single-' + ts[0]
    (Z1, i1), (Z2, i2) = nz; t1, t2 = ts; same = i1[0] == i2[0]
    if 'abc2' in ts: return 'PROVED:T3-merge-into-abc2'
    for (Za, ta), (Zb, tb) in (((Z1, t1), (Z2, t2)), ((Z2, t2), (Z1, t1))):
        if ta in PROVED_SINGLE and R_of(Zb) <= R_of(Za) and reqX(Zb) <= reqX(Za): return 'PROVED:T3-merge'
    if set(ts) <= {'a', 'b', 'c'}: return 'PROVED:T2-letter-pair'
    if not same and set(ts) in ({'ac', 'b'}, {'bc', 'a'}, {'ac', 'bc'}): return 'PROVED:T4-transitional-diff-root'
    return 'OPEN:%s/%s:%s' % (min(t1, t2), max(t1, t2), 'same' if same else 'diff')

def run_config(xs, ctx, cstar, layout, Zs, psis, Ts, stats, fails, tag, controls=True):
    d = len(xs)
    # W_{j'}
    xp = []
    for i, x in enumerate(xs):
        segs = []; pos = 0
        for (kk, (ci, s, e)) in sorted([(k, iv) for k, iv in enumerate(layout) if iv[0] == i], key=lambda t: t[1][1]):
            segs.append(x[pos:s]); segs.append(psis[kk]); pos = e
        segs.append(x[pos:]); xp.append(''.join(segs))
    if d == 1: W = ctx[0] + xp[0] + ctx[1]
    else: W = ctx[0] + xp[0] + ctx[1] + xp[1] + ctx[2]
    GF = gamma(W)
    D = (0,) * 6
    for Z in Zs: D = Dadd(D, Z)
    if Dzero(D): return
    covered = any(Z[0] > 0 and Z[3] > 0 for Z in Zs)
    types = tuple(''.join(sorted(R_of(Z))) or '0' for Z in Zs)
    same = len(layout) == 2 and layout[0][0] == layout[1][0]
    sig = (types, 'same' if same else ('diff' if len(layout) == 2 else 'one'), 'prevHC' if covered else 'NEW')
    cls = classify(Zs, layout, xs)
    for T, GT in Ts:
        GY = GT
        stats['cls:' + cls] += 1
        stats['cases'] += 1; stats['sig:' + '/'.join(sig[0]) + ':' + sig[1] + ':' + sig[2]] += 1
        if not covered: stats['cases_not_prevHC'] += 1
        res = joint(GF, GY, D)
        if res is None:
            stats['J_fail'] += 1; stats['clsfail:' + cls] += 1
            if not covered: stats['J_fail_not_prevHC'] += 1
            if len(fails) < 30:
                fails.append((tag, xs, ctx, cstar, layout, Zs, psis, W, GF, GY, sig))
            continue
        stats['J_ok_e%d' % res[0]] += 1
        if res[0] == 2 and stats['ex_e2'] < 2:
            stats['ex_e2'] += 1
            log('    [e=2 example] %s x=%s ctx=%s c*=%d layout=%s Z=%s psi=%s W_jprime=%s Gamma(W)=%s Gamma(T)=%s holes=%s split=%s sig=%s'
                % (tag, xs, ctx, cstar, layout, Zs, psis, W, GF, GY, res[1], res[2], sig))
        # verify the witness constructively (words, hole spans, expansions)
        e, holes, Ds = res
        wf = hosts((GF,), holes, want=True); wy = hosts(GY, holes, want=True, req=tuple(reqX(Di) for Di in Ds))
        assert wf and wy
        Wst = wf[0][0]; assert gamma(Wst) == GF and dat(Wst) == dat(W)
        for (ci, s0, s1), h in zip(wf[1], holes): assert Wst[s0:s1] == h, (Wst, wf, holes)
        if e == 2: assert wf[1][0][2] < wf[1][1][1], 'F gap'
        for i, yw in enumerate(wy[0]): assert gamma(yw) == GY[i]
        for (ci, s0, s1), h in zip(wy[1], holes): assert wy[0][ci][s0:s1] == h
        if e == 2 and wy[1][0][0] == wy[1][1][0]: assert wy[1][0][2] < wy[1][1][1], 'Y gap'
        # F[t] has dat(W_j) := dat(W_{j'}) + D  (checked on the N2 level, shat level)
        Ft = list(Wst); off = 0
        for (ci, s0, s1), h, Di in zip(wf[1], holes, Ds):
            t = expand(h, Di); assert set(t) == set(h)
            Ft[s0 + off:s1 + off] = list(t); off += len(t) - len(h)
        Ft = ''.join(Ft)
        for (Xn, X), Dx in zip(PROJ, Dcounters(D)):
            diff = N2(proj(Ft, X)); diff.subtract(N2(proj(Wst, X)))
            assert +diff == Dx and not -diff, ('F[t]', Xn)
            assert shat(proj(Ft, X)) == shat(proj(Wst, X))
        # Y side: y^pi = y'[h->t] keeps per-component shat_2 and content (P0 premise)
        ys = list(wy[0])
        for (ci, s0, s1), h, Di in sorted(zip(wy[1], holes, Ds), key=lambda z: (z[0][0], -z[0][1])):
            t = expand(h, Di); ys[ci] = ys[ci][:s0] + t + ys[ci][s1:]
        for i in range(len(ys)):
            assert set(ys[i]) == set(wy[0][i])
            for _, X in PROJ: assert shat(proj(ys[i], X)) == shat(proj(wy[0][i], X)), 'Y shat'
        for (Xn, X), Dx in zip(PROJ, Dcounters(D)):
            tot = Counter()
            for i in range(len(ys)): tot += N2(proj(ys[i], X))
            tot0 = Counter()
            for i in range(len(ys)): tot0 += N2(proj(wy[0][i], X))
            tot.subtract(tot0); assert +tot == Dx and not -tot, 'Y total'
        if controls:
            if joint(GF, GY, D, emax=1) is None: stats['ctrl_e1_fail'] += 1
            nz = [Z for Z in Zs if not Dzero(Z)]
            if len(nz) == 2:
                if joint(GF, GY, D, merge=False, perkappa=(nz[0], nz[1])) is None and \
                   joint(GF, GY, D, merge=False, perkappa=(nz[1], nz[0])) is None:
                    stats['ctrl_perkappa_fail'] += 1

def stage_iter(xs, ctx, cstar, rng, zcap, tk, psik, exhaustive_phi=True):
    M = [marks_of(x, cstar) for x in xs]
    for layout in phi_choices(xs, M, cstar):
        phis = [xs[i][s:e] for i, s, e in layout]
        opts = [z_options(ph, rng, zcap) for ph in phis]
        for Zs in itertools.product(*opts):
            if all(Dzero(Z) for Z in Zs): continue
            psis_list = []
            for _ in range(psik):
                ps = []
                for Z, ph in zip(Zs, phis):
                    while True:
                        w = ''.join(rng.choice('abc') for _ in range(rng.randint(1, 4)))
                        if (Z[0] or Z[1] or Z[2]) and len(proj(w, A)) < 2: continue
                        if (Z[3] or Z[4] or Z[5]) and len(proj(w, B)) < 2: continue
                        break
                    ps.append(w)
                psis_list.append(ps)
            Ts_per = []
            for i, x in enumerate(xs):
                Zi = (0,) * 6
                for Z, iv in zip(Zs, layout):
                    if iv[0] == i: Zi = Dadd(Zi, Z)
                Ts_per.append(T_options(x, Zi, cstar, rng, tk))
            Ts = []
            for combo in itertools.product(*Ts_per):
                Ts.append((tuple(t for t, _ in combo), tuple(g for _, g in combo)))
            for psis in psis_list:
                yield layout, Zs, psis, Ts

def gen_word(rng, L):
    """biased long words: runs and motifs so that every window type recurs > c* times."""
    motifs = ['a', 'b', 'c', 'aa', 'bb', 'cc', 'ab', 'ba', 'ac', 'ca', 'bc', 'cb', 'abc', 'cab', 'acb', 'bca']
    w = ''
    style = rng.random()
    while len(w) < L:
        if style < 0.3: w += rng.choice(motifs)
        elif style < 0.6: w += rng.choice('abc') * rng.randint(1, 4)
        else:
            m = rng.choice(motifs); w += m * rng.randint(1, 3)
    return w[:L]

def gen_sparse(rng):
    """words with few occupied c-segments and long single-letter runs (rigid-like Gamma, small nu)."""
    n = rng.choice((0, 1, 1, 2, 2, 3, 4)); segs = []
    for i in range(n + 1):
        r = rng.random()
        if r < 0.25: segs.append('')
        elif r < 0.5: segs.append('a' * rng.randint(1, 9))
        elif r < 0.75: segs.append('b' * rng.randint(1, 9))
        else:
            u = 'a' * rng.randint(1, 7) + 'b' * rng.randint(1, 7)
            if rng.random() < 0.5: u = u[::-1]
            if rng.random() < 0.3: u = ''.join(rng.sample(u, len(u)))
            segs.append(u)
    w = ''
    for i, sg in enumerate(segs):
        w += sg
        if i < n: w += 'c' * rng.randint(1, 5)
    return w or 'a'

def gen_nonrich(rng):
    """nu_B = 0 (b only in the end segments) but rich A-transitions in the middle, or the mirror."""
    mid = ''
    while mid.count('c') < rng.randint(5, 9):
        mid += rng.choice(['ac', 'ca', 'a', 'c', 'aac', 'acc', 'cc'])
    if not mid.startswith('c'): mid = 'c' + mid
    if not mid.endswith('c'): mid = mid + 'c'
    u0 = rng.choice(['', 'b' * rng.randint(1, 8), 'a' * rng.randint(1, 4) + 'b' * rng.randint(1, 8),
                     'b' * rng.randint(1, 8) + 'a' * rng.randint(1, 4)])
    un = rng.choice(['', 'b' * rng.randint(1, 8), 'a' * rng.randint(1, 4) + 'b' * rng.randint(1, 8),
                     'b' * rng.randint(1, 8) + 'a' * rng.randint(1, 4)])
    if 'b' not in u0 + un: u0 = 'b' * rng.randint(4, 8)
    w = u0 + mid + un
    if rng.random() < 0.5: w = w.translate(str.maketrans('ab', 'ba'))
    return w

def stage_sample(xs, ctx, cstar, rng, nlay, zcap, tk):
    M = [marks_of(x, cstar) for x in xs]
    free = []
    for i, x in enumerate(xs):
        s = 0
        while s < len(x):
            if s in M[i]: s += 1; continue
            e = s
            while e < len(x) and e not in M[i]: e += 1
            free.append((i, s, e)); s = e    if not free: return
    for _ in range(nlay):
        k = rng.choice((1, 2, 2))
        lay = []
        for _ in range(k):
            i, s, e = rng.choice(free)
            a = rng.randint(s, e - 1); b = rng.randint(a + 1, e); lay.append((i, a, b))
        if k == 2:
            u, v = lay
            if u[0] == v[0]:
                if v[1] < u[1]: u, v = v, u
                if not u[2] < v[1]: continue
                lay = [u, v]
        lay = tuple(lay)
        phis = [xs[i][s:e] for i, s, e in lay]
        opts = [z_options(ph, rng, zcap) for ph in phis]
        combos = list(itertools.product(*opts))
        if len(combos) > zcap: combos = rng.sample(combos, zcap)
        for Zs in combos:
            if all(Dzero(Z) for Z in Zs): continue
            ps = []
            for Z in Zs:
                while True:
                    w = ''.join(rng.choice('abc') for _ in range(rng.randint(1, 4)))
                    if (Z[0] or Z[1] or Z[2]) and len(proj(w, A)) < 2: continue
                    if (Z[3] or Z[4] or Z[5]) and len(proj(w, B)) < 2: continue
                    break
                ps.append(w)
            Ts_per = []
            for i, x in enumerate(xs):
                Zi = (0,) * 6
                for Z, iv in zip(Zs, lay):
                    if iv[0] == i: Zi = Dadd(Zi, Z)
                Ts_per.append(T_options(x, Zi, cstar, rng, tk))
            Ts = [(tuple(t for t, _ in c), tuple(g for _, g in c)) for c in itertools.product(*Ts_per)]
            if len(Ts) > 6: Ts = rng.sample(Ts, 6)
            yield lay, Zs, ps, Ts

def main():
    seed = 20261114; K = 400
    args = sys.argv[1:]
    if '--seed' in args: seed = int(args[args.index('--seed') + 1])
    if '--rand' in args: K = int(args[args.index('--rand') + 1])
    rng = random.Random(seed); t0 = time.time()
    log('== Round 10 HC exhaustiveness checker; seed %d ==' % seed)
    # [0]
    classes = {}
    for n in range(1, 9):
        for p in itertools.product('abc', repeat=n):
            w = ''.join(p); classes.setdefault(dat(w), set()).add(gamma(w))
    assert all(len(v) == 1 for v in classes.values())
    g2d = {}
    for dd, gs in classes.items():
        g = next(iter(gs)); assert g not in g2d; g2d[g] = dd
        st = {'A': (dd[0][0], Counter(dict(dd[0][1]))), 'B': (dd[1][0], Counter(dict(dd[1][1])))}
        assert gamma_from_state(st) == g, (dd, g)
    log('[0] dat_ov <-> Gamma: %d words (len<=8), %d classes, bijective; gamma_from_state agrees on every class'
        % (sum(3 ** n for n in range(1, 9)), len(classes)))
    # [1] hosting oracle vs brute force
    byd = {}
    for n in range(1, 8):
        for p in itertools.product('abc', repeat=n):
            w = ''.join(p); byd.setdefault(dat(w), []).append(w)
    singles = ALLW; pairs = [(u, v) for u in ALLW if len(u) <= 2 for v in ALLW if len(v) <= 2]
    nchk = 0; npos = 0
    for dd, ws in byd.items():
        G = gamma(ws[0])
        for h in singles:
            br = any(literal_hosts(w, (h,)) for w in ws); orc = hosts((G,), (h,))
            if len(ws[0]) <= 6: assert hosts_enum(G, (h,)) == orc
            assert br == orc, ('host1', ws[0], h, br, orc); nchk += 1; npos += br
            if orc:
                wt = hosts((G,), (h,), want=True); assert wt and wt[0][0] in ws and wt[0][0][wt[1][0][1]:wt[1][0][2]] == h
        for hp in pairs:
            br = any(literal_hosts(w, hp) for w in ws); orc = hosts((G,), hp)
            assert br == orc, ('host2', ws[0], hp, br, orc); nchk += 1; npos += br
            if orc:
                wt = hosts((G,), hp, want=True); w0 = wt[0][0]; sp = wt[1]
                assert w0 in ws and w0[sp[0][1]:sp[0][2]] == hp[0] and w0[sp[1][1]:sp[1][2]] == hp[1] and sp[0][2] < sp[1][1]
    log('[1] hosting oracle == brute force over full dat classes (len<=7): %d classes, %d (class,hole-list) checks, %d positive; witnesses rebuilt and verified'
        % (len(byd), nchk, npos))
    # [2] H**
    ctxs = [''.join(p) for n in range(0, 3) for p in itertools.product('abc', repeat=n)]
    rnd = [''.join(rng.choice('abc') for _ in range(rng.randint(0, 8))) for _ in range(300)]
    nD = 0; nh = 0; STATSH.clear()
    for D in itertools.product(range(3), repeat=6):
        if Dzero(D) or not conservative(D): continue
        nD += 1
        for h in cands(R_of(D)):
            t = expand(h, D); assert set(t) == set(h) and t != h; nh += 1
            DA, DB = Dcounters(D)
            for u in ctxs + rnd[:40]:
                for v in ctxs[:13] + rnd[40:60]:
                    for (Xn, X), Dx in zip(PROJ, (DA, DB)):
                        diff = N2(proj(u + t + v, X)); diff.subtract(N2(proj(u + h + v, X)))
                        assert +diff == Dx and not -diff, (h, D, u, v, Xn)
                        if len(proj(u + h + v, X)) >= 2:
                            assert shat(proj(u + t + v, X)) == shat(proj(u + h + v, X))
                        elif Dx:
                            STATSH['short'] += 1
    log('[2] H**: %d conservative D (coeff<=2) x holes containing R(D): %d expansions; N2-difference context-free on %d x %d contexts;'
        ' shat_2 of the whole projection unchanged whenever |pi_X(u h v)|>=2 (the %d short-projection contexts with D_X!=0 are exactly'
        ' the ones excluded by the long-projection side condition)' % (nD, nh, len(ctxs) + 40, 33, STATSH['short']))
    # [3] P0
    buckets = {}
    def key0(tp):
        k = []
        for comp in tp:
            for Xn, X in PROJ: k.append(shat(proj(comp, X)))
            k.append(frozenset(comp))
        for Xn, X in PROJ:
            tot = Counter()
            for comp in tp: tot += N2(proj(comp, X))
            k.append(tuple(sorted(tot.items())))
        return tuple(k)
    for _ in range(60000):
        tp = tuple(''.join(rng.choice('abc') for _ in range(rng.randint(1, 6))) for _ in range(2))
        buckets.setdefault(key0(tp), set()).add(tp)
    npair = 0; ndiffcomp = 0
    for kk, tps in buckets.items():
        tps = sorted(tps)
        if len(tps) < 2: continue
        x = tps[0]
        for y in tps[1:4]:
            npair += 1
            if any(N2(proj(x[i], X)) != N2(proj(y[i], X)) for i in range(2) for _, X in PROJ): ndiffcomp += 1
            for _ in range(8):
                E = [''.join(rng.choice('abc') for _ in range(rng.randint(0, 3))) for _ in range(3)]
                if not E[1]: E[1] = rng.choice('abc')
                assert dat(E[0] + x[0] + E[1] + x[1] + E[2]) == dat(E[0] + y[0] + E[1] + y[1] + E[2])
    assert ndiffcomp > 0
    log('[3] P0 (total-N2 form): %d tuple pairs x 8 admissible contexts, equal dat_ov; %d pairs have DIFFERENT per-component N2'
        % (npair, ndiffcomp))
    # [4] adversarial stage model
    stats = Counter(); fails = []
    # exhaustive: d=1, all x of length 4..7, c*=3, one psi per layout, T extremes + 2 random
    nx = 0
    for n in range(4, 8):
        for p in itertools.product('abc', repeat=n):
            x = ''.join(p); nx += 1
            for layout, Zs, psis, Ts in stage_iter([x], ('', ''), 3, rng, 6, 2, 1):
                run_config([x], ('', ''), 3, layout, Zs, psis, Ts, stats, fails, 'EXH', controls=False)
    log('[4a] exhaustive d=1, |x|=4..7 (%d roots), c*=3, empty context: cases=%d  J_fail=%d  (not covered by prev HC: %d cases, %d fails)'
        % (nx, stats['cases'], stats['J_fail'], stats['cases_not_prevHC'], stats['J_fail_not_prevHC']))
    ex_stats = Counter(stats)
    # random: d in {1,2}, longer words, contexts, c* in {3,4}
    stats2 = Counter()
    for it in range(K):
        d = rng.choice((1, 2)); cstar = rng.choice((3, 3, 4))
        xs = [gen_word(rng, rng.randint(14, 30 if d == 1 else 22)) for _ in range(d)]
        ctx = [''.join(rng.choice('abc') for _ in range(rng.randint(0, 2))) for _ in range(d + 1)]
        if d == 2 and not ctx[1]: ctx[1] = rng.choice('abc')
        for layout, Zs, psis, Ts in stage_sample(xs, ctx, cstar, rng, 10, 6, 2):
            run_config(xs, ctx, cstar, layout, Zs, psis, Ts, stats2, fails, 'RND%d' % it, controls=True)
    # [4d] targeted: plant eta components of prescribed shapes behind random mark-absorbing material
    MOT = ['aaaa', 'bbbb', 'cccc', 'aaabbb', 'abab', 'acaca', 'cacac', 'bcbcb', 'cbcbc', 'acbcacbc', 'caccac',
           'ccaacc', 'aacc', 'bbcc', 'abcabc', 'acbacb', 'cabcab', 'bacbac', 'aabbcc', 'ccbbaa', 'ccacc', 'ccbcc',
           'aacaac', 'bbcbbc', 'acbca', 'bcacb', 'aaa', 'bbb', 'ccc',
           'acacabbb', 'cacabbbb', 'bcbcbaaa', 'cbcbaaaa', 'acacacbbbb', 'bbbacaca', 'aaabcbcb']
    tgt = 0; tries = 0
    while tgt < K * 2 and tries < K * 60:
        tries += 1
        d = rng.choice((1, 1, 2)); cstar = 3
        m1, m2 = rng.choice(MOT), rng.choice(MOT)
        def absorber():
            if rng.random() < 0.25: return gen_word(rng, rng.randint(4, 16))
            parts = ['aaaa', 'cccc', 'acacacac', 'bbbb', 'bcbcbcbc']; rng.shuffle(parts)
            return gen_word(rng, rng.randint(0, 3)) + ''.join(parts)
        if d == 1:
            R = [absorber(), gen_word(rng, rng.randint(1, 6)), gen_word(rng, rng.randint(0, 10))]
            xs = [R[0] + m1 + R[1] + m2 + R[2]]
            lay = ((0, len(R[0]), len(R[0]) + len(m1)), (0, len(R[0]) + len(m1) + len(R[1]), len(R[0]) + len(m1) + len(R[1]) + len(m2)))
            if rng.random() < 0.3: lay = lay[:1]
        else:
            R = [absorber() for _ in range(2)]; S2 = [gen_word(rng, rng.randint(0, 6)) for _ in range(2)]
            xs = [R[0] + m1 + S2[0], R[1] + m2 + S2[1]]
            lay = ((0, len(R[0]), len(R[0]) + len(m1)), (1, len(R[1]), len(R[1]) + len(m2)))
        M = [marks_of(x, cstar) for x in xs]
        if any(p in M[i] for i, s0, e0 in lay for p in range(s0, e0)): continue
        ctx = [''.join(rng.choice('abc') for _ in range(rng.randint(0, 2))) for _ in range(d + 1)]
        if d == 2 and not ctx[1]: ctx[1] = rng.choice('abc')
        phis = [xs[i][s0:e0] for i, s0, e0 in lay]
        opts = [z_options(ph, rng, 5) for ph in phis]
        combos = [c for c in itertools.product(*opts) if not all(Dzero(Z) for Z in c)]
        if not combos: continue
        tgt += 1
        for Zs in rng.sample(combos, min(4, len(combos))):
            ps = []
            for Z in Zs:
                while True:
                    w = ''.join(rng.choice('abc') for _ in range(rng.randint(1, 4)))
                    if (Z[0] or Z[1] or Z[2]) and len(proj(w, A)) < 2: continue
                    if (Z[3] or Z[4] or Z[5]) and len(proj(w, B)) < 2: continue
                    break
                ps.append(w)
            Ts_per = []
            for i, x in enumerate(xs):
                Zi = (0,) * 6
                for Z, iv in zip(Zs, lay):
                    if iv[0] == i: Zi = Dadd(Zi, Z)
                Ts_per.append(T_options(x, Zi, cstar, rng, 3))
            Ts = [(tuple(t for t, _ in c), tuple(g for _, g in c)) for c in itertools.product(*Ts_per)]
            if len(Ts) > 6: Ts = rng.sample(Ts, 6)
            run_config(xs, ctx, cstar, lay, Zs, ps, Ts, stats2, fails, 'TGT%d' % tgt, controls=True)
    # [4e] sparse / rigid-like roots (small nu, long runs): the delicate flag configurations
    for it in range(K * 3):
        d = rng.choice((1, 1, 2)); cstar = rng.choice((3, 3, 4))
        xs = [gen_sparse(rng) for _ in range(d)]
        ctx = [''.join(rng.choice('abc') for _ in range(rng.randint(0, 2))) for _ in range(d + 1)]
        if d == 2 and not ctx[1]: ctx[1] = rng.choice('abc')
        if rng.random() < 0.4: ctx = [''] * (d + 1) if d == 1 else ['', rng.choice('abc'), '']
        for layout, Zs, psis, Ts in stage_sample(xs, ctx, cstar, rng, 8, 6, 3):
            run_config(xs, ctx, cstar, layout, Zs, psis, Ts, stats2, fails, 'SPR%d' % it, controls=True)
    log('[4e] sparse/rigid-like roots done')
    # [4g] non-rich roots carrying transitional deletions (the residual OPEN-by-hand region)
    before = Counter(stats2)
    for it in range(K * 3):
        d = rng.choice((1, 1, 1, 2)); cstar = 3
        xs = [gen_nonrich(rng)] + ([gen_sparse(rng)] if d == 2 else [])
        if any(rich(x) for x in xs): continue
        ctx = [''] * (d + 1) if rng.random() < 0.5 else [''.join(rng.choice('abc') for _ in range(rng.randint(0, 2))) for _ in range(d + 1)]
        if d == 2 and not ctx[1]: ctx[1] = rng.choice('abc')
        for layout, Zs, psis, Ts in stage_sample(xs, ctx, cstar, rng, 12, 6, 3):
            run_config(xs, ctx, cstar, layout, Zs, psis, Ts, stats2, fails, 'NR%d' % it, controls=True)
    dd = stats2 - before
    log('[4g] non-rich roots: cases=%d, OPEN-class cases=%d, J_fail=%d' % (dd['cases'],
        sum(v for k, v in dd.items() if k.startswith('cls:OPEN')), dd['J_fail']))
    log('[4d] targeted planted-eta configurations accepted: %d (of %d tries)' % (tgt, tries))
    log('[4b+4d] random d in{1,2}, c* in{3,4}, nonempty contexts: cases=%d  J_fail=%d  (not prev HC: %d cases, %d fails); witnesses e=1:%d e=2:%d'
        % (stats2['cases'], stats2['J_fail'], stats2['cases_not_prevHC'], stats2['J_fail_not_prevHC'],
           stats2['J_ok_e1'], stats2['J_ok_e2']))
    tot = ex_stats + stats2
    sigs = sorted((k, v) for k, v in tot.items() if k.startswith('sig:'))
    log('[4c] per-type coverage (kappa letter-types : layout : prev-HC?) -> cases')
    for k, v in sigs: log('      %-34s %d' % (k[4:], v))
    nnew = sum(v for k, v in sigs if k.endswith('NEW')); log('      types not covered by HC_I/II/III: %d cases' % nnew)
    # [5] controls
    log('[4f] classification by hand-proof coverage (report section 3) -> cases [J failures]')
    for k, v in sorted((k, v) for k, v in tot.items() if k.startswith('cls:')):
        log('      %-44s %6d  [%d]' % (k[4:], v, tot.get('clsfail:' + k[4:], 0)))
    log('[5] controls (random part): e<=1 only fails on %d cases; one-hole-per-kappa without merging fails on %d cases'
        % (stats2['ctrl_e1_fail'], stats2['ctrl_perkappa_fail']))
    stats3 = Counter(); f3 = []
    for it in range(K // 4):
        x = gen_word(rng, rng.randint(10, 20))
        for layout, Zs, psis, Ts in stage_sample([x], ('', ''), 1, rng, 6, 4, 2):
            run_config([x], ('', ''), 1, layout, Zs, psis, Ts, stats3, f3, 'CS1', controls=False)
    log('[5] c*=1 (below the HC threshold): cases=%d J_fail=%d' % (stats3['cases'], stats3['J_fail']))
    if f3:
        tag, xs, ctx, cs, layout, Zs, psis, W, GF, GY, sig = f3[0]
        log('      example c*=1 failure: x=%s layout=%s Z=%s psi=%s W=%s Gamma(W)=%s Gamma(T)=%s'
            % (xs, layout, Zs, psis, W, GF, GY))
    if fails:
        log('[!] J FAILURES at c*>=3 (first %d):' % len(fails))
        for f in fails:
            tag, xs, ctx, cs, layout, Zs, psis, W, GF, GY, sig = f
            log('   ', tag, 'x=', xs, 'ctx=', ctx, 'c*=', cs, 'layout=', layout, 'Z=', Zs, 'psi=', psis, 'W=', W, 'GF=', GF, 'GT=', GY, sig)
    log('time %.1fs' % (time.time() - t0))
    log('SUMMARY', dict(sorted((k, v) for k, v in (ex_stats + stats2).items() if not k.startswith('sig:'))))
    log('ALL CHECKS PASSED' if not fails else 'CHECKS PASSED EXCEPT J (see [!])')

if __name__ == '__main__':
    main()
END SOURCE check_round10_HC_exhaustiveness_2026-11-14.py

### Round ten integration dependency — `check_round10_U2_integration_2026-11-14.py`

BEGIN SOURCE check_round10_U2_integration_2026-11-14.py
#!/usr/bin/env python3
"""Round 10: integration of the round-9 ACTUAL derivation stages with the round-10
hole construction (Theorem 1 of the round-10 report: P0 + H** + R'').

Python 3 standard library only.  Needs, in the same directory:
  check_round9_overlap_P1_B6_2026-11-14.py   (round-9 checker, SHA256 c468f6ad...; used ONLY to
                                              build grammars, derivation trees, eta, DFS antichains,
                                              W_j, and the original deleted windows)
  check_round10_HC_exhaustiveness_2026-11-14.py (round-10 core: independent dat_ov, Gamma,
                                              hosting oracle, expansion H**, joint search J)
Run:   python3 check_round10_U2_integration_2026-11-14.py
Exit 0 and final line ALL CHECKS PASSED on success.

For every greedy DFS stage (round-9 B6 procedure) on every maximal eta it
  * recomputes Z_kappa from the ORIGINAL deleted windows and checks it against an independent
    recomputation from N2 differences of psi^(j), psi^(j') (round-10 code),
  * computes the B6 state S (before) and T (after) per root component,
  * searches holes with J (e<=2) on Gamma(W_{j'}) and Gamma(T),
  * BUILDS the F-side witness W* = F[h] (same dat_ov as W_{j'}) and F[t] (t = expand(h,D)),
    and checks dat_ov(F[t]) == dat_ov(W_j) and, for L_eq families, F[h], F[t] in L,
  * BUILDS y' (realising T), y^pi = y'[h->t], and the current representative y_cur (realising S),
    and checks P0 premises (per-component shat_2 and content, total N2) and, on random
    admissible contexts E, dat_ov(E[y^pi]) == dat_ov(E[y_cur]) and E[y'] in L <=> E[y_cur] in L,
  * checks |y'| < |y_cur| (strict shortening).
Labels: actual-good-derivation (all), typed-minimal actual (OV2typed only), verified-L-in-C
(L_eq families), full-transfer-tested (all checks above executed).
"""
import importlib.util, os, sys, random, hashlib
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
def load(name, fn):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, fn))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

R9_FILE = 'check_round9_overlap_P1_B6_2026-11-14.py'
R9_SHA = 'c468f6ad5eb972b64803ca90de69a3b8c85beeedd21e9762363e89b83c78bde3'
assert hashlib.sha256(open(os.path.join(HERE, R9_FILE), 'rb').read()).hexdigest() == R9_SHA, 'round-9 source changed'
r9 = load('r9', R9_FILE)
hc = load('hc10', 'check_round10_HC_exhaustiveness_2026-11-14.py')

LOG = []
def log(*a):
    s = ' '.join(str(x) for x in a); LOG.append(s); print(s, flush=True)
ST = Counter()

def vec_from_windows(wins):
    """wins: list of round-9 original-window records (comp, Xn, tp, tq, type)."""
    DA = Counter(); DB = Counter()
    for w in wins:
        (DA if w[1] == 'A' else DB)[w[4]] += 1
    return hc.Dvec(DA, DB)

def run_instance(inst, fam, typed_min, Lmem, rng, show):
    G = inst.G; d = inst.d
    x = [r9.word(c) for c in inst.x]
    state = {(i, Xn): Counter(inst.N0[(i, Xn)]) for i in range(d) for Xn in ('A', 'B')}
    sh0 = {(i, Xn): hc.shat(hc.proj(x[i], X)) for i in range(d) for Xn, X in hc.PROJ}
    for eta in sorted(inst.etas, key=lambda n: min(inst.pos[t] for t in n.desc_tags)):
        comps, I, U, Lc = inst.analyse_eta(eta)
        ey = r9.ev(G, eta, {})
        data = [inst.stage_data(eta, comps, I[j], 's') for j in range(Lc + 1)]
        cols = [r9.colour(p, 'span') for p, _ in data]
        k = 0
        while k < Lc:
            same = [jj for jj in range(k + 1, Lc + 1) if cols[jj] == cols[k]]
            if not same: k += 1; continue
            jp = max(same)
            Zs = []; layout = []
            for kap in range(len(comps)):
                wins = [w for Xn, X in r9.PROJ for w in r9.orig_deleted_windows(inst, comps, ey, U[k], U[jp], kap, X, Xn)]
                Z = vec_from_windows(wins)
                # independent recomputation of Z from N2 differences (round-10 code)
                psi_j = r9.word(data[k][0][kap]); psi_jp = r9.word(data[jp][0][kap])
                DA = hc.N2(hc.proj(psi_j, hc.A)); DA.subtract(hc.N2(hc.proj(psi_jp, hc.A)))
                DB = hc.N2(hc.proj(psi_j, hc.B)); DB.subtract(hc.N2(hc.proj(psi_jp, hc.B)))
                assert not -DA and not -DB and hc.Dvec(+DA, +DB) == Z, 'Z recomputation'
                assert hc.conservative(Z)
                Zs.append(Z); layout.append((comps[kap][0], comps[kap][1], comps[kap][2]))
            S = {key: Counter(v) for key, v in state.items()}
            for Z, iv in zip(Zs, layout):
                DA, DB = hc.Dcounters(Z)
                state[(iv[0], 'A')] -= DA; state[(iv[0], 'B')] -= DB
            D = (0,) * 6
            for Z in Zs: D = hc.Dadd(D, Z)
            ST['stages'] += 1
            if hc.Dzero(D):
                k = jp; continue
            ST['stages_nonzero'] += 1
            ST['actual-good-derivation'] += 1
            if typed_min: ST['typed-minimal actual'] += 1
            if Lmem: ST['verified-L-in-C'] += 1
            sup = []
            for Z in Zs:
                DA, DB = hc.Dcounters(Z); sup.append(frozenset(['A:' + e for e in DA] + ['B:' + e for e in DB]))
            nzs = [(sp, iv) for sp, iv in zip(sup, layout) if sp]
            if len(nzs) == 2 and nzs[0][1][0] == nzs[1][1][0]:
                ab = [sp for sp, _ in nzs if sp == frozenset({'A:aa', 'B:bb'})]
                oth = [sp for sp, _ in nzs if sp != frozenset({'A:aa', 'B:bb'})]
                if ab and oth and any(e.endswith('cc') for e in oth[0]): ST['round9-HC_III-shaped (same criterion)'] += 1
            cls = hc.classify(Zs, layout, x); ST['cls:' + cls] += 1
            ST['cls_noT5:' + hc.classify(Zs, layout)] += 1
            Wj = data[k][1]; Wjp = data[jp][1]
            GF = hc.gamma(Wjp)
            Tst = [{'A': (sh0[(i, 'A')], +state[(i, 'A')]), 'B': (sh0[(i, 'B')], +state[(i, 'B')])} for i in range(d)]
            Sst = [{'A': (sh0[(i, 'A')], +S[(i, 'A')]), 'B': (sh0[(i, 'B')], +S[(i, 'B')])} for i in range(d)]
            GY = tuple(hc.gamma_from_state(t) for t in Tst)
            assert all(g is not None for g in GY), 'T not realisable'
            res = hc.joint(GF, GY, D)
            if res is None:
                ST['J_FAIL_ACTUAL'] += 1
                log('  [J FAILURE on actual stage]', fam, 'eta', eta.id, 'j', k, jp, 'Z', Zs, 'W_jprime', Wjp, 'GF', GF, 'GY', GY)
                k = jp; continue
            e, holes, Ds = res
            ST['J_ok_e%d' % e] += 1
            # ---- F side
            wf = hc.hosts((GF,), holes, want=True)
            Wst = wf[0][0]
            assert hc.dat(Wst) == hc.dat(Wjp), 'F[h] dat'
            for (ci, s0, s1), h in zip(wf[1], holes): assert Wst[s0:s1] == h
            if e == 2: assert wf[1][0][2] < wf[1][1][1]
            Ft = Wst
            for (ci, s0, s1), h, Di in sorted(zip(wf[1], holes, Ds), key=lambda z: -z[0][1]):
                t = hc.expand(h, Di); assert set(t) == set(h); Ft = Ft[:s0] + t + Ft[s1:]
            assert hc.dat(Ft) == hc.dat(Wj), 'dat(F[t]) != dat(W_j)'
            if Lmem:
                assert Lmem(Wst) and Lmem(Ft) and Lmem(Wj) and Lmem(Wjp), 'F-side membership'
            # ---- Y side
            req = tuple(hc.reqX(Di) for Di in Ds)
            wy = hc.hosts(GY, holes, want=True, req=req)
            yp = list(wy[0])
            for i in range(d):
                assert hc.gamma(yp[i]) == GY[i]
                for Xn, X in hc.PROJ:
                    assert hc.shat(hc.proj(yp[i], X)) == Tst[i][Xn][0] and hc.N2(hc.proj(yp[i], X)) == Tst[i][Xn][1]
            ypi = list(yp)
            for (ci, s0, s1), h, Di in sorted(zip(wy[1], holes, Ds), key=lambda z: (z[0][0], -z[0][1])):
                assert yp[ci][s0:s1] == h
                ypi[ci] = ypi[ci][:s0] + hc.expand(h, Di) + ypi[ci][s1:]
            ycur = [r9.realise(Sst[i]) for i in range(d)]
            assert all(y is not None for y in ycur)
            for i in range(d):
                assert set(ypi[i]) == set(x[i]) == set(ycur[i]) == set(yp[i]), 'content'
                for Xn, X in hc.PROJ:
                    assert hc.shat(hc.proj(ypi[i], X)) == hc.shat(hc.proj(ycur[i], X)) == sh0[(i, Xn)]
            for Xn, X in hc.PROJ:
                t1 = Counter(); t2 = Counter()
                for i in range(d): t1 += hc.N2(hc.proj(ypi[i], X)); t2 += hc.N2(hc.proj(ycur[i], X))
                assert t1 == t2, 'P0 total'
            if any(hc.N2(hc.proj(ypi[i], X)) != hc.N2(hc.proj(ycur[i], X)) for i in range(d) for _, X in hc.PROJ):
                ST['P0_used_total_only'] += 1
            assert sum(map(len, yp)) < sum(map(len, ycur)), 'not shorter'
            for _ in range(12):
                E = [''.join(rng.choice('abc') for _ in range(rng.randint(0, 4))) for _ in range(d + 1)]
                if d == 2 and not E[1]: E[1] = rng.choice('abc')
                fill = lambda tp: E[0] + ''.join(tp[i] + E[i + 1] for i in range(d))
                assert hc.dat(fill(ypi)) == hc.dat(fill(ycur)), 'P0 in context'
                if Lmem:
                    assert Lmem(fill(yp)) == Lmem(fill(ycur)) == Lmem(fill(ypi)), 'transfer'
            ST['full-transfer-tested'] += 1
            if show[0] < 4 and (e == 2 or cls.startswith('OPEN') or show[0] < 2):
                show[0] += 1
                log('  [stage] %s eta=node %d j=%d<j\'=%d Z=%s class=%s' % (fam, eta.id, k, jp, Zs, cls))
                log('     W_jprime=%s' % Wjp)
                log('     holes=%s D_i=%s  t=%s' % (holes, Ds, [hc.expand(h, Di) for h, Di in zip(holes, Ds)]))
                log('     F[h]=%s' % Wst); log('     F[t]=%s  (dat == dat(W_j): True)' % Ft)
                log("     y'=%s  y^pi=%s  y_cur=%s" % (yp, ypi, ycur))
            k = jp

def main():
    rng = random.Random(20261115)
    log('== Round 10 U2 integration checker (actual round-9 derivations x round-10 holes); seed 20261115 ==')
    log('round-9 source SHA256 verified:', R9_SHA[:16] + '...')
    show = [0]
    fams = []
    for M, cs, reps in ((5, 3, 12), (6, 3, 8), (6, 4, 6)):
        G = r9.grammar_ov(M); th, _ = G.thickness(); sh = G.short_tuples(th)
        for rep in range(reps):
            for mode in ('fixed', 'hash'):
                Rn = r9.full_tree_ov(G, M, rng)
                sroot = r9.Node([r for r in G.by_lhs['S'] if r.kids == ('B%d' % M, 'S')][0],
                                [Rn, r9.Node([r for r in G.by_lhs['S'] if r.tmpl == (('c',),)][0], [])])
                inst = r9.Instance(G, sroot, Rn, cs, sh, rng, r9.L_eq, mode)
                run_instance(inst, 'OV2typed(M=%d,c*=%d)' % (M, cs), True, r9.L_eq, rng, show); ST['inst:OV2typed'] += 1
    for gname, gfun in (('OV2root1', r9.grammar_ov), ('OV3root1', r9.grammar_ov3)):
        for M, cs, reps in ((5, 3, 12), (6, 3, 8), (5, 4, 6)):
            G = gfun(M); th, _ = G.thickness(); sh = G.short_tuples(th)
            for rep in range(reps):
                for mode in ('fixed', 'hash'):
                    Rn = r9.full_tree_ov(G, M, rng); inner = r9.rand_tree(G, rng, 'S', 0, 3)
                    sroot = r9.Node([r for r in G.by_lhs['S'] if r.kids == ('B%d' % M, 'S')][0], [Rn, inner])
                    inst = r9.Instance(G, sroot, sroot, cs, sh, rng, r9.L_eq, mode)
                    run_instance(inst, '%s(M=%d,c*=%d)' % (gname, M, cs), False, r9.L_eq, rng, show); ST['inst:' + gname] += 1
    G = r9.grammar_cfg(); th, _ = G.thickness(); sh = G.short_tuples(th)
    for rep in range(120):
        t = r9.rand_tree(G, rng, 'S', 0, 9, 0.8)
        for cs in (3, 4):
            inst = r9.Instance(G, t, t, cs, sh, rng, r9.L_eq, 'hash')
            run_instance(inst, 'CFG0', False, r9.L_eq, rng, show); ST['inst:CFG0'] += 1
    gdone = 0; gid = 0
    while gdone < 120:
        gid += 1; G = r9.random_grammar(rng, gid)
        try: G.check_good()
        except AssertionError: continue
        th, _ = G.thickness()
        if th > 40: continue
        sh = G.short_tuples(th, 30)
        if any(not sh[n] for n in G.arity): continue
        gdone += 1
        for rep in range(3):
            t = r9.rand_tree(G, rng, 'S', 0, 7, 0.8); order = r9.number(t)
            if len(order) < 8: continue
            cands = [n for n in order if len(n.rule.tmpl) == 2 and n.kids]
            for R in [t] + ([rng.choice(cands)] if cands else []):
                for cs in (3, 4):
                    inst = r9.Instance(G, t, R, cs, sh, rng, None, 'hash')
                    run_instance(inst, G.name, False, None, rng, show); ST['inst:RAND'] += 1
    log('[A] instances:', {k[5:]: v for k, v in sorted(ST.items()) if k.startswith('inst:')})
    log('[B] stages=%d nonzero=%d ; labels: actual-good-derivation=%d typed-minimal actual=%d verified-L-in-C=%d full-transfer-tested=%d'
        % (ST['stages'], ST['stages_nonzero'], ST['actual-good-derivation'], ST['typed-minimal actual'],
           ST['verified-L-in-C'], ST['full-transfer-tested']))
    log('[B\'] stages meeting the round-9 HC_III-shape criterion (same root comp, kappa={A:aa,B:bb}, kappa\' has cc): %d'
        % ST['round9-HC_III-shaped (same criterion)'])
    log('[C] J on actual stages: e=1 %d, e=2 %d, FAIL %d; P0 needed in total-N2 form (per-component N2 of y^pi != y_cur): %d'
        % (ST['J_ok_e1'], ST['J_ok_e2'], ST['J_FAIL_ACTUAL'], ST['P0_used_total_only']))
    log('[D] classification of actual nonzero stages (report section 3):')
    for kk, v in sorted((kk, v) for kk, v in ST.items() if kk.startswith('cls:')): log('      %-44s %d' % (kk[4:], v))
    log('[D\'] same stages classified WITHOUT Lemma T5 (to show what T5 absorbs):')
    for kk, v in sorted((kk, v) for kk, v in ST.items() if kk.startswith('cls_noT5:')): log('      %-44s %d' % (kk[9:], v))
    assert ST['J_FAIL_ACTUAL'] == 0 and ST['full-transfer-tested'] == ST['stages_nonzero'] > 0
    log('ALL CHECKS PASSED')

if __name__ == '__main__':
    main()
END SOURCE check_round10_U2_integration_2026-11-14.py

### Round nine checker dependency — `check_round9_overlap_P1_B6_2026-11-14.py`

BEGIN SOURCE check_round9_overlap_P1_B6_2026-11-14.py
#!/usr/bin/env python3
"""Round 9 (fan-out 2, overlapping projections A={a,c}, B={b,c}, ell=2):
real-derivation checker for P1 (span-tagged pure/impure windows) and B6
(multi-stage count persistence).

Python 3 standard library only.  Run:   python3 check_round9_overlap_P1_B6_2026-11-14.py
Exit code 0 and final line ALL CHECKS PASSED on success.

What is checked (all on ACTUAL derivation trees of explicitly given good MCFGs):
  [0] grammar legality: good (eps-free, nondeleting, nonpermuting, nonmerging),
      fan-out<=2, rank<=2, reduced; soundness/bounded completeness for L_eq.
  [1] typed node-minimality (DP over content-typed nonterminals) for family OV2.
  [2] marks, maximal free subtrees eta (freeness AND maximality asserted),
      contiguity of eta components, DFS prefix antichains I_j, U_j monotone.
  [3] P1 on EVERY same-colour pair j<j' (span colour):
        Z_{k,X} >= 0 edgewise; Z_{k,X} == multiset of ORIGINAL internal windows of
        pi_X(phi_k) whose Sigma-span meets U_j' but not U_j; these windows are
        unmarked; dZ = 0; whole-word identity for W_j,W_j'; shat equality;
        shared-letter (c) conservation per kappa; participation lemma
        (Z_A = 0  =>  Z_B in N*bb, and symmetric); W_j in L.
  [4] B6: greedy DFS stages over all maximal eta; deleted original-window sets
      pairwise disjoint and unmarked; min(N0,c*) <= N_t <= N0; Lemma-P flags;
      explicit realisation of every intermediate state by a word (dat_ov and
      content verified); at least two nontrivial stages required in some runs.
  [5] negative controls: projection-only impurity colour, marked windows whose
      span crosses eta (literal window lost in W_j), empty replacement piece
      (non-eps-free) -- each must be DETECTED.
"""
import random, sys, hashlib
from collections import Counter

A = frozenset('ac'); B = frozenset('bc'); PROJ = (('A', A), ('B', B))
LOG = []
def log(*a):
    s = ' '.join(str(x) for x in a); LOG.append(s); print(s)

STATS = Counter()

# ---------------------------------------------------------------- grammars
class Rule:
    __slots__ = ('lhs', 'kids', 'tmpl', 'idx')
    def __init__(self, lhs, kids, tmpl):
        self.lhs = lhs; self.kids = tuple(kids); self.tmpl = tuple(tuple(c) for c in tmpl)
    def __repr__(self):
        def tk(t): return t if isinstance(t, str) else 'x%d.%d' % (t[0] + 1, t[1] + 1)
        return '%s -> (%s)(%s)' % (self.lhs, ', '.join(''.join(tk(t) for t in c) for c in self.tmpl),
                                   ','.join(self.kids))

def parse_comp(s):
    """'x1.1 a x2.1' tokens separated by spaces; letters may be grouped e.g. 'aac'."""
    out = []
    for tok in s.split():
        if tok[0] == 'x':
            j, k = tok[1:].split('.'); out.append((int(j) - 1, int(k) - 1))
        else:
            out.extend(list(tok))
    return out

class Grammar:
    def __init__(self, name, arity, rules, start='S'):
        self.name = name; self.arity = dict(arity); self.start = start
        self.rules = rules
        for i, r in enumerate(rules): r.idx = i
        self.by_lhs = {n: [r for r in rules if r.lhs == n] for n in self.arity}

    def check_good(self):
        assert self.arity[self.start] == 1
        for r in self.rules:
            assert len(r.kids) <= 2, ('rank', r)
            assert len(r.tmpl) == self.arity[r.lhs], ('arity', r)
            assert self.arity[r.lhs] <= 2
            seen = []
            for comp in r.tmpl:
                assert len(comp) >= 1, ('eps-free', r)
                for a, b2 in zip(comp, comp[1:]):
                    if not isinstance(a, str) and not isinstance(b2, str):
                        assert not (a[0] == b2[0] and b2[1] == a[1] + 1), ('nonmerging', r)
                for t in comp:
                    if not isinstance(t, str):
                        seen.append(t)
                    else:
                        assert t in 'abc'
            # nondeleting + linear
            want = [(j, k) for j, n in enumerate(r.kids) for k in range(self.arity[n])]
            assert sorted(seen) == sorted(want) and len(seen) == len(set(seen)), ('nondeleting', r)
            for j, n in enumerate(r.kids):   # nonpermuting
                ks = [t[1] for t in seen if t[0] == j]
                assert ks == list(range(self.arity[n])), ('nonpermuting', r)
        # reduced
        prod = set(); ch = True
        while ch:
            ch = False
            for r in self.rules:
                if r.lhs not in prod and all(k in prod for k in r.kids):
                    prod.add(r.lhs); ch = True
        assert prod == set(self.arity), ('productive', set(self.arity) - prod)
        reach = {self.start}; ch = True
        while ch:
            ch = False
            for r in self.rules:
                if r.lhs in reach:
                    for k in r.kids:
                        if k not in reach: reach.add(k); ch = True
        assert reach == set(self.arity), ('reachable', set(self.arity) - reach)

    def apply(self, r, kidvals):
        out = []
        for comp in r.tmpl:
            s = []
            for t in comp:
                s.append(t if isinstance(t, str) else kidvals[t[0]][t[1]])
            out.append(''.join(s))
        return tuple(out)

    def thickness(self):
        INF = 10 ** 9
        inside = {n: INF for n in self.arity}; ch = True
        def term(r): return sum(1 for c in r.tmpl for t in c if isinstance(t, str))
        while ch:
            ch = False
            for r in self.rules:
                v = term(r) + sum(inside[k] for k in r.kids)
                if v < inside[r.lhs]: inside[r.lhs] = v; ch = True
        out = {n: INF for n in self.arity}; out[self.start] = 0; ch = True
        while ch:
            ch = False
            for r in self.rules:
                if out[r.lhs] >= INF: continue
                for j, k in enumerate(r.kids):
                    v = out[r.lhs] + term(r) + sum(inside[k2] for j2, k2 in enumerate(r.kids) if j2 != j)
                    if v < out[k]: out[k] = v; ch = True
        th = max(out[r.lhs] + term(r) + sum(inside[k] for k in r.kids) for r in self.rules)
        return max(1, th), inside

    def short_tuples(self, cap_len, cap_count=60):
        """Tuples of L_B(G) with total length <= cap_len (actual derivations)."""
        T = {n: set() for n in self.arity}; ch = True; rounds = 0
        while ch and rounds < 12:
            ch = False; rounds += 1
            for r in self.rules:
                pools = [sorted(T[k], key=lambda u: (sum(map(len, u)), u))[:cap_count] for k in r.kids]
                def rec(j, acc):
                    nonlocal ch
                    if j == len(pools):
                        v = self.apply(r, acc)
                        if sum(map(len, v)) <= cap_len and v not in T[r.lhs] and len(T[r.lhs]) < 4 * cap_count:
                            T[r.lhs].add(v); ch = True
                        return
                    for u in pools[j]: rec(j + 1, acc + [u])
                rec(0, [])
        return {n: sorted(T[n], key=lambda u: (sum(map(len, u)), u))[:cap_count] for n in T}

    def words_upto(self, n):
        T = {k: set() for k in self.arity}; ch = True
        while ch:
            ch = False
            for r in self.rules:
                pools = [list(T[k]) for k in r.kids]
                def rec(j, acc):
                    nonlocal ch
                    if j == len(pools):
                        v = self.apply(r, acc)
                        if sum(map(len, v)) <= n and v not in T[r.lhs]:
                            T[r.lhs].add(v); ch = True
                        return
                    for u in pools[j]: rec(j + 1, acc + [u])
                rec(0, [])
        return {u[0] for u in T[self.start]}

def L_eq(w): return len(w) > 0 and w.count('a') == w.count('b')

S_CFG = ['S -> (x1.1 x2.1)(S,S)', 'S -> (a x1.1 b)(S)', 'S -> (b x1.1 a)(S)',
         'S -> (ab)()', 'S -> (ba)()', 'S -> (c)()']

def mk_rules(specs):
    out = []
    for sp in specs:
        lhs, rhs = sp.split('->'); lhs = lhs.strip(); rhs = rhs.strip()
        tm, kids = rhs.rsplit(')(', 1); tm = tm[1:]; kids = kids[:-1]
        comps = [parse_comp(c) for c in tm.split(',')]
        out.append(Rule(lhs, [k for k in kids.split(',') if k], comps))
    return out

def grammar_ov(M):
    """OV2(M): good fan-out-2 rank-2 MCFG for L_eq, with crossing template and
    content-breaking short escapes (b,a),(cb,ac).  Typed root X=(B_M)_T, T=({a,c},{b,c})."""
    ar = {'S': 1}; specs = list(S_CFG)
    specs.append('S -> (x1.1 x2.1 x1.2)(B%d,S)' % M)
    for m in range(M + 1):
        ar['B%d' % m] = 2
        specs += ['B%d -> (b, a)()' % m, 'B%d -> (cb, ac)()' % m]
        if m == 0:
            specs += ['B0 -> (aac, cbb)()', 'B0 -> (aca, bcb)()']        else:
            specs += ['B%d -> (x1.1 x2.1, x1.2 x2.2)(B%d,B%d)' % (m, m - 1, m - 1),
                      'B%d -> (x1.1 x2.1, x2.2 x1.2)(B%d,B%d)' % (m, m - 1, m - 1)]
    return Grammar('OV2(M=%d)' % M, ar, mk_rules(specs))

def grammar_ov3(M):
    """OV3(M): like OV2 but B0 -> (aabb, ccc) | (abab, ccc): component 1 over {a,b} only,
    component 2 over {c} only.  With an arity-1 root, two eta components share one root
    component -> HC_III-shaped differences (aa/bb in one kappa, cc in the other)."""
    ar = {'S': 1}; specs = list(S_CFG)
    specs.append('S -> (x1.1 x2.1 x1.2)(B%d,S)' % M)
    for m in range(M + 1):
        ar['B%d' % m] = 2
        specs += ['B%d -> (b, a)()' % m, 'B%d -> (ab, c)()' % m]
        if m == 0:
            specs += ['B0 -> (aabb, ccc)()', 'B0 -> (abab, ccc)()']
        else:
            specs += ['B%d -> (x1.1 x2.1, x1.2 x2.2)(B%d,B%d)' % (m, m - 1, m - 1),
                      'B%d -> (x1.1 x2.1, x2.2 x1.2)(B%d,B%d)' % (m, m - 1, m - 1)]
    return Grammar('OV3(M=%d)' % M, ar, mk_rules(specs))

def grammar_cfg():
    return Grammar('CFG0', {'S': 1}, mk_rules(S_CFG))

def random_grammar(rng, gid):
    """Random good fan-out<=2 rank<=2 MCFG over {a,b,c} (L = L(G))."""
    nts = {'S': 1, 'P': 2, 'Q': 2, 'R': 1}
    rules = []
    def rand_tmpl(d0, kid_ar):
        vars_ = []
        seqs = [[(j, k) for k in range(d)] for j, d in enumerate(kid_ar)]
        while any(seqs):
            j = rng.choice([i for i, s in enumerate(seqs) if s]); vars_.append(seqs[j].pop(0))
        cuts = sorted(rng.sample(range(len(vars_) + 1), d0 - 1)) if d0 > 1 else []
        comps = []; prev = 0
        for c in cuts + [len(vars_)]:
            comps.append(vars_[prev:c]); prev = c
        out = []
        for comp in comps:
            comp = list(comp)
            for _ in range(rng.randint(0, 2)):
                comp.insert(rng.randint(0, len(comp)), rng.choice('abc'))
            if not comp: comp = [rng.choice('abc')]
            fixed = []
            for t in comp:
                if fixed and not isinstance(t, str) and not isinstance(fixed[-1], str) \
                        and fixed[-1][0] == t[0] and t[1] == fixed[-1][1] + 1:
                    fixed.append(rng.choice('abc'))
                fixed.append(t)
            out.append(fixed)
        return out
    for n, d in nts.items():
        for _ in range(2):   # terminal rules
            rules.append(Rule(n, [], [[rng.choice('abc') for _ in range(rng.randint(1, 2))] for _ in range(d)]))
        for _ in range(3):
            kids = [rng.choice(list(nts)) for _ in range(rng.randint(1, 2))]
            rules.append(Rule(n, kids, rand_tmpl(d, [nts[k] for k in kids])))
    rules.append(Rule('S', ['P'], [[(0, 0), rng.choice('abc'), (0, 1)]]))
    rules.append(Rule('S', ['R', 'Q'], [[(1, 0), (0, 0), (1, 1)]]))
    return Grammar('RAND%d' % gid, nts, rules)

# ---------------------------------------------------------------- trees
class Node:
    __slots__ = ('rule', 'kids', 'id', 'parent', 'desc_tags', 'leafset')
    def __init__(self, rule, kids):
        self.rule = rule; self.kids = kids; self.parent = None

def number(root):
    cnt = [0]; order = []
    def go(n, p):
        n.id = cnt[0]; cnt[0] += 1; n.parent = p; order.append(n)
        for k in n.kids: go(k, n)
    go(root, None); return order

def ev(G, n, repl):
    """yield with origin tags; repl: node id -> tuple of tagged components."""
    if n.id in repl: return repl[n.id]
    kv = [ev(G, k, repl) for k in n.kids]
    out = []
    for ci, comp in enumerate(n.rule.tmpl):
        s = []
        for ti, t in enumerate(comp):
            if isinstance(t, str): s.append((t, ('o', n.id, ci, ti)))
            else: s.extend(kv[t[0]][t[1]])
        out.append(s)
    return out

def rand_tree(G, rng, nt, depth, maxd, pref_rec=0.75):
    rs = G.by_lhs[nt]
    if depth >= maxd:
        cand = [r for r in rs if not r.kids] or rs
        # pick rule minimising recursion
        cand = [r for r in rs if not r.kids] or sorted(rs, key=lambda r: len(r.kids))[:1]
        r = rng.choice(cand)
    else:
        rec = [r for r in rs if r.kids]
        r = rng.choice(rec) if (rec and rng.random() < pref_rec) else rng.choice(rs)
    return Node(r, [rand_tree(G, rng, k, depth + 1, maxd, pref_rec) for k in r.kids])

def full_tree_ov(G, M, rng):
    def mk(m):
        rs = [r for r in G.by_lhs['B%d' % m] if (r.kids if m else len(r.tmpl[0]) >= 3)]
        r = rng.choice(rs)
        return Node(r, [mk(m - 1) for _ in r.kids])
    return mk(M)

# ---------------------------------------------------------------- data
def proj(w, X): return ''.join(ch for ch in w if ch in X)
def shat(u): return ('w', u) if len(u) < 2 else ('ps', u[0], u[-1])
def N2(u): return Counter(u[i:i + 2] for i in range(len(u) - 1))
def dat(w): return tuple((shat(proj(w, X)), tuple(sorted(N2(proj(w, X)).items()))) for _, X in PROJ)
def bnd(Z):
    d = Counter()
    for e, v in Z.items():
        d[e[0]] -= v; d[e[1]] += v
    return {k: v for k, v in d.items() if v}
def word(t): return ''.join(ch for ch, _ in t)
def cnt_sub(P, Q):
    keys = set(P) | set(Q); return {k: P.get(k, 0) - Q.get(k, 0) for k in keys if P.get(k, 0) - Q.get(k, 0)}

def windows(tw, X):
    """windows of pi_X(tw) as (p,q) indices into tagged word tw."""
    idx = [i for i, (ch, _) in enumerate(tw) if ch in X]
    return [(p, q) for p, q in zip(idx, idx[1:])]

# ---------------------------------------------------------------- core analysis
class Instance:
    """One root x (node R inside sentence tree), marks, maximal free subtrees."""
    def __init__(self, G, sent_root, R, cstar, shorts, rng, Lmem=None, repl_mode='fixed'):
        self.G = G; self.sent = sent_root; self.R = R; self.cstar = cstar
        self.shorts = shorts; self.rng = rng; self.Lmem = Lmem; self.repl_mode = repl_mode
        self.order = number(sent_root)
        for n in reversed(self.order):
            s = set((('o', n.id, ci, ti) for ci, c in enumerate(n.rule.tmpl) for ti, t in enumerate(c) if isinstance(t, str)))
            for k in n.kids: s |= k.desc_tags
            n.desc_tags = frozenset(s)
        self.x = ev(G, R, {})
        self.d = len(self.x)
        self.pos = {}
        for i, comp in enumerate(self.x):
            for p, (ch, tag) in enumerate(comp): self.pos[tag] = (i, p)
        # context admissibility (lem:filling-identity / E_A): separators nonempty
        sent = ev(G, sent_root, {})[0]
        starts = [sent.index(self.x[i][0]) for i in range(self.d)]
        for i in range(self.d - 1):
            assert starts[i] + len(self.x[i]) < starts[i + 1], 'inner separator empty'
        # marks
        self.marked = set(); self.N0 = {}; self.marked_windows = set()
        for i, comp in enumerate(self.x):
            for Xn, X in PROJ:
                seen = Counter()
                for (p, q) in windows(comp, X):
                    e = comp[p][0] + comp[q][0]; seen[e] += 1
                    if seen[e] <= cstar:
                        self.marked |= {comp[p][1], comp[q][1]}
                        self.marked_windows.add((i, Xn, comp[p][1], comp[q][1]))
                self.N0[(i, Xn)] = N2(proj(word(comp), X))
        # maximal free nodes inside R
        inR = set(); stack = [R]
        while stack:
            n = stack.pop(); inR.add(n.id); stack.extend(n.kids)
        self.inR = inR
        free = {n.id for n in self.order if n.id in inR and not (n.desc_tags & self.marked)}
        self.etas = []
        for n in self.order:
            if n.id in free and n.id != R.id:
                assert n.parent is not None and n.parent.id in inR
                if n.parent.id not in free:
                    self.etas.append(n)
        # maximality/freeness asserts (non-vacuous)
        for n in self.etas:
            assert not (n.desc_tags & self.marked)
            assert n.parent.desc_tags & self.marked
        STATS['etas'] += len(self.etas)

    def repl_tuple(self, n, salt):
        lst = self.shorts[n.rule.lhs]
        assert lst, 'no short tuple'
        if self.repl_mode == 'fixed': u = lst[0]
        else:
            h = int(hashlib.sha256(('%d|%s' % (n.id, salt)).encode()).hexdigest(), 16)
            u = lst[h % len(lst)]
        assert all(len(c) >= 1 for c in u)
        return [[(ch, ('i', n.id, ci, k)) for k, ch in enumerate(c)] for ci, c in enumerate(u)]

    def analyse_eta(self, eta):
        G = self.G
        # eta components and their location in root components
        ey = ev(G, eta, {})
        comps = []
        for kappa, c in enumerate(ey):
            i, s = self.pos[c[0][1]]
            assert [t for _, t in self.x[i][s:s + len(c)]] == [t for _, t in c], 'eta component not contiguous'
            comps.append((i, s, s + len(c)))
        # leaves and DFS antichains
        nodes = []; stack = [eta]
        while stack:
            n = stack.pop(); nodes.append(n); stack.extend(reversed(n.kids))
        leaves = [n for n in nodes if not n.kids]
        lidx = {n.id: k for k, n in enumerate(leaves)}
        for n in reversed(nodes):
            n.leafset = frozenset([lidx[n.id]]) if not n.kids else frozenset().union(*[k.leafset for k in n.kids])
        Lc = len(leaves)
        I = []
        for j in range(Lc + 1):
            sel = [n for n in nodes if n.leafset and max(n.leafset) < j and
                   (n is eta or max(n.parent.leafset) >= j)]
            I.append(sel)
        U = [frozenset().union(*[n.desc_tags for n in Ij]) if Ij else frozenset() for Ij in I]
        for j in range(Lc):
            assert U[j] < U[j + 1], 'U_j not strictly increasing'
        return comps, I, U, Lc

    def stage_data(self, eta, comps, Ij, salt):
        repl = {n.id: self.repl_tuple(n, salt) for n in Ij}
        psi = ev(self.G, eta, repl)
        W = word(ev(self.G, self.sent, repl)[0])
        return psi, W

def colour(psi, mode):
    col = []
    for k, c in enumerate(psi):
        for Xn, X in PROJ:
            imp = Counter()
            for (p, q) in windows(c, X):
                if mode == 'span': bad = any(t[0] == 'i' for _, t in c[p:q + 1])
                else: bad = c[p][1][0] == 'i' or c[q][1][0] == 'i'
                if bad: imp[c[p][0] + c[q][0]] += 1
            col.append((k, Xn, shat(proj(word(c), X)), tuple(sorted(imp.items()))))
    return tuple(col)

def orig_deleted_windows(inst, comps, eta_y, Uj, Ujp, kappa, X, Xn):
    c = eta_y[kappa]; out = []
    for (p, q) in windows(c, X):
        span = {t for _, t in c[p:q + 1]}
        if (span & Ujp) and not (span & Uj):
            out.append((comps[kappa][0], Xn, c[p][1], c[q][1], c[p][0] + c[q][0]))
    return out

# ---------------------------------------------------------------- realisation of a state
def euler_word(N, sh):
    if sh[0] == 'w':
        assert sum(N.values()) == 0; return sh[1]
    s, t = sh[1], sh[2]
    adj = {}
    for e, v in N.items():
        for _ in range(v): adj.setdefault(e[0], []).append(e[1])
    for k in adj: adj[k].sort()
    stack = [s]; path = []
    while stack:
        u = stack[-1]
        if adj.get(u):
            stack.append(adj[u].pop())
        else:
            path.append(stack.pop())
    path.reverse()
    w = ''.join(path)
    if len(w) - 1 != sum(N.values()) or w[-1] != t: return None
    return w

def realise(state_i):
    """state_i: dict Xn -> (shat, Counter). Returns word y with dat_ov(y)=state or None."""
    P = euler_word(state_i['A'][1], state_i['A'][0]); Q = euler_word(state_i['B'][1], state_i['B'][0])
    if P is None or Q is None or P.count('c') != Q.count('c'): return None
    ps = P.split('c'); qs = Q.split('c')
    return 'c'.join(p + q for p, q in zip(ps, qs))

# ---------------------------------------------------------------- main checks per instance
def check_instance(inst, tag, want_proj_ctrl=True, trace=False):
    G = inst.G
    total_pairs = 0; nonzero = 0
    state = {k: Counter(v) for k, v in inst.N0.items()}
    shat0 = {(i, Xn): shat(proj(word(inst.x[i]), X)) for i in range(inst.d) for Xn, X in PROJ}
    content0 = [set(word(c)) for c in inst.x]
    deleted_all = set(); stages = 0; stages_nz = 0; max_stage_per_eta = 0
    proj_viol = 0; proj_pairs = 0; span_cross_lost = 0
    for eta in sorted(inst.etas, key=lambda n: min(inst.pos[t] for t in n.desc_tags)):
        comps, I, U, Lc = inst.analyse_eta(eta)
        ey = ev(G, eta, {})
        data = [inst.stage_data(eta, comps, I[j], 's') for j in range(Lc + 1)]
        cols = [colour(p, 'span') for p, _ in data]
        pcols = [colour(p, 'proj') for p, _ in data]
        # literal loss of marked windows whose span crosses eta (negative control 2)
        eta_tags = eta.desc_tags
        for (i, Xn, tp, tq) in inst.marked_windows:
            pi, pp = inst.pos[tp]; qi, qp = inst.pos[tq]
            span = {t for _, t in inst.x[i][pp:qp + 1]}
            if span & eta_tags:
                X = dict(PROJ)[Xn]
                for j in range(Lc + 1):
                    full = ev(G, inst.sent, {n.id: inst.repl_tuple(n, 's') for n in I[j]})[0]
                    idx = [k for k, (ch, t) in enumerate(full) if ch in X]
                    tags = [full[k][1] for k in idx]
                    a = tags.index(tp); b2 = tags.index(tq)
                    if b2 != a + 1:
                        span_cross_lost += 1
                        if STATS['example_span_cross'] == 0:
                            STATS['example_span_cross'] = 1
                            log('    [example span-cross] %s: marked %s-window %s%s at root comp %d pos %d..%d '
                                'spans eta; in W_%d its two letters are no longer consecutive in pi_%s W_j'
                                % (tag, Xn, inst.x[i][pp][0], inst.x[i][qp][0], i, pp, qp, j, Xn))
                        break
        # P1 on every same-colour pair
        for j in range(Lc + 1):
            for jp in range(j + 1, Lc + 1):
                if pcols[j] == pcols[jp] and want_proj_ctrl:
                    proj_pairs += 1
                    bad = False
                    for k, c in enumerate(data[j][0]):
                        for Xn, X in PROJ:
                            Z = cnt_sub(N2(proj(word(c), X)), N2(proj(word(data[jp][0][k]), X)))
                            orig = Counter(w[4] for w in orig_deleted_windows(inst, comps, ey, U[j], U[jp], k, X, Xn))
                            if any(v < 0 for v in Z.values()) or Counter(Z) != orig: bad = True
                    if bad:
                        proj_viol += 1
                        STATS['proj_violations[' + tag.split('(')[0].rstrip('0123456789') + ']'] += 1
                        if (STATS['example_proj'] == 0 and sum(len(c) for c in inst.x) <= 14 and inst.d == 1
                                and any(t[0] == 'i' for c2 in data[jp][0] for _, t in c2)):
                            STATS['example_proj'] = 1
                            log('    [proj-tag counterexample (A)] %s, eta=node %d (%s), j=%d<j\'=%d' % (tag, eta.id, eta.rule.lhs, j, jp))
                            log('      root x =', [word(c) for c in inst.x], ' phi =', [word(c) for c in ey])
                            for k2, c2 in enumerate(data[j][0]):
                                log('      psi^(j)=%s  psi^(j\')=%s (inserted UPPER)' % (
                                    ''.join(ch.upper() if t[0] == 'i' else ch for ch, t in c2),
                                    ''.join(ch.upper() if t[0] == 'i' else ch for ch, t in data[jp][0][k2])))
                                for Xn, X in PROJ:
                                    Z = cnt_sub(N2(proj(word(c2), X)), N2(proj(word(data[jp][0][k2]), X)))
                                    orig = Counter(w[4] for w in orig_deleted_windows(inst, comps, ey, U[j], U[jp], k2, X, Xn))
                                    log('      %s: Z(proj-colour pair)=%s  original deleted windows=%s  span-colours equal=%s'
                                        % (Xn, dict(Z), dict(orig), cols[j] == cols[jp]))
                            log('      derivation (preorder rules):', [repr(n.rule) for n in inst.order])
                            log('      I_j =', [n.id for n in I[j]], ' I_j\' =', [n.id for n in I[jp]], ' short tuples used:', {n.id: inst.shorts[n.rule.lhs][0] if inst.repl_mode=='fixed' else 'hash' for n in I[jp]})
                if cols[j] != cols[jp]: continue
                total_pairs += 1
                psi_j, Wj = data[j]; psi_jp, Wjp = data[jp]
                sumZ = {Xn: Counter() for Xn, _ in PROJ}; any_nz = False
                for k in range(len(psi_j)):
                    Zk = {}
                    for Xn, X in PROJ:
                        uj = proj(word(psi_j[k]), X); ujp = proj(word(psi_jp[k]), X)
                        assert shat(uj) == shat(ujp)
                        Z = cnt_sub(N2(uj), N2(ujp))
                        assert all(v >= 0 for v in Z.values()), ('Z<0', tag, j, jp, k, Xn, Z)
                        orig = orig_deleted_windows(inst, comps, ey, U[j], U[jp], k, X, Xn)
                        assert Counter(Z) == Counter(w[4] for w in orig), ('P1 identity', tag, j, jp, k, Xn, Z, orig)
                        for w in orig:
                            assert w[2] not in inst.marked and w[3] not in inst.marked
                        assert not bnd(Z), ('circulation', Z)
                        Zk[Xn] = Counter(Z); sumZ[Xn] += Counter(Z)
                        if Z: any_nz = True
                    # shared-letter conservation per kappa
                    inA = Zk['A']['ac'] + Zk['A']['cc']; inB = Zk['B']['bc'] + Zk['B']['cc']
                    outA = Zk['A']['ca'] + Zk['A']['cc']; outB = Zk['B']['cb'] + Zk['B']['cc']
                    assert inA == inB and outA == outB, ('c-conservation', Zk)
                    # participation lemma
                    if not Zk['A']: assert set(Zk['B']) <= {'bb'}, Zk
                    if not Zk['B']: assert set(Zk['A']) <= {'aa'}, Zk
                # whole-word identity
                for Xn, X in PROJ:
                    assert shat(proj(Wj, X)) == shat(proj(Wjp, X))
                    assert Counter(cnt_sub(N2(proj(Wj, X)), N2(proj(Wjp, X)))) == sumZ[Xn], 'whole-word'
                if inst.Lmem:
                    assert inst.Lmem(Wj) and inst.Lmem(Wjp), 'W_j not in L'
                if any_nz: nonzero += 1
                if trace and any_nz and STATS['trace_done'] == 0:
                    trace_example(inst, eta, comps, I, U, j, jp, data, ey, tag)
        # B6 greedy on this eta
        k = 0; st_here = 0
        while k < Lc:
            same = [jj for jj in range(k + 1, Lc + 1) if cols[jj] == cols[k]]
            if not same: k += 1; continue
            jp = max(same)
            dels = set(); Zs = {}
            for kap in range(len(comps)):
                for Xn, X in PROJ:
                    for w in orig_deleted_windows(inst, comps, ey, U[k], U[jp], kap, X, Xn):
                        dels.add(w)
                        Zs[(comps[kap][0], Xn)] = Zs.get((comps[kap][0], Xn), Counter()) + Counter([w[4]])
            # classify HC-type of this stage (per kappa support)
            kz = {}
            for w in dels:
                kz.setdefault(w[0], Counter())
            perk = []
            for kap in range(len(comps)):
                sup = set()
                for Xn, X in PROJ:
                    for w in orig_deleted_windows(inst, comps, ey, U[k], U[jp], kap, X, Xn): sup.add(Xn + ':' + w[4])
                perk.append((comps[kap][0], frozenset(sup)))
            nzk = [pk for pk in perk if pk[1]]
            if len(nzk) == 2 and nzk[0][0] == nzk[1][0]:
                STATS['stage_two_nonzero_kappa_same_root'] += 1
                ab = [pk for pk in nzk if pk[1] == frozenset({'A:aa', 'B:bb'})]
                other = [pk for pk in nzk if pk not in ab]
                if ab and other and any(e.endswith('cc') for e in (other[0][1] if other else ())):
                    STATS['stage_HCIII_B_shape'] += 1
                    if STATS['example_hc3'] == 0:
                        STATS['example_hc3'] = 1
                        log('    [HC_III-shaped real stage] %s eta=node %d (%s), j=%d<j\'=%d, per-kappa supports %s'
                            % (tag, eta.id, eta.rule.lhs, k, jp, [sorted(p[1]) for p in perk]))
            elif len(nzk) == 2:
                STATS['stage_two_nonzero_kappa_diff_root'] += 1
            elif len(nzk) == 1:
                STATS['stage_one_nonzero_kappa'] += 1
            ids = {(w[0], w[1], w[2], w[3]) for w in dels}
            assert not (ids & deleted_all), 'B6: deletion sets not disjoint'
            assert not (ids & inst.marked_windows), 'B6: marked window deleted'
            deleted_all |= ids
            for key, Z in Zs.items(): state[key] -= Z
            stages += 1; st_here += 1
            if dels: stages_nz += 1
            # invariants
            for i in range(inst.d):
                st_i = {}
                for Xn, X in PROJ:
                    N0 = inst.N0[(i, Xn)]; Nt = state[(i, Xn)]
                    for e in N0:
                        assert min(N0[e], inst.cstar) <= Nt[e] <= N0[e], ('B6 bound', e, N0[e], Nt[e])
                    assert all(v >= 0 for v in Nt.values()) and set(+Nt) <= set(N0)
                    st_i[Xn] = (shat0[(i, Xn)], +Nt)
                y = realise(st_i)
                assert y is not None, ('state not realisable', st_i)
                assert dat(y) == tuple((st_i[Xn][0], tuple(sorted(st_i[Xn][1].items()))) for Xn, _ in PROJ)
                assert set(y) == content0[i], 'content changed'
                # Lemma P flags (c* >= 2)
                if inst.cstar >= 2:
                    xw = word(inst.x[i])
                    for Xn, X, L1 in (('A', A, 'a'), ('B', B, 'b')):
                        if 'c' in xw:
                            def nu(N, w0first): return N['c' + L1] - (1 if w0first else 0)
                            px = proj(xw, X); py = proj(y, X)
                            nux = N2(px)['c' + L1] - (1 if px[-1] == L1 else 0)
                            nuy = N2(py)['c' + L1] - (1 if py[-1] == L1 else 0)
                            assert (nux >= 1) == (nuy >= 1), 'Lemma P flag'
            k = jp
        max_stage_per_eta = max(max_stage_per_eta, st_here)
    STATS['pairs'] += total_pairs; STATS['pairs_nonzero'] += nonzero
    STATS['stages'] += stages; STATS['stages_nonzero'] += stages_nz
    STATS['proj_pairs'] += proj_pairs; STATS['proj_violations'] += proj_viol
    STATS['span_cross_lost'] += span_cross_lost
    if stages_nz >= 2: STATS['instances_2plus_stages'] += 1
    if max_stage_per_eta >= 2: STATS['instances_2plus_stages_one_eta'] += 1
    return total_pairs, nonzero, stages_nz

def trace_example(inst, eta, comps, I, U, j, jp, data, ey, tag):
    """P1-a explicit trace: a substituted piece with empty pi_A (or pi_B)."""
    for k, c in enumerate(data[j][0]):
        for Xn, X in PROJ:
            for (p, q) in windows(c, X):
                ins = [(ch, t) for ch, t in c[p + 1:q] if t[0] == 'i']
                if ins and all(ch not in X for ch, _ in ins) and c[p][1][0] == 'o' and c[q][1][0] == 'o':
                    STATS['trace_done'] = 1
                    log('    [P1-a trace] %s eta=node %d (%s), kappa=%d in root comp %d [%d,%d), j=%d<j\'=%d'
                        % (tag, eta.id, eta.rule.lhs, k, comps[k][0], comps[k][1], comps[k][2], j, jp))
                    log('      phi_kappa      =', word(ey[k]))
                    log('      psi^(j)_kappa  =', word(c), '  (inserted letters in UPPER case:',
                        ''.join(ch.upper() if t[0] == 'i' else ch for ch, t in c) + ')')
                    log('      window %s%s of pi_%s psi^(j): endpoints original %s,%s; span %s contains inserted '
                        '%s which is EMPTY under pi_%s -> span-IMPURE, projection-tag would call it PURE'
                        % (c[p][0], c[q][0], Xn, inst.pos[c[p][1]], inst.pos[c[q][1]],
                           ''.join(ch for ch, _ in c[p:q + 1]), ''.join(ch for ch, _ in ins), Xn))
                    pos_p = inst.pos[c[p][1]][1]; pos_q = inst.pos[c[q][1]][1]
                    orig_between = ''.join(ch for ch, _ in inst.x[comps[k][0]][pos_p:pos_q + 1])
                    log('      original Sigma-span between these letters in x:', orig_between,
                        '-> in pi_%s(x) they were%s consecutive' %
                        (Xn, '' if len(proj(orig_between, X)) == 2 else ' NOT'))
                    log('      colour(span) equal at j and j\':', colour(data[j][0], 'span') == colour(data[jp][0], 'span'))
                    for Xn2, X2 in PROJ:
                        Z = cnt_sub(N2(proj(word(data[j][0][k]), X2)), N2(proj(word(data[jp][0][k]), X2)))
                        log('      Z_{kappa,%s} =' % Xn2, dict(sorted(Z.items())))
                    return

# ---------------------------------------------------------------- typed minimality DP for OV2
def typed_min_count(G, target_nt, T):
    """min node count and number of min derivations for typed nonterminal (nt, content tuple)."""
    best = {}
    def content(r, kidtypes):
        out = []
        for comp in r.tmpl:
            s = set()
            for t in comp:
                if isinstance(t, str): s.add(t)
                else: s |= kidtypes[t[0]][t[1]]
            out.append(frozenset(s))
        return tuple(out)
    ch = True
    while ch:
        ch = False
        for r in G.rules:
            pools = [[(ty, v) for (n, ty), v in best.items() if n == k] for k in r.kids]
            def rec(j, tys, size, num):
                nonlocal ch
                if j == len(pools):
                    key = (r.lhs, content(r, tys)); s = size + 1
                    old = best.get(key)
                    if old is None or s < old[0]:
                        best[key] = (s, None); ch = True
                    return
                for ty, (sz, _) in pools[j]: rec(j + 1, tys + [ty], size + sz, None)
            rec(0, [], 0, None)
    # counts at minimum (second pass, bottom-up by size)
    cnt = {}
    keys = sorted(best, key=lambda k: best[k][0])
    for key in keys:
        n, ty = key; tot = 0
        for r in G.by_lhs[n]:
            pools = [[(ty2, v) for (n2, ty2), v in best.items() if n2 == k] for k in r.kids]
            def rec(j, tys, size, num):
                nonlocal tot
                if j == len(pools):
                    if content(r, tys) == ty and size + 1 == best[key][0]: tot += num
                    return
                for ty2, (sz, _) in pools[j]:
                    if (r.kids[j], ty2) in cnt: rec(j + 1, tys + [ty2], size + sz, num * cnt[(r.kids[j], ty2)])
            rec(0, [], 0, 1)
        cnt[key] = tot
    key = (target_nt, tuple(frozenset(t) for t in T))
    return best[key][0], cnt[key]

# ---------------------------------------------------------------- negative control 3: empty piece
def neg_control_empty_piece():
    """Simulate a NON-eps-free replacement (an EMPTY piece).  phi = b a b a b; the
    middle b (U_j' \\ U_j) is replaced by the empty word.  Both span colours are equal
    (no inserted letter survives, shat unchanged), but the windows whose span met the
    removed letter are not counted: the original-window identity fails."""
    t = lambda ch, k: (ch, ('o', k))
    phi = [t('b', 1), t('a', 2), t('b', 3), t('a', 4), t('b', 5)]
    psi_j = phi; psi_jp = phi[:2] + phi[3:]
    cj = colour([psi_j], 'span'); cjp = colour([psi_jp], 'span')
    Z = {Xn: cnt_sub(N2(proj(word(psi_j), X)), N2(proj(word(psi_jp), X))) for Xn, X in PROJ}
    expected = {'A': Counter({'aa': 1}), 'B': Counter({'bb': 2})}   # windows whose span contains position 3
    detected = (cj == cjp) and any(Counter(Z[x]) != expected[x] for x in Z)
    return detected, cj == cjp, Z

def exhibit_projtag():
    """Deterministic search (seed 3) for the smallest-eta COUNTEREXAMPLE (A) to the
    projection-only impurity colour inside family OV2 (full assumption set: L=L_eq,
    typed node-minimal root (B_M)_T, good fan-out 2 / rank 2)."""
    rng = random.Random(3); best = None
    for M, cs in ((4, 1), (4, 2), (5, 1), (5, 2), (5, 3)):
        G = grammar_ov(M); th, _ = G.thickness(); shorts = G.short_tuples(th)
        for rep in range(30):
            Rn = full_tree_ov(G, M, rng)
            sroot = Node([r for r in G.by_lhs['S'] if r.kids == ('B%d' % M, 'S')][0],
                         [Rn, Node([r for r in G.by_lhs['S'] if r.tmpl == (('c',),)][0], [])])
            inst = Instance(G, sroot, Rn, cs, shorts, rng, L_eq, 'fixed')
            for eta in inst.etas:
                comps, I, U, Lc = inst.analyse_eta(eta); ey = ev(G, eta, {})
                if best and Lc >= best[0]: continue
                data = [inst.stage_data(eta, comps, I[j], 's') for j in range(Lc + 1)]
                pc = [colour(q, 'proj') for q, _ in data]
                for j in range(Lc + 1):
                    for jp in range(j + 1, Lc + 1):
                        if pc[j] != pc[jp]: continue
                        for k in range(len(comps)):
                            for Xn, X in PROJ:
                                Z = cnt_sub(N2(proj(word(data[j][0][k]), X)), N2(proj(word(data[jp][0][k]), X)))
                                orig = Counter(w[4] for w in orig_deleted_windows(inst, comps, ey, U[j], U[jp], k, X, Xn))
                                if Counter(Z) != orig and (not best or Lc < best[0]):
                                    best = (Lc, M, cs, inst, eta, comps, I, U, j, jp, data, ey, k, Xn, Z, orig)
    assert best, 'proj-tag exhibit not found'
    Lc, M, cs, inst, eta, comps, I, U, j, jp, data, ey, k, Xn, Z, orig = best
    up = lambda c: ''.join(ch.upper() if t[0] == 'i' else ch for ch, t in c)
    log('[5] EXHIBIT proj-tag COUNTEREXAMPLE (A), full assumptions: OV2(M=%d), c*=%d, typed-minimal root (B%d)_T,'
        ' eta=node %d (%s, %d leaves), j=%d<j\'=%d' % (M, cs, M, eta.id, eta.rule.lhs, Lc, j, jp))
    log('      phi =', [word(c) for c in ey])
    for jj in (j, jp):
        log('      j=%d I=%s psi=%s' % (jj, [(n.id, n.rule.lhs) for n in I[jj]], [up(c) for c in data[jj][0]]))
    log('      proj colours equal:', colour(data[j][0], 'proj') == colour(data[jp][0], 'proj'),
        ' span colours equal:', colour(data[j][0], 'span') == colour(data[jp][0], 'span'))
    log('      kappa=%d %s: Z(proj pair)=%s  but original deleted windows=%s' % (k, Xn, dict(sorted(Z.items())), dict(sorted(orig.items()))))
    log('      W_j in L_eq:', L_eq(data[j][1]), ' W_j\' in L_eq:', L_eq(data[jp][1]))
    return True

# ---------------------------------------------------------------- driver
def main():
    rng = random.Random(20261114)
    log('== Round 9 overlap P1/B6 real-derivation checker; seed 20261114 ==')
    # [0] grammars
    G0 = grammar_cfg(); G0.check_good()
    W0 = G0.words_upto(6)
    allw = set()
    def gen(n, pre=''):
        if n == 0:
            if pre: allw.add(pre)
            return
        gen(n - 1, pre)
        if pre == '' or True:
            pass
    from itertools import product
    Leq6 = {''.join(p) for n in range(1, 7) for p in product('abc', repeat=n) if L_eq(''.join(p))}
    assert W0 == Leq6, 'CFG0 != L_eq up to 6'
    log('[0] CFG0 good, reduced; L(CFG0)=L_eq on all %d words of length<=6' % len(Leq6))
    for M in (2, 5, 6):
        G = grammar_ov(M); G.check_good()
        for r in G.rules:   # soundness: every rule balanced
            bal = sum((1 if t == 'a' else -1 if t == 'b' else 0) for c in r.tmpl for t in c if isinstance(t, str))
            assert bal == 0, r
        if M == 2:
            W = G.words_upto(6); assert W == Leq6, 'OV2 != L_eq'
        log('[0] %s good, fan-out 2, rank 2, reduced, rules=%d, all rules balanced (L(G)=L_eq%s)'
            % (G.name, len(G.rules), '; bounded check len<=6 exact' if M == 2 else ''))
    log('[0] L_eq = Sigma^+ cap g^{-1}(0), g(a)=1,g(b)=-1,g(c)=0: (2,c_Sigma)-substitutable by '
        'prop:abelian-coset-filter(ii) (Sigma^+ trivially substitutable), CFL hence 2-MCFL; '
        'membership depends only on |w|_a,|w|_b, which are functions of dat_ov.')
    # [1] typed minimality for OV2
    for M in (2, 3, 4):
        G = grammar_ov(M)
        sz, num = typed_min_count(G, 'B%d' % M, (set('ac'), set('bc')))
        exp_num = 1
        for m in range(M + 1):
            exp_num = 2 if m == 0 else 2 * exp_num * exp_num
        assert sz == 2 ** (M + 1) - 1 and num == exp_num, (M, sz, num, exp_num)
        log('[1] OV2(M=%d): typed root (B%d)_T, T=({a,c},{b,c}): min nodes %d = 2^(M+1)-1, '
            'number of minimal typed derivations %d (= all full trees; escapes excluded)' % (M, M, sz, num))
    # [2-4] families
    fam_counts = Counter()
    # family OV2-typed (root arity 2, typed-minimal x; eta components in different root comps)
    for M, cs, reps in ((5, 3, 20), (6, 3, 20), (6, 2, 12), (5, 1, 12)):
        G = grammar_ov(M); th, _ = G.thickness(); shorts = G.short_tuples(th)
        for rep in range(reps):
            for mode in ('fixed', 'hash'):
                Rn = full_tree_ov(G, M, rng)
                sroot = Node([r for r in G.by_lhs['S'] if r.kids == ('B%d' % M, 'S')][0],
                             [Rn, Node([r for r in G.by_lhs['S'] if r.tmpl == (('c',),)][0], [])])
                inst = Instance(G, sroot, Rn, cs, shorts, rng, L_eq, mode)
                check_instance(inst, 'OV2typed(M=%d,c*=%d,%s,#%d)' % (M, cs, mode, rep), trace=True)
                fam_counts['OV2typed'] += 1
    log('[2-4] family OV2typed done: instances=%d' % fam_counts['OV2typed'])
    # family OV2-root1 (root = sentence, arity 1; both eta components in SAME root component)
    for M, cs, reps in ((5, 3, 20), (6, 3, 12), (5, 2, 12)):
        G = grammar_ov(M); th, _ = G.thickness(); shorts = G.short_tuples(th)
        for rep in range(reps):
            for mode in ('fixed', 'hash'):
                Rn = full_tree_ov(G, M, rng)
                inner = rand_tree(G, rng, 'S', 0, 3)
                sroot = Node([r for r in G.by_lhs['S'] if r.kids == ('B%d' % M, 'S')][0], [Rn, inner])
                inst = Instance(G, sroot, sroot, cs, shorts, rng, L_eq, mode)
                same_root = sum(1 for e in inst.etas if len(e.rule.tmpl) == 2)
                STATS['etas_two_comps_same_root'] += same_root
                check_instance(inst, 'OV2root1(M=%d,c*=%d,%s,#%d)' % (M, cs, mode, rep), trace=True)
                fam_counts['OV2root1'] += 1
    log('[2-4] family OV2root1 done: instances=%d' % fam_counts['OV2root1'])
    for M, cs, reps in ((5, 3, 20), (6, 3, 12), (4, 2, 12)):
        G = grammar_ov3(M); G.check_good()
        for r in G.rules:
            assert sum((1 if t == 'a' else -1 if t == 'b' else 0) for c in r.tmpl for t in c if isinstance(t, str)) == 0
        th, _ = G.thickness(); shorts = G.short_tuples(th)
        for rep in range(reps):
            for mode in ('fixed', 'hash'):
                Rn = full_tree_ov(G, M, rng)
                inner = rand_tree(G, rng, 'S', 0, 3)
                sroot = Node([r for r in G.by_lhs['S'] if r.kids == ('B%d' % M, 'S')][0], [Rn, inner])
                inst = Instance(G, sroot, sroot, cs, shorts, rng, L_eq, mode)
                check_instance(inst, 'OV3root1(M=%d,c*=%d,%s,#%d)' % (M, cs, mode, rep), trace=True)
                fam_counts['OV3root1'] += 1
    log('[2-4] family OV3root1 (good, balanced rules) done: instances=%d' % fam_counts['OV3root1'])
    # family CFG0 (degenerate fan-out 1)
    G = G0; th, _ = G.thickness(); shorts = G.short_tuples(th)
    for rep in range(200):
        t = rand_tree(G, rng, 'S', 0, 9, 0.8)
        for cs in (1, 2, 3):
            inst = Instance(G, t, t, cs, shorts, rng, L_eq, 'hash')
            check_instance(inst, 'CFG0(#%d,c*=%d)' % (rep, cs), trace=True)
            fam_counts['CFG0'] += 1
    log('[2-4] family CFG0 done: instances=%d' % fam_counts['CFG0'])
    # random good grammars, roots: sentence (arity 1) and an inner fan-out-2 node
    gdone = 0; gid = 0; skipped = Counter()
    while gdone < 200:
        gid += 1
        G = random_grammar(rng, gid)
        try:
            G.check_good()
        except AssertionError:
            skipped['grammar_not_reduced'] += 1; continue
        th, inside = G.thickness()
        if th > 40: skipped['thick'] += 1; continue
        shorts = G.short_tuples(th, 30)
        if any(not shorts[n] for n in G.arity): skipped['no_short'] += 1; continue
        gdone += 1
        for rep in range(3):
            t = rand_tree(G, rng, 'S', 0, 7, 0.8)
            order = number(t)
            if len(order) < 8: skipped['tiny_tree'] += 1; continue
            cands = [n for n in order if len(n.rule.tmpl) == 2 and sum(1 for _ in [0]) and len(n.kids) > 0]
            roots = [t] + ([rng.choice(cands)] if cands else [])
            for R in roots:
                for cs in (1, 2, 3):
                    try:
                        inst = Instance(G, t, R, cs, shorts, rng, None, 'hash')
                    except AssertionError as ex:
                        raise
                    check_instance(inst, '%s(#%d,root=%s,c*=%d)' % (G.name, rep, R.rule.lhs, cs))
                    fam_counts['RAND'] += 1
    log('[2-4] random good grammars: %d grammars, %d instances, skipped=%s' % (gdone, fam_counts['RAND'], dict(skipped)))
    # [5] negative controls
    det, sameCol, Z = neg_control_empty_piece()
    assert det, 'empty-piece control not detected'
    log('[5] empty replacement piece (non-eps-free simulation): span colours equal=%s, Z_A=%s but the '
        'deleted original window is aa -> identity FAILS (detected). eps-freeness is used.' % (sameCol, Z))
    assert STATS['proj_violations'] > 0, 'projection-only colour control not detected'    log('[5] projection-only impurity colour: %d same-colour pairs, %d violate Z>=0 or the original-window '
        'identity (DETECTED; span tagging is necessary)' % (STATS['proj_pairs'], STATS['proj_violations']))
    assert STATS['span_cross_lost'] > 0
    assert exhibit_projtag()
    log('[5] marked windows whose Sigma-span crosses an eta component and are NOT literally present in some W_j: %d '
        '(position-form protection of marked WINDOWS fails; count form unaffected)' % STATS['span_cross_lost'])
    assert STATS['instances_2plus_stages'] > 0 and STATS['instances_2plus_stages_one_eta'] > 0
    assert STATS['pairs_nonzero'] > 0 and STATS['stage_HCIII_B_shape'] > 0
    log('SUMMARY', dict(sorted(STATS.items())))
    log('ALL CHECKS PASSED')

if __name__ == '__main__':
    main()
END SOURCE check_round9_overlap_P1_B6_2026-11-14.py

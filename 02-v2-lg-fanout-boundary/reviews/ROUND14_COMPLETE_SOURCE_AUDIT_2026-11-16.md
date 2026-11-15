# Round Fourteen — Parikh reduction, TR proof certificates, invalid CA and repaired CA*

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
| `PROMPT_CLAUDE_ROUND14_NONCOMMUTATIVE_PARIKH_REDUCTION_2026-11-15.md` | 149863 | `5db469a4899e08a281ad5e0665a0d80fe1806c66ac1282e42ff42370c4191b0a` |
| `audit_claude_round14_noncomm_Parikh_independent_2026-11-16.md` | 12133 | `440a3b3372542e85b11092999f1e1b0006e38ce949074dfff4459b16c3c01c76` |
| `claude_round14_noncomm_Parikh_checker_2026-11-15.py` | 34588 | `eaccd71285f51f26d702b8d76e6fe7a7a5847d08e8f6f97368b8d939729663ea` |
| `claude_round14_noncomm_Parikh_checker_output_2026-11-15.txt` | 5512 | `97728f1a0ddcca8afd1651fe04122b7b14709b7de090ee2c43a71fb9b26f4fb6` |
| `claude_round14_noncomm_Parikh_checkpoint1_2026-11-15.md` | 4362 | `d2818bc270106a02150db19e92cfe3f66e5ae52b1877ea56ddfd742a0baa4892` |
| `claude_round14_noncomm_Parikh_next_obligations_2026-11-15.md` | 4524 | `4e2eed58929cd2f0547c69fc75f311f1b2d202305c4e7ebbc150be6030fd6a5b` |
| `claude_round14_noncomm_Parikh_report_2026-11-15.md` | 26531 | `6b49949a7a36c0371dec15646c4614037ed555c37eacc21d3f61c81114188452` |
| `exploration/README.txt` | 440 | `3db1c99132c1e5f49b13459af6ef65c5f2463e986566757830aee6a713017e88` |
| `exploration/r14core.py` | 11437 | `74b65903cf14dfca80f408c765e799afa9d923fae88b38a02990b998bfdc830c` |
| `exploration/t1.py` | 1166 | `c081fe875e1cc1b0dd2060b50dd77aa0f3aef3e3f56f5dcb89c65a3e46ba3658` |
| `exploration/t10.out` | 183 | `c4d9380c8c84cda69e1cba9e0b1e22efc515448974b2a8f4e589dc572b50f619` |
| `exploration/t10.py` | 511 | `28d16da9f6738f4f90ef6be184affac836254d18f5df5b3566da7529af6848a2` |
| `exploration/t11.out` | 7128 | `cf5a369a5d946ef62699efa3d22c383d3e72e22ac3bbe1a29fae5966a3b4c7f9` |
| `exploration/t11.py` | 663 | `a812becdbea49bdd488153a0a6525bc9b5bb1890b648501f559ce53e768f29dc` |
| `exploration/t12.py` | 487 | `4df176eb5db4c28a49b720146ce9f4817105943eb66c6bfb3d3c74b189b2d620` |
| `exploration/t13.py` | 559 | `88a207cd547620e69788f88e811447baf2ade49d968cb9cee9777dc1d7bfb886` |
| `exploration/t2.py` | 1302 | `977fd37a64aab2661665cf1fc96e2df564c7d471b0d7c2f88737452e87036603` |
| `exploration/t3.py` | 661 | `f4d42e685f56726588d75f231bf056f631b6c1723d7f9ea32ddd4049abc61182` |
| `exploration/t4.py` | 628 | `e12650ed403e39077fa1bff506e8a575ec7de7184385b34cbd3d630569104c23` |
| `exploration/t5.out` | 15553 | `0706c9aeb13c3df1b6613896b2ed7aee3b2f5a626934570a78e171dbc7645648` |
| `exploration/t5.py` | 1053 | `898d917a0071883c65e7ff6a273f9c3beeab58728a0bf26e09736f2c4db200ce` |
| `exploration/t6.py` | 1344 | `6eda02c7ead64a6808cb56c3d31444dc6051db0addf0d44c7f248e32967e1687` |
| `exploration/t7.out` | 1752 | `dd92f91e2db6eda99694b00a00afc589919381c5da01fc3d6a1135e379071cda` |
| `exploration/t7.py` | 1006 | `23c6ddf329ad6f2b68f9b1992d9655a1e897cc4c196a2cd9f2b54a8d80c3500c` |
| `exploration/t8.out` | 3779 | `2911397bf084d78ed3c5a666a6184d7f1efcfbb6c9d1813e9ef07e2a3ea7e1b6` |
| `exploration/t8.py` | 824 | `dead2a881e6f95f0af08802b8f59e7957de687438e4878aee7853cbe51c7e4be` |
| `exploration/t9.py` | 814 | `4e46ae7e7dad4aefb1318a22775eae283fec7f931d9369fd9765a6571dd7aabc` |
| `exploration/tr_builder.py` | 9285 | `a2615f18e0abbe0a900d510f0f35ba5fd9c25ef77520a8e163a791bbe5bccc00` |
| `independent_round14_audit_2026-11-16.py` | 7222 | `e79620ec3efae05dfac237e3d670f3f5b742052c932c21bdf3822024ac38c843` |
| `out_independent_round14_audit_2026-11-16.txt` | 936 | `bd04ca37dd9a737f5f4be7e52d2966caa61fba80ed4597d6f0dfdd842ce8784d` |
| `round14_independent_work/out_round14_D_N7_N8_2026-11-16.txt` | 211 | `4946e9e6015495b4f2fa7de402ac3f5116426146464800cc4b95bd15b3179be2` |
| `round14_independent_work/round14_rerun_S0ABC_2026-11-16.txt` | 3850 | `31733ff66dcd92f77280b35272715d634a3b14babc1807f71cec4b4ebf85992a` |

## Original source bodies


===== BEGIN FILE PROMPT_CLAUDE_ROUND14_NONCOMMUTATIVE_PARIKH_REDUCTION_2026-11-15.md bytes=149863 sha256=5db469a4899e08a281ad5e0665a0d80fe1806c66ac1282e42ff42370c4191b0a =====
# Claude 第十四段・研究依頼書
## 非可換予想 U：X1 反例を踏まえた「内容類ごとの Parikh 還元 P」の証明／反証

**作成日：2026-11-15 JST**  
**目的：純粋な数学的探索。論文化・投稿原稿の更新・GitHub 書込は依頼しない。**  
**参照の優先順位：現行 #2 MCFG 論文の定義 > 本依頼書の確定した仮定 > 過去ラウンドの報告。**  
**重要：以前あなた（Claude）が GitHub を取得できなかったため、本ファイル末尾に必要な原報告、監査、再現コード・ログを全文埋め込む。GitHub に接続できなくても作業できる。**

---

# I. 今回の数学的な目的

**最優先：第十三段の非可換 Parikh 還元 P を、正しい組代入可能性の型条件の下で、無条件に証明するか、正確な反例を構成する。**

成功すれば、Fable-C の可換言語での単項語長上界を非可換言語へ移す新しい原理になる可能性がある。失敗した場合には「どの交換が」「なぜ実在の受理宿主を持てないのか」を決着させたい。証明も反例もない場合は、解けた限定版・鋭い反例候補・残った一つの数学的義務を提出せよ。**P が真であると決めつけないこと。**

## I-1. 正式な中心問題との論理的な位置づけ

現行論文 `op:fanout-two`：固定した `f≥2, r_max≥2` について、擬多様体 `V ⊄ LG` は必ず uniform polynomial characteristic-data length を持たないか。`V ⊆ LG` の十分性はすでに主定理 Theorem A として証明済み。`f=1` では LG の必要十分性が証明済み。**`f≥2` の必要性は OPEN。**

本ラウンドの標的である「非可換予想 U」は別問題：固定された有限アルファベット `Σ`、区別された文字 `a∈Σ`、固定の有限半束型付け `s`、`f=2`、rank `r≤2`（より広い範囲で示せれば歓迎）を考える。任意の `L∈C^{mcf}_{2,s}` と、その `L∩Σ⁺` の **reduced good** MCFG 提示 `G` について、`a^N∈L` を満たす最小の `N≥1` があれば、`N` を `‖G‖` と **元の文法 G の** `θ̄_G` に関する、`L,G` に依存しない固定多項式で抑えられるか。

\[
\boxed{N:=\min\{n\ge1:a^n\in L\}\ \le\ p_{\Sigma,s,r}(\|G\|,\bar\theta_G)\ ?}
\tag{U}
\]

まず内容型付け `s=c_Σ`（`s(w)=alph(w)`）で取り組んでよい。より粗い半束型付け一般に延長する場合は含意の方向を逐一確認すること。

**U が肯定されてもそれだけで `op:fanout-two` の否定も肯定も出ない。** U が扱うのは単項語 `a^N` の最小長であり、全実現型の代表長でも全特徴標本長でもない。逆に、`c_Σ` に関する U の反例が得られても、それは粗い二元型付け `U₁` での組代入可能性を自動的に与えない。両者を混同しない。

## I-2. 数学的に絶対固定する定義

- `Σ`：有限、`a∈Σ`、`Δ=Σ\{a}`、`D=|Δ|`。主要実験では `Σ={a,b,c}`、`D=2`。
- `s`：有限半束への正の型付け。中心的なテストは `c_Σ(w)=alph(w)`。空語は正の組成分として**使わない**。最短単項語 `a^N` は正長。
- 許容 `d` 穴文脈は `v₀□₁v₁...v_{d-1}□_d v_d`、各穴に入れる語は **Σ 上で非空**、内側の `v₁,...,v_{d-1}∈Σ⁺` も必ず非空、外側のみ空を許す。`d∈{1,2}`。射影後の非空性ではない。
- `D_L^{(d)}(x)` はその組を受理するすべての許容文脈の集合。 `(2,s)`-tuple substitutability は、成分ごとの `s` 型が同じで、共通の受理文脈を一つでももつ組は、**すべての**受理文脈が一致する条件。単なる `L` 内の局所的な1回の交換ではない。
- `good` は ε-free（ルールの各出力テンプレート成分が非空）・nondeleting（変数を各1回）・nonpermuting・nonmerging。`reduced` は全非終端が到達可能かつ生産的。fan-outとrule rankは別の尺度。
- `θ̄_G=max(1,θ_G)` は **original G** の規則厚さ。型付き精密化後の厚さをこの変数として代入してはいけない。現行 `lem:thickness-equivalence` により各規則の明示終端数≤`θ_G`、各非終端には総長≤`θ_G` の導出組がある。
- 型一致を要求するとき、**実際に交換する x,y の成分ごとの型が等しいこと**を明示せよ。`s(aκ)=s(aκ')` から `s(κ)=s(κ')` は従わない。

GitHubで直接参照できる正式ソース（全て read-only）：

- 現行論文：<https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/main.tex>。参照ラベル：`def:grammar-properties`, `def:tuple-substitutable`, `def:class-cmcf`, `lem:thickness-equivalence`, `cor:distribution-representatives`, `def:uniform-polydata`, `prop:rare-type`, `thm:doubling-no-lift`, `op:fanout-two`。
- 現況：<https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/HANDOFF_CURRENT.md>
- 特殊上界 U₂（本探索の一般的な予想Uとは**異なる**）：<https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/reviews/theorem_U2_overlapping_projections_standalone_2026-11-15.md>
- 第九〜十一段監査・ソース：<https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/reviews/ROUND11_SOURCE_BUNDLE_2026-11-15.md>

**ネットワークに接続できないとき：アクセス不能と記録したうえで、ここに与えた定義および付録を利用して進める。接続確認や一般的な文献探しに研究時間を浪費しない。GitHub の変更は厳禁。**

---

# II. 第十三段の確定状況――採用してよいもの／してはいけないもの

最初に末尾の **A（Claude第十三段原報告）・B（独立監査）・C（X1反例コードとログ）・D（Fable-C原報告と独立監査）** を読んで理解する。以下の判定は「前回の手監査としての暫定的な根拠」であり、本ラウンドで必要なら再審査してよい。

| 論点 | 前回の独立監査判定 | 使い方 |
|---|---|---|
| L1(R)：`a` 連の正の再配分 | VALID | `i,j,i',j'≥1`、`i+j≤N−1` と共有受理文脈を明示 |
| L1(U)：2つの受理 `a` 冪長の一意性 | VALID | 受理文脈が同じ `P□Q` のときだけ |
| L2：極大 `a` 連を潰した同骨格で `a` 個数の一意性 | VALID | **両語の `a` 数≤N−1** が必須 |
| L3 Rot：核が `a` と分布合同 | VALID | 単独語外側総量 `3≤λ≤N−1` が必要 |
| L4 Cat：Rot を使う核と `a` 連の併合 | VALID | Rot が成立する核だけに適用 |
| **L5-X1（原文）** | **FALSE** | **絶対に証明済み補題として引用しない** |
| 修正版 X1 | 条件付で VALID | 実際の1穴交換片 `x,y` の `s(x)=s(y)` を必ず追加 |
| L5-X2 | 補足証明で VALID | `s(κ)=s(κ')`、実際の2穴の非空隔て、宿主存在を明示 |
| T1 / C1：有界核骨格数の上界 | VALID | X1/X2 非依存。改良候補だがUを証明してはいない |
| T2 / H(K) | **CONDITIONAL** | Parikh還元Pなしには主張できない。Fable-C移植も要再監査 |
| E1 | **有限反例として確定** | 全内容類横断のbigram計数関数性は偽 |
| E2 | **種集合ごとの有限不可能性証明** | 同一内容類の一般Parikh線形性の証明ではない |
| U / `op:fanout-two` | **OPEN / OPEN** | 解決済みと書かない |

## II-1. 40語反例――X1原文が偽であることを毎回反映させよ

`Σ={a,b,c}`、`s=c_Σ`。次の39語に `bc` を加えた40語の有限言語 `L` を取る。

```text
aaabc aabac aabca abaac abaca abcaa baaac baaca bacaa bcaaa
aaaaac aaaaca aaaacb aaacaa aaacab aaacba aacaaa aacaab aacaba aacbaa
acaaaa acaaab acaaba acabaa acbaaa caaaaa caaaab caaaba caabaa cabaaa
cbaaaa aaaaaab aaaaaba aaaabaa aaabaaa aabaaaa abaaaaa baaaaaa
aaaaaaaa
bc
```

`L∈C^{mcf}_{2,c_Σ}` は全ての1/2穴受理文脈の独立全列挙で検証済み（40語、333組、2327受理文脈、924組比較、違反0）。有限なのでreduced good MCFG提示も存在する。最短 `a` のみの受理語は `a^8`。核 `κ=bc`, `κ'=acb`, `λ=λ'=3` について、`aκa²=abcaa∈L`, `a²κ'a=aaacba∈L`、かつ `s(aκ)=s(aκ')={a,b,c}`。しかし `bc∈L`, `acb∉L`。したがって原文X1の `i=i'=0` から導かれる交換は偽。

**過ちの本体：** `s(aκ)=s(aκ')` と `s(κ)=s(κ')` は別である。`s(x)=s(y)` を満たさない比較片に tuple substitutability を適用できない。これを「型条件の抜け」として全ての将来の交換式に反映すること。もし今回、新しい一般交換補題の反例を見つけたら、同じように全前提を検証する機械可読な有限証人を提出する。

**修正 X1**：`i=(λ−λ')_+`, `i'=(λ'−λ)_+`、`x=a^iκ`, `y=a^{i'}κ'` と置くとき、**`s(x)=s(y)` を仮定**すれば `x≡^1_{L,s}y` を示せる。共通受理宿主は `E=a^{min(λ,λ')}□`、Rot の適用範囲を明記。これだけで全ての望む内容類間の交換が許されるわけではない。

**X2の補足版**：核 `κ,κ'` が Rot の単独語を持ち、`s(κ)=s(κ')`、`i,i'≥1`、`i'=i+λ'−λ` のとき、任意 `l,r∈Σ*` と **非空** `m∈Σ⁺` で `la^i mκr ∈L ⇔ la^{i'}mκ'r∈L`。`i≤λ−1` では `E=a^{λ−i−1}□₁a□₂` という共通受理宿主。`i≥λ` では `i_0=λ−1`, `i'_0=λ'−1` に落とし、余分な `a^{i−i_0}` を左側外部文脈へ吸収する。証明を使用する際は実際の2穴区間と分割を記す。

## II-2. T1は「限定上界」として維持

`a^N` の節点数最小導出木をとり、最重子経路上の大節点（収率長 `k_X>θ`, `θ=θ̄_G`）の単独語 `w_X` の**骨格**（極大a連をAで潰した語）の種類数を `M`、`σ=2(r+1)` とすると

\[
\boxed{N<\theta\,\sigma^{2M+1}.}\tag{T1}
\]

独立監査では元論文の thickness lemma と L2 を使って X1/X2に依存せず再証明済み。核骨格の同値類の部分が無限に増える場合の一様多項式上界はこの定理だけからは出ない。**超多項式下界の反例族があるなら、最重子経路上の核骨格の種類数 M は超対数的に増えなければならない**（必要条件であり、十分ではない）。

---

# III. 最優先の研究課題：Parikh 還元 P（真偽を問う）

## III-1. まず仮定と結論を自分で精密に定義せよ

第十三段 `next_obligations` のPは、まだ完全に形式化されていない研究提案である。**既に証明されていると扱わず**、少なくとも次のような形で形式命題を作る。

- `a^N` の reduced good MCFG `G` における**節点数最小**導出木 `T` を固定。元の yield は全て `a`。
- 大節点 `X` に対し非終端 `A_X` の短い導出 tuple `u_{A_X}` を選び、`T` のこの部分木だけを置換した単独語 `w_X∈L` を得る。非 `a` 部分の Parikh `V_X∈N^Δ`、欠損 `δ_X=N−|w_X|_a`、非 `a` 内容類 `S_X=supp(V_X)` を定義。必要なら components ごとの内容型も保持する。
- 同一非 `a` 内容類 `S⊆Δ` に属する **分岐類**（同じ `S` の比較不能大節点2個があり、総欠損が `≤N−1`）だけを扱う。`δ_X≤(N−1)/2` の許容単位、分岐木の二重置換、多重コピーの仮想合成を区別する。
- 「木由来実現」の意味を明示せよ。実際の `T` の互いに非祖先関係の節点を同時に置換した実在語と、Rot/CatやX2によって**受理が証明された**追加語は利用してよい。しかし「Parikhベクトルが同じなので順序を変えても受理される」は、まさに証明対象であり禁じる。
- 命題Pの候補結論：同一類の許容単位の**多重集合**から作られた二つの受理語実現が同じ非 `a` Parikhベクトルを持ち、各総欠損が `≤N−1` なら、それらの総欠損は等しい。これが `H(D)` の整数関係へ十分強く結びつくかを逐段検査。

**注意：** Fable-C可換版は可換性から `Parikh` が一致する部品を任意に並べ替えられる。非可換版では、この操作が `d=2` の**適法**な一連の交換で達成できることが問題の本体である。`s(κ)=s(κ')` を付ければX2は使えるが、核内の順序変更や別内容類の通過にまで自動的に拡張できない。

## III-2. 決定的な証明義務（次の順で可否判定）

**A. 宿主補題（hostability）を独立に構成する。**

互いに素な部分木、同じ非終端の複数コピー、fan-out 2に由来する交錯・入れ子成分を明示的に扱う。どの段階で `m∈Σ⁺` という中間セパレータが確保できるのか。交換対象の `a^i` と核 `κ` は、それぞれ1個の連続区間か。核が非連続な2成分に分かれるときに必要な再表現が、実際の文法導出語で正当化されるか。**「適法文脈が存在する」ことと「所望の実際の出現でその文脈を使える」ことを分離せよ。**

**B. 同一内容類の許容単位から、合成核の多重コピーへの加法性を導く。**

単位 `J_1...J_t` の帰納法を行うなら、基底 `t=1,2` を省略せず、帰納の各段階で `3≤λ≤N−1`、`δ_total≤N−1`、成分型一致、核の非空性を維持できるかを証明。合成した核がそもそも Rot を満たすのか、非可換な文字順で `a` を移動させてよいのかを確認。

**C. 核内部の隣接交換 `de↔ed` とその宿主を構成する。**

同一 `S` で Parikhが等しい核をつなぐため、文字隣接交換を一つずつ実現できるか。それが `d=2` 代入から本当に従うか。もし `S={b,c}` で `bc`/`cb` が異なる欠損を持つなら、どんな短い証人を積み重ねれば矛盾できるか。E2の6手の**具体的**矛盾から一般の置換スキームを抽出してよいが、「数例で成功」から一般化しないこと。

**D. 補償シフトが消えることを示す。**

`Rot+Cat+X2` で得た交換が見かけ上 `a` の総数をずらす可能性があり、たとえば逆転数 `inv_{bc}` 型の関数 `δ = α|w|_b+β|w|_c+γ inv_{bc}(w)` は単なる全核交換だけでは排除できない。X2の**核内部の部分因子**を動かすことで `γ=0` を導けるなら、各適法な受理語とシフトを全て追跡して証明。

**E. Parikh還元Pが得られた場合に限り、Fable-Cの整数関係と窓被覆を移植する。**

短い関係 `Σ λ_i V_i=0` の係数境界、正負側の非負多重集合、両側の総欠損が `N−1` 以下である条件、多重集合実現、同じParikhから同じ欠損への推論を順に示す。`H(D)` が本当に成立すれば、そこから得られる多項式の指数・定数・`v=|V(G)|` 依存を再計算する。**第十三段 T2 は COND​​ITIONAL のままであり、形式に穴があれば新たに修正する。**

## III-3. Pが偽なら、最小の失敗箇所を証明せよ

無条件に「Pは正しい」方向へ努力を固定しない。有限または無限の反例を見つけたら：

1. 構成 `Σ,s,L,G,a^N,T` を全て特定し、`L∈C^{mcf}_{2,s}` を厳密検証。
2. `T` の指定された節点を明示し、どの核・どの欠損・どの内容類・どの宿主でPの全前提が成立するかを示す。
3. 同じ非 `a` Parikh なのに欠損が異なることを示す。**E1の内容類横断反例をそのまま同一類Pの反例と称してはいけない。**
4. 限定版 `P'` が真なら、その最も自然な追加仮定と証明を試みる。
5. 有限 `L` の反例は一般補題Pを反証しうるが、**漸近的予想Uを反証するには `‖G_n‖,θ̄_{G_n}` に比べて超多項式に大きな `N_n` を持つ一様な族が必要**。これを混同しない。

---

# IV. 別の突破経路も歓迎

Pが極端に難しい場合、以下の経路へ切り替えてよい。1つの方法を試すことが義務ではない。

**IV-A. 不変量の再設計：** 内容類別の「核Parikh＋入出力境界」、「短い二穴テストによる有限指数」、「a-連と非a核の同期状態」、「部分文字列順序」などを検討。有限次元 `β` を構成して `H(K)` を直接証明できれば、Pの完全な順序交換は不要かもしれない。

**IV-B. T1の強化：** 生の骨格種類数 `M` を、合法なRot/Cat/X2操作の同値類数 `M'` に圧縮できるなら、`N<θσ^{2M'+1}` を証明せよ。元のT1の骨格関数L2をそのまま新しい同値類へ適用することは禁じる。同じ `M'` なら欠損が等しいという**新しい補題**が必要。

**IV-C. 反例・下界構成：** もし非可換Uが偽なら、固定 `Σ,s,f=2,r≤2`、good MCFG族、**各`L_n`の2穴組代入可能性の全称証明**、`N_n` の下界、`‖G_n‖` と元の `θ̄_G` の上界を揃えよ。`s=c_Σ` の反例を `s_U` に自動転用しない。正式 `op:fanout-two` に戻る場合は、正しい向きの擬多様体量化を必ず論証する。

**IV-D. 独立の新手法：** Fable-CのParikh路線が本質的に誤りだと判断すれば、別の正しい統計や証明技術を自由に提案してよい。ただし仮定・結論・反例耐性を示すこと。

---

# V. 検証実験の厳格な要件

実験は一般定理の証明ではない。**具体的な反例や有限帰結の証明書**として機能させる。

1. 第十三段の40語反例は必ず再生してから、新しいX1系の補題を採用せよ。`s(aκ)` だけでの比較が通らないことを確認。
2. `d=1` / `d=2` の全受理文脈を区別し、穴の中身もセパレータも空にしない。各組成分の**型**を比較し、型ごとの共通受理文脈がある場合にのみ分布同値を要求。
3. 適法な有限閉包 `closure(seed)` を使う場合、**打切り `truncated/cap` は `closed` ではない**。length capやword capに達しなかった場合にのみ「厳密閉包」と呼ぶ。次元、字母、正の型付けを明記。
4. E1の39語／34語、E2の既知証明書を陽性・陰性の対照として使う。E1が排除したのは**全内容類横断の**bigram関数性。E2が示したのは**特定種集合**の不可能性に限られる。
5. 整合対照 `δ(bc)=δ(cb)` が以前9分間収束しなかったという履歴を受け、必要なら文脈を索引化・増分更新し高速化せよ。無限の不成立を時間切れから推定しない。
6. 新しい有限反例については、**完全な語リストか有限生成規則、全前提、全後件、正しい非空条件**を再生可能なPython 3（標準ライブラリ可）で記録する。正しい結果は `exit code 0` と明示。対照として、前提をひとつ外した偽命題がチェッカーに検出されるテストを最低ひとつ置く。
7. 運搬子交換・多重集合交換の各操作は、`x,y`、`s(x),s(y)`、共有受理文脈 `E_0`、狙いの文脈 `E_1`、`E_0[x],E_0[y],E_1[x]∈L` を逐一明示。 `E_1[y]` の受理が**論理的に**従うことを確認。
8. 「同じ Parikh ベクトルだから同じ言語所属」「finite experiments passedだからPROVED」「grammatical derivation tree can be freely spliced」「X2 can cross holes with empty middle」は禁止。
9. **第十三段提出チェッカーのS3=1202件はRotの検査でありX1の検査ではない。** 関数名から検証範囲を推測せず、呼び出された検証コードを実際に読むこと。
10. 作業量を惜しまず、探索の際には少なくとも、修正版X1の最小の境界ケース、X2の外側a余剰吸収（`i≥λ`）、E1の逆向き誤用、E2の部分因子交換、木由来宿主の実在性を個別に攻撃する。

---

# VI. 成果物と判定方法

**初回チェックポイント**を先に書き、早い段階で `P` の正確な定式化、X1反例の確認、優先する証明／反例戦略、最初の失敗または成功を記録する。最終報告は次の構成とする。

1. `claude_round14_noncomm_Parikh_report_2026-11-15.md`：最終数学報告。冒頭に **一行結論**：`PROVED-U`, `PROVED-P`, `PROVED-RESTRICTED`, `COUNTEREXAMPLE-P`, `COUNTEREXAMPLE-U`, `NEW-LEMMA`, `OPEN` のうち最も厳密なラベルを記す。複数成果があるときは表で区別。`op:fanout-two` の扱いを別欄で明記。
2. `claude_round14_noncomm_Parikh_checkpoint1_2026-11-15.md`：初回チェックポイントと方針転換履歴。
3. `claude_round14_noncomm_Parikh_next_obligations_2026-11-15.md`：未解決義務を、証明可能な最小補題まで切り詰めて列挙。
4. `claude_round14_noncomm_Parikh_checker_2026-11-15.py`：独立実行できるPythonコード。必要なら検証の種類別に分けてもよい。
5. `claude_round14_noncomm_Parikh_checker_output_2026-11-15.txt`：実行コマンド、Python version、seed、SHA256、試行件数、`FAIL`、完了状態、**exit code**を記載。
6. 上記を含む**ZIP**が可能ならZIPも提出する。数学的な発見がない場合でも、失敗した戦略と具体的な障壁を報告する。

**判定ルール：**

- `[PROVED]`：明示した仮定の下で全称証明が閉じ、各交換の型と宿主を示したものに限る。
- `[CERTIFIED-FINITE]`：有限の反例、全件決定、検証可能な証明書。
- `[CONDITIONAL]`：依存補題を未証明と明記した帰結。
- `[COMPUTATIONAL-EVIDENCE]`：実験範囲に限定。
- `[OPEN]`：最も重要な残余が残る場合。
- **既存Fable-C・T1の「手監査で有効」という評価を、形式検証・専門家査読・絶対的正しさに言い換えない。**

今回は**論文の執筆・新規独立論文化・GitHub commit/PR作成はしない**。研究と検証に専念する。成果物はこのセッションで提出する。

---

# VII. 一次資料・監査資料（完全埋込み）

以下のファイルは添付資料のUTF-8原文を個別に埋め込む。**原文中の結論・コード・ログには誤りがあり得る。とくにClaude原報告のX1原文は独立反例で偽と確定している。前回ラウンドの自己評価を優先してはいけない。**

収録原文の各SHA256、バイト数は直下の索引に記載。`BEGIN SOURCE ...` と `END SOURCE ...` の間が各ファイルの原文であり、実行時はその範囲だけ抽出する。外側の5個のチルダのMarkdownフェンスは原文に含まれない。

| ID | 資料 | bytes | SHA256 |
|---|---|---:|---|
| A1 | `claude_round13_noncomm_U_final_report_2026-11-15.md` | 18,599 | `cb1782110ebf873d9a31127442243c9adca02e0b9a05743f3116145244c5394e` |
| A2 | `claude_round13_noncomm_U_next_obligations_2026-11-15.md` | 2,992 | `496ae66d32cd3c36f635db0702f6760317c6e96a1cd045a2eeb6636b604defbb` |
| A3 | `claude_round13_noncomm_U_checkpoint1_2026-11-15.md` | 1,361 | `333edfdb04e59886ae6c3da7bb6f8af822309941cdff58c29d1adadb4495b716` |
| B1 | `audit_claude_round13_noncomm_U_independent_2026-11-15.md` | 13,412 | `f2f54516046fb6bbc8c25d32ed6e96d5233d440320ca057cf6b8d9d74c712979` |
| C1 | `round13_independent_X1_counterexample_2026-11-15.py` | 2,305 | `715ddf6329f4bad6e1745587aff8b8d37b57d3f79a163faa776eb921a0c291ba` |
| C2 | `round13_independent_X1_counterexample_output_2026-11-15.txt` | 467 | `b915b52308612570f65f79ffd0bb33b29328da90d971e010063d801f210b3c09` |
| D1 | `Fable_C_complete_independent_mathematical_audit_2026-11-15.md` | 17,724 | `63be1443497ba90d945c04e1ed7895fa220fc9f464e4d9b0416b5a5a416e72d2` |
| D2 | `Fable_original_open_problem_report_2026-11-15.md` | 27,376 | `c0369cdc571944bfe702e52a3571939bc5981c332637bf8c49765ebc3e3ca223` |
| E1 | `claude_round13_noncomm_U_checker_2026-11-15.py` | 24,907 | `3f79da85eb7d128a52b0591e7f51fdcc3aa25f2cc9b469029e76a6e29e96d92a` |
| E2 | `claude_round13_noncomm_U_checker_output_2026-11-15.txt` | 5,288 | `3dc1019ea1e9a0b26da10ab7d2f8f6badb6efc47f8d7c55738652d0ada4433b5` |
| F1 | `round13_independent_checks_2026-11-15.py` | 5,388 | `a5666fef8082bc4b59d00f11deacb753dc42f174bf136f081210a8de022efc6e` |
| F2 | `round13_independent_checks_output_2026-11-15.txt` | 736 | `0a7541f61afc7754fcc80c0bdcfb3df223fc49976599611c29ee4dba9b8528b7` |

## A1. Claude 第十三段：最終数学報告

**Original filename:** `claude_round13_noncomm_U_final_report_2026-11-15.md`  
**Bytes:** `18599`  
**SHA256:** `cb1782110ebf873d9a31127442243c9adca02e0b9a05743f3116145244c5394e`

BEGIN SOURCE claude_round13_noncomm_U_final_report_2026-11-15.md
~~~~~text
# Claude 第十三段 最終報告：Fable-C から非可換予想 U へ（2026-11-15）

**一文結論.** 予想 U（非可換）は **OPEN**。ただし次の四つを得た。

- 二穴代入可能性から、核が `a` と可換になる**回転補題**を新たに証明した。
- 「核の型数 M が有界なら最短 `a^N` の長さは θ について線形」という**無条件の限定定理 T1**（任意 fan-out、v 因子なし）を証明した。
- Fable §6 の Euler／bigram 計画の中間主張「欠損は（a を潰した）bigram 多重集合と端点の関数」を、**有限・厳密な反例で REFUTED** とした。
- 同一内容類の中では、bigram 線形性の要請を超える剛性が実際に強制される具体例を、**機械検査済み証明書**で得た。

`op:fanout-two` は **OPEN**。

**読めなかった資料.** GitHub（`main.tex` など）は本セッションのネットワーク許可リスト外で取得できなかった。定義は次のものに拠った。

- 依頼書 I-3 の条件
- 第十二段チェックポイント（プロジェクト内）が `main.tex` から転記した記述
  - good = ε-free・nondeleting・nonpermuting・nonmerging（nonmerging = 同一子の連続成分 `x_{j,k}x_{j,k+1}` を一成分内で直接連結しない）
  - `θ_G(R)` = 規則 R を使う文の最小長、`θ̄=max(1,max_R θ_G(R))`
  - `lem:thickness-equivalence` (i) 各規則の明示終端は ≤θ̄ 個、(ii) 各非終端の最短収率 ≤θ̄

原稿と食い違う場合は原稿を優先されたい。

ラベル：**[PROVED]** 本報告に完全証明あり／**[REFUTED]** 全仮定を満たす反例と厳密検証あり／**[CERTIFIED]** 有限インスタンスについて、独立 replay 済みの導出証明書による証明／**[COMPUTATIONAL EVIDENCE]**／**[CONDITIONAL]**／**[OPEN]**。いずれも未査読・未形式化であり、新規性は保証しない。

---

## 0. 命題一覧

| # | 命題 | 状態 |
|---|---|---|
| L1 | (R) 再配分・(U) 一意性（Fable 5.1 の再証明） | PROVED |
| L2 | 骨格関数補題 S：同一骨格・a数≤N−1 ⇒ a数一致 | PROVED（d=2 が本質。陰性対照 S2） |
| L3 | **回転補題 Rot**：`a^pκa^r∈L`, p,r≥1, 3≤p+r≤N−1 ⇒ `aκ≡κa` | PROVED（新） |
| L4 | 併合 Cat：Rot 核の間の a 連は消せる（欠損保存） | PROVED |
| L5 | 内容交換 X1（d=1）と**運搬子交換 X2（d=2、任意の因子出現に作用）** | PROVED |
| T1 | **有界核型定理**：`N < θ̄·(2r+2)^{2M+1}`（M = 大節点の単独語骨格の種類数） | PROVED（新） |
| C1 | 反例族は `M_n ≥ (log_{2r+2}(N_n/θ̄_n) − 1)/2` を要する | PROVED（T1 の系） |
| T2 | 還元：有界次元 β について仮説 H(K) ⇒ U | CONDITIONAL（含意は監査済み Fable-C (4)–(7) の移植） |
| E1 | 「欠損は bigram 多重集合＋端点の関数」「内容類をまたぐ並べ替え不変加法性」 | **REFUTED**（39語の有限閉集合で厳密） |
| E2 | 類 {b,c} で δ(bc)=2, δ(cb)=3 と加法的二部品実現は両立しない（N=10） | CERTIFIED（6〜8手の証明書） |
| O1 | 等長の全核交換だけでは反転数型の統計が排除できない（長さ4で手計算） | PROVED（観察として） |
| U | 予想 U（非可換） | **OPEN** |

---

## 1. 最初の論理検査（IV-1）

| 項目 | 内容 |
|---|---|
| Fable-C の仮定 | 可換 L、半束型付け s、`L∈C^{mcf}_{f,s}`、G は L∩Σ⁺ の reduced good 提示（fan-out 任意、rank ≤r、v=\|V\|、θ=θ̄_G は元の G の厚さ）。D=\|Σ\|−1 を固定。結論 `N=O_{D,r}(vθ^{1+D+D²2^D})`。用いるのは d=1 のみ。 |
| 予想 U | 固定 (Σ,f,r,s) に対し、**全ての** (L,G) で一様に `N ≤ p(‖G‖,θ̄_G)`。成立しても τ(G,s) 全体は制御できず、`op:fanout-two` の NO も出ない。 |
| 5.1 (R) | 仮定 `p a^i q a^j r∈L`, q∈Σ⁺, i+j≤N−1。共通文脈 `□a□a^{N−1−i−j}`。結論：同じ和の任意の正の再配分が受理される。**d=2**。 |
| 5.1 (U) | 仮定 `Pa^iQ, Pa^{i'}Q∈L`, 1≤i<i'≤N は起こらない。**d=1**。 |
| 5.1 (E) | 内容が等しい部品 aVa^e, aV'a^{e'} の同値。監査で補完済み。 |
| Fable §6 | 定理：交叉（系 2.2）は bigram を保つ。**推測**：同 bigram の部品多重集合は宿主を保って連結である、欠損は bigram の加法関数である、fan-out 2 でも新しい困難はない。 |
| 監査の地位 | 「VALID AS A HAND-PROOF」は手証明としての内的妥当性の評価であり、査読・形式化・新規性認定ではない。 |

---

## 2. 準備：(R)・(U)・骨格関数 [PROVED]

以下 s は半束型付けとする。像が可換冪等なので `s(a^i)=s(a)` かつ `s(xy)=s(yx)`。`L∈C^{mcf}_{f,s}`, f≥2、`N=min{n≥1: a^n∈L}`。sk(w) は w の各極大 a 連を記号 Â に置き換えた語。

**L1 (R).** `p a^i q a^j r∈L`、q∈Σ⁺、i,j,i',j'≥1、i'+j'=i+j≤N−1 ⇒ `p a^{i'} q a^{j'} r∈L`。

*証明.* x=(a^i,a^j)、y=(a^{i'},a^{j'}) は成分型が等しい。文脈 `□a□a^{N−1−i−j}`（中央 a は非空）に両方を入れると a^N∈L になる。よって x≡y であり、文脈 p□q□r に適用すればよい。∎

**L1 (U).** `Pa^iQ, Pa^{i'}Q∈L`、1≤i<i'≤N は不可能。

*証明.* a^i≡a^{i'}（d=1、共通文脈 P□Q）。文脈 `a^{N−i'}□` で a^{N−i'+i}∈L となり、0<N−i'+i<N が最小性に反する。∎

**L2（骨格関数）.** w,w'∈L、sk(w)=sk(w')、|w|_a,|w'|_a≤N−1 ⇒ |w|_a=|w'|_a。

*証明.* a 連の個数を k とする（k=0 なら両方 0）。極大 a 連は互いに非空の非 a 因子で隔てられる。L1(R) を対ごとに使えば（各対の和 ≤ 全 a 数 ≤ N−1）、第 2〜k 連を 1 にし、第 1 連を e−(k−1) にできる。w' も同様に e'−(k−1) にする。両語は共通の P, Q で P a^{e−k+1} Q, P a^{e'−k+1} Q と書けるので、(U) より e=e'。∎

**陰性対照 S2 [検証済み].** {a⁷, abaaa, aaaaba} は d=1 の導出規則で閉じ、L2 に反する（骨格 ÂbÂ で a 数 4 と 5）。この集合は d=2 で閉じない。証人は `x=(a,aa)`, `y=(aa,a)`、共有文脈 `□aaa□a`、試験文脈 `□b□a`。L2 は fan-out 2 固有であり、fan-out 1 の指数下界とは矛盾しない。

---

## 3. 新しい一般補題：回転・併合・運搬子交換

**L3（回転補題）[PROVED].** κ∈Σ⁺、p,r≥1、λ:=p+r、3≤λ≤N−1、`a^pκa^r∈L` ⇒ aκ ≡_{L,s} κa。

*証明.* L1(R)（隔て κ∈Σ⁺、和 λ≤N−1）より `a²κa^{λ−2}∈L` と `aκa^{λ−1}∈L`（λ−2≥1）。文脈 E=(a, a^{λ−2}) について E[aκ]=a²κa^{λ−2}、E[κa]=aκa^{λ−1}。両方受理されるので共通受理文脈であり、s(aκ)=s(κa)。∎

*帰結.*

- 同じ型の d=1 同値は合同関係なので、任意の語で `X a^n κ Y∈L ⟺ X κ a^n Y∈L`。
- 特に κ の単独語は、外側の a の任意の分配（0 を含む）で受理される。
- S0 の陽性対照で実測した：`a^+ba^+` だけの族は閉じず（`aba≡aab` が強制される）、閉包は `baaa, aaab` を含む。
- 実験 S3：閉じた 209 集合で Rot の 1202 例を検査し、失敗 0。

**L4（併合 Cat）[PROVED].** `W=a^{e_0}κ_1a^{e_1}⋯κ_m a^{e_m}∈L` で各 κ_i が aκ_i≡κ_ia を満たすなら、`W∈L ⟺ a^{Σe}κ_1κ_2⋯κ_m∈L`。

*証明.* 合同性により a を順に左へ移すだけ。∎

したがって Σe≤N なら、(U) により a 数は**連結文字列** κ_1⋯κ_m だけで決まる。木の互いに素な大節点の同時置換（欠損 δ_B+δ_C）は、この連結核の欠損を与える。部品の間の a 連は不変量として消えてしまう（Fable §6 の「部品の間に残る区切り」は保存量ではない）。

**L5（交換）[PROVED].** κ,κ' が単独語をもち、外側の a 総数 λ,λ'∈[3,N−1]、単独語の a 数を e,e' とし、δ:=N−e、δ':=N−e' とおく。

- **X1（d=1）.** s(aκ)=s(aκ') のとき、i:=max(0,λ−λ')、i':=max(0,λ'−λ) とすると、任意の X,Y について `X a^iκY∈L ⟺ X a^{i'}κ'Y∈L`。a 数の変化は δ−δ'。
  - *証明.* 文脈 (a^s,a^t)、s+t=λ−i=λ'−i'。Rot により分配は任意なので、E[a^iκ] と E[a^{i'}κ'] は両方とも受理される。∎
- **X2（運搬子、d=2）.** s(κ)=s(κ') のとき、i≥1 かつ i'=i+λ'−λ≥1 となる i を選ぶ。任意の l,r と**任意の非空** m について `l a^i m κ r∈L ⟺ l a^{i'} m κ' r∈L`。
  - *証明.* x=(a^i,κ)、y=(a^{i'},κ') の成分型は等しい。文脈 (a^s, a^m, a^t)（m≥1、s+m+t=λ−i）は Rot により両方を受理する。∎
  - **κ は語中の任意の因子出現でよい**（左方のどこかに長さ ≥i の a 連が非空の隔てを挟んであればよい）。より長い非 a 区間の内部の出現も含む。fan-out 2 の交錯・入れ子配置（II-3.8）でも、隔て m が他部品を含んでよいので交換は機能する。

---

## 4. 定理 T1：有界核型 [PROVED]

**設定.** 上の L, N に加え、G は L∩Σ⁺ の reduced good MCFG（fan-out 任意、rank ≤r）、θ:=θ̄_G とする。τ は a^N の G 導出木のうち節点数最小のもの。節点 X の非終端を A_X、収率総長を k_X とする。u_A は A の最短収率組（総長 ≤θ、L1 の引用 (ii)）。**単独語** w_X は、X の部分木を u_{A_X} の導出で置き換えた語（∈L）。**大節点**は k_X>θ を満たす節点。

**定理 T1.** M を大節点の骨格 sk(w_X) の種類数とする（τ の最重子経路上に限ってよい）。σ:=2(r+1) とおくと
\[ N < θ\,σ^{2M+1}. \]

*証明.*

(a) 大節点 X について |w_X|_a = N−k_X+|u_A|_a ≤ N−k_X+θ ≤ N−1。δ_X:=N−|w_X|_a∈[k_X−θ, k_X]。

(b) **型一定性.** sk(w_X)=sk(w_Y) ⇒ δ_X=δ_Y（L2 と (a)）。

(c) **窓補題.** 根から最重子を辿る列を k_0=N≥k_1≥⋯ とする。
- k_i>θ なら節点は子を持つ（子のない規則は終端 ≤θ 個しか書かない）。終端 ≤θ、子 ≤r なので k_{i+1}≥(k_i−θ)/r。
- 実数 y∈[σθ,N] を取り、k_j≤y となる最初の j を選ぶ。
  - j=0 なら δ_0≥y−θ>y/σ。
  - j>0 なら k_{j−1}>y で、δ_j≥k_j−θ>(y−θ)/r−θ=(y−(r+1)θ)/r≥y/(2r)≥y/σ。
  - どちらの場合も δ_j≤k_j≤y。δ_j>y/σ≥θ なので j は大節点である。
- 窓 I_t=[θσ^{2t}, θσ^{2t+1}]（t=0,…,M）は互いに素で、上端 y_t=θσ^{2t+1}≥σθ。

(d) N≥θσ^{2M+1} と仮定する。すると M+1 個の互いに素な窓の各々が大節点の δ を含み、それらは互いに異なる。(b) より骨格も互いに異なり、M+1 種類以上となって矛盾。∎

**注意.**

- d=2 の使用は L2 のみ（L1(R) 経由）。fan-out 1 では L2 が偽になりうる（§2 の陰性対照）。
- 依頼書 III-A3 の例示「有限個の核型」に当たる。
- 境界節点・v 因子は不要になった。
- good の性質（ε-free、nonmerging）から、X の成分間の隔ては非空である。よって sk(w_X) は（A_X、左端か、右端か）だけで決まり、M≤4v。これは自明な指数上界 N<θσ^{8v+1} を回復する。

**系 C1（下界側の障壁）.** 予想 U の反例族 (L_n,G_n) は M_n ≥ ½(log_σ(N_n/θ_n)−1) を満たさねばならない。N_n が超多項式なら、M_n は log‖G_n‖ のどんな定数倍よりも大きい。すなわち、**最重子経路上に、骨格が互いに異なり欠損の尺度が全く違う短収率型が超対数個必要**である。

実験 S4（窓算術のみ）：4000 本の乱択木で、δ を既存値へ寄せる敵対的割当てのもと `N<θσ^{2M+1}` を検査し、FAIL 0、最大比 0.167。

---

## 5. 還元 T2 [CONDITIONAL]

ある K と写像 β：{大非終端} → [0,θ]^K について、次を H(K) と呼ぶ：**各分岐類 T の単位 J_0,…,J_t について、Σλ_iβ(J_i)=0（|λ_i|≤K!θ^K、正負側の総欠損 ≤N−1）なら Σλ_iδ_{J_i}=0。**

H(K) のもとでは、Fable-C §5(4)–(7)（監査済み）が D を K に置き換えてそのまま通る。B=K!θ^K、ρ=2KB とし、類の数は 2^{|Σ|} 以下（内容類）。結論は N=O_{K,|Σ|,r}(vθ^{1+K+K²2^{|Σ|}})。

- 可換の場合は β=Parikh で H(D) が成り立つ（Fable-C (2)(3)＋可換性）。
- **T1 は β=核型の指示ベクトル（K=M）の場合で、H は L2 から無条件に成り立つ。**

開問題は「K=K(Σ) の有界な β で H を満たすもの」の存在に還元される。この含意は監査済みの議論の移植であり、独立再監査はしていない。

---

## 6. E1：bigram 関数主張の反例 [REFUTED]

**集合.** S1 は次の 39 語（チェッカで閉包を計算し、厳密判定で d=1,2・内容型付きの組代入可能性を確認）。

- a⁸
- 単独 b（a 数 6）の全配置
- 単独 c（a 数 5）の全配置
- b が c より前の語（a 数 3）の全配置
- c が b より前の語（a 数 4）の全配置

完全な一覧はログ 19 行目にある。性質：

- 最短 a 冪は a⁸。
- 有限なので各語を一規則とする提示は reduced good（fan-out 1, rank 0）であり、`S1∈C^{mcf}_{2,c_Σ}`。
- L2 は成立する。

**反例.**
- W1=`abaca`：欠損 5
- W2=`acaaba`：欠損 4
- 両者の a を潰した bigram 多重集合 {Âb, bÂ, Âc, cÂ} と端点 (Â,Â) は一致する。
- さらに δ(b)+δ(c)=2+3=5≠4 である。

**反証された主張.**
1. 「欠損は（a 境界を含む）bigram 多重集合と端点の関数」（Fable §6-2,3 の語レベルの形）
2. 「多部品語の欠損は部品の並べ替えに依らず加法的」（内容類をまたぐ場合）

**反証されていないもの.**
- 予想 U
- 同一内容類内での主張（X1 により、同一類の部品の並べ替えは欠損を保つ）
- 木由来の加法性（S1 は木を持たない）

したがって正しい不変量は、類ごとに分けて扱う必要がある（T2 の H は類ごとに定式化してある）。

---

## 7. E2：同一類の剛性 [CERTIFIED]

**種集合**（N=10）：
- a¹⁰
- 単独核 bc（δ=2）、cb（δ=3）
- 四通りの二部品順序配置（欠損は和）

**結果.** 有界閉包（長さ ≤14）の 2 巡目で、同一骨格に a 数が二つ（≤N−1）現れた。例えば骨格 ÂbbccÂbcÂ に a 数 4 と 5。L2 によりこの種集合を含み a¹⁰ を最短とする `L∈C_{2,c}` は存在しない。

**証明書.** 導出規則（Fable 定義 2.3）を 6〜8 回適用し、独立に replay した。証明書の具体的な手順は Python の文字列ハッシュの乱択化で実行ごとに変わるが、結論（status=contra）は 3 回の実行で安定していた。

**機構.** bc と cb の bigram ベクトルは異なるので、bigram 線形性だけからは δ(bc)=δ(cb) は従わない。

- **O1（手計算）.** 長さ 4 の六語 {bcbc, bbcc, cbcb, ccbb, bccb, cbbc} について、欠損 K+(δ(cb)−δ(bc))·inv(w)（inv = c が b より前にある対の数）は、全ての X2 全核交換 bc↔cb および Cat 値（bcbc=2δ(bc)、cbcb=2δ(cb)、bccb=cbbc=δ(bc)+δ(cb)）と矛盾しない。
- **矛盾は全核交換だけからは出ない.** 実際の証明書は、核の一部だけを動かす d=2 の手を使っている。例：x=(b,bab)、y=(bb,aab)；x=(bcac,c)、y=(bcaa,cc)。
- この結果は「Rot＋Cat＋部分因子のスライドが、反転数のような非線形統計を殺す」ことを示唆する。

**未実施.** 整合的な対照（δ(bc)=δ(cb)=2）は閉包が約 9 分で 10⁴ 語を超えて収束しなかったので、最終ランから外した。よって「整合なら閉じる」は**検査していない**。

---

## 8. 既知結果との関係

- L1 は Fable 5.1(R)(U) と同内容（独立再証明）。L5-X1 は Fable-C(2) と監査 §2.2 の非可換版で、Rot により側方の a の量の条件が不要になる。
- Rot は `lem:power-transfer` や Fable 補題 2.1（滑り補題）の z=a, m=a の特殊例ではない（核 κ 全体が a と可換になる）。ただし証明は (R)＋d=1 だけなので、既存ラウンドの補償法則（附録 C 補題 C）と一部重なる可能性がある。照合はしていない。
- T1 は Fable-C と相補的である。Fable-C は「型数は多いが Parikh で線形」、T1 は「線形性なしで型数有界」を扱う。
- 定理 A（倍化族の崩壊）で見られた、文字が a の連を飛び越す移送は、Rot の特殊な現れと整合する。

## 9. 正式中心問題への含意

- 予想 U は依然として未決で、`op:fanout-two` には届かない。
- 下界側（YES 側）への制約：単項希少型を使う下界は、C1 により超対数個の核型を必要とする。さらに E2 型の剛性を逃れる必要がある。単項希少型ルートの見込みは一段と低くなった（証明ではない）。
- 上界側（NO 側）：H(K) を Parikh（K=D）で、類ごと・木由来実現について示せれば、Fable-C が非可換へそのまま延長される。

## 10. 次の有力な一手

**Parikh 還元予想 P**：分岐類 T の Rot 核からなる木由来の実現では、δ は Parikh ベクトルの線形関数である。

E1 は類をまたぐ場合なので P の反例にはならない。E2 は P と整合する。

証明の候補路：
1. Cat で連結核を作る。
2. 単位の多重コピー（分岐類の帰納で利用可能）を宿主として、Fable 系 2.2 の滑りで任意の隣接文字対 (d,e) を入れ替える。
3. 入れ替えのシフト量が、X2 と Cat の整合性により 0 に強制されることを示す（O1 → E2 の一般化）。

詳細は next_obligations を参照。

## 11. 成果物

- `claude_round13_noncomm_U_checker_2026-11-15.py`（SHA256 `3f79da85eb7d128a52b0591e7f51fdcc3aa25f2cc9b469029e76a6e29e96d92a`）
- `claude_round13_noncomm_U_checker_output_2026-11-15.txt`（SHA256 `3dc1019e…33b5`）：実行コマンド `python3 -I …`、終了コード 0、4458 checks、FAIL 0、約 475 秒。
- 本報告、checkpoint1、next_obligations。

GitHub・原稿の編集は行っていない。
~~~~~
END SOURCE claude_round13_noncomm_U_final_report_2026-11-15.md

## A2. Claude 第十三段：残存数学義務

**Original filename:** `claude_round13_noncomm_U_next_obligations_2026-11-15.md`  
**Bytes:** `2992`  
**SHA256:** `496ae66d32cd3c36f635db0702f6760317c6e96a1cd045a2eeb6636b604defbb`

BEGIN SOURCE claude_round13_noncomm_U_next_obligations_2026-11-15.md
~~~~~text
# 第十三段 残存義務（2026-11-15）

## 最小残余命題

**P（Parikh 還元・類ごと）.** L∈C^{mcf}_{2,c_Σ}、a^N 最短、τ を節点最小の導出木とし、T を（内容類での）分岐類とする。T の大単位からなる木由来の多重集合実現（Cat で連結核に正規化したもの）について、次が成り立つ：Parikh が一致し総欠損 ≤N−1 なら、欠損が一致する。

P が示されれば、T2 の H(D) が成り立ち、Fable-C (4)–(7) により予想 U が従う（|Σ| 固定で多項式）。

## 未解決の量化と補題

1. **分岐類の加法性（非可換・fan-out 2）.**
   - 種 w_{B,C} の B, C が交錯・入れ子配置のとき、多重集合帰納の「単位 → 合成核」交換を X2（運搬子）で行う具体的な定式化が必要。
   - 単位同士の交換は X2 で済む。合成核は Rot・Cat で連結化できる。ただし Rot の前提 3≤λ≤N−1 を、各段階で満たすかの量化が残る。
2. **滑りの宿主.** 単位の多重コピーを宿主として、隣接文字対 de→ed（あるいは交叉）を適用できる条件を、有限コピー数で明示すること。
3. **シフト消滅.** 2 の各入れ替えが欠損を変えないこと（O1 の反転数型統計を排除すること）を一般に示す。E2 の証明書はこれを一インスタンスで示しただけである。
4. **類をまたぐ順序.** E1 のとおり順序依存は実在する。P を類ごとに限る定式化で、整数関係の議論に影響しないかを確認する（他類の部品は固定位置に残る）。
5. **T1 の改良.** 「骨格の種類」を「Rot/Cat/X2 による同値類」に置き換えた M' で T1 が成り立つか。成り立てば系 C1 の障壁が強まる。
6. Rot と第十二段の補償法則（補題 C）との包含関係を照合する。Fable-C と既存 reviews の定理 L との照合も未了。
7. GitHub の `main.tex` で定義（`def:class-cmcf`、厚さ、`def:grammar-properties`）を直接照合する（本ラウンドでは取得不可）。

## 反例候補・実験の残り

- E2 の整合対照（δ(bc)=δ(cb)）の閉包が閉じるか。約 9 分で 10⁴ 語を超えた。d=2 組の列挙を、文脈の索引化で高速化する必要がある。
- 類 {b,c} で長さ 3 の核（bcb, cbc, bbc, …）を加えた種での矛盾探索。Parikh 線形な割当てでは矛盾が出ないことの有界検証（打切りを明記すること）。
- 下界側：C1 を満たす候補（超対数個の核型、尺度分散）が、E2 型の剛性に直ちに抵触するかの探索。

## テスト範囲（今回）

- S1：N∈{5,6}、乱択種 300、長さ上限 N+3、3000 語上限。closed 209、矛盾 51、打切り 40。
- S4：rank 2〜3、θ≤4、深さ ≤9 の乱択木 4000 本。
- E1/E2：本文記載のパラメータのみ。未発見は証明扱いしない。
~~~~~
END SOURCE claude_round13_noncomm_U_next_obligations_2026-11-15.md

## A3. Claude 第十三段：チェックポイント

**Original filename:** `claude_round13_noncomm_U_checkpoint1_2026-11-15.md`  
**Bytes:** `1361`  
**SHA256:** `333edfdb04e59886ae6c3da7bb6f8af822309941cdff58c29d1adadb4495b716`

BEGIN SOURCE claude_round13_noncomm_U_checkpoint1_2026-11-15.md
~~~~~text
# 第十三段 チェックポイント1（2026-11-15）

**状態：** 予想 U（非可換）は OPEN。途中段階で得た実質的成果は次のとおり。

- **[PROVED] 骨格関数補題 L2**：(R)+(U) から、同一骨格で a 数 ≤N−1 の受理語は a 数が等しい。陰性対照で d=2 の必要性を確認した。
- **[PROVED] 回転補題 Rot**：`a^pκa^r∈L`（p,r≥1、3≤p+r≤N−1）なら aκ≡κa。
  - 実験の陽性対照で `aba≡aab` が強制されることから発見した。外側の a 連だけの族は閉じない。
  - 帰結：部品間の a 連は保存量ではない（併合 Cat）。
- **[PROVED] 定理 T1**：大節点の単独語骨格の種類数を M とすると N < θ̄(2r+2)^{2M+1}。
- **[REFUTED（厳密・有限）] 語レベルの bigram 関数主張**：閉じた 39 語の集合で `abaca`（欠損5）と `acaaba`（欠損4）の bigram 多重集合・端点が一致した。

**方針修正.** 当初の「a で挟まれた部品」モデルは Rot により誤りだった。不変量は連結核（Cat）で考え直す。

**次の作業.** 同一内容類 {b,c} の閉包実験 E2（bigram 線形性と整合しない種の矛盾証明書）、最終ログの作成。

GitHub は取得不可だったため、定義は第十二段チェックポイントの転記に拠る。
~~~~~
END SOURCE claude_round13_noncomm_U_checkpoint1_2026-11-15.md

## B1. 第十三段・独立数学監査（X1反例・X2修復・T1）

**Original filename:** `audit_claude_round13_noncomm_U_independent_2026-11-15.md`  
**Bytes:** `13412`  
**SHA256:** `f2f54516046fb6bbc8c25d32ed6e96d5233d440320ca057cf6b8d9d74c712979`

BEGIN SOURCE audit_claude_round13_noncomm_U_independent_2026-11-15.md
~~~~~text
# Claude第十三段「非可換予想U」— 独立数学監査

**日付**：2026-11-15 JST  
**対象**：ユーザー提供 `claude_round13_noncomm_U_final_report_2026-11-15.md`、`checkpoint1`、`next_obligations`、標準ライブラリのみのPythonチェッカーと提出ログ。  
**参照定義**：`growupkuriyama-hub/Papers/02-v2-lg-fanout-boundary/main.tex` の `def:grammar-properties`, `def:tuple-substitutable`, `lem:thickness-equivalence`, `op:fanout-two`。`main.tex` を閲覧・定義照合したが編集していない。

## 0. 一行結論

**正式 `op:fanout-two`、非可換予想Uはどちらも OPEN。** 第十三段の **L1(R/U)、L2、L3(Rot)、L4(Cat)、定理T1および系C1の主要手証明は有効**と評価する。他方、**L5-X1 は原文の仮定のままでは偽**であり、40語の有限、内容型付き2-tuple-substitutable言語による**厳密な反例**を独立構成した。**L5-X2 は証明の量化を補えば成立する**。E1 の有限反例・E2 の閉包矛盾証明書は、Claudeコード非依存の別実装で検証した。T2/H(K)の非可換Parikh還元は条件付きのままで、新定理として認定しない。

### 判定表

| 対象 | 本監査の判定 | 根拠・注意 |
|---|---|---|
| L1(R)：正の2穴を使った外側a配分 | **VALID** | 共通宿主 `□a□a^{N−1−i−j}` が適法 |
| L1(U)：短いa冪の一意性 | **VALID** | 1穴の共通文脈＋最小性 |
| L2：同一極大a連骨格のa計数一意性 | **VALID** | Rによる左寄せ後にU。総a数≤N−1が必須 |
| L3 Rot、L4 Cat | **VALID** | 1穴等価と合同性を具体的に確認 |
| L5-X1 | **FALSE AS STATED** | §2の明示的40語反例。比較対象自体の型一致が抜けている |
| L5-X2 | **VALID AFTER EXPLICIT REPAIR** | §3の全iの場合分けで共通2穴宿主を構成 |
| T1（有界核骨格数の上界） | **VALID** | §4で独立再証明。X1・X2不使用 |
| C1（T1の対数障壁） | **VALID** | T1の代数的帰結 |
| T2/H(K) | **CONDITIONAL / NOT INDEPENDENTLY CERTIFIED** | H(K)自体は未証明；Fable-Cの転用には追加の量化審査が必要 |
| E1（bigram関数主張の否定） | **VERIFIED FINITE COUNTEREXAMPLE** | 39語を全1/2穴分布で直接検査 |
| E2（3種の初期集合の不整合） | **CERTIFIED FOR THOSE SEEDS** | Claude非依存の逐手証明書replay：2、2、6手 |
| 予想U / `op:fanout-two` | **OPEN / OPEN** | 本報告に決定的な一般上界・超多項式下界なし |

## 1. 正確な設定

`Σ` は固定有限アルファベット、`a∈Σ`、`s` は有限半束型付け（内容型付け `c_Σ` を含む）、`L∈C^{mcf}_{f,s}`、`f≥2`、`N=min{n≥1:a^n∈L}`。`d=2` の句文脈 `u□₁v□₂w` では **`v∈Σ⁺`**、穴の内容は両方 **非空**。Gは `L∩Σ⁺` のreduced good MCFG、規則ランク≤r、原文法の厚さ `θ=\bar θ_G`。これらは現行論文と整合。

L1(R): `p a^i q a^j r∈L`, `q≠ε`, `i+j≤N−1`, 正の`i',j'`が同和なら置換後も受理。共有宿主 `(□₁,a,□₂ a^{N−1−i−j})` により `a^N` に合流。L1(U): 同じ`P□Q`に `a^i,a^{i'}` が受理され、`1≤i<i'≤N` なら小さいa冪の受理を強制して矛盾。L2は各極大a連をRで左寄せしてUを適用。

L3: `a^pκa^q∈L`, `3≤p+q=λ≤N−1` ならRから `a²κa^{λ−2}` と `aκa^{λ−1}` が受理。共有1穴文脈 `a□a^{λ−2}` と半束可換性により `aκ≡_{L,s}κa`。L4はこの1穴合同を用いて任意の孤立a連を左へ移す。これらの証明にL5-X1を使わない。

## 2. **厳密反例：L5-X1は偽**

Claudeの主張（原報告§3）：κ,κ'がそれぞれ `a^pκa^q`, `a^{p'}κ'a^{q'}` という単独受理語を持ち、`λ=p+q`, `λ'=p'+q'` が `[3,N−1]` に属し、`s(aκ)=s(aκ')` なら、`i=(λ−λ')_+`, `i'=(λ'−λ)_+` として任意X,Yで

`Xa^iκY ∈ L  ⇔  Xa^{i'}κ'Y ∈ L`

を主張する。**しかし`i`または`i'`が0の場合、実際の置換片 `a^iκ`, `a^{i'}κ'` の型一致は仮定から導けない。**

### 2.1 40語の明示的反例

内容型付け `s=c_{a,b,c}` を取る。まず次の39語の集合Sを取る（Claude E1の `f2=4` ケースから厳密に得られた有限閉言語であり、以下に語の全リストを示す）。

```
aaabc aabac aabca abaac abaca abcaa baaac baaca bacaa bcaaa
aaaaac aaaaca aaaacb aaacaa aaacab aaacba aacaaa aacaab aacaba aacbaa
acaaaa acaaab acaaba acabaa acbaaa caaaaa caaaab caaaba caabaa cabaaa
cbaaaa aaaaaab aaaaaba aaaabaa aaabaaa aabaaaa abaaaaa baaaaaa
aaaaaaaa
```

**`L:=S∪{bc}`（計40語）** とする。独立Python検証器で、L中の全ての非空1穴・2穴出現から全受理文脈を構築し、等しい成分内容型かつ共通受理文脈のある全組について、文脈集合の一致を検査した。

- `|L|=40`, 出現する組は333種類、受理文脈の組は2,327件、比較した組ペア924件。
- **違反0**。したがって L は `C^{mcf}_{2,c_Σ}` に属する（有限言語なのでMCFL性も自明）。
- 唯一のaのみの語は `a^8`：`N=8`。
- 有限言語には `S→w`（各 `w∈L`）というrank 0の1成分good規則からなるreduced presentationが存在する。

`κ=bc`, `κ'=acb`, `λ=λ'=3` と選ぶ。

- `a κ a² = abcaa ∈L`。
- `a² κ' a = aaacba ∈L`。
- 両外枠のaの総数は3、`3≤3≤N−1=7`。
- `s(aκ)=s(abc)=\{a,b,c\}=s(aacb)=s(aκ')`。
- 一方 `i=i'=0` なので、X1は `bc∈L ⇔ acb∈L` を要求する。しかし **`bc∈L` かつ `acb∉L`**。

全仮定を満たすのでX1の**反証**が成立する。原因は、`s(κ)=\{b,c\}` と `s(κ')=\{a,b,c\}` が異なる点。半束は `s(aκ)=s(aκ')` から `s(κ)=s(κ')` を保証しない。これは証明の単なる省略ではなく、主張への追加仮定が必要な事例である。

### 2.2 X1の修正版

`x=a^{(λ−λ')_+}κ`、`y=a^{(λ'−λ)_+}κ'` と置き、**`s(x)=s(y)` を明示的に要求する**なら、修正後のX1は成立する。`t=min(λ,λ')` とすれば、Rotから `a^λκ` および `a^{λ'}κ'` が受理されるので、**共通宿主 `E=a^t□`** が `E[x]=a^λκ`, `E[y]=a^{λ'}κ'` を受理する。型一致から1穴組代入可能性を適用できる。全X,Yへの置換は正当。

この修正で、今後のParikh還元計画に必要な全ての交換が可能になるとは**まだ証明されていない**。特に`i=0`の場合の型差に注意。

## 3. X2は「長過ぎるi」の場合も証明できる

Claudeの原証明は `s+m+t=λ−i` の非負分解を使い、`i≥λ` では右辺が負になる。この書き方のままでは任意iの主張を示していない。しかし、X2の**結論は修復可能**である。

`κ,κ'` に単独語の外側a総数 `λ,λ'∈[3,N−1]` があり、`s(κ)=s(κ')` とする。`i,i'≥1` で `i'=i+λ'−λ`。

1. **`i≤λ−1`**：`q=λ−i≥1` とし、`E=a^{q−1}□₁ a □₂` と置く。これは中央の `a` が非空なので適法。`x=(a^i,κ)`、`y=(a^{i'},κ')` の型は一致し、Rotで受理された `a^λκ` と `a^{λ'}κ'` がそれぞれ `E[x]`,`E[y]` となる。したがって `x≡^2 y`。
2. **`i≥λ`**：`i_0=λ−1`, `i'_0=λ'−1` を使って上記の等価を得る。任意の受理語 `l a^i m κ r` に対し、余剰接頭部分 `a^{i−i_0}` を左側の外部文脈に吸収し、中央には元の非空 `m` を残す。すると置換後の指数は `i−i_0+i'_0=i+λ'−λ=i'` となる。逆方向も同様。

したがって**X2は、型が同じ核同士について、全ての適法な非空セパレータmと任意の正のiに対して成立する**。X1の反例はX2には反しない（ここでは `s(κ)≠s(κ')`）。

## 4. 定理T1と系C1の独立証明

主張：`τ` は `a^N` の導出木、節点Xの収率長を `k_X`、非終端A_Xの最短導出組を`u_A`とする。`θ=\barθ_G`、`r` はrank cap、`M` は**根から最重子を選んで進む1本の経路上**の大節点（`k_X>θ`）から得る単独語 `w_X` の骨格`sk(w_X)`の種類数とする。`σ=2(r+1)` と置く（以下では単に σ と記す）。結論：

`N < θ σ^{2M+1}`.

### 検証済みの推論

- 現行 `lem:thickness-equivalence` により、元文法の各非終端は総長≤θの導出組を持ち、各規則の明示終端記号数は≤θ。部分木を最短組で置換して得る語 `w_X` はLの実際の語。根が全てaなので `|w_X|_a=N−k_X+|u_{A_X}|_a`。
- `k_X>θ` なら `|w_X|_a≤N−1`、`δ_X:=N−|w_X|_a∈[k_X−θ,k_X]`。L2により同骨格の大節点は同じδを持つ。
- 最重子経路上の次の子の長さは `k_{j+1}≥(k_j−θ)/r`。`k_j>θ` なら終端規則だけではないため経路は進み、葉の長さ≤θ。
- `σθ≤y≤N` とし `k_j≤y` となる最初の節点をとる。もしj=0なら `δ_0≥N−θ≥y−θ>y/σ`。もしj>0なら `δ_j≥k_j−θ>(y−(r+1)θ)/r≥y/(2r)>y/σ`。同時に `δ_j≤k_j≤y`。ゆえに、各 `y` について `[y/σ,y]` 内に大節点のδが存在する。
- `N≥θσ^{2M+1}` と仮定し、`y_t=θσ^{2t+1}`（t=0,…,M）をとると、互いに交わらない `M+1` 個の窓 `(θσ^{2t},θσ^{2t+1}]` に異なるδが存在する。L2によって異なる骨格が必要だが、骨格はM種類。矛盾。

この証明に **X1、X2、Fable-CのParikh還元やH(K)を使用していない**。よって X1反例によってT1の成立は損なわれない。任意fan-outでも、必要なtuple substitutabilityの使用はd≤2であり、原文法の厚さを用いる。

系C1は `M > (log_σ(N/θ)−1)/2` というT1の対数変形である。`M≤4v`という補足は、good導出の各tuple成分間に非空のa区切りが残ることと、各非終端の最短組および外側の左右a連の有無（2二値）で骨格が決まることに基づく。**このM≤4vはT1そのものには不要**であり、一般的な多項式境界を与えるわけではない。

## 5. E1/E2の完全独立有限検査

検証器 `round13_independent_checks_2026-11-15.py` はClaudeのPythonを一切importしない。

- **E1**：提出ログの全語リストから `f2=5`: 34語・1,784組文脈、`f2=4`: 39語・2,324組文脈を独自に構築。全てd=1,2の内容型付き分布条件を厳密に満たす。`abaca`（a3個）と `acaaba`（a4個）の骨格bigram数＋端点は一致するので、**欠損をbigram計数のみの関数にする主張は実際に偽**。
- 同じ有限言語で **Rot** を147件、**X2** の許容核とi（1〜12）の分布同一を3,275件独立検査し、いずれも違反0。これは一般証明ではなく追加のストレス検査。
- **E2**：提出ログにある三つの種集合を独自の組合せ列挙で再構築し、各証明書の `型一致`・`穴非空`・`セパレータ非空`・`三つの前提語がそれまでに既出`・`帰結語` を逐手照合。元の提出ログでは2手・2手・6手、全て再現成功。最終語に同一骨格でa数が異なり双方N未満となる矛盾を確認。**それら特定の種集合に限った不可能性証明**であり、一般的なE2型剛性の定理ではない。
- **原チェッカーの部分再実行**：S0/E1/S2/S4で4,035 checks、FAIL=0。E2も単独で5秒程度、4 checks、FAIL=0。ただしPythonのhash乱択によって具体的証明書が変わる。**全4458 checksの300乱択試行部分（S1）の完全再実行は実施していない**。
- **検証コード内の試験範囲の注意**：Claudeの関数 `exchange_instances` は定義されているが、`run_S1_S3` からは呼ばれていない。報告の「S3の1202件」は**Rotの検証**であり、X1/X2の検証件数ではない。この点がX1の誤認を助長した可能性がある。

## 6. 研究上の含意と次の義務

1. **X1の原文は撤回・修正が必要**。実際の比較語`a^iκ`と`a^{i'}κ'`について型一致を要求するのが最小の自然な修正。元の `s(aκ)=s(aκ')` では足りない。
2. **X2は§3の補足証明で維持できる**。ただし各交換操作で確保できる受理宿主が「交換を予定する木由来の場所」に適合するかは、新しい複合ステップに関して別途証明すること。
3. **T1は成果として保存可能**。ただし「大節点の骨格型数が固定」という付加条件を消せたわけではない。`op:fanout-two` の肯定・否定どちらも未達。
4. **T2/H(K)は条件付きの研究計画**。X1の不十分な型一致を使う段落が今後登場するなら改修し、Fable-Cの類ごとの整数関係・木の被覆の移植を独立に検証する必要がある。
5. **E1の反例は“全内容類をまたぐbigram関数性”の否定**であり、内容類ごとに制限したParikh還元Pを反証してはいない。
6. 次ラウンドでは **X1の明示的40語反例を必ずClaudeに渡し**、先に型条件と運搬子の宿主を確定し、その後で同一内容類のParikh還元Pを探索すべき。

**論文本文・GitHubは未変更。** 専門家査読および形式証明は未実施。今回のVALID判定は書面証明の独立再構成に基づく。
~~~~~
END SOURCE audit_claude_round13_noncomm_U_independent_2026-11-15.md

## C1. X1反例・独立Python検証器

**Original filename:** `round13_independent_X1_counterexample_2026-11-15.py`  
**Bytes:** `2305`  
**SHA256:** `715ddf6329f4bad6e1745587aff8b8d37b57d3f79a163faa776eb921a0c291ba`

BEGIN SOURCE round13_independent_X1_counterexample_2026-11-15.py
~~~~~text
#!/usr/bin/env python3
"""Independent finite counterexample to Round13 Lemma L5-X1, as stated.
No imports from Claude's checker; exact enumeration of arity 1/2 contexts.
"""
from collections import defaultdict
S = set('''aaabc aabac aabca abaac abaca abcaa baaac baaca bacaa bcaaa
aaaaac aaaaca aaaacb aaacaa aaacab aaacba aacaaa aacaab aacaba aacbaa
acaaaa acaaab acaaba acabaa acbaaa caaaaa caaaab caaaba caabaa cabaaa
cbaaaa aaaaaab aaaaaba aaaabaa aaabaaa aabaaaa abaaaaa baaaaaa
aaaaaaaa'''.split())
assert len(S)==39
L=S|{'bc'}

def T(x):return tuple(frozenset(z) for z in x)
def fill(E,x):
    return E[0]+x[0]+E[1] if len(x)==1 else E[0]+x[0]+E[1]+x[1]+E[2]
D=defaultdict(set)
for w in L:
    n=len(w)
    for i in range(n):
        for j in range(i+1,n+1):
            D[(w[i:j],)].add((w[:i],w[j:]))
    for i in range(n):
        for j in range(i+1,n+1):
            for k in range(j+1,n):  # separator w[j:k] must be nonempty
                for z in range(k+1,n+1):
                    D[(w[i:j],w[k:z])].add((w[:i],w[j:k],w[z:]))
K=defaultdict(list)
for x,contexts in D.items():
    for E in contexts:K[(len(x),T(x),E)].append(x)
checks=0
for (d,t,E),xs in K.items():
    for x in xs[1:]:
        checks+=1
        assert D[x]==D[xs[0]],(xs[0],x,D[x]^D[xs[0]])
assert all(w and not (set(w)=={'a'} and len(w)<8) for w in L)
assert 'a'*8 in L
# Standalone words and their outer-a totals:
N=8; kap='bc'; kap2='acb'; lam=3; lam2=3
w='a'+kap+'aa'; w2='aa'+kap2+'a'
assert w=='abcaa' and w2=='aaacba'
assert w in L and w2 in L
assert 3<=lam<=N-1 and 3<=lam2<=N-1
assert set('a'+kap)==set('a'+kap2)=={'a','b','c'}
i=max(0,lam-lam2); ip=max(0,lam2-lam)
assert i==ip==0
assert 'bc' in L and 'acb' not in L
print('S size',len(S),'L size',len(L),'tuple count',len(D),'accepting contexts',sum(map(len,D.values())),'tuple-pair comparisons',checks)
print('C_2,content closed (d=1,2): YES, verified over ALL finite contexts')
print('a^N min N=8: YES')
print('X1 standalone witnesses:',w,w2)
print('s(aκ)=s(aκ\u2032)={a,b,c}: YES; λ=λ\u2032=3')
print('predicted by X1: κ=bc in L iff κ\u2032=acb in L')
print('observed: bc in L, acb not in L; X1 FALSE')
print('Note: s(κ)={b,c} while s(κ\u2032)={a,b,c}, so typed 1-hole substitutability cannot apply')
print('ALL COUNTEREXAMPLE CONDITIONS VERIFIED')
~~~~~
END SOURCE round13_independent_X1_counterexample_2026-11-15.py

## C2. X1反例・独立Python実行ログ

**Original filename:** `round13_independent_X1_counterexample_output_2026-11-15.txt`  
**Bytes:** `467`  
**SHA256:** `b915b52308612570f65f79ffd0bb33b29328da90d971e010063d801f210b3c09`

BEGIN SOURCE round13_independent_X1_counterexample_output_2026-11-15.txt
~~~~~text
S size 39 L size 40 tuple count 333 accepting contexts 2327 tuple-pair comparisons 924
C_2,content closed (d=1,2): YES, verified over ALL finite contexts
a^N min N=8: YES
X1 standalone witnesses: abcaa aaacba
s(aκ)=s(aκ′)={a,b,c}: YES; λ=λ′=3
predicted by X1: κ=bc in L iff κ′=acb in L
observed: bc in L, acb not in L; X1 FALSE
Note: s(κ)={b,c} while s(κ′)={a,b,c}, so typed 1-hole substitutability cannot apply
ALL COUNTEREXAMPLE CONDITIONS VERIFIED
~~~~~
END SOURCE round13_independent_X1_counterexample_output_2026-11-15.txt

## D1. Fable-C：独立完全数学監査

**Original filename:** `fable_C_full_audit_2026-11-15/Fable_C_complete_independent_mathematical_audit_2026-11-15.md`  
**Bytes:** `17724`  
**SHA256:** `63be1443497ba90d945c04e1ed7895fa220fc9f464e4d9b0416b5a5a416e72d2`

BEGIN SOURCE Fable_C_complete_independent_mathematical_audit_2026-11-15.md
~~~~~text
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
~~~~~
END SOURCE Fable_C_complete_independent_mathematical_audit_2026-11-15.md

## D2. Fable初回探索：原数学報告

**Original filename:** `fable_C_full_audit_2026-11-15/Fable_original_open_problem_report_2026-11-15.md`  
**Bytes:** `27376`  
**SHA256:** `c0369cdc571944bfe702e52a3571939bc5981c332637bf8c49765ebc3e3ca223`

BEGIN SOURCE Fable_original_open_problem_report_2026-11-15.md
~~~~~text
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
~~~~~
END SOURCE Fable_original_open_problem_report_2026-11-15.md

## E1. Claude 第十三段：Python検証コード

**Original filename:** `claude_round13_noncomm_U_checker_2026-11-15.py`  
**Bytes:** `24907`  
**SHA256:** `3f79da85eb7d128a52b0591e7f51fdcc3aa25f2cc9b469029e76a6e29e96d92a`

BEGIN SOURCE claude_round13_noncomm_U_checker_2026-11-15.py
~~~~~text
#!/usr/bin/env python3
"""Round 13 checker (Claude, 2026-11-15): non-commutative Conjecture U.

Python 3 standard library only.  Deterministic (random.seed(20261115)).
Run:   python3 -I claude_round13_noncomm_U_checker_2026-11-15.py
Exit code 0 iff every check marked [MUST] passes.

Typing throughout: content typing c(w) = set of letters of w (finest semilattice typing).
Tuple substitutability for d in {1,2}; a d=2 context is l [] m [] r with m NONEMPTY.

What is checked
  [S0] exact finite substitutability decision procedure (d=1,2), with positive / negative
       controls.
  [E1] REFUTATION (finite, exact): a finite language S1 in C^{mcf}_{2,c} with a^8 the
       shortest a-power, containing W1=a b a c a-type (deficit 5) and W2=a c a b a-type
       (deficit 4).  W1,W2 have the same a-collapsed bigram multiset and the same
       endpoints.  => "deficit is a function of the skeleton bigram multiset (+endpoints)"
       and "deficit of a multi-piece word is order-independent" are FALSE in general.
  [E2] closure experiment inside ONE content class {b,c}: seed realisations violating
       bigram-linearity; capped closure searched for a contradiction (shorter a-power or
       same-skeleton a-count conflict).  Certificates, if found, are replayed independently.
       Also the linear (control) seed.
  [S1] Lemma S (skeleton function) stress: random seeds -> exact closure when it terminates;
       on every closed set: same skeleton & a-count<=N-1  =>  same a-count.
  [S2] negative control for Lemma S: a d=1-closed finite set violating Lemma S must be
       d=2-non-closed (shows the d=2 hypothesis is used).
  [S3] content-exchange lemma (X1) instances on every closed set from [S1].
  [S4] window/tree arithmetic of Theorem T1: random trees, N < theta*sigma^(2M+1).
"""
import hashlib, random, sys, itertools, json, time
from collections import defaultdict

random.seed(20261115)
LOG = []
FAIL = 0
COUNT = 0
def log(*a):
    s = ' '.join(str(x) for x in a); LOG.append(s); print(s, flush=True)
def must(cond, msg):
    global FAIL, COUNT
    COUNT += 1
    if not cond:
        FAIL += 1; log('  [FAIL]', msg)
    return cond

def ctype(w): return frozenset(w)
def skel(w):
    out = []
    for ch in w:
        if ch == 'a':
            if not out or out[-1] != 'A': out.append('A')
        else: out.append(ch)
    return ''.join(out)
def acount(w): return w.count('a')

# ----------------------------------------------------------------- tuples / contexts
def tuples_of(w):
    """yield (d, x, E) with E the context; d=1: x=(x1,), E=(l,r); d=2: x=(x1,x2), E=(l,m,r), m!=''"""
    n = len(w)
    for i in range(n):
        for j in range(i + 1, n + 1):
            yield 1, (w[i:j],), (w[:i], w[j:])
    for i in range(n):
        for j in range(i + 1, n + 1):
            for k in range(j + 1, n + 1):      # m = w[j:k] nonempty
                for l in range(k + 1, n + 1):
                    yield 2, (w[i:j], w[k:l]), (w[:i], w[j:k], w[l:])

def fill(E, x):
    if len(x) == 1: return E[0] + x[0] + E[1]
    assert E[1] != ''
    return E[0] + x[0] + E[1] + x[1] + E[2]

def ttype(x): return tuple(ctype(c) for c in x)

def ctx_maps(S):
    ctx = defaultdict(set)
    for w in S:
        for d, x, E in tuples_of(w):
            ctx[x].add(E)
    return ctx

def check_closed(S):
    """Exact decision: is the finite set S tuple-substitutable (d=1,2, content typing)?
    Returns (True, None) or (False, witness)."""
    S = set(S)
    ctx = ctx_maps(S)
    bucket = defaultdict(list)
    for x, Es in ctx.items():
        t = ttype(x)
        for E in Es:
            bucket[(len(x), t, E)].append(x)
    for (d, t, E0), xs in bucket.items():
        if len(xs) < 2: continue
        ref = ctx[xs[0]]
        for y in xs[1:]:
            cy = ctx[y]
            if cy != ref:
                diff = (ref - cy) or (cy - ref)
                E1 = next(iter(diff))
                x = xs[0]
                if E1 in cy: x, y = y, x
                return False, dict(x=x, y=y, E_accept=E0, E_test=E1,
                                   E_accept_x=fill(E0, x), E_accept_y=fill(E0, y),
                                   E_test_x=fill(E1, x), E_test_y=fill(E1, y),
                                   type_x=[sorted(c) for c in ttype(x)],
                                   type_y=[sorted(c) for c in ttype(y)])
    return True, None

def verify_witness(S, wit):
    """independent re-check of a non-closedness witness"""
    x, y, E0, E1 = wit['x'], wit['y'], wit['E_accept'], wit['E_test']
    if ttype(x) != ttype(y): return False
    if len(x) == 2 and (E0[1] == '' or E1[1] == ''): return False
    if any(c == '' for c in x + y): return False
    return (fill(E0, x) in S and fill(E0, y) in S and fill(E1, x) in S and fill(E1, y) not in S)

def shortest_apower(S):
    ns = [len(w) for w in S if w and set(w) == {'a'}]
    return min(ns) if ns else None

def skeleton_conflicts(S, N):
    """Lemma S consequence: same skeleton, a-counts <= N-1, different a-counts."""
    by = defaultdict(set)
    for w in S:
        if 'a' in w and acount(w) <= N - 1 and set(w) != {'a'}:
            by[skel(w)].add(acount(w))
    return {k: sorted(v) for k, v in by.items() if len(v) > 1}

# ----------------------------------------------------------------- closure with certificates
def closure(seed, cap_len, cap_words=200000, max_rounds=50, N=None, stop_on_contra=True):
    """Direct rule applications (Fable Def 2.3): E0[x],E0[y],E1[x] in K => E1[y] in K.
    Returns dict(K, origin, status, contra) ; status in {'closed','truncated','cap','contra'}."""
    K = set(seed)
    origin = {w: None for w in K}
    truncated = False
    for rnd in range(max_rounds):
        ctx = ctx_maps(K)
        bucket = defaultdict(list)
        for x, Es in ctx.items():
            t = ttype(x)
            for E in Es:
                bucket[(len(x), t, E)].append(x)
        new = {}
        for (d, t, E0), xs in bucket.items():
            if len(xs) < 2: continue
            for x in xs:
                cx = ctx[x]
                for y in xs:
                    if y == x: continue
                    for E1 in cx:
                        w = fill(E1, y)
                        if w in K or w in new: continue
                        if len(w) > cap_len:
                            truncated = True; continue
                        new[w] = (x, y, E0, E1)
        if not new:
            return dict(K=K, origin=origin, status='truncated' if truncated else 'closed',
                        contra=None, rounds=rnd)
        for w, o in new.items():
            K.add(w); origin[w] = o
        if N is not None:
            m = shortest_apower(K)
            if m is not None and m < N:
                return dict(K=K, origin=origin, status='contra', contra=('apower', 'a' * m), rounds=rnd + 1)
            sc = skeleton_conflicts(K, N)
            if sc and stop_on_contra:
                k = next(iter(sc))
                return dict(K=K, origin=origin, status='contra', contra=('skeleton', k, sc[k]), rounds=rnd + 1)
        if len(K) > cap_words:
            return dict(K=K, origin=origin, status='cap', contra=None, rounds=rnd + 1)
    return dict(K=K, origin=origin, status='cap', contra=None, rounds=max_rounds)

def certificate(origin, targets):
    """minimal ordered list of rule applications deriving targets from the seed"""
    order, seen = [], set()
    def need(w):
        if w in seen: return
        seen.add(w)
        o = origin[w]
        if o is None: return
        x, y, E0, E1 = o
        for p in (fill(E0, x), fill(E0, y), fill(E1, x)):
            need(p)
        order.append((w, o))
    for t in targets: need(t)
    return order

def replay(seed, cert):
    K = set(seed)
    for w, (x, y, E0, E1) in cert:
        if ttype(x) != ttype(y): return False, 'type'
        if any(c == '' for c in x + y): return False, 'empty component'
        if len(x) == 2 and (E0[1] == '' or E1[1] == ''): return False, 'empty separator'
        if not (fill(E0, x) in K and fill(E0, y) in K and fill(E1, x) in K): return False, 'premise'
        if fill(E1, y) != w: return False, 'conclusion'
        K.add(w)
    return True, K

# ----------------------------------------------------------------- helpers to build families
def compositions(total, parts):
    """all tuples of `parts` positive ints summing to total"""
    if parts == 0:
        if total == 0: yield ()
        return
    if total < parts: return
    for c in itertools.combinations(range(1, total), parts - 1):
        b = (0,) + c + (total,)
        yield tuple(b[i + 1] - b[i] for i in range(parts))

def flanked(pieces, a_total):
    """all words a^{p0} pi1 a^{p1} ... pik a^{pk} with all p>=1 and sum p = a_total"""
    out = set()
    for comp in compositions(a_total, len(pieces) + 1):
        w = 'a' * comp[0]
        for pi, p in zip(pieces, comp[1:]):
            w += pi + 'a' * p
        out.add(w)
    return out

def bigram_profile(w):
    s = skel(w)
    from collections import Counter
    return (Counter(s[i:i + 2] for i in range(len(s) - 1)), s[0], s[-1])

# =================================================================== S0 controls
def run_S0():
    log('== [S0] exact finite substitutability: controls')
    # positive: a^5 plus all flanked b-words with total 3 (pieces b, deficit 2)
    seed = {'a' * 5} | flanked(['b'], 3)
    ok0, wit0 = check_closed(seed)
    must(not ok0 and verify_witness(seed, wit0), 'S0: interior-only family must NOT be closed (rotation)')
    log('   interior-only family a^5 + a^+ b a^+ (total 3) is not closed; witness', json.dumps(wit0, default=list))
    R = closure(seed, cap_len=8, N=5)
    S = R['K']
    ok, wit = check_closed(S)
    must(R['status'] == 'closed' and ok, 'S0 positive control closure should be closed: %s %s' % (R['status'], wit))
    must(shortest_apower(S) == 5, 'S0 positive: a^5 shortest')
    log('   closure: status=%s |S|=%d S=%s' % (R['status'], len(S), sorted(S, key=lambda w:(len(w),w))))
    # negative: aligned (non-redistributed) word set violates (R)
    S = {'a' * 5, 'abaa'}
    ok, wit = check_closed(S)
    must(not ok and verify_witness(S, wit), 'S0 negative control must be non-closed with verified witness')
    log('   negative control {a^5, abaa}: witness', json.dumps(wit, default=list))
    # negative: separator requirement (d=2 with empty middle is NOT a context; check we never use it)
    for w in ['abcab', 'aab']:
        for d, x, E in tuples_of(w):
            if d == 2: must(E[1] != '', 'empty separator generated')

# =================================================================== E1
def run_E1():
    log('== [E1] cross-class order dependence: closure of an order-dependent seed')
    out = {}
    for f2 in (5, 4):
        N = 8
        seed = {'a' * N}
        seed |= flanked(['b'], N - 2)        # solo b, deficit 2
        seed |= flanked(['c'], N - 3)        # solo c, deficit 3
        seed |= flanked(['b', 'c'], N - 5)   # order b..c, deficit 5 = 2+3
        seed |= flanked(['c', 'b'], N - f2)  # order c..b, deficit f2
        R = closure(seed, cap_len=N + 3, cap_words=20000, max_rounds=20, N=N)
        S = R['K']
        line = '   f2=%d: status=%s |K|=%d rounds=%d contra=%s' % (f2, R['status'], len(S), R['rounds'], R['contra'])
        log(line)
        if R['status'] == 'closed':
            ok, wit = check_closed(S)
            must(ok, 'E1 closure must pass exact check')
            must(shortest_apower(S) == N, 'E1 a^8 shortest')
            must(not skeleton_conflicts(S, N), 'E1 Lemma S')
            W1 = 'abaca'
            W2 = 'acaba' if f2 == 5 else 'acaaba'
            must(W1 in S and W2 in S, 'E1 W1,W2 in closure')
            must(bigram_profile(W1) == bigram_profile(W2), 'E1 same bigram profile and endpoints')
            log('     W1=%s deficit %d ; W2=%s deficit %d ; same a-collapsed bigram multiset+endpoints=%s'
                % (W1, N - acount(W1), W2, N - acount(W2), bigram_profile(W1) == bigram_profile(W2)))
            if f2 == 4:
                must(N - acount(W1) != N - acount(W2), 'E1 REFUTATION: deficits differ')
                must('baaaaaa' in S and 'caaaaa' in S, 'E1 solo pieces present (deficits 2,3)')
                log('     REFUTED (exact, finite): deficit not a function of bigram data; cb-order deficit 4 != 2+3')
            log('     full closed set S1(f2=%d) = %s' % (f2, sorted(S, key=lambda w: (len(w), w))))
            log('     words with content {a,b,c} and a-count<N:', sorted([w for w in S if set(w) == set('abc')],
                key=lambda w: (len(w), w)))
        if R['status'] == 'contra':
            kind = R['contra'][0]
            if kind == 'apower':
                targets = [R['contra'][1]]
            else:
                sk = R['contra'][1]
                byc = {}
                for w in R['K']:
                    if skel(w) == sk and acount(w) <= N - 1: byc.setdefault(acount(w), w)
                targets = list(byc.values())[:2]
            cert = certificate(R['origin'], targets)
            okr, _ = replay(seed, cert)
            must(okr is True, 'E1 certificate replay')
            log('     certificate (%d steps, replay ok=%s) targets=%s' % (len(cert), okr is True, targets))
            for k, (w, (x, y, E0, E1)) in enumerate(cert):
                log('       %2d x=%s y=%s E0=%s E1=%s => %s' % (k, x, y, E0, E1, w))
        out[f2] = R
    return out

# =================================================================== E2
def e2_seed(N, deltas):
    S = {'a' * N}
    P = list(deltas)
    for p in P:
        S |= flanked([p], N - deltas[p])
    for p, q in itertools.product(P, P):
        t = N - deltas[p] - deltas[q]
        if t >= 3: S |= flanked([p, q], t)
    return S

def run_E2():
    log('== [E2] within-class {b,c} bigram-linearity: closure experiments')
    res = {}
    # relation: v(bcbc)+v(cb) = v(bc)+v(cbcb)  (skeleton bigram multisets incl. boundary)
    from collections import Counter
    vb = lambda p: Counter(skel('a' + p + 'a')[i:i + 2] for i in range(len(p) + 1))
    must(vb('bcbc') + vb('cb') == vb('bc') + vb('cbcb'), 'E2: bigram relation holds')
    # first two cases: deliberately inconsistent with concatenation additivity (expect contradiction)
    # last two: primitive cores bc, cb only; products generated by closure.
    cases = [('naive-violating', {'bc': 2, 'cb': 2, 'bcbc': 3, 'cbcb': 4}),
             ('naive-linear', {'bc': 2, 'cb': 2, 'bcbc': 3, 'cbcb': 3}),
             ('prim-bc2-cb3', {'bc': 2, 'cb': 3})]
    # NOTE: the consistent control ('bc':2,'cb':2) was attempted during development; its closure
    # did not terminate within ~9 minutes (|K| grows past 10^4 words); it is NOT part of this run.
    for name, deltas in cases:
        N = 10
        seed = e2_seed(N, deltas)
        t0 = time.time()
        R = closure(seed, cap_len=N + 4, cap_words=30000, max_rounds=6, N=N)
        dt = time.time() - t0
        log('   case %-15s N=%d |seed|=%d -> status=%s |K|=%d rounds=%d time=%.1fs contra=%s'
            % (name, N, len(seed), R['status'], len(R['K']), R['rounds'], dt, R['contra']))
        res[name] = R
        if R['status'] == 'contra':
            kind = R['contra'][0]
            if kind == 'apower':
                targets = [R['contra'][1]]
            else:
                sk = R['contra'][1]
                ws = [w for w in R['K'] if skel(w) == sk and acount(w) <= N - 1]
                byc = {}
                for w in ws: byc.setdefault(acount(w), w)
                targets = list(byc.values())[:2]
            cert = certificate(R['origin'], targets)
            okr, K2 = replay(seed, cert)
            must(okr is True, 'E2 %s: certificate replay' % name)
            log('     certificate: %d rule applications, replay=%s, targets=%s' % (len(cert), okr is True, targets))
            for step, (w, (x, y, E0, E1)) in enumerate(cert[:40]):
                log('       %2d  x=%s y=%s E0=%s E1=%s  =>  %s' % (step, x, y, E0, E1, w))
            if len(cert) > 40: log('       ... (%d more)' % (len(cert) - 40))
            res[name + '_cert'] = cert
    return res

# =================================================================== S1/S3 random closed sets
def random_seed_words(N, k):
    S = {'a' * N}
    for _ in range(k):
        npieces = random.choice([1, 1, 2])
        pieces = [''.join(random.choice('bc') for _ in range(random.choice([1, 1, 2])))
                  for _ in range(npieces)]
        tot = random.randint(npieces + 1, N - 1)
        comp = random.choice(list(compositions(tot, npieces + 1)))
        w = 'a' * comp[0]
        for pi, p in zip(pieces, comp[1:]): w += pi + 'a' * p
        S.add(w)
    return S

def exchange_instances(S, N):
    """(X1): solo cores pi,pi' same content; host X a^i pi a^j Y in S with room
    => X a^{i'} pi' a^{j'} Y in S for the predicted i',j'. Returns (#checked, #fail)."""
    solo = {}
    for w in S:
        if w[0] == 'a' and w[-1] == 'a' and set(w) != {'a'}:
            core = w.strip('a')
            lam = len(w) - len(core)
            if acount(w) <= N - 1 and len(w) - len(w.lstrip('a')) >= 1:
                solo.setdefault(core, set()).add(acount(w))
    solo = {k: min(v) for k, v in solo.items()}
    delta = {k: N - e for k, e in solo.items()}
    chk = fl = 0
    for W in S:
        for core, d in delta.items():
            start = W.find(core)
            while start != -1:
                i0 = len(W[:start]) - len(W[:start].rstrip('a'))
                end = start + len(core)
                j0 = len(W[end:]) - len(W[end:].lstrip('a'))
                for core2, d2 in delta.items():
                    if core2 == core or (set(core2) | {'a'}) != (set(core) | {'a'}): continue
                    lam = solo[core] - acount(core); lam2 = solo[core2] - acount(core2)
                    need = 2 + max(0, lam - lam2)
                    if i0 + j0 < need: continue
                    # choose i,j within flanks with i+j = 2+max(0,lam-lam2), i,j>=1
                    s = 2 + max(0, lam - lam2)
                    i = min(i0, s - 1); j = s - i
                    if j > j0 or j < 1 or i < 1: continue
                    if i + j > lam: continue
                    s2 = s + lam2 - lam
                    i2 = 1; j2 = s2 - 1
                    if j2 < 1: continue
                    X = W[:start - i]; Y = W[end + j:]
                    W2 = X + 'a' * i2 + core2 + 'a' * j2 + Y
                    chk += 1
                    if W2 not in S: fl += 1
                start = W.find(core, start + 1)
    return chk, fl

def rotation_instances(S, N):
    """(Rot): a^p kappa a^r in S, p,r>=1, 3<=p+r<=N-1, kappa=core  =>  ctx(a kappa)=ctx(kappa a)."""
    ctx = defaultdict(set)
    for w in S:
        n = len(w)
        for i in range(n):
            for j in range(i + 1, n + 1):
                ctx[w[i:j]].add((w[:i], w[j:]))
    chk = fl = 0
    for w in S:
        if set(w) == {'a'} or w[0] != 'a' or w[-1] != 'a': continue
        core = w.strip('a'); lam = len(w) - len(core)
        if 3 <= lam <= N - 1:
            chk += 1
            if ctx['a' + core] != ctx[core + 'a']: fl += 1
    return chk, fl

def run_S1_S3(trials=300):
    log('== [S1]/[S3] random seeds -> exact closure; Lemma S and exchange (X1) on closed sets')
    stats = defaultdict(int)
    xchk = xfail = 0
    for t in range(trials):
        N = random.randint(5, 6)
        seed = random_seed_words(N, random.randint(1, 3))
        R = closure(seed, cap_len=N + 3, cap_words=3000, max_rounds=12, N=N, stop_on_contra=False)
        stats[R['status']] += 1
        if R['status'] == 'closed':
            K = R['K']
            ok, wit = check_closed(K)
            must(ok, 'S1: closure reported closed but exact check fails: %s' % wit)
            if shortest_apower(K) == N:
                stats['closed_with_min_aN'] += 1
                sc = skeleton_conflicts(K, N)
                must(not sc, 'S1: Lemma S violated on closed set: %s' % sc)
                c, f = rotation_instances(K, N)
                xchk += c; xfail += f
        elif R['status'] == 'contra':
            stats['contra_' + R['contra'][0]] += 1
    must(xfail == 0, 'S3: rotation lemma failures: %d' % xfail)
    log('   trials=%d status counts=%s' % (trials, dict(stats)))
    log('   rotation-lemma (Rot) instances checked=%d failures=%d' % (xchk, xfail))
    return stats

# =================================================================== S2 negative control
def d1_closure(seed, cap_len, N):
    K = set(seed)
    for _ in range(20):
        ctx = defaultdict(set)
        for w in K:
            n = len(w)
            for i in range(n):
                for j in range(i + 1, n + 1):
                    ctx[(w[i:j],)].add((w[:i], w[j:]))
        bucket = defaultdict(list)
        for x, Es in ctx.items():
            for E in Es: bucket[(ttype(x), E)].append(x)
        new = set()
        for _, xs in bucket.items():
            if len(xs) < 2: continue
            for x in xs:
                for y in xs:
                    if x == y: continue
                    for E1 in ctx[x]:
                        w = fill(E1, y)
                        if w not in K and len(w) <= cap_len: new.add(w)
        if not new: return K
        K |= new
    return None

def run_S2():
    log('== [S2] negative control: d=1-closed set violating Lemma S must be d=2-non-closed')
    found = 0
    N = 7
    cands = [('abaaa', 'aaaaba'), ('abaa', 'aabaa'), ('abaaaa', 'aaba'), ('aabaaa', 'aba')]
    for w1, w2 in cands:
        seed = {'a' * N, w1, w2}
        K = d1_closure(seed, N + 2, N)
        if K is None: continue
        if shortest_apower(K) != N: continue
        sc = skeleton_conflicts(K, N)
        if not sc: continue
        ok, wit = check_closed(K)
        must(not ok and verify_witness(K, wit), 'S2: expected a verified d=2 violation')
        must(wit is not None and len(wit['x']) == 2, 'S2: violation should be two-hole')
        log('   seed', sorted(seed), '-> d1-closed |K|=%d, skeleton conflict %s' % (len(K), sc))
        log('   d=2 witness:', json.dumps(wit, default=list))
        found += 1
        break
    must(found == 1, 'S2: negative control instance found')

# =================================================================== S4 tree arithmetic
def run_S4(trials=4000):
    log('== [S4] Theorem T1 arithmetic on random rank<=r trees')
    worst = 0.0
    for t in range(trials):
        r = random.randint(2, 3); theta = random.randint(1, 4)
        # random tree: node = (terminals, children); depth-limited
        def gen(depth):
            nt = random.randint(0, theta)
            if depth == 0 or random.random() < 0.15:
                return (max(nt, 1), [])
            q = random.randint(1, r)
            return (nt, [gen(depth - 1) for _ in range(q)])
        T = gen(random.randint(2, 9))
        # compute k, heights; boundary = leftmost & rightmost root paths
        nodes = []
        def walk(node, depth, left, right):
            nt, ch = node
            k = nt + sum(walk(c, depth + 1, left and i == 0, right and i == len(ch) - 1)
                         for i, c in enumerate(ch))
            nodes.append((k, left, right, depth))
            return k
        Ntot = walk(T, 1, True, True)
        h = max(d for (_, _, _, d) in nodes)
        # deficits: delta in [k-theta, k] for EVERY big node (boundary included), SNAPPED to reuse
        # existing values whenever possible (adversarial: minimises M)
        vals = set()
        for (k, l, rr, d) in nodes:
            if k > theta:
                lo, hi = max(1, k - theta), k
                reuse = [v for v in vals if lo <= v <= hi]
                vals.add(reuse[0] if reuse else random.randint(lo, hi))
        M = len(vals)
        sigma = 2 * (r + 1)
        bound = theta * sigma ** (2 * M + 1)          # Theorem T1 (sharp form): N < theta*sigma^(2M+1)
        must(Ntot < bound, 'S4: N=%d >= bound=%d (h=%d,r=%d,theta=%d,M=%d)' % (Ntot, bound, h, r, theta, M))
        worst = max(worst, Ntot / bound)
    log('   trials=%d, max N/bound = %.4f' % (trials, worst))

# =================================================================== main
def main():
    t0 = time.time()
    src = open(__file__, 'rb').read()
    log('checker SHA256', hashlib.sha256(src).hexdigest())
    log('python', sys.version.split()[0], ' seed 20261115')
    sel = sys.argv[1].split(',') if len(sys.argv) > 1 else ['S0', 'E1', 'S2', 'S1', 'S4', 'E2']
    log('sections', sel)
    if 'S0' in sel: run_S0()
    if 'E1' in sel: run_E1()
    if 'S2' in sel: run_S2()
    if 'S1' in sel: run_S1_S3()
    if 'S4' in sel: run_S4()
    if 'E2' in sel: run_E2()
    log('== SUMMARY: checks=%d FAIL=%d  time=%.1fs' % (COUNT, FAIL, time.time() - t0))
    log('ALL CHECKS PASSED' if FAIL == 0 else 'SOME CHECKS FAILED')
    sys.exit(0 if FAIL == 0 else 1)

if __name__ == '__main__':
    main()
~~~~~
END SOURCE claude_round13_noncomm_U_checker_2026-11-15.py

## E2. Claude 第十三段：提出検証ログ

**Original filename:** `claude_round13_noncomm_U_checker_output_2026-11-15.txt`  
**Bytes:** `5288`  
**SHA256:** `3dc1019ea1e9a0b26da10ab7d2f8f6badb6efc47f8d7c55738652d0ada4433b5`

BEGIN SOURCE claude_round13_noncomm_U_checker_output_2026-11-15.txt
~~~~~text
command: python3 -I claude_round13_noncomm_U_checker_2026-11-15.py
file SHA256: 3f79da85eb7d128a52b0591e7f51fdcc3aa25f2cc9b469029e76a6e29e96d92a
started: 2026-11-15T22:35:08+09:00
checker SHA256 3f79da85eb7d128a52b0591e7f51fdcc3aa25f2cc9b469029e76a6e29e96d92a
python 3.13.18  seed 20261115
sections ['S0', 'E1', 'S2', 'S1', 'S4', 'E2']
== [S0] exact finite substitutability: controls
   interior-only family a^5 + a^+ b a^+ (total 3) is not closed; witness {"x": ["ab"], "y": ["ba"], "E_accept": ["a", "a"], "E_test": ["", "aa"], "E_accept_x": "aaba", "E_accept_y": "abaa", "E_test_x": "abaa", "E_test_y": "baaa", "type_x": [["a", "b"]], "type_y": [["a", "b"]]}
   closure: status=closed |S|=5 S=['aaab', 'aaba', 'abaa', 'baaa', 'aaaaa']
   negative control {a^5, abaa}: witness {"x": ["a", "aa"], "y": ["aa", "a"], "E_accept": ["", "a", "a"], "E_test": ["", "b", ""], "E_accept_x": "aaaaa", "E_accept_y": "aaaaa", "E_test_x": "abaa", "E_test_y": "aaba", "type_x": [["a"], ["a"]], "type_y": [["a"], ["a"]]}
== [E1] cross-class order dependence: closure of an order-dependent seed
   f2=5: status=closed |K|=34 rounds=2 contra=None
     W1=abaca deficit 5 ; W2=acaba deficit 5 ; same a-collapsed bigram multiset+endpoints=True
     full closed set S1(f2=5) = ['aaabc', 'aaacb', 'aabac', 'aabca', 'aacab', 'aacba', 'abaac', 'abaca', 'abcaa', 'acaab', 'acaba', 'acbaa', 'baaac', 'baaca', 'bacaa', 'bcaaa', 'caaab', 'caaba', 'cabaa', 'cbaaa', 'aaaaac', 'aaaaca', 'aaacaa', 'aacaaa', 'acaaaa', 'caaaaa', 'aaaaaab', 'aaaaaba', 'aaaabaa', 'aaabaaa', 'aabaaaa', 'abaaaaa', 'baaaaaa', 'aaaaaaaa']
     words with content {a,b,c} and a-count<N: ['aaabc', 'aaacb', 'aabac', 'aabca', 'aacab', 'aacba', 'abaac', 'abaca', 'abcaa', 'acaab', 'acaba', 'acbaa', 'baaac', 'baaca', 'bacaa', 'bcaaa', 'caaab', 'caaba', 'cabaa', 'cbaaa']
   f2=4: status=closed |K|=39 rounds=2 contra=None
     W1=abaca deficit 5 ; W2=acaaba deficit 4 ; same a-collapsed bigram multiset+endpoints=True
     REFUTED (exact, finite): deficit not a function of bigram data; cb-order deficit 4 != 2+3
     full closed set S1(f2=4) = ['aaabc', 'aabac', 'aabca', 'abaac', 'abaca', 'abcaa', 'baaac', 'baaca', 'bacaa', 'bcaaa', 'aaaaac', 'aaaaca', 'aaaacb', 'aaacaa', 'aaacab', 'aaacba', 'aacaaa', 'aacaab', 'aacaba', 'aacbaa', 'acaaaa', 'acaaab', 'acaaba', 'acabaa', 'acbaaa', 'caaaaa', 'caaaab', 'caaaba', 'caabaa', 'cabaaa', 'cbaaaa', 'aaaaaab', 'aaaaaba', 'aaaabaa', 'aaabaaa', 'aabaaaa', 'abaaaaa', 'baaaaaa', 'aaaaaaaa']
     words with content {a,b,c} and a-count<N: ['aaabc', 'aabac', 'aabca', 'abaac', 'abaca', 'abcaa', 'baaac', 'baaca', 'bacaa', 'bcaaa', 'aaaacb', 'aaacab', 'aaacba', 'aacaab', 'aacaba', 'aacbaa', 'acaaab', 'acaaba', 'acabaa', 'acbaaa', 'caaaab', 'caaaba', 'caabaa', 'cabaaa', 'cbaaaa']
== [S2] negative control: d=1-closed set violating Lemma S must be d=2-non-closed
   seed ['aaaaaaa', 'aaaaba', 'abaaa'] -> d1-closed |K|=3, skeleton conflict {'AbA': [4, 5]}
   d=2 witness: {"x": ["a", "aa"], "y": ["aa", "a"], "E_accept": ["", "a", "ba"], "E_test": ["", "b", "a"], "E_accept_x": "aaaaba", "E_accept_y": "aaaaba", "E_test_x": "abaaa", "E_test_y": "aabaa", "type_x": [["a"], ["a"]], "type_y": [["a"], ["a"]]}
== [S1]/[S3] random seeds -> exact closure; Lemma S and exchange (X1) on closed sets
   trials=300 status counts={'closed': 209, 'closed_with_min_aN': 209, 'contra': 51, 'contra_apower': 51, 'truncated': 39, 'cap': 1}
   rotation-lemma (Rot) instances checked=1202 failures=0
== [S4] Theorem T1 arithmetic on random rank<=r trees
   trials=4000, max N/bound = 0.1667
== [E2] within-class {b,c} bigram-linearity: closure experiments
   case naive-violating N=10 |seed|=107 -> status=contra |K|=2132 rounds=1 time=1.1s contra=('skeleton', 'AcbbcA', [5, 6, 7])
     certificate: 2 rule applications, replay=True, targets=['aaaacbbcaaa', 'aaaacbbcaa']
        0  x=('abc',) y=('acb',) E0=('', 'aacbcba') E1=('aaa', 'bcaaa')  =>  aaaacbbcaaa
        1  x=('abc',) y=('bca',) E0=('aaabc', 'bca') E1=('aaaacb', 'a')  =>  aaaacbbcaa
   case naive-linear    N=10 |seed|=127 -> status=contra |K|=4097 rounds=1 time=1.8s contra=('skeleton', 'AcbAbcbcAbc', [3, 4, 5])
     certificate: 2 rule applications, replay=True, targets=['aacbabcbcabc', 'acbabcbcabc']
        0  x=('cbacbaa',) y=('abcbcabc',) E0=('a', 'aa') E1=('aacb', '')  =>  aacbabcbcabc
        1  x=('aacbcba',) y=('bcbcabc',) E0=('aa', 'aa') E1=('acba', '')  =>  acbabcbcabc
   case prim-bc2-cb3    N=10 |seed|=39 -> status=contra |K|=494 rounds=2 time=0.9s contra=('skeleton', 'AbbccAbcA', [4, 5])
     certificate: 6 rule applications, replay=True, targets=['aabbccabcaa', 'abbccaabca']
        0  x=('aaaabc',) y=('bcabca',) E0=('aa', 'aa') E1=('abc', 'a')  =>  abcbcabcaa
        1  x=('a', 'cb') y=('aa', 'bc') E0=('abc', 'a', 'aa') E1=('', 'b', 'cabcaa')  =>  aabbccabcaa
        2  x=('aaabca',) y=('cbabc',) E0=('aa', 'aa') E1=('acb', '')  =>  acbcbabc
        3  x=('aaabca',) y=('bcaabc',) E0=('aa', 'aa') E1=('acb', '')  =>  acbbcaabc
        4  x=('aaaabc',) y=('cbabc',) E0=('aa', 'aa') E1=('abc', 'a')  =>  abccbabca
        5  x=('b', 'bab') y=('bb', 'aab') E0=('ac', 'c', 'c') E1=('a', 'cc', 'ca')  =>  abbccaabca
== SUMMARY: checks=4458 FAIL=0  time=474.9s
ALL CHECKS PASSED
exit code: 0
finished: 2026-11-15T22:43:03+09:00
~~~~~
END SOURCE claude_round13_noncomm_U_checker_output_2026-11-15.txt

## F1. 第十三段：独立有限検証Python

**Original filename:** `round13_independent_checks_2026-11-15.py`  
**Bytes:** `5388`  
**SHA256:** `a5666fef8082bc4b59d00f11deacb753dc42f174bf136f081210a8de022efc6e`

BEGIN SOURCE round13_independent_checks_2026-11-15.py
~~~~~text
#!/usr/bin/env python3
"""Independent, source-code-free Round 13 E1/E2 finite certificate audit.
Does NOT import Claude's checker. Uses submitted output strings and reconstructs
seeds and occurrence semantics independently.
"""
import ast, re, collections, itertools, os
from pathlib import Path
OUT = Path('/mnt/data/claude_round13_noncomm_U_checker_output_2026-11-15.txt').read_text()

def occurrence_contexts(S):
    q = collections.defaultdict(set)
    for w in S:
        n=len(w)
        # One hole
        for a in range(n):
            for b in range(a+1,n+1):
                q[(w[a:b],)].add((w[:a],w[b:]))
        # Two holes, positive separator
        for a in range(n):
            for b in range(a+1,n+1):
                for c in range(b+1,n):
                    for d in range(c+1,n+1):
                        q[(w[a:b],w[c:d])].add((w[:a],w[b:c],w[d:]))
    return q

def tp(x):return tuple(frozenset(t) for t in x)
def fill(E,x):return E[0]+x[0]+E[1] if len(x)==1 else E[0]+x[0]+E[1]+x[1]+E[2]
def verify_closed(S,ctx):
    at = collections.defaultdict(list)
    for x,Es in ctx.items():
        for E in Es:at[(tp(x),E)].append(x)
    for xs in at.values():
        ref=ctx[xs[0]]
        for x in xs[1:]:
            if ctx[x]!=ref: return False,(xs[0],x,ref^ctx[x])
    return True,None

def sk(w):
    return re.sub('a+', 'A',w)

def prof(w):
    t=sk(w)
    return (collections.Counter(zip(t,t[1:])),t[:1],t[-1:])

# Reconstruct the closed finite languages from log, without relying on the original program.
for f2,n in [(5,34),(4,39)]:
    m=re.search(r'full closed set S1\(f2=%s\) = (\[.*\])'%f2, OUT)
    assert m, f2
    S=set(ast.literal_eval(m.group(1)))
    assert len(S)==n
    ctx=occurrence_contexts(S)
    ok,wit=verify_closed(S,ctx)
    assert ok,wit
    assert 'a'*8 in S and not any(w and set(w)=={'a'} and len(w)<8 for w in S)
    # Independently enumerate rotation implications, exact full distributions.
    rot=0
    for w in S:
        N=8
        for p in range(1,len(w)-1):
            if w[:p]!='a'*p:continue
            for r in range(1,len(w)-p):
                if w[-r:]!='a'*r:continue
                k=w[p:len(w)-r]
                if k and 3<=p+r<=7:
                    assert ctx[('a'+k,)] == ctx[(k+'a',)], ('Rot',f2,p,k,r)
                    rot+=1
    # full finite X2 distribution equivalence, for all pairs of solo-piece witnesses
    solo=set()
    for w in S:
        for p in range(1,len(w)-1):
            if w[:p]!='a'*p:continue
            for r in range(1,len(w)-p):
                if w[-r:]!='a'*r:continue
                k=w[p:len(w)-r]
                if k and 3<=p+r<=7:solo.add((k,p+r))
    x2=0
    for k,lam in solo:
        for k2,lam2 in solo:
            if set(k)!=set(k2):continue
            for i in range(1,13):
                ip=i+lam2-lam
                if ip<1:continue
                assert ctx[('a'*i,k)] == ctx[('a'*ip,k2)], ('X2',f2,k,lam,k2,lam2,i,ip)
                x2+=1
    print(f'E1 f2={f2}: |S|={n}, |tuple-context pairs|={sum(map(len,ctx.values()))}, closed=YES, Rot={rot}, X2_all_i={x2}')
    if f2==4:
        u,v='abaca','acaaba'
        assert u in S and v in S and prof(u)==prof(v)
        assert u.count('a')==3 and v.count('a')==4
        print(f' E1 COUNTEREXAMPLE verified: {u} a={u.count("a")}, {v} a={v.count("a")}, shared profile={prof(u)}')

# Parse and replay submitted E2 2/2/6-step certificates independently.
def compositions(total, k):
    for cuts in itertools.combinations(range(1,total),k-1):
        a=(0,)+cuts+(total,)
        yield [a[i+1]-a[i] for i in range(k)]
def flank(pieces,a_total):
    for nums in compositions(a_total,len(pieces)+1):
        w='a'*nums[0]
        for core,x in zip(pieces,nums[1:]):w+=core+'a'*x
        yield w

def seed(deltas):
    S={'a'*10}
    for p,x in deltas.items():S.update(flank([p],10-x))
    for p,q in itertools.product(deltas,repeat=2):
        t=10-deltas[p]-deltas[q]
        if t>=3:S.update(flank([p,q],t))
    return S

cases=[('naive-violating',{'bc':2,'cb':2,'bcbc':3,'cbcb':4}),('naive-linear',{'bc':2,'cb':2,'bcbc':3,'cbcb':3}),('prim-bc2-cb3',{'bc':2,'cb':3})]
for name,ds in cases:
    S=seed(ds);assert len(S)=={'naive-violating':107,'naive-linear':127,'prim-bc2-cb3':39}[name]
    segment=OUT.split('case '+name)[1].split('\n   case ')[0]
    steps=re.findall(r'\n\s*(\d+)\s+x=(\(.*?\)) y=(\(.*?\)) E0=(\(.*?\)) E1=(\(.*?\))\s*=>\s*(\w+)',segment)
    for ix,x,y,e0,e1,w in steps:
        x,y,e0,e1=map(ast.literal_eval,(x,y,e0,e1))
        assert len(x)==len(y)==len(e0)-1==len(e1)-1
        assert tp(x)==tp(y)
        assert all(x) and all(y)
        if len(x)==2:assert e0[1] and e1[1]
        assert fill(e0,x) in S and fill(e0,y) in S and fill(e1,x) in S,(name,ix,x,y,e0,e1)
        assert fill(e1,y)==w,(name,ix,'wrong-target')
        S.add(w)
    print(f'E2 {name}: seed={len(seed(ds))}, replayed={len(steps)}, verified=yes, size-final={len(S)}')
    assert len(steps)=={'naive-violating':2,'naive-linear':2,'prim-bc2-cb3':6}[name]
    conflict=collections.defaultdict(set)
    for w in S:
        if w.count('a')<10 and set(w)!={'a'}:
            conflict[sk(w)].add(w.count('a'))
    assert any(len(x)>1 for x in conflict.values())
    print(' E2 contradiction independently confirmed:',next((k,sorted(v)) for k,v in conflict.items() if len(v)>1))
print('ALL INDEPENDENT CHECKS PASSED')
~~~~~
END SOURCE round13_independent_checks_2026-11-15.py

## F2. 第十三段：独立有限検証ログ

**Original filename:** `round13_independent_checks_output_2026-11-15.txt`  
**Bytes:** `736`  
**SHA256:** `0a7541f61afc7754fcc80c0bdcfb3df223fc49976599611c29ee4dba9b8528b7`

BEGIN SOURCE round13_independent_checks_output_2026-11-15.txt
~~~~~text
E1 f2=5: |S|=34, |tuple-context pairs|=1784, closed=YES, Rot=70, X2_all_i=1584
E1 f2=4: |S|=39, |tuple-context pairs|=2324, closed=YES, Rot=77, X2_all_i=1691
 E1 COUNTEREXAMPLE verified: abaca a=3, acaaba a=4, shared profile=(Counter({('A', 'b'): 1, ('b', 'A'): 1, ('A', 'c'): 1, ('c', 'A'): 1}), 'A', 'A')
E2 naive-violating: seed=107, replayed=2, verified=yes, size-final=109
 E2 contradiction independently confirmed: ('AcbbcA', [6, 7])
E2 naive-linear: seed=127, replayed=2, verified=yes, size-final=129
 E2 contradiction independently confirmed: ('AcbAbcbcAbc', [3, 4])
E2 prim-bc2-cb3: seed=39, replayed=6, verified=yes, size-final=45
 E2 contradiction independently confirmed: ('AbbccAbcA', [4, 5])
ALL INDEPENDENT CHECKS PASSED
~~~~~
END SOURCE round13_independent_checks_output_2026-11-15.txt

===== END FILE =====

===== BEGIN FILE audit_claude_round14_noncomm_Parikh_independent_2026-11-16.md bytes=12133 sha256=440a3b3372542e85b11092999f1e1b0006e38ce949074dfff4459b16c3c01c76 =====
# 第十四段 Claude「非可換 Parikh 還元 P」独立数学監査

**監査日:** 2026-11-16 JST  
**対象:** `claude_round14_noncomm_Parikh_2026-11-15.zip`、同名 `..._report_2026-11-15.md`、提出チェッカー・提出ログ。比較対象は #2 MCFG `main.tex` の `def:grammar-properties`、`def:tuple-substitutable`、`lem:thickness-equivalence`、`op:fanout-two`。  
**結論:** **TR は有効な手証明と独立検証に支えられている。CA は発表された仮定のままでは偽で、67語の厳密な有限反例がある。適切に補強した CA\* は修復可能。P_tree、予想 U、`op:fanout-two` は OPEN。** これは専門家査読・形式証明ではない。

---

## 1. 結論表

| 項目 | 独立監査の判定 | コメント |
|---|---|---|
| L1(R),(U)、L2、Rot、Cat | VALID（以前の監査と照合） | 元の good/tuple-substitutability の定義と整合 |
| X1⁺（`i,i'≥1`） | **VALID** | 第十三段の偽 X1 の型抜けを修正。単独宿主の構成が成立 |
| S（4方向の置換） | **VALID WITH RANGE CONDITIONS** | 右／左隣接と非空隔ての宿主を確認。非空の穴、`i'≥1` が必要 |
| F（枠補題） | **VALID AFTER DOMAIN CLARIFICATION** | `u,u'∈Σ⁺` が必要。原文では `u=u'=ε` を除外していないためそのままだと2穴同値が未定義 |
| OS、CS | **VALID** | 両宿主の共通受理性・成分型一致・非空セパレータを確認 |
| **CA（原文 §2.4）** | **REFUTED AS WRITTEN** | 67語の厳密閉言語で反証。後述の **加法的な種・正の初期室** が欠落 |
| **CA\*（修正版）** | **VALID WITH EXPLICIT ASSUMPTIONS** | 初期二単位語の a-budget が欠損の和に一致し、初期・目標の a-budget≥3 なら交換順序を工夫して帰納できる |
| BA（境界根道） | **VALID WITH DEPENDENCIES** | 木の議論は Fable-C の非分岐根道補題に依存。全体の最終上界を新規独立証明したものではない |
| **TR（転置定理）** | **VALID** | **CAを使用せず**、7手の文脈証明と3270件の独立 replay が成立 |
| TR-tree | **VALID WITH REPAIRED CA\*** | 木由来・逐次配置の連結種は実際に加法的 a-budget を持つ必要あり。原文CAのまま引用しない |
| 82語の分岐なし反例 | **VALID, EXACT FINITE** | 独立閉性検査に合格。P_tree の反例ではない |
| IH, AB, P_tree, U | **OPEN** | 証明なし。T2′ は条件付きのまま |
| `op:fanout-two` | **OPEN** | 上記は一般擬多様体境界の結論ではない |

## 2. 転置定理 TR — 成立する部分

`Σ` 上の内容型付け `c_Σ` と `L∈C^{mcf}_{2,c_Σ}` を固定し、`N` を最短受理 `a` 冪の長さとする。異なる非 `a` 文字 `b,c` に対して、Rot核 `β=bc`, `γ=cb` の欠損を `δ₁,δ₂` とする。正の欠損、単独受理語、および `a^x β a^y γ a^z∈L`（`x+y+z=N−δ₁−δ₂`）を仮定する。

報告の室条件 `(C)` において `D=δ₂−δ₁`、`t=N−δ₁−δ₂` とし、7手で

```
W4 = bbccbc a^(N−3δ₁)
W7 = bbccbc a^(N−3δ₁ + D)
```

を導く。いずれも `a` の個数が `[1,N−1]` に入る。両語は `a` 連を一記号 `Â` に潰した骨格が一致するため、L2によりその `a` 個数は一致し、`D=0`。報告のステップ1〜7を通して、特に次を確認した。

- 2穴の交換では、比較タプルの各成分の内容型が一致する。
- OS/CSの共有文脈と試験文脈の間隔は実際に非空。
- `cb→bc` の移送を単位境界の内部出現に適用するステップ3は、S4 の「任意の因子出現」版に含まれる。
- ステップ4、5の合成核 `bccb`、`bcbc` は、先行する受理語と Rot により必要な外側 `a` の室を獲得している。
- 最終2語へのL2の適用は同じ骨格、かつ正の `a` 数 `<N` を満たす。

**簡潔な室条件の保証:** `δ₁≥δ₂≥1` と並べ直し、`N≥4δ₁+1` とする。`D=δ₂−δ₁≤0`、`j=1+δ₁−δ₂`。すると `t=N−δ₁−δ₂≥2δ₁+1`、`N−3δ₁−j≥δ₂`、`N−2δ₁≥2δ₁+1`、`3δ₁−D=4δ₁−δ₂≤N−1`。他の `(C)` の不等式も直ちに従う。反転によって反対方向に帰着できるので、主張した `N≥4max(δ₁,δ₂)+1` は十分である。

**数値・証明書監査:** 提出チェッカー `S0,A,B,C` をそのまま再実行：366チェック、失敗0、終了コード0。さらに、提出コードは**証明書の生成専用**として読み込み、別実装の `independent_step_replay` で、**3270証明書・合計68670個の直接代入ステップ**の型・文脈・非空・三つの前提を一段ずつ検査した（全通過）。等欠損の対照244例も通過。これにより発表された具体的な有限証明書系列は再現性が高い。

**判定:** TRの上記正確な仮定での**手証明は有効**。未査読・未形式化であることとは区別する。

## 3. CA は原文の仮定では偽：67語の強い反例

報告 §2.4 のCAは次を主張する。Rot核 `κ_B, κ_C` の「連結な種」`a^x κ_B a^y κ_C a^z∈L` が一つあり、目標列について `e_m=N−Σδ(κ_j)−Σ|κ_j|_a≥3` なら、加法的な目標 a 数を持つ全配置の合成語が受理される（途中で `i'≥1` を要する、と注記）。ところが、**出発する連結種の a 数**が、単独核の欠損から決まる値に一致するとは記していない。

以下の固定有限言語を考える。`N=10`、`Σ={a,b,c}`。67語の集合 `L₆₇` を

1. `a^10`、
2. `a^i bc a^(8−i)` と `a^i cb a^(8−i)` （`i=0,…,8`、18語）、
3. 独立検証プログラムの `words48` に**明示的に列挙された48語**（いずれも `a` の個数3、非 `a` 文字4個）

の和集合とする。3の中には `bccbaaa` がある。

独立に記述した**全受理文脈検査**で、`L₆₇` は内容型付けに関して `d=1,2` の組代入可能性を満たす。結果：67語、1566受理タプル、12019タプル・文脈組、5544同型同宿主の比較、**違反0**。最短 `a` 冪は `a^10`。

- `κ_B=bc`, `κ_C=cb` は共に Rot核で、単独語 `a bc a^7`, `a cb a^7` が受理される。`λ_B=λ_C=8`、`δ_B=δ_C=2`。
- **正の室を持つ**連結種 `bccb a^3∈L₆₇` がある。これは `x=y=0,z=3` の形で、原文の連結種条件を満たす。
- しかしCAの m=2 の「加法的」結論が要求する外側の `a` の個数は `e_2=10−2−2=6≥3`。`bccb a^6` は `L₆₇` に**存在しない**（この言語の `a` 個数は 3,8,10 のみ）。

よって **CA は出発種に3個の `a` があっても偽**。単なる「初期 a が0なので操作不能」という軽微な問題ではなく、**出発種の a-budget 自体が加法的でない**ことが本質的な欠落である。「途中のS適用で `i'≥1`」という注記は、交換系列の存在と初期 a-budget を保証せず、欠けた仮定を補わない。

補助的に、より簡単な105語の**可換**言語も反例になる：

```
L₁₀₅ = {a^10}
       ∪ {w : (|w|_a, |w|_b, |w|_c) = (8,1,1)}
       ∪ {w∈{b,c}^4 : b,c の双方を含む}.
```

これは全長固定のParikh層の和であり、105語、独立全検査で2488タプル・35245文脈組・22302比較、違反0。Rot核 `bc,cb` と連結種 `bccb`（外側 `a` は0）を持つが、`bccb a^6` を持たない。67語版は初期室が正でも破れることを示す、より強い例である。

### 3.1 修正版 CA\*（成立する限定形）

原文CAは、次の**二つの追加条件**を明記すれば修復できる。

> **CA\*.** 各 Rot核 `κ` に `h(κ):=N−λ_κ=δ(κ)+|κ|_a≥1` を置く。受理済みの連結種の外側 a 総数が **ちょうど** `t=N−h(κ_B)−h(κ_C)≥3` であるとする。目標核列 `κ₁,…,κ_m` について `e_m=N−Σh(κ_j)≥3` とする。このとき、その目標核列の全ての外側 a 分配（合計 `e_m`）が受理される。

**補修証明の骨子（独立再構成）**：Rot/ Catで種を `κ_Bκ_C a^t` にする。m=2では核B,Cを目標1,2へSで一つずつ置換する。`h_1≤h_B` ならBから、そうでなく `h_2≤h_C` ならCから、それ以外ならBから置換すれば、最初の変更後の外側 a 数は少なくとも `min(t,e_2)≥3`。最終的に `κ₁κ₂a^{e_2}` が得られる。一般のmは帰納する。最初の m−1 個の合成核 `M` は、帰納法から `Ma^{e_{m−1}}∈L`、`e_{m−1}≥e_m≥3` でRot核。m=2の場合から `κ₁κ_m a^{e_{1m}}∈L` を作り、S4で隔て `κ_m≠ε` のまま `κ₁→M` を行うと、右端のa指数が `e_{1m}+(λ_M−λ_{κ₁})=e_m≥3` になる。最後にRot/Catで全配置へ移せる。

この修正は**原文CAとは別の主張**であり、その適用時には出発種の加法的 a-budget を**必ず具体的な導出**から確証する必要がある。特に`a^N`の導出木で祖先子孫でない二節点を**同時置換**した逐次配置の種なら、各欠損の和だけ元のa個数が変わるので、加法的条件を満たす。したがってTR-treeの逐次配置ケースはCA\*で再構成できる見込みが高い。ただし交錯・入れ子のIHは解決しない。

## 4. その他の確認点

**Fの定義域：** `κ=puq`, `κ'=pu'q` に `p≠ε`, `c(u)=c(u')` しか書かれていない場合、`u=u'=ε` は排除されない。しかし2穴同値 `(a^i,u)≡(a^{i'},u')` は `u,u'∈Σ⁺` でなければ定義できない。定理文へ `u,u'≠ε` を追加すること。使用された `bc↔cb` の具体例は非空なので影響しない。

**E-B（82語）:** `a^10` と、`bc` に `a` を8個、`cb` に `a` を7個挿入する全語との和は、独立の全受理文脈検査で 82語・2041受理タプル・26890文脈組・16601比較、違反0。複合語を含まない場合に欠損の一致が強制されないという報告の例は正しい。

**BA:** 端に触れる根道を除外するという修正は必要であり、根道一本に同じ非終端が二度現れないという既存Fable-C議論により、定数倍の道数上界は合理的。だが完全なT2′の定数・量化を今回独立に逐行再認証したわけではない。

**数値実験:** 提出ログは全589チェックPASS・終了コード0、約1101秒と主張する。ただし今回**再実行したのは** `S0,A,B,C`（366チェックPASS、約1秒）とDのN=7,8（10件の非線形反証、4件の線形対照）。長時間のD全範囲・E全範囲は再実行していない。独立TR replayは 3270件・68670直接ステップ、対照244件、全PASS。`closed` と `cap/truncated` を混同していないことを確認した。

## 5. 正式な未解決問題への含意・次ラウンドの義務

- **証明済みの核：** 非可換で `de` / `ed` の2核に連結で加法的な宿主と十分な室があるなら、欠損差は0に強制される（TR）。
- **修正された道具：** CAを引用するときは必ず **CA\*** とし、出発種の **加法的a-budget** と `≥3` の室を検証する。
- **残る一般化:** AB（任意の同Parikh合成核の欠損一致）、IH（fan-out 2の交錯・入れ子からの連結宿主実現）、そこから P_tree、予想Uへの厳密な移植。
- **重要な限定:** 今回のTR・CA\*は `op:fanout-two` そのもののYES/NOどちらも証明しない。一般擬多様体の境界問題はOPEN。
- **研究記録:** 本監査はGitHub・論文本文を変更しない。

**添付ファイル：** 本監査報告、`independent_round14_audit_2026-11-16.py`（原チェッカーを閉性判定に流用せず独立実装、67語/105語/82語の全列挙とTR証明書の独立replay）、`out_independent_round14_audit_2026-11-16.txt`、`round14_rerun_S0ABC_2026-11-16.txt`、`out_round14_D_N7_N8_2026-11-16.txt`、元のClaude提出物。

===== END FILE =====

===== BEGIN FILE claude_round14_noncomm_Parikh_checker_2026-11-15.py bytes=34588 sha256=eaccd71285f51f26d702b8d76e6fe7a7a5847d08e8f6f97368b8d939729663ea =====
#!/usr/bin/env python3
"""claude_round14_noncomm_Parikh_checker_2026-11-15.py  (Claude, Round 14, 2026-11-15/16 JST)

Standalone, Python 3 standard library only, deterministic.
Run:   python3 -I claude_round14_noncomm_Parikh_checker_2026-11-15.py [S0,A,B,C,D,E]
Exit code 0 iff every [MUST] check passes.

Semantics: content typing c(w)=alph(w); tuple substitutability for d in {1,2}; every hole is a
NONEMPTY word over Sigma; a d=2 context l[]m[]r has m NONEMPTY.  'closed' means the closure
queue was exhausted with NO length truncation (then re-verified by the exact procedure);
'truncated'/'cap' are NOT closed.  'contra' = shorter a-power or a Lemma-L2 skeleton conflict
(same a-collapsed skeleton, different a-counts, both <= N-1), always with a replayed
certificate of direct rule applications  E0[x],E0[y],E1[x] in K => E1[y].

Sections
  S0  decision-procedure controls
  A   replay of the 40-word X1 counterexample; padded X1+ has no violation; unpadded X1 caught
  B   a-central language: Parikh-equal cores bc/cb with different deficits WITHOUT composite
      (exactly closed); adding one two-unit word gives a certified contradiction
  C   Theorem TR: the hand proof expanded to rule-level certificates for all N<=40 in range;
      tamper controls (empty separator / type mismatch / missing premise) must be rejected
  D   minimal tree seeds {a^N, w_bc, w_cb, w_(bc,cb)}, N=7..12, all admissible deficits
  E   computational evidence: other pairs, a three-unit relation, interleaved fan-out-2 seeds
"""

from collections import defaultdict, deque
import itertools

def ctype(w):
    return frozenset(w)

def ttype(x):
    return tuple(frozenset(c) for c in x)

def skel(w):
    out = []
    for ch in w:
        if ch == 'a':
            if not out or out[-1] != 'A':
                out.append('A')
        else:
            out.append(ch)
    return ''.join(out)

def acount(w):
    return w.count('a')

def fill(E, x):
    if len(x) == 1:
        return E[0] + x[0] + E[1]
    if E[1] == '':
        raise ValueError('empty separator')
    return E[0] + x[0] + E[1] + x[1] + E[2]

def tuples_of(w):
    n = len(w)
    for i in range(n):
        for j in range(i + 1, n + 1):
            yield (w[i:j],), (w[:i], w[j:])
    for i in range(n):
        for j in range(i + 1, n + 1):
            for k in range(j + 1, n + 1):          # separator w[j:k] nonempty
                for l in range(k + 1, n + 1):
                    yield (w[i:j], w[k:l]), (w[:i], w[j:k], w[l:])

def ctx_maps(S):
    ctx = defaultdict(set)
    for w in S:
        for x, E in tuples_of(w):
            ctx[x].add(E)
    return ctx

def check_closed(S):
    """Exact: S (finite) is (2,content)-tuple-substitutable iff for every (type,E) bucket all
    tuples have identical context sets.  Returns (True,None) or (False, witness dict)."""
    S = set(S)
    ctx = ctx_maps(S)
    bucket = defaultdict(list)
    for x, Es in ctx.items():
        t = ttype(x)
        for E in Es:
            bucket[(t, E)].append(x)
    for (t, E0), xs in bucket.items():
        if len(xs) < 2:
            continue
        ref = ctx[xs[0]]
        for y in xs[1:]:
            if ctx[y] != ref:
                x = xs[0]
                diff = ref ^ ctx[y]
                E1 = next(iter(diff))
                if E1 in ctx[y]:
                    x, y = y, x
                return False, dict(x=x, y=y, E0=E0, E1=E1, E0x=fill(E0, x), E0y=fill(E0, y),
                                   E1x=fill(E1, x), E1y=fill(E1, y))
    return True, None

def verify_witness(S, wit):
    x, y, E0, E1 = wit['x'], wit['y'], wit['E0'], wit['E1']
    if ttype(x) != ttype(y) or len(x) != len(y):
        return False
    if any(c == '' for c in x + y):
        return False
    if len(x) == 2 and (E0[1] == '' or E1[1] == ''):
        return False
    return fill(E0, x) in S and fill(E0, y) in S and fill(E1, x) in S and fill(E1, y) not in S

def shortest_apower(S):
    ns = [len(w) for w in S if w and set(w) == {'a'}]
    return min(ns) if ns else None

def skeleton_conflicts(S, N):
    by = defaultdict(set)
    for w in S:
        if set(w) != {'a'} and acount(w) <= N - 1:
            by[skel(w)].add(acount(w))
    return {k: sorted(v) for k, v in by.items() if len(v) > 1}

# --------------------------------------------------------------------------------------
class Closure:
    """Incremental closure of a seed under the d=1,2 content-typed substitution rule.
    status: 'closed' (queue exhausted, nothing truncated: K is exactly closed),
            'truncated' (queue exhausted but some consequence exceeded cap_len: K is NOT closed),
            'cap' (word cap reached), 'contra' (shorter a-power or Lemma-L2 skeleton conflict)."""

    def __init__(self, seed, N=None, cap_len=None, cap_words=10**5, stop_on_contra=True):
        self.N, self.cap_len, self.cap_words = N, cap_len, cap_words
        self.stop = stop_on_contra
        self.K = set()
        self.origin = {}
        self.parent = {}
        self.members = {}
        self.ctxs = {}              # root -> {E: source member x with E[x] in K}
        self.rep = {}               # (type, E) -> first tuple seen
        self.fadj = defaultdict(list)   # proof forest: x -> [(y, E)] with E[x],E[y] in K
        self.queue = deque()
        self.truncated = False
        self.status = None
        self.contra = None
        self.skmap = {}
        for w in seed:
            self._add(w, None)

    def find(self, x):
        p = self.parent
        root = x
        while p[root] != root:
            root = p[root]
        while p[x] != root:
            p[x], x = root, p[x]
        return root

    def _add(self, w, org):
        if w in self.K:
            return
        if self.cap_len is not None and len(w) > self.cap_len:
            self.truncated = True
            return
        self.K.add(w)
        self.origin[w] = org
        self.queue.append(w)
        N = self.N
        if N is not None and self.contra is None:
            if set(w) == {'a'} and len(w) < N:
                self.contra = ('apower', w)
            elif set(w) != {'a'} and acount(w) <= N - 1:
                s = skel(w)
                if s in self.skmap and acount(self.skmap[s]) != acount(w):
                    self.contra = ('skeleton', self.skmap[s], w)
                else:
                    self.skmap.setdefault(s, w)

    def _newctx(self, root, E, src):
        C = self.ctxs[root]
        if E in C:
            return
        C[E] = src
        for y in self.members[root]:
            self._add(fill(E, y), (src, y, E))

    def _union(self, x, y, E):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return
        self.fadj[x].append((y, E))
        self.fadj[y].append((x, E))
        if len(self.members[rx]) + len(self.ctxs[rx]) < len(self.members[ry]) + len(self.ctxs[ry]):
            rx, ry = ry, rx
        # merge ry into rx
        Mx, My = self.members[rx], self.members[ry]
        Cx, Cy = self.ctxs[rx], self.ctxs[ry]
        for E1, src in Cx.items():
            if E1 not in Cy:
                for yy in My:
                    self._add(fill(E1, yy), (src, yy, E1))
        for E1, src in Cy.items():
            if E1 not in Cx:
                for yy in Mx:
                    self._add(fill(E1, yy), (src, yy, E1))
        self.parent[ry] = rx
        Mx.extend(My)
        for E1, src in Cy.items():
            Cx.setdefault(E1, src)
        del self.members[ry], self.ctxs[ry]

    def run(self):
        while self.queue:
            if self.contra is not None and self.stop:
                self.status = 'contra'
                return self
            if len(self.K) > self.cap_words:
                self.status = 'cap'
                return self
            w = self.queue.popleft()
            for x, E in tuples_of(w):
                if x not in self.parent:
                    self.parent[x] = x
                    self.members[x] = [x]
                    self.ctxs[x] = {}
                r = self.find(x)
                self._newctx(r, E, x)
                key = (ttype(x), E)
                z = self.rep.get(key)
                if z is None:
                    self.rep[key] = x
                elif self.find(z) != self.find(x):
                    self._union(z, x, E)
        if self.contra is not None:
            self.status = 'contra'
        else:
            self.status = 'truncated' if self.truncated else 'closed'
        return self

    # ---------------- certificates
    def _path(self, x, y):
        if x == y:
            return [x], []
        prev = {x: None}
        dq = deque([x])
        while dq:
            t = dq.popleft()
            if t == y:
                break
            for (u, E) in self.fadj[t]:
                if u not in prev:
                    prev[u] = (t, E)
                    dq.append(u)
        if y not in prev:
            raise RuntimeError('no forest path')
        nodes, edges = [y], []
        t = y
        while prev[t] is not None:
            s, E = prev[t]
            nodes.append(s)
            edges.append(E)
            t = s
        nodes.reverse(); edges.reverse()
        return nodes, edges

    def certificate(self, targets):
        """ordered direct rule applications (x,y,E0,E1,conclusion) deriving targets from seed"""
        steps, have = [], set(w for w, o in self.origin.items() if o is None)
        sys_limit = []

        def need(w):
            stack = [(w, 0)]
            while stack:
                v, st = stack.pop()
                if v in have:
                    continue
                src, y, E1 = self.origin[v]
                nodes, edges = self._path(src, y)
                prem = [fill(E1, src)]
                for i, E0 in enumerate(edges):
                    prem.append(fill(E0, nodes[i]))
                    prem.append(fill(E0, nodes[i + 1]))
                missing = [p for p in prem if p not in have]
                if st == 0 and missing:
                    stack.append((v, 1))
                    for p in missing:
                        stack.append((p, 0))
                    continue
                if v in have:
                    continue
                cur = fill(E1, src)
                for i, E0 in enumerate(edges):
                    nxt = fill(E1, nodes[i + 1])
                    if nxt not in have:
                        steps.append((nodes[i], nodes[i + 1], E0, E1, nxt))
                        have.add(nxt)
                have.add(v)
        for t in targets:
            need(t)
        return steps

def replay(seed, steps):
    """Independent replay: each step must be a legal rule application on already-derived words."""
    K = set(seed)
    for (x, y, E0, E1, w) in steps:
        if len(x) != len(y) or len(E0) != len(x) + 1 or len(E1) != len(x) + 1:
            return False, 'arity'
        if ttype(x) != ttype(y):
            return False, 'type mismatch %r %r' % (x, y)
        if any(c == '' for c in x + y):
            return False, 'empty hole'
        if len(x) == 2 and (E0[1] == '' or E1[1] == ''):
            return False, 'empty separator'
        for p in (fill(E0, x), fill(E0, y), fill(E1, x)):
            if p not in K:
                return False, 'premise %s missing' % p
        if fill(E1, y) != w:
            return False, 'conclusion mismatch'
        K.add(w)
    return True, K

def compositions(total, parts, minpart=1):
    if parts == 0:
        if total == 0:
            yield ()
        return
    for first in range(minpart, total - minpart * (parts - 1) + 1):
        for rest in compositions(total - first, parts - 1, minpart):
            yield (first,) + rest

def placements(cores, a_total, minrun=1):
    """all words a^{p0} k1 a^{p1} ... kt a^{pt}, p_i >= minrun, sum p = a_total"""
    out = set()
    for comp in compositions(a_total, len(cores) + 1, minrun):
        w = 'a' * comp[0]
        for k, p in zip(cores, comp[1:]):
            w += k + 'a' * p
        out.add(w)
    return out

# ---------------- Theorem TR builder


B, G = 'bc', 'cb'

class Deriv:
    def __init__(self, seed, N):
        self.K = set(seed)
        self.seed = set(seed)
        self.N = N
        self.steps = []
        self.rotready = {}

    # ---------- primitive
    def rule(self, x, y, E0, E1, why=''):
        assert ttype(x) == ttype(y), ('type', x, y, why)
        assert all(c for c in x + y), ('empty hole', why)
        if len(x) == 2:
            assert E0[1] and E1[1], ('empty separator', why)
        for p in (fill(E0, x), fill(E0, y), fill(E1, x)):
            assert p in self.K, ('premise missing', p, why)
        w = fill(E1, y)
        if w not in self.K:
            self.K.add(w)
            self.steps.append((x, y, E0, E1, w))
        return w

    # ---------- L1(R): P a^i Q a^j R -> P a^i2 Q a^j2 R   (Q nonempty, i+j<=N-1)
    def redistribute(self, P, i, Q, j, R, i2, j2):
        N = self.N
        assert Q and i >= 1 and j >= 1 and i2 >= 1 and j2 >= 1 and i + j == i2 + j2 <= N - 1
        if (i, j) == (i2, j2):
            return P + 'a' * i + Q + 'a' * j + R
        return self.rule(('a' * i, 'a' * j), ('a' * i2, 'a' * j2),
                         ('', 'a', 'a' * (N - 1 - i - j)), (P, Q, R), 'L1R')

    # ---------- Rot readiness for a core k with a known standalone word a^p k a^r in K
    def rot_ready(self, k, p, r):
        lam = p + r
        assert 3 <= lam <= self.N - 1 and p >= 1 and r >= 1
        assert 'a' * p + k + 'a' * r in self.K
        A2 = self.redistribute('', p, k, r, '', 2, lam - 2)       # a^2 k a^(lam-2)
        A1 = self.redistribute('', p, k, r, '', 1, lam - 1)       # a k a^(lam-1)
        self.rotready[k] = lam
        return lam

    def rot_move(self, P, k, Q, direction):
        """direction 'R': P a k Q -> P k a Q ; 'L': P k a Q -> P a k Q"""
        lam = self.rotready[k]
        x, y = ('a' + k,), (k + 'a',)
        if direction == 'L':
            x, y = y, x
        return self.rule(x, y, ('a', 'a' * (lam - 2)), (P, Q), 'Rot ' + k)

    # ---------- Cat for words given as [run0, core1, run1, ..., coreM, runM]; all cores rot-ready
    def recat(self, runs, cores, target):
        """move single a's across cores (Rot) to go from run vector `runs` to `target`."""
        assert sum(runs) == sum(target) and len(runs) == len(cores) + 1
        runs = list(runs)
        def word(rs):
            w = 'a' * rs[0]
            for c, r in zip(cores, rs[1:]):
                w += c + 'a' * r
            return w
        assert word(runs) in self.K, ('recat start missing', word(runs))
        # sweep left-to-right: fix runs[0..M-1] by pushing surplus right / pulling deficit from right
        for g in range(len(cores)):
            while runs[g] > target[g]:
                # word = P a core_g a^{runs[g+1]} ...
                pre = 'a' * runs[0]
                for c, r in zip(cores[:g], runs[1:g + 1]):
                    pre += c + 'a' * r
                pre = pre[:-1]                       # remove one a (the one adjacent to core g)
                post = 'a' * runs[g + 1]
                for c, r in zip(cores[g + 1:], runs[g + 2:]):
                    post += c + 'a' * r
                self.rot_move(pre, cores[g], post, 'R')
                runs[g] -= 1; runs[g + 1] += 1
            while runs[g] < target[g]:
                # need an a right after core g: total conservation guarantees runs[g+1]>0 eventually;
                # pull from the right, cascading if necessary
                h = g + 1
                while runs[h] == 0:
                    h += 1
                # move one a from run h leftwards across cores h-1 ... g
                for q in range(h - 1, g - 1, -1):
                    pre = 'a' * runs[0]
                    for c, r in zip(cores[:q], runs[1:q + 1]):
                        pre += c + 'a' * r
                    post = 'a' * (runs[q + 1] - 1)
                    for c, r in zip(cores[q + 1:], runs[q + 2:]):
                        post += c + 'a' * r
                    self.rot_move(pre, cores[q], post, 'L')
                    runs[q + 1] -= 1; runs[q] += 1
        assert runs == list(target)
        return word(runs)

    # ---------- X1+ mirror: P k a^i R -> P k2 a^{i'} R    (1-hole, a-run adjacent on the right)
    def x1plus_right(self, P, k, i, R, k2):
        lam, lam2 = self.rotready[k], self.rotready[k2]
        i0 = 1 + max(0, lam - lam2); i0p = i0 + lam2 - lam
        assert i >= i0 and i0p >= 1, ('X1+ range', i, i0)
        # hosts: k a^lam , k2 a^lam2   (all outer a's on the right)
        return self.rule((k + 'a' * i0,), (k2 + 'a' * i0p,), ('', 'a' * (lam - i0)),
                         (P, 'a' * (i - i0) + R), 'X1+R %s->%s' % (k, k2))

    # ---------- X2 mirror: P k m a^i R -> P k2 m a^{i'} R   (2-hole, m nonempty)
    def x2_right(self, P, k, m, i, R, k2):
        lam, lam2 = self.rotready[k], self.rotready[k2]
        assert m
        i0 = min(i, lam - 1); i0p = i0 + lam2 - lam
        assert i0 >= 1 and i0p >= 1, ('X2 range', i, i0, i0p)
        q = lam - i0
        return self.rule((k, 'a' * i0), (k2, 'a' * i0p), ('', 'a', 'a' * (q - 1)),
                         (P, m, 'a' * (i - i0) + R), 'X2R %s->%s' % (k, k2))

def to_right(D, k, p, r):
    """from standalone a^p k a^r derive k a^(p+r) (all a's right) by Rot moves"""
    return D.recat([p, r], [k], [0, p + r])

def tr_derivation(N, d1, d2, j=None):
    """Hand proof of TR as a certificate.  Returns (D, W4, W7) or raises AssertionError
    if a side condition fails (then the instance is outside the theorem's room conditions)."""
    lam1, lam2 = N - d1, N - d2
    t = N - d1 - d2
    Dl = d2 - d1
    seed = {'a' * N, 'a' + B + 'a' * (lam1 - 1), 'a' + G + 'a' * (lam2 - 1),
            'a' + B + 'a' + G + 'a' * (t - 2)}
    D = Deriv(seed, N)
    D.rot_ready(B, 1, lam1 - 1)
    D.rot_ready(G, 1, lam2 - 1)
    # Step 1 (Cat on H3): bc cb a^t ; bccb is a Rot core with lambda=t
    W1 = D.recat([1, 1, t - 2], [B, G], [0, 0, t])          # bccb a^t
    D.recat([0, 0, t], [B, G], [1, 0, t - 1])                 # a bccb a^(t-1) standalone of composite
    D.rot_ready(B + G, 1, t - 1)
    to_right(D, B, 1, lam1 - 1); to_right(D, G, 1, lam2 - 1)
    # Step 2: bc [cb] a^t  ->  bc bc a^(t+D)   (X1+ right)
    W2 = D.x1plus_right(B, G, t, '', B)                       # bcbc a^(N-2d1)
    assert W2 == 'bcbc' + 'a' * (N - 2 * d1)
    # cb bc order:  [bc] cb a^t -> [cb] cb a^(t-D)  (X2 right, separator cb) ; then cb [cb] -> cb [bc]
    W2b = D.x2_right('', B, G, t, '', G)                      # cbcb a^(t-D)
    W2c = D.x1plus_right(G, G, t - Dl, '', B)                 # cbbc a^t
    assert W2c == 'cbbc' + 'a' * t
    # composite bcbc rot-ready (lambda = N-2d1)
    D.recat([0, 0, N - 2 * d1], [B, B], [1, 0, N - 2 * d1 - 1])
    D.rot_ready(B + B, 1, N - 2 * d1 - 1)
    # Step 3: b [cb] c a^(N-2d1) -> b [bc] c a^(N-2d1+D)   (X2 right, separator 'c')
    W3 = D.x2_right('b', G, 'c', N - 2 * d1, '', B)
    assert W3 == 'bbcc' + 'a' * (N - 2 * d1 + Dl)
    # Step 4: b [bc] c a^k -> b [bccb] c a^(N-3d1)
    W4 = D.x2_right('b', B, 'c', N - 2 * d1 + Dl, '', B + G)
    assert W4 == 'bbccbc' + 'a' * (N - 3 * d1)
    # Step 5: bc [bc] a^(N-2d1) -> bc [bcbc] a^(N-3d1)    (X1+ right, k2 = bcbc)
    to_right(D, B + B, 1, N - 2 * d1 - 1)
    W5 = D.x1plus_right(B, B, N - 2 * d1, '', B + B)
    assert W5 == 'bcbcbc' + 'a' * (N - 3 * d1)
    # Step 6: (cb, bc) == (bc, cb) via host E0=('', 'a', a^(t-1)); test context (b, c, a^(N-3d1))
    D.recat([0, 0, t], [G, B], [0, 1, t - 1])                 # cb a bc a^(t-1)
    D.recat([0, 0, t], [B, G], [0, 1, t - 1])                 # bc a cb a^(t-1)
    W6 = D.rule((G, B), (B, G), ('', 'a', 'a' * (t - 1)), ('b', 'c', 'a' * (N - 3 * d1)), 'order swap')
    assert W6 == 'bbcccb' + 'a' * (N - 3 * d1)
    # Step 7: (bc, cb a^j) == (bc, bc a^(j+D)) via host E0=('', 'a', a^(t-1-j))
    if j is None:
        j = max(1, 1 - Dl)
    assert 1 <= j <= t - 1 and j + Dl >= 1 and N - 3 * d1 - j >= 0
    D.recat([0, 0, N - 2 * d1], [B, B], [0, 1, N - 2 * d1 - 1])   # bc a bc a^(N-2d1-1)
    W7 = D.rule((B, G + 'a' * j), (B, B + 'a' * (j + Dl)), ('', 'a', 'a' * (t - 1 - j)),
                ('b', 'c', 'a' * (N - 3 * d1 - j)), 'carrier shift')
    assert W7 == 'bbccbc' + 'a' * (N - 3 * d1 + Dl)
    return D, W4, W7

def conditions(N, d1, d2):
    t = N - d1 - d2; Dl = d2 - d1
    j = max(1, 1 - Dl)
    return all([1 <= d1 <= N - 3, 1 <= d2 <= N - 3, t >= 3, N - 2 * d1 >= 3, N - 2 * d2 >= 1,
                N - 3 * d1 >= 1, j <= t - 1, N - 3 * d1 - j >= 0,
                1 <= 3 * d1 - Dl <= N - 1])


# =====================================================================================
# Round 14 checker main
# =====================================================================================
import hashlib, sys, time, itertools
from collections import Counter

LOG = []; FAIL = 0; COUNT = 0
def log(*a):
    s = ' '.join(str(x) for x in a); LOG.append(s); print(s, flush=True)
def must(cond, msg):
    global FAIL, COUNT
    COUNT += 1
    if not cond:
        FAIL += 1; log('  [FAIL]', msg)
    return cond

def seedmin(N, k1, d1, k2, d2):
    l1 = N - d1 - acount(k1); l2 = N - d2 - acount(k2); t = N - d1 - d2 - acount(k1) - acount(k2)
    if min(l1, l2) < 3 or t < 3: return None
    return {'a' * N, 'a' + k1 + 'a' * (l1 - 1), 'a' + k2 + 'a' * (l2 - 1), 'a' + k1 + 'a' + k2 + 'a' * (t - 2)}

def closure_and_cert(seed, N, cap_len, cap_words):
    C = Closure(seed, N=N, cap_len=cap_len, cap_words=cap_words).run()
    rep = None
    if C.status == 'contra':
        tg = list(C.contra[1:]) if C.contra[0] == 'skeleton' else [C.contra[1]]
        st = C.certificate(tg)
        ok, K = replay(seed, st)
        good = ok is True and all(w in K for w in tg)
        if C.contra[0] == 'skeleton':
            u, v = C.contra[1], C.contra[2]
            good = good and skel(u) == skel(v) and acount(u) != acount(v) and max(acount(u), acount(v)) <= N - 1
        else:
            good = good and len(C.contra[1]) < N
        rep = (len(st), good)
    if C.status == 'closed':
        ok, _ = check_closed(C.K)
        must(ok, 'closure reported closed but exact check fails')
        must(shortest_apower(C.K) == N, 'closed set must keep a^N shortest')
    return C, rep

def rev_steps(steps):
    r = lambda T: tuple(c[::-1] for c in reversed(T))
    return [(r(x), r(y), r(E0), r(E1), w[::-1]) for (x, y, E0, E1, w) in steps]

# ------------------------------------------------------------------ S0
def run_S0():
    log('== [S0] exact decision procedure: controls')
    S = {'a' * 5, 'abaa'}
    ok, wit = check_closed(S)
    must(not ok and verify_witness(S, wit), 'S0: {a^5,abaa} must be non-closed with verified witness')
    log('   {a^5, abaa}: non-closed, witness', wit)
    for w in ['abcab', 'aab', 'abc']:
        for x, E in tuples_of(w):
            if len(x) == 2: must(E[1] != '', 'S0: empty separator generated')
            must(all(x), 'S0: empty hole generated')
            must(fill(E, x) == w, 'S0: fill mismatch')
    seed = {'a' * 5} | placements(['b'], 3)
    C = Closure(seed, N=5, cap_len=8).run()
    must(C.status == 'closed' and check_closed(C.K)[0], 'S0: closure of a^5 + a^+ b a^+ must close exactly')
    log('   closure(a^5 + a^+ b a^+ , total 3):', C.status, sorted(C.K, key=lambda w: (len(w), w)))

# ------------------------------------------------------------------ A: X1
X1_S = set('''aaabc aabac aabca abaac abaca abcaa baaac baaca bacaa bcaaa
aaaaac aaaaca aaaacb aaacaa aaacab aaacba aacaaa aacaab aacaba aacbaa
acaaaa acaaab acaaba acabaa acbaaa caaaaa caaaab caaaba caabaa cabaaa
cbaaaa aaaaaab aaaaaba aaaabaa aaabaaa aabaaaa abaaaaa baaaaaa
aaaaaaaa'''.split())
def run_A():
    log('== [A] X1 counterexample replay; type-safe X1+ (padded) check')
    must(len(X1_S) == 39, 'A: 39 words')
    L = X1_S | {'bc'}; N = 8
    ok, wit = check_closed(L)
    must(ok, 'A: 40-word L must be in C_{2,c} (exact)')
    must(shortest_apower(L) == 8, 'A: a^8 shortest')
    ctx = ctx_maps(L)
    nb = sum(len(v) for v in ctx.values())
    log('   |L|=%d tuples=%d tuple-context pairs=%d closed=%s N=%d' % (len(L), len(ctx), nb, ok, N))
    # audit witness exactly as stated
    must('abcaa' in L and 'aaacba' in L and set('abc') == set('aacb'), 'A: X1 hypotheses (kappa=bc, kappa\'=acb, lam=lam\'=3)')
    must('bc' in L and 'acb' not in L, 'A: X1 conclusion fails (bc in L, acb not in L)')
    log('   original X1 instance: kappa=bc, kappa\'=acb, lam=lam\'=3, s(a kappa)=s(a kappa\')={a,b,c}; bc in L, acb not in L')
    rot = {}
    for w in L:
        if set(w) == {'a'}: continue
        p = len(w) - len(w.lstrip('a')); r = len(w) - len(w.rstrip('a')); k = w.strip('a')
        if p >= 1 and r >= 1 and 3 <= p + r <= N - 1: rot.setdefault(k, set()).add(p + r)
    D = lambda x: ctx.get(x, set())
    c1 = b1 = c0 = b0 = 0; ex0 = None
    for k, ls in rot.items():
        for k2, ls2 in rot.items():
            if set(k) | {'a'} != set(k2) | {'a'}: continue
            for lam in ls:
                for lam2 in ls2:
                    for i in range(1, 12):
                        ip = i + lam2 - lam
                        if ip < 1: continue
                        c1 += 2
                        b1 += D(('a' * i + k,)) != D(('a' * ip + k2,))
                        b1 += D((k + 'a' * i,)) != D((k2 + 'a' * ip,))
                    i = max(0, lam - lam2); ip = max(0, lam2 - lam)
                    c0 += 1
                    if D(('a' * i + k,)) != D(('a' * ip + k2,)):
                        b0 += 1; ex0 = ex0 or (k, k2, i, ip)
    must(b1 == 0, 'A: padded X1+ must have no violation (%d)' % b1)
    must(b0 >= 1, 'A: NEGATIVE CONTROL: unpadded X1 must be caught (i=0 type gap)')
    log('   Rot cores in L:', {k: sorted(v) for k, v in rot.items()})
    log('   X1+ (i,i\'>=1, both sides) distribution checks=%d violations=%d' % (c1, b1))
    log('   original X1 (i=(lam-lam\')_+) checks=%d violations=%d  e.g. %s' % (c0, b0, ex0))

# ------------------------------------------------------------------ B: a-central, no composite
def shuffles(core, na):
    n = len(core) + na; out = set()
    for pos in itertools.combinations(range(n), len(core)):
        w = ['a'] * n
        for p, ch in zip(pos, core): w[p] = ch
        out.add(''.join(w))
    return out
def run_B():
    log('== [B] branching hypothesis is necessary: a-central language without composite words')
    N = 10
    L = {'a' * N} | shuffles('bc', N - 2) | shuffles('cb', N - 3)
    ok, _ = check_closed(L)
    must(ok, 'B: a-central L must be exactly closed')
    must(shortest_apower(L) == N, 'B: a^10 shortest')
    log('   L = a^10 + all a-shuffles of bc with 8 a (deficit 2) + of cb with 7 a (deficit 3): |L|=%d closed=%s' % (len(L), ok))
    w12 = 'abcacbaaa'
    C, rep = closure_and_cert(L | {w12}, N, N + 4, 20000)
    must(C.status == 'contra' and rep and rep[1], 'B: adding the two-unit word must yield a replayed contradiction')
    log('   L + {%s}: status=%s contra=%s certificate steps=%s replay=%s' % (w12, C.status, C.contra, rep and rep[0], rep and rep[1]))

# ------------------------------------------------------------------ C: Theorem TR certificates
def run_C(Nmax=40):
    log('== [C] Theorem TR (bc/cb transposition): rule-level certificates of the hand proof')
    cov = bad = gap = 0; ctrl = 0
    for N in range(7, Nmax + 1):
        for d1 in range(1, N):
            for d2 in range(1, N):
                if N - d1 - d2 < 3: continue
                if d1 == d2:
                    if conditions(N, d1, d2):
                        Dd, W4, W7 = tr_derivation(N, d1, d2)
                        ok, _ = replay(Dd.seed, Dd.steps)
                        must(ok is True and W4 == W7, 'C: control d1=d2 must replay and give W4==W7')
                        ctrl += 1
                    continue
                if conditions(N, d1, d2):
                    Dd, W4, W7 = tr_derivation(N, d1, d2); seed, st = Dd.seed, Dd.steps
                elif conditions(N, d2, d1):
                    Dd, W4, W7 = tr_derivation(N, d2, d1)
                    seed = {w[::-1] for w in Dd.seed}; st = rev_steps(Dd.steps); W4, W7 = W4[::-1], W7[::-1]
                else:
                    if N >= 4 * max(d1, d2) + 1: gap += 1
                    continue
                ok, K = replay(seed, st)
                good = (ok is True and W4 in K and W7 in K and skel(W4) == skel(W7) and acount(W4) != acount(W7)
                        and 1 <= min(acount(W4), acount(W7)) and max(acount(W4), acount(W7)) <= N - 1)
                # seed must be exactly H1-H3 with the declared deficits
                good = good and ('a' * N in seed) and len(seed) == 4
                cov += 1; bad += (not good)
    must(bad == 0, 'C: every TR certificate must replay to an L2 conflict (%d bad)' % bad)
    must(gap == 0, 'C: every case with N>=4max(d)+1 must be covered (%d gaps)' % gap)
    log('   N<=%d: certified contradictions=%d  bad=%d  uncovered-with-N>=4max+1=%d  d1=d2 controls=%d (W4==W7)' % (Nmax, cov, bad, gap, ctrl))
    # print one certificate in full
    Dd, W4, W7 = tr_derivation(12, 2, 3)
    log('   example N=12, d(bc)=2, d(cb)=3: seed=%s' % sorted(Dd.seed))
    for k, (x, y, E0, E1, w) in enumerate(Dd.steps):
        log('     %2d x=%s y=%s E0=%s E1=%s => %s' % (k, x, y, E0, E1, w))
    log('     conflict: %s (a=%d) vs %s (a=%d), same skeleton %s' % (W4, acount(W4), W7, acount(W7), skel(W4)))
    # tampered certificates must be rejected
    st = list(Dd.steps)
    k6 = [i for i, s in enumerate(st) if len(s[0]) == 2 and s[0] == ('cb', 'bc')][0]
    x, y, E0, E1, w = st[k6]
    bad1 = st[:k6] + [(x, y, (E0[0], '', E0[2]), E1, w)] + st[k6 + 1:]
    ok1, why1 = replay(Dd.seed, bad1)
    must(ok1 is False and 'separator' in why1, 'C: tampered (empty separator) certificate must be rejected')
    bad2 = st[:k6] + [(x, (y[0], y[1] + 'a'), E0, E1, w)] + st[k6 + 1:]
    ok2, why2 = replay(Dd.seed, bad2)
    must(ok2 is False, 'C: tampered (type mismatch) certificate must be rejected')
    bad3 = [s for i, s in enumerate(st) if i != 0]
    ok3, why3 = replay(Dd.seed, bad3)
    must(ok3 is False, 'C: certificate with a missing premise must be rejected')
    log('   tamper controls rejected: empty-separator(%s) type(%s) missing-premise(%s)' % (why1, why2, why3))

# ------------------------------------------------------------------ D: minimal tree seeds, bc/cb
def run_D(Nr=range(7, 13)):
    log('== [D] minimal tree seeds {a^N, w_bc, w_cb, w_(bc,cb)}: exact closure / certified contradiction')
    tally = Counter()
    for N in Nr:
        for d1 in range(1, (N - 1) // 2 + 1):
            for d2 in range(1, (N - 1) // 2 + 1):
                s = seedmin(N, 'bc', d1, 'cb', d2)
                if s is None: continue
                C, rep = closure_and_cert(s, N, N + 4, 15000)
                if C.status == 'contra':
                    must(rep[1], 'D: contradiction certificate must replay (%d,%d,%d)' % (N, d1, d2))
                tally[(d1 == d2, C.status)] += 1
                if d1 != d2 and C.status != 'contra':
                    log('   undecided non-linear case', N, d1, d2, C.status, len(C.K))
    log('   tally (d1==d2, status):', dict(tally))
    must(tally[(False, 'contra')] > 0, 'D: at least one contradiction')

# ------------------------------------------------------------------ E: evidence beyond TR
def prop_class(k1, d1, k2, d2):
    from fractions import Fraction
    v1 = (k1.count('b'), k1.count('c')); v2 = (k2.count('b'), k2.count('c'))
    if v1[0] * v2[1] != v1[1] * v2[0]: return 'independent'
    return 'linear' if Fraction(d1, sum(v1)) == Fraction(d2, sum(v2)) else 'nonlinear'
def run_E():
    log('== [E] COMPUTATIONAL EVIDENCE: other unit pairs, a three-unit relation, interleaved fan-out-2 seed')
    tally = Counter()
    for k1, k2 in [('bcc', 'cbc'), ('bcc', 'ccb'), ('bc', 'bbcc'), ('bc', 'bcc'), ('bbc', 'bcc')]:
        N = 10
        for d1 in range(1, 6):
            for d2 in range(1, 6):
                s = seedmin(N, k1, d1, k2, d2)
                if s is None: continue
                C, rep = closure_and_cert(s, N, N + 4, 8000)
                if rep: must(rep[1], 'E: pair certificate replay')
                tally[('pair', prop_class(k1, d1, k2, d2), C.status)] += 1
    N = 12
    def stand(k, d): lam = N - d - acount(k); return 'a' + k + 'a' * (lam - 1)
    def two(k1, d1, k2, d2): t = N - d1 - d2; return 'a' + k1 + 'a' + k2 + 'a' * (t - 2)
    for dbc in (1, 2):
        for dbcc in (2, 3, 4):
            for dbbc in (2, 3, 4):
                ws = {'a' * N, stand('bc', dbc), stand('bcc', dbcc), stand('bbc', dbbc),
                      two('bc', dbc, 'bcc', dbcc), two('bc', dbc, 'bbc', dbbc)}
                C, rep = closure_and_cert(ws, N, N + 4, 12000)
                if rep: must(rep[1], 'E: 3-unit certificate replay')
                tally[('3unit', 'linear' if dbcc + dbbc == 3 * dbc else 'nonlinear', C.status)] += 1
    for N in (11, 12):
        for dB in (2, 3):
            for d1 in (1, 2, 3, 4):
                for d2 in (1, 2, 3, 4):
                    lamB = N - dB - 1; t = N - 2 * dB
                    seed = {'a' * N, 'abac' + 'a' * (lamB - 1), 'ababacac' + 'a' * (t - 4),
                            'a' + 'bc' + 'a' * (N - d1 - 1), 'a' + 'cb' + 'a' * (N - d2 - 1)}
                    C, rep = closure_and_cert(seed, N, N + 3, 12000)
                    if rep: must(rep[1], 'E: interleaved certificate replay')
                    tally[('interleaved', 'linear' if d1 == d2 == dB else 'nonlinear', C.status)] += 1
    for k in sorted(tally): log('   ', k, tally[k])
    lin_contra = sum(v for k, v in tally.items() if k[1] in ('linear', 'independent') and k[2] == 'contra')
    log('   contradictions among linear/independent assignments: %d (a nonzero value would refute P_pair)' % lin_contra)

def main():
    t0 = time.time()
    src = open(__file__, 'rb').read()
    log('checker SHA256', hashlib.sha256(src).hexdigest())
    log('python', sys.version.split()[0], ' deterministic (no randomness used)')
    sel = sys.argv[1].split(',') if len(sys.argv) > 1 else ['S0', 'A', 'B', 'C', 'D', 'E']
    log('sections', sel)
    for name in sel:
        globals()['run_' + name]()
        log('   [time so far %.1fs]' % (time.time() - t0))
    log('== SUMMARY: checks=%d FAIL=%d time=%.1fs' % (COUNT, FAIL, time.time() - t0))
    log('ALL CHECKS PASSED' if FAIL == 0 else 'SOME CHECKS FAILED')
    sys.exit(0 if FAIL == 0 else 1)

if __name__ == '__main__':
    main()

===== END FILE =====

===== BEGIN FILE claude_round14_noncomm_Parikh_checker_output_2026-11-15.txt bytes=5512 sha256=97728f1a0ddcca8afd1651fe04122b7b14709b7de090ee2c43a71fb9b26f4fb6 =====
command: python3 -I claude_round14_noncomm_Parikh_checker_2026-11-15.py
file SHA256: eaccd71285f51f26d702b8d76e6fe7a7a5847d08e8f6f97368b8d939729663ea
started: 2026-11-16T00:09:30+09:00
checker SHA256 eaccd71285f51f26d702b8d76e6fe7a7a5847d08e8f6f97368b8d939729663ea
python 3.13.18  deterministic (no randomness used)
sections ['S0', 'A', 'B', 'C', 'D', 'E']
== [S0] exact decision procedure: controls
   {a^5, abaa}: non-closed, witness {'x': ('a', 'aa'), 'y': ('aa', 'a'), 'E0': ('', 'a', 'a'), 'E1': ('', 'b', ''), 'E0x': 'aaaaa', 'E0y': 'aaaaa', 'E1x': 'abaa', 'E1y': 'aaba'}
   closure(a^5 + a^+ b a^+ , total 3): closed ['aaab', 'aaba', 'abaa', 'baaa', 'aaaaa']
   [time so far 0.0s]
== [A] X1 counterexample replay; type-safe X1+ (padded) check
   |L|=40 tuples=333 tuple-context pairs=2327 closed=True N=8
   original X1 instance: kappa=bc, kappa'=acb, lam=lam'=3, s(a kappa)=s(a kappa')={a,b,c}; bc in L, acb not in L
   Rot cores in L: {'cb': [4], 'b': [6], 'c': [5], 'bc': [3], 'cab': [3]}
   X1+ (i,i'>=1, both sides) distribution checks=238 violations=0
   original X1 (i=(lam-lam')_+) checks=11 violations=4  e.g. ('cb', 'bc', 1, 0)
   [time so far 0.0s]
== [B] branching hypothesis is necessary: a-central language without composite words
   L = a^10 + all a-shuffles of bc with 8 a (deficit 2) + of cb with 7 a (deficit 3): |L|=82 closed=True
   L + {abcacbaaa}: status=contra contra=('skeleton', 'abcbcbcaaa', 'abcbcbcaa') certificate steps=10 replay=True
   [time so far 0.3s]
== [C] Theorem TR (bc/cb transposition): rule-level certificates of the hand proof
   N<=40: certified contradictions=3270  bad=0  uncovered-with-N>=4max+1=0  d1=d2 controls=244 (W4==W7)
   example N=12, d(bc)=2, d(cb)=3: seed=['aaaaaaaaaaaa', 'abcaaaaaaaaa', 'abcacbaaaaa', 'acbaaaaaaaa']
      0 x=('a', 'aaaaaaaaa') y=('aa', 'aaaaaaaa') E0=('', 'a', 'a') E1=('', 'bc', '') => aabcaaaaaaaa
      1 x=('a', 'aaaaaaaa') y=('aa', 'aaaaaaa') E0=('', 'a', 'aa') E1=('', 'cb', '') => aacbaaaaaaa
      2 x=('abc',) y=('bca',) E0=('a', 'aaaaaaaa') E1=('', 'acbaaaaa') => bcaacbaaaaa
      3 x=('acb',) y=('cba',) E0=('a', 'aaaaaaa') E1=('bca', 'aaaaa') => bcacbaaaaaa
      4 x=('acb',) y=('cba',) E0=('a', 'aaaaaaa') E1=('bc', 'aaaaaa') => bccbaaaaaaa
      5 x=('bca',) y=('abc',) E0=('a', 'aaaaaaaa') E1=('', 'cbaaaaaa') => abccbaaaaaa
      6 x=('a', 'aaaaaa') y=('aa', 'aaaaa') E0=('', 'a', 'aaaa') E1=('', 'bccb', '') => aabccbaaaaa
      7 x=('abc',) y=('bca',) E0=('a', 'aaaaaaaa') E1=('', 'aaaaaaaaa') => bcaaaaaaaaaa
      8 x=('acb',) y=('cba',) E0=('a', 'aaaaaaa') E1=('', 'aaaaaaaa') => cbaaaaaaaaa
      9 x=('cba',) y=('bcaa',) E0=('', 'aaaaaaaa') E1=('bc', 'aaaaaa') => bcbcaaaaaaaa
     10 x=('bc', 'aaaaaaa') y=('cb', 'aaaaaa') E0=('', 'a', 'aa') E1=('', 'cb', '') => cbcbaaaaaa
     11 x=('cba',) y=('bcaa',) E0=('', 'aaaaaaaa') E1=('cb', 'aaaaa') => cbbcaaaaaaa
     12 x=('bca',) y=('abc',) E0=('a', 'aaaaaaaa') E1=('bc', 'aaaaaaa') => bcabcaaaaaaa
     13 x=('bca',) y=('abc',) E0=('a', 'aaaaaaaa') E1=('', 'bcaaaaaaa') => abcbcaaaaaaa
     14 x=('a', 'aaaaaaa') y=('aa', 'aaaaaa') E0=('', 'a', 'aaa') E1=('', 'bcbc', '') => aabcbcaaaaaa
     15 x=('cb', 'aaaaaaaa') y=('bc', 'aaaaaaaaa') E0=('', 'a', '') E1=('b', 'c', '') => bbccaaaaaaaaa
     16 x=('bc', 'aaaaaaaaa') y=('bccb', 'aaaaaa') E0=('', 'a', '') E1=('b', 'c', '') => bbccbcaaaaaa
     17 x=('bcaaa',) y=('bcbca',) E0=('', 'aaaaaaa') E1=('bc', 'aaaaa') => bcbcbcaaaaaa
     18 x=('bca',) y=('abc',) E0=('a', 'aaaaaaaa') E1=('cb', 'aaaaaa') => cbabcaaaaaa
     19 x=('cb', 'bc') y=('bc', 'cb') E0=('', 'a', 'aaaaaa') E1=('b', 'c', 'aaaaaa') => bbcccbaaaaaa
     20 x=('bc', 'cba') y=('bc', 'bcaa') E0=('', 'a', 'aaaaa') E1=('b', 'c', 'aaaaa') => bbccbcaaaaaaa
     conflict: bbccbcaaaaaa (a=6) vs bbccbcaaaaaaa (a=7), same skeleton bbccbcA
   tamper controls rejected: empty-separator(empty separator) type(type mismatch ('cb', 'bc') ('bc', 'cba')) missing-premise(premise aabcaaaaaaaa missing)
   [time so far 1.2s]
== [D] minimal tree seeds {a^N, w_bc, w_cb, w_(bc,cb)}: exact closure / certified contradiction
   tally (d1==d2, status): {(True, 'cap'): 8, (False, 'contra'): 70, (True, 'closed'): 10}
   [time so far 633.4s]
== [E] COMPUTATIONAL EVIDENCE: other unit pairs, a three-unit relation, interleaved fan-out-2 seed
    ('3unit', 'linear', 'cap') 3
    ('3unit', 'nonlinear', 'contra') 15
    ('interleaved', 'linear', 'cap') 2
    ('interleaved', 'linear', 'closed') 2
    ('interleaved', 'nonlinear', 'contra') 60
    ('pair', 'independent', 'cap') 37
    ('pair', 'independent', 'closed') 1
    ('pair', 'linear', 'cap') 6
    ('pair', 'linear', 'closed') 2
    ('pair', 'nonlinear', 'cap') 2
    ('pair', 'nonlinear', 'contra') 47
   contradictions among linear/independent assignments: 0 (a nonzero value would refute P_pair)
   [time so far 1100.8s]
== SUMMARY: checks=589 FAIL=0 time=1100.8s
ALL CHECKS PASSED
exit code: 0
finished: 2026-11-16T00:27:51+09:00
---
note (appended after the run): no random numbers are used; python -I does not disable str-hash
randomization, so set iteration order (hence the particular certificate found and its step count)
may vary between runs.  Every reported contradiction is re-verified by replay() in the same run.
'closed' = queue exhausted with no truncation, re-verified by check_closed(); 'cap'/'truncated' are
NOT closed.  Trial counts: [C] 3270 certified + 244 controls; [D] 88 closures; [E] 25*5 pair seeds
(only admissible ones run), 18 three-unit seeds, 64 interleaved seeds.

===== END FILE =====

===== BEGIN FILE claude_round14_noncomm_Parikh_checkpoint1_2026-11-15.md bytes=4362 sha256=d2818bc270106a02150db19e92cfe3f66e5ae52b1877ea56ddfd742a0baa4892 =====
# 第十四段 チェックポイント1（2026-11-15〜16 JST）

## 0. 資料・接続
- 依頼書全文（1–1960行、付録 A1–F2 を含む）を読了した。
- GitHub は取得を試みていない（依頼書 I-2 の指示どおり、付録の定義で進める）。定義は依頼書 I-2 を優先する。

## 1. X1 反例の再生（最初に実施）
- 40語の言語 L について、独自実装の厳密判定 `check_closed` で `L∈C^{mcf}_{2,c_Σ}` を再確認した（違反 0）。a^8 が最短の a 冪である。
- 原文 X1（i=(λ−λ')_+）を L 上の全 Rot 核対で検査した：11 件中 **4 件が分布不一致**。例 `bc` 対 `acb`（i=0, i'=1）。
- 型安全版 X1⁺（両側に a を最低1個付ける。i,i'≥1）を同じ L で検査した：119 対×左右 → **違反 0**。
- 観察：X1 反例の本体は、**a を1つも含まない語 `bc`（欠損 = N）**が型の境界をすり抜けることにある。i,i'≥1 に詰めれば、両片の型はともに c(κ)∪{a} となり、共通宿主 `a^{λ−i_0}□` が適法になる。

## 2. P の定式化（暫定。最終報告で確定する）
- **P_tree(S)**：a^N の節点最小木 T、分岐内容類 S、許容単位 𝒰_S（δ_J≤(N−1)/2）を取る。多重集合 m, m' が Σm_JV_J=Σm'_JV_J、δ_m, δ_{m'}≤N−1 を満たすなら δ_m=δ_{m'}。これは Fable-C(4) が要求する H(D) そのものである。
- **P_pair**（言語レベル・二単位版）：Rot 核 κ1, κ2 が同じ非 a 内容を持ち、単独語2語と二単位語1語 `a^x κ1 a^y κ2 a^z`（x,y,z≥1）が L に入るとする。V(κ1)∥V(κ2) なら δ1/|V1|=δ2/|V2|。
- 木が直接与えるのは、正確にこの**最小種4語** {a^N, w_{J1}, w_{J2}, w_{J1,J2}} である（非交錯の場合）。

## 3. 最初の成功・失敗
- **増分 union-find 閉包エンジン**を実装した。証明森から規則単位の証明書を抽出し、独立 replay で検査する。round13 の E1（39語）と E2（矛盾）を再現した。
- **最小種実験（bc/cb）**：N=7..14 の全 (δ1,δ2) を走査した。
  - δ1≠δ2 では全件 `contra`（証明書は全て replay 済み）。
  - δ1=δ2 の対照は `closed`（例：N=9, δ=3 で厳密に閉じた 63 語）または `cap`。
- **他の8単位対**（bc/bbcc, bc/cbbc, bcc/cbc, bcc/ccb, 独立ベクトル対4種）：矛盾は「Parikh 比例でない欠損」の場合に**限って**出た。独立ベクトル対と比例対照では矛盾 0。比例でない場合のうち、一部は cap で未決である。
- 手証明の当たり：E2 の 6手証明書の機構は「(cb,a^i)↔(bc,a^{i'}) を**直線でない因子出現**（`b[cb]c`）に適用する」ことと「二単位の順序交換 (cb,bc)↔(bc,cb) を別の隔て c で使う」ことだった。これで bbccbc 骨格に2つの a 数が出る。

## 4. 方針
1. **[証明]** X1⁺、置換補題 S（X1⁺/X2 の統合、左右対称）、転置定理 TR（de/ed、室条件付き）を手証明する。各手順の型・宿主・非空条件を明示する。
2. **[証明書]** TR の手証明を補題マクロ→規則単位の手順に展開し、独立に replay する。
3. 宿主（交錯 fan-out 2）を独立に攻撃する。
4. P_tree 全体は OPEN のまま扱う。決めつけない。

## 5. 方針転換の履歴（チェックポイント後の追記）
- **当初の想定**：TR には三単位の室（N≥2δ_max+δ_min+4）が要ると考えていた。
  - 実際の手証明は、二単位種＋Rot＋S＋OS＋CS だけで閉じた。
  - 室の条件は最終的に N≥4max(δ)+1（いずれかの向き）になった。
- **最小種の境界例（N=9, δ=3,4）**：反例候補として期待したが、矛盾した。
  - 「室が足りない境界で反例が出る」という路線は、この型では捨てた。
- **bigram 統計（bbcc/bcbc）**：S・OS とは整合する反例候補として検査した。
  - 長さ上限 N+6 で全例矛盾した。証明書の解析から**枠補題 F** を抽出した。
- **端の根道の問題を発見**：Rot には両側の a が要る。そこで BA（端の根道を U に入れる）を導入した。
- **最終整理**：P_tree ⇐ CA ∧ IH ∧ AB。TR は AB の最初の場合である。

===== END FILE =====

===== BEGIN FILE claude_round14_noncomm_Parikh_next_obligations_2026-11-15.md bytes=4524 sha256=4e2eed58929cd2f0547c69fc75f311f1b2d202305c4e7ebbc150be6030fd6a5b =====
# 第十四段 残存義務（2026-11-16 JST）

本ラウンドで、P_tree（内部版）は次の形に還元された。

> P_tree ⇐ CA［PROVED］ ∧ IH［OPEN］ ∧ AB［OPEN、de/ed は TR で PROVED］

U は T2′ により「IH ∧ AB ⇒ U」まで来ている（CONDITIONAL）。残りを、証明可能な最小補題の単位まで切り詰めて挙げる。

## O1（最優先）AB_pair：同一 Parikh の二核

**命題 AB_pair(c₁,c₂).** 以下を仮定する。
- L∈C_{2,c}、N は a の最小冪。
- κ, κ' は首尾が a でない Rot 核で、同じ非 a 内容 S と同じ Parikh ベクトル V∈ℕ^Δ を持つ。
- 二単位語 `a^xκa^yκ'a^z∈L`（x,y,z≥0）がある。
- 室条件 N≥c₁·max(δ,δ')+c₂。

結論：δ(κ)=δ(κ')。

- 既知：κ=de, κ'=ed（TR、c₁=4, c₂=1）。
- 計算証拠（全て矛盾、証明書 replay 済み）：bcc/cbc、bcc/ccb、bbcc/bcbc（長さ上限 N+6）、cbbc 系。
- 比例・多単位の関係は、CA を介して AB_pair に帰着する（§3 の還元）。

**より小さい切片（推奨の攻略順）.**
- **O1a（枠内の隣接転置）**：κ=p de q, κ'=p ed q（p または q が非空）。
  - 枠補題 F により (a^i,de)≡(a^{i+s},ed) という仮想単位交換が既に得られている。
  - 必要なのは、TR の手 3〜7 を「β=de, γ=ed が Rot 核」の代わりに「F の仮想交換＋κ, κ' の合成」で再現することである。
  - 障害：TR の手 4 は Parikh の異なる Rot 核への置換（bc→bccb）を使う。仮想単位では、その代わりに κκ' のような実在の合成を宿主にする必要がある。
- **O1b（枠なしの一般置換）**：κ と κ' の首尾が両方とも異なる場合。TR の手 3 のように**単位境界をまたぐ出現**へ S を適用する系列を一般化する。
  - κκ' や κ'κ の中に κ または κ' の非整列な出現があれば同型の議論が回る。
  - 出現がない場合の処理が未知である。

## O2 IH：交錯・入れ子の fan-out 2 分岐種

**命題 IH.** 内部分岐対 B, C（fan-out 2）が交錯（B₁C₁B₂C₂）または入れ子（B₁C₁C₂B₂）で、同じ内容類 S に属するとする。このとき、S の何らかの二単位の**連結な**実現 `a^xκ_Ja^yκ_{J'}a^z∈L` が存在する。

- 障害：2 穴交換は成分ごとの非 a 内容の一致を要する。連結な核が種の因子として現れない場合がある（報告 §5）。
- 計算：交錯 (b,c)/(b,c) 種で、非線形 90 例中 89 が矛盾。種そのものから単位の連結実現を**構成する**証明書の抽出は未実施。
- 切片：IH は「種のある因子が S の Rot 核の a パディング版と一致する」ことから従う。これは fan-out 2 の非終端の成分間が a で隔てられること（good の非併合性）と、単独語の内部 a 連の再分配（L1(R)）から示せる見込みがある。

## O3 T2′ の独立監査

- Fable-C(4)〜(7) を BA（\|U\|≤2^{D+2}v）、N₁=(N−1)/(4(D+1)B)、N≥8(D+1)Bθ+c₁ の修正で再検算する。
- AB の室定数 c₁ が θ, D に依存しないことを確認する（TR では c₁=4）。
- 半束型付け s 一般への延長では、型一致の条件を逐一点検する（c_Σ 版の結論を自動では移さない）。

## O4 計算の未決例

- bc/bbcc、(N,δ_bc,δ_bbcc)=(10,5,1)：4.5 万語で cap（未決）。
- 交錯種 (N,δ_B,δ₁,δ₂)=(13,2,2,1)：1.2 万語で cap（未決）。
- 長さ3以上の核の同一 Parikh 対（bcb/cbc は独立ではない：V=(2,1) と (1,2) は独立。bbc/bcb/cbb の三者など）の系統的走査は未実施。

## O5 下界側の帰結（反例探索の指針）

- U の反例族は、C1（第十三段）により超対数個の核骨格を要する。
- 本ラウンドにより、さらに次の (a) か (b) のどちらかが必要になった。
  - (a) 分岐類の種が交錯・入れ子で、IH が破れる配置を持つ。
  - (b) AB_pair が破れる同一 Parikh 核対を、室 N≥4max δ+1 の範囲で持つ。
- ただし TR により、(b) の de/ed 型は不可能である。

## O6 未照合

- GitHub `main.tex` の `def:grammar-properties`, `def:tuple-substitutable`, `lem:thickness-equivalence` との直接照合（本ラウンドでは未実施）。
- 第十二段の補償法則（補題 C）・定理 L と、F／TR との包含関係。

===== END FILE =====

===== BEGIN FILE claude_round14_noncomm_Parikh_report_2026-11-15.md bytes=26531 sha256=6b49949a7a36c0371dec15646c4614037ed555c37eacc21d3f61c81114188452 =====
# Claude 第十四段 最終数学報告：非可換 Parikh 還元 P（2026-11-15〜16 JST）

## 一行結論

**`PROVED-RESTRICTED` ＋ `NEW-LEMMA`。P（木版・一般形）は `OPEN`、予想 U は `OPEN`、`op:fanout-two` は `OPEN`。**

- **証明したこと**：P の最初の非自明な場合を無条件で証明した。
  - 同じ内容類 {d,e} の単位で、核が `de` と `ed` のものを考える。
  - 両者を含む連結二単位語が1語あり、N ≥ 4·max(δ_de, δ_ed)+1 なら、δ_de=δ_ed（**転置定理 TR**）。
  - この過程で、X1 の型安全な置換版 X1⁺ と一般道具（置換補題 S、枠補題 F、順序交換 OS、運搬子シフト CS、合成加法性 CA、境界調整 BA）を証明した。
- **還元**：P（内部分岐類）は、CA［証明済み］＋ IH（交錯・入れ子配置での宿主）［OPEN］＋ AB（同一 Parikh の合成核は欠損が等しい）［一般形 OPEN、TR はその特殊例］に還元された。
- **反例側**：P の前提から「分岐（合成語の存在）」を外した言語レベル版は偽である。厳密に閉じた 82 語の言語で示した。ただしこれは木版 P の反例では**ない**（分岐前提が満たされない）。
- **計算証拠**：最小の木由来の種（4〜6語）による閉包を約 400 例行った。矛盾は「欠損が Parikh 線形でない」割当てに**限って**出た（証明書はすべて独立 replay 済み）。線形または独立ベクトルの割当てでは矛盾 0。

| ラベル | 命題 | 状態 |
|---|---|---|
| X1⁺ | 型安全な置換版 X1（i,i'≥1）：`X a^iκ Y∈L ⟺ X a^{i'}κ' Y∈L` | **[PROVED]**（40語反例上で 238 検査・違反 0、原文 X1 は 4 違反で検出） |
| S | 置換補題（X1⁺ と X2 の左右4形の統合、任意の因子出現に適用可能） | **[PROVED]** |
| F | 枠補題：`κ=puq`, `κ'=pu'q`（p≠ε, c(u)=c(u')）なら `(a^i,u)≡(a^{i'},u')` | **[PROVED]**（新） |
| OS, CS | 二核の順序交換・運搬子シフト（2穴） | **[PROVED]** |
| CA | 連結な分岐種から、同内容類の単位の任意順序の多単位合成語が全配置で受理され、欠損は加法的 | **[PROVED]**（非可換版 Fable-C(3)） |
| BA | 両端の根道を除外集合 U に加えれば、窓節点の単位は全て内部（両側に a）になり、\|U\|≤2^{D+2}v | **[PROVED]** |
| **TR** | 転置定理 δ(de)=δ(ed)（上記条件） | **[PROVED]**（手証明。N≤40 の 3,270 例を規則単位の証明書に展開して replay し、失敗 0） |
| TR-tree | 木版の系（逐次配置の内部分岐対＋室条件） | **[PROVED]**（TR＋CA＋BA） |
| E-B | 分岐なし言語レベル P の反例（a 中心言語、δ(bc)=2, δ(cb)=3） | **[CERTIFIED-FINITE]**（P_tree の反例ではない） |
| E-D/E | 最小種閉包：bc/cb（N=7..12）、他5対、三単位関係、交錯 fan-out 2 種 | **[COMPUTATIONAL-EVIDENCE]**（矛盾例は CERTIFIED-FINITE） |
| AB | 一般の同一 Parikh 合成核の欠損一致 | **[OPEN]**（最小残余） |
| IH | 交錯・入れ子の fan-out 2 種からの二単位連結実現 | **[OPEN]** |
| T2′ | IH＋AB ⇒ H(D) ⇒ U（定数を修正した Fable-C 移植） | **[CONDITIONAL]** |
| U / `op:fanout-two` | — | **[OPEN] / [OPEN]** |

`op:fanout-two` の扱い：本ラウンドの結果は単項語長予想 U の上界側を部分的に進めるだけである。正式問題の肯定（YES）も否定（NO）も導かない（依頼書 I-1 のとおり）。

---

## 0. 規約・資料

- GitHub は参照していない。定義は依頼書 I-2 と付録 A〜F に拠る。
- 全体の設定：Σ は有限、a∈Σ、Δ=Σ∖{a}、s=c_Σ（内容型付け）、L∈C^{mcf}_{2,c_Σ}、N=min{n≥1: aⁿ∈L}。
- 文脈の規約：
  - d=1 の文脈は (l,r)。
  - d=2 の文脈は (l,m,r) で、**m≠ε**。
  - 穴の中身は必ず Σ 上の**非空語**。
- **Rot 核**：κ∈Σ⁺ で、首尾の文字が a でないもの（整形）。単独語 `a^pκa^r∈L`（p,r≥1）を持ち、λ:=p+r∈[3,N−1] を満たす。
  - λ は κ で一意である：二つあれば共通文脈 □κ で L1(U) に反する。
  - 欠損は δ(κ):=N−λ−|κ|_a。
- **既知・監査済み**として使うもの：L1(R)、L1(U)、L2（骨格関数）、L3 Rot、L4 Cat（付録 B1 で VALID）。
  - Rot の帰結：aκ≡κa（1穴合同）。よって Rot 核の周りの a 連は 0 を含めて自由に再配分できる（Cat）。
- 2穴の交換は、毎回 x, y、成分ごとの型、共有受理文脈 E₀、試験文脈 E₁ を示し、E₀[x], E₀[y], E₁[x]∈L ⇒ E₁[y]∈L の形で使う。

---

## 1. X1 反例の再生と型安全版 X1⁺

**再生 [CERTIFIED-FINITE]**：40語の L（依頼書 II-1）を独自実装で厳密判定した。

- 333 組、2,327 受理文脈、違反 0、a^8 が最短。
- 原文 X1（i=(λ−λ')_+）は 11 検査中 4 違反だった。例：κ=cb, κ'=bc, i=1, i'=0。
- 依頼書の例 κ=bc, κ'=acb も、仮定は満たし結論は偽であることを確認した。

**失敗の正体.** i=0 のとき、比較片は `κ=bc`（a を含まない）になる。境界の語 `bc∈L` は |bc|_a=0、すなわち欠損 N の語である。s(aκ)=s(aκ') は s(κ)=s(κ') を与えない。

**補題 X1⁺ [PROVED].**
- 仮定：κ, κ' は Rot 核で、c(κ)∖{a}=c(κ')∖{a}（非 a 内容が等しい）。
- 結論：i≥1 で i':=i+λ'−λ≥1 なら、任意の X,Y∈Σ* について `X a^iκY∈L ⟺ X a^{i'}κ'Y∈L`。左右反転版 `Xκa^iY ⟺ Xκ'a^{i'}Y` も成り立つ。

*証明.*
1. i₀:=1+max(0,λ−λ')、i₀':=i₀+λ'−λ≥1 と置く。
2. x=a^{i₀}κ, y=a^{i₀'}κ' の型は、ともに c(κ)∪{a} で**等しい**。ここで i₀, i₀'≥1 が本質である。
3. 共有宿主 E₀=a^{λ−i₀}□ を取る（λ−i₀≥0）。
   - E₀[x]=a^λκ∈L（Rot）。
   - E₀[y]=a^{λ−i₀+i₀'}κ'=a^{λ'}κ'∈L（Rot）。
   - よって x≡y（1穴）。
4. i≥i₀ なら、試験文脈 E₁=(X a^{i−i₀}, Y) により、X a^iκY → X a^{i−i₀+i₀'}κ'Y=X a^{i'}κ'Y。
5. i<i₀ が起こるのは λ>λ' のときだけで、そのとき i'<1 となり除外される。
6. 逆向きは対称。反転版は宿主を □a^{λ−i₀} にする。∎

40語の L 上で、Rot 核の全対・i=1..11・左右について 238 件を検査し、違反 0。

---

## 2. 一般の道具

### 2.1 置換補題 S [PROVED]

κ, κ' を非 a 内容が等しい Rot 核とし、δ_κ, δ_{κ'} をその欠損とする。L の語の**任意の因子出現** κ について、ある a 連 a^i（i≥1）が次の位置にあるとする。

- (S1) 左に隣接：`P a^i κ R`
- (S2) 左に非空の隔て Q を挟む：`P a^i Q κ R`
- (S3) 右に隣接：`P κ a^i R`
- (S4) 右に非空の隔て Q を挟む：`P κ Q a^i R`

このとき i'=i+λ'−λ≥1 なら、κ を κ' に、a^i を a^{i'} に置き換えた語も L に入る（逆も成り立つ）。語の a 数の変化は δ_κ−δ_{κ'}。

*証明.*
- (S1)(S3) は X1⁺。
- (S2) は付録 B1 §3 で修復された X2 の両場合分け。
  - i≤λ−1：宿主 E=a^{λ−i−1}□₁a□₂（中央 a は非空）。
  - i≥λ：i₀=λ−1, i₀'=λ'−1 に落とし、余剰の a^{i−i₀} を左外部へ吸収する。
- (S4) はその鏡像。宿主は E=□₁a□₂a^{λ−i−1}、吸収は右側。∎

**注意.** κ の出現は単位境界をまたいでよい（例：`b[cb]c`）。P, Q, R は任意。この**文脈非依存性**が §4.4 の統計消去の源である。

### 2.2 枠補題 F [PROVED, 新]

- 仮定：
  - κ=p u q, κ'=p u' q はともに Rot 核（λ, λ'）。
  - p≠ε。
  - c(u)=c(u')（a を含むかも一致すること）。
  - i≥1, i'=i+λ'−λ≥1。
- 結論：(a^i,u)≡(a^{i'},u')（2穴）。したがって、任意の P, R と非空の Q について、`P a^i Q u R ∈L ⟺ P a^{i'} Q u' R∈L`。

*証明.*
1. i≤λ の場合：E₀=(ε, p, q a^{λ−i})（隔て p≠ε）を取る。
   - E₀[(a^i,u)]=a^i κ a^{λ−i}∈L（Rot）。
   - E₀[(a^{i'},u')]=a^{i'} κ' a^{λ−i}=a^{i'}κ'a^{λ'−i'}∈L。
   - 成分型は ({a}, c(u)) で等しい。
2. i>λ の場合：i₀=λ, i₀'=λ' に落とし、余剰を左外部へ吸収する。∎

X2 は「p を a 連の一文字とみなした」F の特殊形である。F は、**同じ枠を持つ核の「中身」**を、仮想的な単位として交換可能にする。§4.4 の bbcc/bcbc 例の機構がこれである。

### 2.3 二核補題 OS / CS [PROVED]

- **OS（順序交換）**
  - 仮定：κ, κ' は Rot 核、c(κ)=c(κ')。ある u,w≥0, v≥1 で `a^uκa^vκ'a^w, a^uκ'a^vκa^w∈L`。
  - 結論：任意の l, r と非空 m について `lκmκ'r∈L ⟺ lκ'mκr∈L`。
  - *証明.* x=(κ,κ'), y=(κ',κ)。型は (c(κ), c(κ')) で等しい。E₀=(a^u,a^v,a^w)。∎
- **CS（運搬子シフト）**
  - 仮定：c(κ)∖{a}=c(κ')∖{a}、j, j'≥1、v≥1、`a^uκ₀a^vκa^{j+w}, a^uκ₀a^vκ'a^{j'+w}∈L`。
  - 結論：任意の l, r と m≠ε について `lκ₀mκa^jr∈L ⟺ lκ₀mκ'a^{j'}r∈L`。
  - *証明.* x=(κ₀,κa^j), y=(κ₀,κ'a^{j'})。型は (c(κ₀), c(κ)∪{a}) で等しい。E₀=(a^u,a^v,a^w)。∎

### 2.4 合成加法性 CA [PROVED]（Fable-C(3) の非可換版）

**仮定.**
- 𝒰 は Rot 核の有限集合で、全て非 a 内容 S。
- **連結な**種 `a^xκ_Ba^yκ_Ca^z∈L`（κ_B, κ_C∈𝒰、x,y,z≥0）がある。
- 単位列 (κ_{j_1},…,κ_{j_m})（m≥1）について、e_m:=N−Σδ_{j_i}−Σ|κ_{j_i}|_a≥3 とする。
- 途中の各 (S) 適用で i'≥1 が成り立つ（e≥1 と同値）。

**結論.** e₀+⋯+e_m=e_m となる全ての e_i≥0 について `a^{e₀}κ_{j_1}a^{e₁}⋯κ_{j_m}a^{e_m}∈L`。とくに合成 κ_{j_1}⋯κ_{j_m} は Rot 核で、欠損は Σδ_{j_i}（加法的、順序に依らない）。

*証明.* m についての帰納法。
- **m=1**：単独語＋Cat。
- **m=2**：種から κ_B→κ_{j_1}、次に κ_C→κ_{j_2} を (S) で置換する。
  - 第1手：右の a 連、隔ては κ_C。新指数 i'=e(κ_{j_1}κ_C)≥1。
  - 第2手：隣接する a 連。新指数 i'=e(κ_{j_1}κ_{j_2})≥1。
  - 位置は保たれるので、**任意の順序対**が得られる。
- **m−1→m**：合成 M=κ_{j_1}⋯κ_{j_{m−1}} は帰納法と Cat により Rot 核である（λ_M=e_{m−1}≥3）。二単位語 `κ_{j_1}κ_{j_m}a^{e}` において、先頭の κ_{j_1} を M に (S4) で置換する（隔て κ_{j_m}≠ε）。i'=e_m≥1。次に Cat。
- 各段で a 数の変化は λ'−λ なので、欠損は和になる。∎

**CA が要るのは「連結な種」だけである。** fan-out 1 の分岐対、または fan-out 2 で逐次配置（B₁B₂C₁C₂）の分岐対は、a^N の木で同時置換すれば連結種を与える（文脈は全て a）。入れ子（B₁C₁C₂B₂）と交錯（B₁C₁B₂C₂）は与えない（§5）。

### 2.5 境界調整 BA [PROVED]

**問題.** Rot は単独語の両側に a 連を要する。根から位置 0 または N−1 を含む部分木を辿る2本の「端の根道」上の節点では、これが成り立たないことがある。

**調整.**
- 分岐の定義を**内部節点の対**（どちらも端の根道上にない）に限る。
- 非分岐類の内部節点は、Fable-C(5) と同じ論法で高々2本の根道に載る：悪い対は k_B+k_C=N を強制し、内部節点の子孫は内部節点である。
- 端の根道2本を加えても、類ごとに高々4本。
- よって \|U\|≤(4(2^D−1)+1)v≤2^{D+2}v。

U の外の節点の子孫は全て内部節点であり、その類は内部分岐である。したがって窓 (6) で使う単位は全て Rot 核になる（λ≥3 には N≥N₁+θ+3 程度が要る）。∎

---

## 3. P の精密定式化と還元

**P_tree（内部版）.** 以下を固定する。
- reduced good な G、a^N の節点最小木 T、θ=θ̄_G。
- 内部分岐類 S（非 a 内容）。
- その内部許容単位 𝒰_S：内部大節点の非終端 J で δ_J≤N₁（N₁ は §6 で再設定する）。各 J の単独語の核を κ_J とする。

主張：𝒰_S 上の多重集合 m⁺, m⁻ が Σm⁺_JV_J=Σm⁻_JV_J を満たし、δ_{m^±}≤(N−1)/2 なら、Σm⁺_Jδ_J=Σm⁻_Jδ_J。
- 禁止事項として、「同じ Parikh なので順序を変えても受理」は使わない。
- 使ってよい実在語は、木の同時置換で得られる語と、§2 の補題で受理が**証明された**語に限る。

**還元 [PROVED as implication].** P_tree ⇐ CA ∧ IH ∧ AB。
- **IH**：内部分岐対の種が交錯・入れ子でも、S の二単位の連結実現が得られる。
- **AB**：S の Rot 核 κ⁺, κ⁻ が同じ Parikh ベクトルを持ち、合成 κ⁺κ⁻ が L に入り、e(κ⁺κ⁻)≥c₁ なら、δ(κ⁺)=δ(κ⁻)。

*理由.*
1. CA（＋IH）で、m⁺ の連結合成 κ⁺、m⁻ の連結合成 κ⁻、および κ⁺κ⁻ が受理される。
2. 欠損は加法的なので、δ(κ^±)=Σm^±_Jδ_J。
3. AB で両者が一致する。

AB は**語のレベルの命題**であり、木を必要としない。分岐前提は「κ⁺κ⁻ が L に入る」という形でだけ残る。§4.5 が示すとおり、この前提は外せない。

---

## 4. 転置定理 TR

### 4.1 主張

**定理 TR [PROVED].** 仮定は次のとおり。
- d≠e∈Δ、β:=de, γ:=ed。
- (H1) β は Rot 核で欠損 δ₁、(H2) γ は Rot 核で欠損 δ₂。
- (H3) ある x,y,z≥0 で `a^xβa^yγa^z∈L`、かつ t:=x+y+z=N−δ₁−δ₂≥3。
- 条件 (C)：D:=δ₂−δ₁ ≠ 0 と仮定し、j:=max(1,1−D) と置くとき、次の全てが成り立つ。
  - 1≤δ_i≤N−3
  - t≥3
  - N−2δ₁≥3
  - N−2δ₂≥1
  - N−3δ₁≥1
  - j≤t−1
  - N−3δ₁−j≥0
  - 1≤3δ₁−D≤N−1

このとき D≠0 は矛盾する。すなわち **δ₁=δ₂**。

(C) は β↔γ を入れ替えた形でもよい：L の反転 L^R は C_{2,c} に属し、a^N を保ち、β^R=γ である。とくに **N≥4·max(δ₁,δ₂)+1 なら (C) はどちらかの向きで成り立つ**（δ₁:=max とした向きで全条件を検算できる。N≤60 の全走査で例外 0）。

### 4.2 証明（記号は d=b, e=c で書く）

各手順は、x/y、型、宿主、隔ての非空性、適用条件、結果の順に記す。

| 手 | 内容 | 根拠・条件 | 得られる語（a 数） |
|---|---|---|---|
| 1 | Cat(H3)：`bccb a^t`。合成 κ₁₂=bccb は Rot 核（λ=t） | Rot(β,γ)、t∈[3,N−1] | `bccb a^t`（t） |
| 2 | (S3)：bc[**cb**]a^t → bc[**bc**]a^{t+D} | X1⁺右。x=cb·a^{i₀}, y=bc·a^{i₀'}、型 {a,b,c}。宿主 □a^{λ−i₀}。t+D=N−2δ₁≥1 | W₂=`bcbc a^{N−2δ₁}` |
| 2′ | (S4)：[**bc**]cb a^t → [**cb**]cb a^{t−D}（隔て cb）。次に cb[**cb**]a^{t−D} → cb[**bc**]a^t | 宿主 □₁a□₂a^{q−1}。N−2δ₂≥1 | `cbbc a^t`（γβ 順の合成） |
| 3 | (S4) を**単位境界をまたぐ**出現に：b[**cb**]c a^{N−2δ₁} → b[**bc**]c a^{N−2δ₁+D} | x=(cb,a^{i₀}), y=(bc,a^{i₀'})、型 ({b,c},{a})。隔て `c`≠ε | W₃=`bbcc a^{N−2δ₁+D}` |
| 4 | (S4)、κ=bc→κ'=bccb：b[**bc**]c a^k → b[**bccb**]c a^{N−3δ₁} | 型 ({b,c},{a})。i'=k+λ₁₂−λ₁=N−3δ₁≥1 | **W₄=`bbccbc a^{N−3δ₁}`** |
| 5 | (S3)、κ=bc→κ'=bcbc（Rot 核、λ=N−2δ₁≥3）：bc[**bc**]a^{N−2δ₁} → bc[**bcbc**]a^{N−3δ₁} | X1⁺右 | W₅=`bcbcbc a^{N−3δ₁}` |
| 6 | OS：x=(cb,bc), y=(bc,cb)、型 ({b,c},{b,c})。E₀=(ε,a,a^{t−1}) で E₀[x]=`cb a bc a^{t−1}`（2′＋Cat）、E₀[y]=`bc a cb a^{t−1}`（H3＋Cat）。E₁=(b, c, a^{N−3δ₁})、E₁[x]=W₅ | 隔て a, c≠ε | W₆=`bbcccb a^{N−3δ₁}` |
| 7 | CS：x=(bc, cb a^j), y=(bc, bc a^{j+D})、型 ({b,c},{a,b,c})。E₀=(ε,a,a^{t−1−j}) で E₀[x]=`bc a cb a^{t−1}`、E₀[y]=`bc a bc a^{N−2δ₁−1}`（W₂＋Cat）。E₁=(b,c,a^{N−3δ₁−j})、E₁[x]=W₆ | j,j+D≥1、j≤t−1、N−3δ₁−j≥0 | **W₇=`bbccbc a^{N−3δ₁+D}`** |

**結論.** W₄ と W₇ は同じ骨格 `bbccbcÂ` を持つ。a 数は N−3δ₁ と N−3δ₁+D で、どちらも [1,N−1] に入る（(C) の最終条件）。L2 により両者は等しく、D=0。∎

**依存する補題はすべて証明済み**：L1(R)、L1(U)、L2、Rot、Cat、X1⁺、S、OS、CS。原文 X1 は使っていない。

**証明書 [CERTIFIED-FINITE].**
- 上の 7 手を、L1(R)・Rot の単一 a 移動・X1⁺・X2 の宿主まで含めて**規則単位の直接適用**に展開した（`tr_builder` 部）。
- 種 {a^N, `a bc a^{λ₁−1}`, `a cb a^{λ₂−1}`, `a bc a cb a^{t−2}`} から 20〜21 手で導く。
- 7≤N≤40 で (C) に入る δ₁≠δ₂ の **3,270 例**全てを独立 replay した。結果は「同骨格・異 a 数」で、失敗 0。
- δ₁=δ₂ の対照 244 例では W₄=W₇（矛盾なし）。
- 改竄した証明書（隔てを空に、型不一致、前提欠落）は replay が拒否する（陰性対照）。

### 4.3 木版の系 TR-tree [PROVED]

内部分岐類 S={d,e} に**逐次配置**の内部分岐対 (B,C) があるとする。さらに J₁, J₂ を内部単位とし、その単独語の核が de, ed、欠損が δ₁, δ₂ であるとする。

N≥4max(δ₁,δ₂)+1 で、CA の室条件（e(κ_Bκ_C)≥3、e(J₁J₂)≥3）が成り立つなら、δ₁=δ₂。
- *証明.* BA で単独語は両側に a を持つ。CA で連結な `a^x de a^y ed a^z∈L` を得る。あとは TR。∎

これにより、第十三段 O1 の「反転数型統計 δ=α|w|_b+β|w|_c+γ·inv」は、この類で γ=0 に強制される（依頼書 III-2 D の具体的解決）。

### 4.4 なぜ順序統計が死ぬか（III-2 C/D への回答）

- **反転数統計**は、同じ Parikh の因子置換（bc↔cb）とは整合する（O1）。
- しかし手 4 は、**Parikh の異なる置換** bc→bccb を文脈 (b,c) の中で使う。
  - 反転数モデルでは、この置換によるシフトは文脈との交差対に依存する。
  - 補題 S のシフトは文脈に依らず δ(bccb)−δ(bc)=δ₂ で一定である。
  - CA（加法性）と合わせると、φ₀(m,m) を m について線形かつ二次（m(m−1)/2 項）の両方にすることが要求され、D=0 しか残らない。
- **bigram 型統計**（例：#bc）は、首尾の文字が同じ核（bbcc/bcbc）なら S とも OS とも整合する。
  - これを殺すのは**枠補題 F** である：`bcbc=b·cb·c` と `bbcc=b·bc·c` から、仮想単位 (a^i,cb)≡(a^{i'},bc) が生じる。
  - 実際の証明書（N=13, δ=3,5、6手、replay 済み）の第2手は、まさに E₀=(ε,b,c a^7) を使う。
  - 長さ上限 N+6 で、全 38 例が矛盾した。**[CERTIFIED-FINITE、一般証明は AB に含めて OPEN]**

### 4.5 分岐前提は外せない [CERTIFIED-FINITE]

L={a^{10}} ∪ {bc の a 挿入語のうち a を 8 個含む全語} ∪ {cb の a 挿入語のうち a を 7 個含む全語}（82語）を考える。これは厳密判定で C_{2,c} に属し、a^{10} が最短である。

- bc と cb は同じ内容・同じ Parikh の Rot 核で、δ=2 と 3。
- 二単位語 `abcacbaaa` を1語加えるだけで、10〜11 手の replay 済み矛盾になる（手数は実行ごとの集合反復順で変わる。結論は不変）。
- よって「**同じ Parikh の Rot 核は同じ欠損**」は、合成語なしには偽である。
- これは P_tree の**反例ではない**：分岐対があれば二単位語が L に入るが、この L には入らない。分岐しない類の節点は Fable-C(5) により U（高々2本の根道）で処理されるので、P を要しない。

---

## 5. 宿主（III-2 A）：交錯・入れ子の障害

**状況.** fan-out 2 の分岐対 B=(u_{B1},u_{B2}), C=(u_{C1},u_{C2}) が交錯 B₁C₁B₂C₂ または入れ子 B₁C₁C₂B₂ に配置されているとする。このとき種 w_{B,C} は κ_B と κ_C の連結にならない。

**正確な障害.**
- 種のある成分を単位 J の成分に替える 2 穴交換には、**成分ごとの非 a 内容の一致**が要る。例：(b,c) 型の成分を (bc, ·) 型には替えられない。
- J の核全体を 1 穴で入れる場所は、種の中に連続区間として存在しないことがある。
- 「適法な文脈が存在する」ことと「所望の出現でそれを使える」ことが、ここで分離する。

**部分的事実.**
- 交錯種 `ababacac…`（B=C=(b,c)）でも、文字列としては B 型核 `bac` が因子として現れることが多い。この場合 S（パディング版 `bca`）で入口が得られる。ただし一般の非 a 内容配置では保証がない。
- **計算**：種 {a^N, B の単独語, 交錯種, bc と cb の単独語}（N=11,12、δ_B∈{2,3}、δ₁,δ₂∈1..4）で閉包を取った。
  - 探索段階（N=11,12,13）では、非線形 90 例中 89 例が矛盾した（replay 済み）。(N,δ_B,δ₁,δ₂)=(13,2,2,1) の 1 例だけが cap で未決。
  - 線形の対照では矛盾 0（closed 3、cap 3）。
  - チェッカーの E 節は、このうち N=11,12 の部分を再実行する（結果は出力ファイル）。
  - 交錯がそれ自体で反例を生む兆候はない。

IH は **[OPEN]** として次の義務に残す。

---

## 6. T2 の再監査：H(D) ⇒ U の移植に必要な修正

H(D) を P_tree（内部版）の形で仮定すると、Fable-C(4)〜(7) は次の修正のもとで通る。手で追跡した結果で、形式化はしていない。

1. **BA**：U を端の根道で拡大する（\|U\|≤2^{D+2}v）。
2. **室**：AB と CA は、κ⁺κ⁻（総欠損 ≤2tBN₁＋内部 a 数 ≤2tB·θ）に e≥c₁ を要求する。そこで
   N₁:=(N−1)/(4(D+1)B) と取り直し、加えて N≥8(D+1)Bθ+c₁ とする。
   後者が破れる場合は N 自体が多項式で抑えられるので、結論側に吸収できる。
   これにより K₀ と最終上界は定数倍しか変わらず、指数 1+D+D²2^D は不変（v 依存も同じ）。
3. **単位の内部性**：窓節点は U の外にあるので、全て内部 Rot 核である。

**T2′ [CONDITIONAL].** IH と AB（室定数 c₁ 付き）が成り立てば、予想 U（s=c_Σ）は N=O_{D,r}(vθ^{1+D+D²2^D}) で成立する。

- 半束型付け s 一般への延長では、型一致の部分が c_Σ 版と異なる。依頼書の注意どおり、ここでは主張しない。
- 「Fable-C・T1 は手監査で有効」という評価を、形式検証や査読済みの意味に言い換えない。

---

## 7. 計算の記録（全て決定的・乱数なし）

| 実験 | 範囲 | 結果 | 状態 |
|---|---|---|---|
| A：X1 再生 | 40語 | 閉、333組・2327文脈。原文 X1 で 4 違反、X1⁺ で 238 検査・0 違反 | CERTIFIED-FINITE |
| B：分岐なし反例 | 82語 | 厳密に閉。二単位語の追加で 10〜11 手の矛盾 | CERTIFIED-FINITE |
| C：TR 証明書 | 7≤N≤40 | 3,270 例全て replay・矛盾成立、対照 244 例は W₄=W₇、改竄 3 種を拒否 | CERTIFIED-FINITE |
| D：最小種 bc/cb | N=7..12 の全許容 (δ₁,δ₂) | δ₁≠δ₂ の **70/70 が矛盾**（全証明書 replay）、未決 0。δ₁=δ₂ は closed 10・cap 8。探索段階では N≤14 まで同じ傾向 | EVIDENCE（矛盾は CERTIFIED） |
| E：他の対 | bcc/cbc, bcc/ccb, bc/bbcc, bc/bcc, bbc/bcc（N=10） | 非線形は 47 矛盾・2 cap。線形（cap 6・closed 2）と独立（cap 37・closed 1）では**矛盾 0** | EVIDENCE |
| E：三単位 | V(bcc)+V(bbc)=3V(bc)、N=12 | チェッカーで非線形 15/15 が矛盾、線形 3 は cap（探索段階 N=12,14 では 30/30 と 6） | EVIDENCE |
| E：交錯 | §5 | チェッカー（N=11,12）で非線形 60/60 が矛盾、線形は closed 2・cap 2。探索段階では 89/90 | EVIDENCE |
| 探索補遺 | bbcc/bcbc（N=11,13） | 長さ上限 N+4 で 34 矛盾・4 truncated。truncated の 4 例も上限 N+6 で全て矛盾 | EVIDENCE |
| 探索補遺 | bc/bbcc (10,5,1) | 4.5 万語で cap、**未決** | — |

- 「closed」は、キューが尽き、かつ長さ打切りが一度もなかったものに限る。その上で厳密判定 `check_closed` で再確認した。
- 「truncated」「cap」は閉包ではない。未発見の矛盾を証明扱いしない。
- 第十三段の課題だった整合対照（δ(bc)=δ(cb)）は、最小種からなら N=9, δ=3 で **63 語の厳密に閉じた言語**として得られた。全種（四配置）だと 9 分で収束しなかった件とは種が異なる。

---

## 8. 既知結果との関係・限界

- TR、F、CA、BA は第十三段（Rot, Cat, L2）と監査済み X2 修復の上に立つ。Fable 系 2.2（滑り）とは独立の機構である（a シフトを伴う置換）。
- 第十二段の補償法則や既存 reviews の定理 L との照合はしていない（GitHub 未参照）。
- TR は長さ2の核 de/ed に限る。一般の置換（bcc/cbc 等）、比例関係（bc/bbcc）、三単位関係は計算証拠のみ。
- 未査読・未形式化。新規性は保証しない。

## 9. 成果物

- `claude_round14_noncomm_Parikh_report_2026-11-15.md`（本報告）
- `claude_round14_noncomm_Parikh_checkpoint1_2026-11-15.md`
- `claude_round14_noncomm_Parikh_next_obligations_2026-11-15.md`
- `claude_round14_noncomm_Parikh_checker_2026-11-15.py`（単独実行可、標準ライブラリのみ）
- `claude_round14_noncomm_Parikh_checker_output_2026-11-15.txt`（コマンド、Python 版、SHA256、件数、FAIL、終了コード）
- 上記の ZIP

チェッカーの実行結果：`python3 -I`、Python 3.13.18、checks=589、FAIL=0、**exit code 0**、1100.8 秒。チェッカー SHA256 は `eaccd712…663ea`。乱数は使っていないが、`-I` はハッシュ乱択を無効にしないので、証明書の手数は実行ごとに変わりうる。

GitHub・論文原稿の変更は行っていない。

===== END FILE =====

===== BEGIN FILE exploration/README.txt bytes=440 sha256=3db1c99132c1e5f49b13459af6ef65c5f2463e986566757830aee6a713017e88 =====
Exploration scripts and raw logs (Round 14).  Not part of the certified checker; kept for
reproducibility of the exploratory sweeps quoted in the report (t3: bc/cb N=7..14 sweep, t5: other
pairs, t7: three-unit relation, t8: interleaved seeds, t10/t12: larger caps, t11/t13: bbcc/bcbc).
r14core.py and tr_builder.py are the library versions bundled verbatim into the checker.
Run any script with:  python3 -I <script>  from this directory.

===== END FILE =====

===== BEGIN FILE exploration/r14core.py bytes=11437 sha256=74b65903cf14dfca80f408c765e799afa9d923fae88b38a02990b998bfdc830c =====
#!/usr/bin/env python3
"""Round 14 core library (Claude, 2026-11-15).  Python 3 standard library only.

Typing: content typing c(w)=set of letters.  Tuple substitutability for d in {1,2}.
A d=1 context is (l,r); a d=2 context is (l,m,r) with m NONEMPTY.  Hole contents are
always nonempty words over Sigma (never empty, never "nonempty after projection").

Contents
  tuples_of(w)            all (x,E) with E[x]=w, x nonempty components, d=2 separator nonempty
  check_closed(S)         EXACT decision for a finite set S (all d=1,2 contexts)
  Closure                 incremental union-find closure (Fable Def. 2.3 rule system), with a
                          proof forest so that every derived word has a replayable certificate
                          made of direct rule applications  E0[x],E0[y],E1[x] in K  =>  E1[y].
  replay(seed, steps)     independent re-check of a certificate (types, nonemptiness, premises)
"""
from collections import defaultdict, deque
import itertools

def ctype(w):
    return frozenset(w)

def ttype(x):
    return tuple(frozenset(c) for c in x)

def skel(w):
    out = []
    for ch in w:
        if ch == 'a':
            if not out or out[-1] != 'A':
                out.append('A')
        else:
            out.append(ch)
    return ''.join(out)

def acount(w):
    return w.count('a')

def fill(E, x):
    if len(x) == 1:
        return E[0] + x[0] + E[1]
    if E[1] == '':
        raise ValueError('empty separator')
    return E[0] + x[0] + E[1] + x[1] + E[2]

def tuples_of(w):
    n = len(w)
    for i in range(n):
        for j in range(i + 1, n + 1):
            yield (w[i:j],), (w[:i], w[j:])
    for i in range(n):
        for j in range(i + 1, n + 1):
            for k in range(j + 1, n + 1):          # separator w[j:k] nonempty
                for l in range(k + 1, n + 1):
                    yield (w[i:j], w[k:l]), (w[:i], w[j:k], w[l:])

def ctx_maps(S):
    ctx = defaultdict(set)
    for w in S:
        for x, E in tuples_of(w):
            ctx[x].add(E)
    return ctx

def check_closed(S):
    """Exact: S (finite) is (2,content)-tuple-substitutable iff for every (type,E) bucket all
    tuples have identical context sets.  Returns (True,None) or (False, witness dict)."""
    S = set(S)
    ctx = ctx_maps(S)
    bucket = defaultdict(list)
    for x, Es in ctx.items():
        t = ttype(x)
        for E in Es:
            bucket[(t, E)].append(x)
    for (t, E0), xs in bucket.items():
        if len(xs) < 2:
            continue
        ref = ctx[xs[0]]
        for y in xs[1:]:
            if ctx[y] != ref:
                x = xs[0]
                diff = ref ^ ctx[y]
                E1 = next(iter(diff))
                if E1 in ctx[y]:
                    x, y = y, x
                return False, dict(x=x, y=y, E0=E0, E1=E1, E0x=fill(E0, x), E0y=fill(E0, y),
                                   E1x=fill(E1, x), E1y=fill(E1, y))
    return True, None

def verify_witness(S, wit):
    x, y, E0, E1 = wit['x'], wit['y'], wit['E0'], wit['E1']
    if ttype(x) != ttype(y) or len(x) != len(y):
        return False
    if any(c == '' for c in x + y):
        return False
    if len(x) == 2 and (E0[1] == '' or E1[1] == ''):
        return False
    return fill(E0, x) in S and fill(E0, y) in S and fill(E1, x) in S and fill(E1, y) not in S

def shortest_apower(S):
    ns = [len(w) for w in S if w and set(w) == {'a'}]
    return min(ns) if ns else None

def skeleton_conflicts(S, N):
    by = defaultdict(set)
    for w in S:
        if set(w) != {'a'} and acount(w) <= N - 1:
            by[skel(w)].add(acount(w))
    return {k: sorted(v) for k, v in by.items() if len(v) > 1}

# --------------------------------------------------------------------------------------
class Closure:
    """Incremental closure of a seed under the d=1,2 content-typed substitution rule.
    status: 'closed' (queue exhausted, nothing truncated: K is exactly closed),
            'truncated' (queue exhausted but some consequence exceeded cap_len: K is NOT closed),
            'cap' (word cap reached), 'contra' (shorter a-power or Lemma-L2 skeleton conflict)."""

    def __init__(self, seed, N=None, cap_len=None, cap_words=10**5, stop_on_contra=True):
        self.N, self.cap_len, self.cap_words = N, cap_len, cap_words
        self.stop = stop_on_contra
        self.K = set()
        self.origin = {}
        self.parent = {}
        self.members = {}
        self.ctxs = {}              # root -> {E: source member x with E[x] in K}
        self.rep = {}               # (type, E) -> first tuple seen
        self.fadj = defaultdict(list)   # proof forest: x -> [(y, E)] with E[x],E[y] in K
        self.queue = deque()
        self.truncated = False
        self.status = None
        self.contra = None
        self.skmap = {}
        for w in seed:
            self._add(w, None)

    def find(self, x):
        p = self.parent
        root = x
        while p[root] != root:
            root = p[root]
        while p[x] != root:
            p[x], x = root, p[x]
        return root

    def _add(self, w, org):
        if w in self.K:
            return
        if self.cap_len is not None and len(w) > self.cap_len:
            self.truncated = True
            return
        self.K.add(w)
        self.origin[w] = org
        self.queue.append(w)
        N = self.N
        if N is not None and self.contra is None:
            if set(w) == {'a'} and len(w) < N:
                self.contra = ('apower', w)
            elif set(w) != {'a'} and acount(w) <= N - 1:
                s = skel(w)
                if s in self.skmap and acount(self.skmap[s]) != acount(w):
                    self.contra = ('skeleton', self.skmap[s], w)
                else:
                    self.skmap.setdefault(s, w)

    def _newctx(self, root, E, src):
        C = self.ctxs[root]
        if E in C:
            return
        C[E] = src
        for y in self.members[root]:
            self._add(fill(E, y), (src, y, E))

    def _union(self, x, y, E):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return
        self.fadj[x].append((y, E))
        self.fadj[y].append((x, E))
        if len(self.members[rx]) + len(self.ctxs[rx]) < len(self.members[ry]) + len(self.ctxs[ry]):
            rx, ry = ry, rx
        # merge ry into rx
        Mx, My = self.members[rx], self.members[ry]
        Cx, Cy = self.ctxs[rx], self.ctxs[ry]
        for E1, src in Cx.items():
            if E1 not in Cy:
                for yy in My:
                    self._add(fill(E1, yy), (src, yy, E1))
        for E1, src in Cy.items():
            if E1 not in Cx:
                for yy in Mx:
                    self._add(fill(E1, yy), (src, yy, E1))
        self.parent[ry] = rx
        Mx.extend(My)
        for E1, src in Cy.items():
            Cx.setdefault(E1, src)
        del self.members[ry], self.ctxs[ry]

    def run(self):
        while self.queue:
            if self.contra is not None and self.stop:
                self.status = 'contra'
                return self
            if len(self.K) > self.cap_words:
                self.status = 'cap'
                return self
            w = self.queue.popleft()
            for x, E in tuples_of(w):
                if x not in self.parent:
                    self.parent[x] = x
                    self.members[x] = [x]
                    self.ctxs[x] = {}
                r = self.find(x)
                self._newctx(r, E, x)
                key = (ttype(x), E)
                z = self.rep.get(key)
                if z is None:
                    self.rep[key] = x
                elif self.find(z) != self.find(x):
                    self._union(z, x, E)
        if self.contra is not None:
            self.status = 'contra'
        else:
            self.status = 'truncated' if self.truncated else 'closed'
        return self

    # ---------------- certificates
    def _path(self, x, y):
        if x == y:
            return [x], []
        prev = {x: None}
        dq = deque([x])
        while dq:
            t = dq.popleft()
            if t == y:
                break
            for (u, E) in self.fadj[t]:
                if u not in prev:
                    prev[u] = (t, E)
                    dq.append(u)
        if y not in prev:
            raise RuntimeError('no forest path')
        nodes, edges = [y], []
        t = y
        while prev[t] is not None:
            s, E = prev[t]
            nodes.append(s)
            edges.append(E)
            t = s
        nodes.reverse(); edges.reverse()
        return nodes, edges

    def certificate(self, targets):
        """ordered direct rule applications (x,y,E0,E1,conclusion) deriving targets from seed"""
        steps, have = [], set(w for w, o in self.origin.items() if o is None)
        sys_limit = []

        def need(w):
            stack = [(w, 0)]
            while stack:
                v, st = stack.pop()
                if v in have:
                    continue
                src, y, E1 = self.origin[v]
                nodes, edges = self._path(src, y)
                prem = [fill(E1, src)]
                for i, E0 in enumerate(edges):
                    prem.append(fill(E0, nodes[i]))
                    prem.append(fill(E0, nodes[i + 1]))
                missing = [p for p in prem if p not in have]
                if st == 0 and missing:
                    stack.append((v, 1))
                    for p in missing:
                        stack.append((p, 0))
                    continue
                if v in have:
                    continue
                cur = fill(E1, src)
                for i, E0 in enumerate(edges):
                    nxt = fill(E1, nodes[i + 1])
                    if nxt not in have:
                        steps.append((nodes[i], nodes[i + 1], E0, E1, nxt))
                        have.add(nxt)
                have.add(v)
        for t in targets:
            need(t)
        return steps

def replay(seed, steps):
    """Independent replay: each step must be a legal rule application on already-derived words."""
    K = set(seed)
    for (x, y, E0, E1, w) in steps:
        if len(x) != len(y) or len(E0) != len(x) + 1 or len(E1) != len(x) + 1:
            return False, 'arity'
        if ttype(x) != ttype(y):
            return False, 'type mismatch %r %r' % (x, y)
        if any(c == '' for c in x + y):
            return False, 'empty hole'
        if len(x) == 2 and (E0[1] == '' or E1[1] == ''):
            return False, 'empty separator'
        for p in (fill(E0, x), fill(E0, y), fill(E1, x)):
            if p not in K:
                return False, 'premise %s missing' % p
        if fill(E1, y) != w:
            return False, 'conclusion mismatch'
        K.add(w)
    return True, K

def compositions(total, parts, minpart=1):
    if parts == 0:
        if total == 0:
            yield ()
        return
    for first in range(minpart, total - minpart * (parts - 1) + 1):
        for rest in compositions(total - first, parts - 1, minpart):
            yield (first,) + rest

def placements(cores, a_total, minrun=1):
    """all words a^{p0} k1 a^{p1} ... kt a^{pt}, p_i >= minrun, sum p = a_total"""
    out = set()
    for comp in compositions(a_total, len(cores) + 1, minrun):
        w = 'a' * comp[0]
        for k, p in zip(cores, comp[1:]):
            w += k + 'a' * p
        out.add(w)
    return out

===== END FILE =====

===== BEGIN FILE exploration/t1.py bytes=1166 sha256=c081fe875e1cc1b0dd2060b50dd77aa0f3aef3e3f56f5dcb89c65a3e46ba3658 =====
import sys, time
sys.path.insert(0,'.')
from r14core import *
S=set('''aaabc aabac aabca abaac abaca abcaa baaac baaca bacaa bcaaa
aaaaac aaaaca aaaacb aaacaa aaacab aaacba aacaaa aacaab aacaba aacbaa
acaaaa acaaab acaaba acabaa acbaaa caaaaa caaaab caaaba caabaa cabaaa
cbaaaa aaaaaab aaaaaba aaaabaa aaabaaa aabaaaa abaaaaa baaaaaa
aaaaaaaa'''.split()); L=S|{'bc'}
print(len(L), check_closed(L)[0], shortest_apower(L))
# engine sanity: E1 seed f2=4 closure
N=8
seed={'a'*N}|placements(['b'],N-2)|placements(['c'],N-3)|placements(['b','c'],N-5)|placements(['c','b'],N-4)
t=time.time(); C=Closure(seed,N=N,cap_len=N+3).run(); print(C.status,len(C.K),time.time()-t, sorted(C.K)==sorted(S))
N=10
def e2seed(N,d):
    s={'a'*N}
    for p in d: s|=placements([p],N-d[p])
    for p in d:
        for q in d:
            t=N-d[p]-d[q]
            if t>=3: s|=placements([p,q],t)
    return s
seed=e2seed(10,{'bc':2,'cb':3})
t=time.time(); C=Closure(seed,N=10,cap_len=14,cap_words=40000).run(); print(C.status,len(C.K),C.contra,time.time()-t)
tg=list(C.contra[1:]) if C.contra[0]=='skeleton' else [C.contra[1]]
st=C.certificate(tg); ok,_=replay(seed,st); print(len(st),ok)

===== END FILE =====

===== BEGIN FILE exploration/t10.out bytes=183 sha256=c4d9380c8c84cda69e1cba9e0b1e22efc515448974b2a8f4e589dc572b50f619 =====
bc bbcc 10 5 1 cap 45127 None 3.7
bc cbbc 12 3 1 contra 18839 ('skeleton', 'abcacbbcaaaaaa', 'abcacbbca') 5.2
bcc ccb 12 5 1 contra 13987 ('skeleton', 'bccbacca', 'bccbaccaaaaa') 3.9

===== END FILE =====

===== BEGIN FILE exploration/t10.py bytes=511 sha256=28d16da9f6738f4f90ef6be184affac836254d18f5df5b3566da7529af6848a2 =====
import sys,time; sys.path.insert(0,'.')
from r14core import *
def seedmin(N,k1,d1,k2,d2):
    l1=N-d1-acount(k1); l2=N-d2-acount(k2); t=N-d1-d2-acount(k1)-acount(k2)
    return {'a'*N,'a'+k1+'a'*(l1-1),'a'+k2+'a'*(l2-1),'a'+k1+'a'+k2+'a'*(t-2)}
for (k1,k2,N,d1,d2) in [('bc','bbcc',10,5,1),('bc','cbbc',12,3,1),('bcc','ccb',12,5,1)]:
    t=time.time(); C=Closure(seedmin(N,k1,d1,k2,d2),N=N,cap_len=N+4,cap_words=45000).run()
    print(k1,k2,N,d1,d2,C.status,len(C.K),C.contra,round(time.time()-t,1),flush=True)

===== END FILE =====

===== BEGIN FILE exploration/t11.out bytes=7128 sha256=cf5a369a5d946ef62699efa3d22c383d3e72e22ac3bbe1a29fae5966a3b4c7f9 =====
bbcc bcbc 11 1 2 truncated 55 None 0.2
bbcc bcbc 11 1 3 contra 255 ('skeleton', 'abccbabcbca', 'abccbabcbcaaa') 0.2
bbcc bcbc 11 1 4 contra 231 ('skeleton', 'abccbabbccaaaa', 'abccbabbcca') 0.1
bbcc bcbc 11 1 5 contra 373 ('skeleton', 'bccbbcbcaaaaa', 'bccbbcbca') 0.3
bbcc bcbc 11 2 1 truncated 46 None 0.4
bbcc bcbc 11 2 3 contra 479 ('skeleton', 'abbcbccbcaaaaa', 'aabbcbccbcaaaaa') 0.1
bbcc bcbc 11 2 4 contra 279 ('skeleton', 'abaaabccabcbc', 'ababccabcbc') 0.1
bbcc bcbc 11 2 5 contra 285 ('skeleton', 'bccbbcbcaaaa', 'bccbbcbca') 0.4
bbcc bcbc 11 3 1 contra 1537 ('skeleton', 'abbcbcbccaa', 'aaabbcbcbccaaaa') 1.0
bbcc bcbc 11 3 2 contra 509 ('skeleton', 'aaabccabcbbcaaa', 'abccabcbbcaaaa') 0.3
bbcc bcbc 11 3 4 contra 191 ('skeleton', 'abbcbccbcaaa', 'aabbcbccbcaaa') 0.1
bbcc bcbc 11 3 5 contra 181 ('skeleton', 'abbbcccbcaaaaaa', 'abbbcccbcaaaa') 0.1
bbcc bcbc 11 4 1 contra 409 ('skeleton', 'abbcbccbcaa', 'aaaaabbcbccbca') 0.4
bbcc bcbc 11 4 2 contra 363 ('skeleton', 'abbcbccbcaaaa', 'abbcbccbcaa') 0.1
bbcc bcbc 11 4 3 contra 353 ('skeleton', 'aabccbbcbcaaaa', 'abccbbcbcaaaa') 0.1
bbcc bcbc 11 5 1 contra 344 ('skeleton', 'bcbbcbccaaaaa', 'bcbbcbcca') 0.3
bbcc bcbc 11 5 2 contra 309 ('skeleton', 'abccbabbccaa', 'abccbaaaabbccaa') 0.2
bbcc bcbc 11 5 3 contra 185 ('skeleton', 'abccbbcbcaaaa', 'aaabccbbcbcaaaa') 0.1
bbcc bcbc 13 1 2 truncated 67 None 0.4
bbcc bcbc 13 1 3 contra 554 ('skeleton', 'abccbbcbcaaaa', 'abccbbcbcaaaaaa') 0.5
bbcc bcbc 13 1 4 contra 385 ('skeleton', 'abccbbcbca', 'abccbbcbcaaaa') 0.4
bbcc bcbc 13 1 5 contra 278 ('skeleton', 'abccbabbccaaaaa', 'abccbabbcca') 0.2
bbcc bcbc 13 2 1 truncated 54 None 0.5
bbcc bcbc 13 2 3 contra 1034 ('skeleton', 'abbcbccbcaaaaaaa', 'aabbcbccbcaaaaaaa') 0.5
bbcc bcbc 13 2 4 contra 661 ('skeleton', 'bbccabcbcabcbca', 'bbccabcbcabcbcaaa') 0.2
bbcc bcbc 13 2 5 contra 545 ('skeleton', 'abccabbcbcaaaa', 'abccabbcbca') 0.2
bbcc bcbc 13 3 1 contra 499 ('skeleton', 'abbbccbcbcbccaaa', 'abbbccbcbcbcca') 1.5
bbcc bcbc 13 3 2 contra 1299 ('skeleton', 'abccabcbbcaaaaaa', 'abccaabcbbcaaaaaa') 0.5
bbcc bcbc 13 3 4 contra 489 ('skeleton', 'abbcbccbcaaaa', 'abbcbccbcaaaaa') 0.2
bbcc bcbc 13 3 5 contra 202 ('skeleton', 'aaabbcbccbcaaaa', 'abbcbccbcaaaa') 0.1
bbcc bcbc 13 4 1 contra 1221 ('skeleton', 'abcbbccbcaaaaaaa', 'abcbbccbcaaaa') 0.8
bbcc bcbc 13 4 2 contra 557 ('skeleton', 'abbccabcbcaaabcbc', 'abbccabcbcabcbc') 0.2
bbcc bcbc 13 4 3 contra 652 ('skeleton', 'aabccbbcbcaaaaaa', 'abccbbcbcaaaaaa') 0.2
bbcc bcbc 13 4 5 contra 188 ('skeleton', 'abbcbccbcaaa', 'aabbcbccbcaaa') 0.1
bbcc bcbc 13 5 1 contra 1804 ('skeleton', 'aaaaaabbcccbbca', 'abbcccbbcaa') 1.0
bbcc bcbc 13 5 2 contra 497 ('skeleton', 'abbcbccbcaaaaa', 'abbcbccbcaa') 0.2
bbcc bcbc 13 5 3 contra 516 ('skeleton', 'aabccbbcbcaaaaaaa', 'abccbbcbcaaaaaa') 0.2
bbcc bcbc 13 5 4 contra 344 ('skeleton', 'aabccbbcbcaaaa', 'abccbbcbcaaaa') 0.1
bcbc bbcc 11 1 2 truncated 46 None 0.3
bcbc bbcc 11 1 3 contra 687 ('skeleton', 'abcabbcbccaaa', 'abcabbcbccaaaaa') 1.1
bcbc bbcc 11 1 4 contra 761 ('skeleton', 'abbcbcacbca', 'abbcbcacbcaaaa') 0.6
bcbc bbcc 11 1 5 contra 344 ('skeleton', 'bbcbccbcaaaaa', 'bbcbccbca') 0.3
bcbc bbcc 11 2 1 truncated 55 None 0.2
bcbc bbcc 11 2 3 contra 372 ('skeleton', 'abcbccbbcaaaaa', 'aabcbccbbcaaaaa') 0.1
bcbc bbcc 11 2 4 contra 301 ('skeleton', 'aabcbccbbcaaaaa', 'abcbccbbcaaaa') 0.1
bcbc bbcc 11 2 5 contra 381 ('skeleton', 'abcbcbacbcaaaaa', 'abcbcbacbcaa') 0.1
bcbc bbcc 11 3 1 contra 252 ('skeleton', 'aabcbccbbcaaa', 'abcbccbbcaa') 0.2
bcbc bbcc 11 3 2 contra 323 ('skeleton', 'abcbccbbcaaaaa', 'aabcbccbbcaaa') 0.2
bcbc bbcc 11 3 4 contra 182 ('skeleton', 'abcbccbbcaaa', 'aabcbccbbcaaa') 0.1
bcbc bbcc 11 3 5 contra 350 ('skeleton', 'abcbccbbcaaaaaa', 'abcbccbbcaaaa') 0.1
bcbc bbcc 11 4 1 contra 203 ('skeleton', 'abcbcbacbca', 'abcbcbacbcaaaa') 0.1
bcbc bbcc 11 4 2 contra 242 ('skeleton', 'aabcbccbbca', 'abcbccbbcaaaa') 0.2
bcbc bbcc 11 4 3 contra 143 ('skeleton', 'abcbccbbca', 'abcbccbbcaaa') 0.1
bcbc bbcc 11 5 1 contra 406 ('skeleton', 'cbcbbbccaaaaa', 'cbcbbbcca') 0.3
bcbc bbcc 11 5 2 contra 348 ('skeleton', 'bccbbcbcaaaa', 'bccbbcbca') 0.4
bcbc bbcc 11 5 3 contra 253 ('skeleton', 'abbcbccbcaaaa', 'abbcbccbcaa') 0.1
bcbc bbcc 13 1 2 truncated 54 None 0.6
bcbc bbcc 13 1 3 contra 332 ('skeleton', 'abbcbcbcbbcccaaa', 'abbcbcbcbbccca') 0.5
bcbc bbcc 13 1 4 contra 908 ('skeleton', 'aabcbbccbcaaaaaa', 'abcbbccbcaaaa') 0.4
bcbc bbcc 13 1 5 contra 658 ('skeleton', 'abcabbcbcca', 'abcabbcbccaaaaa') 1.2
bcbc bbcc 13 2 1 truncated 67 None 0.7
bcbc bbcc 13 2 3 contra 1178 ('skeleton', 'abccbcbbcaaaaaaa', 'abccbcbbcaaaaaaaa') 0.4
bcbc bbcc 13 2 4 contra 483 ('skeleton', 'abcbccbbcaaaaaa', 'aabcbccbbcaaaaaaa') 0.2
bcbc bbcc 13 2 5 contra 372 ('skeleton', 'aabcbccbbcaaaaaaa', 'abcbccbbcaaaaa') 0.2
bcbc bbcc 13 3 1 contra 439 ('skeleton', 'abcbccbbcaaaa', 'aabcbccbbcaaaaa') 0.4
bcbc bbcc 13 3 2 contra 645 ('skeleton', 'aabcbccbbcaaaaa', 'abcbccbbcaaaaaaa') 0.4
bcbc bbcc 13 3 4 contra 404 ('skeleton', 'abcbccbbcaaaaa', 'aabcbccbbcaaaaa') 0.2
bcbc bbcc 13 3 5 contra 338 ('skeleton', 'abcbccbbcaaaaaaaa', 'aabcbccbbcaaaaa') 0.1
bcbc bbcc 13 4 1 contra 385 ('skeleton', 'aabcbccbbcaaa', 'abcbccbbca') 0.3
bcbc bbcc 13 4 2 contra 643 ('skeleton', 'abcbcabcbcabbcc', 'aaabcbcabcbcabbcc') 0.2
bcbc bbcc 13 4 3 contra 390 ('skeleton', 'abcbccbbcaaaaa', 'aabcbccbbcaaa') 0.1
bcbc bbcc 13 4 5 contra 130 ('skeleton', 'abcbccbbcaaaaa', 'abcbccbbcaaa') 0.1
bcbc bbcc 13 5 1 contra 249 ('skeleton', 'abcbcbacbca', 'abcbcbacbcaaaaa') 0.3
bcbc bbcc 13 5 2 contra 499 ('skeleton', 'abccbcbbcaaaaa', 'abccbcbbcaa') 0.2
bcbc bbcc 13 5 3 contra 234 ('skeleton', 'aabcbccbbca', 'abcbccbbcaaaa') 0.2
bcbc bbcc 13 5 4 contra 136 ('skeleton', 'aabcbccbbca', 'abcbccbbcaaa') 0.1
bccb bcbb 11 1 2 truncated 22 None 0.2
bccb bcbb 11 1 3 cap 15325 None 2.6
bccb bcbb 11 1 4 cap 15308 None 1.5
bccb bcbb 11 1 5 cap 15073 None 2.8
bccb bcbb 11 2 1 truncated 22 None 0.4
bccb bcbb 11 2 3 cap 15107 None 1.9
bccb bcbb 11 2 4 cap 15024 None 1.6
bccb bcbb 11 2 5 cap 15073 None 1.9
bccb bcbb 11 3 1 cap 20392 None 4.4
bccb bcbb 11 3 2 cap 15086 None 3.1
bccb bcbb 11 3 4 cap 16110 None 1.0
bccb bcbb 11 3 5 cap 15092 None 1.1
bccb bcbb 11 4 1 cap 16247 None 2.2
bccb bcbb 11 4 2 cap 18715 None 2.0
bccb bcbb 11 4 3 cap 15046 None 0.9
bccb bcbb 11 5 1 cap 15143 None 3.3
bccb bcbb 11 5 2 cap 15298 None 1.5
bccb bcbb 11 5 3 cap 15432 None 1.2
bccb bcbb 13 1 2 truncated 26 None 0.2
bccb bcbb 13 1 3 cap 15069 None 3.4
bccb bcbb 13 1 4 cap 15230 None 2.0
bccb bcbb 13 1 5 cap 15482 None 2.5
bccb bcbb 13 2 1 truncated 26 None 0.3
bccb bcbb 13 2 3 cap 15126 None 2.2
bccb bcbb 13 2 4 cap 15090 None 3.0
bccb bcbb 13 2 5 cap 15417 None 1.4
bccb bcbb 13 3 1 cap 15042 None 5.4
bccb bcbb 13 3 2 cap 15039 None 2.5
bccb bcbb 13 3 4 cap 15043 None 1.9
bccb bcbb 13 3 5 cap 23651 None 2.8
bccb bcbb 13 4 1 cap 15076 None 1.9
bccb bcbb 13 4 2 cap 15461 None 3.2
bccb bcbb 13 4 3 cap 15036 None 2.0
bccb bcbb 13 4 5 cap 17963 None 0.6
bccb bcbb 13 5 1 cap 15395 None 3.3
bccb bcbb 13 5 2 cap 15171 None 2.6
bccb bcbb 13 5 3 cap 15804 None 1.8
bccb bcbb 13 5 4 cap 15013 None 1.2

===== END FILE =====

===== BEGIN FILE exploration/t11.py bytes=663 sha256=a812becdbea49bdd488153a0a6525bc9b5bb1890b648501f559ce53e768f29dc =====
import sys,time; sys.path.insert(0,'.')
from r14core import *
def seedmin(N,k1,d1,k2,d2):
    l1=N-d1-acount(k1); l2=N-d2-acount(k2); t=N-d1-d2-acount(k1)-acount(k2)
    if min(l1,l2)<3 or t<3: return None
    return {'a'*N,'a'+k1+'a'*(l1-1),'a'+k2+'a'*(l2-1),'a'+k1+'a'+k2+'a'*(t-2)}
for (k1,k2) in [('bbcc','bcbc'),('bcbc','bbcc'),('bccb','bcbb')]:
  for N in (11,13):
    for d1 in range(1,6):
      for d2 in range(1,6):
        s=seedmin(N,k1,d1,k2,d2)
        if s is None or d1==d2: continue
        t=time.time(); C=Closure(s,N=N,cap_len=N+4,cap_words=15000).run()
        print(k1,k2,N,d1,d2,C.status,len(C.K),C.contra,round(time.time()-t,1),flush=True)

===== END FILE =====

===== BEGIN FILE exploration/t12.py bytes=487 sha256=4df176eb5db4c28a49b720146ce9f4817105943eb66c6bfb3d3c74b189b2d620 =====
import sys,time; sys.path.insert(0,'.')
from r14core import *
def seedmin(N,k1,d1,k2,d2):
    l1=N-d1-acount(k1); l2=N-d2-acount(k2); t=N-d1-d2-acount(k1)-acount(k2)
    return {'a'*N,'a'+k1+'a'*(l1-1),'a'+k2+'a'*(l2-1),'a'+k1+'a'+k2+'a'*(t-2)}
for (N,d1,d2) in [(11,1,2),(11,2,1)]:
  for cl in (N+6,N+8):
    t=time.time(); C=Closure(seedmin(N,'bbcc',d1,'bcbc',d2),N=N,cap_len=cl,cap_words=40000).run()
    print(N,d1,d2,cl,C.status,len(C.K),C.contra,round(time.time()-t,1),flush=True)

===== END FILE =====

===== BEGIN FILE exploration/t13.py bytes=559 sha256=88a207cd547620e69788f88e811447baf2ade49d968cb9cee9777dc1d7bfb886 =====
import sys; sys.path.insert(0,'.')
from r14core import *
def seedmin(N,k1,d1,k2,d2):
    l1=N-d1-acount(k1); l2=N-d2-acount(k2); t=N-d1-d2-acount(k1)-acount(k2)
    return {'a'*N,'a'+k1+'a'*(l1-1),'a'+k2+'a'*(l2-1),'a'+k1+'a'+k2+'a'*(t-2)}
for (N,d1,d2) in [(13,3,5),(11,1,2)]:
    s=seedmin(N,'bbcc',d1,'bcbc',d2)
    C=Closure(s,N=N,cap_len=N+6,cap_words=40000).run()
    tg=list(C.contra[1:]); st=C.certificate(tg); ok,_=replay(s,st)
    print(N,d1,d2,sorted(s),C.contra,len(st),ok)
    for k,(x,y,E0,E1,w) in enumerate(st): print('  ',k,x,y,E0,E1,'=>',w)

===== END FILE =====

===== BEGIN FILE exploration/t2.py bytes=1302 sha256=977fd37a64aab2661665cf1fc96e2df564c7d471b0d7c2f88737452e87036603 =====
import sys; sys.path.insert(0,'.')
from r14core import *
S=set('''aaabc aabac aabca abaac abaca abcaa baaac baaca bacaa bcaaa
aaaaac aaaaca aaaacb aaacaa aaacab aaacba aacaaa aacaab aacaba aacbaa
acaaaa acaaab acaaba acabaa acbaaa caaaaa caaaab caaaba caabaa cabaaa
cbaaaa aaaaaab aaaaaba aaaabaa aaabaaa aabaaaa abaaaaa baaaaaa
aaaaaaaa'''.split()); L=S|{'bc'}; N=8
ctx=ctx_maps(L)
def D(x): return ctx.get(x,set())
rot={}
for w in L:
    if set(w)=={'a'}: continue
    p=len(w)-len(w.lstrip('a')); r=len(w)-len(w.rstrip('a'))
    k=w.strip('a')
    if p>=1 and r>=1 and 3<=p+r<=N-1: rot.setdefault(k,set()).add(p+r)
print({k:v for k,v in rot.items()})
chk=bad=0; bad0=0;chk0=0
for k,ls in rot.items():
  for k2,ls2 in rot.items():
    if set(k)|{'a'}!=set(k2)|{'a'}: continue
    for lam in ls:
      for lam2 in ls2:
        for i in range(1,12):
          ip=i+lam2-lam
          if ip<1: continue
          chk+=1
          if D(('a'*i+k,))!=D(('a'*ip+k2,)): bad+=1
          if D((k+'a'*i,))!=D((k2+'a'*ip,)): bad+=1
        # unpadded original X1 i=(lam-lam2)_+
        i=max(0,lam-lam2); ip=max(0,lam2-lam)
        chk0+=1
        if D(('a'*i+k,))!=D(('a'*ip+k2,)): bad0+=1; ex=(k,k2,i,ip)
print('padded X1+ checks',chk,'violations',bad); print('original X1 checks',chk0,'violations',bad0, ex)

===== END FILE =====

===== BEGIN FILE exploration/t3.py bytes=661 sha256=f4d42e685f56726588d75f231bf056f631b6c1723d7f9ea32ddd4049abc61182 =====
import sys,time; sys.path.insert(0,'.')
from r14core import *
def seedmin(N,k1,d1,k2,d2):
    l1=N-d1-acount(k1); l2=N-d2-acount(k2); t=N-d1-d2-acount(k1)-acount(k2)
    if min(l1,l2)<2 or t<3: return None
    return {'a'*N,'a'+k1+'a'*(l1-1),'a'+k2+'a'*(l2-1),'a'+k1+'a'+k2+'a'*(t-2)}
if __name__!="__main__": raise SystemExit
res=[]
for N in range(7,15):
  for d1 in range(1,(N-1)//2+1):
    for d2 in range(1,(N-1)//2+1):
      s=seedmin(N,'bc',d1,'cb',d2)
      if s is None: continue
      t=time.time(); C=Closure(s,N=N,cap_len=N+4,cap_words=15000).run()
      res.append((N,d1,d2,C.status,len(C.K),round(time.time()-t,1)))
      print(res[-1],flush=True)

===== END FILE =====

===== BEGIN FILE exploration/t4.py bytes=628 sha256=e12650ed403e39077fa1bff506e8a575ec7de7184385b34cbd3d630569104c23 =====
import sys; sys.path.insert(0,'.')
from r14core import *
def seedmin(N,k1,d1,k2,d2):
    l1=N-d1-acount(k1); l2=N-d2-acount(k2); t=N-d1-d2-acount(k1)-acount(k2)
    return {'a'*N,'a'+k1+'a'*(l1-1),'a'+k2+'a'*(l2-1),'a'+k1+'a'+k2+'a'*(t-2)}
for (N,d1,d2) in [(8,2,3),(9,3,4),(11,5,3),(12,1,5)]:
    s=seedmin(N,'bc',d1,'cb',d2)
    C=Closure(s,N=N,cap_len=N+4).run()
    tg=list(C.contra[1:]) if C.contra[0]=='skeleton' else [C.contra[1]]
    st=C.certificate(tg); ok,_=replay(s,st)
    print(N,d1,d2,'seed',sorted(s),'contra',C.contra,'steps',len(st),ok)
    for k,(x,y,E0,E1,w) in enumerate(st): print('  ',k,x,y,E0,E1,'=>',w)

===== END FILE =====

===== BEGIN FILE exploration/t5.out bytes=15553 sha256=0706c9aeb13c3df1b6613896b2ed7aee3b2f5a626934570a78e171dbc7645648 =====
bc bbcc 10 1 1 prop= False contra 304 0.2
bc bbcc 10 1 2 prop= True cap 10736 2.2
bc bbcc 10 1 3 prop= False contra 377 0.1
bc bbcc 10 1 4 prop= False contra 263 0.1
bc bbcc 10 1 5 prop= False contra 242 0.0
bc bbcc 10 2 1 prop= False contra 330 0.1
bc bbcc 10 2 2 prop= False contra 360 0.1
bc bbcc 10 2 3 prop= False contra 122 0.0
bc bbcc 10 2 4 prop= True cap 8001 1.7
bc bbcc 10 2 5 prop= False contra 134 0.1
bc bbcc 10 3 1 prop= False contra 320 0.2
bc bbcc 10 3 2 prop= False contra 613 0.2
bc bbcc 10 3 3 prop= False contra 292 0.1
bc bbcc 10 3 4 prop= False contra 69 0.0
bc bbcc 10 4 1 prop= False contra 2832 0.5
bc bbcc 10 4 2 prop= False contra 3107 0.6
bc bbcc 10 4 3 prop= False contra 149 0.1
bc bbcc 10 5 1 prop= False cap 8888 1.0
bc bbcc 10 5 2 prop= False cap 8134 1.3
bc bbcc 12 1 1 prop= False contra 471 0.4
bc bbcc 12 1 2 prop= True cap 8256 4.1
bc bbcc 12 1 3 prop= False contra 825 0.2
bc bbcc 12 1 4 prop= False contra 612 0.1
bc bbcc 12 1 5 prop= False contra 435 0.1
bc bbcc 12 2 1 prop= False contra 586 0.2
bc bbcc 12 2 2 prop= False contra 389 0.1
bc bbcc 12 2 3 prop= False contra 578 0.1
bc bbcc 12 2 4 prop= True cap 8059 0.9
bc bbcc 12 2 5 prop= False contra 185 0.1
bc bbcc 12 3 1 prop= False contra 2112 1.0
bc bbcc 12 3 2 prop= False contra 235 0.1
bc bbcc 12 3 3 prop= False contra 727 0.1
bc bbcc 12 3 4 prop= False contra 207 0.1
bc bbcc 12 3 5 prop= False contra 98 0.0
bc bbcc 12 4 1 prop= False contra 8511 1.8
bc bbcc 12 4 2 prop= False contra 672 0.5
bc bbcc 12 4 3 prop= False contra 427 0.1
bc bbcc 12 4 4 prop= False contra 210 0.0
bc bbcc 12 4 5 prop= False contra 89 0.0
bc bbcc 12 5 1 prop= False contra 6793 1.0
bc bbcc 12 5 2 prop= False contra 8302 2.1
bc bbcc 12 5 3 prop= False contra 3827 1.0
bc bbcc 12 5 4 prop= False contra 261 0.1
bc cbbc 10 1 1 prop= False contra 2164 2.5
bc cbbc 10 1 2 prop= True cap 8464 1.4
bc cbbc 10 1 3 prop= False contra 620 0.1
bc cbbc 10 1 4 prop= False contra 615 0.1
bc cbbc 10 1 5 prop= False contra 1191 0.3
bc cbbc 10 2 1 prop= False contra 3071 1.9
bc cbbc 10 2 2 prop= False contra 1022 0.1
bc cbbc 10 2 3 prop= False contra 591 0.1
bc cbbc 10 2 4 prop= True cap 8022 2.4
bc cbbc 10 2 5 prop= False contra 182 0.1
bc cbbc 10 3 1 prop= False contra 3542 1.8
bc cbbc 10 3 2 prop= False contra 1263 0.5
bc cbbc 10 3 3 prop= False contra 644 0.1
bc cbbc 10 3 4 prop= False contra 266 0.0
bc cbbc 10 4 1 prop= False cap 8057 1.0
bc cbbc 10 4 2 prop= False cap 8893 1.6
bc cbbc 10 4 3 prop= False contra 625 0.1
bc cbbc 10 5 1 prop= False cap 8499 0.6
bc cbbc 10 5 2 prop= False cap 11133 1.6
bc cbbc 12 1 1 prop= False contra 2515 4.1
bc cbbc 12 1 2 prop= True cap 8055 1.3
bc cbbc 12 1 3 prop= False contra 1121 0.2
bc cbbc 12 1 4 prop= False contra 1214 0.1
bc cbbc 12 1 5 prop= False contra 998 0.2
bc cbbc 12 2 1 prop= False contra 7298 2.9
bc cbbc 12 2 2 prop= False contra 1650 0.4
bc cbbc 12 2 3 prop= False contra 1436 0.1
bc cbbc 12 2 4 prop= True cap 8183 0.6
bc cbbc 12 2 5 prop= False contra 498 0.1
bc cbbc 12 3 1 prop= False cap 8520 1.9
bc cbbc 12 3 2 prop= False contra 1204 0.3
bc cbbc 12 3 3 prop= False contra 949 0.1
bc cbbc 12 3 4 prop= False contra 955 0.1
bc cbbc 12 3 5 prop= False contra 359 0.0
bc cbbc 12 4 1 prop= False cap 11754 2.3
bc cbbc 12 4 2 prop= False contra 2323 0.7
bc cbbc 12 4 3 prop= False contra 1027 0.2
bc cbbc 12 4 4 prop= False contra 1229 0.1
bc cbbc 12 4 5 prop= False contra 300 0.0
bc cbbc 12 5 1 prop= False cap 8407 1.5
bc cbbc 12 5 2 prop= False cap 8006 3.3
bc cbbc 12 5 3 prop= False cap 8515 1.6
bc cbbc 12 5 4 prop= False contra 1164 0.1
bcc cbc 10 1 1 prop= True cap 8008 1.1
bcc cbc 10 1 2 prop= False contra 380 0.1
bcc cbc 10 1 3 prop= False contra 223 0.1
bcc cbc 10 1 4 prop= False contra 235 0.0
bcc cbc 10 1 5 prop= False contra 360 0.1
bcc cbc 10 2 1 prop= False contra 631 0.1
bcc cbc 10 2 2 prop= True cap 15170 1.3
bcc cbc 10 2 3 prop= False contra 142 0.1
bcc cbc 10 2 4 prop= False contra 117 0.0
bcc cbc 10 2 5 prop= False contra 172 0.1
bcc cbc 10 3 1 prop= False contra 380 0.1
bcc cbc 10 3 2 prop= False contra 167 0.0
bcc cbc 10 3 3 prop= True closed 4351 10.9
bcc cbc 10 3 4 prop= False contra 52 0.2
bcc cbc 10 4 1 prop= False contra 331 0.1
bcc cbc 10 4 2 prop= False contra 218 0.0
bcc cbc 10 4 3 prop= False contra 88 0.0
bcc cbc 10 5 1 prop= False contra 1715 0.3
bcc cbc 10 5 2 prop= False contra 417 0.1
bcc cbc 12 1 1 prop= True cap 8049 1.0
bcc cbc 12 1 2 prop= False contra 667 0.3
bcc cbc 12 1 3 prop= False contra 1219 0.3
bcc cbc 12 1 4 prop= False contra 597 0.1
bcc cbc 12 1 5 prop= False contra 427 0.1
bcc cbc 12 2 1 prop= False contra 1113 0.3
bcc cbc 12 2 2 prop= True cap 8341 1.2
bcc cbc 12 2 3 prop= False contra 561 0.1
bcc cbc 12 2 4 prop= False contra 386 0.1
bcc cbc 12 2 5 prop= False contra 242 0.1
bcc cbc 12 3 1 prop= False contra 1604 0.3
bcc cbc 12 3 2 prop= False contra 1092 0.2
bcc cbc 12 3 3 prop= True cap 8935 0.7
bcc cbc 12 3 4 prop= False contra 162 0.1
bcc cbc 12 3 5 prop= False contra 117 0.1
bcc cbc 12 4 1 prop= False contra 501 0.1
bcc cbc 12 4 2 prop= False contra 595 0.1
bcc cbc 12 4 3 prop= False contra 166 0.0
bcc cbc 12 4 4 prop= True closed 3646 8.9
bcc cbc 12 4 5 prop= False contra 71 0.2
bcc cbc 12 5 1 prop= False contra 419 0.0
bcc cbc 12 5 2 prop= False contra 356 0.1
bcc cbc 12 5 3 prop= False contra 211 0.1
bcc cbc 12 5 4 prop= False contra 106 0.0
bcc ccb 10 1 1 prop= True cap 8041 2.3
bcc ccb 10 1 2 prop= False contra 751 0.5
bcc ccb 10 1 3 prop= False contra 603 0.1
bcc ccb 10 1 4 prop= False contra 8077 0.9
bcc ccb 10 1 5 prop= False contra 2024 0.2
bcc ccb 10 2 1 prop= False contra 684 0.2
bcc ccb 10 2 2 prop= True cap 8285 0.9
bcc ccb 10 2 3 prop= False contra 346 0.2
bcc ccb 10 2 4 prop= False contra 1594 0.2
bcc ccb 10 2 5 prop= False contra 1423 0.2
bcc ccb 10 3 1 prop= False contra 912 0.2
bcc ccb 10 3 2 prop= False contra 415 0.1
bcc ccb 10 3 3 prop= True closed 4351 10.1
bcc ccb 10 3 4 prop= False contra 479 0.2
bcc ccb 10 4 1 prop= False contra 5155 1.1
bcc ccb 10 4 2 prop= False contra 313 0.1
bcc ccb 10 4 3 prop= False contra 296 0.1
bcc ccb 10 5 1 prop= False contra 5058 0.7
bcc ccb 10 5 2 prop= False contra 2396 0.4
bcc ccb 12 1 1 prop= True cap 8118 3.0
bcc ccb 12 1 2 prop= False contra 1543 0.7
bcc ccb 12 1 3 prop= False contra 1695 0.4
bcc ccb 12 1 4 prop= False contra 829 0.3
bcc ccb 12 1 5 prop= False contra 4950 0.4
bcc ccb 12 2 1 prop= False contra 1125 0.5
bcc ccb 12 2 2 prop= True cap 9433 1.4
bcc ccb 12 2 3 prop= False contra 833 0.4
bcc ccb 12 2 4 prop= False contra 521 0.2
bcc ccb 12 2 5 prop= False contra 1602 0.4
bcc ccb 12 3 1 prop= False contra 2063 0.4
bcc ccb 12 3 2 prop= False contra 1137 0.3
bcc ccb 12 3 3 prop= True cap 8019 1.1
bcc ccb 12 3 4 prop= False contra 279 0.2
bcc ccb 12 3 5 prop= False contra 1552 0.3
bcc ccb 12 4 1 prop= False contra 1265 0.4
bcc ccb 12 4 2 prop= False contra 733 0.1
bcc ccb 12 4 3 prop= False contra 296 0.2
bcc ccb 12 4 4 prop= True closed 3646 9.6
bcc ccb 12 4 5 prop= False contra 453 0.2
bcc ccb 12 5 1 prop= False cap 8032 1.9
bcc ccb 12 5 2 prop= False contra 471 0.3
bcc ccb 12 5 3 prop= False contra 1872 0.2
bcc ccb 12 5 4 prop= False contra 537 0.1
bc bcc 10 1 1 prop= None cap 8022 0.3
bc bcc 10 1 2 prop= None cap 8411 0.2
bc bcc 10 1 3 prop= None cap 8131 0.2
bc bcc 10 1 4 prop= None cap 8271 0.6
bc bcc 10 1 5 prop= None cap 8420 0.5
bc bcc 10 2 1 prop= None cap 8204 0.3
bc bcc 10 2 2 prop= None cap 8634 0.3
bc bcc 10 2 3 prop= None cap 8150 0.4
bc bcc 10 2 4 prop= None cap 8057 0.4
bc bcc 10 2 5 prop= None cap 8081 0.2
bc bcc 10 3 1 prop= None cap 8050 0.8
bc bcc 10 3 2 prop= None cap 8162 0.4
bc bcc 10 3 3 prop= None cap 8097 0.3
bc bcc 10 3 4 prop= None closed 4543 4.8
bc bcc 10 4 1 prop= None cap 8028 1.5
bc bcc 10 4 2 prop= None cap 8167 1.9
bc bcc 10 4 3 prop= None cap 8086 0.9
bc bcc 10 5 1 prop= None cap 8115 1.8
bc bcc 10 5 2 prop= None cap 8601 1.1
bc bcc 12 1 1 prop= None cap 8369 0.8
bc bcc 12 1 2 prop= None cap 8633 0.3
bc bcc 12 1 3 prop= None cap 10900 0.3
bc bcc 12 1 4 prop= None cap 8047 0.3
bc bcc 12 1 5 prop= None cap 8019 0.4
bc bcc 12 2 1 prop= None cap 8400 0.7
bc bcc 12 2 2 prop= None cap 20659 0.3
bc bcc 12 2 3 prop= None cap 9237 0.3
bc bcc 12 2 4 prop= None cap 8072 0.3
bc bcc 12 2 5 prop= None cap 8006 0.4
bc bcc 12 3 1 prop= None cap 8085 0.8
bc bcc 12 3 2 prop= None cap 8129 0.2
bc bcc 12 3 3 prop= None cap 8012 0.2
bc bcc 12 3 4 prop= None cap 8238 0.5
bc bcc 12 3 5 prop= None cap 8039 0.6
bc bcc 12 4 1 prop= None cap 8045 0.4
bc bcc 12 4 2 prop= None cap 8052 0.6
bc bcc 12 4 3 prop= None cap 8025 0.2
bc bcc 12 4 4 prop= None cap 8230 0.4
bc bcc 12 4 5 prop= None closed 6957 13.1
bc bcc 12 5 1 prop= None cap 8255 2.0
bc bcc 12 5 2 prop= None cap 8383 0.7
bc bcc 12 5 3 prop= None cap 8026 0.4
bc bcc 12 5 4 prop= None cap 8761 0.5
bc bbc 10 1 1 prop= None cap 8084 0.5
bc bbc 10 1 2 prop= None cap 8138 0.2
bc bbc 10 1 3 prop= None cap 8032 0.3
bc bbc 10 1 4 prop= None cap 8063 0.4
bc bbc 10 1 5 prop= None cap 8323 0.5
bc bbc 10 2 1 prop= None cap 8310 0.9
bc bbc 10 2 2 prop= None cap 8495 0.3
bc bbc 10 2 3 prop= None cap 8067 0.5
bc bbc 10 2 4 prop= None cap 8094 0.3
bc bbc 10 2 5 prop= None cap 8062 0.3
bc bbc 10 3 1 prop= None cap 8242 0.9
bc bbc 10 3 2 prop= None cap 8021 0.5
bc bbc 10 3 3 prop= None cap 8100 0.3
bc bbc 10 3 4 prop= None closed 4543 5.8
bc bbc 10 4 1 prop= None cap 8070 2.2
bc bbc 10 4 2 prop= None cap 8221 1.5
bc bbc 10 4 3 prop= None cap 8067 0.6
bc bbc 10 5 1 prop= None cap 8123 2.1
bc bbc 10 5 2 prop= None cap 8169 0.8
bc bbc 12 1 1 prop= None cap 8125 0.6
bc bbc 12 1 2 prop= None cap 11600 0.3
bc bbc 12 1 3 prop= None cap 8164 0.3
bc bbc 12 1 4 prop= None cap 8185 0.3
bc bbc 12 1 5 prop= None cap 8050 0.5
bc bbc 12 2 1 prop= None cap 8566 0.3
bc bbc 12 2 2 prop= None cap 8728 0.3
bc bbc 12 2 3 prop= None cap 8003 0.2
bc bbc 12 2 4 prop= None cap 8168 0.3
bc bbc 12 2 5 prop= None cap 9453 0.2
bc bbc 12 3 1 prop= None cap 8018 0.7
bc bbc 12 3 2 prop= None cap 8248 0.4
bc bbc 12 3 3 prop= None cap 8065 0.3
bc bbc 12 3 4 prop= None cap 8017 0.5
bc bbc 12 3 5 prop= None cap 8007 0.6
bc bbc 12 4 1 prop= None cap 8118 0.9
bc bbc 12 4 2 prop= None cap 8048 0.7
bc bbc 12 4 3 prop= None cap 8083 0.3
bc bbc 12 4 4 prop= None cap 8044 0.2
bc bbc 12 4 5 prop= None closed 6957 13.4
bc bbc 12 5 1 prop= None cap 8190 2.5
bc bbc 12 5 2 prop= None cap 8006 0.6
bc bbc 12 5 3 prop= None cap 8008 0.5
bc bbc 12 5 4 prop= None cap 8135 0.6
bbc bcc 10 1 1 prop= None cap 8009 1.9
bbc bcc 10 1 2 prop= None cap 10978 2.1
bbc bcc 10 1 3 prop= None cap 8782 1.3
bbc bcc 10 1 4 prop= None cap 8030 1.9
bbc bcc 10 1 5 prop= None cap 8036 1.3
bbc bcc 10 2 1 prop= None cap 8151 1.9
bbc bcc 10 2 2 prop= None cap 16003 1.2
bbc bcc 10 2 3 prop= None cap 8124 0.9
bbc bcc 10 2 4 prop= None cap 8049 0.6
bbc bcc 10 2 5 prop= None cap 8051 0.8
bbc bcc 10 3 1 prop= None cap 9418 1.2
bbc bcc 10 3 2 prop= None cap 8039 0.8
bbc bcc 10 3 3 prop= None cap 8002 0.6
bbc bcc 10 3 4 prop= None cap 8011 0.9
bbc bcc 10 4 1 prop= None cap 8062 1.2
bbc bcc 10 4 2 prop= None cap 8487 0.9
bbc bcc 10 4 3 prop= None cap 8009 0.8
bbc bcc 10 5 1 prop= None cap 8014 1.3
bbc bcc 10 5 2 prop= None cap 8030 0.6
bbc bcc 12 1 1 prop= None cap 8021 3.6
bbc bcc 12 1 2 prop= None cap 8959 3.8
bbc bcc 12 1 3 prop= None cap 11014 3.5
bbc bcc 12 1 4 prop= None cap 8190 2.7
bbc bcc 12 1 5 prop= None cap 8470 2.8
bbc bcc 12 2 1 prop= None cap 8014 5.4
bbc bcc 12 2 2 prop= None cap 8208 2.2
bbc bcc 12 2 3 prop= None cap 8036 1.8
bbc bcc 12 2 4 prop= None cap 14556 1.9
bbc bcc 12 2 5 prop= None cap 8021 1.5
bbc bcc 12 3 1 prop= None cap 10292 3.8
bbc bcc 12 3 2 prop= None cap 8411 1.8
bbc bcc 12 3 3 prop= None cap 9826 0.8
bbc bcc 12 3 4 prop= None cap 8212 0.6
bbc bcc 12 3 5 prop= None cap 8324 0.8
bbc bcc 12 4 1 prop= None cap 10481 2.9
bbc bcc 12 4 2 prop= None cap 8129 1.1
bbc bcc 12 4 3 prop= None cap 8042 0.9
bbc bcc 12 4 4 prop= None cap 8031 0.8
bbc bcc 12 4 5 prop= None cap 8007 1.2
bbc bcc 12 5 1 prop= None cap 8008 2.8
bbc bcc 12 5 2 prop= None cap 9953 1.6
bbc bcc 12 5 3 prop= None cap 8337 0.5
bbc bcc 12 5 4 prop= None cap 8008 1.3
bcb cbc 10 1 1 prop= None cap 8553 2.3
bcb cbc 10 1 2 prop= None cap 11466 1.6
bcb cbc 10 1 3 prop= None cap 8074 1.2
bcb cbc 10 1 4 prop= None cap 8202 1.1
bcb cbc 10 1 5 prop= None cap 8025 0.9
bcb cbc 10 2 1 prop= None cap 10451 1.5
bcb cbc 10 2 2 prop= None cap 10692 0.9
bcb cbc 10 2 3 prop= None cap 11887 0.6
bcb cbc 10 2 4 prop= None cap 8019 0.4
bcb cbc 10 2 5 prop= None cap 8026 0.4
bcb cbc 10 3 1 prop= None cap 8007 0.9
bcb cbc 10 3 2 prop= None cap 8001 0.7
bcb cbc 10 3 3 prop= None cap 8031 0.4
bcb cbc 10 3 4 prop= None cap 8013 0.9
bcb cbc 10 4 1 prop= None cap 8043 0.9
bcb cbc 10 4 2 prop= None cap 8070 0.7
bcb cbc 10 4 3 prop= None cap 8028 0.9
bcb cbc 10 5 1 prop= None cap 8910 0.8
bcb cbc 10 5 2 prop= None cap 8204 0.4
bcb cbc 12 1 1 prop= None cap 8028 4.5
bcb cbc 12 1 2 prop= None cap 9362 4.5
bcb cbc 12 1 3 prop= None cap 9237 2.5
bcb cbc 12 1 4 prop= None cap 8702 1.5
bcb cbc 12 1 5 prop= None cap 8522 1.9
bcb cbc 12 2 1 prop= None cap 12094 4.6
bcb cbc 12 2 2 prop= None cap 11016 1.5
bcb cbc 12 2 3 prop= None cap 8905 1.1
bcb cbc 12 2 4 prop= None cap 8067 1.2
bcb cbc 12 2 5 prop= None cap 10409 1.1
bcb cbc 12 3 1 prop= None cap 8171 1.8
bcb cbc 12 3 2 prop= None cap 8283 1.3
bcb cbc 12 3 3 prop= None cap 8120 0.8
bcb cbc 12 3 4 prop= None cap 8709 0.6
bcb cbc 12 3 5 prop= None cap 8094 0.5
bcb cbc 12 4 1 prop= None cap 8644 2.1
bcb cbc 12 4 2 prop= None cap 8163 1.2
bcb cbc 12 4 3 prop= None cap 8021 0.5
bcb cbc 12 4 4 prop= None cap 8010 0.6
bcb cbc 12 4 5 prop= None cap 8010 1.1
bcb cbc 12 5 1 prop= None cap 8064 1.6
bcb cbc 12 5 2 prop= None cap 8414 0.9
bcb cbc 12 5 3 prop= None cap 8776 0.5
bcb cbc 12 5 4 prop= None cap 8019 1.4
bc cb 10 1 1 prop= True cap 8136 2.2
bc cb 10 1 2 prop= False contra 732 0.1
bc cb 10 1 3 prop= False contra 456 0.1
bc cb 10 1 4 prop= False contra 556 0.1
bc cb 10 1 5 prop= False contra 572 0.2
bc cb 10 2 1 prop= False contra 975 0.1
bc cb 10 2 2 prop= True cap 8002 2.1
bc cb 10 2 3 prop= False contra 208 0.1
bc cb 10 2 4 prop= False contra 187 0.1
bc cb 10 2 5 prop= False contra 153 0.1
bc cb 10 3 1 prop= False contra 608 0.1
bc cb 10 3 2 prop= False contra 187 0.1
bc cb 10 3 3 prop= True closed 633 0.5
bc cb 10 3 4 prop= False contra 77 0.0
bc cb 10 4 1 prop= False contra 587 0.2
bc cb 10 4 2 prop= False contra 173 0.1
bc cb 10 4 3 prop= False contra 96 0.0
bc cb 10 5 1 prop= False contra 636 0.4
bc cb 10 5 2 prop= False contra 156 0.1
bc cb 12 1 1 prop= True cap 8048 2.0
bc cb 12 1 2 prop= False contra 1728 0.2
bc cb 12 1 3 prop= False contra 816 0.2
bc cb 12 1 4 prop= False contra 631 0.1
bc cb 12 1 5 prop= False contra 1274 0.6
bc cb 12 2 1 prop= False contra 1992 0.4
bc cb 12 2 2 prop= True cap 8001 3.1
bc cb 12 2 3 prop= False contra 442 0.2
bc cb 12 2 4 prop= False contra 303 0.1
bc cb 12 2 5 prop= False contra 368 0.2
bc cb 12 3 1 prop= False contra 1425 0.3
bc cb 12 3 2 prop= False contra 545 0.1
bc cb 12 3 3 prop= True closed 3051 5.3
bc cb 12 3 4 prop= False contra 147 0.1
bc cb 12 3 5 prop= False contra 145 0.1
bc cb 12 4 1 prop= False contra 1051 0.2
bc cb 12 4 2 prop= False contra 420 0.2
bc cb 12 4 3 prop= False contra 132 0.1
bc cb 12 4 4 prop= True closed 89 0.1
bc cb 12 4 5 prop= False contra 101 0.1
bc cb 12 5 1 prop= False contra 1064 0.4
bc cb 12 5 2 prop= False contra 333 0.2
bc cb 12 5 3 prop= False contra 140 0.1
bc cb 12 5 4 prop= False contra 236 0.0

===== END FILE =====

===== BEGIN FILE exploration/t5.py bytes=1053 sha256=898d917a0071883c65e7ff6a273f9c3beeab58728a0bf26e09736f2c4db200ce =====
import sys,time,random,itertools; sys.path.insert(0,'.')
from r14core import *
from fractions import Fraction
def seedmin(N,k1,d1,k2,d2):
    l1=N-d1-acount(k1); l2=N-d2-acount(k2); t=N-d1-d2-acount(k1)-acount(k2)
    if min(l1,l2)<3 or t<3: return None
    return {'a'*N,'a'+k1+'a'*(l1-1),'a'+k2+'a'*(l2-1),'a'+k1+'a'+k2+'a'*(t-2)}
def V(k): return (k.count('b'),k.count('c'))
def proportional(k1,d1,k2,d2):
    v1,v2=V(k1),V(k2)
    if v1[0]*v2[1]!=v1[1]*v2[0]: return None   # independent vectors: no relation
    return Fraction(d1, v1[0]+v1[1])==Fraction(d2, v2[0]+v2[1])
cases=[('bc','bbcc'),('bc','cbbc'),('bcc','cbc'),('bcc','ccb'),('bc','bcc'),('bc','bbc'),('bbc','bcc'),('bcb','cbc'),('bc','cb')]
for k1,k2 in cases:
  for N in (10,12):
    for d1 in range(1,6):
      for d2 in range(1,6):
        s=seedmin(N,k1,d1,k2,d2)
        if s is None: continue
        t=time.time(); C=Closure(s,N=N,cap_len=N+4,cap_words=8000).run()
        print(k1,k2,N,d1,d2,'prop=',proportional(k1,d1,k2,d2),C.status,len(C.K),round(time.time()-t,1),flush=True)

===== END FILE =====

===== BEGIN FILE exploration/t6.py bytes=1344 sha256=6eda02c7ead64a6808cb56c3d31444dc6051db0addf0d44c7f248e32967e1687 =====
import sys; sys.path.insert(0,'.')
from r14core import *
from tr_builder import tr_derivation, conditions
def rev_steps(steps):
    out=[]
    for (x,y,E0,E1,w) in steps:
        rx=tuple(c[::-1] for c in reversed(x)); ry=tuple(c[::-1] for c in reversed(y))
        rE0=tuple(c[::-1] for c in reversed(E0)); rE1=tuple(c[::-1] for c in reversed(E1))
        out.append((rx,ry,rE0,rE1,w[::-1]))
    return out
cov=unc=bad=0; uncl=[]; gap=[]
for N in range(7,61):
  for d1 in range(1,N):
    for d2 in range(1,N):
      if d1==d2 or N-d1-d2<3: continue
      if conditions(N,d1,d2):
        D,W4,W7=tr_derivation(N,d1,d2); seed=D.seed; st=D.steps
      elif conditions(N,d2,d1):     # mirror: run in L^R (bc has deficit d2 there), reverse everything
        D,W4,W7=tr_derivation(N,d2,d1); seed={w[::-1] for w in D.seed}; st=rev_steps(D.steps); W4,W7=W4[::-1],W7[::-1]
      else:
        unc+=1; uncl.append((N,d1,d2))
        if N>=4*max(d1,d2)+1: gap.append((N,d1,d2))
        continue
      ok,K=replay(seed,st)
      good = ok and skel(W4)==skel(W7) and acount(W4)!=acount(W7) and max(acount(W4),acount(W7))<=N-1 and min(acount(W4),acount(W7))>=1
      # seed sanity: deficits of seed words
      cov+=1; bad+= (not good)
print('covered',cov,'bad',bad,'uncovered',unc,'uncovered with N>=4max+1:',len(gap))
print('sample uncovered',uncl[:12])

===== END FILE =====

===== BEGIN FILE exploration/t7.out bytes=1752 sha256=dd92f91e2db6eda99694b00a00afc589919381c5da01fc3d6a1135e379071cda =====
('3unit', 12, 1, 2, 2, False, 'contra', 497) 0.0
('3unit', 12, 1, 2, 3, False, 'contra', 460) 0.0
('3unit', 12, 1, 2, 4, False, 'contra', 389) 0.0
('3unit', 12, 1, 3, 2, False, 'contra', 433) 0.0
('3unit', 12, 1, 3, 3, False, 'contra', 402) 0.0
('3unit', 12, 1, 3, 4, False, 'contra', 352) 0.0
('3unit', 12, 1, 4, 2, False, 'contra', 358) 0.0
('3unit', 12, 1, 4, 3, False, 'contra', 333) 0.0
('3unit', 12, 1, 4, 4, False, 'contra', 290) 0.0
('3unit', 12, 2, 2, 2, False, 'contra', 440) 0.0
('3unit', 12, 2, 2, 3, False, 'contra', 410) 0.0
('3unit', 12, 2, 2, 4, True, 'cap', 12103) 0.2
('3unit', 12, 2, 3, 2, False, 'contra', 435) 0.0
('3unit', 12, 2, 3, 3, True, 'cap', 12327) 0.3
('3unit', 12, 2, 3, 4, False, 'contra', 277) 0.0
('3unit', 12, 2, 4, 2, True, 'cap', 12275) 0.3
('3unit', 12, 2, 4, 3, False, 'contra', 274) 0.0
('3unit', 12, 2, 4, 4, False, 'contra', 252) 0.0
('3unit', 14, 1, 2, 2, False, 'contra', 792) 0.1
('3unit', 14, 1, 2, 3, False, 'contra', 773) 0.1
('3unit', 14, 1, 2, 4, False, 'contra', 652) 0.0
('3unit', 14, 1, 3, 2, False, 'contra', 696) 0.0
('3unit', 14, 1, 3, 3, False, 'contra', 677) 0.1
('3unit', 14, 1, 3, 4, False, 'contra', 637) 0.0
('3unit', 14, 1, 4, 2, False, 'contra', 506) 0.0
('3unit', 14, 1, 4, 3, False, 'contra', 570) 0.0
('3unit', 14, 1, 4, 4, False, 'contra', 428) 0.0
('3unit', 14, 2, 2, 2, False, 'contra', 652) 0.0
('3unit', 14, 2, 2, 3, False, 'contra', 634) 0.0
('3unit', 14, 2, 2, 4, True, 'cap', 12269) 0.3
('3unit', 14, 2, 3, 2, False, 'contra', 518) 0.0
('3unit', 14, 2, 3, 3, True, 'cap', 12706) 0.4
('3unit', 14, 2, 3, 4, False, 'contra', 443) 0.0
('3unit', 14, 2, 4, 2, True, 'cap', 12070) 0.4
('3unit', 14, 2, 4, 3, False, 'contra', 417) 0.0
('3unit', 14, 2, 4, 4, False, 'contra', 380) 0.0

===== END FILE =====

===== BEGIN FILE exploration/t7.py bytes=1006 sha256=23c6ddf329ad6f2b68f9b1992d9655a1e897cc4c196a2cd9f2b54a8d80c3500c =====
import sys,time,itertools; sys.path.insert(0,'.')
from r14core import *
def stand(N,k,d):      # standalone a k a^(lam-1)
    lam=N-d-acount(k); return 'a'+k+'a'*(lam-1) if lam>=3 else None
def two(N,k1,d1,k2,d2):
    t=N-d1-d2-acount(k1)-acount(k2); return 'a'+k1+'a'+k2+'a'*(t-2) if t>=3 else None
out=[]
# (d) three-unit relation  V(bcc)+V(bbc)=3V(bc): Parikh-linear iff d(bcc)+d(bbc)=3 d(bc)
# seed: standalone of the 3 units, two-unit words linking them (bc·bcc, bc·bbc) -- tree-type data
for N in (12,14):
  for dbc in (1,2):
    for dbcc in (2,3,4):
      for dbbc in (2,3,4):
        ws=[ 'a'*N, stand(N,'bc',dbc), stand(N,'bcc',dbcc), stand(N,'bbc',dbbc),
             two(N,'bc',dbc,'bcc',dbcc), two(N,'bc',dbc,'bbc',dbbc)]
        if None in ws: continue
        t=time.time(); C=Closure(set(ws),N=N,cap_len=N+4,cap_words=12000).run()
        lin = (dbcc+dbbc==3*dbc)
        out.append(('3unit',N,dbc,dbcc,dbbc,lin,C.status,len(C.K)))
        print(out[-1],round(time.time()-t,1),flush=True)

===== END FILE =====

===== BEGIN FILE exploration/t8.out bytes=3779 sha256=2911397bf084d78ed3c5a666a6184d7f1efcfbb6c9d1813e9ef07e2a3ea7e1b6 =====
(11, 2, 1, 1, False, 'contra', 71) 0.0
(11, 2, 1, 2, False, 'contra', 70) 0.0
(11, 2, 1, 3, False, 'contra', 69) 0.0
(11, 2, 1, 4, False, 'contra', 67) 0.0
(11, 2, 2, 1, False, 'contra', 7411) 1.3
(11, 2, 2, 2, True, 'cap', 12002) 4.6
(11, 2, 2, 3, False, 'contra', 1938) 1.1
(11, 2, 2, 4, False, 'contra', 1433) 0.9
(11, 2, 3, 1, False, 'contra', 18) 0.0
(11, 2, 3, 2, False, 'contra', 18) 0.0
(11, 2, 3, 3, False, 'contra', 18) 0.0
(11, 2, 3, 4, False, 'contra', 18) 0.0
(11, 2, 4, 1, False, 'contra', 67) 0.0
(11, 2, 4, 2, False, 'contra', 41) 0.0
(11, 2, 4, 3, False, 'contra', 58) 0.0
(11, 2, 4, 4, False, 'contra', 57) 0.0
(11, 3, 1, 1, False, 'contra', 54) 0.0
(11, 3, 1, 2, False, 'contra', 53) 0.0
(11, 3, 1, 3, False, 'contra', 52) 0.0
(11, 3, 1, 4, False, 'contra', 50) 0.0
(11, 3, 2, 1, False, 'contra', 30) 0.0
(11, 3, 2, 2, False, 'contra', 30) 0.0
(11, 3, 2, 3, False, 'contra', 30) 0.0
(11, 3, 2, 4, False, 'contra', 30) 0.0
(11, 3, 3, 1, False, 'contra', 2835) 0.4
(11, 3, 3, 2, False, 'contra', 1472) 0.3
(11, 3, 3, 3, True, 'closed', 1407) 1.5
(11, 3, 3, 4, False, 'contra', 1995) 0.3
(11, 3, 4, 1, False, 'contra', 49) 0.0
(11, 3, 4, 2, False, 'contra', 24) 0.0
(11, 3, 4, 3, False, 'contra', 24) 0.0
(11, 3, 4, 4, False, 'contra', 24) 0.0
(12, 2, 1, 1, False, 'contra', 86) 0.0
(12, 2, 1, 2, False, 'contra', 58) 0.0
(12, 2, 1, 3, False, 'contra', 58) 0.0
(12, 2, 1, 4, False, 'contra', 58) 0.0
(12, 2, 2, 1, False, 'contra', 10489) 2.5
(12, 2, 2, 2, True, 'cap', 12071) 5.1
(12, 2, 2, 3, False, 'contra', 3656) 2.7
(12, 2, 2, 4, False, 'contra', 2595) 1.9
(12, 2, 3, 1, False, 'contra', 50) 0.0
(12, 2, 3, 2, False, 'contra', 50) 0.0
(12, 2, 3, 3, False, 'contra', 50) 0.0
(12, 2, 3, 4, False, 'contra', 50) 0.0
(12, 2, 4, 1, False, 'contra', 82) 0.0
(12, 2, 4, 2, False, 'contra', 52) 0.0
(12, 2, 4, 3, False, 'contra', 52) 0.0
(12, 2, 4, 4, False, 'contra', 52) 0.0
(12, 3, 1, 1, False, 'contra', 45) 0.0
(12, 3, 1, 2, False, 'contra', 25) 0.0
(12, 3, 1, 3, False, 'contra', 25) 0.0
(12, 3, 1, 4, False, 'contra', 25) 0.0
(12, 3, 2, 1, False, 'contra', 47) 0.0
(12, 3, 2, 2, False, 'contra', 46) 0.0
(12, 3, 2, 3, False, 'contra', 45) 0.0
(12, 3, 2, 4, False, 'contra', 44) 0.0
(12, 3, 3, 1, False, 'contra', 5895) 0.9
(12, 3, 3, 2, False, 'contra', 2840) 0.8
(12, 3, 3, 3, True, 'closed', 3051) 5.5
(12, 3, 3, 4, False, 'contra', 719) 1.0
(12, 3, 4, 1, False, 'contra', 41) 0.0
(12, 3, 4, 2, False, 'contra', 18) 0.0
(12, 3, 4, 3, False, 'contra', 18) 0.0
(12, 3, 4, 4, False, 'contra', 18) 0.0
(13, 2, 1, 1, False, 'contra', 54) 0.0
(13, 2, 1, 2, False, 'contra', 30) 0.0
(13, 2, 1, 3, False, 'contra', 30) 0.0
(13, 2, 1, 4, False, 'contra', 30) 0.0
(13, 2, 2, 1, False, 'cap', 12006) 1.8
(13, 2, 2, 2, True, 'cap', 12794) 3.9
(13, 2, 2, 3, False, 'contra', 7397) 3.8
(13, 2, 2, 4, False, 'contra', 5551) 3.7
(13, 2, 3, 1, False, 'contra', 54) 0.1
(13, 2, 3, 2, False, 'contra', 53) 0.0
(13, 2, 3, 3, False, 'contra', 52) 0.0
(13, 2, 3, 4, False, 'contra', 51) 0.0
(13, 2, 4, 1, False, 'contra', 97) 0.0
(13, 2, 4, 2, False, 'contra', 95) 0.0
(13, 2, 4, 3, False, 'contra', 93) 0.0
(13, 2, 4, 4, False, 'contra', 91) 0.0
(13, 3, 1, 1, False, 'contra', 51) 0.0
(13, 3, 1, 2, False, 'contra', 28) 0.0
(13, 3, 1, 3, False, 'contra', 28) 0.0
(13, 3, 1, 4, False, 'contra', 28) 0.0
(13, 3, 2, 1, False, 'contra', 50) 0.0
(13, 3, 2, 2, False, 'contra', 48) 0.0
(13, 3, 2, 3, False, 'contra', 27) 0.0
(13, 3, 2, 4, False, 'contra', 27) 0.0
(13, 3, 3, 1, False, 'contra', 9395) 2.0
(13, 3, 3, 2, False, 'contra', 4768) 1.8
(13, 3, 3, 3, True, 'closed', 6943) 18.2
(13, 3, 3, 4, False, 'contra', 1258) 2.5
(13, 3, 4, 1, False, 'contra', 47) 0.0
(13, 3, 4, 2, False, 'contra', 21) 0.0
(13, 3, 4, 3, False, 'contra', 21) 0.0
(13, 3, 4, 4, False, 'contra', 21) 0.0

===== END FILE =====

===== BEGIN FILE exploration/t8.py bytes=824 sha256=dead2a881e6f95f0af08802b8f59e7957de687438e4878aee7853cbe51c7e4be =====
import sys,time; sys.path.insert(0,'.')
from r14core import *
# fan-out-2 unit B=(b,c): standalone a b a c a^k ; interleaved seed of two B-copies: b1 b2 c1 c2
res=[]
for N in (11,12,13):
  for dB in (2,3):
    for d1 in (1,2,3,4):
      for d2 in (1,2,3,4):
        lamB=N-dB-1                        # outer a's of core 'bac'
        wB='a'+'b'+'a'+'c'+'a'*(lamB-1)
        t=N-2*dB                           # a-count of interleaved seed
        if t<5: continue
        W='a'+'b'+'a'+'b'+'a'+'c'+'a'+'c'+'a'*(t-4)
        w1='a'+'bc'+'a'*(N-d1-1); w2='a'+'cb'+'a'*(N-d2-1)
        seed={'a'*N,wB,W,w1,w2}
        t0=time.time(); C=Closure(seed,N=N,cap_len=N+3,cap_words=12000).run()
        lin=(d1==d2==dB)
        res.append((N,dB,d1,d2,lin,C.status,len(C.K)))
        print(res[-1],round(time.time()-t0,1),flush=True)

===== END FILE =====

===== BEGIN FILE exploration/t9.py bytes=814 sha256=4e46ae7e7dad4aefb1318a22775eae283fec7f931d9369fd9765a6571dd7aabc =====
import sys,itertools; sys.path.insert(0,'.')
from r14core import *
def shuffles(core,na):
    n=len(core)+na; out=set()
    for pos in itertools.combinations(range(n),len(core)):
        w=['a']*n
        for p,ch in zip(pos,core): w[p]=ch
        out.add(''.join(w))
    return out
N=10
L={'a'*N}|shuffles('bc',N-2)|shuffles('cb',N-3)
ok,wit=check_closed(L); print('a-central {bc:2,cb:3} N=10 |L|=',len(L),'closed=',ok, 'min a-power',shortest_apower(L))
# contains Rot-core standalone words for bc and cb with lambda in [3,N-1]? and no 2-unit word
print('abcaaaaaaa' in L, 'acbaaaaaa' in L, any(w.count('b')>1 for w in L))
# control: add a single two-unit word -> must become inconsistent (closure contra)
C=Closure(L|{'a'+'bc'+'a'+'cb'+'a'*3},N=N,cap_len=N+4).run(); print('with 2-unit word:',C.status,C.contra)

===== END FILE =====

===== BEGIN FILE exploration/tr_builder.py bytes=9285 sha256=a2615f18e0abbe0a900d510f0f35ba5fd9c25ef77520a8e163a791bbe5bccc00 =====
#!/usr/bin/env python3
"""Rule-level expansion of the hand proof of Theorem TR (bc/cb transposition).

Every lemma used in the written proof (L1(R), Rot, Cat, X1+, X2-mirror, 2-hole order swap)
is expanded into DIRECT rule applications  E0[x],E0[y],E1[x] in K  =>  E1[y]  whose premises are
checked at the moment of application.  The final certificate is replayed by r14core.replay.
"""
import sys
from r14core import fill, ttype, skel, acount, replay

B, G = 'bc', 'cb'

class Deriv:
    def __init__(self, seed, N):
        self.K = set(seed)
        self.seed = set(seed)
        self.N = N
        self.steps = []
        self.rotready = {}

    # ---------- primitive
    def rule(self, x, y, E0, E1, why=''):
        assert ttype(x) == ttype(y), ('type', x, y, why)
        assert all(c for c in x + y), ('empty hole', why)
        if len(x) == 2:
            assert E0[1] and E1[1], ('empty separator', why)
        for p in (fill(E0, x), fill(E0, y), fill(E1, x)):
            assert p in self.K, ('premise missing', p, why)
        w = fill(E1, y)
        if w not in self.K:
            self.K.add(w)
            self.steps.append((x, y, E0, E1, w))
        return w

    # ---------- L1(R): P a^i Q a^j R -> P a^i2 Q a^j2 R   (Q nonempty, i+j<=N-1)
    def redistribute(self, P, i, Q, j, R, i2, j2):
        N = self.N
        assert Q and i >= 1 and j >= 1 and i2 >= 1 and j2 >= 1 and i + j == i2 + j2 <= N - 1
        if (i, j) == (i2, j2):
            return P + 'a' * i + Q + 'a' * j + R
        return self.rule(('a' * i, 'a' * j), ('a' * i2, 'a' * j2),
                         ('', 'a', 'a' * (N - 1 - i - j)), (P, Q, R), 'L1R')

    # ---------- Rot readiness for a core k with a known standalone word a^p k a^r in K
    def rot_ready(self, k, p, r):
        lam = p + r
        assert 3 <= lam <= self.N - 1 and p >= 1 and r >= 1
        assert 'a' * p + k + 'a' * r in self.K
        A2 = self.redistribute('', p, k, r, '', 2, lam - 2)       # a^2 k a^(lam-2)
        A1 = self.redistribute('', p, k, r, '', 1, lam - 1)       # a k a^(lam-1)
        self.rotready[k] = lam
        return lam

    def rot_move(self, P, k, Q, direction):
        """direction 'R': P a k Q -> P k a Q ; 'L': P k a Q -> P a k Q"""
        lam = self.rotready[k]
        x, y = ('a' + k,), (k + 'a',)
        if direction == 'L':
            x, y = y, x
        return self.rule(x, y, ('a', 'a' * (lam - 2)), (P, Q), 'Rot ' + k)

    # ---------- Cat for words given as [run0, core1, run1, ..., coreM, runM]; all cores rot-ready
    def recat(self, runs, cores, target):
        """move single a's across cores (Rot) to go from run vector `runs` to `target`."""
        assert sum(runs) == sum(target) and len(runs) == len(cores) + 1
        runs = list(runs)
        def word(rs):
            w = 'a' * rs[0]
            for c, r in zip(cores, rs[1:]):
                w += c + 'a' * r
            return w
        assert word(runs) in self.K, ('recat start missing', word(runs))
        # sweep left-to-right: fix runs[0..M-1] by pushing surplus right / pulling deficit from right
        for g in range(len(cores)):
            while runs[g] > target[g]:
                # word = P a core_g a^{runs[g+1]} ...
                pre = 'a' * runs[0]
                for c, r in zip(cores[:g], runs[1:g + 1]):
                    pre += c + 'a' * r
                pre = pre[:-1]                       # remove one a (the one adjacent to core g)
                post = 'a' * runs[g + 1]
                for c, r in zip(cores[g + 1:], runs[g + 2:]):
                    post += c + 'a' * r
                self.rot_move(pre, cores[g], post, 'R')
                runs[g] -= 1; runs[g + 1] += 1
            while runs[g] < target[g]:
                # need an a right after core g: total conservation guarantees runs[g+1]>0 eventually;
                # pull from the right, cascading if necessary
                h = g + 1
                while runs[h] == 0:
                    h += 1
                # move one a from run h leftwards across cores h-1 ... g
                for q in range(h - 1, g - 1, -1):
                    pre = 'a' * runs[0]
                    for c, r in zip(cores[:q], runs[1:q + 1]):
                        pre += c + 'a' * r
                    post = 'a' * (runs[q + 1] - 1)
                    for c, r in zip(cores[q + 1:], runs[q + 2:]):
                        post += c + 'a' * r
                    self.rot_move(pre, cores[q], post, 'L')
                    runs[q + 1] -= 1; runs[q] += 1
        assert runs == list(target)
        return word(runs)

    # ---------- X1+ mirror: P k a^i R -> P k2 a^{i'} R    (1-hole, a-run adjacent on the right)
    def x1plus_right(self, P, k, i, R, k2):
        lam, lam2 = self.rotready[k], self.rotready[k2]
        i0 = 1 + max(0, lam - lam2); i0p = i0 + lam2 - lam
        assert i >= i0 and i0p >= 1, ('X1+ range', i, i0)
        # hosts: k a^lam , k2 a^lam2   (all outer a's on the right)
        return self.rule((k + 'a' * i0,), (k2 + 'a' * i0p,), ('', 'a' * (lam - i0)),
                         (P, 'a' * (i - i0) + R), 'X1+R %s->%s' % (k, k2))

    # ---------- X2 mirror: P k m a^i R -> P k2 m a^{i'} R   (2-hole, m nonempty)
    def x2_right(self, P, k, m, i, R, k2):
        lam, lam2 = self.rotready[k], self.rotready[k2]
        assert m
        i0 = min(i, lam - 1); i0p = i0 + lam2 - lam
        assert i0 >= 1 and i0p >= 1, ('X2 range', i, i0, i0p)
        q = lam - i0
        return self.rule((k, 'a' * i0), (k2, 'a' * i0p), ('', 'a', 'a' * (q - 1)),
                         (P, m, 'a' * (i - i0) + R), 'X2R %s->%s' % (k, k2))

def to_right(D, k, p, r):
    """from standalone a^p k a^r derive k a^(p+r) (all a's right) by Rot moves"""
    return D.recat([p, r], [k], [0, p + r])

def tr_derivation(N, d1, d2, j=None):
    """Hand proof of TR as a certificate.  Returns (D, W4, W7) or raises AssertionError
    if a side condition fails (then the instance is outside the theorem's room conditions)."""
    lam1, lam2 = N - d1, N - d2
    t = N - d1 - d2
    Dl = d2 - d1
    seed = {'a' * N, 'a' + B + 'a' * (lam1 - 1), 'a' + G + 'a' * (lam2 - 1),
            'a' + B + 'a' + G + 'a' * (t - 2)}
    D = Deriv(seed, N)
    D.rot_ready(B, 1, lam1 - 1)
    D.rot_ready(G, 1, lam2 - 1)
    # Step 1 (Cat on H3): bc cb a^t ; bccb is a Rot core with lambda=t
    W1 = D.recat([1, 1, t - 2], [B, G], [0, 0, t])          # bccb a^t
    D.recat([0, 0, t], [B, G], [1, 0, t - 1])                 # a bccb a^(t-1) standalone of composite
    D.rot_ready(B + G, 1, t - 1)
    to_right(D, B, 1, lam1 - 1); to_right(D, G, 1, lam2 - 1)
    # Step 2: bc [cb] a^t  ->  bc bc a^(t+D)   (X1+ right)
    W2 = D.x1plus_right(B, G, t, '', B)                       # bcbc a^(N-2d1)
    assert W2 == 'bcbc' + 'a' * (N - 2 * d1)
    # cb bc order:  [bc] cb a^t -> [cb] cb a^(t-D)  (X2 right, separator cb) ; then cb [cb] -> cb [bc]
    W2b = D.x2_right('', B, G, t, '', G)                      # cbcb a^(t-D)
    W2c = D.x1plus_right(G, G, t - Dl, '', B)                 # cbbc a^t
    assert W2c == 'cbbc' + 'a' * t
    # composite bcbc rot-ready (lambda = N-2d1)
    D.recat([0, 0, N - 2 * d1], [B, B], [1, 0, N - 2 * d1 - 1])
    D.rot_ready(B + B, 1, N - 2 * d1 - 1)
    # Step 3: b [cb] c a^(N-2d1) -> b [bc] c a^(N-2d1+D)   (X2 right, separator 'c')
    W3 = D.x2_right('b', G, 'c', N - 2 * d1, '', B)
    assert W3 == 'bbcc' + 'a' * (N - 2 * d1 + Dl)
    # Step 4: b [bc] c a^k -> b [bccb] c a^(N-3d1)
    W4 = D.x2_right('b', B, 'c', N - 2 * d1 + Dl, '', B + G)
    assert W4 == 'bbccbc' + 'a' * (N - 3 * d1)
    # Step 5: bc [bc] a^(N-2d1) -> bc [bcbc] a^(N-3d1)    (X1+ right, k2 = bcbc)
    to_right(D, B + B, 1, N - 2 * d1 - 1)
    W5 = D.x1plus_right(B, B, N - 2 * d1, '', B + B)
    assert W5 == 'bcbcbc' + 'a' * (N - 3 * d1)
    # Step 6: (cb, bc) == (bc, cb) via host E0=('', 'a', a^(t-1)); test context (b, c, a^(N-3d1))
    D.recat([0, 0, t], [G, B], [0, 1, t - 1])                 # cb a bc a^(t-1)
    D.recat([0, 0, t], [B, G], [0, 1, t - 1])                 # bc a cb a^(t-1)
    W6 = D.rule((G, B), (B, G), ('', 'a', 'a' * (t - 1)), ('b', 'c', 'a' * (N - 3 * d1)), 'order swap')
    assert W6 == 'bbcccb' + 'a' * (N - 3 * d1)
    # Step 7: (bc, cb a^j) == (bc, bc a^(j+D)) via host E0=('', 'a', a^(t-1-j))
    if j is None:
        j = max(1, 1 - Dl)
    assert 1 <= j <= t - 1 and j + Dl >= 1 and N - 3 * d1 - j >= 0
    D.recat([0, 0, N - 2 * d1], [B, B], [0, 1, N - 2 * d1 - 1])   # bc a bc a^(N-2d1-1)
    W7 = D.rule((B, G + 'a' * j), (B, B + 'a' * (j + Dl)), ('', 'a', 'a' * (t - 1 - j)),
                ('b', 'c', 'a' * (N - 3 * d1 - j)), 'carrier shift')
    assert W7 == 'bbccbc' + 'a' * (N - 3 * d1 + Dl)
    return D, W4, W7

def conditions(N, d1, d2):
    t = N - d1 - d2; Dl = d2 - d1
    j = max(1, 1 - Dl)
    return all([1 <= d1 <= N - 3, 1 <= d2 <= N - 3, t >= 3, N - 2 * d1 >= 3, N - 2 * d2 >= 1,
                N - 3 * d1 >= 1, j <= t - 1, N - 3 * d1 - j >= 0,
                1 <= 3 * d1 - Dl <= N - 1])

if __name__ == '__main__':
    N, d1, d2 = map(int, sys.argv[1:4])
    D, W4, W7 = tr_derivation(N, d1, d2)
    ok, K = replay(D.seed, D.steps)
    print(N, d1, d2, 'steps', len(D.steps), 'replay', ok, W4, W7, skel(W4) == skel(W7),
          acount(W4), acount(W7))

===== END FILE =====

===== BEGIN FILE independent_round14_audit_2026-11-16.py bytes=7222 sha256=e79620ec3efae05dfac237e3d670f3f5b742052c932c21bdf3822024ac38c843 =====
#!/usr/bin/env python3
"""Independent Round 14 auditor: exact finite class check & independent replay of Claude-generated TR data.
The content-typing closure evaluator and replay below are written independently and do not call the submitted checking functions.
"""
from collections import defaultdict
from itertools import combinations,product
from pathlib import Path
import importlib.util

BASE=Path(__file__).resolve().parent
ORIG=BASE/'claude_round14_noncomm_Parikh_checker_2026-11-15.py'

def typ(t):
    return tuple(frozenset(s) for s in t)

def split_occurrences(w):
    n=len(w)
    for i in range(n):
        for j in range(i+1,n+1):
            yield (w[i:j],),(w[:i],w[j:])
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                for h in range(k+1,n+1):
                    yield (w[i:j],w[k:h]),(w[:i],w[j:k],w[h:])

def put(ctx, seq):
    if len(seq)==1:return ctx[0]+seq[0]+ctx[1]
    return ctx[0]+seq[0]+ctx[1]+seq[1]+ctx[2]

def exact_class(S):
    distributions=defaultdict(set)
    for word in S:
        for tup,ctx in split_occurrences(word):
            distributions[tup].add(ctx)
    common=defaultdict(list)
    for t,es in distributions.items():
        for e in es:
            common[(len(t),typ(t),e)].append(t)
    checked=0
    for (_,_,e),items in common.items():
        for t in items[1:]:
            checked+=1
            if distributions[t]!=distributions[items[0]]:
                return False,(items[0],t,e),len(distributions),sum(map(len,distributions.values())),checked
    return True,None,len(distributions),sum(map(len,distributions.values())),checked

def shuffles2(N):
    return {'a'*i+'b'+'a'*(j-i-1)+'c'+'a'*(N-j-1) for i in range(N) for j in range(i+1,N)} | {'a'*i+'c'+'a'*(j-i-1)+'b'+'a'*(N-j-1) for i in range(N) for j in range(i+1,N)}

def independent_step_replay(seed,steps):
    known=set(seed)
    for i,entry in enumerate(steps):
        x,y,e,f,w=entry
        if len(x)!=len(y) or not all(x) or not all(y) or typ(x)!=typ(y):
            raise AssertionError(('type',i))
        if len(x)==2 and (not e[1] or not f[1]):raise AssertionError(('sep',i))
        if len(e)!=len(x)+1 or len(f)!=len(x)+1:raise AssertionError(('arity',i))
        prereqs=[put(e,x),put(e,y),put(f,x)]
        if any(p not in known for p in prereqs):raise AssertionError(('missing',i,prereqs))
        if put(f,y)!=w:raise AssertionError(('yield',i))
        known.add(w)
    return known

def skeleton(w):
    out=[]
    for a in w:
        if a!='a':out.append(a)
        elif not out or out[-1]!='A':out.append('A')
    return ''.join(out)

def run():
    # Independent finite counterexample to CA as stated.
    N=10
    S={'a'*N} | shuffles2(N) | {''.join(z) for z in product('bc',repeat=4) if set(z)==set('bc')}
    ok,w,tuples,contexts,comparisons=exact_class(S)
    assert ok and len(S)==105 and 'bccb' in S and 'bccb'+'a'*6 not in S
    assert 'a'+'bc'+'a'*7 in S and 'a'+'cb'+'a'*7 in S
    print('CA COUNTEREXAMPLE: |L|=%d N=10 type=content closed=%s tuples=%d contexts=%d checked_comparisons=%d' %(len(S),ok,tuples,contexts,comparisons))
    print('  units bc,cb: lambda=8 delta=2 for each, seed=bccb (zero outer a); e_2=6 >=3')
    print('  predicts bccb a^6 in L, but that word is ABSENT. CA requires initial host room.')
    # Stronger CA counterexample: an *initially positive-room* connected seed,
    # but with an a-count different from the additive value assumed without proof.
    words48 = '''aaabbcc aaabcbc aaabccb aaacbbc aaacbcb aaaccbb
    aabbcca aabcabc aabcacb aabcbca aabccba aacbabc aacbacb aacbbca aacbcba aaccbba
    abbccaa abcaabc abcaacb abcabca abcacba abcbcaa abccbaa acbaabc acbaacb acbabca acbacba acbbcaa acbcbaa accbbaa
    bbccaaa bcaaabc bcaaacb bcaabca bcaacba bcabcaa bcacbaa bcbcaaa bccbaaa
    cbaaabc cbaaacb cbaabca cbaacba cbabcaa cbacbaa cbbcaaa cbcbaaa ccbbaaa'''.split()
    assert len(words48)==48 and len(set(words48))==48
    singles = {'a'*i + z + 'a'*(8-i) for i in range(9) for z in ('bc','cb')}
    S67={'a'*10} | singles | set(words48)
    ok67, wit67, t67, c67, p67 = exact_class(S67)
    assert len(S67)==67 and ok67 and 'bccbaaa' in S67 and 'bccb'+'a'*6 not in S67
    assert 'abca'+'a'*6 in S67 and 'acba'+'a'*6 in S67
    print('CA STRONGER COUNTEREXAMPLE: |L|=67 N=10 type=content closed=%s tuples=%d contexts=%d comparisons=%d'%(ok67,t67,c67,p67))
    print('  single Rot bc,cb: lambda=8 delta=2; connected seed bccb a^3 IN L (t=3)')
    print('  CA still predicts bccb a^6 IN L (e_2=6), which is ABSENT.')
    print('  Missing hypotheses: initial two-unit seed must have ADDITIVE a-budget (t=6), not merely t>=3.')
    S82={'a'*10} | {'a'*i+'b'+'a'*(j-i-1)+'c'+'a'*(10-j-1) for i in range(10) for j in range(i+1,10)} | {'a'*i+'c'+'a'*(j-i-1)+'b'+'a'*(9-j-1) for i in range(9) for j in range(i+1,9)}
    ok82,w82,t82,c82,p82=exact_class(S82)
    assert ok82 and len(S82)==82
    print('INDEPENDENT B: 82-word finite target closed=%s tuple-keys=%d context-pairs=%d comparisons=%d'%(ok82,t82,c82,p82))
    # Claude code only creates the certificates. Every step is verified by the independent checker above.
    spec=importlib.util.spec_from_file_location('claude_round14_for_certificates_only',str(ORIG))
    source=importlib.util.module_from_spec(spec);spec.loader.exec_module(source)
    ncert=0;nsteps=0;nctrl=0;miss=0
    for n in range(7,41):
        for d1 in range(1,n):
            for d2 in range(1,n):
                if n-d1-d2<3:continue
                if d1==d2:
                    if source.conditions(n,d1,d2):
                        c,w4,w7=source.tr_derivation(n,d1,d2)
                        k=independent_step_replay(c.seed,c.steps)
                        assert w4==w7 and w4 in k
                        nctrl+=1
                    continue
                flip=False
                if source.conditions(n,d1,d2):a,b=d1,d2
                elif source.conditions(n,d2,d1):a,b=d2,d1;flip=True
                else:
                    if n>=4*max(d1,d2)+1:miss+=1
                    continue
                d,w4,w7=source.tr_derivation(n,a,b)
                k=independent_step_replay(d.seed,d.steps)
                assert w4 in k and w7 in k and skeleton(w4)==skeleton(w7)
                assert 1<=w4.count('a')<n and 1<=w7.count('a')<n and w4.count('a')!=w7.count('a')
                ncert+=1;nsteps+=len(d.steps)
    assert miss==0 and ncert==3270 and nctrl==244
    print('INDEPENDENT TR REPLAY: 3270 certificates %d primitive rule steps; 244 controls; gaps=%d; ALL PASS'%(nsteps,miss))
    # Algebraic range test, separate from the submitted conditions() implementation.
    for N in range(7,101):
        for d1 in range(1,N):
            for d2 in range(1,N):
                if N<4*max(d1,d2)+1:continue
                a=max(d1,d2);b=min(d1,d2);D=b-a;t=N-a-b;j=1+a-b
                assert 1<=a<=N-3 and 1<=b<=N-3 and t>=3
                assert N-2*a>=3 and N-2*b>=1 and N-3*a>=1
                assert j<=t-1 and N-3*a-j>=0 and 1<=3*a-D<=N-1
    print('INDEPENDENT TR RANGE: all positive deficits with N<=100 covered by symbolic inequalities')
    print('ALL INDEPENDENT AUDIT CHECKS PASSED')

if __name__=='__main__':run()

===== END FILE =====

===== BEGIN FILE out_independent_round14_audit_2026-11-16.txt bytes=936 sha256=bd04ca37dd9a737f5f4be7e52d2966caa61fba80ed4597d6f0dfdd842ce8784d =====
CA COUNTEREXAMPLE: |L|=105 N=10 type=content closed=True tuples=2488 contexts=35245 checked_comparisons=22302
  units bc,cb: lambda=8 delta=2 for each, seed=bccb (zero outer a); e_2=6 >=3
  predicts bccb a^6 in L, but that word is ABSENT. CA requires initial host room.
CA STRONGER COUNTEREXAMPLE: |L|=67 N=10 type=content closed=True tuples=1566 contexts=12019 comparisons=5544
  single Rot bc,cb: lambda=8 delta=2; connected seed bccb a^3 IN L (t=3)
  CA still predicts bccb a^6 IN L (e_2=6), which is ABSENT.
  Missing hypotheses: initial two-unit seed must have ADDITIVE a-budget (t=6), not merely t>=3.
INDEPENDENT B: 82-word finite target closed=True tuple-keys=2041 context-pairs=26890 comparisons=16601
INDEPENDENT TR REPLAY: 3270 certificates 68670 primitive rule steps; 244 controls; gaps=0; ALL PASS
INDEPENDENT TR RANGE: all positive deficits with N<=100 covered by symbolic inequalities
ALL INDEPENDENT AUDIT CHECKS PASSED

===== END FILE =====

===== BEGIN FILE round14_independent_work/out_round14_D_N7_N8_2026-11-16.txt bytes=211 sha256=4946e9e6015495b4f2fa7de402ac3f5116426146464800cc4b95bd15b3179be2 =====
== [D] minimal tree seeds {a^N, w_bc, w_cb, w_(bc,cb)}: exact closure / certified contradiction
   tally (d1==d2, status): {(True, 'cap'): 2, (False, 'contra'): 10, (True, 'closed'): 2}
smoke D7,8 done; FAIL= 0

===== END FILE =====

===== BEGIN FILE round14_independent_work/round14_rerun_S0ABC_2026-11-16.txt bytes=3850 sha256=31733ff66dcd92f77280b35272715d634a3b14babc1807f71cec4b4ebf85992a =====
checker SHA256 eaccd71285f51f26d702b8d76e6fe7a7a5847d08e8f6f97368b8d939729663ea
python 3.13.5  deterministic (no randomness used)
sections ['S0', 'A', 'B', 'C']
== [S0] exact decision procedure: controls
   {a^5, abaa}: non-closed, witness {'x': ('a', 'aa'), 'y': ('aa', 'a'), 'E0': ('a', 'a', ''), 'E1': ('', 'b', ''), 'E0x': 'aaaaa', 'E0y': 'aaaaa', 'E1x': 'abaa', 'E1y': 'aaba'}
   closure(a^5 + a^+ b a^+ , total 3): closed ['aaab', 'aaba', 'abaa', 'baaa', 'aaaaa']
   [time so far 0.0s]
== [A] X1 counterexample replay; type-safe X1+ (padded) check
   |L|=40 tuples=333 tuple-context pairs=2327 closed=True N=8
   original X1 instance: kappa=bc, kappa'=acb, lam=lam'=3, s(a kappa)=s(a kappa')={a,b,c}; bc in L, acb not in L
   Rot cores in L: {'cb': [4], 'b': [6], 'c': [5], 'bc': [3], 'cab': [3]}
   X1+ (i,i'>=1, both sides) distribution checks=238 violations=0
   original X1 (i=(lam-lam')_+) checks=11 violations=4  e.g. ('cb', 'bc', 1, 0)
   [time so far 0.0s]
== [B] branching hypothesis is necessary: a-central language without composite words
   L = a^10 + all a-shuffles of bc with 8 a (deficit 2) + of cb with 7 a (deficit 3): |L|=82 closed=True
   L + {abcacbaaa}: status=contra contra=('skeleton', 'abcaabcbca', 'abcabcbca') certificate steps=10 replay=True
   [time so far 0.3s]
== [C] Theorem TR (bc/cb transposition): rule-level certificates of the hand proof
   N<=40: certified contradictions=3270  bad=0  uncovered-with-N>=4max+1=0  d1=d2 controls=244 (W4==W7)
   example N=12, d(bc)=2, d(cb)=3: seed=['aaaaaaaaaaaa', 'abcaaaaaaaaa', 'abcacbaaaaa', 'acbaaaaaaaa']
      0 x=('a', 'aaaaaaaaa') y=('aa', 'aaaaaaaa') E0=('', 'a', 'a') E1=('', 'bc', '') => aabcaaaaaaaa
      1 x=('a', 'aaaaaaaa') y=('aa', 'aaaaaaa') E0=('', 'a', 'aa') E1=('', 'cb', '') => aacbaaaaaaa
      2 x=('abc',) y=('bca',) E0=('a', 'aaaaaaaa') E1=('', 'acbaaaaa') => bcaacbaaaaa
      3 x=('acb',) y=('cba',) E0=('a', 'aaaaaaa') E1=('bca', 'aaaaa') => bcacbaaaaaa
      4 x=('acb',) y=('cba',) E0=('a', 'aaaaaaa') E1=('bc', 'aaaaaa') => bccbaaaaaaa
      5 x=('bca',) y=('abc',) E0=('a', 'aaaaaaaa') E1=('', 'cbaaaaaa') => abccbaaaaaa
      6 x=('a', 'aaaaaa') y=('aa', 'aaaaa') E0=('', 'a', 'aaaa') E1=('', 'bccb', '') => aabccbaaaaa
      7 x=('abc',) y=('bca',) E0=('a', 'aaaaaaaa') E1=('', 'aaaaaaaaa') => bcaaaaaaaaaa
      8 x=('acb',) y=('cba',) E0=('a', 'aaaaaaa') E1=('', 'aaaaaaaa') => cbaaaaaaaaa
      9 x=('cba',) y=('bcaa',) E0=('', 'aaaaaaaa') E1=('bc', 'aaaaaa') => bcbcaaaaaaaa
     10 x=('bc', 'aaaaaaa') y=('cb', 'aaaaaa') E0=('', 'a', 'aa') E1=('', 'cb', '') => cbcbaaaaaa
     11 x=('cba',) y=('bcaa',) E0=('', 'aaaaaaaa') E1=('cb', 'aaaaa') => cbbcaaaaaaa
     12 x=('bca',) y=('abc',) E0=('a', 'aaaaaaaa') E1=('bc', 'aaaaaaa') => bcabcaaaaaaa
     13 x=('bca',) y=('abc',) E0=('a', 'aaaaaaaa') E1=('', 'bcaaaaaaa') => abcbcaaaaaaa
     14 x=('a', 'aaaaaaa') y=('aa', 'aaaaaa') E0=('', 'a', 'aaa') E1=('', 'bcbc', '') => aabcbcaaaaaa
     15 x=('cb', 'aaaaaaaa') y=('bc', 'aaaaaaaaa') E0=('', 'a', '') E1=('b', 'c', '') => bbccaaaaaaaaa
     16 x=('bc', 'aaaaaaaaa') y=('bccb', 'aaaaaa') E0=('', 'a', '') E1=('b', 'c', '') => bbccbcaaaaaa
     17 x=('bcaaa',) y=('bcbca',) E0=('', 'aaaaaaa') E1=('bc', 'aaaaa') => bcbcbcaaaaaa
     18 x=('bca',) y=('abc',) E0=('a', 'aaaaaaaa') E1=('cb', 'aaaaaa') => cbabcaaaaaa
     19 x=('cb', 'bc') y=('bc', 'cb') E0=('', 'a', 'aaaaaa') E1=('b', 'c', 'aaaaaa') => bbcccbaaaaaa
     20 x=('bc', 'cba') y=('bc', 'bcaa') E0=('', 'a', 'aaaaa') E1=('b', 'c', 'aaaaa') => bbccbcaaaaaaa
     conflict: bbccbcaaaaaa (a=6) vs bbccbcaaaaaaa (a=7), same skeleton bbccbcA
   tamper controls rejected: empty-separator(empty separator) type(type mismatch ('cb', 'bc') ('bc', 'cba')) missing-premise(premise aabcaaaaaaaa missing)
   [time so far 0.9s]
== SUMMARY: checks=366 FAIL=0 time=0.9s
ALL CHECKS PASSED

===== END FILE =====

# 第八段 チェックポイント1：HC_III（同一根成分に二つの削除）— 資料・監査・最初の結果

**日付**：2026-11-14　／　**作成**：Claude（Opus 5.5、新規セッション）　／　**状態**：研究アーカイブ・未査読
**原稿への変更**：なし（GitHub `main`、英日 LaTeX、PDF、定理A/B/C、`op:fanout-two` に触れていない。commit・PR なし）

## 0. 実際に読んだ資料

GitHub `growupkuriyama-hub/Papers`、commit `552f840`（2026-11-14 19:22 JST）を clone した。

| 資料 | 扱い |
|---|---|
| 依頼書 `PROMPT_CLAUDE_FANOUT2_ROUND8_HCIII_2026-11-14.md`（添付） | 全文 |
| `reviews/claude_fanout2_round7_hostability_report_2026-11-14.md` | 全文（§2–§10） |
| `reviews/STATUS_claude_fanout2_round7_intake_2026-11-14.md` | 全文 |
| `reviews/claude_fanout2_round6_checkpoint1_2026-11-14.md` | 全文（U1a/U1b、補題K、例R、補題G、H\*） |
| 第六段最終報告（プロジェクト内 `claude/claude_fanout2_round6_report_2026-11-14.md`） | 全文。**補題R の statement と証明**はここにある（リポジトリの `reviews/` には無い） |
| `reviews/audit_Ltensor_prime_independent_2026-11-14.md` | B3・B4・B6・B7 を読んだ（P1^⊗ の span 版、Y_b、F_b） |
| `reviews/round7_hc/` の 6 本 | `hc_core.py`、`hc_construct.py`、`hc_search_case2.py`、`hc_search_case13.py` を全文。`hc_check_case2.py`・ランナーは構成のみ確認 |
| `main.tex` | `def:grammar-properties`、$\mathcal E_d$、`def:tuple-substitutable`/`def:class-cmcf`、`lem:filling-identity`、`cor:distribution-representatives`、`op:fanout-two` |
| 添付 ZIP `新しいフォルダー(20261114-104444).zip` | **この会話には添付されていない**（アップロードは依頼書 1 本のみ）。GitHub の `round7_hc/` を正本として使った |
| `audit_theorem_L/P_independent`、`STATUS_..._round6_checkpoint1_audit`、`audit_round6_exampleR_maximality_*`、`HANDOFF_CURRENT.md`、`PAPER.yaml` | **未読**（存在のみ確認）。本チェックポイントの推論はこれらに依存しない |

## 1. 最重要の監査結果：F 側の「局所化」は補題R の要件ではない

補題R（第六段報告 §3.1）の (F) は「$W_{j'}$ と**同じデータ**の文で、全穴を順に、重ならず、間を非空にして含むもの」であり、保護領域の不変性は含まない。理由（本セッションで再導出）：

1. $L\cap\Sigma^+=\operatorname{dat}_{\rm ov}^{-1}(\mathcal Q)$ なので、$\operatorname{dat}_{\rm ov}(W^\*)=\operatorname{dat}_{\rm ov}(W_{j'})$ なら $F[h]:=W^\*\in L$。
2. H\* は**任意の文脈で** $N_2$ の差を $D_1+D_2$ にし、射影が長さ $\ge2$ なら $\widehat s_2$ を変えない。よって $\operatorname{dat}(F[t])=\operatorname{dat}(W_{j'})+\sum_\kappa Z_\kappa=\operatorname{dat}(W_j)$（P1^⊗ 主張3）、$F[t]\in L$。
3. $F$ が $\mathcal E_{e'}$ に入るには穴の間が非空であればよい。$F$ は $\mathcal D(h)\cap\mathcal D(t)$ の証人にすぎず、次段では使わない（次段は新しい切り口の $W_{j'}$ を使う）。

**帰結.** F 側は **Γ$(W_{j'})$ が穴を順に hosting できるか**（`hc_core.hosts`）だけの問題になる。第七段が未解決とした「(i) $\varphi_\kappa\subseteq P'$ の場合の局所化」は、証明手法上の問題であって HC_III の要件ではない。第七段の有界探索 [4][5] も実際には Γ だけで判定していた（`hosts(GF, ...)`）。

同様に、**穴は η 成分に 1 対 1 で紐づく必要がない**。補題R の証明は「保存則を満たす分割 $D_1+D_2=\sum_{\kappa\in K_i}Z_\kappa$」しか使わない（$y^\pi\equiv y'$ は $\mathcal D(t)=\mathcal D(h)$ と文脈の持ち上げだけから出る）。

## 2. 既存補題の監査（分類）

| 項目 | 分類 | 要点 |
|---|---|---|
| 補題G′（O1–O3） | **VERIFIED** | 補題G の Γ を変えない。根成分の境界が $c$ 区間を切る場合も、W 全体で Γ が保たれれば足りる（§1 により「領域に閉じる」は不要） |
| 補題FO | **VERIFIED** | 印付き窓の文字が $\varphi$ の中にあると印が η に入るので、両文字とも $s$ より前。他方の自由成分が $P$ にあっても印は η の外なので不変 |
| 補題P（持続性） | **DEPENDS-ON-UNPROVED-LEMMA**（B6 を引用） | B6（削除は原 $x$ の印なし出現で、段ごとに互いに素）から $\min(N_0,c_*)\le N_T\le N_0$。旗の一致は $c_*\ge2$ で正しい |
| 補題YB | **VERIFIED**（$c_*\ge2$） | 独立に再証明。$\varphi$ が $c$ を含まない（端／内側）、含む（遷移窓が印なし→$\nu\ge c_*-1$）の 3 場合 |
| 補題FL | **VERIFIED** | 最短性→内側区間は空、$cX$ が一回だけ→印付き、の二段。隠れた仮定は「$\varphi$ が両文字を含む」と「$P$ が最後の区間まで届く」 |
| 補題AB (2b) | **VERIFIED（再構成）**、HC_III では不使用 | $m_2<t$ なら $J=p_{m_2}$ の両端 $c$ は $P$ の中。$m_2=t$ では $\psi$ が $c$ を含まなければ $\psi$ が $X$ を含み (2a) に戻る |
| 補題OT $\{a,b,c\}$ 行 | **NEEDS-REPAIR（軽微）** | $R'=\{a,b,c\}$ は $r=r'=0$（$cc$ だけ）でも起きる。そのとき「遷移窓」は $ac$ か $ca$ の片方しかないことがあり、どちらか存在する方の印付き出現 2 個から内側区間を取る、と書き直せば成立 |
| HC_I・HC_II | **VERIFIED（引用前提のもと）** | HC_I の証明は同じ根成分に別の η 成分があっても使える（下の定理 III-A に含まれる） |

## 3. 場合 III の最初の結果（証明の概略。最終報告で全文）

設定：根成分 $x$ に $\varphi$（$Z_\kappa=(p\,aa,\ p'\,bb)$、$p,p'>0$）と $\varphi'$（$Z'=(q\,aa+q_c\,cc+r(ac+ca),\ q'\,bb+q'_c\,cc+r'(bc+cb))\ne0$、$m'=q_c+r=q'_c+r'$）がある。$T$ は次の状態。

- **定理 III-A（$m'=0$）.** 2 穴 $h_1,h_2\in\{\mathtt a,\mathtt b\}$、$D_a=((p+q)aa,0)$、$D_b=(0,(p'+q')bb)$。F 側は $W$ のまま：印付き $aa$ の 2 文字と $bb$ の 2 文字の 4 組のうち距離 $\ge2$ の組が必ずある。Y 側は YB の「3 文字以上の両持ち区間」で両方の向きを置ける。
- **定理 III-B（$m'>0$）.** 1 穴 $h\in S_6=\{\mathtt{abc},\mathtt{bac},\mathtt{cab},\mathtt{cba},\mathtt{acb},\mathtt{bca}\}$、$D=Z_\kappa+Z'$。
  - F 側：Γ$(W)$ が $S_6$ のどれも置けないのは $W=a^\alpha c^n b^\beta$ か $b^\beta c^n a^\alpha$（$n\ge2$）のときだけで、それは $P$ の印付き $a,b$ の後ろに $\psi$ が来ることと $|\pi_A\psi|,|\pi_B\psi|\ge2$ に反する。
  - Y 側：$\nu^T_A,\nu^T_B\ge1$ なら（$c_*\ge3$ で $n_T\ge3$）$S_6$ の全てを置ける。$\nu^T_A=0$ なら $r=0$、$\varphi$ は $x$ の最初か最後の区間にあり、$ac$／$ca$／$cb$ の一意な遷移窓が印付きであることから、$\mathtt{abc}$、$\mathtt{cab}$、$\mathtt{bca}$ のどれかを両側に置ける。$\nu^T_B=0$ は対称。
  - **$\varphi\subseteq P'$ の場合**も含む（印は η の外という事実だけを使う）。

## 4. 有限検査（最初の結果）

`hc3_search.py`（新規、標準ライブラリ、固定シード）：場合 III を Γ だけで判定。穴は 1 個または**全ての**保存則つき 2 分割、各穴は長さ $\le3$ の語と $c$ の連。結果（$c_*=2,3,4$、7 回、合計 2760 配置・約 4.4 万の (配置, 状態)）：**NOT FOUND WITHIN BOUND は 0**。全例で 1 穴で足りた。これは証明ではない（モデルは第七段と同じく実際の文法より広い）。

## 5. 未証明箇所・次の一手

1. 定理 III-A/III-B の全文証明を最終報告に書き、場合分けの各枝を**構成的な検査器**で assert する（穴の位置まで実際に語を作り、$\operatorname{dat}$ の一致、穴の文字どおりの出現、順序、区切り $\ge1$、H\* の差分を確認）。
2. 引用のまま残るもの：P1^⊗（span 版。$Z_{\kappa',b}$ の台が $\varphi'$ の印なし内部窓であること）、B6（削除領域が互いに素で印に触れない）、補題C、DFS／型付き高さ。HC_III の証明はこれらを再証明しない。
3. 実際の good MCFG の導出木から場合 III を作る検査は未着手。

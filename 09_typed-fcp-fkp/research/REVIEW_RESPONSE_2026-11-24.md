# 外部査読（ChatGPT、2026-11-24）への対応

査読の原本：[`external_review_2026-11-24/`](external_review_2026-11-24/)（報告・判定表・指摘一覧・新規性監査・追加結果・スクリプト・ログ）。
対応後の原稿：`main.tex` revision 2（15 頁）。

## 査読の結論

- 推薦：**major revision**。主定理を崩す数学的反例は見つからず。
- 判定 29 件：CORRECT 11、CORRECT-WITH-FIX 8、GAP 0、**FALSE 0**、KNOWN 10。
- 最大の問題は新規性：Theorem B（旧）は #1 の Prop 9.7 から直ちに従う。Theorem C（旧、一語削除）は「今回の照合範囲では同じ主張なし、最も独立性が高い」。

## 指摘ごとの対応

| 指摘 | 内容 | 自分での確認 | 対応 |
|---|---|---|---|
| I-01 major | Theorem B は #1 Prop 9.7（$\bigcup_s\mathcal C^{\rm cf}_s\subseteq\mathsf{CONG}$）＋合同文法 ⇒ 1-FKP ＋ KY2017 Thm 6 の帰結 | #1 `main.tex` 2080–2113 行で Prop 9.7 と証明を確認。**指摘どおり** | Theorem B を主定理から外し Corollary 6.1（essentially known）に格下げ。序論・abstract・`rem:uniform-known` で出典を明記 |
| I-02 major | Yoshinaka 2015 §8 は signature の比較を扱っている | §8 本文を確認（direct union、congruential は細分化へ移るが逆は不可）。**指摘どおり** | 「どちらの枠組みも観測の比較を扱わない」を削除し、§8 を引用。本稿の追加分（核 SPP と文脈 SPP の逆向きの振る舞い、厳密性の証人、weak FCP の非保存）を明示 |
| I-03 minor | `lem:product` の型の積で中間の終端記号列 $\widehat h(w_i)$ が抜けている | 反例 $S\to AcB$ を確認。**指摘どおり** | 式を修正（パッチ適用） |
| I-04 minor | 核側の厳密性の証人が $k=2$ のみ | 初期記号を $S_+,S_-$ に分ける文法で $\{z\}^{\rhd\lhd}=L(S_+)$ を自分で再計算。**正しい** | $L_K$ が $s_0$ 型付き **strong 1-FKP** を持つと強化。厳密性は $s_0$ と指示型付けの間の型付き包含に限ると明記 |
| I-05 minor | 学習器の移植で空の $C,K$ の正規化、出力ソートの扱いが不足 | 妥当 | `prop:learners` の証明に正規化・有限反駁・安定化の説明を追加（パッチ） |
| I-06 minor | $H_n$ の添字範囲（存在しない $(E_0,\zeta)$） | **指摘どおり** | 範囲と「子が存在する規則だけ」を明記（パッチ） |
| I-07 minor | 文法サイズ・最大証人長・証人の総量の区別 | 妥当 | 表の注記を追加（パッチ） |
| I-08 minor | EXREG のパラメータ対応 | KY2023 の式サイズの定義（部分式の個数）と $\mathrm{EXREG}_r(k)$ の定義を確認。サイズ $2m+b_\mu$ は**正しい** | `rem:exreg` を具体化（パッチ）。正規表現への変換が多項式とは限らない注意も入れた |
| I-09 minor | `op:Mn-context` の部分主張の定義と証明がない | 証明を自分で追った。**正しい** | Proposition 7.7（`prop:Mn-constituent`）として証明つきで本文に入れた |
| I-10 minor | 計算の範囲・シードの再現性 | 型 `frozenset` の並び順がハッシュに依存していたのが原因と特定 | スクリプトを修正（選択をすべてソート済みの列から）。同じシードで規則同値 **2230 件**が再現。付録を修正 |
| I-11 minor | 書誌（Yoshinaka 2015 の題名は単数）、支配の意味 | 題名は保管庫の書誌と一致 | 題名を修正。`cor:primal-dominated` を「クラスの比較であり速度・データ量ではない」と明記。KY2017 の巻・頁は未確認のまま入れていない |

## 査読で得た追加結果（本文に採用）

**Proposition 5.4（`prop:weak-not-preserved`）：型なし weak FCP は 2 元の観測を足すと保存されない。**
KY2017 Thm 14 の言語 $L'$ に、$L_1$ の中心記号 $\$$ を新文字 $@$ に替えた $L_1^@$ を足した $L^+$ は、型なし weak 2-FCP を持つが、$@$ の指示型付けではどの $k$ でも型付き weak FCP を持たない。

- 確認：KY2017 Lemma 8 の文脈表と Lemma 12 の記述を原典で照合した。正側は「S1 以外の旧非終端記号は同じ文脈で弱く特徴づけられたまま」という KY2017 Lemma 12 の記述に依存する。負側は KY2017 Lemma 13 の証明をそのまま使う。
- 状態：**PROVED-CONDITIONAL**（KY2017 Lemmas 8, 12 の特徴づけを前提）。
- これで `op:weak-fcp` のうち「型なし → 型付き」は否定的に解決。「型付き → 型付き」（$s_0$ と $h$ の比較）は、$L^+$ の文法が空語を生む非終端記号を持つため未解決のまま。

## 査読者の再計算（こちらでも再実行して全通過）

- `check_weak_candidate.py`：32,691 語 × 12 非終端記号で文脈の述語が一致。
- `check_kernel_witness.py`：長さ 7 以下の全 21,845 語で $L_K$ の閉包、下界 9 例。
- `check_deletion_independent.py`：$n\le4$ で空の収量を含む捕獲補題 1,228 件。

## 構成についての判断

査読の勧めどおり、一語削除の下界（Theorem B、旧 C）を主結果とし、双対性（Theorem A）は比較原理と厳密性の証人として、一つの学習器の主張は系として置いた。題名「Finite Observation Helps Contexts but Not Kernels」は双対性を前面に出しているので、投稿前に下界を前面に出す題名へ変えるかを検討する（未決）。

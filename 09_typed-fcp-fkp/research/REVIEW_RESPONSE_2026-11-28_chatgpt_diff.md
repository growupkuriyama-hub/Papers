# ChatGPT による 2026-11-28 の差分の査読への対応

査読：[`external_review_2026-11-28_chatgpt_diff/`](external_review_2026-11-28_chatgpt_diff/)（依頼文 `PROMPT.md`、`review.md`、`findings.csv`、`checks/`）。対象は `61f8a16..5cdba4f` の英語版の差分。

## 査読の概要

- **総合判定：局所的な修正で投稿してよい。** 主張の数学的な誤りは C04（自己矛盾）と C13（書誌）の FALSE 2 件。ほかは GAP 3、OVERCLAIM 2、UNCLEAR 4、STYLE 5。
- 数値（$2^n+2n-2$、$6n-4$、$3\cdot2^n-6$、$n\ge10$ での $24n-16<2^{n-2}$、$(n+1)^2$、$3\cdot2^{n-1}-2$、演算 8 回、Abstract 248 語）は `checks/check_numbers.py` で確認。Claude が `python3 -I` で再実行し、同じ出力を得た。
- D3（Algorithm 3）と D4（$\ell+1$、ブール演算）の数学的な中身は ChatGPT が独立に再構成し、正しいとした。Kanazawa の正規化のあとの原子の長さ $(n+1)^2$ も、文字の順序の二つの場合について確認された。
- **C04・C06・C09・C11・C13 は、11-28 の Claude の編集で入った誤り**（前日と同じ種類：圧縮で根拠や範囲が落ちる、言い換えで主張が強まる）。

## 対応（英日とも）

| ID | 判定 | 対応 |
|---|---|---|
| C01 | unclear | Abstract：見本の積は「at least exponential in $n$, tight up to a factor $O(n)$」に（下界であることと、最小値での最適性を明示） |
| C02 | gap | Abstract：「Both bounds extend to general one-word deletions, …」を「The frame upper and exemplar lower bounds extend to suitable one-word deletions」に（定理 6.8 の条件付き。観測器なしの枠の下界は一般化していない） |
| C03 | style | 序論：尺度を「Section 5 が主学習器のデータを抑えるのに使う量」と限定（双対学習器の下界は別の論法） |
| C04 | **false** | 序論：「Theorem A does not count productions」は定理 A(i) が生成規則の数を明記したことと矛盾していた。「The gap in Theorem A does not count productions」に |
| C05 | unclear | 序論：所属質問は文法性判断を求め、否定証拠を「与えうる」（肯定の答えは正の証拠） |
| C06 | overclaim | 序論：定理 C の後の「an observer … is needed for it」は言い過ぎ（観測器なしでも枠と見本の最小の全長の比は未解決、未解決問題 7.3）。「the mark observer yields a gap in total length, and an observer is needed for frames of polynomial total length」に |
| C07 | unclear | 序論：Clark (2016) は近似的な検査による割合の推定。「estimate their prevalence in random grammars」、「none of these compares …」に |
| C08 | gap | §5：「applies verbatim」を「carries over」にし、収束時に $J$ が固定され、$E$ が $\mathrm{Sub}(M_n)$ を尽くせば $Q^{r,s}$ が各商の代表を残すことを明記 |
| C09 | overclaim | §5：(d†′) は $D$ を存在量化し、その長さを抑えない。$D$ が長い語を含めば追加の例は短くてよい。結論を「この短い語を原子を覆う初期の集合とするとき、追加の例をすべて多項式の長さにはできない」に限定 |
| C10 | style | §5：$r$、$s$ は Kanazawa の記法であることを明記（本稿の $s$ は型付け）。演算の集合は $\Gamma$ と書かず「$\cap$ among its operations」 |
| C11 | gap | 注意 5.6：圧縮の際に落とした根拠を補った。「apply the proof of Lemma 5.1 relative to $L$」（$\varepsilon\in L$ なら二重閉包が $\varepsilon$ を含みうるので、補題をそのまま適用するのではなく証明を $L$ に相対的に繰り返す） |
| C12 | gap | §6：「$p_ixq_i\in M_n$ iff $x$ is marked」に「for $x\in L(G_n,E_i)$」を追加（一般の $x$ では偽） |
| C13 | **false** | 参考文献：Coste–Nicolas は ICGI 2018（PMLR 93、刊行 2019）。略記の際に Claude が「ICGI 2019」と誤記していた。ほかの ICGI（2010、2016、2021、2023）は正しいことを確認 |
| C14 | style | Ogden の誌名を Mathematical Systems Theory に戻した |
| C15 | style | Yoshinaka 2015 に ACL を戻した |
| C16 | style | 略記の方針の統一：Springer の JoLLI 様式に変換するときに、その参考文献の書式に合わせて統一する（それまで保留） |

Abstract は 246 語（上限 250）。英語版は 24 頁になった（参考文献の最後の 2 件、4 行が次頁へ）。JoLLI に頁の上限はなく、様式の変換で組版が変わるので、23 頁に戻すための削除はしなかった。日本語版 26 頁。定理・証明の変更なし。

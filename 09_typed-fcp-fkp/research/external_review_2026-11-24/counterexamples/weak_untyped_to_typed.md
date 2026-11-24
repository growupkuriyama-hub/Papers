# 追加の部分結果：untyped weak FCPは型付けで保存されない

原稿が主張していない包含への反例であり、Theorem A–Cの反例ではない。
言語L+、明示CFG、h_{\{@\}}、正側・負側の証明は `../WEAK_FCP_PARTIAL.md`。

L+ ∈ untyped weak 2-FCP かつ L+ ∉ h_{\{@\}}-typed weak FCP。
ただしL+ ∈ s0-typed weak FCPは未証明であり、op:weak-fcpのtyped-to-typed単調性の決着とはしていない。

計算的確認：`python3 -I scripts/check_weak_candidate.py`。

# R16　状態装飾による移送定理

## 結論（3行）

1. 成分ごとの型復元と端点指定生成組を使うと、全ての固定 fan-out・rank で局所計数定理を元の分布代表長に移せる。
2. ある LG 下層で全入口から統語値を復元できる正則骨格は、正の統語半群が $\mathbf{SL}*\mathbf{LG}=\mathbf{LTT}*\mathbf{LG}$ に属するものと一致する。
3. 中立文字付きの二つの reset は位数3でこの方法の外にある。非 LG 下層による装飾厚さの指数例でも、元の代表長は一定になり得る。

## 到達範囲

U0–U5 を扱った。主判定は自己判定 VALID。report.md §1 に既読箇所と Thérien–Weiss (1985) 本文の未読を明記した。一般の fan-out 2 / rank 2 問題は未解決。§6–7 では統語値の完全復元と、装飾後の所属を任意の窓計数で読む方式の両方に対する境界例を示す。

## ファイル

| ファイル | 用途 |
|---|---|
| report.md | 日本語の本報告。定理・系・次数比較・境界例・自己監査 |
| unified_theorem.tex | 英文の DT と全統語値の復元定理。単独コンパイル可能。既存文書に入れる場合は amsmath, amsthm を読み込んだ上で本文に下記の2行を置く |
| code/run_all.py | 有限検査。Python 3 標準ライブラリのみ使用 |
| code/run_all.log | 実行した標準出力（決定的） |
| SHA256SUMS.txt | 自ファイルを除いた上記5ファイルの SHA-256 |

英文の組み込み方

~~~tex
\def\RDecorationFragment{}
\input{unified_theorem.tex}
~~~

展開先のこのディレクトリで次を実行する。Python 部分はこの環境で約0.8秒、ネットワーク不要。

~~~sh
sha256sum -c SHA256SUMS.txt
(cd code && python3 -I run_all.py)
~~~

スタンドアロンの英文は pdflatex unified_theorem.tex で組版できる。

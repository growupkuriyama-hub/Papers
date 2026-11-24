# 304行の積を文字どおり読む場合の反例

位置：`lem:product`、297–318行、特に304行。

Σ={a,b,c}、Gの初期記号S、規則S→AcB、A→a、B→b。
L(G)={acb}。hはc-indicatorでh(a)=h(b)=1、h(c)=ζ。

記載された式ν=ĥ(w0)ν1…νnĥ(wn)は、w0=w2=ε、w1=c、ν1=ν2=1に対してν=1を与える。従って(S,1)→(A,1)c(B,1)を置くが、このRHSの型はζ。構成はh-typedではなく、(S,1)がacbを生成するので L(Gh,(S,1))=L(G,S)∩F1 も破れる。

正しい式はν=ĥ(w0)ν1ĥ(w1)…νnĥ(wn)。これで親は(S,ζ)になり両問題が解消する。

補題全体をFALSEとしたのではなく、意図の明白な中間terminalの欠落としてCORRECT-WITH-FIXとした。ellipsisに全terminal blocksを含める意図だったとしても、式を明示する修正が必要。

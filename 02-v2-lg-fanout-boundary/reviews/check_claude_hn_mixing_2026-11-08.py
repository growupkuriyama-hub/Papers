import numpy as np, sys
# Random walk on H_n = Z_N x| Z_n, N=2^n-1, right mult by a=(1,0), b=(0,1)
for n in range(3,13):
    N=2**n-1; H=N*n
    P=np.zeros((n,N)); P[0,0]=1.0
    t=0
    while True:
        Q=np.zeros_like(P)
        for j in range(n):
            Q[j]+=0.5*np.roll(P[j],(2**j)%N)   # a: c -> c+2^j
            Q[(j+1)%n]+=0.5*P[j]              # b: j -> j+1
        P=Q; t+=1
        if np.max(np.abs(P*H-1))<0.5: break
        if t>20000: break
    print(n, H, "t_mix(sup rel err<1/2) =", t, " t/(n log2 n)=%.2f"%(t/(n*np.log2(n))))

import sys
n=int(sys.argv[1]); N=2**n
P={j:set() for j in range(1,n+1)}; P[n].add((0,0))
changed=True
while changed:
    changed=False
    for j in range(2,n+1):
        h=2**(j-1)
        # E1/E2 equalities both directions
        for (x,y) in list(P[j]):
            for pt in ((x,y+h),(x+h,y)):
                if pt not in P[j-1]: P[j-1].add(pt); changed=True
        for (x,y) in list(P[j-1]):
            if y>=h and (x,y-h) not in P[j]: P[j].add((x,y-h)); changed=True
            if x>=h and (x-h,y) not in P[j]: P[j].add((x-h,y)); changed=True
for j in range(1,n+1):
    xs=sorted(x for x,y in P[j]); print(j, "count",len(xs),"expected even count",(N-2**j)//2+1, xs[:8])

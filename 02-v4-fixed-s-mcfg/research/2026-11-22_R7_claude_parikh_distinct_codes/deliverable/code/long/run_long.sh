#!/bin/sh
# Generic closures with cap |W|, n=6, budget 20000 words, each case in its own process (timeout 600 s).
for host in spine tm; do for code in sq exp pal rnd rig; do
  timeout 600 python3 -I gen_one.py $host $code 6 brk2 20000 || echo "$host $code n=6: stopped (timeout or memory)"
done; done

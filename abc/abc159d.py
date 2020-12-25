import sys
sys.setrecursionlimit(1000000000)
nCr = {}
def cmb(n, r):
    if r == 0 or r == n: return 1
    if r == 1: return n
    if (n,r) in nCr: return nCr[(n,r)]
    nCr[(n,r)] = cmb(n-1,r) + cmb(n-1,r-1)
    return nCr[(n,r)]

from collections import defaultdict
def main():
    N = int(input())
    A = list(map(int, input().split()))
    counter = defaultdict(int)
    for a in A:
        counter[a] += 1

    total = 0
    for key, ct in counter.items():
        if ct > 1:
            total += cmb(ct, 2)
    
    for a in A:
        ans = total
        ct = counter[a]
        if ct > 1:
            before = cmb(ct, 2)
            after  = before * (ct-2) // ct
            ans -= (before-after)
        print(ans)

    

main()
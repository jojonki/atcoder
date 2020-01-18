import bisect

N = int(input())
L = list(map(int, input().split()))
L = sorted(L)
ct = 0

for i in range(N-1):
    a = L[i]
    for j in range(i+1, N):
        b = L[j]
        up_bound = bisect.bisect_left(L, a+b)
        ct += max(0, up_bound - (j+1))

print(ct)
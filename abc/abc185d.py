from math import ceil


def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    intvals = []
    cur = 0
    k = float('inf')
    for i in range(M):
        v = A[i] - 1 - cur
        cur = A[i] - 1 + 1
        if v == 0:
            continue

        intvals.append(v)
        if v < k:
            k = v
    v = N - cur
    if v != 0:
        intvals.append(v)

    res = 0
    if k == float('inf') and intvals:
        print(1)
    else:
        for inv in intvals:
            res += ceil(inv / k)
        print(res)


main()

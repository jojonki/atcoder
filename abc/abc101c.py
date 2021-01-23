from math import ceil


def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    min_v = A[0]
    min_ct = 1
    for a in A[1:]:
        if a == min_v:
            min_ct += 1
    N -= (min_ct - 1)
    ans = ceil((N - K) / (K - 1)) + 1
    print(ans)


main()

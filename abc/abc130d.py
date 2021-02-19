import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    N, K = read_ints()
    A = read_int_list()
    # l, r = 0, 0
    l = 0
    s = 0
    ans = 0
    for r in range(N):
        s += A[r]
        if s >= K:
            ans += N - r
            while l <= r:
                s -= A[l]
                l += 1
                if s >= K:
                    ans += N - r
                else:
                    break

    print(ans)


main()

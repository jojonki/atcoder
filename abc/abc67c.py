import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    N = int(input())
    A = read_int_list()
    l, r = [0 for _ in range(N)], [0 for _ in range(N)]
    l[0] = A[0]
    r[-1] = A[-1]
    for i in range(1, N):
        l[i] = l[i - 1] + A[i]
        r[N - 1 - i] = r[N - 1 - i + 1] + A[N - 1 - i]
    # print(l)
    # print(r)
    ans = INF
    for i in range(N - 1):
        ans = min(ans, abs(l[i] - r[i + 1]))
    print(ans)


main()

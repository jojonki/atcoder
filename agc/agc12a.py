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
    A.sort()
    l, r = 0, 3 * N - 1 - 1
    res = 0
    for _ in range(N):
        res += A[r]
        r -= 2
    # print(sum(A[N:2 * N]))
    print(res)


main()

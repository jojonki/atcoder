import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    n, X = read_ints()
    A = read_int_list()
    ans = 0
    for i in range(n):
        if X & (1 << i):
            # print(i)
            ans += A[i]
    print(ans)


main()

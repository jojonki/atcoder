import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    N, T = read_ints()
    t = read_int_list()
    ans = 0
    for i in range(N - 1):
        if t[i + 1] > t[i] + T:
            ans += T
        else:
            ans += t[i + 1] - t[i]
    ans += T
    print(ans)


main()

import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    ans = 0
    n_S, n_c = read_ints()
    ans = min(n_S, n_c // 2)
    # n_S -= ans
    n_c -= (2 * ans)

    ans += n_c // 4
    print(ans)


main()

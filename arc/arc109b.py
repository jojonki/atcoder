import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    N = int(input())
    ok, ng = 0, 10000000000000
    while ng - ok > 1:
        # print(ok, ng)
        m = (ok + ng) // 2
        if m * (m + 1) // 2 <= N + 1:
            ok = m
        else:
            ng = m
    print(N - ok + 1)


main()

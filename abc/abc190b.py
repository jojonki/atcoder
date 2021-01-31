import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    N, S, D = read_ints()
    for _ in range(N):
        X, Y = read_ints()
        if X >= S or Y <= D:
            continue
        else:
            print('Yes')
            return
    print('No')


main()

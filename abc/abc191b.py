import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    N, X = read_ints()
    res = []
    for a in read_int_list():
        if a != X:
            res.append(str(a))
    print(' '.join(res))


main()

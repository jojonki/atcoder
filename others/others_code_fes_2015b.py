import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


from collections import Counter


def main():
    N, M = read_ints()
    A = read_int_list()
    A = Counter(A)
    v, ct = A.most_common()[0]
    if ct > N // 2:
        print(v)
    else:
        print('?')


main()

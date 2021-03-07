import sys
from typing import DefaultDict
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


from collections import defaultdict


def main():
    N, M, Q = read_ints()
    to = defaultdict(list)
    for _ in range(M):
        u, v = read_ints()
        u -= 1
        v -= 1
        to[u].append(v)
        to[v].append(u)

    C = read_int_list()
    for _ in range(Q):
        q = read_int_list()
        if q[0] == 1:
            x = q[1]
            x -= 1
            print(C[x])
            for to_node in to[x]:
                C[to_node] = C[x]
        else:
            x = q[1]
            x -= 1
            y = q[2]
            print(C[x])
            C[x] = y


main()

import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


from collections import defaultdict


def main():
    N, M = read_ints()
    G = {n: INF for n in range(N)}
    to = defaultdict(list)

    def f(node, dist):
        # print(node, dist, N)
        if dist > 2:
            return False

        if node == N and dist <= 2:
            # print('ret True')
            return True

        for n in to[node]:
            if f(n, dist + 1):
                return True
        else:
            return False

    for _ in range(M):
        a, b = read_ints()
        to[a].append(b)
    # print(to)

    if f(node=1, dist=0):
        print('POSSIBLE')
    else:
        print('IMPOSSIBLE')


main()

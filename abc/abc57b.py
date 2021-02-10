import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    N, M = read_ints()
    P, C = [], []
    for _ in range(N):
        a, b = read_ints()
        P.append((a, b))
    for _ in range(M):
        c, d = read_ints()
        C.append((c, d))

    for a, b in P:
        target = None
        min_dist = INF
        for i, (c, d) in enumerate(C):
            dist = abs(c - a) + abs(d - b)
            if dist < min_dist:
                target = i + 1
                min_dist = dist
        print(target)


main()

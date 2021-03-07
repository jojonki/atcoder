import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    N, M = read_ints()
    dist = [[INF] * N for _ in range(N)]
    for i in range(N):
        dist[i][i] = 0

    for _ in range(M):
        x, y, c = read_ints()
        dist[x][y] = min(dist[x][y], c)

    for k in range(N):
        for x in range(N):
            for y in range(N):
                dist[x][y] = min(dist[x][y], dist[x][k] + dist[k][y])

    print(sum([sum(d) for d in dist]))


main()

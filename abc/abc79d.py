import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def warshall_floyd(N, C):
    dist = [[INF] * N for _ in range(N)]
    for i in range(N):
        dist[i][i] = C[i][i]

    for x in range(N):
        for y in range(N):
            dist[x][y] = C[x][y]

    for k in range(N):
        for x in range(N):
            for y in range(N):
                dist[x][y] = min(dist[x][y], dist[x][k] + dist[k][y])
    return dist


def main():
    H, W = read_ints()
    C = []
    for _ in range(10):
        C.append(read_int_list())
    dist = warshall_floyd(10, C)

    ans = 0
    for _ in range(H):
        for a in read_int_list():
            if a != -1 and a != 1:
                ans += dist[a][1]

    print(ans)


main()

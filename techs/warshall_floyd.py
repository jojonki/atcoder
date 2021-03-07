"""
E - 全点対最短経路問題, 全点対最短経路問題
https://atcoder.jp/contests/typical-algorithm/tasks/typical_algorithm_e

D - Wall, abc 79 D
https://atcoder.jp/contests/abc079/tasks/abc079_d

"""

INF = float('inf')


def warshall_floyd_M_routes(N, M):
    # M本のコスト付ルート
    dist = [[INF] * N for _ in range(N)]
    for i in range(N):
        dist[i][i] = 0

    for x, y, c in M:
        dist[x][y] = min(dist[x][y], c)

    for k in range(N):
        for x in range(N):
            for y in range(N):
                dist[x][y] = min(dist[x][y], dist[x][k] + dist[k][y])

    return dist


def warshall_floyd_from_NxN_table(N, C):
    # NxNのコストテーブル
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

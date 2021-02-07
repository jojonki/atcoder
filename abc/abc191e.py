import sys
from typing import DefaultDict
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


from collections import defaultdict

import heapq


def dijkstra(n_nodes, start_node, goal_node, edges):
    hq = [(0, start_node)]
    cost = [INF] * n_nodes
    cost[start_node] = 0
    ret = INF
    while hq:
        c, frm = heapq.heappop(hq)
        if c > cost[frm]:
            continue
        for c, to in edges[frm]:
            tmp_c = c + cost[frm]
            if to == goal_node:
                ret = min(ret, tmp_c)
            if tmp_c < cost[to]:
                cost[to] = tmp_c
                heapq.heappush(hq, (tmp_c, to))
    return ret


def main():
    N, M = map(int, input().split())
    edges = [[] for _ in range(N)]
    for _ in range(M):
        a, b, c = map(int, input().split())
        a, b = a - 1, b - 1
        edges[a].append((c, b))

    for i in range(N):
        dist = dijkstra(N, i, i, edges)
        if dist == INF:
            print(-1)
        else:
            print(dist)


main()

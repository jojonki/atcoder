import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())

import heapq
def dijkstra(N, edges, start, goal):
    if start==goal:
        return 0
        
    res = INF
    cost = [INF] * N
    cost[start] = 0
    q = [(0, start)]
    heapq.heapify(q)

    while q:
        total_cost, from_node = heapq.heappop(q)
        if total_cost > cost[from_node]:
            # already exists less cost path
            continue

        for c, to_node in edges[from_node]:
            tmp_cost = total_cost + c
            if to_node == goal:
                res = min(res, tmp_cost)
                continue
            if tmp_cost < cost[to_node]:
                cost[to_node] = tmp_cost
                heapq.heappush(q, (cost[to_node], to_node))

    return res


def dik():
    N, M = map(int, input().split())
    edges = [[] for _ in range(N)]

    for _ in range(M):
        a, b, c = read_ints()
        a -= 1
        b -= 1
        edges[a].append((c, b))

    for start_node in range(N):
        c = dijkstra(N, edges, start_node, start_node)
        if c == INF:
            print(-1)
        else:
            print(c)


def main():
    


main()

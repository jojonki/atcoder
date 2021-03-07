import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


from collections import defaultdict
from heapq import heapify, heappush, heappop


def dijkstra(N, to, start, goal):
    res = INF
    cost = [INF] * N
    cost[start] = 0
    q = [(0, start)]
    heapify(q)

    while q:
        total_cost, node = heappop(q)
        if total_cost > cost[node]:
            continue
        # print('cost', c, 'node', node, goal)
        if node == goal:
            res = min(res, total_cost)
            continue

        cost[node] = min(cost[node], total_cost)

        for to_cost, to_node in to[node]:
            heappush(q, (total_cost + to_cost, to_node))
    return res


def main():
    N, M = read_ints()
    to = defaultdict(list)
    for _ in range(M):
        x, y, c = read_ints()
        to[x].append((c, y))

    ans = dijkstra(N, to, 0, N - 1)
    print(ans)


main()

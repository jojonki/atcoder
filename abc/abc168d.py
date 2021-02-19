import sys
import heapq
sys.setrecursionlimit(1 << 20)
INF = float('inf')

INF = float('inf')


def read_ints():
    return map(int, input().split())


def dijkstra(N, edges, start):
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
            if tmp_cost < cost[to_node]:
                cost[to_node] = tmp_cost
                heapq.heappush(q, (cost[to_node], to_node))

    return cost
    # return res


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    N, M = read_ints()
    edges = [[] for _ in range(N)]
    for _ in range(M):
        A, B = read_ints()
        A -= 1
        B -= 1
        edges[A].append((1, B))
        edges[B].append((1, A))
    cost = dijkstra(N, edges, 0)
    # print(cost)
    fail = False
    res = []
    for i in range(1, N):
        tgt = None
        min_cost = cost[i]
        for _, to in edges[i]:
            if cost[to] < min_cost:
                tgt = to
                min_cost = cost[to]
        if tgt is None:
            fail = True
            break
        res.append(str(tgt + 1))
    if fail:
        print('No')
    else:
        print('Yes')
        print('\n'.join(res))


main()

import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def dfs(worker_id, children):
    if not children[worker_id]:  # no subordinate
        return 1

    min_s, max_s = INF, -INF
    for subordinate_id in children[worker_id]:
        s = dfs(subordinate_id, children)
        min_s = min(min_s, s)
        max_s = max(max_s, s)

    return min_s + max_s + 1


def main():
    N = int(input())
    children = [[] for _ in range(N)]
    for i in range(1, N):
        i_boss = int(input())
        i_boss -= 1
        children[i_boss].append(i)

    print(dfs(0, children))


main()

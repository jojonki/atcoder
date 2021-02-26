import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


from collections import defaultdict
N, Q = read_ints()

to = defaultdict(list)
ans = [0] * N

for i in range(N - 1):
    a, b = read_ints()
    a -= 1
    b -= 1
    to[a].append(b)
    to[b].append(a)

# seed = [0 for _ in range(N)]
for _ in range(Q):
    p, x = read_ints()
    p -= 1
    ans[p] += x


def dfs(v, p=-1):
    for child in to[v]:
        if child == p:
            continue
        ans[child] += ans[v]
        dfs(child, v)


def main():
    # print(to)
    # print(seed)

    dfs(0)
    print(' '.join([str(v) for v in ans]))


main()

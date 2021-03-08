import sys
from collections import deque
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def p(table):
    for i in range(len(table)):
        print(*table[i])


def main():
    H, W = read_ints()
    sx, sy = read_ints()
    sx -= 1
    sy -= 1
    gx, gy = read_ints()
    gx -= 1
    gy -= 1
    M = []
    C = []
    for _ in range(H):
        M.append(list(input()))
        C.append([INF] * W)
    # print(M)
    ans = INF
    # C[sx][sy] = 0
    q = deque([(sx, sy, 0)])
    # p(C)
    while q:
        x, y, c = q.popleft()
        # print(x, y, c)
        if C[x][y] <= c:
            continue
        C[x][y] = min(c, C[x][y])
        if x == gx and y == gy:
            ans = min(ans, c)
            continue
        if C[x][y] >= ans:
            continue
        if M[x - 1][y] != '#':
            q.append((x - 1, y, C[x][y] + 1))
        if M[x][y - 1] != '#':
            q.append((x, y - 1, C[x][y] + 1))
        if M[x + 1][y] != '#':
            q.append((x + 1, y, C[x][y] + 1))
        if M[x][y + 1] != '#':
            q.append((x, y + 1, C[x][y] + 1))
    print(ans)


main()

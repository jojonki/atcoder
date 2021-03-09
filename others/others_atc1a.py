import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    H, W = read_ints()
    M = []
    visited = []
    sx, sy = None, None
    for i in range(H):
        M.append(list(input()))
        if 's' in M[-1]:
            sy = M[-1].index('s')
            sx = i

        visited.append([False] * W)
    # print(sx, sy)

    def dfs(r, c):
        visited[r][c] = True
        if M[r][c] == 'g':
            return True

        if r > 0 and M[r - 1][c] != '#' and not visited[r - 1][c]:
            if dfs(r - 1, c):
                return True
        if c > 0 and M[r][c - 1] != '#' and not visited[r][c - 1]:
            if dfs(r, c - 1):
                return True
        if r < H - 1 and M[r + 1][c] != '#' and not visited[r + 1][c]:
            if dfs(r + 1, c):
                return True
        if c < W - 1 and M[r][c + 1] != '#' and not visited[r][c + 1]:
            if dfs(r, c + 1):
                return True

    if dfs(sx, sy):
        print('Yes')
    else:
        print('No')


main()

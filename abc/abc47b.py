import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    W, H, N = read_ints()
    R = [[1 for _ in range(W)] for _ in range(H)]
    for _ in range(N):
        x, y, a = read_ints()
        if a == 1:
            for r in range(H):
                for c in range(x):
                    R[r][c] = 0
        elif a == 2:
            for r in range(H):
                for c in range(x, W):
                    R[r][c] = 0
        elif a == 3:
            for r in range(H - y, H):
                for c in range(W):
                    R[r][c] = 0
        elif a == 4:
            for r in range(H - y):
                for c in range(W):
                    R[r][c] = 0
        # print(x, y, a)
        # for r in R:
        #     print(r)
    ans = 0
    for r in R:
        # print(r)
        ans += sum(r)
    print(ans)


main()

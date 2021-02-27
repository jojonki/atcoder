import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def p(T):
    for i in range(len(T)):
        print(' '.join(T[i]))


def main():
    H, W = read_ints()
    N = int(input())
    A = read_int_list()
    T = [['' for _ in range(W)] for _ in range(H)]
    ct = 0
    i, j = 0, 0
    direction = 'right'
    color_idx = 0
    while ct < H * W:
        while A[color_idx] == 0:
            color_idx += 1
        T[i][j] = str(color_idx + 1)
        A[color_idx] -= 1

        if direction == 'right':
            if j == W - 1:
                direction = 'left'
                i += 1
            else:
                j += 1
        else:  # left
            if j == 0:
                direction = 'right'
                i += 1
            else:
                j -= 1
        ct += 1

    p(T)


main()

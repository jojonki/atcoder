import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    N = int(input())
    S = []
    for _ in range(N):
        S.append(list(input()))
    # print(S)
    for i in range(N - 2, -1, -1):
        for j in range(1, 2 * N - 2):
            if S[i][j] == '#':
                if 'X' in S[i + 1][j - 1:j + 2]:
                    S[i][j] = 'X'
    for i in range(N):
        print(''.join(S[i]))


main()

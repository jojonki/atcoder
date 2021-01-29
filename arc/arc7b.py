import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    N, M = read_ints()
    T = {i: i for i in range(N + 1)}
    # print(T)
    playing = 0
    for _ in range(M):
        next_play = int(input())
        T[playing] = T[next_play]
        T[next_play] = 0
        playing = next_play

    # print(T)
    inv_T = {v: k for k, v in T.items()}
    for i in range(1, N + 1):
        print(inv_T[i])


main()

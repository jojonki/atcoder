import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


from itertools import product


def main_itertools():
    N, K = read_ints()
    T = []
    for _ in range(N):
        T.append(read_int_list())

    C = list(range(K))
    for item in product(C, repeat=N):
        # print(item)
        v = T[0][item[0]]
        for ind, vv in enumerate(item[1:]):
            v = v ^ T[ind + 1][vv]
        if v == 0:
            print('Found')
            return

    print('Nothing')


def main_dfs():
    N, K = read_ints()
    T = []
    for _ in range(N):
        T.append(read_int_list())

    def dfs(row, v):
        if row == N:
            return v == 0

        for k in range(K):
            if dfs(row + 1, v ^ T[row][k]): return True
        return False

    if dfs(0, 0):
        print('Found')
    else:
        print('Nothing')


# main()
main_dfs()

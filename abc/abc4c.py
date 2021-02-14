import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


import copy


def main():
    N = int(input())
    M = []
    cur = [1, 2, 3, 4, 5, 6]
    M.append(copy.copy(cur))
    for i in range(29):
        j = i % 5
        k = j + 1
        cur[j], cur[k] = cur[k], cur[j]
        # print(cur)
        M.append(copy.copy(cur))
        # break
    # print(len(M), M[0])
    print(''.join([str(v) for v in M[N % 30]]))


main()

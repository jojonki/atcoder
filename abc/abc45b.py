import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    M = {'a': [], 'b': [], 'c': []}
    for p in 'abc':
        for c in input():
            M[p].append(c)
    # print(M)
    np = 'a'
    while True:
        if len(M[np]) == 0:
            print(np.upper())
            return
        tmp = M[np][0]
        M[np] = M[np][1:]
        np = tmp


main()

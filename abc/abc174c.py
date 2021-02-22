import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


import math


def prime_factorize(N):
    """素因数分解
    Return:
        [{prime1, exp_count2}, {prime2, exp_count2}]
    
    ex)
        60 = 2**2 * 3 * 5
        -> [(2, 2), (3, 1), (5, 1)]
    """
    res = []
    for i in range(2, int(math.sqrt(N)) + 1):
        if N % i != 0:
            continue

        exp_ct = 0
        while N % i == 0:
            exp_ct += 1
            N = N // i
        res.append((i, exp_ct))
    if N != 1:
        res.append((N, 1))

    return res


def main():
    K = int(input())
    M = set()
    amari = 7 % K
    for i in range(K):  # mod Kの世界ではK個考えれば十分．
        if amari == 0:
            print(i + 1)
            return
        if amari in M:
            print(-1)
            return
        M.add(amari)
        amari = ((10 * amari) + 7) % K
    print(-1)


main()

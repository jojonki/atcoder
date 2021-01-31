# 合成数 N は 1 より大きく √N 以下の約数をもちます
# https://excelmath.atelierkobato.com/composite/

import math


def gcd(m, n):
    if n == 0:
        return m

    return gcd(n, m % n)


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


def get_factors(N, sort=True):
    # 約数のリストを返す
    # 12 -> 1, 2, 3, 4, 6, 12
    res = []
    for i in range(1, int(math.sqrt(N)) + 1):
        if N % i != 0:
            continue
        res.append(i)  # 12 / 2 = 6
        res.append(N // i)  # 12 / 6 = 2

    if sort:
        res.sort()

    return res


if __name__ == "__main__":
    """
    10 : [(2, 1), (5, 1)]
    16 : [(2, 4)]
    60 : [(2, 2), (3, 1), (5, 1)]
    1000000007 : [(1000000007, 1)]
    """
    for v in [10, 16, 60, 1000000007]:
        print(v, ':', prime_factorize(v))

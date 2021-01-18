# 合成数 N は 1 より大きく √N 以下の約数をもちます
# https://excelmath.atelierkobato.com/composite/

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


if __name__ == "__main__":
    """
    10 : [(2, 1), (5, 1)]
    16 : [(2, 4)]
    60 : [(2, 2), (3, 1), (5, 1)]
    1000000007 : [(1000000007, 1)]
    """
    for v in [10, 16, 60, 1000000007]:
        print(v, ':', prime_factorize(v))

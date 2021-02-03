import sys
import math
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


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
    N = int(input())
    p = prime_factorize(N)
    # print(p)
    if N == 1:
        print('Not Prime')
    else:
        for i in range(2, int(math.sqrt(N)) + 1):
            if N % i == 0:
                edge = int(str(N)[-1])
                if edge % 2 == 1 and edge != 5 and N % 3 != 0:
                    print('Prime')
                else:
                    print('Not Prime')
                return
        print('Prime')


main()

import sys
import math
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def f(n):
    if n < 2:
        return 1
    return n * f(n - 2)


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
    if N % 2 == 1:
        print(0)
        return

    ans = 0
    N = N // 2
    while N:
        ans += N // 5
        N = N // 5

    print(ans)


def main_mine():
    N = int(input())
    if N % 2 == 1:
        print(0)
        return

    ans = N // 10
    v = 50
    while N // v > 0:
        ans += N // v
        v *= 5


# print(main(8))
# for i in range(2, 100):
#     main(i)
# ans = 0
# for i in range(500):
# tmp = main(i * 10)
#     # print(tmp - ans)
#     ans = tmp
main()

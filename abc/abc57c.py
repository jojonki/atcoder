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


def F(A, B):
    return max(len(str(A)), len(str(B)))


def prod(v_list):
    ans = v_list[0]
    for v in v_list[1:]:
        ans *= v
    return ans


def main():
    N = int(input())
    C = []
    for v, exp_ct in prime_factorize(N):
        C += [v] * exp_ct
    # print(C)
    ans = INF
    for bit in range(1 << len(C)):
        A, B = [], []
        for i in range(len(C)):
            if bit >> i & 1 == 1:
                A.append(C[i])
            else:
                B.append(C[i])
        if len(A) == 0:
            A = [1]
        if len(B) == 0:
            B = [1]
        A = prod(A)
        B = prod(B)
        ans = min(ans, F(A, B))
    print(ans)


main()

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


def calc_groups(n):
    groups = []
    n_vals = 1  # グループ内の値の数
    while n > 0:
        if (n - n_vals) > n_vals:
            n -= n_vals
            groups.append(n_vals)
            n_vals += 1
        else:
            groups.append(n)
            break
    # print(groups)
    return len(groups)


def main():
    N = int(input())
    ans = 0
    res = prime_factorize(N)
    for prime, exp_ct in res:
        ans += calc_groups(exp_ct)
    print(ans)


main()

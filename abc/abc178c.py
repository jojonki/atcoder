# from techs.mod import mod_pow_rec

M = int(1e9 + 7)


def mod_pow(a, n, mod):
    if n == 0: return 1
    if n == 1: return a % mod
    if n % 2 == 0:
        t = mod_pow(a, n // 2, mod)
        return t * t % mod
    else:
        return a * mod_pow(a, n - 1, mod) % mod


# xの逆元をフェルマーの小定理で求める
def mod_inv(x, mod):
    return mod_pow(x, mod - 2, mod)


def mod_combi(n, k, mod):
    # nCk
    res = 1
    k = min(k, n - k)
    for i in range(k):
        res = (res * (n - i)) % mod
        res = (res * mod_inv(i + 1, mod)) % mod
    return res % mod


def mod_factorial(n, mod):
    res = 1
    for i in range(1, n + 1):
        res = (res * i) % mod
    return res


def main():
    N = int(input())
    res = mod_pow(10, N, M) + mod_pow(8, N, M) - 2 * mod_pow(9, N, M)
    print(res % M)
    # res = (pow(10, N, M) - pow(9, N, M) * 2 + pow(8, N, M)) % M
    # print(res)


main()

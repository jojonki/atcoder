M = 1000000007


def mod_pow(x, n, mod):
    if n == 0: return 1
    if n == 1: return x % mod
    if n % 2 == 0:
        t = mod_pow(x, n // 2, mod)
        return t * t % mod
    else:
        return x * mod_pow(x, n - 1, mod) % mod


def combi(n, k, mod):
    k = min(k, n - k)
    res = 1
    for i in range(k):
        res = (res * (n - i)) % mod
        res *= mod_pow(i + 1, mod - 2, mod)
    return res % mod


def main():
    n, a, b = map(int, input().split())
    res = mod_pow(2, n, M) - 1
    print(combi(n, a, M), combi(n, b, M))
    res -= (combi(n, a, M) + combi(n, b, M))
    res %= M
    print(res)


main()

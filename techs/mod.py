# 【競プロ】繰り返し二乗法と再帰関数
# https://math.nakaken88.com/textbook/cp-binary-exponentiation-and-recursive-function/
# 「1000000007 で割ったあまり」の求め方を総特集！ 〜 逆元から離散対数まで 〜
# https://qiita.com/drken/items/3b4fdf0a78e7a138cd9a#4-%E7%B4%AF%E4%B9%97-an
# pow, mod_inv
# https://atcoder.jp/contests/abc156/tasks/abc156_d


def mod_pow_rec(a, n, mod):
    if n == 0: return 1
    if n == 1: return a % mod
    if n % 2 == 0:
        t = mod_pow_rec(a, n // 2, mod)
        return t * t % mod
    else:
        return a * mod_pow_rec(a, n - 1, mod) % mod


def mod_pow_for(a, n, mod):
    res = 1
    while n > 0:
        if n & 1:
            res = res * a % mod
        a = a * a % mod
        n = n >> 1
    return res % mod


# xの逆元をフェルマーの小定理で求める
def mod_inv(x, mod):
    return mod_pow_rec(x, mod - 2, mod)


def mod_combi(n, k, mod):
    # nCk
    res = 1
    k = min(k, n - k)
    for i in range(k):
        res = (res * (n - i)) % mod
        res = (res * mod_inv(i + 1, mod)) % mod
    return res % mod


if __name__ == "__main__":
    M = 1000000007
    for (x, n, res) in [(1, 0, 1), (2, 1000000006, 1), (3, 45, 644897553)]:
        assert (mod_pow_rec(x, n, M) == res)
        assert (mod_pow_for(x, n, M) == res)

    assert mod_inv(8, M) == 125000001

    assert mod_combi(1000000000, 141421, M) == 516595147
    assert mod_combi(1000000000, 173205, M) == 589953354

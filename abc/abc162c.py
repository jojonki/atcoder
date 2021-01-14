def gcd(m, n, o):
    return _gcd(_gcd(m, n), o)


def _gcd(m, n):
    if n == 0:
        return m

    return _gcd(n, m % n)


def main():
    K = int(input())
    ans = 0

    for a in range(1, K + 1):
        # 3桁同じ
        ans += gcd(a, a, a)

        # 2桁同じ
        for c in range(1, K + 1):
            if c == a:
                continue
            ans += gcd(a, a, c) * 3

        # 1桁同じ（全桁違う）
        if a < K - 1:
            for b in range(a + 1, K):
                for c in range(b + 1, K + 1):
                    ans += gcd(a, b, c) * 6
    print(ans)


main()

def gcd(m, n):
    if n == 0:
        return m

    return gcd(n, m % n)


def main_uso():
    A, B = map(int, input().split())
    g = gcd(A, B)
    print(int(A * B / g))


def main():
    A, B = map(int, input().split())
    if A > B:
        A, B = B, A
    # A<B
    for i in range(0, A * B + 1, B):
        if i == 0: continue
        if i % A == 0 and i % B == 0:
            print(i)
            return


main()

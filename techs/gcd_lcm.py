def gcd(m, n):
    if n == 0:
        return m

    return gcd(n, m % n)


def lcm(a, b):
    # Least Common Multiple
    # a*b = gcd(a, b) * l
    # l = a / gcd(a, b) * b
    return a // gcd(a, b) * b


print(gcd(15, 6))
print(gcd(51, 15))
print(gcd(15, 51))
print(gcd(1071, 1029))
print(lcm(8, 12))

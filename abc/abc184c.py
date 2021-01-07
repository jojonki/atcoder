def main():
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())
    p, q = abs(r2 - r1), abs(c2 - c1)
    if p == q == 0:
        print(0)
    elif p == q or p + q <= 3:
        print(1)
    elif (p + q) % 2 == 0 or p + q <= 6 or abs(p - q) <= 3:
        print(2)
    else:
        print(3)


main()

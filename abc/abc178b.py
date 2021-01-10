def main():
    a, b, c, d = map(int, input().split())
    v = a * c
    v = max(v, a * d)
    v = max(v, b * c)
    v = max(v, b * d)
    print(v)


main()

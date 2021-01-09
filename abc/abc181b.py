def main():
    N = int(input())
    res = 0
    for _ in range(N):
        a, b = map(int, input().split())
        n = b - a + 1
        res += a * n + int(n * (n - 1) / 2)

    print(res)


main()

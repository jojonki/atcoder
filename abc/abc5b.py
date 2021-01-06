def main():
    N = int(input())
    res = float('inf')
    for _ in range(N):
        res = min(res, int(input()))
    print(res)


main()

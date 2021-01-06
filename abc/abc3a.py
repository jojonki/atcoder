def main():
    N = int(input())
    res = 0
    for i in range(N):
        res += (i + 1) * 10000 / N
    print(res)


main()

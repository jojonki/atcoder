def main():
    L = int(input())
    res = 1
    for i in range(1, 12):
        res = res * (L - i) // i

    print(int(res))


main()

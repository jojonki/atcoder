def main():
    X = int(input())
    v = 100
    res = 0
    while v < X:
        v = v * 101 // 100
        res += 1
    print(res)


main()

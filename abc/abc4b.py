def main():
    d = []
    for _ in range(4):
        d.append(input().split())

    for i in range(3, -1, -1):
        t = [d[i][j] for j in range(3, -1, -1)]
        print(' '.join(t))


main()

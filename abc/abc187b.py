def main():
    N = int(input())
    P = []
    for _ in range(N):
        x, y = map(int, input().split())
        P.append((x, y))
    ct = 0
    for i in range(N - 1):
        for j in range(i + 1, N):
            x_i, y_i = P[i]
            x_j, y_j = P[j]
            if abs((y_i - y_j) / (x_i - x_j)) <= 1:
                ct += 1
    print(ct)


main()

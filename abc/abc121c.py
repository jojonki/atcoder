def main():
    N, M = map(int, input().split())
    d = []
    for _ in range(N):
        a, b = map(int, input().split())
        d.append((a, b))

    d.sort(key=lambda x: x[0])

    left = M
    cost = 0
    for a, b in d:
        if left < b:
            cost += a * left
            break
        else:
            cost += a * b
            left -= b
    print(cost)


main()

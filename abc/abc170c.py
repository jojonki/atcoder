def main():
    X, N = map(int, input().split())
    P = set(map(int, input().split()))
    ans = -1
    min_v = float('inf')
    for v in range(-1000, 1001):
        if v not in P:
            diff = abs(X - v)
            if diff < min_v:
                ans = v
                min_v = diff
    print(ans)


main()

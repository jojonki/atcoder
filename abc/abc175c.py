def main():
    X, K, D = map(int, input().split())
    a = round((K * D - X) / (2 * D))
    # print(a)
    a = min(K, max(0, a))
    X = X + a * D - (K - a) * D
    print(abs(X))


main()

def main():
    X, Y = map(int, input().split())
    for n_tsuru in range(X + 1):
        if n_tsuru * 2 + 4 * (X - n_tsuru) == Y:
            print('Yes')
            return
    print('No')


main()

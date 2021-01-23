def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    N = int(input())
    S = list(input())
    ans = 0
    for i in range(N - 1):
        X, Y = set(S[:i]), set(S[i:])
        ct = 0
        for c in X:
            if c in Y:
                ct += 1
        ans = max(ct, ans)
    print(ans)


main()

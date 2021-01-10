def main():
    N, K = map(int, input().split())
    s = set(i for i in range(N))
    for i in range(K):
        _d = input()
        for a in map(int, input().split()):
            if a - 1 in s:
                s.remove(a - 1)
    print(len(s))


main()

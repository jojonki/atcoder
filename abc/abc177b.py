def main():
    S, T = input(), input()
    res = float('inf')
    for i in range(len(S) - len(T) + 1):
        sub = S[i:i + len(T)]
        # print(sub)
        ct = 0
        for c1, c2 in zip(sub, T):
            if c1 != c2:
                ct += 1
        res = min(res, ct)
    print(res)


main()

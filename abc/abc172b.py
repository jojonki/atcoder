def main():
    S, T = input(), input()
    res = 0
    for c1, c2 in zip(S, T):
        if c1 != c2:
            res += 1

    print(res)


main()

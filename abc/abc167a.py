def main():
    s, t = input(), input()
    if s == t[:-1] and len(s) + 1 == len(t):
        print('Yes')
    else:
        print('No')


main()

def main():
    N = int(input())
    d1, d2 = set(), set()
    for _ in range(N):
        c = input()
        if c[0] == '!':
            d2.add(c[1:])
        else:
            d1.add(c)
    for s in d1:
        if s in d2:
            print(s)
            return
    print('satisfiable')


main()

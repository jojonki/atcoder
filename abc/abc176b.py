def main():
    N = input()
    res = 0
    for d in N:
        res += int(d)
    if res % 9 == 0:
        print('Yes')
    else:
        print('No')


main()

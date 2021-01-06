def check(n):
    if n % 2 == 0 or (n + 1) % 3 == 0:
        return False
    else:
        return True


def main():
    N = int(input())
    ct = 0
    for a in map(int, input().split()):
        while check(a) is False:
            a -= 1
            ct += 1
    print(ct)


main()

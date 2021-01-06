def check(v, div):
    while v > 0:
        digit = v % div
        if digit == 7:
            return True
        v = v // div
    return False


def main():
    N = int(input())
    ct = 0
    for v in range(N + 1):
        if check(v, 10) or check(v, 8):
            ct += 1
    print(N - ct)


main()

import math


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    X = int(input())
    ans = -float('inf')
    max_b = int(math.sqrt(X)) + 1
    for b in range(1, max_b + 1):
        for p in range(1, 1000):
            v = math.pow(b, p)
            if v > X:
                break
            ans = max(ans, v)
    print(int(ans))


main()

import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    n = int(input())
    n -= 1
    # if n <= 20:
    #     print(n)
    # elif n <= 40:
    #     n -= 20
    #     print(21 - n)
    # elif n <= 60:
    #     n -= 20 * 2
    #     print(n)

    if (n // 20) % 2 == 0:
        n -= 20 * (n // 20)
        print(n + 1)
    else:
        n -= 20 * (n // 20)
        # print(n)
        print(20 - n)


main()

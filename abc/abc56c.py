import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    X = int(input())

    # def rec(pos, i, steps):
    #     if pos == X:
    #         return steps

    # rec(pos - i, i + 1, steps + 1)
    # rec(pos, i + 1, steps + 1)
    # rec(pos + i, i + 1, steps + 1)

    # ans = rec(0, 1, 0)
    max_range = 0
    steps = 0
    while max_range < X:
        max_range += steps + 1
        steps += 1
    print(steps)

    # print(ans)


main()

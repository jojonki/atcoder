import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    s = input()
    k = int(input())
    p = set()
    for i in range(len(s) - k + 1):
        p.add(s[i:i + k])
    # print(p)
    print(len(p))


main()

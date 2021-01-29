import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    ans = ''
    for c in input():
        if c == 'B':
            if len(ans) > 0:
                ans = ans[:-1]
        else:
            ans += c
    print(ans)


main()

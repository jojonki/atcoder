import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    N = int(input())
    hasu = []
    ans = 0

    for _ in range(N):
        v = int(input())
        if v % 10 != 0:
            hasu.append(v)
        ans += v
    hasu.sort()

    if ans % 10 != 0:
        print(ans)
    elif hasu:
        ans -= hasu[0]
        print(ans)
    else:
        print(0)


main()

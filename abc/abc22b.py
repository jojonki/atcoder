import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    N = int(input())
    m = set()
    ans = 0
    for _ in range(N):
        a = int(input())
        if a in m:
            ans += 1
        m.add(a)
    print(ans)


main()

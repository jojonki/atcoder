import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


cum = {}


def C(v):
    if v not in cum:
        cum[v] = sum([i for i in range(1, v + 1)])
    return cum[v]


def main():
    N = int(input())
    cur = INF
    streak = 0
    ans = N
    for a in read_int_list():
        if a > cur:
            streak += 1
        else:
            ans += C(streak)
            streak = 0
        cur = a
    ans += C(streak)
    print(ans)


main()

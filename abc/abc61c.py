import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    N, K = read_ints()
    d = []
    for i in range(N):
        a, b = read_ints()
        d.append((a, b))
    d.sort(key=lambda x: x[0])

    cur = 0
    for a, b in d:
        if cur + b >= K:
            print(a)
            return
        else:
            cur += b


main()

import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    Q, H, S, D = read_ints()
    N = int(input())
    P = {0.25: Q, 0.5: H, 1: S, 2: D}
    cost = {0.25: Q * 4, 0.5: H * 2, 1: S, 2: D // 2}
    reasonable = sorted(cost.items(), key=lambda x: x[1])

    # print(cost[0.25])
    ans = 0
    # print(reasonable)
    for l, price in reasonable:
        # print(N, l, price)
        n = N // l
        # print('n', n, 'P[l]', P[l])
        ans += int(n * P[l])

        N -= int(n * l)
        if N == 0:
            break
    print(int(ans))


main()

import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main_wa():
    N = int(input())
    A = read_int_list()
    ans = 0
    v1 = A[0]
    for i in range(1, N - 1):
        v2 = A[i]
        if v1 >= 0:
            ans += v1
            v1 = v2
        else:
            ans += (-v1)
            v1 = -v2

    v2 = A[-1]
    if v1 * v2 > 0:
        ans += (abs(v1) + (abs(v2)))
    else:
        if abs(v1) > abs(v2):
            ans += abs(v1)
            ans -= abs(v2)
        else:
            ans += abs(v2)
            ans -= abs(v1)

    print(ans)


def main():
    N = int(input())
    A = read_int_list()
    neg_ct = 0
    min_abs_v = INF
    S = 0
    for a in A:
        min_abs_v = min(min_abs_v, abs(a))
        if a < 0:
            neg_ct += 1
        S += abs(a)

    if neg_ct % 2 == 0:
        print(S)
    else:
        print(S - min_abs_v * 2)


main()

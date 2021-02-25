import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    N, K = read_ints()
    A = read_int_list()

    ans = 0
    max_dup = min(K, N - K + 1)
    for i in range(max_dup - 1):
        ans += A[i] * (i + 1) + A[-i - 1] * (i + 1)
    # print(ans)

    r = -max_dup + 1
    if r == 0:
        ans += sum(A[max_dup - 1:]) * max_dup
    else:
        ans += sum(A[max_dup - 1:r]) * max_dup
    print(ans)


main()

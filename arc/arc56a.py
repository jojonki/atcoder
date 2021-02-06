import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    A, B, K, L = read_ints()
    BL = B / L
    if A <= BL:
        print(K * A)
    else:
        if K % L == 0:
            print(B * (K // L))
        else:
            cand1 = B * (K // L + 1)
            cand2 = B * (K // L) + A * (K - L * (K // L))
            print(min(cand1, cand2))


main()

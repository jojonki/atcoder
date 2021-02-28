import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    N = int(input())
    A = read_int_list()
    M = 0
    B = [0] * N
    b = set()
    cid = N // 2 + 1

    for i in range(cid - 1, N):
        if A[i]:
            M += 1
            # B.append(i)
            B[i] = 1
            b.add(i + 1)
    # print(B)

    for i in range(cid - 2, -1, -1):
        tmp = 0
        j = 2
        while (i + 1) * j < N + 1:
            tmp += B[(i + 1) * j - 1]
            j += 1
        if tmp % 2 != A[i]:
            B[i] = 1
            b.add(i + 1)
            M += 1

    # print(B)
    print(M)
    if b:
        print(' '.join(str(v) for v in b))


main()

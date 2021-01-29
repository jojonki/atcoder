import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(str, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    N = int(input())
    A = read_int_list()
    B = [0] * N
    is_left = True
    left, right = 0, N - 1
    for i in range(N):
        if is_left:
            B[left] = A[N - 1 - i]
            left += 1
            is_left = False
        else:
            B[right] = A[N - 1 - i]
            right -= 1
            is_left = True
    print(' '.join(B))


main()

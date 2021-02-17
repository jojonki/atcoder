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
    A = [a - 1 for a in A]
    ans = 0
    for i in range(N):
        j = A[i]
        if i < j:
            if A[j] == i:
                ans += 1
    print(ans)


main()

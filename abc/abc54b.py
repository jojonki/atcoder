import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_list():
    return list(input())


def read_ints():
    return map(int, input().split())


def p(matrix):
    print('\n'.join([''.join(a) for a in matrix]))
    print()


def match(mA, mB):
    strA = '\n'.join([''.join(a) for a in mA])
    strB = '\n'.join([''.join(b) for b in mB])
    return strA == strB


def main():
    N, M = read_ints()
    A, B = [], []
    for _ in range(N):
        A.append(read_list())
    for _ in range(M):
        B.append(read_list())
    # p(A)
    # p(B)
    for row in range(N - M + 1):
        for col in range(N - M + 1):
            subA = [r[col:col + M] for r in A[row:row + M]]
            if match(subA, B):
                print('Yes')
                return
    print('No')


main()

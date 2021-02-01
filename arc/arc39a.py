import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


import copy


def main():
    A, B = input().split()
    A = list(A)
    B = list(B)
    ans = int(''.join(A)) - int(''.join(B))
    # print('A', A)
    for i in range(3):
        tmp = copy.copy(A)
        tmp[i] = '9'
        tmp = int(''.join(tmp))
        # print(tmp)
        ans = max(ans, tmp - int(''.join(B)))
    for i in range(3):
        tmp = copy.copy(B)
        if i == 0:
            tmp[i] = '1'
        else:
            tmp[i] = '0'
        tmp = int(''.join(tmp))
        ans = max(ans, int(''.join(A)) - tmp)
    print(ans)


main()

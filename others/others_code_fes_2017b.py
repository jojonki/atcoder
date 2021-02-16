import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    N = int(input())
    myP = {}
    for d in read_int_list():
        if d not in myP:
            myP[d] = 0
        myP[d] += 1

    M = int(input())
    for t in read_int_list():
        if t not in myP or myP[t] == 0:
            print('NO')
            return
        else:
            myP[t] -= 1
    print('YES')


main()

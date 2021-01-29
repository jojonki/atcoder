import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    m = int(input())
    km = m / 1000.0
    if km < 0.1:
        print('00')
    elif km <= 5:
        vv = str(int(km * 10))
        if len(vv) == 1:
            vv = '0' + vv
        print(vv)
    elif km <= 30:
        km += 50
        print(int(km))
    elif km <= 70:
        vv = int(((km - 30) / 5) + 80)
        print(vv)
    else:
        print(89)


main()

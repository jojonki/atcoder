import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


from math import ceil


def main():
    N = int(input())
    C = read_int_list()
    Q = int(input())
    ans = 0

    min_a = min(C)
    min_odd_a = INF
    for i in range(N):
        if (i + 1) % 2 == 1:
            min_odd_a = min(min_odd_a, C[i])
    same = min_a == min_odd_a
    # print(min_a, min_odd_a)
    s, z = 0, 0
    for _ in range(Q):
        cmd = read_int_list()
        # print(
        #     f'ans={ans}, min_a={min_a}, min_odd_a={min_odd_a}, {C}  cmd={cmd}')
        if cmd[0] == 1:
            x, a = cmd[1], cmd[2]
            x -= 1
            if (x + 1) % 2 == 1:
                if C[x] - s - z >= a:
                    ans += a
                    C[x] -= a
                min_odd_a = min(min_odd_a, C[x] - s - z)
                min_a = min(min_a, C[x] - s - z)
            else:
                if C[x] - s >= a:
                    ans += a
                    C[x] -= a
                min_a = min(min_a, C[x] - s)
        elif cmd[0] == 2:
            a = cmd[1]
            if min_odd_a >= a:
                ans += ceil(N / 2) * a
                min_odd_a -= a
                min_a = min(min_a, min_odd_a)
                z += a
        else:
            a = cmd[1]
            if min_a >= a:
                ans += a * N
                min_a -= a
                min_odd_a -= a
                s += a
    print(ans)


main()

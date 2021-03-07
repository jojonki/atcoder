import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


from collections import defaultdict


def main():
    N, Q = read_ints()
    follows = [set() for _ in range(N)]
    for _ in range(Q):
        cmd = read_int_list()
        if cmd[0] == 1:
            a, b = cmd[1], cmd[2]
            a -= 1
            b -= 1
            follows[a].add(b)
        elif cmd[0] == 2:
            a = cmd[1]
            a -= 1
            for x in range(N):
                if a == x:
                    continue
                if a in follows[x]:
                    follows[a].add(x)
        else:
            a = cmd[1]
            a -= 1
            for x in list(follows[a]):
                for y in follows[x]:
                    follows[a].add(y)

    for i in range(N):
        row = ''
        for j in range(N):
            if i != j and j in follows[i]:
                row += 'Y'
            else:
                row += 'N'
        print(row)


main()

import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    M = {
        'b': 1,
        'c': 1,
        'd': 2,
        'w': 2,
        't': 3,
        'j': 3,
        'f': 4,
        'q': 4,
        'l': 5,
        'v': 5,
        's': 6,
        'x': 6,
        'p': 7,
        'm': 7,
        'h': 8,
        'k': 8,
        'n': 9,
        'g': 9,
        'z': 0,
        'r': 0,
    }
    N = int(input())
    res = []
    for s in input().split():
        s = s.lower()
        v = ''.join([str(M[c]) for c in s if c in M])
        if v:
            res.append(v)
    # print(res)
    print(*res)


main()

import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    N, M = read_ints()
    used = set()
    history = []
    for _ in range(M):
        a = input()
        history.append(a)

    W = []
    for th_id in history[::-1]:
        if th_id not in used:
            W.append(th_id)
            used.add(th_id)

    res = W + [str(i + 1) for i in range(N) if str(i + 1) not in used]
    print('\n'.join(res))


main()

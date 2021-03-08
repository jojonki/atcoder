import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


from math import ceil


def main():
    N, H = read_ints()
    AB = []

    max_a = 0
    for _ in range(N):
        a, b = read_ints()
        max_a = max(max_a, a)
        AB.append((a, b))

    C = []
    total_b = 0
    for a, b in AB:
        if b > max_a:
            total_b += b
            C.append(b)
    # C += [max_a] * ((H - total_b) // max_a + 1)

    C.sort(reverse=True)
    # print(C)

    atk = 0
    for i in range(len(C)):
        v = max(C[i], max_a)
        if atk + v >= H:
            print(i + 1)
            return
        # print(C[i])
        atk += C[i]
    # print(H, atk, H - atk)
    # print('max_a', max_a)
    ans = len(C) + ceil((H - atk) / max_a)
    print(ans)


main()

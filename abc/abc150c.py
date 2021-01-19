from itertools import permutations


def tuple_to_int(tp):
    return int(''.join(map(str, list(tp))))


def main():
    N = int(input())
    d = [i + 1 for i in range(N)]
    P = list(map(int, input().split()))
    P = tuple_to_int(P)
    Q = list(map(int, input().split()))
    Q = tuple_to_int(Q)

    data = []
    for v in permutations(d, N):
        data.append(tuple_to_int(v))
    data.sort()
    print(abs(data.index(P) - data.index(Q)))


main()

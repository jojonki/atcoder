from itertools import permutations


def main():
    N, K = map(int, input().split())
    T = []
    for _ in range(N):
        seq = list(map(int, input().split()))
        T.append(seq)
    res = 0
    # print(T)
    for seq in permutations(list(range(1, N)), N - 1):
        route = [0] + list(seq) + [0]
        cost = 0
        for i in range(1, len(route)):
            cost += T[route[i - 1]][route[i]]
            if cost > K:
                break
        if cost == K:
            res += 1

        # print(route)
    # print(T)
    print(res)


main()

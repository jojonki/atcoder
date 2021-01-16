def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A = [a - 1 for a in A]
    memo = {0: 0}  # to_idx: k
    route = [0]
    to_idx = 0
    while True:
        src_idx = to_idx
        to_idx = A[src_idx]
        if to_idx in memo:
            # print('break: to', to_idx, 'src', src_idx)
            loop_start = memo[to_idx]
            break
        route.append(to_idx)
        memo[to_idx] = len(route) - 1

    if K < len(route):
        print(route[K] + 1)
    else:
        loop_route = route[loop_start:]
        K -= loop_start
        print(loop_route[K % len(loop_route)] + 1)


main()

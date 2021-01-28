def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


from collections import defaultdict


def main():
    memo = defaultdict(int)
    N = int(input())
    A = read_int_list()
    for v in A:
        memo[v] += 1
    ans = 0
    for v, ct in memo.items():
        if ct < v:
            ans += ct
        else:
            ans += ct - v
    print(ans)


main()

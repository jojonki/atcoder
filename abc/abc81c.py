def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


from collections import defaultdict


def main():
    N, K = read_ints()
    memo = defaultdict(int)
    for a in read_int_list():
        memo[a] += 1
    total_balls = len(memo)
    vals = sorted(memo.values())
    ans = 0
    for i in range(total_balls - K):
        ans += vals[i]
    print(ans)


main()

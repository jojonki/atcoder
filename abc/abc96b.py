def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    A, B, C = read_ints()
    K = int(input())
    max_v = max(A, B, C)
    ans = 0
    for v in [A, B, C]:
        if v == max_v:
            ans += v * (2**K)
            max_v = float('inf')
        else:
            ans += v
    print(ans)


main()

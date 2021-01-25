def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    D = read_int_list()
    D.sort()
    ans = 0
    bc_diff = D[-1] - D[-2]
    ans += bc_diff
    D[0] += bc_diff
    # print(D)
    ac_diff = D[-1] - D[0]
    ans += ac_diff // 2
    if ac_diff % 2 == 1:
        ans += 2
    print(ans)


main()

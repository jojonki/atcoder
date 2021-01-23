def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def n_2(v):
    ct = 0
    while v % 2 == 0:
        ct += 1
        v = v // 2
    return ct


def main():
    N = int(input())
    A = read_int_list()
    ans = 0
    for a in A:
        ans += n_2(a)
    print(ans)


main()

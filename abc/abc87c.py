def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    N = int(input())
    A1 = read_int_list()
    A2 = read_int_list()
    ans = 0
    for i in range(N):
        v = sum(A1[:i + 1]) + sum(A2[i:])
        ans = max(ans, v)
    print(ans)


main()

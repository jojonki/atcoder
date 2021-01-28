def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    N = int(input())
    L = [2, 1]
    if N < 2:
        print(L[N])
    else:
        for i in range(2, N + 1):
            L.append(L[i - 1] + L[i - 2])
        print(L[N])


main()

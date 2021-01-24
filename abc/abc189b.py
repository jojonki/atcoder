def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    N, X = read_ints()
    amount = 0
    for i in range(N):
        V, P = read_ints()
        # print(V * (P / 100))
        amount += V * P
        # print(amount)

        if amount > X * 100:
            print(i + 1)
            return
    print(-1)


main()

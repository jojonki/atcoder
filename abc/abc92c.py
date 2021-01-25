def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    N = int(input())
    A = read_int_list()
    A.append(0)  # tail
    C = [abs(A[0])]
    S = C[0]
    for i in range(N):
        cost = abs(A[i + 1] - A[i])
        C.append(cost)
        S += cost
    for i in range(N):
        if i == 0:
            cost = S - ((C[i] + C[i + 1]) - abs(A[i + 1]))
        else:
            cost = S - ((C[i] + C[i + 1]) - abs(A[i + 1] - A[i - 1]))
        print(cost)
    # print(C)
    # print(S)


main()

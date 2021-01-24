def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


import copy


def main():
    N = int(input())
    X = read_int_list()
    X_sort = copy.copy(X)
    X_sort.sort()
    # print(X, X_sort)
    m_l, m_r = X_sort[N // 2 - 1], X_sort[N // 2]
    # print(m_l, m_r)
    for x in X:
        if x <= m_l:
            print(m_r)
        else:
            print(m_l)


main()

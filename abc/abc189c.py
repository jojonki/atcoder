def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    N = int(input())
    # A = read_int_list()
    A = list(map(int, input().split()))
    am = 0
    for i in range(N):
        amin = A[i]
        for n in range(i, N):
            amin = min(A[n], amin)
            aa = amin * (n - i + 1)
            if aa > am:
                am = aa
            #print(i,n,am,aa,amin)
    print(am)
    # max_v = 0
    # # min_v_dp = [[0] * N for _ in range(N)]  # [l, r]での最小値
    # for l in range(N):
    #     min_v = A[l]
    #     for r in range(l, N):
    #         min_v = min(min_v, A[r])
    #         tmp_v = (r - l + 1) * min_v
    #         if tmp_v > max_v:
    #             max_v = tmp_v
    #         # max_v = max((r - l + 1) * min_v, max_v)

    # print(max_v)


main()

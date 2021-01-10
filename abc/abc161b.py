def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    th = sum(A) / (4 * M)
    ct = 0
    for a in A:
        # print(a, th)
        if a >= th:
            ct += 1
    if ct >= M:
        print('Yes')
    else:
        print('No')


main()

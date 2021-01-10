def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    if A[0] == 0:
        print(0)
        return

    res = A[0]
    for i in range(1, N):
        res *= A[i]
        if res > 1e18:
            print('-1')
            return
    print(res)


main()

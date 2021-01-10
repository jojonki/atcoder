def main():
    A, B, C, K = map(int, input().split())
    res = 0
    if A > 0:
        if K > A:
            res += A
            K -= A
            A = 0
        else:
            res += K
            K = 0
            print(res)
            return

    if B > 0:
        if K > B:
            K -= B
            B = 0
        else:
            print(res)
            return

    res -= K

    print(res)


main()

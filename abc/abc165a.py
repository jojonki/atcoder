def main():
    K = int(input())
    A, B = map(int, input().split())
    for v in range(A, B + 1):
        if v % K == 0:
            print('OK')
            return
    print('NG')


main()

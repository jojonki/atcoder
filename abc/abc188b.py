def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    res = 0
    for a, b in zip(A, B):
        res += a * b
    if res == 0:
        print('Yes')
    else:
        print('No')


main()

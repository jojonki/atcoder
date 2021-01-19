# https://drken1215.hatenablog.com/entry/2020/06/22/122500
def main():
    N = int(input())
    A = list(map(int, input().split()))
    X = []
    B = A[0]
    for i in range(1, len(A)):
        B = B ^ A[i]

    for i in range(N):
        X.append(str(B ^ A[i]))
    print(' '.join(X))


main()

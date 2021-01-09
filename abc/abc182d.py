def main():
    N = int(input())
    A = list(map(int, input().split()))

    S = [A[0]]  # 累積和=A1,...,Ai実行後のdiff
    H = [A[0]]  # i実行後の絶対高さ
    D = [max(0, A[0])]  # A1,...,Ai実行後の最高到達diff

    max_v = D[0]
    for i in range(1, N):
        S.append(S[i - 1] + A[i])
        H.append(H[i - 1] + S[i])  # 開始地点+i実行後のdiff
        D.append(max(S[i], D[i - 1]))  # 最高到達diffの更新
        max_v = max(max_v, H[i - 1] + D[i])  # 開始地点+最高到達diffで更新

    print(max_v)


main()

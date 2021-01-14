def main():
    N = int(input())
    S = input()
    memo = {'R': 0, 'G': 0, 'B': 0}
    for c in S:
        memo[c] += 1
    ans = memo['R'] * memo['G'] * memo['B']
    for i in range(N):
        for j in range(i + 1, N):
            k = j + (j - i)

            if k >= N:
                break
            if S[i] != S[j] and S[i] != S[k] and S[j] != S[k]:
                # print(S[i], S[j], S[k])
                ans -= 1

    print(ans)


main()

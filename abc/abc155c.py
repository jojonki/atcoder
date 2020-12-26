def main():
    N = int(input())
    S = {}
    for _ in range(N):
        s = input()
        if s not in S:
            S[s] = 0
        S[s] += 1
    maxCount = max(S.values())
    res = [s for s, ct in S.items() if ct == maxCount]
    res = sorted(res)
    for s in res:
        print(s)


    

main()
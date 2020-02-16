def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    maxI = 0
    maxV = sum(P[:K])
    curV = maxV
    for i in range(1, N-K+1):
        curV = curV + P[i+K-1] - P[i-1]
        if curV > maxV:
            maxV = curV
            maxI = i

    res = (sum(P[maxI:maxI+K]) + K) / 2.0
    print(res)

main()
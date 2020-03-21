def main():
    N, M, C = map(int, input().split())
    A = []
    res = 0
    B = list(map(int, input().split()))
    for _ in range(N):
        result = C
        for i, a in enumerate(list(map(int, input().split()))):
            result += a * B[i]
        if result > 0:
            res += 1
    print(res)
    

main()
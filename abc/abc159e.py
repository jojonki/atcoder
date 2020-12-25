def main():
    H, W, K = map(int, input().split())
    S = []
    for _ in range(H):
        row = list(map(int, input().split()))
        S.append(row)
    print(S)
    

main()
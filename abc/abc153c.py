def main():
    N, K = map(int, input().split())
    H = list(map(int, input().split()))
    H = sorted(H)[::-1]
    if K >= len(H):
        print(0)
    else:
        print(sum(H[K:]))
    

main()
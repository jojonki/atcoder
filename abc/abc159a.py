def main():
    N, M = map(int, input().split())
    res = 0
    res += (N * (N-1)) //2
    if M > 1:
        res += (M*(M-1))//2
    print(res)
    

main()
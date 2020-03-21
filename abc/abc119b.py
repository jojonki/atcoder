def main():
    BTC = 380000.0
    N = int(input())
    res = 0
    for _ in range(N):
        x, u = input().split()
        x = float(x)
        if u == 'JPY':
            res += x
        else:
            res += BTC * x
    print(res)
    

main()
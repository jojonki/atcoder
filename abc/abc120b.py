def main():
    a, b, k = map(int, input().split())
    ct = 0
    res = []
    for i in range(1, min(a, b)+1):
        if a % i ==0 and b % i == 0:
            res.append(i)
    print(res[-k])

    

main()
def main():
    X = int(input())
    res = 0
    ct = X//500
    res += 1000 * ct
    X -= ct * 500

    ct = X //5
    res += 5 * ct
    print(res)
    

main()
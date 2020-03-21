def main():
    cost, budget, maxCount = map(int, input().split())
    ct = budget // cost
    print(min(maxCount, ct))
    

main()
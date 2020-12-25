def main():
    K, S = map(int, input().split())
    # print(K, S)
    ct = 0
    for x in range(K + 1):
        if x > S:
            break
        for y in range(K + 1):
            if x + y > S:
                break
            if 0 <= S - x - y <= K:
                ct += 1
    print(ct)


main()

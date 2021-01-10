def main():
    N = int(input())
    streak = 0
    for _ in range(N):
        d1, d2 = map(int, input().split())
        if d1 == d2:
            streak += 1
        else:
            streak = 0
        if streak == 3:
            print('Yes')
            return
    print('No')


main()

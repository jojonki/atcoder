def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    cur = 1
    for a in A:
        if a != cur:
            ans += 1
        else:
            cur += 1
    if ans == N:
        print(-1)
    else:
        print(ans)


main()

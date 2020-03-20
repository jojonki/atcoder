def main():
    A, B, X = map(int, input().split())
    ok, ng = 0, 10**9+1
    while abs(ng-ok) > 1:
        mid = (ok + ng) // 2
        if X < A*mid + B*len(str(mid)):
            ng = mid
        else:
            ok = mid
    print(ok)

main()
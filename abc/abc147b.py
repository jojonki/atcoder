def main():
    S = input()
    N = len(S)
    l, r = 0, N-1
    res = 0
    while l < r:
        lc = S[l]
        rc = S[r]
        if lc != rc:
            res += 1
        l += 1
        r -= 1

    print(res)

    

main()
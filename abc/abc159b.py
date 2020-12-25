def main():
    S = input()
    def helper(s):
        l, r = 0, len(s) -1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    N = len(S)
    if helper(S) and helper(S[:(N-1)//2]) and helper(S[(N+3)//2-1:]):
        print('Yes')
    else:
        print('No')
    

main()
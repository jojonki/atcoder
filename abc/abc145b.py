def main():
    N = int(input())
    S = input()
    half = N // 2
    if N % 2 != 0:
        print('No')
    else:
        if S[:half] == S[half:]:
            print('Yes')
        else:
            print('No')
    

main()
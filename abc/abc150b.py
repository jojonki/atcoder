def main():
    N = int(input())
    S = input()
    ct = 0
    for i in range(N-2):
        p = S[i:i+3]
        if p == 'ABC':
            ct += 1

    print(ct)
    

main()
def main():
    N_str = input()
    N = int(N_str)
    S = 0
    for c in N_str:
        S += int(c)
    if N % S == 0:
        print('Yes')
    else:
        print('No')


main()

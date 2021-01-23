def main():
    S, T = input(), input()
    if S == T:
        print('Yes')
        return
    for shift in range(1, len(T)):
        kaiten = S[-shift:] + S[:-shift]
        # print(kaiten)
        if kaiten == T:
            print('Yes')
            return
    print('No')


main()

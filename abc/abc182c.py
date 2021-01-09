def main():
    N = input()
    keta = len(N)
    N = int(N)
    yojo = [0, 0, 0]
    S = 0
    while N > 0:
        digit = (N % 10)
        yo = digit % 3
        S = (S + yo) % 3
        yojo[yo] += 1

        N = N // 10
    # print(S, yojo)
    if S == 0:
        print(0)
        return
    elif S == 1:
        if yojo[1] > 0 and keta > 1:
            print(1)
            return
        elif yojo[2] >= 2 and keta > 2:
            print(2)
            return
    elif S == 2:
        if yojo[2] > 0 and keta > 1:
            print(1)
            return
        elif yojo[1] >= 2 and keta > 2:
            print(2)
            return
    print(-1)


main()

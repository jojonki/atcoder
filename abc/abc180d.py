from math import pow


def main():
    X, Y, A, B = map(int, input().split())
    i = 0
    power = X
    while power < Y:
        kakomon = X * pow(A, (i + 1))
        atcoder = power + B
        if kakomon < atcoder:
            power = kakomon
            if power >= Y:
                break
            # print('@kakomon', power)
        else:
            power = atcoder
            if power >= Y:
                break
            # print('@atcoder', power)
            # i += (Y - power) // B

            # break
        if power >= Y:
            break
        i += 1

    print(int(i))


main()

from math import pow


def main():
    X, Y, A, B = map(int, input().split())
    i = 0
    while X < Y:
        kakomon = X * A
        atcoder = X + B
        if kakomon < atcoder:
            X = kakomon
            if X >= Y:
                break
            i += 1
        else:
            i += (Y - X - 1) // B
            break

    print(int(i))


main()

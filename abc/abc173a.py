from math import ceil


def main():
    N = int(input())
    maisu = ceil(N / 1000)
    print(1000 * maisu - N)


main()

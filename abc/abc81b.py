def count_min_div(v, min_div):
    ct = 0
    while v % 2 == 0:
        if ct >= min_div:
            break
        v /= 2
        ct += 1
    return ct


def main():
    N = int(input())
    A = list(map(int, input().split()))

    min_div = 1000000000
    for a in A:
        min_div = count_min_div(a, min_div)
        # print(a, min_div)

    print(min_div)


main()

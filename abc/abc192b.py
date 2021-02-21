import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    yominikui = True
    for i, c in enumerate(input()):
        if (i + 1) % 2 == 0:  # 大文字
            # cが小文字なら読みやすい
            if c == c.lower():
                yominikui = False
                break
        else:  # 小文字
            # cが大文字なら読みやすい
            if c != c.lower():
                yominikui = False
                break

    if yominikui:
        print('Yes')
    else:
        print('No')


main()

def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    H, W = read_ints()
    if H > W:
        H, W = W, H

    if H == 1 and W == 1:
        ans = 1
    elif H == 1:
        ans = max(0, W - 2)
    elif H == 2:
        ans = 0
    else:  # H,W >=3
        ans = (H - 2) * (W - 2)
    print(ans)


main()

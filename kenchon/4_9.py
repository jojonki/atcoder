N = 4
A = [3, 2, 6, 5]
W = 14


def func(i, w):
    if w == 0:
        return True
    if i <= 0:
        return False

    # not use last one
    if func(i - 1, w):
        return True
    if func(i - 1, w - A[i]):
        return True


print(func(N - 1, W))

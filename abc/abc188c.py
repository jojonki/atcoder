def main():
    N = int(input())
    A = list(map(int, input().split()))
    N = len(A)
    left = A[:N // 2]
    right = A[N // 2:]
    # print('left', left)
    # print('r', right)
    left_max_i, left_max_v = 0, 0
    for i, v in enumerate(left):
        if v > left_max_v:
            left_max_v = v
            left_max_i = i

    right_max_i, right_max_v = 0, 0
    for i, v in enumerate(right):
        if v > right_max_v:
            right_max_v = v
            right_max_i = i + N // 2

    # print(left_max_v, right_max_v)
    if left_max_v < right_max_v:
        print(left_max_i + 1)
    else:
        print(right_max_i + 1)


main()

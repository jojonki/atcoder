def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    H, W = read_ints()
    M = []
    M.append(['.'] * (W + 2))
    for h in range(H):
        row = ['.'] + list(input()) + ['.']
        M.append(row)
    M.append(['.'] * (W + 2))
    # for m in M:
    #     print(''.join(m))
    for h in range(H):
        for w in range(W):
            if M[h + 1][w + 1] == '.':
                continue
            left = M[h + 1][w + 1 - 1]
            right = M[h + 1][w + 1 + 1]
            up = M[h + 1 - 1][w + 1]
            down = M[h + 1 + 1][w + 1]
            if left == right == up == down == '.':
                # print(h + 1, w + 1)
                print('No')
                return
    print('Yes')


main()

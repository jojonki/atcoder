def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    N = int(input())
    t_prev, x_prev, y_prev = 0, 0, 0
    for _ in range(N):
        t_cur, x_cur, y_cur = read_ints()
        T = t_cur - t_prev
        dist = abs(x_cur - x_prev) + abs(y_cur - y_prev)
        if dist <= T:
            if (T - dist) % 2 == 0:
                t_prev, x_prev, y_prev = t_cur, x_cur, y_cur
                continue
            else:
                print('No')
                return

        else:
            print('No')
            return
    print('Yes')


main()

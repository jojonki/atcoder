def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    N, X = read_ints()
    ct = 0
    min_kona = float('inf')
    for _ in range(N):
        m = int(input())
        X -= m
        ct += 1
        if m < min_kona:
            min_kona = m

    ct += (X // min_kona)
    print(ct)


main()

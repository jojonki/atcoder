def rec(cur, use_flag, ct, N):
    if cur > N:
        return ct

    if use_flag == 0x111:
        ct += 1

    ct = rec(10 * cur + 7, use_flag | 0x100, ct, N)
    ct = rec(10 * cur + 5, use_flag | 0x010, ct, N)
    ct = rec(10 * cur + 3, use_flag | 0x001, ct, N)
    return ct


def main():
    N = int(input())
    print(rec(0, 0, 0, N))


main()

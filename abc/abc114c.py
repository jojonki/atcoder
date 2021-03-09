def rec(cur, use_flag, ct, N):
    if cur > N:
        return ct

    if use_flag == 0x111:
        ct += 1

    ct = rec(10 * cur + 7, use_flag | 0x100, ct, N)
    ct = rec(10 * cur + 5, use_flag | 0x010, ct, N)
    ct = rec(10 * cur + 3, use_flag | 0x001, ct, N)
    return ct


# def main():
# N = int(input())
# print(rec(0, 0, 0, N))

ans = 0


def main():
    N = int(input())

    def dfs(v, flag):
        global ans
        # global ans
        if v > N:
            return

        if flag == 0x111:
            ans += 1

        dfs(10 * v + 7, flag | 0x100)
        dfs(10 * v + 5, flag | 0x010)
        dfs(10 * v + 3, flag | 0x001)

    dfs(0, 0x000)
    print(ans)


main()

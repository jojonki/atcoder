import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    N = int(input())
    s, t = input(), input()
    if s == t:
        print(N)
        return

    for i in range(N):
        sub_s = s[i:]
        if sub_s == t[:len(sub_s)]:
            print(len(s[:i] + sub_s + t[len(sub_s):]))
            return
    print(2 * N)


main()

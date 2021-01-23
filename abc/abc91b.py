def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


from collections import defaultdict as dd


def main():
    mem = dd(int)
    N = int(input())
    for _ in range(N):
        mem[input()] += 1
    M = int(input())
    for _ in range(M):
        mem[input()] -= 1
    print(max(max(mem.values()), 0))


main()

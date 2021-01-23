def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    N = int(input())
    D = set()
    for _ in range(N):
        d = int(input())
        D.add(d)
    print(len(D))


main()

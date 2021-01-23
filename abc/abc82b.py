def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    s = list(input())
    t = list(input())
    s.sort()
    t.sort(reverse=True)
    s = ''.join(s)
    t = ''.join(t)
    if s < t:
        print('Yes')
    else:
        print('No')


main()

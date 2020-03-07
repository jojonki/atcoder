def main():
    N, A, B = map(int, input().split())
    ret = 0
    AB = A + B
    times = N // AB
    ret += (times * A)

    left = min(N - AB*times, A)
    ret += left
    print(ret)

main()
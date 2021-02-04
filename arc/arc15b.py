def main():
    N = int(input())
    mousho, manatsu, natsu, nettai, huyu, mahuyu = 0, 0, 0, 0, 0, 0
    for _ in range(N):
        max_t, min_t = map(float, input().split())
        if max_t >= 35.0:
            mousho += 1
        elif max_t >= 30.0:
            manatsu += 1
        elif max_t >= 25.0:
            natsu += 1

        if min_t >= 25.0:
            nettai += 1

        if min_t < 0 and max_t >= 0:
            huyu += 1

        if max_t < 0:
            mahuyu += 1

    print(mousho, manatsu, natsu, nettai, huyu, mahuyu)


main()

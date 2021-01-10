def main():
    N = int(input())
    ac, wa, tle, re = 0, 0, 0, 0
    for _ in range(N):
        r = input()
        if r == 'AC':
            ac += 1
        elif r == 'WA':
            wa += 1
        elif r == 'TLE':
            tle += 1
        elif r == 'RE':
            re += 1
    print('AC x', ac)
    print('WA x', wa)
    print('TLE x', tle)
    print('RE x', re)


main()

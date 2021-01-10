def main():
    S = input()
    res = 0
    rain_streak = 0
    for c in S:
        if c == 'R':
            rain_streak += 1
        else:
            rain_streak = 0
        res = max(rain_streak, res)

    print(res)


main()

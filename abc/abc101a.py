def main():
    ans = 0
    for c in input():
        if c == '-':
            ans -= 1
        else:
            ans += 1
    print(ans)


main()

def main():
    a, b = input().split()
    sa = 0
    for c in a:
        sa += int(c)
    sb = 0
    for c in b:
        sb += int(c)
    print(max(sa, sb))


main()

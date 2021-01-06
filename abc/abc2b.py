def main():
    s = input()
    res = ''
    for c in s:
        if c not in ['a', 'i', 'u', 'e', 'o']:
            res += c
    print(res)


main()

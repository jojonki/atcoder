def main():
    N = int(input())
    S = input()
    res = ''
    for c in S:
        v = ord(c) + N
        if v > 90:
            v = v % 90 + 64
        res += chr(v)
    print(res)
    

main()
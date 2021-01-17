def main():
    N = int(input())
    counter = []
    a_ord = 97
    while N != 0:
        N -= 1
        counter.append(N % 26)
        N = N // 26
    # print(counter[::-1])

    ans = ''
    for i in range(len(counter)):
        d = counter[len(counter) - 1 - i]
        # if i != len(counter):
        #     d -= 1
        ans += chr(a_ord + d)
    print(ans)


main()

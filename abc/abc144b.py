def main():
    N = int(input())

    for i in range(1, 11):
        print(i)
        for j in range(i, 11):
            if i*j == N:
                print('Yes')
                # return

    print('No')
main()
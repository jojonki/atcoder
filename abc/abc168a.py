def main():
    N = int(input())
    amari = N % 10
    if amari in [2, 4, 5, 7, 9]:
        print('hon')
    elif amari in [0, 1, 6, 8]:
        print('pon')
    else:
        print('bon')


main()

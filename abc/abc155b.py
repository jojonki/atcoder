def main():
    N = int(input())
    A = list(map(int, input().split()))
    approve = True
    for a in A:
        if a % 2 == 0:
            if a % 3 == 0 or a % 5 == 0:
                pass # ok
            else:
                approve = False
                break
    if approve:
        print('APPROVED')
    else:
        print('DENIED')

    

main()
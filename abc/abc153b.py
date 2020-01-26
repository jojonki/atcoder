def main():
    H, N = map(int, input().split())
    A = list(map(int, input().split()))
    sA = sum(A)
    if H <= sA:
        print('Yes')
    else:
        print('No')
    

main()
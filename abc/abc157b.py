def main():
    A = []
    for _ in range(3):
        a1,a2,a3 = map(int, input().split()) 
        AA = [[a1,0],[a2,0],[a3,0]]
        A.append(AA)
    N = int(input())
    # print(A)

    for _ in range(N):
        b = int(input())
        for i in range(3):
            for j in range(3):
                if A[i][j][0] == b:
                    A[i][j][1] = 1
        
        # row
        for i in range(3):
            if 3 == sum([v[1] for v in A[i]]):
                print('Yes')
                return
        # column
        for j in range(3):
            if 3 == sum([a[j][1] for a in A]):
                print('Yes')
                return
        # cross
        if 3 == (A[0][0][1]+A[1][1][1]+A[2][2][1]):
            print('Yes')
            return
        if 3 == (A[0][2][1]+A[1][1][1]+A[2][0][1]):
            print('Yes')
            return

    print('No')
        

main()
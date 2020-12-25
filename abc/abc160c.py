def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))

    # A.append((K-A[-1]+A[0]))
    # print(A)
    diff = []
    for i in range(N-1):
        diff.append(A[i+1]-A[i])
    diff.append(K-A[-1]+A[0])
    # print(diff)
    
    print(sum(diff)-max(diff))
    

main()
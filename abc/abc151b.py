import math
def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    X = math.ceil(M*N - sum(A))
    if X <= K:
        print(max(0, X))
    else:
        print(-1)
    

main()
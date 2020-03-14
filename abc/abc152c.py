def main():
    N = int(input())
    P = list(map(int, input().split()))
    crnt_min = float('inf')
    res = 0
    for i, p in enumerate(P):
        if crnt_min >= p:
            res += 1
        if p < crnt_min:
            crnt_min = p
    
    print(res)
    

main()
import math

def main():
    N = int(input())
    rN = math.ceil(math.sqrt(N))
    minDist = float('inf')
    for a in range(1, rN+1):
        if N % a == 0:
            minDist = min(minDist, a+N/a-2)
    print(int(minDist))


main()
import itertools
from math import sqrt
def main():
    def helper():
        pass
    def dist(p1, p2):
        dX, dY = p1[0]-p2[0], p1[1]-p2[1]
        return sqrt(dX*dX+dY*dY)

    N = int(input())
    P = []
    for _ in range(N):
        x, y = map(int, input().split())
        P.append((x, y))
    
    D = []
    ct = 0
    for p_list in itertools.permutations(P, N):
        ct += 1
        d = 0
        for i in range(len(p_list)-1):
            d += dist(p_list[i], p_list[i+1])
        D.append(d)
    print(sum(D)/ct)

main()
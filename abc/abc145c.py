import itertools
import math


def dist(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    return math.sqrt(dx * dx + dy * dy)


def main():
    N = int(input())
    P = []
    for _ in range(N):
        x, y = map(int, input().split())
        P.append((x, y))

    dist_list = []
    for p_list in itertools.permutations(P, N):
        total = 0
        for i in range(len(p_list) - 1):
            total += dist(*p_list[i], *p_list[i + 1])
        dist_list.append(total)
    print(sum(dist_list) / len(dist_list))


main()

# @@ -1,26 +1,4 @@
# -import itertools
# -from math import sqrt
#  def main():
# -    def helper():
# -        pass
# -    def dist(p1, p2):
# -        dX, dY = p1[0]-p2[0], p1[1]-p2[1]
# -        return sqrt(dX*dX+dY*dY)
# -
# -    N = int(input())
# -    P = []
# -    for _ in range(N):
# -        x, y = map(int, input().split())
# -        P.append((x, y))

# -    D = []
# -    ct = 0
# -    for p_list in itertools.permutations(P, N):
# -        ct += 1
# -        d = 0
# -        for i in range(len(p_list)-1):
# -            d += dist(p_list[i], p_list[i+1])
# -        D.append(d)
# -    print(sum(D)/ct)

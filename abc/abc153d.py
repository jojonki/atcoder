from math import floor, log2
from collections import deque

def main():
    H = int(input())
    n = floor(log2(H))
    ct = 0
    for i in range(n+1):
        ct += pow(2, i)
    print(ct)
    # M = deque([H])
    # ct = 0
    # while M:
    #     v = M.popleft()
    #     if v > 1:
    #         new_v = floor(v/2)
    #         M.append(new_v)
    #         M.append(new_v)
    #     ct += 1
    # print(ct)

        
    

main()
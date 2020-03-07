from math import floor
def main():
    A, B = map(int, input().split())
    minX = -1
    fB = (B*10 // 10) * 10
    bXCands = [fB+i for i  in range(10)]
    for aXcand in bXCands:
        if int(aXcand * 0.08) == A:
            minX = aXcand
            break
    print(minX)



    # minX = -1
    # aX = int(A * 100 / 8)
    # if int(aX * 0.1) == B:
    #     minX = aX

    # bX = int(B * 100 / 10)
    # if int(bX * 0.08) == A:
    #     if minX == -1:
    #         minX = bX
    #     else:
    #         minX = min(aX, bX)
    # print(minX)
    

main()
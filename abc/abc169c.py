import math
from decimal import Decimal


def main():
    a, b = input().split()
    a = int(a)
    b = int(float(b) * 100)
    # b = int(Decimal(b) * 100)
    # print(math.floor(a * b))
    print((a * b) // 100)


main()

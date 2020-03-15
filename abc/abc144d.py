import math
def main():
    a, b, x = map(float, input().split())
    thX = a * a * b / 2.0
    if x == (a*a*b):
        print(0)
    elif x <= thX:
        h = 2.0 * x / (a * b)
        deg = math.degrees(math.atan(h / b))
        print(90.0 - deg)
    else:
        c = 2.0 * x / (a*a) - b
        deg = math.degrees(math.atan(a / (b-c)))
        print(90.0 - deg)

main()
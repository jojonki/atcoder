# def pow(a, n):
#     if n == 0: return 1
#     if n == 1: return a
#     if n % 2 == 0:
#         t = pow(a, n // 2)
#         return t * t
#     else:
#         return a * pow(a, n - 1)

BIG = 1000000000


def main():
    X = int(input())
    # for i in range(BIG):
    #     if pow(-i, 5) - pow(-i - 1, 5) >= BIG:
    #         print(i)
    #         break
    # -118<=A<=119

    for a in range(-118, 119 + 1):
        for b in range(-119, 118 + 1):
            # print(a, b)
            if X == pow(a, 5) - pow(b, 5):
                print(a, b)
                return


main()

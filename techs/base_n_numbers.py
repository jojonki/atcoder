# n進法


def base_n(decimal, n):
    # decimalをn進法で表したときの値
    # decimal: int, n:int
    S = 0
    for d in str(decimal):
        S = S * n + int(d)
    return S


if __name__ == '__main__':
    print(base_n(192, 10))  # 192
    print(base_n(22, 3))  # 8
    print(base_n(22, 4))  # 10

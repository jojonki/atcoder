import math


def is_prime(N):
    """素因数分解を使って素数かチェック
    Return:
        [{prime1, exp_count2}, {prime2, exp_count2}]
    
    ex)
        60 = 2**2 * 3 * 5
        -> [(2, 2), (3, 1), (5, 1)]
    """
    res = []
    for i in range(2, int(math.sqrt(N)) + 1):
        if N % i != 0:
            continue
        return False

    return True


def main():
    MAX_V = int(1e10)
    X = int(input())
    for v in range(X, MAX_V + 1):
        if is_prime(v):
            print(v)
            break


main()

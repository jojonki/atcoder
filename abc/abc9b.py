def main():
    N = int(input())
    m1, m2 = -float('inf'), -float('inf')
    for _ in range(N):
        p = int(input())
        if p > m1:
            m2 = m1
            m1 = p
        elif m1 > p > m2:
            m2 = p
    print(m2)


main()

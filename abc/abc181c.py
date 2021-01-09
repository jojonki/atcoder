def calc(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    if x1 == x2:
        a = float('inf')
    else:
        a = (y2 - y1) / (x2 - x1)
    return a


def main():
    N = int(input())
    D = []
    for _ in range(N):
        x, y = map(int, input().split())
        D.append((x, y))
    for i in range(N - 1):
        for j in range(i + 1, N):
            a = calc(D[i], D[j])
            for k in range(N):
                if k == i or k == j:
                    continue
                a_k = calc(D[j], D[k])
                if a == a_k:
                    print('Yes')
                    return
    print('No')


main()

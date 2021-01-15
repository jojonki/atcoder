from collections import defaultdict


def main():
    N = int(input())
    A = list(map(int, input().split()))
    buka = defaultdict(int)
    for a in A:
        buka[a - 1] += 1
    for i in range(N):
        print(buka[i])


main()

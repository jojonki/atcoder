from collections import defaultdict
def main():
    def pair(n):
        a = n % 10
        b = str(n)[0]
        return '{},{}'.format(a, b)

    N = int(input())
    freq = defaultdict(int)
    for i in range(1, N+1):
        p = pair(i)
        freq[p] += 1
    
    res = 0
    for i in range(1, N+1):
        p = pair(i)
        q = ','.join(p.split(',')[::-1])
        res += freq[q]
    print(res)

main()
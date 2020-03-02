def main():
    N, M = map(int, input().split())
    d = {}
    for _ in range(M):
        s, c = map(int, input().split())
        if s == 1 and c==0 and N > 1:
            print('-1')
            return
        if s in d and d[s] != c:
            print('-1')
            return
        if s > N:
            print('-1')
            return
        d[s] = c

    s = ''
    if N == 1:
        if 1 in d:
            s += str(d[1])
        else:
            s += '0'
    else:
        for n in range(1, N+1):
            if n in d:
                s += str(d[n])
            else:
                if n==1:
                    s += '1'
                else:
                    s += '0'
    print(s) 

main()
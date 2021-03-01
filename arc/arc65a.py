import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


from collections import deque


def mainQ():
    S = input()
    q = deque([S])
    cands = ['dream', 'dreamer', 'erase', 'eraser']
    res = False
    while q:
        s = q.popleft()
        for cand in cands:
            if s[:len(cand)] == cand:
                if s == cand:
                    print('YES')
                    return
                q.append(s[len(cand):])
    print('NO')


def main():
    S = input()
    S = S[::-1]
    cands = ['dream', 'dreamer', 'erase', 'eraser']
    cands = [c[::-1] for c in cands]
    # print(cands)
    cur = 0
    while cur < len(S):
        for cand in cands:
            if S[cur:cur + len(cand)] == cand:
                cur += len(cand)
                break
        else:
            print('NO')
            return
    print('YES')


main()

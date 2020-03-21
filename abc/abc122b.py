ACGT = ['A', 'C', 'G', 'T']
def ok(S):
    for c in S:
        if c not in ACGT:
            return False
    return True
def main():
    S = input()
    res = ''
    for i in range(len(S)):
        for j in range(1, len(S)+1):
            ps = S[i:j]
            if ok(ps) and len(ps) > len(res):
                res = ps

    print(len(res))
    

main()
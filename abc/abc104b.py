def cond1(S):
    return S[0] == 'A'


def cond2(S):
    return sum([1 for s in S[2:-1] if s == 'C']) == 1


def cond3(S):
    for s in S:
        if s in ['A', 'C']:
            continue
        if s.lower() == s:
            continue
        else:
            break
    else:
        return True
    return False


def main():
    S = input()
    if cond1(S) and cond2(S) and cond3(S):
        print('AC')
    else:
        print('WA')


main()

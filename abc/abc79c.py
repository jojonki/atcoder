def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    S = list(input())
    A, B, C, D = [int(c) for c in S]
    for op1 in ['+', '-']:
        for op2 in ['+', '-']:
            for op3 in ['+', '-']:
                ans = A
                if op1 == '+':
                    ans += B
                else:
                    ans -= B
                if op2 == '+':
                    ans += C
                else:
                    ans -= C
                if op3 == '+':
                    ans += D
                else:
                    ans -= D
                if ans == 7:
                    print(f'{A}{op1}{B}{op2}{C}{op3}{D}=7')
                    return


main()

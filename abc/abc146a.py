def main():
    W = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    S = input()
    if S == 'SUN':
        print(7)
    else:
        print(7 - W.index(S) - 1)
    

main()
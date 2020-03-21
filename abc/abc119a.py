def main():
    S = input()
    y, m, d = map(int, S.split('/', 2))
    
    if y < 2019:
        print('Heisei')
    elif y > 2019:
        print('TBD')
    else: # 2019
        if m < 4:
            print('Heisei')
        elif m > 4:
            print('TBD')
        else: # 2019/04
            if d <= 30:
                print('Heisei')
            else:
                print('TBD')

main()
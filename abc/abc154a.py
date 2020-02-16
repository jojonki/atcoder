def main():
    # S = list(map(int, input().split()))
    S, T = input().split()
    a, b = map(int, input().split())
    U = input()
    if U == S:
        a -= 1
    else:
        b -= 1
    print(a, b)
    

main()
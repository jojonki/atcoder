def main():
    H, W = map(int, input().split())
    h, w = map(int, input().split())

    n_white = H*W - (h*W + w*H - h*w)
    print(n_white)
    

main()
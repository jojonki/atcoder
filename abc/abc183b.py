def main():
    sx, sy, gx, gy = map(int, input().split())
    gy = -gy
    a = (gy - sy) / (gx - sx)
    print(sx - sy / a)


main()

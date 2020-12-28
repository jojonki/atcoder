def main():
    N = int(input())
    tasks = []
    for _ in range(N):
        a, b = map(int, input().split())
        tasks.append((a, b))
    tasks.sort(key=lambda x: x[1])
    # print(tasks)
    time = 0
    res = 'No'
    for a, b in tasks:
        time += a
        if time <= b:
            continue
        else:
            break
    else:
        res = 'Yes'

    print(res)


main()

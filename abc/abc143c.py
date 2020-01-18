N = int(input())
S = input()
ct = 1
last_c = S[0]
for c in S[1:]:
    if last_c == c:
        continue
    else:
        last_c = c
        ct += 1
print(ct)
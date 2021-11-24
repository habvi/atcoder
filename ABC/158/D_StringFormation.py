s = input()
q = int(input())
cnt = 0
l, r = "", ""
for _ in range(q):
    a = input().split()
    if a[0] == '1':
        cnt = 1 - cnt
        continue
    c = a[2]
    if a[1] == '1':
        if cnt == 0: l += c
        else: r += c
    else:
        if cnt == 0: r += c
        else: l += c

if cnt == 0:
    print(l[::-1] + s + r)
else:
    print(r[::-1] + s[::-1] + l)
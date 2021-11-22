# bruto force a to z

s = input()
n = len(s)
ans = 110
for i in range(ord('a'), ord('z') + 1):
    al = chr(i)
    t = s
    u = ''
    cnt = 0
    while len(set(t)) != 1:
        for j in range(len(t) - 1):
            if t[j] == al or t[j+1] == al:
                u += al
            else:
                u += t[j]
        cnt += 1
        t = u
        u = ''
    ans = min(ans, cnt)
print(ans)
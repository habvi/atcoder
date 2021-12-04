s = input().split('+')
ans = 0
for t in s:
    if len(t) == 1:
        if t != '0':
            ans += 1
    else:
        if '0' not in t.split('*'):
            ans += 1
print(ans)
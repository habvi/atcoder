s = input().split('+')
ans = 0
for t in s:
    if '0' not in t.split('*'):
        ans += 1
print(ans)
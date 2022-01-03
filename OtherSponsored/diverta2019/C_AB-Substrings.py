n = int(input())
S = []
ans = 0
a, b, ab = 0, 0, 0
for _ in range(n):
    s = input()
    ans += s.count('AB')
    S.append(s)
    if s[0] == 'B' and s[-1] == 'A':
        ab += 1
    elif s[0] == 'B':
        b += 1
    elif s[-1] == 'A':
        a += 1

ans += max(0, ab - 1)
if ab:
    if a:
        ans += 1
        a -= 1
    if b:
        ans += 1
        b -= 1    
ans += min(a, b)    
print(ans)
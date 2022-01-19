s = input()
s = s.replace('BC', 'X')

S = []
for t in s.split('C'):
    if not t:
        continue
    for u in t.split('B'):
        if not u:
            continue
        u = u.lstrip('X').rstrip('A')
        if u:
            S.append(u)

ans = 0
for s in S:
    cnt = 0
    for t in s:
        if t == 'A':
            cnt += 1
        else:
            ans += cnt
print(ans)
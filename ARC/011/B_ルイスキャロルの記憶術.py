n = int(input())
w = list(input().split())
d = {}
for i, (s, t) in enumerate(['zr', 'bc', 'dw', 'tj', 'fq', 'lv', 'sx', 'pm', 'hk', 'ng']):
    d[s] = str(i)
    d[t] = str(i)

ans = []
for s in w:
    a = []
    for t in s:
        t = t.lower()
        if t in d:
            a.append(d[t])
    if a:
        ans.append("".join(a))
print(*ans)
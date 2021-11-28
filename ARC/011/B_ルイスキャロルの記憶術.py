n = int(input())
w = list(input().split())
d = {}
for i, (x, y) in enumerate(['bc', 'dw', 'tj', 'fq', 'lv', 'sx', 'pm', 'hk', 'ng', 'zr'], 1):
    d[x] = str(i % 10)
    d[y] = str(i % 10)
print(d)

ans = []
for ww in w:
    a = ''
    for s in ww:
        s = s.lower()
        if s not in d: continue
        a += d[s]
    if a:
        ans.append(a)
print(*ans)
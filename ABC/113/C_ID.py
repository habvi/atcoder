from collections import defaultdict

n, m = map(int, input().split())
py = defaultdict(list)
for i in range(m):
    p, y = map(int, input().split())
    py[p].append((y, i))

ans = [''] * m
for p, v in py.items():
    v.sort()
    for x, (_, i) in enumerate(v, 1):
        ans[i] = "{:06d}".format(p) + "{:06d}".format(x)

print(*ans)
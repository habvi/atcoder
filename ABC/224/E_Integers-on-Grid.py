from collections import defaultdict

h, w, n = map(int, input().split())
g = defaultdict(list)
idx = defaultdict(int)
for i in range(n):
    r, c, a = map(int, input().split())
    r, c = r - 1, c - 1
    g[a].append((r, c))
    idx[(r, c)] = i

max_r = [0] * h
max_c = [0] * w
ans = [None] * n
for k in sorted(g.keys(), reverse=True):
    for r, c in g[k]:
        now = max(max_r[r], max_c[c])
        i = idx[(r, c)]
        ans[i] = now

    for r, c in g[k]:
        i = idx[(r, c)]
        now = ans[i]
        max_r[r] = max(max_r[r], now + 1)
        max_c[c] = max(max_c[c], now + 1)

for a in ans:
    print(a)
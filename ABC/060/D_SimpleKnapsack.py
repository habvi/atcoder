from collections import defaultdict
from itertools import accumulate

n, W = map(int, input().split())
g = defaultdict(list)
for i in range(n):
    w, v = map(int, input().split())
    g[w].append(v)
    if i == 0:
        w0 = w

for k, v in g.items():
    g[k] = [0, *accumulate(sorted(v, reverse=True))]

w1 = w0 + 1
w2 = w1 + 1
w3 = w2 + 1
for i in range(w1, w3 + 1):
    if i not in g:
        g[i].append(0)

ans = 0
for i in range(len(g[w0])):
    for j in range(len(g[w1])):
        for k in range(len(g[w2])):
            for l in range(len(g[w3])):
                if w0*i + w1*j + w2*k + w3*l > W:
                    continue
                ans = max(ans, g[w0][i] + g[w1][j] + g[w2][k] + g[w3][l])
print(ans)
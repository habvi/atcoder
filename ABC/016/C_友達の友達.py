from collections import defaultdict
n, m = map(int, input().split())
g = defaultdict(list)
for _ in range(m):
    a, b = map(lambda x: int(x) - 1, input().split())
    g[a].append(b)
    g[b].append(a)

for i in range(n):
    F = set(g[i])
    FF = set()
    for f in F:
        for ff in g[f]:
            if ff == i or ff in F:
                continue
            FF.add(ff)
    print(len(FF))
from collections import defaultdict

def dfs(v, p):
    global count_
    count_ += 1
    pre[v] += count_
    low[v] = pre[v]

    for nv in g[v]:
        if pre[nv] == -1:
            low[v] = min(low[v], dfs(nv, v))
            if low[nv] == pre[nv]:
                ans.append((v, nv))
        else:
            if nv == p:
                continue
            low[v] = min(low[v], low[nv])

    return low[v]


n, m = map(int, input().split())

g = defaultdict(list)
for _ in range(m):
    a, b = map(lambda x: int(x) - 1, input().split())
    g[a].append(b)
    g[b].append(a)

pre = [-1] * n
low = [-1] * n
count_ = 0
ans = []

dfs(0, -1)

print(len(ans))
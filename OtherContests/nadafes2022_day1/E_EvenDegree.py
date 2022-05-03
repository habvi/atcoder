from collections import defaultdict, deque

def bfs(u):
    que = deque([])
    que.append(u)
    seen[u] = 1
    while que:
        v = que.popleft()
        a = A[v]
        if a > 0:
            plus.append(a)
        else:
            minus.append(a)

        for nv in g[v]:
            if seen[nv]:
                continue
            seen[nv] = 1
            que.append(nv)


n, m = map(int, input().split())
A = list(map(int, input().split()))

g = defaultdict(list)
for i in range(m):
    a, b = map(lambda x: int(x) - 1, input().split())
    g[a].append(b)
    g[b].append(a)

seen = [0] * n
ans = 0
for v in range(n):
    if seen[v]:
        continue

    plus, minus = [], []
    bfs(v)

    total_p = sum(plus)
    if not len(minus) % 2:
        ans += total_p
    else:
        if plus:
            ans += max(total_p + max(minus), total_p - min(plus))
        else:
            ans += max(minus)
print(ans)
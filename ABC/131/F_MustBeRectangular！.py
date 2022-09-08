from collections import defaultdict, deque

def bfs(u):
    seen[u] = 1
    que = deque([])
    que.append(u)
    x, y, edge = 0, 0, 0
    while que:
        v = que.popleft()
        if v < mx:
            x += 1
        else:
            y += 1
        edge += len(xy[v])
        for nv in xy[v]:
            if seen[nv]:
                continue
            seen[nv] = 1
            que.append(nv)
    return x, y, edge


N = int(input())
xy = defaultdict(list)
mx = 10 ** 5
for _ in range(N):
    a, b = map(lambda x: int(x) - 1, input().split())
    xy[a].append(b + mx)
    xy[b + mx].append(a)

seen = [0] * (mx * 2)
ans = 0
for v in range(mx * 2):
    if seen[v]:
        continue
    x, y, edge = bfs(v)
    ans += (x * y - edge // 2)
print(ans)

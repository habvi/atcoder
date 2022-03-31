from collections import defaultdict, deque

def is_bipartite(v, c=0):
    color[v] = c
    return bp_bfs(v, color, c)

def bp_bfs(u, color, c):
    q = deque([])
    q.append((u, c))
    while q:
        v, c = q.popleft()
        for nv in g[v]:
            if color[nv] != -1:
                if color[nv] == c:
                    return False
                continue
            color[nv] = 1 - c
            q.append((nv, 1 - c))
    return True


n, m = map(int, input().split())
g = defaultdict(list)
for _ in range(m):
    a, b = map(lambda x: int(x) - 1, input().split())
    g[a].append(b)
    g[b].append(a)

color = [-1] * n
if is_bipartite(0):
    R, B = color.count(0), color.count(1)
    print(R * B - m)
else:
    print(n * (n - 1) // 2 - m)
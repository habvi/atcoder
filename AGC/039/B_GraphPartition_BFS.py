from collections import defaultdict, deque

def is_bipartite(v, c=0):
    color = [-1] * n
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

n = int(input())
S = [list(map(int, list(input()))) for _ in range(n)]
g = defaultdict(list)
for i in range(n):
    for j in range(i + 1, n):
        if S[i][j]:
            g[i].append(j)
            g[j].append(i)
 
if not is_bipartite(0):
    print(-1)
    exit()
 
dst = S
for i in range(n):
    for j in range(n):
        if i == j:
            dst[i][j] = 0
            continue
        if not dst[i][j]:
            dst[i][j] = float('inf')
 
for k in range(n):
    for i in range(n):
        for j in range(n):
            dst[i][j] = min(dst[i][j], dst[i][k] + dst[k][j])
 
ans = 0
for i in range(n):
    ans = max(ans, max(dst[i]))
print(ans + 1)
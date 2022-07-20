from collections import defaultdict, deque

def bfs(u):
    global ans
    que = deque([])
    que.append(u)
    while que:
        v = que.popleft()
        for nv in g[v]:
            if seen[nv]:
                continue
            seen[v] = 1
            ans = max(ans, A[nv] - mn)
            que.append(nv)


n, m = map(int, input().split())
A = list(map(int, input().split()))

g = defaultdict(list)
for _ in range(m):
    a, b = map(lambda x: int(x) - 1, input().split())
    g[a].append(b)

ai = sorted((a, i) for i, a in enumerate(A))

seen = [0] * n
ans = -float('inf')
for mn, v in ai:
    if not seen[v]:
        bfs(v)
print(ans)
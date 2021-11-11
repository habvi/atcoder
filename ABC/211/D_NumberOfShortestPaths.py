from collections import deque
def bfs(u):
    que = deque([])
    que.append(u)
    while que:
        v = que.popleft()
        for nv in G[v]:
            if dst[nv] < dst[v] + 1: continue
            if dst[nv] != INF:
                if dst[nv] == dst[v] + 1:
                    cnt[nv] += cnt[v]
                    cnt[nv] %= MOD
                continue
            dst[nv] = dst[v] + 1
            cnt[nv] = cnt[v]%MOD
            que.append(nv)

n, m = map(int, input().split())
MOD = 10**9+7
G = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    G[a].append(b)
    G[b].append(a)

INF = 10**10
dst = [INF for _ in range(n)]
dst[0] = 0
cnt = [0]*n
cnt[0] = 1
bfs(0)
print(cnt[n-1]%MOD)
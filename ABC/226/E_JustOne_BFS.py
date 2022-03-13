from collections import deque, defaultdict

def bfs(u):
    global num_v, edge
    q = deque([u])
    seen[u] = 1
    while q:
        v = q.popleft()
        num_v += 1
        edge += len(g[v])
        for nv in g[v]:
            if seen[nv]:
                continue
            seen[nv] = 1
            q.append(nv)


n, m = map(int, input().split())
MOD = 998244353

g = defaultdict(list)
for i in range(m):
    a, b = map(lambda x: int(x) - 1, input().split())
    g[a].append(b)
    g[b].append(a)

seen = [0] * n
group = 0
for i in range(n):
    if seen[i]:
        continue

    num_v = 0
    edge = 0
    bfs(i)

    if edge / 2 != num_v:
        print(0)
        exit()
    group += 1

print(pow(2, group, MOD))
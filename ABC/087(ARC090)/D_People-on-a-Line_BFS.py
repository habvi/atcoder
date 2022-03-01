from collections import defaultdict, deque

n, m = map(int, input().split())
g = defaultdict(list)
check = []
for _ in range(m):
    l, r, d = map(int, input().split())
    l, r = l - 1, r - 1
    g[l].append((r, d))
    g[r].append((l, -d))
    check.append((l, r, d))


def bfs(u):
    dst[u] = 0
    q = deque([u])
    while q:
        v = q.popleft()
        for nv, nd in g[v]:
            if dst[nv] != -1:
                continue
            num[nv] = num[v] + nd
            dst[nv] = dst[v] + 1
            q.append(nv)
    return dst


dst = [-1] * n
num = [None] * n
for i in range(n):
    if dst[i] == -1:
        num[i] = 0
        bfs(i)

for l, r, d in check:
    if num[r] - num[l] != d:
        print('No')
        exit()
print('Yes')
from collections import deque, defaultdict

def bfs(u):
    seen[u] = 1
    q = deque([])
    q.append((u, -1))
    while q:
        v, pi = q.popleft()
        num = 1
        for nv, ni in g[v]:
            if seen[nv]:
                continue

            seen[nv] = 1
            if num == C[pi]:
                num += 1
            C[ni] = num
            num += 1
            q.append((nv, ni))


n = int(input())

g = defaultdict(list)
for i in range(n - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    g[a].append((b, i))
    g[b].append((a, i))

seen = [0] * n
C = [None] * (n - 1)
bfs(0)

print(len(set(C)))
print(*C)
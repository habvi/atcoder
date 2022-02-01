from collections import defaultdict, deque

def bfs(u, w):
    dst = [-1] * n
    dst[u] = 0
    q = deque([])
    q.append((u, w))
    while q:
        v, w = q.popleft()
        for nv, nw in g[v]:
            if dst[nv] != -1:
                continue
            dst[nv] = dst[v] + 1
            xor[nv] = xor[v] ^ nw
            q.append((nv, nw))


n = int(input())
MOD = 10**9 + 7

g = defaultdict(list)
for _ in range(n - 1):
    a, b, w = map(int, input().split())
    a, b = a - 1, b - 1
    g[a].append((b, w))
    g[b].append((a, w))

xor = [0] * n
bfs(0, 0)

lb = 60
ans = 0
exp = 1
for i in range(lb):
    bit = 0
    for x in xor:
        if x >> i & 1:
            bit += 1
    ans += bit * (n - bit) * exp
    ans %= MOD
    exp <<= 1
    exp %= MOD

print(ans)
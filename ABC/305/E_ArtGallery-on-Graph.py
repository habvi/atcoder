from collections import defaultdict
from heapq import heappop, heappush

N, M, K = map(int, input().split())
g = defaultdict(list)
for i in range(M):
    a, b = map(lambda x: int(x) - 1, input().split())
    g[a].append(b)
    g[b].append(a)

H = [-1] * N
hq = []
for _ in range(K):
    p, h = map(int, input().split())
    p -= 1
    heappush(hq, (-h, p))
    H[p] = h

while hq:
    h, v = heappop(hq)
    h *= -1
    if H[v] < h:
        continue
    for nv in g[v]:
        if H[nv] >= h - 1:
            continue
        H[nv] = h - 1
        heappush(hq, (-(h - 1), nv))

ans = [i for i, h in enumerate(H, 1) if h >= 0]
print(len(ans))
print(*ans)
import heapq
def dijkstra(st):
    dst = [float('inf')]*n
    dst[st] = 0
    hq = [(0, st)]
    while hq:
        c, v = heapq.heappop(hq)
        if c > dst[v]: continue
        for nc, nv in G[v]:
            if c+nc >= dst[nv]: continue
            dst[nv] = c+nc
            heapq.heappush(hq, (c+nc, nv))
    return dst

n = int(input())
G = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    a, b = a - 1, b - 1
    G[a].append((c, b))
    G[b].append((c, a))

Q, K = map(int, input().split())
dst = dijkstra(K - 1)
for _ in range(Q):
    x, y = map(int, input().split())
    x, y = x - 1, y - 1
    print(dst[x] + dst[y])
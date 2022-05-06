import heapq

def dijkstra(st):
    dist = [float('inf')] * n
    dist[st] = 0
    hq = [(0, st)]
    while hq:
        c, v = heapq.heappop(hq)
        if c > dist[v]:
            continue
        for nc, nv in G[v]:
            if c + nc >= dist[nv]:
                continue
            dist[nv] = c + nc
            heapq.heappush(hq, (c + nc, nv))
    return dist


n = int(input())
G = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    a, b = a - 1, b - 1
    G[a].append((c, b))
    G[b].append((c, a))

Q, K = map(int, input().split())

dist = dijkstra(K - 1)

for _ in range(Q):
    x, y = map(int, input().split())
    x, y = x - 1, y - 1
    print(dist[x] + dist[y])
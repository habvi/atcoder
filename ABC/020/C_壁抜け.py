h, w, T = map(int, input().split())
s = [input() for _ in range(h)]
for i in range(h):
    for j in range(w):
        if s[i][j] == 'S':
            sy, sx = i, j
        if s[i][j] == 'G':
            gy, gx = i, j

import heapq
def dijkstra(X):
    dst = [[float('inf')] * w for _ in range(h)]
    dst[sy][sx] = 0
    hq = [(0, sy, sx)]
    heapq.heapify(hq)
    while hq:
        c, y, x = heapq.heappop(hq)
        if c > T:
            continue
        if (y, x) == (gy, gx):
            return True
        for dy, dx in zip((0, 1, 0, -1), (1, 0, -1, 0)):
            ny, nx = y + dy, x + dx
            if not (0 <= ny < h and 0 <= nx < w):
                continue
            if s[ny][nx] == "#":
                nc = X
            else:
                nc = 1
            if c + nc >= dst[ny][nx]:
                continue
            dst[ny][nx] = c + nc
            heapq.heappush(hq, (c + nc, ny, nx))
    return False

def is_ok(x):
    if dijkstra(x):
        return True
    return False

def bisect(ng, ok):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

ans = bisect(T + 1, 1)
print(ans)
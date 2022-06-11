def dist_two_points(x1, y1, x2, y2) -> float:
    return ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5


n, K = map(int, input().split())
A = list(map(lambda x: int(x) - 1, input().split()))
xy = [tuple(map(int, input().split())) for _ in range(n)]

INF = float('inf')
mn = [INF] * n
for a in A:
    x, y = xy[a]
    for i, (x2, y2) in enumerate(xy):
        d = dist_two_points(x, y, x2, y2)
        mn[i] = min(mn[i], d)

print(max(mn))
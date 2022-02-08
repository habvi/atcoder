def dist_line_to_point(x1, y1, x2, y2, px, py):
    nmrt = abs((y2 - y1)*px + (x1 - x2)*py + x2*y1 - y2*x1)
    dnmnt = ((y2 - y1)**2 + (x2 - x1)**2) ** 0.5
    return nmrt / dnmnt


sx, sy = map(int, input().split())
n = int(input())
P = [tuple(map(int, input().split())) for _ in range(n)]
P.append(P[0])

ans = float('inf')
for (x1, y1), (x2, y2) in zip(P, P[1:]):
    ans = min(ans, dist_line_to_point(x1, y1, x2, y2, sx, sy))
print(ans)
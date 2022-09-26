def is_point_on_line(x1, y1, x2, y2, px, py):
    return (x2 - x1) * (py - y1) == (y2 - y1) * (px - x1)


N = int(input())
xy = [tuple(map(int, input().split())) for _ in range(N)]

ans = 0
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            x1, y1 = xy[i]
            x2, y2 = xy[j]
            x3, y3 = xy[k]
            ans += (not is_point_on_line(x1, y1, x2, y2, x3, y3))
print(ans)
N = int(input())
xy = [tuple(map(int, input().split())) for _ in range(N)]

ans = 0
for i in range(N):
    for j in range(i + 1, N):
        x1, y1 = xy[i]
        x2, y2 = xy[j]
        ans += (-1 <= (y2 - y1) / (x2 - x1) <= 1)
print(ans)
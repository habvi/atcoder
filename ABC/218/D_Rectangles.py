n = int(input())
xy = [tuple(map(int, input().split())) for _ in range(n)]
s = set(xy)

ans = 0
for i in range(n):
    for j in range(n):
        (x1, y1), (x2, y2) = xy[i], xy[j]
        if x1 < x2 and y1 < y2 and (x2, y1) in s and (x1, y2) in s:
            ans += 1
print(ans)
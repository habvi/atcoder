n = int(input())
a = [tuple(map(int, input().split())) for _ in range(n)]
ans = 0
for i, (x1, y1) in enumerate(a):
    for j, (x2, y2) in enumerate(a[i + 1:], i + 1):
        for x3, y3 in a[j + 1:]:
            dx1 = x1 - x2
            dy1 = y1 - y2
            dx2 = x1 - x3
            dy2 = y1 - y3
            if dx1 * dy2 == dy1 * dx2:
                continue
            ans += 1
print(ans)
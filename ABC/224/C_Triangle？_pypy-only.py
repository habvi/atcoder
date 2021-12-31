n = int(input())
a = [tuple(map(int, input().split())) for _ in range(n)]

ans = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            x1 = a[i][1] - a[j][1]
            y1 = a[i][0] - a[j][0]
            x2 = a[i][1] - a[k][1]
            y2 = a[i][0] - a[k][0]
            if x1 * y2 == y1 * x2: continue
            ans += 1
print(ans)
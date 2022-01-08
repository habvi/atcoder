n = int(input())
a = [tuple(map(int, input().split())) for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(i + 1, n):
        ans = max(ans, ((a[i][0] - a[j][0])**2 + (a[i][1] - a[j][1])**2) ** 0.5)
print(ans)
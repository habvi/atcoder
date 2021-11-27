n, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
a.sort(reverse=True)
g = 0
ans = 0
for i in range(n):
    if g > w:
        break
    if g + a[i][1] > w: 
        for j in range(a[i][1]):
            if g + 1 <= w:
                ans += a[i][0]
                g += 1
            else:
                break
    else:
        ans += a[i][0] * a[i][1]
        g += a[i][1]
print(ans)
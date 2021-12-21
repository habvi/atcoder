n, D, H = map(int, input().split())
ans = 0
for _ in range(n):
    d, h = map(int, input().split())
    k = (H - h)/(D - d)
    ans = max(ans, k * -d + h)
print(ans)
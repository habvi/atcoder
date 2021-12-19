n = int(input())
ans = [0] * 6
for _ in range(n):
    mx, mn = map(float, input().split())
    mn = int(mn * 10)
    mx = int(mx * 10)
    if mx >= 350:
        ans[0] += 1
    if 300 <= mx < 350:
        ans[1] += 1
    if 250 <= mx < 300:
        ans[2] += 1
    if mn >= 250:
        ans[3] += 1
    if mn < 0 and mx >= 0:
        ans[4] += 1
    if mx < 0:
        ans[5] += 1
print(*ans)


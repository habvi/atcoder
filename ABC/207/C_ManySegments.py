n = int(input())
a = []
for _ in range(n):
    t, l, r = map(int, input().split())
    if t in (2, 4):
        r -= 0.5
    if t in (3, 4):
        l += 0.5
    a.append((l, r))
a.sort()

ans = 0
for i in range(n):
    for j in range(i + 1, n):
        if a[j][0] <= a[i][1]:
            ans += 1
print(ans)
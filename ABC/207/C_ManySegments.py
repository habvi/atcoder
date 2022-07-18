n = int(input())

A = []
for _ in range(n):
    t, l, r = map(int, input().split())
    if t in (2, 4):
        r -= 0.5
    if t >= 3:
        l += 0.5
    A.append((l, r))

A.sort()
ans = 0
for i in range(n):
    for j in range(i + 1, n):
        ans += (A[i][1] >= A[j][0])
print(ans)
n, c, k = map(int, input().split())
a = []
for _ in range(n):
    t = int(input())
    a.append((t, t + k))
a.sort(key=lambda x: x[1])

cnt = c
lo = a[0][1]
ans = 1
for l, r in a:
    if not cnt:
        cnt = c
        ans += 1
        lo = r
    if l <= lo:
        cnt -= 1
        continue
    lo = r
    cnt = c - 1
    ans += 1
print(ans)
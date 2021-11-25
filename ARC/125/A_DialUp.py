n, m = map(int, input().split())
s = list(map(int, input().split()))
t = list(map(int, input().split()))
dst = [10 ** 6, 10 ** 6]
for i in range(n):
    if s[i]:
        dst[1] = min(dst[1], i)
        dst[1] = min(dst[1], n - i)
    else:
        dst[0] = min(dst[0], i)
        dst[0] = min(dst[0], n - i)

cnt = [t.count(0), t.count(1)]
if cnt[0]:
    if dst[0] == 10 ** 6:
        print(-1)
        exit()
if cnt[1]:
    if dst[1] == 10 ** 6:
        print(-1)
        exit()

ans, l = 0, 0
if s[0] == t[0]:
    for l in range(m):
        if t[l] == s[0]:
            ans += 1
        else:
            break

if l == m - 1:
    print(ans)
    exit()

ans += dst[t[l]] + 1
for i in range(l, m - 1):
    if t[i] == t[i + 1]:
        ans += 1
    else:
        ans += 2
print(ans)
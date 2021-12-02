from itertools import groupby
n, K = map(int, input().split())
s = input()
a = []
for k, g in groupby(s):
    a.append((k, len(list(g))))

m = len(a)
cnt = 0
for i in range(m):
    if i % 2 == 0:
        cnt += a[i][1]
        if K == 0:
            break
    else:
        if K:
            cnt += a[i][1]
            K -= 1
        else:
            break
ans = cnt - 1

i += 1
if i < m:
    for j in range(i, m):
        ans += a[j][1] - 1
print(ans)
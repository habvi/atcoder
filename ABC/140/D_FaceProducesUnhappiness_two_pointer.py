from itertools import groupby

n, K = map(int, input().split())
s = input()

a = []
for k, g in groupby(s):
    a.append((k, len(list(g))))

T = 'L' if a[0][0] == 'R' else 'R'
r = 0
odd = 0
ans = 0
m = len(a)
cnt = 0
for l in range(m):
    while r < m and odd <= K:
        if a[r][0] == T:
            if odd + 1 > K:
                break
            odd += 1
        cnt += 1
        r += 1

    ans = max(ans, n - (m - cnt + 1))
    if r == l:
        r += 1
    else:
        if a[l][0] == T:
            odd -= 1
        cnt -= 1
print(ans)
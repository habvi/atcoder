from collections import defaultdict

n, k = map(int, input().split())
c = list(map(int, input().split()))

d = defaultdict(int)
for i in range(k):
    d[c[i]] += 1
ans = len(d)

for i in range(k, n):
    d[c[i-k]] -= 1
    if d[c[i-k]] == 0:
        d.pop(c[i-k])
    d[c[i]] += 1
    ans = max(ans, len(d))
print(ans)
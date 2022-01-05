n, k = map(int, input().split())
X = list(map(int, input().split()))
l, r = [], []
for x in X:
    if x < 0:
        l.append(-x)
    else:
        r.append(x)

ans = float('inf')
for i in range(n - k + 1):
    j = i + k - 1
    if j < len(l):
        ans = min(ans, l[i])
    elif i >= len(l):
        j -= len(l)
        ans = min(ans, r[j])
    else:
        j -= len(l)
        ans = min(ans, l[i] * 2 + r[j], l[i] + r[j] * 2)
print(ans)
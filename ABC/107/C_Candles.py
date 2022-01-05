n, k = map(int, input().split())
X = list(map(int, input().split()))
l, r = [], [0]
for x in X:
    if x < 0:
        l.append(-x)
    else:
        r.append(x)
l.append(0)
l = l[::-1]

ans = float('inf')
for i in range(len(l)):
    j = k - i
    if 0 <= j < len(r):
        ans = min(ans, l[i]*2 + r[j], l[i] + r[j]*2)
print(ans)
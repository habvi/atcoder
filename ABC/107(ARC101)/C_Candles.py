n, k = map(int, input().split())
x = list(map(int, input().split()))
l, r = [], [0]
for i in range(n):
    if x[i] <= 0:
        l.append(-x[i])
    else:
        r.append(x[i])
l.append(0)
l = l[::-1]

ans = float('inf')
for i in range(len(l)):
    j = k - i
    if j < 0:
        break
    if j < len(r):
        ans = min(ans, l[i]*2 + r[j], l[i] + r[j]*2)
print(ans)
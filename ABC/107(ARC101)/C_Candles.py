from itertools import accumulate
n, k = map(int, input().split())
x = list(map(int, input().split()))
l, r = [], []
for i in range(n):
    if x[i] <= 0:
        l.append(x[i])
    else:
        r.append(x[i])
l.append(0)
r = [0] + r

dl, dr = [], []
for i in range(len(l) - 1):
    dl.append(l[i + 1] - l[i])
for i in range(len(r) - 1):
    dr.append(r[i + 1] - r[i])

dl = dl[::-1]
al = [0] + list(accumulate(dl))
ar = [0] + list(accumulate(dr))

ans = float('inf')
for i in range(len(al)):
    j = k - i
    if j < 0:
        break
    if j < len(ar):
        ans = min(ans, al[i]*2 + ar[j], al[i] + ar[j]*2)
print(ans)
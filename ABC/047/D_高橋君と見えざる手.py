from collections import defaultdict
n, t = map(int, input().split())
A = list(map(int, input().split()))

mnd = defaultdict(int)
mn = float('inf')
for a in A:
    mn = min(mn, a)
    if mn < a:
        mnd[a - mn] += 1

mxd = defaultdict(int)
mx = 0
for a in reversed(A):
    mx = max(mx, a)
    if a < mx:
        mxd[mx - a] += 1

mx = max(mxd)
print(min(mxd[mx], mnd[mx]))
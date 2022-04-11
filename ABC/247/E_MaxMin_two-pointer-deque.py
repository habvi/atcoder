from collections import deque

n, X, Y = map(int, input().split())
A = list(map(int, input().split()))

B = []
new = []
for a in A:
    if Y <= a <= X:
        new.append(a)
    else:
        B.append(new)
        new = []
if new:
    B.append(new)

ans = 0
for C in B:
    m = len(C)
    mn, mx = 0, 0
    total = 0
    q = deque([])
    for ri, c in enumerate(C):
        q.append(c)
        mx += (c == X)
        mn += (c == Y)

        while q and mn and mx:
            ans += (m - ri)
            rm = q.popleft()
            mx -= (rm == X)
            mn -= (rm == Y)

print(ans)
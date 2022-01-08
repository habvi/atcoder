def Sn(n):
    return n*(n + 1) // 2

from collections import deque
n, k = map(int, input().split())
P = list(map(int, input().split()))
q = deque([])
tot = 0
ans = 0
for p in P:
    if len(q) < k:
        q.append(p)
        tot += Sn(p) / p
        ans = max(ans, tot)
        continue
    rm = q.popleft()
    tot -= Sn(rm) / rm
    
    q.append(p)
    tot += Sn(p) / p
    ans = max(ans, tot)
print(ans)
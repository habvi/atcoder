from collections import deque
from itertools import groupby
n, K = map(int, input().split())
s = input()
a = []
for k, v in groupby(s):
    a.append((int(k), len(list(v))))

q = deque([])
cnt = 0
tot = 0
ans = 0
for b, k in a:
    if b:
        q.append((b, k))
        tot += k
        ans = max(ans, tot)
        continue
    
    while q and cnt >= K:
        rb, rk = q.popleft()
        if not rb:
            cnt -= 1
        tot -= rk

    q.append((b, k))
    cnt += 1
    tot += k
    ans = max(ans, tot)
print(ans)
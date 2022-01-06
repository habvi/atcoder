from collections import deque
from itertools import groupby
S = input()
k = int(input())
if k == 0:
    ans = 0
    for k, v in groupby(S):
        if k == "X":
            ans = max(ans, len(list(v)))
    print(ans)
    exit()
    
q = deque([])
ld, lx = 0, 0
ans = 0
for s in S:
    if s == "X":
        lx += 1
        q.append(s)
        ans = max(ans, len(q))
        continue

    while q and ld >= k:
        rm = q.popleft()
        if rm == ".":
            ld -= 1
        else:
            lx -= 1
    
    ld += 1
    q.append(s)
    ans = max(ans, len(q))
print(ans)
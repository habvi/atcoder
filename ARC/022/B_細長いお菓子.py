from collections import deque
n = int(input())
A = list(map(int, input().split()))
q = deque([])
used = [0] * (10**5 + 1)
ans = 0
for a in A:
    if not used[a]:
        q.append(a)
        used[a] = 1
        ans = max(ans, len(q))
        continue
    while q and used[a]:
        rm = q.popleft()
        used[rm] = 0
    q.append(a)
    used[a] = 1
    ans = max(ans, len(q))
print(ans)
from collections import deque

n, k = map(int, input().split())
A = [int(input()) for _ in range(n)]

q = deque([])
ans = 0
for a in A:
    if q and q[-1] >= a:
        q = deque([])

    if (not q) or (q and q[-1] < a):
        q.append(a)

    if len(q) >= k:
        ans += 1

print(ans)
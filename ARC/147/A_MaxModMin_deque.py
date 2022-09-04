from collections import deque

N = int(input())
A = list(map(int, input().split()))

A.sort()
q = deque(A)
ans = 0
while len(q) > 1:
    x = q.pop()
    x %= q[0]
    ans += 1
    if x >= 1:
        q.appendleft(x)
print(ans)

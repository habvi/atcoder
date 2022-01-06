from collections import deque
n, k = map(int, input().split())
A = [int(input()) for _ in range(n)]
if 0 in A:
    print(n)
    exit()
    
q = deque()
tot = 1
ans = 0
for a in A:
    q.append(a)
    tot *= a
    while q and tot > k:
        rm = q.popleft()
        tot //= rm
    ans = max(ans, len(q))
print(ans)
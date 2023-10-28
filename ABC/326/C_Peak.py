from collections import deque, defaultdict

N, M = map(int, input().split())
A = list(map(int, input().split()))

d = defaultdict(int)
for a in A:
    d[a] += 1

q = deque()
total = 0
ans = 0
for k in sorted(d.keys()):
    q.append(k)
    total += d[k]
    while q and k - q[0] >= M:
        rm = q.popleft()
        total -= d[rm]
    ans = max(ans, total)
print(ans)

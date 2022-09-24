from collections import Counter, deque
from itertools import accumulate

N, K = map(int, input().split())
A = list(map(int, input().split()))

c = Counter(A)
if c[0] == 0:
    c[0] = 1
m = len(c)
ks = sorted(c.keys())
ct = [c[k] for k in ks]

ac = list(accumulate(reversed(ct)))[::-1]
d = deque()
for i, k in enumerate(ks):
    if k >= 1:
        d.append((ac[i], ks[i] - ks[i - 1]))

loop = 0
while K > 0 and d:
    num, x = d.popleft()
    mn = min(K // num, x)
    if mn == 0:
        break
    K -= num * mn
    loop += mn

for i in range(N):
    A[i] = max(0, A[i] - loop)
for i in range(N):
    if K == 0:
        break
    if A[i]:
        A[i] -= 1
        K -= 1
print(*A)

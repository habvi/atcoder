from collections import deque
from itertools import groupby

N = int(input())
A = list(map(int, input().split()))

B = []
mx = 3 * 10**5
for k, v in groupby(sorted(A)):
    v = len(list(v))
    B.append(k)
    for _ in range(v - 1):
        B.append(mx)
B.sort()

d = deque(B)
ans = 0
while d:
    if ans + 1 == d[0]:
        d.popleft()
        ans += 1
    else:
        if len(d) < 2:
            break
        d.pop()
        d.pop()
        ans += 1
print(ans)

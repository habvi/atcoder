from collections import defaultdict
from bisect import bisect

W, H = map(int, input().split())
N = int(input())
pq = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(N)]
a_n = int(input())
A = list(map(int, input().split()))
b_n = int(input())
B = list(map(int, input().split()))

straw = defaultdict(int)
for p, q in pq:
    ai = bisect(A, p)
    bi = bisect(B, q)
    straw[(bi, ai)] += 1

total = (a_n + 1) * (b_n + 1)
val = straw.values()
ans = []
if len(straw) < total:
    ans.append(0)
else:
    ans.append(min(val))
ans.append(max(val))
print(*ans)
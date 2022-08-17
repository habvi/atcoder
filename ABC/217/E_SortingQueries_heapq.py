from heapq import heappop, heappush
from collections import deque

hq = []
d = deque([])

Q = int(input())
for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        x = q[1]
        d.append(q[1])
    elif q[0] == 2:
        if hq:
            print(heappop(hq))
        else:
            print(d.popleft())
    else:
        while d:
            heappush(hq, d.pop())
from heapq import heapify, heappop, heappush
from collections import deque

hq = []
d = deque([])

Q = int(input())
for _ in range(Q):
    *q, = map(int, input().split())

    if q[0] == 1:
        x = q[1]
        d.append(x)
    elif q[0] == 2:
        if hq:
            print(heappop(hq))
        else:
            print(d.popleft())
    else:
        while d:
            heappush(hq, d.popleft())
from heapq import heappop, heappush

hq = []
base = 0

Q = int(input())
for _ in range(Q):
    q, *x = map(int, input().split())
    x = (x[0] if x else None)

    if q == 1:
        heappush(hq, x - base)
    elif q == 2:
        base += x
    else:
        print(heappop(hq) + base)
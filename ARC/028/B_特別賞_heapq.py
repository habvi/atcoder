from heapq import heappop, heappush

n, k = map(int, input().split())
X = list(map(int, input().split()))

hq = []
for i, x in enumerate(X, 1):
    heappush(hq, (-x, i))

    if len(hq) > k:
        heappop(hq)

    if i >= k:
        print(hq[0][1])
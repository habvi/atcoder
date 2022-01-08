from heapq import heapify, heappop, heappush
n, k = map(int, input().split())
P = list(map(int, input().split()))
hq = P[:k]
heapify(hq)

print(hq[0])
for p in P[k:]:
    heappush(hq, p)
    heappop(hq)
    print(hq[0])
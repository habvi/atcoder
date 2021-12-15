from heapq import heapify, heappop, heappush
n, m = map(int, input().split())
a = list(map(lambda x: -int(x), input().split()))
heapify(a)

for _ in range(m):
    b = -heappop(a)
    heappush(a, -(b // 2))
print(-sum(a))
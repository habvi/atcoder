from heapq import heapify, heappop, heappush
x, y, z, K = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
a.sort(reverse=True)
b.sort(reverse=True)
c.sort(reverse=True)

hq = []
heapify(hq)
heappush(hq, (-(a[0] + b[0] + c[0]), 0, 0, 0))
seen = set()
seen.add((0, 0, 0))
for _ in range(K):
    tot, i, j, k = heappop(hq)
    print(-tot)
    if i + 1 < x and (i + 1, j, k) not in seen:
        heappush(hq, (-(a[i + 1] + b[j] + c[k]), i + 1, j, k))
        seen.add((i + 1, j, k))
    if j + 1 < y and (i, j + 1, k) not in seen:
        heappush(hq, (-(a[i] + b[j + 1] + c[k]), i, j + 1, k))
        seen.add((i, j + 1, k))
    if k + 1 < z and (i, j, k + 1) not in seen:
        heappush(hq, (-(a[i] + b[j] + c[k + 1]), i, j, k + 1))
        seen.add((i, j, k + 1))
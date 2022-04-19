from heapq import heappop, heappush

n, K = map(int, input().split())
td = [tuple(map(int, input().split())) for _ in range(n)]

td.sort(key=lambda x: -x[1])

hq = []
kind = set()
total = 0
for i in range(K):
    t, d = td[i]
    total += d
    if t not in kind:
        kind.add(t)
    else:
        heappush(hq, d)

total += len(kind) ** 2

ans = total
for t, d in td[K:]:
    if t in kind:
        continue
    kind.add(t)

    if not hq:
        break
    total -= heappop(hq)
    total += d - (len(kind) - 1) ** 2 + len(kind) ** 2
    ans = max(ans, total)
print(ans)
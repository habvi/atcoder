n, K = map(int, input().split())
td = [tuple(map(int, input().split())) for _ in range(n)]

td.sort(key=lambda x: x[1])

kind = set()
total = 0
ds = []
for i in range(K):
    t, d = td.pop()
    total += d
    if t not in kind:
        kind.add(t)
    else:
        ds.append(d)

total += len(kind) ** 2
ds.sort(reverse=True)

ans = total
while ds and td:
    t, d = td.pop()
    if t in kind:
        continue
    kind.add(t)

    if ds:
        total -= ds.pop()
        total += d - (len(kind) - 1) ** 2 + len(kind) ** 2
        ans = max(ans, total)
print(ans)
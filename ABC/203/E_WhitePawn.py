from collections import defaultdict

n, m = map(int, input().split())
xy = defaultdict(list)
for _ in range(m):
    x, y = map(int, input().split())
    xy[x].append(y)

ys = {n}
for x in sorted(xy.keys()):
    erace = []
    add_ = []
    for y in xy[x]:
        if y in ys and y - 1 not in ys and y + 1 not in ys:
            erace.append(y)
        if y - 1 in ys or y + 1 in ys:
            add_.append(y)

    for y in erace:
        ys.remove(y)

    for y in add_:
        ys.add(y)

print(len(ys))
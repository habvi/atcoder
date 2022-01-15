from collections import defaultdict
n, q = map(int, input().split())
A = list(map(int, input().split()))
d = defaultdict(list)
for i, a in enumerate(A, 1):
    d[a].append(i)

for _ in range(q):
    x, k = map(int, input().split())
    k -= 1
    if len(d[x]) <= k:
        print(-1)
    else:
        print(d[x][k])
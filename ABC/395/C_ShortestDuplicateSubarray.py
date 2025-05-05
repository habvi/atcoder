from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

idx = defaultdict(list)
for i, a in enumerate(A):
    idx[a].append(i)

INF = float('inf')
ans = INF
for k, v in idx.items():
    if len(v) == 1:
        continue
    for i in range(len(v) - 1):
        ans = min(ans, v[i + 1] - v[i] + 1)
print(ans if ans != INF else -1)

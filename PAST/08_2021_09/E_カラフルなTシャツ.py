from collections import defaultdict

n, K = map(int, input().split())
C = list(map(int, input().split()))
P = list(map(int, input().split()))

INF = float('inf')
mn = defaultdict(lambda : INF)
for c, p in zip(C, P):
    mn[c] = min(mn[c], p)

vs = list(mn.values())
vs.sort()
if len(vs) < K:
    print(-1)
else:
    print(sum(vs[:K]))
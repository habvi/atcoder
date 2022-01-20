from collections import defaultdict
n, k = map(int, input().split())
A = list(map(lambda x: int(x) - 1, input().split()))

idx = defaultdict(lambda : -1)
route = []
now = 0
for i in range(n):
    idx[now] = i
    route.append(now)
    now = A[now]
    if now in idx:
        break

loop = idx[now]
if k < loop:
    print(route[k] + 1)
    exit()

route = route[loop:]
k -= loop
print(route[k % len(route)] + 1)
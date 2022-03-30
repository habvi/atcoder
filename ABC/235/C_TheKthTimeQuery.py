from collections import defaultdict

n, Q = map(int, input().split())
A = list(map(int, input().split()))

times = defaultdict(list)
for i, a in enumerate(A):
    times[a].append(i + 1)

for _ in range(Q):
    x, k = map(int, input().split())
    k -= 1
    print(times[x][k] if len(times[x]) > k else -1) 
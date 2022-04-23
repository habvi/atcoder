from collections import defaultdict

n = int(input())
A = list(map(int, input().split()))

g = defaultdict(list)
for i, a in enumerate(A, 2):
    g[a].append(i)

for i in range(1, n + 1):
    print(len(g[i]))
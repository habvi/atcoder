from collections import defaultdict
n = int(input())
A = list(map(int, input().split()))
d = defaultdict(int)
for i, a in enumerate(A):
    d[i - a] += 1

ans = 0
for i, a in enumerate(A):
    ans += d[i + a]
print(ans)
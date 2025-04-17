from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

d = defaultdict(list)
for i, a in enumerate(A):
    d[a].append(i)

mx = 0
ans = -1
for k, v in d.items():
    if len(v) == 1 and k > mx:
        mx = k
        ans = v[0] + 1
print(ans)

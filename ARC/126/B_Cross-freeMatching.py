from bisect import bisect_left

n, m = map(int, input().split())
A = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    A[x].append(y)

for vs in A:
    vs.sort(reverse=True)

lis = [0]
ans = 0
for vs in A:
    for v in vs:
        if lis[-1] < v:
            lis.append(v)
            ans += 1
        else:
            lis[bisect_left(lis, v)] = v

print(ans)
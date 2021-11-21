from bisect import bisect
n, k = map(int, input().split())
a = []
for i in range(n):
    b = tuple(map(int, input().split()))
    a.append(sum(b))

t = sorted(a)
for i in range(n):
    bi = bisect(t, a[i] + 300)
    if n - bi + 1 <= k:
        print('Yes')
    else:
        print('No')
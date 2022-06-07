import bisect
n, m = map(int, input().split())
A = list(map(int, input().split()))

s = [float('inf') for _ in range(n)]
for i, a in enumerate(A):
    if i == 0:
        print(1)
        s[i] = - a
        continue

    bi = bisect.bisect(s, -a)
    if bi >= n:
        print(-1)
        continue
    if bi == 0:
        print(bi+1)
        s[bi] = -a
        continue
    s[bi] = - a
    print(bi+1)

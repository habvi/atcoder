from bisect import bisect

n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

INF = float('inf')
B.extend([-INF, INF])
B.sort()
ans = INF
for a in A:
    bi = bisect(B, a)
    ans = min(ans, B[bi] - a, a - B[bi - 1])
print(ans)
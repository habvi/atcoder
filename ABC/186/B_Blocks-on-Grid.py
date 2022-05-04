h, w = map(int, input().split())
A = []
mn = float('inf')
for _ in range(h):
    a = tuple(map(int, input().split()))
    mn = min(mn, min(a))
    A.append(a)

ans = 0
for i in range(h):
    for j in range(w):
        ans += A[i][j] - mn
print(ans)
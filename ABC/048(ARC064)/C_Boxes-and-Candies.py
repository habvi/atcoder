n, x = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
if A[0] > x:
    ans += A[0] - x
    A[0] = x

for i in range(n - 1):
    if A[i + 1] + A[i] <= x:
        continue

    ans += A[i + 1] - (x - A[i])
    A[i + 1] = x - A[i]
print(ans)
N, M = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
diff = 0
for i in range(M):
    ans += A[i] * (i + 1)
    diff += A[i]

total = ans
for i, a in enumerate(A[M:], M):
    total += M * a
    total -= diff
    ans = max(ans, total)
    diff += a - A[i - M]
print(ans)

n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = 0
for i, b in enumerate(B):
    for j in (i, i + 1):
        minus = min(A[j], b)
        A[j] -= minus
        b -= minus
        ans += minus
print(ans)
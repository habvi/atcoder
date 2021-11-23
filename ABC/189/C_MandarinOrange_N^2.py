# N**2//2 = O(N**7) PyPy3

n = int(input())
A = list(map(int, input().split()))

ans = 0
for i in range(n):
    mn = float('inf')
    for j in range(i, n):
        mn = min(mn, A[j])
        ans = max(ans, mn * (j - i + 1))
print(ans)
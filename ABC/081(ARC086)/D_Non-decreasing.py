N = int(input())
A = list(map(int, input().split()))

mx_i, mx = None, 0
for i, a in enumerate(A):
    if abs(mx) <= abs(a):
        mx_i, mx = i, a

ans = []
for i in range(N):
    A[i] += mx
    ans.append((mx_i + 1, i + 1))

if A[i] >= 0:
    for i in range(N - 1):
        A[i + 1] += A[i]
        ans.append((i + 1, i + 2))
else:
    for i in reversed(range(1, N)):
        A[i - 1] += A[i]
        ans.append((i + 1, i))

print(len(ans))
for a in ans:
    print(*a)

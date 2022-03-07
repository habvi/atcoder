n = int(input())
B = list(map(int, input().split()))

A = [None] * n
A[0] = B[0]
A[-1] = B[-1]

for i in range(n - 2):
    A[i + 1] = min(B[i], B[i + 1])

print(sum(A))
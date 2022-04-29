n = int(input())
A = list(map(lambda x: int(x) - 1, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A.append(-1)
total = 0
for i in range(n):
    total += B[A[i]]
    if A[i] + 1 == A[i + 1]:
        total += C[A[i]]
print(total)
n = int(input())
S = list(map(int, input().split()))

if n == 1:
    print('Yes')
    print(0, 0, S[0])
    exit()

A = [0, 0, 0]
for i in range(n - 1):
    A.append((A[i] + S[i + 1] - S[i]))

m1 = min(A[i] for i in range(0, n + 2, 3))
m2 = min(A[i] for i in range(1, n + 2, 3))
m3 = min(A[i] for i in range(2, n + 2, 3))

if m1 < 0:
    for i in range(0, n + 2, 3):
        A[i] -= m1
if m2 < 0:
    for i in range(1, n + 2, 3):
        A[i] -= m2
if m3 < 0:
    for i in range(2, n + 2, 3):
        A[i] -= m3

s3 = sum(A[:3])
if s3 > S[0]:
    print('No')
    exit()

plus = S[0] - s3
for i in range(0, n + 2, 3):
    A[i] += plus

for i in range(n):
    if sum(A[i : i + 3]) != S[i]:
        print('No')
        exit()

print('Yes')
print(*A)
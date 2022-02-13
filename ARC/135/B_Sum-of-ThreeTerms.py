n = int(input())
S = list(map(int, input().split()))

if n == 1:
    print('Yes')
    print(0, 0, S[0])
    exit()

A = [0, 0, 0]
for i in range(n - 1):
    A.append((A[i] + S[i + 1] - S[i]))


def raise_bottom(start):
    mn = min(A[i] for i in range(start, n + 2, 3))
    if mn < 0:
        for i in range(start, n + 2, 3):
            A[i] -= mn


for i in range(3):
    raise_bottom(i)

s3 = sum(A[:3])
plus = S[0] - s3
if plus < 0:
    print('No')
    exit()

for i in range(0, n + 2, 3):
    A[i] += plus

for i in range(n):
    if sum(A[i : i+3]) != S[i]:
        print('No')
        exit()

print('Yes')
print(*A)
n = int(input())
A = list(map(int, input().split()))

B = [0] * n
for i in reversed(range(1, n + 1)):
    total = 0
    for j in range(i, n + 1, i):
        total += B[j - 1]

    B[i - 1] = (total % 2 != A[i - 1]) * 1

print(sum(B))
for i in range(n):
    if B[i]:
        print(i + 1)
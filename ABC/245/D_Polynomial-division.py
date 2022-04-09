n, m  = map(int, input().split())
A = list(map(int, input().split()))[::-1]
C = list(map(int, input().split()))[::-1]

B = []
for i in range(m + 1):
    div = C[i] // A[0]
    B.append(div)

    for j in range(n + 1):
        C[i + j] -= A[j] * div

print(*B[::-1])
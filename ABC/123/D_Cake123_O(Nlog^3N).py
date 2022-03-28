X, Y, Z, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A.sort(reverse=True)
B.sort(reverse=True)
C.sort(reverse=True)

deli = []
for i in range(X):
    for j in range(min(Y, K // (i + 1) + 1)):
        for k in range(min(Z, K // (i + 1) * (j + 1) + 1)):
            if (i + 1) * (j + 1) * (k + 1) <= K:
                deli.append(A[i] + B[j] + C[k])

for ans in sorted(deli, reverse=True)[:K]:
    print(ans)
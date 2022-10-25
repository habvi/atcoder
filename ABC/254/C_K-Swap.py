N, K = map(int, input().split())
A = list(map(int, input().split()))
B = A[:]

for i in range(K):
    C = []
    for j in range(i, N, K):
        C.append(B[j])
    C.sort()
    for k, j in enumerate(range(i, N, K)):
        A[j] = C[k]
print("Yes" if A == sorted(B) else "No")
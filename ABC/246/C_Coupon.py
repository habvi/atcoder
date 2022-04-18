n, K, X = map(int, input().split())
A = list(map(int, input().split()))

for i in range(n):
    num = min(K, A[i] // X)
    A[i] -= X * num
    K -= num
    if not K:
        break

A.sort(reverse=True)

for i in range(min(K, n)):
    A[i] = 0
print(sum(A))
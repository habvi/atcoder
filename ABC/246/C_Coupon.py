n, K, X = map(int, input().split())
A = list(map(int, input().split()))

A.sort(reverse=True)

for i in range(n):
    if not K or A[i] < X:
        break
    num = min(K, A[i] // X)
    A[i] -= X * num
    K -= num

A.sort(reverse=True)

for i in range(min(n, K)):
    A[i] = 0
print(sum(A))